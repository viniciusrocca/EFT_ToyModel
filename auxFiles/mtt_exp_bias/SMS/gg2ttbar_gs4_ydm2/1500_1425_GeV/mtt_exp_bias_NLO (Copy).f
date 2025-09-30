
      
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
      double precision bias_wgt,p(0:3,nexternal),H_T
      integer ipdg(nexternal),i,j
      double precision pTot(0:3)
      double precision mtt
      double precision polynomial_arg
      double precision polynomial_offset

      
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
         if (mtt .lt. 2601.0d0) then
            polynomial_arg = - ( 1.5d-06 * mtt**2 - 8.5d-03 * mtt - 2.9 )
            polynomial_offset = - ( 1.5d-06 * 500.0**2 - 8.5d-03 * 500.0 - 2.9 )
            bias_wgt = EXP(polynomial_arg - polynomial_offset)

         else if (mtt .ge. 2601.0d0 .and. mtt .lt. 4501.0d0) then

c            polynomial_arg = - ( - 1.2d-06 * mtt**2 + 5.6d-03 * mtt - 2.3 )
c            polynomial_offset =  - ( 1.5d-06 * 500.0**2 - 8.5d-03 * 500.0 - 2.9 )
c            bias_wgt = EXP(polynomial_arg - polynomial_offset)
            polynomial_arg = - ( - 1.1d-06 * mtt**2 + 5.0d-03 * mtt - 22.1 )
            polynomial_offset =  - ( 1.5d-06 * 500.0**2 - 8.5d-03 * 500.0 - 2.9 )
            bias_wgt = EXP(polynomial_arg - polynomial_offset)

         else
            mtt = min(mtt,5000.0)
            polynomial_arg = - ( - 4.5d-07 * mtt**2 + 4.5d-03 * mtt - 33.2 )
            polynomial_offset = - ( 1.5d-06 * 500.0**2 - 8.5d-03 * 500.0 - 2.9 )
            bias_wgt = EXP(polynomial_arg - polynomial_offset)

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
