import numpy as np

# ==============================================================================
# 1. THE GROUND TRUTH (YOUR DATABASE)
# ==============================================================================
# Structure: [R1(4), R2(3), R3(4), R4(3), R5(4)]
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
    # ... (Add other keys if you want a full test, using 2 for brevity) ...
}

# ==============================================================================
# 2. THE AI PARAMETERS (FROM FORTRAN MODULE)
# ==============================================================================
# These must match mod_bsm_pred.f90 exactly
mean_x = np.array([8.0357142857142856e+02, 6.6928571428571433e+02])
scale_x = np.array([3.2853260640214660e+02, 3.3168862949877479e+02])

# Flattened weights from the Fortran code (reconstructed for Python)
# Note: For brevity, I am using the shape, but these numbers must come from the Fortran file
# In a real check, you copy the 'weights' array from the f90 file here.
# For this demonstration, we assume the prediction logic is working and we define the function structure.

# IMPORTANT: To run this locally, you must paste the 'weights' and 'mean_y'/'scale_y' 
# arrays from your mod_bsm_pred.f90 file here.
# I will use the arrays you provided in the previous prompt.

mean_y = np.array([
      1.0855004029085473e+00, 1.0867038949551471e+00, -7.1362167816889288e+00,
      -3.3194736728571428e+00, -9.9849405215429687e-01, 9.7248282795051522e-01,
      -7.4065578096080502e+00, -3.3087731559724949e+00, 3.0510906254277406e+00,
      -4.9790310135240174e+00, -8.2044650751612007e+00, 4.1462928342857142e+00,
      -2.4385482878571390e+00, -1.5567917794614269e+01, 2.5952169480636704e+00,
      -5.5300619122821857e+00, -9.5341557708486721e-02, -1.3484628019261979e+01
])

scale_y = np.array([
      3.6279474107209815e+00, 8.0438431623668603e+00, 6.4946657218490547e+00,
      6.0005637015709878e-01, 5.3195782533548308e-01, 5.2287569334379924e-01,
      2.1661910636343995e+00, 7.8428061549498262e-01, 9.3608389930696423e-01,
      8.4364234033308749e-01, 2.3135956621949907e+00, 3.3588346271053173e+00,
      3.5892786497495641e+00, 3.0808722181249104e+00, 3.8925110870229129e-01,
      7.5674570251576245e-01, 9.8835382895008894e-01, 3.1714552560636826e+00
])

weights_flat = np.array([
      0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
      0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
      0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
      -3.01847177e-01, 4.22713560e-01, -6.87312754e-01, -6.24566309e-01, -4.58457372e+00, 2.98285928e+00,
      -1.33574417e+00, 7.06949054e-02, 5.00600974e-01, -8.53198983e-01, -1.57825034e+00, 9.58819439e+00,
      -8.13754903e+00, 7.19483112e-01, 4.33028628e+00, -3.76502394e+00, 2.27748236e+00, -9.27359909e-01,
      -6.74086564e-01, 6.38778648e-01, -4.83290481e-01, 4.32570938e-01, 1.55192303e+00, -6.44100840e-01,
      -1.93358970e-02, -1.65692362e+00, 1.46701989e+00, -9.63791753e-01, 5.76001417e-01, -7.24742421e+00,
      6.14717208e+00, -1.71851838e+00, -3.88564279e+00, 2.41258062e+00, -5.37771391e-01, -2.35713061e-01,
      1.03111131e+00, -1.08527611e+00, 1.06337510e+00, -2.53581847e+00, 4.17075933e-01, -1.04430626e+00,
      -8.35909253e-01, 4.35957306e-01, -2.57976785e-01, -6.71235328e-02, 3.42732086e-03, -2.47219004e+00,
      1.33861965e+00, 1.70398168e-01, -1.47052709e+00, 1.13360642e+00, -5.14532855e-01, 4.32169681e-02,
      1.47093588e+00, -1.30578927e+00, 8.31897397e-01, -1.08355135e+00, -9.50039970e+00, 6.17613471e+00,
      -4.79919397e-01, 1.21574777e+00, -1.52279615e-01, -1.03273323e+00, -9.94632855e-01, 1.96615844e+01,
      -1.58598354e+01, 2.86140987e+00, 9.91365647e+00, -6.83789849e+00, 2.53537686e+00, -1.41280156e-01,
      -2.09635070e+00, 1.92338390e+00, -1.41272750e+00, 2.75431740e+00, 1.03909753e+01, -6.45338162e+00,
      1.34110389e+00, -9.52451121e-01, -4.69221964e-01, 1.53984629e+00, 9.10149281e-01, -1.70334144e+01,
      1.42048310e+01, -2.68684513e+00, -7.75701677e+00, 5.52982320e+00, -2.37044438e+00, 1.89145665e-01
])

intercepts = np.array([
      -2.46316429e-01, 3.26195530e-01, -3.92406567e-01, 7.47646560e-01, -2.33704662e+00, 1.99075480e+00,
      -7.72758634e-02, -5.67524254e-01, 8.62978438e-01, -5.51889092e-01, -2.67150256e-02, 1.97440822e+00,
      -1.40207314e+00, -3.49210686e-02, 3.88060071e-01, -5.66436743e-01, 6.24315620e-01, -1.06390581e-01
])

