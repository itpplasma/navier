# Review of HF23, Scope A: the unweighted div–curl estimate and its consequences

Independent proof audit, 2026-09-06. Lens: reconstruct every implication from
the first nontrivial one, recompute every constant and exponent, check
quantifiers, function spaces and solution class, and attempt to refute each new
fact by an explicit example, scaling family, or numerics.

Scope A covers §2 "Variational and evolution preliminaries", §3 "An unweighted
div–curl estimate for the actual minimizer", §4 "The divergence defect and an
unconditional mixed-pressure pairing", and §5 "Unconditional spacetime budgets
and the first surviving gap". Sections 6–9 (the HF20 reconstruction, the
spacetime obstruction, the conditional continuation and the literature section)
are **not** audited here.

## Freeze

| object | identity |
|---|---|
| research HEAD at audit time | `928713dcc012adbbea279d681d5298d5a887fcfb` |
| target | `research/evidence/hf23-divcurl-continuation.tex`, 1129 lines, sha256 `abe74421ef6a8a7bacc108c0c08834e32f2a6116530fceb00368c8e67b129075` |
| index note | `research/evidence/hf23-divcurl-continuation.md` |
| manuscript compared | `../navier-paper/main.tex` at `4084330f6b8130241c7afbde3878861229c4cceb`, `sec:quotient` |
| audited inputs consulted | `hf18-divergence-speed-link.md`, `hf21-shifted-hodge-regularity.md` |

The candidate's own pinned revisions (`1014e7e`, `39ccb66`, `54f8e89`) are
earlier than the heads above; nothing in Scope A depends on the difference.
The HF20 hash it quotes matches `PLAN.md`.

## Verdict summary

**PASS.** Scope A contains no invalid or unsupported bridge. Every step of
Theorem 3.1 (`thm:main`), Corollary 4.1 (`cor:sigma`), Theorem 4.2
(`thm:mixed`) and Corollary 5.1 (`cor:budgets`) was reconstructed
independently; every constant — `1/32`, `1/3`, `1/4`, `5/4`, `1/2`, `5/8`,
`5E_0/(8ν)`, `E_0/(8ν)` — was recomputed and is correct as displayed. Nine
refutation attempts failed, including direct numerical minimization of the
cubic functional on `T^3` at four resolutions on 87 distinct data, which the
proof covers verbatim.

The one structural surprise is favourable and should be recorded: **the proof
of `thm:main` uses no repository result at all.** The controller's note calls
HF21-A Theorem 1 (`curl w = curl u`) "one pillar of this candidate"; in fact
the candidate re-derives that identity for the regularized minimizer from
scratch at `eq:regconstraints`, in two lines, so HF23 is logically independent
of HF21-A, of HF18-A/B and of HF20. There is no circularity and no inherited
risk from the HF21-A repair.

Three **expository repairs** are supplied below (R1–R3). None of them changes
a statement, a constant or a consequence; R2 closes a one-line reasoning gap
that is currently asserted rather than proved, and R3 records the sharp form of
the matrix lemma, which the note's own proof already establishes.

The candidate's stated boundary is accurate: it does **not** prove (H2), does
**not** give `w ∈ L^2`, and does **not** establish the arbitrary-data signed
spacetime bound. The first genuinely open step is exactly where the note puts
it, at `eq:firstgap`.

---

## 1. The regularized problem (audit item 1)

`X = L^2 ∩ L^3` with `‖z‖_X = ‖z‖_2 + ‖z‖_3`; `G_X` the `X`-closure of
`{∇φ : φ ∈ C_c^∞}`; data `u ∈ H^m`, `m ≥ 4`.

**Well-posedness. Confirmed.** `u ∈ H^4` gives `u ∈ L^2`, `u ∈ L^6` hence
`u ∈ L^3`, and `∇u ∈ H^3 ⊂ L^2 ∩ L^∞ ⊂ L^2 ∩ L^3`; so `u ∈ X` and the
admissible class `u + G_X` is nonempty, closed, convex, hence weakly closed.
`X` is reflexive as a closed subspace of `L^2 ⊕ L^3`. The growth relations
`eq:regularizer-growth` were re-derived from `f_δ(z) = ∫_0^{|z|} s√(δ²+s²) ds`
using `s ≤ √(δ²+s²) ≤ δ + s`; all three are correct, and the two lower bounds
`f_δ ≥ |z|³/3` and `f_δ ≥ δ|z|²/2` coerce both components of the `X` norm.
`F_δ` is convex and strongly lower semicontinuous (Fatou along an a.e.
subsequence), hence weakly lsc. Direct method gives existence.

**Uniqueness. Confirmed, and for the stated reason.**
`D²f_δ(z) = Dj_δ(z) = r_δ(z) I + z⊗z/r_δ(z) ≻ 0` for every `z`, so `f_δ` is
strictly convex on `R^3` — note this is *strict for all `z` including `z = 0`*,
unlike `|z|^3/3`, which is the point of the regularization. Uniqueness follows.

**Euler–Lagrange. Confirmed.** `|j_δ(z)| = r_δ(z)|z| ≤ δ|z| + |z|²`, so
`j_δ(w_δ) ∈ L^2 + L^{3/2} = X^*`, and differentiation under the integral in
`s` on `|s| ≤ 1` is dominated by `δ‖w_δ+sg‖_2‖g‖_2 + ‖w_δ+sg‖_3²‖g‖_3`. Hence
`eq:regstationary`, and with `g = ∇φ`, `div j_δ(w_δ) = 0` in `D'`. Since `G_X`
is contained in the `L^3`-closure `G_3` and curls of gradients vanish,
`curl w_δ = curl u` in `D'`. Both parts of `eq:regconstraints` hold.

**Is the fixed-`δ` weak derivative proved before it is used? YES.** This is
the place a circular use of the conclusion would hide, and it is not there.
The order in the source is: (i) solve in `X`, using only convexity and
coercivity, no derivative of `w_δ`; (ii) prove `w_δ ∈ H^1` by translation
differences, using only the stationarity identity and the pointwise monotonicity
of `j_δ`; (iii) only then divide the Euler–Lagrange equation pointwise. Step
(ii) is genuinely derivative-free:

- `G_X` is translation invariant (translation is an `X`-isometry mapping
  `C_c^∞` gradients to `C_c^∞` gradients), so translating `eq:regstationary`
  is legitimate and `τ_h q_δ − q_δ` is an admissible test field. Subtracting
  the two identities and inserting
  `τ_h q_δ − q_δ = (τ_h w_δ − w_δ) − (τ_h u − u)` gives `eq:diff-test`
  exactly.
