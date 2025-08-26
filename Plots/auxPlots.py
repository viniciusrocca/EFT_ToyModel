
import glob, pyslha,os
import numpy as np
import itertools
from scipy.interpolate import  griddata
from matplotlib import pyplot as plt
import tempfile
import pylhe
import gzip
import seaborn as sns
import math



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
    weights = []
    for ev in events:
        w = ev.eventinfo.weight/nevents
        weights.append(w)
        for ptc in ev.particles:
            if abs(ptc.id) != 6: continue
            if ptc.id == 6:
                pA = np.array([ptc.px,ptc.py,ptc.pz,ptc.e])
            else:
                pB = np.array([ptc.px,ptc.py,ptc.pz,ptc.e])

        pT1.append(max(np.linalg.norm(pA[0:3]),np.linalg.norm(pB[0:3])))
        pT2.append(min(np.linalg.norm(pA[0:3]),np.linalg.norm(pB[0:3])))
        mTT.append(np.sqrt((pA[-1]+pB[-1])**2-np.linalg.norm(pA[0:3]+pB[0:3])**2))
    
    dists = {'mTT' : mTT, 'pT1' : pT1, 'pT2' : pT2, 
             'weights' : np.array(weights), 'nevents' : nevents}

    return dists


def getInfo(f,labelsDict=None):


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
    
    # Get parameters data:
    parsData = bannerData.split('<slha>')[1].split('</slha>')[0]
    parsSLHA = pyslha.readSLHA(parsData)
    
    mT  = parsSLHA.blocks['MASS'][6]
    if 5000002 in parsSLHA.blocks['MASS']:
        mSDM = parsSLHA.blocks['MASS'][5000002]
        mPsiT = parsSLHA.blocks['MASS'][5000012]        
        yDM = list(parsSLHA.blocks['FRBLOCK'].values())[-1]
    else:
        mSDM = 0.0
        mPsiT = 0.0
        yDM = 0.0

    if yDM == 0.0:
        model = 'SM'


    
    # Get event data:
    eventData = bannerData.split('<MGGenerationInfo>')[1].split('</MGGenerationInfo>')[0]
    nEvents = eval(eventData.split('\n')[1].split(':')[1].strip())
    xsec = eval(eventData.split('\n')[2].split(':')[1].strip())

    fileInfo = {'model' : model, 'process' : proc, '(mSDM,mPsiT,mT,yDM)' : (mSDM,mPsiT,mT,yDM),
               'xsec (pb)' : xsec, 'nevents' : nEvents}
    
    return fileInfo

def selectColor(model, process):
    if model == 'EFT' and process == r'$g g \to t \bar{t}$':
        return sns.color_palette('Paired')[0]
    elif model == '1-loop UV' and process == r'$g g \to t \bar{t}$':
        return sns.color_palette('Paired')[1]
    elif model == 'EFT' and process == r'$q q \to t \bar{t}$':
        return sns.color_palette('Paired')[2]
    else:
        return sns.color_palette('Paired')[3]
    
    
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


def xSecTest(data, display = False):
    #This function checks if the sum of the weights is the total cross section
    for d in data:
        mPsiT,mSDM = d['mass_params']

        if math.isclose(d['xsec (pb)'],  sum(d['weights'] ), rel_tol = 1e-7):
            print(d['model'], d['process'], ' mPsiT: %.1f, mSDM: %.1f' % (mPsiT,mSDM), 'Result: Passed')
        else:
            print(d['model'], d['process'], ' mPsiT: %.1f, mSDM: %.1f' % (mPsiT,mSDM), 'Result: Reproved')

        if display == True:
            print('xsec = %.9f sum of weights = %.9f ' % (d['xsec (pb)'], sum(d['weights'] )))
    return
     
