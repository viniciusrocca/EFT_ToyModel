# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Linux x86 (64-bit) (July 16, 2024)
# Date: Mon 22 Jun 2026 17:31:18



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
gVXc = Parameter(name = 'gVXc',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = 'g_{\\text{VXc}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 1 ])

gVXd = Parameter(name = 'gVXd',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'g_{\\text{VXd}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 2 ])

gAXd = Parameter(name = 'gAXd',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = 'g_{\\text{AXd}}',
                 lhablock = 'DMINPUTS',
                 lhacode = [ 3 ])

gVd11 = Parameter(name = 'gVd11',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vd11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 4 ])

gVu11 = Parameter(name = 'gVu11',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vu11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 5 ])

gVd22 = Parameter(name = 'gVd22',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vd22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 6 ])

gVu22 = Parameter(name = 'gVu22',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vu22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 7 ])

gVd33 = Parameter(name = 'gVd33',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vd33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 8 ])

gVu33 = Parameter(name = 'gVu33',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vu33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 9 ])

gVl11 = Parameter(name = 'gVl11',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Ve}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 10 ])

gVl22 = Parameter(name = 'gVl22',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Vmu}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 11 ])

gVl33 = Parameter(name = 'gVl33',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Vta}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 12 ])

gAd11 = Parameter(name = 'gAd11',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Ad11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 13 ])

gAu11 = Parameter(name = 'gAu11',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Au11}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 14 ])

gAd22 = Parameter(name = 'gAd22',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Ad22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 15 ])

gAu22 = Parameter(name = 'gAu22',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Au22}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 16 ])

gAd33 = Parameter(name = 'gAd33',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Ad33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 17 ])

gAu33 = Parameter(name = 'gAu33',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Au33}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 18 ])

gAl11 = Parameter(name = 'gAl11',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Ae}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 19 ])

gAl22 = Parameter(name = 'gAl22',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Amu}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 20 ])

gAl33 = Parameter(name = 'gAl33',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{Ata}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 21 ])

gnu11 = Parameter(name = 'gnu11',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{nue}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 22 ])

gnu22 = Parameter(name = 'gnu22',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{num}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 23 ])

gnu33 = Parameter(name = 'gnu33',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = 'g_{\\text{nut}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 24 ])

gVu31 = Parameter(name = 'gVu31',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vu31}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 25 ])

gAu31 = Parameter(name = 'gAu31',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Au31}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 26 ])

gVd31 = Parameter(name = 'gVd31',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Vd31}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 27 ])

gAd31 = Parameter(name = 'gAd31',
                  nature = 'external',
                  type = 'real',
                  value = 0.25,
                  texname = 'g_{\\text{Ad31}}',
                  lhablock = 'DMINPUTS',
                  lhacode = [ 28 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 173.,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MXr = Parameter(name = 'MXr',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{MXr}',
                lhablock = 'MASS',
                lhacode = [ 5000511 ])

MXc = Parameter(name = 'MXc',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{MXc}',
                lhablock = 'MASS',
                lhacode = [ 5000512 ])

MXd = Parameter(name = 'MXd',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{MXd}',
                lhablock = 'MASS',
                lhacode = [ 5000521 ])

MY1 = Parameter(name = 'MY1',
                nature = 'external',
                type = 'real',
                value = 1000.,
                texname = '\\text{MY1}',
                lhablock = 'MASS',
                lhacode = [ 5000001 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WY1 = Parameter(name = 'WY1',
                nature = 'external',
                type = 'real',
                value = 10.,
                texname = '\\text{WY1}',
                lhablock = 'DECAY',
                lhacode = [ 5000001 ])

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

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

