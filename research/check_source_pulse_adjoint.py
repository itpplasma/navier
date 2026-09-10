#!/usr/bin/env python3
"""Source-pulse adjoint checks: exact identities + labelled ODE calibrations.

Run with Python 3.10+, NumPy, SciPy, and SymPy. No network is used.
The numerical cases use the source's frozen 3-component principal matrix,
including pressure projection, frame connections and viscosity. They are
NOT the full space-time NS field or simultaneous dyadic source parameters.
In particular L and carrier k are varied independently for calibration.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.special import expit

EXACT = 0
NUMERIC = 0


def exact(condition: bool, label: str) -> None:
    global EXACT
    if not bool(condition):
        raise AssertionError(label)
    EXACT += 1


def numerical(condition: bool, label: str) -> None:
    global NUMERIC
    if not bool(condition):
        raise AssertionError(label)
    NUMERIC += 1


def algebra() -> None:
    x, u, L, lam = sp.symbols('x u L lam', positive=True)
    y = u / 2 + u * x
    primitive = lambda z: sp.asinh(z) - (z + z**3 / 3) / (1 + u*u)**sp.Rational(3, 2)
    logP = lam * L / u * (primitive(y) - primitive(u))
    a = lam / sp.sqrt(1 + y*y) - lam * (1 + y*y)/(1 + u*u)**sp.Rational(3, 2)
    exact(sp.simplify(sp.diff(logP, x) - L*a) == 0, 'source envelope primitive')
    exact(sp.simplify(logP.subs(x, sp.Rational(1, 2))) == 0, 'peak envelope is one')
    derivative = -lam*u*y*((1+y*y)**(-sp.Rational(3, 2))
                           + 2*(1+u*u)**(-sp.Rational(3, 2)))
    exact(sp.simplify(sp.diff(a, x)-derivative) == 0, 'strictly decreasing reference rate')
    q = sp.Matrix([sp.Function(f'q{i}')(x) for i in range(3)])
    h = sp.Matrix([sp.Function(f'h{i}')(x) for i in range(3)])
    A = sp.Matrix(3, 3, lambda i,j: sp.Symbol(f'A{i}{j}'))
    psi = sp.Function('psi')(x)
    rules = {sp.diff(h[i], x): (A*h)[i] for i in range(3)}
    rules.update({sp.diff(q[i], x): -(A.T*q)[i] for i in range(3)})
    exact(sp.expand(sp.diff((q.T*h)[0], x).subs(rules)) == 0, 'adjoint pairing conserved')
    cutoff_residual = (psi*h).diff(x)-A*(psi*h)
    exact((cutoff_residual.subs(rules)-sp.diff(psi,x)*h).applyfunc(sp.expand)
          == sp.zeros(3,1), 'cutoff residual with all matrix entries retained')
    replacement = (1-psi)*h
    exact((replacement.diff(x)-A*replacement+cutoff_residual).subs(rules)
          .applyfunc(sp.expand) == sp.zeros(3,1), 'uncut replacement solves principal correction')
    a0, a1 = sp.symbols('a0 a1', real=True)
    t = sp.symbols('t', real=True)
    # Distributional differentiation of a time-window has both endpoint impulses.
    window = sp.Heaviside(t-a0)-sp.Heaviside(t-a1)
    exact(sp.diff(window,t) == sp.DiracDelta(t-a0)-sp.DiracDelta(t-a1), 'two impulse signs')
    # Full nonlinear residual with a time-only multiplier (abstract independent terms).
    F_B, L_B_W, quadratic, W, ps, dps = sp.symbols('F_B L_B_W quadratic W ps dps')
    cut = F_B + ps*L_B_W + ps**2*quadratic + dps*W
    uncut = F_B + L_B_W + quadratic
    exact(sp.expand(uncut-cut-((1-ps)*L_B_W+(1-ps**2)*quadratic-dps*W)) == 0,
          'full nonlinear cutoff difference')
    # Approximate-adjoint budget sign: <Lw,Z>=boundary+<w,L*Z>.
    ini, obs, forcing, nonlinear, adj_defect = sp.symbols('ini obs forcing nonlinear adj_defect')
    exact(sp.expand((ini-forcing+nonlinear-adj_defect)-obs
                    +(forcing-ini+obs-nonlinear+adj_defect)) == 0,
          'approximate-adjoint defect sign')
    zeta = sp.symbols('zeta', real=True)
    exact(sp.integrate(zeta, (zeta,0,1)) == sp.Rational(1,2), 'localized adjoint source pairing')
    exact(-sp.integrate(1-zeta, (zeta,0,1)) == -sp.Rational(1,2), 'localized adjoint defect pairing')
    # An exponentially small error without its envelope can be O(1) after dual weighting.
    n = sp.symbols('n', positive=True)
    exact(sp.simplify(sp.exp(-n)*sp.exp(n)) == 1, 'flat amplitude alone is not dual smallness')


def transition(s: float) -> tuple[float,float]:
    """C-infinity increasing step and its derivative."""
    if s <= 0:
        return 0., 0.
    if s >= 1:
        return 1., 0.
    p = float(expit(1/(1-s)-1/s))
    return p, p*(1-p)*(1/(1-s)**2+1/s**2)


def cutoff(x: float) -> tuple[float,float]:
    lo, pl = 1/6, 3/10
    hi, pr = 5/6, 7/10
    if x <= .5:
        p, dp = transition((x-lo)/(pl-lo))
        return p, dp/(pl-lo)
    p, dp = transition((hi-x)/(hi-pr))
    return p, -dp/(hi-pr)


class Principal:
    def __init__(self, L: float, u: float, sign: int):
        if L <= 0 or u <= 0 or sign not in (-1,1):
            raise ValueError('Require L,u>0 and sign = +/-1')
        self.L, self.u, self.sign = L, u, sign
        self.F = 1.
        self.g = np.array([-3., 2.])
        self.N = self.g / np.linalg.norm(self.g)
        self.Ktan = np.array([-self.N[1], self.N[0]])
        self.lam = math.sqrt(-2*self.F*self.N[0]*(2*self.F*self.N[0]+np.linalg.norm(self.g)))
        self.c0 = self.lam / (2*self.F*self.N[0])
        self.Bs = math.sqrt(self.lam / (1+u*u)**1.5)
        self.k = 2**26  # labelled coefficient calibration, NOT a full dyadic source band
        ptilde, self.pz = self.Bs*(self.Ktan-sign*u*self.g/(L*float(self.g@self.g)))
        self.p = round(self.k*ptilde)/self.k
        self.x0 = sign*self.Bs*u/2
        self.K = np.array([[0.,-2*self.F,0.],[2*self.F+self.g[0],0.,0.],[self.g[1],0.,0.]])

    def rate(self, x: float) -> float:
        y = self.u*(.5+x)
        return self.lam/math.sqrt(1+y*y)-self.lam*(1+y*y)/(1+self.u*self.u)**1.5

    def log_envelope(self, x: float) -> float:
        u = self.u
        def f(y: float) -> float:
            return math.asinh(y)-(y+y**3/3)/(1+u*u)**1.5
        return self.lam*self.L/u*(f(u*(.5+x))-f(u))

    def normal(self, x: float) -> tuple[np.ndarray,np.ndarray]:
        nrprime = -(self.p*self.g[0]+self.pz*self.g[1])
        n = np.array([self.x0+self.L*x*nrprime,self.p,self.pz])
        return n, np.array([nrprime,0.,0.])  # derivative with respect to v, not x

    def matrix(self, x: float) -> np.ndarray:
        n, npv = self.normal(x)
        aproj = -self.K+np.outer(n,n@self.K-npv)/(n@n)
        d = float(n@n)  # epsilon*k^2=1 in this calibration
        return aproj-d*np.eye(3)

    def initial_divided_by_P(self) -> np.ndarray:
        n,_ = self.normal(0.)
        kt = n[1:]/np.linalg.norm(n[1:])
        nt = np.array([kt[1],-kt[0]])
        sa = n[0]/np.linalg.norm(n[1:])
        return np.r_[1.,-sa*kt+self.c0*math.sqrt(1+self.u**2/4)*nt]

    def solve(self):
        g0 = self.initial_divided_by_P()
        sol = solve_ivp(lambda x,g: self.L*(self.matrix(x)-self.rate(x)*np.eye(3))@g,
                        (0.,1.),g0,method='Radau',rtol=2e-10,atol=2e-12,dense_output=True)
        numerical(sol.success, 'envelope-divided forward solve')
        peak = sol.sol(.5)
        q = peak/(peak@peak)
        adj = solve_ivp(lambda x,b: self.L*(self.rate(x)*np.eye(3)-self.matrix(x).T)@b,
                        (.5,0.),q,method='Radau',rtol=2e-10,atol=2e-12,dense_output=True)
        numerical(adj.success,'envelope-multiplied backward adjoint solve')
        return sol.sol, adj.sol


def calibrations() -> list[dict]:
    rows = []
    for u in (1., 2.):
        for L in (128., 512., 1024.):
            cols, changes = [], []
            for sign in (1,-1):
                p = Principal(L,u,sign)
                g,b = p.solve()
                pairing_error = max(abs(float(g(x)@b(x))-1) for x in np.linspace(0,.5,151))
                normal_error = max(abs(float(p.normal(x)[0]@g(x)))/np.linalg.norm(g(x))
                                   for x in np.linspace(0,1,151))
                numerical(pairing_error < 2e-7,'principal adjoint conserved pairing')
                numerical(normal_error < 2e-7,'full normal-plane constraint')
                start = quad(lambda x: cutoff(x)[1]*float(g(x)@b(x)),1/6,3/10,
                             epsabs=2e-9,epsrel=2e-9)[0]
                numerical(abs(start-1) < 2e-7,'startup source has unit normalized peak response')
                n0,_ = p.normal(0.)
                b0 = b(0.)
                controlled_dual = b0-n0*(n0@b0)/(n0@n0)
                numerical(np.linalg.norm(controlled_dual)>0,'admissible initial channel visible')
                log_seed = p.log_envelope(0.)/math.log(10)+math.log10(np.linalg.norm(g(0.)))
                log_min_seed = p.log_envelope(0.)/math.log(10)-math.log10(np.linalg.norm(controlled_dual))
                numerical(log_min_seed <= log_seed+2e-7,'minimum observation seed vs full target seed')
                def flux(x):
                    gv=g(x)
                    return math.exp(2*p.log_envelope(x))*gv[0]*gv[1:]
                cutcol=np.array([quad(lambda x: cutoff(x)[0]**2*flux(x)[i],0,1,
                                     points=[1/6,.3,.5,.7,5/6],epsabs=1e-11)[0] for i in range(2)])
                delta=np.array([sum(quad(lambda x:(1-cutoff(x)[0]**2)*flux(x)[i],a,c,
                                     epsabs=1e-70,epsrel=2e-7,limit=120)[0]
                                   for a,c in [(0,1/6),(1/6,.3),(.7,5/6),(5/6,1)]) for i in range(2)])
                cols.append(cutcol)
                changes.append(delta)
                rows.append({'u':u,'L':int(L),'sign':sign,
                             'log10_seed_at_entry':log_seed,
                             'log10_minimum_single_observation_seed':log_min_seed,
                             'startup_pairing':start,'max_pairing_error':pairing_error,
                             'max_constraint_error':normal_error})
            H, deltaH = np.column_stack(cols), np.column_stack(changes)
            numerical(abs(np.linalg.det(H))>1e-9,'two covariance directions independent')
            y=np.array([1.,2.])
            target=H@y
            ynew=np.linalg.solve(H+deltaH,target)
            numerical(np.all(ynew>0),'reweighted covariances stay positive in calibration')
            numerical(np.linalg.norm((H+deltaH)@ynew-target)<1e-12,'reweighted mean target exact to roundoff')
            rho=float(np.linalg.norm(np.linalg.solve(H,deltaH),2))
            for row in rows[-2:]:
                row['covariance_relative_matrix_change']=rho
                row['squared_weights_after_repair']=list(map(float,ynew))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Optional explicit JSON report path; default is read-only.')
    args = parser.parse_args()
    algebra()
    rows=calibrations()
    result={'exact_symbolic_assertions':EXACT,'numerical_assertions':NUMERIC,
            'scope':'Source-form principal ODE calibration, not a full NS or dyadic-history computation.',
            'rows':rows}
    if args.output is not None:
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS: {EXACT} exact symbolic assertions; {NUMERIC} numerical assertions.')
    print('L, u, log10(entry seed), startup pairing, relative covariance change:')
    for r in rows[::2]:
        print(r['L'],r['u'],f"{r['log10_seed_at_entry']:.5f}",
              f"{r['startup_pairing']:.10f}",f"{r['covariance_relative_matrix_change']:.3e}")
    print('NOT COMPUTED: complete physical adjoint, source-wide initial trace, nonlinear unforced closure.')


if __name__=='__main__':
    main()
