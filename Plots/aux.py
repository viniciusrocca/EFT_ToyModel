import glob, os, pyslha
import numpy as np
import itertools
from scipy.interpolate import  griddata
from matplotlib import pyplot as plt
import tempfile
import pylhe
import gzip
import sys
import argparse
from pathlib import Path

def getLHEevents(fpath):
    """
    Reads a set of LHE files and returns a dictionary with the file labels as keys
    and the PyLHE Events object as values.
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
    events = list(pylhe.read_lhe_with_attributes(fixedFile))
    nevents = pylhe.read_num_events(fixedFile)
    os.remove(fixedFile)
    return nevents,events

def getDistributions(filename):

    nevents,events = getLHEevents(filename)
    pT1 = []
    pT2 = []
    mTT = []
    deltaPhi = []
    weights = []
    pT = []
    for ev in events:
        w = ev.eventinfo.weight/nevents
        weights.append(w)
        for ptc in ev.particles:
            if abs(ptc.id) != 6: continue
            if ptc.id == 6:
                pA = np.array([ptc.px,ptc.py,ptc.pz,ptc.e])
                pT.append(np.linalg.norm(pA[0:2]))
            else:
                pB = np.array([ptc.px,ptc.py,ptc.pz,ptc.e])

        pT1.append(max(np.linalg.norm(pA[0:2]),np.linalg.norm(pB[0:2])))
        pT2.append(min(np.linalg.norm(pA[0:2]),np.linalg.norm(pB[0:2])))
        mTT.append(np.sqrt((pA[-1]+pB[-1])**2-np.linalg.norm(pA[0:3]+pB[0:3])**2))
        deltaPhi.append(getDeltaPhi(pA,pB))
    
    dists = {'mTT' : np.array(mTT), 'pT1' : np.array(pT1), 'pT2' : np.array(pT2), 
         'deltaPhi' : np.array(deltaPhi), 'weights' : np.array(weights), 'pT': np.array(pT),
         'nevents' : nevents}

    return dists

def getInfoSummary(f):
    # Finding the the summary.txt file in the same directory as the input file 'f'
    summary_path = os.path.join(os.path.dirname(f), 'summary.txt')
        
    with open(summary_path, 'r') as summary_file:
        for line in summary_file:
            clean_line = line.strip()
                
            # Getting process
            if clean_line.startswith('Process'):
                process = clean_line.split('Process', 1)[1].strip()
                process =  process.split('[')[0].strip()

             # Getting cross section
            if clean_line.startswith('Total cross section:'):
                value_str = clean_line.split(':', 1)[1].strip().split()[0]
                cross_section = float(value_str)
                
            
    return {'process': process, 'cross_section': cross_section}


def getInfo(f,nlo = False,labelsDict=None):


    if labelsDict is None:
        labelsDict = {'UV_BSM_ToyModel_NLO-UFO' : '1-loop', 'Top-EFTfull-UFO' : 'EFT', 
                      'SMS-stop-UFO' : 'SM', 'SMS-stop-NLO_SMQCD-UFO' : 'SM',
              'g g > t t~' : r'$g g \to t \bar{t}$', 'g g > t~ t' : r'$g g \to t \bar{t} $',
              'q q > t t~' : r'$q q \to t \bar{t}$', 'q q > t~ t' : r'$q q \to t \bar{t}$',
              'p p > t t~' : r'$p p \to t \bar{t}$', 'p p > t~ t' : r'$p p \to t \bar{t}$'
             }
    
    banner = list(glob.glob(os.path.join(os.path.dirname(f),'*banner*')))[0]
    with open(banner,'r') as bannerF:
        bannerData = bannerF.read()

    if nlo == True:

        #Extracting the summary info
        summary_info = getInfoSummary(f)

        #Getting the process
        proc = summary_info.get('process')
        if proc in labelsDict:
            proc = labelsDict[proc]

        #Getting cross section
        xsec = summary_info.get('cross_section')

        #Need a fix
        nEvents = 'Fail' #Just for now
        model = '1-loop' #Just for now
    else:
        # Get process data:
        processData = bannerData.split('<MGProcCard>')[1].split('</MGProcCard>')[0]

        
        # Get model
        model = processData.split('Begin MODEL')[1].split('End   MODEL')[0]
        model = model.split('\n')[1].strip()
        if model in labelsDict:
            model = labelsDict[model]
        # Get process
        proc = processData.split('Begin PROCESS')[1].split('End PROCESS')[0]
        proc = proc.split('\n')[1].split('#')[0].strip()
        if proc in labelsDict:
            proc = labelsDict[proc]

        # Get event data:
        eventData = bannerData.split('<MGGenerationInfo>')[1].split('</MGGenerationInfo>')[0]
        nEvents = eval(eventData.split('\n')[1].split(':')[1].strip())
        xsec = eval(eventData.split('\n')[2].split(':')[1].strip())
    
    # Get parameters data:
    parsData = bannerData.split('<slha>')[1].split('</slha>')[0]
    parsSLHA = pyslha.readSLHA(parsData)
    
    
    mT  = parsSLHA.blocks['MASS'][6]
    if 5000022 in parsSLHA.blocks['MASS'] and nlo == True:
        mSDM = parsSLHA.blocks['MASS'][5000022]
        mPsiT = parsSLHA.blocks['MASS'][5000006]        
        yDM = list(parsSLHA.blocks['FRBLOCK'].values())[0]
    elif model == 'EFT':
        pars = list(parsSLHA.blocks['FRBLOCK'].values())
        mSDM = pars[3]
        mPsiT = pars[4]     
        yDM = pars[0]
    else:
        mSDM = 0.0
        mPsiT = 0.0
        yDM = 0.0

    if yDM == 0.0:
        model = 'SM'


    

    fileInfo = {'model' : model, 'process' : proc, '(mSDM,mPsiT,mT,yDM)' : (mSDM,mPsiT,mT,yDM),
               'xsec (pb)' : xsec, 'nevents' : nEvents}
    
    return fileInfo

def getDeltaPhi(pA,pB):
    """Calculates the differentce of the azimuthal angle phi for A and B"""
    phi_diff = transversePhi(pA) - transversePhi(pB)
    while phi_diff <= -np.pi: phi_diff += 2 * np.pi
    while phi_diff > np.pi: phi_diff -= 2 * np.pi
    return abs(phi_diff)
    

def transversePhi(p):
    """Calculates the azimuthal angle phi from a momentum vector [px, py, pz, E]."""
    if p[0] == 0.0 and p[1] == 0.0:
        return print('Not defined')
    elif p[0] == 0 and p[1] > 0:
        return np.pi/2
    elif p[0] == 0 and p[1] < 0:
        return -np.pi/2
    elif p[0] < 0 and p[1] >= 0:
        return np.arctan(p[1]/p[0]) + np.pi
    elif p[0] < 0 and p[1] < 0:
        return np.arctan(p[1]/p[0]) - np.pi
    else:
        return np.arctan(p[1]/p[0])
    

def get_params_from_filename(run_dir):
    """Parses a banner's filename containing '_interference_' to find parameters."""
    # Find banner file using glob.glob
    banner_files = glob.glob(os.path.join(run_dir, '*banner.txt'))
    print(run_dir)
    print(banner_files)
    if not banner_files:
        return

    banner_file = banner_files[0]
    # Get filename without extension using os.path
    basename = os.path.basename(banner_file)
    stem = os.path.splitext(basename)[0]
    
    parts = stem.split('_')
    idx = parts.index('banner')
    m1, m2 = parts[idx - 2], parts[idx - 1]
    return f"mPsiT_{m1}_mSDM_{m2}", float(m1), float(m2)

