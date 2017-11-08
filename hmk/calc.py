from __future__ import division
import numpy as np

meV = 1.6e-3
amu = 1.66e-27

r0 = 2.7e-2
r1 = 2.5e-2
X = 7.22e-2
R1 = X**2 + r1**2
r2 = 0.95e-2/2 #measured
A2 = np.pi*r2**2
e = 1.6e-19
z = 2
Z = 79
E = 5.5*meV

A1 = np.pi*(r0**2 - r1**2)
t = 1.25e-6
NA = 6e23
Ag = 197.2*amu
p = 19.3e3 #from wikipedia article for gold

n = (p*NA/Ag)*A1*t
G = n*A2/(R1**2 * r1**2) * (Z**2 * z**2 *e**4)/(16*E**2)
print n
print G
print 100/G