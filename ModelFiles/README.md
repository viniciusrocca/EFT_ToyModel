# FeynRules Model Files

Hold the FeynRules files for distinct model implementations


## Models Description

### UV Simplified Model (SMS-stop)

 * The model is defined in [ModelFiles/UV_BSM_ToyModel.fr](./modelFiles/SMS-stop.fr)

We consider the simple case of a vector-like fermio top partner ($\psi_T$), singlet under $SU(2)_L$, and a singlet scalar ($\phi_s$),
which is a Dark Matter candidate. In addition we impose a $\mathcal{Z}_2$ symmetry, under which the BSM fields are odd and the SM are even. Under this assumptions the renormalizable (UV) BSM lagrangian is:

```math
	\mathcal{L}_{BSM} = \bar{\psi}_T \left( i \gamma^\mu D_\mu -M_T \right) \psi_T+ \frac{1}{2}(\partial_\mu s)^2 - \frac{1}{2}M_s^2 s^2 - y_{DM} \left( \bar{\psi}_T t_R + \bar{t}_R \psi_T \right) s  - V(s) 
```

In addition we assume $m_T > m_{\chi}$, so the DM candidate is stable.



### Top EFT (Top-EFT)

 * The model is defined in [modelFiles/Top-EFT.fr](./modelFiles/Top-EFT.fr)

The model includes the dim-6 EFT operators in the *physical* (on-shell) basis relevant for $q q \to t \bar{t}$ production.
## Files

* [DiagonalCKM](./DiagonalCKM.rst): restriction file for a diagonal CKM matrix

* [LorentzTadpole](./LorentzTadpole.gen): generic model file for FeynArts needed for NLO calculations

* [Massless](./Massless.rst): restriction file for massless quarks

* [Massless](./Massless.rst): restriction file for massless quarks

* [SM](./SM.fr): full SM model file

* [SMQCD](./SMQCD.fr): simplified SM model file containing only QCD and quarks

* [SMS-stop](./SMS-stop.fr): UV BSM model with a scalar top partner and a fermionic DM candidate

* [Top-EFT](./Top-EFT.fr): model file with the relevant EFT operators and the coefficient values.

* [NoDMHiggsCoupling](./LorentzTadpole.gen): restriction file to disable the coupling between the Higgs and the Dark Matter


