# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Linux x86 (64-bit) (July 16, 2024)
# Date: Thu 26 Jun 2025 17:57:41


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
             lorentz = [ L.SSSS1, L.SSSS2 ],
             couplings = {(0,0):C.GC_61,(0,1):C.GC_12})

V_3 = Vertex(name = 'V_3',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_97})

V_4 = Vertex(name = 'V_4',
             particles = [ P.H, P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSSS1 ],
             couplings = {(0,0):C.GC_86})

V_5 = Vertex(name = 'V_5',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1, L.SSS2 ],
             couplings = {(0,0):C.GC_93,(0,1):C.GC_87})

V_6 = Vertex(name = 'V_6',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_101})

V_7 = Vertex(name = 'V_7',
             particles = [ P.ghG, P.ghG__tilde__, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_52})

V_8 = Vertex(name = 'V_8',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV1, L.VVV2 ],
             couplings = {(0,1):C.GC_10,(0,0):C.GC_52})

V_9 = Vertex(name = 'V_9',
             particles = [ P.g, P.g, P.g, P.g ],
             color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
             lorentz = [ L.VVVV1, L.VVVV2, L.VVVV4, L.VVVV5, L.VVVV7, L.VVVV8 ],
             couplings = {(0,1):C.GC_54,(1,5):C.GC_54,(2,4):C.GC_54,(1,2):C.GC_56,(0,0):C.GC_56,(2,3):C.GC_56})

V_10 = Vertex(name = 'V_10',
              particles = [ P.g, P.g, P.g, P.g, P.g ],
              color = [ 'f(-2,1,2)*f(-1,-2,3)*f(4,5,-1)', 'f(-2,1,2)*f(-1,-2,4)*f(3,5,-1)', 'f(-2,1,2)*f(-1,-2,5)*f(3,4,-1)', 'f(-2,1,3)*f(-1,-2,2)*f(4,5,-1)', 'f(-2,1,3)*f(-1,-2,4)*f(2,5,-1)', 'f(-2,1,3)*f(-1,-2,5)*f(2,4,-1)', 'f(-2,1,4)*f(-1,-2,2)*f(3,5,-1)', 'f(-2,1,4)*f(-1,-2,3)*f(2,5,-1)', 'f(-2,1,4)*f(-1,-2,5)*f(2,3,-1)', 'f(-2,1,5)*f(-1,-2,2)*f(3,4,-1)', 'f(-2,1,5)*f(-1,-2,3)*f(2,4,-1)', 'f(-2,1,5)*f(-1,-2,4)*f(2,3,-1)', 'f(-2,2,3)*f(-1,-2,1)*f(4,5,-1)', 'f(-2,2,3)*f(-1,-2,4)*f(1,5,-1)', 'f(-2,2,3)*f(-1,-2,5)*f(1,4,-1)', 'f(-2,2,4)*f(-1,-2,1)*f(3,5,-1)', 'f(-2,2,4)*f(-1,-2,3)*f(1,5,-1)', 'f(-2,2,4)*f(-1,-2,5)*f(1,3,-1)', 'f(-2,2,5)*f(-1,-2,1)*f(3,4,-1)', 'f(-2,2,5)*f(-1,-2,3)*f(1,4,-1)', 'f(-2,2,5)*f(-1,-2,4)*f(1,3,-1)', 'f(-2,3,4)*f(-1,-2,1)*f(2,5,-1)', 'f(-2,3,4)*f(-1,-2,2)*f(1,5,-1)', 'f(-2,3,4)*f(-1,-2,5)*f(1,2,-1)', 'f(-2,3,5)*f(-1,-2,1)*f(2,4,-1)', 'f(-2,3,5)*f(-1,-2,2)*f(1,4,-1)', 'f(-2,3,5)*f(-1,-2,4)*f(1,2,-1)', 'f(-2,4,5)*f(-1,-2,1)*f(2,3,-1)', 'f(-2,4,5)*f(-1,-2,2)*f(1,3,-1)', 'f(-2,4,5)*f(-1,-2,3)*f(1,2,-1)' ],
              lorentz = [ L.VVVVV1, L.VVVVV10, L.VVVVV11, L.VVVVV12, L.VVVVV13, L.VVVVV14, L.VVVVV15, L.VVVVV2, L.VVVVV3, L.VVVVV4, L.VVVVV5, L.VVVVV6, L.VVVVV7, L.VVVVV8, L.VVVVV9 ],
              couplings = {(24,9):C.GC_58,(21,10):C.GC_57,(18,10):C.GC_58,(15,9):C.GC_57,(28,7):C.GC_58,(22,14):C.GC_58,(9,14):C.GC_57,(3,7):C.GC_57,(29,8):C.GC_58,(16,1):C.GC_58,(10,1):C.GC_57,(0,8):C.GC_57,(26,4):C.GC_57,(20,3):C.GC_57,(4,3):C.GC_58,(1,4):C.GC_58,(25,13):C.GC_58,(6,13):C.GC_57,(19,2):C.GC_58,(7,2):C.GC_57,(23,6):C.GC_57,(17,5):C.GC_57,(5,5):C.GC_58,(2,6):C.GC_58,(27,0):C.GC_58,(12,0):C.GC_57,(13,11):C.GC_58,(11,11):C.GC_57,(14,12):C.GC_57,(8,12):C.GC_58})

