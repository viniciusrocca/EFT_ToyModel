! =====================================================
! Auto-generated BSM Prediction Module
! =====================================================
module mod_bsm_pred
  implicit none
  private
  public :: get_bsm_amplitude

  integer, parameter :: dp = kind(1.0d0)
  integer, parameter :: n_input_features = 6
  integer, parameter :: n_coeffs = 17

  ! -- SCALER X --
  real(dp), parameter :: mean_x(2) = (/8.0357142857142856e+02_dp, 6.6928571428571433e+02_dp/)
  real(dp), parameter :: scale_x(2) = (/3.2853260640214660e+02_dp, 3.3168862949877479e+02_dp/)

  ! -- SCALER Y --
  real(dp), parameter :: mean_y(17) = (/ &
      1.2206409720803431e+00_dp, 7.9160611798306812e-01_dp, -6.9318153908260713e+00_dp, &
      -3.3632909571428575e+00_dp, -1.8327067934753825e+00_dp, 1.3191430877209718e+00_dp, &
      -8.4032998671909969e+00_dp, -1.2429707571331454e+00_dp, -2.8513112335657098e+00_dp, &
      -8.9419467972643947e+00_dp, 8.5316647103999994e+00_dp, -8.1775281533142863e+00_dp, &
      -1.2989847477829414e+01_dp, 2.7835444167586374e+00_dp, -5.8113905196962552e+00_dp, &
      1.4691588747077893e-02_dp, -1.3494333971621359e+01_dp &
      /)

  real(dp), parameter :: scale_y(17) = (/ &
      3.5700978227489681e+00_dp, 7.9172958806845184e+00_dp, 6.4199720762414918e+00_dp, &
      5.4728125075917389e-01_dp, 4.0912762431348554e-01_dp, 3.6121148836635847e-01_dp, &
      2.2902174996806339e+00_dp, 4.0143337925752537e-01_dp, 5.4057808311891509e-01_dp, &
      2.2166871294281028e+00_dp, 2.0407200260390437e+00_dp, 2.0522003320203246e+00_dp, &
      2.8728645132680826e+00_dp, 4.1495469608142316e-01_dp, 7.5444909917619540e-01_dp, &
      9.8857865392068967e-01_dp, 3.1695821637688919e+00_dp &
      /)

  ! -- RIDGE WEIGHTS --
  real(dp), parameter :: weights(102) = (/ &
      0.0000000000000000e+00_dp, 0.0000000000000000e+00_dp, 0.0000000000000000e+00_dp, &
      0.0000000000000000e+00_dp, 0.0000000000000000e+00_dp, 0.0000000000000000e+00_dp, &
      0.0000000000000000e+00_dp, 0.0000000000000000e+00_dp, 0.0000000000000000e+00_dp, &
      0.0000000000000000e+00_dp, 0.0000000000000000e+00_dp, 0.0000000000000000e+00_dp, &
      0.0000000000000000e+00_dp, 0.0000000000000000e+00_dp, 0.0000000000000000e+00_dp, &
      0.0000000000000000e+00_dp, 0.0000000000000000e+00_dp, -5.4046361224670235e-02_dp, &
      1.8065607473533818e-01_dp, -4.8277141738673701e-01_dp, -1.2192608016354614e+00_dp, &
      2.7376258251212744e+00_dp, -1.4000406342407077e+00_dp, -1.0826858699669666e+00_dp, &
      -3.9283755648065202e+00_dp, 1.6547348515940088e+00_dp, -1.1335103648526661e+00_dp, &
      1.0877536260415638e+01_dp, -9.4419490638820740e+00_dp, -1.8646142526207804e-01_dp, &
      6.2326480617088489e+00_dp, -5.6651273023884512e+00_dp, 2.8705351603053524e+00_dp, &
      -9.4544424931473292e-01_dp, -7.6763019448904091e-01_dp, 7.3034150714569834e-01_dp, &
      -5.5840529343918788e-01_dp, 6.4903493447687677e-01_dp, -1.4496948067475963e+00_dp, &
      1.3410321875786582e+00_dp, -1.4453247495647156e-01_dp, 1.7721337834329880e+00_dp, &
      -2.2464846403402663e+00_dp, -3.8662571541777213e-02_dp, -8.0883139171721155e+00_dp, &
      6.7738973836030070e+00_dp, -8.6708847353129803e-01_dp, -4.0927209158406148e+00_dp, &
      2.8543154720880799e+00_dp, -6.8615939240601764e-01_dp, -2.3100455150000487e-01_dp, &
      9.3509455468108627e-01_dp, -9.9162791610301770e-01_dp, 9.8093475022631071e-01_dp, &
      -2.5419277748760765e+00_dp, -3.6906028665174534e-01_dp, -6.4225632673228150e-01_dp, &
      1.8842388891186143e-01_dp, 2.6163644566262612e+00_dp, -1.7240479252309400e+00_dp, &
      1.9761968709475664e-01_dp, -4.5437795418253488e+00_dp, 3.1156388514995750e+00_dp, &
      -1.5365386914247523e-02_dp, -1.0244380115464402e+00_dp, 1.0544322100373746e+00_dp, &
      -5.4901157519620658e-01_dp, 4.6589786980955214e-02_dp, 2.0970319664463895e+00_dp, &
      -1.9196791139637615e+00_dp, 1.3481350534636960e+00_dp, -2.4618775175130767e+00_dp, &
      4.8916094058551982e+00_dp, -3.3439847249877239e+00_dp, -9.2034490166114341e-02_dp, &
      -7.2594563315765779e+00_dp, 4.1160390760645154e+00_dp, -2.8568041835223990e-01_dp, &
      2.3122396875915928e+01_dp, -1.8336520442948419e+01_dp, 1.0789324390483208e+00_dp, &
      1.4649891806868657e+01_dp, -1.1483789423206108e+01_dp, 3.9802899629332420e+00_dp, &
      -1.8375788729990419e-01_dp, -2.6947629989002069e+00_dp, 2.5099075685636945e+00_dp, &
      -1.9039143684929236e+00_dp, 4.2137694839799638e+00_dp, -4.3161501972454790e+00_dp, &
      3.1490823269208224e+00_dp, 8.6052989677982986e-02_dp, 5.2258586955422679e+00_dp, &
      -2.5786682240812486e+00_dp, 2.1132314856556075e-01_dp, -1.8838230544789521e+01_dp, &
      1.5372304337975983e+01_dp, -9.3496892113770280e-01_dp, -1.3567861052083929e+01_dp, &
      1.0774073695722340e+01_dp, -3.9467660042150254e+00_dp, 2.3330857985640249e-01_dp &
      /)

  ! -- RIDGE INTERCEPTS --
  real(dp), parameter :: intercepts(17) = (/ &
      -1.1014418659107064e-01_dp, 1.9339680828235581e-01_dp, -2.7908119498653278e-01_dp, &
      5.2328442698177846e-01_dp, 3.2362077119609695e-01_dp, 4.7482853634865319e-01_dp, &
      -1.9241458534097453e-01_dp, -1.3693494150080134e+00_dp, 6.3266153093854061e-01_dp, &
      -1.5421669740532662e-01_dp, 2.7649902104426518e+00_dp, -2.1382365193217705e+00_dp, &
      -1.1692754292772545e-02_dp, 1.5297644057038542e+00_dp, -1.5890174970720681e+00_dp, &
      9.4676327440212882e-01_dp, -1.1605116556335626e-01_dp &
      /)


