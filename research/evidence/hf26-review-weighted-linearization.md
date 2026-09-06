# Review of HF26, Section 3: the weighted linearization and the derivative of the dual field

Independent adversarial proof audit, 2026-09-06. Lens: rebuild every algebraic
identity and constant from scratch (by hand, by `sympy`, and by numerical
extremal search), re-derive every implication from the first nontrivial one,
check quantifiers / topologies / function spaces at every step, and attempt to
refute each new fact by an explicit counterexample, a degenerate configuration,
a sign flip, or a finite-dimensional model of the same variational structure.

## Freeze

| object | identity |
|---|---|
| research HEAD at audit time | `2ba0f1018f51f252ded22953e3553bde73ca74ec` |
| target | `research/evidence/hf26-temporal-continuation.tex`, 1432 lines, sha256 `24b538280c8639b81a1f6f86d4c72370362625ca8a52d1d81a99b29236a540ab` |
| index note (context only) | `research/evidence/hf26-temporal-continuation.md` |
| audited inputs consulted | `hf18-hodge-regularity.md` + `hf18-review-hodge-regularity.md` (PASS), `hf23-divcurl-continuation.{md,tex}` + its two PASS reviews, `hf22-projection-regularity.md` + `hf22-review-projection-regularity.md` |

## Scope

- Section 3 `sec:linear`, lines 280–512: `eq:matrixM`, `eq:Hspace`,
  `eq:Hequiv`, `eq:L3embed`, `eq:weightedE`, `lem:jTaylor`,
  `thm:weightedresponse`, `thm:Aderivative`, `cor:second`, `rem:linear-scope`.
- Appendix `app:weighted`, lines 1234–1283, "Reconstruction of weighted
  dissipation without a zero-set shortcut".
- Inputs from Section 2 were re-derived only where Section 3 or the appendix
  depends on them: `eq:mono`, `eq:Bbelow`, `eq:Babove`, `eq:holder`,
  `eq:weightedbasic`, `eq:Alip`, `eq:Qprime`, `eq:Didentity`, `eq:Dcontrol`,
  `eq:gradA`.

**Not** in scope: Sections 1, 2 (as statements in their own right), 4–9,
`app:spatial`, `app:positive`, and everything about the temporal criterion, the
departure theorem and the comparison curve.

---

## Verdict

**PASS WITH SCOPE.** Every mathematical step of `lem:jTaylor`,
`thm:weightedresponse`, `thm:Aderivative`, `cor:second` and `app:weighted` was
reconstructed independently and is correct as displayed, including both signs
of `ε`, the degenerate weight, and the zero Hilbert space; no step uses
unweighted `L^3` convergence of the difference quotients or unweighted control
of `q` near `{w = 0}`. The scope qualification is that three claims *about the
result* — what `rem:linear-scope` says it closes in HF22-B, which audited
repository result `app:weighted` reconstructs, and under which hypothesis
`eq:Didentity` is asserted — are inaccurate or under-specified and must be
repaired before any import.

Nine refutation attempts were made; seven failed outright (which is positive
evidence for the section), and two succeeded only at the level of attribution,
scope wording and one non-load-bearing constant justification.

**No graph node changes and nothing is promoted by this review.**

---

## Per-question findings

### Q1. Is the strong convergence in `thm:weightedresponse` genuinely proved?

**Verdict: yes, genuinely proved. No step assumes what it proves.**

The architecture is a Minty/Browder-type argument in a degenerate weighted
Hilbert space, and it is executed correctly. I reconstructed it in full:

*Step 1.* `eq:deps` and `eq:zweighted` follow from `eq:holder` and
`eq:weightedbasic` with `h → εh`; I re-derived both inherited estimates from
`eq:Bbelow`/`eq:Babove` and the two-competitor argument
(`F(U + d) ≤ F(U + h)` from minimality at `v + h` with the competitor `U + h`,
plus `⟨j(U), d − h⟩ = 0` because `d − h = q(v+h) − q(v) ∈ G_3`). Constants `6`,
`2`, `4`, `4/3` are correct. `‖z_ε‖_3 = O(|ε|^{-1/3})` is exactly what
`eq:deps` gives.

*Step 2.* Boundedness in `H_U` (from `eq:zweighted` and `eq:Hequiv`) gives a
weak subsequential limit; `h + E_U` is a closed affine subspace hence weakly
closed; `⟨J_ε(z_ε), g⟩ = 0` for `g ∈ G_3` is stationarity at *both* endpoints
(`A(v+εh)` and `A(v)` each annihilate `G_3`, and the pairing extends from
`∇C_c^∞` to its `L^3`-closure by continuity); `eq:Remactual` converts this into
`⟨z_ε, g⟩_U = o(1)`; the limit is therefore the unique element of `h + E_U`
orthogonal to `E_U`, i.e. `L_U h`. Uniqueness of every subsequential weak limit
upgrades to weak convergence of the whole family. Correct.

*Step 3.* This is the only place where a circularity could hide, and it does
not. The monotonicity identity `eq:mono` is applied to
`a = U + εz_ε`, `b = U + εz_m` and divided by `ε²`, so the sign of `ε` is
irrelevant there; `⟨J_ε(z_ε), z_ε − z_m⟩ = 0` because `z_ε − z_m ∈ G_3`; the
two remainder terms are `O_m(|ε|^{1/3})` and `O_m(|ε|^{2/3})`, both obtained by
multiplying the *divergent* bound `‖z_ε‖_3 = O(|ε|^{-1/3})` by a power of `|ε|`
that beats it. Only **weak** convergence of `z_ε` is then used, against the
fixed vector `z_m`. The constant chain is right:

