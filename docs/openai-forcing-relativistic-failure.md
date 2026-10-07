# Why the released OpenAI vortex forcing does not transfer directly to causal BDNK

Updated 2026-10-07. Mathematical status: synthesis of the author proof in
`research/evidence/bdnk-transfer-20261007.md`; independent reconstruction of
that packet remains pending. This note makes no global BDNK regularity claim.

## Statement in one line

The released forced Navier--Stokes construction is tailored to a parabolic
balance. Its direct relativistic proper-velocity lift fails because the full
causal BDNK energy equation introduces a leading time-derivative constitutive
balance that a bounded smooth source cannot cancel, while the pulse mechanism
also loses the arbitrarily strong high-frequency k^2 viscous damping used in
the classical construction.

## 1. Nonlinear leading-order mismatch

Let τ = t* - t. The tested relativistic adapter uses

    u = (γ,w),   γ = sqrt(1+|w|^2),

so physical velocity v = w/γ remains subluminal even when the proper velocity
grows. Thus the obstruction is not the trivial statement that the classical
velocity exceeds c.

For profiles

    γ,w ~ τ^(-a),
    x_i ~ τ^(β_i),
    Θ ~ τ^(-b),
    a>0, 0<β_i<1,

the full conformal BDNK tensor has time-derivative constitutive contributions
of order

    T_der,time ~ τ^(-3b-3a-1).

After one more time derivative in energy conservation the order is
τ^(-3b-3a-2). Spatial divergences gain only τ^(-β_max), so when β_max<1
they are lower order.

The leading energy equation therefore becomes a dilation constraint rather
than the classical Navier--Stokes balance. Define

    κ = (4χ0+2λ0)/(4χ0/3+2λ0-4η0/3) > 1.

The packet rewrites the leading coefficient using the nonnegative quantity

    Z = H^(3κ) G^3.

If

    b > -a/κ,

the dilation equation and regularity at the contracting origin force Z=0,
hence the accelerating profile is trivial. In frame A, κ=25/12, so every
noncooling thermal completion b>=0 is excluded.

A smooth forcing S that remains bounded at t* is lower order than this
divergent leading term and therefore cannot repair it. To preserve the same
profile one must change asymptotic regime -- for example sufficiently strong
cooling, characteristic/finer scales, or unresolved oscillations -- or allow
a source carrying the same singular order, which is no longer the desired
smooth-forcing analogue.

## 2. Loss of the classical parabolic pulse control

The classical forcing construction also uses another specifically
Navier--Stokes ingredient: high-frequency viscous decay strengthens like

    exp(-ν k^2 t).

The pulse design can therefore raise k until damping dominates unwanted
amplification.

Linearized transverse BDNK shear instead satisfies

    λ v_tt + h0 v_t - η v_xx = 0.

Its Fourier exponents are

    s_±(k) = [-h0 ± sqrt(h0^2-4ληk^2)]/(2λ).

At large k,

    Re s_±(k) = -h0/(2λ),

independent of k. Causality has converted the parabolic shear channel into a
damped-wave channel. There is no uniform high-k heat-semigroup gain to reuse.

These two failures are logically independent: the first is a nonlinear
conservation-law obstruction to the direct accelerating core; the second is a
linear exact obstruction to the classical pulse-damping bookkeeping.

## Interpretation

It is fair to say that the OpenAI forcing is **finely tuned to classical
Navier--Stokes**. "Artificial" is an interpretive word; what has actually been
shown is sharper and less subjective:

> The released profile/forcing architecture is not robust under this causal
> relativistic completion.

This is scientifically relevant because a forcing that merely prescribes an
arbitrary singular history could always hide model dependence. Here the source
was smooth in the classical theorem, yet the mechanism that keeps it smooth
while the solution becomes singular depends on the classical parabolic
equations.

The negative conclusion is scoped. We have **not** proved:

- that no smooth forcing can make BDNK singular;
- that relativity globally regularizes viscous hydrodynamics;
- that the OpenAI construction is physically meaningless;
- or that every relativistic closure behaves like BDNK.

The correct next experiment is to design a singular BDNK profile from the
causal equations themselves and ask whether its residual source is smooth.
That is `RNS-BDNK-F001`.
