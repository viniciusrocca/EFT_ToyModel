subroutine bias_weight_function(p,ipdg,bias_wgt)
          implicit none
          include 'nexternal.inc'
          double precision bias_wgt,p(0:3,nexternal),H_T
          integer ipdg(nexternal),i,j
          double precision pTot(0:3)
          double precision mtt, mtt_sq

C --- Local Calculation Variables ---
          double precision p_val, p_offset, final_arg
          double precision stitch_sum
          double precision p1_at_b1, p2_at_b1, p2_at_b2, p3_at_b2
          double precision p3_at_b3, p4_at_b3, p4_at_b4, p5_at_b4
          double precision p5_at_b5, p6_at_b5, p6_at_b6, p7_at_b6

C --- Boundary and Normalization Parameters ---
          double precision, parameter :: bound_1 = 800.0d0
          double precision, parameter :: bound_2 = 1100.0d0
          double precision, parameter :: bound_3 = 1400.0d0
          double precision, parameter :: bound_4 = 1550.0d0
          double precision, parameter :: bound_5 = 1850.0d0
          double precision, parameter :: bound_6 = 2450.0d0

          double precision, parameter :: mtt_norm = 1100.0d0
      
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

          mtt_sq = pTot(0)**2 - pTot(1)**2 - pTot(2)**2 - pTot(3)**2
          mtt = dsqrt(max(0d0, mtt_sq))

          if (mtt .gt. 0.0d0) then

c             Calculate the normalization offset using the first polynomial
              p_offset = 1.5965d-06*mtt_norm**2
              p_offset = p_offset - 5.8118d-03*mtt_norm
              p_offset = p_offset + 1.5179d+01
              p_offset = -p_offset
    
c             Pre-calculate the function values at each boundary
              p1_at_b1 = 1.5965d-06*bound_1**2 - 5.8118d-03*bound_1
              p1_at_b1 = p1_at_b1 + 1.5179d+01
              p1_at_b1 = -p1_at_b1
              
              p2_at_b1 = -3.9932d-06*bound_1**2 + 4.3928d-03*bound_1
              p2_at_b1 = p2_at_b1 + 1.0622d+01
              p2_at_b1 = -p2_at_b1
    
              p2_at_b2 = -3.9932d-06*bound_2**2 + 4.3928d-03*bound_2
              p2_at_b2 = p2_at_b2 + 1.0622d+01
              p2_at_b2 = -p2_at_b2
              
              p3_at_b2 = 9.5163d-06*bound_2**2 - 2.6903d-02*bound_2
              p3_at_b2 = p3_at_b2 + 2.8394d+01
              p3_at_b2 = -p3_at_b2
    
              p3_at_b3 = 9.5163d-06*bound_3**2 - 2.6903d-02*bound_3
              p3_at_b3 = p3_at_b3 + 2.8394d+01
              p3_at_b3 = -p3_at_b3
              
              p4_at_b3 = 5.3077d-05*bound_3**2 - 1.6076d-01*bound_3
              p4_at_b3 = p4_at_b3 + 1.3032d+02
              p4_at_b3 = -p4_at_b3
    
              p4_at_b4 = 5.3077d-05*bound_4**2 - 1.6076d-01*bound_4
              p4_at_b4 = p4_at_b4 + 1.3032d+02
              p4_at_b4 = -p4_at_b4
              
              p5_at_b4 = 1.9278d-08*bound_4**2 - 1.9049d-03*bound_4
              p5_at_b4 = p5_at_b4 + 1.1451d+01
              p5_at_b4 = -p5_at_b4
    
              p5_at_b5 = 1.9278d-08*bound_5**2 - 1.9049d-03*bound_5
              p5_at_b5 = p5_at_b5 + 1.1451d+01
              p5_at_b5 = -p5_at_b5
              
              p6_at_b5 = -1.0516d-06*bound_5**2 + 3.4260d-03*bound_5
              p6_at_b5 = p6_at_b5 + 5.0720d+00
              p6_at_b5 = -p6_at_b5

              p6_at_b6 = -1.0516d-06*bound_6**2 + 3.4260d-03*bound_6
              p6_at_b6 = p6_at_b6 + 5.0720d+00
              p6_at_b6 = -p6_at_b6

              p7_at_b6 = -2.6415d-08*bound_6**2 - 9.0908d-04*bound_6
              p7_at_b6 = p7_at_b6 + 9.4124d+00
              p7_at_b6 = -p7_at_b6

              if (mtt .lt. bound_1) then
c                 --- REGION 1 ---
                  p_val = 1.5965d-06*mtt**2 - 5.8118d-03*mtt 
     &                 + 1.5179d+01
                  p_val = -p_val
                  final_arg = p_val - p_offset

              else if (mtt .lt. bound_2) then
c                 --- REGION 2 ---
                  p_val = -3.9932d-06*mtt**2 + 4.3928d-03*mtt 
     &                 + 1.0622d+01
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1)
                  final_arg = p_val + stitch_sum - p_offset
        
              else if (mtt .lt. bound_3) then
c                 --- REGION 3 ---
                  p_val = 9.5163d-06*mtt**2 - 2.6903d-02*mtt 
     &                 + 2.8394d+01
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  final_arg = p_val + stitch_sum - p_offset

              else if (mtt .lt. bound_4) then
c                 --- REGION 4 ---
                  p_val = 5.3077d-05*mtt**2 - 1.6076d-01*mtt 
     &                 + 1.3032d+02
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  final_arg = p_val + stitch_sum - p_offset
        
              else if (mtt .lt. bound_5) then
c                 --- REGION 5 ---
                  p_val = 1.9278d-08*mtt**2 - 1.9049d-03*mtt 
     &                 + 1.1451d+01
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  stitch_sum = stitch_sum + (p4_at_b4 - p5_at_b4)
                  final_arg = p_val + stitch_sum - p_offset
      
              else if (mtt .lt. bound_6) then
c                 --- REGION 6 ---
                  p_val = -1.0516d-06*mtt**2 + 3.4260d-03*mtt 
     &                 + 5.0720d+00
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  stitch_sum = stitch_sum + (p4_at_b4 - p5_at_b4)
                  stitch_sum = stitch_sum + (p5_at_b5 - p6_at_b5)
                  final_arg = p_val + stitch_sum - p_offset
              
              else
c                 --- REGION 7 ---
                  mtt = min(4500.0d0, mtt)
                  p_val = -2.6415d-08*mtt**2 - 9.0908d-04*mtt 
     &                 + 9.4124d+00
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

          return
      end
