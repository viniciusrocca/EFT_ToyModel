#!/usr/bin/env python3

import os,glob
import numpy as np
import pandas as pd
import pyslha
import time
import progressbar as P
import tempfile,gzip,pylhe

cms_bins = np.array([250.,400.,480.,560.,640.,720.,800.,900.,1000.,
                1150.,1300.,1500.,1700.,2000.,2300.,3500.])

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


def getMTThist(nevents,events,weightMultiplier = 1.0):
    """
    Reads a PyLHE Event object and extracts the ttbar invariant
    mass for each event.
    """
    
    mTT = []
    weights = []
    for ev in events:
        weightPB = weightMultiplier*ev.eventinfo.weight/nevents
        weightAndError = np.array([weightPB,weightPB**2])

        # Add information to particles:
        for ptc in ev.particles:
            ptc.daughters = []
            ptc.PID = int(ptc.id)
            p = np.sqrt(ptc.px**2 + ptc.py**2 + ptc.pz**2)
            ptc.PT = np.sqrt(ptc.px**2 + ptc.py**2)
            if not ptc.PT: # Only for incoming partons
                ptc.Eta = None
                ptc.Phi = None
            else:
                ptc.Eta = (1./2.)*np.log((p+ptc.pz)/(p-ptc.pz))        
                ptc.Phi = np.arctan2(ptc.py,ptc.px)
            ptc.Px = ptc.px
            ptc.Py = ptc.py
            ptc.Pz = ptc.pz
            ptc.E = ptc.e

        # Get tops
        tops = {}
        for ptc in ev.particles:        
            if abs(ptc.PID) == 6:
                tops[ptc.PID] = ptc # Store only the last top/anti-top  

        # Sum the top momenta
        pTot = np.zeros(4)
        for top in tops.values():
            pTot += np.array([top.E,top.Px,top.Py,top.Pz])
        # Compute invariant mass squared
        m2 = np.dot(pTot[0],pTot[0]) - np.dot(pTot[1:4],pTot[1:4])

        mTT.append(np.sqrt(m2))
        weights.append(weightAndError)
    
    weights = np.array(weights)
    mttHist,_ = np.histogram(mTT,weights=weights[:,0],bins=cms_bins)
    mttHistError,_ = np.histogram(mTT,weights=weights[:,1],bins=cms_bins)
    mttHistError = np.sqrt(mttHistError)

    data = np.array(list(zip(cms_bins[:-1],cms_bins[1:],mttHist,mttHistError)))
    
    return data


def getInfo(f):

    procDict = {
                'g g > t t~' : r'$g g \to \bar{t} t$', 'g g > t~ t' : r'$g g \to \bar{t} t$',
                'q q > t t~' : r'$q q \to \bar{t} t$', 'q q > t~ t' : r'$q q \to \bar{t} t$'
                }
    
    banner = list(glob.glob(os.path.join(os.path.dirname(f),'*banner*')))[0]
    with open(banner,'r') as bannerF:
        bannerData = bannerF.read()
    
    # Get process data:
    processData = bannerData.split('<MGProcCard>')[1].split('</MGProcCard>')[0]

    # Get model
    model = processData.split('Begin MODEL')[1].split('End   MODEL')[0]
    model = model.split('\n')[1].strip()

    # Get process
    proc = processData.split('Begin PROCESS')[1].split('End PROCESS')[0]
    proc = proc.split('\n')[1].split('#')[0].strip()
    if proc in procDict:
        proc = procDict[proc]
    
    # Get parameters data:
    parsData = bannerData.split('<slha>')[1].split('</slha>')[0]
    parsSLHA = pyslha.readSLHA(parsData)
    
    mST = parsSLHA.blocks['MASS'][5000002]
    mChi = parsSLHA.blocks['MASS'][5000012]
    mT  = parsSLHA.blocks['MASS'][6]
    yDM = list(parsSLHA.blocks['FRBLOCK'].values())[-1]

    
    # Get event data:
    eventData = bannerData.split('<MGGenerationInfo>')[1].split('</MGGenerationInfo>')[0]
    nEvents = eval(eventData.split('\n')[1].split(':')[1].strip())
    xsec = eval(eventData.split('\n')[2].split(':')[1].strip())

    fileInfo = {'model' : model, 'process' : proc, 'mST' : mST, 'mChi' : mChi, 'mT' : mT, 'yDM' : yDM,
               'xsec (pb)' : xsec, 'MC Events' : nEvents, 'file' : f}
    
    return fileInfo