- **Lemma `lem:regmono` recomputed.** Eigenvalues of `Dj_δ(z)` are `r_δ(z)`
  (twice) and `(δ²+2|z|²)/r_δ(z) ∈ [r_δ, 2r_δ]`; the upper bound
  `eq:reglip` follows from `r_δ(z(t)) ≤ δ + max(|a|,|b|) ≤ B_δ(a,b)`. For the
  lower bound with `M = max(|a|,|b|) = |a|`: on `3/4 ≤ t ≤ 1`,
  `|z(t)| ≥ |a| − (1−t)|a−b| ≥ M − (1/4)(2M) = M/2`, so
  `∫_0^1 r_δ(z(t)) dt ≥ (1/4)(M/2) = M/8 ≥ (|a|+|b|)/16`; the integral is also
  `≥ δ`; half the sum is `≥ (δ + |a| + |b|)/32`. The constant `1/32` is
  correct (not optimal, and nothing downstream uses optimality).
- The weighted Cauchy–Schwarz step and the division are correct, giving
  `W_h ≤ 64² ∫ B_h |τ_h u − u|²`, and Hölder with `‖τ_h w_δ‖_3 = ‖w_δ‖_3`
  gives `eq:difference-bound` with the universal constant `C = 4096`.
- `B_h ≥ δ` then yields
  `‖(τ_h w_δ − w_δ)/h‖_2² ≤ C(‖∂_k u‖_2² + 2δ^{-1}‖w_δ‖_3 ‖∂_k u‖_3²)`,
  uniform in `h` at fixed `δ`, and finite precisely because `u ∈ H^m` supplies
  `∂_k u ∈ L^2 ∩ L^3`. The weak-limit identification of the difference
  quotient is written out and needs no elliptic regularity theorem, as claimed.

The `δ^{-1}` is explicit and the note flags that this bound is **not** uniform
in `δ`. That is correct and is not a defect: the uniform bounds come later from
a different mechanism.

## 2. The Euler–Lagrange equation and the pointwise constraint (audit item 2)

**Chain rule. Confirmed.** `j_δ ∈ C^1(R^3;R^3)` with `j_δ(0) = 0` and
`|Dj_δ(z)| ≤ 2r_δ(z) ≤ 2(δ+|z|)`. With `w_δ ∈ H^1 ⊂ L^6`,
`Dj_δ(w_δ)∇w_δ` is bounded by `2(δ + |w_δ|)|∇w_δ| ∈ L^2 + L^{3/2}`
(`|w_δ||∇w_δ| ∈ L^{3/2}` by `1/6 + 1/2 = 2/3`), so the `C^1` chain rule applies
and the distributional divergence of `j_δ(w_δ)` is the a.e. function
`∂_i(j_δ(w_δ))_i`. Being zero as a distribution and locally integrable, it is
zero a.e.

**The a.e. identity. Confirmed, with one step to display (repair R1).**
`∂_i r_δ(w) = w_k ∂_i w_k / r_δ(w)`, so
`0 = r_δ div w + (w_i w_j / r_δ) ∂_i w_j` a.e., which is the note's display.
The step the note leaves implicit is that `w_i w_j ∂_i w_j = |w|² e^T S e`,
because contraction against the *symmetric* tensor `w ⊗ w` symmetrizes `∇w`.
This is what makes the whole argument a statement about `S = sym ∇w` rather
than about `∇w`, and it should be displayed. Dividing by `r_δ ≥ δ > 0`,

    d_δ + t_δ e_δ^T S_δ e_δ = 0,     t_δ = |w_δ|²/(δ² + |w_δ|²).

**`t ∈ [0,1]`. Confirmed** — in fact `t_δ ∈ [0,1)` strictly for `δ > 0`, and
`Lemma lem:matrix` is stated on the closed interval, so this is safe.

**The zero set (repair R2).** The note says only "At zero points choose any
unit vector; `t_δ = 0` makes that choice irrelevant." Taken literally this
shows only that the *right-hand side* of the constraint is zero; it does not
show that the constraint *holds*, i.e. that `d_δ = 0` there. It does hold, and
the reason is a one-line consequence of the regularization that deserves to be
printed: on `{w_δ = 0}` the a.e. equation reads `δ · div w_δ = 0` with
`δ > 0`, hence `d_δ = 0` a.e. there, and the constraint holds with any `e`.
**This is exactly where the regularizer earns its keep**: in the unregularized
equation the same points give `0 = 0` and carry no information, which is the
content of the note's own `Remark 3.6`. With R2 inserted, the constraint holds
a.e. on all of `R^3`.

## 3. The matrix lemma, independently (audit item 3)

**Statement.** Let `S` be a real symmetric `3×3` matrix, `e ∈ S²`, `t ∈ [0,1]`,
`d = tr S`, and suppose `d = −t e^T S e`. Then `d² ≤ (1/3)|S|_F²`.

**Independent proof.** If `t = 0` the constraint gives `d = 0`. If `t > 0`,
rotate so `e = e_1`: then `S_11 = −d/t` and `S_22 + S_33 = d − S_11 = d + d/t`.
Dropping the six off-diagonal squares and using `a² + b² ≥ (a+b)²/2`,

    |S|_F² ≥ d²/t² + (1/2)(d + d/t)² = d² (t² + 2t + 3)/(2t²).

`(t²+2t+3)/(2t²) ≥ 3` is `3 + 2t − 5t² ≥ 0`, i.e. `−(5t+3)(t−1) ≥ 0`, true on
`[−3/5, 1] ⊇ [0,1]`, with equality exactly at `t = 1`. Reproduced exactly.

**Repair R3: the proof gives the sharp form, which should be recorded.**

> **Lemma (sharp trace control).** Under the same hypotheses,
> `d² ≤ (2t²/(t²+2t+3)) |S|_F² ≤ (1/3)|S|_F²`. For each `t ∈ (0,1]` the first
> inequality is attained, in an orthonormal frame with `e` first, by
> `S = diag(−d/t, (d/2)(1+1/t), (d/2)(1+1/t))`.
>
> *Proof.* The displayed chain is the whole proof; the two discarded quantities
> are `Σ_{i≠j} S_ij²` and `(S_22 − S_33)²/2`, and both vanish for the stated
> `S`. That `S` has `tr S = −d/t + d + d/t = d` and `e^T S e = −d/t`, so the
> constraint `d = −t e^T S e` holds, and
> `|S|_F² = d²/t² + (d²/2)(1+1/t)² = d²(t²+2t+3)/(2t²)`.
> `t ↦ 2t²/(t²+2t+3)` has derivative of the sign of `2t² + 6t > 0` on `(0,1]`,
> so it increases to the value `1/3` at `t = 1`. ∎

