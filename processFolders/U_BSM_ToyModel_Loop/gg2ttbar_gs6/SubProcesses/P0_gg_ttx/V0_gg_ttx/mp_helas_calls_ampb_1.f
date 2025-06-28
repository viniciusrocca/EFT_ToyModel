      SUBROUTINE MP_HELAS_CALLS_AMPB_1(P,NHEL,H,IC)
C     
      USE POLYNOMIAL_CONSTANTS
      IMPLICIT NONE
C     
C     CONSTANTS
C     
      INTEGER    NEXTERNAL
      PARAMETER (NEXTERNAL=4)
      INTEGER    NCOMB
      PARAMETER (NCOMB=16)

      INTEGER NBORNAMPS
      PARAMETER (NBORNAMPS=3)
      INTEGER    NLOOPS, NLOOPGROUPS, NCTAMPS
      PARAMETER (NLOOPS=56, NLOOPGROUPS=37, NCTAMPS=124)
      INTEGER    NLOOPAMPS
      PARAMETER (NLOOPAMPS=180)
      INTEGER    NWAVEFUNCS,NLOOPWAVEFUNCS
      PARAMETER (NWAVEFUNCS=10,NLOOPWAVEFUNCS=122)
      REAL*16     ZERO
      PARAMETER (ZERO=0.0E0_16)
      COMPLEX*32     IZERO
      PARAMETER (IZERO=CMPLX(0.0E0_16,0.0E0_16,KIND=16))
C     These are constants related to the split orders
      INTEGER    NSO, NSQUAREDSO, NAMPSO
      PARAMETER (NSO=5, NSQUAREDSO=2, NAMPSO=3)
C     
C     ARGUMENTS
C     
      REAL*16 P(0:3,NEXTERNAL)
      INTEGER NHEL(NEXTERNAL), IC(NEXTERNAL)
      INTEGER H
C     
C     LOCAL VARIABLES
C     
      INTEGER I,J,K
      COMPLEX*32 COEFS(MAXLWFSIZE,0:VERTEXMAXCOEFS-1,MAXLWFSIZE)
C     
C     GLOBAL VARIABLES
C     

      INCLUDE 'mp_coupl_same_name.inc'

      INTEGER GOODHEL(NCOMB)
      LOGICAL GOODAMP(NSQUAREDSO,NLOOPGROUPS)
      COMMON/FILTERS/GOODAMP,GOODHEL

      INTEGER SQSO_TARGET
      COMMON/SOCHOICE/SQSO_TARGET

      LOGICAL UVCT_REQ_SO_DONE,MP_UVCT_REQ_SO_DONE,CT_REQ_SO_DONE
     $ ,MP_CT_REQ_SO_DONE,LOOP_REQ_SO_DONE,MP_LOOP_REQ_SO_DONE
     $ ,CTCALL_REQ_SO_DONE,FILTER_SO
      COMMON/SO_REQS/UVCT_REQ_SO_DONE,MP_UVCT_REQ_SO_DONE
     $ ,CT_REQ_SO_DONE,MP_CT_REQ_SO_DONE,LOOP_REQ_SO_DONE
     $ ,MP_LOOP_REQ_SO_DONE,CTCALL_REQ_SO_DONE,FILTER_SO

      COMPLEX*32 AMP(NBORNAMPS)
      COMMON/MP_AMPS/AMP
      COMPLEX*32 W(20,NWAVEFUNCS)
      COMMON/MP_W/W

      COMPLEX*32 WL(MAXLWFSIZE,0:LOOPMAXCOEFS-1,MAXLWFSIZE,
     $ -1:NLOOPWAVEFUNCS)
      COMPLEX*32 PL(0:3,-1:NLOOPWAVEFUNCS)
      COMMON/MP_WL/WL,PL

      COMPLEX*32 AMPL(3,NCTAMPS)
      COMMON/MP_AMPL/AMPL

C     
C     ----------
C     BEGIN CODE
C     ----------

C     The target squared split order contribution is already reached
C      if true.
      IF (FILTER_SO.AND.MP_CT_REQ_SO_DONE) THEN
        GOTO 1001
      ENDIF

      CALL MP_VXXXXX(P(0,1),ZERO,NHEL(1),-1*IC(1),W(1,1))
      CALL MP_VXXXXX(P(0,2),ZERO,NHEL(2),-1*IC(2),W(1,2))
      CALL MP_OXXXXX(P(0,3),MDL_MT,NHEL(3),+1*IC(3),W(1,3))
      CALL MP_IXXXXX(P(0,4),MDL_MT,NHEL(4),-1*IC(4),W(1,4))
      CALL MP_VVV10_11P0_1(W(1,1),W(1,2),GC_10,GC_12,ZERO,ZERO,W(1,5))
