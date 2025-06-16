(* ::Package:: *)

LSM = LoadModel["SM"];
DefineField[s,Scalar,Mass->{Heavy,Ms},NiceForm-> {"\!\(\*SubscriptBox[\(\[Phi]\), \(s\)]\)","\!\(\*SubscriptBox[\(M\), \(s\)]\)"},SelfConjugate->True];
DefineField[T, Fermion,Indices->{SU3c[fund],Flavor},Charges  -> {U1Y[2/3]},  Mass->{Heavy,MT,{Flavor}},NiceForm-> {"\!\(\*SubscriptBox[\(\[Psi]\), \(T\)]\)","\!\(\*SubscriptBox[\(M\), \(T\)]\)"}];
DefineCoupling[yHs,SelfConjugate->True,NiceForm->"\!\(\*SubscriptBox[\(y\), \(Hs\)]\)"];
LBSM=FreeLag[s,T]+PlusHc[-yDM[p,r]  Bar@u[a,p]**PL**T[a,r] s[]] - (1/4)*yHs[]Bar[H[i]]H[i]s[]s[];
LUV=LSM+LBSM;
