#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selm_lammps.lammps import IPyLammps
L=IPyLammps();

import numpy as np


# In[2]:


s="""
atom_style	atomic
neighbor	0.3 bin
neigh_modify	delay 5

# create geometry

lattice		fcc 3.52
region		box block 0 100 0 100 0 100
create_box	3 box
create_atoms	1 box"""

for line in s.splitlines():
 # print_log(line);
  L.command(line);


# In[3]:


x=np.random.uniform(3,97,10)
y=np.random.uniform(3,97,10)
z=np.random.uniform(3,97,10)

points=list(zip(x,y,z))


# In[4]:


points


# In[5]:


j=1
for i in points:
    L.region(j,"sphere",i[0],i[1],i[2],3)
    j=j+1


# In[6]:


s="""
info all out
"""

#print_log("Sending commands to LAMMPs");
for line in s.splitlines():
 # print_log(line);
  L.command(line);


# In[8]:


s="""
info all out
"""

#print_log("Sending commands to LAMMPs");
for line in s.splitlines():
 # print_log(line);
  L.command(line);


# In[ ]:




