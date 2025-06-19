# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Linux x86 (64-bit) (July 16, 2024)
# Date: Thu 19 Jun 2025 16:02:55


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSSSS1 ],
             couplings = {(0,0):C.GC_11})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_25})

V_3 = Vertex(name = 'V_3',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_53})

V_4 = Vertex(name = 'V_4',
             particles = [ P.H, P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSSS1 ],
             couplings = {(0,0):C.GC_50})

V_5 = Vertex(name = 'V_5',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_51})

V_6 = Vertex(name = 'V_6',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_54})

V_7 = Vertex(name = 'V_7',
             particles = [ P.ghG, P.ghG__tilde__, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_17})

V_8 = Vertex(name = 'V_8',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV1, L.VVV2 ],
             couplings = {(0,1):C.GC_10,(0,0):C.GC_17})

V_9 = Vertex(name = 'V_9',
             particles = [ P.g, P.g, P.g, P.g ],
             color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
             lorentz = [ L.VVVV1, L.VVVV2, L.VVVV4, L.VVVV5, L.VVVV7, L.VVVV8 ],
             couplings = {(0,1):C.GC_19,(1,5):C.GC_19,(2,4):C.GC_19,(1,2):C.GC_20,(0,0):C.GC_20,(2,3):C.GC_20})

V_10 = Vertex(name = 'V_10',
              particles = [ P.g, P.g, P.g, P.g, P.g ],
              color = [ 'f(-2,1,2)*f(-1,-2,3)*f(4,5,-1)', 'f(-2,1,2)*f(-1,-2,4)*f(3,5,-1)', 'f(-2,1,2)*f(-1,-2,5)*f(3,4,-1)', 'f(-2,1,3)*f(-1,-2,2)*f(4,5,-1)', 'f(-2,1,3)*f(-1,-2,4)*f(2,5,-1)', 'f(-2,1,3)*f(-1,-2,5)*f(2,4,-1)', 'f(-2,1,4)*f(-1,-2,2)*f(3,5,-1)', 'f(-2,1,4)*f(-1,-2,3)*f(2,5,-1)', 'f(-2,1,4)*f(-1,-2,5)*f(2,3,-1)', 'f(-2,1,5)*f(-1,-2,2)*f(3,4,-1)', 'f(-2,1,5)*f(-1,-2,3)*f(2,4,-1)', 'f(-2,1,5)*f(-1,-2,4)*f(2,3,-1)', 'f(-2,2,3)*f(-1,-2,1)*f(4,5,-1)', 'f(-2,2,3)*f(-1,-2,4)*f(1,5,-1)', 'f(-2,2,3)*f(-1,-2,5)*f(1,4,-1)', 'f(-2,2,4)*f(-1,-2,1)*f(3,5,-1)', 'f(-2,2,4)*f(-1,-2,3)*f(1,5,-1)', 'f(-2,2,4)*f(-1,-2,5)*f(1,3,-1)', 'f(-2,2,5)*f(-1,-2,1)*f(3,4,-1)', 'f(-2,2,5)*f(-1,-2,3)*f(1,4,-1)', 'f(-2,2,5)*f(-1,-2,4)*f(1,3,-1)', 'f(-2,3,4)*f(-1,-2,1)*f(2,5,-1)', 'f(-2,3,4)*f(-1,-2,2)*f(1,5,-1)', 'f(-2,3,4)*f(-1,-2,5)*f(1,2,-1)', 'f(-2,3,5)*f(-1,-2,1)*f(2,4,-1)', 'f(-2,3,5)*f(-1,-2,2)*f(1,4,-1)', 'f(-2,3,5)*f(-1,-2,4)*f(1,2,-1)', 'f(-2,4,5)*f(-1,-2,1)*f(2,3,-1)', 'f(-2,4,5)*f(-1,-2,2)*f(1,3,-1)', 'f(-2,4,5)*f(-1,-2,3)*f(1,2,-1)' ],
              lorentz = [ L.VVVVV1, L.VVVVV10, L.VVVVV11, L.VVVVV12, L.VVVVV13, L.VVVVV14, L.VVVVV15, L.VVVVV2, L.VVVVV3, L.VVVVV4, L.VVVVV5, L.VVVVV6, L.VVVVV7, L.VVVVV8, L.VVVVV9 ],
              couplings = {(24,9):C.GC_22,(21,10):C.GC_21,(18,10):C.GC_22,(15,9):C.GC_21,(28,7):C.GC_22,(22,14):C.GC_22,(9,14):C.GC_21,(3,7):C.GC_21,(29,8):C.GC_22,(16,1):C.GC_22,(10,1):C.GC_21,(0,8):C.GC_21,(26,4):C.GC_21,(20,3):C.GC_21,(4,3):C.GC_22,(1,4):C.GC_22,(25,13):C.GC_22,(6,13):C.GC_21,(19,2):C.GC_22,(7,2):C.GC_21,(23,6):C.GC_21,(17,5):C.GC_21,(5,5):C.GC_22,(2,6):C.GC_22,(27,0):C.GC_22,(12,0):C.GC_21,(13,11):C.GC_22,(11,11):C.GC_21,(14,12):C.GC_21,(8,12):C.GC_22})

