# CP02-3 AUDIT (round 2): review of `research/evidence/cp02-pressure.md`

MODE: REVIEW, proof-audit discipline. Date: 2026-09-05. This lane owns only this
file; nothing else was edited, nothing pushed.

## 0. Freeze

| item | value |
|---|---|
| candidate file | `../navier/research/evidence/cp02-pressure.md` |
| `sha256sum` | `0b9fbb4aaf52f4ba7b0b41aca2e8fe96becc09a89ee76b1f4c7b8391ac8a4953` |
| `git -C ../navier rev-parse HEAD` | `f20e6bf579f74c3fef4e365fa5267929667f1228` |
| candidate length | 1012 lines |
| round-1 audit compared | `research/evidence/cp02-review-pressure.md` (712 lines, verdict REPAIR) |
| manuscript read in full | `../navier-paper/main.tex` (562 lines), `references.bib` (5 keys) |
| CP01 records read in full | `cp01-manuscript-obligations.md` (624 lines), `cp01-literature-statements.md` (806 lines) |
| sibling lane read for interface | `research/evidence/cp02-energy-enstrophy.md` |
| Lean development re-opened | `../navier-formal/NavierFormal/Regularization.lean` |
| primary source re-opened **in this lane** | Tao, *Analysis & PDE* **6** (2013) 25–107, publisher PDF `https://msp.org/apde/2013/6-1/apde-v6-n1-p02-s.pdf`, printed pp. 28, 35, 36, 37, 38 read as text (`helpy_pdf`, `mode:"text"`) |

## 1. VERDICT

**REPAIR** — one sentence, and it is the only mathematical defect found.

Round 1's two source-layer defects are fully repaired: all four Tao page
locations were re-verified independently in this lane against the publisher PDF
and are now **correct and verbatim-accurate** (pp. 28, 35, 36, 38), and every
external fact in the LaTeX block now carries a `\cite`. The chapter/section
locations of the three new `[MO]` textbook keys were also checked at
table-of-contents level and are apt (see §4). Every identity, sign, constant and
exponent of the candidate was rederived independently here and reproduced,
including an independent check of the whole balance on an explicit exact
solution (§2.2, item 1).

The single defect is in the proof of Lemma `lem:pressure-convention`(a), and it
was **introduced by round 2's narrowing of the regularity package**: the
sentence asserting that `\widehat{∂_i∂_j(u_iu_j)}` "is an `L^2` function" is
false as a general statement and is not derivable from the declared (R2)–(R3).
It is load-bearing only for the weaker fact "is a measurable, locally integrable
function", which is all Tao's (14) asks for. A complete one-paragraph
replacement is in §5. No downstream statement changes.

## 2. REVIEWED SCOPE

Reconstructed from the first nontrivial implication onward, without relying on
round 1's verification:

1. Conventions: the cutoff construction (`g`, `η`, `χ`, `χ_R` and all four of its
   claimed properties); the Fourier/Plancherel/multiplier/Riesz/`Δ^{-1}` symbol
   chain; the `(∇u)^T u` and `(u⊗u):∇u` identities.
2. The narrowed regularity declaration (R2)–(R3) against D2, and the finiteness
   of the section constants `K_2,K_3,K_4,K_∞,G,Π_2,Π_∞`.
3. `lem:pressure-convention`(a)(b)(c): the symbol computation
   `R_iR_j ↔ −ξ_iξ_j/|ξ|^2`, `∂_i∂_j ↔ −4π^2ξ_iξ_j`, `−Δ ↔ 4π^2|ξ|^2`,
   `Δ^{-1} ↔ −(4π^2|ξ|^2)^{-1}`; well-definedness in Tao's sense; the
   identification with `prop:localtheory`'s normalised pressure through the
   continuous representative; `−Δp = ∂_i∂_j(u_iu_j)`.
4. `lem:integrands`(i)–(iv) and `def:D3P3`, including agreement with the
   manuscript's `D_3`, `P_3` off `{u=0}` and with recommendation P-0.
5. `lem:reg-calculus`(i)–(iv), `lem:divergence`, `lem:diff-under-integral`.
6. `prop:pressure`(i)–(iv), Steps 1–7: measurability and boundedness of `D_3`,
   `P_3`; the three integrations by parts with algebra and signs; the three
   cutoff errors and `C_E`; `eq:cutoff-identity`; the `R→∞` and `ε↓0` limits with
   their majorants; continuity of `X`; the `ρ_ε` proof of `∫W(u,∇u)dx = 0`.
7. `cor:absorption-consequence`(i)–(ii) against `eq:absorption` (`main.tex`
   l. 306–318) and `eq:missing` (l. 393–402), including the `τ=0` separation and
   the `M` formula of l. 405–408.
8. `rem:old-form`, `rem:lean-majorant`, `rem:differential-form`.
9. Every `\cite` in the block against the primary text (five `Tao2013` page
   locations verified as page images/text in this lane; the three textbook keys
   checked at TOC level).
10. Interfaces: `prop:localtheory` (D2), `eq:NS`, `hyp:absorption`,
    `hyp:critical`, `eq:pressure-consequence`, the labels of `main.tex`
    l. 256–262 (`L_J`, `Q_J`), and the sibling lane's
    `lem:div-zero`/`χ_R`/Conventions/`\newtheorem` declarations.
11. Compliance with D1 (conventions), D2 (only R, no preserved Schwartz decay),
    D4 (integrated form, `(∇u)^T u`, retained labels), D5 (sourcing).

### 2.1 Independently confirmed (recorded so no later lane repeats it)

*Signs and factor structure, from scratch.* `d/dt ∫|u|^3/3 = ∫|u|u·u_t`;
`ν∫|u|u·Δu = −ν∫(|u||∇u|^2 + |(∇u)^Tu|^2/|u|)`;
`−∫|u|u·(u·∇)u = −∫u_j∂_j(|u|^3/3) = 0`;
`−∫|u|u·∇p = ∫p\,\mathrm{div}(|u|u) = ∫p\,u·∇|u|`. Hence
`X'/3 = −νD_3 + P_3`, i.e. the candidate's `eq:pressure-balance` with the
candidate's `D_3` (including the factor `2` implicit in `D_3 ≤ 2∫|u||∇u|^2`) and
`P_3`. Confirmed, and confirmed again on an exact solution in §2.2.

*Chain rule / substitution.* `∇_aH_ε = r_ε a`, `∇_a r_ε = a/r_ε`,
`∂_j r_ε(u) = ((∇u)^Tu)_j/r_ε`, `∂_j(H_ε(u)) = r_ε u_i∂_ju_i`,
`u_i∂_ju_i = ((∇u)^Tu)_j`. Confirmed.

