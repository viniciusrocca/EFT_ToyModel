# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Linux x86 (64-bit) (July 16, 2024)
# Date: Fri 6 Feb 2026 14:03:43


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
               couplings = {(0,0,0):C.R2GC_135_24,(0,0,1):C.R2GC_135_25,(0,1,0):C.R2GC_143_26,(0,1,1):C.R2GC_143_27,(0,2,0):C.R2GC_143_26,(0,2,1):C.R2GC_143_27,(0,3,0):C.R2GC_135_24,(0,3,1):C.R2GC_135_25,(0,4,0):C.R2GC_135_24,(0,4,1):C.R2GC_135_25,(0,5,0):C.R2GC_143_26,(0,5,1):C.R2GC_143_27})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.psiT], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_116_10,(2,0,1):C.R2GC_116_11,(0,0,0):C.R2GC_116_10,(0,0,1):C.R2GC_116_11,(4,0,0):C.R2GC_114_6,(4,0,1):C.R2GC_114_7,(3,0,0):C.R2GC_114_6,(3,0,1):C.R2GC_114_7,(8,0,0):C.R2GC_115_8,(8,0,1):C.R2GC_115_9,(6,0,0):C.R2GC_119_15,(6,0,1):C.R2GC_150_33,(7,0,0):C.R2GC_120_17,(7,0,1):C.R2GC_149_32,(5,0,0):C.R2GC_114_6,(5,0,1):C.R2GC_114_7,(1,0,0):C.R2GC_114_6,(1,0,1):C.R2GC_114_7,(11,0,0):C.R2GC_118_13,(11,0,1):C.R2GC_118_14,(10,0,0):C.R2GC_118_13,(10,0,1):C.R2GC_118_14,(9,0,1):C.R2GC_117_12,(0,1,0):C.R2GC_116_10,(0,1,1):C.R2GC_116_11,(2,1,0):C.R2GC_116_10,(2,1,1):C.R2GC_116_11,(5,1,0):C.R2GC_114_6,(5,1,1):C.R2GC_114_7,(1,1,0):C.R2GC_114_6,(1,1,1):C.R2GC_114_7,(7,1,0):C.R2GC_120_17,(7,1,1):C.R2GC_120_18,(4,1,0):C.R2GC_114_6,(4,1,1):C.R2GC_114_7,(3,1,0):C.R2GC_114_6,(3,1,1):C.R2GC_114_7,(8,1,0):C.R2GC_115_8,(8,1,1):C.R2GC_151_34,(6,1,0):C.R2GC_146_28,(6,1,1):C.R2GC_146_29,(11,1,0):C.R2GC_118_13,(11,1,1):C.R2GC_118_14,(10,1,0):C.R2GC_118_13,(10,1,1):C.R2GC_118_14,(9,1,1):C.R2GC_117_12,(0,2,0):C.R2GC_116_10,(0,2,1):C.R2GC_116_11,(2,2,0):C.R2GC_116_10,(2,2,1):C.R2GC_116_11,(5,2,0):C.R2GC_114_6,(5,2,1):C.R2GC_114_7,(1,2,0):C.R2GC_114_6,(1,2,1):C.R2GC_114_7,(7,2,0):C.R2GC_147_30,(7,2,1):C.R2GC_116_11,(4,2,0):C.R2GC_114_6,(4,2,1):C.R2GC_114_7,(3,2,0):C.R2GC_114_6,(3,2,1):C.R2GC_114_7,(8,2,0):C.R2GC_115_8,(8,2,1):C.R2GC_148_31,(6,2,0):C.R2GC_119_15,(6,2,1):C.R2GC_119_16,(11,2,0):C.R2GC_118_13,(11,2,1):C.R2GC_118_14,(10,2,0):C.R2GC_118_13,(10,2,1):C.R2GC_118_14,(9,2,1):C.R2GC_117_12})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.psiT__tilde__, P.t, P.P__tilde__SDM ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.psiT, P.t] ], [ [P.psiT, P.P__tilde__SDM, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_165_40,(0,0,1):C.R2GC_165_41})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.t__tilde__, P.psiT, P.P__tilde__SDM ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.psiT, P.t] ], [ [P.psiT, P.P__tilde__SDM, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_165_40,(0,0,1):C.R2GC_165_41})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.psiT__tilde__, P.psiT, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               loop_particles = [ [ [P.g, P.psiT] ], [ [P.P__tilde__SDM, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_103_1,(0,1,1):C.R2GC_156_36})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_103_1})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.c, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_103_1})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               loop_particles = [ [ [P.g, P.t] ], [ [P.psiT, P.P__tilde__SDM] ] ],
               couplings = {(0,0,0):C.R2GC_103_1,(0,1,1):C.R2GC_156_36})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_103_1})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_103_1})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_103_1})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.psiT__tilde__, P.psiT ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.psiT] ] ],
                couplings = {(0,0,0):C.R2GC_164_39,(0,2,0):C.R2GC_164_39,(0,1,0):C.R2GC_123_20,(0,3,0):C.R2GC_123_20})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_154_35,(0,2,0):C.R2GC_154_35,(0,1,0):C.R2GC_123_20,(0,3,0):C.R2GC_123_20})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_123_20})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_123_20})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_123_20})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_123_20})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_122_19,(0,2,0):C.R2GC_122_19,(0,1,0):C.R2GC_123_20,(0,3,0):C.R2GC_123_20})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.P__tilde__SDM, P.P__tilde__SDM ],
                color = [ '1' ],
                lorentz = [ L.SS1, L.SS2 ],
                loop_particles = [ [ [P.psiT, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_158_38,(0,1,0):C.R2GC_157_37})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.psiT], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.psiT] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.R2GC_134_23,(0,1,0):C.R2GC_105_3,(0,1,3):C.R2GC_105_4,(0,1,4):C.R2GC_105_5,(0,2,1):C.R2GC_133_21,(0,2,2):C.R2GC_133_22})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.g, P.g, P.P__tilde__SDM, P.P__tilde__SDM ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.psiT, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_104_2})

