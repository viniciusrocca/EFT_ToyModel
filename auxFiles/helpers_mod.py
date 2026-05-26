"""
helpers.py

Useful functions for calculations and plotting
"""

import os
import gzip
import urllib.request
import glob
import numpy as np
import pandas as pd
from tqdm.auto import tqdm
from matplotlib.ticker import MaxNLocator
import matplotlib.pyplot as plt
import tempfile
import pylhe

SQRT_S = 13000.0  # Center of mass energy in GeV

# ============================================================
# Data Acquisition & Management
# ============================================================

def download_data_files(base_url, files_dict, out_dir="data"):
    """
    Checks the local directory for the specified dataset files. 
    If a file is missing, it is downloaded from the designated remote 
    repository (e.g., GitHub raw content).
    """
    os.makedirs(out_dir, exist_ok=True)
    for name, url in files_dict.items():
        out = os.path.join(out_dir, f"{name}.lhe.gz")
        if not os.path.exists(out):
            print(f"Downloading {name}...")
            urllib.request.urlretrieve(url, out)
        else:
            print(f"{out} already exists")

def load_model_data(base_path, model_name, rescale=1.0):
    """
    Aggregates all .npz simulation files corresponding to a specific 
    physics model, applies a universal weight rescaling factor (for 
    coupling adjustments), and returns a consolidated Pandas DataFrame.
    """
    file_pattern = f"{base_path}/*{model_name}*.npz"
    files = glob.glob(file_pattern)

    if not files:
        print(f"Warning: No files found for {model_name} at {base_path}")
        return pd.DataFrame(columns=['m_tt', 'weight', 'label'])

    mtt_list, w_list = [], []
    for f in files:
        data = np.load(f, allow_pickle=True)
        mtt_list.append(data['mTT'])
        w_list.append(data['weights'] * rescale)

    df = pd.DataFrame({'m_tt': np.concatenate(mtt_list), 'weight': np.concatenate(w_list)})
    df['label'] = model_name
    return df

# ============================================================
# Kinematics & Parsing
# ============================================================

def rapidity(E, pz, eps=1e-12):
    """Calculates the momentum-dependent rapidity of a particle."""
    num, den = E + pz, E - pz
    if num <= eps or den <= eps: return np.nan
    return 0.5 * np.log(num / den)

def pt(px, py):
    """Calculates the transverse momentum (pT)."""
    return np.hypot(px, py)

def phi(px, py):
    """Calculates the azimuthal angle phi."""
    return np.arctan2(py, px)

def delta_phi(phi1, phi2):
    """Calculates the difference in azimuthal angle between two particles."""
    d = phi1 - phi2
    return (d + np.pi) % (2 * np.pi) - np.pi

def mass(E, px, py, pz):
    """Calculates the invariant mass from a 4-momentum vector."""
    m2 = E*E - px*px - py*py - pz*pz
    return np.sqrt(max(m2, 0.0))

def boost_to_rest_frame(p4, parent):
    """
    Performs a Lorentz transformation, boosting a 4-momentum vector (p4) 
    into the rest frame of its parent particle/system.
    """
    E, px, py, pz = p4
    EP, Px, Py, Pz = parent
    bx, by, bz = Px/EP, Py/EP, Pz/EP
    b2 = bx*bx + by*by + bz*bz
    if b2 >= 1.0 or b2 < 1e-16: return np.array([E, px, py, pz], dtype=float)
    gamma = 1.0 / np.sqrt(1.0 - b2)
    bp = bx*px + by*py + bz*pz
    gamma2 = (gamma - 1.0) / b2
    pxp = px + (-gamma * E + gamma2 * bp) * bx
    pyp = py + (-gamma * E + gamma2 * bp) * by
    pzp = pz + (-gamma * E + gamma2 * bp) * bz
    Ep  = gamma * (E - bp)
    return np.array([Ep, pxp, pyp, pzp], dtype=float)

def parse_event_block(lines, rescale_weight_by=1.0):
    """
    Parses a single <event> block from an LHE file, extracting top quark 
    kinematics and calculating macroscopic event-level observables like 
    invariant mass (m_tt) and transverse momentum (pT).
    """
    content = [ln.strip() for ln in lines if ln.strip()]
    if not content: return None

    header = content[0].split()
    nup, xwgtup = int(header[0]), float(header[2]) * rescale_weight_by

    particles = []
    for ln in content[1:1+nup]:
        cols = ln.split()
        if len(cols) < 13: continue
        particles.append({
            "pid": int(cols[0]), "status": int(cols[1]),
            "px": float(cols[6]), "py": float(cols[7]), "pz": float(cols[8]),
            "E":  float(cols[9]), "M": float(cols[10])
        })

    incoming = [p for p in particles if p["status"] == -1]
    final = [p for p in particles if p["status"] == 1]
    tops, tbars = [p for p in final if p["pid"] == 6], [p for p in final if p["pid"] == -6]
    
    if not tops or not tbars: return None

    t, tb = tops[0], tbars[0]
    t4 = np.array([t["E"], t["px"], t["py"], t["pz"]], dtype=float)
    tb4 = np.array([tb["E"], tb["px"], tb["py"], tb["pz"]], dtype=float)
    tt4 = t4 + tb4

    t_star = boost_to_rest_frame(t4, tt4)
    p_star = np.sqrt(t_star[1]**2 + t_star[2]**2 + t_star[3]**2)
    cos_theta_star = np.nan if p_star < 1e-12 else t_star[3] / p_star

    extra = [p for p in final if abs(p["pid"]) in [1,2,3,4,5,21] and abs(p["pid"]) != 6]
    extra_pts = sorted([pt(p["px"], p["py"]) for p in extra], reverse=True)

    y_t, y_tb = rapidity(t["E"], t["pz"]), rapidity(tb["E"], tb["pz"])
    return {
        "weight": xwgtup,
        "m_t": mass(*t4), "m_tbar": mass(*tb4), "m_tt": mass(*tt4),
        "pt_t": pt(t["px"], t["py"]), "pt_tbar": pt(tb["px"], tb["py"]), "pt_tt": pt(tt4[1], tt4[2]),
        "y_t": y_t, "y_tbar": y_tb, "y_tt": rapidity(tt4[0], tt4[3]),
        "abs_delta_y": abs(y_t - y_tb) if np.isfinite(y_t) and np.isfinite(y_tb) else np.nan,
        "cos_theta_star": cos_theta_star,
        "abs_cos_theta_star": abs(cos_theta_star) if np.isfinite(cos_theta_star) else np.nan,
        "ptj1": extra_pts[0] if len(extra_pts) > 0 else 0.0,
    }

