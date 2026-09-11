# Finite-energy Wiener shadowing of one exact 2D3C purifier channel

Date: 2026-09-11. Repository input:
`itpplasma/navier@7b6f2c5bb9a71485d7c08da6ffb923f0c4ec3ebe`.

**Status: author proof of one-channel finite-energy localization/shadowing;
independent mathematical audit and novelty undetermined.** This packet closes
the Leray-projection gap left by
`2026-09-11-nested-2d3c-localization.md` and constructs an actual unforced
finite-energy `R3` Navier--Stokes solution shadowing one strong clocked 2D3C
purifier channel for its complete `O(N^-2)` operating interval.

It does **not** compose the two minimal purifier channels, couple the purifier
to the clean dyadic gate, prove a regenerative turnover, construct a singular
solution, or prove `NS-R3`.

The key norm is the Wiener algebra

    A(R3)=F L1(R3),
    ||f||_A = integral_R3 |fhat(xi)| dxi                 (0.1)

(up to the fixed Fourier-normalization constant). In this norm:

* multiplication is bounded: `||fg||_A<=||f||_A||g||_A`;
* a scaled smooth cutoff has `A` norm independent of its scale;
* each cutoff derivative costs exactly one inverse localization scale;
* the Leray projector is a bounded Fourier multiplier of norm at most a fixed
  dimension constant; and
* the heat--Leray derivative obeys the exact scaling

      || exp(nu s Delta) P div F ||_A
          <= C (nu s)^(-1/2) ||F||_A.                    (0.2)

Those facts match the nested localization exactly and avoid the false obstacle
that `P` is not bounded on `L-infinity`.

## 1. Wiener algebra bookkeeping for scaled cutoffs

Let `chi in C_c^infinity(R)` and `chi_L(x)=chi(x/L)`. Then

    Fourier(chi_L)(xi)=L Fourier(chi)(L xi),               (1.1)

hence

    ||chi_L||_A=||chi||_A,                                (1.2)

and for every integer `r>=0`,

    ||partial_x^r chi_L||_A
      =L^(-r)||partial_x^r chi||_A.                       (1.3)

The same tensor-product statement holds for the three-dimensional product
cutoffs used in the nested construction.

If

    g(y)=sum_n g_n exp(i lambda_n y),
    sum_n |g_n|<infinity,                                 (1.4)

then multiplication by a compact scaled cutoff gives an `A(R)` function and

    ||chi_L g||_A
      <= ||chi||_A sum_n |g_n|.                           (1.5)

Frequency translation does not change the `L1` norm of the Fourier transform.
Thus the localization radius itself never creates a Wiener loss.

## 2. Channel Wiener bounds

Use the exact channel and potentials from the preceding packet:

    U_N=(v_N(y,t),0,w_N(x,y,t)),                           (2.1)

    partial_y psi_N=v_N,
    partial_x q_N=w_N.                                    (2.2)

For the three shear modes,

    ||v_N||_(periodic A) <= C N,
    ||partial_y v_N||_(periodic A) <= C N^2,
    ||psi_N||_(periodic A) <= C.                          (2.3)

For the scalar ladder, let `z_n(t)` be the coefficient at `(K,nN,0)`. The
exact shift system gives on every fixed scaled horizon `0<=t<=T/N^2`

    sum_n |z_n(t)| <= C N,
    sum_n (1+|n|)|z_n(t)| <= C N.                         (2.4)

The proof is the same `ell1`/first-moment Gronwall argument already recorded in
the nested packet. Therefore

    ||q_N||_(periodic A)
      +||partial_x q_N||_(periodic A) <= C N,

    ||partial_y q_N||_(periodic A)
      +||partial_x partial_y q_N||_(periodic A) <= C N^2. (2.5)

All constants depend on the fixed channel parameters, `nu,T,K`, but not on
`N,L`.

## 3. Nested field and its Wiener size

Use exactly the nested divergence-free potentials

    Phi_L=a_L(x)b_L(y)c_L(z) psi_N(y,t),                  (3.1)

    Theta_L=d_L(x)e_L(y)f_L(z) q_N(x,y,t),                (3.2)

with the outer cutoffs identically one on a neighborhood of the complete inner
support. Put

    V_L=curl(0,0,Phi_L),
    W_L=curl(0,Theta_L,0),
    U_(N,L)=V_L+W_L.                                      (3.3)

