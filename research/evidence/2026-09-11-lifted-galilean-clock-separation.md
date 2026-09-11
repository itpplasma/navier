# Lifted-phase Galilean protection for separated purifier clocks

Date: 2026-09-11. Repository input:
`itpplasma/navier@bc54170894bc0abbfb48414f002746c01731a12c`.

**Status: author theorem for smooth quasiperiodic/lifted Navier--Stokes
families, with an all-orders slow-mode protection consequence; finite-energy
localization of the combined two-clock history is not included. Independent
mathematical audit and novelty are undetermined.**

The preceding exact symbol packet proved that the first `q,-q` return of a fast
carrier to a slow frequency gains `|k|/|q|`. This packet explains and sums that
cancellation to all nonlinear orders over one fast clock. The mechanism is
Galilean invariance exposed by a fixed phase-torus lift.

The result supplies the missing **temporal scheduling mechanism** for the two
sequential rank-one purifier channels at the quasiperiodic level. It does not
yet prove a compact-Schwartz two-clock implementation or a complete clean-gate
stage map.

No recursive turnover, singular solution, or `NS-R3` result is claimed.

## 1. Fixed phase lift

Let `e,K in R3` be fixed vectors with `|e|=1`. Introduce fast and slow phase
variables

    theta, psi in T.                                       (1.1)

For `epsilon>=0`, define the physical differential operator

    D_epsilon = e partial_theta + epsilon K partial_psi.   (1.2)

A lifted field `U(t,theta,psi)` generates the quasiperiodic physical field

    u(t,x)=U(t,e.x,epsilon K.x).                           (1.3)

The incompressible Navier--Stokes equation becomes on the fixed torus

    partial_t U - nu D_epsilon^2 U
      +(U.D_epsilon)U + D_epsilon P =0,                    (1.4)

    D_epsilon.U=0.                                         (1.5)

No moving Fourier lattice is present: all dependence on the physical scale
ratio sits in the coefficients of `D_epsilon`.

For Sobolev index `s` above the classical algebra threshold, the usual energy
proof gives a common local interval for `epsilon` in a compact neighborhood of
zero whenever the initial lifted data are uniformly bounded in `H^s(T2)`. The
viscous term is nonnegative and may be dropped in the existence estimate; the
first-order operator `D_epsilon` has coefficients uniformly bounded in
`epsilon`. Standard Picard/energy differentiation therefore gives smooth
dependence of the classical lifted solution on `epsilon` on every shorter
common interval.

This formulation avoids the discontinuity that would arise if different small
physical frequencies were compared as different atoms in an almost-periodic
Wiener norm.

## 2. Fast shear base and a slow family

Let

    V(t,theta)                                             (2.1)

be a smooth real fast shear satisfying

    e.V=0,
    partial_t V-nu partial_theta^2 V=0.                    (2.2)

Because `V` depends only on `theta` and is transverse to `e`, its nonlinearity
vanishes identically, so it is an exact Navier--Stokes solution of (1.4) for
every `epsilon` when regarded as independent of `psi`.

Let `A(psi)` be a real smooth finite Fourier sum satisfying the slow
transversality condition

    K.partial_psi A=0.                                    (2.3)

Consider initial data

    U_epsilon(0,theta,psi)
      =V(0,theta)+epsilon A(psi).                          (2.4)

The slow family has both amplitude and physical wave number `O(epsilon)` in
fast units. This is exactly the scaling of a later purifier parent family when
the two high frequencies have ratio `epsilon=N_2/N_1` and both have the same
fixed velocity-to-frequency ratio.

## 3. Exact first parameter derivative is the Galilean tangent

At `epsilon=0`, the solution is simply `V(t,theta)`. Differentiate the full
nonlinear lifted equation with respect to `epsilon` at zero and write

    W=partial_epsilon U_epsilon|_(epsilon=0).              (3.1)

Since the base `V` is independent of `psi`, differentiating `D_epsilon` itself
produces no forcing on `V`. Therefore `W` solves the ordinary linearized
Navier--Stokes equation about the fast shear with

    W(0,theta,psi)=A(psi).                                 (3.2)