def AddInfoToDistributions(distributions, args, mPsiT, mSDM, info):
    """Adds the model name, process and mass parameters to the final dictionary"""
    converter_dict = {'TopEFT': 'EFT', 'UV_BSM': '1-loop UV', 'sm':'SM',
                      'qq2ttbar_gs4_ydm2': r'$q q \to t \bar{t}$', 'gg2ttbar_gs4_ydm2': r'$g g \to t \bar{t}$',
                      'pp2ttbar_gs4_ydm2': r'$p p \to t \bar{t}$ ', 'qq2ttbar_gs6': r'$q q \to t \bar{t}$', 'gg2ttbar_gs6': r'$g g \to t \bar{t}$',
                      'pp2ttbar_gs6': r'$p p \to t \bar{t}$', 'qq2ttbar_gs4': r'$q q \to t \bar{t}$', 'gg2ttbar_gs4': r'$g g \to t \bar{t}$',
                      'pp2ttbar_gs4': r'$p p \to t \bar{t}$', 'gs4': r'$g_s^4$', 'gs6': r'$g_s^6$', 'ydm2': r'$y_{DM}^2$'}
    
    #Add new keys with the new information
    distributions['model'] = converter_dict[args.model]
    distributions['process'] = converter_dict[args.process]
    distributions['mass_params'] = (mPsiT,mSDM)
    distributions['ydm'] = info['(mSDM,mPsiT,mT,yDM)'][-1]
    distributions['xsec (pb)'] = info['xsec (pb)']
    

    #Extract the coupling order
    parts = args.process.split('_')
    parts = parts[1:]
    for i,p in enumerate(parts):
        parts[i] = converter_dict[p]

    distributions['cp_order'] = parts[1:]
    
    return distributions


