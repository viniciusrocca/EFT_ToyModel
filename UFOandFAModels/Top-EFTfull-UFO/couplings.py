# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Linux x86 (64-bit) (July 16, 2024)
# Date: Thu 19 Jun 2025 16:02:55


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '2*cdda*complex(0,1)',
                order = {'NPcdd':1,'QCD':4})

GC_2 = Coupling(name = 'GC_2',
                value = '2*cdda*complex(0,1) + 2*cddb*complex(0,1)',
                order = {'NPcdd':1,'QCD':4})

GC_3 = Coupling(name = 'GC_3',
                value = '2*cddb*complex(0,1)',
                order = {'NPcdd':1,'QCD':4})

GC_4 = Coupling(name = 'GC_4',
                value = '2*cddc*complex(0,1)',
                order = {'NPcdd':1,'QED':4})

GC_5 = Coupling(name = 'GC_5',
                value = 'ced*complex(0,1)',
                order = {'NPced':1,'QED':4})

GC_6 = Coupling(name = 'GC_6',
                value = '2*cee*complex(0,1)',
                order = {'NPcG':1,'QED':4})

GC_7 = Coupling(name = 'GC_7',
                value = '4*cee*complex(0,1)',
                order = {'NPcG':1,'QED':4})

GC_8 = Coupling(name = 'GC_8',
                value = 'ceua*complex(0,1)',
                order = {'NPceu':1,'QED':4})

GC_9 = Coupling(name = 'GC_9',
                value = 'ceub*complex(0,1)',
                order = {'NP1':2,'NPceu':1,'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '-6*cG',
                 order = {'NPcG':1,'QCD':3})

GC_11 = Coupling(name = 'GC_11',
                 value = '90*cH*complex(0,1)',
                 order = {'NP2':3,'NPcH':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '-0.3333333333333333*(ee*complex(0,1))',
                 order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '(2*ee*complex(0,1))/3.',
                 order = {'QED':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '-(ee*complex(0,1))',
                 order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = 'ee*complex(0,1)',
                 order = {'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = 'ee**2*complex(0,1)',
                 order = {'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '-G',
                 order = {'QCD':1})

GC_18 = Coupling(name = 'GC_18',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '6*cG*complex(0,1)*G',
                 order = {'NPcG':1,'QCD':4})

GC_20 = Coupling(name = 'GC_20',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '-3*cG*G**2',
                 order = {'NPcG':1,'QCD':5})

GC_22 = Coupling(name = 'GC_22',
                 value = '3*cG*G**2',
                 order = {'NPcG':1,'QCD':5})

GC_23 = Coupling(name = 'GC_23',
                 value = '-(cG*complex(0,1)*G**3)',
                 order = {'NPcG':1,'QCD':6})

GC_24 = Coupling(name = 'GC_24',
                 value = 'cG*complex(0,1)*G**3',
                 order = {'NPcG':1,'QCD':6})

GC_25 = Coupling(name = 'GC_25',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '(CKM1x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '(CKM2x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '(CKM3x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(CKM3x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '(CKM3x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '(ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '(ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-0.5*(cw*ee*complex(0,1))/sw - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '-0.5*(cw*ee*complex(0,1))/sw + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-((cHd*cw*ee*complex(0,1))/sw) - (cHd*ee*complex(0,1)*sw)/cw',
                 order = {'NPcHd':1,'QED':5})

GC_49 = Coupling(name = 'GC_49',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '90*cH*complex(0,1)*vev',
                 order = {'NP2':3,'NPcH':1,'QED':-1})

GC_51 = Coupling(name = 'GC_51',
                 value = '-6*complex(0,1)*lam*vev',
                 order = {'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '45*cH*complex(0,1)*vev**2',
                 order = {'NP2':3,'NPcH':1,'QED':-2})

GC_54 = Coupling(name = 'GC_54',
                 value = '15*cH*complex(0,1)*vev**3',
                 order = {'NP2':3,'NPcH':1,'QED':-3})

GC_55 = Coupling(name = 'GC_55',
                 value = '-((cHd*cw*ee*complex(0,1)*vev)/sw) - (cHd*ee*complex(0,1)*sw*vev)/cw',
                 order = {'NPcHd':1,'QED':4})

GC_56 = Coupling(name = 'GC_56',
                 value = 'ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '-0.5*(cHd*cw*ee*complex(0,1)*vev**2)/sw - (cHd*ee*complex(0,1)*sw*vev**2)/(2.*cw)',
                 order = {'NPcHd':1,'QED':3})

GC_58 = Coupling(name = 'GC_58',
                 value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '-((complex(0,1)*yc)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '-((complex(0,1)*ydo)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-((complex(0,1)*ye)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '-((complex(0,1)*ym)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '-((complex(0,1)*ys)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '-((complex(0,1)*yup)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '(ee*complex(0,1)*complexconjugate(CKM1x3))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '(ee*complex(0,1)*complexconjugate(CKM2x3))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '(ee*complex(0,1)*complexconjugate(CKM3x1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '(ee*complex(0,1)*complexconjugate(CKM3x2))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '(ee*complex(0,1)*complexconjugate(CKM3x3))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

