# CP02-3 AUDIT (round 1): review of `research/evidence/cp02-pressure.md`

MODE: REVIEW, proof-audit discipline. Date: 2026-09-05. Reviewer lane owns only
this file; nothing else was edited, nothing pushed.

## 0. Freeze

| item | value |
|---|---|
| candidate file | `/home/ert/proj/navier/research/evidence/cp02-pressure.md` |
| `sha256sum` | `ad6a10f1f30436ee8e4e7680d3e445e49219263e66156e7b2b29cbfe254fb58e` |
| `git -C /home/ert/proj/navier rev-parse HEAD` | `715ce84ec78d64c510e150360a354b5d55648b9c` |
| candidate length | 783 lines |
| manuscript state read in full | `/home/ert/proj/navier-paper/main.tex` (562 lines), `references.bib` (5 keys: `Fefferman2000`, `ESS2003`, `Kato1984`, `GKP2013`, `Tao2013`) |
| CP01 records read in full | `cp01-manuscript-obligations.md` (624 lines), `cp01-literature-statements.md` (806 lines) |
| sibling lane read for interface | `research/evidence/cp02-energy-enstrophy.md` |
| primary source re-opened in this lane | Tao, *Analysis & PDE* **6** (2013) 25–107, publisher PDF `https://msp.org/apde/2013/6-1/apde-v6-n1-p02-s.pdf`, printed pp. 28, 35, 36, 37, 38 read as text |

## 1. VERDICT

**REPAIR.**

The mathematics of the candidate is correct. Every identity, every constant and
every exponent in Definition `def:D3P3`, Lemmas `lem:psi-theta`,
`lem:reg-calculus`, `lem:divergence`, `lem:diff-under-integral`,
`lem:pressure-convention`, `lem:embedding`, Proposition `prop:pressure`(i)–(iv)
and Corollary `cor:absorption-consequence`(i)–(ii) was rederived independently
here and reproduced. No invalid bridge was found. The repair is confined to the
**source layer** and to **integration hygiene**, and one of the two source
defects is a demonstrable factual error in a `[DI]`-labelled citation, verified
against the publisher PDF in this lane.

## 2. REVIEWED SCOPE

Reconstructed from the first nontrivial implication onward:

1. `lem:embedding`(i)–(iii): the weight integral, the `H^2 ↪ L^∞` constant, the
   `L^q` interpolation, transfer of continuity.
2. `lem:pressure-convention`: the symbol computation
   `R_iR_j ↔ −ξ_iξ_j/|ξ|^2`, `∂_i∂_j ↔ −4π^2ξ_iξ_j`, `Δ^{-1} ↔ −(4π^2|ξ|^2)^{-1}`,
   the identification with Tao's normalised pressure, `−Δp = ∂_i∂_j(u_iu_j)`.
3. `lem:psi-theta`(i)–(iv): the Cauchy–Schwarz bound, the two pointwise
   majorants, joint continuity at `a = 0`, the `r_ε`-regularised bounds and
   limits.
4. `def:D3P3`: agreement with the manuscript's `D_3`, `P_3` off `{u=0}`.
5. `lem:reg-calculus`(i)–(iv): `∇_aH_ε = r_ε a`, `∇_ar_ε = a/r_ε`, the
   `r^3−s^3` estimate, `eq:HEps-majorant`, the `ρ_ε` bound.
6. `lem:divergence`, `lem:diff-under-integral`.
7. `prop:pressure` Steps 1–7: measurability/boundedness of `D_3`, `P_3`; the
   three integrations by parts with their exact algebra and signs; the three
   cutoff errors and `C_E`; `eq:cutoff-identity`; the `R→∞` limit; the `ε↓0`
   limit; continuity of `X`; the `ρ_ε` proof of `∫Θ(u,∇u)dx = 0`.
8. `cor:absorption-consequence`(i)–(ii) against the verbatim `hyp:absorption`
   and `hyp:critical` of `main.tex` (lines 306–318, 393–402).
9. Every `\cite` in the replacement block against the primary text.
10. The declared interfaces: `prop:localtheory` (D2), `eq:NS`, `hyp:absorption`,
    `hyp:critical`, `eq:pressure-consequence`, and the labels of `main.tex`
    lines 256–262 (`L_J`, `Q_J`).

### 2.1 Steps confirmed by independent rederivation (recorded so a later lane
need not repeat them)

*Chain rule and substitution.* `∇_aH_ε(a) = (1/3)(3/2)(|a|^2+ε)^{1/2}·2a = r_ε a`,
so `∂_τ(χ_RH_ε(u)) = χ_R r_ε u·∂_τ u`; substituting
`∂_τu = νΔu − (u·∇)u − ∇p` from `eq:NS` gives the three integrals of Step 3.
Confirmed.

*Diffusion.* With `f = χ_R r_ε u_i`, `g = ∂_ju_i`:
`ν∫χ_R r_ε u_i∂_j∂_ju_i = −ν∫χ_Rr_ε|∇u|^2 − ν∫χ_R(∂_jr_ε)u_i∂_ju_i − ν∫(∂_jχ_R)r_εu_i∂_ju_i`,
and `∂_jr_ε = ((∇u)^Tu)_j/r_ε`, `u_i∂_ju_i = ((∇u)^Tu)_j`. Hence
`ν∫χ_Rr_ε u·Δu = −νD_{ε,R} + E^d_{ε,R}` with exactly the candidate's
`D_{ε,R}` and `E^d_{ε,R} = −ν∫r_ε∇χ_R·(∇u)^Tu`. Confirmed, including the sign.

*Convection.* `∂_j(H_ε(u)) = r_εu_i∂_ju_i`, so
`r_ε u·(u·∇)u = u_j∂_j(H_ε(u))`; with `f = χ_Ru_j`, `g = H_ε(u)` and
`div u = 0`, `−∫χ_Rr_εu·(u·∇)u = ∫H_ε(u)u·∇χ_R = E^c_{ε,R}`, i.e. the
convection term contributes **only** a cutoff error. Confirmed.

*Pressure.* With `f = χ_Rr_εu_i`, `g = p`:
`−∫χ_Rr_εu·∇p = ∫p·div(χ_Rr_εu) = P_{ε,R} + E^p_{ε,R}`, using
`div(r_εu) = u·∇r_ε = u·(∇u)^Tu/r_ε`. Confirmed.

