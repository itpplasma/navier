# Closed affine strain-loop wall for the clean dyadic circuit

Date: 2026-09-11. This packet tests the finite-time escape suggested by
`2026-09-11-clean-gate-strain-filter.md`.

**Status: author proof for linearized perturbations about time-dependent affine
symmetric strains; independent audit and novelty undetermined.** It rules out a
specific parent-filter architecture.  It does not rule out open deformations,
nonlinear filtering, spatially non-affine routing, or localized finite-energy
backgrounds.

## 1. Time-dependent affine strains and Kelvin variables

Let

    U(t,x)=A(t)x,                                          (1.1)

where `A(t)` is smooth, symmetric, and trace free.  Since `Delta U=0` and
`A'(t)+A(t)^2` is symmetric, (1.1) is an exact unforced incompressible
Navier--Stokes solution with a quadratic pressure.  It has infinite kinetic
energy and is used only as a mechanism test.

Let `F` be the deformation gradient

    F'=A F,       F(0)=I.                                 (1.2)

Because the base vorticity is zero, a linearized Kelvin vorticity mode obeys

    k(t)=F(t)^(-T) k_0,                                   (1.3)

    omega(t)=F(t) omega_0
       exp[-nu integral_0^t |F(s)^(-T)k_0|^2 ds].          (1.4)

Equation (1.4) is the affine Cauchy formula with the scalar viscous factor.
It follows directly by substituting a Kelvin mode into the linearized
vorticity equation

    omega_t+(Ax).grad omega=A omega+nu Delta omega.        (1.5)

## 2. A closed strain loop is only a positive quadratic viscous filter

Suppose the strain history restores the carrier geometry exactly,

    F(T)=I.                                                (2.1)

Then `k(T)=k_0` and (1.4) gives

    omega(T)=exp[-nu J(k_0)] omega_0,                      (2.2)

where

    J(k)=integral_0^T |F(t)^(-T)k|^2 dt
        =k^T M k,                                         (2.3)

    M=integral_0^T F(t)^(-1)F(t)^(-T) dt.                 (2.4)

For every nonzero `k`, `J(k)>0`; hence `M` is positive definite.  Since the
wavevector returns, the Biot--Savart relation between Kelvin vorticity and
velocity also returns to its initial algebraic form, so the velocity mode is
multiplied by the same scalar attenuation.

Thus no matter how complicated the closed affine strain history is, its net
linearized spectral selectivity is encoded by one positive quadratic form.

The same conclusion holds if the final deformation is a rigid rotation:
a common orthogonal change of coordinates merely conjugates `M` and does not
alter the argument below.

## 3. Parallelogram obstruction for the two selected `1--3` children

The clean dyadic first gate retains both signed children of the `k1,k3` pair,

    k_- = k1-k3,       k_+ = k1+k3.                       (3.1)

For every quadratic form `J`, the parallelogram identity is

    J(k_-)+J(k_+)=2J(k1)+2J(k3).                          (3.2)

Equivalently,

    [J(k_-)+J(k_+)]/2=J(k1)+J(k3).                        (3.3)

Because `M` in (2.4) is positive definite,

    J(k1)>0,       J(k3)>0.                               (3.4)

Therefore

    max{J(k_-),J(k_+)}
       >= J(k1)+J(k3)
       > max{J(k1),J(k3)}.                                (3.5)

At least one of the two desired children is consequently damped **more** over
the closed loop than either corresponding parent.  In attenuation factors,

    min{e^(-nu J(k_-)),e^(-nu J(k_+))}
       < min{e^(-nu J(k1)),e^(-nu J(k3))}.                (3.6)

Hence a closed affine strain loop cannot simultaneously preserve both selected
`k1+/-k3` children while erasing parents `k1,k3` by viscosity.

## 4. Relation to the instantaneous positive result

There is no contradiction with the preceding instantaneous strain filter.
For the rational matrix found there, all selected children initially have
positive Kelvin amplitude rates while all parents initially decay.  But the
strain simultaneously moves the wavevectors.  If one insists on later undoing
that deformation so the exact dyadic gate geometry is restored, the complete
closed excursion has the scalar action (2.3), and the parallelogram wall
(3.5) applies.

This kills the most attractive version of the proposed `strain loop` repair:

    clean child birth
      -> affine strain separates children from parents
      -> inverse strain restores circuit geometry
      -> next clean gate.                                 (4.1)

No choice of a time-dependent symmetric trace-free affine strain can make
(4.1) a simultaneous viscous parent eraser for both signed `1--3` children.

## 5. Surviving routes

The remaining mechanisms must violate at least one hypothesis of this wall:

1. **open deformation:** do not restore the geometry, and find a new gate
   adapted to the deformed carrier triple;
2. **nonlinear filtering:** let sidebands/background modes participate so the
   perturbation is not governed by the linear Kelvin Cauchy factor alone;
3. **non-affine spatial routing:** separate parent and child packets in
   physical space rather than spectrally attenuating them at the same site;
4. **augmented return class:** retain the inherited modes instead of trying to
   erase them, and prove a larger self-reproducing localized state.

The third and fourth options are now the least contradicted by the exact
algebra accumulated in the current wave.

## 6. Reproducibility

`research/check_closed_strain_loop_wall.py` freezes the generic symmetric
quadratic form and verifies (3.2)--(3.3) symbolically.  Positive definiteness
of (2.4) and the Cauchy formula are analytic arguments above, not numerical
assumptions.

No finite-energy Navier--Stokes solution, localized turnover, or terminal
claim is produced.  NS-R3 remains unresolved.
