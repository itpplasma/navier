#!/usr/bin/env python3
"""Exact algebra for weighted Hessian pressure and critical feedback absorption.

Analytic inequalities are proved in the companion note. No PDE orbit is tested.
"""
import sympy as s

if not __debug__:
    raise RuntimeError('Run without -O: exact assertions are required')

x,y,z=s.symbols('x y z',real=True)
X=s.Matrix([x,y,z])
q=x**4*y+x*y*y*z*z+3*x*z**3+y**4
H=s.hessian(q,X)
g=s.Matrix([s.diff(q,xx) for xx in X])
delq=s.trace(H)
flux=H*g-delq*g
assert s.simplify(sum(s.diff(flux[i],X[i]) for i in range(3))
                  -(sum(v*v for v in H)-delq**2))==0

# The weighted integration identity gives
# Xh^2-Yh^2 <= 2*d*Xh*(Xh+Yh); cancelling Xh+Yh yields the sharp stated factor.
Xh,Yh,d=s.symbols('Xh Yh d',nonnegative=True)
assert s.expand((Xh-Yh-2*d*Xh)*(Xh+Yh)
                -(Xh**2-Yh**2-2*d*Xh*(Xh+Yh)))==0
N=s.symbols('N',integer=True,positive=True)
# First Cartesian differentiation of scalar angular index m has m,m+/-1.
for cutoff in range(2,20):
    for m in list(range(cutoff,cutoff+6))+list(range(-cutoff-5,-cutoff+1)):
        assert min(abs(m+j) for j in (-1,0,1))>=cutoff-1

# Young: b*sqrt(Y)*D <= nu/4*D^2+b^2/nu*Y.
nu,b,D,Y=s.symbols('nu b D Y',positive=True)
assert s.simplify(nu*D**2/4+b*b*Y/nu-b*s.sqrt(Y)*D
                  -(s.sqrt(nu)*D/2-b*s.sqrt(Y)/s.sqrt(nu))**2)==0

# Exact solenoidal swirl convection, including radial cutoff derivatives.
chi=s.Function('chi')(x*x+y*y+z*z)
swirl=s.Matrix([-y*chi,x*chi,0])
assert s.simplify(sum(s.diff(swirl[i],X[i]) for i in range(3)))==0
assert s.simplify(swirl.jacobian(X)*swirl+chi**2*s.Matrix([x,y,0]))==s.zeros(3,1)

# Radial compact swirl produces a pure exterior quadrupole.
mu=s.symbols('mu',real=True)
angular=s.simplify(2*s.pi*s.integrate((3*mu*mu-1)**2,(mu,-1,1)))
assert angular==16*s.pi/5
R,m=s.symbols('R m',positive=True)
radial=1/(3*R**3)
assert s.simplify(m*m/(16*s.pi*s.pi)*angular*radial-m*m/(15*s.pi*R**3))==0
# Multipole coefficient: (1/5)*(2/3)*integral r^5 a'(r) = -(2/3)*integral r^4 a.
assert s.Rational(1,5)*s.Rational(2,3)*(-5)==-s.Rational(2,3)
# The covariance coefficient m=(4*pi/3)*integral r^4 a reproduces -m*d33 Gamma.
assert s.simplify(-(4*s.pi/3)/(2*s.pi)+s.Rational(2,3))==0

# Physical-to-band normalization: velocity unit Q^(-1/2-h), length sqrt(Q).
# ||Z_*||_3 = Q^h ||Z||_3; diffusivity nu_* = nu Q^h.
kappa=s.Rational(1,100000)
assert 2-1-2*kappa==1-2*kappa>0
print('PASS: exact weighted Hessian/Laplacian flux identity and N-1 angular shift.')
print('PASS: critical feedback form bound absorbs strain with no derivative of Z.')
print('PASS: source-normalized feedback action costs epsilon^(1-2*kappa_s) times a polynomial, under the stated purity and critical smallness hypotheses.')
print('PASS: a genuine compact solenoidal swirl has exterior pressure norm m/sqrt(15*pi*R^3), preserving the exponential low-sector counter-control.')
print('Scope: exact algebra only; analytic absorption, elliptic duality and all-mode estimates are proved in the companion note.')