V_11 = Vertex(name = 'V_11',
              particles = [ P.g, P.g, P.g, P.g, P.g, P.g ],
              color = [ 'f(-3,1,2)*f(-2,3,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,2)*f(-2,3,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,2)*f(-2,3,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,2)*f(-2,4,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,2)*f(-2,4,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,2)*f(-2,5,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,3)*f(-2,2,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,3)*f(-2,2,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,3)*f(-2,2,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,3)*f(-2,4,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,3)*f(-2,4,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,3)*f(-2,5,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,4)*f(-2,2,3)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,4)*f(-2,2,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,4)*f(-2,2,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,4)*f(-2,3,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,4)*f(-2,3,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,4)*f(-2,5,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,1,5)*f(-2,2,3)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,5)*f(-2,2,4)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,5)*f(-2,2,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,5)*f(-2,3,4)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,5)*f(-2,3,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,5)*f(-2,4,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,1,6)*f(-2,2,3)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,6)*f(-2,2,4)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,6)*f(-2,2,5)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,6)*f(-2,3,4)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,6)*f(-2,3,5)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,6)*f(-2,4,5)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,2,3)*f(-2,1,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,2,3)*f(-2,1,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,2,3)*f(-2,1,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,2,3)*f(-2,4,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,3)*f(-2,4,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,3)*f(-2,5,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,4)*f(-2,1,3)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,2,4)*f(-2,1,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,2,4)*f(-2,1,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,2,4)*f(-2,3,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,4)*f(-2,3,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,4)*f(-2,5,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,2,5)*f(-2,1,3)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,2,5)*f(-2,1,4)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,2,5)*f(-2,1,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,2,5)*f(-2,3,4)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,5)*f(-2,3,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,5)*f(-2,4,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,2,6)*f(-2,1,3)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,2,6)*f(-2,1,4)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,2,6)*f(-2,1,5)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,2,6)*f(-2,3,4)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,6)*f(-2,3,5)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,6)*f(-2,4,5)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,3,4)*f(-2,1,2)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,3,4)*f(-2,1,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,3,4)*f(-2,1,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,3,4)*f(-2,2,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,3,4)*f(-2,2,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,3,4)*f(-2,5,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,3,5)*f(-2,1,2)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,3,5)*f(-2,1,4)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,3,5)*f(-2,1,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,3,5)*f(-2,2,4)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,3,5)*f(-2,2,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,3,5)*f(-2,4,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,3,6)*f(-2,1,2)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,3,6)*f(-2,1,4)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,3,6)*f(-2,1,5)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,3,6)*f(-2,2,4)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,3,6)*f(-2,2,5)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,3,6)*f(-2,4,5)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,4,5)*f(-2,1,2)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,4,5)*f(-2,1,3)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,4,5)*f(-2,1,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,4,5)*f(-2,2,3)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,4,5)*f(-2,2,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,4,5)*f(-2,3,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,4,6)*f(-2,1,2)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,4,6)*f(-2,1,3)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,4,6)*f(-2,1,5)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,4,6)*f(-2,2,3)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,4,6)*f(-2,2,5)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,4,6)*f(-2,3,5)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,5,6)*f(-2,1,2)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,5,6)*f(-2,1,3)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,5,6)*f(-2,1,4)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,5,6)*f(-2,2,3)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,5,6)*f(-2,2,4)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,5,6)*f(-2,3,4)*f(-1,-2,-3)*f(1,2,-1)' ],
              lorentz = [ L.VVVVVV1, L.VVVVVV10, L.VVVVVV11, L.VVVVVV12, L.VVVVVV13, L.VVVVVV14, L.VVVVVV15, L.VVVVVV2, L.VVVVVV3, L.VVVVVV4, L.VVVVVV5, L.VVVVVV6, L.VVVVVV7, L.VVVVVV8, L.VVVVVV9 ],
              couplings = {(65,9):C.GC_24,(71,11):C.GC_23,(77,11):C.GC_24,(83,9):C.GC_23,(41,7):C.GC_24,(53,1):C.GC_24,(76,1):C.GC_23,(88,7):C.GC_23,(35,8):C.GC_24,(52,4):C.GC_24,(64,4):C.GC_23,(87,8):C.GC_23,(34,3):C.GC_23,(40,2):C.GC_23,(69,2):C.GC_24,(81,3):C.GC_24,(17,8):C.GC_23,(23,3):C.GC_24,(80,3):C.GC_23,(86,8):C.GC_24,(11,7):C.GC_23,(22,2):C.GC_24,(68,2):C.GC_23,(85,7):C.GC_24,(9,1):C.GC_23,(15,4):C.GC_23,(61,4):C.GC_24,(73,1):C.GC_24,(4,9):C.GC_23,(14,4):C.GC_24,(49,4):C.GC_23,(78,9):C.GC_24,(3,11):C.GC_24,(19,2):C.GC_23,(37,2):C.GC_24,(72,11):C.GC_23,(2,11):C.GC_23,(8,1):C.GC_24,(48,1):C.GC_23,(66,11):C.GC_24,(1,9):C.GC_24,(18,3):C.GC_23,(31,3):C.GC_24,(60,9):C.GC_23,(6,7):C.GC_24,(12,8):C.GC_24,(30,8):C.GC_23,(36,7):C.GC_23,(47,13):C.GC_24,(82,13):C.GC_23,(46,5):C.GC_24,(70,5):C.GC_23,(33,6):C.GC_23,(39,14):C.GC_23,(63,14):C.GC_24,(75,6):C.GC_24,(29,6):C.GC_24,(74,6):C.GC_23,(28,14):C.GC_24,(62,14):C.GC_23,(10,13):C.GC_23,(16,5):C.GC_23,(67,5):C.GC_24,(79,13):C.GC_24,(25,14):C.GC_23,(38,14):C.GC_24,(13,5):C.GC_24,(43,5):C.GC_23,(24,6):C.GC_23,(32,6):C.GC_24,(7,13):C.GC_24,(42,13):C.GC_23,(59,0):C.GC_24,(89,0):C.GC_23,(51,10):C.GC_24,(58,10):C.GC_23,(21,10):C.GC_23,(55,10):C.GC_24,(5,0):C.GC_23,(20,10):C.GC_24,(50,10):C.GC_23,(84,0):C.GC_24,(0,0):C.GC_24,(54,0):C.GC_23,(45,12):C.GC_23,(57,12):C.GC_24,(27,12):C.GC_24,(56,12):C.GC_23,(26,12):C.GC_23,(44,12):C.GC_24})

