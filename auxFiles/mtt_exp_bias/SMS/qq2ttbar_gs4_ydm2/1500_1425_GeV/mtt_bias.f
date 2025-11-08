      subroutine bias_wgt(p, original_weight, bias_weight)
          implicit none
C
C Parameters
C
          include '../../maxparticles.inc'
          include '../../nexternal.inc'
C
C Arguments
C
          double precision p(0:3,nexternal)
          double precision pTot(0:3)
          double precision mtt
          double precision original_weight, bias_weight
C
C local variables
C
          integer i,j
          double precision pt(nexternal)
          double precision p_val, p_offset, final_arg
          double precision stitch_sum, mtt_sq
          double precision p1_at_b1, p2_at_b1, p2_at_b2, p3_at_b2
          double precision p3_at_b3, p4_at_b3, p4_at_b4, p5_at_b4
          double precision p5_at_b5, p6_at_b5
          double precision, parameter :: bound_1 = 900.0d0
          double precision, parameter :: bound_2 = 3000.0d0
          double precision, parameter :: bound_3 = 3600.0d0
          double precision, parameter :: bound_4 = 4100.0d0
          double precision, parameter :: bound_5 = 4500.0d0
C
C local variables defined in the run_card
C
          double precision mtt_bias_offset
C
C Global variables
C
C
C Mandatory common block to be defined in bias modules
C
          double precision stored_bias_weight
          data stored_bias_weight/1.0d0/
          logical impact_xsec, requires_full_event_info
C         We only want to bias distributions, but not impact the xsec. 
          data impact_xsec/.False./
C         Of course this module does not require the full event
C         information (color, resonances, helicities, etc..)
          data requires_full_event_info/.False./
          common/bias/stored_bias_weight,impact_xsec,
     &                 requires_full_event_info
C
C Accessingt the details of the event
C
          logical is_a_j(nexternal),is_a_l(nexternal),
     &            is_a_b(nexternal),is_a_a(nexternal),
     &            is_a_onium(nexternal),is_a_nu(nexternal),
     &            is_heavy(nexternal),do_cuts(nexternal)
          common/to_specisa/is_a_j,is_a_a,is_a_l,is_a_b,is_a_nu,
     &                     is_heavy,is_a_onium,do_cuts
C
C     Setup the value of the parameters from the run_card    
C
          include '../bias.inc'

C --------------------
C BEGIN IMPLEMENTATION
C --------------------
          
          bias_weight = 1.0d0
          mtt = 0d0
          pTot = (/ 0d0, 0d0, 0d0, 0d0 /)
          do i=1,nexternal
              if (is_heavy(i)) then
              ! if (abs(idup(i,1,1)).eq.6) then
                  do j =0,3
                      pTot(j) = pTot(j)+p(j,i)
                  enddo 
              endif
          enddo

          mtt_sq = pTot(0)**2 - pTot(1)**2 - pTot(2)**2 - pTot(3)**2
          mtt = dsqrt(max(0d0, mtt_sq))

          if (mtt .gt. 0.0d0) then

c             Calculate the normalization offset using the first polynomial
              p_offset = -5.2343d-06*mtt_bias_offset**2
              p_offset = p_offset + 4.8039d-03*mtt_bias_offset
              p_offset = p_offset - 9.6050d+00
              p_offset = -p_offset
    
c             Pre-calculate the function values at each boundary
              p1_at_b1 = -5.2343d-06*bound_1**2 + 4.8039d-03*bound_1
              p1_at_b1 = p1_at_b1 - 9.6050d+00
              p1_at_b1 = -p1_at_b1
              
              p2_at_b1 = 2.3075d-07*bound_1**2 - 3.2071d-03*bound_1
              p2_at_b1 = p2_at_b1 - 6.7484d+00
              p2_at_b1 = -p2_at_b1
    
              p2_at_b2 = 2.3075d-07*bound_2**2 - 3.2071d-03*bound_2
              p2_at_b2 = p2_at_b2 - 6.7484d+00
              p2_at_b2 = -p2_at_b2
              
              p3_at_b2 = -1.8103d-06*bound_2**2 + 1.0095d-02*bound_2
              p3_at_b2 = p3_at_b2 - 2.8543d+01
              p3_at_b2 = -p3_at_b2
    
              p3_at_b3 = -1.8103d-06*bound_3**2 + 1.0095d-02*bound_3
              p3_at_b3 = p3_at_b3 - 2.8543d+01
              p3_at_b3 = -p3_at_b3
              
              p4_at_b3 = -4.0161d-06*bound_3**2 + 2.9753d-02*bound_3
              p4_at_b3 = p4_at_b3 - 7.0828d+01
              p4_at_b3 = -p4_at_b3
    
              p4_at_b4 = -4.0161d-06*bound_4**2 + 2.9753d-02*bound_4
              p4_at_b4 = p4_at_b4 - 7.0828d+01
              p4_at_b4 = -p4_at_b4
              
              p5_at_b4 = 1.5342d-05*bound_4**2 - 1.3286d-01*bound_4
              p5_at_b4 = p5_at_b4 + 2.7059d+02
              p5_at_b4 = -p5_at_b4
    
              p5_at_b5 = 1.5342d-05*bound_5**2 - 1.3286d-01*bound_5
              p5_at_b5 = p5_at_b5 + 2.7059d+02
              p5_at_b5 = -p5_at_b5
              
              p6_at_b5 = 8.1272d-07*bound_5**2 - 1.0905d-02*bound_5
              p6_at_b5 = p6_at_b5 + 1.5564d+01
              p6_at_b5 = -p6_at_b5

              if (mtt .lt. bound_1) then
c                 --- REGION 1 ---
                  p_val = -5.2343d-06*mtt**2 + 4.8039d-03*mtt 
     &                 - 9.6050d+00
                  p_val = -p_val
                  final_arg = p_val - p_offset

              else if (mtt .lt. bound_2) then
c                 --- REGION 2 ---
                  p_val = 2.3075d-07*mtt**2 - 3.2071d-03*mtt 
     &                 - 6.7484d+00
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1)
                  final_arg = p_val + stitch_sum - p_offset
        
              else if (mtt .lt. bound_3) then
c                 --- REGION 3 ---
                  p_val = -1.8103d-06*mtt**2 + 1.0095d-02*mtt 
     &                 - 2.8543d+01
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  final_arg = p_val + stitch_sum - p_offset

              else if (mtt .lt. bound_4) then
c                 --- REGION 4 ---
                  p_val = -4.0161d-06*mtt**2 + 2.9753d-02*mtt 
     &                 - 7.0828d+01
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  final_arg = p_val + stitch_sum - p_offset
        
              else if (mtt .lt. bound_5) then
c                 --- REGION 5 ---
                  p_val = 1.5342d-05*mtt**2 - 1.3286d-01*mtt 
     &                 + 2.7059d+02
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  stitch_sum = stitch_sum + (p4_at_b4 - p5_at_b4)
                  final_arg = p_val + stitch_sum - p_offset
      
              else
c                 --- REGION 6 ---
                  p_val = 8.1272d-07*mtt**2 - 1.0905d-02*mtt 
     &                 + 1.5564d+01
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  stitch_sum = stitch_sum + (p4_at_b4 - p5_at_b4)
                  stitch_sum = stitch_sum + (p5_at_b5 - p6_at_b5)
                  final_arg = p_val + stitch_sum - p_offset
              endif
c             Calculate the final bias_weight on its own line
              bias_weight = EXP(final_arg)
          endif

          return
      end subroutine bias_wgt