Consequence worth stating in the repository: the constant `1/3` is the
`t → 1` endpoint, i.e. the bound does **not** degenerate as `δ ↓ 0`, and no
`δ`-dependent loss enters. That is the entire reason uniformity in `δ` is
available, and it is the load-bearing observation of the whole paper.

**Numerics (evidence, not proof).** `4·10^5` random `(S, e, t)` with the
constraint imposed exactly by solving for the trace: **zero violations**, and
`max d²/|S|_F² = 0.32822`, attained at `t = 0.99985`. On the equality family
above, `d²/|S|_F²` matched `2t²/(t²+2t+3)` to nine digits at
`t = 1, 0.999, 0.9, 0.5, 0.1`. **The constraint does the work**: for `S = I`
one has `d² = 9` and `|S|_F²/3 = 1`, so the unconstrained inequality is false
by a factor of nine, and the constraint fails there (`−t e^T S e = −t ≠ 3`).

## 4. The div–curl identities and the combination (audit item 4)

Both identities of `eq:hodge` were re-derived by Plancherel for `z ∈ H^1`:
`∫|ξ×ẑ|² + ∫|ξ·ẑ|² = ∫|ξ|²|ẑ|²`, and
`|sym∇z|_F² = (1/2)Σ(∂_j z_i)² + (1/2)∂_j z_i ∂_i z_j` integrates to
`(1/2)‖∇z‖² + (1/2)‖div z‖² = (1/2)‖curl z‖² + ‖div z‖²`. Correct, and
independent of the `2π` convention.

The combination is then forced:
`D_δ ≤ (1/3)‖S_δ‖_2² = (1/3)(D_δ + C/2)`, hence `(2/3)D_δ ≤ C/6`, hence
`D_δ ≤ C/4`, and `‖∇w_δ‖_2² = ‖curl w_δ‖² + D_δ = C + D_δ ≤ 5C/4`. Both
constants confirmed.

- The use of `curl w_δ = curl u` is `eq:regconstraints`, proved in the note
  itself; it is *also* HF21-A Theorem 1, but the candidate does not import it.
- `C = ‖curl u‖_2² = ‖∇u‖_2²` is exactly the first identity of `eq:hodge`
  applied to `u` with `div u = 0`. **Solenoidality is used, and only here.**
  Without it the theorem would read `‖∇w‖² ≤ ‖curl u‖² + (1/4)‖curl u‖²`,
  which is a different (and for non-solenoidal data, weaker) statement.
- `eq:qdelta` needs `q_δ = w_δ − u ∈ H^1`, which holds since `u ∈ H^m` and
  `w_δ ∈ H^1`; `q_δ` is curl free, so `‖∇q_δ‖² = ‖div q_δ‖² = D_δ`. Confirmed.

## 5. The crux: uniformity and passage to the limit (audit item 5)

This is the step the index note flags as the crux, and it is correct. The
danger it names — "a bound uniform in the regularizer for objects converging to
something else" — is explicitly excluded by the argument.

1. `F(w_δ) ≤ F_δ(w_δ) ≤ F_δ(u) ≤ F(u) + (δ/2)‖u‖_2²` bounds `w_δ` in `L^3`
   for `0 < δ ≤ 1`. Weak `L^3` limits `w̄` along subsequences exist and lie in
   `u + G_3`, because `q_δ ∈ G_X ⊂ G_3` (`X`-convergence implies
   `L^3`-convergence) and `G_3` is a closed subspace, hence weakly closed.