C     Amplitude(s) for born diagram with ID 1
      CALL MP_FFV1_0(W(1,4),W(1,3),W(1,5),GC_11,AMP(1))
      CALL MP_FFV1_1(W(1,3),W(1,1),GC_11,MDL_MT,MDL_WT,W(1,6))
C     Amplitude(s) for born diagram with ID 2
      CALL MP_FFV1_0(W(1,4),W(1,6),W(1,2),GC_11,AMP(2))
      CALL MP_FFV1_2(W(1,4),W(1,1),GC_11,MDL_MT,MDL_WT,W(1,7))
C     Amplitude(s) for born diagram with ID 3
      CALL MP_FFV1_0(W(1,7),W(1,3),W(1,2),GC_11,AMP(3))
C     Counter-term amplitude(s) for loop diagram number 4
      CALL MP_FFV3_0(W(1,4),W(1,3),W(1,5),R2GC_159_36,AMPL(1,1))
      CALL MP_FFV3_0(W(1,4),W(1,3),W(1,5),UVGC_159_91_1EPS,AMPL(2,2))
      CALL MP_FFV2_3_0(W(1,4),W(1,3),W(1,5),UVGC_156_87,UVGC_159_91
     $ ,AMPL(1,3))
      CALL MP_FFV1_2(W(1,4),W(1,2),GC_11,MDL_MT,MDL_WT,W(1,8))
C     Counter-term amplitude(s) for loop diagram number 5
      CALL MP_FF5_0(W(1,8),W(1,6),UVGC_158_90_1EPS,AMPL(2,4))
      CALL MP_FF3_5_6_0(W(1,8),W(1,6),UVGC_155_85,UVGC_158_90
     $ ,UVGC_157_89,AMPL(1,5))
C     Counter-term amplitude(s) for loop diagram number 6
      CALL MP_FFV3_0(W(1,4),W(1,6),W(1,2),R2GC_159_36,AMPL(1,6))
      CALL MP_FFV3_0(W(1,4),W(1,6),W(1,2),UVGC_159_91_1EPS,AMPL(2,7))
      CALL MP_FFV2_3_0(W(1,4),W(1,6),W(1,2),UVGC_156_87,UVGC_159_91
     $ ,AMPL(1,8))
      CALL MP_FFV1_1(W(1,3),W(1,2),GC_11,MDL_MT,MDL_WT,W(1,9))
C     Counter-term amplitude(s) for loop diagram number 7
      CALL MP_FF5_0(W(1,7),W(1,9),UVGC_158_90_1EPS,AMPL(2,9))
      CALL MP_FF3_5_6_0(W(1,7),W(1,9),UVGC_155_85,UVGC_158_90
     $ ,UVGC_157_89,AMPL(1,10))
C     Counter-term amplitude(s) for loop diagram number 8
      CALL MP_FFV3_0(W(1,7),W(1,3),W(1,2),R2GC_159_36,AMPL(1,11))
      CALL MP_FFV3_0(W(1,7),W(1,3),W(1,2),UVGC_159_91_1EPS,AMPL(2,12))
      CALL MP_FFV2_3_0(W(1,7),W(1,3),W(1,2),UVGC_156_87,UVGC_159_91
     $ ,AMPL(1,13))
C     Counter-term amplitude(s) for loop diagram number 9
      CALL MP_FFV3_0(W(1,4),W(1,9),W(1,1),R2GC_159_36,AMPL(1,14))
      CALL MP_FFV3_0(W(1,4),W(1,9),W(1,1),UVGC_159_91_1EPS,AMPL(2,15))
      CALL MP_FFV2_3_0(W(1,4),W(1,9),W(1,1),UVGC_156_87,UVGC_159_91
     $ ,AMPL(1,16))
C     Counter-term amplitude(s) for loop diagram number 10
      CALL MP_FFV3_0(W(1,8),W(1,3),W(1,1),R2GC_159_36,AMPL(1,17))
      CALL MP_FFV3_0(W(1,8),W(1,3),W(1,1),UVGC_159_91_1EPS,AMPL(2,18))
      CALL MP_FFV2_3_0(W(1,8),W(1,3),W(1,1),UVGC_156_87,UVGC_159_91
     $ ,AMPL(1,19))
