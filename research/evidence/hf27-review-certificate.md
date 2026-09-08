# Review of HF27, Sections 2–3 and Appendix A: the critical residual certificate

Independent adversarial proof audit, 2026-09-06. Lens: rebuild every constant
and every identity from scratch (by hand, `sympy`, and high-precision `mpmath`
sweeps), decide the two decisive questions before reading any proof
sympathetically, and attempt explicit refutations of each new fact.

## Freeze

| object | identity |
|---|---|
| research HEAD at audit time | `30d715d` (branch `main`, clean) |
| target | `research/evidence/hf27-critical-residual-continuation.tex`, 996 lines |
| target SHA-256 | `3898e9a020d31c4fc58c9f1289ea4794ec9f787b885086e411b98b0cb1f97488` (rehashed; matches the index note) |
| index note (context only) | `research/evidence/hf27-critical-residual-continuation.md` |
| manuscript consulted | `../navier-paper/main.tex` (working tree at audit time) |
| audited inputs consulted | `hf18-hodge-regularity.md` + `hf18-review-hodge-regularity.md` (PASS); `hf23-divcurl-continuation.tex` + `hf23-review-regularity-core.md` (PASS) + `hf23-review-reconstruction-boundary.md` (PASS WITH SCOPE); `hf25-review-defect-criterion.md`; `hf24-review-badset-restriction.md`; `hf24-review-modulus-of-continuity.md`; `hf26-review-temporal-producer.md`; `hf26-review-weighted-linearization.md`; `hf26-review-countermodel-crossings.md`; `PLAN.md`; `docs/proof-graph.yaml`; `literature/current-status.md` |

Nothing outside this file was edited. No commit, no push. The candidate,
`PLAN.md`, `docs/` and the manuscript are untouched. No third-party PDF was
downloaded or retained; no contact was made with any person.

## Scope

- Section 2 `sec:toolkit`, lines 123–229: `lem:basic`, `lem:import`,
  `prop:weighted`, and the constant dictionary `eq:constants1`–`eq:rstar`.
- Section 3 `sec:relative`, lines 231–316: `def:comparison`, `prop:identity`,
  `lem:three`.
- Section 4 `sec:certificate`, lines 318–429: `thm:certificate`, its remark,
  `cor:direct`, and the scaling subsection.
- Appendix A `app:weighted`, lines 864–941.

**Not** in scope: Sections 1, 5 (`sec:oscillation`), 6 (`sec:hierarchy`),
7 (`sec:gap`), 8 (`sec:concentration`), 9 (`sec:boundary`), Appendix B
(`app:checks`) beyond the six arithmetic identities it lists, and the
bibliography except where a cited object is load-bearing for my scope.

---

## VERDICT

**PASS WITH SCOPE (REPAIR before any import).**

*One line:* every proof in this scope is correct and the bootstrap is not
circular, but the certificate is the CCRT a posteriori principle in a critical
norm, its hypothesis is exactly equivalent to the conclusion it produces, and
its weighted-dissipation half is an already-audited, already-imported
manuscript lemma filed here as a new candidate.

Every inequality, constant, exponent, Hölder split, Young maximisation,
interpolation exponent and pointwise identity in Sections 2–3, the certificate,
`cor:direct`, the scaling subsection and Appendix A was recomputed
independently and is **correct as displayed**. The bootstrap in `thm:certificate`
Step 1/Step 3 is **not circular**. `prop:identity` is **exact** and the pressure
**does** genuinely cancel. Eleven refutation attempts were made; all failed at
the level of mathematics.

The scope qualification is entirely about *what the results are*, and it is
decisive on both questions the controller asked first:

1. **`thm:certificate` is the Chernyshenko–Constantin–Robinson–Titi robustness /
   a posteriori regularity principle**, transplanted from the periodic cube to
   `R^3` with a critical norm in place of a high-regularity one, and with this
   programme's quotient functional supplying the critical-norm energy method.
   The architecture — comparison field, retained equation defect, error
   estimate with a Prodi–Serrin Gronwall factor, exit-time bootstrap,
   continuation criterion, plus a Galerkin hierarchy with conditional eventual
   verification — is CCRT's, item for item. Finding it is not new is the correct
   outcome. **The note's prior-art discipline is substantive but materially
   incomplete**: it cites CCRT correctly (including the identifier, which is
   right and which the task brief had wrong) and disclaims novelty, but omits
   the entire critical-norm branch of the same literature — Dashti–Robinson
   2008, Marín-Rubio–Robinson–Sadowski 2013, Burczak–Zajączkowski 2016, and
   above all Brunk–Giesselmann–Tscherpel, arXiv:2509.25105 (Sept 2025), which
   is critical `L^3` + ESS endpoint + the same `ν^{-3}‖v‖_6^4` Gronwall
   exponent + a negative-Sobolev residual, one year earlier (see Q1).
2. **`eq:certsmall`, existentially quantified over admissible comparisons, is
   exactly equivalent to `T_* > H`.** I prove it below in one line in each
   direction. It therefore joins the existential-equivalence class alongside
   HF25's defect hypothesis, HF24-B's bad-set hypothesis and HF26's temporal
   hypothesis; it is **not** the HF24-A corridor exception. A corollary the note
   does not draw: its boxed `eq:missing` is *logically equivalent* to Clay
   alternative A, not a reduction of it.

Three further scope items: `prop:weighted`, `eq:gradA`, `eq:selfbound` and the
whole of Appendix A are **already-owned manuscript results at the very revision
this note pins**, filed here as "self-checked candidates"; a load-bearing
zero-set fact present in HF26 was dropped; and the audited HF18-A/HF23
provenance is nowhere recorded.

**No graph node changes and nothing is promoted by this review.**

---

# The two decisive questions

## Q1. Prior art: is `thm:certificate` the CCRT principle in a different norm?

**Verdict: YES. `thm:certificate` is the Chernyshenko–Constantin–Robinson–Titi
robustness / a posteriori regularity principle, transplanted from the periodic
cube to `R^3` and re-derived in a critical norm. The correspondence is item for
item across four theorems, not a family resemblance. The note's prior-art
discipline is SUBSTANTIVE — it names the right paper, with the right arXiv
identifier, describes its setting correctly, and disclaims novelty — but
MATERIALLY INCOMPLETE, because the entire critical-norm branch of that same
literature is missing, and it is exactly the branch that adjudicates the note's
only claimed advance.**

### CCRT, as read

S. I. Chernyshenko, P. Constantin, J. C. Robinson, E. S. Titi, "A posteriori
regularity of the three-dimensional Navier–Stokes equations from numerical
computations", J. Math. Phys. **48** (2007) 065204, DOI 10.1063/1.2372512,
**arXiv:math/0607181** (v1 7 Jul 2006, v2 24 Sep 2006).

