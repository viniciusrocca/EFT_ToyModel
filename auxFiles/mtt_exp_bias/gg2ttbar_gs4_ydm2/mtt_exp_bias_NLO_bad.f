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
          
C --- Dynamic Variables ---
          double precision peak_loc, dip_loc
          double precision bound_1, bound_2, bound_3, bound_4
          double precision mtt_norm, mtt_shifted
          double precision ref_peak, ref_dip


C     Peak = 2.05 * 1500 = 3075.0
C     Dip  = 2.75 * 1500 + 0.5 * 1425 + 12.5 = 4850.0
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
              dip_loc = 2.75d0 * mdl_mpsit + 0.5d0 * mdl_msdm + 12.5d0

C            
C             We map the bounds from the 1500 GeV reference case to the current mass.
C             Reference Bounds were: 1900, 3000, 4800, 6200
C             Ref Peak = 3075. Ref Dip = 4850.
C
C             B1 (1900) is Peak - 1175
C             B2 (3000) is Peak - 75
C             B3 (4800) is Dip - 50
C             B4 (6200) is Dip + 1350

              bound_1 = peak_loc - 1175.0d0
              bound_2 = peak_loc - 75.0d0
              bound_3 = dip_loc - 50.0d0
              bound_4 = dip_loc + 1350.0d0
              
C             Normalization at an arbitrary low mass point relative to peak
              mtt_norm = peak_loc - 2000.0d0
              if (mtt_norm .lt. 0.0d0) mtt_norm = 500.0d0


C             Shift current mtt so the Dip aligns with the Reference Dip
              mtt_shifted = mtt - (dip_loc - ref_dip)



c             Normalization (Region 1)
C             We evaluate this at the shifted normalization point
              p_offset = 9.7271d-07*(mtt_norm-(dip_loc-ref_dip))**2
              p_offset = p_offset - 7.8786d-03*(mtt_norm-(dip_loc-ref_dip))
              p_offset = p_offset - 2.4171d+00
              p_offset = -p_offset
    
c             Stitch Region 1 -> 2 (at 1900)
              p1_at_b1 = 9.7271d-07*1900.0d0**2 - 7.8786d-03*1900.0d0
              p1_at_b1 = p1_at_b1 - 2.4171d+00
              p1_at_b1 = -p1_at_b1
              
              p2_at_b1 = 8.2416d-06*1900.0d0**2 - 4.3273d-02*1900.0d0
              p2_at_b1 = p2_at_b1 + 3.8591d+01
              p2_at_b1 = -p2_at_b1
    
c             Stitch Region 2 -> 3 (at 3000)
              p2_at_b2 = 8.2416d-06*3000.0d0**2 - 4.3273d-02*3000.0d0
              p2_at_b2 = p2_at_b2 + 3.8591d+01
              p2_at_b2 = -p2_at_b2
              
              p3_at_b2 = -2.4915d-07*3000.0d0**2 - 8.3352d-04*3000.0d0
              p3_at_b2 = p3_at_b2 - 1.2091d+01
              p3_at_b2 = -p3_at_b2
    
c             Stitch Region 3 -> 4 (at 4800)
              p3_at_b3 = -2.4915d-07*4800.0d0**2 - 8.3352d-04*4800.0d0
              p3_at_b3 = p3_at_b3 - 1.2091d+01
              p3_at_b3 = -p3_at_b3
              
              p4_at_b3 = 2.0285d-06*4800.0d0**2 - 2.4944d-02*4800.0d0
              p4_at_b3 = p4_at_b3 + 4.7438d+01
              p4_at_b3 = -p4_at_b3
    
c             Stitch Region 4 -> 5 (at 6200)
              p4_at_b4 = 2.0285d-06*6200.0d0**2 - 2.4944d-02*6200.0d0
              p4_at_b4 = p4_at_b4 + 4.7438d+01
              p4_at_b4 = -p4_at_b4
              
              p5_at_b4 = 1.4288d-05*6200.0d0**2 - 2.0376d-01*6200.0d0
              p5_at_b4 = p5_at_b4 + 6.8577d+02
              p5_at_b4 = -p5_at_b4




              if (mtt_shifted .lt. 1900.0d0) then
c                 --- REGION 1 ---
                  p_val = 9.7271d-07*mtt_shifted**2 
     &                 - 7.8786d-03*mtt_shifted 
     &                 - 2.4171d+00
                  p_val = -p_val
                  final_arg = p_val - p_offset

              else if (mtt_shifted .lt. 3000.0d0) then
c                 --- REGION 2 ---
                  p_val = 8.2416d-06*mtt_shifted**2 
     &                 - 4.3273d-02*mtt_shifted 
     &                 + 3.8591d+01
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1)
                  final_arg = p_val + stitch_sum - p_offset
        
              else if (mtt_shifted .lt. 4800.0d0) then
c                 --- REGION 3 ---
                  p_val = -2.4915d-07*mtt_shifted**2 
     &                 - 8.3352d-04*mtt_shifted 
     &                 - 1.2091d+01
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  final_arg = p_val + stitch_sum - p_offset

              else if (mtt_shifted .lt. 6200.0d0) then
c                 --- REGION 4 ---
                  p_val = 2.0285d-06*mtt_shifted**2 
     &                 - 2.4944d-02*mtt_shifted 
     &                 + 4.7438d+01
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  final_arg = p_val + stitch_sum - p_offset
        
              else
c                 --- REGION 5 ---
                  mtt_shifted = min(3500.0d0, mtt_shifted)
                  p_val = 1.4288d-05*mtt_shifted**2 
     &                 - 2.0376d-01*mtt_shifted 
     &                 + 6.8577d+02
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
