# Stable grade-2 counterterms repair the local hard/easy relay imbalance

Date: 2026-09-12. Repository input: `itpplasma/navier@c66e504c2ff961ec0b01a8ff8201c1300a7dc359`.

**Status: exact leading algebra plus analytic short-stage author theorem in the frozen full-lattice source-reference system; independent mathematical audit and novelty assessment pending.** This repairs the scoped stage-balance wall by enlarging the stage input class with two stable grade-`2m` coordinates. It does not supply those stable counterterms from the global past, does not build a whole-space physical stage, and does not prove an unforced singularity.

## 1. Mechanism change and prediction

The preceding obstruction proved that the dual-tuned four parents alone cannot produce a balanced doubled-parent quartet by birth followed by common linear amplification: two easy channels are `O(epsilon^2)`, two hard channels are `O(epsilon^4)`, and the easy linear rates are larger.

A genuinely different mechanism is to use the complete stable state rather than only the four unstable coordinates. At the left edge of a short normalized stage of duration `T`, add stable positive-branch coordinates directly at the two easy doubled frequencies

    e_3=2p_3,    e_4=2p_4,

with size `O(epsilon^2 T)` and phase opposite to the natural easy quadratic births.

Prediction before the exact test:

1. these counterterms cancel the easy endpoint growing coordinates at order `epsilon^2 T`;
2. phase grade prevents them from contaminating a hard grade-`2m` target at order `epsilon^3`;
3. their first hard-sector effect is at the same `epsilon^4 T^3` order as the desired hard births; and
4. after including those terms, both hard coefficients remain nonzero.

The fourth item is the discriminating calculation.

## 2. Exact leading easy cancellation

Use the dual-tuned parent field `P_1` from the factor-two relay. Let

    Q_3 = Pi_+ B(P_1,P_1)_(2p_3),
    Q_4 = Pi_+ B(P_1,P_1)_(2p_4),                         (2.1)

where `B` is the ordered incompressible Fourier bilinear form. The mixed-order theorem gives `Q_3,Q_4 !=0`.

Let `a_+(s_3),a_+(s_4)` be the positive source eigenpolarizations at the two easy doubled frequencies. Introduce the initial stable counterterm

    S = -epsilon^2 T [ Q_3 a_+(s_3) at 2p_3
                       + Q_4 a_+(s_4) at 2p_4 ]

with the conjugate reality partners. Since the eigen-coordinate normalization satisfies `Pi_+ a_+=1`, the endpoint expansion gives

    Pi_+ u(T)_(2p_j)
      = epsilon^2 T (-Q_j+Q_j) + higher order,
      j=3,4.                                               (2.2)

Both `z=2` positive branches are linearly stable in the current stage. Thus these are genuine stable counterterms, not extra unstable parents.

For the exact full short-stage endpoint map, take the two complex stable input coordinates as variables. The finite-horizon full-lattice source-reference flow is analytic in the initial data, and at `T=0` the derivative of the two easy endpoint coordinates with respect to those two stable input coordinates is the identity. The ordinary real/complex implicit-function theorem therefore gives, for sufficiently small `T` and `epsilon`, an analytic choice of stable counterterms which makes the two easy endpoint growing coordinates exactly zero (or any prescribed `O(epsilon^4)` targets). Its leading term is (2.2).

## 3. Why no lower-order hard contamination appears

The parent phase grades are `+/- m`; the new counterterms have grades `+/-2m`.

A product of one counterterm and one parent has grade `+/- m` or `+/-3m`, never `2m`. Two counterterms have grade `0` or `+/-4m`. Consequently there is no preload-induced hard grade-`2m` term at amplitude degree three, and two counterterms cannot directly make a hard grade-`2m` term at degree four.

The first preload correction to a hard target therefore contains exactly one `epsilon^2 T` counterterm and two `epsilon` parents. It uses two quadratic vertices and enters the endpoint at

    epsilon^4 T^3.                                        (3.1)

This is the same order as the original hard quartic relay coefficient. Linear source/viscous terms cannot enter this leading degree-four/time-cubic coefficient: starting from degree-one parents and a counterterm already carrying one power of `T`, the only admissible terms at (3.1) are the explicit quadratic trees frozen by the checker.

## 4. Both corrected hard coefficients are nonzero

Let `H_j^(0)` be the complete parent-only hard coefficient at `epsilon^4 T^3`, and `H_j^(S)` the complete one-counterterm/two-parent correction. The exact calculation evaluates

    H_j = H_j^(0)+H_j^(S),      j=1,2.                    (4.1)

After the standard Fourier factor `-i`, exact rational radical enclosures are

    H_1 in
    [-8639432917139325862302932448513 /
       38352336059845424841250000000000000,
     -8639432668483494032031234941763 /
       38352336059845424841250000000000000],              (4.2)

and

    H_2 in
    [ 7322206325116158394890121865187 /
       457018940907102767179756250000000000000,
      63132698032192609305399193131 /
       3939818456095713510170312500000000000].             (4.3)

The first interval is strictly negative and the second strictly positive. Hence both hard growing coordinates survive the stable-preload repair.

By continuity, after the exact implicit-function retuning that removes the easy endpoint coordinates, the two hard coefficients remain nonzero for sufficiently small positive stage duration and parent amplitude.

Thus the local frozen full-lattice system admits a short finite-duration **balanced stage** in the following precise sense: two freely supplied stable grade-`2m` coordinates remove the `O(epsilon^2)` easy imbalance while the hard `O(epsilon^4)` births persist, and the easy endpoint targets may be prescribed at the same `O(epsilon^4)` scale.

## 5. The blocker moves backward again

This theorem is a repair, not terminal closure. The counterterms are data at the **left edge of the stage**. In the original unforced Cauchy problem they cannot be reset independently at every scale.

The first unresolved question is therefore:

> Can the required stable grade-`2m` counterterms be produced causally by the returned expanding state from one global Schwartz trace, with the complete nonlinear convolution and physical source evolution retained?

The original four-coordinate backward-eternal unstable manifold already fixes every stable coordinate as an analytic function of the four unstable parents; those values are not free. An immediate exact discriminator is to compare the sign and size of its quadratic easy-target stable coordinates with the counterterms required by (2.2). If they are incompatible, the repair requires genuinely additional inherited modes/state rather than the original four-coordinate causal graph.

This is the next active dependency on the cascade route. The alternative routes remain the full physical interstage propagator/adjoint adapter, sparse thin-collar/nonlocal entry, and the complete full-history adjoint.

## 6. Exact check and non-claims

`research/check_stable_preload_balance.py` verifies the leading easy cancellation, stability of the two preload branches, phase-grade exclusion of lower-order hard contamination, and exact radical enclosures (4.2)--(4.3).

No recursive counterterm supply, finite-`L` physical persistence of this enlarged stage, whole-space localization, common trace, nonlinear de-forcing solution, singularity preservation, or `NS-R3` theorem is claimed.
