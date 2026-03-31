# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Linux x86 (64-bit) (July 16, 2024)
# Date: Mon 23 Jun 2025 11:21:31


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV1, L.VVV2, L.VVV4, L.VVV6, L.VVV7, L.VVV8 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.psiT], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_138_24,(0,0,1):C.R2GC_138_25,(0,1,0):C.R2GC_146_26,(0,1,1):C.R2GC_146_27,(0,2,0):C.R2GC_146_26,(0,2,1):C.R2GC_146_27,(0,3,0):C.R2GC_138_24,(0,3,1):C.R2GC_138_25,(0,4,0):C.R2GC_138_24,(0,4,1):C.R2GC_138_25,(0,5,0):C.R2GC_146_26,(0,5,1):C.R2GC_146_27})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.psiT], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_119_10,(2,0,1):C.R2GC_119_11,(0,0,0):C.R2GC_119_10,(0,0,1):C.R2GC_119_11,(4,0,0):C.R2GC_117_6,(4,0,1):C.R2GC_117_7,(3,0,0):C.R2GC_117_6,(3,0,1):C.R2GC_117_7,(8,0,0):C.R2GC_118_8,(8,0,1):C.R2GC_118_9,(6,0,0):C.R2GC_122_15,(6,0,1):C.R2GC_153_33,(7,0,0):C.R2GC_123_17,(7,0,1):C.R2GC_152_32,(5,0,0):C.R2GC_117_6,(5,0,1):C.R2GC_117_7,(1,0,0):C.R2GC_117_6,(1,0,1):C.R2GC_117_7,(11,0,0):C.R2GC_121_13,(11,0,1):C.R2GC_121_14,(10,0,0):C.R2GC_121_13,(10,0,1):C.R2GC_121_14,(9,0,1):C.R2GC_120_12,(0,1,0):C.R2GC_119_10,(0,1,1):C.R2GC_119_11,(2,1,0):C.R2GC_119_10,(2,1,1):C.R2GC_119_11,(5,1,0):C.R2GC_117_6,(5,1,1):C.R2GC_117_7,(1,1,0):C.R2GC_117_6,(1,1,1):C.R2GC_117_7,(7,1,0):C.R2GC_123_17,(7,1,1):C.R2GC_123_18,(4,1,0):C.R2GC_117_6,(4,1,1):C.R2GC_117_7,(3,1,0):C.R2GC_117_6,(3,1,1):C.R2GC_117_7,(8,1,0):C.R2GC_118_8,(8,1,1):C.R2GC_154_34,(6,1,0):C.R2GC_149_28,(6,1,1):C.R2GC_149_29,(11,1,0):C.R2GC_121_13,(11,1,1):C.R2GC_121_14,(10,1,0):C.R2GC_121_13,(10,1,1):C.R2GC_121_14,(9,1,1):C.R2GC_120_12,(0,2,0):C.R2GC_119_10,(0,2,1):C.R2GC_119_11,(2,2,0):C.R2GC_119_10,(2,2,1):C.R2GC_119_11,(5,2,0):C.R2GC_117_6,(5,2,1):C.R2GC_117_7,(1,2,0):C.R2GC_117_6,(1,2,1):C.R2GC_117_7,(7,2,0):C.R2GC_150_30,(7,2,1):C.R2GC_119_11,(4,2,0):C.R2GC_117_6,(4,2,1):C.R2GC_117_7,(3,2,0):C.R2GC_117_6,(3,2,1):C.R2GC_117_7,(8,2,0):C.R2GC_118_8,(8,2,1):C.R2GC_151_31,(6,2,0):C.R2GC_122_15,(6,2,1):C.R2GC_122_16,(11,2,0):C.R2GC_121_13,(11,2,1):C.R2GC_121_14,(10,2,0):C.R2GC_121_13,(10,2,1):C.R2GC_121_14,(9,2,1):C.R2GC_120_12})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.psiT__tilde__, P.t, P.P__tilde__SDM ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.psiT, P.t] ], [ [P.psiT, P.P__tilde__SDM, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_168_40,(0,0,1):C.R2GC_168_41})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.t__tilde__, P.psiT, P.P__tilde__SDM ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               loop_particles = [ [ [P.g, P.psiT, P.t] ], [ [P.psiT, P.P__tilde__SDM, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_168_40,(0,0,1):C.R2GC_168_41})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.psiT__tilde__, P.psiT, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               loop_particles = [ [ [P.g, P.psiT] ], [ [P.P__tilde__SDM, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_106_1,(0,1,1):C.R2GC_159_36})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_106_1})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.c, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_106_1})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               loop_particles = [ [ [P.g, P.t] ], [ [P.psiT, P.P__tilde__SDM] ] ],
               couplings = {(0,0,0):C.R2GC_106_1,(0,1,1):C.R2GC_159_36})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_106_1})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_106_1})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_106_1})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.psiT__tilde__, P.psiT ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.psiT] ] ],
                couplings = {(0,0,0):C.R2GC_167_39,(0,2,0):C.R2GC_167_39,(0,1,0):C.R2GC_126_20,(0,3,0):C.R2GC_126_20})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_157_35,(0,2,0):C.R2GC_157_35,(0,1,0):C.R2GC_126_20,(0,3,0):C.R2GC_126_20})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_126_20})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_126_20})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_126_20})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_126_20})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_125_19,(0,2,0):C.R2GC_125_19,(0,1,0):C.R2GC_126_20,(0,3,0):C.R2GC_126_20})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.P__tilde__SDM, P.P__tilde__SDM ],
                color = [ '1' ],
                lorentz = [ L.SS1, L.SS2 ],
                loop_particles = [ [ [P.psiT, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_161_38,(0,1,0):C.R2GC_160_37})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.psiT], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.psiT] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.R2GC_137_23,(0,1,0):C.R2GC_108_3,(0,1,3):C.R2GC_108_4,(0,1,4):C.R2GC_108_5,(0,2,1):C.R2GC_136_21,(0,2,2):C.R2GC_136_22})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.g, P.g, P.P__tilde__SDM, P.P__tilde__SDM ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.psiT, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_107_2})

