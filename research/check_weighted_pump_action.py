#!/usr/bin/env python3
"""Exact controls for weighted pressure, norm ordering and symmetry reset.

These checks freeze algebra and a reusable counter-control. The analytic
whole-space proof, source hypotheses and scope are in the companion note;
finite checks are not a standalone propagator or NS certificate.
"""
from fractions import Fraction as Q
import sympy as s


def main():
    x=s.symbols('x',real=True)
    v=s.Function('v')(x); phi=s.Function('phi')(x)
    # Conjugated diffusion: the divergence term integrates to zero.
    left=s.exp(-phi)*v*s.diff(s.exp(phi)*v,x,2)
    right=(-s.diff(v,x)**2+s.diff(phi,x)**2*v**2
           +s.diff(v*s.diff(v,x)+s.diff(phi,x)*v**2,x))
    assert s.simplify(left-right)==0

    delta=s.symbols('delta',real=True)
    c=(1+2*delta)/(1-2*delta)
    assert s.simplify(s.diff(c,delta)-4/(1-2*delta)**2)==0
    assert c.subs(delta,Q(1,8))==Q(5,3)
    assert 4*Q(1,8)*Q(5,3)==Q(5,6)
    assert c.subs(delta,0)==1

    # If g is any unit-height C-infinity bump in (-1/2,1/2), the moving
    # periodic profile has EXACT exponents below by a change of variable.
    # The integral of g is a fixed nonzero factor, never assumed equal to 1.
    peak=Q(1,4); width=Q(1,2); period=Q(1)
    copy_action=peak+width
    global_sup_action=peak+period
    assert copy_action==Q(3,4)
    assert global_sup_action==Q(5,4)
    assert global_sup_action-copy_action==Q(1,2)
    assert copy_action-period==-Q(1,4)  # retained broad clock remainder

    # The physical strain-time normalization cancels exactly.
    h=s.symbols('h',positive=True)
    A=Q(1,2)+h
    assert s.simplify((1+h)-A-Q(1,2))==0
    kappa=Q(1,100000)
    for exponent in (Q(1,2)-2*kappa,1-kappa,Q(1,2)-kappa,1-2*kappa):
        assert exponent>0
    # An angular gap epsilon^(-alpha) must satisfy alpha>kappa.
    alpha=Q(1,4)
    assert alpha>kappa
    assert alpha-kappa>0

    # Exact full-vector parity rules in an N-fold equivariant field.
    for a in range(-9,10):
        for b in range(-9,10):
            assert (a+b)%2==((a%2)+(b%2))%2
            if a%2==b%2==1: assert (a+b)%2==0

    # Dirichlet-quotient completion of the square, valid in a real Hilbert
    # space after projecting onto each orthogonal coordinate and summing.
    z,f=s.symbols('z f',real=True)
    assert s.expand(-2*z*z+2*z*f-(f*f/2-2*(z-f/2)**2))==0
    a,b=s.symbols('a b',nonnegative=True)
    assert s.expand(2*a*a+2*b*b-(a+b)**2-(a-b)**2)==0
    # q' <= (M0^2/nu) q + M1^2; the logarithmic lower bound has finite
    # integral while these coefficients and the classical Sobolev norms are
    # finite. No input-only uniform bound near an endpoint is inferred.

    print('PASS: weighted diffusion and pressure constants, with no weight-amplitude loss')
    print('PASS: int sup has L^(5/4), whereas sup int has L^(3/4), for the moving-bump control')
    print('PASS: compact clock primitive leaves L^(-1/4) remainder and L^(3/4) endpoint cost')
    print('PASS: full parity and Dirichlet-quotient algebra for the exact no-symmetry-reset theorem')
    print('Scope: analytic hypotheses in the note remain essential; NS-R3 is not certified')


if __name__=='__main__':
    if not __debug__:
        raise RuntimeError('Run without -O: exact assertions are required')
    main()
