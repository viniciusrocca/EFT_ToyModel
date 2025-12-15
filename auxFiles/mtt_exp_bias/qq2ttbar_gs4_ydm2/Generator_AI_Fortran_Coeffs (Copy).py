import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from scipy.special import binom

# ==============================================================================
# HELPER FUNCTIONS
# ==============================================================================

def get_poly_on_standard_domain(coeffs, x_min, x_max):
    """
    Converts a polynomial P(x) valid on [x_min, x_max] 
    to a polynomial Q(u) valid on [0, 1] where x = (x_max - x_min)*u + x_min.
    """
    deg = len(coeffs) - 1
    new_coeffs = np.zeros(deg + 1)
    rev_coeffs = coeffs[::-1]
    
    delta = x_max - x_min
    shift = x_min
    
    for k in range(deg + 1):
        c_k = rev_coeffs[k]
        for j in range(k + 1):
            contribution = c_k * binom(k, j) * (delta**j) * (shift**(k-j))
            new_coeffs[j] += contribution
            
    return new_coeffs[::-1]

def get_boundaries(mPsiT, mSDM):
    peak_loc = 2.05 * mPsiT
    dip_loc  = 2.6 * mPsiT + 0.5 * mSDM + 37.5
    b1 = 0.9 * peak_loc
    b2 = peak_loc + 50.0
    b3 = dip_loc - 60.0
    b4 = dip_loc + 140.0
    b5 = dip_loc + 1900.0
    return [0, b1, b2, b3, b4, b5]

# ==============================================================================
# DATASET
# ==============================================================================

# CORRECTED STRUCTURE based on actual data in data_db:
# Region 1: 4 coeffs (Cubic)
# Region 2: 3 coeffs (Quadratic) <-- Fixed to match data (was 4)
# Region 3: 4 coeffs (Cubic)
# Region 4: 3 coeffs (Quadratic)
# Region 5: 4 coeffs (Cubic)
# Total: 18 coefficients
structure = [4, 3, 4, 3, 4] 

data_db = {
    (500, 475): np.concatenate([
        [ 8.17090128e-09, -1.27767291e-05,  2.52870776e-03, -3.83718275e+00],
        [-4.99086469e-05,  9.81138370e-02, -5.40743930e+01],
        [-2.88494557e-08,  1.04077643e-04, -1.33663537e-01,  5.30247056e+01],
        [ 1.10686066e-04, -3.48386128e-01,  2.61486008e+02],
        [ 4.87244884e-10, -4.14730614e-06,  9.30138827e-03, -1.68010198e+01]
    ]),
    (1500, 1425): np.concatenate([
        [-2.17233376e-10,  1.69643662e-06, -6.07376512e-03, -4.47024740e+00],
        [-1.99265118e-06,  1.15414239e-02, -2.85607238e+01],
        [-1.37827437e-09,  1.47525080e-05, -5.62911292e-02,  6.07833974e+01],
        [ 2.08217545e-04, -1.95085764e+00,  4.54662936e+03],
        [ 5.99684476e-10, -1.09605150e-05,  6.47131074e-02, -1.44598815e+02]
    ]),
    (725, 675): np.concatenate([
        [-3.59562989e-10,  3.01486469e-06, -7.55749568e-03, -2.49707439e+00],
        [-3.73514170e-05,  1.07426048e-01, -8.36453908e+01],
        [-1.34854325e-08,  7.12888117e-05, -1.31667654e-01,  7.57401548e+01],
        [ 4.78312391e-05, -2.11993123e-01,  2.18825803e+02],
        [ 4.05226148e-10, -4.51300329e-06,  1.45503927e-02, -2.76406646e+01]
    ]),
    (1000, 500): np.concatenate([
        [-2.39639896e-10,  2.13592580e-06, -6.68913248e-03, -3.13936659e+00],
        [-1.61414323e-05,  6.36849791e-02, -7.14061072e+01],
        [-8.89023167e-09,  6.22099449e-05, -1.50364580e-01,  1.13880507e+02],
        [ 1.07997709e-04, -6.29391586e-01,  8.99869560e+02],
        [ 4.31131638e-10, -5.72620222e-06,  2.31449820e-02, -4.44064079e+01]
    ]),
    (600, 475): np.concatenate([
        [ 2.91994336e-09, -4.08694504e-06, -2.32058351e-03, -3.25148628e+00],
        [-4.45985532e-05,  1.05816666e-01, -6.84943071e+01],
        [-2.21831807e-08,  9.47485560e-05, -1.42421329e-01,  6.64936226e+01],
        [ 2.19057869e-04, -8.05170660e-01,  7.25841744e+02],
        [ 5.32417398e-10, -4.98901121e-06,  1.32005565e-02, -2.22211670e+01]
    ]),
    (800, 760): np.concatenate([
        [-6.21576760e-11,  2.11367983e-06, -6.86059526e-03, -2.88636391e+00],
        [-3.43338437e-05,  1.09105054e-01, -9.36693159e+01],
        [-9.75619695e-09,  5.66701694e-05, -1.15286766e-01,  7.23018064e+01],
        [-4.11998766e-05,  2.21564406e-01, -3.13355753e+02],
        [ 3.78231138e-10, -4.66367169e-06,  1.68276211e-02, -3.28200711e+01]

    ]),
    (500, 375): np.concatenate([
        [ 5.59559214e-09, -7.96073190e-06, -3.59280517e-04, -3.15459439e+00],
        [-6.18215157e-06,  1.32425962e-02, -1.18114298e+01],
        [-3.77346057e-08,  1.32294389e-04, -1.63352321e-01,  6.34291896e+01],
        [ 7.30106945e-05, -2.19842170e-01,  1.53345032e+02],
        [ 4.98284614e-10, -4.09118288e-06,  8.67347408e-03, -1.55891064e+01]
    ])
}

