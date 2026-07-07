# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Linux x86 (64-bit) (July 16, 2024)
# Date: Fri 3 Jul 2026 18:31:11


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
               couplings = {(0,0,0):C.R2GC_144_32,(0,0,1):C.R2GC_144_33})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,1,0):C.R2GC_110_5,(2,1,1):C.R2GC_110_6,(0,1,0):C.R2GC_110_5,(0,1,1):C.R2GC_110_6,(4,1,0):C.R2GC_108_1,(4,1,1):C.R2GC_108_2,(3,1,0):C.R2GC_108_1,(3,1,1):C.R2GC_108_2,(8,1,0):C.R2GC_109_3,(8,1,1):C.R2GC_109_4,(6,1,0):C.R2GC_113_10,(6,1,1):C.R2GC_154_39,(7,1,0):C.R2GC_114_12,(7,1,1):C.R2GC_153_38,(5,1,0):C.R2GC_108_1,(5,1,1):C.R2GC_108_2,(1,1,0):C.R2GC_108_1,(1,1,1):C.R2GC_108_2,(11,0,0):C.R2GC_112_8,(11,0,1):C.R2GC_112_9,(10,0,0):C.R2GC_112_8,(10,0,1):C.R2GC_112_9,(9,0,1):C.R2GC_111_7,(0,2,0):C.R2GC_110_5,(0,2,1):C.R2GC_110_6,(2,2,0):C.R2GC_110_5,(2,2,1):C.R2GC_110_6,(5,2,0):C.R2GC_108_1,(5,2,1):C.R2GC_108_2,(1,2,0):C.R2GC_108_1,(1,2,1):C.R2GC_108_2,(7,2,0):C.R2GC_114_12,(7,2,1):C.R2GC_114_13,(4,2,0):C.R2GC_108_1,(4,2,1):C.R2GC_108_2,(3,2,0):C.R2GC_108_1,(3,2,1):C.R2GC_108_2,(8,2,0):C.R2GC_109_3,(8,2,1):C.R2GC_155_40,(6,2,0):C.R2GC_150_34,(6,2,1):C.R2GC_150_35,(0,3,0):C.R2GC_110_5,(0,3,1):C.R2GC_110_6,(2,3,0):C.R2GC_110_5,(2,3,1):C.R2GC_110_6,(5,3,0):C.R2GC_108_1,(5,3,1):C.R2GC_108_2,(1,3,0):C.R2GC_108_1,(1,3,1):C.R2GC_108_2,(7,3,0):C.R2GC_151_36,(7,3,1):C.R2GC_110_6,(4,3,0):C.R2GC_108_1,(4,3,1):C.R2GC_108_2,(3,3,0):C.R2GC_108_1,(3,3,1):C.R2GC_108_2,(8,3,0):C.R2GC_109_3,(8,3,1):C.R2GC_152_37,(6,3,0):C.R2GC_113_10,(6,3,1):C.R2GC_113_11})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_142_31})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_165_47})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.Y1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_137_26,(0,1,0):C.R2GC_138_27})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.c__tilde__, P.c, P.Y1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               loop_particles = [ [ [P.c, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_62_50,(0,1,0):C.R2GC_63_51})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.d__tilde__, P.d, P.Y1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               loop_particles = [ [ [P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_66_52,(0,1,0):C.R2GC_67_53})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.s__tilde__, P.s, P.Y1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               loop_particles = [ [ [P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_70_54,(0,1,0):C.R2GC_71_55})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.Y1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV5, L.FFV6 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_159_41,(0,1,0):C.R2GC_160_42})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_74_56,(0,1,0):C.R2GC_75_57})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_117_16})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_117_16})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_117_16})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_115_14})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_115_14})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_115_14})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_116_15})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_116_15})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_116_15})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_116_15})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_116_15})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_116_15})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_131_21})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_133_23})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_127_17})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_129_19})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_162_44})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_132_22})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_128_18})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_134_24})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_130_20})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_166_48})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_163_45,(0,1,0):C.R2GC_164_46})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_163_45,(0,1,0):C.R2GC_164_46})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_163_45,(0,1,0):C.R2GC_164_46})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_140_29,(0,1,0):C.R2GC_141_30})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_140_29,(0,1,0):C.R2GC_141_30})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_140_29,(0,1,0):C.R2GC_141_30})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_135_25})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_135_25})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_161_43,(0,1,0):C.R2GC_135_25})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_135_25})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_135_25})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_139_28,(0,1,0):C.R2GC_135_25})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV2, L.VV3, L.VV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,2,2):C.R2GC_60_49,(0,0,0):C.R2GC_77_58,(0,0,3):C.R2GC_77_59,(0,1,1):C.R2GC_80_64})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_78_60,(0,0,1):C.R2GC_78_61})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.g, P.g, P.Y1, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_86_87,(0,0,1):C.R2GC_86_88,(0,0,2):C.R2GC_86_89,(0,0,3):C.R2GC_86_90,(0,0,4):C.R2GC_86_91,(0,0,5):C.R2GC_86_92})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Y1 ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_84_75,(0,0,1):C.R2GC_84_76,(0,0,2):C.R2GC_84_77,(0,0,3):C.R2GC_84_78,(0,0,4):C.R2GC_84_79,(0,0,5):C.R2GC_84_80})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.g, P.g, P.Y1, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_90_99,(0,0,1):C.R2GC_90_100,(0,0,2):C.R2GC_90_101,(0,0,3):C.R2GC_90_102,(0,0,4):C.R2GC_90_103,(0,0,5):C.R2GC_90_104})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Y1 ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV10 ],
                loop_particles = [ [ [P.b] ], [ [P.c] ], [ [P.d] ], [ [P.s] ], [ [P.t] ], [ [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_83_69,(1,0,1):C.R2GC_83_70,(1,0,2):C.R2GC_83_71,(1,0,3):C.R2GC_83_72,(1,0,4):C.R2GC_83_73,(1,0,5):C.R2GC_83_74,(0,1,0):C.R2GC_85_81,(0,1,1):C.R2GC_85_82,(0,1,2):C.R2GC_85_83,(0,1,3):C.R2GC_85_84,(0,1,4):C.R2GC_85_85,(0,1,5):C.R2GC_85_86})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_87_93,(0,0,1):C.R2GC_87_94})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_91_105,(0,0,1):C.R2GC_91_106})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b, P.t] ], [ [P.c, P.d] ], [ [P.c, P.s] ], [ [P.d, P.u] ], [ [P.s, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_96_107,(0,0,1):C.R2GC_96_108,(0,0,2):C.R2GC_96_109,(0,0,3):C.R2GC_96_110,(0,0,4):C.R2GC_96_111})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_81_65,(0,0,1):C.R2GC_81_66})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV10 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_89_97,(1,0,1):C.R2GC_89_98,(0,1,0):C.R2GC_88_95,(0,1,1):C.R2GC_88_96})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV10 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_82_67,(0,0,1):C.R2GC_82_68})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_79_62,(0,0,1):C.R2GC_79_63})

