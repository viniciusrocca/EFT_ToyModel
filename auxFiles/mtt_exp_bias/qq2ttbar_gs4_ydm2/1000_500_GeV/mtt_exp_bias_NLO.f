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

c     --- BOUNDARY PARAMETERS (Updated) ---
      double precision, parameter :: bound_1 = 400.0d0
      double precision, parameter :: bound_2 = 1000.0d0
      double precision, parameter :: bound_3 = 1600.0d0
      double precision, parameter :: bound_4 = 2040.0d0
      double precision, parameter :: bound_5 = 2787.5d0
      double precision, parameter :: bound_6 = 3027.5d0
      
      double precision, parameter :: mtt_norm = 2300.0d0

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
c     1000 GeV falls at the start of Region 3 (1000 <= mtt < 1600).
c     We use Region 3 coefficients for the offset.
c     ==================================================================
      p_offset =  1.48255625d-06 * mtt_norm**2 
     &          - 6.16501386d-03 * mtt_norm 
     &          - 3.93574734d+00

c     ==================================================================
c     CALCULATE P_VAL (Current mtt)
c     All provided regions are Quadratic (3 coeffs).
c     ==================================================================

      if (mtt .lt. bound_1) then
c        --- REGION 1 (Quadratic) < 400 ---
         p_val = -1.77574802d-03 * mtt**2 
     &         +  1.33982025d+00 * mtt 
     &         -  2.58811975d+02

      else if (mtt .lt. bound_2) then
c        --- REGION 2 (Quadratic) 400 - 1000 ---
         p_val =  1.78978674d-06 * mtt**2 
     &         -  6.58685515d-03 * mtt 
     &         -  3.83716148d+00

      else if (mtt .lt. bound_3) then
c        --- REGION 3 (Quadratic) 1000 - 1600 ---
         p_val =  1.48255625d-06 * mtt**2 
     &         -  6.16501386d-03 * mtt 
     &         -  3.93574734d+00

      else if (mtt .lt. bound_4) then
c        --- REGION 4 (Quadratic) 1600 - 2040 ---
         p_val =  6.92490983d-06 * mtt**2 
     &         -  2.55629003d-02 * mtt 
     &         +  1.31952163d+01

      else if (mtt .lt. bound_5) then
c        --- REGION 5 (Quadratic) 2040 - 2787.5 ---
         p_val = -2.28535418d-06 * mtt**2 
     &         +  4.96635306d-03 * mtt 
     &         -  1.07826980d+01
     
      else if (mtt .lt. bound_6) then
c        --- REGION 6 (Quadratic) 2787.5 - 3027.5 ---
         p_val =  1.56973384d-04 * mtt**2 
     &         -  9.14441405d-01 * mtt 
     &         +  1.31386532d+03	
c         p_val = p_val + 6.9d0
      else
c        --- REGION 7 (Quadratic) > 3027.5 ---
         mtt = min(mtt, 3500.0d0)
         p_val = -4.68002156d-06 * mtt**2 
     &         +  3.07002143d-02 * mtt 
     &         -  6.58767304d+01
      endif

c     ==================================================================
c     FINAL BIAS WEIGHT
c     Bias = exp( Reference_Point - Target_Function )
c     ==================================================================
      
      bias_wgt = EXP(p_offset - p_val)
 
      return
      end
