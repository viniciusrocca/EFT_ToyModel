# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Linux x86 (64-bit) (July 16, 2024)
# Date: Mon 22 Jun 2026 19:46:03


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV2 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_89_101,(0,0,1):C.R2GC_89_102})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,1,0):C.R2GC_69_85,(2,1,1):C.R2GC_69_86,(0,1,0):C.R2GC_69_85,(0,1,1):C.R2GC_69_86,(4,1,0):C.R2GC_67_81,(4,1,1):C.R2GC_67_82,(3,1,0):C.R2GC_67_81,(3,1,1):C.R2GC_67_82,(8,1,0):C.R2GC_68_83,(8,1,1):C.R2GC_68_84,(6,1,0):C.R2GC_72_90,(6,1,1):C.R2GC_94_108,(7,1,0):C.R2GC_73_92,(7,1,1):C.R2GC_93_107,(5,1,0):C.R2GC_67_81,(5,1,1):C.R2GC_67_82,(1,1,0):C.R2GC_67_81,(1,1,1):C.R2GC_67_82,(11,0,0):C.R2GC_71_88,(11,0,1):C.R2GC_71_89,(10,0,0):C.R2GC_71_88,(10,0,1):C.R2GC_71_89,(9,0,1):C.R2GC_70_87,(0,2,0):C.R2GC_69_85,(0,2,1):C.R2GC_69_86,(2,2,0):C.R2GC_69_85,(2,2,1):C.R2GC_69_86,(5,2,0):C.R2GC_67_81,(5,2,1):C.R2GC_67_82,(1,2,0):C.R2GC_67_81,(1,2,1):C.R2GC_67_82,(7,2,0):C.R2GC_73_92,(7,2,1):C.R2GC_73_93,(4,2,0):C.R2GC_67_81,(4,2,1):C.R2GC_67_82,(3,2,0):C.R2GC_67_81,(3,2,1):C.R2GC_67_82,(8,2,0):C.R2GC_68_83,(8,2,1):C.R2GC_95_109,(6,2,0):C.R2GC_90_103,(6,2,1):C.R2GC_90_104,(0,3,0):C.R2GC_69_85,(0,3,1):C.R2GC_69_86,(2,3,0):C.R2GC_69_85,(2,3,1):C.R2GC_69_86,(5,3,0):C.R2GC_67_81,(5,3,1):C.R2GC_67_82,(1,3,0):C.R2GC_67_81,(1,3,1):C.R2GC_67_82,(7,3,0):C.R2GC_91_105,(7,3,1):C.R2GC_69_86,(4,3,0):C.R2GC_67_81,(4,3,1):C.R2GC_67_82,(3,3,0):C.R2GC_67_81,(3,3,1):C.R2GC_67_82,(8,3,0):C.R2GC_68_83,(8,3,1):C.R2GC_92_106,(6,3,0):C.R2GC_72_90,(6,3,1):C.R2GC_72_91})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.Y1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.Y1] ] ],
               couplings = {(0,0,0):C.R2GC_127_41,(0,0,1):C.R2GC_127_42,(0,1,0):C.R2GC_128_43,(0,1,1):C.R2GC_128_44})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.c__tilde__, P.c, P.Y1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.Y1] ] ],
               couplings = {(0,0,0):C.R2GC_117_25,(0,0,1):C.R2GC_117_26,(0,1,0):C.R2GC_121_33,(0,1,1):C.R2GC_121_34})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.d__tilde__, P.d, P.Y1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.Y1] ] ],
               couplings = {(0,0,0):C.R2GC_114_19,(0,0,1):C.R2GC_114_20,(0,1,0):C.R2GC_118_27,(0,1,1):C.R2GC_118_28})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.s__tilde__, P.s, P.Y1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               loop_particles = [ [ [P.g, P.s] ], [ [P.s, P.Y1] ] ],
               couplings = {(0,0,0):C.R2GC_115_21,(0,0,1):C.R2GC_115_22,(0,1,0):C.R2GC_119_29,(0,1,1):C.R2GC_119_30})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.Y1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               loop_particles = [ [ [P.g, P.t] ], [ [P.t, P.Y1] ] ],
               couplings = {(0,0,0):C.R2GC_133_49,(0,0,1):C.R2GC_133_50,(0,1,0):C.R2GC_134_51,(0,1,1):C.R2GC_134_52})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.u__tilde__, P.u, P.Y1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               loop_particles = [ [ [P.g, P.u] ], [ [P.u, P.Y1] ] ],
               couplings = {(0,0,0):C.R2GC_116_23,(0,0,1):C.R2GC_116_24,(0,1,0):C.R2GC_120_31,(0,1,1):C.R2GC_120_32})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
               loop_particles = [ [ [P.g, P.u] ], [ [P.u, P.Y1] ] ],
               couplings = {(0,0,0):C.R2GC_75_95,(0,1,1):C.R2GC_110_11,(0,2,1):C.R2GC_111_12})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.Y1] ] ],
                couplings = {(0,0,0):C.R2GC_75_95,(0,1,1):C.R2GC_98_112,(0,2,1):C.R2GC_99_113})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ], [ [P.t, P.Y1] ] ],
                couplings = {(0,0,0):C.R2GC_75_95,(0,1,1):C.R2GC_131_47,(0,2,1):C.R2GC_132_48})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.Y1] ] ],
                couplings = {(0,0,0):C.R2GC_75_95,(0,1,1):C.R2GC_102_3,(0,2,1):C.R2GC_103_4})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.s, P.Y1] ] ],
                couplings = {(0,0,0):C.R2GC_75_95,(0,1,1):C.R2GC_106_7,(0,2,1):C.R2GC_107_8})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.Y1] ] ],
                couplings = {(0,0,0):C.R2GC_75_95,(0,1,1):C.R2GC_125_39,(0,2,1):C.R2GC_126_40})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.Y1] ] ],
                couplings = {(0,1,0):C.R2GC_76_96,(0,1,1):C.R2GC_76_97,(0,3,0):C.R2GC_76_96,(0,3,1):C.R2GC_76_97,(0,4,1):C.R2GC_123_37,(0,2,1):C.R2GC_124_38,(0,0,0):C.R2GC_74_94})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.Y1] ] ],
                couplings = {(0,1,1):C.R2GC_97_111,(0,2,1):C.R2GC_96_110,(0,0,0):C.R2GC_74_94})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.Y1] ] ],
                couplings = {(0,1,1):C.R2GC_101_2,(0,2,1):C.R2GC_100_1,(0,0,0):C.R2GC_74_94})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.s, P.Y1] ] ],
                couplings = {(0,1,1):C.R2GC_105_6,(0,2,1):C.R2GC_104_5,(0,0,0):C.R2GC_74_94})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ], [ [P.t, P.Y1] ] ],
                couplings = {(0,1,0):C.R2GC_135_53,(0,1,1):C.R2GC_135_54,(0,3,0):C.R2GC_135_53,(0,3,1):C.R2GC_135_54,(0,4,1):C.R2GC_129_45,(0,2,1):C.R2GC_130_46,(0,0,0):C.R2GC_74_94})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.u] ], [ [P.u, P.Y1] ] ],
                couplings = {(0,1,1):C.R2GC_109_10,(0,2,1):C.R2GC_108_9,(0,0,0):C.R2GC_74_94})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.Y1, P.Y1 ],
                color = [ '1' ],
                lorentz = [ L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_122_35,(0,0,4):C.R2GC_122_36,(0,1,0):C.R2GC_113_13,(0,1,1):C.R2GC_113_14,(0,1,2):C.R2GC_113_15,(0,1,3):C.R2GC_113_16,(0,1,4):C.R2GC_113_17,(0,1,5):C.R2GC_113_18})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.R2GC_88_100,(0,1,0):C.R2GC_60_55,(0,1,3):C.R2GC_60_56,(0,2,1):C.R2GC_87_98,(0,2,2):C.R2GC_87_99})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.Y1, P.Y1, P.Y1, P.Y1 ],
                color = [ '1' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_64_75,(0,0,1):C.R2GC_64_76,(0,0,2):C.R2GC_64_77,(0,0,3):C.R2GC_64_78,(0,0,4):C.R2GC_64_79,(0,0,5):C.R2GC_64_80,(0,1,0):C.R2GC_64_75,(0,1,1):C.R2GC_64_76,(0,1,2):C.R2GC_64_77,(0,1,3):C.R2GC_64_78,(0,1,4):C.R2GC_64_79,(0,1,5):C.R2GC_64_80,(0,2,0):C.R2GC_64_75,(0,2,1):C.R2GC_64_76,(0,2,2):C.R2GC_64_77,(0,2,3):C.R2GC_64_78,(0,2,4):C.R2GC_64_79,(0,2,5):C.R2GC_64_80})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.g, P.g, P.Y1, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_63_69,(0,0,1):C.R2GC_63_70,(0,0,2):C.R2GC_63_71,(0,0,3):C.R2GC_63_72,(0,0,4):C.R2GC_63_73,(0,0,5):C.R2GC_63_74,(0,1,0):C.R2GC_63_69,(0,1,1):C.R2GC_63_70,(0,1,2):C.R2GC_63_71,(0,1,3):C.R2GC_63_72,(0,1,4):C.R2GC_63_73,(0,1,5):C.R2GC_63_74,(0,2,0):C.R2GC_63_69,(0,2,1):C.R2GC_63_70,(0,2,2):C.R2GC_63_71,(0,2,3):C.R2GC_63_72,(0,2,4):C.R2GC_63_73,(0,2,5):C.R2GC_63_74})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Y1 ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_61_57,(1,0,1):C.R2GC_61_58,(1,0,2):C.R2GC_61_59,(1,0,3):C.R2GC_61_60,(1,0,4):C.R2GC_61_61,(1,0,5):C.R2GC_61_62,(0,1,0):C.R2GC_62_63,(0,1,1):C.R2GC_62_64,(0,1,2):C.R2GC_62_65,(0,1,3):C.R2GC_62_66,(0,1,4):C.R2GC_62_67,(0,1,5):C.R2GC_62_68,(0,2,0):C.R2GC_62_63,(0,2,1):C.R2GC_62_64,(0,2,2):C.R2GC_62_65,(0,2,3):C.R2GC_62_66,(0,2,4):C.R2GC_62_67,(0,2,5):C.R2GC_62_68,(0,3,0):C.R2GC_62_63,(0,3,1):C.R2GC_62_64,(0,3,2):C.R2GC_62_65,(0,3,3):C.R2GC_62_66,(0,3,4):C.R2GC_62_67,(0,3,5):C.R2GC_62_68})