*Diffusion.* `f = χ_Rr_εu_i`, `g = ∂_ju_i` gives
`ν∫χ_Rr_εu_i∂_j∂_ju_i = −ν∫χ_Rr_ε|∇u|^2 − ν∫χ_R|(∇u)^Tu|^2/r_ε − ν∫r_ε∇χ_R·(∇u)^Tu`,
i.e. `−νD_{ε,R} + E^d_{ε,R}` exactly as printed, sign included.

*Convection.* `−∫χ_Rr_εu·(u·∇)u = ∫∂_j(χ_Ru_j)H_ε(u) = ∫H_ε(u)u·∇χ_R` by
`div u = 0`: the convection term contributes only a cutoff error. Confirmed.

*Pressure.* `−∫χ_Rr_εu·∇p = ∫p\,\mathrm{div}(χ_Rr_εu) = P_{ε,R} + E^p_{ε,R}`
with `div(r_εu) = u·(∇u)^Tu/r_ε`. Confirmed.

*Exponents, recomputed.* `∫(|u|^2+|u|)|∇u| ≤ (‖u‖_4^2+‖u‖_2)‖∇u‖_2`
(Cauchy–Schwarz, `‖|u|^2‖_2 = ‖u‖_4^2`); `∫2(|u|^2+|u|^3)|u| = 2(‖u‖_3^3+‖u‖_4^4)`;
`∫|p|(|u|^2+|u|) ≤ ‖p‖_2(‖u‖_4^2+‖u‖_2)`. All three and
`C_E = ‖∇χ‖_∞(2(K_3^3+K_4^4) + ν(K_4^2+K_2)G + Π_2(K_4^2+K_2))` are correct as
printed, and uniform in `ε ∈ (0,1]` because `r_ε ≤ |u|+1` there.

*Majorants.* `r^3−s^3 = (r−s)(r^2+rs+s^2) ≤ 3r^2·(r^2−s^2)/(r+s) ≤ 3r|a|^2`
(valid because `s = √ε ≤ r`), so `H_ε ≤ r_ε|a|^2 ≤ |a|^2(|a|+1) ≤ 2(|a|^2+|a|^3)`
for `ε ≤ 1` — `eq:HEps-majorant`, confirmed, sharp up to the factor `2`.
`0 ≤ g_n ≤ (2|u|+1)|∇u|^2` and `|h_n| ≤ |p||u||∇u|`, with space–time integrals
`(t−s)(2K_∞+1)G^2` and `(t−s)Π_∞K_2G`. Confirmed.

*Zero-set device.* `ρ_ε = r_ε(u)−√ε = |u|^2/(r_ε+√ε) ≤ |u|`, `∇ρ_ε = ∇r_ε`,
`div(ρ_εu) = u·(∇u)^Tu/r_ε`, so
`|∫χ_R u·(∇u)^Tu/r_ε| = |∫ρ_ε u·∇χ_R| ≤ R^{-1}‖∇χ‖_∞‖u(t)‖_2^2 → 0`. Confirmed;
its necessity is proved in §2.2 item 2.

*Cutoff.* `g(s)=e^{-1/s}` extended by `0` is `C^∞`; the denominator
`g(2−r)+g(r−1)` is positive for every real `r` (one of `2−r`, `r−1` is positive);
`η = 1` on `(−∞,1]`, `η = 0` on `[2,∞)`; `χ(x) = η(|x|) ∈ C_c^∞` because `η` is
constant near `0`; `∇χ_R` supported in `{R ≤ |x| ≤ 2R}` with
`‖∇χ_R‖_∞ = R^{-1}‖∇χ‖_∞`. All confirmed.

*Corollary.* From `eq:pressure-balance` (`s=0`, `t=τ`) and `eq:absorption`:
`X(τ) + 3(1−θ)ν∫_0^τD_3 ≤ ‖u_0‖_3^3 + 3A`, both left terms nonnegative, so
`eq:pressure-consequence` and `(1−θ)ν∫_0^τD_3 ≤ (‖u_0‖_3^3+3A)/3` follow; `τ=0`
is separated correctly because `eq:absorption` quantifies `0<τ<min{H,T_*}` only;
cube roots give `hyp:critical` with `M = (‖u_0‖_3^3+3A)^{1/3}`, matching
`main.tex` l. 405–408 verbatim. With `θ = 1` the critical bound still follows, as
the trailing paragraph claims. Confirmed.

*Uses of R, audited line by line.* The block consumes exactly: (R2) pointwise
smoothness of `u`,`p` on `[0,T]×R^3`, `eq:NS` pointwise, `u(0)=u_0`; (R3)
`u ∈ C([0,T];L^q)` for `q ∈ {2,3,4,∞}`, `∇u ∈ C([0,T];L^2)`,
`p ∈ C([0,T];L^2∩L^∞)`. Every one of the seven memberships is used at least once
(`q=3` in Step 5(a) and in `X`; `q=4` in all three cutoff errors; `Π_∞` in
Step 1 and Step 5(c); `Π_2` in `E^p`). Preserved Schwartz decay in time is never
assumed — the cutoff `χ_R` replaces it, as D2 requires. **One exception**, and it
is the defect of §3: the phrase "this is an `L^2` function" needs
`u_iu_j ∈ H^2`, which (R2)–(R3) do not give.

*Non-circularity.* `p̃ := R_iR_j(u_iu_j)` is built from `u_iu_j ∈ L^2`, i.e. from
the `u`-part of R only; `lem:pressure-convention`(c) then identifies it with the
normalised pressure of `prop:localtheory`, after which the `p`-part of R is used.
No circular use. Moreover `prop:pressure`(iv) makes the whole balance insensitive
to a `p → p + c(t)` ambiguity, so even a weaker reading of D2's "normalised `p`"
would not damage the result.

### 2.2 Refutation attempts

1. **Exact-solution test of `eq:pressure-balance`, `D_3` and its factor `2`
   (explicit example).** Take the shear field `u(t,x) = (f(x_2,t),0,0)` with
   `∂_tf = ν∂_2^2f`. Then `div u = 0`, `(u·∇)u = 0`,
   `∂_i∂_j(u_iu_j) = ∂_1^2(f^2) = 0`, so the normalised pressure is `p ≡ 0`, and
   `eq:NS` holds. Here `|∇u|^2 = (∂_2f)^2`, `(∇u)^Tu = f∂_2f\,e_2`, so
   `|(∇u)^Tu|^2/|u| = |f|(∂_2f)^2` and
   `D_3 = ∫(|f|(∂_2f)^2 + |f|(∂_2f)^2) = 2∫|f|(∂_2f)^2`. Independently,
   `d/dt∫|f|^3/3 = ν∫|f|f∂_2^2f = −ν∫∂_2(|f|f)∂_2f = −2ν∫|f|(∂_2f)^2`. The two
   agree, with `P_3 = 0`: the identity, the *sum* of the two terms in
   `eq:D3-def`, and the sharpness of the constant `2` in `eq:D3P3-bounds` are all
   confirmed. (The field is not in the admissible class — `X(t) = ∞` on `R^3` —
   so this is a check of the algebra, not of the theorem; but any factor error in
   `D_3` would show up here, and none does.)
