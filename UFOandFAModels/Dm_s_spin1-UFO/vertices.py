# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Linux x86 (64-bit) (July 16, 2024)
# Date: Mon 22 Jun 2026 17:31:18


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.ghG, P.ghG__tilde__, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_1})

V_2 = Vertex(name = 'V_2',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_1})

V_3 = Vertex(name = 'V_3',
             particles = [ P.g, P.g, P.g, P.g ],
             color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
             lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3 ],
             couplings = {(1,1):C.GC_3,(0,0):C.GC_3,(2,2):C.GC_3})

V_4 = Vertex(name = 'V_4',
             particles = [ P.c__tilde__, P.c, P.g ],
             color = [ 'T(3,2,1)' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_2})

V_5 = Vertex(name = 'V_5',
             particles = [ P.t__tilde__, P.t, P.g ],
             color = [ 'T(3,2,1)' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_2})

V_6 = Vertex(name = 'V_6',
             particles = [ P.u__tilde__, P.u, P.g ],
             color = [ 'T(3,2,1)' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_2})

V_7 = Vertex(name = 'V_7',
             particles = [ P.b__tilde__, P.b, P.g ],
             color = [ 'T(3,2,1)' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_2})

V_8 = Vertex(name = 'V_8',
             particles = [ P.d__tilde__, P.d, P.g ],
             color = [ 'T(3,2,1)' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_2})

V_9 = Vertex(name = 'V_9',
             particles = [ P.s__tilde__, P.s, P.g ],
             color = [ 'T(3,2,1)' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_2})

V_10 = Vertex(name = 'V_10',
              particles = [ P.Y1, P.Xc__tilde__, P.Xc ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_21})

V_11 = Vertex(name = 'V_11',
              particles = [ P.b__tilde__, P.b, P.Y1 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_7,(0,0):C.GC_16})

V_12 = Vertex(name = 'V_12',
              particles = [ P.d__tilde__, P.b, P.Y1 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_6,(0,0):C.GC_15})

V_13 = Vertex(name = 'V_13',
              particles = [ P.c__tilde__, P.c, P.Y1 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_9,(0,0):C.GC_18})

V_14 = Vertex(name = 'V_14',
              particles = [ P.b__tilde__, P.d, P.Y1 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_6,(0,0):C.GC_15})

V_15 = Vertex(name = 'V_15',
              particles = [ P.d__tilde__, P.d, P.Y1 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_4,(0,0):C.GC_13})

V_16 = Vertex(name = 'V_16',
              particles = [ P.s__tilde__, P.s, P.Y1 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_5,(0,0):C.GC_14})

V_17 = Vertex(name = 'V_17',
              particles = [ P.t__tilde__, P.t, P.Y1 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_11,(0,0):C.GC_20})

V_18 = Vertex(name = 'V_18',
              particles = [ P.u__tilde__, P.t, P.Y1 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_10,(0,0):C.GC_19})

V_19 = Vertex(name = 'V_19',
              particles = [ P.t__tilde__, P.u, P.Y1 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_10,(0,0):C.GC_19})

V_20 = Vertex(name = 'V_20',
              particles = [ P.u__tilde__, P.u, P.Y1 ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_8,(0,0):C.GC_17})

V_21 = Vertex(name = 'V_21',
              particles = [ P.Xd__tilde__, P.Xd, P.Y1 ],
              color = [ '1' ],
              lorentz = [ L.FFV1, L.FFV2 ],
              couplings = {(0,1):C.GC_12,(0,0):C.GC_22})

