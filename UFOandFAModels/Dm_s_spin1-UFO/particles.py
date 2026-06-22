# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Linux x86 (64-bit) (July 16, 2024)
# Date: Mon 22 Jun 2026 17:31:18


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

g = Particle(pdg_code = 21,
             name = 'g',
             antiname = 'g',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'g',
             antitexname = 'g',
             charge = 0,
             GhostNumber = 0)

ghG = Particle(pdg_code = 82,
               name = 'ghG',
               antiname = 'ghG~',
               spin = -1,
               color = 8,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'ghG',
               antitexname = 'ghG~',
               charge = 0,
               GhostNumber = 1)

ghG__tilde__ = ghG.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'u~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'u~',
             charge = 2/3,
             GhostNumber = 0)

u__tilde__ = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'c~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'c~',
             charge = 2/3,
             GhostNumber = 0)

c__tilde__ = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 't~',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = 't~',
             charge = 2/3,
             GhostNumber = 0)

t__tilde__ = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'd~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'd~',
             charge = -1/3,
             GhostNumber = 0)

d__tilde__ = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 's~',
             spin = 2,
             color = 3,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 's',
             antitexname = 's~',
             charge = -1/3,
             GhostNumber = 0)

s__tilde__ = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'b~',
             spin = 2,
             color = 3,
             mass = Param.MB,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'b~',
             charge = -1/3,
             GhostNumber = 0)

b__tilde__ = b.anti()

Xr = Particle(pdg_code = 5000511,
              name = 'Xr',
              antiname = 'Xr',
              spin = 1,
              color = 1,
              mass = Param.MXr,
              width = Param.ZERO,
              texname = 'Xr',
              antitexname = 'Xr',
              charge = 0,
              GhostNumber = 0)

Xc = Particle(pdg_code = 5000512,
              name = 'Xc',
              antiname = 'Xc~',
              spin = 1,
              color = 1,
              mass = Param.MXc,
              width = Param.ZERO,
              texname = 'Xc',
              antitexname = 'Xc~',
              charge = 0,
              GhostNumber = 0)

Xc__tilde__ = Xc.anti()

Xd = Particle(pdg_code = 5000521,
              name = 'Xd',
              antiname = 'Xd~',
              spin = 2,
              color = 1,
              mass = Param.MXd,
              width = Param.ZERO,
              texname = 'Xd',
              antitexname = 'Xd~',
              charge = 0,
              GhostNumber = 0)

Xd__tilde__ = Xd.anti()

Y1 = Particle(pdg_code = 5000001,
              name = 'Y1',
              antiname = 'Y1',
              spin = 3,
              color = 1,
              mass = Param.MY1,
              width = Param.WY1,
              texname = 'Y1',
              antitexname = 'Y1',
              charge = 0,
              GhostNumber = 0)

