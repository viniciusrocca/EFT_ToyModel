

import numpy as np

def LF110(m, M, mu):

    if (m-M)**2/((m+M)**22) > 10^(-3):
        return (m**2 - M**2 + m**2*np.log(mu**2/m**2) - M**2*np.log(mu**2/M**2))/(m^2 - M^2)
    else:
        return ((m - 7*M)*(m - M))/(6*M**2) + np.log(mu**2/M**2)

def LF21m1(m, M, mu):

    if (m-M)**2/((m+M)**22) > 10^(-3):
       return (-(m**2 * M**2) + M**4 + (m**4 - 2 * m**2 * M^2) * np.log(mu**2/m**2) + M**4 * np.log(mu**2/M**2))/((m**2 - M**2)**2)
    else:
         return 7/6 + (m*(m - 6*M))/(3 * M**2) + np.log(mu**2/M**2)

def LF210(m, M, mu):

    if (m-M)**2/((m+M)**22) > 10^(-3):
        return (-m**2 + M**2 + M**2 * np.log(m**2/M**2))/((m**2 - M**2)**2)
    else:
        return -1/6*(4* m**2 - 12*m*M + 11* M**2)/(M**4)
    
def LF220(m, M, mu):
    
    if (m-M)**2/((m+M)**22) > 10^(-3):
        return (-2* m**2 + 2* M**2 + (m**2 + M**2)*np.log(m**2/M**2))/((m**2 - M**2)**3)
    else:
        return (13 * m**2 - 36*m*M + 28 * M**2)/(30 * M**6)
    
def LF22m1(m,M, mu):

    if (m-M)**2/((m+M)**22) > 10^(-3):
        return (-m**4 + M**4 + 2 * m**2 * M**2 * np.log(m**2/M**2))/((m**2 - M**2)**3)
    else:
        return  -1/30*(7 * m**2 - 24*m*M + 27 * M**2)/M**4

def LF31m1(m,M, mu):

    if (m-M)**2/((m+M)**22) > 10^(-3):
        return -1/2*(m**4 - 4 * m**2 * M^2 + 3 * M**4 + 2 * M**4 * np.log(m**2/M**2))/((m**2 - M**2)**3)
    else:
        return -1/60*(33 * m**2 - 96*m*M + 83 * M**2)/(M**4)
    

def LF41m2(m,M, mu):
     
     if (m-M)**2/((m+M)**22) > 10^(-3):
         return (-2 * m**6 + 9 * m**4 * M**2 - 18 * m**2 * M**4 + 11 * M**6 + 6 * M**6 * np.log(m**2/M**2))/(6*(m**2 - M**2)**4)
     else:
         -1/60*(28 * m**2 - 80*m*M + 67* M**2)/(M**4)
         

def cdd(mPsiT, mSDM, yDM, gs, g1):

    Pi = np.pi
    cdda = (-27*(gs**4))/(12960*(mPsiT**2)*(Pi**2))
    cddb = ((9*(gs**4)))/(12960*(mPsiT**2)*(Pi**2))
    cddc = ((-16*(g1**4)))/(12960*(mPsiT**2)*(Pi**2))

    return cdda + cddb + cddc

def ced(mPsiT, mSDM, yDM, gs, g1):

    Pi = np.pi
    c = -1/135*(g1**4)/((mPsiT**2)*(Pi**2))

    return c

def cee(mPsiT, mSDM, yDM, gs, g1):
    
    Pi = np.pi
    c = -1/180*(g1**4)/((mPsiT**2)*(Pi**2))

    return c

def ceu(mPsiT, mSDM, yDM, gs, g1, t_op = True):

    Pi = np.pi
    mu = mPsiT
    ceua = (2 * g1**4)/(135 * mPsiT**2 * Pi**2)
    if t_op == True:
        ceub = (g1**2 * yDM**2 * (3 * LF31m1(mPsiT,mSDM,mu) - LF41m2(mPsiT,mSDM,mu)))/(144 * Pi**2)
        return ceua + ceub
    else:
        return ceua
    
def cG(mPsiT, mSDM, yDM, gs, g1):

    Pi = np.pi
    c = -1/2880 * gs**3 /(mPsiT**2 * Pi**2)
    return c

def cH(mPsiT, mSDM, lamHs, gs, g1):

    Pi = np.pi
    c = -1/1536 * lamHs**3 /(mSDM**2 * Pi**2)
    return c

def cHBox(mPsiT, mSDM, lamHs, gs, g1):

    Pi = np.pi
    cHBoxa = -1/23040 * ((64 * g1**4)/(mPsiT**2) )/(Pi**2)
    cHBoxb = -1/23040 * ((15 * lamHs**2)/mSDM**2)/(Pi**2)
    return cHBoxa + cHBoxb

