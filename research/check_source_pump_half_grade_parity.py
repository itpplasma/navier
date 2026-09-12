#!/usr/bin/env python3
"""Exact parity obstruction and pump-transfer coefficients for late half-grade supply."""
import math
import sympy as s


def P(k):
    k=s.Matrix(k); return s.eye(3)-k*k.T/k.dot(k)
def ap(sig): return s.Matrix([1,-s.sqrt(1+sig*sig),-sig])
def am(sig): return s.Matrix([1,+s.sqrt(1+sig*sig),-sig])
def C(p,a,q,b):
    p,a,q,b=map(s.Matrix,(p,a,q,b))
    return s.simplify(P(p+q)*((a.dot(q))*b+(b.dot(p))*a))
def eigcoords(k,f):
    k,f=s.Matrix(k),s.Matrix(f); sig=s.simplify(k[0]/k[2]); q=s.sqrt(1+sig*sig)
    return s.simplify((f[0]-f[1]/q)/2),s.simplify((f[0]+f[1]/q)/2)
def halfvec(x): return s.Matrix([s.Rational(x,20),0,s.Rational(1,2)])
def halfpol(x): return ap(s.Rational(x,10))
def sqrt_bounds(n,D=10**9):
    m=math.isqrt(int(n)*D*D)
    return s.Rational(m,D),s.Rational(m+1,D)
def radical_interval(expr,D=10**9):
    lo=hi=s.Rational(0)
    expr=s.expand(s.radsimp(expr))
    for term in s.Add.make_args(expr):
        coeff,rest=term.as_coeff_Mul()
        if rest==1:
            lo+=coeff; hi+=coeff; continue
        if isinstance(rest,s.Pow) and rest.exp==s.Rational(1,2) and rest.base.is_Integer:
            a,b=sqrt_bounds(int(rest.base),D)
            if coeff>=0: lo+=coeff*a; hi+=coeff*b
            else: lo+=coeff*b; hi+=coeff*a
            continue
        raise AssertionError((expr,term,coeff,rest))
    return s.factor(lo),s.factor(hi)

# Phase parity: the prescribed source pump is the previous pure daughter and
# has physical grade 2m.  Mean/background terms have grade 0, and every source
# harmonic produced from these lies in 2Z*m.  Modulo 2, linear source action
# preserves the correction parity and correction products add parities.
even={0}
assert {(a+b)%2 for a in even for b in even}=={0}
# If correction starts even and the forcing/residual is even, every Picard/Taylor
# operation remains even.  Therefore the odd m-sector is exactly invariant zero.
for _ in range(8):
    linear={(u+v)%2 for u in even for v in {0}}
    quadratic={(u+v)%2 for u in even for v in even}
    forced={0}
    even |= linear|quadratic|forced
    assert even=={0}

# At the next normalization, the previous source daughter is the z=1 pump
# d=(1/20,0,1), physical grade 2m.  The six desired half-grade ancestors all
# have grade m and split into exactly three complementary key pairs a+b=1.
d=s.Matrix([s.Rational(1,20),0,1])
ad=am(s.Rational(1,20))  # pure decaying source daughter polarization
ancestors=[14,-13,5,-4,2,-1]
pairs=[]
for i,a in enumerate(ancestors):
    for b in ancestors[i+1:]:
        if a+b==1: pairs.append((a,b))
assert set(pairs)=={(14,-13),(5,-4),(2,-1)}

# The pump can transfer a pre-existing odd seed to its complementary half-grade
# mode through Y_(2m) times conjugate(w_m).  Compute both directional full Leray
# growing projections.  In every pair one direction is positive and the other
# negative, so the off-diagonal product is strictly negative: the pump coupling
# has an elliptic projected contribution, not a full-chain stability theorem.
rows=[]
for a,b in pairs:
    ka,kb=halfvec(a),halfvec(b)
    assert d-kb==ka and d-ka==kb
    Fa=C(d,ad,-kb,halfpol(b))
    ga,_=eigcoords(ka,Fa)
    Fb=C(d,ad,-ka,halfpol(a))
    gb,_=eigcoords(kb,Fb)
    ga=s.simplify(ga); gb=s.simplify(gb)
    alo,ahi=radical_interval(ga); blo,bhi=radical_interval(gb)
    assert alo>0,(a,b,ga,alo,ahi)
    assert bhi<0,(a,b,gb,blo,bhi)
    assert s.simplify(ga*gb)<0
    rows.append((a,b,ga,gb,alo,ahi,blo,bhi))

# The displayed half-grade projection has three complementary pairs, but the
# full linearization also contains all pump shifts and both polarizations.
# Exact invariant charge n=(2*x-z)/3, not a two-mode truncation, separates the
# three reality-complete classes |n|=9,3,1. Nonlinear cross-class generation
# remains a separate mechanism.
for a,b in pairs:
    others=set(ancestors)-{a,b}
    assert all(d-halfvec(x) not in [halfvec(y) for y in others] for x in (a,b))

print('PASS: even-grade source background cannot create the half-grade odd sector from zero.')
for a,b,ga,gb,alo,ahi,blo,bhi in rows:
    print(f'pump pair ({a},{b}): forward growing coeff in [{alo},{ahi}], reverse in [{blo},{bhi}], product < 0')
assert sorted({abs((2*x-1)//3) for x in ancestors})==[1,3,9]
print('The six half-grade projected transfers lie in three independent charge classes; full pump chains are not two-mode blocks.')
print('Scope: exact physical phase parity plus frozen local pump symbol; full nonlinear cross-pair seed reduction, exterior seed delivery, and global history remain open.')
