#!/usr/bin/env python3
import os
import sys
import glob
import importlib.util
import numpy as np
import pandas as pd
import pylhe
import concurrent.futures
import multiprocessing as mp
import contextlib
import time
import math
import itertools

# --- LHAPDF Path Setup ---
sys.path.append("/home/vinicius/MG5/HEPTools/lhapdf6_py3/lib/python3.14/dist-packages")
import lhapdf

# ==========================================
# 1. CONFIGURATION & SETUP
# ==========================================
E_BEAM = 6500.0    
PDF_NAME = 244800#244600  
MU_F  = 91.188     
MU_R  = 91.188    
MU_R2 = MU_R**2    

# CHUNK SIZE: How many events to process in RAM at a time before saving and clearing memory.
CHUNK_SIZE = 50000 

MODEL_ROOTS = {
    "VLF":    os.path.abspath("/home/vinicius/EFT_ToyModel/processFolders/UV_BSM/MatrixElements/SubProcesses"),
    "Scalar": os.path.abspath("/home/vinicius/EFT_ToyModel/processFolders/SMS_1_loop/MatrixElements/SubProcesses"),
    "Zprime": os.path.abspath("/home/vinicius/EFT_ToyModel/processFolders/z_prime/nlo_MatrixElements/SubProcesses")
}

MODEL_CHANNELS = {
    "VLF":    ["P0_uux_ttx", "P2_gg_ttx"],
    "Scalar": ["P0_uux_ttx", "P2_gg_ttx"],
    "Zprime": ["P2_uux_ttx", "P3_ddx_ttx", "P0_gg_ttx"]
}

PDG_MAP = {"uux": 2, "ddx": 1, "ssx": 3, "ccx": 4, "bbx": 5}

# ==========================================
# 2. HELPER FUNCTIONS & SILENCER
# ==========================================
@contextlib.contextmanager
def suppress_fortran_output():
    devnull = os.open(os.devnull, os.O_WRONLY)
    old_stdout = os.dup(1)
    old_stderr = os.dup(2)
    try:
        os.dup2(devnull, 1)
        os.dup2(devnull, 2)
        yield
    finally:
        os.dup2(old_stdout, 1)
        os.dup2(old_stderr, 2)
        os.close(devnull)
        os.close(old_stdout)
        os.close(old_stderr)

def invert_momenta(p):
    new_p = [[0] * len(p) for _ in range(len(p[0]))]
    for i, onep in enumerate(p):
        for j, x in enumerate(onep):
            new_p[j][i] = x
    return new_p

def init_model_card(module, subproc_path, module_label):
    card_path = os.path.abspath(os.path.join(subproc_path, "..", "..", "Cards", "param_card.dat"))
    if not os.path.exists(card_path):
        raise FileNotFoundError(f"[{module_label}] Could not find parameter card at: {card_path}")
    
    original_cwd = os.getcwd()
    try:
        os.chdir(subproc_path)
        mod_attrs = dir(module)
        lo_init = [a for a in mod_attrs if a.endswith('initialisemodel')]
        nlo_init = [a for a in mod_attrs if 'initialise' in a and not a.endswith('initialisemodel')]
        
        if lo_init:
            getattr(module, lo_init[0])(card_path)
        elif nlo_init:
            getattr(module, nlo_init[0])(card_path)
        else:
            raise AttributeError(f"[{module_label}] No valid initialization subroutine found!")
    finally:
        os.chdir(original_cwd)

