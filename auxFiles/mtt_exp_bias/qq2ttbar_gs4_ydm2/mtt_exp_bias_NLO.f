subroutine bias_weight_function(p,ipdg,bias_wgt)
c     ==================================================================
c
c     REQUIREMENTS:
c     1. mod_bsm_pred.o must be linked during compilation.
c     2. ../MODEL/input.inc must exist and contain mdl_mpsit/mdl_msdm.
c     ==================================================================
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
      
c     --- DYNAMIC BOUNDARY VARIABLES ---
      double precision peak_loc, dip_loc
      double precision b1, b2, b3, b4, b5
      
c     --- STITCHING & EVALUATION VARIABLES ---
      double precision eps
      parameter (eps = 1d-3) ! Small offset to check boundary jumps
      double precision val_raw
      double precision gap1, gap2, gap3, gap4, gap5
      double precision total_stitch_offset
      double precision unnormalized_val
      
c     --- NORMALIZATION VARIABLES ---
      double precision, parameter :: mtt_norm = 1000.0d0
      double precision val_at_norm, norm_stitch_offset


      bias_wgt = 1d0
      
      if (mdl_mpsit .lt. 1.0d0) return

c     Calculate Invariant Mass of the Top Quark Pair 
      mtt = 0d0
      pTot = (/ 0d0, 0d0, 0d0, 0d0 /)
      
      do i=1,nexternal
         if (abs(ipdg(i)).eq.6) then
            do j =0,3
               pTot(j) = pTot(j)+p(j,i)
            enddo 
         endif
      enddo
      


      if (mtt .le. 0.0d0) return

c     --- CMS CONSTRAINT: HARD CUTOFF AT 3500 GEV ---
      if (mtt .gt. mtt_cutoff) then
          bias_wgt = 1d0
          return
      endif

c     Computing the boundaries
      peak_loc = 2.05d0 * mdl_mpsit
      dip_loc  = 2.6d0 * mdl_mpsit + 0.5d0 * mdl_msdm + 37.5d0

      b1 = 0.9d0 * peak_loc
      b2 = peak_loc + 50.0d0
      b3 = dip_loc - 60.0d0
      b4 = dip_loc + 140.0d0
      b5 = dip_loc + 1900.0d0

c    This will make the bias function smooth
      
      gap1 = get_bsm_amplitude(b1-eps, mdl_mpsit, mdl_msdm) - get_bsm_amplitude(b1+eps, mdl_mpsit, mdl_msdm)
      gap2 = get_bsm_amplitude(b2-eps, mdl_mpsit, mdl_msdm) - get_bsm_amplitude(b2+eps, mdl_mpsit, mdl_msdm)
      gap3 = get_bsm_amplitude(b3-eps, mdl_mpsit, mdl_msdm) - get_bsm_amplitude(b3+eps, mdl_mpsit, mdl_msdm)
      gap4 = get_bsm_amplitude(b4-eps, mdl_mpsit, mdl_msdm) - get_bsm_amplitude(b4+eps, mdl_mpsit, mdl_msdm)
      gap5 = get_bsm_amplitude(b5-eps, mdl_mpsit, mdl_msdm) - get_bsm_amplitude(b5+eps, mdl_mpsit, mdl_msdm)


      
      ! Get raw value from AI
      val_raw = get_bsm_amplitude(mtt, mdl_mpsit, mdl_msdm)
      
      ! Add cumulative gaps depending on which region we are in
      total_stitch_offset = 0d0
      if (mtt .ge. b1) total_stitch_offset = total_stitch_offset + gap1
      if (mtt .ge. b2) total_stitch_offset = total_stitch_offset + gap2
      if (mtt .ge. b3) total_stitch_offset = total_stitch_offset + gap3
      if (mtt .ge. b4) total_stitch_offset = total_stitch_offset + gap4
      if (mtt .ge. b5) total_stitch_offset = total_stitch_offset + gap5
      
      unnormalized_val = val_raw + total_stitch_offset
      
c This will guarantee an initial supression and a numerical stability
      
      val_at_norm = get_bsm_amplitude(mtt_norm, mdl_mpsit, mdl_msdm)
      norm_stitch_offset = 0d0
      
      if (mtt_norm .ge. b1) norm_stitch_offset = norm_stitch_offset + gap1
      if (mtt_norm .ge. b2) norm_stitch_offset = norm_stitch_offset + gap2
      if (mtt_norm .ge. b3) norm_stitch_offset = norm_stitch_offset + gap3
      if (mtt_norm .ge. b4) norm_stitch_offset = norm_stitch_offset + gap4
      if (mtt_norm .ge. b5) norm_stitch_offset = norm_stitch_offset + gap5
      

      bias_wgt = EXP( (val_at_norm + norm_stitch_offset) - unnormalized_val )

      return
      end
