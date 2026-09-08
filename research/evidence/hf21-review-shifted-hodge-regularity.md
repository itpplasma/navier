# Audit of HF21-A `hf21-shifted-hodge-regularity.md`

Independent proof audit, 2026-09-06, MODE: proof-audit (adversarial reconstruction).

**Freeze.**

```
target : research/evidence/hf21-shifted-hodge-regularity.md
sha256 : 4dfa00cc8cdce638a1783b2a1a62ca688e230ab9273e6e8823acfc6ebed49c8e
HEAD   : 1c0f68ec34d4987d5345bf048d4c628fc16a8816
```

Everything below was reconstructed from the first nontrivial implication. Constants,
exponents and matrix algebra were recomputed by hand and, where indicated, independently
by machine in this session's scratchpad (`aud3.py`, `aud4.py`, `aud5.py`; the note's own
`chk.py` was not read and not reused). The one external source that carries weight
(Stern, arXiv:2403.19481v2) was fetched and read in this session, not taken from the note.

---

## VERDICT

**REPAIR.** The note's five headline results are correct as *statements*, and four of
them are correct as *proofs*. One proof — Theorem 2, the rigidity of linear zeros — has a
genuine gap at a step that is false as written, and the gap bites in precisely the case
the note's own Corollary 2.1 needs (the HF18-B oscillation model has a rank-two `L`). The
gap is repaired below in full, by cases on `rank L`, with the replacement lemma displayed
and proved and cross-checked numerically; the theorem then stands exactly as stated.

Three further defects are recorded and repaired: (D2) Theorem 6' is *displayed* stronger
than its proof yields (a `ζ^2` weight appears on a right-hand term where Cauchy–Schwarz
gives only `1_{supp ∇ζ}`); (D3) Theorem 6's third bullet silently assumes a gradient bound
`|∇w| ≲ d^{β-1}` that does **not** follow from `|w| ≍ d^β`, so "the entire model class of
power-law vanishing on rectifiable zero sets is settled affirmatively" is not proved;
(D4) the repeated summary phrase that the order of vanishing is "pinned to `1`" / "pinned
near `β = 1`" is an overclaim — the proved statements exclude only `β > 1` (Theorem 5) and
`β = 1/2` in the `C^1`-nondegenerate model (Theorem 2), leaving all of `β ∈ (1/2, 1]`.

No circularity was found. No identity was found masquerading as an estimate. No
instantaneous fact was found promoted to a time-integrated one. The first gap is
untouched, exactly as the note says. Every attempted refutation of the surviving claims
failed, and two of them (Theorem 2's mechanism, Corollary 2.1's closed form) were
independently confirmed numerically to four figures.

---

## REVIEWED SCOPE

Checked, in the order requested:

1. §1.1–1.3 literature placement, with arXiv:2403.19481v2 fetched and read.
2. §2.1 Theorem 1 and corollaries (a), (b), (c).
3. §2.2 Theorem 2 (full algebra, error term, the analytic-continuation step, the chain
   `B = 2L − L^T` → `L = 0`) and §2.3 Corollary 2.1 (both computations recomputed and
   re-verified numerically), plus its compatibility with audited HF18-B Prop. 2.2.
4. §3 Theorem 3 (a)–(d), the global Riesz-transform statement, Remark 3.1, Corollary 3.3.
5. §4 Proposition 4.1, Theorem 4 (4.2), (a), (b), (c), Proposition 4.4 (i)–(v) including
   its minimality certificate against all of `G_3`.
6. §5 Theorem 5, Corollaries 5.1–5.2, Theorem 6, and the quantified shortfall.
7. §6 Theorem 6' (constants recomputed line by line) and the obstruction list O1–O4.
8. §§7–10 record consistency: scaling table C5, boundary terms C6, the scale budget
   family, the non-claims.

Cross-read for compatibility: `hf18-divergence-speed-link.md` §1.3 (Lemma A), §1.4
(Prop. 1.4), §2.3 (Prop. 2.2, Lemma B); `main.tex` `rem:quotient-related`;
`PLAN.md` "HF21". The three HF19 notes and HF20 were not used, consistent with the note's
own declaration that it does not use them.

---

## FIRST BAD BRIDGE

**§2.2, proof of Theorem 2, the sentence:**

> "Hence `M` does not vanish identically on any open set of directions, so by continuity
> there are an open cone `Γ ⊆ Γ_1` and `c_1 > 0` with `|M(n(θ))| >= c_1` on `Γ`."

This inference is invalid. The directions that actually occur are not free: on `Γ_1` one
has `n(x) = Â(x) → \widehat{Lθ}`, so the set of limiting directions is

```
N(L) := { \widehat{Lθ} : θ ∈ Γ_1, Lθ ≠ 0 }  ⊆  S^2 ∩ Range(L).
```

`N(L)` is an open subset of `S^2` **only if `L` is invertible**. If `rank L = 2` it is an
open arc of a great circle (measure zero in `S^2`); if `rank L = 1` it is a single point
`±\hat a`. In those cases the preceding paragraph — which proves only that `M` cannot
vanish on an *open subset of the sphere* — says nothing whatever about `M` on `N(L)`, and
the quantitative lower bound `|M(n(θ))| >= c_1` does not follow.

This is not a pedantic case: the note's own flagship application is rank-deficient. The
HF18-B oscillation model of §2.3 has, near its zero line, `F ≈ (−3b, a, 0)`, i.e.

```
L = [[0, −3, 0], [1, 0, 0], [0, 0, 0]],   rank L = 2, tr L = 0,
```

so Theorem 2 as proved does not cover the very family Corollary 2.1 is about. (Corollary
2.1 itself is *not* damaged — it is established by a direct closed-form computation that
does not route through Theorem 2; see EVIDENCE.)

**A second, smaller defect in the same proof.** The error term in (2.3) is asserted to be
`O(r^{1/2})`, on the ground that the corrections to `∇A` and to `n` are `O(r)`. Under the
stated hypothesis `A ∈ C^1` the correction to `∇A` is only `o(1)` (that is what continuity
of `∇A` gives; `O(r)` would need `A ∈ C^{1,1}`). Multiplied by `|A|^{-1/2} = O(r^{-1/2})`
the error is `o(r^{-1/2})`, not `O(r^{1/2})`. The conclusion survives — see below — but
the displayed rate is wrong and must not be quoted.

---

## EVIDENCE

### E1. Everything before the bad bridge is correct

**§1.1, the Stern identification.** Fetched arXiv:2403.19481v2 in this session and read
the relevant statements. Confirmed verbatim:

- `C_p^k(M) := {f : f ∈ L_p^k(M) and df ∈ L_p^{k+1}(M)}`, `B_p^k(M) := d C_p^{k-1}(M)`,
  `Z_p^k(M) := {z ∈ C_p^k(M) : dz = 0}`.
- Lemma 2.2: "For each `ζ ∈ B_p^k(M)`, `∃! β_∞ ∈ C_p^{k-1}(M)` such that `dβ_∞ = ζ`, and
  `d*(|β_∞|^{p-2}β_∞) = 0`."
- Theorem 2.9: "For each `φ ∈ H^k_{p,red}(M)`, `∃! h ∈ Z_p^k(M)` such that `[h]_red = φ`,
  and `d*(|h|^{p-2}h) = 0`."
- §3: "By elliptic regularity, a `p`-harmonic form `h` is smooth in a neighborhood of any
  point where it is nonzero. It is not necessarily smooth, however, at any point `x_0`
  where `h(x_0) = 0`, but it is Hölder continuous. (See [Uhl77, Main Theorem].)"
- **Additionally verified, and load-bearing for the note's "decisive reading":** the paper
  *defines* `H_p^k(M) := {h ∈ Z_p^k(M) : d*(|h|^{p-2}h) = 0}`. So "`p`-harmonic form"
  there means **closed** and nonlinearly coclosed, and the Uhlenbeck-credited smoothness
  attaches to that class only.
