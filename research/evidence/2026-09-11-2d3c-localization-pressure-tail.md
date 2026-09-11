# First finite-energy localization test for the exact 2D3C pump channel

Date: 2026-09-11. Repository input:
`itpplasma/navier@716ef3ec3bd6ea7e0dd9138563ba5f0851399fb4`.

**Status: scoped author localization lemma at the initial time; independent
audit and novelty undetermined.** The exact clocked 2D3C channel is
translation invariant in one direction and therefore has infinite energy on
`R3`. This packet tests the first obstruction to cutting it off: the canonical
whole-space pressure is nonlocal and reacts instantly to the localization
edge.

The result is positive but deliberately narrow. A compact solenoidal
curl-localization can agree exactly with the channel in a ball of radius `L`,
and the resulting pressure-gradient error in a fixed fraction of that core is
only

    O(N^2/L),                                               (0.1)

where the channel velocity scale is `O(N)`. On the pump clock
`t comparable to N^(-2)`, this is only an `O(1/L)` first-order velocity error.
Thus nonlocal pressure does **not** create an order-one instantaneous
localization obstruction.

No finite-time localized shadowing theorem is proved here. Propagating this
bound through the complete `N^(-2)` pulse interval is the next analytic step.

## 1. Initial exact channel and bounded vector potential

Let `U_N` denote one of the exact three-layer 2D3C initial fields from
`2026-09-11-exact-2d3c-clocked-channel.md`, with pump frequency `N` and the
strong pulse normalization. It is a finite trigonometric sum whose nonzero
frequencies have magnitude comparable to `N` and whose velocity coefficients
have magnitude `O(N)`.

Consequently one can choose a trigonometric vector potential `A_N` satisfying

    curl A_N=U_N                                           (1.1)

with

    ||A_N||_(L^infinity) <= C,                             (1.2)

uniformly in large `N`: each Fourier coefficient of the vector potential gains
one inverse frequency relative to its velocity coefficient.

The exact 2D3C convective term has only the passive-scalar component and is
divergence free. Hence its canonical pressure may be normalized to zero:

    div div(U_N tensor U_N)=0.                             (1.3)

This identity is pointwise, not a cancellation after spatial integration.

## 2. Compact solenoidal curl localization

Choose a fixed smooth radial cutoff `chi` such that

    chi=1 on B_1,
    supp chi subset B_2,                                  (2.1)

and put

    chi_L(x)=chi(x/L).                                    (2.2)

Define

    u_(N,L)(x)=curl[chi_L(x) A_N(x)].                     (2.3)

Then `u_(N,L)` is smooth, compactly supported and exactly solenoidal. Moreover

    u_(N,L)=U_N       on B_L,                              (2.4)

and

    supp u_(N,L) subset B_(2L).                           (2.5)

Using (1.2),

    u_(N,L)=chi_L U_N + grad chi_L cross A_N,              (2.6)

so

    ||u_(N,L)||_infinity <= C(N+L^(-1)).                  (2.7)

For `L>=1` this is `O(N)`, the same amplitude order as the unlocalized pump.
Thus the divergence correction does not introduce a larger velocity scale.

## 3. Pressure comparison in the core

Let `p_(N,L)` be the canonical whole-space pressure of the compact datum,

    -Delta p_(N,L)
      = partial_i partial_j
          [u_(N,L),i u_(N,L),j].                          (3.1)

The pressure gradient may be written using the third derivative of the Newton
potential,

    grad p_(N,L)(x)
      = integral_R3 K(x-y) :
          [u_(N,L) tensor u_(N,L)](y) dy,                 (3.2)

where

    |K(z)| <= C |z|^(-4).                                 (3.3)

For the exact channel, (1.3) implies that the same singular-integral pressure
gradient is zero. Therefore, for points `|x|<=L/2`, subtract the exact channel
tensor and write

    grad p_(N,L)(x)
      = integral K(x-y) :
          [u_(N,L) tensor u_(N,L)
           -U_N tensor U_N](y) dy.                        (3.4)

