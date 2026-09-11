#!/usr/bin/env python3
"""Exact cubic unstable pollution of the factor-two source relay."""
import sympy as s

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

mu=s.Rational(3,5)
K0=s.Matrix([[0,1,0],[1,0,0],[0,0,0]])
def P(k):
    k=s.Matrix(k); return s.eye(3)-k*k.T/k.dot(k)
def ap(sig): return s.Matrix([1,-s.sqrt(1+sig*sig),-sig])
def keyvec(key): return s.Matrix([s.Rational(key[0],10),0,s.Integer(key[1])])
def proj_key(key):
    k=keyvec(key); return s.eye(3)-k*k.T/k.dot(k)
def addkey(a,b): return (a[0]+b[0],a[1]+b[1])
def linear(key,v):
    k=keyvec(key); A=-K0+k*(k.T*K0)/k.dot(k)
    return A*v-mu*k.dot(k)*v
def ordered_pair(kp,a,kq,b):
    kk=addkey(kp,kq)
    if kk==(0,0): return kk,s.zeros(3,1)
    q=keyvec(kq)
    return kk,-s.I*proj_key(kk)*(a.dot(q))*b
def add(D,k,v): D[k]=D.get(k,s.zeros(3,1))+v
def linear_dict(U): return {k:linear(k,v) for k,v in U.items()}
def nonlinear_dict(U,V):
    out={}
    for kp,a in U.items():
        for kq,b in V.items():
            kk,val=ordered_pair(kp,a,kq,b)
            if kk!=(0,0): add(out,kk,val)
    return out
def eigcoords(k,f):
    k,f=s.Matrix(k),s.Matrix(f); c=s.simplify(k[0]/k[2]); q=s.sqrt(1+c*c)
    return s.simplify((f[0]-f[1]/q)/2),s.simplify((f[0]+f[1]/q)/2)

# Pair A from the four-parent cage.  Unit amplitudes suffice to compute the
# universal coefficient multiplying A1^2 conjugate(A2).
k1=(5,1); k2=(-4,1)
U0={k1:ap(s.Rational(1,2)), k2:ap(-s.Rational(2,5))}
U0[(-k1[0],-k1[1])]=U0[k1]
U0[(-k2[0],-k2[1])]=U0[k2]

# Complete U1 and U2 Taylor coefficients of the full source-reference ODE.
tmp={}
for k,v in linear_dict(U0).items(): add(tmp,k,v)
for k,v in nonlinear_dict(U0,U0).items(): add(tmp,k,v)
U1={k:s.simplify(v) for k,v in tmp.items()}

tmp={}
for k,v in linear_dict(U1).items(): add(tmp,k,v)
for A,B in ((U0,U1),(U1,U0)):
    for k,v in nonlinear_dict(A,B).items(): add(tmp,k,v)
U2={k:s.simplify(v/2) for k,v in tmp.items()}

# Extreme cubic sideband.  Frequency arithmetic among the full four-parent
# set {5,-4,2,-1} shows 14=5+5-(-4) is the UNIQUE two-positive/one-negative
# representation, so its coefficient is proportional only to A1^2 conj(A2).
target=(14,1)
v=U2[target]
check(s.simplify(keyvec(target).dot(v))==0,'extreme cubic sideband is transverse')
cp,cm=eigcoords(keyvec(target),v)
expected=-s.Rational(9,29600)*(-11+20*s.sqrt(370)+9*s.sqrt(2146))
check(s.simplify(cp-expected)==0,'exact extreme-sideband growing coordinate')
check(cp<0,'extreme-sideband growing coordinate is strictly nonzero')
# Positivity is elementary: 20 sqrt(370)>380>11.
check(20*s.sqrt(370)>11,'radical sign certificate')

# Unique cubic frequency representation inside the complete four-parent set.
xs=[5,-4,2,-1]
reps=[]
for i,x in enumerate(xs):
    for j,y in enumerate(xs):
        for h,z in enumerate(xs):
            if x+y-z==14:
                reps.append((i,j,h))
check(set(reps)=={(0,0,1)},'A1^2 conjugate(A2) is the unique cubic monomial at key 14')

# At the next factor-two normalization, target/2 has axial scale z=1/2 and
# unchanged tilt s=7/5.  Its + branch is strictly growing.
sig=s.Rational(7,5); z=s.Rational(1,2); q=s.sqrt(1+sig*sig)
rate=s.simplify(1/q-mu*z*z*q*q)
expected_rate=5/s.sqrt(74)-s.Rational(111,250)
check(s.simplify(rate-expected_rate)==0,'exact next-stage half-scale growth rate')
check(rate>0,'cubic pollutant is linearly unstable after factor-two renormalization')
# Exact rational square check for 5/sqrt(74)>111/250.
check(1250**2>111**2*74,'positive-rate integer square certificate')

# Desired doubled-parent coefficients first occur in U3 (quartic amplitude),
# whereas this pollutant is already U2 (cubic amplitude).
check(target not in U0 and target not in U1 and target in U2,
      'pollutant first appears at cubic amplitude order')

print(f'PASS: {len(CHECKS)} exact assertions.')
print('The four-parent factor-two relay unavoidably emits a cubic m=5 sideband.')
print('After factor-two renormalization that sideband is a growing half-scale mode.')
print('It appears one nonlinear order earlier than the desired quartic doubled-parent relay.')
