# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Linux x86 (64-bit) (July 16, 2024)
# Date: Thu 26 Jun 2025 17:57:41


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
                 value = '-(cHD*complex(0,1))',
                 order = {'NPcHD':1,'QED':4})

GC_13 = Coupling(name = 'GC_13',
                 value = 'cld*complex(0,1)',
                 order = {'NPcld':1,'QED':4})

GC_14 = Coupling(name = 'GC_14',
                 value = 'cle*complex(0,1)',
                 order = {'NPcle':1,'QED':4})

GC_15 = Coupling(name = 'GC_15',
                 value = '2*cll*complex(0,1)',
                 order = {'NPcll':1,'QED':4})

GC_16 = Coupling(name = 'GC_16',
                 value = 'clq1*complex(0,1)',
                 order = {'NPclq1':1,'QED':4})

GC_17 = Coupling(name = 'GC_17',
                 value = 'clua*complex(0,1)',
                 order = {'NPclu':1,'QED':4})

GC_18 = Coupling(name = 'GC_18',
                 value = 'club*complex(0,1)',
                 order = {'NP1':2,'NPclu':1,'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = 'cqd1*complex(0,1)',
                 order = {'NPcqd1':1,'QED':4})

GC_20 = Coupling(name = 'GC_20',
                 value = 'cqd8*complex(0,1)',
                 order = {'NPcqd8':1,'QCD':4})

GC_21 = Coupling(name = 'GC_21',
                 value = 'cqe*complex(0,1)',
                 order = {'NPcqd8':1,'QED':4})

GC_22 = Coupling(name = 'GC_22',
                 value = '2*cqq1a*complex(0,1)',
                 order = {'NPcqq1':1,'QCD':4})

GC_23 = Coupling(name = 'GC_23',
                 value = '2*cqq1b*complex(0,1) + 2*cqq1c*complex(0,1)',
                 order = {'NPcqq1':1,'QCD':4})

GC_24 = Coupling(name = 'GC_24',
                 value = '2*cqq1a*complex(0,1) + 2*cqq1b*complex(0,1) + 2*cqq1c*complex(0,1)',
                 order = {'NPcqq1':1,'QCD':4})

GC_25 = Coupling(name = 'GC_25',
                 value = '-2*cqq3*complex(0,1)',
                 order = {'NPcqq3':1,'QCD':4})

GC_26 = Coupling(name = 'GC_26',
                 value = '2*cqq3*complex(0,1)',
                 order = {'NPcqq3':1,'QCD':4})

GC_27 = Coupling(name = 'GC_27',
                 value = '4*cqq3*complex(0,1)',
                 order = {'NPcqq3':1,'QCD':4})

GC_28 = Coupling(name = 'GC_28',
                 value = 'cqu1a*complex(0,1)',
                 order = {'NPcqu1':1,'QED':4})

GC_29 = Coupling(name = 'GC_29',
                 value = 'cqu1b*complex(0,1)',
                 order = {'NP1':2,'NPcqu1':1,'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = 'cqu8a*complex(0,1)',
                 order = {'NPcqu8':1,'QCD':4})

GC_31 = Coupling(name = 'GC_31',
                 value = 'cqu8b*complex(0,1)',
                 order = {'NP1':2,'NPcqu8':1,'QCD':2})

GC_32 = Coupling(name = 'GC_32',
                 value = 'cud1a*complex(0,1)',
                 order = {'NPcud1':1,'QED':4})

GC_33 = Coupling(name = 'GC_33',
                 value = 'cud1b*complex(0,1)',
                 order = {'NP1':2,'NPcud1':1,'QED':2})

GC_34 = Coupling(name = 'GC_34',
                 value = 'cud8a*complex(0,1)',
                 order = {'NPcud8':1,'QCD':4})

GC_35 = Coupling(name = 'GC_35',
                 value = 'cud8b*complex(0,1)',
                 order = {'NP1':2,'NPcud8':1,'QCD':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '(cuG*complex(0,1))/cmath.sqrt(2)',
                 order = {'NP1':2,'NPcuG':1,'QCD':1,'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(3*cuHa*complex(0,1))/cmath.sqrt(2)',
                 order = {'NP1':2,'NPcuH':1,'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '(3*cuHb*complex(0,1))/cmath.sqrt(2)',
                 order = {'NP1':2,'NPcuH':1,'QED':3})

GC_39 = Coupling(name = 'GC_39',
                 value = '2*cuua*complex(0,1)',
                 order = {'NPcuu':1,'QCD':4})

GC_40 = Coupling(name = 'GC_40',
                 value = '2*cuub*complex(0,1)',
                 order = {'NPcuu':1,'QED':4})

GC_41 = Coupling(name = 'GC_41',
                 value = '2*cuua*complex(0,1) + 2*cuuc*complex(0,1)',
                 order = {'NPcuu':1,'QCD':4})

GC_42 = Coupling(name = 'GC_42',
                 value = '2*cuuc*complex(0,1)',
                 order = {'NPcuu':1,'QCD':4})

GC_43 = Coupling(name = 'GC_43',
                 value = 'cuud*complex(0,1)',
                 order = {'NP1':2,'NPcuu':1,'QED':2})

GC_44 = Coupling(name = 'GC_44',
                 value = 'cuue*complex(0,1)',
                 order = {'NP1':2,'NPcuu':1,'QCD':2})

GC_45 = Coupling(name = 'GC_45',
                 value = 'cuuf*complex(0,1)',
                 order = {'NP1':2,'NPcuu':1,'QCD':2})

GC_46 = Coupling(name = 'GC_46',
                 value = '(cuB*cw*complex(0,1))/cmath.sqrt(2)',
                 order = {'NP1':2,'NPcuB':1,'QED':3})

GC_47 = Coupling(name = 'GC_47',
                 value = '-0.3333333333333333*(ee*complex(0,1))',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '(2*ee*complex(0,1))/3.',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '-(ee*complex(0,1))',
                 order = {'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = 'ee*complex(0,1)',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = 'ee**2*complex(0,1)',
                 order = {'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '-G',
                 order = {'QCD':1})

GC_53 = Coupling(name = 'GC_53',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '6*cG*complex(0,1)*G',
                 order = {'NPcG':1,'QCD':4})

GC_55 = Coupling(name = 'GC_55',
                 value = '-((cuG*G)/cmath.sqrt(2))',
                 order = {'NP1':2,'NPcuG':1,'QCD':2,'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '-3*cG*G**2',
                 order = {'NPcG':1,'QCD':5})

GC_58 = Coupling(name = 'GC_58',
                 value = '3*cG*G**2',
                 order = {'NPcG':1,'QCD':5})

GC_59 = Coupling(name = 'GC_59',
                 value = '-(cG*complex(0,1)*G**3)',
                 order = {'NPcG':1,'QCD':6})

GC_60 = Coupling(name = 'GC_60',
                 value = 'cG*complex(0,1)*G**3',
                 order = {'NPcG':1,'QCD':6})

GC_61 = Coupling(name = 'GC_61',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_62 = Coupling(name = 'GC_62',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_64 = Coupling(name = 'GC_64',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_65 = Coupling(name = 'GC_65',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '(cHq3*ee*complex(0,1)*cmath.sqrt(2))/sw',
                 order = {'NP1':2,'NPcHq3':1,'QED':3})

GC_67 = Coupling(name = 'GC_67',
                 value = '-0.5*(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_71 = Coupling(name = 'GC_71',
                 value = '-((cuB*complex(0,1)*sw)/cmath.sqrt(2))',
                 order = {'NP1':2,'NPcuB':1,'QED':3})

GC_72 = Coupling(name = 'GC_72',
                 value = '-0.16666666666666666*(ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '(ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '-((cHd*cw*ee*complex(0,1))/sw) - (cHd*ee*complex(0,1)*sw)/cw',
                 order = {'NPcHd':1,'QED':5})

GC_76 = Coupling(name = 'GC_76',
                 value = '-((cHe*cw*ee*complex(0,1))/sw) - (cHe*ee*complex(0,1)*sw)/cw',
                 order = {'NPcHe':1,'QED':5})

GC_77 = Coupling(name = 'GC_77',
                 value = '-((cHl1*cw*ee*complex(0,1))/sw) - (cHl1*ee*complex(0,1)*sw)/cw',
                 order = {'NPcHl1':1,'QED':5})

GC_78 = Coupling(name = 'GC_78',
                 value = '-((cHq1a*cw*ee*complex(0,1))/sw) - (cHq1a*ee*complex(0,1)*sw)/cw',
                 order = {'NPcHq1':1,'QED':3})

GC_79 = Coupling(name = 'GC_79',
                 value = '-((cHq1b*cw*ee*complex(0,1))/sw) - (cHq1b*ee*complex(0,1)*sw)/cw',
                 order = {'NP1':2,'NPcHq1':1,'QED':3})

GC_80 = Coupling(name = 'GC_80',
                 value = '-((cHq3*cw*ee*complex(0,1))/sw) - (cHq3*ee*complex(0,1)*sw)/cw',
                 order = {'NP1':2,'NPcHq3':1,'QED':3})

GC_81 = Coupling(name = 'GC_81',
                 value = '(cHq3*cw*ee*complex(0,1))/sw + (cHq3*ee*complex(0,1)*sw)/cw',
                 order = {'NP1':2,'NPcHq3':1,'QED':3})

GC_82 = Coupling(name = 'GC_82',
                 value = '-((cHua*cw*ee*complex(0,1))/sw) - (cHua*ee*complex(0,1)*sw)/cw',
                 order = {'NPcHu':1,'QED':5})

GC_83 = Coupling(name = 'GC_83',
                 value = '-((cHub*cw*ee*complex(0,1))/sw) - (cHub*ee*complex(0,1)*sw)/cw',
                 order = {'NP1':2,'NPcHu':1,'QED':3})

GC_84 = Coupling(name = 'GC_84',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = '6*cHD*ee**2*complex(0,1) + (3*cHD*cw**2*ee**2*complex(0,1))/sw**2 + (3*cHD*ee**2*complex(0,1)*sw**2)/cw**2',
                 order = {'NPcHD':1,'QED':6})

GC_86 = Coupling(name = 'GC_86',
                 value = '90*cH*complex(0,1)*vev',
                 order = {'NP2':3,'NPcH':1,'QED':-1})

GC_87 = Coupling(name = 'GC_87',
                 value = '-(cHD*complex(0,1)*vev)',
                 order = {'NPcHD':1,'QED':3})

GC_88 = Coupling(name = 'GC_88',
                 value = '(cuG*complex(0,1)*vev)/cmath.sqrt(2)',
                 order = {'NP1':2,'NPcuG':1,'QCD':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '(3*cuHa*complex(0,1)*vev)/cmath.sqrt(2)',
                 order = {'NP1':2,'NPcuH':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '(3*cuHb*complex(0,1)*vev)/cmath.sqrt(2)',
                 order = {'NP1':2,'NPcuH':1,'QED':2})

GC_91 = Coupling(name = 'GC_91',
                 value = '(cuB*cw*complex(0,1)*vev)/cmath.sqrt(2)',
                 order = {'NP1':2,'NPcuB':1,'QED':2})

GC_92 = Coupling(name = 'GC_92',
                 value = '-((cuG*G*vev)/cmath.sqrt(2))',
                 order = {'NP1':2,'NPcuG':1,'QCD':2})

GC_93 = Coupling(name = 'GC_93',
                 value = '-6*complex(0,1)*lam*vev',
                 order = {'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '(cHq3*ee*complex(0,1)*vev*cmath.sqrt(2))/sw',
                 order = {'NP1':2,'NPcHq3':1,'QED':2})

GC_96 = Coupling(name = 'GC_96',
                 value = '-((cuB*complex(0,1)*sw*vev)/cmath.sqrt(2))',
                 order = {'NP1':2,'NPcuB':1,'QED':2})

GC_97 = Coupling(name = 'GC_97',
                 value = '45*cH*complex(0,1)*vev**2',
                 order = {'NP2':3,'NPcH':1,'QED':-2})

GC_98 = Coupling(name = 'GC_98',
                 value = '(3*cuHa*complex(0,1)*vev**2)/(2.*cmath.sqrt(2))',
                 order = {'NP1':2,'NPcuH':1,'QED':-1})

GC_99 = Coupling(name = 'GC_99',
                 value = '(3*cuHb*complex(0,1)*vev**2)/(2.*cmath.sqrt(2))',
                 order = {'NP1':2,'NPcuH':1,'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '(cHq3*ee*complex(0,1)*vev**2)/(sw*cmath.sqrt(2))',
                  order = {'NP1':2,'NPcHq3':1,'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '15*cH*complex(0,1)*vev**3',
                  order = {'NP2':3,'NPcH':1,'QED':-3})

GC_102 = Coupling(name = 'GC_102',
                  value = '-((cHd*cw*ee*complex(0,1)*vev)/sw) - (cHd*ee*complex(0,1)*sw*vev)/cw',
                  order = {'NPcHd':1,'QED':4})

GC_103 = Coupling(name = 'GC_103',
                  value = '-((cHe*cw*ee*complex(0,1)*vev)/sw) - (cHe*ee*complex(0,1)*sw*vev)/cw',
                  order = {'NPcHe':1,'QED':4})

GC_104 = Coupling(name = 'GC_104',
                  value = '-((cHl1*cw*ee*complex(0,1)*vev)/sw) - (cHl1*ee*complex(0,1)*sw*vev)/cw',
                  order = {'NPcHl1':1,'QED':4})

GC_105 = Coupling(name = 'GC_105',
                  value = '-((cHq1a*cw*ee*complex(0,1)*vev)/sw) - (cHq1a*ee*complex(0,1)*sw*vev)/cw',
                  order = {'NPcHq1':1,'QED':2})

GC_106 = Coupling(name = 'GC_106',
                  value = '-((cHq1b*cw*ee*complex(0,1)*vev)/sw) - (cHq1b*ee*complex(0,1)*sw*vev)/cw',
                  order = {'NP1':2,'NPcHq1':1,'QED':2})

GC_107 = Coupling(name = 'GC_107',
                  value = '-((cHq3*cw*ee*complex(0,1)*vev)/sw) - (cHq3*ee*complex(0,1)*sw*vev)/cw',
                  order = {'NP1':2,'NPcHq3':1,'QED':2})

GC_108 = Coupling(name = 'GC_108',
                  value = '(cHq3*cw*ee*complex(0,1)*vev)/sw + (cHq3*ee*complex(0,1)*sw*vev)/cw',
                  order = {'NP1':2,'NPcHq3':1,'QED':2})

GC_109 = Coupling(name = 'GC_109',
                  value = '-((cHua*cw*ee*complex(0,1)*vev)/sw) - (cHua*ee*complex(0,1)*sw*vev)/cw',
                  order = {'NPcHu':1,'QED':4})

GC_110 = Coupling(name = 'GC_110',
                  value = '-((cHub*cw*ee*complex(0,1)*vev)/sw) - (cHub*ee*complex(0,1)*sw*vev)/cw',
                  order = {'NP1':2,'NPcHu':1,'QED':2})

GC_111 = Coupling(name = 'GC_111',
                  value = 'ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '6*cHD*ee**2*complex(0,1)*vev + (3*cHD*cw**2*ee**2*complex(0,1)*vev)/sw**2 + (3*cHD*ee**2*complex(0,1)*sw**2*vev)/cw**2',
                  order = {'NPcHD':1,'QED':5})

GC_113 = Coupling(name = 'GC_113',
                  value = '-0.5*(cHd*cw*ee*complex(0,1)*vev**2)/sw - (cHd*ee*complex(0,1)*sw*vev**2)/(2.*cw)',
                  order = {'NPcHd':1,'QED':3})

GC_114 = Coupling(name = 'GC_114',
                  value = '-0.5*(cHe*cw*ee*complex(0,1)*vev**2)/sw - (cHe*ee*complex(0,1)*sw*vev**2)/(2.*cw)',
                  order = {'NPcHe':1,'QED':3})

GC_115 = Coupling(name = 'GC_115',
                  value = '-0.5*(cHl1*cw*ee*complex(0,1)*vev**2)/sw - (cHl1*ee*complex(0,1)*sw*vev**2)/(2.*cw)',
                  order = {'NPcHl1':1,'QED':3})

GC_116 = Coupling(name = 'GC_116',
                  value = '-0.5*(cHq1a*cw*ee*complex(0,1)*vev**2)/sw - (cHq1a*ee*complex(0,1)*sw*vev**2)/(2.*cw)',
                  order = {'NPcHq1':1,'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '-0.5*(cHq1b*cw*ee*complex(0,1)*vev**2)/sw - (cHq1b*ee*complex(0,1)*sw*vev**2)/(2.*cw)',
                  order = {'NP1':2,'NPcHq1':1,'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '-0.5*(cHq3*cw*ee*complex(0,1)*vev**2)/sw - (cHq3*ee*complex(0,1)*sw*vev**2)/(2.*cw)',
                  order = {'NP1':2,'NPcHq3':1,'QED':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '(cHq3*cw*ee*complex(0,1)*vev**2)/(2.*sw) + (cHq3*ee*complex(0,1)*sw*vev**2)/(2.*cw)',
                  order = {'NP1':2,'NPcHq3':1,'QED':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '-0.5*(cHua*cw*ee*complex(0,1)*vev**2)/sw - (cHua*ee*complex(0,1)*sw*vev**2)/(2.*cw)',
                  order = {'NPcHu':1,'QED':3})

GC_121 = Coupling(name = 'GC_121',
                  value = '-0.5*(cHub*cw*ee*complex(0,1)*vev**2)/sw - (cHub*ee*complex(0,1)*sw*vev**2)/(2.*cw)',
                  order = {'NP1':2,'NPcHu':1,'QED':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '3*cHD*ee**2*complex(0,1)*vev**2 + (3*cHD*cw**2*ee**2*complex(0,1)*vev**2)/(2.*sw**2) + (3*cHD*ee**2*complex(0,1)*sw**2*vev**2)/(2.*cw**2)',
                  order = {'NPcHD':1,'QED':4})

GC_123 = Coupling(name = 'GC_123',
                  value = 'cHD*ee**2*complex(0,1)*vev**3 + (cHD*cw**2*ee**2*complex(0,1)*vev**3)/(2.*sw**2) + (cHD*ee**2*complex(0,1)*sw**2*vev**3)/(2.*cw**2)',
                  order = {'NPcHD':1,'QED':3})

GC_124 = Coupling(name = 'GC_124',
                  value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

