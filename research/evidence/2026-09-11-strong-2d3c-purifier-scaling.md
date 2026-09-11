# Strong-strain scaling of one exact 2D3C purifier channel

Date: 2026-09-11. Repository input:
`itpplasma/navier@d373e872be540cc7ec2664fb5ced571622b47d2f`.

**Status: author scaling theorem for the already-proved exact 2D3C channel;
independent mathematical audit and novelty are undetermined.** This packet
checks that the autonomous purifier is not restricted to an order-one strain.
It can be scaled to a strain competitive with a clean carrier of wave number
`b`, while its exact scalar-ladder correction remains perturbative provided the
pump frequency `N` is asymptotically larger than `b`.

No two-clock finite-energy localization, recursive turnover, singular solution,
or `NS-R3` result is claimed.

## 1. Unit-strength channel recalled

For one transverse low pair `(kappa,d)`, the exact three-layer channel uses
high shear frequencies

    q_m=m N rho,       m=1,2,3,                            (1.1)

where `rho` is transverse to both `kappa` and `d`.  The paired scalar parents
are at

    p_m=kappa-q_m.                                        (1.2)

The exact gap is

    |p_m|^2+|q_m|^2-|kappa|^2=2m^2N^2.                   (1.3)

For a first-Picard low pulse of unit coefficient, the product of the two parent
scalar coefficients in each layer is proportional to

    N^2 w_m,                                               (1.4)

where `(w_1,w_2,w_3)` are the fixed tail-canceling weights.  A balanced choice
therefore has parent scalar coefficients of size `O(N)`.

The exact full 2D3C scalar ladder differs from its first-Picard low pulse by a
relative `O(N^-1)` amount on a fixed `N^-2` clock.

## 2. Arbitrary target low coefficient

Let

    S>0                                                    (2.1)

be the desired multiplier of the unit low pulse.  Multiply every parent
**product** in (1.4) by `S`.  With balanced factors, individual parent scalar
coefficients become

    O(N sqrt(S)).                                         (2.2)

The first low pulse is multiplied exactly by `S` because the quadratic source
is bilinear.

The scalar ladder is linear in the passive-scalar coefficients and its shift
operator is proportional to the shear coefficients.  On a fixed scaled time
interval `0<=t<=T/N^2`, the integrated shift size is now

    mu := integral |beta(t)| dt
       <= C_T sqrt(S)/N.                                  (2.3)

Thus the exact Duhamel/Neumann expansion which gave the unit-strength
`O(N^-1)` correction now gives

    relative full-ladder correction
       <= C_T sqrt(S)/N                                   (2.4)

whenever the right-hand side is sufficiently small.  More explicitly, the
remainder after the first low-producing interaction is bounded by the first
term times `exp(C mu)-1`.

Hence the exact channel remains asymptotically first-Picard accurate under the
single condition

    sqrt(S)/N ->0.                                        (2.5)

## 3. Gradient-preserving wavelength parameter

Use the internal rescaling

    d_lambda=lambda d,
    kappa_lambda=kappa/lambda.                             (3.1)

It preserves the rank-one gradient:

    d_lambda tensor kappa_lambda=d tensor kappa.          (3.2)

After the strength multiplication of Section 2, the intended low velocity has
size

    O(lambda S),                                          (3.3)

while its gradient has size

    O(S).                                                  (3.4)

The physical high-parent polarization vectors are multiplied by `lambda`, so
the high parent **velocity** scale is

    P_high=O(lambda N sqrt(S)).                            (3.5)

The exact scalar ladder parameter (2.3) is independent of `lambda`: the
rescaling changes the physical polarization but leaves the scalar shift
coefficient `b_lambda.k_(n,lambda)=1` exactly unchanged.

## 4. Calibration to a clean carrier

Let a clean gate operate at physical wave number

    b.                                                     (4.1)

To compete with its viscous/advective rate, the purifier strain should have
size

    S=M nu b^2                                            (4.2)

