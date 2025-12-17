import glob
import os
import pyslha
import numpy as np
import itertools
from scipy.interpolate import griddata
from matplotlib import pyplot as plt
import tempfile
import pylhe
import gzip
import sys
import argparse
from pathlib import Path
import time
import progressbar as P

def getLHEevents(fpath):
    """
    Reads a set of LHE files and returns a dictionary with the file labels as keys
    and the PyLHE Events object as values.
    """
    # Create temp file to handle syntax errors in LHE
    fd, fixedFile = tempfile.mkstemp(suffix='.lhe')
    os.close(fd)
    
    try:
        with gzip.open(fpath, 'rt') as f:
            # Optimize: Read and filter lines efficiently
            # Using list comprehension is slightly faster than appending in loop
            lines = [l for l in f if 'generate' not in l]
            
        with open(fixedFile, 'w') as newF:
            newF.writelines(lines)
            
        # Pylhe reads the file
        events = list(pylhe.read_lhe_with_attributes(fixedFile))
        nevents = pylhe.read_num_events(fixedFile)
        initBlock = pylhe.read_lhe_init(fixedFile)
        initBlock = initBlock['procInfo'][0]
    finally:
        if os.path.exists(fixedFile):
            os.remove(fixedFile)
            
    return nevents, events, initBlock

def getDistributions(filename):
    """
    OPTIMIZED: Uses NumPy vectorization for calculations.
    """
    nevents, events, initBlock = getLHEevents(filename)
    xSec = initBlock['xSection']
    xSecErr = initBlock['error']
    
    # 1. Extract Raw Data into Arrays
    # We iterate once to grab raw numbers. This is unavoidable with pylhe.
    top_list = []
    atop_list = []
    w_list = []
    
    for ev in events:
        w = ev.eventinfo.weight
        w_list.append(w)
        
        p_t = None
        p_at = None
        
        for ptc in ev.particles:
            if ptc.id == 6:
                p_t = [ptc.px, ptc.py, ptc.pz, ptc.e]
            elif ptc.id == -6:
                p_at = [ptc.px, ptc.py, ptc.pz, ptc.e]
            # Handle case where user logic assumed only 2 particles of interest
            elif abs(ptc.id) == 6: 
                # Fallback if id is not exactly 6/-6 but logic implied it
                if p_t is None: p_t = [ptc.px, ptc.py, ptc.pz, ptc.e]
                else: p_at = [ptc.px, ptc.py, ptc.pz, ptc.e]

        # Ensure we found both
        if p_t and p_at:
            top_list.append(p_t)
            atop_list.append(p_at)
        else:
            # Handle edge cases / missing particles
            # Append dummies or skip? Skipping keeps arrays aligned.
            # For safety, we skip this event's weight too if we skip the event
            w_list.pop() 

    # Convert to NumPy Arrays (Shape: N x 4)
    # P[:, 0]=px, P[:, 1]=py, P[:, 2]=pz, P[:, 3]=E
    P_t = np.array(top_list)
    P_at = np.array(atop_list)
    weights = np.array(w_list) / nevents

    if len(P_t) == 0:
        return {}

    # 2. Vectorized Calculations
    
    # Transverse Momentum (pT)
    # pT = sqrt(px^2 + py^2)
    pT_t = np.hypot(P_t[:, 0], P_t[:, 1])
    pT_at = np.hypot(P_at[:, 0], P_at[:, 1])
    
    # Total System (ttbar)
    P_tot = P_t + P_at
    
    # Invariant Mass (mTT)
    # m = sqrt(E^2 - p^2)
    p_tot_sq = np.sum(P_tot[:, 0:3]**2, axis=1)
    mTT = np.sqrt(P_tot[:, 3]**2 - p_tot_sq)
    
    # Rapidity
    rap_t = vectorized_rapidity(P_t)
    rap_tbar = vectorized_rapidity(P_at)
    rap_ttbar = vectorized_rapidity(P_tot)
    
    # Delta Phi
    deltaPhi = vectorized_delta_phi(P_t, P_at)
    
    # Center of Mass Velocity (Vectorized)
    # v_cm = p_tot_vec / E_tot
    # Shape (N, 3)
    # Use explicit newaxis for broadcasting division
    v_cm = P_tot[:, 0:3] / P_tot[:, 3][:, np.newaxis]
    
    # Cost (Cosine Theta in CM frame)
    # Boost tops to CM frame
    P_t_cm = vectorized_boost(P_t, v_cm)
    P_at_cm = vectorized_boost(P_at, v_cm)
    
    # Cos theta = pz / |p|
    p_t_cm_norm = np.linalg.norm(P_t_cm[:, 0:3], axis=1)
    cos_t = np.zeros_like(p_t_cm_norm)
    mask_nz = p_t_cm_norm > 0
    cos_t[mask_nz] = P_t_cm[mask_nz, 2] / p_t_cm_norm[mask_nz]
    
    p_at_cm_norm = np.linalg.norm(P_at_cm[:, 0:3], axis=1)
    cos_tbar = np.zeros_like(p_at_cm_norm)
    mask_nz_at = p_at_cm_norm > 0
    cos_tbar[mask_nz_at] = P_at_cm[mask_nz_at, 2] / p_at_cm_norm[mask_nz_at]

    # pT1, pT2 (Max/Min)
    pT1 = np.maximum(pT_t, pT_at)
    pT2 = np.minimum(pT_t, pT_at)

    dists = {
        'mTT': mTT, 
        'pT1': pT1, 
        'pT2': pT2, 
        'deltaPhi': deltaPhi, 
        'weights': weights, 
        'pT': pT_t, 
        'nevents': nevents, 
        'xsec (pb)': xSec, 
        'xSecErr (pb)': xSecErr, 
        'cost*': cos_t,
        'cost*_bar': cos_tbar, 
        'y_t': rap_t, 
        'y_tbar': rap_tbar,
        'abs_delta_y': np.abs(rap_t - rap_tbar), 
        'delta_y': np.abs(rap_t) - np.abs(rap_tbar)
    }

    return dists