def getInfoSMS(f,nlo = False,labelsDict=None):


    if labelsDict is None:
        labelsDict = {
                      'Top-FormFactorsOneLoop-UFO' : '1-loop (FormFactor)', 'SMS_EFT_UFO' : 'SMS EFT',
                       'sm' : 'SM',
                       'loop_sm' : 'SM',
                      'SMS-stop_NLO-UFO' : '1-loop (SMS)',
              'g g > t t~' : r'$g g \to t \bar{t}$', 'g g > t~ t' : r'$g g \to t \bar{t} $',
              'q q > t t~' : r'$q q \to t \bar{t}$', 'q q > t~ t' : r'$q q \to t \bar{t}$',
              'p p > t t~' : r'$p p \to t \bar{t}$', 'p p > t~ t' : r'$p p \to t \bar{t}$'
             }
    
    runDir = os.path.dirname(f)
    if not os.path.isdir(runDir):
        print(f'Folder {runDir} not found')
        return None
    banners = list(glob.glob(os.path.join(runDir,'*banner*txt')))
    if len(banners) != 1:
        print(f'{len(banners)} found (can only deal with 1 banner).')
        return None
    banner = banners[0]
    with open(banner,'r') as bannerF:
        bannerData = bannerF.read()
    
    # Get process data:
    if '<MGProcCard>' in bannerData:
        processData = bannerData.split('<MGProcCard>')[1].split('</MGProcCard>')[0]
        # Get model
        model = processData.split('Begin MODEL')[1].split('End   MODEL')[0]
        model = model.split('\n')[1].strip()
        # Get process
        proc = processData.split('Begin PROCESS')[1].split('End PROCESS')[0]
        proc = proc.split('\n')[1].split('#')[0].strip()
        
    elif os.path.isfile(os.path.join(runDir,'../../Cards/proc_card_mg5.dat')):
        procCard = os.path.join(runDir,'../../Cards/proc_card_mg5.dat')
        with open(procCard,'r') as f:
            processData = f.readlines()
        modelLine = [l for l in processData if 'import model' in l][-1]
        model = modelLine.strip().split(' ')[-1]
        model = os.path.basename(model)
        procLine = [l for l in processData if 'generate' in l][-1]
        proc = procLine.strip().split('generate ')[-1]
    else:
        model = None
        proc = None

    if '[' in proc and ']' in proc:
        proc = proc.split('[')[0].strip()

    if proc in labelsDict:
        proc = labelsDict[proc]
    if model in labelsDict:
        model = labelsDict[model]

    # Get parameters data:
    parsData = bannerData.split('<slha>')[1].split('</slha>')[0]
    parsSLHA = pyslha.readSLHA(parsData)
    
    mT  = parsSLHA.blocks['MASS'][6]
    if 5000002 in parsSLHA.blocks['MASS']:
        mST = parsSLHA.blocks['MASS'][5000002]
        mChi = parsSLHA.blocks['MASS'][5000012]        
        yDM = list(parsSLHA.blocks['FRBLOCK'].values())[-1]
    elif model == 'SMS EFT':
        pars = list(parsSLHA.blocks['FRBLOCK'].values())
        mST= pars[1]
        mChi = pars[2]     
        yDM = pars[0]
    else:
        mST = 0.0
        mChi = 0.0
        yDM = 0.0

    if yDM == 0.0:
        model = 'SM'
    
    # Get event data:
    if '<MGGenerationInfo>' in bannerData:
        eventData = bannerData.split('<MGGenerationInfo>')[1].split('</MGGenerationInfo>')[0]
        nEvents = eval(eventData.split('\n')[1].split(':')[1].strip())
        xsec = eval(eventData.split('\n')[2].split(':')[1].strip())
    elif os.path.isfile(os.path.join(runDir,'summary.txt')):
        with open(os.path.join(runDir,'summary.txt'),'r') as f:
            summaryLines = f.readlines()
        totalXsecLine = [l for l in summaryLines if 'Total cross section' in l][0]
        if 'DO NOT USE' in totalXsecLine:
            totalXsecLine = [i for i,l in enumerate(summaryLines) if 'Scale variation' in l][0]
            totalXsecLine = summaryLines[totalXsecLine+2]
        if 'Total cross section' in totalXsecLine:
            totalXsecLine = totalXsecLine.split(':')[1].strip()
        totalXsecLine = totalXsecLine.split(' +')[0].strip()
        totalXsecLine = totalXsecLine.replace('pb','')
        xsec = float(totalXsecLine)
        nEvents = -1
    else:
        nEvents = -1
        xsec = -1.0

    fileInfo = {'model' : model, 'process' : proc, '(mST,mChi,mT,yDM)' : (mST,mChi,mT,yDM),
               'xsec (pb)' : xsec, 'nevents' : nEvents}
    
    return fileInfo

    