- On `β_∞` the source states no regularity beyond `β_∞ ∈ C_p^{k-1}(M)`.

The identification itself is legitimate and I re-derived it: with `n = 3`, `p = 3`,
`k = 2`, our `w` satisfies `w ∈ L^3` and `dw = curl u ∈ H^{m-1} ⊂ L^3`, so `w ∈ C_3^1`;
`u ∈ C_3^1` too, so `ζ = curl u = du ∈ B_3^2`; and `d*(|w|w) = −div(|w|w) = 0`. By the
uniqueness in Lemma 2.2, `w = β_∞`. The note's claim 7 is **confirmed**, including the
negative half. This is a real correction to `rem:quotient-related` in the manuscript,
which currently cites only Sibner–Sibner, Scott and Iwaniec–Scott–Stroffolini and does not
name Stern.

The `curl u = 0` aside is also correct: `u ∈ L^3` solenoidal and curl-free is harmonic
componentwise, hence `0` by Liouville, hence `w = q ∈ G_3` and the Euler–Lagrange
condition with `g = w` forces `∫|w|^3 = 0`.

**§1.2, Uhlenbeck.** The negative claim is safe and does not depend on the [MO] sourcing:
failures (i)–(iii) are read off *our* operator `a(x,ξ) = |u(x)+ξ|(u(x)+ξ)`, whose
degeneracy at `ξ = −u(x)` with `u(x) ≠ 0` is the audited HF18-A (1.3)–(1.4). The note
correctly does **not** import any `C^{1,α}` conclusion; check C2 is honestly answered.

**§2.1, Theorem 1.** All three parts are correct.

- (2.1): `q ∈ G_3` is an `L^3` limit of `∇ψ`, `ψ ∈ C_c^∞`; `curl` is continuous
  `D' → D'`, so `curl q = 0` in `D'` (this is exactly (P3), audited). Hence
  `curl w = curl u` in `D'`. `H^{m-1} ⊂ C^{1,1/2}` for `m ≥ 4`: `H^3(R^3) ⊂ C^{k,α}` with
  `k+α = 3 − 3/2 = 3/2`, i.e. `C^{1,1/2}`. ✓
- The prompt's worry — is "`sk(∇w) = sk(∇u)` is smooth" legitimate when `∇w` is only a
  distribution? — is answered yes. `∇w ∈ D'` always exists; the assertion is that its
  skew part *equals a `C^{1,1/2}` function*, which is the content of (2.1) and involves no
  claim that `∇w` is a function.
- (b): the load-bearing step is the a.e. vanishing of the **full** gradient. It is
  obtained componentwise: for `w ∈ W^{1,1}_loc`, `∇w_j = 0` a.e. on `{w_j = 0}`, and
  `{w = 0} ⊆ {w_j = 0}` for each `j`, so `∇w = 0` a.e. on `{w = 0}`, so its skew part
  vanishes a.e. there; two `L^1_loc` representatives of the same distribution agree a.e.,
  so `ω = 0` a.e. on `{w = 0}`. Hence `|{w = 0} ∩ {ω ≠ 0}| > 0` refutes (H1). ✓
- (c): `∫_E|∇w| ≤ (ess inf_E|w|)^{-1/2}|E|^{1/2}‖∇V‖_{L^2(E)}` by (A6) and
  Cauchy–Schwarz, and the approximate-to-weak identification is exactly Proposition 4.1
  applied on `E`; the forward reference is legitimate because Proposition 4.1 is
  independent of §2. ✓

### E2. The bad bridge, and why the theorem is nevertheless true

The algebra up to (2.4) is correct and I reproduced all of it.

With `n = Â` and `(∇A)_{ij} = ∂_iA_j`, `f(z) = |z|^{-1/2}z`,
`Df(z) = |z|^{-1/2}(I − ½ ẑ⊗ẑ)`:
`∂_iw_j = |A|^{-1/2}(∂_iA_j − ½ Â_jÂ_k∂_iA_k)`, so
`∇w = |A|^{-1/2}[ ∇A − ½ (∇A)n ⊗ n ]`. Since `A_j(x) ≈ L_{ji}(x−x_0)_i`, one has
`∇A = L^T` at leading order, hence

```
2 sk(∇w) = |A|^{-1/2} [ −2 sk(L) + ½ ( n⊗L^Tn − L^Tn⊗n ) ] + (error)
        =: |A|^{-1/2} M(n) + (error).                                        ✓ (2.3)
```

Applying `M(n)` to `n` and using `n·L^Tn = n·Ln`:
`M(n)n = −2 sk(L)n + ½[(n·Ln)n − L^Tn]`, so `M(n)n = 0` gives
`sk(L)n = ¼[(n·Ln)n − L^Tn]`, i.e. `2Ln − L^Tn = (n·Ln)n`.               ✓ (2.4)

Homogenization: `2Lx − L^Tx = (x·Lx)x/|x|^2` is real-analytic on `R^3\{0}`, which is
connected, so validity on a nonempty open subset propagates to all `x ≠ 0`.  ✓
Then `B := 2L − L^T` has every vector as an eigenvector, so `B = μI`; transposing,
`2L^T − L = μI`; subtracting gives `3(L − L^T) = 0`, so `L = L^T`, and adding to
`2L − L^T = μI` gives `L = μI`; `tr L = 0` forces `μ = 0`, `L = 0`.       ✓

All of that is right. What fails is only the passage from "`M` does not vanish on an open
subset of `S^2`" to "`|M(n(θ))| >= c_1` on an open cone of `θ`", for the reason given
above. The homogenization step is also unavailable in the rank-deficient case: `M(n)n = 0`
is then known only on a great-circle arc (rank 2) or at one point (rank 1), and
real-analytic continuation from a measure-zero subset of `R^3` is not available.

### E3. Corollary 2.1 is independent of Theorem 2 and is correct

Recomputed from scratch, by hand and by machine.

*Oscillation.* `ψ = δ^2(2+cos kx_1)(sin kx_2)/k` gives
`A_1 = (∂_2ψ, −∂_1ψ, 0) = δ^2 F(kx)`,
`F(y) = ((2+cos y_1)cos y_2, sin y_1 sin y_2, 0)`. ✓ (matches HF18-B §2.3 exactly).
Zeros: `2 + cos y_1 ≥ 1` forces `cos y_2 = 0`, then `sin y_2 = ±1` forces `sin y_1 = 0`;
lines `y = (nπ, π/2 + mπ)`. ✓ Near `(0, π/2)` with `y = (a, π/2+b)`:
`cos y_2 = −sin b ≈ −b`, `2+cos a ≈ 3`, `sin y_1 ≈ a`, `sin y_2 ≈ 1`, so
`F ≈ (−3b, a, 0)`. ✓ With `ρ = (a^2+9b^2)^{1/2}`, `G = ρ^{-1/2}(−3b, a, 0)`:

```
∂_aG_2 = ρ^{-1/2} − ½ a^2 ρ^{-5/2},
∂_bG_1 = −3ρ^{-1/2} + (27/2) b^2 ρ^{-5/2},
(curl G)_3 = ∂_aG_2 − ∂_bG_1 = 4ρ^{-1/2} − ½ ρ^{-5/2}(a^2 + 27b^2).            ✓
```

On `b = 0`: `4|a|^{-1/2} − ½|a|^{-1/2} = (7/2)|a|^{-1/2}`. ✓
Independent centred-difference check (my `aud5.py`, step `10^{-4}·a`):

| `(a,b)` | numeric `(curl G)_3` | closed form |
|---|---|---|
| `(10^{-2}, 0)` | `35.0000` | `35.0000` |
| `(10^{-3}, 0)` | `110.6797` | `110.6797` |
| `(10^{-4}, 0)` | `350.0000` | `350.0000` |
| `(10^{-3}, 2·10^{-3})` | `32.4011` | `32.4011` |
| `(3·10^{-4}, −10^{-4})` | `145.6475` | `145.6475` |

