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
          double precision bound_1, bound_2, bound_3, bound_4, bound_5
          double precision mtt_norm

C --- Stitching Variables ---
          double precision p1_at_b1, p2_at_b1, p2_at_b2, p3_at_b2
          double precision p3_at_b3, p4_at_b3, p4_at_b4, p5_at_b4
          double precision p5_at_b5, p6_at_b5
      
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

C             
C             Peak Location: 2.05 * mPsiT
              peak_loc = 2.05d0 * mdl_mpsit
              
C             Dip Location: 2.75 * mPsiT + 0.5 * mS + 12.5
              dip_loc = 2.75d0 * mdl_mpsit + 0.5d0 * mdl_msdm + 12.5d0
              

              bound_1 = peak_loc - 125.0d0
              bound_2 = dip_loc - 25.0d0
              bound_3 = dip_loc + 125.0d0
              bound_4 = dip_loc + 425.0d0
              bound_5 = dip_loc + 1925.0d0 

              mtt_norm = 1000.0

              
c             Normalization Offset (Region 1 Polynomial)
              p_offset = 2.8824d-06*mtt_norm**2
              p_offset = p_offset - 9.0035d-03*mtt_norm
              p_offset = p_offset - 4.6684d-01
              p_offset = -p_offset
    
c             Stitch Region 1 -> 2
              p1_at_b1 = 2.8824d-06*bound_1**2 - 9.0035d-03*bound_1
              p1_at_b1 = p1_at_b1 - 4.6684d-01
              p1_at_b1 = -p1_at_b1
              
              p2_at_b1 = -9.3391d-06*bound_1**2 + 1.4870d-02*bound_1
              p2_at_b1 = p2_at_b1 - 1.1884d+01
              p2_at_b1 = -p2_at_b1
    
c             Stitch Region 2 -> 3
              p2_at_b2 = -9.3391d-06*bound_2**2 + 1.4870d-02*bound_2
              p2_at_b2 = p2_at_b2 - 1.1884d+01
              p2_at_b2 = -p2_at_b2
              
              p3_at_b2 = 2.4114d-04*bound_2**2 - 7.6391d-01*bound_2
              p3_at_b2 = p3_at_b2 + 5.9023d+02
              p3_at_b2 = -p3_at_b2
    
c             Stitch Region 3 -> 4
              p3_at_b3 = 2.4114d-04*bound_3**2 - 7.6391d-01*bound_3
              p3_at_b3 = p3_at_b3 + 5.9023d+02
              p3_at_b3 = -p3_at_b3
              
              p4_at_b3 = -6.5570d-06*bound_3**2 + 2.3638d-02*bound_3
              p4_at_b3 = p4_at_b3 - 3.3663d+01
              p4_at_b3 = -p4_at_b3
    
c             Stitch Region 4 -> 5
              p4_at_b4 = -6.5570d-06*bound_4**2 + 2.3638d-02*bound_4
              p4_at_b4 = p4_at_b4 - 3.3663d+01
              p4_at_b4 = -p4_at_b4
              
              p5_at_b4 = -1.3595d-08*bound_4**2 - 2.5766d-03*bound_4
              p5_at_b4 = p5_at_b4 - 7.2827d+00
              p5_at_b4 = -p5_at_b4
    

              if (mtt .lt. bound_1) then
c                 --- REGION 1 ---
                  p_val = 2.8824d-06*mtt**2 - 9.0035d-03*mtt 
     &                 - 4.6684d-01
                  p_val = -p_val
                  final_arg = p_val - p_offset

              else if (mtt .lt. bound_2) then
c                 --- REGION 2 ---
                  p_val = -9.3391d-06*mtt**2 + 1.4870d-02*mtt 
     &                 - 1.1884d+01
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1)
                  final_arg = p_val + stitch_sum - p_offset
        
              else if (mtt .lt. bound_3) then
c                 --- REGION 3 ---
                  p_val = 2.4114d-04*mtt**2 - 7.6391d-01*mtt 
     &                 + 5.9023d+02
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  final_arg = p_val + stitch_sum - p_offset

              else if (mtt .lt. bound_4) then
c                 --- REGION 4 ---
                  p_val = -6.5570d-06*mtt**2 + 2.3638d-02*mtt 
     &                 - 3.3663d+01
                  p_val = -p_val
                  stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2)
                  stitch_sum = stitch_sum + (p3_at_b3 - p4_at_b3)
                  final_arg = p_val + stitch_sum - p_offset
        
              else
c                 --- REGION 5 ---
		  mtt = min(dip_loc + 350.0d0, mtt)
                  p_val = -1.3595d-08*mtt**2 - 2.5766d-03*mtt 
     &                 - 7.2827d+00
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
