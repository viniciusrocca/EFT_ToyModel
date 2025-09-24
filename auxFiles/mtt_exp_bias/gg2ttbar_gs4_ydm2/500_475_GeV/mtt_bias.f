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
          double precision p_val, p_offset, mtt_eff
          double precision p1_at_b1, p2_at_b1, p2_at_b2, p3_at_b2
          double precision stitch_factor_12, stitch_factor_23
          double precision, parameter :: bound_1 = 1451.0d0
          double precision, parameter :: bound_2 = 2351.0d0
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

          p_offset = - ( 1.6d-06 * mtt_bias_offset**2 - 8.95d-03 * mtt_bias_offset - 5.87d-01 )

c         Calculate the stitch factors needed at the boundaries
          p1_at_b1 = - ( 1.6d-06 * bound_1**2 - 8.95d-03 * bound_1 - 5.87d-01 )
          p2_at_b1 = - ( 1.0d-06 * bound_1**2 - 7.61d-03 * bound_1 - 1.2d0 )
          stitch_factor_12 = p1_at_b1 - p2_at_b1

          p2_at_b2 = - ( 1.0d-06 * bound_2**2 - 7.61d-03 * bound_2 - 1.2d0 )
          p3_at_b2 = - ( 1.8d-06 * bound_2**2 - 1.2d-02 * bound_2 + 4.5d0 )
          stitch_factor_23 = p2_at_b2 - p3_at_b2

          if (mtt.gt.0.0d0) then
            if (mtt .lt. bound_1) then
              p_val = - ( 1.6d-06 * mtt**2 - 8.95d-03 * mtt - 5.87d-01 )
              bias_weight = EXP(p_val - p_offset)

            else if (mtt .lt. bound_2) then
              p_val = - ( 1.0d-06 * mtt**2 - 7.61d-03 * mtt - 1.03d0 )
              bias_weight = EXP(p_val + stitch_factor_12 - p_offset)

            else
c             Apply cutoff for stability
              mtt = min(mtt, 3500.0)
              p_val = - ( 1.8d-06 * mtt**2 - 1.2d-02 * mtt + 4.7d0 )
              bias_weight = EXP(p_val + stitch_factor_12 + stitch_factor_23 - p_offset)
         endif

          endif

      return

          return

      end subroutine bias_wgt