2. **Attempt to remove the `ρ_ε` device from Step 7.** If one tests with `r_ε u`
   instead of `ρ_ε u`, the cutoff error becomes
   `|∫r_ε u·∇χ_R| ≤ R^{-1}‖∇χ‖_∞∫_{R≤|x|≤2R}(|u|+√ε)|u|`, whose second part is
   bounded only by `R^{-1}√ε‖u‖_2|\{R≤|x|≤2R\}|^{1/2} ∼ √ε\,R^{1/2}‖u‖_2`, which
   **diverges** as `R→∞`. So the subtraction of `√ε` is not cosmetic: without it
   `prop:pressure`(iv) does not follow from the stated memberships (one would need
   `u ∈ L^1`, which D2 does not give). The candidate's device is necessary and
   correct. No defect.
3. **Attempt to break `lem:integrands`(ii) `V ≤ |a||G|^2`.** `a = e_1`,
   `G = e_1⊗e_1`: `G^Ta = e_1`, `V = 1 = |a||G|^2`. Equality — sharp, not false.
4. **Attempt to break `eq:HEps-majorant` numerically.** `ε = 1`: `|a| = 0.1`
   gives `H = 0.00502 ≤ 0.022`; `|a| = 1` gives `0.609 ≤ 4`; `|a| = 10` gives
   `338.0 ≤ 2200`, and `|a|^2r_ε = 1005 ≥ 338`. No violation; the naive bound
   `H_ε ≤ (|a|^2+ε)^{3/2}/3` (without subtracting `ε^{3/2}`) is indeed **not**
   `ε`-uniformly integrable on `R^3`, which is exactly why the candidate's form is
   needed.
5. **Attempt to break `lem:diff-under-integral` at the endpoints `t = 0,T`.** The
   mean value theorem is applied to `τ ↦ F(τ,x)` on a subinterval of `[0,T]`; the
   one-sided difference quotients at the endpoints are covered, and `Φ ∈ C^1([0,T])`
   is used only through the FTC on `[s,t] ⊂ [0,T]`. No defect.
6. **Attempt to break the `L^2`-multiplier claim
   `ξ_iξ_j\widehat{u_iu_j} ∈ L^2`** (the sentence of §3). Counterexample to the
   general implication: `\hat g(ξ) = (1+|ξ|^2)^{-1}` satisfies
   `∫_{R^3}(1+|ξ|^2)^{-2}dξ = π^2 < ∞`, so `g ∈ L^2(R^3)`, while
   `ξ_1^2\hat g(ξ) → 1` as `|ξ|→∞` along `ξ = (ξ_1,0,0)`, so
   `ξ_1^2\hat g ∉ L^2`. Hence "`\widehat{u_iu_j} ∈ L^2` ⟹
   `ξ_iξ_j\widehat{u_iu_j} ∈ L^2`" is invalid, and for the case at hand
   (R2)–(R3) give only `u_iu_j ∈ H^1` (`∇(u_iu_j) = u_i∇u_j+u_j∇u_i ∈ L^2` from
   `u ∈ L^∞`, `∇u ∈ L^2`), i.e. `|ξ|\widehat{u_iu_j} ∈ L^2` — one derivative short
   of the asserted `L^2` membership. **This attempt succeeds**, and is the finding
   of §3.
7. **Attempt to find a use of `prop:localtheory` beyond (R2)–(R3).** None found
   other than item 6. In particular no `L^p` Riesz bound, no Calderón–Zygmund
   theory, no Rademacher theorem, no `W^{1,1}` chain rule, no `L^2` Fourier
   inversion theorem, and no a.e. statement about `∇|u|` appears anywhere.

## 3. FIRST BAD BRIDGE

**No invalid bridge; one unjustified assertion.** In reading order, the first
defective element is in the **proof of Lemma `lem:pressure-convention`, part
(a)**, second sentence:

> With the symbol of `∂_i∂_j` from the Conventions,
> `\widehat{∂_i∂_j(u_iu_j)} = −4π^2ξ_iξ_j\widehat{u_iu_j}` as tempered
> distributions, **and this is an `L^2` function.**

Three things are wrong with the highlighted clause.

* **It is false as a general statement.** `\widehat{u_iu_j} ∈ L^2` does not imply
  `ξ_iξ_j\widehat{u_iu_j} ∈ L^2` (§2.2 item 6, with the explicit
  `\hat g = (1+|ξ|^2)^{-1}`).
* **It is not derivable from the declared hypotheses.** The asserted membership is
  precisely `u_iu_j ∈ H^2`. From (R2)–(R3) one gets `u_iu_j ∈ L^2` (via `u ∈ L^4`)
  and `∇(u_iu_j) ∈ L^2` (via `u ∈ L^∞`, `∇u ∈ L^2`), i.e. `u_iu_j ∈ H^1`, and
  nothing more: (R3) as narrowed in round 2 contains no second-derivative
  information, and (R2) is a pointwise smoothness statement with no decay. So the
  clause is an unsourced appeal to the part of the regularity package that
  round 2 deliberately pruned (round 1's deleted `(R1)`,
  `u ∈ C^j([0,T];H^k)`, would have supplied it). Under D5 this is a step that is
  not written out.
