# Gradient-preserving weak-velocity rescaling of the 2D3C purifier channel

Date: 2026-09-11. Repository input:
`itpplasma/navier@d825f3576c53e5d97f0422843a40dac80f2b445f`.

**Status: exact author scaling theorem; independent mathematical audit and
novelty undetermined.** This packet exposes a free parameter in the exact 2D3C
purifier construction which is useful specifically for the remaining
**two-channel coexistence** problem. It does not yet prove coexistence or a
recursive turnover.

For one transverse low child `(kappa,d)` with `kappa.d=0`, the local purifier
gradient is the rank-one tensor

    2 d tensor kappa.                                      (0.1)

For every `lambda>0`, replace

    d_lambda=lambda d,
    kappa_lambda=kappa/lambda.                             (0.2)

Then

    2 d_lambda tensor kappa_lambda
      =2 d tensor kappa                                   (0.3)

exactly. The low velocity can therefore be made arbitrarily small while its
local gradient is held fixed.

The less obvious fact is that the complete three-layer 2D3C pump architecture
and its viscous clock survive this rescaling without change.

## 1. Exact rescaled pump geometry

Let

    r=kappa cross d,
    rhat=r/|r|.                                             (1.1)

The cross product is invariant under (0.2):

    kappa_lambda cross d_lambda=r.                         (1.2)

For layers `m=1,2,3`, keep the high shear carriers

    q_m=m N rhat                                           (1.3)

unchanged and put

    p_(m,lambda)=kappa_lambda-q_m.                         (1.4)

Choose the rescaled polarizations

    a_lambda=d_lambda=lambda d,                            (1.5)

    b_lambda=kappa_lambda/|kappa_lambda|^2
             =lambda kappa/|kappa|^2.                     (1.6)

Then exactly

    a_lambda.p_(m,lambda)=a_lambda.q_m=0,                 (1.7)

    b_lambda.q_m=0,
    b_lambda.p_(m,lambda)=1.                               (1.8)

Hence the original Leray pair remains

    C(p_(m,lambda),a_lambda;q_m,b_lambda)=a_lambda.        (1.9)

The whole low child is simply multiplied by `lambda`; its gradient is unchanged
because its wavevector is multiplied by `lambda^-1`.

## 2. The `1:4:9` viscous clock is exactly invariant

Since `q_m` is perpendicular to `kappa_lambda`,

    |p_(m,lambda)|^2
      =|kappa_lambda|^2+m^2 N^2.                           (2.1)

Therefore the heat-decay gap is

    D_m
      =|p_(m,lambda)|^2+|q_m|^2-|kappa_lambda|^2
      =2 m^2 N^2.                                         (2.2)

It is completely independent of `lambda`. Thus the three-layer clocked pulse
retains the same `1:4:9` gaps and the same operating time `t=O(N^-2)`.

## 3. The exact scalar ladder is unchanged at coefficient level

The scalar ladder frequencies are

    k_(n,lambda)=kappa_lambda+n N rhat.                    (3.1)

Equation (1.6) gives

    b_lambda.k_(n,lambda)=1                               (3.2)

for every integer `n`. Consequently the exact ladder equation for the scalar
coefficients is **identical** to the unscaled one:

    z_n'+nu |k_(n,lambda)|^2 z_n
      =-i sum_(m=1)^3 [beta_m z_(n-m)
                       +conjugate(beta_m)z_(n+m)].         (3.3)

Only the harmless diagonal low heat factor changes through
`|kappa_lambda|^2`; on the pulse clock it is negligible whenever

    |kappa_lambda|/N -> 0.                                 (3.4)

The shift coefficients, nonlinear Duhamel parameter, and `O(1/N)` ladder
remainder are unchanged.

## 4. Weak velocity with fixed strain

Keep the scalar coefficients `x_m,beta_m` used in the strong pulse unchanged.
Both physical parent polarization vectors are multiplied by `lambda`, so

    parent velocity scale = O(lambda N).                  (4.1)

The generated low velocity is

    low velocity scale = O(lambda),                       (4.2)

while

    low gradient scale
      = O(lambda |kappa_lambda|)=O(1).                    (4.3)

Thus the purifier can have a fixed order-one local strain while its complete
velocity field becomes weak.

This is not Navier--Stokes scaling; viscosity and the high pump frequency `N`
are unchanged. It is an internal geometry rescaling of the transverse low
mode.

## 5. Power-law choice useful for two-channel coexistence

Take

    lambda=N^(-alpha),       0<alpha<1.                   (5.1)

Then

    |kappa_lambda|=O(N^alpha)=o(N),                       (5.2)

so the low carrier remains spectrally separated from the `O(N)` pumps, while

    ||U_channel||_A=O(N^(1-alpha)).                        (5.3)

On the `N^-2` clock the usual Wiener bilinear size becomes

    ||U_channel||_A sqrt(t)
      =O(N^(-alpha)).                                      (5.4)

Hence one channel becomes perturbatively weak as a velocity field even though
its target strain stays fixed.

For two such channels, the first cross-family stress has Wiener size

    O(lambda^2 N^2),                                      (5.5)

and one heat--Leray Duhamel integration over `t=O(N^-2)` gives the high
cross-family velocity scale

    O(lambda^2 N)=O(N^(1-2alpha)).                        (5.6)

Therefore the first global cross correction tends to zero whenever

    alpha>1/2.                                             (5.7)

The interval

    1/2<alpha<1                                            (5.8)

simultaneously gives weak cross dynamics and strict low/high spectral
separation.

## 6. Low-gradient accuracy survives the rescaling

The exact one-channel nonlinear remainder has scalar coefficient
`O(1/N)`. Its physical low velocity remainder is therefore

    O(lambda/N).                                          (6.1)

Multiplication by the low wavevector `|kappa_lambda|=O(lambda^-1)` gives

    low-gradient remainder = O(1/N),                      (6.2)

independent of `lambda`.

Thus weakening the channel does not weaken the accuracy of its intended local
strain.

## 7. Consequence for the live blocker

The two minimal purifier channels from
`2026-09-11-two-shear-purifier-reduction.md` may both be rescaled by the same
`lambda=N^-alpha`, `1/2<alpha<1`:

* their two rank-one gradients still sum to the exact full gradient `G` whose
  symmetric part is the required purifier `H`;
* their pulse clocks remain synchronized because both use the same `N` and the
  same gaps `2m^2N^2`;
* each physical channel is weak in velocity;
* the first cross-family correction is `o(1)` globally in Wiener norm.

The remaining point is **frequency-selective** rather than global existence:
the desired low velocities are only `O(lambda)`, so the coarse global cross
error (5.6) can still exceed them. One must prove that the first cross-family
outputs live in the high spectral region and that returning to either target
low band costs one additional interaction, giving a vanishing target-strain
error. That is the next calculation.

No PLAN, canonical proof graph, manuscript, or formal status is promoted by
this packet. `NS-R3` remains unresolved.