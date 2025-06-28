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
      GC_52(VECID) = -G
      GC_53(VECID) = MDL_COMPLEXI*G
      GC_88(VECID) = (MDL_CUG*MDL_COMPLEXI*MDL_VEV)/MDL_SQRT__2
      GC_92(VECID) = -((MDL_CUG*G*MDL_VEV)/MDL_SQRT__2)
      END