*(Identifier note: `math/0607181` — the identifier in the note's bibliography
and in this repository's own `literature/current-status.md` line 44 — is
**correct**. `math/0608497` is a different paper, on Kuga–Satake abelian
varieties. Nothing is wrong with the note's citation.)*

- **Domain.** Periodic torus `Q = [0,L]^3` only, zero mean. `R^3` is not
  treated; the paper only remarks it would expect similar results for Dirichlet
  boundary conditions.
- **Norm.** `V^m = D(A^{m/2}) = H^m ∩ V` with **`m ≥ 3`** — subcritical by two
  and a half derivatives.
- **Defect.** A *notional forcing* `g := dv/dt + νAv + B(v,v)`, measured in
  `L^1(0,T; V^m)` (with `L^2(0,T;V^{m-1})` in the hypothesis class).
- **Theorem 3 (robustness of regularity).** If
  `‖u_0 − v_0‖_m + ∫_0^T ‖f − g‖_m ds < (1/(c_m T)) exp[−c_m ∫_0^T (‖u‖_m + ‖u‖_{m+1}) ds]`
  then `v` is a strong solution on `[0,T]`.
- **Corollary 5 (the a posteriori check, eq. (21)).** The same inequality with
  the roles swapped so the exponent is built from the *computed* field, making
  the right-hand side computable from the computation alone.
- **Theorem 6 + Theorem 8 (conditional eventual verification).** If a strong
  solution exists, Galerkin approximations converge in `L^∞(0,T;V^m) ∩
  L^2(0,T;V^{m+1})`, and **there exists `N` such that `u_n` satisfies (21) for
  every `n ≥ N`** — finite termination, conditional on regularity, with no
  claim in the failure direction.

*(Second-hand caveat: the displayed inequality is the two-way-corroborated
output of independent extractions from the ar5iv rendering of v2; a literal
transcription could not be obtained. It should be verified against the
published paper before being quoted in a manuscript. The structural facts —
torus, `m ≥ 3`, `L^1_t V^m` defect, exponential threshold, Theorems 6 and 8 —
are not in doubt.)*

### The correspondence, item for item

| CCRT | HF27 | same? |
|---|---|---|
| Thm 3, robustness under perturbed data *and* defect | `thm:certificate` | yes, architecturally identical |
| Cor 5, computable a posteriori criterion | `cor:index` (`eq:indexcertificate`) | yes |
| Thm 6, Galerkin convergence *assuming* a strong solution | `thm:complete` Steps 1–2 (`eq:convergence`) | yes |
| Thm 8, finite termination, conditional on regularity | `thm:complete` `eq:CNzero` + `eq:equiv` | yes; HF27 additionally states the biconditional |
| no claim if the criterion fails | `cor:necessary` | HF27 adds a (weak) contrapositive |

The proof mechanism is also the same one: an energy-type estimate on the error
against the comparison, self-interaction absorbed by smallness of the error in
the working norm via an exit-time bootstrap, cross-interaction producing a
Gronwall factor, defect forced by its own norm, and a continuation criterion
applied to `‖u‖ ≤ ‖v‖ + ‖e‖`.

### What genuinely differs, and whether it matters

1. **Domain `T^3 → R^3`.** Real, and correctly handled: no torus theorem is
   imported, and the whole-space endpoint criterion (ESS, through the
   manuscript) is used in place of an `H^1`/Serrin one. Credit is due here; the
   note's stated discipline is honoured in the proofs.
2. **Norm `H^m (m ≥ 3) → critical `L^3` via `Q`.** Real, and the technically
   substantive part. A critical-norm version cannot be run by an `L^2` pairing:
   `d/dt ∫|e|^3` does not shed the pressure. The cubic gradient quotient `Q`,
   its dual `A = |w|w` with `div A = 0`, and the weighted dissipation `D` are
   exactly the device that removes the pressure (Q4) and makes the critical
   estimate close. That machinery is this programme's own and is not in CCRT.
3. **Defect `L^1_t H^m → L^2_t L^3_x` stress (or `L^1_t L^3_x` velocity).** Real
   and, unlike (2), *not* peculiar to this programme — see below.
4. **Gronwall exponent.** CCRT's is linear in `‖u‖_m + ‖u‖_{m+1}` of the exact
   solution; HF27's is `c_b ν^{-3} ∫ ‖v‖_6^4`, which is verbatim the classical
   Prodi–Serrin `L^4_t L^6_x` weak–strong-stability exponent (the same `ν^{-3}‖v‖_6^4`
   that falls out of `2‖v‖_6‖w‖_2^{1/2}‖∇w‖_2^{3/2} ≤ ν‖∇w‖_2^2 + Cν^{-3}‖v‖_6^4‖w‖_2^2`).
   Not new.
5. **Explicit constants.** CCRT's `c_m` is never given, so its certificate is not
   numerically effective. HF27's constants are explicit in `S, C_3, C_{9/2}, C_9`.
   A genuine improvement in effectivity — but see Burczak–Zajączkowski below,
   who make the same point and act on it.
6. **Scale invariance.** CCRT's threshold is not scale-invariant; HF27's is
   (Q7, all four exponents exactly `0`, `[Z_H] = [ν]`). A genuine structural
   improvement, and the note never says so (R9).

### The missing branch — this is where the incompleteness bites

The note's prior-art paragraph says CCRT "works on a periodic cube in high
Sobolev regularity", which frames the critical norm as the open gap this note
fills. It is not open. The following are all in the same lineage, all
uncited here, and all closer to `thm:certificate` than CCRT is:

- **M. Dashti, J. C. Robinson**, "An a posteriori condition on the numerical
  approximations of the Navier–Stokes equations for the existence of a strong
  solution", SIAM J. Numer. Anal. **46** (2008) 3136–3150,
  DOI 10.1137/060677537, arXiv:math/0701341. Explicitly lowers CCRT's
  regularity to `u_0 ∈ V = H^1` (and an `H^2` case), with the threshold
  `exp(−(k^2/2)∫[(27k^2/2ν^3)|Du|^4 + (1/ν)|Du||Au|])` — the `ν^{-3}‖∇u‖^4`
  exponential again — and **proves the converse** (Thm 6(ii)). Their
  minimal-regularity results hold "in a general bounded domain as well as in the
  absence of boundaries", and the `H^2` case is stated for "periodic domains or
  the whole of `R^3`". This is the closest existing whole-space a posteriori
  result, and it is the one the note should have compared itself to.
- **P. Marín-Rubio, J. C. Robinson, W. Sadowski**, "Solutions of the 3D
  Navier–Stokes equations for initial data in `Ḣ^{1/2}`: robustness of
  regularity and numerical verification of regularity for bounded sets of
  initial data in `Ḣ^1`", J. Math. Anal. Appl. **400** (2013) 76–85,
  DOI 10.1016/j.jmaa.2012.10.064. **Robustness of regularity in a critical
  norm.** (Paywalled, no arXiv version; the exact hypotheses and domain could
  not be determined here. That does not excuse the omission — it makes it more
  urgent, since this is a title-level match with the note's claimed advance.)
- **J. Burczak, W. M. Zajączkowski**, "Quantitative robustness of regularity for
  3D Navier–Stokes system in `Ḣ^α`-spaces", Nonlinear Anal. RWA **31** (2016)
  513–532, DOI 10.1016/j.nonrwa.2016.03.001, arXiv:1409.3485. Torus, `α ∈ [1/2,1]`,
  perturbing **both** data and forcing, forcing measured in the **negative-order**
  `L^2(0,T;Ḣ^{α−1})`, condition
  `(|u_0−v_0|^2_α + K_4∫|f−g|^2_{α−1}) exp(K_3∫|∇u|^4_{L^{3/(2−α)}}) < (ν̄/K_2)^2`,
  with the paper's stated aims being *explicit or computable constants* and
  *scaling* — they note `K_3` becomes scaling-invariant exactly at `α = 1/2`.
  That is HF27's stated programme (critical norm, negative-order residual,
  explicit constants, scale-invariant threshold), on the torus, ten years
  earlier. Their §5.1 also raises the objection that the Galerkin-truncation
  forcing term in this scheme is controlled only under an a priori regularity
  assumption on the exact solution — which is HF27's own `thm:complete`
  limitation, already recorded in the literature.
- **A. Brunk, J. Giesselmann, T. Tscherpel**, "A posteriori existence of strong
  solutions to the Navier–Stokes equations in 3D", arXiv:2509.25105
  (29 Sep 2025). **This is the closest object I found, and it is the one the
  audit should treat as decisive.** From its abstract, verbatim: the approach
  "makes use of a version of the celebrated blow-up criterion in the critical
  space `L^∞(L^3)` by Iskauriaza, Serëgin and Shverak (2003)", is "based on a
  conditional stability estimate in `L^2` and `L^3`", and its criterion
  "involves only negative Sobolev norms of the residual". Their conditional
  stability controls `sup_t(½‖e‖_2^2 + ⅓‖e‖_3^3) + (ν/4)∫(‖|e|^{1/2}∇e‖_2^2 +
  ‖∇e‖_2^2)` with Gronwall rate `α(t) = 4 + ν/3 + (4c/ν)‖û‖_6^2 +
  4(3^3c^2/ν^3)‖û‖_6^4`, and the residual enters as `‖g‖^3_{W^{-1,3}}` and
  `‖g‖^2_{W^{-1,2}}` in time. Compare HF27: same critical `L^3` functional
  (`Q ≍ ⅓‖e‖_3^3`), same weighted dissipation `∫|e||∇e|^2` (HF27's `D`), the
  **same** `ν^{-3}‖v‖_6^4` Gronwall exponent (HF27's `m`), the same
  negative-order residual (HF27's `‖F‖_3` is a `W^{-1,3}`-type norm of `R_v`),
  and the same ESS endpoint criterion. Differences: torus versus `R^3`; a
  direct `L^2 ∩ L^3` functional versus the nonlinear-Hodge quotient `Q`
  (HF27's genuine methodological contribution, and the thing that removes the
  pressure on `R^3`); and BGT explicitly have **no converse**, where HF27 has
  `thm:complete`. It predates HF27 by a year, is on arXiv, and is uncited.
  *(Second-hand: read via its arXiv abstract and reported theorem numbers, not
  by me directly. Must be verified before being relied on — but it is a
  checkable pointer, and it cannot be left out of the comparison.)*

For completeness, the general "openness of the set of data with global
solutions" principle in critical spaces is old and settled: Ponce–Racke–Sideris–Titi,
CMP **159** (1994) 329–341 (`H^1`, data and forcing, under `∫_0^∞‖∇u‖_2^4 < ∞`
— subcritical, and the direct ancestor of CCRT's exponential);
Gallagher–Iftimie–Planchon, Ann. Inst. Fourier **53** (2003) 1387–1424 (`Ḣ^{1/2}`,
on `R^3`); Auscher–Dubois–Tchamitchian, J. Math. Pures Appl. **83** (2004)
673–697 (`BMO^{-1}`); Bahouri–Chemin–Gallagher, J. Éc. polytech. Math. **5**
(2018) 843–911 (weak-topology version). These are openness statements about
exact solutions, not certificates from a supplied comparison, so they are not
the same object — but they establish that critical-norm stability of large
global solutions on `R^3` is not new either.

### Substantive or decorative?

**Substantive, but incomplete, and the incompleteness is load-bearing.**

Substantive, on the record: the note cites CCRT with the correct identifier;
correctly states the torus/high-Sobolev setting; correctly names *both* halves
(robustness *and* conditional eventual verification by Galerkin approximation);
declines to import a torus theorem, and in fact imports none; and its
"Proof boundary" box says outright "No novelty claim is made for a posteriori
regularity or oscillatory large-data constructions". That is more discipline
than the three preceding continuations showed, and the controller is right
about that.

Incomplete, and this is what must be repaired:

1. **The correspondence is never made where it counts.** `sec:scope`'s
   prior-art paragraph says a posteriori regularity is an established idea;
   Section 4 then presents `thm:certificate` with no back-reference, and the
   status table (line 831) files "critical certificate" under "Detailed proofs
   supplied; self-checked candidates" with no prior-art column at all. A reader
   who starts at the theorem — which is how a theorem gets read — would not
   learn that it is CCRT's principle.
2. **The one branch that adjudicates the note's claimed advance is absent.**
   The note's implicit argument is "CCRT is high-regularity; ours is critical".
   Dashti–Robinson (whole space, converse), Marín-Rubio–Robinson–Sadowski
   (`Ḣ^{1/2}` robustness), Burczak–Zajączkowski (critical, negative-order
   residual, explicit constants, scaling) and Brunk–Giesselmann–Tscherpel
   (critical `L^3`, ESS, `ν^{-3}‖v‖_6^4`, negative-Sobolev residual) all sit in
   the gap the note describes as open. None is cited. A prior-art paragraph
   that names only the paper it improves on, and none of the papers that
   already made the improvement, is not a boundary.
3. **The paragraph is not an independent check.** It reproduces, without citing
   it, what this repository's own `literature/current-status.md` line 44 already
   recorded about CCRT — same identifier, same characterisation. Nothing is
   wrong with the content; but it should be recorded as a repository read, not
   as a fresh prior-art determination.

### The honest residual novelty in my scope

After the comparison, what is left that I could not find in the literature is
narrow and should be stated exactly:

> A robustness / a posteriori certificate in a critical norm, **on `R^3`**,
> whose smallness threshold is an absolute multiple of `ν` with explicit
> constants and is **scale-invariant**, obtained by a pressure-free relative
> identity for the cubic gradient quotient `Q(u−v)` — and accompanied by a
> proved converse.

Each clause is needed: BGT have critical + computable + ESS but the torus and no
converse; Dashti–Robinson have the converse and the whole space but a
subcritical norm; Burczak–Zajączkowski have critical + explicit + scaling but
the torus and no converse. The combination may well be new. **But by Q2 the
converse is exactly what makes the criterion existentially equivalent to
regularity, so the novelty and the emptiness are the same fact.** That is the
sentence the note needs and does not have.

## Q2. Existential status of `eq:certsmall`

**Verdict: `eq:certsmall` is EXACTLY EQUIVALENT to `T_* > H`. It is in the
existential-equivalence class. This is a determination, not the document's
disclaimer, and the equivalence is cheaper than in any previous member of the
class.**

### Proposition A (auditor's; new here)

> Fix `nu > 0`, a divergence-free Schwartz datum `u_0`, and `0 < H < infinity`;
> let `u` be the selected maximal classical branch on `[0,T_*)`. Then
>
> > there exist a comparison field `v` on `[0,H]` as in `def:comparison` and a
> > stress `F in L^2(0,H;L^3)` with `R_v = P div F` and `Z_H < r_* nu`
>
> **if and only if** `T_* > H`.

*Proof.* (⇐, necessity of the conclusion for the hypothesis) is
`thm:certificate` itself.

(⇒, necessity of the hypothesis for the conclusion) Suppose `T_* > H`. Take
`v := u|_{[0,H]}` and `F := 0`.

- Admissibility. `T_* > H` makes `[0,H]` a compact subinterval of `[0,T_*)`,
  and the imported local package (line 85) gives `u, p in C^j([0,T];H^k)` for
  all `j,k` on every such interval. So `v` is real, solenoidal and in
  `C^j([0,H];H^k)` for every `j,k` — exactly `def:comparison`.
- Residual. `u` solves the projected equation, so
  `R_v = u_t + P((u.grad)u) - nu Delta u = 0 = P div 0`, and `F = 0` lies in
  `L^2(0,H;L^3)`.
- Certificate value. `Q_0 = Q(u_0 - v(0)) = Q(0) = 0`, and `M_H < infinity`
  because `t -> ||v(t)||_6` is continuous on the compact `[0,H]`. Hence
  `Z_H^2 = e^{2M_H/3}[0 + 0] = 0 < r_* nu`, strictly, since `r_* nu > 0`. ∎

The boundary case is clean: at `T_* = H` exactly, `u` is not defined on the
closed `[0,H]`, no witness exists, and `thm:certificate` forbids one. Both
sides of the equivalence are false there.

### What this settles, and what it does not

- **The certificate is neither weaker nor stronger than regularity at the
  problem's quantifiers.** It is the fourth member of the class after HF25
  (`hf25-review-defect-criterion.md` R3, lines 517–532), HF24-B
  (`hf24-review-badset-restriction.md` Lemma A, lines 477–495) and HF26
  (`hf26-review-temporal-producer.md` Propositions A and B, lines 125–151).
- **It does not escape by the only known route.** `PLAN.md` lines 1400–1425
  records that the escape mechanism is a hypothesis whose *restricting set can
  be vacated by a blow-up* — the HF24-A corridor (`Proposition R1`,
  `hf24-review-modulus-of-continuity.md` lines 556–618). `eq:certsmall`
  restricts nothing that a blow-up can vacate: it is a bare existential over a
  class that always contains the true solution when the true solution exists,
  and `thm:certificate` closes the other direction outright. There is no
  branch `T_* <= H` in which the hypothesis can hold vacuously.
- **The necessity direction here is *cheaper* than in every previous member.**
  HF25/HF24-B/HF26 all needed the three-step "continuity on a compact ⟹ finite
  ⟹ input-only" argument. Here the witness is the solution itself and the
  certificate value is exactly `0`. That is worth recording, because it means
  the equivalence is not a subtle quantifier artefact that a sharper statement
  might dodge.
- **The document knows this and says it about the wrong object.** Line 670
  states "Existence of a successful index is equivalent to continuation, not an
  already proved weaker hypothesis" — but only for the *spectral hierarchy*, and
  only inside a remark after `thm:complete`. The general statement (Proposition
  A) is one line and is never made. The boundary section (line 843) says instead
  "no claim is made that the new criterion is logically weaker than regularity at
  the existential level", which is a refusal to claim, not the determination.
  This is exactly the posture HF26 was repaired for.
- **Consequence the note does not draw: `eq:missing` is Clay alternative A.**
  `cor:index` gives `∃N: C_N < r_*^2 nu^2  ⟹  T_* > H`; `thm:complete` gives the
  converse; so the boxed `eq:missing`
  (`∀nu ∀u_0 ∀H ∃N: C_N < r_*^2 nu^2`) is *equivalent to*
  `∀nu ∀u_0 ∀H: T_* > H`, i.e. to `T_* = infinity` always, i.e. (with the
  energy identity, which the note supplies) to `def:target`. Section
  `sec:gap`'s framing — "the single quantified inequality", "the decisive
  implication still missing" — is therefore a **restatement of the target in a
  new currency with zero logical progress**, and `sec:gap`'s two subsections
  are attempts to prove the Clay problem, not attempts to prove a lemma. The
  note is honest about not succeeding; it is not honest about what would have
  been proved if it had.
- **What is genuinely gained, stated correctly.** For a *fixed, supplied*
  comparison pair `(v,F)`, `Z_H < r_* nu` is a strictly stronger condition than
  regularity — there are regular data for which the heat comparison of
  `cor:heat` fails the test — and it is **effective**: given `(v,F,u_0,nu,H)`
  the quantity `Z_H` is a finite computation. That is the honest description,
  and it is precisely HF25 R3's "a different and more concrete mechanism, not a
  weaker statement", upgraded from *concrete* to *effective for a supplied
  comparison*. The existential form is what is equivalent; the fixed-comparison
  form is what has content. Both facts must be recorded together.

---

# Per-question findings

## Q3. `thm:certificate` Step 1 and Step 3: is the bootstrap circular?

**Verdict: not circular. The argument is the standard strict-improvement
continuity bootstrap, and the strictness it needs is present in the hypothesis.**

The pattern is: the differential inequality `eq:QerrorODE` is *derived under*
`Q^{1/3} <= r_* nu`, and *concludes* `Q^{1/3} <= Z_H`, with `Z_H < r_* nu`
**strictly** by `eq:certsmall`. The derived bound is strictly better than the
assumed one, so the exit set is empty. Written out with the quantifiers the
proof leaves implicit:

Let `J = [0, min{H,T_*})` and `S = { t in J : Q(s)^{1/3} <= r_* nu for all s <= t }`.
`Q` is `C^1` on `J` (see below), `Q_0^{1/3} <= Z_H < r_* nu`, so `S` is a
nonempty subinterval `[0,T_1)` or `[0,T_1]`. On `S`, `eq:QerrorODE` holds, so
Step 2 applies on `[0,t]` for every `t in S` and gives `Q(t)^{1/3} <= Z_H < r_* nu`
strictly. If `T_1 < min{H,T_*}`, continuity extends `Q^{1/3} < r_* nu` to a
neighbourhood of `T_1`, so `T_1` is not maximal. Hence `T_1 = min{H,T_*}` and
`eq:sharpbound` holds on all of `J`. Nothing here assumes what it derives.

Supporting facts I checked rather than assumed:

- **`Q in C^1(J)`.** `lem:basic` proves `Q` Fréchet differentiable on `L^3`
  with `DQ(a)h = <A(a),h>`; `u, v in C^j([0,T];H^k)` gives `e in C^1([0,T];L^3)`;
  `A` is continuous `L^3 -> L^{3/2}` (also `lem:basic`). So `Q' = <A(e),e_t>`
  exists and is continuous. The `e -> 0` case is not special: `A(0) = 0`.
- **Only `|K| <= nu D/4` needs the region.** The Young step for `C_v` and the
  one for the stress term are unconditional. The proof says so correctly.
- **`D >= 0`,** so discarding it in Step 2 is legitimate; and `D = 0` forces
  `nabla V = 0`, hence `V = 0` in `L^2`, hence `Q = 0` — consistent, no
  degenerate branch.
- **`eq:QerrorODE` holds a.e., not everywhere**, because the stress
  representation is only `L^2_t L^3_x`. That is enough to integrate a `C^1`
  function's derivative inequality. The identity `eq:relative` itself holds for
  *every* `t`: under `def:comparison` the residual `R_v` is automatically a
  `C^j([0,H];H^k)` function, so the pairing `<A,R_v>` is classical; only the
  *replacement* `-<A,R_v> = int nabla A : F` is a.e.
- **Step 4 is sound.** If `T_* <= H` then `T_* < infinity`, `J = [0,T_*)`, and
  `eq:ubound` gives `sup_{t<T_*} ||u(t)||_3 <= sup_{[0,H]}||v||_3 + 3^{1/3}C_3 Z_H
  < infinity`, contradicting `eq:endpoint`. `sup_{[0,H]}||v||_3 < infinity`
  because `v in C([0,H];H^k)` and `H^k` embeds in `L^3`.

### The Young step `eq:young`, verified exactly

Both inequalities are the *sharp* elementary maximisations, not lossy Young
applications. `sympy` maximisation of `a x^{3/4} - eps x` returns exactly
`27a^4/(256 eps^3)`, and of `a x^{1/2} - eps x` exactly `a^2/(4 eps)`. With
`eps = nu/4`, `256(nu/4)^3 = 4 nu^3`, so the first remainder is
`27 b^4 ||v||_6^4 Q / (4 nu^3)`; since `b^4 = 12 a_0 (1+2C_{9/2})^4` (verified
symbolically, difference exactly `0`), that is `81 a_0 (1+2C_{9/2})^4 nu^{-3}
||v||_6^4 Q = m Q`. Correct. The second gives
`a^2/nu = 2·3^{1/3} ||F||_3^2 Q^{1/3} / nu`. Correct.

The three absorbed quarters sum to `3nu D/4`, leaving `nu D/4`. Correct.

Step 2's factor: `(2/3)·(2·3^{1/3}/nu) = 4/(3^{2/3} nu)`, verified symbolically.
The integrating-factor solution and the `eps -> 0` passage are correct, and
"the right side is nondecreasing in `t` and at most `Z_H^2`" is right because
`m >= 0`.

`eq:Dbound`: integrating `eq:QerrorODE`, discarding `Q(tau) >= 0`, and using
`Q <= Z_H^3`, `Q^{1/3} <= Z_H` reproduces the displayed right-hand side exactly.

## Q4. `prop:identity`: is the relative quotient identity exact, and does the pressure cancel?

**Verdict: exact, and the pressure genuinely cancels. I derived it from scratch
and obtained `eq:relative`, `eq:Kerror` and `eq:cross` with the displayed
signs.**

Derivation (mine, independent):

1. `eq:errorPDE`. Projecting `eq:NS` removes `nabla p` (`P nabla p = 0`,
   `P u_t = u_t`, `P Delta u = Delta u`). Subtracting `eq:residual` and
   expanding `u = e + v` gives exactly the three nonlinear terms
   `(e.grad)e + (v.grad)e + (e.grad)v`. Confirmed.
2. **Pressure cancellation.** `Q' = <A, e_t>` and every `P` in the pairing is
   removable because `P A = A`: `A in L^{3/2}`, `div A = 0` (from `lem:basic`'s
   stationarity against `grad C_c^infty`), and `P` is a bounded projection on
   `L^{3/2}(R^3)` whose range is the solenoidal subspace. `P` is self-adjoint
   under `L^{3/2}`–`L^3` duality (real even symbol). So the pressure is gone
   *before* any estimate, not absorbed by one. This is genuine.
3. `<A, nu Delta e> = -nu D` by `eq:D`, finite because `A in L^{3/2}` and
   `Delta e in L^3`.
4. **`eq:zerotransport`.** With `A = rho w`, `rho = |w|`:
   `w.((b.grad)A) = rho^2 (b.grad rho) + rho w.((b.grad)w)` and
   `w.((b.grad)w) = rho (b.grad rho)`, so the integrand is
   `2 rho^2 (b.grad rho) = (2/3) b.grad(rho^3)`. Confirmed. `rho^3 in W^{1,1}`:
   `rho^3 in L^1` since `w in L^3`, and
   `||grad rho^3||_1 <= 3||rho^{3/2}||_2 ||rho^{1/2} grad rho||_2
   <= 3 ||w||_3^{3/2} D^{1/2} < infinity` by `eq:Didentity`. Cutoff:
   `|int rho^3 (b.grad chi_R)| <= C R^{-1} ||b||_infty ||w||_3^3 -> 0`. Correct.
   (Nit: the hypothesis should read "solenoidal, bounded, with bounded
   derivatives"; boundedness of `b` itself, not only of its derivatives, is what
   the cutoff estimate uses. Both `b = e` and `b = v` are bounded here, so
   nothing breaks. Repair R6.)
5. Self-convection: `-int A.((e.grad)e) = +int e.((e.grad)A)` (`div e = 0`),
   then `e = w - q` and (4) kill the `w` part, leaving `K(e) = -int q.((e.grad)A)`.
6. `v`-transport: `-int A.((v.grad)e) = +int e.((v.grad)A) = -int q.((v.grad)A)`
   by (4) with `b = v`. That is the **second** term of `eq:cross`. Sign correct.
7. Stretching: `-int A.((e.grad)v) = +int v.((e.grad)A)` by `div e = 0`. That is
   the **first** term of `eq:cross`. Sign correct.
8. Stress: with `(div F)_i = sum_j partial_j F_{ij}` and `(nabla A)_{ij} = partial_j A_i`,
   `<A, div F> = -int nabla A : F`, so `-<A,R_v> = +int nabla A : F`. Correct,
   and the index convention displayed at line 125 is the one that makes it work.

Integrability of every term: `|e|^2 |nabla A| in L^1` by
`L^3 · L^{3/2}` (`e in L^6`, `nabla A in L^{3/2}` from `prop:weighted`);
`|A||e||grad e| in L^1` by `L^{3/2} · L^3` (`e in L^infty`, `grad e in L^3`);
`nabla A : F in L^1` by `L^{3/2} · L^3`. The cutoff boundary terms are
`O(R^{-1})` times fixed `L^1` quantities. All correct.

**Nothing is missing from `eq:cross`.** The error PDE has exactly three
nonlinear terms and they map to exactly `K` plus the two displayed cross terms.

## Q5. `lem:three` and the constant dictionary

**Verdict: all three estimates and all five constants are correct. Every
Hölder split, every interpolation exponent and every arithmetic identity in
`app:checks` that bears on my scope was recomputed and agrees.**

Recomputed independently (`sympy`, exact):

| object | claimed | recomputed |
|---|---|---|
| `a_0` | `(9/8)S^2` | `||w||_9^3 = ||V||_6^2 <= S^2||nabla V||_2^2 <= (9/8)S^2 D` ✓ |
| `C_#` | `sqrt2 C_9 a_0^{1/2}` | `= (3/2) C_9 S` ✓ (symbolic identity confirmed) |
| `c_q` | `3^{1/3}(1+C_3)` | `q = (I-P)w`, `||w||_3 = (3Q)^{1/3}` ✓ |
| `b` | `sqrt2·3^{1/4} a_0^{1/4}(1+2C_{9/2})` | ✓ |
| `b^4` | `12 a_0 (1+2C_{9/2})^4` | difference exactly `0` ✓ |
| `c_b` | `81 a_0 (1+2C_{9/2})^4` | `= 27b^4/4 = 27b^4/(256(nu/4)^3)·nu^3` ✓ |
| `r_*` | `1/(4 C_# c_q)` | `= 1/(6·3^{1/3} C_9 S (1+C_3))` ✓; gives `|K| <= nu D/4` exactly at the wall ✓ |

Hölder splits: `(3,9,18,2)`, `(6,9/2,9,2)`, `(3,6,2)` — reciprocals sum to `1`
in all three cases (verified). `|| |w|^{1/2} ||_{18} = ||w||_9^{1/2}` and
`|| |w|^{1/2} ||_9 = ||w||_{9/2}^{1/2}` and `|| |w|^{1/2} ||_6 = ||w||_3^{1/2}`
are the right identities in the three cases. The shared factor
`(4/3)sqrt(9/8) = sqrt2` is exact (verified).

Interpolation for `eq:crossbound`: solving `2/9 = theta/3 + (1-theta)/9` returns
`theta = 1/2` exactly, so `||w||_{9/2}^{3/2} <= ||w||_3^{3/4}||w||_9^{3/4}
<= (3Q)^{1/4}(a_0 D)^{1/4}`. Confirmed. The sum `||e||_{9/2} + ||q||_{9/2}
<= (1 + 2C_{9/2})||w||_{9/2}` is correct (`||e||_{9/2} <= C_{9/2}||w||_{9/2}`,
`||q||_{9/2} <= (1+C_{9/2})||w||_{9/2}`).

Vector-inequality details I checked rather than assumed:
`|(b.grad)A| <= |b| |nabla A|_F` (Cauchy–Schwarz per component) and
`|nabla A : F| <= |nabla A|_F |F|_F`. Both hold with the Frobenius convention
declared at line 125.

**Dimensional cross-check.** With `[u] = L/T`, `[nu] = L^2/T`: `[Q] = L^6/T^3`,
`[D] = L^4/T^3`, `[Q'] = [nu D] = L^6/T^4`, and each of `C_# c_q Q^{1/3}D`,
`b||v||_6 Q^{1/4}D^{3/4}`, `||F||_3 Q^{1/6}D^{1/2}` has dimension `L^6/T^4`.
`[m] = 1/T`. `[Z_H] = L^2/T = [nu]`, so `Z_H < r_* nu` is dimensionally
consistent. All three estimates pass.

**Provenance (this is where the scope bites).** `eq:selfbound` is the
manuscript's `lem:qe-strain-defect` (`navier-paper/main.tex` lines 8102–8159)
transposed from `u` to `e`: same `(3,9,18,2)` split, same `eq:gradA`, same
constant — the manuscript displays `|K_u| <= (3/2) C_9 C_S ||q||_3 D_Q(u)`, and
`(3/2)C_9C_S` is exactly this note's `C_#`. The only step the manuscript does
not already own is the substitution `||q||_3 <= c_q Q^{1/3}` (it owns
`||q||_3 <= (1+C_P)||w||_3` at line 8587). `eq:crossbound` and `eq:stressbound`
**are** new.

## Q6. `prop:weighted` and Appendix A: which audited result does this reconstruct?

**Verdict: Appendix A reconstructs audited HF18-A Theorem 2 and Corollary 1(c),
(d), (f) — the same target as HF26's analogous appendix — using audited HF23
(`lem:import`) as its input. It does not reconstruct HF23. Worse, at the
revision this note pins, the whole of `prop:weighted` is already a proved
manuscript lemma, and the note says so in one place and contradicts it in
another.**

The mathematics is correct. Independently verified:

- **`eq:Vcomparison`** `(8/9)|V(a)-V(b)|^2 <= (j(a)-j(b)).(a-b) <= 2|V(a)-V(b)|^2`.
  Both middle and outer quantities are affine in the angle cosine `c`
  (`sympy`: second derivatives in `c` are identically zero), so `c = ±1`
  suffices; both endpoint arguments check out, including
  `(r^{3/2}-s^{3/2})^2 <= (9/8)(r+s)(r-s)^2` by Cauchy–Schwarz and
  `rs(r+s) <= r^3+s^3`. A `4·10^6`-point sweep over six decades gives the
  attained ratio range `[0.889146, 1.051562]`, so `8/9` is sharp and `2` is
  loose by a factor `~1.9` — matching what the HF26 audit found.
- **The monotonicity identity** `(j(x)-j(y)).(x-y) = ((|x|+|y|)/2)(|x-y|^2 + (|x|-|y|)^2)`
  simplifies to `0` symbolically in general position. `eq:Bregman`'s two bounds
  `|h|^3/6 <= B(a,h) <= |a||h|^2 + |h|^3/3` were verified at 60-digit precision
  over `2·10^5` random pairs spanning ten decades (min ratio `1.175`, max ratio
  `1.000`); a naive `float64` sweep *appears* to violate both, which is pure
  catastrophic cancellation — worth recording so a later reader does not
  "refute" a correct lemma.
- **`M_h`, `W_h`, `I_h`.** Translation invariance of `G_3` gives
  `int delta_h A . delta_h q = 0`, hence `eq:finiteidentity`; `(1/2)W_h <= M_h`
  from the monotonicity identity; `M_h <= W_h^{1/2}I_h^{1/2}` from the Lipschitz
  bound and weighted Cauchy–Schwarz; `I_h <= 2||w||_3||partial_k a||_3^2`; hence
  `W_h <= 4I_h`, `M_h <= 2I_h`. All correct.
- **`||delta_h V||_2^2 <= (9/8)M_h <= (9/2)||w||_3||partial_k a||_3^2`** — new in
  HF27 relative to HF26, and correct. This route obtains `V in H^1` from
  difference quotients alone, with a constant `4.5` times better than audited
  HF18-A (1.9). A genuine, if non-load-bearing, improvement on an audited
  result; it deserves to be recorded as such rather than buried.
- **The Fatou constant `4`.** HF26 was repaired (its R4) for asserting
  `int rho|partial_k w|^2 <= 4||w||_3||partial_k a||_3^2` without the fact that
  the *translated* `w` also converges a.e., without which Fatou yields `8`.
  **HF27 states exactly that missing clause** (line 906), so the constant `4` is
  now justified. R4 is discharged.
- **Chain rules and identification of the limit.** `partial_k V =
  rho^{1/2}(partial_k w + (1/2)(w/rho) partial_k rho)`, `partial_k A =
  rho partial_k w + w partial_k rho`, `|partial_k V|^2 = rho|partial_k w|^2 +
  (5/4)rho|partial_k rho|^2`, `|partial_k |V||^2 = (9/4)rho|partial_k rho|^2`,
  `partial_k A . partial_k w = rho(|partial_k w|^2 + |partial_k rho|^2)` — all
  five verified symbolically on an explicit non-symmetric smooth field, each
  difference exactly `0`, for each of the three directions. Subtracting one
  ninth of the second from the first gives exactly
  `rho(|partial_k w|^2 + |partial_k rho|^2)`, which is `eq:Didentity`. Also
  verified: `A = |V|^{1/3}V` exactly; the Jacobian of `z -> |z|^{1/3}z` has
  eigenvalues `(4/3)|z|^{1/3}` and `|z|^{1/3}`, so `eq:gradA`'s `4/3` is the
  exact operator norm; and the sharper HF22 form
  `|nabla A|^2 = rho(|nabla V|^2 + (7/9)|nabla|V||^2)` holds exactly, consistent
  with `eq:gradA`.
- **`||partial_k A||_{3/2} <= 2||w||_3^{1/2}(int rho|partial_k w|^2)^{1/2}`**:
  from `|partial_k A| <= 2 rho|partial_k w|` and Hölder `(6,2)`. Correct.
- **The generalised dominated convergence step.** `0 <= delta_h A . delta_h w
  <= 2|delta_h V|^2` from `eq:Vcomparison`; `|delta_h V|^2 -> |partial_k V|^2`
  in `L^1` because `V in H^1`; subsequence-of-subsequence closes it. Correct.
  (Technical nit: a.e. convergence "on compact sets" needs one diagonal
  extraction before Fatou/Vitali on `R^3`. HF26 was equally loose; not a
  regression, but see R7.)

### What this actually is

| HF27 object | already-audited counterpart | already in the pinned manuscript |
|---|---|---|
| `lem:import` (`5/4`, `1/4`, `w,q in L^6 ∩ W^{1,2}_loc`, no `w in L^2`) | HF23 `thm:main` (PASS, `hf23-review-regularity-core.md`) | `prop:quotient-divcurl`, lines 5818–5849 — **verbatim** |
| `eq:Didentity` (both forms), `eq:w9`, `a_0 = (9/8)S^2`, `V in H^1` | HF18-A Theorem 2 (2.1)–(2.2) + Corollary 1(a) (PASS) | `lem:qe-weighted-dissipation`, lines 7233–7275 — **verbatim, with `a_0 = 9C_S^2/8`** |
| `eq:gradA` | HF18-A Corollary 1(c),(d) (1.11) | `eq:qe-Agrad-V`, line 8136 |
| `eq:chainVsquared`, `eq:chainr`, `eq:chainAdot` | HF18-A Corollary 1(f) (1.12) | inside `lem:qe-weighted-dissipation` |
| `eq:Vcomparison` | HF18-A (1.6) with the sharper `8/9`/`2` pair | manuscript line 7424 |
| `eq:selfbound` (up to `c_q`) | — | `lem:qe-strain-defect`, lines 8102–8159, same constant |
| `prop:identity`, `eq:crossbound`, `eq:stressbound`, `thm:certificate`, `cor:direct` | — | **not present; genuinely new** |

So Appendix A is a *third* independent reconstruction of HF18-A Theorem 2 in
this programme (HF18-A itself, HF26's `app:weighted`, HF27's `app:weighted`),
and the second one to be produced *after* the result was already imported into
the manuscript. The note itself records the import at line 107 ("At the pinned
revision HF25's weighted dissipation identity ... [has] been imported into the
paper") and then classifies "Weighted spatial dissipation" in its own status
table (line 831) as "Detailed proofs supplied; self-checked candidates". Those
two sentences contradict each other, and the second is the one that would
mislead an importer into re-auditing an audited result. This is HF26's repair
R2, reproduced in a sharper form because HF27 pinned and read the manuscript
revision that already contains the lemma.

### The one genuine regression relative to HF26

`eq:chainV` contains an explicit `w/rho`, so it is valid only on `{rho > 0}`.
HF26's appendix justified the zero set explicitly ("Weak derivatives of every
component of `w` vanish almost everywhere on its zero level set, so
`nabla w = 0` a.e. on `{w = 0}` ... none of these statements is obtained by
dividing a degenerate Euler–Lagrange equation there"). HF27 replaces this with
the bare assertion "On the zero set the corresponding weak derivatives have the
zero-set values of these formulas" (line 919) plus the main-text sentence at
line 214. The fact is true and available — `w in W^{1,2}_loc` from `lem:import`
gives `nabla w = 0` a.e. on `{w = 0}` by the standard level-set theorem, and
then every displayed identity reads `0 = 0` there — but it is *exactly* the
place where the appendix's only project-level input is consumed, and the
appendix no longer says so. Repair R5.

Minor second regression: `V in L^2` is used at line 904 and never justified;
`||V||_2^2 = int|w|^3 = ||w||_3^3 < infinity` is one line and HF26 displayed it.

### Hypothesis placement (HF26's R3) is fixed

`prop:weighted` carries "Let `a` be solenoidal and belong to every `H^k`", and
`lem:import` alone carries the `H^1` statement. The appendix in fact needs only
`a in W^{1,3} ∩ W^{2,3}` plus `lem:import`, i.e. solenoidal `a in H^3`; the
hypothesis is over-strong but unambiguous and is met at every classical time.
HF26's ambiguity does not recur. (The manuscript's own version asks `H^m`,
`m >= 4`.) No extension to merely-`H^1` data is proved here, as in HF18-A and
HF26; that is inherited scope, not a new defect.

## Q7. `cor:direct` and the scaling subsection

**Verdict: both correct.**

`cor:direct`. `|<A,R_v>| <= ||A||_{3/2}||R_v||_3` with
`||A||_{3/2} = || |w|w ||_{3/2} = ||w||_3^2 = (3Q)^{2/3}` — exact, not an
estimate. Self and cross terms absorb `nu D/4` each, leaving
`Q' + (nu/2)D <= mQ + 3^{2/3}||R_v||_3 Q^{2/3}`. Multiplying by
`(1/3)(Q+eps)^{-2/3}` gives `y' <= (m/3)y + 3^{-1/3}||R_v||_3` for
`y = (Q+eps)^{1/3}`; the integrating factor and `e^{-M(s)/3} <= 1` give exactly
`eq:Zdirect`. The `r_*` wall and the exit argument are unchanged. Correct, and
deliberately lossy only in dropping `e^{-M(s)/3}`.

**Scaling.** I recomputed every claim in `eq:criticalspaces` from scratch. With
`f_lambda(t,x) = lambda^k f(lambda^2 t, lambda x)`, the time-integrated norm
`(int_0^{H/lambda^2} ||f_lambda(t)||_p^r dt)` scales as
`lambda^{r(k - 3/p) - 2}`. The exponents are:

| quantity | `(k,p,r)` | exponent |
|---|---|---|
| `v` in `L^4_t L^6_x` | `(1,6,4)` | `0` |
| `F` in `L^2_t L^3_x` | `(2,3,2)` | `0` |
| `R` in `L^1_t L^3_x` | `(3,3,1)` | `0` |
| `||e(0)||_3` | `(1,3,·)` | `0` |

All four invariant, as claimed. `R_lambda = lambda^3 R(lambda^2 t, lambda x)`
and `F_lambda = lambda^2 F(lambda^2 t, lambda x)` are the correct companions
(`div_x F_lambda = lambda^3 (div F)(lambda^2 t, lambda x)`), and `P` commutes
with dilations. The dilation `T_lambda f = lambda f(lambda·)` is an `L^3`
isometry mapping `G_3` onto itself, so `w(T_lambda a) = T_lambda w(a)` and `Q`
is invariant; `M_H`, `Q_0` and the weighted stress integral are invariant, so
`Z_H` and `Zbar_H` are invariant, and `r_* nu` is invariant because `nu` is
unchanged. **Both certificate conditions are scale-invariant.** The dimensional
identity `[Z_H] = [nu] = L^2/T` corroborates this independently.

This is a real structural advantage over a high-regularity (`H^1`) robustness
statement, whose smallness threshold degrades under rescaling. It is worth
saying explicitly, and the note does not.

**Graph attachment.** "The route joins the current graph at `CRITICAL`, by
`eq:ubound`" is accurate: `CRITICAL` (`docs/proof-graph.yaml` line 128) asks
for `M = M(nu,u_0,H)` bounding `sup ||u||_3` on `[0, min{H,T_*})`, and
`eq:ubound` supplies `M = sup_{[0,H]}||v||_3 + 3^{1/3}C_3 Z_H` **provided the
comparison is selected as a function of `(nu,u_0,H)`** — which is `eq:missing`.
Since `CRITICAL` is itself equivalent to `NS-R3` at these quantifiers
(`CONDITIONAL` forward, continuity on a compact backward), attaching there is
consistent with Q2 and with nothing being promoted.

The last sentence of the subsection — "If a certificate is produced for every
finite horizon and every admissible datum, then `T_* = infinity` ...; the
ordinary energy identity ... supplies `eq:Clay`" — is correct.

---

# Required repairs

Numbering `R1`–`R9`. Every repair is an edit to the *import*, never to the
frozen `.tex`.

**R1 (decisive, statement-level).** State the existential status as a
proposition, with the witness, instead of declining to claim it. Replacement
for the boundary section's "no claim is made that the new criterion is
logically weaker than regularity at the existential level":

> **Proposition (existential status).** For fixed `nu`, `u_0`, `H`, an
> admissible pair `(v,F)` with `Z_H < r_* nu` exists **if and only if**
> `T_* > H`. Sufficiency is Theorem 4.1. Necessity: if `T_* > H`, take
> `v = u|_{[0,H]}` — admissible by the imported local package, since `[0,H]` is
> then a compact subinterval of `[0,T_*)` — and `F = 0`; then `Q_0 = 0` and
> `Z_H = 0 < r_* nu`. Hence the criterion belongs to the programme's
> existential-equivalence class, alongside the HF25 defect hypothesis, the
> HF24-B bad-set hypothesis and the HF26 temporal hypothesis, and it is not the
> HF24-A corridor exception: there is no blow-up branch in which it holds
> vacuously. Its value is that for a *supplied* comparison the test is
> effective, not that it is a weaker assumption.

**R2 (decisive, statement-level).** Record in `sec:gap` that `eq:missing` is
*equivalent to* `def:target`, not a reduction of it. The note already proves
this (`cor:index` plus `thm:complete` give `eq:equiv`; quantify over `nu, u_0, H`).
As written, `sec:gap` presents `eq:missing` as "the single quantified
inequality" still missing, and its two subsections as attempts on it; a reader
must be told that a proof of `eq:missing` would *be* Clay alternative A, so
that "attempting the missing estimate from unconditional energy" is read as an
attempt on the target and not on a lemma.

**R3 (decisive, prior art), part (a).** Say plainly, at `thm:certificate` and not only in
`sec:scope`, that the theorem is the robustness / a posteriori regularity
principle of Chernyshenko, Constantin, Robinson and Titi (Thm 3 / Cor 5),
transplanted to `R^3` and re-derived in a critical norm; that `prop:Galerkin` +
`cor:index` + `thm:complete` are that paper's Galerkin hierarchy and its
conditional eventual verification (Thms 6 and 8); and that what is new is the
norm, the domain, the scale-invariance of the threshold, and the quotient
machinery that makes a critical-norm energy method possible — not the
architecture. Add a prior-art column to the status table.

**R3, part (b).** Add the critical-norm branch, which is the
branch the note's own claimed advance lives in and which it omits entirely:
Dashti–Robinson, SIAM J. Numer. Anal. 46 (2008) 3136–3150, arXiv:math/0701341
(lower regularity, whole space in the `H^2` case, **with converse**);
Marín-Rubio–Robinson–Sadowski, J. Math. Anal. Appl. 400 (2013) 76–85
(robustness of regularity in `Ḣ^{1/2}`); Burczak–Zajączkowski, Nonlinear Anal.
RWA 31 (2016) 513–532, arXiv:1409.3485 (critical `Ḣ^α`, negative-order forcing
norm, explicit constants, scale invariance at `α = 1/2` — i.e. this note's
stated programme on the torus); and **Brunk–Giesselmann–Tscherpel,
arXiv:2509.25105 (Sept 2025)**, an a posteriori existence certificate through
the ESS `L^∞L^3` criterion, from a conditional `L^2`-and-`L^3` stability
estimate with the *same* `ν^{-3}‖v‖_6^4` Gronwall exponent and a residual in
negative Sobolev norms. The last is one year older than this note and matches
`thm:certificate` in norm, endpoint criterion, Gronwall factor and residual
topology; it differs in domain (torus), in using a direct `L^2 ∩ L^3` functional
rather than the nonlinear-Hodge quotient, and in having no converse. Also cite
the openness line for critical-space stability on `R^3` (Ponce–Racke–Sideris–Titi
1994; Gallagher–Iftimie–Planchon 2003; Auscher–Dubois–Tchamitchian 2004;
Bahouri–Chemin–Gallagher 2018), and record the repository's own
`literature/current-status.md` line 44 as the source of the CCRT
characterisation, which the note reproduces without citing it.

After these citations the residual novelty in my scope is exactly one sentence,
and it should be the one that appears: *a critical-norm a posteriori certificate
on `R^3` with a scale-invariant, explicitly constanted threshold and a proved
converse, obtained by a pressure-free relative quotient identity.* Note that
the converse clause is precisely what puts the criterion in the
existential-equivalence class (R1), so the novelty and the emptiness are the
same fact and must be stated together.

**R4 (statement-level, provenance).** Attribute `prop:weighted` and Appendix A
to audited **HF18-A** Theorem 2 (2.1)–(2.2) and Corollary 1(a),(c),(d),(f), and
record that at the pinned `navier-paper` revision the whole statement is
already the manuscript's `lem:qe-weighted-dissipation` (with `a_0 = 9C_S^2/8`),
`eq:qe-Agrad-V` and `lem:qe-strain-defect`. Do **not** file it under
"Detailed proofs supplied; self-checked candidates" in the status table: that
row contradicts the note's own line 107 and would cause an importer to
re-audit an audited, already-imported result. The one thing Appendix A adds is
the sharper `||partial_k V||_2^2 <= (9/2)||w||_3||partial_k a||_3^2`, a factor
`4.5` better than HF18-A (1.9); say that, and only that, as new.

Also correct the citation on `lem:import`: its audited source is HF23
`thm:main` and `hf23-review-regularity-core.md` (PASS). The bibliography's
`\cite{Audit}` points at `hf25-review-defect-criterion.md`, whose Scope B did
cover the HF25 note's `sec:divcurl` but is not the primary audit record for the
div–curl theorem; and `hf23-review-reconstruction-boundary.md` explicitly
certifies **no** Scope A statement, so it must not be cited for it either.

**R5 (closes a real gap in Appendix A).** Restore the zero-set justification
that HF26 had and HF27 dropped. `eq:chainV` contains `w/rho` and is valid only
on `{rho > 0}`; the sentence "On the zero set the corresponding weak
derivatives have the zero-set values of these formulas" must be replaced by:

> Since `lem:import` gives `w in W^{1,2}_loc`, `nabla w = 0` a.e. on `{w = 0}`,
> hence `nabla rho = 0`, `nabla V = 0` and `nabla A = 0` a.e. there and each
> displayed identity reads `0 = 0` on the zero set. No degenerate
> Euler–Lagrange equation is divided there.

This is the single point at which the appendix's declared project-level input
is actually consumed, so it must be visible.

**R6 (expository, closes two one-line gaps).**
(a) `eq:zerotransport`'s hypothesis should read "solenoidal, bounded, with
bounded derivatives": the cutoff estimate uses `||b||_infty`, not only bounded
derivatives. Both uses (`b = e`, `b = v`) satisfy it.
(b) Display `||V||_2^2 = int |w|^3 = ||w||_3^3 < infinity` before "Since
`V in L^2`" at line 904; as written the appendix asserts an unproved membership
(HF26 displayed it).

**R7 (expository).** In Appendix A's limit passage, say that the a.e.
convergence "on compact sets" is upgraded to a.e. convergence on `R^3` by a
diagonal extraction over an exhaustion before Fatou and the generalised
dominated convergence theorem are applied. Also note, for a later reader, that
`eq:Bregman` and `eq:Vcomparison` cannot be checked in `float64` over a wide
dynamic range — the cancellation is catastrophic and produces spurious
violations; both are correct at 60-digit precision.

**R8 (expository, tightens Step 3).** `thm:certificate` Step 3 says "If it first
failed at a classical time `t_1 <= H`". Replace by the exit-time formulation:
let `T_1 = sup{ t : Q(s)^{1/3} <= r_* nu for all s <= t }`; `eq:QerrorODE` holds
on `[0,T_1]`, `eq:sharpbound` therefore gives `Q^{1/3} <= Z_H < r_* nu` there
strictly, and continuity forbids `T_1 < min{H,T_*}`. This is what the proof
does; saying it this way makes the non-circularity checkable without
reconstruction, and makes visible that the strictness of `eq:certsmall` is
load-bearing.

**R9 (expository).** State that `eq:certsmall` is scale-invariant and that this
is a real difference from a high-regularity robustness threshold, which is not.
The scaling subsection proves the invariance of the four norms but never draws
the conclusion about the *condition*, which is the part that matters for
comparison with prior art.

---

# Refutation attempts

Eleven genuine attempts. All failed against the mathematics; three produced the
scope findings above.

**RA1. Break the Step 1/Step 3 bootstrap by circularity.** *Failed.* The
derived bound `Z_H` is *strictly* below the assumed wall `r_* nu`, and
`eq:certsmall` supplies that strictness. Reconstructed the exit-time argument
in full (Q3). Nothing assumes what it derives. What I could break is only the
*phrasing*: "if it first failed" is not the exit time (R8).

**RA2. Find a missing or mis-signed term in `eq:relative`.** *Failed.* Derived
all four terms independently from `eq:errorPDE`; the three nonlinear terms map
onto `K` plus exactly the two terms of `eq:cross`, with the displayed signs, and
`-<A,R_v> = int nabla A : F` with the note's own index convention.

**RA3. Break the pressure cancellation.** *Failed.* The cancellation is
structural: `P nabla p = 0` removes the pressure before any estimate, and
`P A = A` (from `div A = 0`, `A in L^{3/2}`, `1 < 3/2 < infinity`) removes every
remaining projector under the duality pairing. There is no absorbed pressure
term anywhere.

**RA4. Find a wrong constant.** *Failed.* All of `a_0`, `C_#`, `c_q`, `b`,
`b^4`, `c_b`, `r_*`, the two Young remainders, the Hölder splits, the
interpolation exponent, `(4/3)sqrt(9/8) = sqrt2` and the `4/(3^{2/3}nu)`
identity were recomputed symbolically. Every one agrees, and `C_# = (3/2)C_9 S`
matches the manuscript's `lem:qe-strain-defect` and the HF26 audit's
independent cross-check.

**RA5. Break `eq:Bregman` or `eq:Vcomparison` numerically.** *Failed, twice.* A
`float64` sweep over ten decades appears to violate both by many orders of
magnitude; at 60 digits the minimum ratio for the `eq:Bregman` lower bound is
`1.175` and the maximum for the upper bound is exactly `1.000`. `eq:Vcomparison`'s
attained ratio range over `4·10^6` points is `[0.889146, 1.051562]`, inside
`[8/9, 2]`. The apparent refutation is arithmetic, not mathematics (R7).

**RA6. Find a pointwise chain-rule error in the appendix.** *Failed.* All five
identities, plus `A = |V|^{1/3}V`, the exact operator norm `4/3`, and the
sharper `|nabla A|^2 = rho(|nabla V|^2 + (7/9)|nabla|V||^2)`, were checked
symbolically on an explicit non-symmetric smooth field. Every difference is
exactly zero.

**RA7. Break the scaling claim, or show the certificate is secretly
subcritical.** *Failed.* All four norms have scaling exponent exactly `0`, `Q`
is dilation-invariant because the dilation is an `L^3` isometry preserving
`G_3`, and `[Z_H] = [nu]`. The condition is genuinely critical.

**RA8. Show `eq:certsmall` is strictly stronger than regularity (i.e. escape
the equivalence class).** *SUCCEEDED in the opposite direction.* The witness
`v = u|_{[0,H]}`, `F = 0` gives `Z_H = 0`, so the existential form is equivalent
to `T_* > H` (Proposition A, Q2). I then tested the only known escape route —
HF24-A's mechanism, a restricting set a blow-up can vacate — and it does not
apply: the hypothesis is a bare existential over a class containing the true
solution, with no branch in which it can hold vacuously.

**RA9. Show the certificate is vacuous, or provable from the imported package
alone.** *Failed both ways.* It is not vacuous: `cor:heat` and `thm:oscillation`
(out of scope, but the constants they consume are in scope and check out)
exhibit data satisfying it. It is not free: for a *fixed* comparison the
condition is strictly stronger than regularity, since there are regular data
whose heat orbit fails `eq:heatcriterion`. So it is a genuine sufficient
condition that happens to be existentially equivalent to its conclusion —
exactly HF26's Proposition-B situation.

**RA10. Find a project result the appendix silently re-proves or contradicts.**
*SUCCEEDED at the level of attribution.* `prop:weighted` in its entirety, plus
`eq:gradA` and `eq:selfbound`, are already proved in the pinned manuscript
(`lem:qe-weighted-dissipation`, `eq:qe-Agrad-V`, `lem:qe-strain-defect`) and are
audited HF18-A results; `lem:import` is audited HF23 `thm:main`, verbatim, and
is also already `prop:quotient-divcurl` in the manuscript. No contradiction was
found — every constant agrees, including `a_0 = 9C_S^2/8` and `C_# = (3/2)C_9C_S`
— but the note records a false novelty and a mis-directed audit citation (R4).

**RA11. Find `thm:certificate` already in the literature.** *SUCCEEDED in
substance.* The architecture is CCRT's Theorem 3 / Corollary 5 / Theorems 6
and 8, item for item (Q1). Beyond that, four papers occupy the critical-norm
niche the note treats as open, and one of them —
Brunk–Giesselmann–Tscherpel, arXiv:2509.25105 (Sept 2025) — matches
`thm:certificate` in the working norm (`L^3`), the endpoint criterion (ESS
`L^∞L^3`), the Gronwall exponent (`ν^{-3}‖v‖_6^4`), and the residual topology
(negative Sobolev), differing only in domain, in the functional used, and in
lacking a converse. I could **not** find any result combining critical norm,
whole space, scale-invariant explicit threshold and a proved converse; that
combination survives as the residual novelty, and Q2 shows it is also what
makes the criterion existentially empty.

---

# Controller errors in the index note

`research/evidence/hf27-critical-residual-continuation.md`, as it stands after
commit `959b346` (the note was revised while this audit was running; the items
below are against the current text).

1. **The new paragraph "It settles its own logical strength" over-credits the
   document, and reverses the finding it is trying to record.** It says the
   note "does not disclaim: it *proves* the certificate hypothesis equivalent
   to the target, and the equivalence is immediate in one direction because
   taking the comparison flow to be the solution itself makes the critical
   quantity vanish ... the document says so itself rather than being caught at
   it." The mechanism is right — it is my Proposition A — but the attribution
   is wrong on three counts:
   - The document proves an equivalence only for the **spectral hierarchy**
     (`eq:equiv`, inside `thm:complete`), never for `eq:certsmall` itself.
   - The `v = u` witness for the general criterion appears **nowhere** in 996
     lines. The one sentence that mentions `v = u` (the remark after
     `thm:certificate`) points the other way: "Taking `v=u` on a merely known
     shorter interval does not provide a certificate for `H`." That is a
     warning against a misuse, not a statement of equivalence.
   - The boundary section still reads "no claim is made that the new criterion
     is logically weaker than regularity at the existential level" — which is a
     disclaimer, exactly as the note's earlier version said.
   The asymmetry is worth recording on its own: the document proved the *hard*
   version of the equivalence (via `thm:complete`'s high-regularity Galerkin
   convergence) and missed the *one-line* version. Correct the paragraph to:
   the document proves the hierarchy equivalence and concedes it in a remark;
   the general equivalence is one line and the document does not state it; the
   audit states it (Proposition A).
2. **"SURVIVING CONDITIONAL SUFFIX: ... one admissible comparison pair
   satisfying the smallness inequality gives global regularity for that
   datum."** Still overstated, and unchanged in the revision. A single
   admissible pair on `[0,H]` gives `T_* > H` only. Globality needs a
   certificate for *every* finite horizon (which is what `cor:heat` arranges via
   `eta < infinity`). Replace "global regularity for that datum" by "regularity
   past that horizon for that datum".
3. **"FIRST GAP: restated in a new currency."** Accurate as far as it goes, but
   it must be said that by the note's own `thm:complete` the restatement is
   *logically equivalent* to `def:target`, so no reduction of the gap occurred.
   As written a reader would take `eq:missing` for a new, possibly easier
   sub-problem, and would read `sec:gap`'s two subsections as attempts on a
   lemma rather than on the Clay problem.
4. **"Both pinned revisions were checked with `git rev-parse` and match
   exactly."** The note pins **three** repositories (`navier`, `navier-paper`,
   `navier-formal`). Either say which two were checked and why the third was
   not, or say three.
