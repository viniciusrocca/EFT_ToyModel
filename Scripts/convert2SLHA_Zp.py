#!/usr/bin/env python3

import sys, os
import logging
from collections import OrderedDict
import gzip
import fnmatch

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger()

def getSLHAFile(inputLHE, output_dir=None, pidList=[5000001], mg5_path='/home/vrocca/MadGraph/MG5_aMC_v3_6_3/'):
    madgraphPath = os.path.abspath(mg5_path)
    if madgraphPath not in sys.path:
        sys.path.append(madgraphPath)
        
    try:
        from madgraph.various.banner import Banner
    except ImportError:
        logger.error(f"Could not import Banner from {madgraphPath}. Check your MG5 path.")
        return False
        
    lheFile = inputLHE   
    if not os.path.isfile(lheFile):
        return False
    
    try:
        if lheFile.endswith('.gz'):
            f = gzip.open(lheFile, 'rt')
        else: 
            f = open(lheFile, 'r')
            
        banner = Banner()
        banner.read_banner(f)
        f.close()
    except Exception as e:
        return False

    if not 'init' in banner or not 'slha' in banner:
        return False
       
    slhaData = banner['slha'] 

    # --- FIXED MASS EXTRACTION ---
    m_Zp = 0.0
    in_mass_block = False
    for line in slhaData.split('\n'):
        clean_line = line.strip().lower()
        if clean_line.startswith('block mass'):
            in_mass_block = True
            continue
        if clean_line.startswith('block ') and in_mass_block:
            in_mass_block = False
        
        if in_mass_block and clean_line and not clean_line.startswith('#'):
            parts = clean_line.split()
            if len(parts) >= 2:
                try:
                    pdg = int(parts[0])
                    # Added your Z' PID (5000001) to the search list!
                    if pdg in [32, 51, 55, 3000001, 5000001]:
                        m_Zp = float(parts[1])
                except ValueError:
                    pass
    
    if output_dir is not None:
        # --- FIXED NAMING CONVENTION ---
        m_str = str(int(m_Zp)) if m_Zp.is_integer() else str(m_Zp)
        out_filename = f"Reference_M{m_str}.slha"
            
        slhaFile = os.path.join(output_dir, out_filename)
        os.makedirs(output_dir, exist_ok=True)
    else:
        slhaFile = inputLHE[:inputLHE.rfind('.lhe')] + '.slha'
        
    logger.debug('Creating SLHA file %s' % slhaFile)

    if pidList is None or not pidList:
        slhaLines = slhaData.split('\n')  
        qnumbers = [l for l in slhaLines if 'block qnumbers' in l.lower()]
        particleLabels = {x.split('#')[1].strip() : eval(x.split('#')[0].split()[-1]) for x in qnumbers}
        
        for label, pdg in list(particleLabels.items()):
            if -pdg in particleLabels.values(): continue
            else: particleLabels[label+'~'] = -pdg    

        finalStatesDict = {}
        iproc = 0
        for l in banner['mg5proccard'].split('\n'):
            if not l or l[0] == '#': continue
            l = l.strip()
            if l[:8] == 'generate': l = l[l.find('generate')+8:]
            elif l[:11] == 'add process': l = l[l.find('add process')+11:]
            else: continue

            l = l[:l.find('[')].strip()        
            finalStates = l.split('>')[1].split(',')[0].strip().split()
            finalStates = [particleLabels[f] if f in particleLabels else f for f in finalStates[:]]

            if not iproc in finalStatesDict:        
                finalStatesDict[iproc] = finalStates
            else:
                return False
            iproc += 1
    else:
        pidList_eval = [int(p) for p in pidList]
        finalStatesDict = {1 : sorted(pidList_eval)}

    xsecTotal = banner.get_cross()
    if xsecTotal <= 0.: return False
    
    info = banner['init'].split('\n')[0].split()
    sqrts = eval(info[2]) + eval(info[3])
    pdgInitial = list(banner.get_pdg_beam())
    processXsecs = {}
    
    for l in banner['init'].split('\n')[1:]:
        if not l.strip() or l.strip()[0] == '<': continue
        vals = [eval(x) for x in l.split()]
        xsec, xsecErr, _, procID = vals
        if not procID in finalStatesDict: return False
        if not procID in processXsecs:
            processXsecs[procID] = {'xsec (pb)' : xsec, 'xsecErr (pb)' : xsecErr}
        else: return False

    if abs(xsecTotal - sum([x['xsec (pb)'] for x in processXsecs.values()]))/xsecTotal > 0.001:
        return False 
    
    slhaF = open(slhaFile,'w')
    slhaF.write(slhaData)
    slhaF.write('\n\n')
    processXsecs = OrderedDict(sorted(processXsecs.items(), key=lambda proc: proc[1]['xsec (pb)'], reverse=True))
    
    for procID in processXsecs:
        finalStates = finalStatesDict[procID]
        xsec = processXsecs[procID]['xsec (pb)']
        xsecErr = processXsecs[procID]['xsecErr (pb)']
        comment = "# xsec unit: pb xsec error: %1.3e" % (xsecErr)
        
        xsecLine = "\nXSECTION %1.3e " % (sqrts)
        xsecLine += " ".join([str(pdg) for pdg in pdgInitial])
        xsecLine += " %i " % len(finalStates)
        xsecLine += " ".join([str(pdg) for pdg in finalStates])
        
        slhaF.write(xsecLine+' '+comment+' \n')        
        slhaF.write("  0  0  0  0  0  0  %1.4e ufo2slha 1.0\n" % xsec)    
        
    slhaF.close()
    return slhaFile

def process_directory(base_dir, pattern, pid_list, mg5_path, output_dir):
    processed_count = 0
    failed_count = 0
    for root, dirs, files in os.walk(base_dir):
        for filename in fnmatch.filter(files, pattern):
            lhe_path = os.path.join(root, filename)
            result = getSLHAFile(lhe_path, output_dir=output_dir, pidList=pid_list, mg5_path=mg5_path)
            if result: processed_count += 1
            else: failed_count += 1
                
    logger.info(f"Successfully created Reference SLHA files: {processed_count}")

if __name__ == "__main__":
    import argparse    
    ap = argparse.ArgumentParser()
    ap.add_argument('-d', '--dir', required=True)
    ap.add_argument('-o', '--outdir', required=True)
    ap.add_argument('-pt', '--pattern', default='*events.lhe*')
    # Default explicitly set to the Z' PDG for SModelS
    ap.add_argument('-pids', '--pids', default=[5000001], nargs='+')
    ap.add_argument('--mg5', default='/home/vinicius/MadGraph/MG5_aMC_v3_6_3/')
    args = ap.parse_args()
    
    os.makedirs(args.outdir, exist_ok=True)
    process_directory(args.dir, args.pattern, args.pids, args.mg5, args.outdir)