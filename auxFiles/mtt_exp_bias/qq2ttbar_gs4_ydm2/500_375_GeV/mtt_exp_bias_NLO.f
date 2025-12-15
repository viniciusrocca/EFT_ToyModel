subroutine bias_weight_function(p,ipdg,bias_wgt)
          implicit none
          include 'nexternal.inc'
          include '../MODEL/input.inc' 

          double precision bias_wgt,p(0:3,nexternal),H_T
          integer ipdg(nexternal),i,j
          double precision pTot(0:3)
          double precision mtt, mtt_sq

C --- Local Calculation Variables ---
          double precision p_val, p_offset, final_arg
          double precision stitch_sum
          
C --- Dynamic Boundary Variables ---
          double precision peak_loc, dip_loc
          double precision bound_1, bound_2, bound_3, bound_4, bound_5, bound_6
          double precision mtt_norm

C --- Relative Coordinates (for shifting the shape) ---
          double precision m_rel
          
          
          bias_wgt=1d0
          mtt = 0d0
          pTot = (/ 0d0, 0d0, 0d0, 0d0 /)
          do i=1,nexternal
              if (abs(ipdg(i)).eq.6) then
                  do j =0,3
                      pTot(j) = pTot(j)+p(j,i)
                  enddo 
              endif
          enddo

          mtt_sq = pTot(0)**2 - pTot(1)**2 - pTot(2)**2 - pTot(3)**2
          mtt = dsqrt(max(0d0, mtt_sq))

          if (mtt .gt. 0.0d0) then

C             Peak Location: 2.05 * mPsiT
              peak_loc = 2.05d0 * mdl_mpsit
              
C             Dip Location: 2.6 * mPsiT + 0.5 * mS + 37.5
              dip_loc = 2.6d0 * mdl_mpsit + 0.5d0 * mdl_msdm + 37.5d0
              
C             Define Boundaries relative to these features.
C             These offsets are estimates based on the "shape" of the regions 
C             relative to the peak/dip in your fitted examples.
C             R1 ends before peak. R2 contains peak. R3 is valley slope.
C             R4 contains Dip. R5 is recovery.
              
              bound_1 = peak_loc - 150.0d0   ! Just before the peak
              bound_2 = peak_loc + 300.0d0   ! After the peak, start of valley
              bound_3 = dip_loc - 150.0d0    ! Entering the dip
              bound_4 = dip_loc + 150.0d0    ! Exiting the dip
              bound_5 = dip_loc + 1000.0d0   ! Recovery region
              bound_6 = dip_loc + 3000.0d0   ! High mass tail
              
              mtt_norm = 1000.0d0

C   
c             --- Calculate Normalization Offset ---
              p_offset = 5.1229d-06*mtt_norm**2
              p_offset = p_offset - 9.9891d-03*mtt_norm
              p_offset = p_offset - 9.2937d-01
              p_offset = -p_offset
              

              
              p1_at_b1 = 5.1229d-06*bound_1**2 - 9.9891d-03*bound_1
              p1_at_b1 = p1_at_b1 - 9.2937d-01
              p1_at_b1 = -p1_at_b1
              
              p2_at_b1 = -4.8872d-06*bound_1**2 + 2.2192d-03*bound_1
              p2_at_b1 = p2_at_b1 - 2.9131d+00
              p2_at_b1 = -p2_at_b1
    
              p2_at_b2 = -4.8872d-06*bound_2**2 + 2.2192d-03*bound_2
              p2_at_b2 = p2_at_b2 - 2.9131d+00
              p2_at_b2 = -p2_at_b2
              
              p3_at_b2 = 7.7710d-05*bound_2**2 - 2.4027d-01*bound_2
              p3_at_b2 = p3_at_b2 + 1.7239d+02
              p3_at_b2 = -p3_at_b2
    
              p3_at_b3 = 7.7710d-05*bound_3**2 - 2.4027d-01*bound_3
              p3_at_b3 = p3_at_b3 + 1.7239d+02
              p3_at_b3 = -p3_at_b3
              
              p4_at_b3 = -1.4430d-06*bound_3**2 + 2.5955d-03*bound_3
              p4_at_b3 = p4_at_b3 - 1.8494d+01
              p4_at_b3 = -p4_at_b3
    
              p4_at_b4 = -1.4430d-06*bound_4**2 + 2.5955d-03*bound_4
              p4_at_b4 = p4_at_b4 - 1.8494d+01
              p4_at_b4 = -p4_at_b4
              
              p5_at_b4 = 9.1405d-08*bound_4**2 - 4.1761d-03*bound_4
              p5_at_b4 = p5_at_b4 - 7.6892d+00
              p5_at_b4 = -p5_at_b4
    
              p5_at_b5 = 9.1405d-08*bound_5**2 - 4.1761d-03*bound_5
              p5_at_b5 = p5_at_b5 - 7.6892d+00
              p5_at_b5 = -p5_at_b5
              
              p6_at_b5 = -1.7964d-07*bound_5**2 - 4.3487d-04*bound_5
              p6_at_b5 = p6_at_b5 - 1.0989d+01
              p6_at_b5 = -p6_at_b5

              if (mtt .lt. bound_1) then
c                 --- REGION 1  ---
                  p_val = 5.1229d-06*mtt**2 - 9.9891d-03*mtt 
     &                 - 9.2937d-01
                  p_val = -p_val
                  final_arg = p_val - p_offset

              else if (mtt .lt. bound_2) then
c                 --- REGION 2  ---
                  p_val = -4.8872d-06*mtt**2 + 2.2192d-03*mtt 
     &                 - 2.9131d+00
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1)
                  final_arg = p_val + stitch_sum - p_offset
        
              else if (mtt .lt. bound_3) then
c                 --- REGION 3  ---
                  p_val = 7.7710d-05*mtt**2 - 2.4027d-01*mtt 
     &                 + 1.7239d+02
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  final_arg = p_val + stitch_sum - p_offset

              else if (mtt .lt. bound_4) then
c                 --- REGION 4  ---
                  p_val = -1.4430d-06*mtt**2 + 2.5955d-03*mtt 
     &                 - 1.8494d+01
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  final_arg = p_val + stitch_sum - p_offset
        
              else if (mtt .lt. bound_5) then
c                 --- REGION 5  ---
                  p_val = 9.1405d-08*mtt**2 - 4.1761d-03*mtt 
     &                 - 7.6892d+00
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  stitch_sum = stitch_sum + (p4_at_b4 - p5_at_b4)
                  final_arg = p_val + stitch_sum - p_offset
      
              else
c                 --- REGION 6  ---
                  mtt = min(dip_loc + 350.0d0, mtt)
                  p_val = -1.7964d-07*mtt**2 - 4.3487d-04*mtt 
     &                 - 1.0989d+01
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  stitch_sum = stitch_sum + (p4_at_b4 - p5_at_b4)
                  stitch_sum = stitch_sum + (p5_at_b5 - p6_at_b5)
                  final_arg = p_val + stitch_sum - p_offset
              endif
              
              bias_wgt = EXP(final_arg)
          endif

          return
      end
