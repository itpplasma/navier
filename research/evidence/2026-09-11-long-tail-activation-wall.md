# Activation-time wall for the perturbative long-tail purifier

Date: 2026-09-11. Repository input:
`itpplasma/navier@925daabeea73c247ab12b6c9f3a56714eb3a479c`.

**Status: exact scaling obstruction for the co-located perturbative long-tail
implementation. It does not refute the isolated long-tail channel, spatial
staging, or a genuinely nonperturbative 2D3C control construction.**

The long-tail repair fixes the previous action-versus-fast-parent contradiction:
it can accumulate fixed nonzero purifier action on the clean clock while its
high-parent velocity/frequency ratio stays bounded. But a recursive clean gate
needs a second property: the purifier must not already be fully active while the
target modes are being born. In the current co-located preloaded construction,
that timing requirement is incompatible with the perturbative exact-ladder
regime.

The exact algebra is frozen by
`research/check_long_tail_activation_wall.py`.

## 1. Matched clean-gate and filter rate

Let `S>0` denote the physical strain rate required of the inheritance filter.
At fixed Reynolds number one may take `S=M nu b^2`; in the recursive
high-Reynolds regime the stronger requirement is `S` comparable to the clean
advective rate `A b`. The argument below uses only that the target birth/filter
clock is

    t_g = c/S                                               (1.1)

for one fixed `c>0`.

The two-layer long-tail 2D3C channel has pump gaps

    D=2 N^2, 4D,                                           (1.2)

and build variable

    x=nu D t.                                              (1.3)

Its normalized selected low coefficient is

    (4/3)B(x),

    B(x)=3/4-exp(-x)+(1/4)exp(-4x),                        (1.4)

with

    B(0)=0,
    B'(x)>0,
    B(infinity)=3/4.                                       (1.5)

Thus asymptotic dormancy through the clean birth requires

    x_g := 2 c nu N^2/S -> 0.                              (1.6)

If `x_g` instead tends to infinity, the tail is already at its full selected
strength before the matched clean gate has completed.

## 2. The exact-ladder parameter is reciprocal to the activation variable

For target strength `S`, balanced parent factors have size `O(N sqrt(S))`, and
the exact passive-scalar ladder has integrated shift parameter

    mu = O(sqrt(S)/N).                                     (2.1)

The existing perturbative channel theorem uses

    mu -> 0,                                               (2.2)

or equivalently

    S/N^2 -> 0.                                            (2.3)

At the matched clean time (1.1) one has the exact identity

    x_g (S/N^2)=2 c nu.                                    (2.4)

For fixed `nu,c>0`, the two factors cannot both tend to zero. In particular,

    S/N^2 -> 0   implies   x_g -> infinity,                (2.5)

so perturbative exact-ladder accuracy forces the long tail to be essentially
fully active by the time the target birth occurs. Conversely,

    x_g -> 0   implies   S/N^2 -> infinity,                (2.6)

which is outside the small-integrated-shear regime used to prove the selected
low output.

This is not the previous clock-action wall: the long tail *does* provide fixed
action. The new obstruction is **activation ordering**.

## 3. Consequence for the co-located clean-gate architecture

The clean first-gate theorem realizes nonlinear birth on its advective clock.
The common inheritance filter must act after those target components have been
created; if the full strong filter is present from the start, it changes the
carrier geometry and Taylor tree that the clean-gate algebra relies on.

For the present preloaded two-layer long-tail construction, the two desired
asymptotic properties are therefore

1. `mu -> 0`, so the exact full 2D3C output is controlled by the designed low
   interaction;
2. `B(x_g) -> 0`, so the purifier is dormant during the clean birth.

Equations (1.5) and (2.4) show that they are incompatible.

At the recursive high-Reynolds scaling `S comparable to A b`, the statement is
particularly transparent:

    perturbative purifier:   N^2 >> A b,
    delayed activation:      nu N^2 << A b,                (3.1)

up to fixed normalization constants. For fixed positive viscosity there is no
asymptotic regime satisfying both with the required vanishing errors.

## 4. What remains open

This obstruction eliminates only the **co-located perturbative preloaded
long-tail switch**. It leaves genuinely different mechanisms:

* **nonperturbative exact 2D3C control:** allow `mu=O(1)` or larger and solve the
  passive-scalar ladder without a first-interaction approximation, seeking a
  delayed strong selected tail;
* **spatial staging:** generate a long-lived purifier elsewhere and transport
  the newborn clean packets into it after birth;
* **state-triggered or multi-generation construction:** make the filter emerge
  from the clean-gate products themselves rather than an independent preloaded
  pump;
* **positive regularity route:** abandon regenerative blowup and attack the
  arbitrary-data RF-q producer by a mechanism not equivalent to a future
  critical norm.

The first of these is the closest repair because the isolated 2D3C channel is
an exact linear advection-diffusion problem in the scalar component even at
large shear. Its next discriminating question is whether one can design the
initial scalar/shear data so the selected low coefficient remains small until a
prescribed matched time and then acquires the required sign/size, without
requiring an ill-conditioned amount of initial energy.

No PLAN, canonical proof graph, manuscript, or formal status is promoted here.
`NS-R3` remains unresolved.