def vectorized_rapidity(P):
    """
    Computes rapidity for an array of 4-vectors.
    P shape: (N, 4) [px, py, pz, E]
    """
    E = P[:, 3]
    pz = P[:, 2]
    diff = E - pz
    diff[diff == 0] = 1e-10 # Protect
    return 0.5 * np.log((E + pz) / diff)

def vectorized_delta_phi(P_a, P_b):
    """Computes delta phi between two arrays of 4-vectors."""
    # phi = arctan2(py, px)
    phi_a = np.arctan2(P_a[:, 1], P_a[:, 0])
    phi_b = np.arctan2(P_b[:, 1], P_b[:, 0])
    
    dphi = phi_a - phi_b
    

    dphi = (dphi + np.pi) % (2 * np.pi) - np.pi

    
   
    P_tot = P_a + P_b
    v_cm = P_tot[:, 0:3] / P_tot[:, 3][:, np.newaxis]
    
    P_a_cm = vectorized_boost(P_a, v_cm)
    P_b_cm = vectorized_boost(P_b, v_cm)
    
    phi_a_cm = np.arctan2(P_a_cm[:, 1], P_a_cm[:, 0])
    phi_b_cm = np.arctan2(P_b_cm[:, 1], P_b_cm[:, 0])
    
    dphi_cm = phi_a_cm - phi_b_cm
    dphi_cm = (dphi_cm + np.pi) % (2 * np.pi) - np.pi
    
    return dphi_cm

def vectorized_boost(p, v, c=1):
    """
    Vectorized Lorentz boost.
    p: (N, 4) [px, py, pz, E]
    v: (N, 3) [vx, vy, vz]
    """
    # Components
    px, py, pz, E = p[:, 0], p[:, 1], p[:, 2], p[:, 3]
    vx, vy, vz = v[:, 0], v[:, 1], v[:, 2]
    
    v2 = np.sum(v**2, axis=1)
    
    # Result array
    p_new = np.zeros_like(p)
    
    # Mask for v=0 case
    mask_nz = v2 > 0
    mask_z = ~mask_nz
    
    # If v=0, return p
    p_new[mask_z] = p[mask_z]
    
    # If v > 0, apply boost
    if np.any(mask_nz):
        _v2 = v2[mask_nz]
        _gamma = 1.0 / np.sqrt(1 - _v2)
        
        _px = px[mask_nz]
        _py = py[mask_nz]
        _pz = pz[mask_nz]
        _E  = E[mask_nz]
        _vx = vx[mask_nz]
        _vy = vy[mask_nz]
        _vz = vz[mask_nz]
        
        p_dot_v = _px*_vx + _py*_vy + _pz*_vz
        
        factor = (_gamma - 1) / _v2 * p_dot_v
        
        p_new[mask_nz, 3] = _gamma * (_E - p_dot_v) # E'
        
        term = factor - _gamma * _E
        p_new[mask_nz, 0] = _px + _vx * term
        p_new[mask_nz, 1] = _py + _vy * term
        p_new[mask_nz, 2] = _pz + _vz * term
        
    return p_new

