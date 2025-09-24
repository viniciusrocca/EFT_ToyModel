
      
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
      
      double precision, parameter :: bound_1 = 1051.0d0
      double precision, parameter :: bound_2 = 1651.0d0
      double precision, parameter :: bound_3 = 1851.0d0
      double precision, parameter :: bound_4 = 2751.0d0
      double precision, parameter :: mtt_norm = 1000.0d0

      
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

      if (mtt.gt.0.0d0) then


c        Calculate the initial offset to normalize the first piece
         p_offset = - ( 5.0d-06 * mtt_norm**2 - 1.2d-02 * mtt_norm + 0.2d0 )

         if (mtt .lt. bound_1) then
c           --- REGION 1 ---
            p_val = - ( 5.0d-06 * mtt**2 - 1.2d-02 * mtt + 0.2d0 )
            bias_wgt = EXP(p_val - p_offset)

         else if (mtt .lt. bound_2) then
c           --- REGION 2 (Stitched to Region 1) ---
            p_val = - ( - 1.0d-05 * mtt**2 + 1.8d-02 * mtt - 1.43d+01 )
            p1_at_b1 = - ( 5.0d-06 * bound_1**2 - 1.2d-02 * bound_1 + 0.2d0 )
            p2_at_b1 = - ( - 1.0d-05 * bound_1**2 + 1.8d-02 * bound_1 - 1.41d+01 )
            bias_wgt = EXP(p_val + (p1_at_b1 - p2_at_b1) - p_offset)

         else if (mtt .lt. bound_3) then
c           --- REGION 3 (Stitched to Region 2) ---
            p_val = - (  2.8d-04 * mtt**2 - 9.8d-01 * mtt + 8.395d+02 )
            p2_at_b2 = - ( - 1.0d-05 * bound_2**2 + 1.8d-02 * bound_2 - 1.41d+01 ) 
            p3_at_b2 = - (  2.8d-04 * bound_2**2 - 9.8d-01 * bound_2 + 8.395d+02 )
            bias_wgt = EXP(p_val + (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2) - p_offset)

         else if (mtt .lt. bound_4) then
c           --- REGION 4 (Stitched to Region 3) ---
            p_val = - ( - 1.4d-06 * mtt**2 + 5.1d-03 * mtt - 16.5d0 )
            p3_at_b3 = - (  2.8d-04 * bound_3**2 - 9.8d-01 * bound_3 + 8.395d+02 )
            p4_at_b3 = - ( - 1.4d-06 * bound_3**2 + 5.1d-03 * bound_3 - 16.5d0 )
            bias_wgt = EXP(p_val + (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2) + (p3_at_b3 - p4_at_b3) - p_offset)

         else
c           --- REGION 5 (Stitched to Region 4) ---
c	    mtt = min(mtt,4000.0)
            p_val = - ( 4.2d-07 * mtt**2 - 5.8d-03 * mtt - 6.85d-01 )
            p4_at_b4 = - ( - 3.6d-07 * bound_4**2 + 3.2d-05 * bound_4 - 10.5d0 )
            p5_at_b4 = - ( 4.2d-07 * bound_4**2 - 5.8d-03 * bound_4 - 6.85d-01 )
            bias_wgt = EXP(p_val + (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2) + (p3_at_b3 - p4_at_b3) + (p4_at_b4 - p5_at_b4) - p_offset)
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