C     At this point, all CT amps needed for (NP1=2 NP3=0 NP2=0 QCD=4
C      QED=0), i.e. of split order ID=1, are computed.
      IF(FILTER_SO.AND.SQSO_TARGET.EQ.1) GOTO 2000
      CALL MP_FFV1P0_3(W(1,4),W(1,3),GC_11,ZERO,ZERO,W(1,10))
C     Counter-term amplitude(s) for loop diagram number 13
      CALL MP_VV1_3_0(W(1,5),W(1,10),R2GC_137_23,R2GC_136_22,AMPL(1,20)
     $ )
      CALL MP_VV1_0(W(1,5),W(1,10),UVGC_137_27_1EPS,AMPL(2,21))
C     Counter-term amplitude(s) for loop diagram number 14
      CALL MP_FFV1_0(W(1,4),W(1,3),W(1,5),R2GC_106_1,AMPL(1,22))
      CALL MP_FFV1_7_0(W(1,4),W(1,3),W(1,5),UVGC_111_2_1EPS
     $ ,UVGC_156_86_1EPS,AMPL(2,23))
      CALL MP_FFV7_0(W(1,4),W(1,3),W(1,5),UVGC_141_41_1EPS,AMPL(2,24))
      CALL MP_FFV7_0(W(1,4),W(1,3),W(1,5),UVGC_141_41_1EPS,AMPL(2,25))
      CALL MP_FFV7_0(W(1,4),W(1,3),W(1,5),UVGC_141_41_1EPS,AMPL(2,26))
      CALL MP_FFV7_0(W(1,4),W(1,3),W(1,5),UVGC_141_41_1EPS,AMPL(2,27))
      CALL MP_FFV7_0(W(1,4),W(1,3),W(1,5),UVGC_141_42_1EPS,AMPL(2,28))
      CALL MP_FFV7_0(W(1,4),W(1,3),W(1,5),UVGC_141_43_1EPS,AMPL(2,29))
      CALL MP_FFV7_0(W(1,4),W(1,3),W(1,5),UVGC_141_40,AMPL(1,30))
      CALL MP_FFV7_0(W(1,4),W(1,3),W(1,5),UVGC_141_44,AMPL(1,31))
      CALL MP_FFV7_0(W(1,4),W(1,3),W(1,5),UVGC_141_45,AMPL(1,32))
      CALL MP_FFV7_0(W(1,4),W(1,3),W(1,5),UVGC_156_86,AMPL(1,33))
C     Counter-term amplitude(s) for loop diagram number 16
      CALL MP_FF6_7_0(W(1,8),W(1,6),R2GC_157_35,R2GC_126_20,AMPL(1,34))
      CALL MP_FF6_7_0(W(1,8),W(1,6),UVGC_157_88_1EPS,UVGC_155_84_1EPS
     $ ,AMPL(2,35))
      CALL MP_FF6_7_0(W(1,8),W(1,6),UVGC_157_88,UVGC_155_84,AMPL(1,36))
C     Counter-term amplitude(s) for loop diagram number 17
      CALL MP_FFV1_0(W(1,4),W(1,6),W(1,2),R2GC_106_1,AMPL(1,37))
      CALL MP_FFV1_7_0(W(1,4),W(1,6),W(1,2),UVGC_111_2_1EPS
     $ ,UVGC_156_86_1EPS,AMPL(2,38))
      CALL MP_FFV7_0(W(1,4),W(1,6),W(1,2),UVGC_141_41_1EPS,AMPL(2,39))
      CALL MP_FFV7_0(W(1,4),W(1,6),W(1,2),UVGC_141_41_1EPS,AMPL(2,40))
      CALL MP_FFV7_0(W(1,4),W(1,6),W(1,2),UVGC_141_41_1EPS,AMPL(2,41))
      CALL MP_FFV7_0(W(1,4),W(1,6),W(1,2),UVGC_141_41_1EPS,AMPL(2,42))
      CALL MP_FFV7_0(W(1,4),W(1,6),W(1,2),UVGC_141_42_1EPS,AMPL(2,43))
      CALL MP_FFV7_0(W(1,4),W(1,6),W(1,2),UVGC_141_43_1EPS,AMPL(2,44))
      CALL MP_FFV7_0(W(1,4),W(1,6),W(1,2),UVGC_141_40,AMPL(1,45))
      CALL MP_FFV7_0(W(1,4),W(1,6),W(1,2),UVGC_141_44,AMPL(1,46))
      CALL MP_FFV7_0(W(1,4),W(1,6),W(1,2),UVGC_141_45,AMPL(1,47))
      CALL MP_FFV7_0(W(1,4),W(1,6),W(1,2),UVGC_156_86,AMPL(1,48))