V_11 = Vertex(name = 'V_11',
              particles = [ P.g, P.g, P.g, P.g, P.g, P.g ],
              color = [ 'f(-3,1,2)*f(-2,3,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,2)*f(-2,3,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,2)*f(-2,3,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,2)*f(-2,4,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,2)*f(-2,4,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,2)*f(-2,5,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,3)*f(-2,2,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,3)*f(-2,2,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,3)*f(-2,2,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,3)*f(-2,4,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,3)*f(-2,4,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,3)*f(-2,5,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,4)*f(-2,2,3)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,4)*f(-2,2,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,4)*f(-2,2,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,4)*f(-2,3,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,4)*f(-2,3,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,4)*f(-2,5,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,1,5)*f(-2,2,3)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,5)*f(-2,2,4)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,5)*f(-2,2,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,5)*f(-2,3,4)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,5)*f(-2,3,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,5)*f(-2,4,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,1,6)*f(-2,2,3)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,6)*f(-2,2,4)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,6)*f(-2,2,5)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,6)*f(-2,3,4)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,6)*f(-2,3,5)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,6)*f(-2,4,5)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,2,3)*f(-2,1,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,2,3)*f(-2,1,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,2,3)*f(-2,1,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,2,3)*f(-2,4,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,3)*f(-2,4,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,3)*f(-2,5,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,4)*f(-2,1,3)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,2,4)*f(-2,1,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,2,4)*f(-2,1,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,2,4)*f(-2,3,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,4)*f(-2,3,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,4)*f(-2,5,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,2,5)*f(-2,1,3)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,2,5)*f(-2,1,4)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,2,5)*f(-2,1,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,2,5)*f(-2,3,4)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,5)*f(-2,3,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,5)*f(-2,4,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,2,6)*f(-2,1,3)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,2,6)*f(-2,1,4)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,2,6)*f(-2,1,5)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,2,6)*f(-2,3,4)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,6)*f(-2,3,5)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,6)*f(-2,4,5)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,3,4)*f(-2,1,2)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,3,4)*f(-2,1,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,3,4)*f(-2,1,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,3,4)*f(-2,2,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,3,4)*f(-2,2,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,3,4)*f(-2,5,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,3,5)*f(-2,1,2)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,3,5)*f(-2,1,4)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,3,5)*f(-2,1,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,3,5)*f(-2,2,4)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,3,5)*f(-2,2,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,3,5)*f(-2,4,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,3,6)*f(-2,1,2)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,3,6)*f(-2,1,4)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,3,6)*f(-2,1,5)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,3,6)*f(-2,2,4)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,3,6)*f(-2,2,5)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,3,6)*f(-2,4,5)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,4,5)*f(-2,1,2)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,4,5)*f(-2,1,3)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,4,5)*f(-2,1,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,4,5)*f(-2,2,3)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,4,5)*f(-2,2,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,4,5)*f(-2,3,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,4,6)*f(-2,1,2)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,4,6)*f(-2,1,3)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,4,6)*f(-2,1,5)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,4,6)*f(-2,2,3)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,4,6)*f(-2,2,5)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,4,6)*f(-2,3,5)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,5,6)*f(-2,1,2)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,5,6)*f(-2,1,3)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,5,6)*f(-2,1,4)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,5,6)*f(-2,2,3)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,5,6)*f(-2,2,4)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,5,6)*f(-2,3,4)*f(-1,-2,-3)*f(1,2,-1)' ],
              lorentz = [ L.VVVVVV1, L.VVVVVV10, L.VVVVVV11, L.VVVVVV12, L.VVVVVV13, L.VVVVVV14, L.VVVVVV15, L.VVVVVV2, L.VVVVVV3, L.VVVVVV4, L.VVVVVV5, L.VVVVVV6, L.VVVVVV7, L.VVVVVV8, L.VVVVVV9 ],
              couplings = {(65,9):C.GC_60,(71,11):C.GC_59,(77,11):C.GC_60,(83,9):C.GC_59,(41,7):C.GC_60,(53,1):C.GC_60,(76,1):C.GC_59,(88,7):C.GC_59,(35,8):C.GC_60,(52,4):C.GC_60,(64,4):C.GC_59,(87,8):C.GC_59,(34,3):C.GC_59,(40,2):C.GC_59,(69,2):C.GC_60,(81,3):C.GC_60,(17,8):C.GC_59,(23,3):C.GC_60,(80,3):C.GC_59,(86,8):C.GC_60,(11,7):C.GC_59,(22,2):C.GC_60,(68,2):C.GC_59,(85,7):C.GC_60,(9,1):C.GC_59,(15,4):C.GC_59,(61,4):C.GC_60,(73,1):C.GC_60,(4,9):C.GC_59,(14,4):C.GC_60,(49,4):C.GC_59,(78,9):C.GC_60,(3,11):C.GC_60,(19,2):C.GC_59,(37,2):C.GC_60,(72,11):C.GC_59,(2,11):C.GC_59,(8,1):C.GC_60,(48,1):C.GC_59,(66,11):C.GC_60,(1,9):C.GC_60,(18,3):C.GC_59,(31,3):C.GC_60,(60,9):C.GC_59,(6,7):C.GC_60,(12,8):C.GC_60,(30,8):C.GC_59,(36,7):C.GC_59,(47,13):C.GC_60,(82,13):C.GC_59,(46,5):C.GC_60,(70,5):C.GC_59,(33,6):C.GC_59,(39,14):C.GC_59,(63,14):C.GC_60,(75,6):C.GC_60,(29,6):C.GC_60,(74,6):C.GC_59,(28,14):C.GC_60,(62,14):C.GC_59,(10,13):C.GC_59,(16,5):C.GC_59,(67,5):C.GC_60,(79,13):C.GC_60,(25,14):C.GC_59,(38,14):C.GC_60,(13,5):C.GC_60,(43,5):C.GC_59,(24,6):C.GC_59,(32,6):C.GC_60,(7,13):C.GC_60,(42,13):C.GC_59,(59,0):C.GC_60,(89,0):C.GC_59,(51,10):C.GC_60,(58,10):C.GC_59,(21,10):C.GC_59,(55,10):C.GC_60,(5,0):C.GC_59,(20,10):C.GC_60,(50,10):C.GC_59,(84,0):C.GC_60,(0,0):C.GC_60,(54,0):C.GC_59,(45,12):C.GC_59,(57,12):C.GC_60,(27,12):C.GC_60,(56,12):C.GC_59,(26,12):C.GC_59,(44,12):C.GC_60})

V_12 = Vertex(name = 'V_12',
              particles = [ P.t__tilde__, P.t, P.H, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSSS1 ],
              couplings = {(0,0):C.GC_37})

