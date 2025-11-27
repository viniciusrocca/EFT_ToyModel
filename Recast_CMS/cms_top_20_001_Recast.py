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

def clean_item(item):
        # If it's a numpy array (0-d or otherwise), get the scalar value
        if isinstance(item, np.ndarray):
            return item.item()
        # If it's a numpy scalar (like np.float64), convert to python type
        if hasattr(item, 'item'):
            return item.item()
        return item


def getMTThistAndInfo(file, weightMultiplier = 1.0):
    """
    Reads the .npz file with top-related distributions computed from MC Events and extracts some info and the invariant mass distribution. 
    Computes the invariant mass histogram and its error for the cms binning.
    """
    data = np.load(file, allow_pickle = True)
    
    #Getting info:
    process = str(clean_item(data['process']))
    model   = str(clean_item(data['model']))
    mPsiT   = float(data['mass_params'][0])
    mSDM    = float(data['mass_params'][1])
    yDM     = float(data['ydm'])
    mT      = 172.5 # GeV
    weights = weightMultiplier * data['weights']
    weights = np.array([[w, w**2] for w in weights])

    #Storing the info in a dictionary
    fileInfo = {'model' : model, 'process' : process, 'mPsiT' : float(mPsiT), 'mSDM' : float(mSDM), 'mT' : mT, 'yDM' : float(yDM),
               'xsec (pb)' : clean_item(data['xsec (pb)']), 'MC Events' : clean_item(data['nevents']), 'file' : file}

    #Computing the histogram
    mttHist,_ = np.histogram(data['mTT'],bins=cms_bins,weights=weights[:,0])
    #Compute MC error
    mttHistError,_ = np.histogram(data['mTT'],bins=cms_bins,weights=weights[:,1])
    mttHistError = np.sqrt(mttHistError)    

    data_set = np.array(list(zip(cms_bins[:-1],cms_bins[1:],mttHist,mttHistError)))
    
    return data_set, fileInfo



def getRecastData(inputFiles,weightMultiplier=1.0,skipParameters=[]):

    # Filter files (if needed)
    if not skipParameters:
        selectedFiles = inputFiles[:]
    else:
        selectedFiles = []
        for f in inputFiles:
            # print('\nReading file: %s' %f)
            aux, fileInfo = getMTThistAndInfo(f,weightMultiplier=weightMultiplier)
            parInfo = (fileInfo['mPsiT'],fileInfo['mSDM'],fileInfo['yDM'], 
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
        data, fileInfo = getMTThistAndInfo(f,weightMultiplier=weightMultiplier)
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
            "Run the recasting for CMS-TOP-20-001 using one or multiple mTT distributions computed from MadGraph (parton level) events. "
            + "If multiple files are given as argument, add them."
            + " Store the SR bins in a pickle (Pandas DataFrame) file." )
    ap.add_argument('-f', '--inputFile', required=True,nargs='+',
            help='path to the .npz file(s) with the distributions.', default =[])
    ap.add_argument('-o', '--outputFile', required=False,
            help='path to output file storing the DataFrame with the recasting data.'
                 + 'If not defined, will use the name of the first input file', 
            default = None)
    ap.add_argument('-w', '--weightMultiplier', required=True, type=float,
                    help='Factor used to multiply the weights (in case events were generated with specific top decays in each branch) [default=1.0]', default = 1.0)
    ap.add_argument('-O', '--overwrite', required=False, action='store_true',
                    help='If set, will overwrite the existing output file. Otherwise, it will simply add the points not yet present in the file', default = False)

    t0 = time.time()

    # # Set output file
    args = ap.parse_args()
    inputFiles = args.inputFile
    outputFile = args.outputFile
    weightMultiplier = args.weightMultiplier

    if outputFile is None:
        outputFile = inputFiles[0].replace('.npz','_cms_top_20_001.pcl')

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
                skipParameters.append((row['mPsiT'],row['mSDM'],row['yDM'], row['mT'], row['model'], row['process']))


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
