# Long-tail purifier repair of the clock-action obstruction

Date: 2026-09-11. Repository input:
`itpplasma/navier@10588b702fed78078235875b208e7f74f94c4486`.

**Status: author proof for one exact 2D3C rank-one purifier channel, including
strong clean-scale calibration and a finite-energy long-clock Wiener-shadowing
extension. Independent mathematical audit and novelty are undetermined.**

This note changes one load-bearing design choice in the clocked purifier. The
three-layer pulse deliberately canceled the slow low-frequency heat tail. That
made switch-off easy, but forced all useful Kelvin action into the pump clock
`N^-2`, leading to the exact incompatibility in
`2026-09-11-strong-purifier-clock-action-obstruction.md`.

Here the slow low tail is retained on purpose. Two pump layers cancel the
instantaneous low source, so the output still has quadratic onset, but they do
**not** cancel the slow low heat tail. The resulting selected low strain builds
on the fast pump clock and then persists on the clean `b^-2` clock. Under the
strong calibration `S=M nu b^2`, `lambda b=eta`, this gives fixed nonzero
integrated clean-band action while the high-parent velocity/frequency ratio
stays bounded and the exact 2D3C ladder error remains `O(b/N)`.

The exact algebra is frozen by `research/check_long_tail_purifier.py`.
No clean-gate stage map, regenerative turnover, finite-time singularity, or
`NS-R3` theorem is claimed.

## 1. Two layers: quadratic onset but nonzero slow tail

Use the exact 2D3C channel of
`2026-09-11-exact-2d3c-clocked-channel.md` for one transverse low pair
`(kappa,d)`. Let the two shear layers have frequencies `N rho` and `2N rho`, so
the parent-product heat gaps are

    D, 4D,          D=2 N^2                              (1.1)

in the normal-form normalization. Let their source products be

    c_1=c,          c_2=-c.                               (1.2)

The instantaneous low source cancels exactly:

    c_1+c_2=0.                                             (1.3)

The first shear interaction at the low child is

    F_tail(t)
      = c/(nu D) exp(-nu |kappa|^2 t) B(x),               (1.4)

    x=nu D t,                                              (1.5)

with

    B(x)=3/4-exp(-x)+(1/4)exp(-4x).                       (1.6)

Put `z=exp(-x)`. Then

    B=(1/4)(1-z)^2(z^2+2z+3).                             (1.7)

Hence `B(x)>0` for every `x>0`. Moreover

    B'(x)=exp(-4x)(exp(3x)-1)>0,                          (1.8)

    B(x)=(3/2)x^2-(5/2)x^3+O(x^4),                       (1.9)

and

    B(x) -> 3/4.                                           (1.10)

Thus the low mode is born quadratically, has no sign reversal, and converges
monotonically to a nonzero slow heat tail. This is the exact complement of the
old `(5,-32,27)` choice: (1.3) keeps the delayed onset, while the missing second
cancellation is precisely what retains useful long action.

For a desired asymptotic low scalar coefficient `S`, choose

    c=(4/3) nu D S.                                       (1.11)

Then

    F_tail(t)
      = S exp(-nu |kappa|^2 t) (4/3)B(nu D t),            (1.12)

whose fast-clock factor tends to one.

## 2. Exact full 2D3C control survives at strong amplitude

Balance the two factors in each parent product. Since `|c|=O(S N^2)`, the
scalar parent coefficients are

    O(N sqrt(S)).                                         (2.1)

The exact 2D3C passive-scalar ladder is unchanged except that only two shear
harmonics are used. Its integrated shift size obeys

    mu <= C sqrt(S)/N.                                    (2.2)

The Duhamel series therefore gives, on every fixed clean-clock interval as long
as `sqrt(S)/N` is small,

    full ladder = heat + first shear interaction
                  + relative O(sqrt(S)/N).                (2.3)

In particular the selected low tail has relative error

    O(sqrt(S)/N).                                         (2.4)

This estimate is uniform beyond the pump interval: the time integral of the
shear operator is finite and already saturated on the `N^-2` clock.

## 3. Strong clean-scale calibration has no clock-action contradiction

Use the gradient-preserving internal rescaling

    d -> d_lambda=lambda d,
    kappa -> kappa_lambda=kappa/lambda,                   (3.1)

