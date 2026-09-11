#!/usr/bin/env python3
"""Exact damping-compatible state-triggered Raman basis.

Five explicit Raman shifts span Sym_0(3) at the clean algebraic root.  For each
module, every translated original parent, first-generation carrier and other
second target is either absent or strictly damped by the common M=2048 filter.
The complete inherited ladder is also strictly damped for every n>=1.
"""
from __future__ import annotations
import sympy as sp

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

z,N,n=sp.symbols('z N n', real=True)
lo=sp.Rational(12847,10000); hi=sp.Rational(803,625); mid=(lo+hi)/2
Qclean=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)
check(Qclean.eval(lo)<0 and Qclean.eval(hi)>0 and Qclean.count_roots(lo,hi)==1,
      'unique positive clean root isolated')

H=sp.Matrix([
 [sp.Rational(71,100),-1,sp.Rational(147,200)],
 [-1,sp.Rational(-143,200),sp.Rational(7,25)],
 [sp.Rational(147,200),sp.Rational(7,25),sp.Rational(1,200)],
])
Mstrength=sp.Integer(2048)
check(H==H.T and sp.trace(H)==0,'inheritance filter symmetric trace free')

# Actual ancestry-contaminated middle target, common -i phase removed.
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
a=sp.Matrix([sp.cancel(x) for x in pure+other])
h=sp.Matrix([z-2,-1,-1])
check(sp.simplify(h.dot(a))==0,'actual middle trigger transverse')

dens=[sp.denom(x) for x in a]
D=dens[0]
for d in dens[1:]: D=sp.lcm(D,d)
A=sp.Matrix([sp.expand(sp.cancel(D*x)) for x in a])
check(sp.factor(h.dot(A))==0,'cleared trigger transverse')

# Search-selected basis, now frozen exactly.
GEOM=[
 ((-3,0,0),(0,3,-1)),
 ((-2,-2,1),(2,-2,0)),
 ((-2,2,0),(2,2,-1)),
 ((0,-3,0),(2,0,-2)),
 ((-1,-2,-2),(0,2,-2)),
]


def dscaled(k,l,Q):
    """Positive scalar multiple of P_{k+l}[(l.(k+l))l-(m.(k+l))m]."""
    k=sp.Matrix(k); l=sp.Matrix(l); Q=sp.Matrix(Q)
    ko=k+l; m=Q.cross(l)
    W=sp.expand((l.dot(ko))*l-(m.dot(ko))*m)
    k2=sp.expand(ko.dot(ko))
    return ko,sp.expand(k2*W-ko*(ko.dot(W)))


def rate_numerator(k,l,Q):
    ko,d=dscaled(k,l,Q)
    if all(sp.simplify(x)==0 for x in d):
        return None
    d2=sp.expand(d.dot(d))
    dHd=sp.expand((d.T*H*d)[0])
    return sp.factor(-Mstrength*dHd-sp.expand(ko.dot(ko))*d2)

# Exact state-triggered span columns.  The common denominator D and positive
# Leray denominator factors are cleared, which does not affect rank.
cols=[]
for j,(lt,qt) in enumerate(GEOM):
    l=sp.Matrix(lt); qdir=sp.Matrix(qt); m=qdir.cross(l)
    check(l.dot(qdir)==0,f'module {j}: l perpendicular Q')

    # Equal-length near-opposite parents and exact direct Leray silence.
    l2=l.dot(l); q2=qdir.dot(qdir)
    q=l/2+N*qdir; r=l/2-N*qdir
    beta=l-(l2/(2*N*q2))*qdir+m
    eps=l+(l2/(2*N*q2))*qdir-m
    check(sp.simplify(q.dot(beta))==0,f'module {j}: q.beta=0')
    check(sp.simplify(r.dot(eps))==0,f'module {j}: r.eps=0')
    direct=(beta.dot(r))*eps+(eps.dot(q))*beta
    check(sp.simplify(direct-2*l2*l)==sp.zeros(3,1),
          f'module {j}: direct high-high source longitudinal')

    kappa=h+l
    W=sp.expand(2*(A.dot(qdir))*((l.dot(kappa))*l-(m.dot(kappa))*m))
    k2=sp.expand(kappa.dot(kappa))
    d=sp.expand(k2*W-kappa*(kappa.dot(W)))
    check(sp.expand(kappa.dot(d))==0,f'module {j}: triggered output transverse')
    S=(d*kappa.T+kappa*d.T)/2
    check(sp.expand(sp.trace(S))==0,f'module {j}: triggered strain trace free')
    cols.append(sp.Matrix([
        sp.expand(S[0,0]),sp.expand(S[1,1]),sp.expand(S[0,1]),
        sp.expand(S[0,2]),sp.expand(S[1,2])]))

