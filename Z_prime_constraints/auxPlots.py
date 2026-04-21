
import glob, pyslha,os
import numpy as np
import itertools
from scipy.interpolate import  griddata
from matplotlib import pyplot as plt
import tempfile
import pylhe
import gzip
import sys



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

def applyATLAScuts2(event,etamax=2.0,pTmin=355.0):
    
    import fastjet
    jetdef = fastjet.JetDefinition(fastjet.antikt_algorithm, 0.4)
    fatjetdef = fastjet.JetDefinition(fastjet.antikt_algorithm, 1.0)
    error = False

    cutFlow = { 'decays' : False,
                'njets' : False, 
               'FatJet' : False,
               'FatJet Mass' : False,
               'FatJet pT' : False,
               'FatJet Eta' : False,
               'FatJet hasB' : False,
               'Lepton pT' : False,
               'Lepton Eta' : False,
               'Lepton dRb' : False,
               'mlb' : False,
               'mlj': False,
               'MET cut' : False
               }

    # Add information to particles:
    for ptc in event.particles:
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
        
    for ptc in event.particles:
        for mom in ptc.mothers():
            mom.daughters.append(ptc)
    
    # Get tops and their final decays:
    tops = {}
    topDecays = {}
    for ptc in event.particles:        
        if abs(ptc.PID) == 6:
            tops[ptc.PID] = ptc # Store only the last top/anti-top            
            daughters = {d.PID : d for d in ptc.daughters}
            hasDaughters = [pid for pid,d in daughters.items() if d.daughters]
            while len(hasDaughters) > 0:
                for pid in hasDaughters:
                    d = daughters.pop(pid)
                    for dd in d.daughters:
                        daughters[dd.PID] = dd
                hasDaughters = [pid for pid,d in daughters.items() if d.daughters]
            topDecays[ptc.PID] = list(daughters.values())
    
    # Select events with one lepton and one hadronic top:
    topH = None
    topLep = None
    for topPID,daughters in topDecays.items():        
        dPIDs =  [abs(ptc.PID) for ptc in daughters]
        if len(dPIDs) != 3:
            error = True
            print('Error getting daughters:',dPIDs)
            break
        if not 5 in dPIDs:
            continue # Skip rare decays to W+c
        if (11 in dPIDs) or (13 in dPIDs):
            topLep = topPID
        elif max(dPIDs) <= 5:
            topH = topPID

    if error:
        return False
    
    if topH is None or topLep is None:
        return False
    cutFlow['decays'] = True

    # Hadronic top:    
    # Regular jets:
    quarks = [ptc for ptc in topDecays[topH]]
    jetArray = [fastjet.PseudoJet(q.Px,q.Py,q.Pz,q.E) for q in quarks if abs(q.Eta) < 4.5]
    for ij,j in enumerate(jetArray):
        j.set_user_index(quarks[ij].PID)
    cluster = fastjet.ClusterSequence(jetArray, jetdef)
    jets = cluster.inclusive_jets(ptmin = 26.0)
    jets = [j for j in jets if abs(j.eta()) < 2.5]
    if len(jets) == 0:
        return tops[topH],tops[topLep],cutFlow    
    cutFlow['njets'] = True

    # ## Fat jet:    
    jetArray = [fastjet.PseudoJet(j.px(),j.py(),j.pz(),j.E()) for j in jets]
    for ij,j in enumerate(jetArray):
        for q in jets[ij].constituents():
            if abs(q.user_index()) == 5:
                j.set_user_index(5) # Tag the regular jets containing a b-quark
    clusterFat = fastjet.ClusterSequence(jetArray, fatjetdef)
    if len(clusterFat.inclusive_jets()) == 0:
        return tops[topH],tops[topLep],cutFlow
    cutFlow['FatJet'] = True
    
    # Use hardest fat jet
    fatJet = sorted([j for j in clusterFat.inclusive_jets()], key = lambda j: j.pt(), reverse=True)[0]
    # Invariant mass cut:
    if not (120. < fatJet.m() < 220.):
        return tops[topH],tops[topLep],cutFlow
    cutFlow['FatJet Mass'] = True
    # PT cut
    if fatJet.pt() < pTmin:
        return tops[topH],tops[topLep],cutFlow
    cutFlow['FatJet pT'] = True

    # Eta cut
    if abs(fatJet.eta()) > etamax:
        return tops[topH],tops[topLep],cutFlow
    cutFlow['FatJet Eta'] = True

    # Require a b inside the Fat jet
    hasB = False
    for q in fatJet.constituents():
        if q.user_index() == 5:
            hasB = True
    if not hasB:
        return tops[topH],tops[topLep],cutFlow
    cutFlow['FatJet hasB'] = True

    # Leptonic top:
    leptons = [ptc for ptc in topDecays[topLep] if abs(ptc.PID) in [11,13]]
    neutrinos = [ptc for ptc in topDecays[topLep] if abs(ptc.PID) in [12,14]]
    bLep = [ptc for ptc in topDecays[topLep] if abs(ptc.PID) ==5]
    if len(leptons) != 1:
        error = True
        print('Error getting leptons')
    if len(neutrinos) != 1:
        error = True
        print('Error getting neutrinos')
    if len(bLep) != 1:
        error = True
        print('Error getting b-jet')
        return False
    if error:
        return False
    lepton = leptons[0]
    nu = neutrinos[0]
    bLep = bLep[0]
    
    pTlepton = lepton.PT
    etaLep = np.abs(lepton.Eta)
    # Lepton pT cut
    if pTlepton < 27.0:
        return tops[topH],tops[topLep],cutFlow
    cutFlow['Lepton pT'] = True
    # Lepton eta cut
    if etaLep > 2.5:
        return tops[topH],tops[topLep],cutFlow
    cutFlow['Lepton Eta'] = True

    # Require the b to be close to the lepton
    dRlep = np.sqrt((lepton.Eta-bLep.Eta)**2 + (lepton.Phi-bLep.Phi)**2)
    if dRlep > 2.0:
        return tops[topH],tops[topLep],cutFlow
    cutFlow['mlb'] = True
    # Invariant mass of lepton and b < 180:
    mlb = np.sqrt((lepton.E+bLep.E)**2-(lepton.Px+bLep.Px)**2-(lepton.Py+bLep.Py)**2-(lepton.Pz+bLep.Pz)**2)
    if mlb > 180.0:
        return tops[topH],tops[topLep],cutFlow
    cutFlow['mlb'] = True
    # Skip events where lepton overlaps to jet
    dRlep = min([np.sqrt((lepton.Eta-j.eta())**2 + (lepton.Phi-j.phi())**2) for j in jets])    
    if dRlep < 0.4:
        return tops[topH],tops[topLep],cutFlow
    cutFlow['mlj'] = True
    # MET cut
    if (nu.PT < 20.0):
        return tops[topH],tops[topLep],cutFlow
    cutFlow['MET cut'] = True
    
    return tops[topH],tops[topLep],cutFlow