* **It is stronger than needed, so it should be replaced rather than justified.**
  The clause is load-bearing only for the assertion that
  `\widehat{∂_i∂_j(u_iu_j)}` *is a function* (so that pointwise multiplication by
  `−(4π^2|ξ|^2)^{-1}` in `\cite[eq.~(14), p.~38]{Tao2013}` is meaningful) and that
  the resulting expression is locally integrable. Both follow from
  `\widehat{u_iu_j} ∈ L^2 ⊂ L^1_{loc}` and the local boundedness of `ξ ↦ ξ_iξ_j`,
  which is exactly Tao's own hypothesis in (14) — and which the candidate itself
  verifies one sentence later ("bounded by `|\widehat{u_iu_j}| ∈ L^2`, hence
  locally integrable"). Nothing downstream uses the `L^2` claim.

Consequence for the verdict: the lemma's conclusion, and therefore everything
downstream (`def:D3P3`, `prop:pressure`(i)–(iv), `cor:absorption-consequence`),
stands unchanged once the sentence is replaced. **REPAIR**, not FAIL, and the
repair is one paragraph (§5).

Everything else that round 1 flagged is closed. In particular:

* **Round 1's first defect (Tao page numbers) is fixed and verified here.** All
  four locations were read independently in this lane against the publisher PDF
  and are correct, with the quoted wording verbatim (§4, facts 1–5). The
  now-unused `H^s` citation was correctly reassigned to p. 36 and then dropped.
* **Round 1's second defect (unsourced textbook facts) is fixed.** Grep of the
  block shows `\cite` at every use of Plancherel, the distributional symbol of
  `∂_j`, Hölder, DCT, Tonelli/Fubini, the MVT and the FTC; the round-1 worry that
  the promised keys were never used is gone. The retreat from theorem numbers to
  chapter/section level is the right call under D5 (a primary source plus a status
  label is what D5 asks for), and the section locations are apt (§4, facts 6–10).
* **`lem:embedding` and `(R1)` are gone**, the `L^2` inversion theorem and the
  `π^2` weight integral with them; `(R3)` is narrowed to exactly what is consumed
  (verified in §2.1); `Θ/Ψ → W/V` and `ϑ → λ` remove the three-way theta
  collision; `rem:old-form`, `eq:D3P3-bounds`, the named section constants and the
  subsequence-principle sentence all landed.

## 4. EVIDENCE

**Primary source, re-opened in this lane** (Tao, APDE 6 (2013) 25–107, publisher
PDF, printed pagination from the running heads; read as text):

| printed page | content found | matches candidate? |
|---|---|---|
| 28 | `Δp = −∂_i∂_j(u_iu_j) + ∇·f` (8); "We then say that the periodic smooth solution `(u,p,u_0,f,T)` has normalised pressure if one has" `p = −Δ^{-1}∂_i∂_j(u_iu_j) + Δ^{-1}∇·f` (9); "We remark that this normalised pressure condition can also be imposed for smooth finite energy solutions (because `∂_i∂_j(u_iu_j)` is a second derivative of an `L^1_x(R^3)` function, and `∇·f` is the first derivative of an `L^2_x(R^3)` function), but it will turn out that normalised pressure is essentially automatic in that setting anyway; see Lemma 4.1"; footnote 4 as quoted | **yes**, verbatim, including the periodic scoping the candidate now states |
| 35 | `\hat f(ξ) := ∫_{R^3}e^{−2πix·ξ}f(x)dx` for `f ∈ L^1_x(R^3)`; "we then extend this Fourier transform to tempered distributions in the usual manner"; also the Einstein summation declaration and "We define the absolute value of a tensor in the usual Euclidean sense. Thus … `|u|^2 = u_iu_i`, `|∇u|^2 = (∂_iu_j)(∂_iu_j)`" | **yes** for the Fourier convention; the tensor-absolute-value sentence is also here (see §7 item 1) |
| 36 | classical `‖u‖_{H^k_x(Ω)} = (Σ_{j≤k}‖∇^ju‖_{L^2}^2)^{1/2}`; `‖u‖_{H^s_x(R^3)} = (∫(1+|ξ|^2)^s|û|^2dξ)^{1/2}`; `H^s_x`, `Ḣ^s_x` "the space of tempered distributions with finite … norm"; "the two norms are equivalent up to constants" | **yes**; correctly recorded as no longer used |
| 37 | `C^k_x`, the mixed norms `L^p_tX_x`, `C^k_tX_x`, and `X^s := L^∞_tH^s_x ∩ L^2_xH^{s+1}_x` (13) | confirms that 35/36, not 37/38, are the right pages — round 1's correction stands |
| 38 | "All of these above function spaces can of course be extended to functions that are vector or tensor-valued without difficulty (there are multiple ways to define the norms in these cases, but all such definitions will be equivalent up to constants)"; `\widehat{Δ^{-1}f}(ξ) := −(4π^2|ξ|^2)^{-1}\hat f(ξ)` (14), "which is well-defined for any tempered distribution `f : R^3 → R` for which the right-hand side of (14) is locally integrable. This is for instance the case if `f` lies in the `k`-th derivative of a function in `L^1_x(R^3)` for some `k ≥ 0`, or the `k`-th derivative of a function in `L^2_x(R^3)` for some `k ≥ 1`"; Newton potential (15); Leray projection and the Calderón–Zygmund `L^p` remark | **yes**, verbatim |

So four of four `[DI]` Tao facts (and the fifth, p. 36, recorded as unused) are
confirmed in content **and** location. The citation layer of the block is sound.

**Textbook `[MO]` locations, checked at table-of-contents level** (the books were
not opened; this check is itself `[MO]`): Stein–Weiss, *Introduction to Fourier
Analysis on Euclidean Spaces*, Ch. I "The Fourier Transform" has §2 "The `L^2`
theory and the Plancherel theorem" and §3 "The class of tempered distributions",
so the candidate's `\cite[Ch.~I, \S2]{SteinWeiss1971}` for Plancherel and
`\cite[Ch.~I, \S3]{SteinWeiss1971}` for `\widehat{∂_jf} = 2πiξ_j\hat f` on
tempered distributions are in the right place. Rudin *RCA* Ch. 1 (Abstract
integration — dominated convergence), Ch. 3 (`L^p`-spaces — Hölder), Ch. 8
(Integration on product spaces — Fubini/Tonelli) and Rudin *PMA* Ch. 5
(Differentiation — MVT), Ch. 6 (Riemann–Stieltjes integral — FTC) likewise match
the facts cited to them.

**Independent rederivation:** §2.1, done before reading the candidate's own
justifications; every constant recomputed (`3r|a|^2`, `‖u‖_4^2`,
`‖u‖_3^3+‖u‖_4^4`, `C_E`, the factor `2` in `eq:D3P3-bounds`, `(1−θ)`,
`M = (‖u_0‖_3^3+3A)^{1/3}`).

**Refutation attempts:** §2.2, seven of them, one with an exact solution, one
numerical, one with an explicit `L^2` counterexample. Six failed; the seventh
(item 6) succeeded and is §3.

**Lean cross-check of `rem:lean-majorant`:** all five named lemmas exist in
`../navier-formal/NavierFormal/Regularization.lean` at the lines the
candidate's fact table gives — `rEps_le_norm_add_sqrt` l. 94,
`HEps_le_norm_sq_mul_rEps` l. 141, `abs_HEps_le_two` l. 177, `tendsto_HEps`
l. 202, `hasFDerivAt_HEps` l. 260 — and the module header does say "Everything is
stated for a general real inner product space `E`". The remark's stronger claim
that all of `lem:reg-calculus`(i)–(iii) is formalised is *also* true, via
`norm_le_rEps` (l. 87), `HEps_nonneg` (l. 131), `tendsto_rEps` (l. 190) and
`hasFDerivAt_rEps` (l. 238), which the remark does not name (§7 item 5).

**Manuscript comparison:** `main.tex` l. 199 (`\section{A signed critical
balance}`), l. 201–254 (old `prop:pressure` and its proof, ending at
`\end{proof}` on l. 254), l. 256–262 (`L_J`, `Q_J` with `u·∇|u|`), l. 345–353
(the `eq:pressure-consequence` paragraph), l. 393–412 (`hyp:critical` and the `M`
formula). Every line range the candidate's §2.1 gives is correct.
`references.bib`'s `Tao2013` is the APDE article with `pages = {25--107}`, so the
printed pagination the candidate uses is the right one.

**Sibling-lane interface:** `cp02-energy-enstrophy.md` declares
`\newtheorem{lemma}` and `\newtheorem{definition}` (l. 16–17), so only
`corollary` is new — as the candidate says; it fixes the same `χ_R` (l. 69–70)
and proves `lem:div-zero` (l. 130) for `g ∈ C^1` with `g,∂_ig ∈ L^1`, of which
this lane's `lem:divergence` is the compact-support case (the reduction the
candidate states is correct: apply `lem:div-zero` to `fg_i`, which is `C^1` with
compact support, hence `fg_i, ∂_i(fg_i) ∈ L^1`). Its Tao citations are
`\cite[p.~14]` (Fourier convention) and `\cite[p.~15]` (classical `H^k` norm);
the candidate's instruction to change them to printed **35** and **36** is
verified correct by the table above.

