#!/usr/bin/env python3
"""Exact finite algebra for smooth pulse inversion and normalized-work failure.

This is not a PDE solver, a continuum proof validator, or an independent audit.
Run from the full research checkout; use --json to retain assertion counts.
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

    def equal(left: s.Expr, right: s.Expr, group: str, label: str) -> None:
        check(s.simplify(s.expand(left-right)) == 0, group, label)

    v, theta = s.symbols("v theta", real=True)
    L, kappa = s.symbols("L kappa", positive=True)
    a = s.Function("a")(v)
    y = s.Function("y")(v)
    h = s.Function("h")(v)
    D = lambda f: s.diff(f,v)-a*f
    Dadj = lambda f: -s.diff(f,v)-a*f
    equal(D(Dadj(y)), -s.diff(y,v,2)+(a*a-s.diff(a,v))*y,
          "factorization", "exact D D-adjoint sign")
    equal(Dadj(y)**2-(s.diff(y,v)**2+(a*a-s.diff(a,v))*y*y),
          s.diff(a*y*y,v), "factorization", "Dirichlet form boundary term")
    equal(Dadj(y)*h+s.diff(y*h,v), y*(s.diff(h,v)-a*h),
          "factorization", "orthogonality boundary identity")
    equal(s.diff(y,v)**2+(a*a+kappa/L)*y*y-kappa/L*y*y,
          s.diff(y,v)**2+a*a*y*y, "factorization", "coercive remainder")
    ap = s.Function("a")(theta,v)
    yp = s.Function("y")(theta,v)
    potential = ap*ap-s.diff(ap,v)
    Hp = lambda f: -s.diff(f,v,2)+potential*f
    for order in (1,2,3):
        rhs = Hp(s.diff(yp,theta,order))
        for j in range(1,order+1):
            rhs += s.binomial(order,j)*s.diff(potential,theta,j)*s.diff(yp,theta,order-j)
        equal(s.diff(Hp(yp),theta,order),rhs,
              "parameter", f"fixed-domain derivative {order}")
    # Pull the clamped-root integral back to [0,1] before differentiating.
    r = s.symbols("r", real=True)
    integrand = -L*theta*s.exp(L*theta**2*(-r+r*r/2))
    equal(s.diff(integrand,theta).subs(theta,0), -L,
          "parameter", "right derivative at clamped root")
    equal(s.diff(s.Integer(0),theta),0,
          "parameter", "left derivative at clamped root")

    lam0, us = s.symbols("lambda0 ustar", positive=True)
    m = s.symbols("m", integer=True, nonzero=True)
    yy = us/2+us*v/L
    lam = lam0/s.sqrt(1+yy*yy)
    dref = lam0*(1+yy*yy)/(1+us*us)**s.Rational(3,2)
    am = lam-m*m*dref
    derivative = -lam0*us*yy/(L*(1+yy*yy)**s.Rational(3,2)) \
                 -2*m*m*lam0*us*yy/(L*(1+us*us)**s.Rational(3,2))
    equal(s.diff(am,v),derivative,"harmonics","all-harmonic growth derivative")
    equal(am.subs({m:1,v:L/2}),0,"harmonics","primary midpoint root")
    d0, lm, mm = s.symbols("d0 lambda_max m2", positive=True)
    equal(lm+1-mm*d0/2-(-mm*d0/4),lm+1-mm*d0/4,
          "harmonics","high-harmonic dissipative remainder")
    equal((m*m)*(1/(m*m)),1,"harmonics","parameter derivative damping cancellation")
    for jj in (1,2,3):
        for uu in (F(1,2),F(1),F(2)):
            value = derivative.subs({lam0:1,us:s.Rational(uu.numerator,uu.denominator),
                                    m:jj,L:10,v:5})
            check(bool(value<0),"harmonics","rational regular-patch slope")

    pulse = s.exp(-L*s.cos(2*s.pi*v/L)**2)
    growth = 2*s.pi*s.sin(4*s.pi*v/L)
    equal(s.diff(pulse,v)/pulse,growth,"history","connected two-pulse growth")
    equal(pulse.subs(v,L/4),1,"history","first peak")
    equal(pulse.subs(v,3*L/4),1,"history","second peak")
    equal(s.diff(growth,v).subs(v,L/4),-8*s.pi**2/L,
          "history","negative slope at first peak")
    equal(s.diff(growth,v).subs(v,L/2),8*s.pi**2/L,
          "history","positive slope between peaks")
    chi = s.Function("chi")(v)
    equal(s.diff(chi*pulse,v)-growth*chi*pulse,s.diff(chi,v)*pulse,
          "history","entire cutoff residual")
    z = s.Function("z")(v)
    equal(s.diff(z/h,v),(s.diff(z,v)*h-z*s.diff(h,v))/h**2,
          "history","common-history compatibility quotient")
    for rr in (s.Rational(3,8),s.Rational(1,2),s.Rational(5,8)):
        check(bool(s.cos(2*s.pi*rr)**2>=s.Rational(1,2)),
              "history","flat transition carrier sample")
    c0, c1 = s.symbols("c0 c1", real=True)
    equal((1+c0)-c0,1,"history","unavoidable peak difference")
    equal((1+c0)**2+c0**2,2*(c0+s.Rational(1,2))**2+s.Rational(1,2),
          "history","real free-trace lower bound")
    # Sufficient exact thresholds for exponential flatness; logs are bounded
    # in the proof by log(2)<=1 and log(ell)<=ell, for ell>=1.
    for M in (0,1,3,10):
        for N in (1,2,5):
            ell = F(4*(M+N+1))
            check(-ell*ell/2+(M+N)*ell <= -ell*ell/4,
                  "flatness","quadratic exponent dominates fixed losses")

    x = s.symbols("x0:3", real=True)
    X,Y,Z=x
    gaussian = s.exp(-sum(q*q for q in x))
    psi=X*gaussian
    datum=s.Matrix([s.diff(psi,Y),-s.diff(psi,X),0])
    div=lambda f: sum(s.diff(f[i],x[i]) for i in range(3))
    grad=lambda f: s.Matrix([s.diff(f,q) for q in x])
    lap=lambda f: sum(s.diff(f,q,2) for q in x)
    curl=lambda f: s.Matrix([s.diff(f[2],Y)-s.diff(f[1],Z),
                            s.diff(f[0],Z)-s.diff(f[2],X),
                            s.diff(f[1],X)-s.diff(f[0],Y)])
    adv=lambda f,g: s.Matrix([sum(f[j]*s.diff(g[i],x[j]) for j in range(3))
                              for i in range(3)])
    equal(div(datum),0,"gaussian","Schwartz parent is solenoidal")
    conv=adv(datum,datum)
    target=s.Matrix([-4*X**3+2*X,-4*X*X*Y-2*Y,0])*gaussian**2
    for i in range(3):
        equal(conv[i],target[i],"gaussian",f"complete convection component {i}")
    equal(curl(conv)[2],8*X*Y*gaussian**2,
          "gaussian","nonzero angular daughter survives pressure curl")
    radius,angle=s.symbols("radius angle",real=True)
    polar={X:radius*s.cos(angle),Y:radius*s.sin(angle)}
    # Factor out the common radial Gaussian before mode identification.
    dr=(datum[0]*s.cos(angle)+datum[1]*s.sin(angle))/gaussian
    dt=(-datum[0]*s.sin(angle)+datum[1]*s.cos(angle))/gaussian
    equal(s.trigsimp(dr.subs(polar)),-s.sin(angle),"rotation","parent radial mode")
    equal(s.trigsimp(dt.subs(polar)),(2*radius**2-1)*s.cos(angle),
          "rotation","parent azimuthal mode")
    equal(8*radius**2*s.cos(angle)*s.sin(angle),4*radius**2*s.sin(2*angle),
          "rotation","axial daughter mode two")
    equal(s.integrate(s.sin(2*angle)*s.exp(-2*s.I*angle),(angle,0,2*s.pi))/(2*s.pi),
          1/(2*s.I),"rotation","exact complex daughter coefficient")
    cc=s.Matrix([s.Function(f"c{i}")(*x) for i in range(3)])
    for i in range(3):
        equal(curl(curl(cc))[i],grad(div(cc))[i]-lap(cc[i]),
              "seed","curl-curl equals gradient-divergence minus Laplacian")
    equal(div(curl(curl(cc))),0,"seed","seed divergence")
    for i in range(3):
        equal(-cc[i]*lap(cc[i]),sum(s.diff(cc[i],q)**2 for q in x)
              -div(cc[i]*grad(cc[i])),"seed","positive pairing after integration")

    time=s.symbols("t",positive=True)
    w=s.Matrix([s.Function(f"w{i}")(time,*x) for i in range(3)])
    B=s.Matrix([s.Function(f"B{i}")(time,*x) for i in range(3)])
    pp=s.Function("p")(time,*x)
    equal(w.dot(w.diff(time)),s.diff(w.dot(w),time)/2,"energy","time term")
    equal(w.dot(grad(pp)),div(pp*w)-pp*div(w),"energy","canonical pressure pairing")
    equal(w.dot(adv(B,w)),div(B*w.dot(w)/2)-div(B)*w.dot(w)/2,
          "energy","full background transport")
    JB=B.jacobian(x)
    equal(w.dot(adv(w,B)),(w.T*((JB+JB.T)/2)*w)[0],
          "energy","only symmetric strain contributes")
    E=s.Function("E")(time)
    equal(s.diff(s.log(s.sqrt(E)),time),s.diff(E,time)/(2*E),
          "birth","exact logarithmic mode energy derivative")
    magnitude=s.symbols("magnitude",positive=True)
    for order in (1,2,3,4):
        amplitude=time**order*magnitude
        equal(s.diff(amplitude,time)*amplitude/amplitude**2,order/time,
              "birth","normalized source singularity")
    delta,tstar=s.symbols("delta tstar",positive=True)
    equal(s.integrate(1/(delta+time),(time,0,tstar)),
          s.log(delta+tstar)-s.log(delta),"birth","seeded logarithmic divergence")
    eps,energy0,enstrophy0=s.symbols("epsilon energy0 enstrophy0",positive=True)
    equal(((eps**2*energy0)*(eps**2*enstrophy0))**s.Rational(1,4),
          eps*(energy0*enstrophy0)**s.Rational(1,4),
          "smallness","small-data energy-enstrophy bootstrap scaling")
    check(F(1,3)==F(1,2)/2+F(1,2)/6,"smallness","L3 interpolation")
    check(F(1,3)+F(1,6)+F(1,2)==1,"smallness","enstrophy Holder exponents")

    report={"scope":"finite exact algebra only; not continuum or independent validation",
            "groups":dict(sorted(counts.items())),"assertions":sum(counts.values())}
    print(json.dumps(report,indent=2,sort_keys=True))
    if output is not None:
        output.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json",type=Path)
    main(parser.parse_args().json)
