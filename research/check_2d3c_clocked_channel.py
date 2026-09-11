#!/usr/bin/env python3
"""Exact 2D3C invariant clocked-pump channel in normal form."""
import sympy as sp

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

K,N=sp.symbols('K N', nonzero=True, real=True)
def proj(k,v):
    return sp.simplify(v-k*(k.dot(v))/k.dot(k))
def pair(p,a,q,b):
    return sp.simplify(proj(p+q,(a.dot(q))*b+(b.dot(p))*a))

e1=sp.Matrix([1,0,0]); e2=sp.Matrix([0,1,0]); e3=sp.Matrix([0,0,1])
kappa=K*e1; a=e3; b=e1/K

for m in (1,2,3):
    q=m*N*e2
    p=kappa-q
    check(sp.simplify(a.dot(p))==0 and sp.simplify(a.dot(q))==0,f'{m}: scalar polarization transverse')
    check(sp.simplify(b.dot(q))==0 and sp.simplify(b.dot(p)-1)==0,f'{m}: shear polarization normalized')
    check(sp.simplify(pair(p,a,q,b)-a)==sp.zeros(3,1),f'{m}: exact prescribed low child')
    D=sp.factor(p.dot(p)+q.dot(q)-kappa.dot(kappa))
    check(D==2*m*m*N*N,f'{m}: exact decay gap')
    check(sp.simplify(pair(p,a,-q,b)-a)==sp.zeros(3,1),f'{m}: sibling remains scalar polarized')

# Every pair of in-plane collinear shear harmonics has zero NS interaction.
for m in (1,2,3):
    for n in (1,2,3):
        qm=m*N*e2; qn=n*N*e2
        check(sp.simplify(pair(qm,b,qn,b))==sp.zeros(3,1),f'shear {m},{n}: mutual nonlinearity zero')

# Every pair of e3-polarized scalar modes in the xy plane has zero interaction.
r,s=sp.symbols('r s', integer=True)
kr=sp.Matrix([K,r*N,0]); ks=sp.Matrix([K,s*N,0])
check(sp.simplify(pair(kr,a,ks,a))==sp.zeros(3,1),'all scalar-scalar interactions vanish')

# A shear harmonic shifts every scalar lattice mode with the same coefficient.
n=sp.symbols('n', integer=True)
kn=sp.Matrix([K,n*N,0])
for m in (1,2,3):
    qm=m*N*e2
    check(sp.simplify(pair(kn,a,qm,b)-a)==sp.zeros(3,1),f'+{m}: constant scalar ladder coupling')
    check(sp.simplify(pair(kn,a,-qm,b)-a)==sp.zeros(3,1),f'-{m}: constant scalar ladder coupling')

weights={1:sp.Integer(5),2:sp.Integer(-32),3:sp.Integer(27)}
check(sum(weights.values())==0,'source onset cancels')
check(sum(weights[m]/sp.Integer(m*m) for m in (1,2,3))==0,'slow low heat tail cancels')

print(f'PASS: {len(CHECKS)} exact symbolic assertions.')
print('The three-layer pump is an exact 2D3C invariant subsystem:')
print('the collinear in-plane shear evolves by heat, and the e3 component is a linear passive scalar.')
print('All scalar ladder couplings have coefficient one; D_m=2 m^2 N^2 gives the 1:4:9 clock exactly.')
