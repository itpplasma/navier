# Passive carry of the old parents to half grade is super-amplifying, not a reusable small-data bridge

Date: 2026-09-12. Repository input before integration: `itpplasma/navier@09b7565007c91f87dd9fe1fa5742fed190ad69fc`.

**Status: exact continuously self-similar source-reference exponent theorem. Independent mathematical audit and novelty assessment pending.** This packet tests the first necessary bridge for the newly active grade-changing/nonparent route. It does not analyze the complete physical interstage propagator and it does not exclude nonlinear cancellation, depletion, saturation, or genuinely late regeneration.

## 1. Prediction before the test

The recentered `z=1` four-parent adapter is closed, but one could try to keep the old physical parents while the source scale contracts. At the next factor-two normalization they would be inherited `z=1/2` modes and could participate in a late quadratic/cubic regeneration of the new `z=1` parent quartet.

Prediction: unlike the doubled modes, which are super-damped, the old parents are **super-amplified** over the same scale interval. Their continuously self-similar reference gain is `exp(+c Q^{-h})`. Therefore a quasi-Gaussian small parent trace used at one stage cannot simply be reused as a small half-grade ancestor at the next stage. A surviving construction must actively remove/cancel it or regenerate the needed half-grade state late.

## 2. Exact one-step parent exponent

Let `q_0=Q` be the source similarity scale at the first stage and

    rho=2^(-2/h),       q_1=rho q_0.

For a fixed old physical parent, its normalized axial scale during the contraction `q=x q_0` is

    z(x)=x^(h/2),

so `z(1)=1` and `z(rho)=1/2`. The frozen positive-branch rate is

    r_+(z,s)=a-b z^2,
    a=(1+s^2)^(-1/2),
    b=(3/5)(1+s^2).

Using the same continuously self-similar source prefactor as in the passive doubled-mode packet, the integrated exponent is, up to the same fixed positive regular-coordinate factor,

    I_parent
      = q_0^(-h) integral_rho^1 x^(-1-h)
          [a-b x^h] dx
      = q_0^(-h)/h [3a-2b log 2].

Here `rho^(-h)=4` and `log(1/rho)=2 log 2/h` were used exactly.

## 3. Uniform positive margin on all four caged parents

The four parent tilts are

    1/2,  -2/5,  1/5,  -1/10.

Hence `|s|<=1/2`, so

    a >= 2/sqrt(5),
    b <= 3/4.

Also `log 2<1`. Therefore

    3a-2b log 2
      > 6/sqrt(5)-3/2
      > 9/10.

The last inequality is purely algebraic (`6/sqrt(5)>12/5`). Thus every old caged parent obeys the uniform reference lower bound

    I_parent > [9/(10h)] q_0^(-h)

up to the common fixed positive coordinate factor.

This is the opposite sign from the doubled-mode passive-carry exponent in `2026-09-12-reference-interstage-exponent.md`.

## 4. Small-data consequence

Write `q_0=2^(-ell)` and retain the source scaling `L comparable to ell^2`. Then

    q_0^(-h)=2^(h ell),
    q_0^(-h)/L -> infinity.

Consequently any parent component whose stage-one size is only quasi-Gaussian,

    |A_0| >= exp(-C L+o(L)),

is amplified in this reference model to

    |A_1| >= exp(c q_0^(-h)-C L+o(q_0^(-h))),

which leaves every fixed small-data neighborhood for sufficiently large `ell`. Conversely, demanding a small quasi-Gaussian-size half-grade ancestor at `q_1` forces its predecessor at `q_0` to be smaller by `exp(-c q_0^(-h))`, far below every `exp(-C L)` scale.

This is a **conditional amplitude-interface statement**, not a theorem that the actual parent amplitudes must equal a particular quasi-Gaussian sequence. Its use is to rule out the simplest bridge in which the same small parent trace is passively reused at consecutive source scales.

## 5. Recomputed constructive interface

The grade-changing idea is not dead. The exact frequency algebra still allows two inherited half-grade modes to sum to a new `z=1` parent, and the previously proved factor-two homogeneity shows local late nonlinear births do not vanish merely under frequency scaling.

What fails is passive reuse of the old parent amplitudes. The next constructive mechanism must therefore do at least one of the following:

1. cancel/deplete the old parents after they serve the current pulse and regenerate half-grade ancestors only near the next source window;
2. use nonparent inherited modes with a different one-step exponent and a new hyperbolic structure; or
3. exploit a genuinely nonlinear finite-duration stage in which the large positive linear action is balanced by transfer rather than treated as passive propagation.

The complete physical adapter, the one-Schwartz-trace condition, nonlinear de-forcing, singularity preservation and `NS-R3` remain open.

Companion checker: `research/check_half_grade_parent_carry.py`.