Off-ray agreement (last two rows) is stronger than the note's own on-ray check and
confirms the closed form, not merely the ray value.

*Bulk.* `A_0 = curl(φ_0e_3) = (∂_2φ_0, −∂_1φ_0, 0)` with `∂_iφ_0 = −8x_i(1−|x|^2)^3`, so
`A_0 = 8(1−|x|^2)^3(−x_2, x_1, 0)`, `|A_0| = 8(1−|x|^2)^3ρ`, and
`w_0 = √8(1−|x|^2)^{3/2}ρ^{-1/2}(−x_2,x_1,0)` with speed
`f = √8(1−|x|^2)^{3/2}ρ^{1/2}`. ✓ For an azimuthal field
`curl w = −(∂_zf)e_ρ + ρ^{-1}∂_ρ(ρf)e_z`, and `ρ^{-1}∂_ρ(ρ^{3/2}) = (3/2)ρ^{-1/2} → ∞` on
the axis, where the prefactor `√8(1−|x|^2)^{3/2}` is bounded away from `0`. ✓

**Compatibility with HF18-B Prop. 2.2 — checked, no contradiction.** HF18-B Prop. 2.2
asserts, for its family, `w_δ ∈ M`, boundedness and compact support, `(H1)`, explicitly
`|∇w_δ| ∼ d^{-1/2}` at the zero lines, and `‖σ_δ‖_{3/2}^{3/2} ≥ cδ^{-5/4}`; its
conclusion is about the class `M` at `L^3` data, and it nowhere asserts that `u_δ = Pw_δ`
is smooth or `H^m`. Corollary 2.1 says `curl u_δ ∉ L^∞_loc`, which is the *same* fact as
HF18-B's own `|∇w_δ| ∼ d^{-1/2}`, and is consistent with (H1) because `d^{-1/2}` is
locally integrable across a codimension-two set (`∫_0 t^{-1/2}·t dt < ∞`). So Prop. 2.2's
conclusions survive intact, and the note's scope paragraph is accurate, not a hedge.

### E4. Theorem 3 is correct; the "no circularity" claim is genuine

`div w = div u + div q = Δφ` as a distribution requires only `u ∈ L^1_loc` solenoidal and
`q = ∇φ ∈ L^3`; `Δφ ∈ W^{-1,3}` is well defined with no regularity of `w` presupposed.
Remark 3.1 is right, and the check C1 answer is right: `σ` (the approximate-gradient
object) is used only in Corollary 3.3, downstream of (H1). ✓

Proof of (a): `f = ηT ∈ L^p` compactly supported, `ψ = N*f`, CZ gives `D^2ψ ∈ L^p` with
`‖D^2ψ‖_p ≤ C_p‖f‖_p` for `1 < p < ∞`. ✓ `Δ(φ−ψ) = T − f = 0` in `D'(B_r)` since `η ≡ 1`
there; `φ − ψ ∈ L^1_loc` (from `φ ∈ W^{1,3}_loc` and `ψ ∈ W^{2,p}_loc`), so Weyl's lemma
applies and `φ − ψ` is harmonic hence smooth on `B_r`. ✓

*Constant slip (harmless).* The interior estimate is displayed as
`‖D^2(φ−ψ)‖_{L^∞(B_{r/2})} ≤ C r^{-2}‖∇(φ−ψ)‖_{L^1(B_r)}`. The correct scaling is
`r^{-4}` (apply the derivative estimate for the harmonic vector field `h = ∇(φ−ψ)`:
`‖Dh‖_{L^∞(B_{r/2})} ≤ C r^{-4}‖h‖_{L^1(B_r)}`). Since the theorem statement carries the
constant as `C(p,r)`, nothing downstream changes. Similarly, `‖∇ψ‖_{L^3(B_r)}` is not
available for every `p > 1`, but only `‖∇ψ‖_{L^1(B_r)}` is needed, and that follows from
`∇ψ = (∇N)*f ∈ L^q_loc`, `1/q = 1/p − 1/3` when `p < 3`, `q > 1`. Both are cosmetic.

(b) is immediate. (c) follows. The restriction `1 < p < ∞` is genuinely necessary (CZ
fails at both endpoints), and (d) is the correct disposition of the endpoints: `L log L`
gives `L^1`, a measure gives only weak-`L^1`, which does **not** give (H1). Both are
labelled [MO] and non-load-bearing. ✓

Global statement: `\widehat{∂_iq_j} = (ξ_iξ_j/|ξ|^2)\widehat{div q}`, i.e.
`∂_iq_j = −R_iR_j T`, so `T ∈ L^{3/2}` gives `Hess φ ∈ L^{3/2}` by `L^{3/2}` boundedness
of the Riesz transforms. ✓ (A pedantic gap the note skips: the two tempered distributions
agree up to a polynomial, and a nonzero polynomial lies neither in `L^{3/2}` nor in
`W^{-1,3}`, so the polynomial is `0`. Conclusion unchanged.)

Corollary 3.3 is correct in both directions and is honestly scoped as a statement about
the logical structure of HF18-B's two hypotheses. (B2) is quoted faithfully from HF18-B
Lemma A (checked line by line against `hf18-divergence-speed-link.md` §1.3).

### E5. §4 is correct, including the counterexample to necessity

**Proposition 4.1.** `Ψ_τ(z) = (|z|^2+τ^2)^{-1/6}z` is `C^1` with
`DΨ_τ(z) = (|z|^2+τ^2)^{-1/6}(I − ⅓ z⊗z/(|z|^2+τ^2))`, whose operator norm is `≤ 1` times
the prefactor (eigenvalues `1` and `1 − |z|^2/(3(|z|^2+τ^2)) ∈ [2/3,1]`), so
`|DΨ_τ| ≤ (|V|^2+τ^2)^{-1/6} ≤ |V|^{-1/3} = |w|^{-1/2}`. ✓ `Ψ_τ` is globally Lipschitz
(constant `τ^{-1/3}`), so the chain rule on `V ∈ H^1` is legitimate. `|Ψ_τ(z)| ≤ |z|^{2/3}`
gives the `L^3` domination; `∇V = 0` a.e. on `{V = 0}` handles the zero set; closedness of
the weak gradient closes it. ✓

**Theorem 4.** (4.2): on `E_j`, `|w| ≥ 2^{-j-1}` gives `|w|^{-1/2} ≤ 2^{(j+1)/2}`, then
Cauchy–Schwarz per layer, then sum. ✓ (a): Cauchy–Schwarz in `j` with
`2^j|E_j| ≤ ∫_{E_j}|w|^{-1}` (valid since `|w| < 2^{-j}` on `E_j`) and
`Σ_j‖∇V‖^2_{L^2(E_j)} ≤ ‖∇V‖_2^2`. ✓ (b): the abstract fact
"`Σc_j^2 = ∞` ⟹ `∃ a ∈ ℓ^2` with `Σc_ja_j = ∞`" is standard. ✓ (c): Hölder. ✓ The
endpoint readings (`p = 2` → `|w|^{-1}`; `p = ∞` → `|w|^{-1/2}`) are right, and the
conclusion that no amount of higher integrability of `∇V` removes a negative moment of
`|w|` (O3) is a correct and useful observation.

*Scope caveat on the word "sharp".* Part (b) is sharpness of the **abstract layered
inequality**, not of the criterion for (H1): it exhibits an admissible *sequence*
`a_j = ‖∇V‖_{L^2(E_j)}`, and does not exhibit a minimizer `V` realizing it. The note's own
"Equivalently:" sentence states this correctly, but the theorem title
"(layered criterion; sharp)" and the §10 claim "is sharp in the sense of 4(b)" should be
read only in that abstract sense. Also, §7 constraint 5 attributes to Theorem 4(b) an
implication that comes from Theorem 4(a) (a counterexample needs `∫_E|w|^{-1} = ∞`
*because* (a) makes finiteness sufficient). Label slip only.

