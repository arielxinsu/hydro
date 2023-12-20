#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from lammps import IPyLammps
L=IPyLammps();

random.seed(27848)
deltaperturb = 0.2

for i in range(L.system.natoms):
    x, y = L.atoms[i].position
    dx = deltaperturb * random.uniform(-1, 1)
    dy = deltaperturb * random.uniform(-1, 1)
    L.atoms[i].position  = (x+dx, y+dy)

L.run(0)

