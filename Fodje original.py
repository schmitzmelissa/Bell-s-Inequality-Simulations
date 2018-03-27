from __future__ import division
import numpy
from clifford import *
layout, blades = Cl(3,0)
e0, e1, e2 = [blades['e%i'%k] for k in range(3)]
I = (e0^e1^e2)

def randVec3d(lo=0, hi=2*numpy.pi):
    theta = numpy.random.uniform(lo, hi)
    z = numpy.random.uniform(-1, 1)
    sn = numpy.sqrt(1-z**2)
    y = sn*numpy.sin(theta)
    x = sn*numpy.cos(theta)
    return (x^e0) + (y^e1) + (z^e2)

N = 20000
s = 0
a = randVec3d()
b = randVec3d()

for i in range(N):
    L = numpy.random.choice([-1., 1.])
    mu = L&I
    C = (-I)*a
    D = I*b
    E = mu*a
    F = mu*b
    A = C&E
    B = F&D
    q = ((-C)&A&B&(-D)) if L == 1 else ((-D)&B&A&(-C))
    s = s+q

print s^(1./N)
print -(a*b)

# Typical Run
#
# 0.44353 - (0.00776^e01) - (0.0068^e02) + (0.00131^e12) # Model
# 0.44353 # -a.b
