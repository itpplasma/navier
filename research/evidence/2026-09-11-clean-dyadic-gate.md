# Contamination-free first dyadic Leray gate

Date: 2026-09-11. Base branch was refreshed through
`itpplasma/navier@667c28ee253d989f4e82d54b3564ac139c9bb840` before this additive packet.

**Status: exact author algebra at the original Leray quadratic symbol; independent
audit and novelty undetermined.** This is not a closed Fourier subsystem, a
localized turnover, an exact Navier--Stokes orbit, or an unforced singularity.
No PLAN/manuscript/formal/canonical status is promoted.

The preceding dyadic-circuit packet found a genuine three-dimensional signed
carrier map whose cube doubles all wavevectors, but its original rational
polarizations generated seven unwanted first-generation real-field outputs.
The routed-packet packet then showed how the original rational geometry can
separate some parent collisions in physical space.  Here a different repair is
proved: deform the carrier geometry itself so that **all three unwanted
first-generation signed pair interactions vanish identically**, while the
three selected generations still close projectively and double scale.

## 1. Exact one-parameter clean family

For a real parameter `z`, set

    k1=(1,0,0),       a1=(0,1,z),
    k2=(0,1,0),       a2=(1,0,z),
    k3=(-z,0,1),      a3=(1,0,z).                         (1.1)

Each `a_j` is transverse to `k_j`, and

    det[k1 k2 k3]=1,                                      (1.2)

so the wavevectors span `R3` for every `z`.

Write the exact symmetric Leray pair, with only the common Fourier factor
`-i` suppressed, as

    B((p,a),(q,b))
      = P_(p+q)[(a.q)b+(b.p)a].                           (1.3)

Use the same signed gate as in the preceding circuit:

    k1'=-k1-k2,
    k2'= k1-k3,
    k3'= k1+k3,                                           (1.4)

with the corresponding exact Leray polarizations.  The three first-generation
channels which were unwanted in the original rational circuit now satisfy the
identities

    B(( k1,a1),(-k2,a2)) = 0,                             (1.5)
    B(( k2,a2),( k3,a3)) = 0,                             (1.6)
    B(( k2,a2),(-k3,a3)) = 0.                             (1.7)

These are identities in `z`, not small-error statements.  Their geometry is
transparent.  The common vector `a2=a3` is orthogonal to both `k2` and `k3`,
so the unused `2--3` pair is null for either sign.  For the `1--2` difference,

    (a1.(-k2)) a2 + (a2.k1) a1 = a1-a2=(-1,1,0),          (1.8)

which is parallel to `-(k1-k2)` and is therefore killed exactly by the Leray
projection.

Thus a real field containing only the six initial modes `+/-k_j` has, at the
quadratic first derivative, no `k1-k2` sibling and no `k2+/-k3` outputs.  Up
to conjugation, only the three selected gate children survive.

## 2. Three gates still double the wavevector geometry

The signed wavevector transformation is unchanged:

    T=[[-1,-1,0],
       [ 1, 0,-1],
       [ 1, 0, 1]],                                      (2.1)

and

    T^3=2 I.                                              (2.2)

Hence after three selected generations

    (k1''',k2''',k3''')=(2k1,2k2,2k3).                   (2.3)

The nontrivial question is whether the polarizations also return to their
original projective lines.

## 3. Projective return reduces to one explicit polynomial

Direct exact evaluation of three Leray gates gives

    a2''' = lambda2(z) a2,
    a3''' = lambda3(z) a3                              (3.1)

identically in `z`.  For the first channel the sole orientation residual is

    (a1''' x a1)_x
      = -16 z^3 Q(z) / D1(z),                            (3.2)

where `D1(z)>0` for real `z` and

    Q(z)= z^10-z^9+4z^8+2z^6-2z^5
          -8z^3-32z^2+40z-16.                            (3.3)

In particular

    Q(32/25)<0,       Q(129/100)>0,                       (3.4)

so there is a real root

    z_* in (32/25,129/100).                              (3.5)