5. **The prior-art bullet is right to ask the question; the answer is
   substantive but materially incomplete** (Q1). The note's own conditional —
   "the novelty is at most the choice of norm and the quotient machinery" — is
   right and should be promoted to a finding, then narrowed further: the choice
   of norm is *also* prior art (Marín-Rubio–Robinson–Sadowski 2013,
   Burczak–Zajączkowski 2016, Brunk–Giesselmann–Tscherpel 2025), so the residual
   novelty is the whole-space domain, the scale-invariant explicit threshold,
   the quotient machinery, and the combination with a proved converse.
   Also: the note's praise "It names Chernyshenko, Constantin, Robinson and
   Titi ... explicitly declining to import a torus theorem" is accurate and the
   citation identifier is correct — I checked, and `math/0607181` is right.
6. **The appendix bullet is correct and was confirmed**: the analogous appendix
   reconstructs HF18-A, not HF23, and so does this one. Add the sharper fact
   the earlier case did not have: at the pinned `navier-paper` revision the
   entire statement is **already an imported manuscript lemma**
   (`lem:qe-weighted-dissipation`), and the note says so at its own line 107
   while its status table calls the same object a self-checked candidate.
7. Not an error, but a gap: the index note does not record that `eq:selfbound`
   is the manuscript's `lem:qe-strain-defect` transposed from `u` to `e`, with
   the same constant. An importer should know that in my scope only
   `prop:identity`, `eq:crossbound`, `eq:stressbound`, `thm:certificate` and
   `cor:direct` are new to the repository.

