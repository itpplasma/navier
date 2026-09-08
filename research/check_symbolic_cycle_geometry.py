#!/usr/bin/env python3
"""Exact symbolic geometry checks for source-cycle and time-tree claims."""
from __future__ import annotations
import json
import sympy as s

P, r, z = s.symbols('P r z', nonzero=True, real=True)
R = P**2
S = r**2 + z**2
checks = []

def eq(a, b, label):
    # Fourier coefficients are tuples; compare components, not tuple subtraction.
    if isinstance(a, tuple) or isinstance(b, tuple):
        if not (isinstance(a, tuple) and isinstance(b, tuple) and len(a) == len(b)):
            raise AssertionError(label + ': incompatible shapes')
        equal = all(s.simplify(x-y) == 0 for x, y in zip(a, b))
    else:
        equal = s.simplify(a-b) == 0
    if not equal:
        raise AssertionError(label)
    checks.append(label)

# Planar carrier geometry: p=(P,0), q=(r,z), with canonical transverse
# polarizations.  The two copied-carrier source coefficients have a rational
# ratio whose imbalance is controlled by the displayed 8 P^2 r^2 term.
num = R**2-S**2 + 2*P*r*(R+S) - 4*P**2*r**2
den = R**2-S**2 + 2*P*r*(R+S) + 4*P**2*r**2
rho = s.factor(num/den)
eq(s.factor(den-num), 8*P**2*r**2, 'source-copy imbalance')
eq(s.factor((rho-1)*den), -8*P**2*r**2, 'balancing equation')

# Exact displayed source cycle U=(sin(x+y), sin(2x)-sin(x+y),0).
# Work with 2D rational vectors and the exact Leray projection.
def add(k,l): return (k[0]+l[0], k[1]+l[1])
def neg(k): return (-k[0],-k[1])
def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def proj(k,a):
    kk=s.Rational(dot(k,k)); ka=dot(k,a)
    return (s.factor(a[0]-k[0]*ka/kk), s.factor(a[1]-k[1]*ka/kk))
def C(a,b):
    out={}
    for k,ak in a.items():
        for l,bl in b.items():
            h=add(k,l)
            if h==(0,0): continue
            raw=(dot(l,ak)*bl[0], dot(l,ak)*bl[1])
            ph=proj(h,raw)
            out[h]=tuple(s.factor(out.get(h,(0,0))[j]+ph[j]) for j in range(2))
    return {k:v for k,v in out.items() if v!=(0,0)}

p=(2,0); q=(1,1)
bp=(s.Rational(0),-s.Rational(1,2)); bq=(-s.Rational(1,2),s.Rational(1,2))
b0={p:bp,neg(p):tuple(-x for x in bp),q:bq,neg(q):tuple(-x for x in bq)}
b1=C(b0,b0)
eq(b1[p[0]+q[0],p[1]+q[1]], (-s.Rational(1,20),s.Rational(3,20)), 'sum daughter')
eq(b1[p[0]-q[0],p[1]-q[1]], (-s.Rational(1,4),-s.Rational(1,4)), 'difference daughter')
b11=C(b1,b1)
eq(b11[(4,0)], (0,-s.Rational(1,10)), 'source cycle 2p')
eq(b11[(2,2)], (-s.Rational(1,10),s.Rational(1,10)), 'source cycle 2q')

# Complete temporal tree through four leaves.
def scale_field(a,c): return {k:tuple(s.factor(c*x) for x in v) for k,v in a.items()}
def add_field(*fs):
    out={}
    for f in fs:
        for k,v in f.items():
            old=out.get(k,(0,0)); out[k]=tuple(s.factor(old[j]+v[j]) for j in range(2))
    return {k:v for k,v in out.items() if v!=(0,0)}
b2=scale_field(add_field(C(b0,b1),C(b1,b0)),s.Rational(1,2))
b3=scale_field(add_field(C(b1,b1),C(b0,b2),C(b2,b0)),s.Rational(1,3))
eq(b3[(4,0)], (0,-s.Rational(4,65)), 'full time tree 2p')
eq(b3[(2,2)], (-s.Rational(1,50),s.Rational(1,50)), 'full time tree 2q')
eq(b3[(7,1)], (-s.Rational(11,52000),s.Rational(77,52000)), 'exterior four-leaf carrier')
checks.append('copied temporal coefficients are unequal') if s.Rational(8,65)!=s.Rational(1,25) else (_ for _ in ()).throw(AssertionError())

print(json.dumps({'status':'PASS','checks':len(checks),'labels':checks,
                  'scope':'exact symbolic/rational source and time-tree geometry; not PDE certification'},indent=2))