V_13 = Vertex(name = 'V_13',
              particles = [ P.t__tilde__, P.t, P.H, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSSS1 ],
              couplings = {(0,0):C.GC_38})

V_14 = Vertex(name = 'V_14',
              particles = [ P.t__tilde__, P.t, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_89})

V_15 = Vertex(name = 'V_15',
              particles = [ P.t__tilde__, P.t, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_90})

V_16 = Vertex(name = 'V_16',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2 ],
              couplings = {(0,0):C.GC_98,(0,1):C.GC_125})

V_17 = Vertex(name = 'V_17',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_99})

V_18 = Vertex(name = 'V_18',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_124})

V_19 = Vertex(name = 'V_19',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_126})

V_20 = Vertex(name = 'V_20',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_50})

V_21 = Vertex(name = 'V_21',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_62})

V_22 = Vertex(name = 'V_22',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_94})

V_23 = Vertex(name = 'V_23',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_51})

V_24 = Vertex(name = 'V_24',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_69})

V_25 = Vertex(name = 'V_25',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_63})

V_26 = Vertex(name = 'V_26',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV6 ],
              couplings = {(0,0):C.GC_70})

V_27 = Vertex(name = 'V_27',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_84})

V_28 = Vertex(name = 'V_28',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_122})

V_29 = Vertex(name = 'V_29',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_111})

V_30 = Vertex(name = 'V_30',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_123})

V_31 = Vertex(name = 'V_31',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_64})

V_32 = Vertex(name = 'V_32',
              particles = [ P.Z, P.Z, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSSSS1 ],
              couplings = {(0,0):C.GC_85})

V_33 = Vertex(name = 'V_33',
              particles = [ P.Z, P.Z, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSSS1 ],
              couplings = {(0,0):C.GC_112})

V_34 = Vertex(name = 'V_34',
              particles = [ P.e__plus__, P.e__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_49})

V_35 = Vertex(name = 'V_35',
              particles = [ P.mu__plus__, P.mu__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_49})

V_36 = Vertex(name = 'V_36',
              particles = [ P.ta__plus__, P.ta__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_49})

V_37 = Vertex(name = 'V_37',
              particles = [ P.u__tilde__, P.u, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_48})

V_38 = Vertex(name = 'V_38',
              particles = [ P.c__tilde__, P.c, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_48})

V_39 = Vertex(name = 'V_39',
              particles = [ P.t__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1, L.FFV7 ],
              couplings = {(0,0):C.GC_48,(0,1):C.GC_91})

V_40 = Vertex(name = 'V_40',
              particles = [ P.d__tilde__, P.d, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_47})

V_41 = Vertex(name = 'V_41',
              particles = [ P.s__tilde__, P.s, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_47})

V_42 = Vertex(name = 'V_42',
              particles = [ P.b__tilde__, P.b, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_47})

V_43 = Vertex(name = 'V_43',
              particles = [ P.u__tilde__, P.u, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_53})

V_44 = Vertex(name = 'V_44',
              particles = [ P.c__tilde__, P.c, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_53})

V_45 = Vertex(name = 'V_45',
              particles = [ P.t__tilde__, P.t, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1, L.FFV7 ],
              couplings = {(0,0):C.GC_53,(0,1):C.GC_88})

V_46 = Vertex(name = 'V_46',
              particles = [ P.d__tilde__, P.d, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_53})

V_47 = Vertex(name = 'V_47',
              particles = [ P.s__tilde__, P.s, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_53})

V_48 = Vertex(name = 'V_48',
              particles = [ P.b__tilde__, P.b, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_53})

V_49 = Vertex(name = 'V_49',
              particles = [ P.d__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_65})

V_50 = Vertex(name = 'V_50',
              particles = [ P.s__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_65})

V_51 = Vertex(name = 'V_51',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_65})

V_52 = Vertex(name = 'V_52',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_100})

V_53 = Vertex(name = 'V_53',
              particles = [ P.u__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_65})

V_54 = Vertex(name = 'V_54',
              particles = [ P.c__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_65})

V_55 = Vertex(name = 'V_55',
              particles = [ P.t__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_65})

V_56 = Vertex(name = 'V_56',
              particles = [ P.t__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_100})

V_57 = Vertex(name = 'V_57',
              particles = [ P.e__plus__, P.ve, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_65})

V_58 = Vertex(name = 'V_58',
              particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_65})

V_59 = Vertex(name = 'V_59',
              particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_65})

V_60 = Vertex(name = 'V_60',
              particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_65})

V_61 = Vertex(name = 'V_61',
              particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_65})

V_62 = Vertex(name = 'V_62',
              particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_65})

V_63 = Vertex(name = 'V_63',
              particles = [ P.u__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3, L.FFV6 ],
              couplings = {(0,0):C.GC_68,(0,2):C.GC_72,(0,1):C.GC_120})

V_64 = Vertex(name = 'V_64',
              particles = [ P.u__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_116})

V_65 = Vertex(name = 'V_65',
              particles = [ P.c__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3, L.FFV6 ],
              couplings = {(0,0):C.GC_68,(0,2):C.GC_72,(0,1):C.GC_120})

V_66 = Vertex(name = 'V_66',
              particles = [ P.c__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_116})

V_67 = Vertex(name = 'V_67',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3, L.FFV6, L.FFV8 ],
              couplings = {(0,0):C.GC_68,(0,2):C.GC_72,(0,1):C.GC_120,(0,3):C.GC_96})

V_68 = Vertex(name = 'V_68',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_116,(0,1):C.GC_121})

V_69 = Vertex(name = 'V_69',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_117})

V_70 = Vertex(name = 'V_70',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_119})

V_71 = Vertex(name = 'V_71',
              particles = [ P.d__tilde__, P.d, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_67,(0,2):C.GC_72,(0,1):C.GC_113})

V_72 = Vertex(name = 'V_72',
              particles = [ P.d__tilde__, P.d, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_116})