**Proposition 4.4 — the minimality certificate is genuine; I re-derived it.**
`ψ = −|x_1|x_1^2/3 = −|x_1|^3/3`, so `∂_1ψ = −|x_1|x_1` and `ψ ∈ C^2` (third derivative
jumps, second is `−2|x_1|`, continuous). Hence `χψ e_3 ∈ C_c^2` and
`A = curl(χψe_3) ∈ C_c^1`. ✓ On `B`, `A = (∂_2ψ, −∂_1ψ, 0) = (0, |x_1|x_1, 0)`,
`|A| = x_1^2`, `w = |A|^{-1/2}A = (0, x_1, 0)`. ✓ `div w = 0`, `curl w = e_3`,
`∇w` constant. ✓ (The note writes `∇w = e_2⊗e_1`; with its own convention
`(∇w)_{ij} = ∂_iw_j` it is `e_1⊗e_2`. Convention slip, no consequence.)

The load-bearing question the prompt raises — *is it really minimal against all of `G_3`?*
— is answered **yes**, and not by inspection. `A` is a curl, so `div A = 0` in `D'`; `A` is
`C^1` with compact support, so `A ∈ L^{3/2}(R^3)`; `|w|w = |A|^{1/2}·|A|^{-1/2}A = A`, so
`div(|w|w) = 0`, i.e. `w ∈ M`. Audited HF18-B Prop. 1.4 (quoted correctly as (B1), checked
against the source text) then supplies: `w` is the minimizing representative of
`u = Pw ∈ L^3`, `q = (I−P)w ∈ G_3`, and `∫|w|w·g = 0` for **all** `g ∈ G_3`. So the
Euler–Lagrange condition against the whole test class is imported, not assumed. ✓

(iii): `div q = div w − div u = div w = 0` on `B`, so `Δφ = 0` in `D'(B)`, `φ ∈ W^{1,3}_loc`,
Weyl gives `φ` real-analytic on `B`, hence `q ∈ C^∞(B)` and `u = w − q ∈ C^∞(B)` with
`curl u = curl w = e_3 ≠ 0`. ✓ (iv): `|w| = |x_1| = d(x, \{w=0\})`, `∫_B|x_1|^{-1} = ∞`,
`w ∈ W^{1,∞}(B)`. ✓ (v): `|E_j| ≍ 2^{-j}`, `|V| = |x_1|^{3/2}`, `|∇V| ≍ |x_1|^{1/2}`,
`‖∇V‖_{L^2(E_j)} ≍ 2^{-j}`, `S(B) ≍ Σ_j 2^{-j} < ∞`. ✓

**Internal consistency check I ran against Theorem 2:** here `A = (0,|x_1|x_1,0)` has
`DA = 0` on `{x_1 = 0}` — a *degenerate* zero — so Theorem 2 does not apply and there is no
contradiction with the bounded `curl w = e_3`. The example is exactly the degenerate case
Corollary 2.2 says a counterexample would have to live in. This coherence is a point in
the note's favour and I could not break it.

The honest scope note (the datum is not claimed globally `H^m`) is correct and necessary:
outside `B` the cutoff region of `A` generically has linear zeros and Theorem 2 then makes
`curl u` unbounded there. As a refutation of the *necessity* of `|w|^{-1} ∈ L^1_loc` the
example is nevertheless valid, since (H1) is local and all local hypotheses hold on `B`.

### E6. §5 is correct

**Theorem 5.** The cylinder `C = {|x'−x_0'| ≤ r/2, |z| ≤ r/2}` has farthest points at
distance `r/√2 < r`, so `C ⊂ B_r(x_0)`. ✓ `curl w_ε = ρ_ε*ω` with `w_ε = ρ_ε*w ∈ C^∞`. ✓
Stokes on each disc, `∮|w_ε|dl ≥ |∮w_ε·dl| = |∫_D(ρ_ε*ω)·n| ≥ πs^2c_ε` (trivially true if
`c_ε < 0`). ✓ Cylindrical Fubini,
`∫_C|w_ε| = ∫_{-r/2}^{r/2}∫_0^{r/2}(∮_{∂D_{s,z}}|w_ε|dl)ds dz ≥ r·πc_ε(r/2)^3/3 = πc_εr^4/24`. ✓
Divide by `|B_r| = 4πr^3/3`: `⨍_{B_r}|w| ≥ (πcr^4/24)/(4πr^3/3) = cr/32`. ✓ The constant
`32` is exactly right, and the limit `ε ↓ 0` is legitimate (`w_ε → w` in `L^1(C)`,
`ρ_ε*ω → ω` uniformly on compacts by continuity of `ω`).

Sanity check I ran: rigid rotation `w = ½ e_3 × x`, `ω = e_3`. Then
`⨍_{B_r}|w| = (3π/32)r ≈ 0.294r ≥ r/32 = 0.031r`. Consistent, with about a factor `9.4` of
slack; no contradiction, and the constant is not claimed sharp.

Corollaries 5.1 and 5.2 follow. The quantified shortfall in §5 is correct: splitting and
Hölder give `|{|w| ≥ λ} ∩ B_r| ≥ ((cr/64)|B_r|/‖w‖_{L^3(B_r)})^{3/2}`, and `r = 64λ/c`
turns this into `≥ Cλ^6`, a fraction `≍ λ^3` of `|B_r|`, hence `≥ Cλ^3` on a unit ball
after covering — far from the `|{|w| < λ}| = O(λ^{1+η})` Theorem 4 would need. I
reproduced every step. The note does not overclaim here.

**Theorem 6 — third bullet is not proved (defect D3).** The hypothesis is `|w| ≍ d^β`.
From this alone, `|∇w| ≲ d^{β-1}` does **not** follow: `|w| ≍ d^β` is compatible with
arbitrarily fast oscillation of `w` at fixed amplitude, and the only structural gradient
bound available is `|∇w| ≤ |w|^{-1/2}|∇V|` (A6), which needs a bound on `|∇V|` that is not
hypothesised. The subsequent "so **(H1)** holds locally" and the sentence "the entire model
class of power-law vanishing on rectifiable zero sets is settled affirmatively" are
therefore not established as stated. The repair is to add the gradient hypothesis (below);
with it the integrability arithmetic is correct (`∫_0 t^{β-1}dt < ∞` in codimension one,
`∫_0 t^{β-1}·t dt < ∞` in codimension two, for `β > 0`).

**Defect D4 — "pinned to 1".** Three places assert that the vanishing order is pinned to
`β = 1` (Summary bullet 4; §2.2 "Reading of Theorem 2"; §5 "pinned near `β = 1`"). What is
actually proved is: `β ≤ 1` (Cor. 5.1) and, in the `C^1` model with `DA(x_0) ≠ 0`,
`β = 1/2` is excluded (Thm 2). If `A ∈ C^1` and the zero is degenerate then `|A| = o(d)`
forces `β > 1/2`. Nothing excludes `β ∈ (1/2,1)`; e.g. `β = 3/4` survives every displayed
argument. The word "pinned" must go.

### E7. §6 Theorem 6' — constants correct, one displayed weight is not

