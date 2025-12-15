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
          double precision p1_at_b1, p2_at_b1, p2_at_b2, p3_at_b2
          double precision p3_at_b3, p4_at_b3, p4_at_b4, p5_at_b4
          double precision p5_at_b5, p6_at_b5, p6_at_b6, p7_at_b6
          
C --- Dynamic Variables ---
          double precision peak_loc, dip_loc
          double precision bound_1, bound_2, bound_3, bound_4, bound_5, bound_6
          double precision mtt_norm, mtt_shifted
          double precision ref_peak, ref_dip

C     Peak = 2.05 * mdl_mpsit 
C     Dip  = 2.6d0 * mdl_mpsit + 0.5d0 * mdl_msdm + 37.5d0
          parameter (ref_peak = 3075.0d0)
          parameter (ref_dip  = 4850.0d0)
      
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


              peak_loc = 2.05d0 * mdl_mpsit
              dip_loc = 2.6d0 * mdl_mpsit + 0.5d0 * mdl_msdm + 37.5d0


C             -----------------------------------------
C             We map the bounds from the 1500 GeV reference case to the current mass.
C             Reference Bounds: 900, 1450, 1700, 2000, 4500
C             Note: The 1500 GeV fit boundaries are quite far from the dip/peak 
C             compared to the 500 GeV case because the features are much wider.
C             
C             Mapping strategy: Anchor bounds relative to the dip location,
C             as the dip is the most critical feature for the bias.
C             
C             Ref Dip = 4850.
C             B1 (900)  is Dip - 3950 (Far left tail)
C             B2 (1450) is Dip - 3400
C             B3 (1700) is Dip - 3150
C             B4 (2000) is Dip - 2850
C             B5 (4500) is Dip - 350

              bound_1 = dip_loc - 3950.0d0
              bound_2 = dip_loc - 3400.0d0
              bound_3 = dip_loc - 3150.0d0
              bound_4 = dip_loc - 2850.0d0
              bound_5 = dip_loc - 350.0d0
              
C             Normalization at an arbitrary low mass point
              mtt_norm = bound_1 - 100.0d0
              if (mtt_norm .lt. 0.0d0) mtt_norm = 500.0d0


C             Shift current mtt so the Dip aligns with the Reference Dip
              mtt_shifted = mtt - (dip_loc - ref_dip)




c             Normalization (Region 1)
C             We evaluate this at the shifted normalization point
              p_offset = 2.8824d-06*(mtt_norm-(dip_loc-ref_dip))**2
              p_offset = p_offset - 9.0035d-03*(mtt_norm-(dip_loc-ref_dip))
              p_offset = p_offset - 4.6684d-01
              p_offset = -p_offset
    
c             Stitch Region 1 -> 2 (at 900)
              p1_at_b1 = 2.8824d-06*900.0d0**2 - 9.0035d-03*900.0d0
              p1_at_b1 = p1_at_b1 - 4.6684d-01
              p1_at_b1 = -p1_at_b1
              
              p2_at_b1 = -9.3391d-06*900.0d0**2 + 1.4870d-02*900.0d0
              p2_at_b1 = p2_at_b1 - 1.1884d+01
              p2_at_b1 = -p2_at_b1
    
c             Stitch Region 2 -> 3 (at 1450)
              p2_at_b2 = -9.3391d-06*1450.0d0**2 + 1.4870d-02*1450.0d0
              p2_at_b2 = p2_at_b2 - 1.1884d+01
              p2_at_b2 = -p2_at_b2
              
              p3_at_b2 = 2.7732d-04*1450.0d0**2 - 8.7849d-01*1450.0d0
              p3_at_b2 = p3_at_b2 + 6.7964d+02
              p3_at_b2 = -p3_at_b2
    
c             Stitch Region 3 -> 4 (at 1700)
              p3_at_b3 = 2.7732d-04*1700.0d0**2 - 8.7849d-01*1700.0d0
              p3_at_b3 = p3_at_b3 + 6.7964d+02
              p3_at_b3 = -p3_at_b3
              
              p4_at_b3 = -1.1147d-05*1700.0d0**2 + 4.0184d-02*1700.0d0
              p4_at_b3 = p4_at_b3 - 6.1547d+01
              p4_at_b3 = -p4_at_b3
    
c             Stitch Region 4 -> 5 (at 2000)
              p4_at_b4 = -1.1147d-05*2000.0d0**2 + 4.0184d-02*2000.0d0
              p4_at_b4 = p4_at_b4 - 6.1547d+01
              p4_at_b4 = -p4_at_b4
              
              p5_at_b4 = -1.8082d-08*2000.0d0**2 - 3.4268d-03*2000.0d0
              p5_at_b4 = p5_at_b4 - 1.5324d+01
              p5_at_b4 = -p5_at_b4




              if (mtt_shifted .lt. 900.0d0) then
c                 --- REGION 1 ---
                  p_val = 2.8824d-06*mtt_shifted**2 
     &                 - 9.0035d-03*mtt_shifted 
     &                 - 4.6684d-01
                  p_val = -p_val
                  final_arg = p_val - p_offset

              else if (mtt_shifted .lt. 1450.0d0) then
c                 --- REGION 2 ---
                  p_val = -9.3391d-06*mtt_shifted**2 
     &                 + 1.4870d-02*mtt_shifted 
     &                 - 1.1884d+01
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1)
                  final_arg = p_val + stitch_sum - p_offset
        
              else if (mtt_shifted .lt. 1700.0d0) then
c                 --- REGION 3 ---
                  p_val = 2.7732d-04*mtt_shifted**2 
     &                 - 8.7849d-01*mtt_shifted 
     &                 + 6.7964d+02
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  final_arg = p_val + stitch_sum - p_offset

              else if (mtt_shifted .lt. 2000.0d0) then
c                 --- REGION 4 ---
                  p_val = -1.1147d-05*mtt_shifted**2 
     &                 + 4.0184d-02*mtt_shifted 
     &                 - 6.1547d+01
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  final_arg = p_val + stitch_sum - p_offset
        
              else
c                 --- REGION 5 ---
                  mtt_shifted = min(3500.0d0, mtt_shifted)
                  p_val = -1.8082d-08*mtt_shifted**2 
     &                 - 3.4268d-03*mtt_shifted 
     &                 - 1.5324d+01
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  stitch_sum = stitch_sum + (p4_at_b4 - p5_at_b4)
                  final_arg = p_val + stitch_sum - p_offset
      
              endif
c             Calculate the final bias_weight on its own line
              bias_wgt = EXP(final_arg)
          endif

          return
      end