V_22 = CTVertex(name = 'V_22',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.psiT] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_135_31,(0,0,1):C.UVGC_135_32,(0,0,2):C.UVGC_135_33,(0,0,3):C.UVGC_113_7,(0,0,4):C.UVGC_135_34,(0,0,5):C.UVGC_135_35,(0,1,0):C.UVGC_143_48,(0,1,1):C.UVGC_143_49,(0,1,2):C.UVGC_143_50,(0,1,3):C.UVGC_143_51,(0,1,4):C.UVGC_143_52,(0,1,5):C.UVGC_143_53,(0,3,0):C.UVGC_143_48,(0,3,1):C.UVGC_143_49,(0,3,2):C.UVGC_145_56,(0,3,3):C.UVGC_112_5,(0,3,4):C.UVGC_143_52,(0,3,5):C.UVGC_143_53,(0,5,0):C.UVGC_135_31,(0,5,1):C.UVGC_135_32,(0,5,2):C.UVGC_137_38,(0,5,3):C.UVGC_137_39,(0,5,4):C.UVGC_135_34,(0,5,5):C.UVGC_135_35,(0,6,0):C.UVGC_135_31,(0,6,1):C.UVGC_135_32,(0,6,2):C.UVGC_136_36,(0,6,3):C.UVGC_136_37,(0,6,4):C.UVGC_135_34,(0,6,5):C.UVGC_135_35,(0,7,0):C.UVGC_143_48,(0,7,1):C.UVGC_143_49,(0,7,2):C.UVGC_144_54,(0,7,3):C.UVGC_144_55,(0,7,4):C.UVGC_143_52,(0,7,5):C.UVGC_143_53,(0,2,2):C.UVGC_112_4,(0,2,3):C.UVGC_112_5,(0,4,2):C.UVGC_113_6,(0,4,3):C.UVGC_113_7})