def getATLASdistributions(filename,etamax=2.0,pTmin=355.0,getCutFlow=False):

    nevents,events = getLHEevents(filename)
    pT1 = []
    pT2 = []
    mTT = []
    weights = []
    cutFlow = {'decays' : [],
            'njets' : [], 
            'FatJet' : [],
            'FatJet Mass' : [],
            'FatJet pT' : [],
            'FatJet Eta' : [],
            'FatJet hasB' : [],
            'Lepton pT' : [],
            'Lepton Eta' : [],
            'Lepton dRb' : [],
            'mlb' : [],
            'mlj': [],
            'MET cut' : []
            }
    for ev in events:
        w = ev.eventinfo.weight/nevents
        if getCutFlow:
            passCuts = applyATLAScuts2(ev,etamax,pTmin)
        else:
            passCuts = applyATLAScuts(ev,etamax,pTmin)
        if passCuts is False:
            continue
        if getCutFlow:
            topHadronic,topLeptonic,cutFlowEv = passCuts
        else:
            topHadronic,topLeptonic = passCuts

        pA = np.array([topHadronic.px,topHadronic.py,topHadronic.pz,topHadronic.e])
        pB = np.array([topLeptonic.px,topLeptonic.py,topLeptonic.pz,topLeptonic.e])

        pT1.append(np.linalg.norm(pA[0:3]))
        pT2.append(np.linalg.norm(pB[0:3]))
        mTT.append(np.sqrt((pA[-1]+pB[-1])**2-np.linalg.norm(pA[0:3]+pB[0:3])**2))
        weights.append(w)

        if getCutFlow:
            for key in cutFlow:
                cutFlow[key].append(cutFlowEv[key])
        
    dists = {'mTT' : mTT, 'pTh' : pT1, 'pTlep' : pT2, 
             'weights' : np.array(weights), 'nevents' : nevents}
    if getCutFlow:
        dists['cutFlow'] = cutFlow

    return dists

