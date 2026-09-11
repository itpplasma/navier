# Fast--slow Leray return cancellation and scale-separated purifier scheduling

Date: 2026-09-11. Repository input:
`itpplasma/navier@d70c74c0256d25758d25af54daeac03a67be290e`.

**Status: exact author symbol lemma plus second-Picard time-scale consequence;
independent mathematical audit and novelty are undetermined.** The lemma
identifies the first nonzero mechanism by which a fast real Fourier carrier can
leave a slow carrier's frequency and then return to it through its conjugate.
The return is smaller by the scale ratio `|k|/|q|` than naive two-interaction
power counting.

This is the first quantitative mechanism needed to schedule the two sequential
purifier channels at very different viscous clocks. It is not yet an all-orders
nonlinear scheduling theorem.

No recursive turnover, singular solution, or `NS-R3` result is claimed.

## 1. Exact Leray pair

For nonzero output wavevector `p+q`, write

    C(p,a;q,b)
      =P_(p+q)[(a.q)b+(b.p)a],                            (1.1)

where

    P_xi=I-xi tensor xi/|xi|^2.                           (1.2)

The common Fourier factor `-i` is irrelevant for the norm estimate below.

Let `k` be a slow wavevector, `a` any polarization, and let `(q,b)` be a fast
transverse carrier:

    b.q=0.                                                 (1.3)

Assume

    0<|k| <= |q|/2.                                       (1.4)

The first fast sideband is

    c=C(k,a;q,b)                                           (1.5)

at wavevector `k+q`. Its first possible conjugate return to the original slow
frequency is

    d=C(k+q,c;-q,b),                                      (1.6)

whose output wavevector is exactly `k`.

## 2. Galilean cancellation lemma

**Lemma.** Under (1.3)--(1.4),

    |d| <= C |k| |q| |a| |b|^2,                          (2.1)

with a universal constant `C`.

A generic two-symbol estimate would give `C |q|^2 |a||b|^2`; hence (2.1)
gains the factor

    |k|/|q|.                                               (2.2)

### Proof

Set

    c_0=(a.q)b.                                            (2.3)

Since `b.q=0`,

    P_q c_0=c_0,
    c_0.q=0.                                               (2.4)

The orthogonal projector depends Lipschitz-continuously on direction away from
the origin. Under `|k|<=|q|/2`,

    ||P_(q+k)-P_q|| <= C |k|/|q|.                         (2.5)

Using

    c=P_(q+k)[(a.q)b+(b.k)a],                             (2.6)

we obtain

    |c-c_0| <= C |k| |a| |b|,                            (2.7)

and also

    |c| <= C |q| |a| |b|.                                (2.8)

For the return symbol, transversality again gives

    d=P_k[-(c.q)b+(b.k)c].                                (2.9)

Because `c_0.q=0`,

    |c.q|=|(c-c_0).q|
      <= C |q| |k| |a| |b|.                              (2.10)

Combining (2.8)--(2.10) and `||P_k||=1` proves (2.1). QED.

The cancellation at `k=0` is the Fourier-symbol trace of Galilean invariance:
a spatially constant velocity can translate a fast wave but cannot be altered
by that wave through a `q,-q` excursion.

## 3. Exact coordinate check

Rotate and scale so

    q=e1,
    b=e2,
    k=epsilon (K1,K2,K3).                                (3.1)

For a generic vector `a=(A1,A2,A3)`, direct exact substitution into (1.5)--(1.6)
shows that **every component** of `d` has an explicit factor `epsilon`.
The first-order expansion is

    d_1 = -2 A1 epsilon K1 K2^2/|K|^2 + O(epsilon^2),     (3.2)

    d_2 =  2 A1 epsilon K2(K1^2+K3^2)/|K|^2
             +O(epsilon^2),                              (3.3)

    d_3 = -2 A1 epsilon K2^2 K3/|K|^2 + O(epsilon^2).     (3.4)

Thus the scale-ratio gain is generically sharp: it is one power of
`epsilon=|k|/|q|`, not two.

The companion checker freezes the exact factorization, not merely the series.