V_73 = Vertex(name = 'V_73',
              particles = [ P.s__tilde__, P.s, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_67,(0,2):C.GC_72,(0,1):C.GC_113})

V_74 = Vertex(name = 'V_74',
              particles = [ P.s__tilde__, P.s, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_116})

V_75 = Vertex(name = 'V_75',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3, L.FFV4 ],
              couplings = {(0,0):C.GC_67,(0,2):C.GC_72,(0,1):C.GC_113})

V_76 = Vertex(name = 'V_76',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_116})

V_77 = Vertex(name = 'V_77',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_117})

V_78 = Vertex(name = 'V_78',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_118})

V_79 = Vertex(name = 'V_79',
              particles = [ P.ve__tilde__, P.ve, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_74})

V_80 = Vertex(name = 'V_80',
              particles = [ P.ve__tilde__, P.ve, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_115})

V_81 = Vertex(name = 'V_81',
              particles = [ P.vm__tilde__, P.vm, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_74})

V_82 = Vertex(name = 'V_82',
              particles = [ P.vm__tilde__, P.vm, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_115})

V_83 = Vertex(name = 'V_83',
              particles = [ P.vt__tilde__, P.vt, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_74})

V_84 = Vertex(name = 'V_84',
              particles = [ P.vt__tilde__, P.vt, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_115})

V_85 = Vertex(name = 'V_85',
              particles = [ P.e__plus__, P.e__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV3, L.FFV5 ],
              couplings = {(0,0):C.GC_67,(0,2):C.GC_73,(0,1):C.GC_114})

V_86 = Vertex(name = 'V_86',
              particles = [ P.e__plus__, P.e__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_115})

V_87 = Vertex(name = 'V_87',
              particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV3, L.FFV5 ],
              couplings = {(0,0):C.GC_67,(0,2):C.GC_73,(0,1):C.GC_114})

V_88 = Vertex(name = 'V_88',
              particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_115})

V_89 = Vertex(name = 'V_89',
              particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV3, L.FFV5 ],
              couplings = {(0,0):C.GC_67,(0,2):C.GC_73,(0,1):C.GC_114})

V_90 = Vertex(name = 'V_90',
              particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_115})

V_91 = Vertex(name = 'V_91',
              particles = [ P.b__tilde__, P.t, P.W__minus__, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVSS1 ],
              couplings = {(0,0):C.GC_66})

V_92 = Vertex(name = 'V_92',
              particles = [ P.b__tilde__, P.t, P.W__minus__, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1 ],
              couplings = {(0,0):C.GC_95})

V_93 = Vertex(name = 'V_93',
              particles = [ P.t__tilde__, P.b, P.W__plus__, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVSS1 ],
              couplings = {(0,0):C.GC_66})

V_94 = Vertex(name = 'V_94',
              particles = [ P.t__tilde__, P.b, P.W__plus__, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVS1 ],
              couplings = {(0,0):C.GC_95})

V_95 = Vertex(name = 'V_95',
              particles = [ P.d__tilde__, P.d, P.Z, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,0):C.GC_78,(0,1):C.GC_75})

V_96 = Vertex(name = 'V_96',
              particles = [ P.s__tilde__, P.s, P.Z, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,0):C.GC_78,(0,1):C.GC_75})

V_97 = Vertex(name = 'V_97',
              particles = [ P.b__tilde__, P.b, P.Z, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVSS1, L.FFVSS2 ],
              couplings = {(0,0):C.GC_78,(0,1):C.GC_75})

V_98 = Vertex(name = 'V_98',
              particles = [ P.b__tilde__, P.b, P.Z, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVSS1 ],
              couplings = {(0,0):C.GC_79})

V_99 = Vertex(name = 'V_99',
              particles = [ P.b__tilde__, P.b, P.Z, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFVSS1 ],
              couplings = {(0,0):C.GC_80})

V_100 = Vertex(name = 'V_100',
               particles = [ P.d__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,0):C.GC_105,(0,1):C.GC_102})

V_101 = Vertex(name = 'V_101',
               particles = [ P.s__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,0):C.GC_105,(0,1):C.GC_102})

V_102 = Vertex(name = 'V_102',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,0):C.GC_105,(0,1):C.GC_102})

V_103 = Vertex(name = 'V_103',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_106})

V_104 = Vertex(name = 'V_104',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_107})

V_105 = Vertex(name = 'V_105',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_77,(0,1):C.GC_76})

V_106 = Vertex(name = 'V_106',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_77,(0,1):C.GC_76})

V_107 = Vertex(name = 'V_107',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_77,(0,1):C.GC_76})

V_108 = Vertex(name = 'V_108',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,0):C.GC_104,(0,1):C.GC_103})

V_109 = Vertex(name = 'V_109',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,0):C.GC_104,(0,1):C.GC_103})

V_110 = Vertex(name = 'V_110',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,0):C.GC_104,(0,1):C.GC_103})

V_111 = Vertex(name = 'V_111',
               particles = [ P.t__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_78,(0,1):C.GC_82})

V_112 = Vertex(name = 'V_112',
               particles = [ P.t__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_79,(0,1):C.GC_83})

V_113 = Vertex(name = 'V_113',
               particles = [ P.t__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_81})

V_114 = Vertex(name = 'V_114',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4 ],
               couplings = {(0,0):C.GC_105,(0,1):C.GC_109,(0,2):C.GC_71})

V_115 = Vertex(name = 'V_115',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,0):C.GC_106,(0,1):C.GC_110})

V_116 = Vertex(name = 'V_116',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_108})

V_117 = Vertex(name = 'V_117',
               particles = [ P.u__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_78,(0,1):C.GC_82})

V_118 = Vertex(name = 'V_118',
               particles = [ P.c__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_78,(0,1):C.GC_82})

V_119 = Vertex(name = 'V_119',
               particles = [ P.u__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,0):C.GC_105,(0,1):C.GC_109})

V_120 = Vertex(name = 'V_120',
               particles = [ P.c__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,0):C.GC_105,(0,1):C.GC_109})

