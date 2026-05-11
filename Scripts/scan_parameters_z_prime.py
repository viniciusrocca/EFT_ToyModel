import numpy as np

# ---------------------------------------------------------
# Mass Grid
# ---------------------------------------------------------
masses = np.arange(1500.0, 5100.0, 100.0).tolist()

# ---------------------------------------------------------
#  Coupling Grid
# ---------------------------------------------------------
#  1% width benchmark constraint: 2 * g_q^2 + g_t^2 = 0.01 * 4 * pi
target_width_fraction = 0.01
constraint_val = target_width_fraction * 4 * np.pi

coupling_pairs = []

# Using 40 points 
gq_values = np.linspace(0.01, 0.245, 1)

for gq in gq_values:
    # Calculate dependent g_t
    gt = np.sqrt(constraint_val - 2 * (gq**2))
    
    # Keeping 4 decimal places for precision in the MadGraph parameter card
    coupling_pairs.append((float(round(gq, 4)), float(round(gt, 4))))

# Format the lists into the $loop{...} syntax
mass_loop_str = f"$loop{{{masses}}}"
coup_loop_str = f"$loop{{{coupling_pairs}}}"

# ---------------------------------------------------------
# Construct the .ini File Content
# ---------------------------------------------------------
ini_content = f"""[options]
cleanOutput = True
runMadGraph = True
runConvertSLHA = False
runPythia = False
runDelphes = False
runMadSpin = False
runFixCollier = False
ncpu = 2
ncore = 12

[AuxPars]
mZp_scan = {mass_loop_str}
coupling_scan = {coup_loop_str}

[MadGraphPars]
# MG5 Cards:
proccard = /home/vinicius/EFT_ToyModel/processFolders/z_prime/pp2Zprime/Cards/proc_card.dat
paramcard = /home/vinicius/EFT_ToyModel/processFolders/z_prime/pp2Zprime/Cards/param_card.dat
runcard = /home/vinicius/EFT_ToyModel/processFolders/z_prime/pp2Zprime/Cards/run_card.dat
processFolder = /home/vinicius/EFT_ToyModel/processFolders/z_prime/pp2Zprime

[MadGraphSet]
nevents = 2000
mt = 172.5

# Assign the looped variables to MadGraph parameters
my1 = ${{AuxPars:mZp_scan}}
gvd11 = ${{AuxPars:coupling_scan}}[0]
gvu11 = ${{AuxPars:coupling_scan}}[0]
gvu33 = ${{AuxPars:coupling_scan}}[1]

wy1 = 'auto'

fixed_order = OFF
run_tag = "Zprime_1pct_m%1.0f_gq%1.3f_gt%1.3f" %(${{my1}}, ${{gvu11}}, ${{gvu33}})
"""

# ---------------------------------------------------------
# Write to File
# ---------------------------------------------------------
output_filename = "scan_parameters_Zprime.ini"
with open(output_filename, "w") as f:
    f.write(ini_content)

print(f"Successfully generated {output_filename}")