V_26 = CTVertex(name = 'V_26',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,1,0):C.UVGC_89_164,(0,1,1):C.UVGC_89_165,(0,1,4):C.UVGC_89_166,(0,2,2):C.UVGC_65_140,(0,0,3):C.UVGC_66_141})

V_27 = CTVertex(name = 'V_27',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(2,1,3):C.UVGC_68_145,(2,1,4):C.UVGC_68_144,(0,1,3):C.UVGC_68_145,(0,1,4):C.UVGC_68_144,(4,1,3):C.UVGC_67_142,(4,1,4):C.UVGC_67_143,(3,1,3):C.UVGC_67_142,(3,1,4):C.UVGC_67_143,(8,1,3):C.UVGC_68_144,(8,1,4):C.UVGC_68_145,(6,1,0):C.UVGC_93_178,(6,1,2):C.UVGC_93_179,(6,1,3):C.UVGC_94_183,(6,1,4):C.UVGC_94_184,(6,1,5):C.UVGC_93_182,(7,1,0):C.UVGC_93_178,(7,1,2):C.UVGC_93_179,(7,1,3):C.UVGC_93_180,(7,1,4):C.UVGC_93_181,(7,1,5):C.UVGC_93_182,(5,1,3):C.UVGC_67_142,(5,1,4):C.UVGC_67_143,(1,1,3):C.UVGC_67_142,(1,1,4):C.UVGC_67_143,(11,0,3):C.UVGC_71_148,(11,0,4):C.UVGC_71_149,(10,0,3):C.UVGC_71_148,(10,0,4):C.UVGC_71_149,(9,0,3):C.UVGC_70_146,(9,0,4):C.UVGC_70_147,(0,2,3):C.UVGC_68_145,(0,2,4):C.UVGC_68_144,(2,2,3):C.UVGC_68_145,(2,2,4):C.UVGC_68_144,(5,2,3):C.UVGC_67_142,(5,2,4):C.UVGC_67_143,(1,2,3):C.UVGC_67_142,(1,2,4):C.UVGC_67_143,(7,2,1):C.UVGC_72_150,(7,2,3):C.UVGC_73_152,(7,2,4):C.UVGC_73_153,(4,2,3):C.UVGC_67_142,(4,2,4):C.UVGC_67_143,(3,2,3):C.UVGC_67_142,(3,2,4):C.UVGC_67_143,(8,2,0):C.UVGC_95_185,(8,2,2):C.UVGC_95_186,(8,2,3):C.UVGC_95_187,(8,2,4):C.UVGC_95_188,(8,2,5):C.UVGC_95_189,(6,2,0):C.UVGC_90_167,(6,2,3):C.UVGC_90_168,(6,2,4):C.UVGC_90_169,(6,2,5):C.UVGC_90_170,(0,3,3):C.UVGC_68_145,(0,3,4):C.UVGC_68_144,(2,3,3):C.UVGC_68_145,(2,3,4):C.UVGC_68_144,(5,3,3):C.UVGC_67_142,(5,3,4):C.UVGC_67_143,(1,3,3):C.UVGC_67_142,(1,3,4):C.UVGC_67_143,(7,3,0):C.UVGC_90_167,(7,3,3):C.UVGC_91_171,(7,3,4):C.UVGC_91_172,(7,3,5):C.UVGC_90_170,(4,3,3):C.UVGC_67_142,(4,3,4):C.UVGC_67_143,(3,3,3):C.UVGC_67_142,(3,3,4):C.UVGC_67_143,(8,3,0):C.UVGC_92_173,(8,3,2):C.UVGC_92_174,(8,3,3):C.UVGC_92_175,(8,3,4):C.UVGC_92_176,(8,3,5):C.UVGC_92_177,(6,3,1):C.UVGC_72_150,(6,3,3):C.UVGC_72_151,(6,3,4):C.UVGC_70_146})