## 5. REPLACEMENT ARGUMENT (complete)

Exactly one passage changes. In the proof of Lemma `lem:pressure-convention`,
part (a), replace the two sentences

> `(a) $u_iu_j\in L^2$ because $u(t)\in L^4$ by (R3) and
> $\norm{u_iu_j}_2\leq\norm{|u|^2}_2=\norm u_4^2$.  With the symbol of
> $\partial_i\partial_j$ from the Conventions,
> $\widehat{\partial_i\partial_j(u_iu_j)}=-4\pi^2\xi_i\xi_j\,\widehat{u_iu_j}$
> as tempered distributions, and this is an $L^2$ function.  The right-hand
> side of \cite[eq.~(14)]{Tao2013} applied to $f=\partial_i\partial_j(u_iu_j)$
> is therefore ...`

by

```latex
(a) $u_iu_j\in L^2$ because $u(t)\in L^4$ by (R3) and
$\norm{u_iu_j}_2\leq\norm{|u|^2}_2=\norm u_4^2$; hence, by Plancherel's
theorem \cite[Ch.~I, \S2]{SteinWeiss1971}, $\widehat{u_iu_j}$ is (almost
everywhere) an $L^2(\R^3)$ function.  With the symbol of
$\partial_i\partial_j$ from the Conventions,
\[
 \widehat{\partial_i\partial_j(u_iu_j)}
 =-4\pi^2\xi_i\xi_j\,\widehat{u_iu_j}
\]
as tempered distributions.  The right-hand side is a measurable function,
being the product of the continuous function $\xi\mapsto-4\pi^2\xi_i\xi_j$
with an $L^2$ function, and it is integrable on every compact subset of
$\R^3$, since $\xi_i\xi_j$ is bounded there and $L^2(K)\subset L^1(K)$ for
compact $K$ by the Cauchy--Schwarz inequality.  In particular
$\widehat{\partial_i\partial_j(u_iu_j)}$ is a function and may be multiplied
pointwise by $-(4\pi^2|\xi|^2)^{-1}$.  (We do not assert
$\xi_i\xi_j\widehat{u_iu_j}\in L^2$, which would amount to
$u_iu_j\in H^2$ and does not follow from (R2)--(R3); local integrability is
all that \cite[eq.~(14), p.~38]{Tao2013} requires.)  The right-hand side of
\cite[eq.~(14), p.~38]{Tao2013} applied to
$f=\partial_i\partial_j(u_iu_j)$ is therefore ...
```

