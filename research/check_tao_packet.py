#!/usr/bin/env python3
"""Exact finite regressions for the Tao packet audit, not PDE certification."""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
import json
from typing import TypeAlias

Quad: TypeAlias = tuple[F, F]  # a+b*sqrt(2)
Vec: TypeAlias = tuple[F, F]
counts: dict[str, int] = {}


def check(group: str, condition: bool, description: str) -> None:
    if not condition:
        raise AssertionError(f"{group}: {description}")
    counts[group] = counts.get(group, 0) + 1


def add(x: Quad, y: Quad) -> Quad:
    return x[0] + y[0], x[1] + y[1]


def mul(x: Quad, y: Quad) -> Quad:
    return x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def pump(v: Vec) -> Vec:
    x, y = v
    return -x * y, x * x


def bilinear(v: Vec, w: Vec) -> Vec:
    x, y = v
    a, b = w
    return -(x * b + a * y) / 2, x * a


def dot(v: Vec, w: Vec) -> F:
    return v[0] * w[0] + v[1] * w[1]


def main() -> None:
    counts.clear()
    # The same smooth solenoidal sequence can have bounded L2 and L^{3,q}
    # but unbounded L3. These are exponent checks, not simulated solutions.
    for q in (F(7, 2), F(4), F(6), F(12), F(100)):
        alpha = (1 / q + F(1, 3)) / 2
        check("lorentz_gap", q * alpha > 1, "finite Lorentz logarithmic integral")
        check("lorentz_gap", 3 * alpha < 1, "divergent cubic logarithmic integral")
        check("lorentz_gap", 1 - 3 * alpha > 0, "positive cubic growth exponent")
    check("lorentz_gap", F(3, 2) - 3 / F(3, 2) == -F(1, 2),
          "dual packet Lorentz norm scales as lambda^(-n/2)")
    for x, y, z in ((1, 2, 3), (-2, 5, 0), (3, -1, 4), (0, 2, -3)):
        check("solenoidal_cutoff", x * (-y) + y * x + z * 0 == 0,
              "radial gradient is orthogonal to the rotation field")

    check("cascade_exponents", F(1, 2) - F(1, 100) == F(49, 100),
          "packet critical amplitude grows")
    check("cascade_exponents", F(5, 2) - F(1, 100) == F(249, 100),
          "checkpoint time upper bounds are summable")
    check("cascade_exponents", 2 * 4 - 10 == -2,
          "bootstrap energy tail controls H4")
    check("cascade_exponents", 2 * 10 - 10 > 0,
          "the same tail alone does not directly bound H10")
    for n0 in (1, 2, 17, 100):
        check("cascade_exponents",
              -F(n0, 100) - F(249 * n0, 100) == -F(5 * n0, 2),
              "summed horizon numerator")

    # Exact geometric-series identity in Q(sqrt(2)), avoiding floating point.
    one: Quad = (F(1), F(0))
    r: Quad = (F(0), F(1, 2))
    total: Quad = (F(2), F(1))
    check("dyadic_tail", mul((F(1), -F(1, 2)), total) == one,
          "1/(1-2^(-1/2))=2+sqrt(2)")
    partial: Quad = (F(0), F(0))
    power = one
    for _ in range(20):
        partial = add(partial, power)
        power = mul(power, r)
        check("dyadic_tail", add(partial, mul(power, total)) == total,
              "finite sum plus exact tail")

    for n0 in (F(1, 8), F(1), F(3)):
        for rho in (3 * n0, F(7, 2) * n0, 4 * n0, 17 * n0, 1000 * n0):
            j = 0
            while 2 ** (j + 1) * n0 < rho:
                j += 1
            nj = 2 ** j * n0
            check("packet_threshold", nj >= rho / 2,
                  "first surviving increment has N_J>=rho/2")
            check("packet_threshold", nj < rho,
                  "all preceding increments and coarse term are orthogonal")

    # A finite pump has cubic cancellation but a nonzero mixed energy term.
    # It is only an algebra oracle, not a fluid solution or a Tao PDE solver.
    for x, y in product(range(-3, 4), repeat=2):
        v = F(x), F(y)
        check("energy_algebra", dot(v, pump(v)) == 0, "cubic cancellation")
        check("energy_algebra", bilinear(v, v) == pump(v), "polarisation")
    z, v = (F(1), F(1)), (F(1), F(0))
    check("energy_algebra", 2 * dot(z, bilinear(z, v)) == 1,
          "the mixed term must not be discarded in the convergence proof")
    zplusv = z[0] + v[0], z[1] + v[1]
    qsum = pump(zplusv)
    qz, qv, mixed = pump(z), pump(v), bilinear(z, v)
    check("energy_algebra", qsum == (qz[0] + qv[0] + 2 * mixed[0],
                                     qz[1] + qv[1] + 2 * mixed[1]),
          "exact quadratic difference expansion")

    # Common translation phases multiply precisely at p+q, not at an
    # independently assigned output carrier. Integer half-period phases
    # suffice to check this identity without numerical complex arithmetic.
    pairs = (((1, 0, 0), (0, 1, 0)), ((1, 2, -1), (-2, 1, 1)),
             ((2, -1, 3), (1, 1, -2)), ((-1, 0, 2), (1, -2, 1)))
    shifts = ((1, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 1))
    def phase(k: tuple[int, int, int], a: tuple[int, int, int]) -> int:
        return 1 if sum(x * y for x, y in zip(k, a)) % 2 == 0 else -1
    for (p, q), a in product(pairs, shifts):
        k = tuple(x + y for x, y in zip(p, q))
        check("translation_phase", phase(p, a) * phase(q, a) == phase(k, a),
              "convolution respects the common-translation character")
    v = (F(1), F(0))
    translated = (-v[0], -v[1])
    qv = pump(v)
    check("translation_phase", pump(translated) != (-qv[0], -qv[1]),
          "an assigned same-carrier pump fails the phase identity")

    for delta in (F(1, 32), F(1, 16), F(1, 10), F(6, 25)):
        check("one_carrier_support", 2 * delta < F(1, 2),
              "zero-centred output misses the middle annulus")
        check("one_carrier_support", 2 - 2 * delta > F(3, 2),
              "double-carrier output misses the middle annulus")

    print(json.dumps({
        "status": "PASS",
        "assertions": sum(counts.values()),
        "groups": counts,
        "scope": "exact finite algebra and exponent regressions only",
        "not_certified": ["PDE existence or convergence", "Tao checkpoint localisation",
                          "independent mathematical audit", "NS-R3 regularity"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