def getInfoSummary(f):
    # Finding the the summary.txt file in the same directory as the input file 'f'
    summary_path = os.path.join(os.path.dirname(f), 'summary.txt')
    if not os.path.exists(summary_path):
        return {'process': 'Unknown', 'cross_section': 0}
        
    with open(summary_path, 'r') as summary_file:
        process = 'Unknown'
        cross_section = 0
        for line in summary_file:
            clean_line = line.strip()
                
            # Getting process
            if clean_line.startswith('Process'):
                try:
                    process = clean_line.split('Process', 1)[1].strip()
                    process =  process.split('[')[0].strip()
                except IndexError:
                    pass
                
    return {'process': process, 'cross_section': cross_section}


def getInfo(f,nlo = False,labelsDict=None):
    """
    Reads the banner and/or the summary of the process to extract information such: cross section, process name, model used, BSM masses and coupling.
    """
    if labelsDict is None:
        labelsDict = {'UV_BSM_ToyModel_NLO-UFO' : '1-loop VLF', 'Top-EFTfull-UFO' : 'VLF EFT', 
                      'SMS-stop-UFO' : 'Scalar EFT', 'SMS-stop_NLO-UFO' : '1-loop Scalar',
              'g g > t t~' : r'$g g \to t \bar{t}$', 'g g > t~ t' : r'$g g \to t \bar{t} $',
              'q q > t t~' : r'$q q \to t \bar{t}$', 'q q > t~ t' : r'$q q \to t \bar{t}$',
              'p p > t t~' : r'$p p \to t \bar{t}$', 'p p > t~ t' : r'$p p \to t \bar{t}$'
              }
    
    runDir = os.path.dirname(f)
    if not os.path.isdir(runDir):
        print(f'Folder {runDir} not found')
        return None
    banners = list(glob.glob(os.path.join(runDir,'*banner*txt')))
    if len(banners) != 1:
        if len(banners) == 0: return None
        banner = banners[0]
    else:
        banner = banners[0]

    with open(banner,'r') as bannerF:
        bannerData = bannerF.read()
    
    # Get process data:
    model = None
    proc = None
    if '<MGProcCard>' in bannerData:
        try:
            processData = bannerData.split('<MGProcCard>')[1].split('</MGProcCard>')[0]
            # Get model
            model = processData.split('Begin MODEL')[1].split('End  MODEL')[0]
            model = model.split('\n')[1].strip()
            # Get process
            proc = processData.split('Begin PROCESS')[1].split('End PROCESS')[0]
            proc = proc.split('\n')[1].split('#')[0].strip()
        except IndexError:
            pass
        
    elif os.path.isfile(os.path.join(runDir,'../../Cards/proc_card_mg5.dat')):
        try:
            procCard = os.path.join(runDir,'../../Cards/proc_card_mg5.dat')
            with open(procCard,'r') as f:
                processData = f.readlines()
            modelLine = [l for l in processData if 'import model' in l][-1]
            model = modelLine.strip().split(' ')[-1]
            model = os.path.basename(model)
            procLine = [l for l in processData if 'generate' in l][-1]
            proc = procLine.strip().split('generate ')[-1]
        except:
            pass

    if proc and '[' in proc and ']' in proc:
        proc = proc.split('[')[0].strip()

    if proc in labelsDict:
        proc = labelsDict[proc]
    if model in labelsDict:
        model = labelsDict[model]

    # Get parameters data:
    mSDM = 0.0
    mPsiT = 0.0
    yDM = 0.0
    mT = 172.5 

    try:
        if '<slha>' in bannerData:
            parsData = bannerData.split('<slha>')[1].split('</slha>')[0]
            parsSLHA = pyslha.readSLHA(parsData)
            
            if 6 in parsSLHA.blocks['MASS']:
                mT  = parsSLHA.blocks['MASS'][6]
            
            if 5000022 in parsSLHA.blocks['MASS'] and nlo == True:
                mSDM = parsSLHA.blocks['MASS'][5000022]
                mPsiT = parsSLHA.blocks['MASS'][5000006]        
                if 'FRBLOCK' in parsSLHA.blocks:
                    yDM = list(parsSLHA.blocks['FRBLOCK'].values())[0]
            elif model == 'VLF EFT':
                 if 'FRBLOCK' in parsSLHA.blocks:
                    pars = list(parsSLHA.blocks['FRBLOCK'].values())
                    if len(pars) > 4:
                        mSDM = pars[3]
                        mPsiT = pars[4]     
                        yDM = pars[0]
            elif 5000002 in parsSLHA.blocks['MASS'] and nlo == True:
                mST = parsSLHA.blocks['MASS'][5000002]
                mChi = parsSLHA.blocks['MASS'][5000012]        
                if 'FRBLOCK' in parsSLHA.blocks:
                    yDM = list(parsSLHA.blocks['FRBLOCK'].values())[-1]
                mSDM = mChi
                mPsiT = mST
            elif model == 'SMS EFT':
                if 'FRBLOCK' in parsSLHA.blocks:
                    pars = list(parsSLHA.blocks['FRBLOCK'].values())
                    if len(pars) > 2:
                        mST= pars[1]
                        mChi = pars[2]     
                        yDM = pars[0]
                        mSDM = mChi
                        mPsiT = mST
    except Exception as e:
        pass

    if yDM == 0.0:
        model = 'SM'
    
    # Get event data:
    nEvents = -1
    xsec = -1.0
    
    if '<MGGenerationInfo>' in bannerData:
        try:
            eventData = bannerData.split('<MGGenerationInfo>')[1].split('</MGGenerationInfo>')[0]
            nEvents = eval(eventData.split('\n')[1].split(':')[1].strip())
            xsec = eval(eventData.split('\n')[2].split(':')[1].strip())
        except:
            pass
    elif os.path.isfile(os.path.join(runDir,'summary.txt')):
        try:
            with open(os.path.join(runDir,'summary.txt'),'r') as f:
                summaryLines = f.readlines()
            
            totalXsecLines = [l for l in summaryLines if 'Total cross section' in l]
            if totalXsecLines:
                totalXsecLine = totalXsecLines[0]
                if 'DO NOT USE' in totalXsecLine:
                    idx_list = [i for i,l in enumerate(summaryLines) if 'Scale variation' in l]
                    if idx_list:
                        totalXsecLine = summaryLines[idx_list[0]+2]

                if 'Total cross section' in totalXsecLine:
                    totalXsecLine = totalXsecLine.split(':')[1].strip()
                    totalXsecLine = totalXsecLine.split(' +')[0].strip()
                    totalXsecLine = totalXsecLine.replace('pb','')
                    xsec = float(totalXsecLine)
        except:
            pass

    fileInfo = {'model' : model, 'process' : proc, '(mSDM,mPsiT,mT,yDM)' : (mSDM,mPsiT,mT,yDM),
               'xsec (pb)' : xsec, 'nevents' : nEvents}
    
    return fileInfo

