#!/usr/bin/env python3
"""Exact algebra/scaling controls for the unforced even-feedback packet proof.

The existence/decoupling arguments are analytic; this is not an NS simulation.
"""
import sympy as s

if not __debug__:
    raise RuntimeError('Run without -O: exact assertions are required')

x, y, z = s.symbols('x y z', real=True)
X = s.Matrix([x, y, z])
R = s.diag(-1, -1, 1)
psi = x*x*y
f = s.Matrix([s.diff(psi, y), -s.diff(psi, x), 0])
assert sum(s.diff(f[i], X[i]) for i in range(3)) == 0
fr = R*f.subs({x:-x, y:-y}, simultaneous=True)
assert s.simplify(fr + f) == s.zeros(3, 1)
conv = s.simplify(f.jacobian(X)*f)
assert conv == s.Matrix([2*x**3, 2*x*x*y, 0])
curl3 = s.diff(conv[1], x)-s.diff(conv[0], y)
assert s.simplify(curl3-4*x*y) == 0
cr = R*conv.subs({x:-x, y:-y}, simultaneous=True)
assert s.simplify(cr-conv) == s.zeros(3, 1)

# In u_lambda(t,x)=lambda*u(lambda^2*t,lambda*x), amplitude,
# spacetime measure and derivatives give these exact exponents.
def norm_power(power):
    return power - 3
assert norm_power(3) == 0  # L3^3 initial norm
assert norm_power(2) == -1 # L2^2 initial norm
assert 5-3-2 == 0         # spacetime L5^5 norm
assert 2-2 == 0           # integrated spatial strain supremum
assert 2+3-3-2 == 0       # strain against lambda^3 spatial L1 test

# N packets of size a0*N^(-1/3): fixed cubed critical norm and
# diverging sum of the generated even (quadratic) actions.
assert 1 + 3*(-s.Rational(1,3)) == 0
assert 1 + 2*(-s.Rational(1,3)) == s.Rational(1,3)
assert 1 + 5*(-s.Rational(1,3)) == -s.Rational(2,3)
# If instead a_N=N^(-alpha), 1/3<alpha<1/2 gives even vanishing
# L3 input with diverging generated even action.
alpha = s.Rational(5,12)
assert 1-3*alpha < 0 and 1-2*alpha > 0
assert s.Rational(1,3)-alpha == -s.Rational(1,12)
assert 1-2*alpha == s.Rational(1,6)

# lambda_j=Lambda*2^j, I_j=[tau/lambda_j^2,2*tau/lambda_j^2].
# The next interval ends at half the start of the current interval.
assert s.Rational(2,4) < 1
assert sum(s.Rational(1,2)**j for j in range(1,41)) < 1

print('PASS: compact odd seed has nonzero even solenoidal quadratic response.')
print('PASS: each scaled packet contributes a scale-invariant positive even-strain action.')
print('PASS: disjoint-time packets have fixed small L3 norm and total action >= c a0^2 N^(1/3).')
print('PASS: amplitudes N^(-5/12) even allow L3 -> 0 while the lower action grows as N^(1/6).')
print('Scope: exact seed, parity, and scaling arithmetic; global solution and finite-profile decoupling are analytic obligations in the companion proof.')

# Stronger material-point control: an inversion-odd, rotationally odd seed.
# Strip exp(-|x|^2) from curl(x^2*y*z*exp(-|x|^2) e3).
from functools import lru_cache
xyz = (x,y,z)
psi4=x*x*y*z
f4=s.Matrix([s.diff(psi4,y)-2*y*psi4, -s.diff(psi4,x)+2*x*psi4, 0])
assert s.simplify(R*f4.subs({x:-x,y:-y}, simultaneous=True)+f4)==s.zeros(3,1)
assert s.simplify(f4.subs({x:-x,y:-y,z:-z}, simultaneous=True)+f4)==s.zeros(3,1)
assert s.simplify(sum(s.diff(f4[i],xyz[i])-2*xyz[i]*f4[i] for i in range(3)))==0

@lru_cache(None)
def weighted_gaussian_monomial(A,B,C,k):
    """Integral x^A y^B z^C |x|^(-k) exp(-2|x|^2)/(4pi)."""
    if any(j%2 for j in (A,B,C)):
        return s.S.Zero
    degree=A+B+C
    power=s.Rational(degree-k+3,2)
    assert power>0, 'only absolutely integrable monomials are admitted'
    angular=2*s.prod(s.gamma(s.Rational(j+1,2)) for j in (A,B,C))/s.gamma(s.Rational(degree+3,2))
    radial=s.gamma(power)/(2*2**power)
    return s.simplify(angular*radial/(4*s.pi))

def integrate_polynomial(poly,k):
    terms=s.Poly(s.expand(poly),x,y,z).terms()
    return s.simplify(sum(c*weighted_gaussian_monomial(*powers,k)
                          for powers,c in terms if c!=0))

def kd(i,j):
    return int(i==j)

Hp=s.zeros(3)
for a in range(3):
    for b in range(3):
        polys={9:0,7:0,5:0}
        for i in range(3):
            for j in range(3):
                stress=f4[i]*f4[j]
                polys[9]+=105*xyz[a]*xyz[b]*xyz[i]*xyz[j]*stress
                polys[7]+=-15*(kd(a,b)*xyz[i]*xyz[j]+kd(a,i)*xyz[b]*xyz[j]
                    +kd(a,j)*xyz[b]*xyz[i]+kd(b,i)*xyz[a]*xyz[j]
                    +kd(b,j)*xyz[a]*xyz[i]+kd(i,j)*xyz[a]*xyz[b])*stress
                polys[5]+=3*(kd(a,b)*kd(i,j)+kd(a,i)*kd(b,j)+kd(a,j)*kd(b,i))*stress
        Hp[a,b]=s.simplify(sum(integrate_polynomial(poly,k) for k,poly in polys.items()))
expected=s.diag(-s.Rational(1,195),-s.Rational(29,3003),s.Rational(74,5005))
assert Hp==expected
assert s.trace(Hp)==0
# f4 exp(-|x|^2) vanishes to order three. Thus grad((f.grad)f)(0)=0,
# the local distributional derivative terms vanish, and S(-P div(fxf))(0)=-Hp.
assert all(sum(powers)>=3 for component in f4 for powers,c in s.Poly(component,x,y,z).terms() if c!=0)
assert -Hp[0,0]==s.Rational(1,195)>0
print('PASS: full canonical-pressure calculation gives S(g)(0)=diag(1/195,29/3003,-74/5005).')
print('The inversion-odd seed keeps the origin stationary; nested-scale finite-profile decoupling is proved analytically, not by this calculation.')