V_121 = Vertex(name = 'V_121',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_77})

V_122 = Vertex(name = 'V_122',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_77})

V_123 = Vertex(name = 'V_123',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_77})

V_124 = Vertex(name = 'V_124',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_104})

V_125 = Vertex(name = 'V_125',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_104})

V_126 = Vertex(name = 'V_126',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_104})

V_127 = Vertex(name = 'V_127',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(1,0):C.GC_24,(0,2):C.GC_24,(0,3):C.GC_19,(2,3):C.GC_20,(1,6):C.GC_19,(3,6):C.GC_20,(1,4):C.GC_19,(3,4):C.GC_20,(1,5):C.GC_2,(0,7):C.GC_19,(2,7):C.GC_20,(0,1):C.GC_2})

V_128 = Vertex(name = 'V_128',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF3, L.FFFF7 ],
               couplings = {(1,0):C.GC_26,(0,2):C.GC_26,(1,3):C.GC_4,(0,1):C.GC_4})

V_129 = Vertex(name = 'V_129',
               particles = [ P.s__tilde__, P.d, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF3, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(1,0):C.GC_23,(0,2):C.GC_22,(1,5):C.GC_19,(2,5):C.GC_20,(1,3):C.GC_19,(2,3):C.GC_20,(1,4):C.GC_3,(0,1):C.GC_1})

V_130 = Vertex(name = 'V_130',
               particles = [ P.s__tilde__, P.d, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF7 ],
               couplings = {(0,0):C.GC_26,(1,1):C.GC_4})

V_131 = Vertex(name = 'V_131',
               particles = [ P.b__tilde__, P.d, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF3, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(1,0):C.GC_23,(0,2):C.GC_22,(1,5):C.GC_19,(2,5):C.GC_20,(1,3):C.GC_19,(2,3):C.GC_20,(1,4):C.GC_3,(0,1):C.GC_1})

V_132 = Vertex(name = 'V_132',
               particles = [ P.b__tilde__, P.d, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF7 ],
               couplings = {(0,0):C.GC_26,(1,1):C.GC_4})

V_133 = Vertex(name = 'V_133',
               particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(1,0):C.GC_23,(0,3):C.GC_24,(1,2):C.GC_22,(0,4):C.GC_19,(2,4):C.GC_20,(1,7):C.GC_19,(3,7):C.GC_20,(1,5):C.GC_19,(3,5):C.GC_20,(1,6):C.GC_2,(0,8):C.GC_19,(2,8):C.GC_20,(0,1):C.GC_2})

V_134 = Vertex(name = 'V_134',
               particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF3, L.FFFF7 ],
               couplings = {(1,0):C.GC_26,(0,2):C.GC_26,(1,3):C.GC_4,(0,1):C.GC_4})

V_135 = Vertex(name = 'V_135',
               particles = [ P.b__tilde__, P.s, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF3, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(1,0):C.GC_23,(0,2):C.GC_22,(1,5):C.GC_19,(2,5):C.GC_20,(1,3):C.GC_19,(2,3):C.GC_20,(1,4):C.GC_3,(0,1):C.GC_1})

V_136 = Vertex(name = 'V_136',
               particles = [ P.b__tilde__, P.s, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF7 ],
               couplings = {(0,0):C.GC_26,(1,1):C.GC_4})

V_137 = Vertex(name = 'V_137',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(1,0):C.GC_24,(0,2):C.GC_24,(0,3):C.GC_19,(2,3):C.GC_20,(1,6):C.GC_19,(3,6):C.GC_20,(1,4):C.GC_19,(3,4):C.GC_20,(1,5):C.GC_2,(0,7):C.GC_19,(2,7):C.GC_20,(0,1):C.GC_2})

V_138 = Vertex(name = 'V_138',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF3, L.FFFF7 ],
               couplings = {(1,0):C.GC_26,(0,2):C.GC_26,(1,3):C.GC_4,(0,1):C.GC_4})

V_139 = Vertex(name = 'V_139',
               particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,0):C.GC_15,(0,2):C.GC_15,(0,3):C.GC_14,(0,6):C.GC_14,(0,4):C.GC_14,(0,5):C.GC_7,(0,7):C.GC_14,(0,1):C.GC_7})

V_140 = Vertex(name = 'V_140',
               particles = [ P.e__plus__, P.e__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF9 ],
               couplings = {(0,1):C.GC_15,(0,2):C.GC_14,(0,3):C.GC_6,(0,4):C.GC_14,(0,0):C.GC_6})

V_141 = Vertex(name = 'V_141',
               particles = [ P.e__plus__, P.e__minus__, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF9 ],
               couplings = {(0,1):C.GC_15,(0,2):C.GC_14,(0,3):C.GC_6,(0,4):C.GC_14,(0,0):C.GC_6})

V_142 = Vertex(name = 'V_142',
               particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,0):C.GC_15,(0,2):C.GC_15,(0,3):C.GC_14,(0,6):C.GC_14,(0,4):C.GC_14,(0,5):C.GC_7,(0,7):C.GC_14,(0,1):C.GC_7})

V_143 = Vertex(name = 'V_143',
               particles = [ P.mu__plus__, P.mu__minus__, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF7, L.FFFF9 ],
               couplings = {(0,1):C.GC_15,(0,2):C.GC_14,(0,3):C.GC_6,(0,4):C.GC_14,(0,0):C.GC_6})

V_144 = Vertex(name = 'V_144',
               particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(0,0):C.GC_15,(0,2):C.GC_15,(0,3):C.GC_14,(0,6):C.GC_14,(0,4):C.GC_14,(0,5):C.GC_7,(0,7):C.GC_14,(0,1):C.GC_7})

V_145 = Vertex(name = 'V_145',
               particles = [ P.d__tilde__, P.d, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_16,(0,2):C.GC_13,(0,3):C.GC_21,(0,0):C.GC_5})