def main():
    #Defining the inputs
    parser = argparse.ArgumentParser(description="Process LHE files for a specific model and process.")
    parser.add_argument("model", type=str, help="The model name (e.g., TopEFT, UV_BSM, sm).")
    parser.add_argument("process", type=str, help="The process name (e.g., qq2ttbar_gs4_ydm2).")
    parser.add_argument("output_path", type=str, help="The full path for the output .npz file (e.g., /home/user/distributions).")
    args = parser.parse_args()

    #Building the event folder of the specified process
    process_dir = Path(f"/home/vinicius/EFT_ToyModel/processFolders/{args.model}/{args.process}/Events")
    if not process_dir.exists():
        print(f"[Error] Directory not found: {process_dir}"); return

    lhe_files = sorted(list(process_dir.glob('run_*/*events.lhe.gz')))
    if not lhe_files:
        print(f"[Error] No 'run_*/*events.lhe.gz' files found in {process_dir}"); return

    print(f"Found {len(lhe_files)} run files for model '{args.model}' and process '{args.process}'.")

   # Create an output directory named after the process 
    output_dir = Path(f"{args.output_path}/{args.model}/{args.process}")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Find all individual run directories
    run_dirs = sorted([p.parent for p in process_dir.glob('run_*/*events.lhe.gz')])
    if not run_dirs:
        print(f"[Error] No run directories found in {process_dir}"); return

    print(f"Found {len(run_dirs)} runs to process for '{args.process}'. Storing results in '{output_dir}'.")

    # Loop over each individual run directory 
    for run_dir in run_dirs:
        
        # Get the specific parameters for this run
        identifier_string, mPsiT, mSDM = get_params_from_filename(run_dir)
        
        # Construct a unique output filename for this run
        output_filename = f"{identifier_string}.npz"
        output_path = output_dir / output_filename
        
        # Process the LHE file for this run only
        if args.model == 'UV_BSM':
            lhe_file_path = next(run_dir.glob('events.lhe.gz'))
            info = getInfo(lhe_file_path, nlo = True)
        else:
            lhe_file_path = next(run_dir.glob('unweighted_events.lhe.gz'))
            info = getInfo(lhe_file_path)
        #events = getLHEevents(lhe_file_path)

        #Computing the distributions
        distributions = getDistributions(lhe_file_path)

        if distributions and 'mTT' in distributions and distributions['mTT'].size > 0:
        
            #Adding lables
            distributions = AddInfoToDistributions(distributions, args, mPsiT, mSDM, info)
            
            #Saving the file
            np.savez_compressed(output_path, **distributions)
            print(f"Saved results to: {output_path}")
        
        else:
            # If the check above fails
            print("  -> No valid events found. No output generated.")

if __name__ == "__main__":
    main()


