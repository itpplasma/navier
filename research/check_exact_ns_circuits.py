#!/usr/bin/env python3
"""Exact arithmetic regressions only; not a PDE proof or independent audit."""
from __future__ import annotations
import argparse
import json
from collections import defaultdict
from itertools import permutations
from pathlib import Path
import sympy as s

Vec = s.Matrix
ZERO = s.zeros(3, 1)
checks: list[str] = []


def check(label, condition):
    if not bool(condition):
        raise AssertionError(label)
    checks.append(label)


def simplify_field(field):
    result = {}
    for k, value in field.items():
        value = s.simplify(value)
        if value != ZERO:
            result[k] = value
    return result


def add_fields(*fields):
    result = defaultdict(lambda: s.zeros(3, 1))
    for field in fields:
        for k, value in field.items():
            result[k] += value
    return simplify_field(result)


def bilinear(left, right):
    """Full ordered convolution, no aliasing, cutoff or daughter deletion."""
    result = defaultdict(lambda: s.zeros(3, 1))
    for p, a in left.items():
        for q, b in right.items():
            k = tuple(x + y for x, y in zip(p, q))
            if k == (0, 0, 0):
                continue  # Divergence form gives the exact zero mean.
            K = Vec(k)
            value = -s.I * Vec(q).dot(a) * b
            result[k] += value - K * K.dot(value) / K.dot(K)
    return simplify_field(result)


def real_field(positive):
    return positive | {tuple(-x for x in k): s.conjugate(v)
                       for k, v in positive.items()}


def norm2(field):
    return s.simplify(sum(s.conjugate(v).dot(v) for v in field.values()))


def inner(left, right):
    return s.simplify(sum(s.conjugate(v).dot(right.get(k, ZERO))
                          for k, v in left.items()))


def constraints(name, field):
    check(name + ': divergence', all(Vec(k).dot(v) == 0
                                    for k, v in field.items()))
    check(name + ': reality', all(field.get(tuple(-x for x in k)) == s.conjugate(v)
                                 for k, v in field.items()))


