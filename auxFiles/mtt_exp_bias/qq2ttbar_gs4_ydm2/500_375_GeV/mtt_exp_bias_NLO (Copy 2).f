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
          double precision, parameter :: bound_2 = 1050.0d0
          double precision, parameter :: bound_3 = 1400.0d0
          double precision, parameter :: bound_4 = 1700.0d0
          double precision, parameter :: bound_5 = 2650.0d0
          double precision, parameter :: bound_6 = 4500.0d0

          double precision, parameter :: mtt_norm = 2000.0d0
      
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
              p_offset = 2.0610d-06*mtt_norm**2
              p_offset = p_offset - 6.2254d-03*mtt_norm
              p_offset = p_offset - 2.0355d+00
              p_offset = -p_offset
    
c             Pre-calculate the function values at each boundary
              p1_at_b1 = 2.0610d-06*bound_1**2 - 6.2254d-03*bound_1
              p1_at_b1 = p1_at_b1 - 2.0355d+00
              p1_at_b1 = -p1_at_b1
              
              p2_at_b1 = 1.1971d-05*bound_1**2 - 2.2037d-02*bound_1
              p2_at_b1 = p2_at_b1 + 4.3060d+00
              p2_at_b1 = -p2_at_b1
    
              p2_at_b2 = 1.1971d-05*bound_2**2 - 2.2037d-02*bound_2
              p2_at_b2 = p2_at_b2 + 4.3060d+00
              p2_at_b2 = -p2_at_b2
              
              p3_at_b2 = -4.8872d-06*bound_2**2 + 2.2192d-03*bound_2
              p3_at_b2 = p3_at_b2 - 2.9131d+00
              p3_at_b2 = -p3_at_b2
    
              p3_at_b3 = -4.8872d-06*bound_3**2 + 2.2192d-03*bound_3
              p3_at_b3 = p3_at_b3 - 2.9131d+00
              p3_at_b3 = -p3_at_b3
              
              p4_at_b3 = 7.0646d-05*bound_3**2 - 2.1843d-01*bound_3
              p4_at_b3 = p4_at_b3 + 1.5563d+02
              p4_at_b3 = -p4_at_b3
    
              p4_at_b4 = 7.0646d-05*bound_4**2 - 2.1843d-01*bound_4
              p4_at_b4 = p4_at_b4 + 1.5563d+02
              p4_at_b4 = -p4_at_b4
              
              p5_at_b4 = -1.4029d-06*bound_4**2 + 2.5234d-03*bound_4
              p5_at_b4 = p5_at_b4 - 1.7980d+01
              p5_at_b4 = -p5_at_b4
    
              p5_at_b5 = -1.4029d-06*bound_5**2 + 2.5234d-03*bound_5
              p5_at_b5 = p5_at_b5 - 1.7980d+01
              p5_at_b5 = -p5_at_b5
              
              p6_at_b5 = 7.6171d-08*bound_5**2 - 3.4801d-03*bound_5
              p6_at_b5 = p6_at_b5 - 6.4077d+00
              p6_at_b5 = -p6_at_b5

              p6_at_b6 = 7.6171d-08*bound_6**2 - 3.4801d-03*bound_6
              p6_at_b6 = p6_at_b6 - 6.4077d+00
              p6_at_b6 = -p6_at_b6

              p7_at_b6 = -1.7964d-07*bound_6**2 - 4.3487d-04*bound_6
              p7_at_b6 = p7_at_b6 - 1.0989d+01
              p7_at_b6 = -p7_at_b6

              if (mtt .lt. bound_1) then
c                 --- REGION 1 ---
                  p_val = 2.0610d-06*mtt**2 - 6.2254d-03*mtt 
     &                 - 2.0355d+00
                  p_val = -p_val
                  final_arg = p_val - p_offset

              else if (mtt .lt. bound_2) then
c                 --- REGION 2 ---
                  p_val = 1.1971d-05*mtt**2 - 2.2037d-02*mtt 
     &                 + 4.3060d+00
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1)
                  final_arg = p_val + stitch_sum - p_offset
        
              else if (mtt .lt. bound_3) then
c                 --- REGION 3 ---
                  p_val = -4.8872d-06*mtt**2 + 2.2192d-03*mtt 
     &                 - 2.9131d+00
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  final_arg = p_val + stitch_sum - p_offset

              else if (mtt .lt. bound_4) then
c                 --- REGION 4 ---
                  p_val = 7.0646d-05*mtt**2 - 2.1843d-01*mtt 
     &                 + 1.5563d+02
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  final_arg = p_val + stitch_sum - p_offset
        
              else if (mtt .lt. bound_5) then
c                 --- REGION 5 ---
                  p_val = -1.4029d-06*mtt**2 + 2.5234d-03*mtt 
     &                 - 1.7980d+01
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  stitch_sum = stitch_sum + (p4_at_b4 - p5_at_b4)
                  final_arg = p_val + stitch_sum - p_offset
      
              else if (mtt .lt. bound_6) then
c                 --- REGION 6 ---
                  p_val = 7.6171d-08*mtt**2 - 3.4801d-03*mtt 
     &                 - 6.4077d+00
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  stitch_sum = stitch_sum + (p4_at_b4 - p5_at_b4)
                  stitch_sum = stitch_sum + (p5_at_b5 - p6_at_b5)
                  final_arg = p_val + stitch_sum - p_offset
              
              else
c                 --- REGION 7 ---
                  mtt = min(4700.0d0, mtt)
                  p_val = -1.7964d-07*mtt**2 - 4.3487d-04*mtt 
     &                 - 1.0989d+01
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
