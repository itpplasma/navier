# CP01: manuscript proof-obligation audit for checkpoint CP1

MODE: REVIEW (proof-audit / math-frontier discipline). Standard: complete,
self-contained, referee-proof paper proof of CP1, followed by Lean
formalization. Date: 2026-09-05.

Reviewed inputs (all directly inspected unless marked):

- Manuscript `../navier-paper/main.tex` at HEAD `1ad73c2` (562
  lines, read in full). The graph's recorded `manuscript_commit: d84950b…`
  resolves as a commit object in that repository but is not HEAD; the
  quotient section postdates it.
- `../navier/PLAN.md` (the CP1 definition and wave table were
  updated on disk during this audit; the version with `checkpoint: CP1` and
  the CP01–CP07 wave table is the one compared against),
  `docs/proof-graph.yaml`, `docs/proof.md`.
- `literature/foundations.md`, `literature/critical-criteria.md`,
  `research/evidence/review-{estimates,pressure,frequency,integration}.md`,
  `hf03-review-paper.md`, `hf17-quotient-functional.md`,
  `hf17-review-quotient-functional.md`, `hf17-quotient-evolution.md`,
  `hf17-review-quotient-evolution.md`.
- Primary sources, directly inspected through text extraction of the arXiv
  PDFs (page numbers are the arXiv PDF page numbers):
  - Tao, *Localisation and compactness properties of the Navier–Stokes global
    regularity problem*, arXiv:1108.1165v4 (Anal. PDE 6 (2013) 25–107):
    definitions of smooth/finite-energy/H¹ solutions (p. 3), viscosity
    normalisation ν = 1 (footnote 3, p. 4), normalised pressure (9) (p. 5),
    H¹ mild solution definition (p. 9), non-preservation of the Schwartz
    property (p. 7), Theorem 1.12 (p. 7), Sobolev/X^s conventions (13) and
    Fourier convention (pp. 14–16), inverse Laplacian (14) and Leray
    projection (p. 17–18), Corollary 4.3 (p. 28), Theorem 5.1 and
    Corollary 5.2 (periodic, pp. 28–31), **Theorem 5.4 (pp. 33–34)** with
    its proof and the remark after it, Lemma 5.5 and Proposition 5.6
    (pp. 34–36).
  - Gallagher–Koch–Planchon, arXiv:1012.0145v3 (Math. Ann. 355 (2013)):
    equation (0.1) with unit viscosity (p. 1), definition of NS(u₀), the
    Duhamel/Leray-projection sense, E_{p,q}(T), T*(u₀), and the L³ remarks
    (p. 5), **Theorem 4 and the L_{3,∞} remark (p. 18)**, Theorems 5–8
    (pp. 19–20).
  - Fefferman's Clay statement: **metadata-only here** (not reopened in this
    audit); the exact text is taken from `literature/foundations.md`, which
    records direct inspection of PDF pages 63–64 of the Clay volume.
- Mathlib: local checkout `../stafford38/.lake/packages/mathlib`
  at `0df444a` (2026-08-21, toolchain `leanprover/lean4:v4.33.1`), grepped
  only, not built. Coverage statements below are grep-level, not
  type-checked.

No file other than this one was written. Nothing here proves or claims
HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, or NS-R3.

---

## 0. What the two imported theorems actually say

These are the exact statements the paper may import. Anything beyond them is
a project obligation.

### 0.1 Tao 2013, Theorem 5.4 (directly inspected, pp. 33–34)

Setting: ν = 1 (footnote 3, p. 4). "H¹ data" (u₀,f,T): u₀ ∈ H¹_x(ℝ³)
divergence-free, f ∈ L^∞_t H¹_x([0,T]×ℝ³), 0<T<∞. An "H¹ mild solution"
(u,p,u₀,f,T) (p. 9): u ∈ L^∞_t H¹_x ∩ L²_t H²_x([0,T]×ℝ³), divergence-free,
with p given by the normalised pressure (9)
p = −Δ⁻¹∂_i∂_j(u_iu_j) + Δ⁻¹∇·f, obeying the Duhamel formula (10)/(11).
Here Δ⁻¹ is the Fourier multiplier −1/(4π²|ξ|²) with Tao's convention
f̂(ξ)=∫e^{−2πix·ξ}f (p. 14, (14)).

Theorem 5.4. Let (u₀,f,T) be H¹ data.
(i) Every H¹ mild solution has u ∈ C⁰_t H¹_x([0,T]×ℝ³).
(ii) If (‖u₀‖_{H¹} + ‖f‖_{L¹_tH¹_x})⁴ T ≤ c (absolute c>0), there is an H¹
mild solution with ‖u‖_{X¹} ≲ ‖u₀‖_{H¹}+‖f‖_{L¹_tH¹_x}, and, for each k ≥ 1,
‖u‖_{X^k([0,T]×ℝ³)} ≲_{k,‖u₀‖_{H^k},‖f‖_{L¹_tH^k}} 1, where
X^s = L^∞_t H^s_x ∩ L²_t H^{s+1}_x (13). "In particular, one has local
existence whenever T is sufficiently small depending on H1(u₀,f,T)."
(iii) There is at most one H¹ mild solution with the given data.
(iv) If (u,p,u₀,f,T) is an H¹ mild solution and (u₀,f,T) is Schwartz, then
u and p are smooth; in fact ∂_t^j u, ∂_t^j p ∈ L^∞_t H^k([0,T]×ℝ³) for all
j,k ≥ 0. (Remark after the proof: it suffices that u₀ ∈ H^k for all k and
f ∈ C^j_tH^k_x.)
(v) Lipschitz stability (not used).

What Theorem 5.4 does **not** state: (a) an ℝ³ maximal Cauchy development
(Corollary 5.2 on p. 31 is stated for the periodic case only; the sentence
"A similar statement holds …" there concerns smooth periodic data); (b) that
∂_t^j u ∈ C_t H^k (only L^∞_t); (c) any L³-based uniqueness; (d) preservation
of Schwartz decay — the paper explicitly says the Schwartz property "need not
be preserved over time" (p. 7); (e) any statement with ν ≠ 1.

Corollary 4.3 (p. 28, directly inspected): an almost smooth H¹ solution
(u,p,u₀,f,T) becomes an H¹ mild solution after replacing p by the normalised
pressure p̃, and ∇p = ∇p̃ for a.e. t. This is the bridge from "classical
solution with some pressure" to Tao's uniqueness class.

Consequences the manuscript may derive but must write out (obligation L-1
below): with u₀ Schwartz and f = 0, for every k the datum is H^k; (ii)
gives a solution on [0,T₁] with T₁ ≳ ‖u₀‖_{H¹}^{−4}; restart from u(T₁) ∈ H¹
(by (i)); define T_* = sup{T : an H¹ mild solution exists on [0,T]}; (iii)
glues the pieces into a single H¹ mild solution on every [0,T], T<T_*;
(iv) applied on each [0,T] gives u,p ∈ C^∞([0,T]×ℝ³) with all
∂_t^j u, ∂_t^j p ∈ L^∞_t H^k; and if T_* < ∞ then limsup_{t↑T_*}‖u(t)‖_{H¹} =
∞ (otherwise (ii) restarts past T_*). Uniqueness of "the classical solution"
means: uniqueness among solutions that are H¹ mild in Tao's sense, i.e.
among classical solutions with u ∈ L^∞_tH¹ ∩ L²_tH² and normalised pressure
(Corollary 4.3 supplies the pressure normalisation).

