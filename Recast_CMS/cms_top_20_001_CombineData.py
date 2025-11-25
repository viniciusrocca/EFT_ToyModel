#!/usr/bin/env python3


import pandas as pd
import numpy as np

def combineRecastData(files,outputFile):

    # Get files
    if not files:
        print('No valid files found')
    else:
        print('Combining %i files' %len(files))

    allData = pd.read_pickle(files[0])
    for f in files[1:]:
        recastData = pd.read_pickle(f)
        allData = pd.concat((allData,recastData),ignore_index=True)

        
    allColumns = allData.columns.tolist()
    orderColumns = ['model', 'mST', 'mChi', 'mT', 'yDM']
    binErrorColumns = [c for c in allColumns if 'bin' in c.lower() and 'error' in c.lower()]
    allCols = orderColumns[:] + [c for c in allColumns if not c in orderColumns]
    allData = allData[allCols]
    allData.sort_values(orderColumns,inplace=True,
                ascending=[False,True,True,True,True],ignore_index=True)     

    # Split datasets by process:
    procDataDict = {}
    for proc in allData['process'].unique():
        dataProc = allData[allData['process'] == proc].copy(deep=True)
        dataProc.reset_index(inplace=True,drop=True)
        procDataDict[proc] = dataProc

    # Make sure all datasets have the same length and BSM parameters
    nrows = len(dataProc)
    if any(len(data) != nrows for data in procDataDict.values()):
        print('Data for processes differ')
        return
    for dataProcB in procDataDict.values():
        if not dataProc[orderColumns].equals(dataProcB[orderColumns]):
            print('Datasets for different processes have distinct BSM values')
            return

    # Create an empty dataframe with columns
    totalData = None
    for proc,data in procDataDict.items():
        if totalData is None:
            totalData = data.copy(deep=True)
        else:
            for c in totalData.columns:
                if c in orderColumns:
                    continue
                elif c not in binErrorColumns:
                    totalData[c] = totalData[c] +  data[c]
                else:
                    totalData[c] = np.sqrt(totalData[c]**2 + data[c]**2)

    # ### Save DataFrame to pickle file
    print('Saving to',outputFile)
    totalData.to_pickle(outputFile)        
        

if __name__ == "__main__":
    
    import argparse    
    ap = argparse.ArgumentParser(description=
            "Merge individual DataFrames for model points to a single DataFrame (pickle file).")
    ap.add_argument('-f', '--inputFiles', required=True,nargs='+',
            help='list of pickle files to be merged', default =[])
    ap.add_argument('-o', '--outputFile', required=True, help='output file.')


    args = ap.parse_args()
    inputFiles = args.inputFiles
    outputFile = args.outputFile
    
    combineRecastData(inputFiles,outputFile)







