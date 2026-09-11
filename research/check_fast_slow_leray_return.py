#!/usr/bin/env python3
"""Exact symbolic check of the one-power fast--slow Leray return cancellation.

Normalize q=e1, b=e2, k=epsilon*K.  The two-step return
C(k+q,C(k,a;q,b);-q,b) must carry an exact factor epsilon in every
component.  This freezes the sharp first nonzero return behind the
scale-separated purifier scheduling packet.
"""
import sympy as sp

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

eps=sp.symbols('epsilon')
K1,K2,K3=sp.symbols('K1 K2 K3', real=True)
A1,A2,A3=sp.symbols('A1 A2 A3', real=True)
K=sp.Matrix([K1,K2,K3])
k=eps*K
q=sp.Matrix([1,0,0])
a=sp.Matrix([A1,A2,A3])
b=sp.Matrix([0,1,0])

def P(r,v):
    return sp.simplify(v-r*(r.dot(v))/r.dot(r))

def C(p,A,qv,B):
    return P(p+qv,(A.dot(qv))*B+(B.dot(p))*A)

c1=C(k,a,q,b)
c2=sp.Matrix([sp.factor(x) for x in C(k+q,c1,-q,b)])

# Every rational component has numerator divisible by epsilon after reduction.
for j,x in enumerate(c2):
    num,den=map(sp.factor,sp.together(x).as_numer_denom())
    check(sp.rem(sp.Poly(num,eps),sp.Poly(eps,eps))==0,
          f'component {j}: exact epsilon factor')
    quot=sp.factor(num/eps)
    check(quot!=0,f'component {j}: cancellation is generically only first order')

Ksq=K.dot(K)
first=[sp.simplify(sp.limit(x/eps,eps,0)) for x in c2]
expected=[
    -2*A1*K1*K2**2/Ksq,
     2*A1*K2*(K1**2+K3**2)/Ksq,
    -2*A1*K2**2*K3/Ksq,
]
for j in range(3):
    check(sp.simplify(first[j]-expected[j])==0,
          f'component {j}: first-order coefficient')

# The leading return is transverse to the slow output wavevector K.
check(sp.simplify(K.dot(sp.Matrix(first)))==0,
      'first-order returned vector is transverse to K')

print(f'PASS: {len(CHECKS)} exact symbolic assertions.')
print('All return components have an exact epsilon=|k|/|q| factor; the generic leading term is nonzero and transverse.')
print('Scope: two-step Fourier-symbol return only; all-orders nonlinear scheduling remains separate.')