def read_lhe_features(filepath, label=None, max_events=None, rescale_weight_by=1.0):
    """
    Iterates through a compressed or raw LHE file, feeding events to the parser 
    and compiling the returned variables into an analysis-ready Pandas DataFrame.
    """
    data = {
        "weight": [], "m_t": [], "m_tbar": [], "m_tt": [],
        "pt_t": [], "pt_tbar": [], "pt_tt": [],
        "y_t": [], "y_tbar": [], "y_tt": [],
        "abs_delta_y": [], "cos_theta_star": [], "abs_cos_theta_star": [], "ptj1": []
    }
    if label: data["label"] = []

    block, in_event = [], False
    event_count = 0
    opener = gzip.open if filepath.endswith(".gz") else open
    
    with opener(filepath, "rt", encoding="utf-8", errors="ignore") as f:
        for line in tqdm(f, desc=f"Reading {os.path.basename(filepath)}"):
            if "<event>" in line:
                in_event = True
                block = []
                continue
            if "</event>" in line:
                rec = parse_event_block(block, rescale_weight_by)
                if rec is not None:
                    for key, val in rec.items():
                        data[key].append(val)
                    if label:
                        data["label"].append(label)
                        
                    event_count += 1
                    if max_events and event_count >= max_events: break
                in_event = False
                continue
            if in_event: 
                block.append(line)

    return pd.DataFrame(data)

def get_run_metadata(filepath, is_nlo=False):
    """
    Extracts the true cross-section, LHE cross-section, and event count.
    - LO: Truth is strictly the LHE file.
    - NLO: Truth is strictly the summary.txt file.
    """
    run_dir = os.path.dirname(filepath)
    info = {'nevents': -1, 'xsec_lhe': -1.0, 'xsec_true': -1.0}
    
    fd, fixedFile = tempfile.mkstemp(suffix='.lhe')
    os.close(fd)
    try:
        with gzip.open(filepath, 'rt') as f_in, open(fixedFile, 'w') as f_out:
            for line in f_in:
                if 'generate' not in line:
                    f_out.write(line)
        
        initBlock = pylhe.read_lhe_init(fixedFile)
        info['xsec_lhe'] = initBlock['procInfo'][0]['xSection']
        info['nevents'] = pylhe.read_num_events(fixedFile)
        info['xsec_true'] = info['xsec_lhe'] 
        
    except Exception as e:
        print(f"Error parsing LHE header from {os.path.basename(filepath)}: {e}")
    finally:
        if os.path.exists(fixedFile):
            os.remove(fixedFile)

    if is_nlo:
        summary_path = os.path.join(run_dir, 'summary.txt')
        if os.path.isfile(summary_path):
            with open(summary_path, 'r') as f:
                lines = f.readlines()
                
            try:
                target_idx = [i for i, l in enumerate(lines) if 'Total cross section' in l][0]
                xsec_line = lines[target_idx]
                
                if 'DO NOT USE' in xsec_line:
                    scale_idx = [i for i, l in enumerate(lines) if 'Scale variation' in l][0]
                    xsec_line = lines[scale_idx + 2]
                    
                if 'Total cross section' in xsec_line:
                    xsec_line = xsec_line.split(':')[1].strip()
                    
                xsec_line = xsec_line.split(' +')[0].strip().replace('pb', '')
                info['xsec_true'] = float(xsec_line)
            except Exception:
                pass

    if info['nevents'] <= 0:
        banners = glob.glob(os.path.join(run_dir, '*banner*txt'))
        if banners:
            with open(banners[0], 'r') as f:
                banner_data = f.read()
            if '<MGGenerationInfo>' in banner_data:
                gen_info = banner_data.split('<MGGenerationInfo>')[1].split('</MGGenerationInfo>')[0]
                try:
                    info['nevents'] = eval(gen_info.split('\n')[1].split(':')[1].strip())
                except Exception:
                    pass
                    
    return info

