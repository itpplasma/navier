#!/usr/bin/env python3
"""Uncertified discovery: periodic spherical NS Galerkin with full retained feedback.

This is NOT a continuum solution, interval computation, R3 packet proof,
turnover theorem, or terminal estimate. Requires numpy and scipy. The grid
L>3N prevents quadratic aliasing INTO retained modes; a genuine Galerkin
cutoff still discards modes above N. No phase or polarization is imposed
on the evolving solution. Outputs are diagnostic floating-point values.
"""
from __future__ import annotations
import argparse
import json
from itertools import permutations
from pathlib import Path
from time import perf_counter
import numpy as np
from scipy.fft import fftn, ifftn, next_fast_len


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--N', type=int, default=10)
    parser.add_argument('--nu', type=float, default=.01)
    parser.add_argument('--dt', type=float, default=.00625)
    parser.add_argument('--T', type=float, default=.25)
    parser.add_argument('--json', type=Path)
    args = parser.parse_args()
    if args.N < 3 or args.nu < 0 or args.dt <= 0 or args.T <= 0:
        parser.error('Require N>=3, nu>=0, dt>0, T>0.')
    steps = round(args.T/args.dt)
    if steps < 1 or abs(steps*args.dt-args.T) > 1e-10*args.T:
        parser.error('T must be a positive integer multiple of dt.')
    n, nu, dt = args.N, args.nu, args.dt
    length = next_fast_len(3*n+1)
    k = np.stack(np.meshgrid(*(np.fft.fftfreq(length)*length,)*3, indexing='ij'), axis=0)
    k = np.rint(k).astype(int)
    k2 = (k*k).sum(axis=0)
    inv_k2 = 1/np.maximum(k2, 1)
    mask = (k2 > 0) & (k2 <= n*n)
    axes = (1, 2, 3)
    velocity = np.zeros((3, length, length, length), complex)
    parent = np.zeros((length,)*3, bool)
    target = np.zeros_like(parent)
    side = np.zeros_like(parent)
    for modes, selection in [([((2, 1, 0))], parent),
                              ([(3, 3, 0), (4, 1, 1)], target),
                              ([(3, 2, 1)], side)]:
        for representative in modes:
            for wave in set(permutations(representative)):
                for sign in (-1, 1):
                    index = tuple((sign*x) % length for x in wave)
                    selection[index] = True
                    if selection is parent:
                        a = np.ones(3)-np.array(wave)*sum(wave)/sum(x*x for x in wave)
                        velocity[(slice(None),)+index] = -sign*1j*a
    initial_energy = float((abs(velocity)**2).sum())
    transverse_k2 = k2-k.sum(axis=0)**2/3

    def rhs(h):
        u = ifftn(h, axes=axes).real*length**3
        omega_h = 1j*np.cross(k, h, axisa=0, axisb=0, axisc=0)
        omega = ifftn(omega_h, axes=axes).real*length**3
        q = fftn(np.cross(u, omega, axisa=0, axisb=0, axisc=0), axes=axes)/length**3
        q -= k*(k*q).sum(axis=0)*inv_k2
        return (q-nu*k2*h)*mask

    def dissipation(h):
        return float(2*nu*(k2*(abs(h)**2).sum(axis=0)).sum())

    def observe(t, h, spent):
        e = (abs(h)**2).sum(axis=0)
        outside = float(e[~parent].sum())
        return {'time': t, 'energy': float(e.sum()),
                'critical_squared_over_two': float((np.sqrt(k2)*e).sum()/2),
                'outside_parent_fraction': outside/initial_energy,
                'intended_fraction': float(e[target].sum())/initial_energy,
                'side_fraction': float(e[side].sum())/initial_energy,
                'boundary_075N_fraction': float(e[k2 > (.75*n)**2].sum())/initial_energy,
                'outside_parent_mean_transverse_k2':
                    float((transverse_k2*e)[~parent].sum())/outside if outside else None,
                'max_real_fourier_component': float(abs(h.real).max()),
                'viscous_energy_balance_error': float(e.sum())+spent-initial_energy}

    spent = 0.
    rows = [observe(0., velocity, spent)]
    start = perf_counter()
    stride = max(1, round(.05/dt))
    for j in range(steps):
        h = velocity
        r1 = rhs(h)
        h2 = h+dt*r1/2
        r2 = rhs(h2)
        h3 = h+dt*r2/2
        r3 = rhs(h3)
        h4 = h+dt*r3
        r4 = rhs(h4)
        spent += dt*(dissipation(h)+2*dissipation(h2)+2*dissipation(h3)+dissipation(h4))/6
        velocity = h+(dt/6)*(r1+2*r2+2*r3+r4)
        if (j+1) % stride == 0 or j+1 == steps:
            row = observe((j+1)*dt, velocity, spent)
            rows.append(row)
            print(json.dumps(row, sort_keys=True), flush=True)
    result = {'scope': __doc__, 'N': n, 'grid': length, 'nu': nu, 'dt': dt,
              'T': args.T, 'rows': rows, 'seconds': perf_counter()-start}
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(result, indent=2)+'\n')
    print('NOT CERTIFIED: Galerkin and floating-point errors remain.', flush=True)


if __name__ == '__main__':
    main()