V_23 = CTVertex(name = 'V_23',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.psiT], [P.s], [P.t], [P.u] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.psiT] ], [ [P.t] ] ],
                couplings = {(2,0,3):C.UVGC_115_11,(2,0,4):C.UVGC_115_10,(0,0,3):C.UVGC_115_11,(0,0,4):C.UVGC_115_10,(4,0,3):C.UVGC_114_8,(4,0,4):C.UVGC_114_9,(3,0,3):C.UVGC_114_8,(3,0,4):C.UVGC_114_9,(8,0,3):C.UVGC_115_10,(8,0,4):C.UVGC_115_11,(6,0,0):C.UVGC_149_70,(6,0,2):C.UVGC_149_71,(6,0,3):C.UVGC_150_76,(6,0,4):C.UVGC_150_77,(6,0,5):C.UVGC_149_74,(6,0,6):C.UVGC_149_75,(7,0,0):C.UVGC_149_70,(7,0,2):C.UVGC_149_71,(7,0,3):C.UVGC_149_72,(7,0,4):C.UVGC_149_73,(7,0,5):C.UVGC_149_74,(7,0,6):C.UVGC_149_75,(5,0,3):C.UVGC_114_8,(5,0,4):C.UVGC_114_9,(1,0,3):C.UVGC_114_8,(1,0,4):C.UVGC_114_9,(11,0,3):C.UVGC_118_14,(11,0,4):C.UVGC_118_15,(10,0,3):C.UVGC_118_14,(10,0,4):C.UVGC_118_15,(9,0,3):C.UVGC_117_12,(9,0,4):C.UVGC_117_13,(0,1,3):C.UVGC_115_11,(0,1,4):C.UVGC_115_10,(2,1,3):C.UVGC_115_11,(2,1,4):C.UVGC_115_10,(5,1,3):C.UVGC_114_8,(5,1,4):C.UVGC_114_9,(1,1,3):C.UVGC_114_8,(1,1,4):C.UVGC_114_9,(7,1,1):C.UVGC_119_16,(7,1,3):C.UVGC_120_18,(7,1,4):C.UVGC_120_19,(4,1,3):C.UVGC_114_8,(4,1,4):C.UVGC_114_9,(3,1,3):C.UVGC_114_8,(3,1,4):C.UVGC_114_9,(8,1,0):C.UVGC_151_78,(8,1,2):C.UVGC_151_79,(8,1,3):C.UVGC_151_80,(8,1,4):C.UVGC_151_81,(8,1,5):C.UVGC_151_82,(8,1,6):C.UVGC_151_83,(6,1,0):C.UVGC_146_57,(6,1,3):C.UVGC_146_58,(6,1,4):C.UVGC_146_59,(6,1,5):C.UVGC_146_60,(6,1,6):C.UVGC_146_61,(11,1,3):C.UVGC_118_14,(11,1,4):C.UVGC_118_15,(10,1,3):C.UVGC_118_14,(10,1,4):C.UVGC_118_15,(9,1,3):C.UVGC_117_12,(9,1,4):C.UVGC_117_13,(0,2,3):C.UVGC_115_11,(0,2,4):C.UVGC_115_10,(2,2,3):C.UVGC_115_11,(2,2,4):C.UVGC_115_10,(5,2,3):C.UVGC_114_8,(5,2,4):C.UVGC_114_9,(1,2,3):C.UVGC_114_8,(1,2,4):C.UVGC_114_9,(7,2,0):C.UVGC_146_57,(7,2,3):C.UVGC_147_62,(7,2,4):C.UVGC_147_63,(7,2,5):C.UVGC_146_60,(7,2,6):C.UVGC_146_61,(4,2,3):C.UVGC_114_8,(4,2,4):C.UVGC_114_9,(3,2,3):C.UVGC_114_8,(3,2,4):C.UVGC_114_9,(8,2,0):C.UVGC_148_64,(8,2,2):C.UVGC_148_65,(8,2,3):C.UVGC_148_66,(8,2,4):C.UVGC_148_67,(8,2,5):C.UVGC_148_68,(8,2,6):C.UVGC_148_69,(6,2,1):C.UVGC_119_16,(6,2,3):C.UVGC_119_17,(6,2,4):C.UVGC_117_12,(11,2,3):C.UVGC_118_14,(11,2,4):C.UVGC_118_15,(10,2,3):C.UVGC_118_14,(10,2,4):C.UVGC_118_15,(9,2,3):C.UVGC_117_12,(9,2,4):C.UVGC_117_13})

V_24 = CTVertex(name = 'V_24',
                type = 'UV',
                particles = [ P.psiT__tilde__, P.t, P.P__tilde__SDM ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.psiT] ], [ [P.g, P.psiT, P.t] ], [ [P.g, P.t] ], [ [P.psiT, P.P__tilde__SDM] ], [ [P.psiT, P.P__tilde__SDM, P.t] ], [ [P.psiT, P.t] ], [ [P.P__tilde__SDM, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_165_104,(0,0,2):C.UVGC_165_105,(0,0,3):C.UVGC_165_106,(0,0,5):C.UVGC_165_107,(0,0,6):C.UVGC_165_108,(0,0,1):C.UVGC_165_109,(0,0,4):C.UVGC_165_110})