V_146 = Vertex(name = 'V_146',
               particles = [ P.d__tilde__, P.d, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_16,(0,2):C.GC_13,(0,3):C.GC_21,(0,0):C.GC_5})

V_147 = Vertex(name = 'V_147',
               particles = [ P.d__tilde__, P.d, P.ta__plus__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_16,(0,2):C.GC_13,(0,3):C.GC_21,(0,0):C.GC_5})

V_148 = Vertex(name = 'V_148',
               particles = [ P.s__tilde__, P.s, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_16,(0,2):C.GC_13,(0,3):C.GC_21,(0,0):C.GC_5})

V_149 = Vertex(name = 'V_149',
               particles = [ P.s__tilde__, P.s, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_16,(0,2):C.GC_13,(0,3):C.GC_21,(0,0):C.GC_5})

V_150 = Vertex(name = 'V_150',
               particles = [ P.s__tilde__, P.s, P.ta__plus__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_16,(0,2):C.GC_13,(0,3):C.GC_21,(0,0):C.GC_5})

V_151 = Vertex(name = 'V_151',
               particles = [ P.b__tilde__, P.b, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_16,(0,2):C.GC_13,(0,3):C.GC_21,(0,0):C.GC_5})

V_152 = Vertex(name = 'V_152',
               particles = [ P.b__tilde__, P.b, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_16,(0,2):C.GC_13,(0,3):C.GC_21,(0,0):C.GC_5})

V_153 = Vertex(name = 'V_153',
               particles = [ P.b__tilde__, P.b, P.ta__plus__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_16,(0,2):C.GC_13,(0,3):C.GC_21,(0,0):C.GC_5})

V_154 = Vertex(name = 'V_154',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF3, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(1,0):C.GC_24,(0,1):C.GC_27,(1,4):C.GC_19,(2,4):C.GC_20,(1,2):C.GC_28,(2,2):C.GC_30,(1,3):C.GC_32,(2,3):C.GC_34})

V_155 = Vertex(name = 'V_155',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_156 = Vertex(name = 'V_156',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF3, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(1,0):C.GC_23,(0,1):C.GC_27,(1,4):C.GC_19,(2,4):C.GC_20,(1,2):C.GC_28,(2,2):C.GC_30,(1,3):C.GC_32,(2,3):C.GC_34})

V_157 = Vertex(name = 'V_157',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF3, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(1,0):C.GC_23,(0,1):C.GC_27,(1,4):C.GC_19,(2,4):C.GC_20,(1,2):C.GC_28,(2,2):C.GC_30,(1,3):C.GC_32,(2,3):C.GC_34})

V_158 = Vertex(name = 'V_158',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF5, L.FFFF7 ],
               couplings = {(0,0):C.GC_29,(1,0):C.GC_31,(0,1):C.GC_33,(1,1):C.GC_35})

V_159 = Vertex(name = 'V_159',
               particles = [ P.s__tilde__, P.d, P.u__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)' ],
               lorentz = [ L.FFFF3 ],
               couplings = {(0,0):C.GC_22})

V_160 = Vertex(name = 'V_160',
               particles = [ P.s__tilde__, P.d, P.u__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)' ],
               lorentz = [ L.FFFF3 ],
               couplings = {(0,0):C.GC_25})

V_161 = Vertex(name = 'V_161',
               particles = [ P.b__tilde__, P.d, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)' ],
               lorentz = [ L.FFFF3 ],
               couplings = {(0,0):C.GC_22})

V_162 = Vertex(name = 'V_162',
               particles = [ P.b__tilde__, P.d, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)' ],
               lorentz = [ L.FFFF3 ],
               couplings = {(0,0):C.GC_25})

V_163 = Vertex(name = 'V_163',
               particles = [ P.d__tilde__, P.s, P.c__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)' ],
               lorentz = [ L.FFFF3 ],
               couplings = {(0,0):C.GC_22})

V_164 = Vertex(name = 'V_164',
               particles = [ P.d__tilde__, P.s, P.c__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)' ],
               lorentz = [ L.FFFF3 ],
               couplings = {(0,0):C.GC_25})

V_165 = Vertex(name = 'V_165',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF3, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(1,0):C.GC_23,(0,1):C.GC_27,(1,4):C.GC_19,(2,4):C.GC_20,(1,2):C.GC_28,(2,2):C.GC_30,(1,3):C.GC_32,(2,3):C.GC_34})

V_166 = Vertex(name = 'V_166',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF3, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(1,0):C.GC_24,(0,1):C.GC_27,(1,4):C.GC_19,(2,4):C.GC_20,(1,2):C.GC_28,(2,2):C.GC_30,(1,3):C.GC_32,(2,3):C.GC_34})

V_167 = Vertex(name = 'V_167',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF1 ],
               couplings = {(0,0):C.GC_25})

V_168 = Vertex(name = 'V_168',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF3, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(1,0):C.GC_23,(0,1):C.GC_27,(1,4):C.GC_19,(2,4):C.GC_20,(1,2):C.GC_28,(2,2):C.GC_30,(1,3):C.GC_32,(2,3):C.GC_34})

V_169 = Vertex(name = 'V_169',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF5, L.FFFF7 ],
               couplings = {(0,0):C.GC_29,(1,0):C.GC_31,(0,1):C.GC_33,(1,1):C.GC_35})

V_170 = Vertex(name = 'V_170',
               particles = [ P.b__tilde__, P.s, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)' ],
               lorentz = [ L.FFFF3 ],
               couplings = {(0,0):C.GC_22})

V_171 = Vertex(name = 'V_171',
               particles = [ P.b__tilde__, P.s, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)' ],
               lorentz = [ L.FFFF3 ],
               couplings = {(0,0):C.GC_25})

V_172 = Vertex(name = 'V_172',
               particles = [ P.d__tilde__, P.b, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)' ],
               lorentz = [ L.FFFF3 ],
               couplings = {(0,0):C.GC_22})

V_173 = Vertex(name = 'V_173',
               particles = [ P.d__tilde__, P.b, P.t__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)' ],
               lorentz = [ L.FFFF3 ],
               couplings = {(0,0):C.GC_25})

