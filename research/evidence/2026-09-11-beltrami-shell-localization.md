# Thin-shell positive-helicity localization removes the raw Beltrami source wall

Date: 2026-09-11. Repository input:
`itpplasma/navier@566ac862b650c7de1d59dfebc99fde8858fd216c`.

**Status: exact functional identity and scaling compatibility theorem; nonlinear
stability is explicitly not proved.** The common-sphere Beltrami construction
from `2026-09-11-beltrami-raman-span.md` cannot itself be a nonzero finite-energy
field on `R^3`, because an `L^2` curl eigenfield with nonzero constant eigenvalue
would have Fourier support on a measure-zero sphere. This note replaces that
inadmissible exact eigenfield by a real Schwartz, positive-helicity Fourier
packet in a thin radial shell. The entire high-high residual is then controlled
by the shell thickness rather than by the high carrier frequency.

The explicit exponent ledger is frozen by
`research/check_beltrami_shell_scaling.py`.

## 1. Exact finite-energy helical shell identity

Fix `Lambda>delta>0`. Let `U` be a real Schwartz divergence-free field whose
Fourier transform is positive helicity and is supported in

    ||xi|-Lambda| <= delta.                                (1.1)

Positive helicity means

    i xi cross Uhat(xi)=|xi| Uhat(xi),                    (1.2)

and is compatible with the reality condition at `-xi`. Such nonzero Schwartz
fields exist with Fourier support in arbitrarily small smooth patches around
any finite collection of nonzero directions, together with their reflected
patches.

Define

    E=(curl-Lambda)U=(|D|-Lambda)U.                        (1.3)

For every `s>=0`, the support condition gives exactly

    ||E||_{H^s} <= delta ||U||_{H^s}.                     (1.4)

Using

    (U.grad)U=grad(|U|^2/2)-U cross curl U                (1.5)

and Leray projection `P`, one obtains the exact identity

    B(U,U):=P[(U.grad)U]
           =-P[U cross E],                                (1.6)

because `U cross (Lambda U)=0`. In particular

    ||B(U,U)||_2 <= delta ||U||_infinity ||U||_2.         (1.7)

Thus the generic high-high derivative scale `O(Lambda)` is replaced by the
radial shell width `O(delta)`.

This is not a perturbative cancellation between selected pairs: it controls the
complete quadratic self-interaction of the full finite-energy high packet.

## 2. Heat evolution also remains coherent on the high viscous clock

For `0<=t<=c/(nu Lambda^2)`, the heat multiplier and the common-sphere scalar
satisfy on (1.1)

    |exp(-nu |xi|^2 t)-exp(-nu Lambda^2 t)|
      <= nu t ||xi|^2-Lambda^2|
      <= c (2 delta/Lambda+(delta/Lambda)^2).              (2.1)

Therefore for every `s>=0`,

    ||e^{nu t Delta}U-e^{-nu Lambda^2 t}U||_{H^s}
      <= c (2 delta/Lambda+(delta/Lambda)^2)||U||_{H^s}.  (2.2)

So shell localization does not introduce an order-one differential heat clock
when `delta/Lambda ->0`.

## 3. Compatibility with the useful Raman scaling

Use the route variables

    R=N/b,
    rho=P/(nu N),                                         (3.1)

where `b` is the clean scale, `N~Lambda` the high scale, and `P` a high-parent
velocity amplitude. The useful target-triggered Raman action requires

    rho^2/R = O(1).                                       (3.2)

Write

    epsilon=delta/b.                                      (3.3)

On one high viscous interval `t_H=O((nu N^2)^-1)`, the raw Duhamel size of the
shell residual (1.7), relative to a high-parent amplitude, has the scale

    t_H P^2 delta / P
      =O(rho delta/N)
      =O(rho epsilon/R).                                  (3.4)

This is only a source-size ledger; it does not bound the propagator of the
large linearization about the high field.

An explicit compatible sequence is

    Re=sigma^12,
    R=sigma^4,
    rho=sigma^2,
    epsilon=sigma^-1.                                     (3.5)

Then exactly

    rho^2/R=1,                                            (3.6)
    R^2/Re=sigma^-4 ->0,                                  (3.7)
    P/A=R^(3/2)/Re=sigma^-6 ->0,                          (3.8)
    rho epsilon/R=sigma^-3 ->0,                           (3.9)
    delta/N=epsilon/R=sigma^-5 ->0.                       (3.10)

Here `A=nu b Re` is the clean velocity scale used in the preceding Raman
packet. Multiplying (3.8) and (3.9), the raw shell-residual source measured
relative to the clean amplitude is `sigma^-9`. Also

    b/delta=epsilon^-1=sigma -> infinity,                 (3.11)

so the physical packet envelope is broader than the clean wavelength.

Hence finite-energy localization is not ruled out by the previous amplitude,
clock, or raw high-high source scalings.

## 4. What is and is not closed

This closes only the **raw localization-source** version of the Beltrami wall.
It does not prove that the exact Navier--Stokes solution remains close to the
thin-shell heat background. A generic energy estimate around a high field
would contain the integrated Lipschitz size

    integral_0^{t_H} ||grad U_H||_infinity dt
      ~ P/(nu N)=rho,                                     (4.1)

which diverges like `sigma^2` in (3.5). Therefore a Gronwall estimate loses the
small factor (3.9) completely and is not an admissible closure.

The first unresolved term is now sharply identified: the propagator of the
**high--slow linearized operator about a large positive-helicity Beltrami
background** at `rho->infinity`, after extracting the intended order-one Raman
Schur complement. One must show either

* a normal-form/unitary/skew structure controls the large `O(rho)` sideband
  excursion and leaves only the designed `rho^2/R` slow operator, or
* an explicit nonnormal/Floquet growth mode survives and refutes this repair.

The cheapest next discriminator is the finite Fourier star formed by one slow
mode, the ten common-sphere high carriers, and their first high sidebands. Keep
the exact heat gaps and helicity coefficients, eliminate the high sidebands by
an exact Schur complement, and inspect the spectrum/norm of the residual
high-block propagator before adding packet width.

No PLAN/canonical proof-graph promotion, regenerative turnover, finite-time
singularity, or `NS-R3` claim is made here.
