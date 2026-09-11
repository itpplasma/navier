#!/usr/bin/env python3
"""Exact exponent ledger for the angular quartic-event budget.

The analytic theorem is in research/evidence/2026-09-11-angular-quartic-event-budget.md.
This checker freezes only the algebraic source-scale comparison; it is not a PDE proof.
"""
from fractions import Fraction

# Source proof-outline scales on a dyadic q-band:
# n^2 ~ q^{-h}, pointwise A_wave^2 ~ q^{-1-h}, active volume ~ q^{3/2-h},
# physical pulse time ~ q^{1+h} * polylog.
h = Fraction(1, 100)  # worst allowed endpoint; the source assumes strictly smaller h
energy_exp = Fraction(3, 2) - h - (1 + h)  # E=||Pi_n u||_2^2
assert energy_exp == Fraction(1, 2) - 2*h
cost_exp = (-h) + 2*energy_exp + (1 + h)
assert cost_exp == 2 - 4*h
assert cost_exp == Fraction(49, 25) > 0

# The angular uncertainty step uses
#   (|n|-1)^2 E_n^2 <= ||r v_n||_2^2 ||grad v_n||_2^2.
# Summing and integrating is paid by the moment supremum and ordinary dissipation.
print('PASS: source pulse quartic-event exponent is 2-4h; at h=1/100 it is 49/25>0.')
print('Scope: algebraic scale ledger only; the angular-event inequality itself is analytic.')