V_25 = CTVertex(name = 'V_25',
                type = 'UV',
                particles = [ P.t__tilde__, P.psiT, P.P__tilde__SDM ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.psiT] ], [ [P.g, P.psiT, P.t] ], [ [P.g, P.t] ], [ [P.psiT, P.P__tilde__SDM] ], [ [P.psiT, P.P__tilde__SDM, P.t] ], [ [P.psiT, P.t] ], [ [P.P__tilde__SDM, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_165_104,(0,0,2):C.UVGC_165_105,(0,0,3):C.UVGC_165_106,(0,0,5):C.UVGC_165_107,(0,0,6):C.UVGC_165_108,(0,0,1):C.UVGC_165_109,(0,0,4):C.UVGC_165_110})

V_26 = CTVertex(name = 'V_26',
                type = 'UV',
                particles = [ P.psiT__tilde__, P.psiT, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.psiT] ], [ [P.psiT] ], [ [P.P__tilde__SDM, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,6):C.UVGC_161_99,(0,3,4):C.UVGC_108_2,(0,4,0):C.UVGC_138_40,(0,4,1):C.UVGC_138_41,(0,4,2):C.UVGC_138_42,(0,4,3):C.UVGC_138_43,(0,4,5):C.UVGC_138_44,(0,4,7):C.UVGC_138_45,(0,4,4):C.UVGC_159_95,(0,4,6):C.UVGC_159_96,(0,2,6):C.UVGC_110_3,(0,1,6):C.UVGC_163_101})

V_27 = CTVertex(name = 'V_27',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.psiT] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_108_2,(0,1,0):C.UVGC_138_40,(0,1,1):C.UVGC_138_41,(0,1,2):C.UVGC_138_42,(0,1,3):C.UVGC_138_43,(0,1,5):C.UVGC_138_44,(0,1,6):C.UVGC_138_45,(0,1,4):C.UVGC_138_46,(0,2,0):C.UVGC_138_40,(0,2,1):C.UVGC_138_41,(0,2,2):C.UVGC_138_42,(0,2,3):C.UVGC_138_43,(0,2,5):C.UVGC_138_44,(0,2,6):C.UVGC_138_45,(0,2,4):C.UVGC_138_46})

V_28 = CTVertex(name = 'V_28',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.psiT] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_108_2,(0,1,0):C.UVGC_138_40,(0,1,1):C.UVGC_138_41,(0,1,3):C.UVGC_138_42,(0,1,4):C.UVGC_138_43,(0,1,5):C.UVGC_138_44,(0,1,6):C.UVGC_138_45,(0,1,2):C.UVGC_138_46,(0,2,0):C.UVGC_138_40,(0,2,1):C.UVGC_138_41,(0,2,3):C.UVGC_138_42,(0,2,4):C.UVGC_138_43,(0,2,5):C.UVGC_138_44,(0,2,6):C.UVGC_138_45,(0,2,2):C.UVGC_138_46})

V_29 = CTVertex(name = 'V_29',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.psiT] ], [ [P.psiT, P.P__tilde__SDM] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_108_2,(0,2,0):C.UVGC_138_40,(0,2,1):C.UVGC_138_41,(0,2,2):C.UVGC_138_42,(0,2,3):C.UVGC_138_43,(0,2,5):C.UVGC_138_44,(0,2,7):C.UVGC_138_45,(0,2,4):C.UVGC_153_86,(0,2,6):C.UVGC_156_91,(0,1,0):C.UVGC_138_40,(0,1,1):C.UVGC_138_41,(0,1,2):C.UVGC_138_42,(0,1,3):C.UVGC_138_43,(0,1,5):C.UVGC_138_44,(0,1,7):C.UVGC_138_45,(0,1,4):C.UVGC_153_86,(0,1,6):C.UVGC_153_87})

V_30 = CTVertex(name = 'V_30',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.psiT] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_108_2,(0,1,0):C.UVGC_138_40,(0,1,1):C.UVGC_138_41,(0,1,3):C.UVGC_138_42,(0,1,4):C.UVGC_138_43,(0,1,5):C.UVGC_138_44,(0,1,6):C.UVGC_138_45,(0,1,2):C.UVGC_138_46,(0,2,0):C.UVGC_138_40,(0,2,1):C.UVGC_138_41,(0,2,3):C.UVGC_138_42,(0,2,4):C.UVGC_138_43,(0,2,5):C.UVGC_138_44,(0,2,6):C.UVGC_138_45,(0,2,2):C.UVGC_138_46})

