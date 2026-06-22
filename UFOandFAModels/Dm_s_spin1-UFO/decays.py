# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Linux x86 (64-bit) (July 16, 2024)
# Date: Mon 22 Jun 2026 17:31:18


from object_library import all_decays, Decay
import particles as P


Decay_Y1 = Decay(name = 'Decay_Y1',
                 particle = P.Y1,
                 partial_widths = {(P.Xc__tilde__,P.Xc):'((-(gVXc**2*MXc**2) + (gVXc**2*MY1**2)/4.)*cmath.sqrt(-4*MXc**2*MY1**2 + MY1**4))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.b,P.b__tilde__):'((-48*gAd33**2*MB**2 + 24*gVd33**2*MB**2 + 12*gAd33**2*MY1**2 + 12*gVd33**2*MY1**2)*cmath.sqrt(-4*MB**2*MY1**2 + MY1**4))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.b,P.d__tilde__):'((-MB**2 + MY1**2)*(-6*gAd31**2*MB**2 - 6*gVd31**2*MB**2 - (6*gAd31**2*MB**4)/MY1**2 - (6*gVd31**2*MB**4)/MY1**2 + 12*gAd31**2*MY1**2 + 12*gVd31**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.c,P.c__tilde__):'(MY1**2*(12*gAu22**2*MY1**2 + 12*gVu22**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.d,P.b__tilde__):'((-MB**2 + MY1**2)*(-6*gAd31**2*MB**2 - 6*gVd31**2*MB**2 - (6*gAd31**2*MB**4)/MY1**2 - (6*gVd31**2*MB**4)/MY1**2 + 12*gAd31**2*MY1**2 + 12*gVd31**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.d,P.d__tilde__):'(MY1**2*(12*gAd11**2*MY1**2 + 12*gVd11**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.s,P.s__tilde__):'(MY1**2*(12*gAd22**2*MY1**2 + 12*gVd22**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.t,P.t__tilde__):'((-48*gAu33**2*MT**2 + 24*gVu33**2*MT**2 + 12*gAu33**2*MY1**2 + 12*gVu33**2*MY1**2)*cmath.sqrt(-4*MT**2*MY1**2 + MY1**4))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.t,P.u__tilde__):'((-MT**2 + MY1**2)*(-6*gAu31**2*MT**2 - 6*gVu31**2*MT**2 - (6*gAu31**2*MT**4)/MY1**2 - (6*gVu31**2*MT**4)/MY1**2 + 12*gAu31**2*MY1**2 + 12*gVu31**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.u,P.t__tilde__):'((-MT**2 + MY1**2)*(-6*gAu31**2*MT**2 - 6*gVu31**2*MT**2 - (6*gAu31**2*MT**4)/MY1**2 - (6*gVu31**2*MT**4)/MY1**2 + 12*gAu31**2*MY1**2 + 12*gVu31**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.u,P.u__tilde__):'(MY1**2*(12*gAu11**2*MY1**2 + 12*gVu11**2*MY1**2))/(48.*cmath.pi*abs(MY1)**3)',
                                   (P.Xd,P.Xd__tilde__):'((-16*gAXd**2*MXd**2 + 8*gVXd**2*MXd**2 + 4*gAXd**2*MY1**2 + 4*gVXd**2*MY1**2)*cmath.sqrt(-4*MXd**2*MY1**2 + MY1**4))/(48.*cmath.pi*abs(MY1)**3)'})

Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.Y1,P.d):'((MB**2 - MY1**2)*(6*gAd31**2*MB**2 + 6*gVd31**2*MB**2 + (6*gAd31**2*MB**4)/MY1**2 + (6*gVd31**2*MB**4)/MY1**2 - 12*gAd31**2*MY1**2 - 12*gVd31**2*MY1**2))/(96.*cmath.pi*abs(MB)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.Y1,P.u):'((MT**2 - MY1**2)*(6*gAu31**2*MT**2 + 6*gVu31**2*MT**2 + (6*gAu31**2*MT**4)/MY1**2 + (6*gVu31**2*MT**4)/MY1**2 - 12*gAu31**2*MY1**2 - 12*gVu31**2*MY1**2))/(96.*cmath.pi*abs(MT)**3)'})