and let the clean carrier scale be `b`. Fix

    S=M nu b^2,
    lambda=eta/b,                                         (3.2)

where `M,nu,eta>0` are fixed and `eta` is the required affine-separation
parameter.

The low tail has velocity size

    lambda S = O_eta(b)                                   (3.3)

and gradient size `O(S)=O(b^2)`. The physical high-parent velocity scale is

    P_high=O(lambda N sqrt(S)),                           (3.4)

so

    P_high/N=O(lambda sqrt(S))
            =O(eta sqrt(M nu)),                           (3.5)

independent of both `b` and `N`. Meanwhile the exact-ladder parameter is

    sqrt(S)/N = sqrt(M nu) b/N.                           (3.6)

Thus `N/b -> infinity` simultaneously makes the exact channel accurate and
keeps the fast lifted data in the bounded velocity/frequency regime. The old
three-way contradiction

    S/N^2 >= c0,
    lambda b >= eta0,
    lambda sqrt(S) <= C0                                  (3.7)

is simply not the relevant scaling for this repair: useful action no longer
has to be accumulated during `N^-2`.

## 4. Fixed nonzero action is accumulated on the clean clock

Let `kappa_0` denote the unscaled low wave number magnitude, so

    |kappa_lambda|=kappa_0 b/eta.                         (4.1)

Over a clean interval

    0<=t<=tau/b^2,                                        (4.2)

ignore for the moment the fast build factor `(4/3)B`; its deviation from one is
confined to `O(N^-2)` and contributes only `O((b/N)^2)` to the normalized
action.

The principal integrated low strain is exactly

    I_b
      = integral_0^(tau/b^2)
          S exp(-nu |kappa_lambda|^2 t) dt

      = (M eta^2/kappa_0^2)
          [1-exp(-nu kappa_0^2 tau/eta^2)].               (4.3)

It is independent of `b` and strictly positive for every `tau>0`. For small
`tau` it is linear in `tau`, as required by the finite-duration Kelvin
consumer. The fast build window contributes at scale

    S N^-2 = M nu (b/N)^2,                                (4.4)

which vanishes under `N/b -> infinity`.

Therefore the exact 2D3C module now has the quantity missing in the obstruction
note: nonzero integrated clean-band action with a bounded fast-parent ratio.

## 5. Finite-energy localization survives for the longer `b^-2` clock

The previous Wiener shadowing theorem was written only for a tail-canceling
`N^-2` pulse. The same nested localization extends to the long-tail channel by
splitting the estimates into the fast pump part and the low tail part.