def derivatives(field):
    first = bilinear(field, field)
    second = add_fields(bilinear(field, first), bilinear(first, field))
    return first, second


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', type=Path)
    args = parser.parse_args()
    p, q = (1, 0, 0), (0, 1, 0)
    pair = real_field({p: Vec([0, 1, 1]), q: Vec([-1, 0, -1])})
    first, second = derivatives(pair)
    check('two: complete first derivative', first == real_field({(1, 1, 0): Vec([0, 0, 2*s.I])}))
    check('two: complete second derivative', second == real_field({
        p: Vec([0, 0, -2]), q: Vec([0, 0, 2]),
        (2, 1, 0): Vec([0, 0, 2]), (1, 2, 0): Vec([0, 0, -2])}))
    for name, field in [('two input', pair), ('two Q', first), ('two DQ.Q', second)]:
        constraints(name, field)
    check('two: complete nonlinear second energy derivative', norm2(first) + inner(pair, second) == 0)

    e = [Vec([int(i == j) for i in range(3)]) for j in range(3)]
    sigma = Vec([1, 1, 1])
    triple = real_field({tuple(v): sigma - v for v in e})
    first3, second3 = derivatives(triple)
    expected1 = {}
    expected2 = {tuple(v): -2*(sigma-v) for v in e}
    for i in range(3):
        for j in range(i+1, 3):
            ell = 3-i-j
            expected1[tuple(e[i]+e[j])] = -2*s.I*e[ell]
        for j in range(3):
            if i != j:
                ell = 3-i-j
                expected2[tuple(2*e[i]+e[j])] = -2*e[ell]
        expected2[tuple(2*e[i]-sigma)] = -s.Rational(2,3)*(sigma+e[i])
    check('three: complete first derivative', first3 == real_field(expected1))
    check('three: complete second derivative', second3 == real_field(expected2))
    check('three: cancelled triple sum', (1,1,1) not in second3)
    check('three: mode counts', (len(first3), len(second3)) == (6,24))
    check('three: second energy derivative', norm2(first3)+inner(triple, second3) == 0)
    constraints('three second derivative', second3)
    # A field with occupied daughter and return modes: both conservation pairings
    # now include nonzero terms instead of being vacuous support orthogonality.
    mixed = add_fields(triple,
                       {k:v/7 for k,v in first3.items()},
                       {k:v/11 for k,v in second3.items()})
    qm = bilinear(mixed, mixed)
    curlm = {k:s.I*Vec(k).cross(v) for k,v in mixed.items()}
    check('occupied network: energy cancellation', inner(mixed,qm) == 0)
    check('occupied network: helicity cancellation', inner(curlm,qm) == 0)

    def level(n):
        m = n//2
        base = 2**n*sigma
        vectors = [base+3**m*Vec([1,0,-1])] if n % 2 == 0 else [
            base+3**m*Vec([1,1,-2]), base+3**m*Vec([2,-1,-1])]
        return set().union(*(set(permutations(tuple(v))) for v in vectors))

    table = []
    for n in range(5):
        parents = level(n)
        initial = real_field({k:-s.I*(sigma-Vec(k)*Vec(k).dot(sigma)/Vec(k).dot(Vec(k)))
                              for k in parents})
        output = bilinear(initial, initial)
        positive = {k:v for k,v in output.items() if sum(k)>0}
        intended = {k:v for k,v in positive.items() if k in level(n+1)}
        side = {k:v for k,v in positive.items() if k not in level(n+1)}
        ratio = s.factor(norm2(side)/norm2(intended))
        expected = 3*s.Rational(3*4**n*2+3*3**n, 3*4**n*2+3**n)
        check(f'six level {n}: ALL source modes', len(output)==24 and len(intended)==len(side)==6)
        check(f'six level {n}: exact omitted/intended ratio', ratio==expected)
        check(f'six level {n}: ratio exceeds three', ratio>3)
        parent_radius2 = Vec(next(iter(parents))).dot(Vec(next(iter(parents))))
        check(f'six level {n}: all sources above parents', all(Vec(k).dot(Vec(k))>parent_radius2 for k in output))
        constraints(f'six level {n}', output)
        table.append({'level':n, 'intended_norm2_positive':str(norm2(intended)),
                      'omitted_norm2_positive':str(norm2(side)), 'ratio':str(ratio)})
        if n == 0:
            check('six level zero: exact intended norm', norm2(intended)==s.Rational(216,25))
            check('six level zero: exact omitted norm', norm2(side)==s.Rational(5832,175))
            check('six level zero: exact omitted modes', set(side)==set(permutations((3,2,1))))

    # Rational half-angle parameterization proves the generic symbol identities
    # as rational identities. B,D stand for the conjugate coefficients at q.
    r,z,t,g,A,B,C,D = s.symbols('r z t g A B C D', real=True, nonzero=True)
    c=(1-t*t)/(1+t*t); h=2*t/(1+t*t)
    p=Vec([r*c,-r*h,z]); q=Vec([r*c,r*h,z])
    m1=Vec([z*c,-z*h,-r]); m2=Vec([z*c,z*h,-r])
    t1=Vec([h,c,0]); t2=Vec([-h,c,0])
    def proj(k,v):
        return v-k*k.dot(v)/k.dot(k)
    a=A*m1+C*t1; b=B*m2+D*t2
    minus=proj(p-q,-q.dot(a)*b+p.dot(b)*a)
    expected=(A*D+C*B)*Vec([-2*r*z*h,0,2*r*r*h*c])
    check('symbolic: generic difference identity', all(s.factor(x)==0 for x in minus-expected))
    a=m1+s.I*g*t1; b=m2+s.I*g*t2
    plus=proj(p+q,q.dot(a)*b+p.dot(b)*a)
    expected=(-4*r*z*(r*r+z*z-g*g)*h*h*c/(z*z+r*r*c*c))*Vec([z,0,-r*c])
    check('symbolic: helical-mixture sum identity', all(s.factor(x)==0 for x in plus-expected))
    recurrence=lambda n,i: s.Rational(2**n-(-1)**n,3)*sigma+(-1)**n*e[i]
    check('three: complementary-sum recurrence', all(
        recurrence(n,j)+recurrence(n,k)==recurrence(n+1,i)
        for n in range(7) for i in range(3)
        for j,k in [[a for a in range(3) if a!=i]]))
    report={'status':'PASS','assertions':len(checks),'checks':checks,
            'six_carrier_table':table,
            'scope':'Exact finite and symbolic arithmetic only. No PDE proof, terminal bound, independent audit or full repository verification.'}
    if args.json:
        args.json.parent.mkdir(parents=True,exist_ok=True)
        args.json.write_text(json.dumps(report,indent=2)+'\n')
    print(f'PASS: {len(checks)} exact assertions; full-pair convolution and symbolic identities.')
    print(report['scope'])

if __name__ == '__main__':
    main()
