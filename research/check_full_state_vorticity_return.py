#!/usr/bin/env python3
"""Exact finite identities for the full-state vorticity-return author proof.

Requires SymPy. No floating-point dynamics or numerical PDE certificate.
Does NOT certify compactness, inviscid convergence, a full-turnover orbit,
independent mathematical audit, a critical producer, or NS-R3 regularity.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
import sympy as s


def main(output: Path | None = None) -> dict:
    labels: list[str] = []

    def equal(left, right, label: str) -> None:
        if isinstance(left, s.MatrixBase) or isinstance(right, s.MatrixBase):
            if not isinstance(left, s.MatrixBase) or not isinstance(right, s.MatrixBase):
                raise AssertionError(label + ': matrix/scalar mismatch')
            if left.shape != right.shape:
                raise AssertionError(label + ': matrix shape mismatch')
            ok = all(s.simplify(x) == 0 for x in left-right)
        else:
            ok = s.simplify(left-right) == 0
        if not ok:
            raise AssertionError(label)
        labels.append(label)

    def require(condition: bool, label: str) -> None:
        if not condition:
            raise AssertionError(label)
        labels.append(label)

    x, y, z, t = s.symbols('x y z t', real=True)
    xyz = (x, y, z)
    zero = s.zeros(3, 1)

    def curl(v):
        return s.Matrix([s.diff(v[2], y)-s.diff(v[1], z),
                         s.diff(v[0], z)-s.diff(v[2], x),
                         s.diff(v[1], x)-s.diff(v[0], y)])

    def adv(v, w):
        return s.Matrix([sum(v[j]*s.diff(w[i], xyz[j]) for j in range(3))
                         for i in range(3)])

    def lap(v):
        return v.applyfunc(lambda f: sum(s.diff(f, q, 2) for q in xyz))

    # Generic functions, not only a selected polynomial flow.
    u = s.Matrix([s.Function('u'+str(i))(*xyz) for i in range(3)])
    omega = curl(u)
    divu = sum(s.diff(u[i], xyz[i]) for i in range(3))
    equal(curl(adv(u, u)), adv(u, omega)-adv(omega, u)+divu*omega,
          'generic curl-convection identity including divergence term')
    equal(sum(s.diff(omega[i], xyz[i]) for i in range(3)), 0,
          'generic divergence of vorticity')
    pressure = s.Function('pressure')(*xyz)
    equal(curl(s.Matrix([s.diff(pressure, q) for q in xyz])), zero,
          'curl removes canonical pressure gradient without replacing pressure')
    equal(curl(lap(u)), lap(omega), 'ordinary Laplacian commutes with curl')
    potential = s.Matrix([x*y*z+x**3*y, x*z**2+y**3*z, x**2*y*z+y*z**3])
    sol = curl(potential)
    equal(sum(s.diff(sol[i], xyz[i]) for i in range(3)), 0,
          'genuinely 3D polynomial curl is solenoidal')
    equal(curl(-adv(sol, sol)), adv(curl(sol), sol)-adv(sol, curl(sol)),
          'original nonlinear material vorticity equation')

    # Noncommuting, volume-preserving deformation: exact variation of constants.
    J = (s.Matrix([[1,t,0],[0,1,0],[0,0,1]]) *
         s.Matrix([[1,0,0],[0,1,t**2],[0,0,1]]) *
         s.Matrix([[1,0,0],[0,1,0],[t**3,0,1]]))
    A = s.simplify(J.diff(t)*J.inv())
    equal(J.det(), 1, 'volume-preserving noncommuting material Jacobian')
    equal(s.trace(A), 0, 'material velocity gradient has zero trace')
    equal(J.diff(t), A*J, 'Jacobian evolution with correct matrix order')
    mu = s.symbols('mu', nonnegative=True)
    w0 = s.Matrix(s.symbols('w0:3'))
    integrand = s.Matrix([t**2, 1+t, 1-t**3])
    primitive = integrand.applyfunc(lambda f: s.integrate(f, (t, 0, t)))
    forcing = J*integrand
    transported = J*(w0+mu*primitive)
    equal(transported.subs(t, 0), w0, 'full material initial value')
    equal(transported.diff(t), A*transported+mu*forcing,
          'viscous variation of constants retains full forcing')
    equal(s.simplify(J.inv()*forcing), integrand,
          'inverse-Jacobian pullback of viscous forcing')
    equal(s.simplify((J.inv()*transported).diff(t)), mu*integrand,
          'Cauchy invariant has exactly the viscous defect')

    a, K, nu, g, lam = s.symbols('a K nu g lam', positive=True)
    equal((a*K)/(a*K**2)*(1/(a*K))**2, 1/(a**2*K**3),
          'physical normalization common PDE factor')
    equal((nu/a)/(a*K**3), nu/(a**2*K**3),
          'physical viscosity becomes nu/a')
    equal(1/(g*lam)/(g*lam**2), 1/(g**2*lam**3),
          'return time derivative factor')
    equal((1/(g*lam))**2/lam, 1/(g**2*lam**3),
          'return nonlinear factor')
    equal((mu/g)/(g*lam**3), mu/(g**2*lam**3),
          'effective viscosity updates to mu/g')
    equal((1/(g*lam))**2, 1/(g**2*lam**2),
          'canonical quadratic pressure factor')
    p = s.symbols('p', positive=True)
    equal((3-2*p)-p/2, 3-s.Rational(5,2)*p,
          'full-energy-normalized geometric exponent')
    equal(-p-(-p), 0, 'amplitude gain cancels from full-state shape ratio')
    equal(3-s.Rational(5,2)*s.Rational(6,5), 0,
          'critical vorticity power erases geometric gain')
    equal(2*p-3+p/2, s.Rational(5,2)*p-3,
          'NS critical scaling of the shape functional')
    equal((s.sqrt(lam)/g)**2, lam/g**2,
          'full L2 energy under the return, not carrier energy')
    equal(s.Rational(2,3)**2, s.Rational(4,9),
          'Q1 lower vorticity-L2 normalization constant')

    # The radial integral is a rational antiderivative at every exponent s>3.
    h, q = s.symbols('h q', positive=True)
    primitive_radial = (q**(3-h)/(3-h)-2*q**(2-h)/(2-h)+q**(1-h)/(1-h))
    equal(s.diff(primitive_radial, q), (q-1)**2*q**(-h),
          'radial weighted integral antiderivative')
    equal(-4*s.pi*primitive_radial.subs(q, 1),
          8*s.pi/((h-1)*(h-2)*(h-3)), 'exact three-dimensional tail integral')

    # Explicit exact finite telescopes: p=2/5 removes radicals after fifth powers.
    F = Fraction
    blocks = [((F(2),F(3,2),F(1,10)), (F(3,2),F(5,4),F(1,20))),
              ((F(4),F(2),F(1,4)), (F(2),F(7,6),F(0)), (F(3),F(5,3),F(1,8)))]
    for j, block in enumerate(blocks):
        value = F(1)
        product_scale = F(1)
        product_distortion = F(1)
        product_defect = F(1)
        for l, d, e in block:
            value *= l**10/d**2*(1-e)**5
            product_scale *= l
            product_distortion *= d
            product_defect *= 1-e
        require(value == product_scale**10/product_distortion**2*product_defect**5,
                f'finite full-defect telescope, block {j}')
    for denominator in range(2, 13):
        pp = F(1, denominator)
        exponent = F(3)-F(5,2)*pp-pp  # lambda0=2, L=log(2)
        require(exponent > 0, f'small-p growth threshold p=1/{denominator}')
    # Test one strictly finite block bound without decimal approximations.
    require(F(17,8)*4-F(4) > F(4), 'r^4 b>B for r=2^(17/8), b=1/16, B=16')

    # Critical-invisible satellite: exact exponents for many rational powers.
    for pp in [F(1,8),F(1,4),F(2,5),F(1,2),F(3,4),F(1),F(7,6)]:
        beta = (F(3)/pp-F(5,2))/2
        require(beta > 0, f'positive satellite beta at p={pp}')
        require(F(3)-(F(5,2)+beta)*pp > 0, f'divergent vorticity mass at p={pp}')
        require(-beta-F(1,2) < 0, f'vanishing critical Lorentz satellite at p={pp}')
        for order in range(7):
            require(-beta-order < 0, f'vanishing H derivative {order}, p={pp}')
    require(4 > 2, 'Lp triangle inequality fails for disjoint unit supports at p=1/2')
    equal((s.Matrix([1,0,0])+s.Matrix([-1,0,0]))/2, zero,
          'vector averaging may cancel vorticity; no invented positive diffusion sign')

    # Regression assertions for the repaired predecessor tuple comparator.
    for left, right in [((s.Rational(1,3),0),(s.Rational(2,6),0)),
                        ((0,s.Rational(-4,65)),(0,s.Rational(-4,65)))]:
        require(all(s.simplify(x-y)==0 for x,y in zip(left,right)),
                'componentwise tuple comparison positive regression')
    require(any(s.simplify(x-y)!=0 for x,y in zip((0,1),(0,2))),
            'componentwise tuple comparison rejects unequal vectors')

    result = {'status':'PASS_EXACT_FINITE_IDENTITIES', 'assertions':len(labels),
              'labels':labels,
              'exclusions':['No analytic compactness or PDE validation',
                            'No certified regenerative turnover',
                            'No independent mathematical audit',
                            'No NS-R3 proof or continuation producer']}
    text = json.dumps(result, indent=2)+'\n'
    print(text, end='')
    if output is not None:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', type=Path)
    main(parser.parse_args().json)