Every step was recomputed. Translation invariance of `G_3` and of the problem gives
`∫D_hA·g = 0` for `g ∈ G_3` (change of variables sends `g ↦ τ_{-h}g ∈ G_3`). ✓ The test
field `ψ = ζ^2(D_hφ − c_k)` is compactly supported with `ψ ∈ L^3` and
`∇ψ = ζ^2D_hq + 2ζ(D_hφ−c_k)∇ζ ∈ L^3`, so `∇ψ ∈ G_3` by (P2). ✓ (A5) gives
`D_hA·D_hw ≥ (8/9)|D_hV|^2` and `|D_hA| ≤ 2√2(|τ_hw|+|w|)^{1/2}|D_hV|`. ✓ The chain
`(8/9)X^2 ≤ 2√2 XY_1 + 4√2‖∇ζ‖_∞XY_2` → `X ≤ (9/8)(2√2Y_1 + 4√2‖∇ζ‖_∞Y_2)` → squaring
with `(a+b)^2 ≤ 2a^2+2b^2` → `Y_1^2 → 2∫ζ^2|w||∂_ku|^2`,
`Y_2^2 → 2∫ζ^2|w||q_k−c_k|^2` → summing over `k` reproduces **exactly**
`(81/2)` and `162`. I get the same two constants. ✓ The consistency check is also right:
`ζ ↑ 1`, `c = 0` gives `‖∇V‖_2^2 ≤ (81/2)‖w‖_3‖∇u‖_3^2`, exactly twice the audited (A1)
bound `(81/4)‖w‖_3‖∇u‖_3^2`. ✓

**Defect D2.** In the boundary term the integrand carries `ζ|∇ζ|`, and Cauchy–Schwarz must
allocate the single factor `ζ` to the `|D_hV|` side to produce `X`. What is then left on
the other side is `‖∇ζ‖_∞ · (∫_{supp∇ζ}(|τ_hw|+|w|)|D_hφ−c_k|^2)^{1/2}` — with **no**
`ζ^2` weight. The note's `Y_2 := (∫ζ^2(…))^{1/2}` and the `∫ζ^2|w||q−c|^2` in the displayed
(6.1) therefore claim a strictly stronger inequality than the argument delivers (since
`ζ^2 ≤ 1`). Repair below; the corrected form is the one a Gehring iteration would want
anyway (an annulus term), so §6.2's conclusions are unaffected.

O1–O4 are correct and are the honest content of the section. In particular O2 is a real
exhibited circularity, not a conjecture: converting `r^{-2}∫|w||q−c|^2` into a lower power
of `∫|∇V|^2` needs Sobolev–Poincaré for `q`, i.e. `q ∈ W^{1,s}_loc`, i.e. (H1). ✓

### E8. Refutations attempted and failed

