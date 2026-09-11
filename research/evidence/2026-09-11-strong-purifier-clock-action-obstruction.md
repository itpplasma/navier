# Clock-action obstruction for the strong 2D3C purifier scaling

Date: 2026-09-11. Repository input:
`itpplasma/navier@3b26bdc3d307bcd93fb41dc529eff602251c18f3`.

**Status: exact scaling consequence of the already-proved 2D3C channel and the
strong-scaling packet; independent mathematical audit and novelty are
undetermined.** This note corrects the interpretation of the strong purifier
calibration. It does not refute the exact 2D3C channel itself. It shows that the
particular asymptotic regime proposed in
`2026-09-11-strong-2d3c-purifier-scaling.md` does not yet realize the fixed
nonzero Kelvin action required by the sequential purifier consumer.

No recursive turnover, singular solution, or `NS-R3` result is claimed.

## 1. The missing quantity is integrated strain, not peak strain

The exact clocked 2D3C channel has fast time

    Delta t_N = O(N^-2).                                   (1.1)

This is explicit in the exact-channel construction: with
`x=2 nu N^2 t`, the low child pulse is a fixed function of `x` and hence is
supported on a physical time window comparable to `N^-2`.

In the strong-scaling packet, multiplying every parent product by `S` multiplies
the intended low pulse by `S`. Thus its low velocity gradient has size

    |grad U_low| = O(S)                                    (1.2)

through that same `N^-2` clock. Therefore the dimensionless deformation seen
by any clean Kelvin carrier is controlled first by the time integral

    A_N := integral |grad U_low(t)| dt
         = O(S/N^2).                                       (1.3)

The sequential two-shear consumer requires a **fixed positive** filter duration
`tau>0` (small is allowed, but independent of `N`) so that its strict carrier
signs persist. Consequently a strong clocked purifier intended to approximate
that consumer must satisfy, up to fixed constants,

    S/N^2 -> tau > 0.                                      (1.4)

In particular,

    S comparable to tau N^2.                              (1.5)

The calibration `S comparable to M nu b^2` with `N/b -> infinity` instead gives

    A_N = O((b/N)^2) -> 0,                                 (1.6)

so the clean carrier sees the identity map to first order in the accumulated
strain. Peak strain competitive with the instantaneous clean viscous rate is
not enough when the purifier exists only for the much shorter `N^-2` clock.

## 2. Restoring fixed action removes the previous small parameter

For the exact scalar ladder, the strong-scaling packet gives

    mu_N <= C sqrt(S)/N,                                   (2.1)

where `mu_N` is the integrated shear parameter controlling the nonlinear
Duhamel remainder. Under the fixed-action requirement (1.5),

    sqrt(S)/N comparable to sqrt(tau).                    (2.2)

Thus the full-ladder correction is no longer asymptotically driven to zero by
`N/b -> infinity`. This does **not** kill the channel: because the sequential
consumer only needs sufficiently small fixed `tau`, one may still hope to make
`mu_N` a small fixed number. But the previous `O(b/N)` asymptotic accuracy no
longer follows from scale separation alone.

## 3. Fixed action conflicts with the bounded fast-parent ratio used for clean protection

The gradient-preserving wavelength rescaling in the strong-scaling packet is

    d_lambda=lambda d,
    kappa_lambda=kappa/lambda,
    eta=lambda b,                                         (3.1)

with fixed large `eta` used to make the low purifier vary slowly across a clean
carrier of wave number `b`. The same packet gives the high-parent velocity
scale

    P_high = O(lambda N sqrt(S)).                          (3.2)

Hence its velocity-to-frequency ratio is

    P_high/N = O(lambda sqrt(S))
             = O(eta sqrt(S)/b).                           (3.3)

Under the fixed-action condition `S comparable to tau N^2`,

    P_high/N = O(eta sqrt(tau) N/b).                       (3.4)

Therefore, in the regime required by the existing clock-separation argument,

    eta >= eta_0 > 1,
    N/b -> infinity,                                      (3.5)

one necessarily has

    P_high/N -> infinity.                                 (3.6)

This is precisely outside the bounded fast lifted-data regime used in
`2026-09-11-lifted-galilean-clock-separation.md`, where the high-parent
velocity/frequency ratio was `O(eta)` uniformly in the scale separation.
Likewise the fast--slow return estimate quoted in the strong-scaling error
ledger cannot retain an `O_eta(b/N)` constant when its coefficient contains the
diverging factor (3.4).

Equivalently, keeping `P_high/N=O(1)` while enforcing fixed action would require

    lambda = O(1/N),                                      (3.7)

and hence

    eta=lambda b = O(b/N) -> 0,                            (3.8)

which destroys the required slow-variation condition `eta >> 1` for the low
purifier across the clean carrier.

## 4. Scoped incompatibility theorem

Within the present exact 2D3C purifier ansatz and the
`d_lambda=lambda d`, `kappa_lambda=kappa/lambda` rescaling, there is no
asymptotic sequence with `N/b -> infinity` satisfying all three properties:

1. **nontrivial clean-filter action**:

       S/N^2 >= c0 > 0;

2. **slow low purifier relative to the clean carrier**:

       eta=lambda b >= eta0 > 1;

3. **uniformly bounded fast-parent velocity/frequency ratio**:

       lambda sqrt(S) <= C0.

Indeed, 1 and 3 imply

    lambda N <= C0/sqrt(c0),                               (4.1)

while 2 implies

    lambda N >= eta0 N/b -> infinity,                     (4.2)

which is a contradiction.

This is an exact algebraic incompatibility of the current scaling requirements;
it is not a numerical observation.

## 5. Consequence for the live route

The exact 2D3C clocked channel remains valid, as do the finite-energy
localization and the carrier-level sequential Kelvin discriminator. What fails
is the claim that the already-written strong calibration `S~b^2`, together
with `N/b->infinity`, by itself bridges the two.

A genuine repair must change at least one load-bearing ingredient. The main
possibilities are:

* build a **long-lived low tail/plateau** whose integrated strain is `O(1)` even
  though the high parents operate on the `N^-2` clock;
* concatenate many weak clocked pulses while proving their total high-parent
  contamination remains summable;
* redesign the autonomous channel so its useful low output persists on the
  clean `b^-2` clock rather than the pump `N^-2` clock; or
* replace the slow-affine purifier consumer by a discriminator whose required
  integrated action tends to zero with `N/b` while retaining strict enough
  margins for recursive purification.

Merely increasing the instantaneous amplitude to `S~N^2` does not preserve the
existing clean-protection estimates because it produces the divergence
(3.4)--(3.6).

The first uncontrolled quantity is therefore again explicit: construct a
finite-energy purifier with **fixed nonzero integrated clean-band action** and
simultaneously controlled high-frequency return. Until that is done, the
clean-gate/purifier composition theorem is not closed.

No PLAN, canonical proof graph, manuscript, or formal status is promoted. Full
repository verification and independent audit are pending.
