#!/usr/bin/env python3
"""Exact trace-free strain obstruction for nonlinear adjoint sign certificates."""
from fractions import Fraction

# Any nonzero real symmetric trace-free 3x3 matrix cannot be positive or
# negative semidefinite: its eigenvalues sum to zero.  Freeze diagonal exact
# representatives spanning all sign patterns compatible with nonzero trace 0.
triples=[(1,1,-2),(1,-1,0),(3,-1,-2),(5,-2,-3),(-1,-1,2)]
for t in triples:
    assert sum(t)==0 and any(x>0 for x in t) and any(x<0 for x in t)

# Whole-space solenoidal Korn identity at each nonzero Fourier frequency:
# S_hat = i/2(k tensor z + z tensor k), k.z=0,
# so 2|S_hat|_F^2 = |k|^2 |z|^2 = |grad z|^2.
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm2(a): return dot(a,a)
for k,z in [((1,0,0),(0,2,3)),((1,2,0),(2,-1,4)),((2,-1,3),(1,2,0))]:
    assert dot(k,z)==0
    # Frobenius norm squared of sym outer product, omitting the harmless i.
    S2=Fraction(0)
    for i in range(3):
        for j in range(3):
            sij=Fraction(k[i]*z[j]+z[i]*k[j],2)
            S2 += sij*sij
    assert 2*S2 == norm2(k)*norm2(z)

# A pointwise quadratic form with a trace-free nonzero strain can take either
# sign by aligning with positive/negative eigendirections.  Diagonal examples
# make that exact without floating point.
for lam in triples:
    qpos=max(lam); qneg=min(lam)
    assert qpos>0 and qneg<0

print('PASS: exact adjoint strain-sign wall.')
print('For every solenoidal adjoint, tr S(z)=0; nonzero strain is pointwise indefinite.')
print('The Fourier Korn identity 2||S(z)||_2^2=||grad z||_2^2 shows an L2 solenoidal field with S=0 is zero.')
print('Therefore no nonzero admissible adjoint can make (w⊗w):S(z) one-signed for arbitrary corrections w.')
print('Scope: rules out sign-only nonlinear adjoint certificates; quantitative full-history budgets remain open.')