C     Counter-term amplitude(s) for loop diagram number 19
      CALL MP_FF6_7_0(W(1,7),W(1,9),R2GC_157_35,R2GC_126_20,AMPL(1,49))
      CALL MP_FF6_7_0(W(1,7),W(1,9),UVGC_157_88_1EPS,UVGC_155_84_1EPS
     $ ,AMPL(2,50))
      CALL MP_FF6_7_0(W(1,7),W(1,9),UVGC_157_88,UVGC_155_84,AMPL(1,51))
C     Counter-term amplitude(s) for loop diagram number 20
      CALL MP_FFV1_0(W(1,7),W(1,3),W(1,2),R2GC_106_1,AMPL(1,52))
      CALL MP_FFV1_7_0(W(1,7),W(1,3),W(1,2),UVGC_111_2_1EPS
     $ ,UVGC_156_86_1EPS,AMPL(2,53))
      CALL MP_FFV7_0(W(1,7),W(1,3),W(1,2),UVGC_141_41_1EPS,AMPL(2,54))
      CALL MP_FFV7_0(W(1,7),W(1,3),W(1,2),UVGC_141_41_1EPS,AMPL(2,55))
      CALL MP_FFV7_0(W(1,7),W(1,3),W(1,2),UVGC_141_41_1EPS,AMPL(2,56))
      CALL MP_FFV7_0(W(1,7),W(1,3),W(1,2),UVGC_141_41_1EPS,AMPL(2,57))
      CALL MP_FFV7_0(W(1,7),W(1,3),W(1,2),UVGC_141_42_1EPS,AMPL(2,58))
      CALL MP_FFV7_0(W(1,7),W(1,3),W(1,2),UVGC_141_43_1EPS,AMPL(2,59))
      CALL MP_FFV7_0(W(1,7),W(1,3),W(1,2),UVGC_141_40,AMPL(1,60))
      CALL MP_FFV7_0(W(1,7),W(1,3),W(1,2),UVGC_141_44,AMPL(1,61))
      CALL MP_FFV7_0(W(1,7),W(1,3),W(1,2),UVGC_141_45,AMPL(1,62))
      CALL MP_FFV7_0(W(1,7),W(1,3),W(1,2),UVGC_156_86,AMPL(1,63))
C     Counter-term amplitude(s) for loop diagram number 22
      CALL MP_FFV1_0(W(1,4),W(1,9),W(1,1),R2GC_106_1,AMPL(1,64))
      CALL MP_FFV1_7_0(W(1,4),W(1,9),W(1,1),UVGC_111_2_1EPS
     $ ,UVGC_156_86_1EPS,AMPL(2,65))
      CALL MP_FFV7_0(W(1,4),W(1,9),W(1,1),UVGC_141_41_1EPS,AMPL(2,66))
      CALL MP_FFV7_0(W(1,4),W(1,9),W(1,1),UVGC_141_41_1EPS,AMPL(2,67))
      CALL MP_FFV7_0(W(1,4),W(1,9),W(1,1),UVGC_141_41_1EPS,AMPL(2,68))
      CALL MP_FFV7_0(W(1,4),W(1,9),W(1,1),UVGC_141_41_1EPS,AMPL(2,69))
      CALL MP_FFV7_0(W(1,4),W(1,9),W(1,1),UVGC_141_42_1EPS,AMPL(2,70))
      CALL MP_FFV7_0(W(1,4),W(1,9),W(1,1),UVGC_141_43_1EPS,AMPL(2,71))
      CALL MP_FFV7_0(W(1,4),W(1,9),W(1,1),UVGC_141_40,AMPL(1,72))
      CALL MP_FFV7_0(W(1,4),W(1,9),W(1,1),UVGC_141_44,AMPL(1,73))
      CALL MP_FFV7_0(W(1,4),W(1,9),W(1,1),UVGC_141_45,AMPL(1,74))
      CALL MP_FFV7_0(W(1,4),W(1,9),W(1,1),UVGC_156_86,AMPL(1,75))
