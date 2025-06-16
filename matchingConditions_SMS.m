(* Created with the Wolfram Language : www.wolfram.com *)
{Coupling[gL, {}, 0] -> Coupling[gL, {}, 0], 
 Coupling[gs, {}, 0] -> Coupling[gs, {}, 0] - 
   (hbar*Coupling[gs, {}, 0]^3*FlavorSum[Index[d$$1, Flavor]]*
     Log[\[Mu]bar2/Coupling[MT, {Index[d$$1, Flavor]}, 0]^2])/3, 
 Coupling[gY, {}, 0] -> Coupling[gY, {}, 0] - 
   (8*hbar*Coupling[gY, {}, 0]^3*FlavorSum[Index[d$$1, Flavor]]*
     Log[\[Mu]bar2/Coupling[MT, {Index[d$$1, Flavor]}, 0]^2])/9, 
 Coupling[Yd, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  Coupling[Yd, {Index[i1, Flavor], Index[i2, Flavor]}, 0], 
 Coupling[Ye, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  Coupling[Ye, {Index[i1, Flavor], Index[i2, Flavor]}, 0], 
 Coupling[Yu, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  Coupling[Yu, {Index[i1, Flavor], Index[i2, Flavor]}, 0] + 
   (hbar*Coupling[yDM, {Index[d$$2, Flavor], Index[d$$1, Flavor]}, 0]*
     Coupling[yDM, {Index[i2, Flavor], Index[d$$1, Flavor]}, 0]*
     Coupling[Yu, {Index[i1, Flavor], Index[d$$2, Flavor]}, 0]*
     (1 - 4*LF[{Coupling[Ms, {}, 0], Coupling[MT, {Index[d$$1, Flavor]}, 0]}, 
        {1, 1, 0}] + 2*LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], 
         Coupling[Ms, {}, 0]}, {2, 1, -1}]))/8, 
 Coupling[\[Lambda], {}, 0] -> Coupling[\[Lambda], {}, 0] - 
   (hbar*Coupling[yHs, {}, 0]^2*Log[\[Mu]bar2/Coupling[Ms, {}, 0]^2])/8, 
 Coupling[\[Mu]2, {}, 2] -> Coupling[\[Mu]2, {}, 2] + 
   (hbar*Coupling[Ms, {}, 0]^2*Coupling[yHs, {}, 0]*
     (1 + \[Epsilon] + \[Epsilon]*Log[\[Mu]bar2/Coupling[Ms, {}, 0]^2]))/
    (4*\[Epsilon]), Coupling[cdd, {Index[i1_, Flavor], Index[i2_, Flavor], 
    Index[i3_, Flavor], Index[i4_, Flavor]}, 0] -> 
  -1/810*(hbar*(16*Coupling[gY, {}, 0]^4*Delta[Index[i1, Flavor], 
        Index[i2, Flavor]]*Delta[Index[i3, Flavor], Index[i4, Flavor]] + 
      9*Coupling[gs, {}, 0]^4*(3*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
         Delta[Index[i2, Flavor], Index[i3, Flavor]] - 
        Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
          Index[i4, Flavor]]))*FlavorSum[Index[d$$1, Flavor]])/
    Coupling[MT, {Index[d$$1, Flavor]}, 0]^2, 
 Coupling[ced, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (-16*hbar*Coupling[gY, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]]*FlavorSum[Index[d$$1, Flavor]])/
   (135*Coupling[MT, {Index[d$$1, Flavor]}, 0]^2), 
 Coupling[cee, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (-4*hbar*Coupling[gY, {}, 0]^4*
    (Delta[Index[i1, Flavor], Index[i4, Flavor]]*Delta[Index[i2, Flavor], 
       Index[i3, Flavor]] + Delta[Index[i1, Flavor], Index[i2, Flavor]]*
      Delta[Index[i3, Flavor], Index[i4, Flavor]])*
    FlavorSum[Index[d$$1, Flavor]])/
   (45*Coupling[MT, {Index[d$$1, Flavor]}, 0]^2), 
 Coupling[ceu, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (hbar*Coupling[gY, {}, 0]^2*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*
    ((32*Coupling[gY, {}, 0]^2*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
       FlavorSum[Index[d$$1, Flavor]])/Coupling[MT, {Index[d$$1, Flavor]}, 0]^
       2 + 15*Coupling[yDM, {Index[i3, Flavor], Index[d$$1, Flavor]}, 0]*
      Coupling[yDM, {Index[i4, Flavor], Index[d$$1, Flavor]}, 0]*
      (3*LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], Coupling[Ms, {}, 0]}, 
         {3, 1, -1}] - LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], 
         Coupling[Ms, {}, 0]}, {4, 1, -2}])))/135, 
 Coupling[cG, {}, 0] -> -1/180*(hbar*Coupling[gs, {}, 0]^3*
     FlavorSum[Index[d$$1, Flavor]])/Coupling[MT, {Index[d$$1, Flavor]}, 0]^
     2, Coupling[cH, {}, 0] -> -1/96*(hbar*Coupling[yHs, {}, 0]^3)/
    Coupling[Ms, {}, 0]^2, Coupling[cHBox, {}, 0] -> 
  -1/96*(hbar*Coupling[yHs, {}, 0]^2)/Coupling[Ms, {}, 0]^2 - 
   (2*hbar*Coupling[gY, {}, 0]^4*FlavorSum[Index[d$$1, Flavor]])/
    (45*Coupling[MT, {Index[d$$1, Flavor]}, 0]^2), 
 Coupling[cHd, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (8*hbar*Coupling[gY, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
    FlavorSum[Index[d$$1, Flavor]])/
   (135*Coupling[MT, {Index[d$$1, Flavor]}, 0]^2), 
 Coupling[cHD, {}, 0] -> (-8*hbar*Coupling[gY, {}, 0]^4*
    FlavorSum[Index[d$$1, Flavor]])/
   (45*Coupling[MT, {Index[d$$1, Flavor]}, 0]^2), 
 Coupling[cHe, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (8*hbar*Coupling[gY, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
    FlavorSum[Index[d$$1, Flavor]])/
   (45*Coupling[MT, {Index[d$$1, Flavor]}, 0]^2), 
 Coupling[cHl1, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (4*hbar*Coupling[gY, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
    FlavorSum[Index[d$$1, Flavor]])/
   (45*Coupling[MT, {Index[d$$1, Flavor]}, 0]^2), 
 Coupling[cHq1, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (-4*hbar*Coupling[gY, {}, 0]^4*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
     FlavorSum[Index[d$$1, Flavor]])/
    (135*Coupling[MT, {Index[d$$1, Flavor]}, 0]^2) - 
   (hbar*Bar[Coupling[Yu, {Index[i2, Flavor], Index[d$$1, Flavor]}, 0]]*
     Coupling[yDM, {Index[d$$1, Flavor], Index[d$$2, Flavor]}, 0]*
     Coupling[yDM, {Index[d$$3, Flavor], Index[d$$2, Flavor]}, 0]*
     Coupling[Yu, {Index[i1, Flavor], Index[d$$3, Flavor]}, 0]*
     (LF[{Coupling[MT, {Index[d$$2, Flavor]}, 0], Coupling[Ms, {}, 0]}, 
       {2, 1, 0}] - 2*LF[{Coupling[MT, {Index[d$$2, Flavor]}, 0], 
         Coupling[Ms, {}, 0]}, {3, 1, -1}] + 
      LF[{Coupling[MT, {Index[d$$2, Flavor]}, 0], Coupling[Ms, {}, 0]}, 
       {4, 1, -2}]))/4, 
 Coupling[cHq3, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (hbar*Bar[Coupling[Yu, {Index[i2, Flavor], Index[d$$1, Flavor]}, 0]]*
    Coupling[yDM, {Index[d$$1, Flavor], Index[d$$2, Flavor]}, 0]*
    Coupling[yDM, {Index[d$$3, Flavor], Index[d$$2, Flavor]}, 0]*
    Coupling[Yu, {Index[i1, Flavor], Index[d$$3, Flavor]}, 0]*
    (LF[{Coupling[MT, {Index[d$$2, Flavor]}, 0], Coupling[Ms, {}, 0]}, 
      {2, 1, 0}] - 2*LF[{Coupling[MT, {Index[d$$2, Flavor]}, 0], 
        Coupling[Ms, {}, 0]}, {3, 1, -1}] + 
     LF[{Coupling[MT, {Index[d$$2, Flavor]}, 0], Coupling[Ms, {}, 0]}, 
      {4, 1, -2}]))/4, 
 Coupling[cHu, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (hbar*Coupling[gY, {}, 0]^2*
    ((-32*Coupling[gY, {}, 0]^2*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
       FlavorSum[Index[d$$1, Flavor]])/Coupling[MT, {Index[d$$1, Flavor]}, 0]^
       2 + 15*Coupling[yDM, {Index[i1, Flavor], Index[d$$1, Flavor]}, 0]*
      Coupling[yDM, {Index[i2, Flavor], Index[d$$1, Flavor]}, 0]*
      (-3*LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], Coupling[Ms, {}, 0]}, 
         {3, 1, -1}] + LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], 
         Coupling[Ms, {}, 0]}, {4, 1, -2}])))/270, 
 Coupling[cld, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (-8*hbar*Coupling[gY, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]]*FlavorSum[Index[d$$1, Flavor]])/
   (135*Coupling[MT, {Index[d$$1, Flavor]}, 0]^2), 
 Coupling[cle, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (-8*hbar*Coupling[gY, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]]*FlavorSum[Index[d$$1, Flavor]])/
   (45*Coupling[MT, {Index[d$$1, Flavor]}, 0]^2), 
 Coupling[cll, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (-2*hbar*Coupling[gY, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]]*FlavorSum[Index[d$$1, Flavor]])/
   (45*Coupling[MT, {Index[d$$1, Flavor]}, 0]^2), 
 Coupling[clq1, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (4*hbar*Coupling[gY, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]]*FlavorSum[Index[d$$1, Flavor]])/
   (135*Coupling[MT, {Index[d$$1, Flavor]}, 0]^2), 
 Coupling[clu, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (hbar*Coupling[gY, {}, 0]^2*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*
    ((32*Coupling[gY, {}, 0]^2*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
       FlavorSum[Index[d$$1, Flavor]])/Coupling[MT, {Index[d$$1, Flavor]}, 0]^
       2 + 15*Coupling[yDM, {Index[i3, Flavor], Index[d$$1, Flavor]}, 0]*
      Coupling[yDM, {Index[i4, Flavor], Index[d$$1, Flavor]}, 0]*
      (3*LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], Coupling[Ms, {}, 0]}, 
         {3, 1, -1}] - LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], 
         Coupling[Ms, {}, 0]}, {4, 1, -2}])))/270, 
 Coupling[cqd1, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (8*hbar*Coupling[gY, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]]*FlavorSum[Index[d$$1, Flavor]])/
   (405*Coupling[MT, {Index[d$$1, Flavor]}, 0]^2), 
 Coupling[cqd8, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (-2*hbar*Coupling[gs, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]]*FlavorSum[Index[d$$1, Flavor]])/
   (15*Coupling[MT, {Index[d$$1, Flavor]}, 0]^2), 
 Coupling[cqe, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (8*hbar*Coupling[gY, {}, 0]^4*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
     Index[i4, Flavor]]*FlavorSum[Index[d$$1, Flavor]])/
   (135*Coupling[MT, {Index[d$$1, Flavor]}, 0]^2), 
 Coupling[cqq1, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  -1/1620*(hbar*(8*Coupling[gY, {}, 0]^4*Delta[Index[i1, Flavor], 
        Index[i2, Flavor]]*Delta[Index[i3, Flavor], Index[i4, Flavor]] + 
      9*Coupling[gs, {}, 0]^4*(3*Delta[Index[i1, Flavor], Index[i4, Flavor]]*
         Delta[Index[i2, Flavor], Index[i3, Flavor]] - 
        2*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
         Delta[Index[i3, Flavor], Index[i4, Flavor]]))*
     FlavorSum[Index[d$$1, Flavor]])/Coupling[MT, {Index[d$$1, Flavor]}, 0]^
     2, Coupling[cqq3, {Index[i1_, Flavor], Index[i2_, Flavor], 
    Index[i3_, Flavor], Index[i4_, Flavor]}, 0] -> 
  -1/60*(hbar*Coupling[gs, {}, 0]^4*Delta[Index[i1, Flavor], 
      Index[i4, Flavor]]*Delta[Index[i2, Flavor], Index[i3, Flavor]]*
     FlavorSum[Index[d$$1, Flavor]])/Coupling[MT, {Index[d$$1, Flavor]}, 0]^
     2, Coupling[cqu1, {Index[i1_, Flavor], Index[i2_, Flavor], 
    Index[i3_, Flavor], Index[i4_, Flavor]}, 0] -> 
  (hbar*Coupling[gY, {}, 0]^2*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
    ((-32*Coupling[gY, {}, 0]^2*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
       FlavorSum[Index[d$$1, Flavor]])/Coupling[MT, {Index[d$$1, Flavor]}, 0]^
       2 + 15*Coupling[yDM, {Index[i3, Flavor], Index[d$$1, Flavor]}, 0]*
      Coupling[yDM, {Index[i4, Flavor], Index[d$$1, Flavor]}, 0]*
      (-3*LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], Coupling[Ms, {}, 0]}, 
         {3, 1, -1}] + LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], 
         Coupling[Ms, {}, 0]}, {4, 1, -2}])))/810, 
 Coupling[cqu8, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (hbar*Coupling[gs, {}, 0]^2*
    Delta[Index[i1, Flavor], Index[i2, Flavor]]*
    ((-4*Coupling[gs, {}, 0]^2*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
       FlavorSum[Index[d$$1, Flavor]])/Coupling[MT, {Index[d$$1, Flavor]}, 0]^
       2 + 5*Coupling[yDM, {Index[i3, Flavor], Index[d$$1, Flavor]}, 0]*
      Coupling[yDM, {Index[i4, Flavor], Index[d$$1, Flavor]}, 0]*
      (-3*LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], Coupling[Ms, {}, 0]}, 
         {3, 1, -1}] + LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], 
         Coupling[Ms, {}, 0]}, {4, 1, -2}])))/30, 
 Coupling[cuB, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (hbar*Coupling[gY, {}, 0]*Coupling[yDM, {Index[d$$2, Flavor], 
      Index[d$$1, Flavor]}, 0]*Coupling[yDM, {Index[i2, Flavor], 
      Index[d$$1, Flavor]}, 0]*Coupling[Yu, {Index[i1, Flavor], 
      Index[d$$2, Flavor]}, 0]*
    (-LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], Coupling[Ms, {}, 0]}, 
       {3, 1, -1}] + LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], 
       Coupling[Ms, {}, 0]}, {4, 1, -2}]))/6, 
 Coupling[cud1, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (hbar*Coupling[gY, {}, 0]^2*
    Delta[Index[i3, Flavor], Index[i4, Flavor]]*
    ((32*Coupling[gY, {}, 0]^2*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
       FlavorSum[Index[d$$1, Flavor]])/Coupling[MT, {Index[d$$1, Flavor]}, 0]^
       2 + 15*Coupling[yDM, {Index[i1, Flavor], Index[d$$1, Flavor]}, 0]*
      Coupling[yDM, {Index[i2, Flavor], Index[d$$1, Flavor]}, 0]*
      (3*LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], Coupling[Ms, {}, 0]}, 
         {3, 1, -1}] - LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], 
         Coupling[Ms, {}, 0]}, {4, 1, -2}])))/405, 
 Coupling[cud8, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> (hbar*Coupling[gs, {}, 0]^2*
    Delta[Index[i3, Flavor], Index[i4, Flavor]]*
    ((-4*Coupling[gs, {}, 0]^2*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
       FlavorSum[Index[d$$1, Flavor]])/Coupling[MT, {Index[d$$1, Flavor]}, 0]^
       2 + 5*Coupling[yDM, {Index[i1, Flavor], Index[d$$1, Flavor]}, 0]*
      Coupling[yDM, {Index[i2, Flavor], Index[d$$1, Flavor]}, 0]*
      (-3*LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], Coupling[Ms, {}, 0]}, 
         {3, 1, -1}] + LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], 
         Coupling[Ms, {}, 0]}, {4, 1, -2}])))/30, 
 Coupling[cuG, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (hbar*Coupling[gs, {}, 0]*Coupling[yDM, {Index[d$$2, Flavor], 
      Index[d$$1, Flavor]}, 0]*Coupling[yDM, {Index[i2, Flavor], 
      Index[d$$1, Flavor]}, 0]*Coupling[Yu, {Index[i1, Flavor], 
      Index[d$$2, Flavor]}, 0]*
    (-LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], Coupling[Ms, {}, 0]}, 
       {3, 1, -1}] + LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], 
       Coupling[Ms, {}, 0]}, {4, 1, -2}]))/4, 
 Coupling[cuH, {Index[i1_, Flavor], Index[i2_, Flavor]}, 0] -> 
  (hbar*(Coupling[yDM, {Index[d$$2, Flavor], Index[d$$1, Flavor]}, 0]*
      Coupling[yDM, {Index[i2, Flavor], Index[d$$1, Flavor]}, 0]*
      Coupling[yHs, {}, 0]*Coupling[Yu, {Index[i1, Flavor], 
        Index[d$$2, Flavor]}, 0]*
      (2*LF[{Coupling[Ms, {}, 0], Coupling[MT, {Index[d$$1, Flavor]}, 0]}, 
         {2, 1, 0}] - LF[{Coupling[Ms, {}, 0], Coupling[MT, 
          {Index[d$$1, Flavor]}, 0]}, {2, 2, -1}]) - 
     4*Bar[Coupling[Yu, {Index[d$$1, Flavor], Index[d$$2, Flavor]}, 0]]*
      Coupling[yDM, {Index[d$$2, Flavor], Index[d$$3, Flavor]}, 0]*
      Coupling[yDM, {Index[d$$4, Flavor], Index[d$$3, Flavor]}, 0]*
      Coupling[Yu, {Index[d$$1, Flavor], Index[i2, Flavor]}, 0]*
      Coupling[Yu, {Index[i1, Flavor], Index[d$$4, Flavor]}, 0]*
      (LF[{Coupling[MT, {Index[d$$3, Flavor]}, 0], Coupling[Ms, {}, 0]}, 
        {2, 1, 0}] - 2*LF[{Coupling[MT, {Index[d$$3, Flavor]}, 0], 
          Coupling[Ms, {}, 0]}, {3, 1, -1}] + 
       LF[{Coupling[MT, {Index[d$$3, Flavor]}, 0], Coupling[Ms, {}, 0]}, 
        {4, 1, -2}])))/8, 
 Coupling[cuu, {Index[i1_, Flavor], Index[i2_, Flavor], Index[i3_, Flavor], 
    Index[i4_, Flavor]}, 0] -> 
  (hbar*(18*Coupling[gs, {}, 0]^4*(-3*Delta[Index[i1, Flavor], 
         Index[i4, Flavor]]*Delta[Index[i2, Flavor], Index[i3, Flavor]] + 
       Delta[Index[i1, Flavor], Index[i2, Flavor]]*Delta[Index[i3, Flavor], 
         Index[i4, Flavor]])*FlavorSum[Index[d$$1, Flavor]] - 
     8*Coupling[gY, {}, 0]^2*Delta[Index[i1, Flavor], Index[i2, Flavor]]*
      (16*Coupling[gY, {}, 0]^2*Delta[Index[i3, Flavor], Index[i4, Flavor]]*
        FlavorSum[Index[d$$1, Flavor]] + 
       15*Coupling[MT, {Index[d$$1, Flavor]}, 0]^2*Coupling[yDM, 
         {Index[i3, Flavor], Index[d$$1, Flavor]}, 0]*
        Coupling[yDM, {Index[i4, Flavor], Index[d$$1, Flavor]}, 0]*
        (3*LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], Coupling[Ms, {}, 0]}, 
           {3, 1, -1}] - LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], 
           Coupling[Ms, {}, 0]}, {4, 1, -2}])) + 45*Coupling[gs, {}, 0]^2*
      Coupling[MT, {Index[d$$1, Flavor]}, 0]^2*Coupling[yDM, 
       {Index[i4, Flavor], Index[d$$1, Flavor]}, 0]*
      (Coupling[yDM, {Index[i3, Flavor], Index[d$$1, Flavor]}, 0]*
        Delta[Index[i1, Flavor], Index[i2, Flavor]] - 
       3*Coupling[yDM, {Index[i1, Flavor], Index[d$$1, Flavor]}, 0]*
        Delta[Index[i2, Flavor], Index[i3, Flavor]])*
      (3*LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], Coupling[Ms, {}, 0]}, 
         {3, 1, -1}] - LF[{Coupling[MT, {Index[d$$1, Flavor]}, 0], 
         Coupling[Ms, {}, 0]}, {4, 1, -2}])))/
   (1620*Coupling[MT, {Index[d$$1, Flavor]}, 0]^2)}