V_12 = Vertex(name = 'V_12',
              particles = [ P.d__tilde__, P.d, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_60})

V_13 = Vertex(name = 'V_13',
              particles = [ P.s__tilde__, P.s, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_63})

V_14 = Vertex(name = 'V_14',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_58})

V_15 = Vertex(name = 'V_15',
              particles = [ P.e__plus__, P.e__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_61})

V_16 = Vertex(name = 'V_16',
              particles = [ P.mu__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_62})

V_17 = Vertex(name = 'V_17',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_65})

V_18 = Vertex(name = 'V_18',
              particles = [ P.u__tilde__, P.u, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_66})

V_19 = Vertex(name = 'V_19',
              particles = [ P.c__tilde__, P.c, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_59})

V_20 = Vertex(name = 'V_20',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_64})

V_21 = Vertex(name = 'V_21',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_15})

V_22 = Vertex(name = 'V_22',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_26})

V_23 = Vertex(name = 'V_23',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_52})

V_24 = Vertex(name = 'V_24',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_16})

V_25 = Vertex(name = 'V_25',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_39})

V_26 = Vertex(name = 'V_26',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_27})

V_27 = Vertex(name = 'V_27',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV6 ],
              couplings = {(0,0):C.GC_40})

V_28 = Vertex(name = 'V_28',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_49})

