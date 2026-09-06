#!/usr/bin/env python3
"""Arithmetic/source regression checks, NOT a mathematical or Lean verifier."""
from __future__ import annotations

import argparse
import math
from fractions import Fraction as F
from pathlib import Path
import re


def check_exponents() -> None:
    for s in (F(8, 5), F(7, 4), F(2), F(5, 2), F(3), F(6), F(100)):
        alpha = F(3, 2) / s
        p = 2 * s / (2 * s - 3)
        r = 3 * s / (s - 1)
        assert 0 < alpha < 1 and 3 < r < 9
        assert 1 / r == (1 - alpha) / 3 + alpha / 9
        assert p * (1 - alpha) == 1
        assert 2 / p + 3 / s == 2
        assert alpha / (1 - alpha) == 3 / (2 * s - 3)
        assert p * (2 - 3 / s) - 2 == 0


def check_constants() -> None:
    # S factors are suppressed here: k has S^2 and a0 has S^2.
    k = 2 * F(27, 256) / F(1, 2)**3
    a0 = F(9, 8)
    pressure_l6 = a0 / 3
    assert k == F(27, 16)
    assert pressure_l6 == F(3, 8)
    assert k * pressure_l6 == F(81, 128)
    alpha = F(3, 4)
    coefficient_s2 = (1 - alpha) * alpha**3 * 2**3 * 3
    assert coefficient_s2 == F(81, 32)
    assert F(4, 3) * F(1, 2) == F(2, 3)
    assert 1 / F(2, 3) == F(3, 2)  # integrated Q^(4/3) budget
    assert F(1, 4)**2 == F(1, 16)


def check_young_samples() -> int:
    count = 0
    for alpha in (0.25, 0.5, 0.75, 0.9):
        for b in (0.1, 0.5, 1.0, 3.0):
            for eps in (0.2, 1.0, 4.0):
                xstar = (alpha * b / eps)**(1 / (1 - alpha))
                remainder = ((1 - alpha) * alpha**(alpha / (1 - alpha))
                             * eps**(-alpha / (1 - alpha))
                             * b**(1 / (1 - alpha)))
                optimum = b * xstar**alpha - eps * xstar
                assert math.isclose(optimum, remainder, rel_tol=2e-12, abs_tol=1e-12)
                for multiple in (0.0, 0.1, 0.9, 1.0, 1.1, 10.0):
                    x = multiple * xstar
                    lhs = b * x**alpha
                    rhs = eps * x + remainder
                    assert lhs <= rhs + 1e-11 * max(1.0, abs(lhs), abs(rhs))
                    count += 1
    return count


def check_boundary_examples() -> None:
    # Scalar counterexample to coefficient-one absorption => finite dissipation.
    H, nu = 2.0, 0.7
    previous = 0.0
    for n in range(1, 15):
        t = H * (1 - 2.0**(-n))
        integral_d = math.log(H / (H - t))
        assert integral_d > previous
        integral_k = nu * integral_d
        assert math.isclose(1 + nu * integral_d, 1 + integral_k)
        previous = integral_d
    # g(t)=(H-t)^(-1/3): g^2 integrable, g^4 not integrable at H.
    assert F(2, 3) < 1 < F(4, 3)


def check_source(tex: Path) -> int:
    text = tex.read_text(encoding='utf-8')
    labels = re.findall(r'\\label\{([^}]+)\}', text)
    assert len(labels) == len(set(labels)), 'duplicate TeX labels'
    references = re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', text)
    assert set(references) <= set(labels), 'unresolved internal references'
    bibliography = set(re.findall(r'\\bibitem\{([^}]+)\}', text))
    cited = {key.strip() for group in re.findall(r'\\cite\{([^}]+)\}', text)
             for key in group.split(',')}
    assert cited <= bibliography, 'unresolved citations'
    assert 'independent\nmathematical audit is pending' in text
    assert 'does not cover $s=\\infty$' in text
    assert '0\\le\\theta<1' in text
    assert text.count('\\begin{document}') == text.count('\\end{document}') == 1
    return len(labels)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tex', type=Path, required=True,
                        help='Path to dissipation_budget_continuation.tex')
    args = parser.parse_args()
    if not args.tex.is_file():
        parser.error(f'not a file: {args.tex}')
    check_exponents()
    check_constants()
    n = check_young_samples()
    check_boundary_examples()
    labels = check_source(args.tex)
    print(f'PASS: exact exponents/constants, {n} Young samples, boundary examples, '
          f'{labels} unique/resolved labels and bibliography.')
    print('Scope: arithmetic and source regression only; no PDE correctness, '
          'independent mathematical audit, or Lean proof is certified.')


if __name__ == '__main__':
    main()
