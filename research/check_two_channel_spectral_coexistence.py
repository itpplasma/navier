#!/usr/bin/env python3
"""Exact geometry checks for the two-channel purifier spectral moat.

Reconstruct the rank-two transverse decomposition over
T^2=708331/5680000 and verify that the two low carriers and the two high pump
directions are genuinely nonparallel.  Also verify the gradient-preserving
rescaling identities used by the coexistence argument.
"""
import sympy as sp

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

T=sp.symbols('T', real=True)
rel=sp.Poly(5680000*T**2-708331,T)

def zero_mod(expr):
    num,den=map(sp.factor,sp.together(expr).as_numer_denom())
    return sp.factor(sp.rem(sp.Poly(num,T),rel).as_expr())==0

def nonzero_mod(expr):
    num,den=map(sp.factor,sp.together(expr).as_numer_denom())
    return sp.gcd(sp.Poly(num,T),rel).degree()==0

def matrix_zero_mod(M):
    return all(zero_mod(M[i,j]) for i in range(M.rows) for j in range(M.cols))

H=sp.Matrix([
 [sp.Rational(71,100),-1,sp.Rational(147,200)],
 [-1,sp.Rational(-143,200),sp.Rational(7,25)],
 [sp.Rational(147,200),sp.Rational(7,25),sp.Rational(1,200)],
])
A=sp.Matrix([[0,0,0],[0,0,-T],[0,T,0]])
G=H+A
U=G[:,0:2]
ab=sp.simplify(U[0:2,:].inv()*G[0:2,2])
Vt=sp.Matrix([[1,0,ab[0]],[0,1,ab[1]]])
C=sp.simplify(Vt*U)
M=sp.Matrix([[1,C[0,0]],[0,C[1,0]]])
U2=sp.simplify(U*M)
Vt2=sp.simplify(M.inv()*Vt)

pairs=[]
for i in range(2):
    d=sp.simplify(U2[:,i]/2)
    k=sp.simplify(Vt2[i,:].T)
    r=sp.simplify(k.cross(d))
    check(zero_mod((d.T*k)[0]),f'channel {i+1}: transverse low pair')
    check(any(nonzero_mod(c) for c in r),f'channel {i+1}: nonzero pump direction')
    pairs.append((d,k,r))

# The two low carriers must be nonparallel, otherwise a cross low-low sum could
# return directly to one target carrier.
k1,k2=pairs[0][1],pairs[1][1]
kcross=sp.simplify(k1.cross(k2))
check(any(nonzero_mod(c) for c in kcross),'low carriers are nonparallel')

# The two high pump directions must be nonparallel.  Then the 3x2 direction
# matrix has a fixed positive smallest singular value after normalization,
# yielding |n1 rho1+n2 rho2| >= sigma sqrt(n1^2+n2^2).
r1,r2=pairs[0][2],pairs[1][2]
rcross=sp.simplify(r1.cross(r2))
check(any(nonzero_mod(c) for c in rcross),'high pump directions are nonparallel')

# Reconstruct the exact full purifier gradient and its symmetric part.
R=sp.zeros(3)
for d,k,_ in pairs:
    R += 2*d*k.T
check(matrix_zero_mod(R-G),'two channel gradients reconstruct G')
check(matrix_zero_mod((R+R.T)/2-H),'symmetric purifier strain is exactly H')

# Gradient-preserving rescaling d -> lambda d, k -> k/lambda and invariance of
# r=k cross d are exact identities before imposing any asymptotic choice.
lam=sp.symbols('lambda', positive=True, nonzero=True)
for i,(d,k,r) in enumerate(pairs):
    dl=lam*d; kl=k/lam
    check(matrix_zero_mod(2*dl*kl.T-2*d*k.T),
          f'channel {i+1}: gradient invariant under lambda rescaling')
    check(matrix_zero_mod(kl.cross(dl)-r),
          f'channel {i+1}: pump direction invariant under lambda rescaling')

# Numerical orientation only, derived from the exact positive quadratic root.
Tv=sp.sqrt(sp.Rational(708331,5680000))
r1v=sp.Matrix([sp.N(c.subs(T,Tv),30) for c in r1])
r2v=sp.Matrix([sp.N(c.subs(T,Tv),30) for c in r2])
cosang=sp.N(r1v.dot(r2v)/(sp.sqrt(r1v.dot(r1v))*sp.sqrt(r2v.dot(r2v))),15)
check(abs(float(cosang)) < 1,'numeric high directions not parallel')
# For two unit columns, singular values squared are 1 +/- |cos(theta)|.
sigma_min=sp.sqrt(1-abs(cosang))
check(float(sigma_min)>sp.Rational(1,4),'conservative sigma_min > 1/4 calibration')

print(f'PASS: {len(CHECKS)} exact/algebraic assertions plus orientation calibrations.')
print(f'normalized high-direction dot product = {float(cosang):.12f}')
print(f'positive singular-value lower calibration = {float(sigma_min):.12f}')
print('Scope: carrier geometry/spectral moat only; finite-energy localization and clean-gate composition are separate.')