def load_lhe_with_corrections(file_pattern, label=None, is_nlo=False, custom_rescale=1.0, max_events=None):
    """
    Finds LHE files and streams them into a DataFrame. 
    Guarantees that sum(weights) exactly equals the true cross section.
    """
    files = glob.glob(file_pattern)
    if not files:
        print(f"Warning: No files found for pattern {file_pattern}")
        return pd.DataFrame(columns=["weight", "m_t", "m_tbar", "m_tt", "pt_t", "pt_tbar", "pt_tt", "label"])
        
    print(f"Loading {label} from {len(files)} LHE files...")
    df_list = []
    
    for f in files:
        info = get_run_metadata(f, is_nlo=is_nlo)
        base_rescale = 1.0
        
        if not is_nlo and info['nevents'] > 0:
            base_rescale = 1.0 / info['nevents']
            
        elif is_nlo and info['xsec_lhe'] > 0 and info['xsec_true'] > 0:
            drift = abs(info['xsec_lhe'] - info['xsec_true']) / info['xsec_true']
            if drift > 0.01:
                bias_factor = info['xsec_true'] / info['xsec_lhe']
                base_rescale = bias_factor
                
                run_name = os.path.basename(os.path.dirname(f))
                print(f"  -> [BIAS DETECTED] {run_name}: Rescaled weights by {bias_factor:.5f} "
                      f"(True: {info['xsec_true']:.5e} pb, LHE: {info['xsec_lhe']:.5e} pb)")
        
        total_rescale = custom_rescale * base_rescale
        df = read_lhe_features(f, label=label, max_events=max_events, rescale_weight_by=total_rescale)
        
        if not df.empty:
            df_list.append(df)
        else:
            print(f"  -> Skipping {os.path.basename(f)} (No valid events)")
            
    if not df_list:
        return pd.DataFrame()
        
    return pd.concat(df_list, ignore_index=True)

# ============================================================
# Histogram & Template Operations
# ============================================================

def class_normalized_weights(df, label_col="label", weight_col="weight"):
    w = df[weight_col].astype(float).copy()
    out = np.zeros(len(df), dtype=float)
    for lab in df[label_col].unique():
        mask = (df[label_col] == lab).values
        s = np.sum(np.abs(w[mask]))
        out[mask] = w[mask] / s if s > 0 else 0.0
    return out

def event_number_normalization(h_ref, h, lum=500.0):
    n_ref, n = lum * np.asarray(h_ref, dtype=float) * 1000.0, lum * np.asarray(h, dtype=float) * 1000.0
    return n * sum(n_ref)/sum(n) if sum(n) != 0 else n

def weighted_hist(x, w, bins):
    h, _ = np.histogram(x, bins=bins, weights=w)
    return h.astype(float)

def build_template(x, w, bins, alpha=1e-12, density=False):
    h, _ = np.histogram(x, bins=bins, weights=w)
    h = h.astype(float) + alpha
    if density: h /= h.sum()
    return h

def build_shape_template(h, alpha=1e-12):
    h_shape = h + alpha
    return h_shape / h_shape.sum()

def build_signed_delta(h_hyp, h_sm, alpha=1e-12):
    return (h_hyp - h_sm) / (h_sm + alpha)

def normalize_signed_template(delta, alpha=1e-12):
    norm = np.sum(np.abs(delta))
    return delta / norm if norm > alpha else None

def js_divergence(p, q, eps=1e-12):
    p, q = np.asarray(p, dtype=float) + eps, np.asarray(q, dtype=float) + eps
    p, q = p / p.sum(), q / q.sum()
    m = 0.5 * (p + q)
    return 0.5 * np.sum(p * np.log(p / m)) + 0.5 * np.sum(q * np.log(q / m))

def kl_divergence(p, q, eps=1e-12):
    p, q = np.asarray(p, dtype=float) + eps, np.asarray(q, dtype=float) + eps
    p, q = p / p.sum(), q / q.sum()
    return np.sum(p * np.log(p / q))

def signed_l2_distance(d1, d2):
    return np.sqrt(np.mean((d1 - d2)**2))

def asimov_shape_llr_stat_only(p_true, p_test, N=10000, eps=1e-12):
    p_true, p_test = np.asarray(p_true, dtype=float) + eps, np.asarray(p_test, dtype=float) + eps
    p_true, p_test = p_true / p_true.sum(), p_test / p_test.sum()
    n = N * p_true
    q = 2.0 * np.sum(n * np.log(p_true / p_test))
    return q, np.sqrt(max(q, 0.0))

# ============================================================
# Variance and Significance Calculations
# ============================================================

def calc_variance_hat_delta(h_hyp, h_sm, eps, alpha=1e-12):
    n_hyp = h_hyp
    n_sm = h_sm
    delta = (n_hyp - n_sm) / (n_sm + alpha)
    S = np.sum(np.abs(delta)) + alpha
    
    sigma2_delta = (n_hyp / (n_sm**2 + alpha)) + (n_hyp**2 * eps**2) / (n_sm**2 + alpha)
    bracket_i = (1.0 / S**2) - (2.0 * np.abs(delta) / S**3) + (delta**2 / S**4)
    term_same = bracket_i * sigma2_delta
    
    sum_sigma2_j_neq_i = np.sum(sigma2_delta) - sigma2_delta
    term_diff = (delta**2 / S**4) * sum_sigma2_j_neq_i
    
    return term_same + term_diff

def asimov_signed_Z_rigorous(dA, dB, hA, hB, n_sm, eps, mode="avg", alpha=1e-12):
    var_hat_A = calc_variance_hat_delta(hA, n_sm, eps, alpha=alpha)
    var_hat_B = calc_variance_hat_delta(hB, n_sm, eps, alpha=alpha)
    
    if mode =="test": var_n_ref = var_hat_B
    else: var_n_ref = (1/2)**2 * (var_hat_A + var_hat_B)
    num = (dA - dB)**2
    den = var_n_ref + alpha
    
    return np.sqrt(max(np.sum(num / den), 0.0)), num, den