def getXsection(fpath):
    """
    Reads a LHE files and returns a the cross section and it's error
    """
    fixedFile = tempfile.mkstemp(suffix='.lhe')
    os.close(fixedFile[0])
    fixedFile = fixedFile[1]
    with gzip.open(fpath,'rt') as f:
        data = f.readlines()
        with open(fixedFile,'w') as newF:
            for l in data:
                if 'generate' in l:
                    continue
                newF.write(l)
    initBlock = pylhe.read_lhe_init(fixedFile)
    initBlock = initBlock['procInfo'][0]
    os.remove(fixedFile)
    return (initBlock['xSection'], initBlock['error'])

    

def get_params_from_filename(run_dir):
    """Parses a banner's filename containing '_interference_' to find parameters."""
    banner_files = glob.glob(os.path.join(run_dir, '*banner.txt'))
    if not banner_files:
        print(f" Error: No banner file found in {run_dir.name}")
        return None, None, None 
    else:
        # Added print back as requested
        print(f" -> Processing run: {os.path.basename(banner_files[0])}")

    banner_file = banner_files[0]
    basename = os.path.basename(banner_file)
    stem = os.path.splitext(basename)[0]
    
    try:
        parts = stem.split('_')
        idx = parts.index('banner')
        m1, m2 = parts[idx - 2], parts[idx - 1]
        return f"mPsiT_{m1}_mSDM_{m2}", float(m1), float(m2)
    except (ValueError, IndexError):
        return f"run_{os.path.basename(run_dir)}", 0.0, 0.0

