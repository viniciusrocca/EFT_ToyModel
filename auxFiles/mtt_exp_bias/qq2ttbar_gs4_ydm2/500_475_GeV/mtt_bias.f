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
          double precision polynomial_arg
          double precision polynomial_offset
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
	  
          if (mtt.gt.0.0d0) then
            if (mtt .lt. 1601.0d0) then
              polynomial_arg = - (1.1d-06 * mtt**2 - 5.7d-03 * mtt - 2.46d0)
              polynomial_offset =  - (1.1d-06 * mtt_bias_offset**2 - 5.7d-03 * mtt_bias_offset - 2.36d0)

            else if (mtt .ge. 1601.0d0 .and. mtt .lt. 2701.0d0) then
              polynomial_arg = - (1.0d-07 * mtt**2 - 2.78d-03 * mtt - 4.6d0)
              polynomial_offset =  - (1.1d-06 * mtt_bias_offset**2 - 5.7d-03 * mtt_bias_offset - 2.46d0)


            else
            mtt = min(mtt, 3500.0)
              polynomial_arg = - (7.2d-07 * mtt**2 - 6.6d-03 * mtt + 1.45d0)
              polynomial_offset =  - (1.1d-06 * mtt_bias_offset**2 - 5.7d-03 * mtt_bias_offset - 2.36d0)
          endif

          bias_weight = EXP(polynomial_arg - polynomial_offset)
          endif

      return

          return

      end subroutine bias_wgt
