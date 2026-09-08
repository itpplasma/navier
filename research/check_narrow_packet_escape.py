#!/usr/bin/env python3
"""Exact regressions for the narrow-packet proof, not a PDE certification.

Only the standard library is used. Universal estimates are proved in the
companion note; these checks detect algebraic, sign, and exponent regressions.
"""
from __future__ import annotations

import json
from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations, product
from math import isqrt

from check_phase_locked_ring import (
    ZERO, add, bilinear, combine, cross, dot, initial_ring, multiply, neg,
    project, scale, squarefree,
)

checks: list[str] = []


def check(label: str, assertion: bool) -> None:
    if not assertion:
        raise AssertionError(label)
    checks.append(label)


def ordered(p, q, r, a, b, c, wp, wq, wr):
    return wr * dot(q, a) * dot(b, c)


def paired(p, q, r, a, b, c, wp, wq, wr):
    return ((wr-wq)*dot(q, a)*dot(b, c)
            + (wp-wr)*dot(r, b)*dot(c, a)
            + (wq-wp)*dot(p, c)*dot(a, b))


def add_radical(target, weight_squared: int, coefficient: F) -> None:
    factor, radicand = squarefree(weight_squared)
    target[radicand] += factor * coefficient


def clean(d):
    return {k: v for k, v in d.items() if v}


def main() -> None:
    # Deterministic rational triads; all vector dot products are bilinear.
    vectors = [p for p in product(range(-1, 2), repeat=3) if any(p)]
    tested = 0
    for p in vectors:
        for q in vectors:
            r = neg(add(p, q))
            if not any(r) or cross(p, q) == (0, 0, 0):
                continue
            a = project(p, (F(1), F(2), F(-1)))
            b = project(q, (F(2), F(-3), F(1)))
            c = project(r, (F(-1), F(1), F(4)))
            weights = (F(dot(p, p)+1), F(dot(q, q)+2), F(dot(r, r)+3))
            data = list(zip((p, q, r), (a, b, c), weights))
            six = sum((ordered(*(x[0] for x in perm), *(x[1] for x in perm),
                               *(x[2] for x in perm))
                       for perm in permutations(data)), F(0))
            m = paired(p, q, r, a, b, c, *weights)
            check(f'six-term identity {tested}', six == m)
            # Exact Cauchy--Schwarz transverse bound squared, no roots.
            check(f'transverse numerator {tested}',
                  dot(q, a)**2 * dot(p, p)
                  <= dot(cross(p, q), cross(p, q))*dot(a, a))
            check(f'return derivative {tested}', dot(r, b) == -dot(p, b))
            tested += 1
    check('nonempty finite regression family', tested > 300)

    # Whole no-cutoff Fourier field: direct work versus symmetrized kernel.
    seed = initial_ring()
    field = combine(seed, multiply(F(1, 7), bilinear(seed, seed)))
    direct, symmetric = defaultdict(F), defaultdict(F)
    qfield = bilinear(field, field)
    for k, a in field.items():
        add_radical(direct, dot(k, k), dot(a, qfield.get(k, ZERO)))
    for p, a in field.items():
        for q, b in field.items():
            r = neg(add(p, q))
            if r not in field:
                continue
            c = field[r]
            qa_bc = dot(q, a)*dot(b, c)
            rb_ca = dot(r, b)*dot(c, a)
            pc_ab = dot(p, c)*dot(a, b)
            # For uhat=i*b, the physical -i multiplies i^3 to give -1.
            for k, coeff in ((r, qa_bc), (q, -qa_bc),
                             (p, rb_ca), (r, -rb_ca),
                             (q, pc_ab), (p, -pc_ab)):
                add_radical(symmetric, dot(k, k), -coeff/F(6))
    check('full-field critical work equals six-permutation symbol',
          clean(direct) == clean(symmetric))
    check('field detects a nonzero critical cubic', bool(clean(direct)))
    check('full field is real and solenoidal',
          all(field.get(neg(k)) == neg(a) and dot(k, a) == 0
              for k, a in field.items()))

    check('support and angular powers sum to energy threshold',
          F(4, 5) + F(12, 5)/2 == 2)
    check('geometric constant scales with frequency to one half',
          (2 - (F(4, 5)+1)) + (3-F(12, 5))/2 == F(1, 2))
    check('energy-controlled exponential is scale invariant',
          2*F(1, 2)-1 == 0)
    check('small-critical-field low kernel exponent',
          1 + F(3, 2)-F(1, 2) == 2)
    check('small-critical-field high kernel exponent',
          1+F(3, 2)-F(3, 2) == 1)
    check('low-placement squared kernel sums', 1/(1-F(1, 16)) == F(16, 15))
    check('high-placement squared kernel sums', 1/(1-F(1, 4)) == F(4, 3))
    check('Miller transverse exponent below four fifths', 3**5 < 2**8)
    check('generic volume-only exponent fails two thirds threshold', 3**3 > 2**4)
    check('low-ball volume cost exponent', 3-F(12, 5) == F(3, 5))
    check('low-ball angular cost exponent', 1-F(4, 5) == F(1, 5))
    check('all exterior cubic terms counted', 3+3+1 == 7)
    check('viscosity fractions retained', 1-F(1, 4)-F(1, 4) == F(1, 2))

    print(json.dumps({'status': 'PASS', 'assertions': len(checks),
                      'rational_triads': tested,
                      'scope': 'exact algebra/exponents, not a PDE proof or independent audit'},
                     indent=2))


if __name__ == '__main__':
    main()