2. The upper bound is the decisive move and it is correct. Pick
   `g_m = ∇φ_m ∈ C_c^∞` with `g_m → w − u` in `L^3`, which exists by the
   definition of `G_3`. Each `u + g_m ∈ X` is admissible for **every**
   regularized problem, so `F_δ(w_δ) ≤ F_δ(u + g_m)` for every `δ` and `m`;
   letting `δ ↓ 0` at fixed `m` gives `limsup F_δ(w_δ) ≤ F(u + g_m)`, using
   `|F_δ(z) − F(z)| ≤ (δ/2)‖z‖_2²` and `u + g_m ∈ L^2`. Then `m → ∞` and
   continuity of `F` on `L^3` give `limsup F(w_δ) ≤ F(w) = Q(u)`.
   **Note the quantifier order is the safe one**: the `L^2` norm that blows up
   as `m → ∞` never has to be controlled, because `δ → 0` is taken first at
   fixed `m`. The note states this ("It does not assume that `w − u` can be
   approximated in `L^2`") and the statement is accurate.
3. Weak lower semicontinuity gives `F(w̄) ≤ liminf F(w_δ) ≤ F(w)`;
   admissibility gives `F(w̄) ≥ Q(u) = F(w)`; so all are equalities and
   strict convexity forces `w̄ = w`. **The regularized minimizers do converge
   to the actual `L^3` minimizer.** Norms converge too, so uniform convexity
   of `L^3` (Radon–Riesz) upgrades to `w_δ → w` strongly in `L^3`. Every
   subsequence argument, hence the full limit. Correct.
4. Lower semicontinuity is then used correctly and in the right direction:
   `∇w_δ` is bounded in `L^2` and `w_δ` in `L^6` by the **δ-uniform**
   `eq:uniform-h1`; weak limits exist; strong `L^3` convergence identifies
   them as `∇w` and `w` distributionally (`∫∇w_δ φ = −∫w_δ ∇φ → −∫w∇φ`);
   and `‖∇w‖_2 ≤ liminf ‖∇w_δ‖_2` transfers `5C/4`, `‖div w‖_2 ≤ liminf` 
   transfers `C/4`. No constant is lost and none is claimed to improve.
5. `w ∈ W^{1,2}_loc` because `w ∈ L^6 ⊂ L^2_loc` and `∇w ∈ L^2`. The
   statement understates what is proved: `w` and `q` lie in `Ḣ^1(R^3)` in the
   `L^6`-representative sense, globally.
6. The equality `‖∇q‖_2² = ‖div w‖_2²` is proved by cutoff, and correctly.
   `χ_R q ∈ H^1`, `eq:hodge` applies to it, and the error terms are controlled
   by `‖q ∇χ_R‖_2 ≤ ‖∇χ_R‖_3 ‖q‖_{L^6(R≤|x|≤2R)}` with `1/3 + 1/6 = 1/2` and
   `‖∇χ_R‖_3 = ‖∇χ‖_3` independent of `R`. Both facts recomputed; correct.

**Verdict on the crux: sound.** The bound is uniform in `δ` *and* the objects
converge to the intended limit, and the two facts are established by
independent arguments.

## 6. Extension from `H^m` to every solenoidal `H^1` input (audit item 6)

`u_n = e^{Δ/n} u` is solenoidal (the heat semigroup commutes with `div`),
lies in every `H^m`, converges to `u` in `H^1`, and hence in `L^3` by
`‖f‖_3 ≤ ‖f‖_2^{1/2}‖f‖_6^{1/2}` with `H^1 ↪ L^6`. `w(u_n) → w(u)` in `L^3`
is the continuity of `w : L^3 → L^3` from `lem:derivative`, whose proof was
independently verified (see §8 below). The `H^m` bounds then transfer by the
same weak-limit and lower-semicontinuity argument as in §5, with
`‖∇u_n‖_2 → ‖∇u‖_2`. The cutoff argument for the equality in `eq:mainq`
carries over verbatim (`q ∈ L^6`, `∇q ∈ L^2`, `curl q = 0`, `div q = div w`).
`u ∈ H^1 ⊂ L^3` guarantees `w(u)` is defined in the first place. **Confirmed.**

## 7. The defect corollary (audit item 7)

**`A = |w|w ∈ W^{1,3/2}`. Confirmed.** `j(z) = |z|z` is `C^1` on all of `R^3`
— `Dj(z) = |z|I + z⊗z/|z|` for `z ≠ 0`, `Dj(0) = 0`, and `|Dj(z)| ≤ 2|z| → 0`
— so no truncation is actually needed at the origin, and the chain rule gives
`|∇A| ≤ 2|w||∇w| ∈ L^{3/2}` (`1/6 + 1/2 = 2/3`) while `|A| = |w|² ∈ L^{3/2}`
since `w ∈ L^3`.

**The a.e. identity including the zero set. Confirmed.**
`div A = 0` is `eq:stationary` for the unregularized minimizer, tested against
`∇φ`; since `div A ∈ L^{3/2}`, it vanishes a.e. On `{w ≠ 0}`,
`0 = |w| div w + w·∇|w|` gives `div w = −ŵ·∇|w| = −σ`. On `{w = 0}` the
argument is the level-set fact: for `f ∈ W^{1,1}_loc`, `∇f = 0` a.e. on
`{f = c}`; applied componentwise, `∇w = 0` a.e. on `{w = 0} ⊆ ⋂_i {w_i = 0}`,
so `div w = 0 = σ` there by the definition `eq:sigma`. The hypothesis of the
level-set fact is available because `thm:main` has already delivered
`w ∈ W^{1,2}_loc` — **and only because of that**; this is precisely the step
that was conditional on (H1) in HF18-B, and it is now unconditional.

**The Newtonian potential representation. Confirmed.**
`∇q_* = −∇⊗∇(−Δ)^{-1}σ` is an order-zero multiplier of `σ ∈ L^2`, so
`∇q_* ∈ L^2` with `‖∇q_*‖_2 ≤ ‖σ‖_2`, and `q_* ∈ L^6` as the `Ḣ^1`
representative. `div q_* = Δ(−Δ)^{-1}σ = −σ` and `div q = div w = −σ`
(using `div u = 0`), so the signs agree; `curl q = curl q_* = 0`. Then
`Δ(q − q_*) = ∇div(q−q_*) − curl curl(q−q_*) = 0`, so `q − q_*` is a
distributionally harmonic, hence smooth, `L^6` vector field, and the mean-value
inequality gives `|h(x)| ≤ |B_R|^{-1}∫_{B_R}|h| ≤ |B_R|^{-1/6}‖h‖_6 ~ R^{-1/2}‖h‖_6 → 0`.
The exponent `R^{-1/2}` is correct. This matches the audited HF18-B convention
`q = −∇(Γ*σ)`, `Γ = −1/(4π|x|)`, i.e. `q = ∇(−Δ)^{-1}σ`. The note's caveat
that this is not a claim of absolute pointwise convergence of a Newton
convolution is appropriate and should be preserved in any import.

## 8. The mixed-pressure theorem (audit item 8)

**`eq:advectw`. Confirmed.** `A_i u_j ∂_j w_i = |w| u_j |w| ∂_j|w| = u_j ∂_j(|w|³/3)`,
integrable by `A ∈ L^3`, `u ∈ L^6`, `∇w ∈ L^2` (`1/3+1/6+1/2 = 1`); the
cutoff boundary term is `O(R^{-1}‖u‖_∞‖w‖_3³) → 0`.

**`eq:strainK`. Confirmed.** Substituting `∂_j u_i = ∂_j w_i − ∂_j q_i`, using
`eq:advectw`, then `∂_j q_i = ∂_i q_j` and one integration by parts against
`div A = 0`, gives `K(u) = −∫ q·((A·∇)u)` with `(3, 3/2, ∞)` Hölder.

**Riesz multiplier bound with Frobenius operator norm one. Confirmed.**
The symbol of `R_i R_j` is `−ξ_i ξ_j/|ξ|²`, so
`Π̂_b = −ê^T T̂ ê` with `ê = ξ/|ξ|` and `T = b ⊗ A`. Since
`|ê^T T ê| = |⟨T, ê⊗ê⟩_F| ≤ |T|_F` and `|ê⊗ê|_F = 1`, Plancherel gives
`‖Π_b‖_2 ≤ ‖b⊗A‖_2 = ‖ |b||A| ‖_2 ≤ ‖b‖_6‖A‖_3 = ‖b‖_6‖w‖_6²`
(`1/6 + 1/3 = 1/2`). Confirmed.

**Sign of the Leray decomposition. Confirmed by symbol computation and by
numerics.** With `(I − P)_{jk} = −R_j R_k` and `(F_b)_k = ∂_i(b_i A_k)`, the
symbol of `((I−P)F_b)_j` acting on `b̂_i A_k` is `iξ_i ξ_j ξ_k/|ξ|²`, and the
symbol of `(−∇Π_b)_j` acting on `b̂_i A_k` is the same. So
`(I − P)F_b = −∇Π_b`, i.e. `eq:rieszsign` holds with the sign printed. This
matches the audited HF18-B convention (`Π_L` redefined so that
`(I−P)F = −∇Π_L`, `p = +R_iR_j(u_iu_j)`). `∫ q·P F_b = 0` by duality
`L^3 × L^{3/2}`, `div(P F_b) = 0`, and density of `C_c^∞` gradients in `G_3`.

**Radius cutoff and boundary term. Confirmed.**
`∫ χ_R q·∇Π_b = −∫ χ_R (div q) Π_b − ∫ (q·∇χ_R) Π_b`, and
`|∫ (q·∇χ_R)Π_b| ≤ ‖q‖_3‖Π_b‖_2‖∇χ_R‖_6` with `1/3 + 1/2 + 1/6 = 1` and
`‖∇χ_R‖_6 = R^{-1/2}‖∇χ‖_6 → 0`. The bulk terms converge absolutely.
Using `div q = −σ` gives `eq:mixedpair`.

**Exponent bookkeeping of `eq:KY`. Recomputed, correct.**
`‖σ‖_2 ≤ (1/2)Y^{1/2}`, `‖u‖_6 ≤ S Y^{1/2}`,
`‖w‖_6² ≤ S²‖∇w‖_2² ≤ (5/4)S² Y`, product `= (5/8) S³ Y²`. Also
`‖Π_u‖_2 ≤ ‖u‖_6‖w‖_6² ≤ (5/4)S³Y^{3/2}`, as stated in §5. Both correct.

**Scaling check (independent refutation attempt, failed).** Under `u ↦ b u`,
`w(bu) = b w(u)` so `K ~ b^4` and `Y² ~ b^4`; under `u ↦ T_λ u`, `K ~ λ²` and
`Y² ~ λ²`. `eq:KY` is therefore critical in **both** amplitude and dilation,
so no scaling family can refute it, and it is dimensionally comparable with
the audited HF18-A bound `|K| ≤ C_* Q^{1/3} D_3(w)`, which is also `(b^4, λ²)`.
The two are incomparable in general; `eq:KY` is not claimed to supersede it.

**`K_u = K(u)`.** `eq:strainK` with `b = u` identifies `K_b` with the original
transport term. Confirmed. Note `thm:mixed` requires `b` solenoidal and in
`H^m`; the ledger's application `b = u − S_L u` satisfies both, since the
Littlewood–Paley multiplier commutes with `div`.

## 9. The budgets (audit item 9)

`∫_0^τ ‖∇w‖_2² ≤ (5/4)∫_0^τ Y = (5/4)(E_0/(2ν)) = 5E_0/(8ν)` and
`∫_0^τ ‖σ‖_2² ≤ (1/4)(E_0/(2ν)) = E_0/(8ν)`. Both constants confirmed against
the energy identity `‖u(t)‖_2² + 2ν∫_0^t Y = E_0`.

**Measurability. Confirmed and non-circular.** `t ↦ w(t)` is continuous into
`L^3` (composition of `t ↦ u(t) ∈ C_t L^3` on the classical branch with the
continuous map `w : L^3 → L^3`), so for each fixed `φ ∈ C_c^∞` the map
`t ↦ −∫ w(t) ∂_k φ` is continuous; `‖∂_k w(t)‖_2` is the supremum of countably
many such continuous functions over a countable `L^2`-dense family of unit
`φ`, hence lower semicontinuous, hence Borel. No `L^2` norm of `w` is used
anywhere, consistent with the theorem not asserting `w ∈ L^2`.

**`eq:Pi-conditional` and `eq:firstgap`.** Both recomputed and correct:
`|∫K| ≤ (∫‖σ‖_2²)^{1/2}(∫‖Π_u‖_2²)^{1/2} ≤ (E_0/8ν)^{1/2}(∫‖Π_u‖_2²)^{1/2}`,
and `∫K ≤ (5/8)S³∫Y²`. The note's own diagnosis is exact: the energy identity
controls `∫Y`, not `∫Y²`, and the scalar `y = (T−t)^{-1/2}`, `y' = y³/2`, is a
correct illustration that no purely scalar cubic differential inequality plus a
finite `∫y` forces finite `∫y²`. **This is where Scope A stops, and the note
says so.**

## 10. Consistency with the audited HF21-A (audit item 10)

The three statements are **mutually consistent**, and the consistency is not an
accident: HF23 *implies* the hypothesis-side of HF21-A Theorem 1(b) is never
triggered. Explicitly:

> **Forced consequence (new, unconditional, worth recording).** For every
> solenoidal `u ∈ H^1(R^3)^3`, the vorticity `ω = curl u` vanishes almost
> everywhere on `{w = 0}`; equivalently `|{w = 0} ∩ {ω ≠ 0}| = 0`.
>
> *Proof.* By `thm:main`, `w ∈ W^{1,2}_loc`, so `∇w = 0` a.e. on `{w = 0}`
> (level-set fact, componentwise), hence `curl w = 0` a.e. there. By
> `eq:regconstraints` in the limit (equivalently HF21-A Theorem 1),
> `curl w = curl u = ω` as distributions and both sides are `L^2` functions,
> so `ω = 0` a.e. on `{w = 0}`. ∎

HF21-A Theorem 1(b) is the contrapositive: a minimizer vanishing on a
positive-measure subset of `{ω ≠ 0}` would refute (H1). HF23 proves (H1),
so no such configuration exists — the falsification criterion is now known to
be unreachable rather than merely unrealized. HF21-A itself notes that "no such
construction is produced here"; HF23 explains why none can be.

HF21-A Theorem 2 (rigidity of linear zeros) is untouched and remains
consistent: it excludes `w = |A|^{-1/2}A` with `DA(x_0) ≠ 0` as the minimizer
of an `H^m` datum, on the grounds that `curl w ∉ L^∞_loc` forces
`u ∉ H^s_loc` for `s > 5/2`. That is a statement about *datum smoothness*, not
about (H1); and such a `w` does satisfy `∇w ∈ L^2_loc` (`|∇w| ~ d^{-1/2}`,
`∫_B d^{-1} < ∞` in `R^3`), so there is no clash with `thm:main`.

HF21-A Corollary 3.3 ("(H1) and (H2) ⟺ `div w ∈ L^{3/2}`") also survives, and
now sharpens: (H1) is discharged, `div w ∈ L^2`, and the residual content of
the pair is **exactly (H2)**, which HF23 correctly declines to claim
(`L^2 ⊄ L^{3/2}` on a space of infinite measure). HF21-A Theorem 3(c) ((H1)
follows from `div w ∈ L^p_loc` for one `p > 1`) is now satisfied at `p = 2`,
as the index note predicted.

**None of the three must be wrong.** No repair to HF21-A is implied.

## 11. Refutation attempts (all failed)

All numerics are bounded evidence at finite resolution and are never proof.
The candidate's proof applies verbatim on `T^3` (Plancherel identities,
gradient space, Leray projection, direct method all hold; the `L^2 ∩ L^3`
regularization is not even needed there), so a periodic minimization is a
legitimate falsification target for the *global* inequalities.

