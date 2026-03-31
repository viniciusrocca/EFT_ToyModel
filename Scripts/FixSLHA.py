import os
import glob

# Set this to the folder containing your SLHA files
folder_path = "./../processFolders/Slhas" 

# Find all SLHA files in the directory
slha_files = glob.glob(os.path.join(folder_path, "*.slha"))
print(f"Found {len(slha_files)} SLHA files. Applying correct Z2 parities...")

for filepath in slha_files:
    with open(filepath, 'r') as f:
        lines = f.readlines()

    new_lines = []
    current_pid = None

    for line in lines:
        new_lines.append(line)
        
        # 1. Identify which particle block we are currently in
        if line.strip().startswith("BLOCK QNUMBERS"):
            parts = line.strip().split()
            try:
                current_pid = int(parts[2]) # Extract the PID (e.g., 5000006)
            except (IndexError, ValueError):
                current_pid = None
                
        # 2. When we hit parameter '4' (the last standard line of the block)
        elif current_pid is not None and line.strip().startswith("4 "):
            
            # Apply 11 1 for BSM particles, 11 0 for SM particles
            if abs(current_pid) in [5000006, 5000022]:
                new_lines.append("      11 1 # z2 parity\n")
            else:
                new_lines.append("      11 0 # z2 parity\n")
            
            # Reset the PID so we don't accidentally add it twice
            current_pid = None 

    # Overwrite the file with the perfectly formatted lines
    with open(filepath, 'w') as f:
        f.writelines(new_lines)

print("✅ Done! Added '11 1' for 5000006/5000022 and '11 0' for the rest.")