#!/usr/bin/env python3
"""Exact symmetric inverse-divergence symbol for a solenoidal force mode."""
from fractions import Fraction

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm2(a): return dot(a,a)

samples=[
    ((1,0,0),(0,2,3)),
    ((1,2,0),(2,-1,4)),
    ((2,-1,3),(1,2,0)),
    ((3,4,0),(4,-3,5)),
]
for k,f in samples:
    assert dot(k,f)==0
    K2=norm2(k)
    # Omit the harmless Fourier factor -i.  H=(k⊗f+f⊗k)/|k|^2
    # then H k=f, so G=-i H satisfies i k_j G_ij=f_i.
    H=[[Fraction(k[i]*f[j]+f[i]*k[j],K2) for j in range(3)] for i in range(3)]
    assert all(H[i][j]==H[j][i] for i in range(3) for j in range(3))
    Hk=[sum(H[i][j]*k[j] for j in range(3)) for i in range(3)]
    assert tuple(Hk)==tuple(Fraction(x) for x in f)
    H2=sum(H[i][j]*H[i][j] for i in range(3) for j in range(3))
    assert H2 == Fraction(2*norm2(f),K2)

    # Exact strain-dual identity: H : sym(k⊗z) = f.z for every test z.
    for z in [(1,0,2),(2,-1,3),(0,4,-2)]:
        lhs=Fraction(0)
        for i in range(3):
            for j in range(3):
                Sz=Fraction(k[i]*z[j]+z[i]*k[j],2)
                lhs += H[i][j]*Sz
        assert lhs == dot(f,z)

print('PASS: exact principal-force symmetric stress duality.')
print('For k.f=0, Ghat=-i(k⊗f+f⊗k)/|k|^2 is symmetric and i k_j G_ij=f_i.')
print('Its Frobenius norm is sqrt(2)|f|/|k| and G pairs only with symmetric strain.')
print('Thus a high-frequency principal solenoidal force is small in the same strain-dual norm as the nonlinear correction stress.')
print('Scope: exact Fourier/principal-carrier symbol; localization, envelope terms and full source history remain open.')