V_22 = CTVertex(name = 'V_22',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.psiT] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_138_31,(0,0,1):C.UVGC_138_32,(0,0,2):C.UVGC_138_33,(0,0,3):C.UVGC_116_7,(0,0,4):C.UVGC_138_34,(0,0,5):C.UVGC_138_35,(0,1,0):C.UVGC_146_48,(0,1,1):C.UVGC_146_49,(0,1,2):C.UVGC_146_50,(0,1,3):C.UVGC_146_51,(0,1,4):C.UVGC_146_52,(0,1,5):C.UVGC_146_53,(0,3,0):C.UVGC_146_48,(0,3,1):C.UVGC_146_49,(0,3,2):C.UVGC_148_56,(0,3,3):C.UVGC_115_5,(0,3,4):C.UVGC_146_52,(0,3,5):C.UVGC_146_53,(0,5,0):C.UVGC_138_31,(0,5,1):C.UVGC_138_32,(0,5,2):C.UVGC_140_38,(0,5,3):C.UVGC_140_39,(0,5,4):C.UVGC_138_34,(0,5,5):C.UVGC_138_35,(0,6,0):C.UVGC_138_31,(0,6,1):C.UVGC_138_32,(0,6,2):C.UVGC_139_36,(0,6,3):C.UVGC_139_37,(0,6,4):C.UVGC_138_34,(0,6,5):C.UVGC_138_35,(0,7,0):C.UVGC_146_48,(0,7,1):C.UVGC_146_49,(0,7,2):C.UVGC_147_54,(0,7,3):C.UVGC_147_55,(0,7,4):C.UVGC_146_52,(0,7,5):C.UVGC_146_53,(0,2,2):C.UVGC_115_4,(0,2,3):C.UVGC_115_5,(0,4,2):C.UVGC_116_6,(0,4,3):C.UVGC_116_7})

