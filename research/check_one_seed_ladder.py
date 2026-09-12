#!/usr/bin/env python3
"""Exact shortest-time trees and the one-seed bridge-balance obstruction.

The model is the full frozen source-reference convolution, initialized with
one decaying pump and one growing seed plus reality partners. Shortest-time
coefficients are computed in exact rational arithmetic; the only radicals are
in the passive transverse component. No PDE trajectory is certified here.
See evidence/2026-09-12-one-seed-ladder-balance.md for the all-orders scope.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import isqrt

ZERO = (Q(0),) * 4
# (radial, sqrt(26) coefficient, sqrt(401) coefficient, axial)
SEED = (Q(1), -Q(1, 5), Q(0), -Q(1, 5))
PUMP = (Q(1), Q(0), Q(1, 20), -Q(1, 20))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(a, c):
    return tuple(x * c for x in a)


def wave(n, p):
    """n seed wavevectors + p pump wavevectors (radial, axial)."""
    return Q(n, 10) + Q(p, 20), Q(n, 2) + p


def bilinear(k, a, q, b):
    """Ordered Leray symbol, with its common -i factor stripped."""
    h = k[0] + q[0], k[1] + q[1]
    den = h[0] ** 2 + h[1] ** 2
    if not den:
        return ZERO
    v = scale(b, a[0] * q[0] + a[3] * q[1])
    dot = (v[0] * h[0] + v[3] * h[1]) / den
    return v[0] - h[0] * dot, v[1], v[2], v[3] - h[1] * dot


def shortest_cone(ns, np, seed_sign, pump_sign):
    """All ordered trees at minimum total degree a+b and time a+b-1.

    Every leaf must have the indicated sign: an opposite leaf pair or a
    linear vertex would need a later time order. This is an exact coefficient
    extraction, not a Galerkin approximation or a selected shear path.
    """
    w = {(1, 0): SEED, (0, 1): PUMP}
    for degree in range(2, ns + np + 1):
        for a in range(max(0, degree - np), min(ns, degree) + 1):
            b = degree - a
            v = ZERO
            for i in range(a + 1):
                for j in range(b + 1):
                    left, right = (i, j), (a - i, b - j)
                    if left not in w or right not in w:
                        continue
                    k = wave(seed_sign * i, pump_sign * j)
                    q = wave(seed_sign * (a - i), pump_sign * (b - j))
                    v = add(v, bilinear(k, w[left], q, w[right]))
            w[a, b] = scale(v, Q(1, degree - 1))
            k = wave(seed_sign * a, pump_sign * b)
            assert k[0] * w[a, b][0] + k[1] * w[a, b][3] == 0
    return w


def sqrt_interval(x, digits=80):
    x = Q(x)
    assert x > 0
    den = 10 ** digits
    m = isqrt(x.numerator * den * den // x.denominator)
    lo, hi = Q(m, den), Q(m + 1, den)
    assert lo * lo <= x < hi * hi
    return lo, hi


def interval_scale(c, bounds):
    a, b = bounds
    return (c * a, c * b) if c >= 0 else (c * b, c * a)


def growing_interval(v, n, p):
    k = wave(n, p)
    assert k[1] != 0
    tilt = k[0] / k[1]
    rt = sqrt_interval(1 + tilt * tilt)
    vy_a = interval_scale(v[1], sqrt_interval(26))
    vy_b = interval_scale(v[2], sqrt_interval(401))
    vy = vy_a[0] + vy_b[0], vy_a[1] + vy_b[1]
    # c_+ = (v_x - v_y/sqrt(1+tilt^2))/2.
    quotients = [x / y for x in vy for y in rt]
    return (v[0] - max(quotients)) / 2, (v[0] - min(quotients)) / 2


def sign_certificate(v, n, p, expected):
    lo, hi = growing_interval(v, n, p)
    assert lo > 0 if expected > 0 else hi < 0, (n, p, lo, hi)
    # Compact *outward* rational enclosure, still checked without floats.
    den = 10 ** 20
    lower = lo.numerator * den // lo.denominator
    upper = -((-hi.numerator * den) // hi.denominator)
    assert Q(lower, den) <= lo <= hi <= Q(upper, den)
    return f'[{lower}/{den}, {upper}/{den}]'


def main():
    # In integer keys k=(x/20,0,z/2), pump=(1,2), seed=(2,1).
    # n=(2x-z)/3 and p=(2z-x)/3 are the unique signed leaf counts.
    half_keys = [2, -1, 5, -4, 14, -13]
    charges = {x: (2 * x - 1) // 3 for x in half_keys}
    assert charges == {2: 1, -1: -1, 5: 3, -4: -3, 14: 9, -13: -9}
    targets = [(10, 2), (-8, 2), (4, 2), (-2, 2)]
    target_ns = [(2 * x - z) // 3 for x, z in targets]
    assert target_ns == [6, -6, 2, -2]
    assert [sum(abs(v) for v in target_ns[:2]),
            sum(abs(v) for v in target_ns[2:])] == [12, 4]
    assert 12 - 4 == 8

    forward = shortest_cone(9, 5, 1, -1)
    backward = shortest_cone(9, 5, -1, 1)
    rows = [(1, 0, 'seed 2', 1), (3, -1, 'half 5', 1),
            (5, -2, 'half 8', 1), (7, -3, 'half 11', 1),
            (9, -4, 'half 14', 1), (6, -2, 'outer +5', 1),
            (-1, 1, 'half -1', -1), (-3, 2, 'half -4', 1),
            (-5, 3, 'half -7', -1), (-7, 4, 'half -10', 1),
            (-9, 5, 'half -13', -1), (-6, 4, 'outer -4', -1),
            (-2, 2, 'inner -1', -1)]
    for n, p, label, sign in rows:
        w = forward[n, -p] if n > 0 else backward[-n, p]
        bounds = sign_certificate(w, n, p, sign)
        print(f'{label}: charge {n}, time order {abs(n)+abs(p)-1}, c+ in {bounds}')

    # The inner +2 target is a collinear double seed, so its degree-two
    # coefficient vanishes. Compute the COMPLETE homogeneous Euler jets
    # through time three, with BOTH signs of BOTH initial modes retained.
    initial = {(1, 0): SEED, (-1, 0): SEED, (0, 1): PUMP, (0, -1): PUMP}
    jets = [initial]
    for j in range(3):
        out = {}
        for i in range(j + 1):
            for k, a in jets[i].items():
                for q, b in jets[j - i].items():
                    h = k[0] + q[0], k[1] + q[1]
                    if h == (0, 0):
                        continue
                    out[h] = add(out.get(h, ZERO), bilinear(wave(*k), a, wave(*q), b))
        jets.append({k: scale(v, Q(1, j + 1)) for k, v in out.items() if v != ZERO})
    assert all((2, 0) not in jets[j] for j in range(3))
    bounds = sign_certificate(jets[3][2, 0], 2, 0, 1)
    print('inner +2: charge 2, time order 3, c+ in', bounds)
    for j, values in enumerate(jets):
        for (n, p), v in values.items():
            k = wave(n, p)
            assert k[0] * v[0] + k[1] * v[3] == 0
            # Restore the common (-i)^j to obtain complex Fourier reality.
            assert values[-n, -p] == scale(v, (-1) ** j)
    # One-direction-only shortest cones agree with the unrestricted recurrence.
    for j, values in enumerate(jets):
        for (n, p), v in values.items():
            if n >= 0 and p <= 0 and n - p == j + 1:
                assert v == forward[n, -p]
    assert bilinear(wave(1, 0), SEED, wave(1, 0), SEED) == ZERO

    print('PASS: all shortest-time ladder trees survive, with exact sign enclosures.')
    print('Outer/inner next-parent product ratio is O(|seed|^8) on a fixed short horizon.')
    print('This refutes inheriting the six-independent-input rank-four map from one small seed.')
    print('Scope: frozen reference with fixed pump; no physical global supply or NS-R3 claim.')


if __name__ == '__main__':
    main()