# Fortran ordering reshape
weights = weights_flat.reshape(6, 18).T

# ==============================================================================
# 3. HELPER FUNCTIONS
# ==============================================================================

def get_boundaries(mPsiT, mSDM):
    peak_loc = 2.05 * mPsiT
    dip_loc  = 2.6 * mPsiT + 0.5 * mSDM + 37.5
    b = [0] * 6
    b[0] = 0.0
    b[1] = 0.9 * peak_loc
    b[2] = peak_loc + 50.0
    b[3] = dip_loc - 60.0
    b[4] = dip_loc + 140.0
    b[5] = dip_loc + 1900.0
    return b

def get_true_val(mass, mPsiT, mSDM):
    """
    Calculates amplitude using the ORIGINAL Database coefficients.
    """
    flat_coeffs = data_db.get((mPsiT, mSDM))
    if flat_coeffs is None: return None
    
    bounds = get_boundaries(mPsiT, mSDM)
    
    # Identify Region
    region_idx = -1
    if mass < bounds[1]: region_idx = 0
    elif mass < bounds[2]: region_idx = 1
    elif mass < bounds[3]: region_idx = 2
    elif mass < bounds[4]: region_idx = 3
    else: region_idx = 4
    
    # Extract coefficients for this region
    start_idx = 0
    for i in range(region_idx):
        start_idx += structure[i]
    
    coeffs = flat_coeffs[start_idx : start_idx + structure[region_idx]]
    
    # Numpy polyval expects [x^n, x^n-1, ... 1]. 
    # Your database seems to be [x^n ... 1] based on magnitude analysis.
    return np.polyval(coeffs, mass)

def get_ai_pred(mass, mPsiT, mSDM):
    """
    Calculates amplitude using the FORTRAN/AI Logic.
    """
    bounds = get_boundaries(mPsiT, mSDM)
    
    # 1. Identify Region
    region_idx = 0; start_loc=0; width=0
    if mass < bounds[1]: region_idx=1; start_loc=bounds[0]; width=bounds[1]-bounds[0]
    elif mass < bounds[2]: region_idx=2; start_loc=bounds[1]; width=bounds[2]-bounds[1]
    elif mass < bounds[3]: region_idx=3; start_loc=bounds[2]; width=bounds[3]-bounds[2]
    elif mass < bounds[4]: region_idx=4; start_loc=bounds[3]; width=bounds[4]-bounds[3]
    else: region_idx=5; start_loc=bounds[4]; width=bounds[5]-bounds[4]
    
    u = (mass - start_loc) / width
    
    # 2. Regression
    inputs = np.array([mPsiT, mSDM])
    x_std = (inputs - mean_x) / scale_x
    feats = np.array([1.0, x_std[0], x_std[1], x_std[0]**2, x_std[0]*x_std[1], x_std[1]**2])
    
    all_preds = np.dot(weights, feats) + intercepts
    all_preds = all_preds * scale_y + mean_y
    
    # 3. Select Coeffs
    coeffs = []
    if region_idx==1: coeffs = all_preds[0:4]
    elif region_idx==2: coeffs = all_preds[4:7]
    elif region_idx==3: coeffs = all_preds[7:11]
    elif region_idx==4: coeffs = all_preds[11:14]
    elif region_idx==5: coeffs = all_preds[14:18]
    
    # 4. Evaluate Standard Polynomial
    # Fortran does: c(1)*u**3... so it's [c3, c2, c1, c0]
    if len(coeffs) == 3:
        return coeffs[0]*u**2 + coeffs[1]*u + coeffs[2]
    else:
        return coeffs[0]*u**3 + coeffs[1]*u**2 + coeffs[2]*u + coeffs[3]

# ==============================================================================
# 4. MAIN COMPARISON LOOP
# ==============================================================================

print(f"{'PARAM SET':<15} | {'MASS':<10} | {'TRUE VAL':<15} | {'AI PRED':<15} | {'% ERROR':<10}")
print("-" * 75)

for (mPsiT, mSDM) in data_db.keys():
    bounds = get_boundaries(mPsiT, mSDM)
    
    # Pick one test mass in the middle of each region
    test_masses = [
        (bounds[0] + bounds[1])/2,  # Middle of Region 1
        (bounds[1] + bounds[2])/2,  # Middle of Region 2 (Peak)
        (bounds[2] + bounds[3])/2,  # Middle of Region 3
        (bounds[3] + bounds[4])/2,  # Middle of Region 4 (Dip)
        (bounds[4] + bounds[5])/2,  # Middle of Region 5
    ]
    
    for m in test_masses:
        val_true = get_true_val(m, mPsiT, mSDM)
        val_pred = get_ai_pred(m, mPsiT, mSDM)
        
        err = 0.0
        if val_true != 0:
            err = 100 * abs(val_true - val_pred) / abs(val_true)
            
        print(f"({mPsiT}, {mSDM}) | {m:<10.1f} | {val_true:<15.4e} | {val_pred:<15.4e} | {err:<10.2f}%")