def getInfo(f,labelsDict=None):


    if labelsDict is None:
        labelsDict = {'Top-FormFactorsOneLoop-UFO' : '1-loop', 'Top-EFT-UFO' : 'EFT', 
                      'Top-EFTphysical_simple-UFO' : 'EFT',
                      'SMS-stop-UFO' : 'SM', 'SMS-stop-NLO_SMQCD-UFO' : 'SM',
              'g g > t t~' : r'$g g \to \bar{t} t$', 'g g > t~ t' : r'$g g \to \bar{t} t$',
              'q q > t t~' : r'$q q \to \bar{t} t$', 'q q > t~ t' : r'$q q \to \bar{t} t$',
              'p p > t t~' : r'$p p \to \bar{t} t$', 'p p > t~ t' : r'$p p \to \bar{t} t$'
             }
    
    banner = list(glob.glob(os.path.join(os.path.dirname(f),'*banner*')))[0]
    with open(banner,'r') as bannerF:
        bannerData = bannerF.read()
    
    # Get process data:
    processData = bannerData.split('<MGProcCard>')[1].split('</MGProcCard>')[0]
#     print(processData)
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
        mST = parsSLHA.blocks['MASS'][5000002]
        mChi = parsSLHA.blocks['MASS'][5000012]        
        yDM = list(parsSLHA.blocks['FRBLOCK'].values())[-1]
    else:
        mST = 0.0
        mChi = 0.0
        yDM = 0.0

    if yDM == 0.0:
        model = 'SM'


    
    # Get event data:
    eventData = bannerData.split('<MGGenerationInfo>')[1].split('</MGGenerationInfo>')[0]
    nEvents = eval(eventData.split('\n')[1].split(':')[1].strip())
    xsec = eval(eventData.split('\n')[2].split(':')[1].strip())

    fileInfo = {'model' : model, 'process' : proc, '(mST,mChi,mT,yDM)' : (mST,mChi,mT,yDM),
               'xsec (pb)' : xsec, 'nevents' : nEvents}
    
    return fileInfo

def interpolateData(x,y,z,nx=200,ny=200,method='linear',fill_value=np.nan,xnew=None,ynew=None):

    if x.min() == x.max() or y.min() == y.max(): # Can not interpolate
        return None,None,None
    elif xnew is None or ynew is None:
        xnew = np.linspace(x.min(),x.max(),nx)
        ynew = np.linspace(y.min(),y.max(),ny)

    xi = np.array([list(v) for v in itertools.product(xnew,ynew)])
    znew = griddata(list(zip(x,y)),z,xi=xi, 
                    method=method,fill_value=fill_value)
    znew = np.reshape(znew,(len(xnew),len(ynew)))
    xnew,ynew  = np.meshgrid(xnew,ynew,indexing='ij')

    return xnew,ynew,znew

def getContours(x, y, z, contourValues):
    # Generate contours
    contours = plt.contour(x, y, z, contourValues)
    plt.close() # Close the figure to prevent it from displaying

    contoursDict = {}

    # Iterate through the contour levels using .allsegs
    # contours.allsegs is a list of length len(contourValues)
    # Each element is a list of polygon segments for that level
    for i, segs in enumerate(contours.allsegs):
        cV = contourValues[i]
        
        # Collect all vertices for this contour level
        xData = []
        yData = []
        
        for poly in segs:
            # poly is an (N, 2) array of vertices for one segment
            xData.extend(poly[:, 0])
            yData.extend(poly[:, 1])
        
        if len(xData) == 0:
            continue
            
        contoursDict[cV] = np.array(list(zip(xData, yData)))
    
    return contoursDict

