#!/usr/bin/env python3
"""Exact quadratic/Duhamel data for the finite-time six-mode half-grade bridge."""
import sympy as s

mu=s.Rational(3,5)

def P(k):
    k=s.Matrix(k); return s.eye(3)-k*k.T/k.dot(k)
def ap(sig): return s.Matrix([1,-s.sqrt(1+sig*sig),-sig])
def C(p,a,q,b):
    p,a,q,b=map(s.Matrix,(p,a,q,b))
    return s.simplify(P(p+q)*((a.dot(q))*b+(b.dot(p))*a))
def eigcoords(k,f):
    k,f=s.Matrix(k),s.Matrix(f); sig=s.simplify(k[0]/k[2]); q=s.sqrt(1+sig*sig)
    return s.simplify((f[0]-f[1]/q)/2),s.simplify((f[0]+f[1]/q)/2)
def halfvec(x): return s.Matrix([s.Rational(x,20),0,s.Rational(1,2)])
def halfpol(x): return ap(s.Rational(x,10))
def targetvec(K): return s.Matrix([s.Rational(K,10),0,1])
def rate(z,sig):
    q2=1+sig*sig
    return s.simplify(1/s.sqrt(q2)-mu*z*z*q2)

ancestors=[14,-13,5,-4,2,-1]
targets=[5,-4,2,-1]
edges=[(14,-4,5),(-13,5,-4),(5,-1,2),(-4,2,-1)]

# For each target, enumerate all positive-half-grade decompositions.  The only
# alternative to the selected cross pair is a self pair, and incompressibility
# makes every self-pair coefficient identically zero for any transverse vector.
coeff={}; mismatch={}
for a,b,K in edges:
    pairs=[]
    for i,x in enumerate(ancestors):
        for y in ancestors[i:]:
            if x+y==2*K: pairs.append((x,y))
    assert (a,b) in pairs or (b,a) in pairs,(K,pairs)
    for x,y in pairs:
        if x==y:
            pol=halfpol(x); k=halfvec(x)
            assert s.simplify(k.dot(pol))==0
            assert C(k,pol,k,pol)==s.zeros(3,1)
        else:
            assert {x,y}=={a,b},(K,pairs)

    F=C(halfvec(a),halfpol(a),halfvec(b),halfpol(b))
    cp,_=eigcoords(targetvec(K),F)
    cp=s.simplify(cp)
    assert cp!=0
    coeff[K]=cp

    la=rate(s.Rational(1,2),s.Rational(a,10))
    lb=rate(s.Rational(1,2),s.Rational(b,10))
    lt=rate(s.Integer(1),s.Rational(K,10))
    D=s.simplify(la+lb-lt)
    # Exact positive mismatch: the Duhamel factor
    #   (exp(D*T)-1)/D
    # is strictly positive for every T>0.
    assert D>0,(a,b,K,D)
    mismatch[K]=D

# Introduce abstract positive Duhamel factors f_K.  The exact quadratic
# finite-time map differs from the instantaneous map only by the nonzero
# scalar exp(lambda_K*T)*f_K (and the common Fourier -i factor), so its
# four-control Jacobian stays invertible for every fixed T>0.
f5,fm4,f2,fm1=s.symbols('f5 fm4 f2 fm1', positive=True, nonzero=True)
x14,xm13,x5,xm4,x2,xm1=s.symbols('x14 xm13 x5 xm4 x2 xm1', nonzero=True)
factors={5:f5,-4:fm4,2:f2,-1:fm1}
Y=s.Matrix([
    factors[5]*coeff[5]*x14*xm4,
    factors[-4]*coeff[-4]*xm13*x5,
    factors[2]*coeff[2]*x5*xm1,
    factors[-1]*coeff[-1]*xm4*x2,
])
controls=s.Matrix([x14,xm13,xm1,x2])
J=Y.jacobian(controls)
det=s.factor(J.det())
expected=s.factor(f5*fm4*f2*fm1*coeff[5]*coeff[-4]*coeff[2]*coeff[-1]*xm4**2*x5**2)
assert s.simplify(det-expected)==0
assert det!=0

print('PASS: six-mode bridge has an invertible quadratic finite-time target map for every fixed T>0.')
for K in targets:
    print(f'target {K}: exact growth mismatch D={s.radsimp(mismatch[K])} > 0')
print('Each Duhamel factor (exp(D*T)-1)/D is positive; self-pair competitors vanish identically.')
print('The normalized four-target Jacobian is nonzero, so analytic full-lattice evolution admits small exact retuning by the real IFT.')
print('Scope: frozen source-reference full infinite lattice on a fixed finite horizon; physical finite-L/whole-space lift and causal six-mode supply remain open.')