V_23 = CTVertex(name = 'V_23',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.psiT], [P.s], [P.t], [P.u] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.psiT] ], [ [P.t] ] ],
                couplings = {(2,0,3):C.UVGC_118_11,(2,0,4):C.UVGC_118_10,(0,0,3):C.UVGC_118_11,(0,0,4):C.UVGC_118_10,(4,0,3):C.UVGC_117_8,(4,0,4):C.UVGC_117_9,(3,0,3):C.UVGC_117_8,(3,0,4):C.UVGC_117_9,(8,0,3):C.UVGC_118_10,(8,0,4):C.UVGC_118_11,(6,0,0):C.UVGC_152_70,(6,0,2):C.UVGC_152_71,(6,0,3):C.UVGC_153_76,(6,0,4):C.UVGC_153_77,(6,0,5):C.UVGC_152_74,(6,0,6):C.UVGC_152_75,(7,0,0):C.UVGC_152_70,(7,0,2):C.UVGC_152_71,(7,0,3):C.UVGC_152_72,(7,0,4):C.UVGC_152_73,(7,0,5):C.UVGC_152_74,(7,0,6):C.UVGC_152_75,(5,0,3):C.UVGC_117_8,(5,0,4):C.UVGC_117_9,(1,0,3):C.UVGC_117_8,(1,0,4):C.UVGC_117_9,(11,0,3):C.UVGC_121_14,(11,0,4):C.UVGC_121_15,(10,0,3):C.UVGC_121_14,(10,0,4):C.UVGC_121_15,(9,0,3):C.UVGC_120_12,(9,0,4):C.UVGC_120_13,(0,1,3):C.UVGC_118_11,(0,1,4):C.UVGC_118_10,(2,1,3):C.UVGC_118_11,(2,1,4):C.UVGC_118_10,(5,1,3):C.UVGC_117_8,(5,1,4):C.UVGC_117_9,(1,1,3):C.UVGC_117_8,(1,1,4):C.UVGC_117_9,(7,1,1):C.UVGC_122_16,(7,1,3):C.UVGC_123_18,(7,1,4):C.UVGC_123_19,(4,1,3):C.UVGC_117_8,(4,1,4):C.UVGC_117_9,(3,1,3):C.UVGC_117_8,(3,1,4):C.UVGC_117_9,(8,1,0):C.UVGC_154_78,(8,1,2):C.UVGC_154_79,(8,1,3):C.UVGC_154_80,(8,1,4):C.UVGC_154_81,(8,1,5):C.UVGC_154_82,(8,1,6):C.UVGC_154_83,(6,1,0):C.UVGC_149_57,(6,1,3):C.UVGC_149_58,(6,1,4):C.UVGC_149_59,(6,1,5):C.UVGC_149_60,(6,1,6):C.UVGC_149_61,(11,1,3):C.UVGC_121_14,(11,1,4):C.UVGC_121_15,(10,1,3):C.UVGC_121_14,(10,1,4):C.UVGC_121_15,(9,1,3):C.UVGC_120_12,(9,1,4):C.UVGC_120_13,(0,2,3):C.UVGC_118_11,(0,2,4):C.UVGC_118_10,(2,2,3):C.UVGC_118_11,(2,2,4):C.UVGC_118_10,(5,2,3):C.UVGC_117_8,(5,2,4):C.UVGC_117_9,(1,2,3):C.UVGC_117_8,(1,2,4):C.UVGC_117_9,(7,2,0):C.UVGC_149_57,(7,2,3):C.UVGC_150_62,(7,2,4):C.UVGC_150_63,(7,2,5):C.UVGC_149_60,(7,2,6):C.UVGC_149_61,(4,2,3):C.UVGC_117_8,(4,2,4):C.UVGC_117_9,(3,2,3):C.UVGC_117_8,(3,2,4):C.UVGC_117_9,(8,2,0):C.UVGC_151_64,(8,2,2):C.UVGC_151_65,(8,2,3):C.UVGC_151_66,(8,2,4):C.UVGC_151_67,(8,2,5):C.UVGC_151_68,(8,2,6):C.UVGC_151_69,(6,2,1):C.UVGC_122_16,(6,2,3):C.UVGC_122_17,(6,2,4):C.UVGC_120_12,(11,2,3):C.UVGC_121_14,(11,2,4):C.UVGC_121_15,(10,2,3):C.UVGC_121_14,(10,2,4):C.UVGC_121_15,(9,2,3):C.UVGC_120_12,(9,2,4):C.UVGC_120_13})

V_24 = CTVertex(name = 'V_24',
                type = 'UV',
                particles = [ P.psiT__tilde__, P.t, P.P__tilde__SDM ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.psiT] ], [ [P.g, P.psiT, P.t] ], [ [P.g, P.t] ], [ [P.psiT, P.P__tilde__SDM] ], [ [P.psiT, P.P__tilde__SDM, P.t] ], [ [P.psiT, P.t] ], [ [P.P__tilde__SDM, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_168_104,(0,0,2):C.UVGC_168_105,(0,0,3):C.UVGC_168_106,(0,0,5):C.UVGC_168_107,(0,0,6):C.UVGC_168_108,(0,0,1):C.UVGC_168_109,(0,0,4):C.UVGC_168_110})