and continue with the candidate's text unchanged from
"`is therefore $-(4\pi^2|\xi|^2)^{-1}\cdot(-4\pi^2\xi_i\xi_j)\widehat{u_iu_j}
=\xi_i\xi_j|\xi|^{-2}\widehat{u_iu_j}$ for $\xi\neq0$ …`" to the end of the
lemma. No other line of the block changes; no displayed formula, constant,
exponent or sign changes anywhere; no new external fact is introduced (the
Plancherel citation is already in the Conventions, and Cauchy–Schwarz is already
cited there through Hölder).

A second, inferior route would be to restore round 1's `(R1)`
(`u ∈ C^j([0,T];H^k)` for all `j,k`, which D2 does supply) and deduce
`u_iu_j ∈ H^2`. That would make the sentence true but would re-widen the
interface with `prop:localtheory` for no gain, since the conclusion needs only
local integrability. The repair above is the one to apply.

With that paragraph applied, the block discharges P-0, P-1, P-2, P-3 and
`eq:pressure-consequence` at the D5 standard, is self-contained (no statement in
it rests on an evidence file), and every external fact in it carries a primary
source with a `[DI]`/`[MO]` status recorded in the candidate's §3 and cross-checked
in §4 above.

## 6. UNNECESSARY DEPENDENCIES

1. **The `L^2` clause of §3 is itself an unnecessary dependency** — on regularity
   the lane does not declare. Removing it (§5) *shrinks* the interface with
   `prop:localtheory` to exactly (R2)–(R3).
2. **Remark `rem:lean-majorant`** is needed by no statement and still points at a
   repository with no bibliographic record (round-1 §6.5, not closed). Keep at
   most one Lean remark across the two lanes and give the development a citable
   record (repository plus commit) in `references.bib`, or drop the remark.
3. **`lem:integrands`(iv)'s monotonicity clause** ("the first one increasingly")
   remains unused: only dominated, never monotone, convergence is invoked
   (round-1 §6.4). Harmless documentation.
4. **`lem:divergence`, the Conventions paragraph and the `χ_R` construction**
   duplicate the sibling lane. Only one copy may survive integration; the
   candidate's own integration note gives the mechanical replacement and is
   correct (§4).
5. No further pruning found. `K_2,K_3,K_4,K_∞,G,Π_2,Π_∞` are all genuinely used;
   `lem:reg-calculus`(iv) is used only in Step 7 but is used; the explicit
   construction of `g`, `η`, `χ` is needed for self-containedness if the sibling's
   copy is the one deleted. The restriction `R ≥ 1` in Step 2 is never used
   (`C_E/R` holds for every `R>0`) and may be dropped.

## 7. MINOR EDITORIAL ISSUES FOR THE INTEGRATOR

1. **`\norm u_q:=\norm{|u|}_q` is not "componentwise".** The candidate's
   Conventions say "Vector fields are measured componentwise, `‖u‖_q := ‖|u|‖_q`,
   which is one of the equivalent tensor-valued conventions of
   `\cite[p.~38]{Tao2013}`". The formula is the Euclidean-norm convention, not a
   componentwise one; and its exact source is printed **p. 35** ("We define the
   absolute value of a tensor in the usual Euclidean sense. Thus … `|u|^2 = u_iu_i`,
   `|∇u|^2 = (∂_iu_j)(∂_iu_j)`", verified `[DI]` in this lane), with p. 38 kept only
   for "these function spaces … can be extended to functions that are vector or
   tensor-valued". Suggested: "Tensors are measured in the Euclidean sense,
   `‖u‖_q := ‖|u|‖_q` `\cite[p.~35]{Tao2013}`; the function spaces extend to
   tensor-valued functions, all such conventions being equivalent up to constants
   `\cite[p.~38]{Tao2013}`." Note that Tao's `|∇u|^2 = (∂_iu_j)(∂_iu_j)` agrees
   with the candidate's `|∇u|^2 = Σ_{i,j}(∂_ju_i)^2`.
2. **The Einstein summation convention is used but never declared.** Displays such
   as `ν∫χ_Rr_εu_i\,∂_j∂_ju_i\,dx`, `∂_j(χ_Ru_j)` and the statement
   `p = R_iR_j(u_iu_j)` sum over repeated indices; `lem:pressure-convention` writes
   `Σ_{i,j}` explicitly. Declare the convention once in the Conventions (Tao does
   so on p. 35) and drop the mixed usage.
3. **`p` is never observed to be real-valued.** `R_iR_j` has the real, even symbol
   `−ξ_iξ_j/|ξ|^2`, hence maps real `L^2` functions to real `L^2` functions. One
   clause in `lem:pressure-convention` closes this.
4. **The regularity `enumerate` begins at `\item[(R2)]`** with no `(R1)`, a
   visible scar of the round-2 deletion. Renumber to `(R1)`, `(R2)` (or `(a)`,
   `(b)`) and adjust the ten in-text references.
5. **`rem:lean-majorant` under-names its own support.** The claim covers
   `lem:reg-calculus`(i)–(iii), but the five lemmas listed omit `norm_le_rEps`
   (l. 87), `HEps_nonneg` (l. 131), `tendsto_rEps` (l. 190) and `hasFDerivAt_rEps`
   (l. 238), which carry the rest. Either name them or weaken the claim to
   `eq:HEps-majorant` plus `hasFDerivAt_HEps`/`tendsto_HEps`. (See also §6 item 2.)
6. **`rem:differential-form` understates the generalised dominated convergence
   hypothesis.** Pratt's form needs the majorants to converge *almost everywhere*
   as well as in `L^1`; the sketch should say that the subsequence is chosen so
   that `u(t_n)`, `∇u(t_n)` and the majorants all converge a.e. As a remark that
   explicitly disclaims the result this is acceptable, but a referee will notice.
7. **`cor:absorption-consequence`(ii) mixes quantifier scopes.** The corollary
   opens by fixing `ν, u_0, H`, then (ii) asserts the globally quantified
   `hyp:critical`. Either move (ii) out of the "fix" scope or append "since
   `ν, u_0, H` were arbitrary".
8. **Four `\subsection*` levels appear in Section 4** where `main.tex` has none
   (round-1 §7.6, still open). Harmless, but make it uniform with whatever the
   sibling lane's block introduces.
9. **Integration list, unchanged and still owed:** one merged Conventions
   paragraph (with the sibling's `p.~14`/`p.~15` → **35**/**36**), one `χ_R`, one
   divergence lemma (`lem:div-zero` or `lem:divergence`), one regularity
   paragraph, at most one Lean remark, `\newtheorem{corollary}[theorem]{Corollary}`,
   and the three bib records of the candidate's §2.3 (which are well formed).
10. **Lane F-1 interface, still blocking for the integrated file.** `main.tex`
    l. 260–262 defines `L_J`, `Q_J` through `u·∇|u|`; until the candidate's §2.4
    patch lands, the integrated manuscript both contains `∇|u|` (against P-0) and
    has an unproved `P_3 = L_J + Q_J`. The patch itself is correct, and the
    absolute convergence it invokes (`p_{≤J}, p_{>J} ∈ L^∞` from `p ∈ L^2∩L^∞`
    plus an `L^1` kernel for `S_J`, which holds for D1's `P_{≤2^J}` since
    `φ(·/N)` has a Schwartz kernel) is correctly marked as F-1's obligation.
11. **`eq:D3P3-bounds`** drops the `(t,x)` argument on its middle integral; and
    the trailing prose after the corollary duplicates `main.tex` l. 351–353 with
    slight rewording — check that only one copy survives.
12. The candidate's fact-table row 1 routes `prop:localtheory` to Tao Theorem
    5.4(iv) and Corollary 5.8; `cp01-literature-statements` §8 item 1 records that
    citing Theorem 5.4 alone under-cites the maximal development. Not this lane's
    file, but the reopening condition below covers it.

## 8. CONDITIONAL SUFFIX THAT SURVIVES

Unchanged by this review, and now resting on a proof whose only defect is the
one-paragraph repair of §5:

* `prop:pressure` (integrated form) and `cor:absorption-consequence` give
  `hyp:absorption ⟹ hyp:critical` with `M = (‖u_0‖_3^3+3A(ν,u_0,H))^{1/3}`,
  unconditionally on the classical Schwartz-data branch of `prop:localtheory`, for
  arbitrary `ν>0`, unforced, on `R^3`, together with
  `‖u(τ)‖_3^3 + 3(1−θ)ν∫_0^τD_3 ≤ ‖u_0‖_3^3 + 3A` for `0 ≤ τ < min{H,T_*}`,
  `0 ≤ D_3 ≤ 2∫|u||∇u|^2`, `|P_3| ≤ ‖p‖_∞‖u‖_2‖∇u‖_2`, and `∫W(u,∇u)dx = 0`
  (so `P_3` is invariant under `p → p + c(t)`).
* The programme suffix is therefore unchanged: `hyp:highpressure` (with the proved
  `prop:lowpressure`) `⟹ hyp:absorption ⟹ hyp:critical ⟹ def:target` via
  `thm:continuation` and `thm:conditional`. The first unproved link remains
  `hyp:highpressure`.
* Nothing in this lane, and nothing in this review, bears on the truth of
  `hyp:highpressure`, `hyp:absorption` or `hyp:critical`.

## 9. NON-CLAIMS

* No HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION or NS-R3 result is
  asserted, approached, or made more likely by this review.
* `hyp:highpressure`, `hyp:absorption` and `hyp:critical` remain hypotheses.
* The differential form `X'/3 + νD_3 = P_3` is not claimed; continuity of
  `t ↦ D_3(t)`, `P_3(t)` is not proved here either.
