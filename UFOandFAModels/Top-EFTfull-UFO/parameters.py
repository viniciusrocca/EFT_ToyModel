# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Linux x86 (64-bit) (July 16, 2024)
# Date: Thu 19 Jun 2025 16:02:55



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

yDM = Parameter(name = 'yDM',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = 'y_{\\text{DM}}',
                lhablock = 'FRBlock',
                lhacode = [ 1 ])

lamHs = Parameter(name = 'lamHs',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = '\\lambda _{\\text{Hs}}',
                  lhablock = 'FRBlock',
                  lhacode = [ 2 ])

lamS = Parameter(name = 'lamS',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = '\\lambda _S',
                 lhablock = 'FRBlock',
                 lhacode = [ 3 ])

mSDM = Parameter(name = 'mSDM',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = 'm_{\\text{SDM}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 4 ])

mPsiT = Parameter(name = 'mPsiT',
                  nature = 'external',
                  type = 'real',
                  value = 500.,
                  texname = 'm_{\\psi _T}',
                  lhablock = 'FRBlock',
                  lhacode = [ 5 ])

mu = Parameter(name = 'mu',
               nature = 'external',
               type = 'real',
               value = 1000.,
               texname = '\\mu',
               lhablock = 'FRBlock',
               lhacode = [ 6 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

cH = Parameter(name = 'cH',
               nature = 'internal',
               type = 'real',
               value = '-0.0006510416666666666*lamHs**3/(cmath.pi**2*mSDM**2)',
               texname = 'c_H')

cHBoxb = Parameter(name = 'cHBoxb',
                   nature = 'internal',
                   type = 'real',
                   value = '-0.0006510416666666666*lamHs**2/(cmath.pi**2*mSDM**2)',
                   texname = 'c_{\\text{HBoxb}}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

cdda = Parameter(name = 'cdda',
                 nature = 'internal',
                 type = 'real',
                 value = '-0.0020833333333333333*G**4/(cmath.pi**2*mPsiT**2)',
                 texname = 'c_{\\text{dda}}')

cddb = Parameter(name = 'cddb',
                 nature = 'internal',
                 type = 'real',
                 value = 'G**4/(1440.*cmath.pi**2*mPsiT**2)',
                 texname = 'c_{\\text{ddb}}')

cG = Parameter(name = 'cG',
               nature = 'internal',
               type = 'real',
               value = '-0.00034722222222222224*G**3/(cmath.pi**2*mPsiT**2)',
               texname = 'c_G')

cqd8 = Parameter(name = 'cqd8',
                 nature = 'internal',
                 type = 'real',
                 value = 'G**4/(120.*cmath.pi**2*mPsiT**2)',
                 texname = 'c_{\\text{qd8}}')

cqq1a = Parameter(name = 'cqq1a',
                  nature = 'internal',
                  type = 'real',
                  value = '-0.0010416666666666667*G**4/(cmath.pi**2*mPsiT**2)',
                  texname = 'c_{\\text{qq1a}}')

cqq1c = Parameter(name = 'cqq1c',
                  nature = 'internal',
                  type = 'real',
                  value = 'G**4/(1440.*cmath.pi**2*mPsiT**2)',
                  texname = 'c_{\\text{qq1c}}')

cqq3 = Parameter(name = 'cqq3',
                 nature = 'internal',
                 type = 'real',
                 value = '-0.0010416666666666667*G**4/(cmath.pi**2*mPsiT**2)',
                 texname = 'c_{\\text{qq3}}')

cqu8a = Parameter(name = 'cqu8a',
                  nature = 'internal',
                  type = 'real',
                  value = '-0.008333333333333333*G**4/(cmath.pi**2*mPsiT**2)',
                  texname = 'c_{\\text{qu8a}}')

cud8a = Parameter(name = 'cud8a',
                  nature = 'internal',
                  type = 'real',
                  value = '-0.008333333333333333*G**4/(cmath.pi**2*mPsiT**2)',
                  texname = 'c_{\\text{ud8a}}')

cuua = Parameter(name = 'cuua',
                 nature = 'internal',
                 type = 'real',
                 value = '-0.0020833333333333333*G**4/(cmath.pi**2*mPsiT**2)',
                 texname = 'c_{\\text{uua}}')

cuuc = Parameter(name = 'cuuc',
                 nature = 'internal',
                 type = 'real',
                 value = 'G**4/(1440.*cmath.pi**2*mPsiT**2)',
                 texname = 'c_{\\text{uuc}}')

cqu8b = Parameter(name = 'cqu8b',
                  nature = 'internal',
                  type = 'real',
                  value = '((-3*( -0.5*(mPsiT**4 - 4*mPsiT**2*mSDM**2 + 3*mSDM**4 + 2*mSDM**4*cmath.log(mPsiT**2/mSDM**2))/(mPsiT**2 - mSDM**2)**3 if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(33*mPsiT**2 - 96*mPsiT*mSDM + 83*mSDM**2)/mSDM**4 ) + ( (-2*mPsiT**6 + 9*mPsiT**4*mSDM**2 - 18*mPsiT**2*mSDM**4 + 11*mSDM**6 + 6*mSDM**6*cmath.log(mPsiT**2/mSDM**2))/(6.*(mPsiT**2 - mSDM**2)**4) if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(28*mPsiT**2 - 80*mPsiT*mSDM + 67*mSDM**2)/mSDM**4 ))*G**2*yDM**2)/(96.*cmath.pi**2)',
                  texname = 'c_{\\text{qu8b}}')

cud8b = Parameter(name = 'cud8b',
                  nature = 'internal',
                  type = 'real',
                  value = '((-3*( -0.5*(mPsiT**4 - 4*mPsiT**2*mSDM**2 + 3*mSDM**4 + 2*mSDM**4*cmath.log(mPsiT**2/mSDM**2))/(mPsiT**2 - mSDM**2)**3 if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(33*mPsiT**2 - 96*mPsiT*mSDM + 83*mSDM**2)/mSDM**4 ) + ( (-2*mPsiT**6 + 9*mPsiT**4*mSDM**2 - 18*mPsiT**2*mSDM**4 + 11*mSDM**6 + 6*mSDM**6*cmath.log(mPsiT**2/mSDM**2))/(6.*(mPsiT**2 - mSDM**2)**4) if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(28*mPsiT**2 - 80*mPsiT*mSDM + 67*mSDM**2)/mSDM**4 ))*G**2*yDM**2)/(96.*cmath.pi**2)',
                  texname = 'c_{\\text{ud8b}}')

cuue = Parameter(name = 'cuue',
                 nature = 'internal',
                 type = 'real',
                 value = '((3*( -0.5*(mPsiT**4 - 4*mPsiT**2*mSDM**2 + 3*mSDM**4 + 2*mSDM**4*cmath.log(mPsiT**2/mSDM**2))/(mPsiT**2 - mSDM**2)**3 if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(33*mPsiT**2 - 96*mPsiT*mSDM + 83*mSDM**2)/mSDM**4 ) - ( (-2*mPsiT**6 + 9*mPsiT**4*mSDM**2 - 18*mPsiT**2*mSDM**4 + 11*mSDM**6 + 6*mSDM**6*cmath.log(mPsiT**2/mSDM**2))/(6.*(mPsiT**2 - mSDM**2)**4) if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(28*mPsiT**2 - 80*mPsiT*mSDM + 67*mSDM**2)/mSDM**4 ))*G**2*yDM**2)/(576.*cmath.pi**2)',
                 texname = 'c_{\\text{uue}}')

cuuf = Parameter(name = 'cuuf',
                 nature = 'internal',
                 type = 'real',
                 value = '-0.005208333333333333*((3*( -0.5*(mPsiT**4 - 4*mPsiT**2*mSDM**2 + 3*mSDM**4 + 2*mSDM**4*cmath.log(mPsiT**2/mSDM**2))/(mPsiT**2 - mSDM**2)**3 if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(33*mPsiT**2 - 96*mPsiT*mSDM + 83*mSDM**2)/mSDM**4 ) - ( (-2*mPsiT**6 + 9*mPsiT**4*mSDM**2 - 18*mPsiT**2*mSDM**4 + 11*mSDM**6 + 6*mSDM**6*cmath.log(mPsiT**2/mSDM**2))/(6.*(mPsiT**2 - mSDM**2)**4) if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(28*mPsiT**2 - 80*mPsiT*mSDM + 67*mSDM**2)/mSDM**4 ))*G**2*yDM**2)/cmath.pi**2',
                 texname = 'c_{\\text{uuf}}')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

cddc = Parameter(name = 'cddc',
                 nature = 'internal',
                 type = 'real',
                 value = '-0.0012345679012345679*g1**4/(cmath.pi**2*mPsiT**2)',
                 texname = 'c_{\\text{ddc}}')

ced = Parameter(name = 'ced',
                nature = 'internal',
                type = 'real',
                value = '-0.007407407407407408*g1**4/(cmath.pi**2*mPsiT**2)',
                texname = 'c_{\\text{ed}}')

cee = Parameter(name = 'cee',
                nature = 'internal',
                type = 'real',
                value = '-0.005555555555555556*g1**4/(cmath.pi**2*mPsiT**2)',
                texname = 'c_e')

ceua = Parameter(name = 'ceua',
                 nature = 'internal',
                 type = 'real',
                 value = '(2*g1**4)/(135.*cmath.pi**2*mPsiT**2)',
                 texname = 'c_{\\text{eua}}')

cHBoxa = Parameter(name = 'cHBoxa',
                   nature = 'internal',
                   type = 'real',
                   value = '-0.002777777777777778*g1**4/(cmath.pi**2*mPsiT**2)',
                   texname = 'c_{\\text{HBoxa}}')

cHd = Parameter(name = 'cHd',
                nature = 'internal',
                type = 'real',
                value = 'g1**4/(270.*cmath.pi**2*mPsiT**2)',
                texname = 'c_{\\text{Hd}}')

cHD = Parameter(name = 'cHD',
                nature = 'internal',
                type = 'real',
                value = '-0.011111111111111112*g1**4/(cmath.pi**2*mPsiT**2)',
                texname = 'c_{\\text{HD}}')

cHe = Parameter(name = 'cHe',
                nature = 'internal',
                type = 'real',
                value = 'g1**4/(90.*cmath.pi**2*mPsiT**2)',
                texname = 'c_{\\text{He}}')

cHl1 = Parameter(name = 'cHl1',
                 nature = 'internal',
                 type = 'real',
                 value = 'g1**4/(180.*cmath.pi**2*mPsiT**2)',
                 texname = 'c_{\\text{Hl1}}')

cHq1a = Parameter(name = 'cHq1a',
                  nature = 'internal',
                  type = 'real',
                  value = '-0.001851851851851852*g1**4/(cmath.pi**2*mPsiT**2)',
                  texname = 'c_{\\text{Hq1a}}')

cHua = Parameter(name = 'cHua',
                 nature = 'internal',
                 type = 'real',
                 value = '-0.007407407407407408*g1**4/(cmath.pi**2*mPsiT**2)',
                 texname = 'c_{\\text{Hua}}')

cld = Parameter(name = 'cld',
                nature = 'internal',
                type = 'real',
                value = '-0.003703703703703704*g1**4/(cmath.pi**2*mPsiT**2)',
                texname = 'c_{\\text{ld}}')

cle = Parameter(name = 'cle',
                nature = 'internal',
                type = 'real',
                value = '-0.011111111111111112*g1**4/(cmath.pi**2*mPsiT**2)',
                texname = 'c_{\\text{le}}')

cll = Parameter(name = 'cll',
                nature = 'internal',
                type = 'real',
                value = '-0.002777777777777778*g1**4/(cmath.pi**2*mPsiT**2)',
                texname = 'c_{\\text{ll}}')

clq1 = Parameter(name = 'clq1',
                 nature = 'internal',
                 type = 'real',
                 value = 'g1**4/(540.*cmath.pi**2*mPsiT**2)',
                 texname = 'c_{\\text{lq1}}')

clua = Parameter(name = 'clua',
                 nature = 'internal',
                 type = 'real',
                 value = 'g1**4/(135.*cmath.pi**2*mPsiT**2)',
                 texname = 'c_{\\text{lua}}')

cqd1 = Parameter(name = 'cqd1',
                 nature = 'internal',
                 type = 'real',
                 value = 'g1**4/(810.*cmath.pi**2*mPsiT**2)',
                 texname = 'c_{\\text{qd1}}')

cqe = Parameter(name = 'cqe',
                nature = 'internal',
                type = 'real',
                value = 'g1**4/(270.*cmath.pi**2*mPsiT**2)',
                texname = 'c_{\\text{qe}}')

cqq1b = Parameter(name = 'cqq1b',
                  nature = 'internal',
                  type = 'real',
                  value = '-0.00030864197530864197*g1**4/(cmath.pi**2*mPsiT**2)',
                  texname = 'c_{\\text{qq1b}}')

cqu1a = Parameter(name = 'cqu1a',
                  nature = 'internal',
                  type = 'real',
                  value = '-0.0024691358024691358*g1**4/(cmath.pi**2*mPsiT**2)',
                  texname = 'c_{\\text{qu1a}}')

cud1a = Parameter(name = 'cud1a',
                  nature = 'internal',
                  type = 'real',
                  value = '(2*g1**4)/(405.*cmath.pi**2*mPsiT**2)',
                  texname = 'c_{\\text{ud1a}}')

cuub = Parameter(name = 'cuub',
                 nature = 'internal',
                 type = 'real',
                 value = '(-2*g1**4)/(405.*cmath.pi**2*mPsiT**2)',
                 texname = 'c_{\\text{uub}}')

ceub = Parameter(name = 'ceub',
                 nature = 'internal',
                 type = 'real',
                 value = '((3*( -0.5*(mPsiT**4 - 4*mPsiT**2*mSDM**2 + 3*mSDM**4 + 2*mSDM**4*cmath.log(mPsiT**2/mSDM**2))/(mPsiT**2 - mSDM**2)**3 if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(33*mPsiT**2 - 96*mPsiT*mSDM + 83*mSDM**2)/mSDM**4 ) - ( (-2*mPsiT**6 + 9*mPsiT**4*mSDM**2 - 18*mPsiT**2*mSDM**4 + 11*mSDM**6 + 6*mSDM**6*cmath.log(mPsiT**2/mSDM**2))/(6.*(mPsiT**2 - mSDM**2)**4) if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(28*mPsiT**2 - 80*mPsiT*mSDM + 67*mSDM**2)/mSDM**4 ))*g1**2*yDM**2)/(144.*cmath.pi**2)',
                 texname = 'c_{\\text{eub}}')

cHq1b = Parameter(name = 'cHq1b',
                  nature = 'internal',
                  type = 'real',
                  value = '-0.03125*((-2*( -0.5*(mPsiT**4 - 4*mPsiT**2*mSDM**2 + 3*mSDM**4 + 2*mSDM**4*cmath.log(mPsiT**2/mSDM**2))/(mPsiT**2 - mSDM**2)**3 if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(33*mPsiT**2 - 96*mPsiT*mSDM + 83*mSDM**2)/mSDM**4 ) + ( (-2*mPsiT**6 + 9*mPsiT**4*mSDM**2 - 18*mPsiT**2*mSDM**4 + 11*mSDM**6 + 6*mSDM**6*cmath.log(mPsiT**2/mSDM**2))/(6.*(mPsiT**2 - mSDM**2)**4) if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(28*mPsiT**2 - 80*mPsiT*mSDM + 67*mSDM**2)/mSDM**4 ) + ( (-mPsiT**2 + mSDM**2 + mSDM**2*cmath.log(mPsiT**2/mSDM**2))/(mPsiT**2 - mSDM**2)**2 if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.16666666666666666*(4*mPsiT**2 - 12*mPsiT*mSDM + 11*mSDM**2)/mSDM**4 ))*yDM**2*ymt**2)/(cmath.pi**2*vev**2)',
                  texname = 'c_{\\text{Hq1b}}')

cHq3 = Parameter(name = 'cHq3',
                 nature = 'internal',
                 type = 'real',
                 value = '((-2*( -0.5*(mPsiT**4 - 4*mPsiT**2*mSDM**2 + 3*mSDM**4 + 2*mSDM**4*cmath.log(mPsiT**2/mSDM**2))/(mPsiT**2 - mSDM**2)**3 if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(33*mPsiT**2 - 96*mPsiT*mSDM + 83*mSDM**2)/mSDM**4 ) + ( (-2*mPsiT**6 + 9*mPsiT**4*mSDM**2 - 18*mPsiT**2*mSDM**4 + 11*mSDM**6 + 6*mSDM**6*cmath.log(mPsiT**2/mSDM**2))/(6.*(mPsiT**2 - mSDM**2)**4) if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(28*mPsiT**2 - 80*mPsiT*mSDM + 67*mSDM**2)/mSDM**4 ) + ( (-mPsiT**2 + mSDM**2 + mSDM**2*cmath.log(mPsiT**2/mSDM**2))/(mPsiT**2 - mSDM**2)**2 if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.16666666666666666*(4*mPsiT**2 - 12*mPsiT*mSDM + 11*mSDM**2)/mSDM**4 ))*yDM**2*ymt**2)/(32.*cmath.pi**2*vev**2)',
                 texname = 'c_{\\text{Hq3}}')

cHub = Parameter(name = 'cHub',
                 nature = 'internal',
                 type = 'real',
                 value = '((-3*( -0.5*(mPsiT**4 - 4*mPsiT**2*mSDM**2 + 3*mSDM**4 + 2*mSDM**4*cmath.log(mPsiT**2/mSDM**2))/(mPsiT**2 - mSDM**2)**3 if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(33*mPsiT**2 - 96*mPsiT*mSDM + 83*mSDM**2)/mSDM**4 ) + ( (-2*mPsiT**6 + 9*mPsiT**4*mSDM**2 - 18*mPsiT**2*mSDM**4 + 11*mSDM**6 + 6*mSDM**6*cmath.log(mPsiT**2/mSDM**2))/(6.*(mPsiT**2 - mSDM**2)**4) if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(28*mPsiT**2 - 80*mPsiT*mSDM + 67*mSDM**2)/mSDM**4 ))*g1**2*yDM**2)/(288.*cmath.pi**2)',
                 texname = 'c_{\\text{Hub}}')

club = Parameter(name = 'club',
                 nature = 'internal',
                 type = 'real',
                 value = '((3*( -0.5*(mPsiT**4 - 4*mPsiT**2*mSDM**2 + 3*mSDM**4 + 2*mSDM**4*cmath.log(mPsiT**2/mSDM**2))/(mPsiT**2 - mSDM**2)**3 if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(33*mPsiT**2 - 96*mPsiT*mSDM + 83*mSDM**2)/mSDM**4 ) - ( (-2*mPsiT**6 + 9*mPsiT**4*mSDM**2 - 18*mPsiT**2*mSDM**4 + 11*mSDM**6 + 6*mSDM**6*cmath.log(mPsiT**2/mSDM**2))/(6.*(mPsiT**2 - mSDM**2)**4) if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(28*mPsiT**2 - 80*mPsiT*mSDM + 67*mSDM**2)/mSDM**4 ))*g1**2*yDM**2)/(288.*cmath.pi**2)',
                 texname = 'c_{\\text{lub}}')

cqu1b = Parameter(name = 'cqu1b',
                  nature = 'internal',
                  type = 'real',
                  value = '((-3*( -0.5*(mPsiT**4 - 4*mPsiT**2*mSDM**2 + 3*mSDM**4 + 2*mSDM**4*cmath.log(mPsiT**2/mSDM**2))/(mPsiT**2 - mSDM**2)**3 if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(33*mPsiT**2 - 96*mPsiT*mSDM + 83*mSDM**2)/mSDM**4 ) + ( (-2*mPsiT**6 + 9*mPsiT**4*mSDM**2 - 18*mPsiT**2*mSDM**4 + 11*mSDM**6 + 6*mSDM**6*cmath.log(mPsiT**2/mSDM**2))/(6.*(mPsiT**2 - mSDM**2)**4) if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(28*mPsiT**2 - 80*mPsiT*mSDM + 67*mSDM**2)/mSDM**4 ))*g1**2*yDM**2)/(864.*cmath.pi**2)',
                  texname = 'c_{\\text{qu1b}}')

cuB = Parameter(name = 'cuB',
                nature = 'internal',
                type = 'real',
                value = '((-( -0.5*(mPsiT**4 - 4*mPsiT**2*mSDM**2 + 3*mSDM**4 + 2*mSDM**4*cmath.log(mPsiT**2/mSDM**2))/(mPsiT**2 - mSDM**2)**3 if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(33*mPsiT**2 - 96*mPsiT*mSDM + 83*mSDM**2)/mSDM**4 ) + ( (-2*mPsiT**6 + 9*mPsiT**4*mSDM**2 - 18*mPsiT**2*mSDM**4 + 11*mSDM**6 + 6*mSDM**6*cmath.log(mPsiT**2/mSDM**2))/(6.*(mPsiT**2 - mSDM**2)**4) if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(28*mPsiT**2 - 80*mPsiT*mSDM + 67*mSDM**2)/mSDM**4 ))*g1*yDM**2*ymt)/(48.*cmath.pi**2*vev*cmath.sqrt(2))',
                texname = 'c_{\\text{uB}}')

cud1b = Parameter(name = 'cud1b',
                  nature = 'internal',
                  type = 'real',
                  value = '((3*( -0.5*(mPsiT**4 - 4*mPsiT**2*mSDM**2 + 3*mSDM**4 + 2*mSDM**4*cmath.log(mPsiT**2/mSDM**2))/(mPsiT**2 - mSDM**2)**3 if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(33*mPsiT**2 - 96*mPsiT*mSDM + 83*mSDM**2)/mSDM**4 ) - ( (-2*mPsiT**6 + 9*mPsiT**4*mSDM**2 - 18*mPsiT**2*mSDM**4 + 11*mSDM**6 + 6*mSDM**6*cmath.log(mPsiT**2/mSDM**2))/(6.*(mPsiT**2 - mSDM**2)**4) if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(28*mPsiT**2 - 80*mPsiT*mSDM + 67*mSDM**2)/mSDM**4 ))*g1**2*yDM**2)/(432.*cmath.pi**2)',
                  texname = 'c_{\\text{ud1b}}')

cuHa = Parameter(name = 'cuHa',
                 nature = 'internal',
                 type = 'real',
                 value = '-0.015625*((-2*( (mPsiT**2 - mSDM**2 + mPsiT**2*cmath.log(mSDM**2/mPsiT**2))/(-mPsiT**2 + mSDM**2)**2 if (-mPsiT + mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.16666666666666666*(11*mPsiT**2 - 12*mPsiT*mSDM + 4*mSDM**2)/mPsiT**4 ) + ( (-mSDM**4 + PsiT**4 + 2*mSDM**2*PsiT**2*cmath.log(mSDM**2/PsiT**2))/(mSDM**2 - PsiT**2)**3 if (mSDM - PsiT)**2/(mSDM + PsiT)**2>0.001 else -0.03333333333333333*(7*mSDM**2 - 24*mSDM*PsiT + 27*PsiT**2)/PsiT**4 ))*lamHs*yDM**2*ymt)/(cmath.pi**2*vev*cmath.sqrt(2))',
                 texname = 'c_{\\text{uHa}}')

cuHb = Parameter(name = 'cuHb',
                 nature = 'internal',
                 type = 'real',
                 value = '-0.125*((-2*( -0.5*(mPsiT**4 - 4*mPsiT**2*mSDM**2 + 3*mSDM**4 + 2*mSDM**4*cmath.log(mPsiT**2/mSDM**2))/(mPsiT**2 - mSDM**2)**3 if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(33*mPsiT**2 - 96*mPsiT*mSDM + 83*mSDM**2)/mSDM**4 ) + ( (-2*mPsiT**6 + 9*mPsiT**4*mSDM**2 - 18*mPsiT**2*mSDM**4 + 11*mSDM**6 + 6*mSDM**6*cmath.log(mPsiT**2/mSDM**2))/(6.*(mPsiT**2 - mSDM**2)**4) if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(28*mPsiT**2 - 80*mPsiT*mSDM + 67*mSDM**2)/mSDM**4 ) + ( (-mPsiT**2 + mSDM**2 + mSDM**2*cmath.log(mPsiT**2/mSDM**2))/(mPsiT**2 - mSDM**2)**2 if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.16666666666666666*(4*mPsiT**2 - 12*mPsiT*mSDM + 11*mSDM**2)/mSDM**4 ))*yDM**2*ymt**3)/(cmath.pi**2*vev**3*cmath.sqrt(2))',
                 texname = 'c_{\\text{uH}}')

cuud = Parameter(name = 'cuud',
                 nature = 'internal',
                 type = 'real',
                 value = '-0.004629629629629629*((3*( -0.5*(mPsiT**4 - 4*mPsiT**2*mSDM**2 + 3*mSDM**4 + 2*mSDM**4*cmath.log(mPsiT**2/mSDM**2))/(mPsiT**2 - mSDM**2)**3 if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(33*mPsiT**2 - 96*mPsiT*mSDM + 83*mSDM**2)/mSDM**4 ) - ( (-2*mPsiT**6 + 9*mPsiT**4*mSDM**2 - 18*mPsiT**2*mSDM**4 + 11*mSDM**6 + 6*mSDM**6*cmath.log(mPsiT**2/mSDM**2))/(6.*(mPsiT**2 - mSDM**2)**4) if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(28*mPsiT**2 - 80*mPsiT*mSDM + 67*mSDM**2)/mSDM**4 ))*g1**2*yDM**2)/cmath.pi**2',
                 texname = 'c_{\\text{uud}}')

cuG = Parameter(name = 'cuG',
                nature = 'internal',
                type = 'real',
                value = '((-( -0.5*(mPsiT**4 - 4*mPsiT**2*mSDM**2 + 3*mSDM**4 + 2*mSDM**4*cmath.log(mPsiT**2/mSDM**2))/(mPsiT**2 - mSDM**2)**3 if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(33*mPsiT**2 - 96*mPsiT*mSDM + 83*mSDM**2)/mSDM**4 ) + ( (-2*mPsiT**6 + 9*mPsiT**4*mSDM**2 - 18*mPsiT**2*mSDM**4 + 11*mSDM**6 + 6*mSDM**6*cmath.log(mPsiT**2/mSDM**2))/(6.*(mPsiT**2 - mSDM**2)**4) if (mPsiT - mSDM)**2/(mPsiT + mSDM)**2>0.001 else -0.016666666666666666*(28*mPsiT**2 - 80*mPsiT*mSDM + 67*mSDM**2)/mSDM**4 ))*G*yDM**2*ymt)/(32.*cmath.pi**2*vev*cmath.sqrt(2))',
                texname = 'c_{\\text{uG}}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