For each fixed `psi`, put `c=A(psi)`. Galilean invariance gives the exact family

    V_c(t,x)=c+V(t,e.(x-ct)).                              (3.3)

Differentiating (3.3) at `c=0` in direction `c` yields

    W(t,theta,psi)
      =A(psi)-t [A(psi).e] partial_theta V(t,theta).       (3.4)

Direct substitution also verifies (3.4): the heat terms cancel using (2.2),
while `(W.e) partial_theta V` cancels the derivative of the translated shear.

The key consequence is exact preservation of the zero-fast-harmonic part:

    average_theta W(t,theta,psi)=A(psi)                   (3.5)

for every time on the common interval.

Thus **the slow parent profile is unchanged at first order in the scale
ratio**, even though order-`epsilon` fast sidebands are generated. This is the
all-orders nonlinear origin of the one-power return cancellation from the
preceding symbol packet.

## 4. Full nonlinear relative protection

Smooth dependence on `epsilon` gives, in a fixed lower Sobolev norm,

    U_epsilon(t)=V(t)+epsilon W(t)+O_T(epsilon^2).         (4.1)

Take the zero-fast-harmonic projection `Pi_0`, i.e. average in `theta`. By
(3.5),

    Pi_0[U_epsilon(t)-V(t)]
      =epsilon A(psi)+O_T(epsilon^2).                     (4.2)

Therefore the slow-family coefficient/profile is preserved with **relative**
error

    O_T(epsilon).                                          (4.3)

This estimate includes every nonlinear fast excursion over the fixed fast
clock. It is not a truncation at second Picard order.

All nonzero fast harmonics generated at first order are contained in the
explicit translation term in (3.4). They carry the fast phase and are therefore
eligible for fast viscous decay after the fast pulse.

## 5. Near-opposite fast purifier parents: a second lifted phase

An actual 2D3C purifier channel is not exactly the limiting heat shear. Its
scalar parent frequencies are

    -m N e + K_p,                                         (5.1)

while its shear parents are `m N e`. In fast units introduce

    delta=|K_p|/N                                         (5.2)

and a second fixed phase `phi`, so that

    D_(delta,epsilon)
       =e partial_theta
         +delta Khat_p partial_phi
         +epsilon K partial_psi.                          (5.3)

The exact clocked 2D3C family is a smooth lifted solution in the
`(theta,phi)` variables. At `delta=0`, opposite parent labels collapse to the
same fast harmonics and their sum is again a transverse heat shear: all
physical wavevectors are collinear with `e`, all velocities are transverse,
and the nonlinear term vanishes.

Apply the same common-interval smooth-dependence argument jointly in
`(delta,epsilon)`. The derivative with respect to the slow-family amplitude at
`epsilon=0` differs from the Galilean tangent (3.4) by `O_T(delta)`. Hence

    Pi_slow[U_(delta,epsilon)(t)-V_delta(t)]
      =epsilon A
        +O_T(epsilon delta+epsilon^2),                    (5.4)

or, relative to the slow parent amplitude,

    relative slow-parent distortion
      <= C_T (delta+epsilon).                             (5.5)

Here `Pi_slow` means zero fast harmonic with the prescribed slow-phase label;
it is a fixed Fourier-label projection on the lifted torus.

Equation (5.5) is the desired all-orders fast/slow protection estimate.

## 6. Purifier-clock calibration

Let the clean carrier scale be `b`, and choose a fixed affine-separation
parameter

    eta=lambda b >1,                                     (6.1)

so the purifier low wave number is

    K_p comparable to b/eta.                              (6.2)

A strong rank-one purifier producing strain `S comparable to b^2` has high
parent velocity/frequency ratio `O(eta)`; after division by its high frequency,
the fast lifted data therefore lie in a fixed `eta`-dependent bounded set.

Take two clock frequencies

    N_1 >> N_2 >> b.                                      (6.3)

