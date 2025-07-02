ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP3( VECID)

      IMPLICIT NONE
      INTEGER VECID
      INCLUDE 'model_functions.inc'
      INCLUDE '../vector.inc'


      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_22(VECID) = 2.000000D+00*MDL_CQQ1A*MDL_COMPLEXI
      GC_26(VECID) = 2.000000D+00*MDL_CQQ3*MDL_COMPLEXI
      GC_30(VECID) = MDL_CQU8A*MDL_COMPLEXI
      GC_39(VECID) = 2.000000D+00*MDL_CUUA*MDL_COMPLEXI
      GC_42(VECID) = 2.000000D+00*MDL_CUUC*MDL_COMPLEXI
      GC_53(VECID) = MDL_COMPLEXI*G
      GC_23(VECID) = 2.000000D+00*MDL_CQQ1B*MDL_COMPLEXI+2.000000D+00
     $ *MDL_CQQ1C*MDL_COMPLEXI
      END