def AddInfoToDistributions(distributions, params, mPsiT, mSDM, info, nlo = False, bias = False):
    """Adds the model name, process and mass parameters to the final dictionary"""
    converter_dict = {'TopEFT': 'VLF EFT', 'UV_BSM': '1-loop VLF', 'sm':'SM',
                      'SMS_EFT': 'Scalar EFT', 'SMS_1_loop': '1-loop Scalar',
                      'qq2ttbar_gs4_ydm2': r'$q q \to t \bar{t}$', 'gg2ttbar_gs4_ydm2': r'$g g \to t \bar{t}$',
                      'pp2ttbar_gs4_ydm2': r'$p p \to t \bar{t}$ ', 'qq2ttbar_gs6': r'$q q \to t \bar{t}$', 'gg2ttbar_gs6': r'$g g \to t \bar{t}$',
                      'pp2ttbar_gs6': r'$p p \to t \bar{t}$', 'qq2ttbar_gs4': r'$q q \to t \bar{t}$', 'gg2ttbar_gs4': r'$g g \to t \bar{t}$',
                      'pp2ttbar_gs4': r'$p p \to t \bar{t}$', 'gs4': r'$g_s^4$', 'gs6': r'$g_s^6$', 'ydm2': r'$y_{DM}^2$'}
    
    #Add new keys with the new information
    distributions['model'] = converter_dict.get(params.get('model'), params.get('model'))
    distributions['process'] = converter_dict.get(params.get('process'), params.get('process'))
    distributions['mass_params'] = (mPsiT,mSDM)
    distributions['ydm'] = info['(mSDM,mPsiT,mT,yDM)'][-1]
    distributions['bias'] = bias

    if nlo == True:
        distributions['weights'] = distributions['nevents']*distributions['weights']

    
    #Correcting the weights when doing bias generation
    if info['xsec (pb)'] > 0 and distributions['xsec (pb)'] > 0:
        if abs((distributions['xsec (pb)']-info['xsec (pb)'])/info['xsec (pb)']) > 0.01 and nlo == True:
            distributions['weights'] = (info['xsec (pb)']/distributions['xsec (pb)']) * distributions['weights']
            distributions['xsec (pb)'] = info['xsec (pb)']
    

    #Extract the coupling order
    if 'process' in params and '_' in params['process']:
        parts = params['process'].split('_')
        parts = parts[1:]
        clean_parts = []
        for p in parts:
             clean_parts.append(converter_dict.get(p, p))
        distributions['cp_order'] = clean_parts
    else:
        distributions['cp_order'] = []
    
    return distributions


    
def read_config(config_file_path):
    """Reads key-value pairs from the specified configuration file."""
    config = {}
    try:
        with open(config_file_path, 'r') as f:
            for line in f:
                if line.strip() and not line.strip().startswith('#'):
                    key, value = line.strip().split(':', 1)
                    config[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"Error: Configuration file not found at '{config_file_path}'")
        return None
    return config
    
def str_to_bool(s):
    if s.lower() in ['true', '1', 't', 'yes', 'on']:
        return True
    return False