- **Against Theorem 2.** I looked for a `C^1` solenoidal `A` with a nondegenerate zero and
  bounded `curl(|A|^{-1/2}A)`. The repaired case analysis (below) shows there is none.
  Numerically (`aud4.py`), for the symmetric traceless `L = diag(1,1,−2)` (so `sk(L) = 0`,
  the most favourable case for the note's `M`), `|curl w|·r^{1/2}` is constant to four
  figures — `0.5946` along `θ = (1,1,1)/√3`, `0.5407` along `(1,2,0.5)`-direction, at
  `r = 10^{-2}, 10^{-4}, 10^{-6}` — and is exactly `0` along the eigendirection
  `θ = e_1`. This confirms both that the blow-up is real and that the theorem is correctly
  scoped to an **open cone** rather than to all directions: a "for all `θ`" version would
  be false.
- **Against the repaired rank analysis.** `aud3.py`: for `400` random normalized traceless
  `L` of each rank, `max_{n ∈ S^2 ∩ Range(L)}|M(n)|` never approached `0`; minima
  `0.7071` (rank 1, matching the exact value `|a⊗b − b⊗a|_F/2 = 1/√2` derived below),
  `0.576` (rank 2), `0.5367` (rank 3). For the HF18-B oscillation model
  `L = [[0,−3,0],[1,0,0],[0,0,0]]`, `min_{n∈Range L}|M(n)| = 3.5355`, `max = 4.9497` —
  bounded away from `0` on the *whole* realized circle, so that application is comfortable.
- **Against Corollary 2.1 vs HF18-B Prop. 2.2.** Attempted to derive a contradiction from
  "the family satisfies (H1)" (HF18-B) and "the family is inadmissible" (HF21). None
  exists: `(H1)` is `W^{1,1}_loc`, inadmissibility is `∇u ∉ L^∞_loc`, and `d^{-1/2}` on a
  codimension-two set is in `L^1_loc` but not `L^∞_loc`.
- **Against Theorem 3.** Looked for circularity (none: the object is `Δφ`, defined from
  `q ∈ L^3` alone) and for an endpoint abuse (none: `1 < p < ∞` is stated and the
  endpoints are correctly quarantined in (d)).
- **Against Proposition 4.4.** Looked for a failure of minimality (none: (B1) applies
  because `A ∈ C_c^1`, `div A = 0`, `A ∈ L^{3/2}`), for a smoothness failure of `ψ`
  (`ψ ∈ C^2` exactly, `C^3` fails, which is all that is used), and for a hidden conflict
  with Theorem 1(b) (none: `{w = 0} ∩ B` is Lebesgue-null).
- **Against Theorem 5.** Tested on rigid rotation; inequality holds with slack `≈ 9.4`.
  Looked for a boundary term at infinity or an unjustified limit; the proof is on a fixed
  compact cylinder throughout.
- **Against the §7 scale budget.** Recomputed the family `m_j = 2^{-j}`, `δ_j = 2^{-2j}`,
  `k_j = 2^{3j}`: `Σδ_j^3k_j^2m_j = Σ2^{-j} < ∞`, `Σδ_jk_jm_j = Σ1 = ∞`,
  `Σδ_j^3m_j < ∞`, `δ_jk_j = 2^j → ∞`. Exactly as claimed, including the fact that
  constraint 2 (not the dissipation budget) is what vetoes it.
- **Against check C5 (scaling).** Verified (5.1) is scale-covariant under
  `S_λ: u ↦ λu(λ·)`: `w ↦ λw(λ·)`, `ω ↦ λ^2ω(λ·)`, and the radius carries as `r ↦ r/λ`;
  the scaled inequality at radius `r` is the original at radius `λr` multiplied by `λ`.
  No radius-free constant is claimed anywhere. ✓

---

## REPLACEMENT ARGUMENT

### R1 (repairs the first bad bridge). Rank-stratified non-vanishing of `M`

**Lemma R1.** Let `L ∈ R^{3×3}`, `L ≠ 0`, `tr L = 0`, and let

```
M(n) := −2 sk(L) + ½ ( n⊗L^Tn − L^Tn⊗n ),      n ∈ S^2 .
```

Then `M(n) ≠ 0` for at least one `n ∈ S^2 ∩ Range(L)`.

*Proof.* By rank.

**rank `L` = 3.** `Range(L) = R^3`. Suppose `M(n) = 0` for all `n` in some nonempty open
`U ⊆ S^2` (which is what `Range(L) = R^3` makes available: `θ ↦ \widehat{Lθ}` is an open
map). Applying `M(n)` to `n` gives (2.4), `2Ln − L^Tn = (n·Ln)n` on `U`. Homogenize:
`H(x) := 2Lx − L^Tx − (x·Lx)x/|x|^2` is real-analytic on the connected set `R^3\{0}` and
vanishes on the nonempty open cone over `U`, hence everywhere. Thus `B := 2L − L^T` has
every `x ≠ 0` as an eigenvector, so `B = μI`. Transposing, `2L^T − L = μI`; subtracting,
`3(L − L^T) = 0`, so `L = L^T`; then `2L − L = L = μI` and `tr L = 0` gives `μ = 0`,
`L = 0` — contradiction. So `M` does not vanish on any open subset of `S^2`, and in
particular not on all of `S^2 ∩ Range(L)`.

**rank `L` = 1.** Write `L = a⊗b`, i.e. `Lx = a(b·x)`, `a,b ≠ 0`; `tr L = a·b = 0`.
`Range(L) = span(a)`, so `n = ±\hat a` and, `M` being quadratic in `n`, it is enough to
evaluate at `n = \hat a`. Then `L^T\hat a = b(a·\hat a) = |a| b`, and
`sk(L) = ½(a⊗b − b⊗a)`, so

```
M(\hat a) = −(a⊗b − b⊗a) + ½( |a| \hat a⊗b − |a| b⊗\hat a )
          = −(a⊗b − b⊗a) + ½( a⊗b − b⊗a ) = −½ ( a⊗b − b⊗a ).
```

This vanishes iff `a ∥ b`, which with `a·b = 0` and `a ≠ 0` forces `b = 0`, i.e. `L = 0`.
Hence `M(\hat a) ≠ 0`, with the exact value `|M(\hat a)|_F = |a||b|/√2` (`= 1/√2` for
`|L|_F = 1`, matching the numerical minimum `0.7071` reported above).

**rank `L` = 2.** Let `R := Range(L)` and pick an orthonormal basis `f_1, f_2` of `R`;
extend by `f_3 ⊥ R`. In these coordinates `L f_3`-row structure is: `Lx ∈ R` for all `x`,
so the third row of `L` vanishes,

```
L = [[α, β, γ], [δ, ε, ζ], [0, 0, 0]],      tr L = α + ε = 0 .
```

Suppose `M(n) = 0` for every unit `n ∈ R`; write `n = (cos t, sin t, 0)`. `M(n) = 0` says

```
n⊗L^Tn − L^Tn⊗n = 4 sk(L)                                                (R1.1)
```

for all `t`. The left side is skew; identify a skew matrix `X` with the vector `x` such
that `X = x^∧`. With `L^Tn = (αn_1+δn_2, βn_1+εn_2, γn_1+ζn_2)`, the components of the
left side of (R1.1) are

```
(1,3)- and (2,3)-entries:  γ n_1n_2 + ζ n_2^2   and   −γ n_1^2 − ζ n_1n_2 ,
(1,2)-entry:               β n_1^2 + (ε−α) n_1n_2 − δ n_2^2 .
```

Constancy in `t` of the first two forces, via `n_1n_2 = ½sin2t`, `n_2^2 = ½(1−cos2t)`,
`n_1^2 = ½(1+cos2t)`,

```
γ = 0,   ζ = 0 ;
```

constancy of the third forces `β + δ = 0` and `ε − α = 0`, which with `α + ε = 0` gives
`α = ε = 0`. Hence `L = β(e_1⊗e_2 − e_2⊗e_1)` is skew. But then a direct evaluation gives
`n⊗L^Tn − L^Tn⊗n = L` for every unit `n ∈ R` (with `L^Tn = −Ln`, the `(1,2)`-entry is
`n_1(L^Tn)_2 − (L^Tn)_1n_2 = β(cos^2t + sin^2t) = β`), while the right side of (R1.1) is
`4 sk(L) = 4L`. So `3L = 0`, i.e. `L = 0` — contradiction. ∎

*(Only an open arc of `t` is actually available in the application; the entries above are
trigonometric polynomials in `t`, so constancy on an arc is constancy everywhere and the
argument is unchanged.)*

**Corrected proof of Theorem 2.** Replace the paragraph beginning "Suppose `M(n) = 0` …"
and the following paragraph by:

> Let `Γ_1` be an open cone of directions `θ` with `|Lθ| ≥ κ > 0`, so that
> `A(x) = rLθ + o(r)` and `|A| ≥ κr/2` for small `r`, and `w` is `C^1` there. Since
> `A ∈ C^1`, `∇A(x) = L^T + o(1)` and `n(x) = \widehat{Lθ} + o(1)`, uniformly on `Γ_1`,
> so
> ```
> 2 sk(∇w)(x) = |A(x)|^{-1/2} M(n(x)) + o(r^{-1/2}) .
> ```
> By Lemma R1 there is `n_* ∈ S^2 ∩ Range(L)` with `M(n_*) ≠ 0`; choose `θ_*` with
> `\widehat{Lθ_*} = n_*` (possible because `n_* ∈ Range(L)`) and shrink `Γ_1` to an open
> cone `Γ ∋ θ_*` on which `|M(\widehat{Lθ})| ≥ c_1 := ½|M(n_*)| > 0`, by continuity of
> `θ ↦ M(\widehat{Lθ})` on `{Lθ ≠ 0}`. With `|A| ≤ Cr`,
> ```
> |sk(∇w)(x)| ≥ ½ (Cr)^{-1/2} c_1 − o(r^{-1/2}) ≥ c_0 r^{-1/2}
> ```
> for `r < r_0`, which is (2.2).

Two changes are essential: the quantifier now runs over `S^2 ∩ Range(L)` rather than over
an open subset of `S^2`, and the error rate is `o(r^{-1/2})` rather than `O(r^{1/2})`.
With them, **Theorem 2, Corollary 2.1, Corollary 2.2 and §7 constraint 3 stand exactly as
stated in the note.**

### R2 (repairs D2). Corrected Theorem 6'

Replace (6.1) by

```
∫ ζ^2|∇V|^2 ≤ (81/2) ∫ ζ^2 |w| |∇u|^2  +  162 ‖∇ζ‖_∞^2 ∫_{supp ∇ζ} |w| |q − c|^2 .   (6.1')
```

*Proof.* Unchanged up to the Cauchy–Schwarz step, with
`Y_2 := (∫_{supp∇ζ}(|τ_hw|+|w|)|D_hφ − c_k|^2)^{1/2}`; the single factor `ζ` in the
boundary integrand is allocated to `|D_hV|` to form `X`, and `|∇ζ| ≤ ‖∇ζ‖_∞1_{supp∇ζ}`
is used on the other factor. All constants are unchanged. ∎

`(6.1')` is what the §6.2 discussion needs (an annulus term is the right shape for a
reverse-Hölder attempt), so O1–O4 are untouched. The `ζ ↑ 1`, `c = 0` consistency check is
also unchanged, since `supp∇ζ` may then be taken with `‖∇ζ‖_∞ → 0`.

### R3 (repairs D3, D4). Corrected Theorem 6 and the "pincer" language

Replace Theorem 6's third bullet by:

> - if in addition `|∇w| ≲ d(x,Z)^{β−1}` near `x_0` (a hypothesis on the model, **not** a
>   consequence of `|w| ≍ d^β`) and `Z` is a `C^1` submanifold of codimension `1` or `2`,
>   then `d^{β−1} ∈ L^1_loc` for every `β > 0` (codimension 1: `∫_0 t^{β−1}dt < ∞`;
>   codimension 2: `∫_0 t^{β−1}·t dt < ∞`), so (H1) holds locally.

and replace the sentence after it by:

> So within the model class in which the gradient scales with the amplitude, power-law
> vanishing on a `C^1` zero set of codimension `1` or `2` is compatible with (H1). What is
> proved about the exponent itself is only `β ≤ 1` (Corollary 5.1) and, in the `C^1` model
> with `DA(x_0) ≠ 0`, the exclusion of `β = 1/2` (Theorem 2); the interval
> `β ∈ (1/2, 1]` is not narrowed.

Correspondingly: in the Summary bullet 4, delete "the order of vanishing of `|w|` is
forced to be exactly `1`, and there (H1) is automatic" and write "the order of vanishing
of `|w|` is confined to `(1/2, 1]`"; in §2.2 "Reading of Theorem 2", replace "the order at
a nondegenerate model zero is pinned to `1`" by "the order at a `C^1` model zero is
confined to `(1/2, 1]`"; in §5, replace "the admissible exponent is pinned near `β = 1`"
by "the admissible exponent is confined to `(1/2, 1]`".

### R4 (cosmetic, for the record)

- §3 proof: `Cr^{-2}` in the harmonic interior estimate should be `Cr^{-4}`; and only
  `‖∇ψ‖_{L^1(B_r)}` is needed, not `‖∇ψ‖_{L^3(B_r)}`. No statement changes.
- §4 Prop. 4.4(ii): with the note's own convention `(∇w)_{ij} = ∂_iw_j`, `∇w = e_1⊗e_2`,
  not `e_2⊗e_1`.
- §7 constraint 5: the implication "requires `∫_E|w|^{-1} = ∞`" is Theorem 4(**a**), not
  4(b).
- Theorem 4's title "(layered criterion; sharp)" should read "(layered criterion)", with
  the sharpness confined to part (b) and its stated abstract meaning.

---

## CONDITIONAL SUFFIX THAT SURVIVES

Everything below is at one fixed time of a classical solution, `u ∈ H^m(R^3;R^3)`,
`m ≥ 4`, `div u = 0`, unforced whole space, no smallness, unless narrower. All of it is
unconditional (not conditional on (H1)) except where marked.

1. **Theorem 1, in full.** `curl w = curl u = ω ∈ H^{m-1} ⊂ C^{1,1/2} ∩ L^∞` in `D'`;
   (H1) is equivalent to `sym(∇w) ∈ L^1_loc`; if `|{w = 0} ∩ {ω ≠ 0}| > 0` then (H1) is
   **false**; (H1) holds on every open `E` with `ess inf_E|w| > 0`, with
   `∫_E|∇w| ≤ (ess inf_E|w|)^{-1/2}|E|^{1/2}‖∇V‖_{L^2(E)}`.
2. **Theorem 2, with the proof replaced by R1.** If `A` is `C^1` near `x_0`, `div A = 0`,
   `A(x_0) = 0`, `DA(x_0) ≠ 0`, and `w = |A|^{-1/2}A`, then `|sk(∇w)| ≥ c_0d^{-1/2}` on an
   open cone at `x_0`; hence for `A ∈ L^{3/2}(R^3)` solenoidal, `u = Pw ∉ H^s_loc` for
   `s > 5/2`, and `w` is the minimizer of no datum satisfying (0.1).
   **Corollary 2.1** (independently verified by closed-form computation and by my own
   finite differences on and off the ray): no member of the HF18-B witness family, bulk or
   oscillation, is the minimizer of an admissible datum. **Corollary 2.2**: a
   counterexample built as `w = |A|^{-1/2}A` with `A ∈ C^1 ∩ L^{3/2}` solenoidal must have
   every zero of `A` degenerate.
3. **Theorem 3, in full,** including (a)–(d) and the global Riesz-transform statement:
   for `1 < p < ∞`, `w ∈ W^{1,p}_loc ⟺ div w ∈ L^p_loc` (distributional `div w = Δφ`);
   (H1) follows from `div w ∈ L^p_loc` for a single `p > 1`; `T ∈ L^{3/2}(R^3)` gives
   `Hess φ ∈ L^{3/2}(R^3)`. **Corollary 3.3**: (H1) ∧ (H2) `⟺ div w ∈ L^{3/2}(R^3)`, with
   `σ = −div w`. No circularity: `Δφ` is defined from `q ∈ L^3` alone.
4. **Proposition 4.1 and Theorem 4 (a), (b), (c), in full**, with "sharp" read in the
   abstract sense of E5. `∫_E|w|^{-1/2}|∇V| < ∞ ⟹ w ∈ W^{1,1}(E)`; the layered sum (4.2)
   suffices; `|w|^{-1} ∈ L^1(E)` suffices; `∇V ∈ L^p(E)` and `|w|^{-p'/2} ∈ L^1(E)`
   suffice for `p ∈ [2,∞]`. Higher integrability of `∇V` never removes the negative moment.
5. **Proposition 4.4, in full**, with its stated scope (`u` smooth on `B`, not globally
   `H^m`): a genuine element of `M`, minimal against **all** of `G_3` by audited HF18-B
   Prop. 1.4, with `∫_B|w|^{-1} = ∞`, `w ∈ C^∞(B)`, `u ∈ C^∞(B)`, `curl u = e_3 ≠ 0`.
   Hence `|w|^{-1} ∈ L^1_loc` is **not necessary** for (H1).
6. **Theorem 5 and Corollaries 5.1, 5.2, in full**: for `w ∈ L^3` with continuous
   `curl w = ω`, `⨍_{B_r(x_0)}|w| ≥ (r/32)max_{|n|=1}inf_{B_r}(ω·n)` and
   `limsup_{r↓0}r^{-1}⨍_{B_r}|w| ≥ |ω(x_0)|/32`; `|w| = O(|x−x_0|^α)` with `α > 1` forces
   `ω(x_0) = 0`; `w = 0` a.e. on an open `U` forces `ω = 0` on `U`. The quantified
   shortfall (`|{|w| ≥ λ} ∩ B_1| ≥ Cλ^3` only) is correct.
7. **Theorem 6, only in the form R3** (with the gradient hypothesis added); the exponent
   is confined to `(1/2, 1]` and is not pinned.
8. **Theorem 6' in the form (6.1')**, constants `81/2` and `162` confirmed, together with
   O1–O4: no Caccioppoli with `V − V_B` on the right is derivable from this
   Euler–Lagrange condition; converting the boundary term needs Sobolev–Poincaré for `q`,
   i.e. needs (H1); and even a successful Gehring would not suffice.
