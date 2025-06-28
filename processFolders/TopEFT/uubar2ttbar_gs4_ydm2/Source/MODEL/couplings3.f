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
      GC_31(VECID) = MDL_CQU8B*MDL_COMPLEXI
      GC_44(VECID) = MDL_CUUE*MDL_COMPLEXI
      GC_45(VECID) = MDL_CUUF*MDL_COMPLEXI
      GC_53(VECID) = MDL_COMPLEXI*G
      GC_88(VECID) = (MDL_CUG*MDL_COMPLEXI*MDL_VEV)/MDL_SQRT__2
      END