def asimov_shape_Z_with_syst(p_true, p_test, frac_syst=0.05, mode="avg", eps=1e-12):
    p_true = np.asarray(p_true, dtype=float) + eps
    p_test = np.asarray(p_test, dtype=float) + eps

    if mode == "test": n_ref = p_test
    else: n_ref = 0.5 * (p_true + p_test)

    var = n_ref + (frac_syst * n_ref)**2
    num = (p_true - p_test)**2
    
    return np.sqrt(max(np.sum(num / var), 0.0)), num, var

# ============================================================
# Plotting Utilities
# ============================================================

def beautify_axis(ax, grid=False):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(direction="in", top=False, right=False, length=5)
    if grid: ax.grid(True, alpha=0.22, linewidth=0.7)

def get_best_pair_and_cut(df, N=100000):
    col = df.columns[-1]
    for c in [f"Z_{N}_a_true", f"Z_{N}_eps_00", f"Z_{N}_eps_02", "Z_eps_00", "Z_eps_02", "Z_shape"]:
        if c in df.columns:
            col = c
            break
    row = df.loc[df[col].idxmax()]
    return row["pair"], int(row["mcut"])

def format_model_label(model_name):
    formatted = model_name.replace("Zprime", r"$Z^\prime$")
    formatted = formatted.replace("FakeData", "Fake Data")
    return formatted

def get_mass_label_from_fits(model_name, best_fits):
    """
    Parses the best_fits dictionary and returns the properly formatted LaTeX 
    string containing the model masses.
    """
    if not best_fits or model_name not in best_fits:
        return ""
    
    fits = best_fits[model_name]
    if model_name == "VLF":
        return rf"$m_{{\psi_T}} = {fits.get('mPsiT', 0):.0f}$ GeV, $m_{{\phi}} = {fits.get('mSDM', 0):.0f}$ GeV"
    elif model_name == "Scalar":
        return rf"$m_{{\varphi_T}} = {fits.get('mST', 0):.0f}$ GeV, $m_{{\chi}} = {fits.get('mChi', 0):.0f}$ GeV"
    elif "Zprime" in model_name:
        return rf"$m_{{Z^\prime}} = {fits.get('mZp', 0):.0f}$ GeV"
    
    return ""

# ============================================================
# Optimized Mass & Luminosity Scans
# ============================================================

def run_fast_lumi_scan(sm_data, bsm_data, labels, target_mcut, mcut_max, bin_width, lumi_targets, eps_values, alpha=1e-12, fake_model='FakeData', bin_offset=0.0, sig_norm = True):
    sm_x, sm_w = sm_data["x"], sm_data["w"]
    sm_mask = (sm_x > target_mcut) & (sm_x <= mcut_max)
    sm_x_tail, sm_w_tail = sm_x[sm_mask], sm_w[sm_mask]
    
    if len(sm_x_tail) == 0:
        print(f"Warning: 0 SM events found above {target_mcut} GeV.")
        return pd.DataFrame()

    bins = np.arange(target_mcut + bin_offset, mcut_max + bin_width, bin_width)
    h_sm_raw = weighted_hist(sm_x_tail, sm_w_tail, bins)

    raw_templates = {}
    for lab in labels:
        if lab not in bsm_data: continue
        
        lab_x, lab_w = bsm_data[lab]["x"], bsm_data[lab]["w"]
        hyp_mask = (lab_x > target_mcut) & (lab_x <= mcut_max)
        if np.sum(hyp_mask) == 0: continue
        
        raw_templates[lab] = weighted_hist(lab_x[hyp_mask], lab_w[hyp_mask], bins)

    if fake_model not in raw_templates:
        print(f"Error: fake_model '{fake_model}' not found in data.")
        return pd.DataFrame()

    ref_template = raw_templates[fake_model].copy()
    scaled_templates = {}
    norm_templates = {}
    
    for lab in labels:
        if lab not in raw_templates: continue
        
        if sig_norm:
          aligned_sig = event_number_normalization(ref_template, raw_templates[lab], lum=1e-3)
          scaled_templates[lab] = aligned_sig + h_sm_raw
        else:
          aligned_sig = raw_templates[lab] 
          scaled_templates[lab] = aligned_sig 
        
        delta = build_signed_delta(scaled_templates[lab], h_sm_raw, alpha=alpha)
        norm_templates[lab] = normalize_signed_template(delta, alpha=alpha)

    rows = []
    for lum in lumi_targets:
        n_sm = h_sm_raw * lum * 1000.0

        for lab in labels:
            if lab not in raw_templates or lab == fake_model:
                continue 

            a, b = fake_model, lab
            
            hA, hB = scaled_templates[a]*1000.0*lum, scaled_templates[b]*1000.0*lum
            dA, dB = norm_templates[a], norm_templates[b]
            
            base_row = {"lumi": lum, "pair": f"{a} vs {b}"}
            
            for eps in eps_values:
                Z_fa, _, _ = asimov_signed_Z_rigorous(dA, dB, hA, hB, n_sm, eps, mode = "test", alpha = alpha)
                base_row[f"Z_fa_eps_{int(100*eps):02d}"] = Z_fa
                
                Z_sh, _, _ = asimov_shape_Z_with_syst(hA, hB, frac_syst=eps, mode="test", eps=alpha)
                base_row[f"Z_sh_eps_{int(100*eps):02d}"] = Z_sh
                
            rows.append(base_row)

    return pd.DataFrame(rows)