def eval_full_me(mod, subproc_path, p_fortran, alphas, scale2, model_name, nhel=-1):
    """
    Evaluates the Matrix Element and unpacks the Fortran array based on the model type.
    """
    mod_attrs = dir(mod)
    nlo_eval = [a for a in mod_attrs if a.endswith('get_me')]
    
    original_cwd = os.getcwd()
    try:
        os.chdir(subproc_path)
        res, ret_code = getattr(mod, nlo_eval[0])(p_fortran, alphas, scale2, nhel)
        res_arr = np.array(res)
        
        # -------------------------------------------------------------
        # Z PRIME UNPACKING LOGIC
        # -------------------------------------------------------------
        if model_name == "Zprime":
            if res_arr.ndim == 1 and res_arr.size == 3:
                # Patched 1D Wrapper (Size 7)
                # Index 0: Total Sum
                # Index 1: NP=4, QCD=0 (Pure Z' Breit-Wigner)
                # Index 2: NP=2, QCD=2 (Interference)
                # Index 3: NP=0, QCD=4 (Pure SM QCD)
                born_sm = float(res_arr[3])
                bsm_leading = float(res_arr[1])
            elif res_arr.ndim == 1 and res_arr.size == 2:
                # Legacy 2D Wrapper fallback
                born_sm = float(res_arr[0])
                bsm_leading = 0.0
            elif res_arr.ndim == 1 and res_arr.size == 4:
                # Unpatched Original 1D Wrapper
                born_sm = float(res_arr[0])
                bsm_leading = float(res_arr[1])
            else:
                # Fallback for unexpected sizes
                res_list = np.ravel(res_arr)
                born_sm = 0.0
                bsm_leading = float(res_list[0]) if len(res_list) > 0 else 0.0
                
            return {"born_sm": born_sm, "bsm_leading": bsm_leading}

        # -------------------------------------------------------------
        # VLF & SCALAR (LOOP) UNPACKING LOGIC
        # -------------------------------------------------------------
        else:
            if res_arr.ndim == 2:
                if res_arr.shape[1] > 3:
                    born_sm, bsm_leading = float(res_arr[0, 3]), float(res_arr[0, 1])
                else:
                    born_sm, bsm_leading = float(res_arr[0, 0]), 0.0
                return {"born_sm": born_sm, "bsm_leading": bsm_leading}
            elif res_arr.ndim == 1 and res_arr.size == 4:
                return {"born_sm": float(res_arr[0]), "bsm_leading": float(res_arr[1])}
            else:
                res_list = np.ravel(res_arr)
                finite_val = float(res_list[0]) if len(res_list) > 0 else 0.0
                return {"born_sm": 0.0, "bsm_leading": finite_val}
                
    finally:
        os.chdir(original_cwd)

