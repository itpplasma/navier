# Input-only quartic angular-event budget, and why the source pulses evade it

Date: 2026-09-11. Repository input:
`itpplasma/navier@7649b2eff78298188437d7b0240c8699fa845c45`.

**Status: exact author theorem on every compact classical interval of the
original unforced whole-space Navier--Stokes branch, followed by a
source-scale compatibility calculation.** The theorem combines the existing
whole-space first-moment bound with the exact vector angular-mode inequality.
It converts the normalized angular-preparation information into an absolute,
input-only spacetime budget for high-angular-mode events.

The resulting budget is genuine new information, but the forced source's
shrinking-volume pulses are too cheap in `L2` for it to exclude their scale
sequence. Thus this checkpoint advances the positive/negative interface and
also supplies a negative control: absolute quartic angular event counting is
not the missing source-prehistory obstruction.

No terminal regularity theorem or unforced singular solution is claimed.

## 1. Rotation modes and the moment input

Let `u` be the classical unforced solution on

    0 <= t <= min(H,T_*),

with Schwartz datum `d`, fixed `nu>0`, and let `Pi_n` be the exact vector
rotation-mode projections from
`2026-09-08-angular-preparation-obstruction.md`. Put

    v_n=Pi_n u,
    E_n(t)=||v_n(t)||_2^2,
    r=sqrt(x_1^2+x_2^2).                                  (1.1)

The September 11 weighted-moment theorem gives an input-only finite-horizon
constant `M_H` such that

    sup_t || |x|u(t)||_2 <= M_H,                           (1.2)

and the ordinary energy identity gives

    integral_0^min(H,T_*) ||grad u||_2^2 dt
      <= ||d||_2^2/(2 nu).                                (1.3)

Because multiplication by `r` is rotation invariant, it commutes with the
angular projections. Orthogonality therefore gives, in particular,

    ||r v_n||_2 <= ||r u||_2 <= M_H.                      (1.4)

## 2. Angular uncertainty converts energy into dissipation

For `|n|>=2`, the exact vector cylindrical calculation already proved

    ||grad v_n||_2^2
      >= (|n|-1)^2 integral |v_n|^2/r^2 dx.               (2.1)

Cauchy--Schwarz with the factors `r|v_n|` and `|v_n|/r` yields

    E_n^2
      <= ||r v_n||_2^2 integral |v_n|^2/r^2 dx.           (2.2)

Combining (1.4), (2.1), and (2.2),

    (|n|-1)^2 E_n(t)^2
      <= M_H^2 ||grad v_n(t)||_2^2.                       (2.3)

This is an instantaneous uncertainty inequality. No angular mean equation,
source decomposition, strain bound, or future norm is used.

## 3. Exact input-only quartic angular-event theorem

The rotation projections commute with spatial derivatives and are mutually
orthogonal. Hence

    sum_n ||grad v_n||_2^2 = ||grad u||_2^2.              (3.1)

Sum (2.3) over `|n|>=2` and integrate in time. Equations (1.2)--(1.3) give

    integral_0^min(H,T_*)
      sum_(|n|>=2) (|n|-1)^2 ||Pi_n u(t)||_2^4 dt
       <= M_H^2 ||d||_2^2/(2 nu).                         (3.2)

Every constant on the right depends only on the initial datum, `nu`, and the
fixed horizon `H`; it is independent of the maximal smooth time and of any
future critical norm.

Equivalently, for any thresholds `e_n>0`,

    sum_(|n|>=2) (|n|-1)^2 e_n^2
       |{t<=min(H,T_*): E_n(t)>=e_n}|
      <= M_H^2 ||d||_2^2/(2 nu).                          (3.3)

Thus an arbitrary sequence of high-angular-mode events cannot have both large
`L2` energy and long duration. This is an **absolute** event budget, unlike the
normalized nonlinear-work lower bound in the older angular-preparation packet.

## 4. Calibration against the actual forced source scales

The OpenAI forced construction itself explains why this theorem is not yet an
exclusion of its pulse architecture. In the proof outline the physical pulse
amplitude satisfies

    A_wave^2 ~ q^(-1-h),                                  (4.1)

while the active core/shell volume has scale

    q^(3/2-h).                                             (4.2)

Therefore the schematic `L2` energy of one pulse-scale angular event is

    E_n ~ q^(1/2-2h)                                      (4.3)

up to the fixed/profile and polylogarithmic factors present in the detailed
construction. The principal carrier has

    n^2 ~ q^(-h)                                          (4.4)

on nondegenerate-pitch labels. The pulse coordinate satisfies
`t_* = Q^(1+h) partial_t` and has length polynomial in
`ell=log_2(Q^-1)`, so its physical duration is

    Delta t ~ q^(1+h) polylog(q^-1).                      (4.5)

Substitution into the left-hand scale of (3.2) gives

    n^2 E_n^2 Delta t
      ~ q^(2-4h) polylog(q^-1).                           (4.6)

Since the source fixes `0<h<1/100`, the exponent satisfies

    2-4h > 49/25 >0.                                      (4.7)

Hence dyadic contributions of the form (4.6) are strongly summable. The source
construction deliberately combines increasing pointwise speed with shrinking
volume; that mechanism also makes its pulse events inexpensive in the quartic
`L2` budget (3.2).

Equation (4.6) is a scale compatibility calculation, not a proof that an
individual source pulse equals one exact global angular projection with sharp
lower constants. It is sufficient for the present negative conclusion: the
known source scalings do not force divergence of (3.2), so this budget cannot
by itself retire the source-prehistory route.

## 5. Recomputed frontier

The absolute angular-event budget closes one possible escape from the older
normalized-work limitation, but not the terminal problem. The source-specific
prehistory remains capable, at the level of absolute energy scaling, of using
very small high-frequency packets.

The active discriminator therefore remains more structural:

1. **physical prehistory matching:** can exterior transport or nonlinear
   regeneration actually deliver the exponentially cheap local entry seeds
   through the full viscous propagator from one Schwartz datum, while retaining
   every generated mean/sideband and pressure term; or
2. **complete physical adjoint:** do exact global backward observations prove
   that those entry traces require a minimum-prefix control cost or nonlinear
   de-forcing budget that diverges?

The existing frozen-ray continuation has an `exp(c L^4)` preparation cost, but
that is not a theorem for every physical prehistory. The existing nonlinear
regeneration packet supplies a nonzero source-polarized birth channel, but also
an unavoidable same-order sideband and a nonclosed higher jet. Those are the
next load-bearing data, not another `L2` event count.

Companion checker `research/check_angular_event_budget.py` freezes the exact
source exponent arithmetic only. The PDE theorem above is analytic and is not
certified by that script.

NON-CLAIMS: no RF-q producer, no absolute nonlinear-generation cost, no common
Schwartz trace, no source-profile exclusion, and no `NS-R3` conclusion.
Independent mathematical audit and novelty assessment remain pending.