for a fixed dimensionless discrimination strength `M` (for example the
repository's explicit common-inheritance choice `M=2048`).  Constants `M,nu`
do not affect the scale conclusions below, so

    sqrt(S) comparable to b.                              (4.3)

Condition (2.5) becomes simply

    b/N ->0.                                               (4.4)

Thus a pump scale far above the clean carrier makes the strong exact channel
more, not less, accurately described by its intended low pulse.

The low purifier should vary slowly across the clean wave packet.  Write

    eta=lambda b.                                         (4.5)

Then the low purifier wave number satisfies

    |kappa_lambda|/b comparable to eta^-1.                (4.6)

Choosing one fixed large `eta` makes the rank-one sine field as slowly varying
relative to the clean carrier as required by the strict discrimination
margins, while (4.4) independently controls the nonlinear channel remainder.

With this choice,

    P_high comparable to eta N                            (4.7)

up to fixed `M,nu` constants.  The high pump is strong but has a fixed
velocity-to-frequency ratio `O(eta)`, precisely the regime covered by the
lifted Galilean scale-separation theorem when two purifier clocks are separated.

## 5. Strong finite-energy one-channel localization

The nested localization estimates can also be rescaled.  In `A=F L1`,

    ||U_channel||_A <= C P_high
       <= C lambda N sqrt(S).                             (5.1)

The linear cutoff commutators scale as

    C lambda N^2 sqrt(S)/L,                               (5.2)

while the nonlinear edge terms, each carrying one cutoff derivative after
nesting, scale as

    C P_high^2/L
      <= C lambda^2 N^2 S/L.                              (5.3)

For fixed

    eta=lambda sqrt(S),                                   (5.4)

the nonlinear term is only a fixed factor `O(eta)` larger than the linear
one.  On the `N^-2` clock the projected residual therefore has integrated
Wiener size

    O_eta(eta^2/L).                                       (5.5)

The linearized Volterra coefficient around the exact channel is

    sqrt(t)||U_channel||_A
      <= C eta,                                            (5.6)

which need not be small but is fixed.  The same finite-subinterval argument as
in the one-channel Wiener-shadowing packet gives a shadowing constant depending
on `eta,T` but not on `N,L`.  Consequently, for every fixed strong-filter
parameter `eta`, choosing

    L -> infinity                                         (5.7)

closes the finite-energy localization error of one strong rank-one channel.

This observation is important: the weak-velocity rescaling used for
simultaneous two-channel coexistence is **not** required after the sequential
reduction.  A single channel may be used at full clean-carrier strain.

## 6. Error ledger for one strong purifier pulse

For fixed `M,nu,eta,T`, one isolated rank-one pulse acting on a clean carrier
scale `b` has the following independent small parameters:

    exact 2D3C ladder error:          O(b/N),              (6.1)

    low heat over the pump clock:     O((b/N)^2),          (6.2)

    finite-energy localization:       O_eta(L^-1),         (6.3)

    high-parent conjugate return
      to a clean frequency:           O_eta(b/N),          (6.4)

where (6.4) is the fast--slow Leray-return estimate with
`|B|/|q|=O(eta)`.

All can be made small simultaneously by

    N/b -> infinity,
    L -> infinity.                                        (6.5)

For two sequential pulses, the additional clock-separation error is

    O_eta(N_2/N_1)                                        (6.6)

from the lifted Galilean theorem.

## 7. Remaining issue

There is now no amplitude-scale contradiction between

* a purifier slowly varying relative to the clean carrier,
* a strain strong enough to compete with clean dynamics,
* exact full-nonlinear 2D3C self-evolution,
* finite-energy localization of one channel, and
* temporal separation of two rank-one channels.

The remaining task is to put the **clean gate packets themselves** into the
same finite-energy two-clock history and prove that their retained spectral
windows experience the sequential purifier map while high-pump sidebands stay
outside those windows.  That is a multi-scale packet-composition theorem, not
an amplitude obstruction.

No PLAN, canonical proof graph, manuscript, or formal status is promoted. Full
repository verification and independent audit are pending. `NS-R3` remains
unresolved.