Let `U_(b,N,L)` be the nested compact divergence-free localization of the
strong two-layer channel, using the same outer-shear and inner-scalar vector
potentials as in `2026-09-11-wiener-2d3c-shadowing.md`. On
`0<=t<=T/b^2`, the exact ladder decomposition and (2.3) give the Wiener-size
schematic bound

    ||U_(b,N,L)(t)||_A
      <= C_eta,T [
          N exp(-c N^2 t)
          + b exp(-c' b^2 t)
          + b^2/N],                                      (5.1)

where fixed `M,nu,kappa_0` are absorbed into the constants. The three terms are
respectively the fast parents/sidebands, the intended low tail, and the
higher-ladder remainder.

Every term in the exact nested localization residual contains at least one
cutoff derivative. Applying the same Wiener algebra bookkeeping term by term,
with the high and low pieces of (5.1) separated, yields

    ||F_(b,N,L)(t)||_A
      <= C_eta,T/L [
          N^2 exp(-c N^2 t)
          + b^2 exp(-c' b^2 t)
          + b^2 (b/N)],                                  (5.2)

up to harmless faster-decaying mixed terms such as `Nb exp(-cN^2t)`. Hence

    integral_0^(T/b^2) ||F_(b,N,L)(t)||_A dt
      <= C_eta,T/L [1+O(b/N)].                            (5.3)

For the correction `r=u-U`, the heat--Leray bilinear kernel is controlled by

    sup_(t<=T/b^2)
      integral_0^t (t-s)^(-1/2)||U(s)||_A ds
      <= C_eta,T [1+O(b/N)].                              (5.4)

Indeed the fast term contributes `O_eta(1)` on its own `N^-2` interval and
`O_eta(b/N)` once observed on the clean clock; the low term contributes
`O_eta(b sqrt(t))=O_eta,T(1)`; and the ladder remainder contributes
`O_eta,T(b/N)`.

The same finite-subinterval Volterra contraction used in the existing Wiener
shadowing proof therefore gives, for `N/b` sufficiently large and
`L>=L_0(eta,T)`, an actual original unforced classical solution with the same
compact-Schwartz initial datum and

    sup_(0<=t<=T/b^2) ||u(t)-U_(b,N,L)(t)||_A
      <= C_eta,T/L.                                       (5.5)

This is a long-clock estimate: the correction remains controlled after the
high pumps have died and throughout the useful low-tail interval.

For a smooth selected low-band projector `Pi_low` centered at
`+/-kappa_lambda`, its support has frequency `O(b)`, so

    ||grad Pi_low (u-U)||_infinity
      <= C b/L.                                           (5.6)

Relative to the intended `O(b^2)` strain this is `O((bL)^-1)`, and its
integrated action error is `O((bL)^-1)` on the clean clock. High-center leakage
into `Pi_low` is superalgebraic in the frequency moat exactly as in the
existing localization packet. Thus choosing

    N/b -> infinity,
    bL -> infinity                                        (5.7)

preserves the nonzero action (4.3) in one finite-energy Schwartz solution.

## 6. High-frequency return remains controlled at the pump stage

The high parent amplitudes in (3.4) are the same order as in the old strong
pulse calibration. Therefore every exact fast--slow Leray-return estimate whose
constant depends on the bounded ratio `P_high/N=O_eta(1)` retains its previous
small parameter

    O_eta(b/N).                                           (6.1)

The only design change is the coefficient of the selected low child after the
fast parents have decayed. No high parent is strengthened to `S~N^2`; hence the
divergence isolated by the clock-action obstruction is absent.

Equation (6.1) is a statement about the already-analyzed return channel during
the pump stage. A complete nonlinear clean-gate/purifier composition theorem is
still required before recursive use.

## 7. Scoped repair theorem

**Theorem (one-channel finite-energy long-tail purifier).** Fix `nu>0`, a
rank-one transverse purifier geometry, `M,eta,T>0`, and let `b->infinity` with
`N/b->infinity`. Use `S=M nu b^2`, `lambda=eta/b`, the two-layer source products
`c,-c` calibrated by (1.11), and nested localization scale `L` with
`bL->infinity`. Then one compactly supported smooth solenoidal datum generates
an original unforced `R3` Navier--Stokes solution on `0<=t<=T/b^2` such that:

1. the selected low purifier gradient has quadratic fast onset and converges,
   after the `N^-2` build layer, to the intended rank-one strong tail with
   relative error `O(b/N)+O((bL)^-1)`;
2. its integrated selected-band strain on every fixed clean subinterval has a
   strictly positive `b`-independent limit given by (4.3);
3. the fast-parent velocity/frequency ratio is uniformly bounded; and
4. the previously proved high-parent return coefficient remains
   `O_eta(b/N)`.

This repairs the **scaling incompatibility** of the tail-canceling strong pulse.
It does not yet prove that two rank-one tails and the clean gate coexist in one
recursive stage.

## 8. Recomputed frontier

The first blocker is no longer “obtain fixed action from an `N^-2` purifier
without unbounded fast-parent ratio.” One exact mechanism now does so.

The next discriminating problem is a combined-history question:

* preload two long-tail rank-one channels on separated fast clocks;
* prove that the first generated low tail distorts the later fast channel only
  by `O((b/N_2)^2)` action plus the existing fast/slow return errors;
* after the second build, obtain a common low tail whose symmetric gradient is
  the required `H` for a clean `b^-2` interval; and
* then test the actual contaminated clean-gate stage map against that common
  tail, with all high sidebands included.

If the two-tail composition fails, the first non-summable cross term is the
next obstruction. Another isolated one-channel purifier calculation would not
advance the terminal route.

No PLAN, canonical proof graph, manuscript, or formal status is promoted by
this note. `NS-R3` remains unresolved.