V_28 = CTVertex(name = 'V_28',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.b, P.Y1] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.UVGC_127_100,(0,0,3):C.UVGC_127_101,(0,0,4):C.UVGC_127_102,(0,0,5):C.UVGC_127_103,(0,0,6):C.UVGC_127_104,(0,0,7):C.UVGC_127_105,(0,0,1):C.UVGC_127_106,(0,0,2):C.UVGC_127_107,(0,1,0):C.UVGC_128_108,(0,1,3):C.UVGC_128_109,(0,1,4):C.UVGC_128_110,(0,1,5):C.UVGC_128_111,(0,1,6):C.UVGC_128_112,(0,1,7):C.UVGC_128_113,(0,1,1):C.UVGC_128_114,(0,1,2):C.UVGC_128_115})

V_29 = CTVertex(name = 'V_29',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.c, P.Y1] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.UVGC_117_53,(0,0,1):C.UVGC_117_54,(0,0,3):C.UVGC_117_55,(0,0,4):C.UVGC_117_56,(0,0,5):C.UVGC_117_57,(0,0,6):C.UVGC_117_58,(0,0,2):C.UVGC_117_59,(0,1,0):C.UVGC_121_81,(0,1,1):C.UVGC_121_82,(0,1,3):C.UVGC_121_83,(0,1,4):C.UVGC_121_84,(0,1,5):C.UVGC_121_85,(0,1,6):C.UVGC_121_86,(0,1,2):C.UVGC_121_87})

