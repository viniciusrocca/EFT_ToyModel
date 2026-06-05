import os
import numpy as np
import glob

# ---------------------------------------------------------
# Configuration & Parameters
# ---------------------------------------------------------
masses = np.arange(800.0, 5100.0, 100.0).tolist()
width_fractions = [0.005, 0.010, 0.02]

# --- Scan limits ---
min_S_target = 1e-5 # pb
max_S_target = 10.0 # pb
num_points = 70

# --- Reference run parameters---
ref_width_fraction = 0.010
ref_gq = 1.000000e-02
ref_gt = np.sqrt((ref_width_fraction * 4 * np.pi) - 2 * (ref_gq**2)) 

# Folders
input_dir = "/home/vinicius/EFT_ToyModel/processFolders/Zp_SLHAs_ref/"
output_dir = "/home/vinicius/EFT_ToyModel/processFolders/Zp_SLHAs/"
os.makedirs(output_dir, exist_ok=True)

# ---------------------------------------------------------
# Rescaling Logic 
# ---------------------------------------------------------
def rescale_slha(ref_slha_path, mass, output_dir):
    try:
        with open(ref_slha_path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File not found: {ref_slha_path}. Skipping...")
        return 0

    ref_xsec = 0.0
    ref_br_top = 0.0
    in_zp_decay = False
    
    for line in lines:
        if "ufo2slha" in line:
            parts = line.split()
            ref_xsec = float(parts[6])
            
        if line.startswith("DECAY") and "5000001" in line:
            in_zp_decay = True
            continue 
        elif line.startswith("DECAY"):
            in_zp_decay = False
            continue
            
        if in_zp_decay and not line.strip().startswith("#"):
            parts = line.split()
            if len(parts) >= 4:
                try:
                    pids = [int(parts[2]), int(parts[3])]
                    if 6 in pids and -6 in pids:
                        ref_br_top = float(parts[0])
                except ValueError:
                    pass 
            
    if ref_xsec == 0.0 or ref_br_top == 0.0:
        print(f"Error: Could not find cross-section or BR in {ref_slha_path}")
        return 0

    points_generated = 0
    
    for w_frac in width_fractions:
        constraint_val = w_frac * 4 * np.pi 
        A = (ref_xsec * ref_br_top) / ((ref_gq**2) * (ref_gt**2))
        S_max_physical = (A * (constraint_val**2)) / 8.0
        max_S_scan = min(max_S_target, S_max_physical) 
        
        num_high_points = 20  # 20 points will cover 0.05 pb up to the ceiling
        num_low_points = 50   # 50 points will cover 1e-5 pb up to 0.05 pb
        
        high_points = np.geomspace(0.05, max_S_scan, num_high_points)
        low_points = np.geomspace(min_S_target, high_points[0], num_low_points)
        
        # Merge the two grids into the final target list
        target_S_values = np.concatenate([low_points, high_points])
        
        for S in target_S_values:
            discriminant = (A * constraint_val)**2 - 8 * A * S
            if discriminant < 0: 
                discriminant = 0.0 
            
            # =========================================================
            # Calculate roots
            # =========================================================
            gq_sq_roots = [
                (2 * S) / (A * constraint_val + np.sqrt(discriminant)),
                (A * constraint_val + np.sqrt(discriminant)) / (4 * A)
            ]
            
            for idx, gq_sq in enumerate(gq_sq_roots):
                gq = np.sqrt(gq_sq)
                
                # Floating point safeguard to handle the exact 0 limit
                if 2 * gq_sq >= constraint_val:
                    gt = 0.0
                else:
                    gt = np.sqrt(constraint_val - 2 * gq_sq)
                

                if gt > gq:
                    regime = "topDom"
                else:
                    regime = "jetDom"
                
                xsec_scale = (gq**2) / (ref_gq**2)
                new_xsec = ref_xsec * xsec_scale
                
                width_ratio = ref_width_fraction / w_frac
                
                if ref_gt > 0:
                    br_scale_top = (gt**2 / ref_gt**2) * width_ratio
                else:
                    br_scale_top = 0.0
                    
                br_scale_light = (gq**2 / ref_gq**2) * width_ratio
                
                new_lines = []
                in_zp_decay = False
                
                # We define the new total width here so it can be used for partial widths
                new_total_width = mass * w_frac
                
                for line in lines:
                    # Update the Total Width
                    if line.startswith("DECAY") and "5000001" in line:
                        in_zp_decay = True
                        new_lines.append(f"DECAY 5000001   {new_total_width:.6e} #  wy1\n")
                        continue

                    # Exit the Z' Decay Block
                    elif line.startswith("DECAY"):
                        in_zp_decay = False
                        
                    # Update the Couplings in DMINPUTS
                    if "# gvd11" in line or "# gvu11" in line:
                        parts = line.split()
                        if len(parts) >= 2:
                            line = line.replace(parts[1], f"{gq:.6e}", 1)
                    elif "# gvu33" in line:
                        parts = line.split()
                        if len(parts) >= 2:
                            line = line.replace(parts[1], f"{gt:.6e}", 1)
                        
                    # Update Branching Ratios and Partial Widths
                    if in_zp_decay and not line.strip().startswith("#"):
                        parts = line.split()
                        if len(parts) >= 4:
                            try:
                                pids = [int(parts[2]), int(parts[3])]
                                if 6 in pids and -6 in pids:
                                    new_br = float(parts[0]) * br_scale_top
                                    new_partial_width = new_total_width * new_br
                                    line = f"      {new_br:.6e}   2  -6   6 # {new_partial_width:.6e}\n"
                                    
                                elif any(abs(p) in [1, 2, 3, 4, 5] for p in pids):
                                    new_br = float(parts[0]) * br_scale_light
                                    new_partial_width = new_total_width * new_br
                                    # Formats the PID spacing so it perfectly matches MadGraph's alignment
                                    line = f"      {new_br:.6e}   2  {pids[0]:>2}  {pids[1]:>2} # {new_partial_width:.6e}\n"
                            except ValueError:
                                pass 

                    # Update Cross-Section Error
                    elif line.startswith("XSECTION"):
                        parts = line.split()
                        old_err = float(parts[-1]) 
                        new_err = old_err * xsec_scale
                        line = line.replace(parts[-1], f"{new_err:.3e}\n")

                    # Update Nominal Cross-Section
                    elif "ufo2slha" in line:
                        line = f"  0  0  0  0  0  0  {new_xsec:.4e} ufo2slha 1.0\n"
                        
                    new_lines.append(line)
                    
                width_pct = int(w_frac * 1000) 
                out_name = f"Zprime_W{width_pct:02d}_m{int(mass)}_S{S:.2e}_{regime}_R{idx+1}.slha"
                
                with open(os.path.join(output_dir, out_name), 'w') as f:
                    f.writelines(new_lines)
                
                points_generated += 1
            
    return points_generated

# ---------------------------------------------------------
# Main Loop
# ---------------------------------------------------------
total_points = 0
for mass in masses:
    search_pattern = os.path.join(input_dir, f"*{int(mass)}*.slha")
    matching_files = glob.glob(search_pattern)
    
    if not matching_files:
        print(f"File not found: No files matching *{int(mass)}*.slha in {input_dir}. Skipping...")
        continue
        
    ref_file = matching_files[0] 
    
    print(f"Processing {os.path.basename(ref_file)}...")
    total_points += rescale_slha(ref_file, mass, output_dir)

print("-" * 50)
print(f"DONE! Successfully generated {total_points} rescaled SLHA files.")