V_31 = CTVertex(name = 'V_31',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.psiT] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_108_2,(0,1,0):C.UVGC_138_40,(0,1,1):C.UVGC_138_41,(0,1,2):C.UVGC_138_42,(0,1,3):C.UVGC_138_43,(0,1,5):C.UVGC_138_44,(0,1,6):C.UVGC_138_45,(0,1,4):C.UVGC_138_46,(0,2,0):C.UVGC_138_40,(0,2,1):C.UVGC_138_41,(0,2,2):C.UVGC_138_42,(0,2,3):C.UVGC_138_43,(0,2,5):C.UVGC_138_44,(0,2,6):C.UVGC_138_45,(0,2,4):C.UVGC_138_46})

V_32 = CTVertex(name = 'V_32',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.psiT] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_108_2,(0,1,0):C.UVGC_138_40,(0,1,2):C.UVGC_138_41,(0,1,3):C.UVGC_138_42,(0,1,4):C.UVGC_138_43,(0,1,5):C.UVGC_138_44,(0,1,6):C.UVGC_138_45,(0,1,1):C.UVGC_142_47,(0,2,0):C.UVGC_138_40,(0,2,2):C.UVGC_138_41,(0,2,3):C.UVGC_138_42,(0,2,4):C.UVGC_138_43,(0,2,5):C.UVGC_138_44,(0,2,6):C.UVGC_138_45,(0,2,1):C.UVGC_142_47})

V_33 = CTVertex(name = 'V_33',
                type = 'UV',
                particles = [ P.psiT__tilde__, P.psiT ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.psiT] ], [ [P.P__tilde__SDM, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_164_102,(0,0,1):C.UVGC_164_103,(0,2,0):C.UVGC_164_102,(0,2,1):C.UVGC_164_103,(0,1,0):C.UVGC_160_97,(0,1,1):C.UVGC_160_98,(0,3,0):C.UVGC_160_97,(0,3,1):C.UVGC_162_100})

V_34 = CTVertex(name = 'V_34',
                type = 'UV',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ], [ [P.psiT, P.P__tilde__SDM] ] ],
                couplings = {(0,0,0):C.UVGC_154_88,(0,0,1):C.UVGC_154_89,(0,2,0):C.UVGC_154_88,(0,2,1):C.UVGC_154_89,(0,1,0):C.UVGC_152_84,(0,1,1):C.UVGC_152_85,(0,3,0):C.UVGC_152_84,(0,3,1):C.UVGC_155_90})

V_35 = CTVertex(name = 'V_35',
                type = 'UV',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_123_21,(0,1,0):C.UVGC_106_1,(0,2,0):C.UVGC_106_1})

V_36 = CTVertex(name = 'V_36',
                type = 'UV',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_123_21,(0,1,0):C.UVGC_106_1,(0,2,0):C.UVGC_106_1})

V_37 = CTVertex(name = 'V_37',
                type = 'UV',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_123_21,(0,1,0):C.UVGC_106_1,(0,2,0):C.UVGC_106_1})

V_38 = CTVertex(name = 'V_38',
                type = 'UV',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_123_21,(0,1,0):C.UVGC_106_1,(0,2,0):C.UVGC_106_1})

V_39 = CTVertex(name = 'V_39',
                type = 'UV',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_122_20,(0,2,0):C.UVGC_122_20,(0,1,0):C.UVGC_132_22,(0,3,0):C.UVGC_132_22})

V_40 = CTVertex(name = 'V_40',
                type = 'UV',
                particles = [ P.P__tilde__SDM, P.P__tilde__SDM ],
                color = [ '1' ],
                lorentz = [ L.SS1, L.SS2 ],
                loop_particles = [ [ [P.psiT, P.t] ], [ [P.P__tilde__SDM] ] ],
                couplings = {(0,0,1):C.UVGC_158_93,(0,0,0):C.UVGC_158_94,(0,1,0):C.UVGC_157_92})

V_41 = CTVertex(name = 'V_41',
                type = 'UV',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.g] ], [ [P.ghG] ], [ [P.psiT] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_134_26,(0,0,1):C.UVGC_134_27,(0,0,2):C.UVGC_134_28,(0,0,3):C.UVGC_134_29,(0,0,4):C.UVGC_134_30,(0,1,0):C.UVGC_133_23,(0,1,3):C.UVGC_133_24,(0,1,4):C.UVGC_133_25})