* Stein–Weiss and the two Rudin volumes were **not opened** in this lane; their
  chapter/section locations were checked only against a table of contents, which
  is itself `[MO]`. The candidate's decision to cite at chapter/section level
  rather than by theorem number is endorsed.
* Tao's Lemma 4.1 was not read (in this lane or in the candidate's); it is not
  needed, since the regularity and normalisation of `p` come from
  `prop:localtheory` (D2).
* No `L^p` bound for the Riesz transforms, no Calderón–Zygmund theory, no
  Rademacher theorem, no `W^{1,1}` chain rule and no a.e. statement about `∇|u|`
  is used in the candidate or in this repair; checked line by line.
* The shear field of §2.2 item 1 is an algebra check, not an admissible solution
  of the manuscript's Cauchy problem; no conclusion about `R^3` blowup is drawn
  from it.

## 10. REOPENING CONDITION

Reopen if any of the following changes:

1. `prop:localtheory` as finally written does **not** deliver, for every
   `T < T_*`: `u, p ∈ C^∞([0,T]×R^3)` with `eq:NS` pointwise and `u(0) = u_0`;
   `u ∈ C([0,T];L^q)` for `q ∈ {2,3,4,∞}`; `∇u ∈ C([0,T];L^2)`; and, for the
   **normalised** pressure, `p ∈ C([0,T];L^2)∩C([0,T];L^∞)`. `Π_∞` is used twice
   (Step 1 and Step 5(c)) and `Π_2` once (`E^p`), so the `L^∞` half is not
   optional.
2. The definition of `p` in the manuscript changes away from `p = R_iR_j(u_iu_j)`,
   or the Fourier convention of D1 changes: the symbol computation of
   `lem:pressure-convention`, and only it, is convention-bound.
3. `(R3)` is narrowed further, or `u ∈ C([0,T];L^4)` is withdrawn: all three
   cutoff errors use `K_4`.
4. Lane F-1 does not rewrite `L_J`, `Q_J` with `W(u,∇u)` (§7 item 10), or
   normalises `W` differently.
5. `hyp:absorption` is restated with a different `τ`-range, a `θ`-dependent `A`,
   or `D_3` replaced by another weighted dissipation: the corollary's arithmetic
   is tied to `eq:absorption` exactly as it stands at `main.tex` l. 311.
6. `def:D3P3` is changed so that `V` or `W` is no longer the continuous extension
   by `0` across `{u=0}`: every measurability statement in `prop:pressure`(i)
   rests on that continuity and on nothing else.

## 11. External facts used by THIS REVIEW

| # | Fact, as used here | Source | Status |
|---|---|---|---|
| 1 | `\hat f(ξ)=∫e^{−2πix·ξ}f(x)dx` for `f ∈ L^1_x(R^3)`, extended "to tempered distributions in the usual manner"; the Einstein summation declaration; "the absolute value of a tensor in the usual Euclidean sense … `|u|^2=u_iu_i`, `|∇u|^2=(∂_iu_j)(∂_iu_j)`" | Tao, APDE 6 (2013) 25–107, printed **p. 35** | **[DI]** (publisher PDF read as text in this lane) |
| 2 | classical `H^k` norm; `‖u‖_{H^s_x(R^3)}`; `H^s_x`, `Ḣ^s_x` as spaces of tempered distributions; "equivalent up to constants" | Tao, printed **p. 36** | **[DI]** |
| 3 | `C^k_x`, mixed norms, `X^s` (13) — the pages round 1 showed had been mis-cited | Tao, printed **p. 37** | **[DI]** |
| 4 | `\widehat{Δ^{-1}f}(ξ) := −(4π^2|ξ|^2)^{-1}\hat f(ξ)` (14), "well-defined for any tempered distribution `f : R^3 → R` for which the right-hand side of (14) is locally integrable. This is for instance the case if `f` lies in the `k`-th derivative of a function in `L^1_x(R^3)` for some `k ≥ 0`, or the `k`-th derivative of a function in `L^2_x(R^3)` for some `k ≥ 1`"; the vector/tensor extension of the function spaces; Newton potential (15) | Tao, printed **p. 38** | **[DI]** |
| 5 | `Δp = −∂_i∂_j(u_iu_j) + ∇·f` (8); `p = −Δ^{-1}∂_i∂_j(u_iu_j) + Δ^{-1}∇·f` (9) for periodic smooth solutions; the remark extending the normalisation to smooth finite-energy solutions on `R^3` ("second derivative of an `L^1_x(R^3)` function … see Lemma 4.1"); footnote 4 on the additive constant | Tao, printed **p. 28** | **[DI]** |
| 6 | Stein–Weiss Ch. I "The Fourier Transform" contains §2 "The `L^2` theory and the Plancherel theorem" and §3 "The class of tempered distributions" | publisher/aggregator table of contents for Stein–Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (PMS-32) | **[MO]** (book not opened; TOC only) |
| 7 | Rudin *RCA* Ch. 1 (dominated convergence), Ch. 3 (Hölder), Ch. 8 (Fubini/Tonelli); Rudin *PMA* Ch. 5 (mean value theorem), Ch. 6 (fundamental theorem of calculus) | standard chapter structure of the two volumes | **[MO]** |
| 8 | `R_iR_j = ∂_i∂_j(−Δ)^{-1} = −Δ^{-1}∂_i∂_j`; identity of `main.tex`'s `p` with Tao's normalised pressure; no sign error; sign audit of `eq:NS` against Tao (3), GKP, ESS (1.1), Kato, Fefferman (1) | `research/evidence/cp01-literature-statements.md` §7.3 | **[DI] there**, re-read here |
| 9 | Tao Theorem 5.4(iv) and Corollary 5.8 behind `prop:localtheory`; the recorded under-citation of the maximal development | `cp01-literature-statements.md` §1.2–1.3, §8 item 1 | **[DI] there**, not re-opened here |
| 10 | `rEps_le_norm_add_sqrt` (l. 94), `HEps_le_norm_sq_mul_rEps` (l. 141), `abs_HEps_le_two` (l. 177), `tendsto_HEps` (l. 202), `hasFDerivAt_HEps` (l. 260), and additionally `norm_le_rEps` (l. 87), `HEps_nonneg` (l. 131), `tendsto_rEps` (l. 190), `hasFDerivAt_rEps` (l. 238); module header "Everything is stated for a general real inner product space `E`" | `../navier-formal/NavierFormal/Regularization.lean` | **[DI]** (file read in this lane) |
| 11 | `\section{A signed critical balance}` at l. 199; old `prop:pressure` l. 201–254; `L_J`,`Q_J` l. 256–262; `eq:pressure-consequence` paragraph l. 345–353; `hyp:critical` and the `M` formula l. 393–412; `Tao2013` = APDE, `pages = {25--107}` | `../navier-paper/main.tex`, `references.bib` | **[DI]** |
| 12 | Sibling lane declares `\newtheorem{lemma}`/`{definition}` (l. 16–17), fixes the same `χ_R` (l. 69–70), proves `lem:div-zero` (l. 130), and cites Tao as `p.~14`/`p.~15` | `research/evidence/cp02-energy-enstrophy.md` | **[DI]** |
| 13 | `∫_{R^3}(1+|ξ|^2)^{-2}dξ = π^2 < ∞`, so `\hat g = (1+|ξ|^2)^{-1}` is in `L^2(R^3)` while `ξ_1^2\hat g ∉ L^2` | recomputed inline (`r = tan λ`), §2.2 item 6 | proved here |
| 14 | The shear-field verification of `eq:pressure-balance` and of the factor `2` in `D_3` | computed inline, §2.2 item 1 | proved here |