def saveContours(contoursDict,fname,header):

    with open(fname,'w') as f:
        for cV,data in contoursDict.items():
            np.savetxt(f,data,fmt='%.4e',delimiter=',',header=header,comments='\n\n# Contour value=%1.2f \n' %cV)
    print('Contours saved to %s' %fname)

def readContours(fname):

    contoursDict = {}
    with open(fname,'r') as f:
        dataBlocks = f.read().split('#')[1:]
        for data in dataBlocks: 
            data = data.splitlines()
            cV = eval(data[0].split('=')[1])
            dataPts = np.genfromtxt(data,delimiter=',',names=True,skip_header=1)
            contoursDict[cV] = dataPts

    return contoursDict

def Cg(mChi,mST,yDM,gs):
    
    c = -gs*yDM**2/(384*np.pi**2)
    if 1-mChi**2/mST**2 < 0.1:
        r = mChi**2/(5*mST**4)-4*mChi/(5*mST**3) + 11/(10*mST**2)
    else:
        r = mST**6/mChi**6 
        r += 2*(1 - (3*mST**4)/mChi**4) 
        r += 3*mST**2*(1 + 4*np.log(mST/mChi))/mChi**2
        r = r/(mChi**2*(1 - mST**2/mChi**2)**4)
    
    return c*r
               
def Cq(mChi,mST,yDM,gs):
    
    c = 6*gs**2*yDM**2/(3456*np.pi**2)
    if 1-mChi**2/mST**2 < 0.1:
        r = mChi**2/(10*mST**4)-4*mChi/(5*mST**3)+11/(5*mST**2)
    else:
        r = 6*(mChi**2/mST**2)*np.log(mChi**2/mST**2)
        r += -11*mChi**2/mST**2 
        r += 18
        r += -9*mST**2/mChi**2 
        r += 2*mST**4/mChi**4
        r = r*mST**2*mChi**4/((mChi**2-mST**2)**4)
    
    return c*r               

def label_line(fig,line, label_text, 
               near_i=None, near_x=None, near_y=None, 
               rotation_offset=0, offset=(0,0),fontsize=13,
               xmin=None,rotation=None,boxalpha=1.0):
    """call 
        l, = plt.loglog(x, y)
        label_line(l, "text", near_x=0.32)
    """
    def put_label(i):
        """put label at given index"""
        i = min(i, len(x)-2)
        dx = sx[i+1] - sx[i]
        dy = sy[i+1] - sy[i]
        if rotation is None:
            rot = np.rad2deg(np.arctan2(dy, dx)) + rotation_offset
        else:
            rot = rotation
        pos = [(x[i] + x[i+1])/2. + offset[0], (y[i] + y[i+1])/2 + offset[1]]
        if pos[0] > xmin:
            plt.text(pos[0], pos[1], label_text, size=fontsize, 
                     rotation=rot, color = line.get_color(),
                     ha="center", va="center", bbox = dict(ec='1',fc='1',alpha=boxalpha))

    x = line.get_xdata()
    y = line.get_ydata()
    ax = fig.get_axes()[0]
    if ax.get_xscale() == 'log':
        sx = np.log10(x)    # screen space
    else:
        sx = x
    if ax.get_yscale() == 'log':
        sy = np.log10(y)
    else:
        sy = y

    # find index
    if near_i is not None:
        i = near_i
        if i < 0: # sanitize negative i
            i = len(x) + i
        put_label(i)
    elif near_x is not None:
        for i in range(len(x)-2):
            if (x[i] < near_x and x[i+1] >= near_x) or (x[i+1] < near_x and x[i] >= near_x):
                put_label(i)
    elif near_y is not None:
        for i in range(len(y)-2):
            if (y[i] < near_y and y[i+1] >= near_y) or (y[i+1] < near_y and y[i] >= near_y):
                put_label(i)
    else:
        raise ValueError("Need one of near_i, near_x, near_y")
