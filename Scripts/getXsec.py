
import glob, os, pyslha
import numpy as np
from scipy.interpolate import  griddata
from matplotlib import pyplot as plt
import tempfile
import pylhe
import gzip
import argparse
from pathlib import Path


def getXsectionFromLHE(fpath):
    """
    Reads a set of LHE files and returns a the cross section and it's error
    """

    # It is necessary to remove the < signs from the LHE files (in the generate line) before parsing with pylhe
    fixedFile = tempfile.mkstemp(suffix='.lhe')
    os.close(fixedFile[0])
    fixedFile = fixedFile[1]
    with  gzip.open(fpath,'rt') as f:
        data = f.readlines()
        with open(fixedFile,'w') as newF:
            for l in data:
                if 'generate' in l:
                    continue
                newF.write(l)
    initBlock = pylhe.read_lhe_init(fixedFile)
    initBlock = initBlock['procInfo'][0]
    os.remove(fixedFile)
    return initBlock['xSection'], initBlock['error']

def getXsectionSummary(f):
    """
    Reads a summary.txt file and returns the cross section and its error.
    """
    runDir = os.path.dirname(f)
    summary_path = os.path.join(runDir, 'summary.txt')

    if not os.path.isfile(summary_path):
        print(f'Error: No summary file found in {runDir}.')
        return -1.0, 0.0

    try:
        with open(summary_path, 'r') as summary_file:
            summaryLines = summary_file.readlines()

        # Find the line containing the cross section information
        totalXsecLine = [l for l in summaryLines if 'Total cross section' in l][0]
        
        # Handle the special "DO NOT USE" case
        if 'DO NOT USE' in totalXsecLine:
            scale_line_index = [i for i, l in enumerate(summaryLines) if 'Scale variation' in l][0]
            totalXsecLine = summaryLines[scale_line_index + 2]

        # Isolate the part of the string with the numbers (after the colon)
        if ':' in totalXsecLine:
            value_part = totalXsecLine.split(':')[1].strip()
        else: #Handles the fallback from the "DO NOT USE" case
            value_part = totalXsecLine.strip()
            
        #Split the value part into the cross section and the error
        if ' +-' in value_part:
            parts = value_part.split(' +- ')
            xsec_str = parts[0]
            err_str = parts[1].split()[0] #Take the first piece to discard 'pb'
            
            xsec = float(xsec_str)
            xsec_err = float(err_str)
        else:
            # Fallback if there is no error listed, just a value
            xsec_str = value_part.split()[0]
            xsec = float(xsec_str)
            xsec_err = 0.0

    except (IndexError, ValueError) as e:
        # This handles errors if a line isn't found or a number can't be parsed
        print(f"Warning: Could not parse summary file in {runDir}. Error: {e}")
        return -1.0, 0.0

    return xsec, xsec_err

def get_params_from_filename(run_dir):
    """Parses a banner's filename containing '_interference_' to find parameters."""
   
    try:
        banner_file_path = glob.glob(os.path.join(run_dir, '*banner.txt'))[0]
        stem = Path(banner_file_path).stem
        parts = stem.split('_')
        idx = parts.index('banner')
        m1, m2 = parts[idx - 2], parts[idx - 1]
        return float(m1), float(m2)
    except (IndexError, ValueError):
        print(f"    [Warning] Could not parse banner filename in {run_dir}.")
        return None, None

def process_run(files: str, output_file: str):
    """
    Finds all LHE files for a single job, extracts the data, and writes it to an output file.
    """
    # Find all LHE files for all runs within the specified directory
    files = os.path.join(files, 'run_*', '*events.lhe.gz')
    lhe_files = glob.glob(files)

    if not lhe_files:
        print(f"  [Info] No '*events.lhe.gz' files found in '{files}'. Skipping this process.")
        return

    print(f"  Found {len(lhe_files)} LHE files to process.")

    results = []
    for fpath in sorted(lhe_files):
        run_dir = os.path.dirname(fpath)
        
        m1, m2 = get_params_from_filename(run_dir)
        if 'UV_BSM' in files:
            xsec, xsec_err = getXsectionSummary(fpath)
        else:
            xsec, xsec_err = getXsectionFromLHE(fpath)

        if m1 is not None and xsec is not None:
            results.append({'m1': m1, 'm2': m2, 'xsec': xsec, 'xsec_err': xsec_err})

    # Ensure the output directory exists
    output_dir_path = os.path.dirname(output_file)
    if output_dir_path:
        os.makedirs(output_dir_path, exist_ok=True)

    # Write all collected results to the output file
    with open(output_file, 'w') as f_out:
        f_out.write("# mPsiT, mSDM, CrossSection_pb, Error_pb\n")
        for res in sorted(results, key=lambda r: (r['m1'], r['m2'])) : # Sort by mass
            f_out.write(f"{res['m1']}, {res['m2']}, {res['xsec']:.6e}, {res['xsec_err']:.6e}\n")

    print(f"Successfully saved {len(results)} results to '{output_file}'.")


def main():
    """
    Main function that reads a process file and calls process_run for each entry.
    """
    parser = argparse.ArgumentParser(description="Extract cross-sections from a list of process in a text file.")
    parser.add_argument("process_file", type=str, help="Path to a .txt file with jobs (format: model,process,search_dir,output_file).")
    args = parser.parse_args()

    if not os.path.exists(args.process_file):
        print(f"[Error] Process file not found at '{args.process_file}'")
        return

    with open(args.process_file, 'r') as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith('#'): # Skip empty lines and comments
                continue

            try:
                # Unpack the four comma-separated values
                model, process, search_dir, output_file = [item.strip() for item in line.split(',')]
                print(f"\n--- Starting process run {i}: {model}/{process} ---")
                process_run(search_dir, output_file)
            except ValueError:
                print(f"[Warning] Skipping malformed line {i}: '{line}' (expected 4 comma-separated values)")
                continue
            except Exception as e:
                # This will catch any other unexpected errors from inside process_run
                print(f"[ERROR] Job {i} ({model}/{process}) failed with an unexpected error: {e}")

if __name__ == "__main__":
    main()