*Assembly and errors.* `Φ'_{ε,R} = −νD_{ε,R} + P_{ε,R} + E_{ε,R}`; FTC gives
`eq:cutoff-identity`. Recomputed exponents:
`∫(|u|^2+|u|)|∇u| ≤ (‖u‖_4^2+‖u‖_2)‖∇u‖_2` (Cauchy–Schwarz, `‖|u|^2‖_2 = ‖u‖_4^2`);
`∫2(|u|^2+|u|^3)|u| = 2(‖u‖_3^3+‖u‖_4^4)`;
`∫|p|(|u|^2+|u|) ≤ ‖p‖_2(‖u‖_4^2+‖u‖_2)`. All three, and `C_E`, are correct as
printed, and all are uniform in `ε ∈ (0,1]` because `r_ε ≤ |u|+1` there.

*Majorants.* `0 ≤ g_n ≤ (2|u|+1)|∇u|^2` uses `r_ε ≤ |u|+1` and
`|(∇u)^Tu|^2/r_ε ≤ |u||∇u|^2`; `|h_n| ≤ |p||u||∇u|` uses
`|a·G^Ta|/r_ε(a) ≤ |a||G|`. Both space–time integrals are finite by Tonelli with
`(t−s)(2K_∞+1)G^2` and `(t−s)Π_∞K_2G`. Confirmed. The `ε`-uniform time-primitive
majorant `|H_ε(a)| ≤ 2(|a|^2+|a|^3)` (`0<ε≤1`) follows from
`r^3−s^3 = (r−s)(r^2+rs+s^2) ≤ 3r^2(r^2−s^2)/(r+s) ≤ 3r|a|^2`, i.e.
`H_ε ≤ r_ε|a|^2 ≤ |a|^2(|a|+1)`. Confirmed; it is in fact sharp up to the
factor `2`.

*Weight integral.* `∫_{R^3}(1+|ξ|^2)^{-2}dξ = 4π∫_0^∞ r^2(1+r^2)^{-2}dr
= 4π∫_0^{π/2}\sin^2ϑ\,dϑ = π^2` under `r = tan ϑ`, so `‖f̂‖_1 ≤ π‖f‖_{H^2}`.
Confirmed, including the constant.

*Zero-set device.* `ρ_ε = r_ε(u)−√ε` satisfies `∇ρ_ε = ∇r_ε` and
`ρ_ε|u| ≤ |u|^2` because `ρ_ε = |u|^2/(r_ε+√ε) ≤ |u|`. Hence
`|∫χ_R u·(∇u)^Tu/r_ε| = |∫ρ_ε u·∇χ_R| ≤ R^{-1}‖∇χ‖_∞‖u(t)‖_2^2 → 0`, and the
naive test function `r_ε u` (which would need `u ∈ L^1`) is indeed avoided.
Confirmed; this is the sharpest single idea in the candidate.

*Corollary.* From `eq:pressure-balance` with `s=0`, `t=τ` and `eq:absorption`:
`X(τ)/3 ≤ X(0)/3 − (1−θ)ν∫_0^τ D_3 + A`, so
`X(τ) + 3(1−θ)ν∫_0^τD_3 ≤ ‖u_0‖_3^3 + 3A`, both left terms nonnegative;
`eq:pressure-consequence` and `(1−θ)ν∫_0^τD_3 ≤ (‖u_0‖_3^3+3A)/3` follow.
`τ = 0` is separated correctly, since `hyp:absorption` (`main.tex` line 313)
quantifies `0<τ<min{H,T_*}` only. Cube roots give `hyp:critical` with
`M = (‖u_0‖_3^3+3A)^{1/3}`, matching the manuscript's line 406 formula exactly.
Confirmed.

*Non-circularity.* `p := R_iR_j(u_iu_j)` is defined from `u_iu_j ∈ L^2`, which
uses only the `u`-part of the regularity package; `lem:pressure-convention` then
identifies it with the normalised pressure, after which the `p`-part of the
package may be used. There is no circular use of `prop:localtheory`. Confirmed.