```
limsup (1/2)∫ρ|z_ε−z_m|²  ≤  ‖z_m−z‖_U²          (weak convergence + z ⟂ E_U)
⟹ limsup ‖z_ε−z_m‖_U²     ≤  4‖z_m−z‖_U²          (eq:Hequiv upper constant 2)
⟹ limsup ‖z_ε−z‖_U        ≤  3‖z_m−z‖_U           (triangle)
```

and `m → ∞` kills the right side because `z_m → z` in `H_U` by definition of
`E_U` as a closure. The order of limits ("fix `m` before sending `ε` to zero")
is stated and respected; `‖z_m‖_3` is allowed to blow up with `m` and never
enters a limit taken at fixed `ε`.

*Both signs of `ε`.* `ε` enters `eq:deps`/`eq:zweighted` as `|ε|`, the
monotonicity step as `ε²`, and the remainder estimates as `|ε|`. The final
sentence of the proof is accurate. I confirmed sign symmetry numerically in a
finite-dimensional model of the same variational structure (see RA3).

*`U = 0` on a set of positive measure.* `H_U` is `L²(ρ dx)`, which is blind to
`{ρ = 0}`; the theorem correctly asserts nothing there. `E_U` may be a proper
subspace, may be all of `H_U`, and may fail to distinguish gradients supported
in the interior of `{U = 0}` (these map to `0` in `H_U`) — the quotient
construction handles all three, and this is exactly the kernel that HF22-B §4.2
identified. I built a finite-dimensional model in which `G` contains a vector
supported entirely on the zero-weight site, so that `E_U` is genuinely
deficient there, and the weighted convergence still held at rate `O(ε)`.

*`U = 0` a.e.* Then `H_U = {0}`, `E_U = {0}`, `L_U h = 0`, and `eq:wresponse`
is vacuously true; the document says so. This is not a hole, because the
downstream use (`thm:Aderivative`) does not go through `H_U` in that case: by
`eq:deps` with `‖U‖_3 = 0` one gets `‖d_ε‖_3 ≤ 2^{1/3}‖h‖_3|ε|`, hence
`‖J_ε(z_ε)‖_{3/2} ≤ 2‖d_ε‖_3²/|ε| = O(|ε|) → 0 = ‖B_v h‖_{3/2}`. The
document's one-line justification ("the subsequent dual conclusion follows from
`eq:Remactual`") is correct. I cross-checked the same case against the exact
homogeneity `Q(v + εh) = |ε|³Q(h)` for `v ∈ G_3`, which is consistent with
`eq:Qsecond`'s vanishing second-order term.

### Q2. Does any step silently use unweighted `L^3` convergence, or unweighted control of `q` near `{w = 0}`?

**Verdict: no. I audited every occurrence and found no violation.**

`‖z_ε‖_3` (or `‖d_ε‖_3`) appears exactly four times in Section 3:

1. Step 1, as the explicitly labelled "potentially divergent" bound
   `O(|ε|^{-1/3})`;
2. `eq:Remactual`, as `2‖d_ε‖_3²/|ε| = O(|ε|^{1/3})`;
3. Step 3, `(|ε|/2)‖z_m‖_3(‖z_ε‖_3+‖z_m‖_3)² = O_m(|ε|^{1/3})`;
4. Step 3, `2|ε|‖z_m‖_3²(‖z_ε‖_3+‖z_m‖_3) = O_m(|ε|^{2/3})`.

In each case the divergent quantity is multiplied by a strictly larger power of
`|ε|`. Nowhere is `z_ε` asserted to converge in `L^3`, and nowhere is
`z_ε − z` or `L_U h` claimed to lie in `L^3`. The unweighted integral
`∫|z_m||z_ε − z_m|²` in `eq:strongbase` is genuinely unweighted, but it carries
a factor `|ε|` and is the *error* term, not the controlled term.

The one place where a reader could suspect a hidden unweighted statement is
`thm:Aderivative`, whose conclusion is an *unweighted* `L^{3/2}` limit. It is
clean, and the mechanism deserves to be stated: on `{ρ = 0}` one has
`M_U = 0` and `J_ε(z_ε) = j(d_ε)/ε`, whose `L^{3/2}` norm restricted to that
set is `‖d_ε‖_{L^3({ρ=0})}²/|ε| = O(|ε|^{1/3})`. The zero set therefore
contributes nothing to the `L^{3/2}` limit *for free*, by the quadratic
remainder alone, with no control of `z_ε` there. That is precisely why the
`L^{3/2}` conclusion is compatible with the boundary-section warning at line
1055, and it should be said in the proof (repair R7).

I also checked `rem:linear-scope`'s disclaimers against the actual proofs:
`L_U h ∈ L^3` is not shown and not used; no unweighted derivative of `w` is
shown or used; no two-point `L^3` Lipschitz estimate for `q` is shown or used;
no operator-norm continuity of `v ↦ B_v` is shown or used. All four disclaimers
are accurate.

### Q3. `lem:jTaylor`: the constants `4` and `2`, verified independently

**Verdict: both constants are correct (valid upper bounds). Neither is sharp.**

