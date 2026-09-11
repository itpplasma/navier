#!/usr/bin/env python3
"""Exact common-Beltrami-sphere repair of the Raman high-cross wall.

Five equal-radius, same-helicity high-pair modules are jointly Beltrami, hence
their complete high-high Navier--Stokes self-interaction is pure pressure at
arbitrary amplitude.  Their target-triggered leading Raman strains still span
Sym_0(3) at the clean return root.
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

# Actual ancestry-contaminated middle target, exactly as frozen in the previous
# state-triggered Raman checker.  Remove its common Fourier phase and clear one
# common nonzero denominator; column-span tests are invariant under this scalar.
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
D=sp.denom(a[0])
for x in a[1:]: D=sp.lcm(D,sp.denom(x))
A=sp.Matrix([sp.expand(sp.cancel(D*x)) for x in a])
h=sp.Matrix([z-2,-1,-1])
check(sp.factor(h.dot(A))==0,'actual contaminated trigger is transverse')

# All five modules use |Q|=|l|=1 and Q.l=0.  Therefore
# q=NQ+l/2 and r=-NQ+l/2 lie on one common sphere |k|^2=N^2+1/4.
# With m=Qxl and L=sqrt(N^2+1/4),
#   beta=m+i(qxm)/L, epsilon=m+i(rxm)/L
# are positive-helicity eigenvectors: i k x b = L b.
# Consequently the sum of every selected high mode is a single Beltrami
# eigenfield curl U=L U, so P[(U.grad)U]=0 identically at arbitrary amplitude.
MODULES=[
 ((-1,0,0),(0,0,1)),
 ((0,-1,0),(0,0,1)),
 ((-1,0,0),(0,1,0)),
 ((0,0,-1),(0,1,0)),
 ((0,-1,0),(1,0,0)),
]
L=sp.sqrt(N**2+sp.Rational(1,4))
cols=[]
for j,(lt,Qt) in enumerate(MODULES):
    l=sp.Matrix(lt); Q=sp.Matrix(Qt); m=Q.cross(l)
    check(l.dot(Q)==0 and l.dot(l)==1 and Q.dot(Q)==1 and m.dot(m)==1,
          f'module {j}: orthonormal Beltrami geometry')
    q=N*Q+l/2; r=-N*Q+l/2
    check(sp.expand(q.dot(q)-L**2)==0 and sp.expand(r.dot(r)-L**2)==0,
          f'module {j}: common Beltrami sphere')
    beta=m+sp.I*q.cross(m)/L
    eps=m+sp.I*r.cross(m)/L
    check(sp.simplify(q.dot(beta))==0 and sp.simplify(r.dot(eps))==0,
          f'module {j}: helical parents transverse')
    check(all(sp.simplify(x)==0 for x in sp.I*q.cross(beta)-L*beta) and
          all(sp.simplify(x)==0 for x in sp.I*r.cross(eps)-L*eps),
          f'module {j}: common positive helicity')

    # Leading target-assisted Raman symbol.  For same-helicity near-opposite
    # parents, beta->m-i l and epsilon->m+i l.  After the second interaction
    # and the final Leray projection the leading direction is, up to the common
    # nonzero scalar -2,
    #   (A.Q)(Q.kappa) P_kappa Q.
    # Multiply by |kappa|^2 to keep the exact column polynomial.
    kappa=h+l
    k2=sp.expand(kappa.dot(kappa)); qk=sp.expand(Q.dot(kappa))
    d=sp.expand((A.dot(Q))*qk*(k2*Q-kappa*qk))
    check(sp.expand(kappa.dot(d))==0,f'module {j}: effective output transverse')
    S=(d*kappa.T+kappa*d.T)/2
    check(sp.expand(sp.trace(S))==0,f'module {j}: effective strain trace free')
    cols.append(sp.Matrix([
        sp.expand(S[0,0]),sp.expand(S[1,1]),sp.expand(S[0,1]),
        sp.expand(S[0,2]),sp.expand(S[1,2])]))

M=sp.Matrix.hstack(*cols)
det=sp.Poly(sp.expand(M.det(method='berkowitz')),z)
check(det.degree()==61,'Beltrami span determinant has exact degree 61')
check(sp.gcd(det,Qclean).degree()==0,
      'Beltrami span determinant is coprime to clean return polynomial')

print(f'PASS: {len(CHECKS)} exact assertions.')
print('Five same-helicity equal-radius modules span Sym_0(3) at the clean root.')
print('Their complete high background lies in one Beltrami eigenspace, so high-high self-interaction is pure pressure at arbitrary amplitude.')
print('Scope: exact Fourier-symbol/common-sphere theorem; whole-space finite-energy localization and high-slow normal form remain open.')
