#!/usr/bin/env python3
"""Small deterministic Fourier snapshot for the signed cubic pressure test.

This is a diagnostic calculation on (R/2pi Z)^3.  It is deliberately not a
time integration or a validated proof.
"""
from __future__ import annotations

import argparse
import numpy as np
from scipy import fft

MODES = ((1, 0, 1), (0, 1, 1), (1, 1, 0), (1, 1, 1), (2, 1, 1))


def coefficients(seed: int):
    rng = np.random.default_rng(seed)
    return [(k, rng.normal(size=3), rng.normal(size=3)) for k in MODES]


def velocity(n: int, modes, scale: float = 1.0):
    x = 2 * np.pi * np.arange(n) / n
    X = np.meshgrid(x, x, x, indexing="ij")
    xyz = np.stack(X)
    u = np.zeros((3, n, n, n))
    for k, a, b in modes:
        theta = np.einsum("i,ixyz->xyz", k, xyz)
        # A=a cos(k.x)+b sin(k.x), and the implemented field is u=-curl A.
        u += np.cross(a, k)[:, None, None, None] * (-np.sin(theta))
        u += np.cross(b, k)[:, None, None, None] * np.cos(theta)
    return scale * u


def snapshot(u):
    n = u.shape[1]
    uh = fft.fftn(u, axes=(1, 2, 3))
    one = fft.fftfreq(n) * n
    K = np.meshgrid(one, one, one, indexing="ij")
    K2 = sum(k * k for k in K)
    denom = np.where(K2 == 0, 1.0, K2)
    ph = np.zeros((n, n, n), dtype=complex)
    for i in range(3):
        for j in range(3):
            ph += (-K[i] * K[j] / denom) * fft.fftn(u[i] * u[j])
    ph[0, 0, 0] = 0.0
    p = fft.ifftn(ph).real
    speed = np.sqrt(np.sum(u * u, axis=0))
    # epsilon is only a pointwise guard at |u|=0; report its use explicitly.
    grad_speed = np.empty((3, n, n, n))
    for j in range(3):
        directional = np.zeros_like(speed)
        for i in range(3):
            directional += u[i] * fft.ifftn(1j * K[j] * uh[i]).real
        grad_speed[j] = directional / np.maximum(speed, 1e-14)
    grad_p = np.array([fft.ifftn(1j * K[j] * ph).real for j in range(3)])
    cell = (2 * np.pi / n) ** 3
    P3 = cell * np.sum(p * np.einsum("ixyz,ixyz->xyz", u, grad_speed))
    independent = -cell * np.sum(speed * np.einsum("ixyz,ixyz->xyz", u, grad_p))
    div_hat = sum(K[i] * uh[i] for i in range(3))
    div_residual = np.max(np.abs(div_hat)) / np.max(np.abs(uh))
    return P3, independent, div_residual, np.sqrt(cell * np.sum(u * u))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--grid", type=int, nargs="+", default=[32, 64, 128])
    args = ap.parse_args()
    raw = velocity(args.grid[0], coefficients(args.seed))
    rms = np.sqrt(np.mean(raw * raw))
    modes = coefficients(args.seed)
    print(f"seed={args.seed} modes={MODES} normalization=divide by componentwise RMS {rms:.16g}")
    for n in args.grid:
        result = snapshot(velocity(n, modes) / rms)
        print(f"N={n} P3={result[0]:.16g} independent={result[1]:.16g} "
              f"div_hat_rel={result[2]:.3e} L2={result[3]:.16g}")
    n = args.grid[-1]
    plus = snapshot(velocity(n, modes) / rms)[0]
    minus = snapshot(-velocity(n, modes) / rms)[0]
    print(f"sign-flip check N={n}: P3(u)={plus:.16g} P3(-u)={minus:.16g}")


if __name__ == "__main__":
    main()