def cHd(mPsiT, mSDM, yDM, gs, g1):

    Pi = np.pi
    c = (g1**4)/(270 * mPsiT**2 * Pi**2)
    return c

def cHD(mPsiT, mSDM, yDM, gs, g1):
    
    Pi = np.pi
    c = -1/90 * g1**4 / (mPsiT**2 * Pi**2)
    return c

def cHe(mPsiT, mSDM, yDM, gs, g1):
        
    Pi = np.pi
    c=(g1**4)/(90 * mPsiT**2 * Pi**2)
    return c

def cHl1(mPsiT, mSDM, yDM, gs, g1):

    Pi = np.pi
    c = (g1**4)/(180 * mPsiT**2 * Pi**2)
    return c

def cHq1(mPsiT, mSDM, yDM, gs, g1, vev, ymt, t_op = True):

    Pi = np.pi
    mu = mPsiT
    cHq1a = -1/540 * (g1**4)/(mPsiT**2 * Pi**2)
    if t_op == True:
        cHq1b = (-1)*(yDM**2 * ymt**2 * (LF210(mPsiT,mSDM,mu) - 2 * LF31m1(mPsiT,mSDM,mu) + LF41m2(mPsiT,mSDM,mu)))/(32 * Pi**2 * vev**2)
        return cHq1a + cHq1b
    else:
        return cHq1a
    
def cHq3(mPsiT, mSDM, yDM, gs, g1, vev, ymt, t_op = True):

    Pi = np.Pi
    mu = mPsiT
    c = (yDM**2 * ymt**2 * (LF210(mPsiT,mSDM,mu) - 2 * LF31m1(mPsiT,mSDM,mu) + LF41m2(mPsiT,mSDM,mu)))/(32 * Pi**2 * vev**2)
    return c

def cHu(mPsiT, mSDM, yDM, gs, g1, t_op = True):

    Pi = np.pi
    mu = mPsiT
    cHua = -1/135 * (g1**4)/(mPsiT**2 * Pi**2)
    if t_op == True:
        cHub = (g1**2 * yDM**2 * (-3*LF31m1(mPsiT,mSDM,mu) + LF41m2(mPsiT,mSDM,mu)))/(288*Pi^2)
        return cHua + cHub
    else:
        return cHua


def cld(mPsiT, mSDM, yDM, gs, g1):

    Pi = np.pi
    c =  -1/270*(g1**4)/(mPsiT**2 * Pi**2)
    return c

def cle(mPsiT, mSDM, yDM, gs, g1):

    Pi = np.pi
    c = -1/90*(g1**4)/(mPsiT**2 * Pi**2)
    return c

def cll(mPsiT, mSDM, yDM, gs, g1):

    Pi = np.pi
    c = -1/360*(g1**4)/(mPsiT**2 * Pi**2)
    return c

def clq1(mPsiT, mSDM, yDM, gs, g1):

    Pi = np.pi
    c = (g1**4)/(540 * mPsiT**2 * Pi**2)
    return c

def clu(mPsiT, mSDM, yDM, gs, g1, t_op = True):

    Pi = np.pi
    mu = mPsiT
    clua = (g1**4)/(135 * mPsiT**2 * Pi**2)
    if t_op == True:
        club = (g1**2 * yDM**2 * (3*LF31m1(mPsiT,mSDM,mu) - LF41m2(mPsiT,mSDM,mu)))/(288 * Pi**2)
        return clua + club
    else:
        return clua
    
def cqd1(mPsiT, mSDM, yDM, gs, g1):


    Pi = np.pi
    c = (g1**4)/(810 * mPsiT**2 * Pi**2)
    return c

def cqd8(mPsiT, mSDM, yDM, gs, g1):

    Pi = np.pi
    c = 1/120*(gs**4)/(mPsiT**2 * Pi**2)
    return c

def cqe(mPsiT, mSDM, yDM, gs, g1):

    Pi = np.pi
    c = (g1**4)/(270 * mPsiT**2 * Pi**2)
    return c

def cqq1(mPsiT, mSDM, yDM, gs, g1):

    Pi = np.pi
    cqq1a = (-27*gs**4)/(25920 * mPsiT**2 * Pi**2)
    cqq1b = (-8*g1**4 )/(25920 * mPsiT**2 * Pi**2)
    cqq1c = ( 18*gs**4)/(25920 * mPsiT**2 * Pi**2)
    return cqq1a + cqq1b + cqq1c

def cqq3(mPsiT, mSDM, yDM, gs, g1):

    Pi = np.pi
    c = -1/960*(gs**4)/(mPsiT**2 * Pi**2)
    return c

