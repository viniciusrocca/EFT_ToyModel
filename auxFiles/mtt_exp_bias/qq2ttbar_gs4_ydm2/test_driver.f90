program test_bsm_pred
  use mod_bsm_pred
  implicit none

  integer, parameter :: dp = kind(1.0d0)
  
  ! Test inputs
  real(dp) :: mPsiT, mSDM
  real(dp) :: mass_points(5)
  real(dp) :: amp
  integer :: i

  ! 1. Define the Physics Parameters
  mPsiT = 1000.0_dp
  mSDM  = 500.0_dp

  ! 2. Define Mass points that hit different regions
  ! Based on mPsiT=1000, mSDM=500:
  ! Peak ~ 2050, Dip ~ 2887
  mass_points(1) = 1200.0_dp  ! Region 1 (Cubic)
  mass_points(2) = 2100.0_dp  ! Region 2 (Quadratic)
  mass_points(3) = 2300.0_dp  ! Region 3 (Cubic)
  mass_points(4) = 2900.0_dp  ! Region 4 (Quadratic)
  mass_points(5) = 4000.0_dp  ! Region 5 (Cubic)

  print *, "=========================================="
  print *, " FORTRAN PREDICTION TEST"
  print *, " mPsiT =", mPsiT, " mSDM =", mSDM
  print *, "=========================================="

  do i = 1, 5
     amp = get_bsm_amplitude(mass_points(i), mPsiT, mSDM)
     print *, "Mass:", mass_points(i), " => Amp:", amp
  end do
  print *, "=========================================="

end program test_bsm_pred