`Dj(a) = |a|I + a⊗a/|a|` off zero, `Dj(0) = 0`, and `j ∈ C¹(R³;R³)` because
`‖Dj(z)‖_op = 2|z| → 0`; this last point is what makes the fundamental theorem
of calculus along the segment `a + td` legitimate even when the segment passes
through the origin.

The displayed decomposition is an exact identity — I expanded it:

```
(a−b)⊗a + b⊗(a−b) = a⊗a − b⊗b ,
```

so `[(a−b)⊗a + b⊗(a−b)]/|a| + (b⊗b)(1/|a| − 1/|b|) = a⊗a/|a| − b⊗b/|b|` ✓.
With `|a| ≥ |b| > 0`, `‖u⊗v‖_op = |u||v|` gives the three operator norms
`|a−b|`, `(|b|/|a|)|a−b|` and `|b|(|a|−|b|)/|a| ≤ (|b|/|a|)|a−b|`; adding
`‖(|a|−|b|)I‖_op ≤ |a−b|` gives `≤ (2 + 2|b|/|a|)|a−b| ≤ 4|a−b|` ✓. The `b = 0`
case gives `2|a| = 2|a−b|` ✓, and the left side of `eq:jmatrixlip` is symmetric
in `(a,b)`, which is what licenses "interchanging `a,b`".

`eq:jTaylor` then follows from `∫₀¹ 4t|d|·|d| dt = 2|d|²` ✓.

*Independent numerics.* Over `4·10⁵` random pairs spanning six decades of
scale, including antipodal, near-equal and zero configurations, plus a
`3·10⁶`-point two-dimensional sweep, the maximum of
`‖Dj(a)−Dj(b)‖_op/|a−b|` was `2.000000` and the maximum of
`|j(a+d)−j(a)−Dj(a)d|/|d|²` was `1.000000`. Both maxima are attained on whole
families and are exactly computable: for collinear same-direction `a = αe`,
`b = βe` one has `Dj(a) − Dj(b) = (α−β)·diag(2,1,1)` in the frame of `e`, so the
ratio is exactly `2` for every such pair; and for `a = te`, `d = e` the
remainder is exactly `1 = |d|²` for every `t > 0`. So the document's `4` and `2`
are each loose by a factor `2` on a large set of configurations. This is not a
defect — the claims as written are true, and I did not prove that `2` and `1`
are upper bounds — but the slack propagates into `eq:Remactual` and thence into
the `O_m(|ε|^{2/3})` remainder, so it is worth recording if constants are ever
tightened (repair R6).

I also re-derived `eq:mono` and confirmed it is an *exact identity* (max
relative error `1.3·10^{-15}` over `2·10⁵` random pairs), and re-derived
`eq:Bbelow` (`1/4`, `1/6`) and `eq:Babove` (`1`, `1/3`) by integrating it. All
correct.

### Q4. `thm:Aderivative`: Hadamard vs Fréchet, and the `L^{3/2}` target

**Verdict: the Hadamard claim is correct, is genuinely Hadamard, is not
Fréchet, is load-bearing, and `L^{3/2}` is the right target. Hölder bookkeeping
verified.**

*The multiplier bound.* `M_U² ≤ 2ρM_U` as quadratic forms is exact: `M_U` has
eigenvalues `(ρ, ρ, 2ρ)`, `M_U²` has `(ρ², ρ², 4ρ²)`, `2ρM_U` has
`(2ρ², 2ρ², 4ρ²)`. Verified numerically as sharp. Then
`|M_U z|² ≤ 2ρ(z·M_U z)`, and Hölder with exponents `(4, 4/3)`:

```
∫|M_U z|^{3/2} ≤ 2^{3/4}∫ρ^{3/4}(z·M_U z)^{3/4} ≤ 2^{3/4}‖U‖_3^{3/4}‖z‖_U^{3/2},
```

i.e. `‖M_U z‖_{3/2} ≤ (2‖U‖_3)^{1/2}‖z‖_U` ✓. Composed with `eq:L3embed` and
the contraction property of `L_U`, this gives `‖B_v h‖_{3/2} ≤ 2‖U‖_3‖h‖_3` ✓.

*Fixed direction.* `(A(v+εh) − A(v))/ε = J_ε(z_ε)`, and
`J_ε(z_ε) − M_U z_ε → 0` in `L^{3/2}` by `eq:Remactual`, while
`M_U z_ε → M_U L_U h` in `L^{3/2}` by `thm:weightedresponse` and the multiplier
bound. Correct. Note that `M_U L_U h` is a well-defined `L^{3/2}` function even
though `L_U h` is only an `H_U`-class, because `M_U = 0` off `{ρ > 0}`.

*Hadamard upgrade.* `eq:Alip` applied at base point `v + ε_n h` with increment
`ε_n(h_n − h)` bounds the difference of the two quotients by
`2(‖w(v+ε_nh_n)‖_3 + ‖w(v+ε_nh)‖_3)‖h_n−h‖_3`, and `‖w(x)‖_3 ≤ ‖x‖_3` keeps
the prefactor bounded. Correct for both signs. This is the standard fact that a
locally Lipschitz map with directional derivatives is Hadamard differentiable;
`A` is locally Lipschitz `L^3 → L^{3/2}` by `eq:Alip`, which I re-derived
(the exponent-`(4, 4/3)` Hölder step, `eq:mono`, and the cancellation
`⟨j(w_1) − j(w_0), w_1 − w_0 − h⟩ = 0`; the constant `2` is correct).