def cqu1(mPsiT, mSDM, yDM, gs, g1, t_op = True):

    Pi = np.pi
    mu = mPsiT
    cqu1a = -1/405*(g1**4)/(mPsiT**2 * Pi**2)
    if t_op == True:
        
        cqu1b = (g1**2 * yDM**2 * (-3*LF31m1(mPsiT,mSDM,mu) + LF41m2(mPsiT,mSDM,mu)))/(864 * Pi**2)
        return cqu1a + cqu1b
    else:
        return cqu1a
    
def cqu8(mPsiT, mSDM, yDM, gs, g1, t_op = True):

    Pi = np.pi
    mu = mPsiT
    cqu8a = -1/120*(gs**4)/(mPsiT**2 * Pi**2)
    if t_op == True:
        cqu8b = (gs**2 * yDM**2 * (-3*LF31m1(mPsiT,mSDM,mu) + LF41m2(mPsiT,mSDM,mu)))/(96 * Pi**2)
        return cqu8a + cqu8b
    else:
        return cqu8a
    
def cuB(mPsiT, mSDM, yDM, gs, g1, ymt, vev):

    Pi = np.Pi
    mu = mPsiT
    c = (g1 * yDM**2 * ymt * (-LF31m1(mPsiT,mSDM,mu) + LF41m2(mPsiT,mSDM,mu)))/(48 * np.sqrt(2) * Pi**2 * vev)
    return c

def cud1(mPsiT, mSDM, yDM, gs, g1, t_op = True):

    Pi = np.pi
    mu = mPsiT
    cud1a = (2*g1**4)/(405 * mPsiT**2 * Pi**2)
    if t_op == True:
        cud1b = (g1**2 * yDM**2 * (3*LF31m1(mPsiT,mSDM,mu) - LF41m2(mPsiT,mSDM,mu)))/(432 * Pi**2)
        return cud1a + cud1b
    else:
        return cud1a
    
def cud8(mPsiT, mSDM, yDM, gs, g1, t_op = True):

    Pi = np.pi
    mu = mPsiT
    cud8a = -1/120*(gs**4)/(mPsiT**2 * Pi**2)
    if t_op == True:
        cud8b = (gs**2 * yDM**2 * (-3*LF31m1(mPsiT,mSDM,mu) + LF41m2(mPsiT,mSDM,mu)))/(96 * Pi**2) 
        return cud8a + cud8b
    else:
        return cud8a
    
def cuG(mPsiT, mSDM, yDM, gs, g1, ymt, vev):

    Pi = np.pi
    mu = mPsiT
    c = (gs * yDM**2 * ymt * (-LF31m1(mPsiT,mSDM,mu) + LF41m2(mPsiT,mSDM,mu)))/(32 * np.sqrt(2) * Pi**2 * vev)
    return c

def cuH(mPsiT, mSDM, yDM, gs, g1, lamHs, ymt, vev, t_op = True):

    Pi = np.pi
    mu = mPsiT
    if t_op == True:
        cuHa = -1/64 * (yDM**2 * ymt * lamHs * vev**2 * (-2*LF210(mSDM,mPsiT,mu) + LF22m1(mSDM,mPsiT,mu)) )/(np.sqrt(2) * Pi**2 * vev**3)
        cuHb = -1/8 * (yDM**2 * ymt**3 * (LF210(mPsiT,mSDM,mu) - 2*LF31m1(mPsiT,mSDM,mu) + LF41m2(mPsiT,mSDM,mu)))/(np.sqrt(2) * Pi**2 * vev**3)
        return cuHa + cuHb
    else:
        return 0
    
def cuu(mPsiT, mSDM, yDM, gs, g1, ymt, vev, t_op = True):

    Pi = np.pi
    mu = mPsiT
    cuua = (-27 * gs**4)/(12960 * mPsiT**2 * Pi**2)
    cuub = (-64 * g1**4)/(12960 * mPsiT**2 * Pi**2)
    cuuc = (9 * gs**4)/(12960 * mPsiT**2 * Pi**2)
    if t_op == True:
        cuud = -(yDM**2 * 8 * g1**2 * (3*LF31m1(mPsiT,mSDM,mu) - LF41m2(mPsiT,mSDM,mu)))/(1728 * Pi**2)
        cuue = -(yDM**2 * (-3 * gs**2) * ( 3*LF31m1(mPsiT,mSDM,mu) - LF41m2(mPsiT,mSDM,mu)))/(1728 * Pi**2)
        cuuf = (-9 * yDM**2 * gs**2 * ( 3*LF31m1(mPsiT,mSDM,mu) - LF41m2(mPsiT,mSDM,mu)))/(1728 * Pi**2)
        return cuua + cuub + cuuc + cuud + cuue + cuuf
    else:
        return cuua + cuub + cuuc