*Uses of R.* The candidate uses `(R2)` pointwise smoothness on `[0,T]×R^3`, and
`(R3)` only for `u ∈ C([0,T];L^q)`, `q ∈ {2,3,4,∞}`, `∇u ∈ C([0,T];L^2)`,
`p ∈ C([0,T];L^2∩L^∞)`. It never assumes preserved Schwartz decay in time
(D2's prohibition) — the cutoff `χ_R` is what replaces it. Legitimate.

### 2.2 Refutation attempts (all failed; recorded)

1. `Ψ(a,G) ≤ |a||G|^2`: tested at `a = e_1`, `G = e_1⊗e_1` (`∂_1u_1 = 1`,
   all other entries `0`). Then `G^Ta = e_1`, `Ψ = 1`, `|a||G|^2 = 1`:
   equality. The inequality is sharp, not false.
2. `(∇u)^Tu = |u|∇|u|` off `{u=0}` with a possible factor `1/2` or `2`: tested
   on the shear `u = (u_1(x_2),0,0)`. `|u|∇|u| = u_1u_1'e_2` and
   `((∇u)^Tu)_2 = u_1∂_2u_1 = u_1u_1'`: equal, no stray factor.
3. `∫Θ(u,∇u)dx = 0` (`prop:pressure`(iv)): tested on the same shear
   (`Θ ≡ 0` identically there) and on `u = (∂_2ψ,−∂_1ψ,0)` with
   `ψ ∈ C_c^∞`, where `∫u·∇|u| = −∫|u|\,\mathrm{div}\,u = 0`. No
   counterexample; and Step 7's proof does not go through `∇|u|` at all, so the
   zero set cannot break it.
4. The `ε`-uniform majorant with the exponent `3/2` replaced by the naive bound
   `H_ε ≤ (1/3)(|a|^2+ε)^{3/2}`: this is **not** `ε`-uniformly integrable near
   `|a| = 0` on `R^3` (it does not vanish as `|a| → 0`), which is exactly why
   the subtraction of `ε^{3/2}` in `H_ε` is necessary. The candidate's
   `H_ε ≤ r_ε|a|^2` is the correct repair and is used. No defect.
5. Reversal of the diffusion sign (the classical trap in this computation):
   checked against `main.tex` lines 249–250 (`−∫Δu·|u|u = D_3`,
   `∫∇p·|u|u = −P_3`) and against `cp01-manuscript-obligations.md` §1.7. The
   candidate's `ε→0` limits give exactly these. No sign error.
6. `lem:diff-under-integral` with `K` not containing `supp χ_R`: not applicable,
   `K = {|x| ≤ 2R} ⊇ supp χ_R`. The hypothesis "F vanishes off K for all t" is
   met because `χ_R` carries the vanishing, not `H_ε(u)`.

## 3. FIRST BAD BRIDGE

**No invalid mathematical bridge.** The first *defective element*, in reading
order, is in `\subsection*{Conventions}` of the replacement block: the page
locations attached to `\cite{Tao2013}`.

The candidate writes (block lines 24–32):

> `this is the convention of \cite[p.~37]{Tao2013}` (Fourier transform)
> `... \norm f_{H^s}=\norm{(1+|\xi|^2)^{s/2}\hat f}_{L^2}<\infty
>  \cite[p.~38]{Tao2013}; vector fields belong to $H^s$ componentwise.`

Verified in this lane against the publisher PDF (`msp.org`, printed pagination
visible in the running heads):

* the Fourier transform `f̂(ξ) := ∫_{R^3}e^{−2πix·ξ}f(x)dx`, "we then extend
  this Fourier transform to tempered distributions in the usual manner", is on
  printed **p. 35** (end of the page), not p. 37;
* the definition `‖u‖_{H^s_x(R^3)} := (∫_{R^3}(1+|ξ|^2)^s|û(ξ)|^2dξ)^{1/2}`
  together with "let `H^s_x(R^3)`, `Ḣ^s_x(R^3)` be the space of tempered
  distributions with finite … norm", and the sentence that the classical `H^k`
  norm "conflicts slightly … but the two norms are equivalent up to constants",
  are on printed **p. 36**, not p. 38;
* printed p. 37 carries `C^k_x`, the mixed norms and `X^s` (13);
* printed **p. 38** carries `Δ^{-1}` (14) with the words "well-defined for any
  tempered distribution `f` … for which the right-hand side of (14) is locally
  integrable" — so the candidate's two `\cite[eq.~(14)]{Tao2013}` uses and the
  wording it borrows are **exact**, and the clause "vector fields belong to
  `H^s` componentwise" is legitimately p. 38 ("All of these above function
  spaces can of course be extended to functions that are vector or
  tensor-valued … all such definitions will be equivalent up to constants"),
  although Tao does not privilege the componentwise definition;
* `p = −Δ^{-1}∂_i∂_j(u_iu_j) + Δ^{-1}∇·f` (9) is on printed **p. 28**, and is
  introduced there for *periodic* smooth solutions ("We then say that the
  periodic smooth solution … has normalised pressure if one has (9)"); the
  `R^3` case is the immediately following remark ("this normalised pressure
  condition can also be imposed for smooth finite energy solutions, because
  `∂_i∂_j(u_iu_j)` is a second derivative of an `L^1_x(R^3)` function … see
  Lemma 4.1"). The candidate's fact table (row 5) says "APDE p. 5" which is not
  a page of this article; and the bare `\cite[eq.~(9)]{Tao2013}` hides the
  periodic scoping.

The candidate's `[DI]` claim for these facts is therefore **partly wrong in the
location**, though right in the content: it converted arXiv pagination to APDE
pagination with a `+2` error. Under D5 a `[DI]` label carries the page.

The second defective element, immediately after, is that the block cites **only**
`Tao2013`. Grep of the fenced block returns five `\cite` commands, all
`{Tao2013}`. But the candidate's own placement note promises
"`\cite{SteinWeiss1971}` and `\cite{RudinRCA}` / `\cite{RudinPMA}` are new keys
for the `[MO]` sources in §3 (the integrator adds the bib records)", and the
block uses, without any source: Plancherel's theorem (twice: the `L^2`
extension, and the `‖m‖_∞` multiplier bound), the `L^2` Fourier inversion
theorem, the dominated convergence theorem (five times), Tonelli's and Fubini's
theorems (four times), the mean value theorem, and the fundamental theorem of
calculus (twice). Under D5 ("no 'standard', 'well known' … every external fact
stated exactly with a primary source") the replacement text as delivered is not
compliant; the `[MO]` table in §3 of the evidence file is not part of the
manuscript, and D5 also forbids the manuscript from resting on an evidence file.

Neither defect touches the truth of any statement. Hence REPAIR, not FAIL.

## 4. EVIDENCE

* Independent rederivation of §2.1 above, done symbol by symbol before reading
  the candidate's own justifications; every constant recomputed
  (`π^2` weight integral, `3r|a|^2`, `‖u‖_4^2`, `‖u‖_3^3+‖u‖_4^4`, `C_E`,
  `(1−θ)`, `M = (‖u_0‖_3^3+3A)^{1/3}`).
* Six refutation attempts, §2.2, all failed; two of them (items 1, 2) with
  explicit test data.
* Primary source re-opened: Tao, APDE 6 (2013) 25–107, publisher PDF, printed
  pp. 28, 35, 36, 37, 38 read as text in this lane (`helpy_pdf`,
  `mode:"text"`). This is the evidence for §3 and it contradicts the candidate's
  page numbers for two of its four `[DI]` Tao facts while confirming the
  content of all four, plus the `Δ^{-1}` wording verbatim.
* Cross-check of the four other `[DI]` claims routed through
  `cp01-literature-statements.md` §1.1 (normalised pressure), §1.2 (Thm 5.4),
  §6 S10 (Hölder), §7.3 (`R_iR_j = −Δ^{-1}∂_i∂_j`, "no sign error"): all
  consistent with the candidate's use.
* `hyp:absorption`, `hyp:critical`, `eq:pressure-consequence`,
  `eq:absorption`, `eq:missing` compared verbatim with `main.tex` lines
  306–318, 345–353, 393–409; the corollary matches the manuscript's own `M`
  formula.
* Lean cross-check of Remark `rem:lean-majorant`: the four named lemmas exist in
  `/home/ert/proj/navier-formal/NavierFormal/Regularization.lean`
  (`rEps_le_norm_add_sqrt` l. 94, `HEps_le_norm_sq_mul_rEps` l. 141,
  `abs_HEps_le_two` l. 177, `tendsto_HEps` l. 202, `hasFDerivAt_HEps` l. 260),
  the module header does state "Everything is stated for a general real inner
  product space `E`", and `abs_HEps_le_two` is literally
  `|HEps ε v| ≤ 2*(‖v‖^2+‖v‖^3)` under `0 ≤ ε ≤ 1`. The remark is accurate.
* Sibling-lane interface: `research/evidence/cp02-energy-enstrophy.md` already
  declares `\newtheorem{lemma}`/`{definition}`, already fixes the Fourier
  convention, the `H^k` definition, the tensor norms and the cutoff `χ_R`
  (with `χ = 1` on `{|x|≤1}`, `χ = 0` on `{|x|≥2}`, `‖∇χ_R‖_∞ = R^{-1}‖∇χ‖_∞`),
  already states the regularity package, and already proves
  `lem:div-zero` (`g,∂_ig ∈ L^1`, `g ∈ C^1` ⟹ `∫∂_ig = 0`), `lem:plancherel`,
  `lem:interp`. It cites the same two Tao facts as `\cite[p.~14]{Tao2013}` and
  `\cite[p.~15]{Tao2013}` — arXiv pages, also wrong for the APDE `references.bib`
  record. The two lanes must be reconciled; see §7.

## 5. REPLACEMENT ARGUMENT (complete)

Three things are replaced: (a) the citation layer of
`\subsection*{Conventions}`; (b) the two clauses of `lem:pressure-convention`
that need an exactness fix; (c) the insertion of the `[MO]` citations at the
eleven places where the block uses an unsourced external fact. Nothing else in
the candidate's block changes; in particular no displayed formula, constant or
exponent changes.

New environments required are unchanged from the candidate
(`lemma`, `corollary`, `definition`, all `[theorem]`-numbered). Three new bib
keys are required and are supplied below.

```latex
% =====================================================================
% (a) REPLACEMENT for the whole \subsection*{Conventions} of
%     cp02-pressure.md.  Corrected Tao page numbers (verified against
%     APDE 6 (2013) 25--107: Fourier transform p. 35, H^s p. 36,
%     vector/tensor extension p. 38, Delta^{-1} (14) p. 38), and the
%     [MO] sources now cited in the text.
% =====================================================================

\subsection*{Conventions}

Throughout this section $|\cdot|$ is the Euclidean norm on $\R^3$ and the
Frobenius norm on $3\times3$ matrices.  For a vector field $u$ we write
$(\nabla u)_{ij}=\partial_ju_i$, so that $|\nabla u|^2=\sum_{i,j}(\partial_ju_i)^2$,
and $(\nabla u)^{\mathsf T}u$ denotes the vector with components
\[
 \bigl((\nabla u)^{\mathsf T}u\bigr)_j=\sum_i u_i\,\partial_ju_i .
\]
With this notation $(u\otimes u):\nabla u:=\sum_{i,j}u_iu_j\partial_ju_i
=u\cdot(\nabla u)^{\mathsf T}u$.  Where $u\neq0$ one has
$(\nabla u)^{\mathsf T}u=|u|\nabla|u|$, but $\nabla|u|$ is never used below.

The Fourier transform is $\hat f(\xi)=\int_{\R^3}e^{-2\pi ix\cdot\xi}f(x)\,dx$
for $f\in L^1$, extended to $L^2$ by Plancherel's theorem
\cite[Ch.~I, Thm.~2.1 and Cor.~2.2]{SteinWeiss1971} and to tempered
distributions in the usual way; this is the convention of
\cite[p.~35]{Tao2013}.  Plancherel's theorem gives, for bounded measurable $m$
defined almost everywhere, that the multiplier
$T_mf:=\mathcal F^{-1}(m\hat f)$ satisfies
$\norm{T_mf}_2=\norm{m\hat f}_2\leq\norm m_\infty\norm f_2$, so $T_m$ is
bounded on $L^2$ with norm at most $\norm m_\infty$.  The Riesz transforms are
defined by $\widehat{R_jf}=-i\,\xi_j|\xi|^{-1}\hat f$ (a symbol defined for
$\xi\neq0$, hence almost everywhere), and $\Delta^{-1}$ is the multiplier
$-(4\pi^2|\xi|^2)^{-1}$ of \cite[eq.~(14), p.~38]{Tao2013}, which is well
defined on every tempered distribution for which the resulting expression is
locally integrable.  For $s\in\R$, $H^s=H^s(\R^3)$ is the space of tempered
distributions with
$\norm f_{H^s}=\norm{(1+|\xi|^2)^{s/2}\hat f}_{L^2}<\infty$
\cite[p.~36]{Tao2013}; for nonnegative integers $s=k$ this norm is equivalent,
up to constants depending only on $k$, to the classical Sobolev norm
$\bigl(\sum_{j\leq k}\norm{\nabla^ju}_2^2\bigr)^{1/2}$, so the two describe the
same space \cite[p.~36]{Tao2013}.  Vector fields belong to $H^s$
componentwise, with $\norm u_{H^s}^2=\sum_i\norm{u_i}_{H^s}^2$; any of the
equivalent tensor-valued conventions of \cite[p.~38]{Tao2013} would serve.

% =====================================================================
% (b) REPLACEMENT for the last two sentences of the proof of
%     Lemma lem:pressure-convention (everything from "Hence
%     $-\Delta^{-1}\partial_i\partial_j(u_iu_j)$ is well defined" to the
%     end of that proof), and for the statement's reference to (9).
%     Two fixes: (i) Tao's (9) is introduced for periodic solutions, the
%     R^3 case being the remark following it and his Lemma 4.1, so the
%     citation is widened to what the source actually supports;
%     (ii) the identification is a.e., and the continuous representative
%     is named before the pointwise equation is used.
% =====================================================================

% -- in the STATEMENT of lem:pressure-convention, replace
%    "i.e.\ $p$ is the normalised pressure of \cite[eq.~(9)]{Tao2013}
%     with $f=0$"
%    by:
i.e.\ $p$ is the normalised pressure in the sense of
\cite[eq.~(9), p.~28, and the remark following it]{Tao2013} with $f=0$
(that remark records that the normalisation \eqref{eq:NS}--(9) may be imposed
for smooth finite-energy solutions on $\R^3$, because
$\partial_i\partial_j(u_iu_j)$ is a second derivative of an $L^1(\R^3)$
function)

% -- and replace the closing of the PROOF by:
Hence the right-hand side of \cite[eq.~(14), p.~38]{Tao2013} applied to
$\partial_i\partial_j(u_iu_j)$ is the $L^2$ function
$\xi_i\xi_j|\xi|^{-2}\widehat{u_iu_j}$, which is locally integrable, so
$\Delta^{-1}\partial_i\partial_j(u_iu_j)$ is well defined in Tao's sense and
$-\Delta^{-1}\partial_i\partial_j(u_iu_j)=R_iR_j(u_iu_j)$ as elements of
$L^2$.  Multiplying the symbol $-\xi_i\xi_j/|\xi|^2$ by the symbol
$4\pi^2|\xi|^2$ of $-\Delta$ gives $-4\pi^2\xi_i\xi_j$, the symbol of
$\partial_i\partial_j$, which is the last identity.  Proposition~%
\ref{prop:localtheory} is stated for the normalised pressure; its conclusion
(R2) supplies a representative of that $L^2$ class which is smooth on
$[0,T]\times\R^3$ and satisfies \eqref{eq:NS} pointwise.  Since two
representatives of one $L^2$ class agree almost everywhere and at most one of
them is continuous, we identify $p$ with that smooth representative from now
on; (R1)--(R3) then apply to $p$, and Lemma~\ref{lem:embedding} gives the
$L^2\cap L^\infty$ statement.

% =====================================================================
% (c) THE ELEVEN [MO] CITATIONS.  Each line below gives the phrase as it
%     stands in cp02-pressure.md and the phrase that replaces it.  No
%     other text changes.
% =====================================================================

% lem:embedding, proof, (i):
%   "the inversion theorem gives"
% ->
the Fourier inversion theorem for $L^1\cap L^2$
\cite[Ch.~I, Thm.~1.9 and Cor.~2.3]{SteinWeiss1971} gives

% lem:embedding, proof, (i):
%   "the right side is continuous (dominated convergence)"
% ->
the right side is continuous by dominated convergence
\cite[Thm.~1.34]{RudinRCA}

% lem:embedding, proof, (iii):
%   "The maps $H^2\to L^2$ (Plancherel, norm $\leq1$)"
% ->
The maps $H^2\to L^2$ (Plancherel \cite[Ch.~I, Thm.~2.1]{SteinWeiss1971};
the norm is at most $1$ because $|\hat f|\leq(1+|\xi|^2)|\hat f|$)

% lem:divergence, proof:
%   "so Fubini's theorem applies and"
% ->
so Fubini's theorem \cite[Thm.~8.8]{RudinRCA} applies and

% lem:divergence, proof:
%   "by the fundamental theorem of calculus applied to the $C^1$ function"
% ->
by the fundamental theorem of calculus \cite[Thm.~6.21]{RudinPMA} applied to
the $C^1$ function

% lem:diff-under-integral, proof:
%   "the mean value theorem gives"
% ->
the mean value theorem \cite[Thm.~5.10]{RudinPMA} gives

% prop:pressure, Step 1:
%   "Tonelli's theorem (for $D_3$) and Fubini's theorem (for $P_3$)"
% ->
Tonelli's theorem (for $D_3$) and Fubini's theorem (for $P_3$),
\cite[Thm.~8.8]{RudinRCA},

% prop:pressure, Step 4, Assembly:
%   "The fundamental theorem of calculus for the $C^1$ function
%    $\Phi_{\varepsilon,R}$ yields"
% ->
The fundamental theorem of calculus \cite[Thm.~6.21]{RudinPMA} for the $C^1$
function $\Phi_{\varepsilon,R}$ yields

% prop:pressure, Step 5(b) and Step 5(c):
%   "By Tonelli's theorem" / "Dominated convergence on $[s,t]\times\R^3$
%    and Fubini's theorem give"
% ->
By Tonelli's theorem \cite[Thm.~8.8]{RudinRCA}
% and
Dominated convergence \cite[Thm.~1.34]{RudinRCA} on $[s,t]\times\R^3$ and
Fubini's theorem \cite[Thm.~8.8]{RudinRCA} give

% prop:pressure, Steps 5(a), 6(a), 6(b), 6(c), 7:
%   each "Dominated convergence"
% -> (first occurrence only; later ones may then read "dominated convergence")
Dominated convergence \cite[Thm.~1.34]{RudinRCA}

% prop:pressure, Step 1 and Step 4, and lem:psi-theta(i):
%   each bare "Cauchy--Schwarz inequality" / "H\"older"
% -> add, at the first occurrence in the section,
(H\"older's inequality on $L^p(\R^3)$, in the form
$\norm{fg}_1\leq\norm f_p\norm g_{p'}$ with $1/p+1/p'=1$)

% =====================================================================
% (d) BIB RECORDS for the three new keys.  These are the [MO] sources of
%     the table in Section 3 of this review; the theorem numbers above
%     are the ones the integrator must confirm against the printed books
%     before the manuscript is circulated (see Section 6, item 2).
% =====================================================================

@book{SteinWeiss1971,
  author    = {Elias M. Stein and Guido Weiss},
  title     = {Introduction to Fourier Analysis on Euclidean Spaces},
  series    = {Princeton Mathematical Series},
  number    = {32},
  publisher = {Princeton University Press},
  address   = {Princeton, NJ},
  year      = {1971}
}

@book{RudinRCA,
  author    = {Walter Rudin},
  title     = {Real and Complex Analysis},
  edition   = {3},
  publisher = {McGraw--Hill},
  address   = {New York},
  year      = {1987}
}

@book{RudinPMA,
  author    = {Walter Rudin},
  title     = {Principles of Mathematical Analysis},
  edition   = {3},
  publisher = {McGraw--Hill},
  address   = {New York},
  year      = {1976}
}

% =====================================================================
% (e) NOT THIS LANE, but required for the integrated manuscript to be
%     internally consistent with Definition def:D3P3.  Lane F-1 owns the
%     Littlewood--Paley paragraph at main.tex lines 256--262, which
%     still writes u\cdot\nabla|u|.  The minimal patch, stated here so
%     that no lane has to guess it:
% =====================================================================
\[
 P_3=L_J+Q_J,
 \quad L_J=\int_{\R^3} p_{\leq J}\,\Theta(u,\nabla u)\,dx,
 \quad Q_J=\int_{\R^3} p_{>J}\,\Theta(u,\nabla u)\,dx,
\]
% with the bound used in prop:lowpressure obtained from
% Lemma lem:psi-theta(ii) and Cauchy--Schwarz:
% \norm{\Theta(u,\nabla u)}_1 \leq \norm{u}_2\norm{\nabla u}_2 .
```

With (a)–(d) applied, the candidate's block discharges P-0, P-1, P-2, P-3 and
`eq:pressure-consequence` at the D5 standard, and is self-contained: no
statement in it rests on an evidence file, and every external fact carries a
primary source with a `[DI]` or `[MO]` label recorded in §7 below.

## 6. UNNECESSARY DEPENDENCIES

1. **Lemma `lem:embedding` is not needed by this lane.** D2 hands the lane
   `u,p ∈ C([0,T];L^q)` for all `2 ≤ q ≤ ∞` directly, and the candidate's own
   `(R3)` says so; the lemma is used nowhere except to "record, for
   completeness", the route from `(R1)`. Its constant `π` is used nowhere. The
   sibling lane `cp02-energy-enstrophy.md` also proves the interpolation
   (`lem:interp`). Drop `lem:embedding`, and with it external facts 6, 7 and 12
   of the candidate's table (Plancherel inversion and the `π^2` weight
   integral); Plancherel is still needed, once, for the `‖m‖_∞` multiplier
   bound in `lem:pressure-convention`.
2. **Lemma `lem:divergence` duplicates the sibling lane's `lem:div-zero`.**
   Only one may survive integration. `lem:div-zero` (`g ∈ C^1` with
   `g,∂_ig ∈ L^1` ⟹ `∫∂_ig = 0`) is the stronger statement and already covers
   every integration by parts of this lane, since each of this lane's `f` has
   compact support. Recommendation: keep `lem:div-zero`, delete
   `lem:divergence`, and rewrite this lane's Step 4 to invoke it.
3. **`(R3)` is over-declared.** The proof uses `u ∈ C([0,T];L^q)` only for
   `q ∈ {2,3,4,∞}`, `∇u ∈ C([0,T];L^2)`, `p ∈ C([0,T];L^2∩L^\infty)`. The
   memberships `∂_tu, Δu, ∇p ∈ C([0,T];L^q)` are never used in `L^q` form —
   only pointwise, via `(R2)`. Narrowing `(R3)` makes the dependence on
   `prop:localtheory` visibly smaller and removes an interface the local-theory
   lane would otherwise have to guarantee.
4. **`lem:psi-theta`(iv)'s monotonicity clause** ("the first one increasingly")
   is unused: the proof uses dominated, never monotone, convergence. Harmless;
   may stay as documentation.
5. **Remark `rem:lean-majorant`** is not needed for any statement and points at
   a repository with no bibliographic record. Its content was verified accurate,
   but the sibling lane carries a second such remark (`rem:lean`); at most one
   should reach the manuscript, and it needs a citable record.
6. `K_∞` is used only through `D_3(t) ≤ 2K_∞G^2` in `prop:pressure`(i) and the
   Step 5(b) majorant, and `Π_∞` only through `|P_3| ≤ Π_∞K_2G`; both are
   genuinely used. No further pruning found: `K_2, K_3, K_4, G, Π_2` all appear
   in `C_E`.

## 7. MINOR EDITORIAL ISSUES FOR THE INTEGRATOR

1. **Two `\cite` page numbers are wrong** (see §3): `p.~37 → p.~35`,
   `p.~38 → p.~36` for the `H^s` clause. The sibling lane
   `cp02-energy-enstrophy.md` cites the *arXiv* pages (`p.~14`, `p.~15`) for
   the same two facts; since `references.bib`'s `Tao2013` is the APDE article
   (`pages = {25--107}`), **both** lanes must use the printed pages 35 and 36.
   Fix in one place, since the Conventions paragraphs of the two lanes should be
   merged anyway (item 2).
2. **The three new bib keys must be verified.** The theorem numbers used in §5
   (`RudinRCA` Thm 1.34, 1.26, 8.8; `RudinPMA` Thm 5.10, 6.21; `SteinWeiss1971`
   Ch. I Thm 1.9, 2.1, Cor. 2.2, 2.3) were **not** checked against the printed
   books in this lane either, and the candidate says as much. They remain
   `[MO]`. Either confirm them, or cite by chapter/section only (which is
   enough for D5, since D5 asks for a primary source and a status label, not a
   theorem number).
3. **Duplication with the sibling lane.** `cp02-energy-enstrophy.md` already
   supplies: the Fourier convention, the `H^k` definition, the tensor norms, the
   cutoff `χ_R` (there defined once and for all, with the same
   `‖∇χ_R‖_∞ = R^{-1}‖∇χ‖_∞`), the statement of the regularity package, and
   `\newtheorem{lemma}`/`{definition}`. This lane redefines all of them, and
   builds its own `χ` from a radial profile `η`. The integrator must keep one
   Conventions subsection (the earlier one), one `χ_R`, one regularity-package
   paragraph, and add only `\newtheorem{corollary}[theorem]{Corollary}` beyond
   the sibling's two lines. This lane's Step 2 then reduces to "fix
   `ε ∈ (0,1]`".
4. **Interface break with lane F-1 (blocking for the integrated file).**
   `main.tex` lines 260–262 still define `L_J`, `Q_J` through `u·∇|u|`. After
   `def:D3P3`, `P_3 = L_J + Q_J` is not a tautology unless those two displays
   are rewritten with `Θ(u,∇u)`. The exact patch is in §5(e). Until it lands,
   the integrated manuscript both contains `∇|u|` (against P-0) and has an
   unproved splitting.
5. **Notation collision `Θ` vs `θ`.** `hyp:absorption` and
   `hyp:highpressure` use `θ ∈ [0,1)`; this lane introduces `Θ(a,G)`, and its
   proofs additionally use `ϑ` (in `lem:embedding` and
   `lem:diff-under-integral`). Three thetas in one section. Rename the
   integrand, e.g. `W(a,\mathsf G)` (for the pressure *work* density) and
   `S(a,\mathsf G)` for `Ψ`, or at least replace `\vartheta` by `σ` and `r`.
6. `\subsection*{...}` appears nowhere else in `main.tex`; if the sibling lane's
   block is accepted the style is already introduced, otherwise the four
   starred subsections in this lane are a new sectioning level. Harmless but
   should be uniform.
7. The candidate's fact table row 5 gives "Tao, APDE p. 5, eq. (9)"; the article
   occupies pp. 25–107, and (9) is on p. 28. Table-only error, but it should be
   corrected in the evidence file so a later lane does not inherit it.
8. `\eqref{eq:constants}` is referenced as "the constants of \eqref{eq:constants}";
   an `\eqref` to a display of definitions reads oddly. Prefer a named display or
   plain "(4.1)".
9. The unlabeled `\begin{remark}[Relation to the earlier formulation]` should
   get a label (e.g. `rem:old-form`) so that the proof-boundary section can
   point at it.
10. `prop:pressure`(i) states four distinct facts (continuity, sign, two bounds,
    measurability); splitting off the two bounds as a displayed equation would
    let `hyp:highpressure`'s "`|Q_0| ≤ C‖u‖_6^3‖∇u‖_2`" paragraph cite them.
11. Remark `rem:differential-form`'s sketch is sound as far as it goes (a
    generalised dominated convergence / Vitali argument with the `L^1`-convergent
    majorants `2‖u(t_n)‖_∞|∇u(t_n)|^2` and a.e.-convergent subsequences drawn
    from `L^2` convergence, plus the subsequence principle for continuity), but
    it should say explicitly that the subsequence principle is what turns
    subsequential convergence into continuity; as written a reader may think a
    gap is being hidden. The remark correctly does not claim the result.
12. The section-opening sentence of `main.tex` line 199 (`\section{A signed
    critical balance}`) is retained; the abstract (lines 21–33) still advertises
    only "energy, scaling, interpolation, and enstrophy estimates" and does not
    mention the pressure balance. Controller item, not this lane's.

## 8. CONDITIONAL SUFFIX THAT SURVIVES

Unchanged by this review, and now resting on a verified proof:

* `prop:pressure` (integrated form) and `cor:absorption-consequence` give
  `hyp:absorption ⟹ hyp:critical` with `M = (‖u_0‖_3^3+3A(ν,u_0,H))^{1/3}`,
  unconditionally on the classical Schwartz branch of `prop:localtheory`, for
  arbitrary `ν>0`, unforced, on `R^3`.
* Therefore the surviving suffix of the whole programme is unchanged:
  `hyp:highpressure` (plus the proved `prop:lowpressure`) `⟹ hyp:absorption`
  `⟹ hyp:critical` `⟹ def:target` via `thm:continuation` and
  `thm:conditional`. The first unproved link remains `hyp:highpressure`.
* Nothing in this lane, and nothing in this review, bears on the truth of
  `hyp:highpressure`, `hyp:absorption` or `hyp:critical`.

## 9. NON-CLAIMS

* No HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION or NS-R3 result is
  asserted, approached, or made more likely by this review.
* `hyp:highpressure`, `hyp:absorption` and `hyp:critical` remain hypotheses.
* The differential form `X'/3 + νD_3 = P_3` is not claimed; continuity of
  `t ↦ D_3(t)`, `P_3(t)` is not proved here either.
* The three `[MO]` textbook sources were not opened in this lane; the theorem
  numbers proposed in §5 are `[MO]` and are flagged as such.
* Tao's Lemma 4.1 (which is what makes the normalised pressure "essentially
  automatic" for smooth finite-energy solutions on `R^3`) was **not** read in
  this lane; only (8), (9) and the remark after (9) on p. 28 were read. The
  audit does not need it, because the regularity of `p` is taken from
  `prop:localtheory` (D2), not from Lemma 4.1.
* No `L^p` bound for the Riesz transforms, no Calderón–Zygmund theory, no
  Rademacher theorem and no `W^{1,1}` chain rule is used anywhere in the
  candidate or in this repair; this was checked line by line.

## 10. REOPENING CONDITION

Reopen this audit if any of the following changes:

1. `prop:localtheory` as finally written by the local-theory lane does **not**
   deliver, for every `T < T_*`: `u ∈ C^∞([0,T]×R^3)` with `eq:NS` pointwise and
   `u(0) = u_0`; `u ∈ C([0,T];L^q)` for `q ∈ {2,3,4,∞}`;
   `∇u ∈ C([0,T];L^2)`; and, for the normalised pressure,
   `p ∈ C^∞([0,T]×R^3) ∩ C([0,T];L^2∩L^∞)`. These, and nothing more, are what
   the candidate's proof consumes.
2. The definition of `p` in the manuscript changes away from
   `p = R_iR_j(u_iu_j)`, or the Fourier convention of D1 changes (the symbol
   computation of `lem:pressure-convention`, and only it, is convention-bound).
3. Lane F-1 does not rewrite `L_J`, `Q_J` with `Θ(u,∇u)` (§5(e)), or rewrites
   them with a different normalisation of `Θ`.
4. `hyp:absorption` is restated with a different `τ`-range, a `θ`-dependent
   `A`, or `D_3` replaced by another weighted dissipation: the corollary's
   arithmetic is tied to `eq:absorption` exactly as it stands at `main.tex`
   line 311.
5. `def:D3P3` is changed so that `Ψ` or `Θ` is no longer the continuous
   extension by `0` across `{u=0}`: every measurability statement in
   `prop:pressure`(i) rests on that continuity, and nothing else.

## 11. External facts used by THIS REVIEW

| # | Fact, as used here | Source | Status |
|---|---|---|---|
| 1 | Fourier transform `f̂(ξ)=∫e^{−2πix·ξ}f(x)dx` for `f ∈ L^1_x(R^3)`, "we then extend this Fourier transform to tempered distributions in the usual manner" | Tao, APDE 6 (2013) 25–107, printed **p. 35** | **[DI]** (publisher PDF read as text in this lane) |
| 2 | `‖u‖_{H^s_x(R^3)} := (∫(1+|ξ|^2)^s|û(ξ)|^2 dξ)^{1/2}`; `H^s_x(R^3)` is the space of tempered distributions with finite norm; the classical `H^k` norm "conflicts slightly … but the two norms are equivalent up to constants" | Tao, printed **p. 36** | **[DI]** |
| 3 | `C^k_x`, mixed norms, `X^s(I×Ω) := L^∞_tH^s_x ∩ L^2_xH^{s+1}_x` (13) — the page the candidate mis-cited for facts 1–2 | Tao, printed **p. 37** | **[DI]** |
| 4 | `\widehat{Δ^{-1}f}(ξ) := −(4π^2|ξ|^2)^{-1}\hat f(ξ)` (14), "well-defined for any tempered distribution `f` … for which the right-hand side of (14) is locally integrable … the `k`-th derivative of a function in `L^2_x(R^3)` for some `k ≥ 1`"; and the vector/tensor extension of the function spaces | Tao, printed **p. 38** | **[DI]** |
| 5 | `Δp = −∂_i∂_j(u_iu_j) + ∇·f` (8) and `p = −Δ^{-1}∂_i∂_j(u_iu_j) + Δ^{-1}∇·f` (9), introduced for periodic smooth solutions, with the remark that the normalisation "can also be imposed for smooth finite energy solutions (because `∂_i∂_j(u_iu_j)` is a second derivative of an `L^1_x(R^3)` function) … see Lemma 4.1" | Tao, printed **p. 28** | **[DI]** |
| 6 | Tao Theorem 5.4(iv) and Corollary 5.8 (the literature inputs behind `prop:localtheory`) | `cp01-literature-statements.md` §1.2–1.3, quoting APDE pp. 52–53, 56–57 | **[DI] there**, not re-opened here |
| 7 | `R_iR_j = ∂_i∂_j(−Δ)^{-1} = −Δ^{-1}∂_i∂_j`; identity of `main.tex`'s `p` with Tao's normalised pressure; no sign error | `cp01-literature-statements.md` §7.3 | **[DI] there** |
| 8 | Hölder / Cauchy–Schwarz on `L^p(R^3)` | `cp01-literature-statements.md` §6, S10 | **[DI] there** |
| 9 | `abs_HEps_le_two : 0 ≤ ε → ε ≤ 1 → |HEps ε v| ≤ 2*(‖v‖^2+‖v‖^3)`, plus `rEps_le_norm_add_sqrt`, `HEps_le_norm_sq_mul_rEps`, `tendsto_HEps`, `hasFDerivAt_HEps`, stated "for a general real inner product space `E`" | `/home/ert/proj/navier-formal/NavierFormal/Regularization.lean`, lines 1–38, 94, 141, 177, 202, 260 | **[DI]** (file read in this lane) |
| 10 | `hyp:absorption` (`eq:absorption`), `hyp:critical` (`eq:missing`), `eq:pressure-consequence`, the `M` formula, `L_J`/`Q_J` | `/home/ert/proj/navier-paper/main.tex` lines 199–353, 393–409 | **[DI]** |
| 11 | Plancherel; `L^2` Fourier inversion; DCT, MCT, Tonelli/Fubini; MVT, FTC for `C^1` | Stein–Weiss 1971 Ch. I; Rudin, *RCA* 3rd ed.; Rudin, *PMA* 3rd ed. | **[MO]** — theorem numbers proposed in §5 are unverified |
| 12 | `∫_0^∞ r^2(1+r^2)^{-2}dr = π/4`, hence `∫_{R^3}(1+|ξ|^2)^{-2}dξ = π^2` | recomputed inline (`r = tan ϑ`) | proved here |

## 12. Frontier record

**MODE / RESULT.** REVIEW — complete, round 1, verdict **REPAIR**. The
candidate's proof of `prop:pressure` in integrated form and of
`cor:absorption-consequence` is mathematically correct: every identity, sign,
constant and exponent was independently rederived and confirmed, and six
refutation attempts (two with explicit test data) failed. Two source-layer
defects and one cross-lane interface break must be fixed before integration;
the complete repair is supplied in §5 and is purely editorial in its
mathematical content.

**CLAIM AND SCOPE.** For the classical Schwartz-data branch of
`prop:localtheory` on `R^3`, unforced, arbitrary `ν>0`, with
`p = R_iR_j(u_iu_j) = −Δ^{-1}∂_i∂_j(u_iu_j)` under
`f̂(ξ)=∫e^{−2πix·ξ}f`: the identity
`X(t)/3 − X(s)/3 + ν∫_s^t D_3 = ∫_s^t P_3` for all `0 ≤ s ≤ t < T_*`, with
`D_3`, `P_3` defined through the continuous extensions `Ψ`, `Θ` of
`|(∇u)^Tu|^2/|u|` and `u·(∇u)^Tu/|u|`, together with `D_3 ≥ 0`,
`D_3 ≤ 2∫|u||∇u|^2`, `|P_3| ≤ ‖p‖_∞‖u‖_2‖∇u‖_2`, `∫Θ(u,∇u)dx = 0`, and
`hyp:absorption ⟹ hyp:critical` with `M = (‖u_0‖_3^3+3A)^{1/3}`, is **verified**
at this lane's standard of proof. This review asserts nothing beyond that
verification.

**EVIDENCE.** §4: independent rederivation (§2.1), six failed refutations
(§2.2), and re-inspection of the primary source in this lane — Tao, APDE 6
(2013), printed pp. 28, 35, 36, 37, 38 — which confirms the content of all four
of the candidate's `[DI]` Tao facts and refutes two of its page locations.
Lean cross-check of `rem:lean-majorant` against
`NavierFormal/Regularization.lean`. Verbatim comparison with `main.tex`
lines 199–353, 393–409 and with `cp02-energy-enstrophy.md`.

**FIRST GAP.** No gap inside the reviewed scope. The first defective element is
the citation layer of `\subsection*{Conventions}`: `\cite[p.~37]{Tao2013}` and
`\cite[p.~38]{Tao2013}` name the wrong printed pages (correct: 35 and 36), and
the eleven uses of Plancherel / inversion / DCT / Tonelli–Fubini / MVT / FTC
carry no citation at all, although the candidate's placement note promises
three new bib keys that the block never uses. Behind that, outside this lane:
lane F-1's `L_J`, `Q_J` are still written with `u·∇|u|`, so `P_3 = L_J + Q_J`
does not yet hold for the `P_3` this lane defines.

**SURVIVING CONDITIONAL SUFFIX.** `hyp:highpressure` (with the proved
`prop:lowpressure`) `⟹ hyp:absorption` `⟹ hyp:critical` `⟹ def:target`. The
middle implication is now audited and complete. The first link is untouched and
remains the frontier.

**NON-CLAIMS.** §9. In particular: no HIGH-PRESSURE, HIGH-STRAIN, CRITICAL,
ABSORPTION or NS-R3 result is asserted; the differential form of the balance is
not claimed; the `[MO]` textbook theorem numbers are unverified; Tao's
Lemma 4.1 was not read.

**NEXT DISTINCT ACTION.** Apply §5(a)–(d) to `cp02-pressure.md` (author lane,
round 2), and hand §5(e) plus §7 item 3 to the F-1 and integration lanes; then
a single merged Conventions/regularity paragraph shared by
`cp02-energy-enstrophy.md` and `cp02-pressure.md`, with the Tao pages fixed to
35/36 in one place. Independently: open Stein–Weiss and the two Rudin volumes
to promote fact 11 of §11 from `[MO]` to `[DI]`, or downgrade the citations to
chapter level.
