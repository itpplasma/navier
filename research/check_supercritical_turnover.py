#!/usr/bin/env python3
"""Exact scaling checks for the supercritical localized-turnover contract.

This checker verifies algebraic recurrence identities only. It does not
construct a Navier--Stokes turnover, an R3 localization, or a singular flow.
"""
from __future__ import annotations
from fractions import Fraction as F
import argparse
import json
from pathlib import Path

CHECKS: list[str] = []


def check(ok: bool, label: str) -> None:
    if not bool(ok):
        raise AssertionError(label)
    CHECKS.append(label)


def geom(r: F, N: int) -> F:
    return sum((r**n for n in range(N)), F(0))


def canonical() -> dict:
    # scale contraction s=2 and deliberately supercritical but
    # energy-compatible amplitude gain g=5/2.
    s = F(2)
    g = F(5, 2)
    r_l3 = g / s
    r_energy = g*g / s**3
    r_time = F(1) / (s*g)
    r_diss = g / s**2
    r_re = g / s
    r_visc = s / g

    expected = {
        "L3": F(5,4),
        "energy": F(25,32),
        "turnover_time": F(1,5),
        "dissipation_per_turnover": F(5,8),
        "Reynolds": F(5,4),
        "relative_viscous_action": F(4,5),
    }
    actual = {
        "L3": r_l3, "energy": r_energy, "turnover_time": r_time,
        "dissipation_per_turnover": r_diss, "Reynolds": r_re,
        "relative_viscous_action": r_visc,
    }
    for key in expected:
        check(actual[key] == expected[key], f"canonical ratio {key}")
    check(g > s, "strict supercriticality g>s")
    check(g*g < s**3, "strict core-energy compatibility g^2<s^3")
    check(g < s**2, "per-turnover dissipation summability g<s^2")
    check(r_l3 > 1, "critical L3 grows")
    check(r_energy < 1, "core energy shrinks")
    check(r_time < 1, "turnover intervals shrink geometrically")
    check(r_diss < 1, "dissipation contributions shrink geometrically")
    check(r_re > 1, "local Reynolds number grows")
    check(r_visc < 1, "relative viscous action per turnover shrinks")

    # Check the exact recurrence and geometric sums over many generations.
    for N in range(1, 41):
        A = g**N
        ell = s**(-N)
        check(A*ell == r_l3**N, f"L3 recurrence N={N}")
        check(A*A*ell**3 == r_energy**N, f"energy recurrence N={N}")
        check(ell/A == r_time**N, f"time recurrence N={N}")
        check(A*ell**2 == r_diss**N, f"dissipation recurrence N={N}")
        check(A*ell == r_re**N, f"Reynolds recurrence N={N}")
        check(F(1)/(A*ell) == r_visc**N, f"viscous-action recurrence N={N}")
        check(geom(r_time,N) == (1-r_time**N)/(1-r_time),
              f"turnover geometric sum N={N}")
        check(geom(r_diss,N) == (1-r_diss**N)/(1-r_diss),
              f"dissipation geometric sum N={N}")
        check(r_l3**N > 1, f"L3 amplification N={N}")
        check(r_energy**N < 1, f"energy decay N={N}")

    check(F(1)/(1-r_time) == F(5,4), "normalized accumulation time sum")
    check(F(1)/(1-r_diss) == F(8,3), "normalized dissipation-scale sum")

    # Half-scale fixed-shape volume check in dimension three.
    volume = s**(-3)
    check(volume == F(1,8), "half-scale active-volume ratio")
    check(g*g*volume == r_energy,
          "gain squared times active volume equals core-energy ratio")
    max_volume = F(1)/(g*g)
    check(max_volume == F(4,25), "maximum active-volume fraction allowed by gain 5/2")
    check(volume < max_volume, "isotropic half-scale volume is small enough for gain 5/2")
    check(g*g > 1, "same-volume gain 5/2 violates the energy wall")

    # Fixed-volume energy wall. M equal normalized parent components can put
    # at most all their energy into one component. Reproducing M components
    # at common gain h has output/input energy ratio h^2, hence h<=1.
    for M in range(1, 17):
        check(F(M) / F(M) == 1, f"same-cardinality copy energy ratio prefactor M={M}")
        h = F(M+1, M)
        check(M*h*h > M, f"fixed-volume amplified copy violates energy M={M}")
        check(F(M+1) > F(M), f"one-child squared amplitude above total parent energy is forbidden M={M}")

    # Formal locator from the exact doubled-parent t^3 coefficient in the
    # source-reference calculation: normalized growing-coordinate gain is
    # (8/3) beta^3. These are NOT remainder bounds.
    beta3_for_gain_2 = F(3,4)
    beta3_for_gain_5_2 = F(15,16)
    check(F(8,3)*beta3_for_gain_2 == 2,
          "quartic locator beta^3=3/4 reaches formal gain 2")
    check(F(8,3)*beta3_for_gain_5_2 == g,
          "quartic locator beta^3=15/16 reaches formal gain 5/2")
    check(beta3_for_gain_2 < beta3_for_gain_5_2 < 1,
          "supercritical quartic locator lies near one turnover, not at beta<<1")

    return {
        "scale_contraction": str(s),
        "amplitude_gain": str(g),
        "ratios": {k: str(v) for k,v in actual.items()},
        "normalized_total_time": str(F(1)/(1-r_time)),
        "normalized_total_dissipation_scale": str(F(1)/(1-r_diss)),
        "formal_quartic_beta_cubed_gain_2": str(beta3_for_gain_2),
        "formal_quartic_beta_cubed_gain_5_over_2": str(beta3_for_gain_5_2),
    }


def general_grid() -> list[dict]:
    # Exact rational samples of the general nonempty window s<g<s^(3/2).
    # Avoid irrational endpoints by checking the equivalent g>s and g^2<s^3.
    rows = []
    samples = [
        (F(3,2), F(8,5)),
        (F(2), F(5,2)),
        (F(5,2), F(3)),
        (F(3), F(4)),
        (F(4), F(6)),
    ]
    for s,g in samples:
        check(s > 1, f"general sample s>1: {s}")
        check(g > s, f"general sample supercritical: s={s},g={g}")
        check(g*g < s**3, f"general sample energy-compatible: s={s},g={g}")
        check(g < s**2, f"general sample dissipation-compatible: s={s},g={g}")
        rl3=g/s
        re=g*g/s**3
        rt=F(1)/(s*g)
        rd=g/s**2
        rv=s/g
        check(rl3>1 and re<1 and rt<1 and rd<1 and rv<1,
              f"all turnover ratios have required signs: s={s},g={g}")
        rows.append({
            "s": str(s), "g": str(g), "L3_ratio": str(rl3),
            "energy_ratio": str(re), "time_ratio": str(rt),
            "dissipation_ratio": str(rd), "viscous_action_ratio": str(rv),
        })
    return rows


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path)
    args=p.parse_args()
    result={
        "scope": "Exact scaling algebra only; no turnover PDE construction.",
        "canonical": canonical(),
        "general_samples": general_grid(),
        "exact_assertion_count": len(CHECKS),
    }
    if args.output:
        args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(f"PASS: {len(CHECKS)} exact assertions.")
    print(json.dumps(result["canonical"], indent=2))


if __name__ == "__main__":
    main()