By (1.2)--(1.5) and (2.3)--(2.5),

    sup_(0<=t<=T/N^2) ||U_(N,L)(t)||_A <= C N.            (3.4)

The field is real, smooth, compactly supported, and exactly solenoidal.

## 4. The raw residual has the same `N^2/L` Wiener gain

Define

    R_(N,L)=partial_t U_(N,L)-nu Delta U_(N,L)
              +(U_(N,L).grad)U_(N,L).                    (4.1)

The preceding packet gave the exact residual formulas. Every surviving term
contains at least one derivative of an inner or outer cutoff. The dangerous
term with no cutoff derivative was removed exactly by nesting.

The same term-by-term proof works in `A`, because it is a Banach algebra and
(1.3) records the cutoff derivative exactly. For example the inner linear
error is

    curl(0,E_i,0),                                        (4.2)

    E_i=-nu[2 grad chi_i.grad q_N+q_N Delta chi_i]
          +v_N(partial_x chi_i)q_N,                       (4.3)

and the final curl differentiates only in `x,z`, never in the high `y`
direction. Equations (1.3), (2.3), and (2.5) give

    ||curl(0,E_i,0)||_A <= C N^2/L.                       (4.4)

The inner self-interaction, outer heat commutator, and outer shear
self-interaction obey the identical scale. Hence

    sup_(0<=t<=T/N^2) ||R_(N,L)(t)||_A
       <= C N^2/L.                                        (4.5)

This is stronger than the previous `L-infinity` estimate because it survives
order-zero Fourier multipliers.

## 5. Leray projection closes with no loss

For `xi!=0`,

    P(xi)=I-xi tensor xi/|xi|^2                            (5.1)

is an orthogonal projection. Define its value at `xi=0` arbitrarily; one point
is irrelevant to the Fourier integral. Therefore

    ||P f||_A <= C ||f||_A                                (5.2)

for vector fields, with only the harmless fixed matrix-norm convention in
`C`.

Because `U_(N,L)` is divergence free,

    F_(N,L)
      :=partial_t U_(N,L)-nu Delta U_(N,L)
        +P div(U_(N,L) tensor U_(N,L))
      =P R_(N,L).                                         (5.3)

Combining (4.5) and (5.2),

    sup_(0<=t<=T/N^2) ||F_(N,L)(t)||_A
       <= C N^2/L.                                        (5.4)

Thus the full projected Navier--Stokes residual is small by one complete power
of the localization scale. There is no Calderon--Zygmund or logarithmic loss
in the Wiener norm.

## 6. Heat--Leray bilinear estimate in `A`

For a tensor field `G`, Fourier multiplication gives

    | exp(-nu s|xi|^2) P(xi) i xi . Ghat(xi) |
      <= C |xi| exp(-nu s|xi|^2)|Ghat(xi)|.               (6.1)

Since

    sup_(r>=0) r exp(-nu s r^2)
       =(2 e nu s)^(-1/2),                                (6.2)

we have

    || exp(nu s Delta) P div G ||_A
       <= C (nu s)^(-1/2)||G||_A.                         (6.3)

Together with the Banach-algebra inequality this is the only nonlinear
estimate needed below.

## 7. Exact unforced shadowing theorem

Let `u_(N,L)` be sought as

    u_(N,L)=U_(N,L)+r_(N,L),                              (7.1)

with the same initial datum,

    r_(N,L)(0)=0.                                         (7.2)

Then `u_(N,L)` solves the original unforced projected Navier--Stokes equation
iff `r=r_(N,L)` solves

    r(t)=-integral_0^t exp(nu(t-s)Delta) F_(N,L)(s) ds

         -integral_0^t exp(nu(t-s)Delta) P div[
             U_(N,L) tensor r+r tensor U_(N,L)+r tensor r] ds.   (7.3)

Fix `T<infinity` and introduce scaled time

    tau=N^2 t.                                             (7.4)

Let

    E(tau)=||r(tau/N^2)||_A.                               (7.5)

From (3.4), (5.4), and (6.3),

    E(tau)
      <= C tau/L
        +C integral_0^tau (tau-sigma)^(-1/2) E(sigma) d sigma
        +(C/N) integral_0^tau
             (tau-sigma)^(-1/2) E(sigma)^2 d sigma.        (7.6)

All constants are independent of `N,L`.

