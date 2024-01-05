# import the lammps module
try:  
  from selm_lammps.lammps import IPyLammps # use this for the pip install of pre-built package
  lammps_import_comment = "from selm_lammps.lammps import IPyLammps";  
  from selm_lammps import util as atz_util;
except Exception as e:  
  from lammps import IPyLammps # use this for direct install of package
  lammps_import_comment = "from lammps import IPyLammps";
  from atz_lammps import util as atz_util;
except Exception as e: # if fails to import, report the exception   
  print(e);
  lammps_import_comment = "import failed";

import numpy as np;
import matplotlib;
import matplotlib.pyplot as plt;
import sys,shutil,pickle,pdb;

import logging;

L = IPyLammps();
atz_util.print_version_info(L);    

s="""

# 2d LJ obstacle flow

dimension	2
boundary	p s p

atom_style	atomic
neighbor	0.3 bin
neigh_modify	delay 5

# create geometry

lattice		hex 0.7
region		box block 0 40 0 10 -0.25 0.25
create_box	3 box
create_atoms	1 box

mass		1 1.0
mass		2 1.0
mass		3 1.0

# LJ potentials

pair_style	lj/cut 1.12246
pair_coeff	* * 1.0 1.0 1.12246

# define groups

region	        1 block INF INF INF 1.25 INF INF
group		lower region 1
region		2 block INF INF 8.75 INF INF INF
group		upper region 2
group		boundary union lower upper
group		flow subtract all boundary

set		group lower type 2
set		group upper type 3

# initial velocities

compute	        mobile flow temp
velocity	flow create 1.0 482748 temp mobile
fix		1 all nve
fix		2 flow temp/rescale 200 1.0 1.0 0.02 1.0
fix_modify	2 temp mobile

# Poiselle flow

velocity	boundary set 0.0 0.0 0.0
fix		3 lower setforce 0.0 0.0 0.0
fix		4 upper setforce 0.0 NULL 0.0
fix		5 upper aveforce 0.0 -0.5 0.0
fix		6 flow addforce 1.0 0.0 0.0
"""
print_log("Sending commands to LAMMPs");
for line in s.splitlines():
  print_log(line);
  L.command(line);

x=np.random.uniform(4,36,2)
y=np.random.uniform(4,36,2)


points=list(zip(x,y,z))

j=3                                                  
for i in points:
    L.region(j,"sphere",i[0],i[1],i[2],3)
    j=j+1

original="delete_atoms region "
for j in range(3,5):
    line1=original+str(j)
    line2="fix "+ str(j) +" flow indent "+str(100)+" sphere "+ str(points[j-3][0])+" "+str(points[j-3][1])+" "+str(4)
    L.command(line1)
    print_log(line1)
    L.command(line2)
    print_log(line2)

s="""
fix		9 all enforce2d

# Run

timestep	0.003
thermo		1000
thermo_modify	temp mobile

dump		1 all atom 100 dump.obstacle

#dump		2 all image 500 image.*.jpg type type &
#		zoom 1.6 adiam 1.5
#dump_modify	2 pad 5

#dump		3 all movie 500 movie.mpg type type &
#		zoom 1.6 adiam 1.5
#dump_modify	3 pad 5

run		25000
"""
print_log("Sending commands to LAMMPs");
for line in s.splitlines():
  print_log(line);
  L.command(line);

