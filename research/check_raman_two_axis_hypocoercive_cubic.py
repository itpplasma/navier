#!/usr/bin/env python3
"""Exact cubic hypocoercive selectivity for two-axis Raman export.

For u_t=(S-D)u with S the reality-paired Raman operator (S*=-S) and
D acting by |k|^2 on each slow Fourier mode, a source initially supported on one
carrier has

  (log ||u||^2)'(0)   = -2 |k|^2,
  (log ||u||^2)''(0)  = 0,
  (log ||u||^2)'''(0) = -4 sum_j (|k_j|^2-|k|^2)||S_{j,k}a||^2/|a|^2.

For a Beltrami Raman module with axis Q, shift l perpendicular to Q and strength
|alpha|^2=w, the two reality-paired sidebands k+/-l give a completely explicit
rational contribution.  Two equal-length shifts certify a factor >4 separation
between four unwanted carriers and the three desired clean targets.
"""
from __future__ import annotations
import sympy as sp

z=sp.symbols('z',real=True)
Qclean=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)
lo=sp.Rational(12847,10000); hi=sp.Rational(803,625)
assert Qclean.eval(lo)<0 and Qclean.eval(hi)>0 and Qclean.count_roots(lo,hi)==1

QA=sp.Matrix([-1,-5,-6]);  lA=sp.Matrix([-7,-1,2]);  wA=sp.Integer(30)
QB=sp.Matrix([10,-3,-1]);  lB=sp.Matrix([-2,-7,1]);  wB=sp.Integer(10)
assert QA.dot(lA)==0 and QB.dot(lB)==0
assert lA.dot(lA)==lB.dot(lB)==54

def assert_positive_on_clean(expr,label):
    num,den=map(sp.factor,sp.together(expr).as_numer_denom())
    p=sp.Poly(num,z)
    mid=(lo+hi)/2
    assert p.count_roots(lo,hi)==0,label
    assert p.eval(mid)>0,label
    assert den.subs(z,mid)>0,label

def gamma_axis(k,a,Q,l,w):
    """One axis's Gamma contribution, where (log E)'''_coupling=-16 Gamma."""
    q2=Q.dot(Q)
    kq=k.dot(Q)
    base=sp.factor(w*(a.dot(Q)**2)*(kq**2)/(a.dot(a)*q2**2))
    d0=sp.expand(k.dot(k))
    out=0
    for sg in (1,-1):
        kd=k+sg*l
        dd=sp.expand(kd.dot(kd))
        gap=sp.expand(dd-d0)
        # l.Q=0, so Q.(k+/-l)=Q.k.  |P_kd qhat|^2 is the factor below.
        cproj=sp.factor(1-kq**2/(q2*dd))
        out += gap*cproj
    return sp.factor(base*out)

def Gamma(k,a):
    return sp.factor(gamma_axis(k,a,QA,lA,wA)+gamma_axis(k,a,QB,lB,wB))

def physk(h):
    return sp.Matrix([sp.Integer(h[0])-z*sp.Integer(h[2]),sp.Integer(h[1]),sp.Integer(h[2])])

def vsel(h):
    if h==(0,1,1):
        return sp.Matrix([
          2*z**2*(z**2-2)/(3*(z**2+2)),
         -2*z**3*(z**2+4*z+2)/(3*(z**2+2)*(z**2+2*z+2)),
          2*z**3*(z**4+2*z**3+z**2-2)/(3*(z**2+2)*(z**2+2*z+2))])
    if h==(-2,-1,-1):
        return sp.Matrix([
         -2*z*(z**3+2*z-4)/(3*(z**2-4*z+6)),
         -2*z*(z**4-8*z**3+14*z**2-16*z+8)/(3*(z**2-4*z+6)*(z**2-2*z+2)),
         -2*z*(z**6-4*z**5+7*z**4-8*z**3+14*z**2-16*z+8)/(3*(z**2-4*z+6)*(z**2-2*z+2))])
    if h==(0,-1,1):
        return sp.Matrix([
         -2*z**2*(z**2-2)/(3*(z**2+2)),
         -2*z**3*(z**2-4*z+2)/(3*(z**2+2)*(z**2-2*z+2)),
         -2*z**3*(z**4-2*z**3+z**2-2)/(3*(z**2+2)*(z**2-2*z+2))])
    raise KeyError(h)

targets=[(physk(h),vsel(h)) for h in [(0,1,1),(-2,-1,-1),(0,-1,1)]]
Dp=z**2+2*z+2; Dm=z**2-2*z+2
unwanted=[
 ('p1',sp.Matrix([1,0,0]),sp.Matrix([0,1,z])),
 ('g2',sp.Matrix([1+z,0,-1]),sp.Matrix([-z**3/Dp,1,-z**3*(z+1)/Dp])),
 ('g3',sp.Matrix([1-z,0,1]),sp.Matrix([z**3/Dm,1,z**3*(z-1)/Dm])),
 ('r1',sp.Matrix([-1,-1,0]),sp.Matrix([0,0,1])),
]

# First verify that every +/- sideband used below lies at strictly higher
# viscous frequency for every load-bearing source.
for idx,(k,a) in enumerate(targets+[(k,a) for _,k,a in unwanted]):
    d0=sp.expand(k.dot(k))
    for tag,l in [('A',lA),('B',lB)]:
        for sg in (1,-1):
            gap=sp.factor((k+sg*l).dot(k+sg*l)-d0)
            assert_positive_on_clean(gap,f'source {idx} {tag}{sg}: positive viscous gap')

# Desired carriers have weak cubic export coefficient.
for j,(k,a) in enumerate(targets):
    g=Gamma(k,a)
    assert_positive_on_clean(25-g,f'desired {j}: Gamma < 25')

# Four unwanted carriers have at least four times larger coefficient.
for name,k,a in unwanted:
    g=Gamma(k,a)
    assert_positive_on_clean(g-100,f'{name}: Gamma > 100')

print('PASS: exact two-axis cubic hypocoercive selectivity on the clean-root interval.')
print('QA=(-1,-5,-6), lA=(-7,-1,2), |alpha_A|^2=30; QB=(10,-3,-1), lB=(-2,-7,1), |alpha_B|^2=10.')
print('All paired sidebands have positive viscous gap; Gamma<25 on each desired target and Gamma>100 on p1,g2,g3,r1.')
print("Thus the first coupling-dependent log-energy term, -16 Gamma t^3/6, is at least four times stronger on the load-bearing unwanted set.")
print('Scope: local-in-time hypocoercive theorem; finite-time spectral gap and nonlinear high-mode realization remain open.')
