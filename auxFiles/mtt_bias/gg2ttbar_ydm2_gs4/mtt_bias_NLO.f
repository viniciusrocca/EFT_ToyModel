
      
subroutine bias_weight_function(p,ipdg,bias_wgt)
c This is a user-defined function to which to bias the event generation.
c A non-flat distribution will generate events with a certain weight
c inversely proportinal to the bias_wgt. This is particularly useful to
c generate more events (with smaller weight) in tails of distributions.
c It computes the bias_wgt factor from the momenta and multiplies the
c weight that goes into MINT (or vegas) with this factor.  Before
c writing out the events (or making the plots), this factor is again
c divided out. A value different from 1 makes that MINT (or vegas) does
c not list the correct cross section, but the cross section can still be
c computed from summing all the weights of the events (and dividing by
c the number of events). Since the weights of the events are no longer
c identical for all events, the statistical uncertainty on this total
c cross section can be much larger than without including the bias.
c
c The 'bias_wgt' should be a IR-safe function of the momenta.
c      
c For this to be used, the 'event_norm' option in the run_card should be
c set to
c      'bias' = event_norm      
c
      implicit none
      include 'nexternal.inc'
      include '../../Source/MODEL/coupl.inc'
      double precision bias_wgt
      double precision p(0:3,nexternal)
      integer ipdg(nexternal)
      integer i,j
      double precision pTot(0:3)
      double precision mtt
      double precision peak_loc
      double precision bound_1, bound_2, bound_3
      double precision den_1, den_2, den_3
      
c local variables defined in the run_card
c
c      double precision mtt_bias_target_mtt
c      double precision mtt_bias_enhancement_power

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
    

      mtt = dsqrt(pTot(0)**2 - pTot(1)**2 - pTot(2)**2 - pTot(3)**2)
      if (mtt.gt.0.0d0) then
          peak_loc = 2.05 * mdl_mpsit
          if (peak_loc.gt.2900.0d0) then
             bound_1 = (3710.0d0/3075.0d0) * peak_loc 
             bound_2 = (3850.0d0/3075.0d0) * peak_loc
             den_1 = peak_loc
             den_2 = peak_loc
             den_3 = (3207.0d0/3075.0d0) * peak_loc
             if (mtt.lt.bound_1) then
                bias_wgt = (mtt/den_1)**5.3
             else if (mtt.lt.bound_2) then
                bias_wgt = (mtt/den_2)**2.3
             else
                bias_wgt = (mtt/den_3)**8.0
             endif
          else
             bound_1 = (1600.0d0/1500.0d0) * peak_loc 
             bound_2 = (1800.0d0/1500.0d0) * peak_loc
             bound_3 = (2000.0d0/1050.0d0) * peak_loc
             den_1 = bound_2
             den_2 = peak_loc
             if (mdl_mpsit.lt.625.0d0) then
                den_3 = (1400.0d0/1050.0d0) * peak_loc
             else
                den_3 = (1550.0d0/1500.0d0) * peak_loc
             endif
             if (mtt.lt.bound_1) then
                bias_wgt = (mtt/den_1)**3.3
             else if (mtt.lt.bound_2) then
                bias_wgt = (mtt/den_2)**3.5
             else if (mtt.lt.2000.0d0) then
                bias_wgt = (mtt/den_2)**6.8
             else
                bias_wgt = (mtt/den_3)**10.0
             endif
          endif
      endif

c How to enhance the tails is very process dependent. For example for
c top quark production one could use:
c      do i=1,nexternal
c         if (ipdg(i).eq.6) then
c            bias_wgt=sqrt(p(1,i)**2+p(2,i)**2)**3
c         endif
c      enddo
c Or to use H_T^2 one does     
c      H_T=0d0
c      do i=3,nexternal
c         H_T=H_T+sqrt(max(0d0,(p(0,i)+p(3,i))*(p(0,i)-p(3,i))))
c      enddo
c      bias_wgt=H_T**2
      return
      end