1. **Unconstrained matrix inequality.** `S = I` violates `d² ≤ |S|_F²/3` by a
   factor 9 — but the constraint fails there. The lemma is not the false
   unconstrained statement. *Refutation fails; the constraint does the work.*
2. **Random constrained matrices.** `4·10^5` samples, zero violations,
   supremum `0.32822 < 1/3` approached only as `t → 1`. *Failed.*
3. **Sharpness family.** `d²/|S|_F²` matched `2t²/(t²+2t+3)` to nine digits;
   the lemma is sharp for every `t`, so no better constant exists by this
   route. *Failed (and yields R3).*
4. **Direct minimization on `T^3`, random data.** 81 shapes (`N = 16`,
   spectral cutoffs 2/3/4, three anisotropies, three spectral slopes):
   `D/C ∈ [0.023, 0.0373]`, always `≤ 1/4`; `‖∇w‖²/C ∈ [1.023, 1.048]`,
   always `≤ 5/4`. Margin roughly a factor 7 on `D/C`. *Failed.*
5. **Resolution study.** Same datum at `N = 16, 24, 32, 40`: the pointwise
   Euler–Lagrange residual `‖d + t e^T S e‖_{L²}` falls `0.318 → 0.207 →
   0.146 → 0.109`, and `‖curl w‖²/‖curl u‖²` converges to `1` as
   `1.00095 → 1.00016 → 1.00004 → 1.000017`. The residual and the excess are
   aliasing artefacts, not a violation of the a.e. constraint. The `99th`
   percentile of `d²/|S|_F²` converges to `≈ 0.286 < 1/3`. *Failed.*