### 0.2 Gallagher–Koch–Planchon 2013, Theorem 4 (directly inspected, p. 18)

Setting (p. 1, (0.1)): ∂_t u = Δu − ∇·(u⊗u) − ∇π, ∇·u = 0, unit viscosity.
For u₀ ∈ Ḃ^{s_p}_{p,q}(ℝ^d), d<p≤q<∞, s_p = −1+d/p, NS(u₀) denotes "the
local in time strong solution", meaning a divergence-free solution of
u_t = Δu − ℙ∇·(u⊗u), u|_{t=0}=u₀ "in the Duhamel sense" (p. 5). NS(u₀)
belongs to E_{p,q}(T) = L^∞([0,T];Ḃ^{s_p}_{p,q}) ∩ L^{2p/(p+1)}([0,T];
Ḃ^{s_p+1+1/p}_{p,q}) for T<T*, and T* = T*(u₀) is the maximal such time. The
L³ case: "The specific case of L^d data is included in such a result, as
any additional 'regularity' is propagated along the flow (see [9])", and "if
NS(u₀) belongs to E_{p,q}(T) and u₀ belongs to … L^d(ℝ^d) … then NS(u₀)
belongs to … C([0,T];L^d(ℝ^d)) with the same life span (see [9] for
instance, or [1])". Reference [9] is Gallagher–Iftimie–Planchon (Ann. Inst.
Fourier 2003) — not inspected in this audit.

Theorem 4 (Endpoint regularity criterion). For any u₀ ∈ L³(ℝ³),
sup_{t∈[0,T*(u₀))} ‖NS(u₀)(t)‖_{L³(ℝ³)} < ∞ ⟹ T*(u₀) = +∞.
Remark (p. 18): by time-continuity in L³ of strong solutions, the left side
is equivalent to NS(u₀) ∈ L^∞((0,T*);L³), "or in the notation of [8],
NS(u₀) ∈ L_{3,∞}(0,T*)".

What Theorem 4 does **not** state: (a) any uniqueness theorem (uniqueness of
NS(u₀) is implicit in "the" strong solution and rests on the contraction
argument of [5],[22],[9], which GKP cite but do not restate); (b) that
T*(u₀) coincides with the H¹ blow-up time of a Schwartz-data classical
solution; (c) smoothness of NS(u₀) for t>0; (d) any statement for ν ≠ 1.
Items (a)–(b) are project obligations (C-2 below) that the manuscript
currently discharges in one sentence.

### 0.3 Clay alternative (A) (metadata-only for this audit; text from
`literature/foundations.md`)

Data: u₀ smooth, divergence-free, with |∂^α_x u₀(x)| ≤ C_{αK}(1+|x|)^{−K}
for all α, K (this is exactly the Schwartz class). Force f ≡ 0. Required:
p,u ∈ C^∞(ℝ³×[0,∞)) and ∫|u(x,t)|²dx < C for all t ≥ 0 (one constant C).
The manuscript's `def:target` states precisely this (sup_t ∫|u|² < ∞ is the
same as a single C). Match: PASS.

---

## 1. Result-by-result audit

Classification key: **proved** (complete on the page, modulo named standard
inequalities); **sketched** (idea given; a nontrivial estimate, limit, or
justification must be written); **asserted** (no argument); **delegated**
(to literature; the exact cited statement is named, and whether it covers
the use is stated).

### 1.1 `premise:local` (unlabelled theorem-like paragraph, §1)

Claims: (a) unique maximal classical solution on [0,T_*), 0<T_*≤∞;
(b) for Schwartz data u and p are smooth through t=0 by Tao 5.4;
(c) "Persistence of higher Sobolev regularity and uniqueness identify this
branch with the maximal mild solutions used in the continuation theorem".

| Step | Class | Obligation |
| --- | --- | --- |
| Local existence, uniqueness in H¹ mild class | delegated: Tao 5.4(ii),(iii); covers the use after ν-normalisation (eq:nu-normalization is introduced only in §5; it must be invoked here) | L-1 |
| Maximal development T_* on ℝ³ | delegated but **not covered**: Tao states Corollary 5.2 for the periodic case only | L-1 (blocking) |
| "Classical" = smooth through t=0 | delegated: Tao 5.4(iv) covers it on each [0,T], T<T_*, given (u,p) is an H¹ mild solution on [0,T] | L-2 |
| Uniqueness class of "the classical solution" | asserted; needs Corollary 4.3 to put any classical H¹ solution into the mild class | L-1 |
| Identification with GKP's NS(u₀) | asserted here, sketched in thm:continuation | C-2 |

### 1.2 `def:target` (Theorem [Target])

Statement only; correctly not claimed. Matches Clay (A) (§0.3). For Lean it
is the terminal statement NS-R3; no obligation except to keep "u,p ∈
C^∞(ℝ³×[0,∞))" and the single energy constant explicit.

### 1.3 `prop:energy`

| Step | Class | Obligation |
| --- | --- | --- |
| d/dt ½‖u‖₂² = ∫u·u_t | sketched: needs u ∈ C¹([0,T];L²), which follows from Tao (iv) (∂_t u, ∂_t²u ∈ L^∞_tH^k ⇒ u ∈ C¹_tH^k) | E-1 |
| ∫u·Δu = −‖∇u‖₂² | sketched ("radial cutoff"): for u(t) ∈ H² no cutoff is needed — density of C_c^∞ in H² or Plancherel | E-1 |
| ∫u·(u·∇)u = 0 | sketched: u ∈ H² ⊂ L^∞(ℝ³), so u_j|u|² ∈ W^{1,1} and ∫∂_j(·)=0 by density; uses div u = 0 | E-1 |
| ∫u·∇p = 0 | sketched: needs p ∈ H¹ (Tao (iv) gives p ∈ H^k) | E-1 |
| Integration in time | proved once the derivative identity holds pointwise and the right side is continuous in t (∇u ∈ C_tL²) | E-1 |

Verdict: correct; a complete proof is a half page using only Tao (iv) and
density. The phrase "strong-solution Sobolev bounds" must be replaced by the
exact memberships used (u ∈ C¹_tH^k, p ∈ C_tH^k for a stated k).

### 1.4 `prop:scaling`

| Step | Class | Obligation |
| --- | --- | --- |
| Scaling invariance of the system | proved (chain rule) | none |
| ‖u_λ(t)‖_q = λ^{1−3/q}‖u(λ²t)‖_q | proved | none |
| ‖u‖₃ ≤ ‖u‖₂^{1/2}‖u‖₆^{1/2} | proved (Hölder) | none |
| ‖u‖₆ ≤ C‖∇u‖₂ | delegated to "the Sobolev inequality" (standard; needs the H¹ version, i.e. density extension of the C¹_c inequality) | S-1 |
| eq:L4L3 | proved from the above | none |
| "they do not imply u ∈ L^∞(0,T;L³)" and "no deduction … can be" | asserted meta-statement, not a mathematical proposition | S-2 (minor: reformulate or delete from the proposition statement) |