V_30 = CTVertex(name = 'V_30',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.d, P.Y1] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.UVGC_114_32,(0,0,1):C.UVGC_114_33,(0,0,2):C.UVGC_114_34,(0,0,4):C.UVGC_114_35,(0,0,5):C.UVGC_114_36,(0,0,6):C.UVGC_114_37,(0,0,3):C.UVGC_114_38,(0,1,0):C.UVGC_118_60,(0,1,1):C.UVGC_118_61,(0,1,2):C.UVGC_118_62,(0,1,4):C.UVGC_118_63,(0,1,5):C.UVGC_118_64,(0,1,6):C.UVGC_118_65,(0,1,3):C.UVGC_118_66})

V_31 = CTVertex(name = 'V_31',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.s, P.Y1] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.UVGC_115_39,(0,0,1):C.UVGC_115_40,(0,0,2):C.UVGC_115_41,(0,0,3):C.UVGC_115_42,(0,0,5):C.UVGC_115_43,(0,0,6):C.UVGC_115_44,(0,0,4):C.UVGC_115_45,(0,1,0):C.UVGC_119_67,(0,1,1):C.UVGC_119_68,(0,1,2):C.UVGC_119_69,(0,1,3):C.UVGC_119_70,(0,1,5):C.UVGC_119_71,(0,1,6):C.UVGC_119_72,(0,1,4):C.UVGC_119_73})