V_29 = Vertex(name = 'V_29',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_56})

V_30 = Vertex(name = 'V_30',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_28})

V_31 = Vertex(name = 'V_31',
              particles = [ P.e__plus__, P.e__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_14})

V_32 = Vertex(name = 'V_32',
              particles = [ P.mu__plus__, P.mu__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_14})

V_33 = Vertex(name = 'V_33',
              particles = [ P.ta__plus__, P.ta__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_14})

V_34 = Vertex(name = 'V_34',
              particles = [ P.u__tilde__, P.u, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_13})

V_35 = Vertex(name = 'V_35',
              particles = [ P.c__tilde__, P.c, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_13})

V_36 = Vertex(name = 'V_36',
              particles = [ P.t__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_13})

V_37 = Vertex(name = 'V_37',
              particles = [ P.d__tilde__, P.d, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_12})

V_38 = Vertex(name = 'V_38',
              particles = [ P.s__tilde__, P.s, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_12})

V_39 = Vertex(name = 'V_39',
              particles = [ P.b__tilde__, P.b, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_12})

V_40 = Vertex(name = 'V_40',
              particles = [ P.u__tilde__, P.u, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_18})

V_41 = Vertex(name = 'V_41',
              particles = [ P.c__tilde__, P.c, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_18})

V_42 = Vertex(name = 'V_42',
              particles = [ P.t__tilde__, P.t, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_18})

V_43 = Vertex(name = 'V_43',
              particles = [ P.d__tilde__, P.d, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_18})

V_44 = Vertex(name = 'V_44',
              particles = [ P.s__tilde__, P.s, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_18})

V_45 = Vertex(name = 'V_45',
              particles = [ P.b__tilde__, P.b, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_18})

V_46 = Vertex(name = 'V_46',
              particles = [ P.d__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_30})

V_47 = Vertex(name = 'V_47',
              particles = [ P.s__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_31})

V_48 = Vertex(name = 'V_48',
              particles = [ P.b__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_32})

V_49 = Vertex(name = 'V_49',
              particles = [ P.d__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_33})

V_50 = Vertex(name = 'V_50',
              particles = [ P.s__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_34})

V_51 = Vertex(name = 'V_51',
              particles = [ P.b__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_35})

V_52 = Vertex(name = 'V_52',
              particles = [ P.d__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_36})

V_53 = Vertex(name = 'V_53',
              particles = [ P.s__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_37})

V_54 = Vertex(name = 'V_54',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_38})

V_55 = Vertex(name = 'V_55',
              particles = [ P.u__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_67})

V_56 = Vertex(name = 'V_56',
              particles = [ P.c__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_70})

V_57 = Vertex(name = 'V_57',
              particles = [ P.t__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_73})

V_58 = Vertex(name = 'V_58',
              particles = [ P.u__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_68})

V_59 = Vertex(name = 'V_59',
              particles = [ P.c__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_71})

V_60 = Vertex(name = 'V_60',
              particles = [ P.t__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_74})

V_61 = Vertex(name = 'V_61',
              particles = [ P.u__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_69})

V_62 = Vertex(name = 'V_62',
              particles = [ P.c__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_72})

V_63 = Vertex(name = 'V_63',
              particles = [ P.t__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_75})

V_64 = Vertex(name = 'V_64',
              particles = [ P.e__plus__, P.ve, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_29})