### 1.5 `prop:enstrophy`

| Step | Class | Obligation |
| --- | --- | --- |
| ½Y' + ν‖Δu‖₂² = ∫(u·∇)u·Δu | sketched: needs u ∈ C¹_tH², integration by parts ∫∇u:∇u_t = −∫u_t·Δu (u ∈ H², u_t ∈ H¹ ⊂ L²), and ∫∇p·Δu = −∫p Δ(div u) = 0 (p ∈ H¹, Δu ∈ H¹) | N-1 |
| ‖u‖₆ ≤ C‖∇u‖₂ | delegated (Sobolev) | S-1 |
| ‖∇u‖₃ ≤ C‖∇u‖₂^{1/2}‖Δu‖₂^{1/2} | delegated without source; provable as ‖∇u‖₃ ≤ ‖∇u‖₂^{1/2}‖∇u‖₆^{1/2} ≤ C‖∇u‖₂^{1/2}‖∇²u‖₂^{1/2} and ‖∇²u‖₂ = ‖Δu‖₂ by Plancherel for u ∈ H² | N-1 |
| Hölder with 1/6+1/3+1/2 = 1 and Young (4/3, 4) | proved (exponents checked: CY^{3/4}‖Δu‖^{3/2} ≤ (ν/2)‖Δu‖² + Cν^{−3}Y³) | none |

Verdict: correct; the constant path is standard. Not used in the
conditional chain (review-integration.md already notes this).

### 1.6 `prop:ode`

