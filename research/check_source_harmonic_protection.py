#!/usr/bin/env python3
"""Phase-integer grading for the source physical daughter window.

The analytic PDE statement is in the companion evidence note.  This script
freezes the grading arithmetic only.
"""

# Four causal parents use one nonzero physical phase integer m.
m=1
parents=[m,m,m,m]
assert all(x==m for x in parents)

# Axisymmetric/mean coefficients have grade zero.  Every linear source
# operation therefore preserves the parent grade.
mean=0
assert all(x+mean==m for x in parents)

# Both designated pair decompositions land in the exact same daughter grade.
dA=parents[0]+parents[1]
dB=parents[2]+parents[3]
assert dA==dB==2*m

# A mean generated at quadratic order cannot pollute the daughter linearly:
# mean x parent remains grade m.  A daughter x mean remains grade 2m.
assert mean+m==m
assert mean+2*m==2*m

# At order epsilon, only grade m occurs.  Grade 2m first occurs at quadratic
# order from two nonzero-wave factors.
linear_grades={m}
assert 2*m not in linear_grades
quadratic_grades={a+b for a in {m,-m} for b in {m,-m}}
assert 2*m in quadratic_grades and quadratic_grades=={-2*m,0,2*m}

print('PASS: source phase grading forbids O(epsilon) pollution of the 2m daughter.')
print('Linear mean/slow/pressure operations preserve m; the designated daughter first appears quadratically.')
print('Scope: exact harmonic grading only; coefficient-size and whole-space PDE estimates are analytic.')
