#!/usr/bin/env python3
"""Algebraic full-correction cancellation of a mean-assisted zero-wave startup."""
import sympy as s

# Bilinear symbols stand for one fixed Fourier/polarization coefficient of the
# projected NS bilinear form.  Only bilinearity is used.
A,B=s.symbols('A B')  # B(mean,source wave), B(source wave,mean)
y,w,b=s.symbols('y w b')

# Cross interaction of a mean correction b with source wave y enters L_U w.
linear_cross=b*y*(A+B)
# The quadratic correction contains the same interaction with correction wave w.
quadratic_cross=b*w*(A+B)
full=s.factor(linear_cross+quadratic_cross)
assert full==b*(A+B)*(w+y)

# If the total wave q=y+w is zero, the complete mean-wave interaction vanishes.
assert s.simplify(full.subs(w,-y))==0

# More generally it acts on the total wave q, so q=0 is invariant under an
# axisymmetric mean.  This is independent of coefficient signs or cutoff size.
q=s.symbols('q')
assert s.simplify(full.subs(w,q-y)-b*(A+B)*q)==0

print('PASS: full mean-wave coupling is proportional to the TOTAL wave y+w.')
print('An axisymmetric mean cannot regenerate a harmonic after the correction has canceled it exactly.')
print('Scope: exact bilinear/full-correction algebra; non-axisymmetric supply and exterior import remain open.')
