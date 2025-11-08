
      
      subroutine bias_weight_function(p,ipdg,bias_wgt)
c This is a user-defined function to which to bias the event generation.
c A non-flat distribution will generate events with a certain weight
c inversely proportinal to the bias_wgt. This is particularly useful to
c generate more events (with smaller weight) in tails of distributions.
c It computes the bias_wgt factor from the momenta and multiplies the
c weight that goes into MINT (or vegas) with this factor.  Before
c writing out the events (or making the plots), this factor is again
c divided out. A value different from 1 makes that MINT (or vegas) does
c not list the correct cross section, but the cross section can still be
c computed from summing all the weights of the events (and dividing by
c the number of events). Since the weights of the events are no longer
c identical for all events, the statistical uncertainty on this total
c cross section can be much larger than without including the bias.
c
c The 'bias_wgt' should be a IR-safe function of the momenta.
c      
c For this to be used, the 'event_norm' option in the run_card should be
c set to
c      'bias' = event_norm      
c
      implicit none
      include 'nexternal.inc'
      double precision bias_wgt,p(0:3,nexternal),H_T
      integer ipdg(nexternal),i,j
      double precision pTot(0:3)
      double precision mtt
      double precision p_val, p_offset
      double precision p1_at_b1, p2_at_b1, p2_at_b2, p3_at_b2
      double precision p3_at_b3, p4_at_b3, p4_at_b4, p5_at_b4
      double precision p5_at_b5, p6_at_b5, p6_at_b6, p7_at_b6

c --- Boundary and Normalization Parameters ---
      double precision, parameter :: bound_1 = 900.0d0
      double precision, parameter :: bound_2 = 2200.0d0
      double precision, parameter :: bound_3 = 2800.0d0
      double precision, parameter :: bound_4 = 4600.0d0
      double precision, parameter :: bound_5 = 5700.0d0
      double precision, parameter :: bound_6 = 6500.0d0
      double precision, parameter :: mtt_norm = 2000.0d0
      
c local variables defined in the run_card
c
c      double precision mtt_bias_target_mtt
c      double precision mtt_bias_enhancement_power

      bias_wgt=1d0
      mtt = 0d0
      pTot = (/ 0d0, 0d0, 0d0, 0d0 /)
      do i=1,nexternal
          if (abs(ipdg(i)).eq.6) then
          ! if (abs(idup(i,1,1)).eq.6) then
            do j =0,3
              pTot(j) = pTot(j)+p(j,i)
            enddo 
          endif
      enddo

      mtt = dsqrt(pTot(0)**2 - pTot(1)**2 - pTot(2)**2 - pTot(3)**2)
if (mtt .gt. 0.0d0) then

c        Calculate the normalization offset using the first polynomial at mtt_norm
         p_offset = -(-6.1329d-06*mtt_norm**2 + 6.2221d-03*mtt_norm - 1.0890d+01)
         
c        Pre-calculate the function values at each boundary for stitching
         p1_at_b1 = -(-6.1329d-06*bound_1**2 + 6.2221d-03*bound_1 - 1.0890d+01)
         p2_at_b1 = -( 4.1848d-07*bound_1**2 - 3.6289d-03*bound_1 - 7.2336d+00)
         
         p2_at_b2 = -( 4.1848d-07*bound_2**2 - 3.6289d-03*bound_2 - 7.2336d+00)
         p3_at_b2 = -(-9.4944d-07*bound_2**2 + 3.0940d-03*bound_2 - 1.5519d+01)

         p3_at_b3 = -(-9.4944d-07*bound_3**2 + 3.0940d-03*bound_3 - 1.5519d+01)
         p4_at_b3 = -(-4.1803d-07*bound_3**2 + 8.8715d-04*bound_3 - 1.4067d+01)

         p4_at_b4 = -(-4.1803d-07*bound_4**2 + 8.8715d-04*bound_4 - 1.4067d+01)
         p5_at_b4 = -( 8.2147d-07*bound_4**2 - 1.1271d-02*bound_4 + 1.5970d+01)
         
         p5_at_b5 = -( 8.2147d-07*bound_5**2 - 1.1271d-02*bound_5 + 1.5970d+01)
         p6_at_b5 = -( 9.0804d-07*bound_5**2 - 1.3142d-02*bound_5 + 2.3229d+01)
         
         p6_at_b6 = -( 9.0804d-07*bound_6**2 - 1.3142d-02*bound_6 + 2.3229d+01)
         p7_at_b6 = -(-2.5237d-06*bound_6**2 + 2.8872d-02*bound_6 - 1.0532d+02)

c --- Main piecewise function with stitching ---
         if (mtt .lt. bound_1) then
c           --- REGION 1 ---
            p_val = -(-6.1329d-06*mtt**2 + 6.2221d-03*mtt - 1.0890d+01)
            bias_wgt = EXP(p_val - p_offset)

         else if (mtt .lt. bound_2) then
c           --- REGION 2 (Stitched) ---
            p_val = -( 4.1848d-07*mtt**2 - 3.6289d-03*mtt - 7.2336d+00)
            bias_wgt = EXP(p_val + (p1_at_b1 - p2_at_b1) - p_offset)
            
         else if (mtt .lt. bound_3) then
c           --- REGION 3 (Stitched) ---
            p_val = -(-9.4944d-07*mtt**2 + 3.0940d-03*mtt - 1.6019d+01)
            bias_wgt = EXP(p_val + (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2) - p_offset)

         else if (mtt .lt. bound_4) then
c           --- REGION 4 (Stitched) ---
            p_val = -(-4.1803d-07*mtt**2 + 8.8715d-04*mtt - 1.4267d+01)
            bias_wgt = EXP(p_val + (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2) + (p3_at_b3 - p4_at_b3) - p_offset)
            
         else if (mtt .lt. bound_5) then
c           --- REGION 5 (Stitched) ---
            p_val = -( 8.2147d-07*mtt**2 - 1.1271d-02*mtt + 1.5770d+01)
            bias_wgt = EXP(p_val + (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2) + (p3_at_b3 - p4_at_b3) + (p4_at_b4 - p5_at_b4) - p_offset)
         
         else if (mtt .lt. bound_6) then
c           --- REGION 6 (Stitched) ---
            p_val = -( 9.0804d-07*mtt**2 - 1.3142d-02*mtt + 2.3029d+01)
            bias_wgt = EXP(p_val + (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2) + (p3_at_b3 - p4_at_b3) + (p4_at_b4 - p5_at_b4) + (p5_at_b5 - p6_at_b5) - p_offset)

         else
c           --- REGION 7 (Stitched) ---
	    mtt = min(7500.0, mtt)
            p_val = -(-2.5237d-06*mtt**2 + 2.8872d-02*mtt - 1.05523d+02)
            bias_wgt = EXP(p_val + (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2) + (p3_at_b3 - p4_at_b3) + (p4_at_b4 - p5_at_b4) + (p5_at_b5 - p6_at_b5) + (p6_at_b6 - p7_at_b6) - p_offset)
         endif
      endif

c How to enhance the tails is very process dependent. For example for
c top quark production one could use:
c      do i=1,nexternal
c         if (ipdg(i).eq.6) then
c            bias_wgt=sqrt(p(1,i)**2+p(2,i)**2)**3
c         endif
c      enddo
c Or to use H_T^2 one does     
c      H_T=0d0
c      do i=3,nexternal
c         H_T=H_T+sqrt(max(0d0,(p(0,i)+p(3,i))*(p(0,i)-p(3,i))))
c      enddo
c      bias_wgt=H_T**2
      return
      end