def run_fast_mcut_scan(sm_data, bsm_data, labels, mcuts, mcut_max, bin_width, L_target, eps_values, alpha=1e-12, fake_model='FakeData', bin_offset=0.0, sig_norm = True):
    rows = []
    
    mcut_base = mcuts[0]
    bins = np.arange(mcut_base + bin_offset, mcut_max + bin_width, bin_width)
    bin_edges = bins[:-1] 
    
    sm_mask = (sm_data["x"] > mcut_base) & (sm_data["x"] <= mcut_max)
    h_sm_raw = weighted_hist(sm_data["x"][sm_mask], sm_data["w"][sm_mask], bins)
    n_sm = h_sm_raw * L_target * 1000.0

    raw_templates = {}
    for lab in labels:
        if lab not in bsm_data: continue
        lab_x, lab_w = bsm_data[lab]["x"], bsm_data[lab]["w"]
        hyp_mask = (lab_x > mcut_base) & (lab_x <= mcut_max)
        raw_templates[lab] = weighted_hist(lab_x[hyp_mask], lab_w[hyp_mask], bins)
    
    if fake_model not in raw_templates:
        print(f"Error: fake_model '{fake_model}' not found in data.")
        return pd.DataFrame()

    ref_template = raw_templates[fake_model].copy()
    for lab in labels:
        if lab not in raw_templates: continue
        if sig_norm:
          aligned_sig = event_number_normalization(ref_template, raw_templates[lab], lum=L_target)
          raw_templates[lab] = aligned_sig + n_sm
        else:
          aligned_sig =  raw_templates[lab] * L_target * 1000.0
          raw_templates[lab] = aligned_sig + n_sm

    for mcut in mcuts:
        cut_mask = (bin_edges >= mcut) & (bin_edges < mcut_max)
        
        if not np.any(cut_mask): continue
            
        n_sm_cut = n_sm[cut_mask]
        
        norm_templates = {}
        for lab in labels:
            if lab not in raw_templates: continue
            h_combined_cut = raw_templates[lab][cut_mask]
            delta = build_signed_delta(h_combined_cut, n_sm_cut, alpha=alpha)
            norm_templates[lab] = normalize_signed_template(delta, alpha=alpha)

        for lab in labels:
            if lab not in raw_templates or lab == fake_model: continue
            
            a, b = fake_model, lab
            hA = raw_templates[a][cut_mask]
            hB = raw_templates[b][cut_mask]
            dA, dB = norm_templates[a], norm_templates[b]
            
            base_row = {"mcut": mcut, "pair": f"{a} vs {b}"}
            
            for eps in eps_values:
                Z_fa, _, _ = asimov_signed_Z_rigorous(dA, dB, hA, hB, n_sm_cut, eps, mode = "test", alpha = alpha)
                base_row[f"Z_fa_eps_{int(100*eps):02d}"] = Z_fa
                
                Z_sh, _, _ = asimov_shape_Z_with_syst(hA, hB, frac_syst=eps, mode="test", eps=alpha)
                base_row[f"Z_sh_eps_{int(100*eps):02d}"] = Z_sh
                
            rows.append(base_row)

    return pd.DataFrame(rows)




# ============================================================
# Grid Plotting Functions (Shape vs Falloff Comparisons)
# ============================================================

def plot_mcut_syst_grid(results, mcut_max, eps_values, metric="sh", outfile=None, excl_stats=False, fake_model='FakeData', best_fits=None):
    syst_styles = {0.00: ("black", "-"), 0.02: ("#1f77b4", "--"), 0.05: ("#ff7f0e", "-."), 0.10: ("#d62728", ":")}
    
    pairs = list(results["pair"].unique())
    fig, axes = plt.subplots(1, len(pairs), figsize=(5.0*len(pairs), 5.2), sharex=True)
    if len(pairs) == 1: axes = [axes]
    
    method_name = "Standard Shape Method" if metric == "sh" else "Normalized Falloff Method"

    for j, pair in enumerate(pairs):
        ax = axes[j]
        sub = results[results["pair"] == pair].sort_values("mcut")
        eps_v = eps_values[1:] if excl_stats else eps_values

        for eps_syst in eps_v:
            col = f"Z_{metric}_eps_{int(100*eps_syst):02d}" 
            if col not in sub.columns: continue
                
            color, ls = syst_styles.get(eps_syst, ("black", "-"))
            label = "stat. only" if eps_syst == 0 else rf"{int(100*eps_syst)}\% syst."
            ax.plot(sub["mcut"], sub[col], marker="o", color=color, linestyle=ls, label=label)

        ax.axhline(3.0, color='gray', linestyle='--', alpha=0.7, linewidth=1.5, label=r"$Z = 3\sigma$")
        ax.axhline(5.0, color='gray', linestyle=':', alpha=0.7, linewidth=1.5, label=r"$Z = 5\sigma$")

        bsm_name = pair.split(" vs ")[-1] if " vs " in pair else pair
        title_str = format_model_label(pair)
        
        mass_str = get_mass_label_from_fits(bsm_name, best_fits)
        if mass_str:
            title_str += f"\n[{mass_str}]"
        
        ax.set_title(title_str)
        if j == 0:
            ax.set_ylabel(r"Separation Significance $Z$")

        upper_label = f"{mcut_max}" if mcut_max is not None else r"\infty"
        ax.set_xlabel(rf"$m_{{t\bar t}}^{{\min}}$ up to {upper_label} [GeV]")
        ax.set_ylim(bottom=0) 
        beautify_axis(ax, grid=True) 

    plt.tight_layout(rect=[0, 0, 1, 0.86])

    handles, labels_ = axes[-1].get_legend_handles_labels()
    by_label = dict(zip(labels_, handles))
    

    fig.legend(by_label.values(), by_label.keys(), loc="center", ncol=3, frameon=False, bbox_to_anchor=(0.5, 0.88))
    fig.suptitle(method_name + f' [Fake Data Baseline: {format_model_label(fake_model)}]' , fontsize=16, y=0.98)

    if outfile:
        fig.savefig(outfile, bbox_inches="tight", dpi=300)
    plt.show()