6. **Data whose minimizer genuinely vanishes.** ABC with `(A,B,C) = (1,1,0)`
   gives `min|w| ~ 3·10^{-11}` and Taylor–Green gives `min|w| ~ 9·10^{-17}` at
   `N = 48`; the bounds still hold (`D/C = 0.024` and `0.042`,
   `‖∇w‖²/C = 1.024` and `1.042`) and `‖curl w‖²/‖curl u‖² = 1.000000`.
   *Failed.* This also probes the zero set, which the random data did not.
7. **The forced consequence of §10, tested.** For Taylor–Green
   `u = (sin x cos y cos z, −cos x sin y cos z, 0)`, `w` vanishes on the
   planes `{cos z = 0}` — forced by the reflection `z ↦ π − z`, under which
   `u ↦ −u`, hence `w ↦ −w` by uniqueness, hence `w_3 = 0` and
   `q_1 = q_2 = u_1 = u_2 = 0` on the fixed plane. There `ω ≠ 0`. This is a
   **codimension-one zero set meeting `{ω ≠ 0}`, of measure zero**, exactly
   the configuration HF21-A Theorem 1(b) permits and HF23 requires. *Failed
   as a refutation; confirms the §10 prediction in a nontrivial case.*
8. **Sign of the Leray/Riesz decomposition.** Four independent evaluations of
   the transport term — `K_direct = −∫A·(u·∇)u`, `K_strain = −∫q·((A·∇)u)`,
   `K_∇Π = ∫q·∇Π_u`, `K_σΠ = ∫σΠ_u` — agree to relative `2·10^{-4}` at
   `N = 40` (and `2·10^{-3}` at `N = 24`, converging). The opposite sign
   convention in `eq:rieszsign` is off by exactly a factor `−1`. *Failed;
   `eq:strainK`, `eq:rieszsign` and `eq:mixedpair` are confirmed with signs.*
9. **Scaling refutation of `eq:KY`.** `(b^4, λ²)` on both sides; no scaling
   family can break it. *Failed.*

**Limitation of the evidence.** The numerics are periodic, at `N ≤ 48`, on
smooth band-limited data, without dealiasing; they can neither confirm nor
refute the whole-space passage to the limit of §5, which is a purely analytic
step and was checked by hand only. They also do not probe data whose minimizer
vanishes on a set of *positive* measure, since no such datum is known.

## 12. Unnecessary dependencies

- **§2 duplicates audited manuscript content.** `lem:min` is
  `lem:quotient-minimizer` + `lem:quotient-coercive`; `lem:convex` is
  `lem:cubic-pointwise`; `lem:derivative` is `lem:quotient-stability` +
  `prop:quotient-derivative`; `lem:evolution` is `lem:quotient-heat` +
  `lem:quotient-chainrule` + `lem:quotient-pressure`. All were re-checked and
  are correct (including the monotonicity identity
  `(j(a)−j(b))·(a−b) = ((|a|+|b|)/2)(|a−b|² + (|a|−|b|)²)`, verified by
  expansion, and the three bounds of `eq:convex`), but **none should be
  re-imported into the manuscript**; cite the existing lemmas.
- `C_P = ‖P‖_{L^3→L^3}` and the coercivity chain `eq:coercive` are used
  nowhere in Scope A's positive results.
- `lem:evolution` (heat sign, `D_Q ≥ 0`, the evolution identity) is not used
  by `thm:main`, `cor:sigma` or `thm:mixed`; only §5 needs the energy identity,
  which is `eq:energy`, not `eq:evolution`.
- HF18-A's `V ∈ H^1`, `D_Q = D_3(w)`, `D_3(w) ≥ c‖u‖_9³` and
  `|K| ≤ C_* Q^{1/3} D_3(w)`, HF18-B, HF20, HF21-A and HF21-B are **not used**
  anywhere in Scope A. The candidate is self-contained. Correct the index
  note's sentence "an audited repository result is one pillar of this
  candidate": it is a corroborating parallel, not a dependency.

## 13. Non-claims

Scope A does not establish, and this audit does not certify: (H2)
`σ ∈ L^{3/2}(R^3)`; `w ∈ L^2` or `w ∈ H^1(R^3)`; the weighted
Calderón–Zygmund inequality; any bound on `∫_0^τ Y²` or `∫_0^τ ‖Π_u‖_2²`; any
regularity or blowup result; the arbitrary-data signed spacetime bound; the
optimality of `5/4` or `1/4`; anything about §6–§9 of the candidate; any
novelty or priority claim. NS-R3 remains open, and `HIGH-STRAIN` and
`HIGH-PRESSURE` remain the open producers.

---

## VERDICT

**PASS** for Scope A, with three expository repairs (R1, R2, R3) that change no
statement and no constant. Theorem `thm:main`, Corollary `cor:sigma`, Theorem
`thm:mixed` and Corollary `cor:budgets` are proved. Hypothesis (H1) of HF18-B
is discharged unconditionally, in the strong global form `∇w ∈ L^2(R^3)` with
`‖∇w‖_2² ≤ (5/4)‖∇u‖_2²`, for every solenoidal `u ∈ H^1(R^3)^3`, with no
smallness. The mixed-pressure pairing is unconditional in `L^2 × L^2`.

## REVIEWED SCOPE