V_25 = CTVertex(name = 'V_25',
                type = 'UV',
                particles = [ P.t__tilde__, P.psiT, P.P__tilde__SDM ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.psiT] ], [ [P.g, P.psiT, P.t] ], [ [P.g, P.t] ], [ [P.psiT, P.P__tilde__SDM] ], [ [P.psiT, P.P__tilde__SDM, P.t] ], [ [P.psiT, P.t] ], [ [P.P__tilde__SDM, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_168_104,(0,0,2):C.UVGC_168_105,(0,0,3):C.UVGC_168_106,(0,0,5):C.UVGC_168_107,(0,0,6):C.UVGC_168_108,(0,0,1):C.UVGC_168_109,(0,0,4):C.UVGC_168_110})

V_26 = CTVertex(name = 'V_26',
                type = 'UV',
                particles = [ P.psiT__tilde__, P.psiT, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.psiT] ], [ [P.psiT] ], [ [P.P__tilde__SDM, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,6):C.UVGC_164_99,(0,3,4):C.UVGC_111_2,(0,4,0):C.UVGC_141_40,(0,4,1):C.UVGC_141_41,(0,4,2):C.UVGC_141_42,(0,4,3):C.UVGC_141_43,(0,4,5):C.UVGC_141_44,(0,4,7):C.UVGC_141_45,(0,4,4):C.UVGC_162_95,(0,4,6):C.UVGC_162_96,(0,2,6):C.UVGC_113_3,(0,1,6):C.UVGC_166_101})

V_27 = CTVertex(name = 'V_27',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.psiT] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_111_2,(0,1,0):C.UVGC_141_40,(0,1,1):C.UVGC_141_41,(0,1,2):C.UVGC_141_42,(0,1,3):C.UVGC_141_43,(0,1,5):C.UVGC_141_44,(0,1,6):C.UVGC_141_45,(0,1,4):C.UVGC_141_46,(0,2,0):C.UVGC_141_40,(0,2,1):C.UVGC_141_41,(0,2,2):C.UVGC_141_42,(0,2,3):C.UVGC_141_43,(0,2,5):C.UVGC_141_44,(0,2,6):C.UVGC_141_45,(0,2,4):C.UVGC_141_46})

V_28 = CTVertex(name = 'V_28',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.psiT] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_111_2,(0,1,0):C.UVGC_141_40,(0,1,1):C.UVGC_141_41,(0,1,3):C.UVGC_141_42,(0,1,4):C.UVGC_141_43,(0,1,5):C.UVGC_141_44,(0,1,6):C.UVGC_141_45,(0,1,2):C.UVGC_141_46,(0,2,0):C.UVGC_141_40,(0,2,1):C.UVGC_141_41,(0,2,3):C.UVGC_141_42,(0,2,4):C.UVGC_141_43,(0,2,5):C.UVGC_141_44,(0,2,6):C.UVGC_141_45,(0,2,2):C.UVGC_141_46})

V_29 = CTVertex(name = 'V_29',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.psiT] ], [ [P.psiT, P.P__tilde__SDM] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_111_2,(0,2,0):C.UVGC_141_40,(0,2,1):C.UVGC_141_41,(0,2,2):C.UVGC_141_42,(0,2,3):C.UVGC_141_43,(0,2,5):C.UVGC_141_44,(0,2,7):C.UVGC_141_45,(0,2,4):C.UVGC_156_86,(0,2,6):C.UVGC_159_91,(0,1,0):C.UVGC_141_40,(0,1,1):C.UVGC_141_41,(0,1,2):C.UVGC_141_42,(0,1,3):C.UVGC_141_43,(0,1,5):C.UVGC_141_44,(0,1,7):C.UVGC_141_45,(0,1,4):C.UVGC_156_86,(0,1,6):C.UVGC_156_87})

V_30 = CTVertex(name = 'V_30',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.psiT] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_111_2,(0,1,0):C.UVGC_141_40,(0,1,1):C.UVGC_141_41,(0,1,3):C.UVGC_141_42,(0,1,4):C.UVGC_141_43,(0,1,5):C.UVGC_141_44,(0,1,6):C.UVGC_141_45,(0,1,2):C.UVGC_141_46,(0,2,0):C.UVGC_141_40,(0,2,1):C.UVGC_141_41,(0,2,3):C.UVGC_141_42,(0,2,4):C.UVGC_141_43,(0,2,5):C.UVGC_141_44,(0,2,6):C.UVGC_141_45,(0,2,2):C.UVGC_141_46})

