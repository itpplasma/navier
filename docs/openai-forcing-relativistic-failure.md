# Why the released OpenAI vortex forcing does not transfer directly to causal BDNK

Updated 2026-10-07. Mathematical status: synthesis of the author proof in
`research/evidence/bdnk-transfer-20261007.md`; independent reconstruction of
that packet remains pending. This note makes no global BDNK regularity claim.

## Statement in one line

The released forced Navier--Stokes construction is tailored to a parabolic
balance. Its direct relativistic proper-velocity lift fails because the full
causal BDNK energy equation introduces a leading time-derivative constitutive
balance that a bounded smooth source cannot cancel, while the pulse mechanism
also loses the arbitrarily strong high-frequency (k^2) viscous damping used in
the classical construction.

## 1. Nonlinear leading-order mismatch

Let (	au=t_*-t). The tested relativistic adapter uses
[
u^mu=(gamma,w),qquad
gamma=sqrt{1+|w|^2},
]
so physical velocity (v=w/gamma) remains subluminal even when the proper
velocity grows. Thus the obstruction is not the trivial statement “the
classical velocity exceeds (c).”

For profiles
[
gamma,wsim	au^{-a},qquad
x_isim	au^{eta_i},qquad
Thetasim	au^{-b},
quad a>0,quad0<eta_i<1,
]
the full conformal BDNK tensor has time-derivative constitutive contributions
of order
[
T^{mu
u}_{m der,time}sim	au^{-3b-3a-1}.
]
After one more time derivative in energy conservation the order is
(	au^{-3b-3a-2}). Spatial divergences gain only
(	au^{-eta_{max}}), so for (eta_{max}<1) they are lower order.

The leading energy equation therefore becomes a dilation constraint rather
than the classical Navier--Stokes balance. Writing
[
kappa=
rac{4chi_0+2lambda_0}
     {4chi_0/3+2lambda_0-4eta_0/3}>1,
]
the packet rewrites the leading coefficient using the nonnegative quantity
[
Z=H^{3kappa}G^3.
]
For
[
b>-a/kappa
]
the dilation equation and regularity at the contracting origin force
(Z=0), hence the accelerating profile is trivial. In frame A,
(kappa=25/12), so all (bge0) thermal completions are excluded.

A smooth forcing (S^
u) that remains bounded at (t_*) is lower order than
this divergent leading term and therefore cannot repair it. To preserve the
same profile one would need to change the asymptotic regime—e.g. sufficiently
strong cooling, characteristic/finer scales, unresolved oscillations—or allow
a source carrying the same singular order, which is no longer the desired
smooth-forcing analogue.

## 2. Loss of the classical parabolic pulse control

The classical forcing construction also uses another specifically
Navier--Stokes ingredient: high-frequency viscous decay strengthens like
[
exp(-
u k^2 t).
]
The pulse design can therefore raise (k) until damping dominates unwanted
amplification.

Linearized transverse BDNK shear instead satisfies
[
lambda v_{tt}+h_0v_t-eta v_{xx}=0.
]
Its Fourier exponents are
[
s_pm(k)=
rac{-h_0pmsqrt{h_0^2-4lambdaeta k^2}}{2lambda}.
]
At large (k),
[
operatorname{Re}s_pm(k)=-rac{h_0}{2lambda},
]
independent of (k). Causality has converted the parabolic shear channel into
a damped-wave channel. There is no uniform high-(k) heat-semigroup gain to
reuse.

These two failures are logically independent: the first is a nonlinear
conservation-law obstruction to the direct accelerating core, the second is a
linear exact obstruction to the classical pulse-damping bookkeeping.

## Interpretation

It is fair to say that the OpenAI forcing is **finely tuned to classical
Navier--Stokes**. “Artificial” is an interpretive word; what has actually been
shown is sharper and less subjective:

[
oxed{	ext{the released profile/forcing architecture is not robust under this causal relativistic completion}.}
]

This is scientifically relevant because a forcing that merely prescribes an
arbitrary singular history could always hide model dependence. Here the source
was smooth in the classical theorem, yet the *mechanism that keeps it smooth
while the solution becomes singular* depends on the classical parabolic
equations.

The negative conclusion is scoped. We have **not** proved:

- that no smooth forcing can make BDNK singular;
- that relativity globally regularizes viscous hydrodynamics;
- that the OpenAI construction is physically meaningless;
- or that every relativistic closure behaves like BDNK.

The correct next experiment is to design a singular BDNK profile from the
causal equations themselves and ask whether its residual source is smooth.
That is `RNS-BDNK-F001`.