## 4. Second-Picard return on the fast viscous clock

Now let the fast real carrier have vector Fourier amplitude `B`, so the two
fast modes are `(q,B)` and `(-q,conjugate(B))`, with

    q.B=0.                                                 (4.1)

Suppose the slow coefficient has vector amplitude `A` at `k`. On a time
interval

    0<=t<=c/(nu |q|^2),                                   (4.2)

heat semigroups are contractions. The part of the second Picard iterate which
leaves `k` through `+q` and returns through `-q` is bounded, using (2.1), by

    C |A| |B|^2 |k| |q| t^2.                             (4.3)

The opposite ordering has the same bound. Therefore

    |returned slow correction|/|A|
      <= C_(c,nu)
          (|B|/|q|)^2 (|k|/|q|).                         (4.4)

This is the useful dimensionless form.

## 5. Strong purifier parent calibration

Let the clean carrier scale be `b_clean`, so a filter competitive with
viscosity/advective dynamics needs low strain size

    S comparable to b_clean^2                              (5.1)

in dimensionless fixed-viscosity units. Let a rank-one purifier low carrier
have wave number

    K_p comparable to 1/lambda                            (5.2)

and desired low velocity `lambda S`, so its gradient is order `S`.
The exact 2D3C pump producing that low mode uses high parent frequency `N` and,
under balanced parent factors, physical high-mode velocity scale

    |B| comparable to lambda N sqrt(S).                   (5.3)

Then (4.4), for a slow carrier of wave number `K_s`, becomes

    relative conjugate-return error
      <= C lambda^2 S K_s/N.                              (5.4)

In particular, on the clean carrier itself `K_s comparable to b_clean`,

    error <= C lambda^2 b_clean^3/N.                     (5.5)

For protection of a later purifier parent's frequency `K_s comparable to N_2`
from an earlier fast family at `N_1`,

    error <= C lambda_1^2 S N_2/N_1.                     (5.6)

Thus arbitrary scale separation can beat the strong parent amplitudes at this
first return order.

## 6. Compatibility with a slowly varying purifier field

To make the generated low purifier act approximately as an affine shear on a
clean packet of carrier scale `b_clean`, its low wave number must be below the
packet bandwidth and in particular below the carrier scale. In the simplest
scale comparison this asks

    1/lambda << b_clean,

or

    eta:=lambda b_clean >>1.                              (6.1)

A simultaneous weak-channel argument had difficulty in this regime because its
global cross norm scales with `eta`. The return lemma shows that a
**scale-separated sequential** construction has a different small parameter.
For the clean carrier, (5.5) is

    C eta^2 b_clean/N.                                    (6.2)

Hence both

    eta >>1,
    eta^2 b_clean/N <<1                                  (6.3)

are compatible: choose

    b_clean << N/eta^2.                                   (6.4)

Likewise two sequential purifier clocks can satisfy

    N_2 >> eta_2^2 b_clean,
    N_1 >> eta_1^2 N_2.                                  (6.5)

There is no scale contradiction at second return order.

## 7. What remains before autonomous scheduling is proved

The lemma controls the first exact frequency-return channel, but the strong
fast field need not be perturbatively small in a global Wiener norm when
`eta>>1`. Therefore summing all higher fast excursions requires another idea.
The natural one is Galilean/slow-variation stability:

* after rescaling the fast family to unit frequency and unit fast time, the
  later parent has wave number `epsilon=N_2/N_1`;
* at `epsilon=0` it is spatially constant, and adding a constant velocity to a
  Navier--Stokes solution is exactly a Galilean transformation;
* smooth dependence on the slow spatial parameter should therefore upgrade the
  one-power cancellation to an all-orders bound of the form

      slow-parent distortion <= C(eta,T) N_2/N_1.        (7.1)

Proving (7.1) in a norm compatible with the localized finite-energy channel is
the next decisive scheduling theorem. If it closes, the two rank-one purifier
pulses can be clock-separated instead of coexisting strongly.

No PLAN, canonical proof graph, manuscript, or formal status is promoted. Full
repository verification and independent audit are pending. `NS-R3` remains
unresolved.