9. **§1.1, in full, confirmed against the primary source.** Our `w` is Stern's `β_∞`
   (Lemma 2.2, arXiv:2403.19481v2); that paper states no regularity for `β_∞`; and the
   Uhlenbeck-credited smoothness in its §3 attaches to `H_p^k = {h ∈ Z_p^k : d*(|h|^{p-2}h)=0}`,
   i.e. to forms that are additionally **closed**, which `w` is not.

**New conditional suffixes contributed by the lane, both strictly inside the (H1)
question, both surviving:** if `div w ∈ L^p_loc` for one `p > 1` then (H1), hence audited
HF18-A Proposition 3'; and if the layered sum (4.2) is finite on every bounded set then
(H1).

**The HF18 conditional suffix is unchanged**, neither extended nor reduced. In particular
the first gap — an input-only spacetime bound
`∫_0^τ K dt ≤ θν∫_0^τ D_3(w)dt + M∫_0^τ Q dt + A_input`, uniformly for `τ < min(H,T_*)`,
`θ ≤ 1` — is untouched by every result above, and (H1) granted in full would not close it.
Check C7's answer is accurate and I confirm it: the note contains no time integral, no
absorption, no evolution equation, and no statement about `K`.

---

## UNNECESSARY DEPENDENCIES

- **(A4)** (`D_Q(u) = D_3(w) ≥ c‖u‖_9^3`) is imported in §0 and used nowhere.
- **(A1)**'s quantitative bounds enter only the Theorem 6' consistency check, not any
  proof.
- **Theorem 6'** is not used by any other statement in the note; §6.2 immediately shows it
  does not iterate. It is a self-contained deliverable, not a dependency.
- **Theorem 6** is likewise terminal (and, per R3, needs a hypothesis it does not have).
- **§1.3** (Sibner–Sibner, Iwaniec–Scott–Stroffolini, Otway, Giaquinta, Lindqvist) is
  entirely non-load-bearing, as the note itself says.