The tensor difference vanishes identically on `B_L` by (2.4). Outside `B_L`,
both tensors are bounded by `C N^2` for `L>=1`. Although `U_N` is not
integrable at infinity, this difference representation is absolutely
convergent because the kernel tail `|z|^(-4)` is integrable in three dimensions.
Thus

    |grad p_(N,L)(x)|
      <= C N^2 integral_(|y|>=L/2) |y|^(-4) dy
      <= C N^2/L,                                        (3.5)

uniformly for

    |x|<=L/2.                                              (3.6)

This is the claimed pressure-tail estimate.

The argument uses the exact zero-pressure structure of the 2D3C channel. A
generic infinite-energy comparison field would not permit the same clean
subtraction.

## 4. Initial acceleration error on the pump clock

At every point in `B_L`, the localized datum and exact channel agree together
with all spatial derivatives. Hence at `t=0` the viscous term and local
convective term agree exactly in the core. The only difference between their
instantaneous accelerations there is the nonlocal pressure gradient.

Therefore, for `|x|<=L/2`,

    |partial_t u_(N,L)(0,x)-partial_t U_N(0,x)|
      <= C N^2/L.                                        (4.1)

The clocked channel acts on

    Delta t_N comparable to 1/(nu N^2).                   (4.2)

Multiplying (4.1) by this clock gives the first-order calibration

    Delta t_N
      |partial_t u_(N,L)-partial_t U_N|_(t=0)
      <= C_nu/L.                                          (4.3)

Thus one may take `L` large independently, or for example `L=N^alpha` with any
`alpha>0`, to make the instantaneous pressure contamination vanish.

This does **not** prove that the error remains `O(1/L)` for all
`0<t<c/N^2`; (4.3) is only the correct initial scaling.

## 5. Linear diffusion from the edge is even smaller

There is no comparable linear-heat obstruction on the short pump clock. The
localization edge is a distance comparable to `L` from the inner core. A
Gaussian heat kernel crossing that distance in time `t<=c/N^2` carries the
factor

    exp[-c' L^2/(nu t)]
      <= exp[-c'' N^2 L^2].                               (5.1)

Thus direct heat import from the cutoff annulus is super-algebraically smaller
than (3.5). The load-bearing propagation mechanism is the nonlinear/nonlocal
pressure coupling, not ordinary diffusion.

## 6. What is now required for an R3 pulse theorem

The exact channel plus (3.5) suggests a concrete bootstrap target. Let
`U_N(t)` be the exact 2D3C pulse and let `u_(N,L)(t)` be the compact whole-space
solution from (2.3). Prove on a fixed inner ball and for

    0<=t<=c/(nu N^2)                                      (6.1)

an estimate of the schematic form

    ||u_(N,L)(t)-U_N(t)||_(local)
      <= C [L^(-1)+N^(-1)+exp(-cN^2L^2)],                 (6.2)

with enough derivatives to preserve the low-child strain observation. The
`N^(-1)` term is the already proved exact scalar-ladder remainder of the
clocked channel; the new localization contribution should be the `L^(-1)`
term.

A proof needs a local high-regularity energy estimate coupled to a split
pressure representation: near-field differences handled by the bootstrap and
far-field stress handled by the integrable `|x-y|^(-4)` tail. The short clock
and the exact core equality at `t=0` are the two available small parameters.

If such a bootstrap closes, one obtains a genuine finite-energy Schwartz
approximation of **one** strong purifier channel on its complete operating
interval. The remaining problem would then be coexistence of the two minimal
channels and their action on the clean target triple.

If it does not close, the first term in the local error inequality that loses a
power of `L` or `N` should be recorded as the exact localization obstruction.

No finite-time R3 shadowing theorem, recursive turnover, or singular solution
is claimed in this packet. `NS-R3` remains unresolved.