§2 `sec:prelim` (all four lemmas), §3 `sec:regularity` (Theorem 3.1 and all six
subsections), §4 `sec:mixed` (Corollary 4.1, `eq:advectw`, `eq:strainK`,
Theorem 4.2 and its remark), §5 `sec:budget` (energy identity, Corollary 5.1,
`eq:Pi-conditional`, `eq:firstgap`). Not reviewed: §1, §6 `sec:hf20`, §7
`sec:spacetime`, §8 `sec:frontier`, §9 `sec:literature`, the ledger's claims
about §6–§8, and the bibliography's source-verification assertions.

## FIRST BAD BRIDGE

**None in Scope A.** The first implication that is *not proved* is the one the
candidate itself declares open: passing from `eq:firstgap`,
`∫_0^τ K ≤ (5/8)S³∫_0^τ Y²`, to a datum-only finite bound, since the energy
identity controls `∫Y` and not `∫Y²`. That is a declared boundary, not a bad
bridge. The nearest thing to a defect is the one-line assertion at the zero set
in §3.3, repaired below as R2 — as written it asserts irrelevance of the choice
of `e` where a one-line proof that `d_δ = 0` is required. The conclusion is
unchanged.

## EVIDENCE

Recomputed by hand: `1/32` and `4096` in `lem:regmono`/`eq:difference-bound`;
the eigenvalue interval `[r_δ, 2r_δ]` of `Dj_δ`; the monotonicity identity of
`lem:convex` by expansion; `1/4`, `1/6` and `(2|a|+|d|)|d|` in `eq:convex`;
both identities of `eq:hodge` by Plancherel; `D_δ ≤ C/4` and `5C/4`;
`‖∇q_δ‖² = D_δ`; the `R^{-1/2}` and `R^{-1}` cutoff rates; the `C^1`-ness of
`j` at the origin; the exponent triples `(3,6,2)`, `(3,3/2,∞)`, `(6,3)`,
`(3,2,6)`; `(5/8)S³Y²` and `(5/4)S³Y^{3/2}`; `5E_0/(8ν)` and `E_0/(8ν)`; the
symbol computation confirming `(I−P)F_b = −∇Π_b`; and the `(b^4, λ²)` scaling
of `eq:KY`. Numerics as listed in §11: nine refutation attempts, all failed;
scripts were run in the session scratchpad and are evidence, not proof.

## REPLACEMENT ARGUMENT

**R1 (display the symmetrization).** In §3.3, after the a.e. equation
`r_δ div w_δ + (w_{δ,i} w_{δ,j}/r_δ) ∂_i w_{δ,j} = 0`, insert:

> Since `w ⊗ w` is symmetric, `w_i w_j ∂_i w_j = w_i w_j (sym ∇w)_{ij} = |w|² e^T S e`
> wherever `w ≠ 0`, so the equation involves only the symmetric part of `∇w`.

**R2 (prove the zero-set case instead of asserting it).** Replace "At zero
points choose any unit vector; `t_δ = 0` makes that choice irrelevant." by:

> At points where `w_δ = 0` the displayed equation reads `δ · div w_δ = 0`
> with `δ > 0`, so `d_δ = 0` there; since `t_δ = 0` as well, the constraint
> `d_δ = −t_δ e^T S_δ e` holds for an arbitrary choice of unit vector `e`.
> This is the only place where the regularization is indispensable: the
> unregularized equation degenerates to `0 = 0` at its zero set and supplies
> no constraint there.

*Proof of R2.* The a.e. identity is `r_δ(w_δ) div w_δ + (w_{δ,i}w_{δ,j}/r_δ(w_δ))∂_i w_{δ,j} = 0`.
On `{w_δ = 0}` the second term vanishes identically and `r_δ(0) = δ`, so
`δ div w_δ = 0` a.e. there, i.e. `d_δ = 0` a.e. on `{w_δ = 0}`. ∎

**R3 (record the sharp matrix lemma).** Replace `lem:matrix` by the sharp
form displayed in §3 above, `d² ≤ (2t²/(t²+2t+3))|S|_F² ≤ (1/3)|S|_F²`, with
the equality family `S = diag(−d/t, (d/2)(1+1/t), (d/2)(1+1/t))` in the
`e`-frame, and the proof given there. This costs one line and makes visible
that `1/3` is the `t → 1` endpoint, which is the precise reason the estimate is
uniform in `δ`.

**R4 (statement strengthening, optional).** `eq:mainspaces` may be stated as
`w, q ∈ L^6(R^3) ∩ Ḣ^1(R^3)` with `∇w, ∇q ∈ L^2(R^3)`; `W^{1,2}_loc`
understates what §3.5 proves. Keep the explicit disclaimer that `w ∈ L^2` is
not asserted.

## CONDITIONAL SUFFIX THAT SURVIVES

Nothing in Scope A is conditional. Unconditionally, for every solenoidal
`u ∈ H^1(R^3)^3`:

- `‖∇w‖_2² ≤ (5/4)‖∇u‖_2²` and `‖∇q‖_2² = ‖div w‖_2² ≤ (1/4)‖∇u‖_2²`;
  `w, q ∈ L^6`, `∇w, ∇q ∈ L^2`, `w ∈ W^{1,2}_loc`. Hypothesis (H1) holds.
- `A = |w|w ∈ W^{1,3/2}`, `σ = −div w` a.e. and distributionally including
  across `{w = 0}`, `‖σ‖_2² ≤ (1/4)‖∇u‖_2²`, and `q = ∇(−Δ)^{-1}σ`.
- `ω = curl u = 0` a.e. on `{w = 0}` (the forced consequence of §10).
- For solenoidal `u, b ∈ H^m`, `m ≥ 4`:
  `K_b = ∫ q·∇Π_b = ∫ σ Π_b` with both integrals absolutely convergent,
  `‖Π_b‖_2 ≤ ‖b‖_6‖w‖_6²`, `|K_b| ≤ (1/2)‖∇u‖_2‖b‖_6‖w‖_6²`, and
  `|K(u)| ≤ (5/8)S³Y²`. No `L^{3/2}` hypothesis on `σ`.
- On the classical branch, `∫_0^τ ‖∇w‖_2² ≤ 5E_0/(8ν)` and
  `∫_0^τ ‖σ‖_2² ≤ E_0/(8ν)` for every `τ < T_*`.

Everything downstream of (H1) in HF18-B — Lemma A (identification of the
distribution `div w` with `−σ`), the potential formula, and the pairing form
`K_L = ∫ σ Π_L` — becomes unconditional, the last one in the `L^2 × L^2` form
rather than the `L^{3/2} × L^3` form, which is why (H2) is bypassed and not
needed.

## UNNECESSARY DEPENDENCIES