V_65 = Vertex(name = 'V_65',
              particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_29})

V_66 = Vertex(name = 'V_66',
              particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_29})

V_67 = Vertex(name = 'V_67',
              particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_29})

V_68 = Vertex(name = 'V_68',
              particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_29})

V_69 = Vertex(name = 'V_69',
              particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_29})

V_70 = Vertex(name = 'V_70',
              particles = [ P.u__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_45,(0,1):C.GC_42})

V_71 = Vertex(name = 'V_71',
              particles = [ P.c__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_45,(0,1):C.GC_42})

V_72 = Vertex(name = 'V_72',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_45,(0,1):C.GC_42})

V_73 = Vertex(name = 'V_73',
              particles = [ P.d__tilde__, P.d, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_44,(0,1):C.GC_41})

V_74 = Vertex(name = 'V_74',
              particles = [ P.d__tilde__, P.d, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_57})

V_75 = Vertex(name = 'V_75',
              particles = [ P.s__tilde__, P.s, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_44,(0,1):C.GC_41})

V_76 = Vertex(name = 'V_76',
              particles = [ P.s__tilde__, P.s, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_57})

V_77 = Vertex(name = 'V_77',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_44,(0,1):C.GC_41})

V_78 = Vertex(name = 'V_78',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV3 ],
              couplings = {(0,0):C.GC_57})

V_79 = Vertex(name = 'V_79',
              particles = [ P.ve__tilde__, P.ve, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_47})

V_80 = Vertex(name = 'V_80',
              particles = [ P.vm__tilde__, P.vm, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_47})

V_81 = Vertex(name = 'V_81',
              particles = [ P.vt__tilde__, P.vt, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_47})

V_82 = Vertex(name = 'V_82',
              particles = [ P.e__plus__, P.e__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_46,(0,1):C.GC_43})

V_83 = Vertex(name = 'V_83',
              particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_46,(0,1):C.GC_43})

V_84 = Vertex(name = 'V_84',
              particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_46,(0,1):C.GC_43})

V_85 = Vertex(name = 'V_85',
              particles = [ P.d__tilde__, P.d, P.Z, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVSS1 ],
              couplings = {(0,0):C.GC_48})

V_86 = Vertex(name = 'V_86',
              particles = [ P.s__tilde__, P.s, P.Z, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVSS1 ],
              couplings = {(0,0):C.GC_48})

V_87 = Vertex(name = 'V_87',
              particles = [ P.b__tilde__, P.b, P.Z, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVSS1 ],
              couplings = {(0,0):C.GC_48})

V_88 = Vertex(name = 'V_88',
              particles = [ P.d__tilde__, P.d, P.Z, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1 ],
              couplings = {(0,0):C.GC_55})

V_89 = Vertex(name = 'V_89',
              particles = [ P.s__tilde__, P.s, P.Z, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1 ],
              couplings = {(0,0):C.GC_55})

V_90 = Vertex(name = 'V_90',
              particles = [ P.b__tilde__, P.b, P.Z, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1 ],
              couplings = {(0,0):C.GC_55})

V_91 = Vertex(name = 'V_91',
              particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF1, L.FFFF2 ],
              couplings = {(0,0):C.GC_7,(0,1):C.GC_7})

V_92 = Vertex(name = 'V_92',
              particles = [ P.mu__plus__, P.e__minus__, P.e__plus__, P.mu__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF1, L.FFFF2 ],
              couplings = {(0,0):C.GC_6,(0,1):C.GC_6})

V_93 = Vertex(name = 'V_93',
              particles = [ P.ta__plus__, P.e__minus__, P.e__plus__, P.ta__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF1, L.FFFF2 ],
              couplings = {(0,0):C.GC_6,(0,1):C.GC_6})

V_94 = Vertex(name = 'V_94',
              particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF1, L.FFFF2 ],
              couplings = {(0,0):C.GC_7,(0,1):C.GC_7})

V_95 = Vertex(name = 'V_95',
              particles = [ P.ta__plus__, P.mu__minus__, P.mu__plus__, P.ta__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF1, L.FFFF2 ],
              couplings = {(0,0):C.GC_6,(0,1):C.GC_6})

