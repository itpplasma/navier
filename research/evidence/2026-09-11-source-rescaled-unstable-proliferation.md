# Factor-two source rescaling has no fixed finite unstable cage

Date: 2026-09-11. Repository input:
`itpplasma/navier@3bf9aded944dfb4f24e902ddc0aa491846008be9`.

**Status: exact source-reference linear spectral theorem.** The cubic pollution in the factor-two relay is not an isolated extra unstable direction. Under repeated factor-two rescaling, the number of linearly unstable lattice sites grows without bound. Consequently no fixed finite-dimensional source cage can be invariant under a recursive factor-two relay, even before nonlinear amplitudes, finite-`L` corrections, localization or pressure/exterior errors are considered.

This does not exclude an infinite-dimensional cascade or a stage-dependent expanding unstable manifold. It sharply identifies that as the remaining constructive object.

The exact arithmetic is frozen by
`research/check_source_rescaled_unstable_proliferation.py`.

## 1. Positive-branch rate on the rescaled lattice

For the caged source reference system with viscosity

    mu=3/5,                                                (1.1)

the positive-branch rate at normalized axial scale `z>0` and tilt `s` is

    r_+(z,s)
      =1/sqrt(1+s^2)-mu z^2(1+s^2).                       (1.2)

At the original parent scale `z=1`, the caged lattice has tilt sites

    s_m=(3m-1)/10,
    m in Z.                                                (1.3)

After `j` factor-two rescalings, a frequency inherited without the corresponding axial doubling sits at relative scale

    z_j=2^(-j).                                            (1.4)

For the same tilt index `m`, positivity of (1.2) is equivalent to

    (1+s_m^2)^(3/2) < 1/(mu z_j^2).                       (1.5)

All quantities are positive, so squaring gives the exact rational criterion

    (1+s_m^2)^3 < (25/9) 16^j.                            (1.6)

No numerical eigenvalue computation is required.

## 2. Exact early unstable intervals

Applying (1.6) gives the consecutive unstable integer intervals

    j=0:   -1 <= m <=  2,       4 sites,
    j=1:   -4 <= m <=  5,      10 sites,
    j=2:   -9 <= m <=  9,      19 sites,
    j=3:  -15 <= m <= 15,      31 sites,
    j=4:  -24 <= m <= 25,      50 sites.                  (2.1)

The adjacent integer sites on both sides fail (1.6), so these intervals are exact.

In particular the cubic pollutant isolated in
`2026-09-11-source-factor-two-pollution-wall.md` is `m=5`: it is stable in the original `j=0` cage and unstable already at `j=1`.

## 3. Unbounded proliferation theorem

Fix any `M>=1`. For all `|m|<=M`,

    1+s_m^2 <= Q_M^2                                     (3.1)

for a finite rational `Q_M^2`. Since the right side of (1.6) grows like `16^j`, choose finite `j` with

    Q_M^6 < (25/9)16^j.                                   (3.2)

Then every lattice site

    |m|<=M                                                 (3.3)

has positive linear growth at that rescaled stage.

Therefore

    number of unstable lattice sites -> infinity          (3.4)

under repeated factor-two rescaling.

Quantitatively the unstable tilt radius grows like `z_j^(-2/3)`, so the number of unstable `m` sites grows on the order of `2^(2j/3)`.

## 4. Consequence for the four-parent relay

The original all-orders spectral cage is a valid **single-stage** theorem: at `z=1` exactly four positive-branch sites grow. The factor-two relay theorem proves that those four can seed their doubled-frequency copies. But the rescaled state also contains lower-frequency sidebands. As the normalization advances, viscosity weakens on those inherited modes and more lattice sites cross into the unstable spectrum.

The cubic `m=5` pollutant proves this is not a merely hypothetical spectral enlargement: at least one newly unstable direction is unavoidably populated one nonlinear order earlier than the desired relay.

Thus a recursive proof cannot have the form

    four parents -> four parents -> four parents -> ... . (4.1)

Nor can it be repaired by selecting any other **fixed finite number** of inherited lattice coordinates as the stage state: eventually additional retained lattice sites become linearly unstable.

## 5. Recomputed constructive problem

A surviving source-prehistory cascade must now control an expanding, ultimately infinite unstable state. The next mathematical questions are:

1. whether the exact full convolution has a stage-dependent unstable-manifold / graph transform whose dimension expands according to (3.4) while its physical amplitudes remain summable from one Schwartz trace;
2. whether the newly unstable directions generated at lower nonlinear order inevitably dominate the desired source-parent coordinates and destroy the pulse geometry; or
3. whether a larger interference architecture can force the populated state into a codimension-growing subspace that avoids the newly unstable sites.

The existing four amplitudes cannot cancel the explicit extreme `m=5` cubic monomial, so option 3 requires genuinely new modes/geometry, not retuning the current cell.

The alternative terminal route is the complete physical adjoint / minimum-prefix-control test: prove that any bounded correction attempting to populate this expanding unstable family has divergent control cost or violates the nonlinear de-forcing budget.

## 6. Scope

This is a linear spectral/architecture theorem, not a blow-up or global regularity result. It does not prove that every newly unstable mode has nonzero amplitude, although one such mode (`m=5`) is already proved unavoidable. It does not rule out infinite-dimensional nonlinear cascade control. No common Schwartz trace, full nonlinear de-forcing, singularity preservation or `NS-R3` conclusion is claimed. Independent audit and novelty assessment remain pending.