V_174 = Vertex(name = 'V_174',
               particles = [ P.s__tilde__, P.b, P.t__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)' ],
               lorentz = [ L.FFFF3 ],
               couplings = {(0,0):C.GC_22})

V_175 = Vertex(name = 'V_175',
               particles = [ P.s__tilde__, P.b, P.t__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)' ],
               lorentz = [ L.FFFF3 ],
               couplings = {(0,0):C.GC_25})

V_176 = Vertex(name = 'V_176',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF3, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(1,0):C.GC_23,(0,1):C.GC_27,(1,4):C.GC_19,(2,4):C.GC_20,(1,2):C.GC_28,(2,2):C.GC_30,(1,3):C.GC_32,(2,3):C.GC_34})

V_177 = Vertex(name = 'V_177',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF3, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(1,0):C.GC_23,(0,1):C.GC_27,(1,4):C.GC_19,(2,4):C.GC_20,(1,2):C.GC_28,(2,2):C.GC_30,(1,3):C.GC_32,(2,3):C.GC_34})

V_178 = Vertex(name = 'V_178',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF3, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(1,0):C.GC_24,(0,1):C.GC_27,(1,4):C.GC_19,(2,4):C.GC_20,(1,2):C.GC_28,(2,2):C.GC_30,(1,3):C.GC_32,(2,3):C.GC_34})

V_179 = Vertex(name = 'V_179',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF5, L.FFFF7 ],
               couplings = {(0,0):C.GC_25,(0,1):C.GC_29,(1,1):C.GC_31,(0,2):C.GC_33,(1,2):C.GC_35})

V_180 = Vertex(name = 'V_180',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_16,(0,2):C.GC_21,(0,3):C.GC_17,(0,0):C.GC_8})

V_181 = Vertex(name = 'V_181',
               particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF3, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_21,(0,3):C.GC_17,(0,2):C.GC_8})

V_182 = Vertex(name = 'V_182',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_16,(0,2):C.GC_21,(0,3):C.GC_17,(0,0):C.GC_8})

V_183 = Vertex(name = 'V_183',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF9 ],
               couplings = {(0,1):C.GC_18,(0,0):C.GC_9})

V_184 = Vertex(name = 'V_184',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_16,(0,2):C.GC_21,(0,3):C.GC_17,(0,0):C.GC_8})

V_185 = Vertex(name = 'V_185',
               particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_16,(0,2):C.GC_21,(0,3):C.GC_17,(0,0):C.GC_8})

V_186 = Vertex(name = 'V_186',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_16,(0,2):C.GC_21,(0,3):C.GC_17,(0,0):C.GC_8})

V_187 = Vertex(name = 'V_187',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF9 ],
               couplings = {(0,1):C.GC_18,(0,0):C.GC_9})

V_188 = Vertex(name = 'V_188',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_16,(0,2):C.GC_21,(0,3):C.GC_17,(0,0):C.GC_8})

V_189 = Vertex(name = 'V_189',
               particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_16,(0,2):C.GC_21,(0,3):C.GC_17,(0,0):C.GC_8})

V_190 = Vertex(name = 'V_190',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_16,(0,2):C.GC_21,(0,3):C.GC_17,(0,0):C.GC_8})

V_191 = Vertex(name = 'V_191',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF9 ],
               couplings = {(0,1):C.GC_18,(0,0):C.GC_9})

V_192 = Vertex(name = 'V_192',
               particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(1,0):C.GC_24,(0,2):C.GC_24,(0,3):C.GC_28,(2,3):C.GC_30,(1,6):C.GC_28,(3,6):C.GC_30,(1,4):C.GC_28,(3,4):C.GC_30,(1,5):C.GC_41,(0,7):C.GC_28,(2,7):C.GC_30,(0,1):C.GC_41})

V_193 = Vertex(name = 'V_193',
               particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF3, L.FFFF7 ],
               couplings = {(1,0):C.GC_26,(0,2):C.GC_26,(1,3):C.GC_40,(0,1):C.GC_40})

V_194 = Vertex(name = 'V_194',
               particles = [ P.c__tilde__, P.u, P.u__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF3, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(1,0):C.GC_23,(0,2):C.GC_22,(1,5):C.GC_28,(2,5):C.GC_30,(1,3):C.GC_28,(2,3):C.GC_30,(1,4):C.GC_40,(0,1):C.GC_39})

V_195 = Vertex(name = 'V_195',
               particles = [ P.c__tilde__, P.u, P.u__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF7 ],
               couplings = {(0,0):C.GC_26,(1,1):C.GC_42})

V_196 = Vertex(name = 'V_196',
               particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF3, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(1,0):C.GC_23,(0,2):C.GC_22,(1,5):C.GC_28,(2,5):C.GC_30,(1,3):C.GC_28,(2,3):C.GC_30,(1,4):C.GC_40,(0,1):C.GC_39})

V_197 = Vertex(name = 'V_197',
               particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_26,(1,2):C.GC_29,(2,2):C.GC_31,(1,3):C.GC_42,(0,0):C.GC_45})

V_198 = Vertex(name = 'V_198',
               particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_43})

V_199 = Vertex(name = 'V_199',
               particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_44})

V_200 = Vertex(name = 'V_200',
               particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(1,0):C.GC_24,(0,2):C.GC_24,(0,3):C.GC_28,(2,3):C.GC_30,(1,6):C.GC_28,(3,6):C.GC_30,(1,4):C.GC_28,(3,4):C.GC_30,(1,5):C.GC_41,(0,7):C.GC_28,(2,7):C.GC_30,(0,1):C.GC_41})

V_201 = Vertex(name = 'V_201',
               particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF3, L.FFFF7 ],
               couplings = {(1,0):C.GC_26,(0,2):C.GC_26,(1,3):C.GC_40,(0,1):C.GC_40})

