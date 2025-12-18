import pandas as pd
import numpy as np

file_path = 'qq_gg_cms_top_20_001.pcl'

print(f"Loading {file_path}...")
try:
    df = pd.read_pickle(file_path)
    print("File loaded successfully.")
    
    found_problem = False
    print("\n--- Checking for 0-dimensional arrays ---")
    
    for col in df.columns:
        # We only need to check object columns (where arrays usually hide)
        if df[col].dtype == 'object':
            # Get the first non-null value to check type
            sample = df[col].iloc[0]
            
            if isinstance(sample, np.ndarray):
                print(f"[!] Column '{col}' contains NumPy arrays.")
                print(f"    Shape: {sample.shape}")
                print(f"    Example value: {sample}")
                
                if sample.ndim == 0:
                    print("    -> THIS IS A 0-D ARRAY (Unhashable!)")
                    found_problem = True
                print("-" * 30)

    if not found_problem:
        print("No 0-dimensional arrays found. The data types seem clean.")
    else:
        print("\nSummary: Found 0-d arrays. You need to clean these columns.")
        
except Exception as e:
    print(f"Could not read file: {e}")