V_58 = CTVertex(name = 'V_58',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,1,0):C.UVGC_144_47,(0,1,1):C.UVGC_144_48,(0,1,4):C.UVGC_144_49,(0,2,2):C.UVGC_97_95,(0,0,3):C.UVGC_98_96})

V_59 = CTVertex(name = 'V_59',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(2,1,3):C.UVGC_109_9,(2,1,4):C.UVGC_109_8,(0,1,3):C.UVGC_109_9,(0,1,4):C.UVGC_109_8,(4,1,3):C.UVGC_108_6,(4,1,4):C.UVGC_108_7,(3,1,3):C.UVGC_108_6,(3,1,4):C.UVGC_108_7,(8,1,3):C.UVGC_109_8,(8,1,4):C.UVGC_109_9,(6,1,0):C.UVGC_153_68,(6,1,2):C.UVGC_153_69,(6,1,3):C.UVGC_154_73,(6,1,4):C.UVGC_154_74,(6,1,5):C.UVGC_153_72,(7,1,0):C.UVGC_153_68,(7,1,2):C.UVGC_153_69,(7,1,3):C.UVGC_153_70,(7,1,4):C.UVGC_153_71,(7,1,5):C.UVGC_153_72,(5,1,3):C.UVGC_108_6,(5,1,4):C.UVGC_108_7,(1,1,3):C.UVGC_108_6,(1,1,4):C.UVGC_108_7,(11,0,3):C.UVGC_112_12,(11,0,4):C.UVGC_112_13,(10,0,3):C.UVGC_112_12,(10,0,4):C.UVGC_112_13,(9,0,3):C.UVGC_111_10,(9,0,4):C.UVGC_111_11,(0,2,3):C.UVGC_109_9,(0,2,4):C.UVGC_109_8,(2,2,3):C.UVGC_109_9,(2,2,4):C.UVGC_109_8,(5,2,3):C.UVGC_108_6,(5,2,4):C.UVGC_108_7,(1,2,3):C.UVGC_108_6,(1,2,4):C.UVGC_108_7,(7,2,1):C.UVGC_113_14,(7,2,3):C.UVGC_114_16,(7,2,4):C.UVGC_114_17,(4,2,3):C.UVGC_108_6,(4,2,4):C.UVGC_108_7,(3,2,3):C.UVGC_108_6,(3,2,4):C.UVGC_108_7,(8,2,0):C.UVGC_155_75,(8,2,2):C.UVGC_155_76,(8,2,3):C.UVGC_155_77,(8,2,4):C.UVGC_155_78,(8,2,5):C.UVGC_155_79,(6,2,0):C.UVGC_150_57,(6,2,3):C.UVGC_150_58,(6,2,4):C.UVGC_150_59,(6,2,5):C.UVGC_150_60,(0,3,3):C.UVGC_109_9,(0,3,4):C.UVGC_109_8,(2,3,3):C.UVGC_109_9,(2,3,4):C.UVGC_109_8,(5,3,3):C.UVGC_108_6,(5,3,4):C.UVGC_108_7,(1,3,3):C.UVGC_108_6,(1,3,4):C.UVGC_108_7,(7,3,0):C.UVGC_150_57,(7,3,3):C.UVGC_151_61,(7,3,4):C.UVGC_151_62,(7,3,5):C.UVGC_150_60,(4,3,3):C.UVGC_108_6,(4,3,4):C.UVGC_108_7,(3,3,3):C.UVGC_108_6,(3,3,4):C.UVGC_108_7,(8,3,0):C.UVGC_152_63,(8,3,2):C.UVGC_152_64,(8,3,3):C.UVGC_152_65,(8,3,4):C.UVGC_152_66,(8,3,5):C.UVGC_152_67,(6,3,1):C.UVGC_113_14,(6,3,3):C.UVGC_113_15,(6,3,4):C.UVGC_111_10})

