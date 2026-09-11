# One common strain discriminates all three clean second-generation targets

Date: 2026-09-11. This packet removes the apparent need to spatially separate
the three ancestry-contaminated second-generation target modes merely in order
to polarize them.

**Status: exact author carrier theorem; independent audit and novelty
undetermined.** The theorem is for affine Kelvin rates.  The repository's
finite-energy localized-strain theorem provides a route to a compact short-time
version, but a full mixed-packet purification theorem and regenerative turnover
are still separate steps.

## 1. Target and rejected directions

At each nominal second-generation target

    h_+=(0,1,1),
    h_0=(-2,-1,-1),
    h_-=(0,-1,1),                                         (1.1)

let `k_j` be its physical wavevector and let `v_j` be the intended selected-gate
polarization from the exact quartic/order-three Taylor calculation.  Each
`v_j` is transverse to `k_j`.

The full co-located Taylor coefficient has a nonzero component along `v_j` by
`2026-09-11-clean-gate-purifiable-second-targets.md`.  Define the unique
transverse rejected direction, up to scale, by

    f_j=k_j cross v_j.                                    (1.2)

Then

    k_j.v_j=k_j.f_j=v_j.f_j=0.                            (1.3)

A mode coefficient at target `j` therefore decomposes uniquely into intended
and rejected polarization components along `(v_j,f_j)`.

## 2. One rational trace-free matrix works for all three

Set

    S = [[ 9/8,   1/36,   1/4 ],
         [ 1/36, -1/5,    1/14],
         [ 1/4,   1/14, -37/40]].                         (2.1)

This matrix is real, symmetric, and trace free.

Let `z_*` be the unique positive clean-circuit root in

    1.2847 < z_* < 1.2848.                                (2.2)

Exact rational-function sign checks on this whole isolating interval give,
for every `j in {+,0,-}`,

    v_j^T S v_j < 0,                                      (2.3)

    f_j^T S f_j > 0.                                      (2.4)

Numerically, after unit normalization, the three intended quadratic forms are
approximately

    -0.5311,  -0.4952,  -0.4965,                          (2.5)

while the three rejected forms are approximately

     0.4870,   0.4988,   0.4915.                          (2.6)

The near symmetry of these margins was not imposed; it emerged from the
five-parameter trace-free feasibility problem and was then rationalized to
(2.1).

## 3. Strength 10 beats viscosity on every desired target

For a common carrier scale `b`, use the affine strain background

    U(x)=10 nu b^2 S x.                                   (3.1)

For a transverse carrier `(b k,a)`, the instantaneous logarithmic amplitude
energy rate divided by `nu b^2` is

    R(k,a)=-10 (a^T S a)/|a|^2-|k|^2.                    (3.2)

The exact checker proves on the entire root interval (2.2) that

    -10 v_j^T S v_j - |k_j|^2 |v_j|^2 > 0                (3.3)

for all three targets.  Hence

    R(k_j,v_j)>0.                                         (3.4)

For the rejected directions, (2.4) immediately gives

    R(k_j,f_j)<-|k_j|^2<0.                                (3.5)

Thus **one and the same affine strain simultaneously amplifies all three
intended second-target polarizations and damps all three transverse rejected
polarizations**.

This is materially stronger than three independent mode-specific affine
purifiers.  It removes the algebraic incompatibility that motivated a
three-station purifier router.

## 4. Consequence for the architecture

The current chain can now be reorganized as

    clean co-located first gate
      -> ancestry-contaminated second-target modes
      -> one common polarization-discriminating strain region
      -> purified three-target triple
      -> next nonlinear gate.                             (4.1)

Spatial separation is no longer required *for polarization discrimination
itself*.  The difficult PDE task becomes more local:

1. realize the common strain (2.1) as a finite-energy background on the same
   region occupied by the three target packets;
2. prove a finite-time **mixed-packet** statement, not merely separate growth
   tests for six individually prepared directions;
3. control old parents, ladder modes and off-target frequencies during the
   strain interval;
4. show the resulting three desired components have the spatial envelopes and
   relative phases needed for the next gate.

The concurrent finite-energy localized-strain amplifier already proves that a
compact exact strain germ can produce strict short-time growth/decay on the
correct parabolic scale.  Since (2.1) gives uniform strict margins on six
finite carrier directions, standard finite-dimensional perturbation of that
argument is now a plausible route to item 2.  It still has to be written and
checked; separate-solution energy inequalities alone are not a mixture
purification theorem.

## 5. Why the closed-strain-loop wall is not contradicted

The closed-loop wall concerned an affine deformation that first separates
parents/children and then restores the original carrier geometry.  Its net
viscous action is one positive quadratic form in wavevector and the
parallelogram identity forbids simultaneous parent erasure.

Here no closed deformation is asserted.  Matrix (2.1) is used as a local
polarization discriminator on the already-born target triple.  The next gate
must be proved from the actual post-strain state; no inverse strain is silently
inserted.

## 6. Reproducibility

`research/check_common_second_target_strain.py` records the exact rational
matrix (2.1), reconstructs all three intended target vectors, their orthogonal
rejected directions, isolates the clean root, and proves (2.3)--(3.5) by exact
polynomial root counting and rational sign checks.

No finite-time common mixed-packet purifier, exact second gate in the original
finite-energy solution, recursive turnover, or NS-R3 conclusion is claimed.