def plot_lumi_syst_grid(results, eps_values, metric="sh", outfile=None, excl_stats=False, shareY=True, fake_model='FakeData', best_fits=None):
    syst_styles = {0.00: ("black", "-"), 0.02: ("#1f77b4", "--"), 0.05: ("#ff7f0e", "-."), 0.10: ("#d62728", ":")}
    
    pairs = list(results["pair"].unique())
    fig, axes = plt.subplots(1, len(pairs), figsize=(5.0*len(pairs), 5.2), sharex=True, sharey=shareY)
    if len(pairs) == 1: axes = [axes]
    
    method_name = "Standard Shape Method" if metric == "sh" else "Normalized Falloff Method"

    for j, pair in enumerate(pairs):
        ax = axes[j]
        sub = results[results["pair"] == pair].sort_values("lumi")
        eps_v = eps_values[1:] if excl_stats else eps_values

        for eps_syst in eps_v:
            col = f"Z_{metric}_eps_{int(100*eps_syst):02d}" 
            if col not in sub.columns: continue

            color, ls = syst_styles.get(eps_syst, ("black", "-"))
            label = "stat. only" if eps_syst == 0 else rf"{int(100*eps_syst)}\% syst."
            ax.plot(sub["lumi"], sub[col], marker="o", color=color, linestyle=ls, label=label)

        ax.axhline(3.0, color='gray', linestyle='--', alpha=0.7, linewidth=1.5, label=r"$Z = 3\sigma$")
        ax.axhline(5.0, color='gray', linestyle=':', alpha=0.7, linewidth=1.5, label=r"$Z = 5\sigma$")

        bsm_name = pair.split(" vs ")[-1] if " vs " in pair else pair
        title_str = format_model_label(pair)
        
        mass_str = get_mass_label_from_fits(bsm_name, best_fits)
        if mass_str:
            title_str += f"\n[{mass_str}]"
            
        ax.set_title(title_str)
        if j == 0 or not shareY:
            ax.set_ylabel(r"Separation Significance $Z$")

        ax.set_xlabel(rf"Integrated Luminosity $\mathcal{{L}}$ [fb$^{{-1}}$]")
        ax.set_ylim(bottom=0) 
        beautify_axis(ax, grid=True) 

    # Bulletproof Spacing
    plt.tight_layout(rect=[0, 0, 1, 0.86])

    handles, labels_ = axes[-1].get_legend_handles_labels()
    by_label = dict(zip(labels_, handles))
    fig.legend(by_label.values(), by_label.keys(), loc="center", ncol=3, frameon=False, bbox_to_anchor=(0.5, 0.88))
    fig.suptitle(method_name + f' [Fake Data Baseline: {format_model_label(fake_model)}]' , fontsize=16, y=0.98)

    if outfile:
        fig.savefig(outfile, bbox_inches="tight", dpi=300)
    plt.show()


def plot_ratio_pairwise(results, mcut_max, eps_values, outfile=None, best_fits=None):
    eps_styles = {0.0: ('-', 'D'), 0.02: ("-.", "o"), 0.05: ("--", "s"), 0.10: (":", "^")}
    pairs = list(results["pair"].unique())
    upper_lim = f"{mcut_max}" if mcut_max is not None else r"\infty"

    fig, axes = plt.subplots(1, len(pairs), figsize=(5.2 * len(pairs), 5.2), sharey=True)
    if len(pairs) == 1: axes = [axes]

    for j, (ax, pair) in enumerate(zip(axes, pairs)):
        sub_pair = results[results["pair"] == pair].sort_values("mcut")
        
        for eps in eps_values:
            fa_col = f"Z_fa_eps_{int(100*eps):02d}"
            sh_col = f"Z_sh_eps_{int(100*eps):02d}"
            if fa_col not in sub_pair.columns or sh_col not in sub_pair.columns: continue
            
            with np.errstate(divide='ignore', invalid='ignore'):
                ratio = np.where(sub_pair[sh_col] > 0, sub_pair[fa_col] / sub_pair[sh_col], np.nan)
            
            ls, mk = eps_styles.get(eps, ('-', 'o'))
            ax.plot(sub_pair["mcut"], ratio, linestyle=ls, marker=mk, color=plt.cm.tab10(j), label=rf"${int(100*eps)}\%$ syst.")

        ax.axhline(1.0, color="black", linestyle="--", linewidth=1.0)
        
        bsm_name = pair.split(" vs ")[-1] if " vs " in pair else pair
        title_str = format_model_label(pair)
        
        mass_str = get_mass_label_from_fits(bsm_name, best_fits)
        if mass_str:
            title_str += f"\n[{mass_str}]"
            
        ax.set_title(title_str)
        ax.set_xlabel(rf"$m_{{t\bar t}}^{{\min}}$ [$m_{{t\bar t}}^{{\max}}={upper_lim}$] [GeV]")
        beautify_axis(ax, grid=True)

    axes[0].set_ylabel(rf"Improvement Ratio ($Z_{{\rm falloff}}/Z_{{\rm shape}}$)")
    
    # Compress slightly to ensure the title fits
    plt.tight_layout(rect=[0, 0, 1, 0.90])
    axes[-1].legend(loc="best")

    if outfile:
        fig.savefig(outfile, bbox_inches="tight", dpi=300)
    plt.show()