C     Counter-term amplitude(s) for loop diagram number 23
      CALL MP_FFV1_0(W(1,8),W(1,3),W(1,1),R2GC_106_1,AMPL(1,76))
      CALL MP_FFV1_7_0(W(1,8),W(1,3),W(1,1),UVGC_111_2_1EPS
     $ ,UVGC_156_86_1EPS,AMPL(2,77))
      CALL MP_FFV7_0(W(1,8),W(1,3),W(1,1),UVGC_141_41_1EPS,AMPL(2,78))
      CALL MP_FFV7_0(W(1,8),W(1,3),W(1,1),UVGC_141_41_1EPS,AMPL(2,79))
      CALL MP_FFV7_0(W(1,8),W(1,3),W(1,1),UVGC_141_41_1EPS,AMPL(2,80))
      CALL MP_FFV7_0(W(1,8),W(1,3),W(1,1),UVGC_141_41_1EPS,AMPL(2,81))
      CALL MP_FFV7_0(W(1,8),W(1,3),W(1,1),UVGC_141_42_1EPS,AMPL(2,82))
      CALL MP_FFV7_0(W(1,8),W(1,3),W(1,1),UVGC_141_43_1EPS,AMPL(2,83))
      CALL MP_FFV7_0(W(1,8),W(1,3),W(1,1),UVGC_141_40,AMPL(1,84))
      CALL MP_FFV7_0(W(1,8),W(1,3),W(1,1),UVGC_141_44,AMPL(1,85))
      CALL MP_FFV7_0(W(1,8),W(1,3),W(1,1),UVGC_141_45,AMPL(1,86))
      CALL MP_FFV7_0(W(1,8),W(1,3),W(1,1),UVGC_156_86,AMPL(1,87))
C     Counter-term amplitude(s) for loop diagram number 26
      CALL MP_VVV10_11_0(W(1,1),W(1,2),W(1,10),R2GC_138_25,R2GC_146_27
     $ ,AMPL(1,88))
      CALL MP_VVV10_11_0(W(1,1),W(1,2),W(1,10),UVGC_138_31_1EPS
     $ ,UVGC_146_48_1EPS,AMPL(2,89))
      CALL MP_VVV10_11_0(W(1,1),W(1,2),W(1,10),UVGC_138_32_1EPS
     $ ,UVGC_146_49_1EPS,AMPL(2,90))
      CALL MP_VVV10_11_0(W(1,1),W(1,2),W(1,10),UVGC_138_32_1EPS
     $ ,UVGC_146_49_1EPS,AMPL(2,91))
      CALL MP_VVV10_11_0(W(1,1),W(1,2),W(1,10),UVGC_138_32_1EPS
     $ ,UVGC_146_49_1EPS,AMPL(2,92))
      CALL MP_VVV10_11_0(W(1,1),W(1,2),W(1,10),UVGC_138_32_1EPS
     $ ,UVGC_146_49_1EPS,AMPL(2,93))
      CALL MP_VVV10_11_0(W(1,1),W(1,2),W(1,10),UVGC_138_34_1EPS
     $ ,UVGC_146_52_1EPS,AMPL(2,94))
      CALL MP_VVV10_11_0(W(1,1),W(1,2),W(1,10),UVGC_138_35_1EPS
     $ ,UVGC_146_53_1EPS,AMPL(2,95))
      CALL MP_VVV12_13_2_6_7_8_0(W(1,1),W(1,2),W(1,10),UVGC_116_7_1EPS
     $ ,UVGC_115_5_1EPS,UVGC_146_51_1EPS,UVGC_140_39_1EPS
     $ ,UVGC_139_37_1EPS,UVGC_147_55_1EPS,AMPL(2,96))
      CALL MP_VVV1_2_3_4_5_6_7_8_0(W(1,1),W(1,2),W(1,10)
     $ ,UVGC_138_33_1EPS,UVGC_146_50_1EPS,UVGC_115_4_1EPS
     $ ,UVGC_148_56_1EPS,UVGC_116_6_1EPS,UVGC_140_38_1EPS
     $ ,UVGC_139_36_1EPS,UVGC_147_54_1EPS,AMPL(2,97))
      CALL MP_VVV10_11_0(W(1,1),W(1,2),W(1,10),UVGC_138_31,UVGC_146_48
     $ ,AMPL(1,98))
      CALL MP_VVV10_11_0(W(1,1),W(1,2),W(1,10),UVGC_138_34,UVGC_146_52
     $ ,AMPL(1,99))
      CALL MP_VVV10_11_0(W(1,1),W(1,2),W(1,10),UVGC_138_35,UVGC_146_53
     $ ,AMPL(1,100))
