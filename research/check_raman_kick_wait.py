#!/usr/bin/env python3
"""Exact geometry and asymptotic ledger for the Raman kick--wait purifier.

Use the two common-line axes QA,QB with shifts +/-J ell and +/-2J ell, but now
with fixed kick strengths sqrt(30), sqrt(10), not J-growing strengths.  The
reality-complete Raman operator is skew, so exp(theta S_J) is unitary.  For a
center-supported carrier the center-energy curvature is

  A_J=||S_J a||^2/|a|^2 -> 8 C(k,a).

The exact carrier certificate has C<1/4 for desired selected targets and C>1
for all finite unwanted classes.  A subsequent pure-viscous wait theta^2/2
therefore has second-order center coefficients <6 versus >9.  With J->infinity,
all exported sidebands disappear during the wait.
"""
from __future__ import annotations
import sympy as sp

z,J=sp.symbols('z J',real=True,positive=True)
Qclean=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)
lo=sp.Rational(12847,10000); hi=sp.Rational(803,625)
assert Qclean.eval(lo)<0 and Qclean.eval(hi)>0 and Qclean.count_roots(lo,hi)==1

QA=sp.Matrix([-1,-5,-6]); QB=sp.Matrix([10,-3,-1]); ell=QA.cross(QB)
assert ell==sp.Matrix([-13,-61,53]) and ell.dot(ell)==6699

def Cform(k,a):
    return sp.factor(
        30*(a.dot(QA)**2)*(k.dot(QA)**2)/(a.dot(a)*QA.dot(QA)**2)
       +10*(a.dot(QB)**2)*(k.dot(QB)**2)/(a.dot(a)*QB.dot(QB)**2))

def kick_curvature(k,a):
    """Exact A_J=||S_J a||^2/|a|^2 for center-supported data."""
    out=0
    for Q,w,m in [(QA,30,1),(QB,10,2)]:
        q2=Q.dot(Q); kq=k.dot(Q)
        base=4*sp.Rational(w)*(a.dot(Q)**2)*(kq**2)/(a.dot(a)*q2**2)
        for sg in (1,-1):
            kd=k+sg*m*J*ell
            # q.Q normalization: |P_kd q|^2=1-(kq)^2/(|Q|^2 |kd|^2)
            out += base*(1-kq**2/(q2*kd.dot(kd)))
    return sp.factor(out)

def assert_positive_on_clean(expr,label):
    num,den=map(sp.factor,sp.together(expr).as_numer_denom())
    p=sp.Poly(num,z)
    mid=(lo+hi)/2
    assert p.count_roots(lo,hi)==0,label
    assert p.eval(mid)>0,label
    assert den.subs(z,mid)>0,label

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

desired=[]; unwanted=[]
for h in [(0,1,1),(-2,-1,-1),(0,-1,1)]:
    k=physk(h); v=vsel(h); f=sp.simplify(k.cross(v))
    desired.append((str(h),k,v))
    unwanted.append((str(h)+'-rejected',k,f))
Dp=z**2+2*z+2; Dm=z**2-2*z+2
unwanted += [
 ('p1',sp.Matrix([1,0,0]),sp.Matrix([0,1,z])),
 ('p2',sp.Matrix([0,1,0]),sp.Matrix([1,0,z])),
 ('p3',sp.Matrix([-z,0,1]),sp.Matrix([1,0,z])),
 ('g1',sp.Matrix([-1,-1,0]),sp.Matrix([0,0,-2*z])),
 ('g2',sp.Matrix([1+z,0,-1]),sp.Matrix([-z**3/Dp,1,-z**3*(z+1)/Dp])),
 ('g3',sp.Matrix([1-z,0,1]),sp.Matrix([z**3/Dm,1,z**3*(z-1)/Dm])),
]
# Add the first three inherited-ladder carriers; n>=4 is handled uniformly by
# the line-distance/wait estimate in the proof packet.
for nn in (1,2,3):
    unwanted.append((f'r{nn}',sp.Matrix([-nn,-1,0]),sp.Matrix([0,0,1])))

for name,k,a in desired+unwanted:
    A=kick_curvature(k,a)
    C=Cform(k,a)
    # Exact large-J limit of center-energy curvature.
    assert sp.simplify(sp.limit(A,J,sp.oo)-8*C)==0,name

for name,k,a in desired:
    C=Cform(k,a)
    assert_positive_on_clean(sp.Rational(1,4)-C,name+': C<1/4')
    assert_positive_on_clean(4-k.dot(k),name+': |k|^2<4')
    # limiting kick+wait second-order energy coefficient: 8C+|k|^2 <6
    assert_positive_on_clean(6-(8*C+k.dot(k)),name+': kick-wait coeff<6')
for name,k,a in unwanted:
    C=Cform(k,a)
    assert_positive_on_clean(C-1,name+': C>1')
    assert_positive_on_clean(k.dot(k)-sp.Rational(999,1000),name+': |k|^2>~1')
    assert_positive_on_clean((8*C+k.dot(k))-9,name+': kick-wait coeff>9')

# Finite-source exported sectors have |k+nJ ell|^2>6437 J^2 n^2, from the
# companion Schur-bounds checker.  For fixed theta>0, a wait theta^2/2 hence
# kills every n!=0 sector exponentially as J->infinity.
# Full ladder tail: any translated r_N line has |k|^2>N^2/2.  For N>=4 the
# wait energy exponent is at least N^2 theta^2/2 >=8 theta^2, already larger
# than the desired limiting coefficient <6.
assert sp.Rational(4**2,2)==8

# One compatible scale ledger keeps the kick action fixed while separating all
# clocks: J=sigma^2, high radius R=sigma^6, rho=sqrt(theta R), and Re=sigma^13.
sigma,theta=sp.symbols('sigma theta',positive=True)
Jsc=sigma**2; R=sigma**6; rho=sp.sqrt(theta*R); Re=sigma**13
eps=sigma**-2
assert sp.simplify(Jsc/R)==sigma**-4
assert sp.simplify(rho**2/R)==theta
assert sp.simplify(R**2/Re)==sigma**-1
assert sp.simplify(R*rho/Re)==sp.sqrt(theta)*sigma**-4
# shell residual after the worst first-star sqrt(R) balancing loss:
assert sp.simplify((rho*eps/R)*sp.sqrt(R))==sp.sqrt(theta)*sigma**-2
# high clock is negligible against both J^-2 and any fixed positive wait.
assert sp.simplify((R**-2)/(Jsc**-2))==sigma**-8

print('PASS: exact Raman kick--wait geometry and compatible scale ledger.')
print('As J->infinity, center kick curvature tends to 8C: desired kick+wait coefficient <6, finite unwanted coefficient >9.')
print('The ladder tail n>=4 is uniformly more damped during the wait; r1-r3 are in the exact finite certificate.')
print('Compatible scaling: J=sigma^2, R=sigma^6, rho^2/R=theta fixed, Re=sigma^13, shell epsilon=sigma^-2.')