## 12. Frontier record

**MODE / RESULT.** REVIEW — complete, round 2, verdict **REPAIR** (one
paragraph). Round 1's two source-layer defects are closed and independently
re-verified in this lane: all four Tao page locations (28, 35, 36, 38) are
correct and the quoted wording verbatim, and every external fact in the LaTeX
block now carries a `\cite` at a chapter/section location that matches the
source. The mathematics is correct: every identity, sign, constant and exponent
was rederived here, the whole balance was re-checked on an exact shear solution,
and six of seven refutation attempts failed. The seventh succeeded, against a
single clause.

**CLAIM AND SCOPE.** For the classical Schwartz-data branch of
`prop:localtheory` on `R^3`, unforced, arbitrary `ν>0`, with
`p = R_iR_j(u_iu_j) = −Δ^{-1}∂_i∂_j(u_iu_j)` under `\hat f(ξ)=∫e^{−2πix·ξ}f`:
`X(t)/3 − X(s)/3 + ν∫_s^tD_3 = ∫_s^tP_3` for all `0 ≤ s ≤ t < T_*`, with `D_3`,
`P_3` defined through the continuous extensions `V`, `W` of `|(∇u)^Tu|^2/|u|` and
`u·(∇u)^Tu/|u|`; `0 ≤ D_3 ≤ 2∫|u||∇u|^2`; `|P_3| ≤ ‖p‖_∞‖u‖_2‖∇u‖_2`;
`∫W(u,∇u)dx = 0`; and `hyp:absorption ⟹ hyp:critical` with
`M = (‖u_0‖_3^3+3A)^{1/3}`. **Verified** at this lane's standard of proof,
subject to the one-paragraph repair of §5. This review asserts nothing beyond
that verification.

**EVIDENCE.** §4 and §11: five Tao printed pages re-read as text in this lane
(28, 35, 36, 37, 38), all four `[DI]` facts confirmed in content *and* location;
Stein–Weiss and Rudin locations checked at TOC level; independent rederivation of
every identity, sign, constant and exponent (§2.1); seven refutation attempts
(§2.2), including an exact-solution check of `eq:pressure-balance` and the
factor `2` in `D_3`, a proof that the `ρ_ε` device is necessary (the naive test
function diverges like `√ε R^{1/2}`), and an explicit `L^2` counterexample;
Lean cross-check of nine lemmas by name and line; verbatim comparison with
`main.tex` l. 199–254, 256–262, 345–353, 393–412 and with the sibling lane.

**FIRST GAP.** One clause: "`\widehat{∂_i∂_j(u_iu_j)}` … is an `L^2` function" in
`lem:pressure-convention`(a). False as a general statement (§2.2 item 6), not
derivable from the round-2-narrowed (R2)–(R3) — it amounts to `u_iu_j ∈ H^2`,
whereas (R2)–(R3) give only `u_iu_j ∈ H^1` — and stronger than the proof needs.
Replaced in §5 by the local-integrability statement that Tao's (14) actually
requires. Behind that, outside this lane: lane F-1's `L_J`, `Q_J` are still
written with `u·∇|u|`, and the two lanes' Conventions/`χ_R`/divergence lemma are
still duplicated.

**SURVIVING CONDITIONAL SUFFIX.** `hyp:highpressure` (with the proved
`prop:lowpressure`) `⟹ hyp:absorption ⟹ hyp:critical ⟹ def:target` via
`thm:continuation` and `thm:conditional`. The middle implication is audited and,
after §5, complete. The first link is untouched and remains the frontier.

**NON-CLAIMS.** §9. In particular: no HIGH-PRESSURE, HIGH-STRAIN, CRITICAL,
ABSORPTION or NS-R3 result is asserted; the differential form of the balance is
not claimed; the three textbook sources were not opened; Tao's Lemma 4.1 was not
read; the shear field used for the algebra check is not an admissible solution.

**NEXT DISTINCT ACTION.** Apply §5 to `cp02-pressure.md` (one paragraph) and the
twelve items of §7; that closes this lane. Then integrate with
`cp02-energy-enstrophy.md` — one Conventions paragraph with Tao pp. 35/36, one
`χ_R`, one divergence lemma, one regularity paragraph, one Lean remark,
`\newtheorem{corollary}`, three bib records — and hand §2.4 of the candidate to
lane F-1. Independently, and lowest priority: open Stein–Weiss Ch. I and Rudin
*RCA* Ch. 1, 3, 8 / *PMA* Ch. 5, 6 to promote facts 6–7 of §11 from `[MO]` to
`[DI]`.
