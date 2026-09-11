# Large-amplitude coercivity wall for the comparable-frequency heat normal form

Date: 2026-09-11. Repository input:
`itpplasma/navier@df07e9984052c62096b60f8bc51243d8c507465e`.

**Status: exact scaling obstruction to the first normal-form use of the new
angular-resonance budget.** The weighted-moment theorem gives an input-only
`O(eta)` spacetime cost for concentration in relative-width heat-resonance
slabs. Away from those slabs, however, integrating the signed comparable-scale
production by the parabolic homological denominator produces a boundary
correction one amplitude degree higher than the critical entropy. At arbitrary
critical amplitude this correction is not uniformly coercive and cannot be
absorbed into the sixth-power smooth-block functional.

This does not refute every spacetime use of the angular budget. It rules out the
straightforward scheme

    resonance-slab split
      + one heat normal-form integration
      + absorb the boundary primitive into W.

No terminal regularity claim is made.

## 1. Critical homogeneity of the smooth-block functional

On one fixed comparable dyadic cluster at frequency `lambda`, scale all Fourier
amplitudes by a scalar `M`, keeping the frequency geometry and polarization
fixed. For the audited sixth-power functional,

    W_cluster ~ M^6.                                      (1.1)

Its viscous term has the same amplitude degree,

    D_cluster ~ lambda^2 M^6.                             (1.2)

The comparable-frequency nonlinear production contains the state-dependent
fourth-power weight `gamma_k` times one trilinear convection pairing. Hence

    Pi_cluster ~ lambda^2 M^7.                            (1.3)

The extra amplitude degree is the scale-local ratio already isolated in the
audited bound `|Pi|<=C A D`.

There are admissible comparable triads with nonzero signed production. The
explicit centrally odd planar calibration preserved in
`2026-09-08-signed-transfer-interrupted.md` has strictly positive production;
by continuity of the Fourier/Leray symbol, arbitrarily close non-right-angle
frequency triples retain nonzero production while having a fixed nonzero heat
mismatch. Thus the following scaling is not vacuous.

## 2. Nonresonant heat denominator

For a triad `p+q=k`, the heat mismatch is

    Omega=nu(|p|^2+|q|^2-|k|^2)=-2nu p.q.                 (2.1)

On the nonresonant comparable region

    |p.q| >= eta lambda^2,                                (2.2)

one has

    |Omega| >= 2nu eta lambda^2.                          (2.3)

A single integration by parts in time therefore replaces the production by a
boundary primitive whose natural size is

    |N_cluster|
      ~ |Pi_cluster|/|Omega|
      ~ M^7/(nu eta).                                     (2.4)

Consequently

    |N_cluster|/W_cluster
      ~ M/(nu eta).                                       (2.5)

For any fixed `0<eta<=1`, the ratio (2.5) is unbounded as `M->infinity`.
Thus no constant independent of the current critical amplitude can make

    W + N                                                   (2.6)

comparable to `W` on arbitrary-amplitude states. The same obstruction appears
if the primitive is kept only as an endpoint term: its final-time value cannot
be absorbed by the desired critical bound with a coefficient below one.

## 3. The resonance width cannot fix the amplitude degree

The new weighted-moment theorem gives a near-resonant spacetime budget
proportional to `eta`. Shrinking `eta` therefore helps the resonant piece, but
(2.5) becomes worse like `eta^-1` on the nonresonant piece.

To make the normal-form primitive perturbative relative to `W` would require
schematically

    eta >= c M/nu.                                        (3.1)

For arbitrary critical amplitude `M>>nu`, (3.1) is incompatible with a
relative angular width `eta<=1`. Hence optimizing the resonance split cannot
repair the coercivity failure.

This is independent of the exact `O(eta)` constant in the slab theorem and of
how sharply the near-resonant part is estimated. The obstruction occurs before
the derivative created by the time integration is even analyzed.

## 4. State-dependent weights create an additional circular term

The actual multiplier is

    m_U(xi)=sum_k gamma_k phi(xi/lambda_k)^2,
    gamma_k=lambda_k a_k^4.                               (4.1)

A time normal form differentiates not only the Fourier amplitudes but also the
weights `gamma_k`. Their derivatives contain the block energy-transfer terms
that generated the original comparable-frequency production. Therefore, even
if the boundary term (2.4) were coercive, the normal-form remainder would feed
back into the same signed critical transfer unless a new trajectory estimate
controlled `dot gamma_k`.

The large-amplitude wall (2.5) is stronger: the straightforward correction
already fails before this circular derivative is reached.

## 5. Recomputed positive-route frontier

The weighted-moment/angular result remains useful information: it proves that
whole-space solutions cannot concentrate arbitrary spacetime `L^2` mass in a
prescribed thin heat-resonance slab. What it does **not** provide is a
large-amplitude critical normal form.

The positive route is therefore reduced again to the genuinely nonlinear
trajectory question:

    control accumulated comparable-scale transfer
    at arbitrary critical amplitude without
    (a) an instantaneous sign,
    (b) a perturbative normal-form correction,
    (c) sup_k a_k, or
    (d) integral ||grad u||_2^4.                           (5.1)

The preserved exact counterexamples already exclude scalar phase averaging,
signed-helicity-only budgets, static heat slaving, and absolute smooth-block
bounds as solutions to (5.1).

Under the diversification rule, the next terminal attack should therefore move
to the independent full-PDE mixed-trace/exactification architecture rather
than iterate more critical-entropy corrections with the same amplitude-degree
wall.

NON-CLAIMS: no RF-q producer, no exclusion of every possible use of weighted
moments or angular information, and no `NS-R3` conclusion. Independent audit
and novelty assessment are pending.