To close (7.6) without hiding a long-time existence assumption, partition
`[0,T]` into finitely many intervals of length `delta`, where `delta>0` is
chosen so that the linear Volterra norm on one interval is smaller than
`1/4`. On one such interval the heat semigroup is contractive in `A`; the
forcing contributes at most `C delta/L`; and, under the bootstrap `E<=1`, the
quadratic term is bounded by the same Volterra kernel times `E` for `N>=1`.
Thus the mild map is a contraction after the usual ball enlargement.
Iterating over the finite number `ceil(T/delta)` of intervals gives

    sup_(0<=t<=T/N^2)
      ||r_(N,L)(t)||_A <= C_T/L                            (7.7)

provided `L>=L_0(T)`; increasing `L_0` closes the `E<=1` bootstrap. The same
iteration constructs the solution on the whole interval, so (7.7) is not a
conditional estimate assuming prior existence.

The initial datum

    u_(N,L)(0)=U_(N,L)(0)                                 (7.8)

is real, compactly supported, smooth, and solenoidal, hence belongs to
`S_sigma(R3;R3)`. Parabolic smoothing and the smooth initial datum upgrade the
mild solution to the classical branch on the displayed interval.

Therefore:

**Theorem (one-channel finite-energy shadowing).** For every fixed
`nu>0`, fixed exact three-layer 2D3C purifier channel and fixed scaled horizon
`T`, there are constants `C_T,L_0(T)` such that for every `N>=1` and
`L>=L_0(T)`, one compactly supported Schwartz datum generates an original
unforced `R3` Navier--Stokes solution on `0<=t<=T/N^2` satisfying

    sup_t ||u_(N,L)(t)-U_(N,L)(t)||_A <= C_T/L.            (7.9)

In particular

    sup_t ||u_(N,L)(t)-U_(N,L)(t)||_infinity <= C_T/L.    (7.10)

This is a finite-energy theorem for one complete strong purifier channel, not
merely an initial pressure estimate or second-Picard calculation.

## 8. Preservation of the low purifier output

Choose a fixed smooth low-frequency multiplier `Pi_low` which equals one on a
small neighborhood of the desired low child `+/-K e_1` and vanishes on every
high parent/sideband center for all sufficiently large `N`.

From (7.7),

    ||grad Pi_low [u_(N,L)-U_(N,L)]||_infinity
       <= C_(Pi,T)/L.                                     (8.1)

Indeed `|xi|` is bounded on the fixed support of `Pi_low`.

For the approximate field itself, multiplying a periodic channel by a smooth
cutoff of scale `L` convolves each discrete frequency with a Fourier profile of
width `O(L^-1)`. Since the cutoffs are `C_c^infinity`, their Fourier transforms
are Schwartz. Hence:

* the fixed low child passes through `Pi_low` with error `O_M(L^-M)` for every
  `M` after choosing the multiplier equal to one on a fixed neighborhood of
  that child;
* every high center at distance `comparable to N` leaks into the fixed low band
  by `O_M((NL)^-M)` times its polynomial channel amplitude.

Consequently the low purifier strain of the actual finite-energy solution
agrees with the exact 2D3C low pulse by

    O_T(L^-1)+O_M(L^-M)+O_M(N^C (NL)^-M),                 (8.2)

and therefore converges to the exact pulse as `L->infinity`, uniformly on the
scaled operating interval.

## 9. What blocker remains now

The single-channel finite-energy localization problem from
`2026-09-11-exact-2d3c-clocked-channel.md` is therefore closed at author-proof
level. The pressure tail is not the surviving obstruction.

The live obstruction moves to the next item already isolated by the two-shear
reduction:

1. construct **both** minimal transverse purifier channels in one Schwartz
   datum;
2. control their mutual cross interactions over the common `N^-2` clock;
3. retain the intended symmetric strain while keeping the antisymmetric
   rotation explicitly;
4. then couple that finite-energy two-channel pulse to the contaminated clean
   dyadic gate and test the supercritical stage map.

The natural next discriminator is frequency and/or spatial separation of the
two exact channels. If their cross terms can be made `o(1)` in the same Wiener
framework, the purifier becomes a genuine finite-energy module. If not, the
first non-decaying cross term is the next precise obstruction.

No PLAN, canonical proof graph, manuscript, or formal status is promoted here.
Independent mathematical audit is pending. `NS-R3` remains unresolved.