The revised note's paragraph on the backward self-similar curve (that the
citation requirement is stronger than first recorded, and that no occurrence of
the ansatz or of either author appears in 996 lines) is consistent with what I
can see from the bibliography: neither Nečas–Růžička–Šverák nor Tsai appears.
That scope is not mine and I did not verify the identification.

---

# What I did NOT check

- Sections 5–8 as statements in their own right: `cor:heat`,
  `thm:oscillation`, `prop:Galerkin`, `cor:index`, `thm:complete`,
  `prop:weakresidual`, `cor:necessary`, `thm:concentration`, `cor:weaksmall`.
  I used `cor:index`/`thm:complete` only as *given* in the Q2 corollary about
  `eq:missing`; if either is wrong, that corollary weakens but Proposition A
  does not, since Proposition A does not use them.
- The proof of `lem:import` (audited HF23, PASS elsewhere) and of the endpoint
  continuation `eq:endpoint` (audited manuscript chain through Leray–Hopf, ESS
  and the Serrin-type enstrophy bound). I checked only that HF27's statements of
  them are faithful transcriptions, which they are.
- The external references: Clay, Tao Theorem 5.4 / Corollaries 4.3 and 5.8, ESS,
  Chemin–Gallagher. I did not fetch any of them and retained no third-party PDF.