On the first clock, the later purifier family has

    epsilon=N_2/N_1,                                      (6.4)

while the first channel's near-opposite offset is

    delta_1 comparable to b/(eta N_1).                    (6.5)

Thus (5.5) gives

    relative change of every later parent label
      <= C_(eta,T)[N_2/N_1+b/(eta N_1)].                 (6.6)

No smallness of `eta` is required; it is fixed before the scale separation is
sent large.

The slow channel's own viscous change during the first fast interval is only
`O((N_2/N_1)^2)`. Its three-layer low output has quadratic onset, so at
`t=O(N_1^-2)` its intended low pulse is smaller than its later peak by

    O((N_2/N_1)^4).                                       (6.7)

Hence the second purifier is still essentially unactivated and its parent
coefficients are preserved when the first purifier pulse occurs.

## 7. Decay between the two clocks

The three-layer purifier was designed to cancel the slow low-frequency tail.
After the first `O(N_1^-2)` pulse, every component of the first ideal channel
decays on the fast clock. At the later time `t comparable to N_2^-2`, its
remaining ideal amplitude is bounded by

    exp[-c (N_1/N_2)^2]                                   (7.1)

up to fixed polynomial factors.

The order-`epsilon` sidebands in the Galilean tangent (3.4) have nonzero fast
harmonic and inherit the same fast heat scale. Higher fast-harmonic remainders
from (4.1) do likewise. The only pieces not forced to decay at the fast rate
are zero-fast-harmonic slow-sector corrections, and these are already bounded
relatively by (6.6).

Therefore, at the start of the second clock, the lifted state has the form

    pristine slow purifier state
      + O_[relative](N_2/N_1+b/(eta N_1))
      + exponentially small fast residue.                 (7.2)

Classical continuous dependence on the fixed second scaled interval then gives
the same relative accuracy for the second low purifier pulse.

## 8. Sequential scheduling theorem at quasiperiodic level

Combine Sections 5--7 with the sequential two-shear carrier theorem.

**Theorem.** Fix the two rank-one purifier geometries, a finite scaled pulse
horizon, fixed `eta`, and fixed viscosity. In the lifted quasiperiodic setting,
choose

    N_2/b -> infinity,
    N_1/N_2 -> infinity.                                  (8.1)

Load both exact three-layer purifier parent families at time zero, with their
fast scales `N_1,N_2` and amplitudes chosen to produce the required two
rank-one strain strengths. Then one original unforced Navier--Stokes history
has:

1. a first rank-one purifier pulse on the `N_1^-2` clock;
2. relative distortion of the later parent labels tending to zero;
3. vanishing first-pulse residue by the `N_2^-2` clock; and
4. a second rank-one purifier pulse converging to its isolated-channel pulse.

Consequently the two low purifier pulses converge, in their respective clock
windows, to the **sequential** pair whose net Kelvin discrimination was proved
in `2026-09-11-sequential-two-shear-purifier.md`.

This removes the need for strong simultaneous two-channel coexistence at the
quasiperiodic mechanism level.

## 9. Remaining finite-energy issue

The theorem is formulated on a fixed lifted phase torus and therefore
represents quasiperiodic/infinite-energy carrier families. The repository
already has finite-energy nested localization and one-channel Wiener shadowing,
but a hierarchy with `N_1>>N_2` must still be localized without destroying the
phase-label estimate (5.5).

The next target is a **two-clock localization theorem**: choose nested spatial
envelopes and low-band projections so that

* cutoff residuals are smaller than the scale-separation errors in (6.6);
* Fourier tails do not identify distinct lifted fast/slow labels;
* the first localized fast pulse changes the retained slow-parent packet by
  `o(1)` relative norm; and
* fast pressure/sideband tails are negligible by the second clock.

This is now a localization/packet theorem, not an unknown purifier algebra.

No PLAN, canonical proof graph, manuscript, or formal status is promoted. Full
repository verification and independent audit are pending. `NS-R3` remains
unresolved.