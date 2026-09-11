# Passive factor-two interstage carry loses at order `exp(-c Q^{-h})` in the continuously self-similar source reference

Date: 2026-09-12. Repository input before integration: current `main`.

**Status: exact reference-model exponent theorem and exact adapter obstruction. Independent mathematical audit and novelty assessment pending.** This packet answers the discriminating calculation requested by the frozen factor-two relay note, but only in the continuously self-similar extension of the source reference rate. The repository does not currently contain the full physical propagator comparison needed to promote the result to the actual interstage source history.

## 1. Prediction before the test

The factor-two relay creates doubled frequencies while they are still linearly stable in the current frozen cage. One proposed realization was passive interstage carry: retain such a doubled mode until the source similarity scale contracts enough that the same physical frequency becomes a normalized parent.

Prediction: even the most favorable continuously self-similar frozen reference damps this carry by `exp(-c Q^{-h})`, which is asymptotically far smaller than the local source entry scale `exp(-C L)` with `L~ell^2`. If correct, a successful cascade cannot rely on passive carry in that reference model; it must feed the new grade late or exploit a physical mechanism not represented by the reference propagator.

## 2. Exact normalization interval

The frozen positive-branch rate already proved for normalized axial scale `z>0` and tilt `s` is

    r_+(z,s)=a-b z^2,
    a=(1+s^2)^(-1/2),
    b=(3/5)(1+s^2).                                      (2.1)

Let `q_0` be the physical similarity scale when a doubled parent is born. The native carrier scale is proportional to `q^{-h/2}`. If the doubled physical frequency is then carried passively, its normalized scale at `q=x q_0` is

    z(x)=2 x^(h/2).                                      (2.2)

It becomes a normalized `z=1` parent at

    rho=2^(-2/h),       q_1=rho q_0.                    (2.3)

Hence exactly

    rho^(-h)=4,
    log(1/rho)=2 log 2 / h.                              (2.4)

This is a fixed similarity ratio depending on the source parameter `h`, not a small local fast-time window.

## 3. Exact continuously self-similar reference exponent

Assume for this section only that the frozen-reference rate (2.1) is transported continuously between `q_0` and `rho q_0` with the source physical prefactor proportional to `q^(-1-h)`. The exact source similarity identity at fixed regular `eta` gives `dt` equal to a fixed positive factor times `-dq`; that factor does not affect the sign below.

Up to this fixed positive factor, the integrated exponent is

    I = integral_(rho q_0)^(q_0)
          q^(-1-h) [a-4b(q/q_0)^h] dq

      = q_0^(-h)/h [3a-8b log 2].                       (3.1)

The bracket is strictly negative for every real tilt `s`. Indeed

    a <= 1,
    b >= 3/5,                                             (3.2)

and the positive atanh series gives

    log 2 = 2 atanh(1/3) > 2/3.                         (3.3)

Therefore

    3a-8b log 2
      < 3 - 8(3/5)(2/3)
      = -1/5.                                             (3.4)

Thus the continuously self-similar reference passive carry satisfies an exponent bounded above by

    I <= -c_h q_0^(-h),                                  (3.5)

for a fixed positive `c_h` (including the regular-coordinate positive factor).

Writing `q_0=2^(-ell)`, one has `q_0^(-h)=2^(h ell)`, which dominates every fixed power of `ell`. Consequently

    exp[-c_h q_0^(-h)] = o(exp[-C ell^p])                (3.6)

for every fixed `C,p>0`. In particular it is asymptotically much smaller than the local entry seed `exp(-gamma L)` with `L~ell^2`.

So **passive factor-two carry is dead in this continuously self-similar frozen reference model**.

## 4. Why this is not yet a physical source theorem

The adapter is the load-bearing issue. The existing finite-`L` lattice persistence theorem proves the source principal operator is a uniform perturbation of the frozen cage only on a **fixed fast-time window**. It explicitly does not claim such closeness on an interval growing like `L` or over the remote prehistory.

Likewise the inspected identity `partial_t v=Q^(-1-h)` is proved on a fixed lifted pulse label. Promoting (3.1) to the actual interstage evolution would require one source-wide propagator comparison over the finite but enormous scale ratio

    q_1/q_0=2^(-2/h),                                    (4.1)

with the moving frame, pressure constraint, slow coefficients, localization, exterior interaction and every nonlinear returned mode retained. No such estimate is presently proved in the repository.

The older long frozen-ray extrapolation had a severe preparation cost, but its own evidence file already marks that extrapolation as not the actual full physical prehistory. Reusing it would merely rename the same adapter gap.

Therefore the exact conclusion is two-part:

1. the simplest passive interstage mechanism fails decisively in the natural continuously self-similar reference; and
2. the first missing theorem for turning this into a physical exclusion is a **full interstage propagator adapter**, not another local Taylor coefficient.

## 5. Recomputed frontier

For the nonlinear factor-two route, passive carry no longer deserves further frozen-reference parameter search. The surviving constructive mechanism is continuous/late nonlinear feeding: generate or replenish a future grade close enough to the time when it becomes amplifying that it avoids the reference loss (3.5), while controlling the full expanding inherited state.

Alternatively one can prove a physical interstage propagator/adjoint estimate strong enough to transfer (3.5), or obtain a different full-history obstruction. Sparse thin-collar/nonlocal entry remains distinct and open.

No common Schwartz trace, physical passive-carry exclusion, full nonlinear de-forcing solution, singularity preservation or `NS-R3` result is claimed.

`research/check_reference_interstage_exponent.py` freezes the exact normalization and sign arithmetic. The analytic adapter limitation is not a numerical issue and is not removed by the checker.
