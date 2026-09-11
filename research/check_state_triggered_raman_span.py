#!/usr/bin/env python3
"""Exact state-triggered Raman span for the actual contaminated middle target.

Five explicit near-opposite high-pair geometries have zero direct quadratic
low output after Leray projection.  Their leading two-step action on the
actual ancestry-contaminated middle second target spans Sym_0(3) at the clean
root, hence in particular spans the common inheritance filter H.
"""
from __future__ import annotations
import sympy as sp

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

z,N=sp.symbols('z N', real=True, positive=True)
lo=sp.Rational(12847,10000); hi=sp.Rational(803,625)
Qclean=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)
check(Qclean.eval(lo)<0 and Qclean.eval(hi)>0 and Qclean.count_roots(lo,hi)==1,
      'unique positive clean root isolated')

# Actual full leading coefficient at h=(-2,-1,-1), with its common -i phase
# removed: pure selected child-child contribution plus all old-parent/second-jet
# contributions frozen in check_clean_gate_second_generation_wall.py.
pure=sp.Matrix([
 2*z*(z**3+2*z-4)/(3*(z**2-4*z+6)),
 2*z*(z**4-8*z**3+14*z**2-16*z+8)/(3*(z**2-4*z+6)*(z**2-2*z+2)),
 2*z*(z**6-4*z**5+7*z**4-8*z**3+14*z**2-16*z+8)/(3*(z**2-4*z+6)*(z**2-2*z+2)),
])
other=sp.Matrix([
 (5*z**10-32*z**9+89*z**8-120*z**7+67*z**6-12*z**5+159*z**4-396*z**3+412*z**2-176*z+20)/(6*(z**2-4*z+5)*(z**2-4*z+6)*(z**2-2*z+2)*(z**2-2*z+3)),
 (4*z**7-31*z**6+85*z**5-132*z**4+89*z**3-3*z**2-42*z+10)/(3*(z**2-4*z+6)*(z**2-2*z+2)*(z**2-2*z+3)),
 (5*z**11-42*z**10+145*z**9-204*z**8-151*z**7+1108*z**6-1901*z**5+1324*z**4+374*z**3-1326*z**2+872*z-140)/(6*(z**2-4*z+5)*(z**2-4*z+6)*(z**2-2*z+2)*(z**2-2*z+3)),
])
a=sp.Matrix([sp.cancel(x) for x in (pure+other)])
h=sp.Matrix([z-2,-1,-1])
check(sp.simplify(h.dot(a))==0,'actual contaminated trigger is transverse')

# Clear the common trigger denominator once.  All span tests are invariant
# under this common nonzero scalar.
dens=[sp.denom(x) for x in a]
D=dens[0]
for d in dens[1:]: D=sp.lcm(D,d)
A=sp.Matrix([sp.expand(sp.cancel(D*x)) for x in a])
check(sp.factor(h.dot(A))==0,'cleared trigger remains transverse')

H=sp.Matrix([
 [sp.Rational(71,100),-1,sp.Rational(147,200)],
 [-1,sp.Rational(-143,200),sp.Rational(7,25)],
 [sp.Rational(147,200),sp.Rational(7,25),sp.Rational(1,200)],
])
check(H==H.T and sp.trace(H)==0,'inheritance filter lies in Sym_0(3)')

def P(k,v):
    return sp.simplify(v-k*(k.dot(v))/k.dot(k))

def C(p,u,q,v):
    return P(p+q,(u.dot(q))*v+(v.dot(p))*u)

# Five small integer geometries.  In every row l.Q=0.
GEOM=[
 ((1,0,-1),(1,-1,1)),
 ((1,-1,0),(1,1,-1)),
 ((0,1,-1),(1,-1,-1)),
 ((1,1,0),(1,-1,1)),
 ((0,1,1),(1,-1,1)),
]

cols=[]
for j,(lt,qt) in enumerate(GEOM):
    l=sp.Matrix(lt); qdir=sp.Matrix(qt)
    check(l.dot(qdir)==0,f'module {j}: l perpendicular Q')
    m=qdir.cross(l)
    l2=l.dot(l); q2=qdir.dot(qdir)

    # Equal-length near-opposite high wavevectors and paired polarizations.
    q=l/2+N*qdir
    r=l/2-N*qdir
    beta=l-(l2/(2*N*q2))*qdir+m
    eps=l+(l2/(2*N*q2))*qdir-m
    check(sp.simplify(q.dot(beta))==0,f'module {j}: first high parent transverse')
    check(sp.simplify(r.dot(eps))==0,f'module {j}: second high parent transverse')

    # Their direct output at l is pure longitudinal pressure and Leray-zero.
    direct=C(q,beta,r,eps)
    check(all(sp.simplify(x)==0 for x in direct),f'module {j}: direct high-high output vanishes')

    # For kappa=h+l, the exact high-N two-step symbol has one scale-separation
    # loss.  With beta_0=l+m and eps_0=l-m,
    #   N^{-1} C(h+q,C(h,A;q,beta);r,eps)
    # -> 2 (A.Q) P_kappa[(l.kappa)l-(m.kappa)m].
    kappa=h+l
    W=sp.expand(2*(A.dot(qdir))*((l.dot(kappa))*l-(m.dot(kappa))*m))
    k2=sp.expand(kappa.dot(kappa))
    dscaled=sp.expand(k2*W-kappa*(kappa.dot(W))) # k2 times effective output
    check(sp.expand(kappa.dot(dscaled))==0,f'module {j}: effective output transverse')

    # Encode a trace-free symmetric tensor by (xx,yy,xy,xz,yz); zz=-xx-yy.
    S=(dscaled*kappa.T+kappa*dscaled.T)/2
    check(sp.expand(sp.trace(S))==0,f'module {j}: effective strain trace free')
    cols.append(sp.Matrix([
        sp.expand(S[0,0]),sp.expand(S[1,1]),sp.expand(S[0,1]),
        sp.expand(S[0,2]),sp.expand(S[1,2])]))

M=sp.Matrix.hstack(*cols)
det=sp.expand(M.det(method='berkowitz'))
Pdet=sp.Poly(det,z)
check(Pdet.degree()==71,'span determinant has expected exact degree')
check(Pdet.count_roots(lo,hi)==0,'span determinant has no zero in clean-root interval')
check(Pdet.eval((lo+hi)/2)>0,'span determinant positive calibration')

# Therefore the five effective tensors form a basis of Sym_0(3), so H is in
# their span.  Check the target coordinate vector is well-defined at midpoint.
hvec=sp.Matrix([H[0,0],H[1,1],H[0,1],H[0,2],H[1,2]])
Mmid=M.subs(z,(lo+hi)/2)
coeff=Mmid.inv()*hvec
check(Mmid*coeff==hvec,'five triggered strains synthesize H at calibration point')

print(f'PASS: {len(CHECKS)} exact assertions.')
print('Five state-triggered Raman modules span Sym_0(3) throughout the clean-root interval.')
print('Each preloaded high pair is exactly Leray-silent at its own low difference frequency.')
print('Scope: high-frequency effective Fourier-symbol theorem; time-integrated PDE realization and off-target Raman clutter remain open.')