V_32 = CTVertex(name = 'V_32',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.g, P.t] ], [ [P.s] ], [ [P.t] ], [ [P.t, P.Y1] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.UVGC_133_122,(0,0,1):C.UVGC_133_123,(0,0,2):C.UVGC_133_124,(0,0,4):C.UVGC_133_125,(0,0,5):C.UVGC_133_126,(0,0,7):C.UVGC_133_127,(0,0,3):C.UVGC_133_128,(0,0,6):C.UVGC_133_129,(0,1,0):C.UVGC_134_130,(0,1,1):C.UVGC_134_131,(0,1,2):C.UVGC_134_132,(0,1,4):C.UVGC_134_133,(0,1,5):C.UVGC_134_134,(0,1,7):C.UVGC_134_135,(0,1,3):C.UVGC_134_136,(0,1,6):C.UVGC_134_137})

V_33 = CTVertex(name = 'V_33',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ], [ [P.u, P.Y1] ] ],
                couplings = {(0,0,0):C.UVGC_116_46,(0,0,1):C.UVGC_116_47,(0,0,2):C.UVGC_116_48,(0,0,3):C.UVGC_116_49,(0,0,4):C.UVGC_116_50,(0,0,5):C.UVGC_116_51,(0,0,6):C.UVGC_116_52,(0,1,0):C.UVGC_120_74,(0,1,1):C.UVGC_120_75,(0,1,2):C.UVGC_120_76,(0,1,3):C.UVGC_120_77,(0,1,4):C.UVGC_120_78,(0,1,5):C.UVGC_120_79,(0,1,6):C.UVGC_120_80})

V_34 = CTVertex(name = 'V_34',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ], [ [P.u, P.Y1] ] ],
                couplings = {(0,0,4):C.UVGC_75_155,(0,1,0):C.UVGC_102_4,(0,1,1):C.UVGC_102_5,(0,1,2):C.UVGC_102_6,(0,1,3):C.UVGC_102_7,(0,1,5):C.UVGC_102_8,(0,1,4):C.UVGC_102_9,(0,1,6):C.UVGC_110_18,(0,2,0):C.UVGC_102_4,(0,2,1):C.UVGC_102_5,(0,2,2):C.UVGC_102_6,(0,2,3):C.UVGC_102_7,(0,2,5):C.UVGC_102_8,(0,2,4):C.UVGC_102_9,(0,2,6):C.UVGC_111_19})