def main():
    parser = argparse.ArgumentParser(description="Calculate distributions from LHE files using a configuration file.")
    parser.add_argument('config_file', type=str, help='Path to the configuration file (e.g., config.txt)')
    args = parser.parse_args()

    params = read_config(args.config_file)
    if params is None:
        return

    required_keys = ['process_directory', 'output_path', 'model', 'process', 'run_name']
    if not all(key in params for key in required_keys):
        print("Error: One or more required keys are missing from the configuration file.")
        print(f"Required keys are: {required_keys}")
        return

    skip_existing = str_to_bool(params.get('skip_existing', 'False'))

    process_dir = Path(params['process_directory']) / params['model'] / params['process'] / 'Events'
    if not process_dir.exists():
        print(f"Error, directory not found: {process_dir}")
        return
    
    run_name_to_search = params.get('run_name', 'run_*')
    lhe_files = sorted(list(set(process_dir.glob(f"{run_name_to_search}/*events.lhe.gz"))))
    if not lhe_files:
        print(f"Error, no {params['run_name']}/*events.lhe.gz files found in {process_dir}")
        return

    base_output_path = Path(params['output_path'])
    run_dirs = sorted(list(set([p.parent for p in lhe_files]))) 
    if not run_dirs:
        print(f"Error, no run directories found in {process_dir}")
        return

    print(f"Found {len(run_dirs)} runs for model '{params['model']}' and process '{params['process']}. Storing results in '{base_output_path}'.")
    if skip_existing:
        print("Option 'skip_existing' is ON. Existing files will be skipped.")

    # PROGRESSBAR SETUP
    widgets = [
        'Run: ', P.Counter(), f'/{len(run_dirs)} ',
        P.Percentage(), ' ',
        P.Bar(marker=P.RotatingMarker(), left='[', right=']'),
        ' ', P.Timer(), ' ', P.ETA()
    ]
    
    pbar = P.ProgressBar(widgets=widgets, maxval=len(run_dirs)).start()

    for i, run_dir in enumerate(run_dirs):
        start_time = time.time()
        
        nlo = False
        banner_file = glob.glob(os.path.join(run_dir, '*banner.txt'))
        
        is_biased_run = False
        if banner_file and 'bias' in os.path.basename(banner_file[0]).lower():
            is_biased_run = True

        base_run_name = params['run_name'].removesuffix('_*')
        if is_biased_run and base_run_name == 'run':
            output_dir = base_output_path / 'bias' / params['model'] / params['process']
        elif base_run_name == 'run':
            output_dir = base_output_path / params['model'] / params['process']
        elif is_biased_run:
            output_dir = base_output_path / 'bias' / params['model'] / params['process'] / base_run_name
        else:
            output_dir = base_output_path / params['model'] / params['process'] / base_run_name

        output_dir.mkdir(parents=True, exist_ok=True)

        identifier_string, mPsiT, mSDM = get_params_from_filename(run_dir)
        if identifier_string is None:
            identifier_string = run_dir.name
        
        output_filename = f"{identifier_string}.npz"
        output_path = output_dir / output_filename
        
        if skip_existing and output_path.exists():
            print(f"Skipping {run_dir.name} (File exists)")
            pbar.update(i + 1)
            continue
        
        if params['model'] == 'UV_BSM' or params['model'] == 'SMS_1_loop':
            try:
                lhe_file_path = next(run_dir.glob('events.lhe.gz'))
                nlo = True
            except StopIteration:
                lhe_file_path = None
        else:
            try:
                lhe_file_path = next(run_dir.glob('unweighted_events.lhe.gz'))
            except StopIteration:
                lhe_file_path = None

        if not lhe_file_path:
            print(f"No LHE file found in {run_dir.name}. Skipping.")
            pbar.update(i + 1)
            continue

        try:
            info = getInfo(lhe_file_path, nlo)
            distributions = getDistributions(lhe_file_path)

            if distributions and 'mTT' in distributions and distributions['mTT'].size > 0:
                distributions = AddInfoToDistributions(distributions, params, mPsiT, mSDM, info, nlo, is_biased_run)
                np.savez_compressed(output_path, **distributions)
                
                #  SAVED RESULTS PRINT
                print(f"Saved results to: {output_path}")
                
                end_time = time.time()
                elapsed = end_time - start_time
                print(f"Run {run_dir.name} done in {elapsed:.2f}s")
                print() 
            
            else:
                print(f"Run {run_dir.name} -> No valid events found.")
        except Exception as e:
            print(f"Error processing {run_dir.name}: {e}")
        
        pbar.update(i + 1)

    pbar.finish()

if __name__ == "__main__":
    main()