# Simultaneous-pump time ordering cancels the leading Raman transfer

Date: 2026-09-11. Repository input:
`itpplasma/navier@2fa27115858236aa06dc0fae9ef7da8afad2c6ca`.

**Status: exact scoped obstruction correcting the interpretation of the current
state-triggered Raman programme.** The earlier Raman span/lattice packets froze
one ordered two-step tree in which the target first interacts with high parent
`q` and the resulting high sideband then interacts with `r`. In the actual
simultaneous evolution with both high parents preloaded, the reverse ordering
`r` then `q` is present with the same perturbative order. For both Raman pump
families used by the repository, the two leading ordered symbols are exact
negatives. The physical symmetrized leading transfer therefore vanishes.

The exact symmetry is frozen by

* `research/check_beltrami_raman_order_cancellation.py`, and
* `research/check_raman_simultaneous_order_wall.py`.

This does not refute every possible Raman mechanism. It refutes the current
architecture in which two near-opposite high parents are simultaneously
preloaded and their one-ordered target-assisted composition is interpreted as
the leading slow transfer. A surviving Raman route must break the ordering
symmetry dynamically or change the interaction geometry.

## 1. Original Leray-silent pair

The original state-triggered Raman packet uses near-opposite high parents

    q=l/2+N Q,
    r=l/2-N Q,                                             (1.1)

with `l.Q=0`. Its frozen one-order high-frequency limit is

    L_orig(Q)
      =2(A.Q) P_kappa[
          (l.kappa)l-(m.kappa)m],
    m=Q cross l,                                           (1.2)

where `(h,A)` is the newborn slow target and `kappa=h+l`.

Exchanging the two high parents sends

    Q -> -Q,
    m -> -m.                                               (1.3)

The bracket in (1.2) is unchanged because it is quadratic in `m`, whereas
`A.Q` changes sign. Hence the reverse ordering has

    L_orig(-Q)=-L_orig(Q).                                (1.4)

Therefore

    L_(q then r)+L_(r then q)=0                           (1.5)

at the leading `O(N)` scale.

## 2. Common-Beltrami pair

The later same-helicity common-sphere construction has one-order limit

    L_B(Q)
      =-2(A.Q)(Q.kappa)P_kappa Q.                         (2.1)

Under the same exchange `Q->-Q`, all three `Q`-dependent factors in (2.1)
change sign. The common signs acquired by the two helical parent polarizations
multiply to `+1`, so the reverse ordered tree is exactly

    L_B(-Q)=-L_B(Q).                                      (2.2)

Again,

    L_(q then r)+L_(r then q)=0                           (2.3)

at leading order.

This cancellation is separate from the Fourier-reality reflection issue. It
occurs already between the two time orderings of one simultaneously present
near-opposite pump pair.

## 3. Scope correction for preceding Raman packets

The preceding exact checkers that established

* rank-five strain spans;
* pointed or bidirectional slow translation lattices;
* damping-compatible sideband geometry;
* common-Beltrami high-high silence;
* common-line Schur reduction; and
* kick--wait carrier separation

remain valid for the algebraic **one-ordered effective Raman symbol** that they
explicitly manipulate. They are not, by themselves, certificates for the
leading coefficient of the simultaneous-pump time evolution because that
coefficient contains both orderings and (1.5)/(2.3) cancel it.

In particular, the common-Beltrami repair removes high-high pump self-cascade
but also retains the ordering symmetry. It therefore does not restore the
claimed `rho^2/R` slow action.

No canonical proof-graph claim is demoted here because these packets were never
promoted to the terminal proof graph. Their scope is corrected at the research
frontier.

## 4. Residual scaling is outside the controlled Beltrami regime

After cancellation of the `O(N)` ordered terms, a slow shift scale `J=o(R)` can
supply at most an `O(J+1)` residual coefficient at the next static order. On one
high viscous clock, the corresponding action is no better than

    rho^2 J/R^2.                                          (4.1)

To keep (4.1) bounded below by a fixed `c>0` requires

    rho^2 >= c R^2/J.                                     (4.2)

The first-star Beltrami/Krein rate then satisfies

    (rho/sqrt(R))^2 >= c R/J -> infinity                 (4.3)

whenever

    J/R ->0.                                              (4.4)

Thus the subleading residual cannot simply replace the canceled leading term
while retaining the previously controlled `O(1)` Krein first-star scale.

## 5. Recomputed Raman frontier

A surviving near-opposite Raman mechanism must break the `q<->r` ordering
symmetry at leading order. There are only a few inexpensive possibilities to
test before invoking a new nonlinear preparation mechanism:

1. **different Stokes clocks:** make one parent decay substantially before the
   other;
2. **amplitude/phase imbalance:** weight the two orderings differently through
   initial complex coefficients;
3. **polarization diode:** choose parent polarizations so the target can enter
   one first high sideband but not the reverse one; or
4. **genuine autonomous ordering:** create or activate one parent only after the
   other ordering is no longer available.

The first three are algebraic/clock questions and should be eliminated or
certified exactly before any new full nonlinear construction. If all three
fail, Raman reduces to a new autonomous high-parent preparation problem and is
no longer the current shortcut around UE0/UE1.

No terminal regularity theorem, finite-time singular solution, regenerative
turnover, or `NS-R3` resolution is claimed.
