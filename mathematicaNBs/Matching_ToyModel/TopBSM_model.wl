(* ::Package:: *)

LSM = LoadModel["SM"];
DefineField[s,Scalar,Mass->{Heavy,Ms},NiceForm-> {"\!\(\*SubscriptBox[\(\[Phi]\), \(s\)]\)","\!\(\*SubscriptBox[\(M\), \(s\)]\)"},SelfConjugate->True];
DefineField[T, Fermion,Indices->{SU3c[fund],Flavor},Charges  -> {U1Y[2/3]},  Mass->{Heavy,MT,{Flavor}},NiceForm-> {"\!\(\*SubscriptBox[\(\[Psi]\), \(T\)]\)","\!\(\*SubscriptBox[\(M\), \(T\)]\)"}];
DefineCoupling[yHs,SelfConjugate->True,NiceForm->"\!\(\*SubscriptBox[\(y\), \(Hs\)]\)"];
DefineCoupling[lamHs,SelfConjugate->True,NiceForm->"\!\(\*SubscriptBox[\(\[Lambda]\), \(Hs\)]\)"];
DefineCoupling[lamS,SelfConjugate->True,NiceForm->"\!\(\*SubscriptBox[\(\[Lambda]\), \(S\)]\)"];
LBSM=FreeLag[s,T]+PlusHc[-yDM[p,r]  Bar@u[a,p]**PL**T[a,r] s[]] - (1/4)*lamHs[]Bar[H[i]]H[i]s[]s[] - (1/24) * lamS[]s[]s[]s[]s[] ;
LUV=LSM+LBSM;