def getRecastData(inputFiles,weightMultiplier=1.0,skipParameters=[]):

    
    # Filter files (if needed)
    if not skipParameters:
        selectedFiles = inputFiles[:]
    else:
        selectedFiles = []
        for f in inputFiles:
            # print('\nReading file: %s' %f)
            fileInfo = getInfo(f)
            parInfo = (fileInfo['mST'],fileInfo['mChi'],fileInfo['yDM'], 
                        fileInfo['mT'], fileInfo['model'], fileInfo['process'])
            if parInfo in skipParameters:
                continue
            selectedFiles.append(f)
        print('Skipping %i files' %(len(inputFiles)-len(selectedFiles)))
    
    if not selectedFiles:
        return None
    
    allData = []

    progressbar = P.ProgressBar(widgets=["Reading %i Files: " %len(selectedFiles), 
                            P.Percentage(),P.Bar(marker=P.RotatingMarker()), P.ETA()])
    progressbar.maxval = len(selectedFiles)
    progressbar.start()
    nfiles = 0
    for f in selectedFiles:       
        fileInfo = getInfo(f) 
        # Get events:
        nevents,events = getLHEevents(f)
        data = getMTThist(nevents,events,weightMultiplier=weightMultiplier)
        # Create a dictionary with the bin counts and their errors
        dataDict = fileInfo
        bins_left = data[:,0]
        bins_right = data[:,1]
        w = data[:,2]
        wError = data[:,3]    
        nfiles += 1
        progressbar.update(nfiles)
        for ibin,b in enumerate(bins_left):
            label = 'bin_%1.0f_%1.0f'%(b,bins_right[ibin])
            dataDict[label] = w[ibin]
            dataDict[label+'_Error'] = wError[ibin]
        allData.append(dataDict)
        

    progressbar.finish()
    return allData


if __name__ == "__main__":
    
    import argparse    
    ap = argparse.ArgumentParser( description=
            "Run the recasting for CMS-TOP-20-001 using one or multiple MadGraph (parton level) LHE files. "
            + "If multiple files are given as argument, add them."
            + " Store the SR bins in a pickle (Pandas DataFrame) file." )
    ap.add_argument('-f', '--inputFile', required=True,nargs='+',
            help='path to the LHE event file(s) generated by MadGraph.', default =[])
    ap.add_argument('-o', '--outputFile', required=False,
            help='path to output file storing the DataFrame with the recasting data.'
                 + 'If not defined, will use the name of the first input file', 
            default = None)
    ap.add_argument('-w', '--weightMultiplier', required=True, type=float,
                    help='Factor used to multiply the weights (in case events were generated with specific top decays in each branch) [default=2.0]', default = 2.0)
    ap.add_argument('-O', '--overwrite', required=False, action='store_true',
                    help='If set, will overwrite the existing output file. Otherwise, it will simply add the points not yet present in the file', default = False)

    t0 = time.time()

    # # Set output file
    args = ap.parse_args()
    inputFiles = args.inputFile
    outputFile = args.outputFile
    weightMultiplier = args.weightMultiplier

    if outputFile is None:
        outputFile = inputFiles[0].replace('.lhe.gz','_cms_top_20_001.pcl')

    if os.path.splitext(outputFile)[1] != '.pcl':
        outputFile = os.path.splitext(outputFile)[0] + '.pcl'

    skipParameters = []
    if os.path.isfile(outputFile):
        if args.overwrite:
            print('Output file %s will be overwritten!' %outputFile)
        else:
            df_orig = pd.read_pickle(outputFile)
            skipParameters = []
            for irow,row in df_orig.iterrows():
                skipParameters.append((row['mST'],row['mChi'],row['yDM'], row['mT'], row['model'], row['process']))


    print('-----------------\n Running with weight multiplier = %1.1f\n -------------------------' %weightMultiplier)

    dataDict = getRecastData(inputFiles,weightMultiplier,skipParameters)
    if dataDict:
        # #### Create pandas DataFrame
        df = pd.DataFrame.from_dict(dataDict)
        if os.path.isfile(outputFile) and skipParameters:
            df = pd.concat([df_orig,df])

        # ### Save DataFrame to pickle file
        print('Saving to',outputFile)
        df.to_pickle(outputFile)

    print("\n\nDone in %3.2f min" %((time.time()-t0)/60.))
