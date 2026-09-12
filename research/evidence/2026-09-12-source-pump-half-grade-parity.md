# Even-grade source pumping cannot create the half-grade odd sector from zero

Date: 2026-09-12. Repository input before integration: `itpplasma/navier@28652ef900904a684d6ed221c344198fffd34f21`.

**Status: exact physical phase-parity theorem plus exact frozen local Leray pump coefficients; independent mathematical audit and novelty assessment pending.** This is the first causal-supply checkpoint after the local six-mode bridge was closed. It rules out zero-seed production of the half-grade ancestor sector by the already-present source wave alone, while showing exactly what that wave can do once a nonzero odd-grade seed exists.

## 1. Prediction before the test

At one relay step the six half-grade ancestors have physical phase grade `m`, whereas the previous pure source daughter has grade `2m`. The local source mean/background has grade zero. Products and linear source-wave couplings add physical Fourier integers.

Prediction: if the correction contains no odd multiple of `m`, the full correction equation cannot create one from the source background, because the source itself contains only even multiples of `m`. Thus the half-grade sector is an invariant zero sector. The previous daughter may nevertheless couple existing odd modes in complementary pairs.

## 2. Exact parity closure

Measure physical phase integer in units of `m` and reduce modulo two. The local prescribed source is generated from

    grade 0 mean/background,
    grade 2 primary daughter,

and their physical operations. Slow differentiation, curls, pressure reconstruction, diffusion and axisymmetric localization preserve grade, while wave products add grades. Hence every source coefficient and every source residual lies in the even class.

Write the exact correction equation schematically as

    w_t = L_(U_even) w + N(w,w) + f_even.

If `w` initially contains only even grades, then

* `L_(U_even) w` is even because even+even is even;
* `N(w,w)` is even because even+even is even; and
* `f_even` is even.

By uniqueness of the local classical/mild correction flow, the odd sector remains exactly zero. No asymptotic estimate or smallness argument is involved.

Therefore the source daughter cannot create the first half-grade `m` ancestor from an exactly zero odd sector. A successful parametric route still needs at least one nonzero odd-grade seed somewhere in its causal ancestry.

## 3. The previous daughter pump splits the six modes into three pairs

After factor-two normalization, the previous pure daughter has wavevector

    d=(1/20,0,1)

and physical grade `2m`. Its polarization is the decaying source eigenvector at tilt `1/20`.

The six half-grade ancestor keys are

    14,-13,5,-4,2,-1,

with `h_x=(x/20,0,1/2)`. The exact relation `d=h_a+h_b` is equivalent to

    a+b=1.

Among the six keys this gives precisely the three complementary pairs

    (14,-13),    (5,-4),    (2,-1).

Thus a positive pump interacting with the reality partner of one member can create the other member at the linearized level.

## 4. All six pump-transfer coefficients are nonzero

Use the full unordered Leray symbol with pump polarization `a_-(1/20)` and project the output onto the growing half-grade source eigenvector. For each pair `(a,b)`, let `gamma_a` be the growing projection of

    C(d,a_- ; -h_b,a_+(b/10))

onto `h_a`, and define `gamma_b` analogously.

Exact rational radical enclosures give

    (14,-13):
      gamma_14 in
        [940334275827/11840000000000,
         940334275881/11840000000000] >0,
      gamma_-13 in
        [-396515826369/5380000000000,
         -317212661079/4304000000000] <0,

    (5,-4):
      gamma_5 in
        [326753665209/2000000000000,
         81688416309/500000000000] >0,
      gamma_-4 in
        [-813331185039/4640000000000,
         -162666236997/928000000000] <0,

    (2,-1):
      gamma_2 in
        [11438852967/160000000000,
         74352544287/1040000000000] >0,
      gamma_-1 in
        [-23788850559/323200000000,
         -297360631983/4040000000000] <0.

Hence every directional transfer is genuinely present.

For a fixed real pump phase, the projected 2-by-2 submatrix in variables `(x_a,conj x_b)` has off-diagonal product proportional to

    gamma_a gamma_b <0

in all three blocks. This projected pair contribution is elliptic. It is not a stability theorem for the full linearized system: both polarizations and the infinite chains of pump-shifted axial grades must also be retained. The ordinary source-reference rates remain separate.

## 5. Exact single-pump limitation

The pump complement map is

    a -> 1-a.

On the six-key set it consists of exactly the three disjoint two-cycles above. The six half-grade modes do not form a closed linearization: pump shifts also create other axial grades. The invariant linear classes are instead the additive charge n=(2x-z)/3 in integer keys k=(x/20,0,z/2). With reality the displayed pairs occupy |n|=9,3,1, respectively. An entire charge class initialized zero stays zero under the single-pump linearization; each class includes all of its pump-shifted sidebands. See the complete-chain correction in 2026-09-12-one-seed-ladder-balance.md.

Thus one seed confined to one charge class cannot linearly reach the other two classes. Nonzero projected pair transfer does not assert independent endpoint controllability within a class, and the source cannot eliminate odd-grade seeding altogether.

This is deliberately scoped to the single-pump linearization. The full nonlinear correction can generate grade-zero difference shears from an occupied pair, and those shears can couple different half-grade keys. That is a genuinely different mechanism and is not excluded here.

## 6. Recomputed frontier

The zero-seed parametric shortcut is closed by exact phase parity. The next constructive question is whether **one nonzero odd seed can spread nonlinearly across the six-mode state**. The inner pair is the natural candidate: pump transfer can create `-1` from key `2`; their difference produces a grade-zero radial shear of key `3`; such a shear shifts half-grade keys by three. This suggests the ladder

    2 -> 5 -> 8 -> 11 -> 14,
    -1 -> -4 -> -7 -> -10 -> -13,

which would populate all six bridge ancestors from one odd seed if the complete ordered trees do not cancel.

The repository already contains a distinct prescribed-shear infinite-lattice transmission theorem, but it does not compose automatically with a dynamically generated shear. The next discriminator must therefore test the dynamic handoff itself, retaining all same-order paths.

No common Schwartz trace, physical whole-space seed delivery, nonlinear de-forcing solution, singularity preservation, or `NS-R3` conclusion is claimed.

Companion checker: `research/check_source_pump_half_grade_parity.py`.