def plot_ratio_pairwise_lumi(results, target_mcut, eps_values, outfile=None, best_fits=None):
    eps_styles = {0.0: ('-', 'D'), 0.02: ("-.", "o"), 0.05: ("--", "s"), 0.10: (":", "^")}
    pairs = list(results["pair"].unique())

    fig, axes = plt.subplots(1, len(pairs), figsize=(5.2 * len(pairs), 5.2), sharey=True)
    if len(pairs) == 1: axes = [axes]

    for j, (ax, pair) in enumerate(zip(axes, pairs)):
        sub_pair = results[results["pair"] == pair].sort_values("lumi")
        
        for eps in eps_values:
            fa_col = f"Z_fa_eps_{int(100*eps):02d}"
            sh_col = f"Z_sh_eps_{int(100*eps):02d}"
            if fa_col not in sub_pair.columns or sh_col not in sub_pair.columns: continue
            
            with np.errstate(divide='ignore', invalid='ignore'):
                ratio = np.where(sub_pair[sh_col] > 0, sub_pair[fa_col] / sub_pair[sh_col], np.nan)
            
            ls, mk = eps_styles.get(eps, ('-', 'o'))
            ax.plot(sub_pair["lumi"], ratio, linestyle=ls, marker=mk, color=plt.cm.tab10(j), label=rf"${int(100*eps)}\%$ syst.")

        ax.axhline(1.0, color="black", linestyle="--", linewidth=1.0)
        
        bsm_name = pair.split(" vs ")[-1] if " vs " in pair else pair
        title_str = format_model_label(pair)
        
        mass_str = get_mass_label_from_fits(bsm_name, best_fits)
        if mass_str:
            title_str += f"\n[{mass_str}]"
            
        ax.set_title(title_str)
        ax.set_xlabel(rf"Integrated Luminosity $\mathcal{{L}}$ [fb$^{{-1}}$]")
        beautify_axis(ax, grid=True)

    axes[0].set_ylabel(rf"Improvement Ratio ($Z_{{\rm falloff}}/Z_{{\rm shape}}$)")
    
    # Compress slightly to ensure the title fits
    plt.tight_layout(rect=[0, 0, 1, 0.90])
    axes[-1].legend(loc="best")

    if outfile:
        fig.savefig(outfile, bbox_inches="tight", dpi=300)
    plt.show()

# ============================================================
# Standalone Ratio Significance vs Lumi Scan (The Grid Plot)
# ============================================================