*Hadamard is not decoration.* `eq:Atime` applies the derivative along the
*varying* directions `h_ε = (v(t+ε) − v(t))/ε`, which converge to `v_t` but are
not equal to it. A Gateaux statement would be insufficient there. This should
be said (repair R7); the document currently leaves the reader to notice it.

*Fréchet is correctly not claimed.* `rem:linear-scope` disclaims operator-norm
continuity of `v ↦ B_v`, so no `C²` claim is made. I found no step that needs
Fréchet differentiability.

*`L^{3/2}` is right.* `|A(v)| = |w|²` with `w ∈ L^3` forces
`‖A(v)‖_{3/2} = ‖w‖_3²`, and `|B_v h| ≲ ρ|L_U h| = ρ^{1/2}·(ρ^{1/2}|L_U h|)`
with `ρ^{1/2} ∈ L^6` and `ρ^{1/2}|L_U h| ∈ L²`, giving exactly `L^{3/2}` by
`1/6 + 1/2 = 2/3`. No better global exponent is available from the hypotheses.
Scaling is consistent: `w(λv) = λw(v)` gives `A(λv) = λ²A(v)`, and
`M_{λU} = λM_U`, `E_{λU} = E_U`, `P_{λU} = P_U`, so `B_{λv} = λB_v`, matching
the `1`-homogeneity of the bound `2‖U‖_3‖h‖_3` in `U`.

*`eq:Hessian`.* `⟨M_U L_U h, k⟩ = ⟨k, L_U h⟩_U = ⟨L_U k, L_U h⟩_U` since
`M_U` is symmetric and `P_U k ⟂ L_U h`. Symmetry and diagonal nonnegativity
follow ✓. I confirmed the bilinear identity to 15 significant digits in the
finite-dimensional model (RA3), which is a genuine test because symmetry of the
Hessian of `Q` is not built into the construction of `B_v`.

### Q5. `cor:second`: the second variation and the time derivative

**Verdict: all three formulas are correct as stated.**

`eq:Qsecond`. `Q` is `C¹` along the line with `d/ds Q(v+sh) = ⟨A(v+sh), h⟩`
(`eq:Qprime`), so `Q(v+εh) − Q(v) = ∫₀^ε⟨A(v+sh), h⟩ ds`; inserting
`A(v+sh) = A(v) + sB_vh + o(|s|)` and using
`|∫₀^ε o(|s|) ds| ≤ |ε| sup_{|s|≤|ε|} o(|s|) = o(ε²)` gives
`Q(v) + ε⟨A(v),h⟩ + (ε²/2)‖L_U h‖_U² + o(ε²)` ✓, for both signs of `ε`. I
re-derived `eq:Qprime` itself (upper error from `eq:Babove`; lower error by
testing `w(v+h) − h` at `v` and then `eq:Alip`), and it is correct with
`O(‖h‖_3²)`.

Two independent consistency checks passed: (i) `Q` is convex, being the partial
minimization of a jointly convex function, so the second-order term must be
`≥ 0`, and `‖L_U h‖_U² ≥ 0` ✓; (ii) for `h ∈ G_3` one has `Q(v+h) = Q(v)`
identically and `L_U h = 0`, so all orders vanish ✓. Numerically, the discrete
model reproduced `‖L_U h‖_U²` to three digits at `ε = 10^{-3}` from both sides.

`eq:Atime`. Correct, and it is exactly the step that needs Hadamard (see Q4).

`eq:Qtt`. `d/dt Q(v(t)) = ⟨A(v(t)), v_t(t)⟩` by the chain rule for the `C^{1,1}`
functional `Q`; differentiating the `L^{3/2}`–`L^3` pairing by the product rule
needs `A(v(t))` differentiable in `L^{3/2}` (from `eq:Atime`) and `v_t`
differentiable in `L^3` (from `v ∈ C²(L^3)`), both available, and gives
`⟨B_{v(t)}v_t, v_t⟩ + ⟨A, v_tt⟩ = ‖L_U v_t‖_U² + ⟨A, v_tt⟩` ✓. The one-sided
statement at an initial time is correct because the Hadamard statement is
already two-sided. The corollary claims a pointwise second derivative, not
`Q ∈ C²`, and does not overreach: continuity of
`t ↦ ‖L_{w(v(t))}v_t(t)‖²_{w(v(t))}` is neither claimed nor available. I
checked the degenerate instant `w(v(t)) = 0`, where the formula gives
`Q'' = 0`, against the exact behaviour `Q(v(t)+s·) ~ c|s|³`; consistent.

### Q6. Completeness and density for `H_U`

**Verdict: `eq:Hequiv` and `eq:L3embed` are correct and sharp; the density
claim is correct; the definition is under-specified but repairable.**

`eq:Hequiv`: pointwise `ρ|a|² ≤ a·M_U a = ρ|a|² + (U·a)²/ρ ≤ 2ρ|a|²` on
`{ρ>0}`, both sides `0` on `{ρ=0}` ✓. Both constants are attained (`a ⟂ U` and
`a ∥ U`), confirmed numerically.

Completeness: `ρ dx` is σ-finite (`|{ρ > 1/n}| ≤ n³‖ρ‖_3³ < ∞` and
`∫_{ρ>1/n} ρ dx ≤ ‖ρ‖_3|{ρ>1/n}|^{2/3} < ∞`, with `{ρ=0}` of `ρ`-measure zero),
so `L²(ρ dx; R³)` is complete, and `eq:Hequiv` transfers completeness to
`‖·‖_U` ✓.