# ==============================================================================
# PREPROCESSING & TRAINING
# ==============================================================================

print("Normalizing Data (Physical Domain -> Standard Domain)...")
X_raw = []
Y_norm = []

for (mPsiT, mSDM), flat_coeffs in data_db.items():
    bounds = get_boundaries(mPsiT, mSDM)
    norm_flat = []
    cursor = 0
    for i, count in enumerate(structure):
        c_poly = flat_coeffs[cursor : cursor + count]
        norm_poly = get_poly_on_standard_domain(c_poly, bounds[i], bounds[i+1])
        norm_flat.extend(norm_poly)
        cursor += count
    
    X_raw.append([mPsiT, mSDM])
    Y_norm.append(norm_flat)

X_train = np.array(X_raw)
Y_train = np.array(Y_norm)

print("Training Regression Model...")

scaler_x = StandardScaler()
X_scaled = scaler_x.fit_transform(X_train)

poly = PolynomialFeatures(degree=2, include_bias=True)
X_poly = poly.fit_transform(X_scaled)

scaler_y = StandardScaler()
Y_scaled = scaler_y.fit_transform(Y_train)

ridge = Ridge(alpha=0.001)
ridge.fit(X_poly, Y_scaled)

print("   Model trained. Features:", X_poly.shape[1], "Targets:", Y_scaled.shape[1])

# ==============================================================================
#  FORTRAN CODE GENERATOR
# ==============================================================================

def write_fortran_array(f, name, data, chunk_size=3):
    """
    Writes a numpy array to Fortran, ensuring strictly correct syntax.
    """
    size = len(data)
    f.write(f"  real(dp), parameter :: {name}({size}) = (/ &\n")
    
    for i in range(0, size, chunk_size):
        chunk = data[i:i+chunk_size]
        formatted_nums = [f"{x:.16e}_dp" for x in chunk]
        line = ", ".join(formatted_nums)
        
        if i + chunk_size < size:
            line += ", &"
        else:
            line += " &" 
            
        f.write("      " + line + "\n")
        
    f.write("      /)\n\n")

def write_fortran_module(filename="mod_bsm_pred.f90"):
    print(f" Generating Fortran Module: {filename} ...")
    
    n_features = X_poly.shape[1]
    n_coeffs = Y_scaled.shape[1]  # Should be 18 now
    
    with open(filename, "w") as f:
        # Header
        f.write("! =====================================================\n")
        f.write("! Auto-generated BSM Prediction Module\n")
        f.write("! =====================================================\n")
        f.write("module mod_bsm_pred\n")
        f.write("  implicit none\n")
        f.write("  private\n")
        f.write("  public :: get_bsm_amplitude\n\n")
        
        f.write("  integer, parameter :: dp = kind(1.0d0)\n")
        f.write(f"  integer, parameter :: n_input_features = {n_features}\n")
        f.write(f"  integer, parameter :: n_coeffs = {n_coeffs}\n\n")

        # 1. Scalers
        f.write("  ! -- SCALER X --\n")
        f.write(f"  real(dp), parameter :: mean_x(2) = (/{scaler_x.mean_[0]:.16e}_dp, {scaler_x.mean_[1]:.16e}_dp/)\n")
        f.write(f"  real(dp), parameter :: scale_x(2) = (/{scaler_x.scale_[0]:.16e}_dp, {scaler_x.scale_[1]:.16e}_dp/)\n\n")

        f.write("  ! -- SCALER Y --\n")
        write_fortran_array(f, "mean_y", scaler_y.mean_)
        write_fortran_array(f, "scale_y", scaler_y.scale_)

        # 2. Weights
        flat_weights = ridge.coef_.flatten(order='F')
        f.write("  ! -- RIDGE WEIGHTS --\n")
        write_fortran_array(f, "weights", flat_weights)
        
        f.write("  ! -- RIDGE INTERCEPTS --\n")
        write_fortran_array(f, "intercepts", ridge.intercept_)

        # 3. Fortran Logic
        f.write("""
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
    
    ! UPDATED INDICES for Structure [4, 3, 4, 3, 4] (Total 18)
    select case (rid)
    case (1)
       ! R1 (4 coeffs): 1..4
       out_coeffs(1:4) = all_preds(1:4)
    case (2)
       ! R2 (3 coeffs): 5..7
       out_coeffs(1:3) = all_preds(5:7)
    case (3)
       ! R3 (4 coeffs): 8..11
       out_coeffs(1:4) = all_preds(8:11)
    case (4)
       ! R4 (3 coeffs): 12..14
       out_coeffs(1:3) = all_preds(12:14)
    case (5)
       ! R5 (4 coeffs): 15..18
       out_coeffs(1:4) = all_preds(15:18)
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
""")
    print(f"Successfully generated {filename}")

# Run it
if __name__ == "__main__":
    write_fortran_module()