Listed in §12: the whole of §2 duplicates audited manuscript lemmas; `C_P` and
`eq:coercive` are unused; `lem:evolution` is unused by the positive chain; and
no HF18/HF20/HF21 result is used at all. The index note's claim that HF21-A
Theorem 1 is "one pillar of this candidate" should be corrected to a
corroboration.

## NON-CLAIMS

As listed in §13. In particular this audit certifies nothing about §6–§9 of the
candidate, promotes no graph node, and does not touch NS-R3, `HIGH-STRAIN` or
`HIGH-PRESSURE`.

## REOPENING CONDITION

This PASS is reopened if any of the following is exhibited.

1. A solenoidal `u ∈ H^1(R^3)^3` (or on `T^3`) whose cubic minimizer satisfies
   `‖div w‖_2² > (1/4)‖∇u‖_2²` or `‖∇w‖_2² > (5/4)‖∇u‖_2²`.
2. A `δ > 0` and a datum for which the a.e. constraint
   `d_δ = −t_δ e_δ^T S_δ e_δ` fails on a set of positive measure — in
   particular any failure of the fixed-`δ` difference-quotient bound or of the
   `C^1` chain rule for `j_δ ∘ w_δ`.
3. A failure of `F(w_δ) → F(w)` as `δ ↓ 0`, i.e. any datum for which the
   regularized minimizers do not converge to the actual `L^3` minimizer, which
   would void the transfer of the uniform constants.
4. A minimizer vanishing on a set of positive measure inside `{ω ≠ 0}`, which
   by HF21-A Theorem 1(b) would refute (H1) and hence `thm:main` directly.
5. A counterexample to the level-set fact as used (`∇f = 0` a.e. on `{f = c}`
   for `f ∈ W^{1,1}_loc`) in the vector-valued form applied in `cor:sigma`.

## EXACT EDITS THE CONTROLLER SHOULD MAKE IF THIS VERDICT STANDS

**Manuscript (`navier-paper/main.tex`, `sec:quotient`).**

1. `sec:quotient` opens with "This section records an analytic mechanism, not a
   regularity theorem." That sentence becomes false once `thm:main` is added.
   Replace it with a sentence saying the section records the mechanism together
   with one unweighted regularity estimate for the representative, and that no
   estimate for the remaining strain term is proved anywhere in the section
   (the second half is still true and should be kept).
2. Add, after `prop:quotient-derivative` and before
   `rem:quotient-scope`, a new subsection containing:
   - `prop:quotient-divcurl` — the statement of `thm:main` for solenoidal
     `u ∈ H^1`, with the proof of §3 of the candidate, incorporating repairs
     R1, R2 and the sharp form R3, and citing `lem:quotient-minimizer`,
     `lem:cubic-pointwise`, `lem:quotient-stability` and `lem:leray` instead of
     re-proving §2 of the candidate.
   - `cor:quotient-defect` — `A ∈ W^{1,3/2}`, `σ = −div w` a.e. including
     across the zero set, `‖σ‖_2 ≤ (1/2)‖∇u‖_2`, `q = ∇(−Δ)^{-1}σ`.
   - `cor:quotient-vorticity-zero` — the forced consequence: `curl u = 0` a.e.
     on `{w = 0}`. Two lines, and it is the sharpest structural statement the
     programme now has about the zero set.
   - `lem:quotient-mixed-pressure` — `thm:mixed` in the `L^2 × L^2` form, with
     `(I−P)F_b = −∇Π_b` matching the sign convention already fixed in
     `subsec:quotient-conventions`, and `|K| ≤ (5/8)S³Y²`.
   - `cor:quotient-budgets` — the two spacetime budgets, with the measurability
     sentence of §9 above.
3. Add one sentence to `rem:quotient-scope` recording that these statements
   hold for every solenoidal `H^1` datum with no smallness, that `w ∈ L^2` is
   not asserted, and that `σ ∈ L^{3/2}` remains unproved.
4. Do **not** add anything to `hyp:highstrain`, `hyp:highpressure`,
   `lem:quotient-lowstrain` or `prop:quotient-conditional`. Nothing here
   touches the conditional route.

**Claim graph.**

5. Record (H1) as **discharged**: the HF18-B node gated on `w ∈ W^{1,1}_loc`
   becomes unconditional, at `W^{1,2}_loc` with explicit constants.
6. Record the mixed-pressure pairing as unconditional in the `L^2 × L^2` form,
   and record explicitly that (H2) is **bypassed, not proved**, so the HF21-A
   Corollary 3.3 collapse now reads: the residual content of the (H1)+(H2) pair
   is exactly (H2).
7. Record `|K| ≤ (5/8)S³Y²` and the two spacetime budgets as new unconditional
   facts under the quotient route, with the note that `eq:KY` is
   `(b^4, λ²)`-critical and incomparable with the audited HF18-A bound.
8. Promote no node. `HIGH-STRAIN`, `HIGH-PRESSURE`, `CRITICAL` and NS-R3 are
   untouched.

**`PLAN.md`.**

9. In the HF23 section, replace "UNAUDITED" by an audit record: Scope A
   audited 2026-09-06 at research HEAD `928713d`, verdict PASS with three
   expository repairs, candidate frozen at
   `abe74421ef6a8a7bacc108c0c08834e32f2a6116530fceb00368c8e67b129075`.
10. Correct the controller-check paragraph: HF21-A Theorem 1 is **not** a
    dependency of HF23; the candidate re-derives `curl w_δ = curl u` itself,
    so HF23 is self-contained and inherits no risk from the HF21-A repair.
11. Add the forced consequence (`ω = 0` a.e. on `{w = 0}`) to the HF21 section
    as the resolution of the open consistency question flagged there.
12. In "Ordered next actions", record that Scope A is closed and that the
    remaining HF23 work is Scope B (§6–§9: the HF20 reconstruction against the
    audited HF20 record, `thm:spacetime`, and the conditional continuation),
    which this audit did not touch.
13. Keep the first gap **unchanged**. Scope A moves the spatial gate, not the
    dynamical producer.

**`research/evidence/hf23-divcurl-continuation.md`.**

14. Change the status line from "UNAUDITED candidate" to "Scope A audited,
    PASS with expository repairs; Scope B unaudited", and link this file.
15. Correct the sentence "an audited repository result is one pillar of this
    candidate" per item 10.

**Not to be done.**

16. Do not edit `research/evidence/hf23-divcurl-continuation.tex`. It is the
    frozen artifact; the repairs R1–R3 belong in the manuscript import, not in
    the artifact.
17. Do not import §2 of the candidate into the manuscript; it duplicates
    audited lemmas.
18. Do not state (H2), `w ∈ L^2`, or any bound on `∫Y²` anywhere as a
    consequence of this audit.