`eq:L3embed`: `‖h‖_U² ≤ 2∫ρ|h|² ≤ 2‖ρ‖_3‖h‖_3² = 2‖U‖_3‖h‖_3²` ✓.

Density: for `a ∈ L²(ρ dx)` choose the representative vanishing on `{ρ=0}` and
truncate, `a_n = a·1_{|a|≤n}·1_{|x|≤n}`; dominated convergence with dominant
`|a|²` gives `∫ρ|a−a_n|² → 0`, and each `a_n` is bounded, compactly supported,
hence in `L^3` ✓. So the embedding `L^3 → H_U` has dense range ✓. (This claim
is decorative: no proof in Section 3 uses it. The density that *is* used is
density of `G_3` in `E_U`, which holds by definition of `E_U` as a closure.)

The definition itself ("the Hilbert space of measurable vector fields modulo
equality for the measure `ρ dx`") presupposes the structure it then verifies
and does not state the membership condition `∫ρ|a|² < ∞`; see repair R5.

### Q7. Does `app:weighted` agree with our audited HF23?

**Verdict: the appendix is correct, but it does not reconstruct HF23, and the
index note's framing of this point is wrong. Its audited counterpart is
HF18-A Theorem 2, which it upgrades using HF23.**

HF23 explicitly disclaims this identity. `hf23-divcurl-continuation.tex` line
262 reads: *"Neither the stronger weighted identity `D_Q = D_3(w)` from HF18
nor a time derivative of `w` is required to prove the main unweighted theorem
below."* HF23's audited content is the unweighted `5/4`, `1/4` div–curl
estimate, which is reconstructed in `app:spatial`, not here.

The correct comparison target is `hf18-hodge-regularity.md` Theorem 2 and
Corollary 1, **audited PASS** in `hf18-review-hodge-regularity.md`. Item by
item:

| HF26 `app:weighted` | audited HF18-A | agreement |
|---|---|---|
| `D = ∫ρ(\|∇w\|² + \|∇ρ\|²) = ∫(\|∇V\|² − (1/9)\|∇\|V\|\|²)` (`eq:Didentity`) | (2.2) + (1.12) + (2.1) | exact |
| `D ≥ (8/9)‖∇V‖_2²` (`eq:Dcontrol`) | (2.1) | exact |
| `‖w‖_9³ ≤ (9/8)S²D` (`eq:Dcontrol`) | (2.2) corollary `D_Q ≥ (8/9S²)‖w‖_9³` | exact |
| `\|∇A\| ≤ (4/3)\|w\|^{1/2}\|∇V\|` (`eq:gradA`) | (1.11) | exact |
| `\|∂_kV\|² = ρ\|∂_kw\|² + (5/4)ρ\|∂_kρ\|²` | (1.12) | exact |
| `∂_kA·∂_kw = ρ(\|∂_kw\|² + \|∂_kρ\|²)` | (1.12) | exact |

I verified all six pointwise identities symbolically on an explicit smooth
non-symmetric field, plus the audited HF22 remark
`|∇A|² = ρ(|∇V|² + (7/9)|∇|V||²)`, and they agree to machine precision. As a
cross-check on the constants I re-derived `C_♯ = (3/2)C_9S` in `eq:Kq` from
`eq:gradA` and `eq:Dcontrol` through the `(3,9,18,2)` Hölder split and obtained
exactly `(4/3)·C_9·(9/8)·S`; the constants in my scope are used consistently
downstream.

**What the appendix genuinely adds** — and what should be said explicitly — is
that HF18-A could only read `∫ρ(|∇w|² + |∇ρ|²)` *in the approximate-gradient
sense*, because hypothesis (H1) (`w ∈ W^{1,1}_loc`) was open there; HF18-A's
own note (N2) says so verbatim. HF23 discharged (H1) in the strong form
`∇w ∈ L²`, and `app:weighted` uses that (via `app:spatial`) to make the
identity a genuine weak-derivative statement, with no special treatment of the
zero set beyond the standard `∇w = 0` a.e. on `{w = 0}`. That is the real
content of "without a zero-set shortcut", and it is a legitimate upgrade of one
audited result by another. It is not, however, a reconstruction of HF23.

*Steps re-derived independently.* `eq:appendweightedDQ` (translation invariance
of `G_3` plus stationarity at both endpoints) ✓; the monotonicity lower bound
`W_h/2` ✓; `W_h ≤ 4∫f|δ_hu|² ≤ 8‖w‖_3‖∂_ku‖_3²` via weighted Cauchy–Schwarz
and `|j(a) − j(b)| ≤ (|a|+|b|)|a−b|` ✓; `V ∈ H¹` with `‖V‖_2² = ‖w‖_3³` ✓;
`|∇|V||² = (9/4)ρ|∇ρ|²` ✓; the difference-quotient convergences
`δ_hV → ∂_kV` in `L²`, `δ_hA → ∂_kA` in `L^{3/2}`, `δ_hu → ∂_ku` in `L³` (all
by Minkowski's integral inequality plus `L^p`-continuity of translation, which
needs only the *derivative* in `L^p` — this matters because `w ∉ L²` is
explicitly not asserted) ✓; the Vitali step with dominant `2|δ_hV|²` ✓;
integration by parts in the `W^{1,3/2}`–`W^{1,3}` pairing ✓.

`eq:appendVcomp` is correct, and its verification method is sound: both sides
are affine in the angle cosine `c` for fixed `r = |a|`, `s = |b|` — I confirmed
this symbolically (`∂²/∂c² = 0` for both) — so checking `c = ±1` suffices. At
`c = +1`, `M − (8/9)S = (16r^{3/2}s^{3/2} + r³ − 9r²s − 9rs² + s³)/9 ≥ 0` with
equality at `r = s` (so `8/9` is sharp), and `2S − M = (r+s)(r²+s²) −
4(rs)^{3/2} ≥ 0` by AM–GM. At `c = −1`, `M − S = rs(√r−√s)² ≥ 0` and
`2S − M = (r+s)(r−s)² + 4(rs)^{3/2} ≥ 0`. A numerical sweep gives the attained
range `[0.888889, 1.05157]` (the upper end at `|b|/|a| ≈ 0.1895`, `c = −1`), so
the lower constant `8/9` is sharp and the upper constant `2` is loose by nearly
a factor `2`. All correct as claimed.

The one place where the stated justification does not deliver the stated
constant is `eq:appendweightedgrad`; see repair R4.

---

## Required repairs

Numbering is `R1`–`R8`. Every repair is an edit to the *import*, never to the
frozen `.tex`.

**R1 (statement-level).** `rem:linear-scope`, first sentence, currently reads
"The weighted linearized problem in the repaired HF22-B discussion is now
justified". This over-reads. HF22-B §4.1 flags `(LIN)` as formal because *"the
ansatz `q_eps = eps grad phi + o(eps)` presupposes differentiability of
`eps -> q(U+eps h)` in `L^3` at `eps = 0`, which is exactly the object whose
regularity is in question"*. `thm:weightedresponse` proves the **weighted**
version of that differentiability and nothing about the `L^3` version, so what
is justified is the identification of the weighted limit, not HF22-B's `L^3`
ansatz. Replace with, e.g.: "the weighted linearized problem `(LIN)` of the
repaired HF22-B discussion is now justified *in the weighted topology*: the
`H_U`-limit of `(q(v+εh) − q(v))/ε` exists and equals `−P_U h`, which is
exactly the Lax–Milgram solution of `(LIN)`. HF22-B §4.3's residual question —
the higher-integrability gain from the degenerate energy space `L²(|U| dx)` to
`L^3` for `−div(a ∇φ) = div(a h)` — is untouched, and so is §4.4's open
question about the rate on `{U = 0}`."

Add the constant-consistency observation, which is a genuine corroboration:
`‖P_U h‖_U ≤ ‖h‖_U` plus `eq:Hequiv` gives `∫ρ|P_U h|² ≤ 2∫ρ|h|²`, reproducing
HF22-B §4.2's Lax–Milgram bound with constant `√2` exactly.

**R2 (statement-level).** `app:weighted`'s attribution. The weighted
dissipation identity is not an HF23 result; HF23 states that it does not need
it. Attribute the reconstruction to audited HF18-A Theorem 2 (2.1)–(2.3) and
Corollary 1(c),(d),(f), and state the one thing that is new: HF18-A's
`∫ρ(|∇w|² + |∇ρ|²)` was valid only in the approximate-gradient sense under the
then-open (H1), whereas HF23's discharge of (H1) (`∇w ∈ L²`, imported here
through `app:spatial`) makes it a genuine weak-derivative identity. Without
this the import would record a false dependency and would silently re-audit an
already audited result.