V_31 = CTVertex(name = 'V_31',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.psiT] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_111_2,(0,1,0):C.UVGC_141_40,(0,1,1):C.UVGC_141_41,(0,1,2):C.UVGC_141_42,(0,1,3):C.UVGC_141_43,(0,1,5):C.UVGC_141_44,(0,1,6):C.UVGC_141_45,(0,1,4):C.UVGC_141_46,(0,2,0):C.UVGC_141_40,(0,2,1):C.UVGC_141_41,(0,2,2):C.UVGC_141_42,(0,2,3):C.UVGC_141_43,(0,2,5):C.UVGC_141_44,(0,2,6):C.UVGC_141_45,(0,2,4):C.UVGC_141_46})

V_32 = CTVertex(name = 'V_32',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.psiT] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_111_2,(0,1,0):C.UVGC_141_40,(0,1,2):C.UVGC_141_41,(0,1,3):C.UVGC_141_42,(0,1,4):C.UVGC_141_43,(0,1,5):C.UVGC_141_44,(0,1,6):C.UVGC_141_45,(0,1,1):C.UVGC_145_47,(0,2,0):C.UVGC_141_40,(0,2,2):C.UVGC_141_41,(0,2,3):C.UVGC_141_42,(0,2,4):C.UVGC_141_43,(0,2,5):C.UVGC_141_44,(0,2,6):C.UVGC_141_45,(0,2,1):C.UVGC_145_47})

V_33 = CTVertex(name = 'V_33',
                type = 'UV',
                particles = [ P.psiT__tilde__, P.psiT ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.psiT] ], [ [P.P__tilde__SDM, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_167_102,(0,0,1):C.UVGC_167_103,(0,2,0):C.UVGC_167_102,(0,2,1):C.UVGC_167_103,(0,1,0):C.UVGC_163_97,(0,1,1):C.UVGC_163_98,(0,3,0):C.UVGC_163_97,(0,3,1):C.UVGC_165_100})

V_34 = CTVertex(name = 'V_34',
                type = 'UV',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ], [ [P.psiT, P.P__tilde__SDM] ] ],
                couplings = {(0,0,0):C.UVGC_157_88,(0,0,1):C.UVGC_157_89,(0,2,0):C.UVGC_157_88,(0,2,1):C.UVGC_157_89,(0,1,0):C.UVGC_155_84,(0,1,1):C.UVGC_155_85,(0,3,0):C.UVGC_155_84,(0,3,1):C.UVGC_158_90})

V_35 = CTVertex(name = 'V_35',
                type = 'UV',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_126_21,(0,1,0):C.UVGC_109_1,(0,2,0):C.UVGC_109_1})

V_36 = CTVertex(name = 'V_36',
                type = 'UV',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_126_21,(0,1,0):C.UVGC_109_1,(0,2,0):C.UVGC_109_1})

V_37 = CTVertex(name = 'V_37',
                type = 'UV',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_126_21,(0,1,0):C.UVGC_109_1,(0,2,0):C.UVGC_109_1})

V_38 = CTVertex(name = 'V_38',
                type = 'UV',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_126_21,(0,1,0):C.UVGC_109_1,(0,2,0):C.UVGC_109_1})

V_39 = CTVertex(name = 'V_39',
                type = 'UV',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_125_20,(0,2,0):C.UVGC_125_20,(0,1,0):C.UVGC_135_22,(0,3,0):C.UVGC_135_22})

V_40 = CTVertex(name = 'V_40',
                type = 'UV',
                particles = [ P.P__tilde__SDM, P.P__tilde__SDM ],
                color = [ '1' ],
                lorentz = [ L.SS1, L.SS2 ],
                loop_particles = [ [ [P.psiT, P.t] ], [ [P.P__tilde__SDM] ] ],
                couplings = {(0,0,1):C.UVGC_161_93,(0,0,0):C.UVGC_161_94,(0,1,0):C.UVGC_160_92})

V_41 = CTVertex(name = 'V_41',
                type = 'UV',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.g] ], [ [P.ghG] ], [ [P.psiT] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_137_26,(0,0,1):C.UVGC_137_27,(0,0,2):C.UVGC_137_28,(0,0,3):C.UVGC_137_29,(0,0,4):C.UVGC_137_30,(0,1,0):C.UVGC_136_23,(0,1,3):C.UVGC_136_24,(0,1,4):C.UVGC_136_25})

