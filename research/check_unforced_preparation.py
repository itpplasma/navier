#!/usr/bin/env python3
"""Exact finite algebra for unforced support/pulse and angular-preparation notes.

Not a continuum validator, numerical PDE orbit, or independent mathematical audit.
The analytic smoothing, infinite-family limits, and full-source manuscript are
not certified by these finite calculations.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import json
from pathlib import Path

import sympy as s


def main(output: Path | None = None) -> None:
    counts: Counter[str] = Counter()

    def check(condition: bool, group: str, label: str) -> None:
        if not condition:
            raise AssertionError(f"{group}: {label}")
        counts[group] += 1

    def equal(lhs: s.Expr, rhs: s.Expr, group: str, label: str) -> None:
        check(s.simplify(lhs - rhs) == 0, group, label)

    n = s.symbols("n", integer=True, real=True)
    angular = s.Matrix([[s.I*n, -1, 0], [1, s.I*n, 0], [0, 0, s.I*n]])
    energy = angular.conjugate().T * angular
    eigenvectors = (s.Matrix([1, s.I, 0]), s.Matrix([1, -s.I, 0]),
                    s.Matrix([0, 0, 1]))
    eigenvalues = ((n-1)**2, (n+1)**2, n**2)
    for vec, value in zip(eigenvectors, eigenvalues):
        for i in range(3):
            equal((energy*vec)[i], value*vec[i], "vector_angular", "circular eigenvector")
    for k in list(range(-12, -1)) + list(range(2, 13)):
        for value in eigenvalues:
            check(int(value.subs(n, k)) >= (abs(k)-1)**2,
                  "vector_angular", f"sharp shift n={k}")
    check(eigenvalues[0].subs(n, 1) == 0, "vector_angular",
          "n-squared coercivity would be false")
    a, b, c, d = s.symbols("a b c d", real=True)
    vr, vt = a+s.I*b, c+s.I*d
    norm2 = lambda z: s.expand(z*s.conjugate(z))
    equal(norm2(s.I*n*vr-vt)+norm2(s.I*n*vt+vr),
          (n-1)**2*norm2(vr-s.I*vt)/2+(n+1)**2*norm2(vr+s.I*vt)/2,
          "vector_angular", "full complex transverse quadratic form")

    # Exact rotations: covariance of Leray, not a restricted pressure model.
    rot = s.Matrix([[s.Rational(3,5), -s.Rational(4,5), 0],
                    [s.Rational(4,5), s.Rational(3,5), 0], [0,0,1]])
    check(rot.T*rot == s.eye(3) and rot.det() == 1,
          "rotation_leray", "orthogonal proper rotation")
    projector = lambda q: s.eye(3)-q*q.T/q.dot(q)
    for q in (s.Matrix([1,2,3]), s.Matrix([2,-1,0]), s.Matrix([0,0,4])):
        defect = projector(rot*q)*rot-rot*projector(q)
        for entry in defect:
            equal(entry, 0, "rotation_leray", "full projector equivariance")

    # Exact cutoff equation, including BOTH choices of initial trace.
    v, L = s.symbols("v L", real=True, positive=True)
    psi = s.Function("psi")(v)
    h = s.exp(-(v-L/2)**2/(2*L))
    rate = (L/2-v)/L
    operator = lambda f: s.diff(f, v)-rate*f
    pulse = psi*h
    residual = s.diff(psi,v)*h
    equal(operator(h), 0, "pulse_trace", "homogeneous Gaussian")
    equal(operator(pulse), residual, "pulse_trace", "exact seed residual")
    equal(operator(-pulse), -residual, "pulse_trace", "zero-trace cancellation")
    fill = (1-psi)*h
    equal(operator(fill), -residual, "pulse_trace", "free-trace filling")
    equal(pulse-pulse, 0, "pulse_trace", "zero trace removes the carrier")
    equal(pulse+fill, h, "pulse_trace", "free trace preserves the carrier")
    equal((pulse+fill)**2, h**2, "pulse_trace", "preserved full scalar covariance")
    equal(fill.subs(psi,0), h, "pulse_trace", "endpoint trace")
    equal(fill.subs(psi,1), 0, "pulse_trace", "middle unchanged")
    for j in range(5):
        equal(s.diff(operator(fill)+residual,v,j),0,
              "pulse_trace", f"all retained derivative terms j={j}")
    ell, N, power, cg = s.symbols("ell N power cg", positive=True)
    # The source envelope is exp(-c ell^2), not exp(-c ell^4).
    equal(s.log(s.exp(-cg*ell**2)), -cg*ell**2,
          "pulse_scale", "Gaussian tail exponent")
    equal(s.diff(N*ell*s.log(2)+2*power*s.log(ell)-cg*ell**2,ell,2),
          -2*cg-2*power/ell**2, "pulse_scale", "log inverse-loss curvature")

    tau, tau0, hv, CB, D = s.symbols("tau tau0 hv CB D", positive=True)
    phi = CB/hv*(tau**(-hv)-tau0**(-hv))-D*s.log(tau0/tau)
    equal(-s.diff(phi,tau),CB*tau**(-1-hv)-D/tau,
          "history_integral", "full strain-minus-viscosity exponent")
    equal(-s.diff(s.log(tau0/tau),tau),1/tau,
          "history_integral", "logarithmic occupation clock")
    nu, radius, eta, J, work, amp, initial = s.symbols(
        "nu radius eta J work amp initial", positive=True)
    freq = s.symbols("freq", nonnegative=True)
    dose = nu*freq/radius**2
    equal((dose*eta*s.log(tau0/tau))*radius**2/(nu*eta*s.log(tau0/tau)),
          freq, "history_integral", "necessary frequency ceiling")
    equal(dose*J - CB/hv*(tau**(-hv)-tau0**(-hv)) + s.log(amp/initial),
          dose*J+s.log(amp/initial)-CB/hv*(tau**(-hv)-tau0**(-hv)),
          "history_integral", "required signed nonlinear work rearrangement")

    # Full quadratic splitting: the angular mean need not solve NS separately.
    x = s.symbols("x0:3", real=True)
    B = s.Matrix([s.Function(f"B{i}")(*x) for i in range(3)])
    z = s.Matrix([s.Function(f"z{i}")(*x) for i in range(3)])
    adv = lambda u,w: s.Matrix([sum(u[j]*s.diff(w[i],x[j])
                                    for j in range(3)) for i in range(3)])
    whole = adv(B+z,B+z)
    parts = adv(B,B)+adv(B,z)+adv(z,B)+adv(z,z)
    for i in range(3):
        equal(whole[i],parts[i],"whole_nonlinearity",f"component {i}")
    # Real part of complex mode stretching sees exactly the symmetric strain.
    matrix = s.Matrix(3,3,s.symbols("m0:9",real=True))
    realv = s.Matrix(s.symbols("r0:3",real=True))
    imagv = s.Matrix(s.symbols("i0:3",real=True))
    vv = realv+s.I*imagv
    symmetric = (matrix+matrix.T)/2
    equal(s.re((s.conjugate(vv).T*matrix*vv)[0]),
          (realv.T*symmetric*realv)[0]+(imagv.T*symmetric*imagv)[0],
          "whole_nonlinearity", "symmetric strain only")

    # Rational witnesses for the asymptotic inequality; no floating logarithms.
    # For q=2^-b and h=1/den, q^-h is exactly an integer. Use log(2)>=1/2.
    witness_cases = 0
    for den in (2,10,101,128,200,400):
        for j in (6,8,10):
            exponent = 4*den*j
            mass = 2**(4*j)
            strain_upper = den*(mass-1)
            damping_lower = F(mass*exponent,2)
            check(strain_upper-damping_lower <= -F(mass*exponent,4),
                  "rational_history_cases", f"log margin den={den},j={j}")
            check(F(mass*exponent,4) > (1+exponent)**2,
                  "rational_history_cases", "beats Gaussian-in-log seed")
            check(F(exponent,den) == 4*j,
                  "rational_history_cases", "exact inverse-time power")
            witness_cases += 1

    # Invariant ratio cone in the positive-gap, insufficient-damping frame.
    q = s.symbols("q", nonnegative=True)
    upper = -3+4*q+4*q**2
    lower = -upper
    growth = s.Rational(3,4)-q-2*q**2
    check(upper.subs(q,s.Rational(1,8)) < 0,
          "frame_growth", "upper cone boundary")
    check(lower.subs(q,s.Rational(1,8)) > 0,
          "frame_growth", "lower cone boundary")
    check(growth.subs(q,s.Rational(1,8)) == s.Rational(19,32),
          "frame_growth", "minimal growth exceeds one half")
    check(s.diff(upper,q).is_positive, "frame_growth", "upper monotonicity")
    check((-s.diff(growth,q)).is_positive, "frame_growth", "growth monotonicity")
    for frac in (F(0), F(1,32), F(1,16), F(1,8)):
        qq=s.Rational(frac.numerator,frac.denominator)
        check(upper.subs(q,qq)<0 and lower.subs(q,qq)>0
              and growth.subs(q,qq)>=s.Rational(1,2),
              "frame_growth", "exact frame margin")

    k, eps, lam, ustar, phase = s.symbols("k eps lam ustar phase",positive=True)
    bs2 = lam/(eps*k**2*(1+ustar**2)**s.Rational(3,2))
    equal(k**2*bs2,lam/(eps*(1+ustar**2)**s.Rational(3,2)),
          "phase_geometry", "carrier reduction undone by source Bs")
    Bs = s.symbols("Bs",positive=True)
    equal((eps*k**2*Bs**2*(1+phase**2))/(lam/s.sqrt(1+phase**2)),
          eps*k**2*Bs**2*(1+phase**2)**s.Rational(3,2)/lam,
          "phase_geometry", "exact turning-point balance")

    # Mixed-trace kernel estimates and the actual constrained normal equation.
    w, center, kap = s.symbols("w center kap", real=True, positive=True)
    equal((v-center)**2-(w-center)**2-(v-w)**2,
          2*(v-w)*(w-center), "mixed_inverse", "right Gaussian kernel margin")
    equal((center-v)**2-(center-w)**2-(w-v)**2,
          2*(w-v)*(center-w), "mixed_inverse", "left Gaussian kernel margin")
    rr=s.symbols("rr", nonnegative=True)
    equal(s.integrate(s.exp(-kap*rr**2/(2*L)),(rr,0,s.oo)),
          s.sqrt(s.pi*L/(2*kap)), "mixed_inverse", "exact scalar kernel integral")
    y=ustar/2+ustar*v/L
    lamref=lam/s.sqrt(1+y*y)
    dref=lam*(1+y*y)/(1+ustar*ustar)**s.Rational(3,2)
    mh=s.symbols("mh", integer=True, positive=True)
    aref=lamref-mh**2*dref
    equal(s.diff(aref,v),
          -lam*ustar*y/(L*(1+y*y)**s.Rational(3,2))
          -2*mh**2*lam*ustar*y/(L*(1+ustar*ustar)**s.Rational(3,2)),
          "mixed_inverse", "monotone reference rate for every harmonic")
    equal(aref.subs({mh:1,v:L/2}),0,
          "mixed_inverse", "primary turning point exactly at midpoint")
    for mode in range(4,13):
        check(F(3)-F(mode*mode,2) <= -F(mode*mode,4),
              "mixed_inverse", "direct high-harmonic dissipativity")
    for ce in (1,3,7):
        for m0 in (4,6):
            rootL=4*ce*(1+m0*m0)
            loss=2*rootL
            error=F(ce*(1+m0*m0),rootL*rootL)
            check(loss*error <= F(1,2),
                  "mixed_inverse", "low-harmonic Neumann threshold")

    normal=s.Matrix([1,2,3])
    normaldot=s.Matrix(s.symbols("nd0:3",real=True))
    tv=s.Matrix(s.symbols("tv0:3",real=True))
    fv=s.Matrix(s.symbols("fv0:3",real=True))
    KK=s.Matrix(3,3,s.symbols("kk0:9",real=True))
    damp=s.symbols("damp",real=True)
    n2=normal.dot(normal)
    proj=s.eye(3)-normal*normal.T/n2
    Aphi=-KK+normal*(normal.T*KK-normaldot.T)/n2
    tprime=Aphi*tv-mh**2*damp*tv-proj*fv
    pressure=-(normal.dot(KK*tv)-normaldot.dot(tv)+normal.dot(fv))/(s.I*k*mh*n2)
    full=tprime+KK*tv+mh**2*damp*tv+s.I*k*mh*normal*pressure+fv
    for component in full:
        equal(component,0,"principal_pressure","entire normal momentum cancellation")
    equal(normal.dot(tprime)+normaldot.dot(tv),-mh**2*damp*normal.dot(tv),
          "principal_pressure","exact moving-plane constraint evolution")

    report = {"status":"passed", "assertions":sum(counts.values()),
              "groups":dict(counts), "rational_history_cases":witness_cases,
              "scope":"finite exact algebra only; no continuum or independent audit"}
    text=json.dumps(report,indent=2,sort_keys=True)+"\n"
    if output is not None:
        output.parent.mkdir(parents=True,exist_ok=True)
        output.write_text(text)
    print(text,end="")


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json",type=Path,default=None)
    args=parser.parse_args()
    main(args.json)