Span=sp.Matrix.hstack(*cols)
det=sp.expand(Span.det(method='berkowitz'))
Pdet=sp.Poly(det,z)
check(Pdet.degree()==70,'damping-compatible span determinant degree 70')
check(sp.gcd(Pdet,Qclean).degree()==0,
      'span determinant coprime to clean return polynomial')
check(Pdet.eval(mid)!=0,'span determinant midpoint calibration nonzero')

# No translated tracked carrier may collide with a desired Raman output or a
# clean second-target window at the clean algebraic root.
tracked=[
 ('p1',sp.Matrix([1,0,0])),
 ('p2',sp.Matrix([0,1,0])),
 ('p3',sp.Matrix([-z,0,1])),
 ('g1',sp.Matrix([-1,-1,0])),
 ('g2',sp.Matrix([1+z,0,-1])),
 ('g3',sp.Matrix([1-z,0,1])),
 ('h+',sp.Matrix([-z,1,1])),
 ('h-',sp.Matrix([-z,-1,1])),
]
Ls=[sp.Matrix(x[0]) for x in GEOM]
desired=[h+l for l in Ls]
target_windows=[sp.Matrix([-z,1,1]),h,sp.Matrix([-z,-1,1])]

def distinct_at_clean_root(u,v,label):
    diffs=[sp.expand(u[i]-v[i]) for i in range(3)]
    for x in diffs:
        if x==0: continue
        p=sp.Poly(x,z)
        check(sp.gcd(p,Qclean).degree()==0,label)
        return
    raise AssertionError(label+': vectors are identically equal')

for j,(lt,qt) in enumerate(GEOM):
    l=sp.Matrix(lt)
    for name,k in tracked:
        ko=k+l
        for rnum,kd in enumerate(desired):
            distinct_at_clean_root(ko,kd,
                f'module {j} {name}: no collision with desired {rnum}')
        for rnum,kt in enumerate(target_windows):
            distinct_at_clean_root(ko,kt,
                f'module {j} {name}: no collision with target window {rnum}')

# Every first-order translated finite tracked carrier is strictly damped on the
# whole clean-root isolating interval.  Zero effective outputs are harmless.
for j,(lt,qt) in enumerate(GEOM):
    for name,k in tracked:
        rn=rate_numerator(k,lt,qt)
        if rn is None:
            CHECKS.append(f'module {j} {name}: effective output identically zero')
            continue
        p=sp.Poly(sp.expand(rn),z)
        check(p.count_roots(lo,hi)==0,
              f'module {j} {name}: rate numerator root-free on clean interval')
        check(p.eval(mid)<0,
              f'module {j} {name}: translated carrier strictly damped')

# Complete inherited ladder r_n=(-n,-1,0), n>=1.  The rate numerators are
# z-independent polynomials.  Prove -rate>0 on [1,infinity) by Sturm count.
for j,(lt,qt) in enumerate(GEOM):
    rn=rate_numerator(sp.Matrix([-n,-1,0]),lt,qt)
    if rn is None:
        CHECKS.append(f'module {j}: inherited ladder effective output zero')
        continue
    num,den=map(sp.factor,sp.together(-rn).as_numer_denom())
    check(den>0,f'module {j}: ladder sign denominator positive')
    p=sp.Poly(num,n)
    check(p.eval(1)>0,f'module {j}: ladder positive calibration at n=1')
    check(p.count_roots(1,sp.oo)==0,
          f'module {j}: ladder rate strictly negative for all n>=1')

print(f'PASS: {len(CHECKS)} exact assertions.')
print('Five Raman modules span Sym_0(3) at the clean root and have no first-order required-window collisions.')
print('All translated tracked finite carriers and the complete inherited ladder are strictly damped by H at M=2048.')
print('Scope: leading effective Raman slow operator only; repeated Raman translations and full PDE realization remain open.')