V_35 = CTVertex(name = 'V_35',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.c, P.Y1] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_75_155,(0,1,0):C.UVGC_102_4,(0,1,1):C.UVGC_102_5,(0,1,4):C.UVGC_102_6,(0,1,5):C.UVGC_102_7,(0,1,6):C.UVGC_102_8,(0,1,2):C.UVGC_102_9,(0,1,3):C.UVGC_98_192,(0,2,0):C.UVGC_102_4,(0,2,1):C.UVGC_102_5,(0,2,4):C.UVGC_102_6,(0,2,5):C.UVGC_102_7,(0,2,6):C.UVGC_102_8,(0,2,2):C.UVGC_102_9,(0,2,3):C.UVGC_99_193})

V_36 = CTVertex(name = 'V_36',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ], [ [P.t, P.Y1] ] ],
                couplings = {(0,0,4):C.UVGC_75_155,(0,1,0):C.UVGC_102_4,(0,1,1):C.UVGC_102_5,(0,1,2):C.UVGC_102_6,(0,1,3):C.UVGC_102_7,(0,1,5):C.UVGC_102_8,(0,1,4):C.UVGC_131_119,(0,1,6):C.UVGC_131_120,(0,2,0):C.UVGC_102_4,(0,2,1):C.UVGC_102_5,(0,2,2):C.UVGC_102_6,(0,2,3):C.UVGC_102_7,(0,2,5):C.UVGC_102_8,(0,2,4):C.UVGC_131_119,(0,2,6):C.UVGC_132_121})

V_37 = CTVertex(name = 'V_37',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.d, P.Y1] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_75_155,(0,1,0):C.UVGC_102_4,(0,1,1):C.UVGC_102_5,(0,1,4):C.UVGC_102_6,(0,1,5):C.UVGC_102_7,(0,1,6):C.UVGC_102_8,(0,1,2):C.UVGC_102_9,(0,1,3):C.UVGC_102_10,(0,2,0):C.UVGC_102_4,(0,2,1):C.UVGC_102_5,(0,2,4):C.UVGC_102_6,(0,2,5):C.UVGC_102_7,(0,2,6):C.UVGC_102_8,(0,2,2):C.UVGC_102_9,(0,2,3):C.UVGC_103_11})

V_38 = CTVertex(name = 'V_38',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.s, P.Y1] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_75_155,(0,1,0):C.UVGC_102_4,(0,1,1):C.UVGC_102_5,(0,1,2):C.UVGC_102_6,(0,1,3):C.UVGC_102_7,(0,1,6):C.UVGC_102_8,(0,1,4):C.UVGC_102_9,(0,1,5):C.UVGC_106_14,(0,2,0):C.UVGC_102_4,(0,2,1):C.UVGC_102_5,(0,2,2):C.UVGC_102_6,(0,2,3):C.UVGC_102_7,(0,2,6):C.UVGC_102_8,(0,2,4):C.UVGC_102_9,(0,2,5):C.UVGC_107_15})

V_39 = CTVertex(name = 'V_39',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.b, P.Y1] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_75_155,(0,1,0):C.UVGC_102_4,(0,1,3):C.UVGC_102_5,(0,1,4):C.UVGC_102_6,(0,1,5):C.UVGC_102_7,(0,1,6):C.UVGC_102_8,(0,1,1):C.UVGC_125_97,(0,1,2):C.UVGC_125_98,(0,2,0):C.UVGC_102_4,(0,2,3):C.UVGC_102_5,(0,2,4):C.UVGC_102_6,(0,2,5):C.UVGC_102_7,(0,2,6):C.UVGC_102_8,(0,2,1):C.UVGC_125_97,(0,2,2):C.UVGC_126_99})

