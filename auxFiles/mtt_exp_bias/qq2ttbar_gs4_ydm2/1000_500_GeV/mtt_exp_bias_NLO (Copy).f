subroutine bias_weight_function(p,ipdg,bias_wgt)

      implicit none
      include 'nexternal.inc'

c     --- ARGUMENTS ---
      double precision bias_wgt
      double precision p(0:3,nexternal)
      integer ipdg(nexternal)

c     --- LOCAL VARIABLES ---
      integer i,j
      double precision pTot(0:3)
      double precision mtt
      double precision p_val, p_offset

c     --- BOUNDARY PARAMETERS ---
      double precision, parameter :: bound_1 = 1337.625d0
      double precision, parameter :: bound_2 = 1536.250d0
      double precision, parameter :: bound_3 = 2200.0d0
      double precision, parameter :: bound_4 = 2400.0d0
      double precision, parameter :: bound_5 = 4160.0d0
      
      double precision, parameter :: mtt_norm = 1000.0d0

c     --- INITIALIZATION ---
      bias_wgt = 1d0
      mtt = 0d0
      pTot = (/ 0d0, 0d0, 0d0, 0d0 /)

c     --- CALCULATE INVARIANT MASS (mtt) ---
      do i=1,nexternal
         if (abs(ipdg(i)).eq.6) then
            do j =0,3
               pTot(j) = pTot(j)+p(j,i)
            enddo 
         endif
      enddo

      mtt = dsqrt(pTot(0)**2 - pTot(1)**2 - pTot(2)**2 - pTot(3)**2)

      if (mtt .le. 0.0d0) return

c     ==================================================================
c     CALCULATE NORMALIZATION OFFSET (mtt = 1000 GeV)
c     Using Region 1 Coefficients (since 1000 < 1337.625)
c     ==================================================================
      p_offset = 3.56949962d-11 * mtt_norm**3 
     &         + 1.86036127d-06 * mtt_norm**2 
     &         - 6.48783136d-03 * mtt_norm 
     &         - 2.80379538d+00

c     ==================================================================
c     CALCULATE P_VAL (Current mtt)
c     ==================================================================

      if (mtt .lt. bound_1) then
c        --- REGION 1 (Cubic) ---
         p_val = 3.56949962d-11 * mtt**3 
     &         + 1.86036127d-06 * mtt**2 
     &         - 6.48783136d-03 * mtt 
     &         - 2.80379538d+00

      else if (mtt .lt. bound_2) then
c        --- REGION 2 (Quadratic) ---
         p_val = -3.66915916d-05 * mtt**2 
     &         + 1.05484164d-01 * mtt 
     &         - 9.17199776d+01

      else if (mtt .lt. bound_3) then
c        --- REGION 3 (Cubic) ---
         p_val = -1.38083045d-08 * mtt**3 
     &         + 7.29203858d-05 * mtt**2 
     &         - 1.34423253d-01 * mtt 
     &         + 6.65990117d+01

      else if (mtt .lt. bound_4) then
c        --- REGION 4 (Quadratic) ---
         p_val =  4.93901208d-05 * mtt**2 
     &         - 2.18831485d-01 * mtt 
     &         + 2.28299685d+02

      else if (mtt .lt. bound_5) then
c        --- REGION 5 (Cubic) ---
         mtt = min(mtt, 3500.0d0)
         p_val =  5.96796474d-10 * mtt**3 
     &         - 6.41566734d-06 * mtt**2 
     &         + 2.07459830d-02 * mtt 
     &         - 3.42598704d+01

      endif

c     ==================================================================
c     FINAL BIAS WEIGHT
c     Bias = exp( Reference_Point - Target_Function )
c     ==================================================================
      bias_wgt = EXP(p_offset - p_val)

      return
      end