V_60 = CTVertex(name = 'V_60',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_142_44})

V_61 = CTVertex(name = 'V_61',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_165_91})

V_62 = CTVertex(name = 'V_62',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_137_39,(0,1,0):C.UVGC_138_40})

V_63 = CTVertex(name = 'V_63',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Y1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV5, L.FFV6 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_159_83,(0,1,0):C.UVGC_160_84})

V_64 = CTVertex(name = 'V_64',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_117_20,(0,1,0):C.UVGC_100_1,(0,2,0):C.UVGC_100_1})

V_65 = CTVertex(name = 'V_65',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_117_20,(0,1,0):C.UVGC_100_1,(0,2,0):C.UVGC_100_1})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_117_20,(0,1,0):C.UVGC_157_81,(0,2,0):C.UVGC_157_81})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_115_18,(0,1,0):C.UVGC_102_3,(0,2,0):C.UVGC_102_3})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_115_18,(0,1,0):C.UVGC_102_3,(0,2,0):C.UVGC_102_3})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_115_18,(0,1,0):C.UVGC_136_38,(0,2,0):C.UVGC_136_38})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_116_19,(0,1,0):C.UVGC_145_50,(0,1,1):C.UVGC_145_51,(0,1,2):C.UVGC_145_52,(0,1,3):C.UVGC_145_53,(0,1,5):C.UVGC_145_54,(0,1,4):C.UVGC_145_55,(0,2,0):C.UVGC_145_50,(0,2,1):C.UVGC_145_51,(0,2,2):C.UVGC_145_52,(0,2,3):C.UVGC_145_53,(0,2,5):C.UVGC_145_54,(0,2,4):C.UVGC_145_55})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_116_19,(0,1,0):C.UVGC_145_50,(0,1,1):C.UVGC_145_51,(0,1,3):C.UVGC_145_52,(0,1,4):C.UVGC_145_53,(0,1,5):C.UVGC_145_54,(0,1,2):C.UVGC_145_55,(0,2,0):C.UVGC_145_50,(0,2,1):C.UVGC_145_51,(0,2,3):C.UVGC_145_52,(0,2,4):C.UVGC_145_53,(0,2,5):C.UVGC_145_54,(0,2,2):C.UVGC_145_55})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_116_19,(0,1,0):C.UVGC_145_50,(0,1,1):C.UVGC_145_51,(0,1,2):C.UVGC_145_52,(0,1,3):C.UVGC_145_53,(0,1,5):C.UVGC_145_54,(0,1,4):C.UVGC_158_82,(0,2,0):C.UVGC_145_50,(0,2,1):C.UVGC_145_51,(0,2,2):C.UVGC_145_52,(0,2,3):C.UVGC_145_53,(0,2,5):C.UVGC_145_54,(0,2,4):C.UVGC_158_82})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_116_19,(0,1,0):C.UVGC_145_50,(0,1,1):C.UVGC_145_51,(0,1,3):C.UVGC_145_52,(0,1,4):C.UVGC_145_53,(0,1,5):C.UVGC_145_54,(0,1,2):C.UVGC_145_55,(0,2,0):C.UVGC_145_50,(0,2,1):C.UVGC_145_51,(0,2,3):C.UVGC_145_52,(0,2,4):C.UVGC_145_53,(0,2,5):C.UVGC_145_54,(0,2,2):C.UVGC_145_55})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_116_19,(0,1,0):C.UVGC_145_50,(0,1,1):C.UVGC_145_51,(0,1,2):C.UVGC_145_52,(0,1,3):C.UVGC_145_53,(0,1,5):C.UVGC_145_54,(0,1,4):C.UVGC_145_55,(0,2,0):C.UVGC_145_50,(0,2,1):C.UVGC_145_51,(0,2,2):C.UVGC_145_52,(0,2,3):C.UVGC_145_53,(0,2,5):C.UVGC_145_54,(0,2,4):C.UVGC_145_55})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_116_19,(0,1,0):C.UVGC_145_50,(0,1,2):C.UVGC_145_51,(0,1,3):C.UVGC_145_52,(0,1,4):C.UVGC_145_53,(0,1,5):C.UVGC_145_54,(0,1,1):C.UVGC_149_56,(0,2,0):C.UVGC_145_50,(0,2,2):C.UVGC_145_51,(0,2,3):C.UVGC_145_52,(0,2,4):C.UVGC_145_53,(0,2,5):C.UVGC_145_54,(0,2,1):C.UVGC_149_56})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_131_29,(0,0,1):C.UVGC_131_30})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.s__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_133_33,(0,0,1):C.UVGC_133_34})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.d__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_127_21,(0,0,0):C.UVGC_127_22})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_129_25,(0,0,1):C.UVGC_129_26})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_162_86,(0,0,2):C.UVGC_162_87,(0,0,1):C.UVGC_162_88})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_132_31,(0,0,1):C.UVGC_132_32})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.c__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.d, P.g] ], [ [P.c, P.g], [P.d, P.g] ] ],
                couplings = {(0,0,1):C.UVGC_128_23,(0,0,0):C.UVGC_128_24})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.u__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.g, P.s], [P.g, P.u] ], [ [P.g, P.s, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_134_35,(0,0,1):C.UVGC_134_36})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_130_27,(0,0,1):C.UVGC_130_28})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_166_92,(0,0,2):C.UVGC_166_93,(0,0,1):C.UVGC_166_94})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_163_89,(0,1,0):C.UVGC_164_90})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_140_42,(0,1,0):C.UVGC_141_43})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_101_2})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_101_2})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_161_85,(0,1,0):C.UVGC_156_80})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_101_2})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_101_2})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_139_41,(0,1,0):C.UVGC_135_37})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV5 ],
                loop_particles = [ [ [P.b] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,1,0):C.UVGC_143_45,(0,1,3):C.UVGC_143_46,(0,0,1):C.UVGC_107_4,(0,0,2):C.UVGC_107_5})