def plot_ratio_significance_vs_lumi(df_sm, df_bsm, 
                                    target_models=["Scalar", "VLF", "Zprime"],
                                    var="m_tt", 
                                    lums=np.array([300, 500, 1000, 1500, 2000, 2500, 3000]),
                                    sys_err_list=[0.0, 0.02, 0.05, 0.10],
                                    rng=(1500, 4500), 
                                    peak_search_rng=(1500, 2500),
                                    asimov_model='FakeData',
                                    n_bp=18, n_ap=27,
                                    best_fits=None):
    
    results = {model: {sys: [] for sys in sys_err_list} for model in target_models}
    
    def get_cols(df):
        l_col = "label" if "label" in df.columns else "model"
        w_col = "weight" if "weight" in df.columns else "w_norm"
        return l_col, w_col

    lbl_sm, wgt_sm = get_cols(df_sm)
    df_sm_clean = df_sm[[lbl_sm, var, wgt_sm]].replace([np.inf, -np.inf], np.nan).dropna()
    x_sm = df_sm_clean[var].values

    lbl_bsm, wgt_bsm = get_cols(df_bsm)
    df_bsm_clean = df_bsm[[lbl_bsm, var, wgt_bsm]].replace([np.inf, -np.inf], np.nan).dropna()

    bin_edges = np.arange(rng[0], rng[1] + 100, 100)
    bin_centers_full = bin_edges[:-1] + np.diff(bin_edges)/2

    for lum in lums:
        w_sm = df_sm_clean[wgt_sm].values * lum * 1000.0
        h_sm, _ = np.histogram(x_sm, bins=bin_edges, weights=w_sm)
        var_sm, _ = np.histogram(x_sm, bins=bin_edges, weights=w_sm**2) 

        raw_signals = {}
        for sig in [asimov_model] + target_models:
            sig_df = df_bsm_clean[df_bsm_clean[lbl_bsm].astype(str) == sig]
            if not sig_df.empty:
                x_sig = sig_df[var].values
                w_sig = sig_df[wgt_bsm].values * lum * 1000.0
                h_sig, _ = np.histogram(x_sig, bins=bin_edges, weights=w_sig)
                v_sig, _ = np.histogram(x_sig, bins=bin_edges, weights=w_sig**2)
                raw_signals[sig] = {'h_sig': h_sig, 'v_sig': v_sig}

        for sys_err in sys_err_list:
            hypotheses = {}
            for sig, data in raw_signals.items():
                h_tot = h_sm + data['h_sig']
                err_tot = np.sqrt(var_sm + data['v_sig'] + (sys_err * h_sm)**2)
                hypotheses[sig] = {'h': h_tot, 'err': err_tot}

            h_asimov = hypotheses[asimov_model]['h']
            excess_ratio = np.divide(h_asimov, h_sm, out=np.zeros_like(h_asimov), where=h_sm > 0)

            range_mask = (bin_centers_full >= peak_search_rng[0]) & (bin_centers_full <= peak_search_rng[1])
            valid_mask = range_mask & (h_sm > 0)
            valid_indices = np.where(valid_mask)[0]
            
            b_peak = valid_indices[np.argmax(excess_ratio[valid_indices])]

            start_idx = max(0, b_peak - n_bp)
            end_idx = min(len(bin_edges)-1, b_peak + n_ap)
            peak_local_idx = b_peak - start_idx
            
            ratios_dict = {}
            for name, data in hypotheses.items():
                h, herr = data['h'], data['err']
                aux, err = [], []
                for j in range(start_idx, end_idx):
                    A, B = h[j], h[b_peak]
                    errA, errB = herr[j], herr[b_peak]
                    val = A / B if B > 0 else 0
                    aux.append(val)
                    safe_err = val * np.sqrt((errA / A)**2 + (errB / B)**2) if (A > 0 and B > 0) else 0.0
                    err.append(safe_err)
                ratios_dict[name] = {'r': np.array(aux), 'err': np.array(err)}

            r_A = ratios_dict[asimov_model]['r']
            stats_mask = np.arange(len(r_A)) != peak_local_idx
            valid_r_A = r_A[stats_mask]
            N_eval = len(valid_r_A)

            for model in target_models:
                r_B = ratios_dict[model]['r'][stats_mask]
                n_B = hypotheses[model]['h'][start_idx:end_idx][stats_mask]
                n_peak_B = hypotheses[model]['h'][b_peak]

                n_ref = n_B
                n_peak_ref = n_peak_B
                
                C_ref = np.zeros((N_eval, N_eval))
                eps = sys_err
                peak_var_term = (1.0 + (eps**2) * n_peak_ref) / n_peak_ref if n_peak_ref > 0 else 0.0

                for i in range(N_eval):
                    for j in range(N_eval):
                        if i == j:
                            bin_var_term = (1.0 + (eps**2) * n_ref[i]) / n_ref[i] if n_ref[i] > 0 else 0.0
                            C_ref[i, j] = (r_B[i]**2) * (bin_var_term + peak_var_term)
                        else:
                            C_ref[i, j] = r_B[i] * r_B[j] * peak_var_term

                try:
                    C_inv = np.linalg.inv(C_ref)
                except np.linalg.LinAlgError:
                    C_inv = np.diag(1.0 / np.diag(C_ref))

                delta_r = valid_r_A - r_B
                q_A = delta_r.T @ C_inv @ delta_r
                Z_score = max(np.sqrt(q_A), 0.0)
                
                results[model][sys_err].append(Z_score)


    fig, axes = plt.subplots(1, 3, figsize=(16, 5.5), sharey=False)
    
    style_map = {
        0.0:  {'c': 'black',   'ls': '-',  'lbl': 'stat. only'},
        0.02: {'c': '#1f77b4', 'ls': '--', 'lbl': '2\% syst.'},
        0.05: {'c': '#ff7f0e', 'ls': '-.', 'lbl': '5\% syst.'},
        0.10: {'c': '#d62728', 'ls': ':',  'lbl': '10\% syst.'}
    }

    for i, model in enumerate(target_models):
        ax = axes[i]
        for sys_err in sys_err_list:
            st = style_map[sys_err]
            ax.plot(lums, results[model][sys_err], color=st['c'], linestyle=st['ls'], 
                    linewidth=2.5, marker='o', markersize=5, label=st['lbl'])

        ax.axhline(3.0, color='gray', linestyle='--', alpha=0.7, linewidth=1.8, label='$Z=3\sigma$')
        ax.axhline(5.0, color='gray', linestyle=':', alpha=0.7, linewidth=1.8, label='$Z=5\sigma$')

        title_str = f"Fake Data vs {format_model_label(model)}"
        mass_str = get_mass_label_from_fits(model, best_fits)
        if mass_str:
            title_str += f"\n[{mass_str}]"

        ax.set_title(title_str, fontsize=15, pad=10)
        ax.set_xlabel(r'Integrated Luminosity $\mathcal{L}$ [fb$^{-1}$]', fontsize=14, labelpad=8)
        ax.set_ylabel(r'Separation Significance $Z$', fontsize=14)
        
        ax.grid(True, alpha=0.3)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.tick_params(axis='both', labelsize=12)

    plt.tight_layout(rect=[0, 0, 1, 0.86]) 

    handles, labels = axes[-1].get_legend_handles_labels()
    fig.legend(handles, labels, loc='center', bbox_to_anchor=(0.5, 0.88), ncol=3, fontsize=12, frameon=False)
    fig.suptitle('Peak Ratio Method [Fake Data Baseline: Scalar]', fontsize=18, y=0.98)

    plt.savefig('Ratio_Method_Significance_vs_Lumi.pdf', bbox_inches='tight', dpi=300)
    plt.show()