**R3 (statement-level).** Hypothesis placement for `eq:Didentity`–`eq:gradA`.
The main text introduces them after a block whose stated hypothesis is
"solenoidal `u ∈ H¹`", under the phrase "For a smooth enough solenoidal field",
but `app:weighted` proves them only for solenoidal `u ∈ H^m`, `m ≥ 4`, and —
unlike `app:spatial`, which extends `eq:divcurl` to all solenoidal `H¹` by
mollification — performs no extension. State `u ∈ H^m`, `m ≥ 4` at
`eq:Didentity`, or supply the extension. On the classical branch this is
harmless, but the quantifier must not be left ambiguous in the import.

**R4 (expository, closes a constant gap).** `eq:appendweightedgrad`. As
justified ("an a.e. convergent subsequence of the already known `L²` difference
quotients and Fatou"), Fatou applied to `ρ|δ_hw|² ≤ W_h` yields the constant
`8`, not `4`. The stated constant `4` requires applying Fatou to the *full*
integrand `(|τ_hw| + |w|)|δ_hw|²`, whose a.e. limit is `2ρ|∂_kw|²`, which needs
the additional (true, but unstated) fact `τ_hw → w` a.e. along the subsequence,
available from `τ_hw → w` in `L^3`. Add that sentence. The constant is not
load-bearing — it is used only to conclude square-integrability, for which `8`
suffices — so this changes no downstream statement.

**R5 (expository).** `eq:Hspace`. State the membership condition
`∫ρ|a|² < ∞`, record that `H_U` *is* `L²(ρ dx; R³)` as a set, and note that
`ρ dx` is σ-finite because `ρ ∈ L^3` — the σ-finiteness is what completeness
and the truncation/exhaustion density argument both rest on. As written the
sentence assumes the Hilbert structure it then verifies.

**R6 (expository).** `lem:jTaylor`. (a) Say that the displayed decomposition is
proved under the normalization `|a| ≥ |b| > 0`, and that the interchange of
`a, b` is licensed because the left-hand side of `eq:jmatrixlip` is symmetric.
(b) Record that `4` and `2` are not sharp: the ratio equals exactly `2`
(respectively `1`) on the collinear same-direction families `a = αe`, `b = βe`
(respectively `a = te`, `d = e`), and no sweep found anything larger. This
matters only if the `O(|ε|^{1/3})` and `O_m(|ε|^{2/3})` remainders are ever
quantified, but a later reader who recomputes and gets `2` should not conclude
the lemma is wrong.

**R7 (expository, and the most useful addition).** In `thm:Aderivative`'s
proof, add the two sentences that make the section self-defending against the
boundary-section warning at line 1055:

1. On `{ρ = 0}`, `M_U = 0` and `J_ε(z_ε) = j(d_ε)/ε`, whose `L^{3/2}` norm over
   that set is `‖d_ε‖_{L^3({ρ=0})}²/|ε| = O(|ε|^{1/3})`; the zero set therefore
   contributes nothing to the unweighted limit by `eq:jTaylor` alone, with no
   control of the difference quotient there. This is exactly why an `L^{3/2}`
   conclusion is available although the weighted differential of `q` does not
   control its unweighted `L^3` differential near `w = 0`.
2. The Hadamard (rather than Gateaux) form is load-bearing: `eq:Atime` applies
   the derivative along the varying directions `(v(t+ε) − v(t))/ε`, not along a
   fixed direction.

**R8 (expository).** `app:weighted`'s two chain rules — `A = j(w) ∈ W^{1,3/2}`
with `∇A = Dj(w)∇w`, and `∂_kV = ρ^{1/2}(∂_kw + (1/2)ŵ ∂_kρ)` — are asserted in
one clause each ("The chain rule yields", "the chain rule, first for truncated
maps"). `Dj` is unbounded, so both need a truncation or mollification argument;
these are precisely the two points at which audited HF18-A Corollary 1(c) is
careful. Either cite HF18-A Corollary 1(c) or reproduce the truncation. The
conclusion is correct either way.

---

## Refutation attempts made, and their outcomes

**RA1. Break the Lipschitz constant `4` or the remainder constant `2`
(`lem:jTaylor`).** `4·10⁵` random pairs over six decades, biased toward
near-equal, antipodal and zero configurations, plus a dedicated antipodal
one-parameter sweep and a collinear-opposite sweep for the remainder.
**FAILED.** Attained maxima `2.000` and `1.000` (on explicitly identified
collinear families); both claimed bounds hold with a factor `2` to spare.

**RA2. Find a circular step in Step 3 of `thm:weightedresponse` — a place where
strong convergence, or `L^3` convergence, of `z_ε` is used to produce strong
convergence.** Line-by-line reconstruction of the Minty argument, tracking
every appearance of `‖z_ε‖_3`. **FAILED.** All four appearances are the
divergent a priori bound multiplied by a strictly larger power of `|ε|`; the
only convergence used is weak convergence in `H_U` against a *fixed* `z_m`.

**RA3. Refute the identification of the limit with `L_U h` by building the
whole variational structure in finite dimensions and computing.** `R^8` with a
`3`-dimensional "gradient" subspace `G`, `F(x) = (1/3)Σ|x_i|³`, base point
solved so that stationarity `B^T j(U) = 0` holds exactly *and* `U₁ = 0` (a
genuine degenerate weight site). Difference quotients computed by high-accuracy
convex minimization for `ε = ±10^{-1} … ±10^{-4}`. **FAILED to refute.**
`‖z_ε − L_U h‖_U → 0` at rate `O(ε)` for both signs;
`⟨B_v h, k⟩ = ⟨L_U h, L_U k⟩_U` agreed to 15 digits (a nontrivial test, since
symmetry of the Hessian is not built into `B_v`); the second-variation quotient
converged to `‖L_U h‖_U²` from both sides; and the `L^{3/2}`-analogue
difference quotient of `A` converged to `M_U L_U h`, with the zero-weight
component going to `0` at rate `O(ε)` exactly as `eq:Remactual` predicts.

**RA4. Exhibit a configuration where `E_U` is deficient on the zero set, so
that the weighted limit is genuinely undetermined there and the theorem is
vacuous or inconsistent.** Second finite-dimensional model in which `G` contains
a vector supported entirely on the zero-weight site, so `E_U` has dimension
`k − 1` and `L_U h` is not pinned at that site. **FAILED to refute the
theorem**, and it *confirms the scope*: the weighted convergence still held,
and the value at the zero-weight site was numerically arbitrary. This is
HF22-B §4.2's nontrivial kernel, and `thm:weightedresponse` correctly says
nothing about it. (Note for the record: in *finite* dimensions with `G`
finite-dimensional, `h + G` meets `E_U^⊥` in a single point of the ambient
space, so the model cannot exhibit the genuinely infinite-dimensional failure —
an `E_U`-element with no `L^3` representative in `h + G_3`. The model therefore
cannot refute the `L^3` disclaimers either; it can only fail to contradict
them, which it does.)

**RA5. Break the `ε < 0` branch.** Traced every occurrence of `ε`: `|ε|` in
`eq:deps`/`eq:zweighted`/remainders, `ε²` in the monotonicity step (which is
where a sign error would be fatal), and the identity
`⟨J_ε(z_ε), z_ε − z_m⟩ = 0` which is sign-free. Confirmed numerically in RA3
for both signs at every `ε`. **FAILED.**

**RA6. Break `cor:second` against an exact computation.** Two independent
checks: convexity of `Q` (partial minimization of a jointly convex functional)
forces a nonnegative second-order term, which `‖L_U h‖_U² ≥ 0` respects; and at
`v ∈ G_3` (so `U = 0` a.e.) the exact homogeneity `Q(v + εh) = |ε|³Q(h)` must
make the second-order term vanish, which it does since `L_U h = 0` in the zero
space. Also checked `h ∈ G_3`, where `Q(v+h) = Q(v)` identically and every
order must vanish. **FAILED.**

**RA7. Break `eq:appendVcomp`'s constants `8/9` and `2`.** Symbolic proof that
both sides are affine in the angle cosine, symbolic factorization at
`c = ±1`, and a `4·10⁵`-sample plus endpoint sweep. **FAILED.** Attained ratio
range `[8/9, 1.05157]`; `8/9` sharp at `r = s`, `2` loose.

**RA8. Find a numerical disagreement between `app:weighted` and audited
HF18-A.** All six pointwise identities evaluated symbolically on an explicit
non-symmetric smooth field, plus the HF22-audited sharper form
`|∇A|² = ρ(|∇V|² + (7/9)|∇|V||²)`, plus an end-to-end recomputation of
`C_♯ = (3/2)C_9S`. **FAILED to find a disagreement.** They agree exactly.

**RA9. Find an unstated hypothesis or an attribution error.** **PARTIALLY
SUCCEEDED**, three times, all repaired above: the HF23-vs-HF18-A attribution
(R2), the `H^m`/`H¹` quantifier for `eq:Didentity` (R3), and the constant `4`
in `eq:appendweightedgrad` whose stated Fatou justification delivers `8` (R4).
Also the `rem:linear-scope` over-reading (R1).

---

## Controller-note observations

Recorded for the controller; these are observations about
`hf26-temporal-continuation.md`, not about the frozen candidate.

1. **Wrong comparison target.** The note says "The appendices reconstruct
   HF23's estimate and a weighted dissipation identity; check these against our
   already audited HF23 rather than assuming agreement." Only `app:spatial`
   reconstructs HF23. `app:weighted` reconstructs audited **HF18-A** Theorem 2;
   HF23's own text states that it does not need that identity. An audit that
   followed the note literally would have compared `app:weighted` against a
   document that disclaims it.
2. **A naming collision worth recording.** HF22-B §4.2 already uses `H_U` for
   the completion of the *gradient quotient*, which is HF26's `E_U`, not
   HF26's `H_U` (all of `L²(ρ dx)`). Since `rem:linear-scope` explicitly links
   the two documents, an import that mixes the notations will be read wrongly.
3. The note's other characterizations of Section 3 that I checked are accurate:
   the strong-convergence claim, the degeneracy, the `L^{3/2}` Hadamard target,
   the formula `∂_h A(v) = M_w L_w h`, and the warning that the weighted
   differential of `q` does not control its unweighted `L^3` differential. The
   candidate does respect that warning throughout Section 3.

---

## What I did NOT check

- Sections 1, 4, 5, 6, 7, 8, 9 of the candidate, including `thm:NSdeparture`,
  `thm:temporal`, `thm:qtime`, `cor:residualmeasure`, `thm:curve`,
  `cor:curveenstrophy`, `thm:fullconditional` and the crossing-count
  discussion. In particular I did **not** check the uses of `cor:second` and
  `eq:Atime` made in `sec:departure` (lines ~531, 541, 597, 607, 623) or in
  `sec:boundary` (line 1049) beyond confirming that the displayed
  `‖A_t‖_{3/2} ≤ 2‖w‖_3‖u_t‖_3` is the operator bound of
  `thm:Aderivative` applied correctly.
- `app:spatial` (the HF23 reconstruction) as a proof. I re-derived only
  `eq:appendmatrix` (correct: `(t²+2t+3)/(2t²) ≥ 3` ⟺ `(1−t)(5t+3) ≥ 0` on
  `[0,1]`) and `eq:appenduniform`'s arithmetic (`B ≤ (B + Y/2)/3 ⟹ B ≤ Y/4`,
  `‖∇w‖_2² ≤ 5Y/4`), both correct, because `app:weighted` depends on its
  conclusion. Whether `app:spatial` genuinely reproves HF23 is Scope-A
  territory of the HF23 audits and was not re-litigated.
- `app:positive` and the seed field `W_0`.
- Section 2 as a set of statements in its own right; I re-derived only the
  inputs Section 3 and `app:weighted` consume.
- Novelty and prior art for `thm:Aderivative` (the candidate's own §
  `sec:priorart` flags Li's preprint on directional differentiability of metric
  projections). I made no novelty judgement and import no external theorem.
- Any Lean or formal statement surface. No build was run.
- Whether `E_U = H_U` can occur for physically relevant `U` (which would make
  `B_v = 0`). This is a question about the geometry of `G_3` in `L²(ρ dx)`, not
  about the correctness of Section 3; the theorem is a true statement either
  way. I verified only that it does *not* occur in the model case of a weight
  supported in a ball, where divergence-free fields with vanishing normal trace
  are `H_U`-orthogonal to every global gradient.

---

**Nothing in this review promotes a result, discharges a hypothesis, or changes
a claim-graph node.** `thm:weightedresponse`, `thm:Aderivative` and
`cor:second` remain unaudited-elsewhere candidate results whose Section-3
proofs I find correct, subject to repairs R1–R8 at import.
