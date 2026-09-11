#!/usr/bin/env python3
"""Exact regression checks for Gaussian-vs-exponential prefix summability."""
from fractions import Fraction

checks = 0

# For a term 2^E_j with E_j=-2*gamma*j^2 + c*j, the consecutive
# exponent difference is -4*gamma*j - 2*gamma + c.  Check exact
# eventual negativity for a broad rational grid, including extra fixed
# polynomial-frequency weights folded into c.
for gp in range(1, 8):
    for gq in range(1, 8):
        gamma = Fraction(gp, gq)
        for cp in range(-8, 17):
            for cq in range(1, 6):
                c = Fraction(cp, cq)
                threshold = max(1, int((c - 2*gamma) / (4*gamma)) + 2)
                for j in (threshold, threshold + 1, threshold + 7, threshold + 31):
                    diff = -4*gamma*j - 2*gamma + c
                    assert diff < 0
                    checks += 1

# Exact monomial exponent check with unstable multiplicity 2^(2j/3),
# seed 2^(-alpha*j^2+b*j), and a fixed frequency weight 2^(N*kappa*j).
for alpha_num in range(1, 6):
    alpha = Fraction(alpha_num, 5)
    for b_num in range(-3, 5):
        b = Fraction(b_num, 3)
        for N in range(0, 9):
            kappa = Fraction(5, 4)
            c = Fraction(2, 3) + 2*b + 2*N*kappa
            j = max(2, int((c - 2*alpha) / (4*alpha)) + 3)
            E_j = -2*alpha*j*j + c*j
            E_next = -2*alpha*(j+1)*(j+1) + c*(j+1)
            assert E_next < E_j
            checks += 1

print(f"prefix-summability exact checks: {checks} passed")