V_96 = Vertex(name = 'V_96',
              particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.ta__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFFF1, L.FFFF2 ],
              couplings = {(0,0):C.GC_7,(0,1):C.GC_7})

V_97 = Vertex(name = 'V_97',
              particles = [ P.d__tilde__, P.d, P.e__plus__, P.e__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_5})

V_98 = Vertex(name = 'V_98',
              particles = [ P.d__tilde__, P.d, P.mu__plus__, P.mu__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_5})

V_99 = Vertex(name = 'V_99',
              particles = [ P.d__tilde__, P.d, P.ta__plus__, P.ta__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFFF2 ],
              couplings = {(0,0):C.GC_5})

V_100 = Vertex(name = 'V_100',
               particles = [ P.s__tilde__, P.s, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_5})

V_101 = Vertex(name = 'V_101',
               particles = [ P.s__tilde__, P.s, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_5})

V_102 = Vertex(name = 'V_102',
               particles = [ P.s__tilde__, P.s, P.ta__plus__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_5})

V_103 = Vertex(name = 'V_103',
               particles = [ P.b__tilde__, P.b, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_5})

V_104 = Vertex(name = 'V_104',
               particles = [ P.b__tilde__, P.b, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_5})

V_105 = Vertex(name = 'V_105',
               particles = [ P.b__tilde__, P.b, P.ta__plus__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_5})

V_106 = Vertex(name = 'V_106',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_8})

V_107 = Vertex(name = 'V_107',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_9})

V_108 = Vertex(name = 'V_108',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_8})

V_109 = Vertex(name = 'V_109',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_9})

V_110 = Vertex(name = 'V_110',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_8})

V_111 = Vertex(name = 'V_111',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_9})

V_112 = Vertex(name = 'V_112',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_8})

V_113 = Vertex(name = 'V_113',
               particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_8})

V_114 = Vertex(name = 'V_114',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_8})

V_115 = Vertex(name = 'V_115',
               particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_8})

V_116 = Vertex(name = 'V_116',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_8})

V_117 = Vertex(name = 'V_117',
               particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF2 ],
               couplings = {(0,0):C.GC_8})

V_118 = Vertex(name = 'V_118',
               particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF1, L.FFFF2 ],
               couplings = {(1,0):C.GC_2,(0,1):C.GC_2})

V_119 = Vertex(name = 'V_119',
               particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF1, L.FFFF2 ],
               couplings = {(1,0):C.GC_4,(0,1):C.GC_4})

V_120 = Vertex(name = 'V_120',
               particles = [ P.c__tilde__, P.u, P.u__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF1, L.FFFF2 ],
               couplings = {(1,0):C.GC_3,(0,1):C.GC_1})

V_121 = Vertex(name = 'V_121',
               particles = [ P.c__tilde__, P.u, P.u__tilde__, P.c ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_4})

V_122 = Vertex(name = 'V_122',
               particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF1, L.FFFF2 ],
               couplings = {(1,0):C.GC_3,(0,1):C.GC_1})

V_123 = Vertex(name = 'V_123',
               particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_4})

V_124 = Vertex(name = 'V_124',
               particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF1, L.FFFF2 ],
               couplings = {(1,0):C.GC_2,(0,1):C.GC_2})

V_125 = Vertex(name = 'V_125',
               particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF1, L.FFFF2 ],
               couplings = {(1,0):C.GC_4,(0,1):C.GC_4})

V_126 = Vertex(name = 'V_126',
               particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF1, L.FFFF2 ],
               couplings = {(1,0):C.GC_3,(0,1):C.GC_1})

V_127 = Vertex(name = 'V_127',
               particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_4})

V_128 = Vertex(name = 'V_128',
               particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF1, L.FFFF2 ],
               couplings = {(1,0):C.GC_2,(0,1):C.GC_2})

V_129 = Vertex(name = 'V_129',
               particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF1, L.FFFF2 ],
               couplings = {(1,0):C.GC_4,(0,1):C.GC_4})