contains

  ! =========================================================
  ! Main Function: Get Amplitude
  ! =========================================================
  function get_bsm_amplitude(mass, mPsiT, mSDM) result(amp)
    real(dp), intent(in) :: mass, mPsiT, mSDM
    real(dp) :: amp
    
    real(dp) :: bounds(6)
    real(dp) :: region_coeffs(4)
    integer :: region_idx
    real(dp) :: u, width, start_loc
    
    call get_boundaries(mPsiT, mSDM, bounds)
    
    if (mass < bounds(2)) then
       region_idx = 1
       start_loc = bounds(1)
       width = bounds(2) - bounds(1)
    else if (mass < bounds(3)) then
       region_idx = 2
       start_loc = bounds(2)
       width = bounds(3) - bounds(2)
    else if (mass < bounds(4)) then
       region_idx = 3
       start_loc = bounds(3)
       width = bounds(4) - bounds(3)
    else if (mass < bounds(5)) then
       region_idx = 4
       start_loc = bounds(4)
       width = bounds(5) - bounds(4)
    else
       region_idx = 5
       start_loc = bounds(5)
       width = bounds(6) - bounds(5)
    end if
    
    u = (mass - start_loc) / width
    call predict_region_coeffs(region_idx, mPsiT, mSDM, region_coeffs)
    
    ! UPDATED LOGIC: Regions 2 and 4 are Quadratic. Regions 1, 3, 5 are Cubic.
    if (region_idx == 2 .or. region_idx == 4) then
       ! Quadratic Regions (Passed as [a, b, c, 0])
       amp = region_coeffs(1)*u**2 + region_coeffs(2)*u + region_coeffs(3)
    else
       ! Cubic Regions (Passed as [a, b, c, d])
       amp = region_coeffs(1)*u**3 + region_coeffs(2)*u**2 + region_coeffs(3)*u + region_coeffs(4)
    end if

  end function get_bsm_amplitude

  ! =========================================================
  ! Helper: Predict Coeffs
  ! =========================================================
  subroutine predict_region_coeffs(rid, m1, m2, out_coeffs)
    integer, intent(in) :: rid
    real(dp), intent(in) :: m1, m2
    real(dp), intent(out) :: out_coeffs(4)
    
    real(dp) :: x_std(2), feats(6)
    real(dp) :: all_preds(n_coeffs)
    real(dp) :: val
    integer :: i, j, k
    
    out_coeffs = 0.0_dp
    
    x_std(1) = (m1 - mean_x(1)) / scale_x(1)
    x_std(2) = (m2 - mean_x(2)) / scale_x(2)
    
    feats(1) = 1.0_dp
    feats(2) = x_std(1)
    feats(3) = x_std(2)
    feats(4) = x_std(1)**2
    feats(5) = x_std(1) * x_std(2)
    feats(6) = x_std(2)**2
    
    do i = 1, n_coeffs
       val = intercepts(i)
       do j = 1, n_input_features
          k = i + (j-1)*n_coeffs 
          val = val + weights(k) * feats(j)
       end do
       all_preds(i) = val * scale_y(i) + mean_y(i)
    end do
    
    ! UPDATED INDICES for Structure [4, 3, 3, 3, 4] (Total 17)
    select case (rid)
    case (1)
       ! R1 (4 coeffs): 1..4
       out_coeffs(1:4) = all_preds(1:4)
    case (2)
       ! R2 (3 coeffs): 5..7
       out_coeffs(1:3) = all_preds(5:7)
    case (3)
       ! R3 (4 coeffs): 8..11
       out_coeffs(1:3) = all_preds(8:10)
    case (4)
       ! R4 (3 coeffs): 12..14
       out_coeffs(1:3) = all_preds(11:13)
    case (5)
       ! R5 (4 coeffs): 15..18
       out_coeffs(1:4) = all_preds(14:17)
    end select
    
  end subroutine predict_region_coeffs

  subroutine get_boundaries(mPsiT, mSDM, b)
    real(dp), intent(in) :: mPsiT, mSDM
    real(dp), intent(out) :: b(6)
    real(dp) :: peak_loc, dip_loc
    
    peak_loc = 2.05_dp * mPsiT
    dip_loc  = 2.6_dp * mPsiT + 0.5_dp * mSDM + 37.5_dp
    
    b(1) = 0.0_dp
    b(2) = 0.9_dp * peak_loc
    b(3) = peak_loc + 50.0_dp
    b(4) = dip_loc - 60.0_dp
    b(5) = dip_loc + 140.0_dp
    b(6) = dip_loc + 1900.0_dp
    
  end subroutine get_boundaries

end module mod_bsm_pred
