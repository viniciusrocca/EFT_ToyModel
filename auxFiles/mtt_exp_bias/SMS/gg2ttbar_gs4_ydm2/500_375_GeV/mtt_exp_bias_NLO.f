
      
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
      double precision mtt, mtt_sq
      double precision p_val, p_offset, final_arg
      double precision stitch_sum
      double precision p1_at_b1, p2_at_b1, p2_at_b2, p3_at_b2
      double precision p3_at_b3, p4_at_b3, p4_at_b4, p5_at_b4

C --- Boundary and Normalization Parameters ---
      double precision, parameter :: bound_1 = 900.0d0
      double precision, parameter :: bound_2 = 1200.0d0
      double precision, parameter :: bound_3 = 1900.0d0
      double precision, parameter :: bound_4 = 3400.0d0
      double precision, parameter :: mtt_norm = 1500.0d0

      
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

c             Calculate the normalization offset using the first polynomial
              p_offset = -4.5930d-06*mtt_norm**2
              p_offset = p_offset - 2.9131d-03*mtt_norm
              p_offset = p_offset - 1.2490d+00
              p_offset = -p_offset
    
c             Pre-calculate the function values at each boundary
              p1_at_b1 = -4.5930d-06*bound_1**2 - 2.9131d-03*bound_1
              p1_at_b1 = p1_at_b1 - 1.2490d+00
              p1_at_b1 = -p1_at_b1
              
              p2_at_b1 = -1.4674d-04*bound_1**2 + 3.0145d-01*bound_1
              p2_at_b1 = p2_at_b1 - 1.6292d+02
              p2_at_b1 = -p2_at_b1
    
              p2_at_b2 = -1.4674d-04*bound_2**2 + 3.0145d-01*bound_2
              p2_at_b2 = p2_at_b2 - 1.6292d+02
              p2_at_b2 = -p2_at_b2
              
              p3_at_b2 = -7.4646d-07*bound_2**2 - 2.4963d-04*bound_2
              p3_at_b2 = p3_at_b2 - 7.4813d+00
              p3_at_b2 = -p3_at_b2
    
              p3_at_b3 = -7.4646d-07*bound_3**2 - 2.4963d-04*bound_3
              p3_at_b3 = p3_at_b3 - 7.4813d+00
              p3_at_b3 = -p3_at_b3
              
              p4_at_b3 = 5.5304d-08*bound_3**2 - 2.7483d-03*bound_3
              p4_at_b3 = p4_at_b3 - 6.2571d+00
              p4_at_b3 = -p4_at_b3
    
              p4_at_b4 = 5.5304d-08*bound_4**2 - 2.7483d-03*bound_4
              p4_at_b4 = p4_at_b4 - 6.2571d+00
              p4_at_b4 = -p4_at_b4
              
              p5_at_b4 = -4.0408d-07*bound_4**2 + 1.1178d-03*bound_4
              p5_at_b4 = p5_at_b4 - 1.4871d+01
              p5_at_b4 = -p5_at_b4

              if (mtt .lt. bound_1) then
c                 --- REGION 1 ---
                  p_val = -4.5930d-06*mtt**2 - 2.9131d-03*mtt 
     &                 - 1.2490d+00
                  p_val = -p_val
                  final_arg = p_val - p_offset

              else if (mtt .lt. bound_2) then
c                 --- REGION 2 ---
                  p_val = -1.4674d-04*mtt**2 + 3.0145d-01*mtt 
     &                 - 1.6292d+02
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1)
                  final_arg = p_val + stitch_sum - p_offset
        
              else if (mtt .lt. bound_3) then
c                 --- REGION 3 ---
                  p_val = -7.4646d-07*mtt**2 - 2.4963d-04*mtt 
     &                 - 7.4813d+00
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  final_arg = p_val + stitch_sum - p_offset

              else if (mtt .lt. bound_4) then
c                 --- REGION 4 ---
                  p_val = 5.5304d-08*mtt**2 - 2.7483d-03*mtt 
     &                 - 6.2571d+00
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  final_arg = p_val + stitch_sum - p_offset
        
              else
c                 --- REGION 5 ---
                  mtt = min(7000.0d0, mtt)
                  p_val = -4.0408d-07*mtt**2 + 1.1178d-03*mtt 
     &                 - 1.4871d+01
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  stitch_sum = stitch_sum + (p4_at_b4 - p5_at_b4)
                  final_arg = p_val + stitch_sum - p_offset
      
              endif
c             Calculate the final bias_weight on its own line
              bias_wgt = EXP(final_arg)
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
