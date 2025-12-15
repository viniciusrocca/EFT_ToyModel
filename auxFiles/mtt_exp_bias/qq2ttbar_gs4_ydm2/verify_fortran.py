import numpy as np

# ==============================================================================
# PARAMETERS EXTRACTED DIRECTLY FROM YOUR FORTRAN CODE
# ==============================================================================
mean_x = np.array([8.0357142857142856e+02, 6.6928571428571433e+02])
scale_x = np.array([3.2853260640214660e+02, 3.3168862949877479e+02])

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
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
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

# Reshape weights to (18, 6) because Fortran iterates i then j
# k = i + (j-1)*n_coeffs  (Fortran Column Major)
weights = weights_flat.reshape(6, 18).T

# ==============================================================================
# LOGIC
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

def predict(mass, mPsiT, mSDM):
    # 1. Boundaries
    bounds = get_boundaries(mPsiT, mSDM)
    
    region_idx = 0
    start_loc = 0
    width = 0
    
    if mass < bounds[1]:
        region_idx = 1; start_loc = bounds[0]; width = bounds[1] - bounds[0]
    elif mass < bounds[2]:
        region_idx = 2; start_loc = bounds[1]; width = bounds[2] - bounds[1]
    elif mass < bounds[3]:
        region_idx = 3; start_loc = bounds[2]; width = bounds[3] - bounds[2]
    elif mass < bounds[4]:
        region_idx = 4; start_loc = bounds[3]; width = bounds[4] - bounds[3]
    else:
        region_idx = 5; start_loc = bounds[4]; width = bounds[5] - bounds[4]
        
    u = (mass - start_loc) / width

    # 2. Input Scaling
    inputs = np.array([mPsiT, mSDM])
    x_std = (inputs - mean_x) / scale_x
    
    # 3. Features
    feats = np.zeros(6)
    feats[0] = 1.0
    feats[1] = x_std[0]
    feats[2] = x_std[1]
    feats[3] = x_std[0]**2
    feats[4] = x_std[0] * x_std[1]
    feats[5] = x_std[1]**2
    
    # 4. Matrix Multiplication (Coeff Prediction)
    # y = Wx + b
    all_preds = np.dot(weights, feats) + intercepts
    
    # 5. Output Scaling
    all_preds = all_preds * scale_y + mean_y
    
    # 6. Select Coeffs
    coeffs = []
    is_quadratic = False
    
    if region_idx == 1:
        coeffs = all_preds[0:4]
    elif region_idx == 2:
        coeffs = all_preds[4:7]
        is_quadratic = True
    elif region_idx == 3:
        coeffs = all_preds[7:11]
    elif region_idx == 4:
        coeffs = all_preds[11:14]
        is_quadratic = True
    elif region_idx == 5:
        coeffs = all_preds[14:18]
        
    # 7. Evaluate Polynomial
    if is_quadratic:
        # a*u^2 + b*u + c
        amp = coeffs[0]*u**2 + coeffs[1]*u + coeffs[2]
    else:
        # a*u^3 + b*u^2 + c*u + d
        amp = coeffs[0]*u**3 + coeffs[1]*u**2 + coeffs[2]*u + coeffs[3]
        
    return amp

# RUN TEST
mPsiT = 1000.0
mSDM = 500.0
mass_points = [1200.0, 2100.0, 2300.0, 2900.0, 4000.0]

print("==========================================")
print(" PYTHON VERIFICATION (GROUND TRUTH)")
print(f" mPsiT = {mPsiT}  mSDM = {mSDM}")
print("==========================================")

for m in mass_points:
    val = predict(m, mPsiT, mSDM)
    print(f"Mass: {m} => Amp: {val}")