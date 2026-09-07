#!/usr/bin/env python3
"""Exact finite regression oracle, not a universal PDE proof.

Uses only Python's standard library. Exponential-polynomial coefficients are
represented exactly by rational numbers: (rate, degree) -> coefficient of
exp(-rate*t)*t**degree. Rates use the normalized nu=K=1 Duhamel problem.
Run from any directory; JSON is printed to stdout.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb, factorial
import json

Poly = dict[tuple[int, int], F]
COUNTS: dict[str, int] = {}


def check(ok: bool, group: str) -> None:
    if not ok:
        raise AssertionError(group)
    COUNTS[group] = COUNTS.get(group, 0) + 1


def clean(p: Poly) -> Poly:
    return {k: v for k, v in p.items() if v}


def add(p: Poly, q: Poly) -> Poly:
    out = p.copy()
    for k, v in q.items():
        out[k] = out.get(k, F(0)) + v
    return clean(out)


def scale(p: Poly, a: F) -> Poly:
    return clean({k: a*v for k, v in p.items()})


def derivative(p: Poly) -> Poly:
    out: Poly = {}
    for (r, d), c in p.items():
        out = add(out, {(r, d): -r*c})
        if d:
            out = add(out, {(r, d-1): d*c})
    return out


def shift_rate(p: Poly, amount: int) -> Poly:
    return {(r+amount, d): c for (r, d), c in p.items()}


def initial(p: Poly) -> F:
    return sum((c for (r, d), c in p.items() if d == 0), F(0))


def convolve(p: Poly, rate: int) -> Poly:
    """Return integral_0^t exp(-rate*(t-s))*p(s) ds exactly."""
    out: Poly = {}
    for (r, m), c in p.items():
        delta = rate-r
        if delta == 0:
            out = add(out, {(rate, m+1): c/F(m+1)})
        else:
            for j in range(m+1):
                a = c * F((-1)**j * factorial(m),
                          factorial(m-j)*delta**(j+1))
                out = add(out, {(r, m-j): a})
            a0 = -c * F((-1)**m * factorial(m), delta**(m+1))
            out = add(out, {(rate, 0): a0})
    return out


def coefficient_table(order: int, cutoff: int | None) -> list[dict[int, Poly]]:
    """Factor out (-i*a0)**m from the +K transverse Fourier branch."""
    rows: list[dict[int, Poly]] = [{0: {(1, 0): F(1)}}]
    for m in range(1, order+1):
        prev = rows[-1]
        out: dict[int, Poly] = {}
        for n in range(-m, m+1):
            if cutoff is not None and abs(n)>cutoff:
                continue
            src = scale(shift_rate(add(prev.get(n-1, {}),
                                        prev.get(n+1, {})), 1), F(1, 2))
            p = convolve(src, n*n+1)
            if p:
                out[n] = p
        rows.append(out)
    return rows


def main() -> None:
    # Actual orthogonal NS parent vectors: projection leaves K*e3 unchanged.
    for k in range(1, 17):
        p, q = (k, 0, 0), (0, k, 0)
        r = tuple(p[i]+q[i] for i in range(3))
        numerator = (0, 0, k)
        check(sum(p[i]*q[i] for i in range(3)) == 0, 'orthogonal_parent')
        check(sum(r[i]*numerator[i] for i in range(3)) == 0,
              'leray_numerator_survives')
        for nu in (F(1, 4), F(1), F(3, 2)):
            low = nu*k*k
            high = nu*sum(x*x for x in r)
            check(high == 2*low and k != 0, 'homological_obstruction')
        check(sum(x*x for x in r)>k*k, 'high_mode_outside_coarse')

    # Orthogonally compressed cos*x2-derivative: i times a real symmetric
    # adjacency matrix. Row/column sums <=1 prove the normalized norm bound.
    for cutoff in range(9):
        indices = list(range(-cutoff, cutoff+1))
        mat = [[F(1, 2) if abs(i-j)==1 else F(0)
                for j in indices] for i in indices]
        check(all(mat[i][j] == mat[j][i]
                  for i in range(len(indices)) for j in range(len(indices))),
              'compressed_skew_adjoint')
        check(all(sum(row)<=1 for row in mat), 'operator_schur_bound')

    order = 7
    full = coefficient_table(order, None)
    check(full[1] == {-1: {(2, 1): F(1, 2)},
                      1: {(2, 1): F(1, 2)}}, 'first_resonant_coefficient')
    for cutoff in (0, 1, 2, 4, 8):
        rows = coefficient_table(order, cutoff)
        for m in range(order+1):
            for n, poly in rows[m].items():
                if m == 0:
                    check(initial(poly) == 1, 'initial_coefficient')
                    continue
                src = scale(shift_rate(add(rows[m-1].get(n-1, {}),
                                            rows[m-1].get(n+1, {})), 1), F(1, 2))
                lhs = add(derivative(poly), scale(poly, F(n*n+1)))
                check(lhs == src, 'exact_duhamel_recurrence')
                check(initial(poly) == 0, 'zero_initial_correction')
                check(abs(n)<=m and (n-m)%2 == 0, 'support_and_parity')
            if m<=cutoff:
                check(rows[m] == full[m], 'lossless_below_cutoff')
        if cutoff == 0:
            check(all(not row for row in rows[1:]), 'coarse_omits_resonance')

    # Scalar majorants E_m=exp(-t)(1-exp(-t))**m/m! have exactly the
    # recurrence used in the simplex estimate, with no floating-point fit.
    for m in range(1, 13):
        env = {(j+1, 0): F((-1)**j*comb(m, j), factorial(m))
               for j in range(m+1)}
        prev = {(j+1, 0): F((-1)**j*comb(m-1, j), factorial(m-1))
                for j in range(m)}
        check(add(derivative(env), env) == shift_rate(prev, 1),
              'factorial_envelope_recurrence')
        check(initial(env) == 0, 'factorial_envelope_initial')
    for j in range(16):
        m = 2**j-1
        check(m*m+1 <= 4**j, 'dyadic_lossless_support')
        check(m+1 == 2**j, 'dyadic_tail_order')

    # Negative controls: a sign flip, omitted source rate, or dropping the
    # resonant daughter is detected by the SAME exact residual check.
    good = {(2, 1): F(1, 2)}
    src = {(2, 0): F(1, 2)}
    wrong_sign = scale(good, F(-1))
    check(add(derivative(wrong_sign), scale(wrong_sign, F(2))) != src,
          'negative_wrong_ns_sign')
    wrong_rate = convolve({(1, 0): F(1, 2)}, 2)
    check(add(derivative(wrong_rate), scale(wrong_rate, F(2))) != src,
          'negative_missing_shear_decay')
    check({} != src, 'negative_dropped_resonant_forcing')
    print(json.dumps({
        'status': 'PASS', 'arithmetic': 'exact rational, standard library',
        'assertions': sum(COUNTS.values()), 'groups': COUNTS,
        'ranges': {'parent_K': [1, 16], 'viscosities': ['1/4', '1', '3/2'],
                   'max_duhamel_order': order, 'compressed_cutoffs': [0,1,2,4,8],
                   'max_envelope_order': 12, 'dyadic_j': [0,15]},
        'non_claims': ['not a universal PDE proof', 'not independent mathematical review',
                       'no numerical solver or full-repository verifier run',
                       'no arbitrary-data NS-R3 progress certified']
    }, indent=2))


if __name__ == '__main__':
    main()
