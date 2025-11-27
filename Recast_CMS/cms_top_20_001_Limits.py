#!/usr/bin/env python3

import numpy as np
import pandas as pd
import time,os,sys
import progressbar as P
import numpy as np
import csv 
import pandas as pd
from scipy.optimize import minimize, brentq

cms_bins = np.array([250.,400.,480.,560.,640.,720.,800.,900.,1000.,
                1150.,1300.,1500.,1700.,2000.,2300.,3500.])
bin_widths  = cms_bins[1:]-cms_bins[:-1]                

def csv_reader(filename):
    output = []
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            output.append(row)
        csvfile.close()

    return output

def get_ratio_err(bg_ratio, bg_ratio_err):
    '''
    Convert the coordinates of the top of the error bar to the actual length of error bar
    '''
    ratio_err = []
    for i,item in enumerate(bg_ratio_err[2:]):
        ratio_err.append(float(item[1]) - float(bg_ratio[i+2][1])) #Compute the length of the upper error bar
    return ratio_err

def get_bg_error(cms_bg, data, bg_ratio_err):
    '''
    Computes the background error from the data and ratio values and errors.
    '''
    bg_err = []
    for i,item in enumerate(data[9:24]):
        data_err = np.sqrt(float(item[4])**2 + float(item[6])**2) #Considering the statistical and systematic errors
        err = (float(item[3])**2 / cms_bg[i]) * np.sqrt(bg_ratio_err[i]**2 + (data_err / float(item[3]))**2) #computing the error
        bg_err.append(err)
    return np.array(bg_err)

def read_CMSdata(dataDir='./data',bg="MATRIX"):
    '''
    Read data and covmat from hepdata. Computes the backgorund and its error from the ratio of the plot.
    '''
    data = csv_reader(os.path.join(dataDir,'parton_abs_ttm.csv'))
    cms_data  = []
    for item in data[9:24]:
        cms_data.append(float(item[3]))

    
    if bg == "MATRIX":
        bg_ratio = csv_reader(os.path.join(dataDir,'ratioMATRIX_Fig19a.csv'))
        bg_ratio_err = csv_reader(os.path.join(dataDir,'err_ratioMATRIX_Fig19a.csv')) #Coordinates of the top of the error bars
        bg_ratio_err = get_ratio_err(bg_ratio, bg_ratio_err) #Convert the coordinates in the error 
    elif bg == "MG5":
        bg_ratio = csv_reader(os.path.join(dataDir,'ratioMGPY8_Fig19a.csv'))
    else:
        print("Only MATRIX and MG5 backgrounds are available")
    cms_bg = []
    for i,item in enumerate(bg_ratio[2:]):
        cms_bg.append(float(item[1])*cms_data[i]) #Multiplying the ratio by the data to obtain MATRIX
    # The digitized values are divided by the width
    #cms_bg = np.array(cms_bg)*bin_widths
    
    cms_bg_err = get_bg_error(cms_bg, data, bg_ratio_err)

    covdata = csv_reader(os.path.join(dataDir,'parton_abs_ttm_covariance.csv'))
    covmat = np.zeros(15*15).reshape(15,15)

    covmatlist = []
    count=0
    for item in covdata[9:234]:
        covmatlist.append(float(item[6]))

    for i in range(15):
        for j in range(15):
            covmat[i,j] = covmatlist[count]
            count+=1

    return np.array(cms_data), np.array(cms_bg), np.array(covmat), np.array(cms_bg_err)

def getSMLO(smFile='./sm/sm_tt_lo_cms_top_20_001.pcl'):

    # ### Load Recast Data
    recastData = pd.read_pickle(smFile)

    binCols = [c for c in recastData.columns 
               if 'bin_' in c.lower() and not 'error' in c.lower()]
    bins_left = np.array([eval(c.split('_')[1]) for c in binCols])
    bins_right = np.array([eval(c.split('_')[2]) for c in binCols])
    # Check that bins are consistent:
    if not np.array_equal(bins_left,cms_bins[:-1]):
        print('Bins from data do not match CMS')
        return
    if bins_right[-1] != cms_bins[-1]:
        print('Bins from data do not match CMS')
        return

    if len(recastData) != 1:
        print('SM LO file %s has multiple entries' %smFile)
        return False
    
    pt = recastData.iloc[0]
    smLO = list(zip(bins_left,pt[binCols].values))
    smLO = np.array(sorted(smLO))[:,1]

    return smLO


def getKfactor(smNNLO,smLO):
    """
    Compute bin-by-bin kfactors using the CMS NNLO and the LO xsecs
    """
    
    # Get k-factor for each bin
    kfac = np.divide(smNNLO,smLO)

    return 1.0

def chi2(yDM,signal,sm,data,covmat,deltas=0.0, deltabg=0.0):
    theory = (sm + yDM**2*signal)
    diff = (theory - data)
    CovTotal = covmat + np.diag((yDM**2*signal*deltas)**2 + (sm*deltabg)**2) 
    Vinv = np.linalg.inv(CovTotal)
    return ((diff).dot(Vinv)).dot(diff)