Proved in full (y' = Cy³ and ∫₀^T y = √(2T/C) both rechecked). No
obligation.

### 1.7 `prop:pressure` (special attention item 1)

Statement issues first:

- D₃ contains |∇|u||. For smooth u, |u| is locally Lipschitz, so ∇|u| exists
  a.e. (Rademacher) and equals (∇u)ᵀu/|u| on {u≠0}; the manuscript's
  sentence "∇|u| = 0 a.e. on the zero set of its Sobolev representative" is
  the standard W^{1,1}_loc fact (e.g. Gilbarg–Trudinger Lemma 7.7; not
  cited). **Recommendation P-0:** avoid ∇|u| altogether. Define pointwise
  D₃ = ∫(|u||∇u|² + |(∇u)ᵀu|²/|u|) and P₃ = ∫_{u≠0} p (u⊗u):∇u/|u|, with
  both integrands defined as 0 where u = 0. These are the quantities that
  actually arise from ∇r_ε = (∇u)ᵀu/r_ε, are manifestly measurable, and
  make the "zero at u=0" convention a definition rather than an a.e. claim.
  With this definition |(∇u)ᵀu|²/|u| ≤ |u||∇u|² pointwise, which is all the
  domination that is used.

Proof steps:

| Step | Class | Obligation |
| --- | --- | --- |
| Regularity used: "u ∈ L²∩L⁶, ∇u ∈ L², p = R_iR_j(u_iu_j) ∈ L²∩L³" on compact intervals | sketched; the source of p ∈ L²∩L³ is not named (Calderón–Zygmund is implicit). Cleaner: Tao (iv) gives p ∈ L^∞_tH^k, hence p ∈ L²∩L^∞ ⊂ L²∩L³, **provided** the manuscript's p = R_iR_j(u_iu_j) is shown to equal Tao's p = −Δ⁻¹∂_i∂_j(u_iu_j) (same L² multiplier −ξ_iξ_j/|ξ|² under Tao's convention with R̂_i = −iξ_i/|ξ|; this must be stated with the convention fixed) | P-1 |
| Time derivative under the integral: d/dt ∫χ_R H_ε(u) = ∫χ_R r_ε u·u_t | sketched: needs u ∈ C¹_tL⁴ ∩ C¹_tL² (so r_ε u·u_t ≤ (|u|²+ε^{1/2}|u|)|u_t| ∈ L¹ uniformly in t) and the majorant H_ε(u) ≤ C(|u|²+|u|³), uniform in ε ≤ 1 (verified: (a+ε)^{3/2}−ε^{3/2} ≤ (3/2)(a+1)^{1/2}a) | P-2 |
| Convection: ∫χ_R (u·∇)u·r_εu = −∫H_ε(u)u·∇χ_R | sketched; needs H_ε(u)u ∈ W^{1,1} (true: u bounded, u ∈ L²∩L³, ∇u ∈ L²), div u = 0; cutoff error ≤ (C/R)∫(|u|³+|u|⁴) → 0 | P-2 |
| Diffusion: −ν∫χ_RΔu·r_εu = ν∫χ_R(r_ε|∇u|² + |(∇u)ᵀu|²/r_ε) + ν∫(∇χ_R⊗r_εu):∇u | sketched; formula rechecked; cutoff error ≤ (C/R)∫(|u|²+ε^{1/2}|u|)|∇u| → 0 | P-2 |
| Pressure: ∫χ_R∇p·r_εu = −∫χ_R p (u·∇u·u)/r_ε − ∫p r_ε u·∇χ_R | sketched; rechecked; cutoff error needs p|u|², p|u| ∈ L¹ (p ∈ L², u ∈ L²∩L⁴) | P-2 |
| R → ∞ | sketched ("R^{−1} factors and integrable tails"); each error term must be displayed | P-2 |
| ε ↓ 0 | sketched: r_ε|∇u|² ↓ |u||∇u|² and |(∇u)ᵀu|²/r_ε ↑ |(∇u)ᵀu|²/|u| dominated by (‖u‖_∞+1)|∇u|²; pressure integrand dominated by |p||u||∇u|; time primitive by C(|u|²+|u|³) | P-2 |
| Passage from integrated identity to X'(t) pointwise | asserted. The argument yields the integrated form X(t)/3 − X(s)/3 + ν∫_s^tD₃ = ∫_s^tP₃. Pointwise X' requires continuity of t ↦ D₃(t), P₃(t) (true via u ∈ C_t(L^∞∩H¹), p ∈ C_tL², and Vitali for the nonlinear integrand). **Recommendation:** state the proposition in integrated form; that is all `eq:pressure-consequence` uses | P-3 |
| P₃ unchanged under p → p + c(t) | proved (∫div(|u|u) = 0 for |u|u ∈ W^{1,1}) | none |

Verdict: the identity is correct (independently rederived here, agreeing
with review-pressure.md items 1–4). Every step is determined; none is
written. This is a **major** (not blocking) obligation because no new
mathematics is needed, but for a referee-proof text the entire proof must
be displayed with the exact memberships from Tao (iv).

### 1.8 `prop:lowpressure` (special attention item 2)

| Step | Class | Obligation |
| --- | --- | --- |
| Littlewood–Paley conventions (real, even, smooth homogeneous partition; S_J symbol χ(2^{−J}ξ) = Σ_{j≤0}φ(2^{−j}·), supported in |ξ| ≤ 2^{J+1}, equal to 1 near 0 for ξ≠0) | asserted ("Fix a smooth homogeneous LP partition"); review-frequency.md already required the real/even statement | F-1 |
| ‖K_J‖_∞ ≤ C2^{3J} for the kernel of S_JR_iR_j | sketched. Exact path: m_J(ξ) = χ(2^{−J}ξ)(−ξ_iξ_j/|ξ|²) is measurable, |m_J| ≤ 1_{B(0,2^{J+1})}, so ‖m_J‖_{L¹_ξ} ≤ (4π/3)2^{3(J+1)}; K_J := F⁻¹m_J satisfies ‖K_J‖_∞ ≤ ‖m_J‖₁ (constant 1 with the e^{−2πix·ξ} convention). So the multiplier **is** in L¹ of frequency, and the constant is explicit: C = (4π/3)·8 for cutoff radius 2^{J+1}, times the Fourier-normalisation factor | F-1 |
| S_JR_iR_j f = K_J ∗ f for f = u_iu_j ∈ L¹∩L² | asserted; needs: R_iR_j and S_J are L² multipliers, m_J ∈ L¹∩L² so K_J ∈ L²∩L^∞, and F(K_J∗f) = m_J f̂ for f ∈ L¹ (Fourier of a convolution of L² with L¹) | F-1 |
| ‖p_{≤J}‖_∞ ≤ C2^{3J}‖u⊗u‖₁ ≤ C2^{3J}‖u₀‖₂² | proved from the kernel bound, Young (L^∞ = L^∞∗L¹) and prop:energy | none |
| ‖u·∇|u|‖₁ ≤ ‖u‖₂‖∇u‖₂ | proved (|∇|u|| ≤ |∇u| a.e.; with P-0 this is |(∇u)ᵀu|/|u| ≤ |∇u| pointwise) | none |
| ∫₀^τ‖∇u‖₂ ≤ τ^{1/2}(∫₀^τ‖∇u‖₂²)^{1/2} ≤ ‖u₀‖₂(H/2ν)^{1/2} | proved (time Cauchy–Schwarz; τ ≤ H) | none |
| Measurability/integrability of t ↦ L_J(t) | asserted; follows from |L_J| ≤ C2^{3J}‖u₀‖₂³‖∇u(t)‖₂ and continuity of ∇u in L² | F-1 (minor) |

Verdict: correct with the displayed constant path; all missing text is
routine. Note that the constant C in eq:lowpressure depends only on the
Fourier convention and the cutoff profile radius; a complete proof should
say "C = (32π/3)·c_F" or similar.

### 1.9 `hyp:highpressure`, `hyp:absorption`, and the paragraphs after them (special attention item 5)

- Both hypotheses: statements only. Quantifier order ∃θ ∀(ν,u₀,H) ∃(J,A) ∀τ
  agrees with `docs/proof-graph.yaml` HIGH-PRESSURE and with PLAN.md's
  "Exact target". See §2 for the ABSORPTION-node wording.
- "prop:lowpressure and hyp:highpressure imply hyp:absorption with
  A = A_low + A_high": proved (addition; the J in A_low is the J(ν,u₀,H)
  supplied by hyp:highpressure — state this).
- `eq:pressure-consequence`: proved once prop:pressure is available in
  integrated form (X(τ) + 3(1−θ)ν∫₀^τD₃ ≤ ‖u₀‖₃³ + 3A, rechecked). Needs
  P-3.
- Existential-equivalence paragraph. Forward direction: proved by the
  chain hyp:high ⇒ hyp:absorption ⇒ hyp:critical ⇒ (thm:conditional) T_* = ∞
  for each datum; depends on C-1, C-2. Converse: sketched. Missing pieces:
  (i) "bounded high Sobolev norms on [0,H]" is Tao (iv) on [0,H] once
  T_* = ∞; (ii) |Q₀| ≤ C‖u‖₆³‖∇u‖₂ requires ‖p_{>0}‖₃ ≤ ‖p‖₃ + ‖S₀p‖₃ ≤
  C‖u‖₆², i.e. either Calderón–Zygmund on L³ or Tao's p ∈ H^k ⊂ L³ together
  with S₀ bounded on L³ (its kernel is Schwartz, so Young); (iii) then
  A_high := ∫₀^H|Q₀| < ∞ and the inequality holds for every τ<H with θ=0,
  J=0. All elementary; must be written as a labelled proposition if it is
  to be part of CP1 (PLAN.md's CP1 table does not list it; it is manuscript
  content and was audited in hf03-review-paper.md). Obligation X-1.
- "No converse from an arbitrary smooth finite-energy solution class to the
  selected strong branch is asserted": correct scoping; keep.

### 1.10 `thm:continuation` (special attention item 3)

Statement issue: the conclusion "then u extends as a classical solution
beyond T_*" is ill-formed when T_* is by definition maximal; the proof
actually shows the hypotheses T_*<∞ and eq:endpoint are jointly
contradictory. **Restate** as: "If sup_{0<t<T_*}‖u(t)‖₃ < ∞ then T_* = ∞",
or equivalently "T_* < ∞ ⟹ sup_{t<T_*}‖u(t)‖₃ = ∞". This is also the shape
the Lean statement needs. Obligation C-0 (statement shape; major for
faithfulness).

"ess sup": since u ∈ C([0,T_*);H^m) ⊂ C([0,T_*);L³), ess sup = sup; say so
or write sup (the graph and PLAN use sup). Minor, part of C-0.

Proof steps:

| Step | Class | Obligation |
| --- | --- | --- |
| Schwartz data ∈ H^m ∩ L³ | proved | none |
| ν-normalisation eq:nu-normalization: v(x,s)=ν^{−1}u(x,s/ν), q=ν^{−2}p(x,s/ν) solves the unit-viscosity system, S_* = νT_*, ‖v(s)‖₃ = ν^{−1}‖u(s/ν)‖₃ | proved (rechecked: v_s = ν^{−2}u_t, (v·∇)v = ν^{−2}(u·∇)u, ∇q = ν^{−2}∇p, Δv = ν^{−1}Δu = ν^{−2}·νΔu) | none |
| Classical branch is a GKP strong solution on [0,T] for every T<νT_* (v ∈ E_{p,p}(T) for some 3<p<9, v satisfies the Leray-projected Duhamel formula) | asserted ("standard persistence"). Needs: v ∈ L^∞_tH^m ⊂ L^∞_t Ḃ^{s_p}_{p,p} ∩ L^{2p/(p+1)}_t Ḃ^{4/p}_{p,p} (embeddings H^m ↪ L³ ↪ Ḃ^{s_p}_{p,3} ↪ Ḃ^{s_p}_{p,p} and H^m ↪ B^{4/p}_{p,p} ↪ Ḃ^{4/p}_{p,p} for 4/p>0), and the Duhamel identity with ℙ from the classical equation with normalised pressure (Tao (19)/Corollary 4.3) | C-2 |
| Uniqueness identifying the classical branch with NS(v₀) on [0,T] | delegated to an unnamed "uniqueness in the mild class". GKP Theorem 4 does **not** contain it. A source must be named: uniqueness of Duhamel solutions in E_{p,p}(T) (contraction, GKP's [9]/[5]/[22]) or, simpler, uniqueness in C([0,T];L³) (Furioli–Lemarié-Rieusset–Terraneo, Rev. Mat. Iberoam. 16 (2000) 605–667, Thm — not inspected here) after showing both solutions lie in C([0,T];L³) (classical: from H^m; NS(v₀): GKP p. 5 citing [9]) | C-2 (blocking) |
| Hence T*(v₀) ≥ νT_* | proved once the previous line holds | C-2 |
| Case T*(v₀) = νT_*: GKP Theorem 4 applies with the given bound ⇒ T*(v₀) = ∞ ⇒ T_* = ∞, contradiction | proved | none |
| Case T*(v₀) > νT_*: the manuscript's "S_* = νT_*" silently excludes this case. To close it: NS(v₀) ∈ E_{p,p}(νT_*+δ), hence in a Serrin class L^r_tL^q_x (2/r+3/q = 1, q>3) up to νT_*+δ; Prodi–Serrin/Ladyzhenskaya regularity then bounds ‖u(t)‖_{H¹} up to T_*, contradicting the H¹ blow-up alternative from L-1. Alternatively prove directly that NS(v₀) coincides with an H¹ mild solution on [0,νT_*+δ]. Either way a named persistence/regularity theorem is required | C-2 (blocking) |

Verdict: the conditional logic is right and the ν-normalisation is exact
(review-pressure.md item 8), but the identification step is the single
sentence "Tao's local theorem and standard persistence give a classical
solution, while uniqueness in the mild class identifies it with the maximal
L³ solution". For a complete proof this sentence must become a lemma with
named sources for (a) the uniqueness class and (b) regularity of the L³
strong solution past the classical time. **Blocking** for "self-contained,
referee-proof".

### 1.11 `hyp:critical` and "hyp:absorption ⟹ hyp:critical"

Statement; the implication with M = (‖u₀‖₃³+3A)^{1/3} is proved from
eq:pressure-consequence (needs P-3). The sentence "Finite-horizon dependence
is enough: if T_*<∞, choose any finite H>T_*" is proved. Small-data remark
(Kato 1984) is decorative and unused.

### 1.12 `thm:conditional` (special attention item 4)

| Step | Class | Obligation |
| --- | --- | --- |
| If T_*<∞, choose H>T_*; hyp:critical gives eq:endpoint; thm:continuation gives contradiction; so T_* = ∞ | proved given C-0/C-2 | none |
| "Persistence in Tao's local theorem preserves smoothness for every finite time, including at t=0" | sketched and misnamed: the correct statement is Tao 5.4(iv) applied to the restriction to [0,T] for every T<∞ (each restriction is an H¹ mild solution with Schwartz data, by L-1); smoothness on ℝ³×[0,∞) then follows because smoothness is local in t. Also needed: the lemma "∂_t^j u ∈ L^∞_tH^k for all j,k ⟹ u ∈ C^∞([0,T]×ℝ³)" (Sobolev embedding H^k ↪ C^{k−2}_b plus Lipschitz-in-time of every derivative) | C-3 |
| sup_t‖u(t)‖₂² ≤ ‖u₀‖₂² | proved by prop:energy | E-1 |
| Pressure "recovered up to a function of time from −Δp = ∂_i∂_j(u_iu_j) and smooth through t=0 by the same local theorem" | sketched: Tao (iv) gives the normalised p smooth on [0,T]×ℝ³ directly; "up to a function of time" is unnecessary once the normalised pressure is fixed (and Fefferman accepts any smooth p). Say: take p = R_iR_j(u_iu_j) = Tao's normalised pressure (P-1) | C-3 |
| "Hence all parts of def:target": u,p ∈ C^∞(ℝ³×[0,∞)), ∫|u|²dx < C for all t, equation holds, u(0)=u₀ | proved modulo the above | none |

Fefferman's exact requirements (bounded energy for all t with one constant;
p,u ∈ C^∞(ℝ³×[0,∞))) are met by the argument once C-3 is written.

### 1.13 `sec:compactness`

Discussion only; no claims used by CP1. No obligation.

### 1.14 `sec:quotient` (special attention item 6)

Every sentence of this section is a **summary** of
`hf17-quotient-functional.md` and `hf17-quotient-evolution.md`; none is a
proof at manuscript standard. The reviews (hf17-review-*) reconstruct the
arguments and pass them, but the reviews are evidence files, not the paper.
The section must be rewritten as labelled propositions with proofs (PLAN.md
gate 1 already says so). Sentence-by-sentence:

| Sentence(s) | Class | Needed lemma(s) |
| --- | --- | --- |
| Definition of 𝒢₃ and 𝒬 | definition | Q-0: state that 𝒢₃ is a closed linear subspace; fix L³ = L³(ℝ³;ℝ³) real |
| "The minimizer q exists by reflexivity and weak lower semicontinuity" | sketched | Q-1: L³ reflexive (or: bounded sequences in L³ have weakly convergent subsequences); closed convex ⇒ weakly closed (Mazur); norm weakly l.s.c.; minimizing sequence bounded since ‖q_n‖ ≤ ‖u+q_n‖+‖u‖ |
| "unique by strict convexity" | sketched | Q-2: strict convexity of the L³ norm (Clarkson, 1<p<∞); uniqueness of the minimiser of a strictly convex function on a convex set |
| "Stationarity gives ∫A·g = 0 for every g ∈ 𝒢₃" | sketched | Q-3: differentiation of s ↦ ∫|w+sg|³ under the integral (dominant 3(|w|+|g|)²|g| ∈ L¹) |
| "The bounded Leray projection ℙ annihilates this space, so for solenoidal u, coercivity" | sketched; the boundedness of ℙ on L³ is delegated with no source | Q-4: ℙ bounded on L³ (Calderón–Zygmund; e.g. Stein, *Singular Integrals*, Ch. II §4 / Grafakos CFA Cor. 5.2.8 for Riesz transforms — sources to be pinned by CP01 literature lane); ℙ∇φ = 0 for φ ∈ C_c^∞ (symbol computation) and by continuity ℙq = 0 on 𝒢₃; **ℙu = u for every distributionally solenoidal u ∈ L³** (needs a duality proof: ⟨(I−ℙ)u,φ⟩ = ⟨u,∇Δ⁻¹div φ⟩ and a cutoff approximation of the potential Δ⁻¹div φ, whose gradient decays like |x|^{−3}); then ‖u‖₃ ≤ ‖ℙ‖‖w‖₃; upper bound from q = 0 |
| "cubic in amplitude and invariant under the critical spatial scaling" | sketched | Q-5: S_λ is an L³ isometry mapping 𝒢₃ bijectively onto itself (S_λ∇φ = ∇[φ(λ·)]); Q(S_λu) = Q(u) (elementary, provable in full) |
| "Heat preserves 𝒢₃ and contracts L³; applying heat to a minimizing representative proves 𝒬(e^{sΔ}u) ≤ 𝒬(u)" | sketched | Q-6: heat semigroup as Gaussian convolution, ‖G_sf‖₃ ≤ ‖f‖₃ (Young with an L¹-normalised kernel); G_s∇φ = ∇G_sφ; G_sφ Schwartz; ∇ψ ∈ 𝒢₃ for Schwartz ψ (cutoff: ∇(χ_Rψ) → ∇ψ in L³); extension to the closure by continuity of G_s; then the two inequalities |
| "Fréchet differentiable, D𝒬(u)[h] = ∫A·h. For completeness …" | sketched (the argument given is essentially complete but compressed) | Q-7: (a) pointwise uniform monotonicity (|a|a−|b|b)·(a−b) ≥ c|a−b|³ in ℝ³ (p = 3 ≥ 2; e.g. Lindqvist, *Notes on the p-Laplace equation*, Ch. 12 (I)); (b) ∥|a|a−|b|b∥ ≤ (|a|+|b|)|a−b|, hence ‖A'−A‖_{3/2} ≤ C(‖w‖₃+‖w'‖₃)‖w'−w‖₃; (c) the cancellation ∫(A'−A)·(q'−q) = 0; (d) quotient contraction ‖w'‖₃ ≤ ‖w‖₃+‖h‖₃; (e) conclusion ‖w'−w‖₃ ≤ C‖h‖₃^{1/2}; (f) pointwise Taylor bound |a+h|³−|a|³−3|a|a·h ≤ C(|a|+|h|)|h|²; (g) the two competitor inequalities give 𝒬(u+h)−𝒬(u)−∫A·h = O(‖h‖₃^{3/2}). All elementary; must be written |
| "On compact classical intervals with u ∈ CH^m, u_t ∈ CH^{m−2}, m ≥ 4, the pressure satisfies p,∇p ∈ L³" | sketched | Q-8: from Tao (iv) directly (p ∈ H^k), given P-1; no Calderón–Zygmund needed |
| "Cutting off p and mollifying proves ∇p ∈ 𝒢₃" | sketched | Q-9: ∇(χ_Rp) → ∇p in L³ (needs p ∈ L³), mollification of χ_Rp gives C_c^∞ potentials with gradients converging in L³ |
| "The chain rule therefore cancels pressure exactly" | sketched | Q-10: u ∈ C¹([0,T];L³) (from ∂_tu, ∂_t²u ∈ L^∞_tH^k), chain rule for a Fréchet-differentiable functional along a C¹ curve, u_t = νΔu−(u·∇)u−∇p with each term in L³, then D𝒬(u)[∇p] = 0 by Q-3/Q-9 |
| "D_𝒬(u) = −∫A·Δu ≥ 0; its sign follows by differentiating the heat contraction at zero; Δu ∈ L³ justifies this generator limit" | sketched | Q-11: (G_su−u)/s → Δu in L³ for u with u,Δu ∈ L³ ∩ C_b (write G_su−u = ∫₀^sG_rΔu dr and use strong continuity of G_r on L³); then Fréchet differentiability gives D𝒬(u)[Δu] = lim(𝒬(G_su)−𝒬(u))/s ≤ 0 |
| Inner variation: flow Φ_s, competitor q_s, envelope (11), limits (12), equality of linear coefficients | sketched (the note's argument is rechecked here and is correct) | Q-12: global flow of the bounded smooth divergence-free u(t) (fixed t) with Φ_s a volume-preserving C^k diffeomorphism, DΦ_s → I and (DΦ_s^{−T}−I)/s → −(∇u)ᵀ uniformly (needs ∇u bounded and uniformly continuous; both from H^m, m ≥ 4); Q-13: pullback of compact gradients is a compact gradient (chain rule), pullback bounded on L³ with norm ‖DΦ_{−s}‖_∞ (volume preservation), hence q_s ∈ 𝒢₃; Q-14: change of variables in the envelope with Jacobian 1; Q-15: (u∘Φ_{−s}−u)/s → −(u·∇)u in L³ (continuity of g ↦ g∘Φ_{−r} in L³ at r = 0 for g ∈ L³, via approximation by C_c and volume preservation); Q-16: two-sided expansion: LHS by Fréchet differentiability, RHS by the pointwise Taylor bound (f) with M_s := (DΦ_s^{−T}−I)/s → −(∇u)ᵀ uniformly and q ∈ L³, giving ∫A·((u·∇)u) = ∫q·((A·∇)u) (index contraction rechecked: −∫A_i(∂_iu_j)q_j) |
| eq:quotient-evolution | proved from Q-10, Q-11, Q-16 | — |
| "The remaining low-strain term has absolute value at most M𝒬(u), M = C2^{5L/2}‖u₀‖₂: use Hölder, ‖q‖₃ ≤ C‖w‖₃, Bernstein, and energy" | sketched | Q-17: Hölder (1/∞+1/3+2/3), ‖A‖_{3/2} = ‖w‖₃², ‖q‖₃ = ‖(I−ℙ)w‖₃ ≤ (1+‖ℙ‖)‖w‖₃, so the term is ≤ 3(1+‖ℙ‖)‖∇S_Lu‖_∞𝒬(u); Bernstein ‖∇S_Lf‖_∞ ≤ C2^{5L/2}‖f‖₂ (kernel ∇K_L ∈ L² with ‖∇K_L‖₂ ≤ C2^{5L/2}, Cauchy–Schwarz — same technique as F-1); energy ‖u(t)‖₂ ≤ ‖u₀‖₂ |
| "Integration of eq:quotient-evolution and Gronwall would then bound 𝒬, hence L³" | asserted (conditional) | Q-18: with eq:quotient-gap, 𝒬(τ)+(1−θ)ν∫₀^τD_𝒬 ≤ 𝒬(0)+A_input+M∫₀^τ𝒬, Gronwall gives 𝒬(τ) ≤ (𝒬(0)+A_input)e^{MH}, then ‖u(τ)‖₃³ ≤ 3‖ℙ‖³𝒬(τ); needs 𝒬∘u absolutely continuous (from Q-10) |

None of Q-0…Q-18 is deep; Q-4 (Leray projection on L³ and ℙu = u for
solenoidal L³ fields), Q-7, and Q-12–Q-16 are the ones that need real
pages. The section's current disclaimers ("no quantitative comparison with
the original cubic dissipation is claimed", "neither eq:quotient-gap nor a
quantitative dissipation mechanism has been proved") are correct and must
be kept.

---

## 2. Quantifier / solution-class discrepancies with the graph and PLAN

1. **Graph ESS node.** Statement: "A maximal smooth finite-energy ℝ³
   solution with finite maximal time has unbounded L³ norm on that
   interval". The imported theorem (GKP Theorem 4) is about NS(u₀), the
   maximal L³/Besov strong (mild) solution with u₀ ∈ L³; it says nothing
   about "smooth finite-energy solutions" as a class (Tao's smooth
   finite-energy solutions need not even have u₀ ∈ L³ in general). The
   manuscript's thm:continuation is (correctly) restricted to the
   Schwartz-data classical branch and reaches GKP through the
   identification C-2. The graph statement should be the GKP statement
   verbatim plus the identification lemma as a separate paper node; the Lean
   literature axiom must be GKP's statement, not the graph's paraphrase.
2. **Graph ABSORPTION node.** "there is a finite a priori A, and a fixed
   theta less than one" places θ inside the ∀(u₀,ν,T) scope by reading
   order; the manuscript (and HIGH-PRESSURE node, and PLAN "Exact target")
   put ∃θ first. Harmless mathematically (both directions of the chain work
   with either reading), but not an exact statement match.
3. **Graph LOCAL node** says "unique maximal classical finite-energy
   solution"; the uniqueness class (H¹ mild, i.e. finite enstrophy and
   L²_tH², normalised pressure) is not stated anywhere. Tao's Theorem 1.12
   (p. 7) shows why the class matters for non-Schwartz data.
4. **Graph has no node for the quotient results**; PLAN.md's CP1 table
   already marks "QUOTIENT (to be added)". `docs/proof.md`'s quotient
   paragraph matches the manuscript.
5. **thm:continuation conclusion shape** ("extends beyond T_*") differs from
   the graph ESS wording ("finite maximal time ⟹ unbounded L³") and from
   PLAN; the graph wording is the correct one (C-0).
6. **ess sup vs sup** (manuscript vs graph/PLAN): identical here because
   u ∈ C([0,T_*);L³); say so.
7. **Graph `source_revision.manuscript_commit`** (`d84950b…`) is not the
   manuscript HEAD (`1ad73c2`); the recorded revision predates sec:quotient.
8. **CRITICAL node** uses "0 ≤ t"; manuscript uses "0 < t". Trivial.
9. The existential-equivalence paragraph is manuscript content audited in
   hf03-review-paper.md but is not listed in PLAN.md's CP1 table; decide
   whether it is a CP1 proposition (then X-1) or a remark.

No discrepancy of domain (ℝ³), equation (unforced, viscosity ν>0),
data class (Schwartz, divergence-free), or solution class (Tao H¹-mild
classical branch) was found between the manuscript and the Clay target.
No forced, averaged, hyperdissipative, Euler, periodic, or weak-nonunique
variant is used anywhere in the CP1 chain.

---

## 3. Mathlib coverage (grep-level, checkout `0df444a`, not built)

Present (file paths relative to `Mathlib/`):

- Schwartz space, tempered distributions, Fourier multipliers on 𝓢 and 𝓢',
  Bessel-potential Sobolev spaces `TemperedDistribution.MemSobolev` with
  p = 2 results (`Analysis/Distribution/{SchwartzSpace,TemperedDistribution,
  FourierMultiplier,Sobolev}.lean`).
- Fourier transform on L² as a linear isometry (Plancherel):
  `Analysis/Fourier/LpSpace.lean` (`fourierTransformₗᵢ`, `norm_fourier_eq`).
- Gagliardo–Nirenberg–Sobolev inequality for C¹ compactly supported maps:
  `Analysis/FunctionalSpaces/SobolevInequality.lean`
  (`eLpNorm_le_eLpNorm_fderiv_of_eq`, hypotheses `ContDiff ℝ 1 u`,
  `HasCompactSupport u`, (p')⁻¹ = p⁻¹ − n⁻¹). The H¹ version needed for
  S-1/N-1 requires a density extension (project lemma).
- Derivative of ‖·‖^p in inner-product spaces:
  `Analysis/InnerProductSpace/NormPow.lean` (`hasFDerivAt_norm_rpow`, p>1) —
  gives the pointwise ingredient for Q-3 and Q-7(f).
- Differentiation under the integral:
  `Analysis/Calculus/ParametricIntegral.lean`
  (`hasFDerivAt_integral_of_dominated_loc_of_lip`).
- Rademacher: `Analysis/Calculus/Rademacher.lean` (only needed if ∇|u| is
  kept; P-0 avoids it).
- Gronwall: `Analysis/ODE/Gronwall.lean`
  (`norm_le_gronwallBound_of_norm_deriv_right_le`) — for Q-18.
- Picard–Lindelöf local existence (`Analysis/ODE/PicardLindelof.lean`),
  Gaussian integrals and the Fourier transform of Gaussians
  (`Analysis/SpecialFunctions/Gaussian/*`).

Not located by grep (treat as **mathlib-absent** until CP03 checks):

- Calderón–Zygmund theory, Riesz transforms, Leray projection on L^p (Q-4,
  and P-1 if the CZ route is used; the Tao route avoids CZ in prop:pressure).
- Heat semigroup on L^p (contractivity, strong continuity, commutation with
  ∇) (Q-6, Q-11).
- Uniform/strict convexity and reflexivity of L^p, Clarkson inequalities
  (`UniformConvexSpace` instances exist only for inner-product spaces; no
  `StrictConvexSpace` instance for `Lp` found) (Q-1, Q-2).
- Young's convolution inequality on L^p (no `eLpNorm_convolution` found;
  `Analysis/Convolution.lean` has no L^p bound) (F-1, Q-6, Q-17).
- Littlewood–Paley partitions, Bernstein inequalities (F-1, Q-17).
- Global flows of bounded smooth vector fields with differentiable
  dependence on initial data, volume preservation (Q-12).
- Gagliardo–Nirenberg interpolation ‖∇u‖₃ ≲ ‖∇u‖₂^{1/2}‖Δu‖₂^{1/2} (N-1;
  provable from Hölder + Sobolev + Plancherel).
- Mixed-norm spaces L^∞_tH^k, C¹_tH^k, and the Sobolev embedding
  H^k(ℝ³) ↪ C^{k−2}_b (C-3, E-1).

---

## 4. Ranked obligations

Severity is relative to the goal "complete, self-contained, referee-proof
paper proof of CP1". IDs are used in the frontier record.

### Blocking

- **L-1** (premise:local). Write the ℝ³ maximal-development lemma from Tao
  5.4(ii),(iii) + Corollary 4.3: definition of T_*, gluing, uniqueness class
  (H¹ mild ⇔ classical with u ∈ L^∞_tH¹∩L²_tH² and normalised pressure),
  H¹ blow-up alternative, and the ν-normalisation applied to the local
  theory (Tao is stated for ν = 1). Tao's Corollary 5.2 is periodic only.
- **C-2** (thm:continuation). Write the identification lemma "classical
  branch = NS(v₀) with T*(v₀) = νT_*": (a) membership of the classical
  solution in GKP's class E_{p,p}(T) and in the Duhamel form; (b) a named
  uniqueness theorem for that class (or for C([0,T];L³)); (c) the case
  T*(v₀) > νT_* via a named persistence/regularity theorem for the L³
  strong solution, contradicting the H¹ blow-up alternative. GKP Theorem 4
  covers only the final implication.
- **Q-block** (sec:quotient). Restructure into labelled propositions with
  proofs Q-0…Q-18 (§1.14). In particular Q-4 (ℙ on L³ and ℙu = u for
  solenoidal L³ fields), Q-7 (Fréchet derivative), Q-12–Q-16 (inner
  variation). Every sentence of the section is currently a summary of
  hf17-*.md.

### Major

- **C-0**. Restate thm:continuation as "T_*<∞ ⟹ sup_{t<T_*}‖u‖₃ = ∞" (or
  its contrapositive); replace ess sup by sup with justification.
- **C-3** (thm:conditional). Replace "persistence … preserves smoothness"
  by: Tao 5.4(iv) on every [0,T]; lemma "∂_t^ju ∈ L^∞_tH^k ∀j,k ⟹ u ∈
  C^∞([0,T]×ℝ³)"; the pressure is the normalised pressure (P-1), smooth by
  the same item; conclude p,u ∈ C^∞(ℝ³×[0,∞)).
- **P-1** (prop:pressure). Fix the Fourier/Riesz convention and prove
  R_iR_j(u_iu_j) = −Δ⁻¹∂_i∂_j(u_iu_j) = Tao's normalised pressure; obtain
  p ∈ L²∩L^∞ (hence L²∩L³) from Tao (iv) without Calderón–Zygmund, or cite
  CZ exactly if that route is kept.
- **P-2** (prop:pressure). Display every cutoff-error estimate and both
  limits (R→∞, ε↓0) with the exact memberships (u ∈ C¹_t(L²∩L⁴)∩C_t(L^∞∩H¹),
  p ∈ C_tL²) and the ε-uniform majorant.
- **P-3** (prop:pressure, eq:pressure-consequence). State the balance in
  integrated form or prove continuity of D₃ and P₃ in t.
- **F-1** (prop:lowpressure). State the LP conventions (real, even), the
  explicit L¹-frequency bound and the constant, the convolution
  representation for f ∈ L¹∩L², and measurability of L_J.
- **E-1**, **N-1** (prop:energy, prop:enstrophy). Replace "strong-solution
  Sobolev bounds justify" by the exact memberships and the density/Plancherel
  arguments; name the Sobolev inequality source (S-1); prove the
  Gagliardo–Nirenberg step.
- **X-1** (existential-equivalence paragraph). If it is CP1 content, make it
  a proposition; supply ‖p_{>0}‖₃ ≤ C‖u‖₆² with a stated route (CZ, or Tao
  p ∈ H^k plus S₀ ∈ L¹-kernel).
- **G-1** (graph/PLAN). Fix items 1–4 and 7 of §2 (ESS statement class,
  ABSORPTION θ placement, LOCAL uniqueness class, QUOTIENT node, stale
  source revision). Controller task; not edited here.

### Minor

- **P-0**. Redefine D₃ and P₃ through (∇u)ᵀu (no ∇|u|, no a.e. statement).
- **S-2**. Remove the non-mathematical clause "they do not imply u ∈
  L^∞(0,T;L³)" from the statement of prop:scaling (keep as a remark), or
  give an explicit counterexample function.
- **S-1**. Name the Sobolev inequality source and constant convention.
- The word "persistence" is used in two senses (Sobolev persistence along
  the flow; the H¹→H^k regularity in Tao (iv)); disambiguate.
- Kato 1984 small-data remark is unused; keep or drop.
- def:target is typeset as a Theorem; harmless, but the Lean challenge
  should present it as the terminal statement, not a proved result.

### Literature status of imported premises

| Premise | Status | Note |
| --- | --- | --- |
| Tao 5.4 (i)–(iv), Corollary 4.3 | literature, directly inspected | exact text in §0.1; ν = 1; ℝ³ maximal development not stated |
| GKP Theorem 4 | literature, directly inspected | exact text in §0.2; ν = 1; uniqueness and identification not stated |
| Uniqueness of L³ / E_{p,p} strong solutions | literature, **not inspected**; source to be pinned (GKP's [9], FLT 2000, or Kato 1984) | required by C-2 |
| Regularity/persistence of L³ strong solutions past the classical time | literature, **not inspected**; source to be pinned | required by C-2 |
| Fefferman (A) exact text | literature, metadata-only here (dossier records direct inspection) | matches def:target |
| Calderón–Zygmund L^p bounds for Riesz transforms / Leray projection | literature, not inspected here; needed for Q-4 (and optionally P-1, X-1) | mathlib-absent |
| Sobolev inequality, Clarkson, heat semigroup, Young, Bernstein | standard; see §3 for Mathlib status | — |

---

## Frontier record

**CLAIM AND SCOPE.** Every manuscript-owned step of CP1 (prop:energy,
prop:scaling, prop:enstrophy, prop:ode, prop:pressure, prop:lowpressure,
thm:continuation, thm:conditional, the existential-equivalence paragraph,
and the sec:quotient results) is either correct as sketched or correct as
asserted, on the original unforced ℝ³ equation with Schwartz divergence-free
data and arbitrary ν>0, in the Tao H¹-mild classical branch. No step was
found to be false. No step except prop:ode is currently written at the
standard of a complete paper proof.

**EVIDENCE.** Independent rederivation of every displayed identity and
exponent (pressure balance, cutoff and ε-limits, kernel bound and constant,
time Cauchy–Schwarz, ν-normalisation, quotient stationarity, coercivity,
heat contraction, Fréchet derivative with remainder O(‖h‖^{3/2}), inner
variation and index contraction, low-strain Bernstein bound, Gronwall
closure); direct inspection of Tao Theorem 5.4/Corollary 4.3 and GKP
Theorem 4 with their definitions; comparison with the frozen audits
review-{estimates,pressure,frequency,integration}.md, hf03-review-paper.md,
hf17-review-*.md, which agree with the findings here.

**FIRST GAP (for the CP1 paper-proof goal, not for the Millennium claim).**
The identification step in thm:continuation (C-2): "uniqueness in the mild
class identifies [the classical branch] with the maximal L³ solution" and
the implicit equality S_* = νT_* are asserted without a named uniqueness
theorem, without the membership of the classical solution in GKP's class,
and without treatment of the case T*(v₀) > νT_*. Immediately behind it:
L-1 (ℝ³ maximal development is not in the cited Tao theorem) and the
unwritten sec:quotient proofs.

**SURVIVING CONDITIONAL SUFFIX.** Given L-1 and C-2 written with named
sources, the chain hyp:highpressure ⟹ hyp:absorption ⟹ hyp:critical ⟹
(thm:continuation, normalised GKP Theorem 4) T_* = ∞ ⟹ (Tao 5.4(iv),
prop:energy) Clay alternative (A) is valid; and, independently, the
quotient identities eq:quotient-evolution with D_𝒬 ≥ 0 and the low-strain
Gronwall coefficient are valid on compact classical intervals.

**UNNECESSARY DEPENDENCIES.** prop:enstrophy, prop:ode, sec:compactness,
the Kato small-data remark, and strict θ<1 are not used in the conditional
chain (already recorded in review-integration.md). Calderón–Zygmund theory
is unnecessary for prop:pressure and thm:conditional if Tao's p ∈ H^k is
used (P-1); it remains necessary for Q-4 (Leray projection on L³) and, in
the CZ route, for X-1. Rademacher/∇|u| is unnecessary after P-0. The abstract
uniform-smoothness-of-quotient argument in hf17-quotient-functional.md §5
is unnecessary; the manuscript's direct competitor argument (Q-7) suffices.

**NON-CLAIMS.** No HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION, or
NS-R3 result is asserted or approached. No literature theorem is declared
verified beyond the pages inspected and quoted above; the two uniqueness /
persistence sources needed by C-2 were not inspected. Mathlib statements
are grep-level and were not type-checked.

**NEXT DISTINCT ACTION.** CP01 literature lane: pin exact statements and
locations for (a) uniqueness of L³ (or E_{p,p}) strong solutions and (b)
regularity/persistence of the L³ strong solution, so that C-2 can be
written; then CP02 writes L-1, C-2, and the sec:quotient propositions
Q-0…Q-18 first, the routine P-1…P-3, F-1, E-1, N-1, C-0, C-3 second.
