
      
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
      double precision p_val, p_offset, final_arg
      double precision stitch_sum
      double precision p1_at_b1, p2_at_b1, p2_at_b2, p3_at_b2
      double precision p3_at_b3, p4_at_b3, p4_at_b4, p5_at_b4
      double precision p5_at_b5, p6_at_b5, p6_at_b6, p7_at_b6

c --- Boundary and Normalization Parameters ---
      double precision, parameter :: bound_1 = 850.0d0
      double precision, parameter :: bound_2 = 1050.0d0
      double precision, parameter :: bound_3 = 1400.0d0
      double precision, parameter :: bound_4 = 1550.0d0
      double precision, parameter :: bound_5 = 1850.0d0
      double precision, parameter :: bound_6 = 2450.0d0
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


      if (mtt .gt. 0.0d0) then

c             Calculate the normalization offset using the first polynomial
              p_offset = 2.5878d-06*mtt_norm**2
              p_offset = p_offset - 6.8259d-03*mtt_norm
              p_offset = p_offset - 1.8399d+00
              p_offset = -p_offset
    
c             Pre-calculate the function values at each boundary
              p1_at_b1 = 2.5878d-06*bound_1**2 - 6.8259d-03*bound_1
              p1_at_b1 = p1_at_b1 - 1.8399d+00
              p1_at_b1 = -p1_at_b1
              
              p2_at_b1 = 1.1212d-05*bound_1**2 - 2.0580d-02*bound_1
              p2_at_b1 = p2_at_b1 + 3.6067d+00
              p2_at_b1 = -p2_at_b1
    
              p2_at_b2 = 1.1212d-05*bound_2**2 - 2.0580d-02*bound_2
              p2_at_b2 = p2_at_b2 + 3.6067d+00
              p2_at_b2 = -p2_at_b2
              
              p3_at_b2 = -4.8872d-06*bound_2**2 + 2.2192d-03*bound_2
              p3_at_b2 = p3_at_b2 - 2.9151d+00
              p3_at_b2 = -p3_at_b2
    
              p3_at_b3 = -4.8872d-06*bound_3**2 + 2.2192d-03*bound_3
              p3_at_b3 = p3_at_b3 - 2.9151d+00
              p3_at_b3 = -p3_at_b3
              
              p4_at_b3 = 1.4715d-04*bound_3**2 - 4.5200d-01*bound_3
              p4_at_b3 = p4_at_b3 + 3.3500d+02
              p4_at_b3 = -p4_at_b3
    
              p4_at_b4 = 1.4715d-04*bound_4**2 - 4.5200d-01*bound_4
              p4_at_b4 = p4_at_b4 + 3.3500d+02
              p4_at_b4 = -p4_at_b4
              
C             *** REGION 5 IS CUBIC (ax^3 + bx^2 + cx + d) ***
              p5_at_b4 = -3.7256d-09*bound_4**3 + 5.5659d-06*bound_4**2
              p5_at_b4 = p5_at_b4 + 1.4874d-02*bound_4 - 3.3335d+01
              p5_at_b4 = -p5_at_b4
    
              p5_at_b5 = -3.7256d-09*bound_5**3 + 5.5659d-06*bound_5**2
              p5_at_b5 = p5_at_b5 + 1.4874d-02*bound_5 - 3.3335d+01
              p5_at_b5 = -p5_at_b5
              
              p6_at_b5 = -2.7966d-07*bound_5**2 - 8.2221d-04*bound_5
              p6_at_b5 = p6_at_b5 - 7.9264d+00
              p6_at_b5 = -p6_at_b5

              p6_at_b6 = -2.7966d-07*bound_6**2 - 8.2221d-04*bound_6
              p6_at_b6 = p6_at_b6 - 7.9264d+00
              p6_at_b6 = -p6_at_b6

              p7_at_b6 = 7.2738d-08*bound_6**2 - 2.8587d-03*bound_6
              p7_at_b6 = p7_at_b6 - 5.4113d+00
              p7_at_b6 = -p7_at_b6

              if (mtt .lt. bound_1) then
c                 --- REGION 1 ---
                  p_val = 2.5878d-06*mtt**2 - 6.8259d-03*mtt 
     &                 - 1.8399d+00
                  p_val = -p_val
                  final_arg = p_val - p_offset

              else if (mtt .lt. bound_2) then
c                 --- REGION 2 ---
                  p_val = 1.1212d-05*mtt**2 - 2.0580d-02*mtt 
     &                 + 3.6067d+00
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1)
                  final_arg = p_val + stitch_sum - p_offset
        
              else if (mtt .lt. bound_3) then
c                 --- REGION 3 ---
                  p_val = -4.8872d-06*mtt**2 + 2.2192d-03*mtt 
     &                 - 2.9151d+00
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  final_arg = p_val + stitch_sum - p_offset

              else if (mtt .lt. bound_4) then
c                 --- REGION 4 ---
                  p_val = 1.4715d-04*mtt**2 - 4.5200d-01*mtt 
     &                 + 3.3500d+02
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  final_arg = p_val + stitch_sum - p_offset
        
              else if (mtt .lt. bound_5) then
c                 --- REGION 5 (Cubic Fit) ---
                  p_val = -3.7256d-09*mtt**3 + 5.5659d-06*mtt**2
                  p_val = p_val + 1.4874d-02*mtt - 3.3335d+01
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  stitch_sum = stitch_sum + (p4_at_b4 - p5_at_b4)
                  final_arg = p_val + stitch_sum - p_offset
      
              else if (mtt .lt. bound_6) then
c                 --- REGION 6 ---
                  p_val = -2.7966d-07*mtt**2 - 8.2221d-04*mtt 
     &                 - 7.9264d+00
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  stitch_sum = stitch_sum + (p4_at_b4 - p5_at_b4)
                  stitch_sum = stitch_sum + (p5_at_b5 - p6_at_b5)
                  final_arg = p_val + stitch_sum - p_offset
              
              else
c                 --- REGION 7 ---
                  mtt = min(9000.0d0, mtt)
                  p_val = 7.2738d-08*mtt**2 - 2.8587d-03*mtt 
     &                 - 5.4113d+00
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  stitch_sum = stitch_sum + (p4_at_b4 - p5_at_b4)
                  stitch_sum = stitch_sum + (p5_at_b5 - p6_at_b5)
                  stitch_sum = stitch_sum + (p6_at_b6 - p7_at_b6)
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
