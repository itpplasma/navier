#!/usr/bin/env python3
"""Exact clock separation between a Beltrami Raman kick and slow-sideband diffusion.

If R=Lambda/b is the high/clean scale and J is the exported slow-sideband scale,
the Beltrami Raman symbol requires J/R->0.  The freely decaying high background
lives on dimensionless time O(R^-2), while an exported J-scale slow sideband
diffuses on O(J^-2).  Hence the slow-sideband viscous exponent accumulated
during one high pulse is O((J/R)^2)->0.

This is a scoped obstruction to lifting the continuous S_J-D_J Schur model by
one freely heat-decaying high sphere.  It points to kick-then-wait splitting.
"""
from __future__ import annotations
import sympy as sp

sigma=sp.symbols('sigma',positive=True)
a,b=sp.symbols('a b',positive=True)
# Example compatible powers: J=sigma^2, R=sigma^6.
J=sigma**2; R=sigma**6
assert sp.simplify(J/R)==sigma**-4
assert sp.simplify((J/R)**2)==sigma**-8
# High clock / sideband diffusion clock = (J/R)^2.
t_high=R**-2
t_side=J**-2
assert sp.simplify(t_high/t_side)==sigma**-8
# Conversely a wait of order J^-2 contains R^2/J^2 -> infinity high clocks,
# so the high sphere has disappeared exponentially before the wait completes.
assert sp.simplify(t_side/t_high)==sigma**8

print('PASS: high-pulse/slow-sideband clocks separate exactly.')
print('For J/R->0, J-scale viscous action during one R^-2 Beltrami pulse is (J/R)^2->0.')
print('A direct continuous Raman-plus-J-viscosity Schur lift is therefore not the one-pulse realization; kick then viscous wait is the compatible split.')
