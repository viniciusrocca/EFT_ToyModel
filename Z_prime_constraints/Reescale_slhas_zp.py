import os
import numpy as np
import glob

# ---------------------------------------------------------
# 1. Configuration & Parameters
# ---------------------------------------------------------
# 13 generated mass points
masses = np.arange(2000.0, 5100.0, 100.0).tolist()

# The contour slices for total width (0.5% up to 3%)
width_fractions = [0.005, 0.010, 0.015, 0.020, 0.025, 0.030, 0.035]

# Cross section maximum value
max_xsec_limit = 15.0 # pb

# --- REFERENCE RUN PARAMETERS ---
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

    # Extract the reference cross-section to evaluate the 15 pb limit mathematically
    ref_xsec = 0.0
    for line in lines:
        if "ufo2slha" in line:
            parts = line.split()
            ref_xsec = float(parts[6])
            break
            
    if ref_xsec == 0.0:
        print(f"Error: Could not find cross-section in {ref_slha_path}")
        return 0

    points_generated = 0
    
    for w_frac in width_fractions:
        constraint_val = w_frac * 4 * np.pi
        max_gq = np.sqrt(constraint_val / 2.0)
        
        # Set the scan values
        #gq_values = np.linspace(1e-2, max_gq - 0.005, 40)
        gq_values = np.geomspace(1e-5, max_gq - 0.005, 60)
        
        for gq in gq_values:
            xsec_scale = (gq**2) / (ref_gq**2)
            new_xsec = ref_xsec * xsec_scale
            
            # --- 15 pb maximum limit---
            if new_xsec > max_xsec_limit:
                continue 
            
            gt = np.sqrt(constraint_val - 2 * (gq**2))
            width_ratio = ref_width_fraction / w_frac
            
            br_scale_top = (gt**2 / ref_gt**2) * width_ratio
            br_scale_light = (gq**2 / ref_gq**2) * width_ratio
            
            new_lines = []
            in_zp_decay = False
            
            for line in lines:
                # Update the Total Width
                if line.startswith("DECAY  5000001"):
                    in_zp_decay = True
                    new_total_width = mass * w_frac
                    new_lines.append(f"DECAY  5000001   {new_total_width:.6e} #  wy1\n")
                    continue

                elif line.startswith("DECAY "):
                    in_zp_decay = False
                    
                # Update the Branching Ratios
                if in_zp_decay and len(line.strip()) > 0 and not line.startswith("#"):
                    parts = line.split()
                    if len(parts) >= 4:
                        old_br = float(parts[0])
                        pids = [int(parts[2]), int(parts[3])]
                        
                        if 6 in pids and -6 in pids:
                            new_br = old_br * br_scale_top
                        elif any(abs(p) in [1, 2, 3, 4, 5] for p in pids):
                            new_br = old_br * br_scale_light
                        else:
                            new_br = old_br 
                            
                        line = line.replace(parts[0], f"{new_br:.6e}", 1)

                # Update Cross-Section Error
                elif line.startswith("XSECTION"):
                    parts = line.split()
                    old_err = float(parts[-1]) 
                    new_err = old_err * xsec_scale
                    line = line.replace(parts[-1], f"{new_err:.3e}\n")

                # 4. Update Nominal Cross-Section
                elif "ufo2slha" in line:
                    line = f"  0  0  0  0  0  0  {new_xsec:.4e} ufo2slha 1.0\n"
                    
                new_lines.append(line)
                
            width_pct = int(w_frac * 1000) 
            out_name = f"Zprime_W{width_pct:02d}_m{int(mass)}_gq{gq:.4f}_gt{gt:.4f}.slha"
            
            with open(os.path.join(output_dir, out_name), 'w') as f:
                f.writelines(new_lines)
            
            points_generated += 1
            
    return points_generated

# ---------------------------------------------------------
#  Execution 
# ---------------------------------------------------------

total_points = 0
for mass in masses:
    # Look for ANY file in the input directory that contains the mass integer and ends with .slha
    search_pattern = os.path.join(input_dir, f"*{int(mass)}*.slha")
    matching_files = glob.glob(search_pattern)
    
    if not matching_files:
        print(f"File not found: No files matching *{int(mass)}*.slha in {input_dir}. Skipping...")
        continue
        
    # Grab the first file that matches the pattern
    ref_file = matching_files[0] 
    
    print(f"Processing {os.path.basename(ref_file)}...")
    total_points += rescale_slha(ref_file, mass, output_dir)

print("-" * 50)
print(f"DONE! Successfully generated {total_points} rescaled SLHA files.")