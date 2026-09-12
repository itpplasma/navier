# Recentered four-parent cage loses exact return and then hyperbolicity

Date: 2026-09-12. Repository input before integration: `itpplasma/navier@6ab58f81b245b458ce08e9d63188cabe0cc71d66`.

**Status: exact source-phase/spectral obstruction for recentered propagation that remains in the `z=1` four-growing-parent class. Independent mathematical audit and novelty assessment pending.** This packet tests the first repair left by the single-label interstage wall. It does **not** rule out a physical transition which temporarily leaves the four-parent class, changes normalized grade, uses additional modes, or regenerates parents late.

## 1. Prediction before the test

The direct fixed-label adapter fails because the exact finite-`L` lattice shear becomes nonperturbative over a factor-two scale change. The natural repair is to cover the interstage interval by overlapping local frames and repeatedly recenter the parent quartet.

Prediction: exact recentering does not reset the load-bearing four-parent geometry. At fast-time ratio `tau=v/L`, both pair separations are multiplied by the same factor

    a = 1+tau.

Returning exactly to the already-proved rational cage after a positive shift is impossible. If instead the new local frame inherits the enlarged separations, the outer parent eventually leaves the positive source branch, so the four-growing-parent hyperbolicity needed by the causal relay is lost.

## 2. Exact recenter identity

The finite-`L` source phase theorem gives the four `z=1` tilts

    c +/- a u_A,    c +/- a u_B,

with

    c=1/20,    u_A=9/20,    u_B=3/20,    a=1+v/L.       (2.1)

The common daughter fixes the center, because each symmetric pair always sums to `2c`. Thus a new left-edge frame representing the same quartet cannot change `c` without changing the physical daughter.

Let `S(a)` be the multiset of the four centered tilts in (2.1). Its second centered moment is

    M_2(a)
      = 2 a^2 (u_A^2+u_B^2)
      = a^2 M_2(1).                                      (2.2)

Therefore exact equality of multisets `S(a)=S(1)`, even allowing arbitrary permutation of the four parents, implies

    a^2=1.                                                (2.3)

For a forward local shift one has `a>0`, hence

    a=1.                                                  (2.4)

So **no nonzero forward fast shift can be recentered exactly into the same proved rational four-parent cage**. This is a coordinate-invariant statement about the centered four-point set, not an artifact of parent ordering.

## 3. Following the separation does not preserve four growing parents

One can weaken the repair and allow the new frame to inherit the enlarged pair separations `a u_A,a u_B`. The source-reference positive rate at `z=1` is

    gamma_+(1,s)
      = 1/sqrt(1+s^2) - (3/5)(1+s^2).                    (3.1)

The outer positive parent has tilt

    s_out(a)=c+a u_A.                                    (3.2)

At the exact multiplier

    a_*=13/9,                                             (3.3)

one gets

    s_out(a_*)=7/10.                                     (3.4)

The all-orders spectral-cage theorem already certified

    gamma_+(1,7/10)
      = 10/sqrt(149)-447/500 <0.                          (3.5)

The sign has the integer certificate

    5000^2 < 447^2 * 149.                                (3.6)

Writing `q=sqrt(1+s^2)`, the rate is

    f(q)=1/q-(3/5)q^2,
    f'(q)=-1/q^2-(6/5)q <0.                              (3.7)

Hence for every `a>=13/9` the same outer parent remains strictly stable. A recentered chain which stays in this `z=1` geometry can therefore not carry four growing source parents beyond that finite separation enlargement.

## 4. What this closes and what remains

This is the second exact kinematic attack on the physical interstage adapter after the single-label wall:

1. one fixed label leaves every perturbative neighborhood of the frozen cage over the factor-two interval;
2. repeatedly resetting to the same rational cage is impossible after any nonzero forward shift; and
3. allowing the local separations to follow the shift eventually stabilizes an outer parent.

Therefore the surviving physical adapter cannot be a chain of local frames which simply keeps the inherited state inside the same `z=1` four-growing-parent family. It must use a genuinely different mechanism: a grade-changing/nonparent transition, additional inherited modes with a new hyperbolic structure, or late nonlinear regeneration near the next source window.

This packet does **not** prove that all multi-label physical adapters fail. In particular it does not analyze transitions through normalized grades `z!=1`, nor does it bound the full nonlinear source propagator. Sparse thin-collar/nonlocal entry and the complete physical adjoint remain distinct routes.

No common Schwartz trace, unforced correction, singularity preservation, or `NS-R3` theorem is claimed.

Companion checker: `research/check_recenter_cage_wall.py`.
