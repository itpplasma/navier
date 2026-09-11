# The factor-two source relay emits an unavoidable lower-order unstable contaminant

Date: 2026-09-11. Repository input:
`itpplasma/navier@82747b5cccc351bebd296ea5bd36429ba92e32d9`.

**Status: exact scoped obstruction to a four-coordinate self-similar relay.** The full-jet factor-two theorem remains correct: the dual-tuned four-parent cage generates all four doubled parent frequencies in their growing polarizations at quartic amplitude order. But the same dynamics necessarily creates an additional lattice sideband at **cubic** amplitude order. After factor-two renormalization this sideband is itself linearly unstable. Its frequency has a unique parent monomial, so the second designated pair or scalar phase tuning cannot cancel it while the first pair remains active.

This does not prove that every enlarged nonlinear cascade fails. It proves that the attractive four-parent factor-two cell is not closed under its own exact dynamics. A recursive construction must carry an expanding unstable state, not only the four desired parent coordinates.

The exact calculation is frozen by
`research/check_source_factor_two_pollution.py`.

## 1. Unique extreme cubic sideband

Use the four caged parent frequency keys

    5, -4, 2, -1                                          (1.1)

at axial index `z=1`, in the integer notation where key `x` means physical reference wavevector `(x/10,0,1)`.

The first designated pair is

    p_1=(5/10,0,1),
    p_2=(-4/10,0,1).                                      (1.2)

The complete source-reference Taylor expansion, including the linear source matrix, viscosity, reality partners and every quadratic ordering, generates at cubic amplitude order the sideband

    k_*=(14/10,0,1).                                      (1.3)

Among the **complete four-parent set**, the frequency `14` has exactly one representation by two positive-frequency parents and one reflected parent:

    14=5+5-(-4).                                          (1.4)

Thus its cubic coefficient is proportional to the single monomial

    A_1^2 conjugate(A_2).                                 (1.5)

No term involving the second designated pair has the same frequency. In particular, once both `A_1` and `A_2` are nonzero—as they must be for the factor-two relay—no scalar phase choice can make (1.5) vanish.

## 2. Exact growing-coordinate coefficient

With unit amplitudes for the purpose of extracting the universal coefficient, the full `t^2` Taylor coefficient at (1.3) has growing source-eigenbranch coordinate

    beta_* =
      -9/29600 [-11+20 sqrt(370)+9 sqrt(2146)].            (2.1)

This is strictly negative and hence nonzero. The sign already follows from

    20 sqrt(370) > 380 > 11.                              (2.2)

The checker obtains (2.1) from the **complete** order-two recurrence; it is not a selected-tree numerator. The coefficient is transverse to `k_*` exactly.

For general nonzero pair amplitudes, (2.1) is simply multiplied by the nonzero product (1.5), up to the fixed Fourier phase convention.

## 3. It becomes unstable one scale later

Divide frequencies by two to view the next factor-two normalized stage. The pollutant becomes

    k_*/2=(7/10,0,1/2),                                   (3.1)

whose tilt ratio is still

    s=(7/10)/(1/2)=7/5.                                   (3.2)

For the caged source viscosity `mu=3/5`, the positive-branch rate at normalized axial scale `z=1/2` is

    r_*
      =1/sqrt(1+s^2)-mu z^2(1+s^2)
      =5/sqrt(74)-111/250
      >0.                                                  (3.3)

The final inequality is certified without floating point by

    1250^2 > 111^2 * 74.                                  (3.4)

Therefore the sideband that was stable in the original `z=1` cage becomes a genuine unstable direction after the factor-two rescaling.

## 4. Order comparison with the desired relay

The unwanted mode (1.3) first appears in `U_2`, i.e. cubic amplitude order.
The four desired doubled-parent growing coordinates in
`2026-09-11-source-factor-two-relay.md` first appear in `U_3`, i.e. quartic amplitude order.

Hence for a small common parent amplitude `epsilon`, before any later stagewise amplification,

    unwanted unstable seed = O(epsilon^3),
    desired doubled-parent seeds = O(epsilon^4).           (4.1)

The contaminant is parametrically larger by one inverse power of the small amplitude. The four-parent relay therefore cannot be iterated perturbatively while retaining only the four desired growing coordinates.

## 5. Recomputed cascade question

The factor-two result has not become useless. It proves that the source dynamics contains a genuine upward frequency relay. What fails is **finite-dimensional closure**.

At a factor-two rescaling, lower-frequency lattice modes experience weaker viscosity. More `z=1/2` lattice sites are unstable than the four `z=1` parent sites. The cubic pollutant is the first explicit example and is unavoidable.

A surviving nonlinear-prehistory route must therefore do one of two things:

1. construct and control an **expanding / ultimately infinite unstable cascade state**, including the sidebands that become unstable after each rescaling; or
2. find a new interference/geometry that cancels the lower-order unstable pollutants while retaining the quartic factor-two outputs.

Because the extreme mode (1.3) has a unique cubic monomial, the second option cannot be achieved by retuning the existing four parent amplitudes alone. It requires genuinely new parent geometry or additional modes whose cubic frequencies coincide with the extreme pollutant.

The immediate discriminator is whether the number of unstable lattice sites necessarily grows without bound under repeated factor-two rescaling. If it does, the present four-parent architecture has reduced the terminal problem to an infinite-dimensional cascade/control problem rather than a repeated finite cell.

## 6. Scope

No statement is made that an infinite-dimensional cascade cannot be controlled. No global parent supply, common Schwartz trace, nonlinear de-forcing solution, singularity preservation or `NS-R3` theorem is claimed. Independent mathematical audit and novelty assessment remain pending.