# ==========================================
# 3. ISOLATED WORKER PROCESS
# ==========================================
def worker_evaluate_model(model_name, ch_name, subproc_path, kinematics_list):
    """Processes a chunk of events safely."""
    results = []
    
    with suppress_fortran_output():
        if subproc_path not in sys.path:
            sys.path.append(subproc_path)
            
        so_files = glob.glob(os.path.join(subproc_path, f"*matrix_{model_name}*.so")) or \
                   glob.glob(os.path.join(subproc_path, "*matrix*.so"))
        if not so_files:
            return pd.DataFrame()
            
        so_path = so_files[0]
        # Force a strictly unique module name in Python's sys.modules to prevent cross-talk
        lib_name = f"matrix_{model_name}_{ch_name}"
        
        spec = importlib.util.spec_from_file_location(lib_name, so_path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[lib_name] = mod
        spec.loader.exec_module(mod)
        init_model_card(mod, subproc_path, f"{model_name} | {ch_name}")

        for global_idx, P_fortran, alphas, scale_sq in kinematics_list:
            event_record = {"Event": global_idx}
            try:
                # Initial Evaluation
                me_dict = eval_full_me(mod, subproc_path, P_fortran, alphas, scale_sq, model_name, -1)
                
                # ============================================================
                # SAFETY MECHANISM for Zprime (uux & ddx)
                # ============================================================
                if model_name == "Zprime" and ch_name in ["P2_uux_ttx", "P3_ddx_ttx"]:
                    attempts = 0
                    max_retries = 7
                    
                    # Loop if the value explodes or returns NaN
                    while (me_dict["bsm_leading"] > 2.0 or math.isnan(me_dict["bsm_leading"])) and attempts < max_retries:
                        me_dict = eval_full_me(mod, subproc_path, P_fortran, alphas, scale_sq, model_name, -1)
                        attempts += 1
                    
                    # If it still fails after max_retries, nullify to protect the dataset
                    if me_dict["bsm_leading"] > 2.0 or math.isnan(me_dict["bsm_leading"]):
                        me_dict["born_sm"] = np.nan
                        me_dict["bsm_leading"] = np.nan
                # ============================================================
                
                #  Assign Results to Record
                if model_name == "Zprime":
                    event_record[f"ME_Born_SM_{model_name}_{ch_name}"] = me_dict["born_sm"]
                    event_record[f"ME_Born_NP_{model_name}_{ch_name}"] = me_dict["bsm_leading"]
                else:
                    event_record[f"ME_Born_{model_name}_{ch_name}"] = me_dict["born_sm"]
                    event_record[f"ME_Finite_{model_name}_{ch_name}"] = me_dict["bsm_leading"]
                    
            except Exception:
                if model_name == "Zprime":
                    event_record[f"ME_Born_SM_{model_name}_{ch_name}"] = np.nan
                    event_record[f"ME_Born_NP_{model_name}_{ch_name}"] = np.nan
                else:
                    event_record[f"ME_Born_{model_name}_{ch_name}"] = np.nan
                    event_record[f"ME_Finite_{model_name}_{ch_name}"] = np.nan
                    
            results.append(event_record)
            
    df = pd.DataFrame(results)
    temp_file = f"temp_ME_{model_name}_{ch_name}.pkl"
    df.to_pickle(temp_file)
    return temp_file

# ==========================================
# 4. MASTER PIPELINE ORCHESTRATOR
# ==========================================
def compute_matrix_elements_in_chunks(lhe_path, output_csv_path, model_path_dict):
    print(f"\n[{time.strftime('%H:%M:%S')}] Processing LHE file: {lhe_path}", flush=True)
    pdf = lhapdf.mkPDF(PDF_NAME) if isinstance(PDF_NAME, int) else lhapdf.mkPDF(str(PDF_NAME), 0)
    
    try:
        total_events = pylhe.read_num_events(lhe_path)
    except:
        total_events = None

    events_generator = pylhe.read_lhe_with_attributes(lhe_path)
    total_chunks = math.ceil(total_events / CHUNK_SIZE) if total_events else "Unknown"
    
    first_chunk = True
    ctx = mp.get_context('fork')
    
    for chunk_idx in itertools.count():
        chunk_events = list(itertools.islice(events_generator, CHUNK_SIZE))
        if not chunk_events:
            break 
            
        print(f"\n[{time.strftime('%H:%M:%S')}] ==============================================", flush=True)
        print(f"[{time.strftime('%H:%M:%S')}] STARTING CHUNK {chunk_idx + 1} / {total_chunks}", flush=True)
        print(f"[{time.strftime('%H:%M:%S')}] Events: {chunk_idx * CHUNK_SIZE} to {(chunk_idx * CHUNK_SIZE) + len(chunk_events) - 1}", flush=True)
        print(f"[{time.strftime('%H:%M:%S')}] ==============================================", flush=True)

        base_results, kinematics_list = [], []
        
        for idx, event in enumerate(chunk_events):
            global_idx = (chunk_idx * CHUNK_SIZE) + idx
            
            outgoing = [p for p in event.particles if p.status == 1]
            if len(outgoing) != 2: continue
                
            tops = sorted(outgoing, key=lambda x: x.id, reverse=True)
            t, tbar = tops[0], tops[1]
            
            E_tt, pz_tt = t.e + tbar.e, t.pz + tbar.pz
            x1, x2 = (E_tt + pz_tt) / (2.0 * E_BEAM), (E_tt - pz_tt) / (2.0 * E_BEAM)
            if not (0 < x1 < 1.0 and 0 < x2 < 1.0): continue
                
            s_hat = E_tt**2 - (t.px + tbar.px)**2 - (t.py + tbar.py)**2 - pz_tt**2
            HT = sum(np.sqrt(p.m**2 + p.px**2 + p.py**2) for p in outgoing)
            dynamic_scale = HT / 2.0
            alphas = pdf.alphasQ(dynamic_scale)
            
            w_gg = (pdf.xfxQ(21, x1, dynamic_scale) / x1) * (pdf.xfxQ(21, x2, dynamic_scale) / x2)
            pdf_fluxes = {"w_gg": w_gg}
            for q_name, q_id in PDG_MAP.items():
                fq_1, fqbar_2 = pdf.xfxQ(q_id, x1, dynamic_scale) / x1, pdf.xfxQ(-q_id, x2, dynamic_scale) / x2
                fqbar_1, fq_2 = pdf.xfxQ(-q_id, x1, dynamic_scale) / x1, pdf.xfxQ(q_id, x2, dynamic_scale) / x2
                pdf_fluxes[f"w_{q_name}"] = (fq_1 * fqbar_2) + (fqbar_1 * fq_2)
            
            P_fortran = np.asfortranarray(invert_momenta([
                [x1 * E_BEAM, 0.0, 0.0,  x1 * E_BEAM],
                [x2 * E_BEAM, 0.0, 0.0, -x2 * E_BEAM],
                [t.e, t.px, t.py, t.pz], [tbar.e, tbar.px, tbar.py, tbar.pz]
            ]), dtype=np.float64)
            
            base_results.append({"Event": global_idx, "x1": x1, "x2": x2, "s_hat": s_hat, 
                                 "dynamic_scale": dynamic_scale, "alphas": alphas, 
                                 "mg_weight": event.eventinfo.weight, **pdf_fluxes})
            
            kinematics_list.append((global_idx, P_fortran, alphas, dynamic_scale**2))

        df_master = pd.DataFrame(base_results)
        temp_files_created = []
        
        # Force fresh memory for every single channel using maxtasksperchild=1
        with ctx.Pool(processes=7, maxtasksperchild=1) as pool:
            futures = []
            for m_name, ch_paths in model_path_dict.items():
                for ch_name, subproc_path in ch_paths.items():
                    # pool.apply_async executes the task in a dedicated, isolated process
                    result = pool.apply_async(worker_evaluate_model, (m_name, ch_name, subproc_path, kinematics_list))
                    futures.append(result)
            
            for future in futures:
                try:
                    # .get() will raise the exception if the process crashed
                    temp_files_created.append(future.get())
                except Exception as exc:
                    print(f"  [{time.strftime('%H:%M:%S')}] -> Channel failed: {exc}", flush=True)

        for temp_file in temp_files_created:
            df_model = pd.read_pickle(temp_file)
            df_master = pd.merge(df_master, df_model, on="Event")
            os.remove(temp_file) 
        
        df_master = df_master.dropna().reset_index(drop=True)
        
        if first_chunk:
            df_master.to_csv(output_csv_path, index=False)
            first_chunk = False
        else:
            df_master.to_csv(output_csv_path, mode='a', header=False, index=False)
            
        print(f"[{time.strftime('%H:%M:%S')}] Chunk saved to disk successfully.", flush=True)
        
        del chunk_events
        del kinematics_list
        del base_results
        del df_master
        
# ==========================================
# 5. EXECUTION BLOCK
# ==========================================
if __name__ == '__main__':
    print("==========================================================")
    print(" BSM ttbar Matrix Element Evaluator (Low-Memory Chunked) ")
    print("==========================================================")
    
    model_path_dict = {}
    for m_name, root_dir in MODEL_ROOTS.items():
        model_path_dict[m_name] = {ch: os.path.join(root_dir, ch) for ch in MODEL_CHANNELS[m_name]}
    
    lhe_file_path = "/home/vinicius/EFT_ToyModel/processFolders/FF_Scalar/pp2ttbar_gs4_ydm2/Events/mtt_cut_1000_900/unweighted_events.lhe.gz"
    #"/home/vinicius/UnfoldingBSMttbar/processFolders/Scalar/pp2ttbar_gs4_ydm2/Events/mtt_cut4_1000_900/events.lhe.gz"
    output_file   = "/home/vinicius/UnfoldingBSMttbar/Matrix_AllModels_FF_swapFix.csv"

    compute_matrix_elements_in_chunks(lhe_file_path, output_file, model_path_dict)
    
    print("\n" + "="*58)
    print(" RUN COMPLETE ")
    print("="*58)