V_40 = CTVertex(name = 'V_40',
                type = 'UV',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.Y1] ] ],
                couplings = {(0,1,0):C.UVGC_76_156,(0,1,1):C.UVGC_76_157,(0,3,0):C.UVGC_76_156,(0,3,1):C.UVGC_76_157,(0,4,0):C.UVGC_123_94,(0,4,1):C.UVGC_123_95,(0,2,0):C.UVGC_123_94,(0,2,1):C.UVGC_124_96,(0,0,0):C.UVGC_74_154})

V_41 = CTVertex(name = 'V_41',
                type = 'UV',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.c, P.g] ], [ [P.c, P.Y1] ] ],
                couplings = {(0,1,0):C.UVGC_100_1,(0,1,1):C.UVGC_97_191,(0,2,0):C.UVGC_100_1,(0,2,1):C.UVGC_96_190,(0,0,0):C.UVGC_74_154})

V_42 = CTVertex(name = 'V_42',
                type = 'UV',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.d, P.g] ], [ [P.d, P.Y1] ] ],
                couplings = {(0,1,0):C.UVGC_100_1,(0,1,1):C.UVGC_101_3,(0,2,0):C.UVGC_100_1,(0,2,1):C.UVGC_100_2,(0,0,0):C.UVGC_74_154})

V_43 = CTVertex(name = 'V_43',
                type = 'UV',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.s] ], [ [P.s, P.Y1] ] ],
                couplings = {(0,1,0):C.UVGC_100_1,(0,1,1):C.UVGC_105_13,(0,2,0):C.UVGC_100_1,(0,2,1):C.UVGC_104_12,(0,0,0):C.UVGC_74_154})

V_44 = CTVertex(name = 'V_44',
                type = 'UV',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ], [ [P.t, P.Y1] ] ],
                couplings = {(0,1,0):C.UVGC_135_138,(0,1,1):C.UVGC_135_139,(0,3,0):C.UVGC_135_138,(0,3,1):C.UVGC_135_139,(0,4,0):C.UVGC_129_116,(0,4,1):C.UVGC_129_117,(0,2,0):C.UVGC_129_116,(0,2,1):C.UVGC_130_118,(0,0,0):C.UVGC_74_154})

V_45 = CTVertex(name = 'V_45',
                type = 'UV',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.u] ], [ [P.u, P.Y1] ] ],
                couplings = {(0,1,0):C.UVGC_100_1,(0,1,1):C.UVGC_109_17,(0,2,0):C.UVGC_100_1,(0,2,1):C.UVGC_108_16,(0,0,0):C.UVGC_74_154})

V_46 = CTVertex(name = 'V_46',
                type = 'UV',
                particles = [ P.Y1, P.Y1 ],
                color = [ '1' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,1,0):C.UVGC_122_88,(0,1,1):C.UVGC_122_89,(0,1,2):C.UVGC_122_90,(0,1,3):C.UVGC_122_91,(0,1,4):C.UVGC_122_92,(0,1,5):C.UVGC_122_93,(0,2,0):C.UVGC_113_26,(0,2,1):C.UVGC_113_27,(0,2,2):C.UVGC_113_28,(0,2,3):C.UVGC_113_29,(0,2,4):C.UVGC_113_30,(0,2,5):C.UVGC_113_31,(0,0,0):C.UVGC_112_20,(0,0,1):C.UVGC_112_21,(0,0,2):C.UVGC_112_22,(0,0,3):C.UVGC_112_23,(0,0,4):C.UVGC_112_24,(0,0,5):C.UVGC_112_25})

V_47 = CTVertex(name = 'V_47',
                type = 'UV',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_88_160,(0,0,1):C.UVGC_88_161,(0,0,2):C.UVGC_88_162,(0,0,3):C.UVGC_88_163,(0,1,0):C.UVGC_87_158,(0,1,3):C.UVGC_87_159})