- **Theorem 3(d)** (Stein's `L log L` endpoint, CZ weak type) is quoted and unused.
- The note's own numerics (`chk.py`) are not needed: Theorem 2 is proved symbolically
  (once repaired by R1) and Corollary 2.1 in closed form. I did not read `chk.py`; my own
  computations reproduce and extend both checks.
- Conversely, nothing load-bearing is missing: (P1)–(P3), (A5), (A6), (B1), (B2) are all
  genuinely used, and all six were checked against their audited sources.

---

## NON-CLAIMS (of this audit)

- I do **not** certify (H1), nor its negation, nor its independence.
- I do **not** certify that the HF18-B classification of weighted inequalities is
  unchanged when restricted to the admissible class; that question is untouched by this
  audit as by the note.
- I do **not** certify Uhlenbeck 1977's hypotheses from the primary source; I read only
  the arXiv statement of Stern §3 that credits it. The note's inapplicability argument
  does not need Uhlenbeck's text, since it is a statement about *our* operator, which is
  audited in HF18-A.
- I do **not** certify that Stern contains no regularity statement for `β_∞` anywhere in
  the paper by exhaustive reading; I confirmed it for §§2–3 and by targeted query, and the
  note's claim is negative and non-load-bearing in the sense that nothing here uses a
  regularity theorem.
- Confirming Corollary 2.1 is **not** a re-audit of HF18-B Prop. 2.2. I checked only that
  the two are logically compatible; they are.
- Theorem 5's constant `32` is not claimed sharp, by the note or by me.
- No statement in the note or this audit bears on the first gap, on `K`, on HIGH-STRAIN,
  on HIGH-PRESSURE, or on continuation.

---

## REOPENING CONDITION

This audit's REPAIR verdict must be reopened if any of the following occurs.

1. **Lemma R1 is contradicted**: a nonzero traceless `L ∈ R^{3×3}` is exhibited with
   `M(n) = 0` for every unit `n ∈ Range(L)`. Then Theorem 2 fails for the corresponding
   model zero, Corollary 2.2 and §7 constraint 3 collapse, and the "linear-zero mechanism
   is vetoed" headline must be withdrawn. (Corollary 2.1 would still survive, being a
   direct computation.)
2. **The `C^1` hypothesis in Theorem 2 is weakened** in any downstream use — to `A`
   merely differentiable at `x_0`, or to `DA` merely approximately continuous. The
   repaired error term `o(r^{-1/2})` uses continuity of `∇A` in a full neighbourhood, and
   nothing weaker was checked.
3. **Theorem 6' is used as an input to a higher-integrability or reverse-Hölder claim.**
   Only `(6.1')` is proved; any argument that needs the `ζ^2` weight on the boundary term,
   or that needs the term localized more tightly than `supp ∇ζ`, is not covered.
4. **Theorem 6 is cited for the unrestricted model class**, i.e. without the added
   gradient hypothesis of R3, or the exponent is again described as "pinned" to `1`.
5. **Corollary 3.3 is read as a statement about `M` rather than about admissible data.**
   It rests on (B2)/HF18-B Lemma A, whose standing hypothesis is `V ∈ H^1`, i.e. the
   admissible setting; on the raw class `M` the equivalence was not checked.
6. **Proposition 4.4 is upgraded to a globally admissible example** without proving that
   the cutoff region of `A` can be made to have only degenerate zeros. As written the
   example is local, and Theorem 2 predicts that the naive global completion fails.
7. **HF18-B Prop. 2.2 is re-audited and changes**, in particular if its family is ever
   claimed to have smooth data; then the compatibility argument in E3 must be redone.

---

## EXACT EDITS FOR THE CONTROLLER, IF THIS VERDICT STANDS

**A. To `research/evidence/hf21-shifted-hodge-regularity.md`** (the note's own repair pass;
this audit does not perform them):

- A1. Insert **Lemma R1** (statement and proof, as displayed above) immediately before the
  proof of Theorem 2, and replace the two paragraphs of that proof beginning
  "Suppose `M(n) = 0` for all `n` in some open subset `U`" and
  "Hence `M` does not vanish identically" by the corrected proof text of **R1** above.
  Change the error term in (2.3) and in the final display from `O(1)` / `O(r^{1/2})` to
  `o(r^{-1/2})`, and state explicitly that `A ∈ C^1` gives `∇A(x) = L^T + o(1)`.
- A2. Replace (6.1) by **(6.1')** and redefine `Y_2` with `∫_{supp∇ζ}` in place of
  `∫ζ^2`; keep both constants.
- A3. Apply **R3**: add the gradient hypothesis to Theorem 6's third bullet, replace the
  "settled affirmatively" sentence, and remove "pinned to `1`" / "pinned near `β = 1`"
  from the Summary bullet 4, §2.2 and §5.
- A4. Apply **R4** (four cosmetic corrections).
- A5. In §10 EVIDENCE, replace the sentence "the homogenized identity ... and its
  real-analytic continuation from an open cone" by a description that names the
  rank-stratified Lemma R1, since the analytic-continuation step covers only
  `rank L = 3`.

**B. To `../navier-paper/main.tex`** — one edit only, and it is a citation
correction, not a new result:

- B1. In `rem:quotient-related` (line ≈4856), after the Sibner–Sibner / Scott /
  Iwaniec–Scott–Stroffolini sentence, add a sentence recording that the minimizing
  representative of `def:quotient` is, in the language of `L^p` cohomology, the canonical
  `p`-coclosed primitive of Stern, *`L_p`-cohomology and the geometry of `p`-harmonic
  forms*, arXiv:2403.19481, Lemma 2.2 (with `n = 3`, `p = 3`, `k = 2`); that the
  regularity statement in that paper's §3, credited to Uhlenbeck, is for the class
  `H_p^k = {h ∈ Z_p^k : d^*(|h|^{p-2}h) = 0}` of forms that are additionally **closed**,
  which the datum here is not; and that no regularity for the primitive is stated there.
  Add the bibliography entry `Stern2024`. This is directly inspected and confirmed by this
  audit and by HF18-B's scope note; it sharpens an existing remark and introduces no new
  claim.
- B2. **No other manuscript edit.** Nothing in HF21-A is ready for `sec:quotient`:
  Theorems 1–6' are all inside the (H1) question, which the manuscript treats as a
  hypothesis, and none of them changes `prop:localtheory`, `lem:upgrade`,
  `prop:pressure`, `prop:energy`, `prop:lowpressure`, `hyp:highpressure`,
  `hyp:absorption`, `hyp:highstrain`, `prop:quotient-conditional` or `rem:no-monotone`.

**C. To `docs/proof-graph.yaml`**:

- C1. Do **not** add a node. Extend the `review:` field of the node whose
  `evidence: research/evidence/hf18-hodge-regularity.md` (line ≈225–226) with one
  sentence: that HF21-A, audited REPAIR
  (`research/evidence/hf21-review-shifted-hodge-regularity.md`), reduces (H1) to the
  scalar statement `div w ∈ L^p_loc` for one `p > 1`, shows the standard obstacle
  `|w|^{-1} ∈ L^1_loc` is sufficient but not necessary, and vetoes the linear-zero
  construction mechanism; and that by its own scope ceiling it leaves the spacetime
  hypothesis and the first gap untouched.

**D. To `PLAN.md`**:

- D1. In "HF21: shifted-Hodge regularity and the crossing sign structure", change the
  heading's `(UNAUDITED)` for this lane to record the audit: HF21-A audited **REPAIR**,
  review at `research/evidence/hf21-review-shifted-hodge-regularity.md`, with the repair
  of Theorem 2 (rank-stratified Lemma R1), the correction of Theorem 6' to (6.1'), the
  added hypothesis in Theorem 6, and the withdrawal of the "order pinned to 1" language.
  The lane's other reported results are confirmed. `hf21-crossing-sign-structure.md`
  remains unaudited.
- D2. In "Ordered next actions" item 4, add to the list of results the two new
  conditional suffixes (`div w ∈ L^p_loc`, `p > 1`, implies (H1); the layered sum (4.2)
  implies (H1)) and the new veto (the linear-zero construction mechanism is closed for
  admissible data), and record the lane's own next action: decide whether a compactly
  supported solenoidal `A ∈ L^{3/2}` can have only degenerate zeros, and whether
  `∫|w|σ^2 ≤ D_3/2` restricted to the admissible class upgrades to `div w ∈ L^p_loc`.
- D3. Leave the first-gap statement in `PLAN.md` **unchanged**. Nothing in this lane
  touches it, and the note says so correctly.

**E. Not to be done**: no promotion of any HF21-A statement to a manuscript lemma; no
removal of `hyp:highstrain` or `hyp:absorption`; no weakening of HF18-B Prop. 2.2, whose
conclusions on `M` are untouched.
