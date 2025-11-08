C ************************************************************
C Source for the library implementing a bias function that 
C populates the large pt tale of the leading jet. 
C
C The two options of this subroutine, that can be set in
C the run card are:
C    > (double precision) mtt_bias_offset : target mtt value
C
C
C Schematically, the functional form of the enhancement is
C    bias_wgt = [mtt(evt)/mean_mtt]^enhancement_power
C ************************************************************
C
C The following lines are read by MG5aMC to set what are the 
C relevant parameters for this bias module.
C
C  parameters = {'mtt_bias_offset': 2000.0}
C

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
          double precision max_mtt

c --- Local Calculation Variables ---
          double precision p_val, p_offset
          double precision p1_at_b1, p2_at_b1, p2_at_b2, p3_at_b2
          double precision p3_at_b3, p4_at_b3, p4_at_b4, p5_at_b4
          double precision stitch_sum
      
c --- Boundary and Normalization Parameters ---
          double precision, parameter :: bound_1 = 650.0d0
          double precision, parameter :: bound_2 = 1100.0d0
          double precision, parameter :: bound_3 = 2450.0d0
          double precision, parameter :: bound_4 = 2700.0d0


c
c local variables defined in the run_card
c
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
     &                requires_full_event_info

C
C Accessingt the details of the event
C
          logical is_a_j(nexternal),is_a_l(nexternal),
     &            is_a_b(nexternal),is_a_a(nexternal),
     &            is_a_onium(nexternal),is_a_nu(nexternal),
     &            is_heavy(nexternal),do_cuts(nexternal)
          common/to_specisa/is_a_j,is_a_a,is_a_l,is_a_b,is_a_nu,
     &                      is_heavy,is_a_onium,do_cuts
C
C    Setup the value of the parameters from the run_card    
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

          mtt = dsqrt(pTot(0)**2 - pTot(1)**2 - pTot(2)**2 - pTot(3)**2)
	  
          if (mtt .gt. 0.0d0) then

c        Calculate the normalization offset using the first polynomial at mtt_bias_offset
            p_offset = -(-2.0864d-05*mtt_bias_offset**2 + 2.2111d-02*mtt_bias_offset - 1.2906d+01)
         
c        Pre-calculate the function values at each boundary for stitching
            p1_at_b1 = -(- 2.0864d-05*bound_1**2 + 2.2111d-02*bound_1 - 1.2906d+01)
            p2_at_b1 = -(- 2.8785d-08*bound_1**2 - 2.8296d-03*bound_1 - 5.4234d+00)
         
            p2_at_b2 = -(- 2.8785d-08*bound_2**2 - 2.8296d-03*bound_2 - 5.4234d+00)
            p3_at_b2 = -( 2.1151d-07*bound_2**2 - 3.1376d-03*bound_2 - 5.3761d+00)

            p3_at_b3 = -( 2.1151d-07*bound_3**2 - 3.1376d-03*bound_3 - 5.3761d+00)
            p4_at_b3 = -(- 9.8702d-06*bound_3**2 + 4.9014d-02*bound_3 - 7.2694d+01)

            p4_at_b4 = -(- 9.8702d-06*bound_4**2 + 4.9014d-02*bound_4 - 7.2694d+01)
            p5_at_b4 = -(- 2.2881d-07*bound_4**2 - 7.2571d-04*bound_4 - 8.6016d+00)

            if (mtt .lt. bound_1) then
c           --- REGION 1 ---
              p_val = -(- 2.0864d-05*mtt**2 + 2.2111d-02*mtt - 1.2906d+01)
              bias_weight = EXP(p_val - p_offset)

            else if (mtt .lt. bound_2) then
c           --- REGION 2  ---
              p_val = -(- 2.8785d-08*mtt**2 - 2.8296d-03*mtt - 5.4234d+00)
              bias_weight = EXP(p_val + (p1_at_b1 - p2_at_b1) - p_offset)
            
            else if (mtt .lt. bound_3) then
c           --- REGION 3  ---
              p_val = -( 2.1151d-07*mtt**2 - 3.1376d-03*mtt - 5.3761d+00)
              bias_weight = EXP(p_val + (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2) - p_offset)

            else if (mtt .lt. bound_4) then
c           --- REGION 4  ---
              p_val = -(- 9.8702d-06*mtt**2 + 4.9014d-02*mtt - 7.2694d+01)
              bias_weight = EXP(p_val + (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2) + (p3_at_b3 - p4_at_b3) - p_offset)
            
            else
c           --- REGION 5 (Stitched) ---
              mtt = min(mtt, 3500.0)
              p_val = -(- 2.2881d-07*mtt**2 - 7.2571d-04*mtt - 8.6016d+00)
              stitch_sum = (p1_at_b1 - p2_at_b1) + (p2_at_b2 - p3_at_b2) + (p3_at_b3 - p4_at_b3) + (p4_at_b4 - p5_at_b4)
              bias_weight = EXP(p_val + stitch_sum  - p_offset)
            endif
          endif

      return

          return

      end subroutine bias_wgt
