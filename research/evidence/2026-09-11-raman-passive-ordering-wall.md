# Passive asymmetries cannot repair the Raman time-order cancellation

Date: 2026-09-11. Repository input:
`itpplasma/navier@8c9f1c054df01839f77a5663c0a6eae25c4a39d7`.

**Status: exact scoped no-go.** After the leading cancellation between the two
time orderings of a simultaneously preloaded near-opposite Raman pair, none of
the three cheapest passive repairs restores one-way leading action: the current
pump geometries have equal Stokes clocks; arbitrary complex amplitude/phase
weights multiply both ordered trees by the same scalar product; and the two
leading target-to-high first legs share the same target factor `A.Q`, so
polarization cannot kill only one of them while retaining the `O(N)` Raman
scale.

The exact algebra is frozen by
`research/check_raman_passive_ordering_wall.py`.

This narrows a surviving Raman route to a genuinely new operation: dynamically
create/remove one high parent, spatially order the interactions, or replace the
near-opposite two-parent geometry.

## 1. Heat clocks do not order the current pairs

Both current Raman families use centered near-opposite parents

    q=l/2+NQ,
    r=l/2-NQ,
    l.Q=0.                                                 (1.1)

Hence exactly

    |q|^2=|r|^2.                                          (1.2)

Their Stokes factors are identical for every time, so viscosity cannot prefer
`q then r` to `r then q`.

Even without the orthogonality in (1.1), a centered near-opposite pair obeys

    |q|^2-|r|^2=2N Q.l.                                   (1.3)

On one high clock `t=c/(N^2|Q|^2)`, the relative heat exponent is

    t(|q|^2-|r|^2)
      =2c (Q.l)/(N|Q|^2).                                 (1.4)

Thus it tends to zero whenever the low sum remains scale separated,
`|l|/(N|Q|)->0`. A fixed order-one Stokes asymmetry is incompatible with the
near-opposite slow-sum limit itself.

## 2. Phases and amplitudes multiply both trees equally

Let the complex Fourier amplitudes of the two high parents be `a_q,a_r`. The
leading two-step response is bilinear in the high background. Therefore the
forward and reverse trees have scalar weights

    a_q a_r L,
    a_q a_r (-L),                                         (2.1)

respectively, where the exact previous checkpoint proves the geometric symbols
are opposite.

Changing the magnitude or phase of either preloaded parent multiplies both
terms by the same product. It cannot remove their cancellation unless one
parent is removed, in which case the two-parent transfer itself is absent.

## 3. Leading polarization diode is impossible

Let `(h,A)` be the slow target and take

    q=NQ+O(l),
    r=-NQ+O(l),                                           (3.1)

with nonzero transverse limiting parent polarizations `beta_0,epsilon_0`. The
symmetric Leray interaction has the exact leading limits

    N^-1 C(h,A;q,beta)
      -> (A.Q) beta_0,                                    (3.2)

    N^-1 C(h,A;r,epsilon)
      -> -(A.Q) epsilon_0.                                (3.3)

The limiting polarizations are transverse to `Q`, so Leray does not remove
these vectors.

If `A.Q!=0` and both parents are nonzero, both first legs are present at the
same leading scale. If `A.Q=0`, both lose that scale. Hence no choice of
nonzero parent polarizations makes exactly one target-to-high leg dark while
retaining the leading Raman mechanism.

## 4. Small residual asymmetry is not enough in the Beltrami lift

Suppose one tried to use a relative ordering asymmetry of only `O(J/R)`, as in
the general heat-clock bound. A fixed residual action would scale as

    rho^2 J/R^2.                                          (4.1)

Keeping (4.1) order one forces

    (rho/sqrt(R))^2 comparable to R/J -> infinity        (4.2)

when `J/R->0`. This leaves the controlled first-star Beltrami/Krein regime
isolated in the earlier exact checkpoint.

## 5. Recomputed Raman frontier

The current preloaded-pair Raman shortcut is therefore exhausted at leading
order. A surviving Raman route must add a genuinely new autonomous ingredient.
The cheapest remaining constructive candidate is **nonlinear parent birth**:
preload one Raman parent together with a separate high shear/clock mode and let
an exact invariant high subsystem generate the second near-opposite parent from
zero. The repository already contains an exact 2D3C shear/passive-scalar
channel in which a real shear translates a scalar Fourier ladder linearly; it
is the natural discriminator for this idea.

That mechanism must pass two tests before it is useful:

1. the full target-assisted Taylor coefficient, including every ordering through
   the generating shear, must remain nonzero after summing all trees; and
2. its fixed-action scaling must not require a high-parent norm that reintroduces
   an uncontrolled `O(rho)` propagator or the previously excluded activation
   clock.

If it fails either test, further Raman work would merely move the autonomous
preparation hard core into a larger high subsystem, and the route should be
retired in favor of a distinct terminal mechanism.

No terminal regularity theorem, finite-time singular solution, regenerative
turnover, or `NS-R3` resolution is claimed.
