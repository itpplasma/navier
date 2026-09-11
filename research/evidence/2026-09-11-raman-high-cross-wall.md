# Cross-module high-high wall for the independent Raman-pump realization

Date: 2026-09-11. Repository input:
`itpplasma/navier@36d25a0fffd48454ae5619300a3843dd765dc0e3`.

**Status: exact scoped obstruction.** The all-orders effective Raman lattice
from `2026-09-11-all-orders-raman-lattice.md` cannot be lifted by simply
superposing its five high pairs as approximately independent Stokes-decaying
pumps at the scaling required for order-one Raman action. Two modules already
produce a cross high-frequency sideband whose amplitude relative to a parent is
`O(rho)`, while useful Raman coupling forces `rho->infinity`.

The obstruction is frozen by
`research/check_raman_high_cross_wall.py`.

It does not refute state-triggered purification itself. It eliminates one
specific full-NS realization: five mutually generic large high-frequency pump
pairs treated as if cross-module high-high interactions were perturbative.

## 1. Explicit cross coefficient

For the first two modules of the all-orders-safe effective basis, the leading
high directions and leading parent polarizations are

    Q_1=(1,-2,-3),
    beta_1=(-14,5,-8),                                    (1.1)

    Q_2=(0,1,1),
    beta_2=(1,-5,5).                                      (1.2)

Both polarizations are transverse to their high directions. The exact Leray
interaction coefficient is

    C(Q_1,beta_1;Q_2,beta_2)
      =(49,-1,25) !=0.                                    (1.3)

The heat exponents are

    |Q_1|^2=14,
    |Q_2|^2=2,                                             (1.4)

while the cross sideband direction is

    Q_1+Q_2=(1,-1,-2),
    |Q_1+Q_2|^2=6.                                        (1.5)

Thus the Stokes-Duhamel heat gap is exactly

    14+2-6=10.                                             (1.6)

There is no resonance or cancellation hiding the cross interaction.

## 2. The cross sideband is larger than a parent at useful Raman scaling

Let the two physical high-parent velocity amplitudes be of common scale `P`
and write

    rho=P/(nu N).                                         (2.1)

At time

    t=tau/(nu N^2),                                       (2.2)

the second-Picard cross sideband generated from the two heat-decaying parents
has the exact leading coefficient

    (P^2/(nu N))
      [(exp(-6 tau)-exp(-16 tau))/10]
      (49,-1,25).                                         (2.3)

Relative to one parent this is

    rho
      [(exp(-6 tau)-exp(-16 tau))/10]
      (49,-1,25).                                         (2.4)

For every fixed `tau>0` the scalar factor is nonzero. Hence the cross sideband
is not an `o(P)` correction when `rho` grows.

The state-triggered Raman return has the one-power fast/slow loss recorded in
the preceding packets:

    effective slow coupling ~ rho^2/R,
    R=N/b.                                                 (2.5)

To retain a nonzero order-one effective filter as `R->infinity`, one needs

    rho^2/R >= gamma>0.                                   (2.6)

Therefore

    rho >= sqrt(gamma R) -> infinity.                     (2.7)

Combining (2.4) and (2.7), the cross high sideband becomes unbounded relative
to the nominal high parents. The five-module background is therefore not a
small perturbation of the independent heat evolution used to derive the
leading effective Raman operator.

## 3. What this kills, and what it does not

This obstruction kills the following lift:

    five generic large preloaded high pairs
      -> evolve each pair essentially by heat
      -> ignore cross-module high-high sidebands
      -> retain only the designed slow Raman operator.     (3.1)

At the required scaling, step two is false before one even addresses
finite-energy localization.

The effective slow theorem itself remains exact as an algebraic/high-frequency
model. The failure is in the proposed high background realizing it.

The natural escape is to require the complete high background to be
**nonlinearly silent at arbitrary amplitude** rather than merely pairwise
silent at its own low difference frequency. A particularly strong candidate is
a common Beltrami eigenspace:

    curl U_high=lambda U_high.                            (3.2)

Then

    P[(U_high.grad)U_high]=0                               (3.3)

identically, and viscosity simply multiplies the entire high field by
`exp(-nu lambda^2 t)`, irrespective of amplitude and of cross-mode content.

The next discriminating question is therefore whether one can choose
same-helicity, equal-|k| high pairs on one Beltrami sphere so that their
state-triggered two-step slow responses still span the required inheritance
filter. If the Beltrami constraint collapses the response span below dimension
five, this escape fails algebraically. If it retains full span, the high-high
wall is removed exactly and the remaining task becomes the linearized/high-slow
normal form about a known exact high background.

No PLAN/canonical proof-graph promotion, recursive turnover, singular solution,
or `NS-R3` claim is made here.