C     Counter-term amplitude(s) for loop diagram number 37
      CALL MP_VV1_0(W(1,5),W(1,10),UVGC_137_28_1EPS,AMPL(2,101))
C     Counter-term amplitude(s) for loop diagram number 40
      CALL MP_VV3_0(W(1,5),W(1,10),R2GC_136_21,AMPL(1,102))
      CALL MP_VV3_0(W(1,5),W(1,10),R2GC_136_21,AMPL(1,103))
      CALL MP_VV3_0(W(1,5),W(1,10),R2GC_136_21,AMPL(1,104))
      CALL MP_VV3_0(W(1,5),W(1,10),R2GC_136_21,AMPL(1,105))
C     Counter-term amplitude(s) for loop diagram number 41
      CALL MP_VVV10_11_0(W(1,1),W(1,2),W(1,10),R2GC_138_24,R2GC_146_26
     $ ,AMPL(1,106))
      CALL MP_VVV10_11_0(W(1,1),W(1,2),W(1,10),R2GC_138_24,R2GC_146_26
     $ ,AMPL(1,107))
      CALL MP_VVV10_11_0(W(1,1),W(1,2),W(1,10),R2GC_138_24,R2GC_146_26
     $ ,AMPL(1,108))
      CALL MP_VVV10_11_0(W(1,1),W(1,2),W(1,10),R2GC_138_24,R2GC_146_26
     $ ,AMPL(1,109))
C     Counter-term amplitude(s) for loop diagram number 43
      CALL MP_VV2_0(W(1,5),W(1,10),R2GC_108_3,AMPL(1,110))
      CALL MP_VV3_0(W(1,5),W(1,10),R2GC_136_21,AMPL(1,111))
      CALL MP_VV1_3_0(W(1,5),W(1,10),UVGC_137_26_1EPS,UVGC_136_23_1EPS
     $ ,AMPL(2,112))
      CALL MP_VV1_3_0(W(1,5),W(1,10),UVGC_137_26,UVGC_136_23,AMPL(1
     $ ,113))
C     Counter-term amplitude(s) for loop diagram number 44
      CALL MP_VVV10_11_0(W(1,1),W(1,2),W(1,10),R2GC_138_24,R2GC_146_26
     $ ,AMPL(1,114))
C     Counter-term amplitude(s) for loop diagram number 46
      CALL MP_VV2_0(W(1,5),W(1,10),R2GC_108_5,AMPL(1,115))
      CALL MP_VV3_0(W(1,5),W(1,10),R2GC_136_21,AMPL(1,116))
      CALL MP_VV1_3_0(W(1,5),W(1,10),UVGC_137_30_1EPS,UVGC_136_25_1EPS
     $ ,AMPL(2,117))
      CALL MP_VV1_3_0(W(1,5),W(1,10),UVGC_137_30,UVGC_136_25,AMPL(1
     $ ,118))
C     Counter-term amplitude(s) for loop diagram number 47
      CALL MP_VVV10_11_0(W(1,1),W(1,2),W(1,10),R2GC_138_24,R2GC_146_26
     $ ,AMPL(1,119))
C     Counter-term amplitude(s) for loop diagram number 49
      CALL MP_VV2_0(W(1,5),W(1,10),R2GC_108_4,AMPL(1,120))
      CALL MP_VV3_0(W(1,5),W(1,10),R2GC_136_21,AMPL(1,121))
      CALL MP_VV1_3_0(W(1,5),W(1,10),UVGC_137_29_1EPS,UVGC_136_24_1EPS
     $ ,AMPL(2,122))
      CALL MP_VV1_3_0(W(1,5),W(1,10),UVGC_137_29,UVGC_136_24,AMPL(1
     $ ,123))
C     Counter-term amplitude(s) for loop diagram number 50
      CALL MP_VVV10_11_0(W(1,1),W(1,2),W(1,10),R2GC_138_24,R2GC_146_26
     $ ,AMPL(1,124))
C     At this point, all CT amps needed for (NP1=0 NP3=0 NP2=0 QCD=6
C      QED=0), i.e. of split order ID=2, are computed.
      IF(FILTER_SO.AND.SQSO_TARGET.EQ.2) GOTO 2000

      GOTO 1001
 2000 CONTINUE
      MP_CT_REQ_SO_DONE=.TRUE.
 1001 CONTINUE
      END