- **The prior-art reading in Q1 is second-hand and bounded.** It came from
  abstract pages, arXiv/ar5iv renderings and bibliographic metadata gathered on
  my behalf; no third-party PDF was retained. Specifically: (i) CCRT's
  Theorem 3 / eq. (21) is a two-way-corroborated reconstruction, not a literal
  transcription, and must be checked against the published paper before being
  quoted; (ii) CCRT's constant `c_m` appears never to be given explicitly, which
  I could not confirm from the source itself; (iii)
  Marín-Rubio–Robinson–Sadowski 2013 is paywalled with no preprint — I have its
  title and bibliographic data but not its theorem, so its domain and its exact
  threshold are **undetermined**, and it is the single most likely place for a
  closer match than the ones I did read; (iv) Brunk–Giesselmann–Tscherpel is
  read from its arXiv abstract and reported theorem numbers only, and its
  journal status is unknown; (v) general web search was unavailable during the
  reconnaissance, so the survey is not exhaustive and a further pass could
  surface additional whole-space a posteriori work.
- Whether the concentration curve of `thm:concentration` is the
  Nečas–Růžička–Šverák / Tsai backward self-similar object, as the revised
  index note now asserts on another audit's authority. Out of scope; I checked
  only that neither name appears in the bibliography.
- The `navier-formal` and `navier-paper` pinned commit hashes; I read the
  manuscript from the local working tree, not from the pinned revision, so the
  manuscript line numbers above are working-tree line numbers.
- Whether the `.tex` compiles, and the "small symbolic script" the note says
  accompanies its source (no such script is in this repository).
- Sharpness of `C_3`, `C_{9/2}`, `C_9`, `S`: I verified the constants as stated
  in terms of those symbols and did not substitute numerical bounds.