At any root of `Q`, all three polarization lines therefore return after three
selected generations.  The exact projective multipliers may be taken as

    lambda1 =
      -32 z^3(2z^7-z^5-4z^4+8z^3-4z^2-12z+8)
      /[(z^2+2)(z^2-4z+6)(z^2-2z+2)(z^2+2z+2)],          (3.6)

    lambda2 =
       32 z^6(z^2-2)
      /[(z^2+2)(z^2-2z+2)(z^2+2z+2)],                    (3.7)

    lambda3 =
      -16 z^5(z^6-6z^4+6z^2-4)
      /[(z^2+1)(z^2+2)(z^2-2z+2)(z^2+2z+2)].             (3.8)

The companion exact checker verifies that `Q` is coprime to every numerator
in (3.6)--(3.8).  Hence no root of `Q` kills a recursive channel.  All real
denominators displayed above are strictly positive because they are products
of terms such as `(z+/-1)^2+1`, `z^2+1`, `z^2+2`, and `(z-2)^2+2`.

Numerically the positive root is approximately

    z_* = 1.284713517442987...                             (3.9)

and the corresponding multipliers are approximately

    (lambda1,lambda2,lambda3)
       =(-0.111176324,-2.048626384,5.117256637).           (3.10)

The sign pattern is therefore `(-,-,+)` at this root.  As in the previous
circuit, one can choose the three initial scalar Fourier coefficients with a
common phase `-i` and magnitudes proportional to
`(|lambda1|,|lambda2|,|lambda3|)`.  The three-generation scalar monomial map
then gives a common positive physical gain

    g = C alpha^7,
    C=|lambda1|^4 |lambda2|^2 |lambda3|^2,                 (3.11)

so any prescribed positive selected-circuit gain, including `g=5/2`, can be
represented algebraically by choosing `alpha=(g/C)^(1/7)`.  This is again a
selected-symbol gain, not an energy statement about an actual solution.

## 4. What this removes

For the original rational circuit the very first co-located generation had a
hard contamination problem: the `1--2` pair necessarily produced a sibling,
and the unused `2--3` pair produced two further signed children.  Equations
(1.5)--(1.7) show that this burden is not intrinsic to the dyadic matrix `T` or
to three-dimensional Leray geometry.  There exists a genuinely 3-D exact
projective circuit whose **initial quadratic gate is algebraically clean**.
No physical-space routing is required for that first gate.

This is stronger than merely making the unwanted coefficients small.  It also
removes the need to use nonlocal pressure tails to dispose of those three
specific first-generation outputs.

## 5. What remains open: old/new cross terms and later-generation pollution

The result does **not** make the three selected modes an invariant Fourier
subsystem.  During a real Navier--Stokes evolution the original parents do not
disappear when the first children are born.  Parent--child interactions then
create additional frequencies.  Moreover, applying the same unwanted-channel
test to the first-generation triple gives nonzero terms for generic roots of
`Q`; the algebraic cleanliness is not automatically inherited at the next
intermediate geometry.

Therefore the decisive next problem is no longer the first gate.  It is a
**full-history closure problem**:

1. quantify all parent--child and child--child outputs over one complete
   three-gate cycle;
2. determine whether their phases/geometries can cancel, remain perturbative,
   or be incorporated into a larger exact return class;
3. retain viscosity and localization;
4. obtain a state after the third gate that is admissible as the input to the
   next doubled cycle without deleting the old spectrum.

An especially sharp algebraic test is to augment the return class by the
finite set of unavoidable parent--child frequencies and ask for a projective
three-gate invariant manifold rather than a three-mode invariant set.  A
negative result should be recorded as such; another isolated carrier birth is
not the target.

## 6. Reproducibility and scope

`research/check_clean_dyadic_gate.py` freezes the exact identities above.  It
checks transversality, three-dimensionality, the three exact unwanted-channel
zeros, `T^3=2I`, the exact three-gate return obstruction `Q`, an exact rational
root bracket, squarefreeness, and coprimality of `Q` with all three multiplier
numerators.

No continuum packet estimate, time-evolution theorem, repository-wide verifier,
manuscript build, Lean build, or independent mathematical audit is supplied by
this additive packet.  NS-R3 remains unresolved and no unforced counterexample
is claimed.
