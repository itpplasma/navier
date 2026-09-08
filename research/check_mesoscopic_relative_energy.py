#!/usr/bin/env python3
"""Finite exact checks for mesoscopic full-flow relative-energy obstructions.

These verify algebra and scaling, not a PDE orbit or independent audit.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

import sympy as s


def main(output: Path | None = None) -> None:
    counts: Counter[str] = Counter()

    def check(condition: bool, group: str, label: str) -> None:
        if not condition:
            raise AssertionError(f"{group}: {label}")
        counts[group] += 1

    def eq(left: s.Expr, right: s.Expr, group: str, label: str) -> None:
        check(s.simplify(left-right) == 0, group, label)

    A, K, L, C, nu = s.symbols("A K L C nu", positive=True)
    order = s.symbols("order", real=True)
    rho = L/K
    amplitude = C/A*rho
    eq(amplitude*rho**(order-s.Rational(3,2)),
       C/A*rho**(order-s.Rational(1,2)), "scaling", "whole cloud Hs")
    eq((C*L)**2/L**3, C**2/L, "scaling", "physical cloud energy")
    eq((C*L)**2/L**3*(C*L**2)**2/L**3, C**4,
       "scaling", "small-cloud energy/enstrophy product")
    eq(amplitude*rho**(-1), C/A, "scaling", "normalized cloud critical norm")
    eq(amplitude**2*rho**(-3), C**2/A**2*K/L,
       "scaling", "normalized cloud energy")
    eq((A*K)**2/K**3, A**2/K, "scaling", "physical core energy")
    eq((A*K**2)**2/K**3/(A*K**2), A/K,
       "scaling", "entire physical enstrophy integral")
    eq(nu/A*(A**2/K), nu*A/K,
       "scaling", "positive physical viscosity retained")

    alpha, beta, chi = F(1,4), F(1,4), -F(1,16)
    expected = {
        "physical_cloud_critical": -F(1,16),
        "physical_cloud_energy": -F(3,8),
        "physical_core_energy": -F(1,2),
        "normalized_cloud_energy": F(1,8),
        "normalized_cloud_critical": -F(5,16),
        "normalized_cloud_gradient": -F(11,16),
        "normalized_cloud_third_derivative": -F(35,16),
        "normalized_cloud_speed": -F(17,16),
        "physical_time": -F(9,4),
        "physical_dissipation_bound": -F(3,4),
        "relative_normalization": F(1,2),
        "core_to_cloud_L2_ratio": -F(1,16),
    }
    actual = {
        "physical_cloud_critical": chi,
        "physical_cloud_energy": 2*chi-beta,
        "physical_core_energy": 2*alpha-1,
        "normalized_cloud_energy": 2*chi-2*alpha+1-beta,
        "normalized_cloud_critical": chi-alpha,
        "normalized_cloud_gradient": chi-alpha+(beta-1)/2,
        "normalized_cloud_third_derivative": chi-alpha+F(5,2)*(beta-1),
        "normalized_cloud_speed": chi-alpha+beta-1,
        "physical_time": -alpha-2,
        "physical_dissipation_bound": alpha-1,
        "relative_normalization": 1-2*alpha,
        "core_to_cloud_L2_ratio": alpha-F(1,2)-chi+beta/2,
    }
    for name, value in expected.items():
        check(actual[name] == value, "high_amplitude_exponents", name)

    a0 = F(0)
    exact_ns_exponents = {
        "cloud_energy": 2*chi-2*a0+1-beta,
        "cloud_gradient": chi-a0+(beta-1)/2,
        "cloud_third_derivative": chi-a0+F(5,2)*(beta-1),
        "cloud_critical": chi-a0,
    }
    for name, val in zip(exact_ns_exponents,
                         (F(5,8),-F(7,16),-F(31,16),-F(1,16))):
        check(exact_ns_exponents[name] == val,
              "fixed_viscosity_exponents", name)
    check(-F(1) < 2*chi-beta < 0, "fixed_viscosity_exponents",
          "full viscous cost is negligible relative to cloud energy")

    x = s.symbols("x0:3", real=True)
    t, mu, mu0 = s.symbols("t mu mu0", real=True)
    w = s.Matrix([s.Function(f"w{i}")(t,*x) for i in range(3)])
    z = s.Matrix([s.Function(f"z{i}")(t,*x) for i in range(3)])
    U = w+z
    lap = lambda f: sum(s.diff(f,y,2) for y in x)
    adv = lambda v,b: s.Matrix([sum(v[j]*s.diff(b[i],x[j])
                                    for j in range(3)) for i in range(3)])
    left = U.diff(t)-mu*U.applyfunc(lap)+adv(U,U) \
           -(w.diff(t)-mu0*w.applyfunc(lap)+adv(w,w))
    right = z.diff(t)-mu*z.applyfunc(lap)+adv(U,z)+adv(z,w) \
            -(mu-mu0)*w.applyfunc(lap)
    for i in range(3):
        eq(left[i],right[i],"full_equation",f"component {i}")
        for j in range(3):
            eq(U[i]*U[j]-w[i]*w[j],w[i]*z[j]+z[i]*w[j]+z[i]*z[j],
               "full_pressure_stress",f"stress {i},{j}")
    p, q = s.symbols("p q", real=True)
    eq(2*p*p+2*q*q-(p-q)**2,(p+q)**2,
       "energy", "full-to-relative dissipation inequality remainder")
    eq((p+q)**2-p*p-q*q,2*p*q,
       "energy", "all core-cloud cross terms retained")

    kappa, norm, source, dt = s.symbols("kappa norm source dt", positive=True)
    # Actual band at physical frequency K*kappa of A*K*U(K*x).
    band_l2 = A*K*K**(-s.Rational(3,2))*norm
    eq(s.sqrt(K*kappa)*band_l2,A*s.sqrt(kappa)*norm,
       "finite_events", "annular critical amplitude")
    src_l2 = (A*K)*(A*K**2)*K**(-s.Rational(3,2))*source
    eq(src_l2/((K*kappa)**s.Rational(5,2)*band_l2**2),
       source/(kappa**s.Rational(5,2)*norm**2),
       "finite_events", "complete quadratic source efficiency")
    eq(dt/(A*K**2)*(A*s.sqrt(kappa)*norm)*(K*kappa)**2,
       dt*s.sqrt(kappa)*norm*kappa**2,
       "finite_events", "actual nonlinear clock")

    region_cases = 0
    for al, be, ch in product((F(1,8),F(1,4),F(3,8)),
                              (F(1,8),F(1,4),F(3,8)),
                              (-F(1,64),-F(1,32),-F(1,16))):
        if 2*al+be-2*ch >= 1:
            continue
        region_cases += 1
        ec = 2*ch-be
        er = 1-2*al+ec
        check(ec < 0 and ch < 0,"open_region","physical cloud vanishes")
        check(er > 0,"open_region","normalized relative energy diverges")
        check(al-1 < 2*al-1 < ec,"open_region","full cost/core smaller than cloud")
        check(ch-al < -al,"open_region","critical cloud below reference error")
        check(be < 1,"open_region","mesoscopic below core frequency")
        check(ch-al+(be-1)/2 < -al,"open_region","derivative bootstrap small")
        check(-al-2 < ec/2,"open_region","fixed smooth time error negligible")
        check((2*al-1-ec)/2 == -er/2,"open_region","cross term relative rate")

    result = {
        "status": "PASS_EXACT_FINITE_IDENTITIES",
        "assertions":sum(counts.values()),
        "groups":dict(counts),
        "rational_open_region_cases":region_cases,
        "scope_exclusions":[
            "No continuum stability or small-data theorem certification",
            "No floating-point PDE search or validated numerical orbit",
            "No positive regenerative cell or infinite shadowing constructed",
            "No independent mathematical audit or NS-R3 resolution",
        ],
    }
    text=json.dumps(result,indent=2)+"\n"
    print(text,end="")
    if output is not None:
        output.parent.mkdir(parents=True,exist_ok=True)
        output.write_text(text)


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json",type=Path)
    main(parser.parse_args().json)