def getUL(signal,sm_bin,xsecsObs,covMatrix,deltas=0.0, deltabg=0.0):

    #First find minima of the chi profile, such that the delta chi2 can then be calculated
    def func_to_solve_deltachi2(yDMval):
        return chi2(yDMval, signal, sm_bin, xsecsObs, covMatrix, deltas, deltabg)

    yDMmin = minimize(func_to_solve_deltachi2, x0=20).x
    chi2min = chi2(yDMmin, signal, sm_bin, xsecsObs, covMatrix, deltas, deltabg)

    def func_to_solve_95(yDMval):
        return chi2(yDMval, signal, sm_bin, xsecsObs, covMatrix, deltas, deltabg) - chi2min - 3.84

    yDM95 = brentq(func_to_solve_95, a=1000,b=yDMmin)
    deltaChi95 = chi2(yDM95, signal, sm_bin, xsecsObs, covMatrix, deltas, deltabg)-chi2min

    return {'yDMmin' : yDMmin, 'chi2min' : chi2min, 
            'yDM95' : yDM95, 'deltaChi95' : deltaChi95}


def computeULs(inputFile,outputFile,full=False):

    # ### Load CMS data and BG
    xsecsObs,sm,covMatrix, sm_err = read_CMSdata()
    deltabg_array = np.divide(sm_err, sm, out=np.zeros_like(sm), where=sm!=0)
    
    # ### Load LO background from MG5
    smLO = getSMLO()
    # Get k-factor for each bin
    kfac = getKfactor(sm,smLO)

    # ### Load Recast Data
    recastData = pd.read_pickle(inputFile)

    binCols = [c for c in recastData.columns 
               if 'bin_' in c.lower() and not 'error' in c.lower()]
    bins_left = np.array([eval(c.split('_')[1]) for c in binCols])
    bins_right = np.array([eval(c.split('_')[2]) for c in binCols])
    # Check that bins are consistent:
    if not np.array_equal(bins_left,cms_bins[:-1]):
        print('Bins from data do not match CMS')
        return
    if bins_right[-1] != cms_bins[-1]:
        print('Bins from data do not match CMS')
        return


    progressbar = P.ProgressBar(widgets=["Computing upper limits: ", P.Percentage(),
                                P.Bar(marker=P.RotatingMarker()), P.ETA()])
    progressbar.maxval = len(recastData)
    progressbar.start()

    yDM95list = []
    yDM95expList = []
    deltaChi95list = []
    for ipt,pt in recastData.iterrows():

        progressbar.update(ipt)
        signal = list(zip(bins_left,pt[binCols].values))
        signal = np.array(sorted(signal))[:,1]
        yDM = pt['yDM']
        # Make sure signal is normalized to yDM = 1
        signal = signal/yDM**2
        # Rescale predictions by bin-dependent k-factors
        signal = kfac*signal

        if not full: # Use simplified chi-square
            # Finally, divide by the bin widths
            signal = signal/bin_widths
            sm_bin = sm/bin_widths
            resDict = getUL(signal,sm_bin,xsecsObs,covMatrix,deltas=0.0, deltabg = deltabg_array)
            yDM95 = resDict['yDM95']
            deltaChi95 = resDict['deltaChi95']       

            # Expected
            resDictExp = getUL(signal,sm_bin,sm_bin,covMatrix,deltas=0.0, deltabg = deltabg_array)
            yDM95exp = resDictExp['yDM95']            
            
        else: # Use full CLs calculation
            import sys
            sys.path.append('../statisticalTools')
            from simplifiedLikelihoods import Data,UpperLimitComputer,LikelihoodComputer
            ulComp = UpperLimitComputer()

            # ### Get number of observed and expected (BG) events
            lumi = 137*1e3
            nobs = xsecsObs*bin_widths*lumi
            nbg = sm*lumi
            ns = signal*lumi
            cov = covMatrix*(lumi*bin_widths)**2
            data = Data(observed=nobs, backgrounds=nbg, 
                        covariance=cov, 
                        nsignal=ns,deltas_rel=0.0)
            ul = ulComp.getUpperLimitOnMu(data)
            yDM95 = np.sqrt(ul)
            # Signal for 95% C.L. limit:
            data95 = Data(observed=nobs, backgrounds=nbg, 
                          covariance=cov, 
                          nsignal=ns*ul,deltas_rel=0.0)
            computer = LikelihoodComputer(data95)
            deltaChi95 = computer.chi2()

        # Store result
        yDM95list.append(yDM95)
        yDM95expList.append(yDM95exp)
        deltaChi95list.append(deltaChi95)

    recastData['yDM (95% C.L.)'] = yDM95list
    recastData['yDMexp (95% C.L.)'] = yDM95expList
    recastData[r'$\Delta \chi^2$ (95% C.L.)'] = deltaChi95list
    progressbar.finish()
    recastData.to_pickle(outputFile)



if __name__ == "__main__":
    
    import argparse    
    ap = argparse.ArgumentParser(description=
            "Compute the upper limit on mu from CMS-EXO-20-004 for the recast data stored in the input file.")
    ap.add_argument('-f', '--inputFile', required=True,
            help='path to the pickle file containing the Pandas DataFrame with the recasting results for the models')
    ap.add_argument('-o', '--outputFile', required=False,
            help='path to output file. If not defined the upper limits will be stored in the input file.',
            default = None)

    t0 = time.time()

    # # Set output file
    args = ap.parse_args()
    inputFile = args.inputFile
    if not os.path.isfile(inputFile):
        print("File %s not found" %inputFile)
        sys.exit()
    outputFile = args.outputFile
    if outputFile is None:
        outputFile = inputFile
    
    computeULs(inputFile,outputFile)

    print("\n\nDone in %3.2f min" %((time.time()-t0)/60.))





