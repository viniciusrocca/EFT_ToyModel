subroutine bias_weight_function(p,ipdg,bias_wgt)
      use mod_bsm_pred, only: get_bsm_amplitude
      implicit none
      
c     --- MADGRAPH INCLUDES ---
      include 'nexternal.inc'
      include '../MODEL/input.inc' 

c     --- ARGUMENTS ---
      double precision bias_wgt
      double precision p(0:3,nexternal)
      integer ipdg(nexternal)

c     --- LOCAL VARIABLES ---
      integer i, j
      double precision pTot(0:3)
      double precision mtt
      
c     --- EVALUATION VARIABLES ---
      double precision val_raw
      double precision val_at_norm
      
c     --- NORMALIZATION VARIABLES ---
      double precision mtt_norm 

c     --- INITIALIZATION ---
      bias_wgt = 1d0
      
      mtt_norm = 1300.0d0
      mtt = 0d0
      pTot = (/ 0d0, 0d0, 0d0, 0d0 /)
      
      do i=1,nexternal
         if (abs(ipdg(i)).eq.6) then  ! Top quark (PDG ID 6)
            do j =0,3
               pTot(j) = pTot(j)+p(j,i)
            enddo 
         endif
      enddo
      
      ! Calculate invariant mass: sqrt(E^2 - Px^2 - Py^2 - Pz^2)
      mtt = pTot(0)**2 - pTot(1)**2 - pTot(2)**2 - pTot(3)**2
      if (mtt .gt. 0d0) then
         mtt = dsqrt(mtt)
      else
         return
      endif

c     CMS data limitation
      mtt = min(mtt,3500.0d0)
      val_raw = get_bsm_amplitude(mtt, mdl_mpsit, mdl_msdm)
      
c     Get the prediction at the normalization point 
      val_at_norm = get_bsm_amplitude(mtt_norm, mdl_mpsit, mdl_msdm)



      bias_wgt = EXP( val_at_norm - val_raw )
      
      
      return
      end