V_202 = Vertex(name = 'V_202',
               particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF3, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(1,0):C.GC_23,(0,2):C.GC_22,(1,5):C.GC_28,(2,5):C.GC_30,(1,3):C.GC_28,(2,3):C.GC_30,(1,4):C.GC_40,(0,1):C.GC_39})

V_203 = Vertex(name = 'V_203',
               particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF3, L.FFFF5, L.FFFF7 ],
               couplings = {(0,1):C.GC_26,(1,2):C.GC_29,(2,2):C.GC_31,(1,3):C.GC_42,(0,0):C.GC_45})

V_204 = Vertex(name = 'V_204',
               particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_43})

V_205 = Vertex(name = 'V_205',
               particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_44})

V_206 = Vertex(name = 'V_206',
               particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF3, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8, L.FFFF9 ],
               couplings = {(1,0):C.GC_24,(0,2):C.GC_24,(0,3):C.GC_28,(2,3):C.GC_30,(1,6):C.GC_28,(3,6):C.GC_30,(1,4):C.GC_28,(3,4):C.GC_30,(1,5):C.GC_41,(0,7):C.GC_28,(2,7):C.GC_30,(0,1):C.GC_41})

V_207 = Vertex(name = 'V_207',
               particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF3, L.FFFF7, L.FFFF8 ],
               couplings = {(1,0):C.GC_26,(0,2):C.GC_26,(1,4):C.GC_29,(2,4):C.GC_31,(1,3):C.GC_40,(0,1):C.GC_40})

V_208 = Vertex(name = 'V_208',
               particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF10, L.FFFF7 ],
               couplings = {(1,1):C.GC_43,(0,0):C.GC_45})

V_209 = Vertex(name = 'V_209',
               particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
               color = [ 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF7 ],
               couplings = {(0,0):C.GC_44})

V_210 = Vertex(name = 'V_210',
               particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_15,(0,1):C.GC_14})

V_211 = Vertex(name = 'V_211',
               particles = [ P.e__plus__, P.e__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_15,(0,1):C.GC_14})

V_212 = Vertex(name = 'V_212',
               particles = [ P.e__plus__, P.e__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_15,(0,1):C.GC_14})

V_213 = Vertex(name = 'V_213',
               particles = [ P.mu__plus__, P.mu__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_15,(0,1):C.GC_14})

V_214 = Vertex(name = 'V_214',
               particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_15,(0,1):C.GC_14})

V_215 = Vertex(name = 'V_215',
               particles = [ P.mu__plus__, P.mu__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_15,(0,1):C.GC_14})

V_216 = Vertex(name = 'V_216',
               particles = [ P.ta__plus__, P.ta__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_15,(0,1):C.GC_14})

V_217 = Vertex(name = 'V_217',
               particles = [ P.ta__plus__, P.ta__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_15,(0,1):C.GC_14})

V_218 = Vertex(name = 'V_218',
               particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_15,(0,1):C.GC_14})

V_219 = Vertex(name = 'V_219',
               particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_17})

V_220 = Vertex(name = 'V_220',
               particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_17})

V_221 = Vertex(name = 'V_221',
               particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_17})

V_222 = Vertex(name = 'V_222',
               particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_17})

V_223 = Vertex(name = 'V_223',
               particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_17})

V_224 = Vertex(name = 'V_224',
               particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_17})

V_225 = Vertex(name = 'V_225',
               particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_17})

V_226 = Vertex(name = 'V_226',
               particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_18})

V_227 = Vertex(name = 'V_227',
               particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_17})

V_228 = Vertex(name = 'V_228',
               particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_18})

V_229 = Vertex(name = 'V_229',
               particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_17})

V_230 = Vertex(name = 'V_230',
               particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_18})

V_231 = Vertex(name = 'V_231',
               particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF1, L.FFFF3 ],
               couplings = {(0,0):C.GC_15,(0,1):C.GC_15})

V_232 = Vertex(name = 'V_232',
               particles = [ P.ve__tilde__, P.ve, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF3 ],
               couplings = {(0,0):C.GC_15})

V_233 = Vertex(name = 'V_233',
               particles = [ P.ve__tilde__, P.ve, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF3 ],
               couplings = {(0,0):C.GC_15})

V_234 = Vertex(name = 'V_234',
               particles = [ P.vm__tilde__, P.vm, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF1, L.FFFF3 ],
               couplings = {(0,0):C.GC_15,(0,1):C.GC_15})

V_235 = Vertex(name = 'V_235',
               particles = [ P.vm__tilde__, P.vm, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF3 ],
               couplings = {(0,0):C.GC_15})

V_236 = Vertex(name = 'V_236',
               particles = [ P.vt__tilde__, P.vt, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF1, L.FFFF3 ],
               couplings = {(0,0):C.GC_15,(0,1):C.GC_15})

V_237 = Vertex(name = 'V_237',
               particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_13})

V_238 = Vertex(name = 'V_238',
               particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_13})

V_239 = Vertex(name = 'V_239',
               particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_13})

V_240 = Vertex(name = 'V_240',
               particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_13})

V_241 = Vertex(name = 'V_241',
               particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_13})

V_242 = Vertex(name = 'V_242',
               particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_13})

V_243 = Vertex(name = 'V_243',
               particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_13})

V_244 = Vertex(name = 'V_244',
               particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_13})

V_245 = Vertex(name = 'V_245',
               particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_13})

V_246 = Vertex(name = 'V_246',
               particles = [ P.t__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3 ],
               couplings = {(0,0):C.GC_46})

V_247 = Vertex(name = 'V_247',
               particles = [ P.t__tilde__, P.t, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS3 ],
               couplings = {(0,0):C.GC_36})

V_248 = Vertex(name = 'V_248',
               particles = [ P.t__tilde__, P.t, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1 ],
               couplings = {(0,0):C.GC_55})

V_249 = Vertex(name = 'V_249',
               particles = [ P.t__tilde__, P.t, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1 ],
               couplings = {(0,0):C.GC_92})

