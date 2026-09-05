# CP02 integration audit, round 1

Wave: CP02. Role: integration auditor. Date: 2026-09-05.
Object: `../navier-paper/main.tex` (assembled CP1 manuscript) with
`references.bib`.

## Freeze

- `sha256sum main.tex`:
  `77714b3d8bf8b7573e47d2b37d16c1390173375caa9b2eb9fdb7aed33a028263`
- `git -C ../navier-paper rev-parse HEAD`:
  `909ff21fdbf9f702668f03a3f483ac62b78daadb`
- `main.tex` is 6892 lines; it was read in full, in order.
- `docs/proof-graph.yaml` at `c1f757d` (rewritten for the assembled
  manuscript; `manuscript_commit: 909ff21…`), PLAN.md "CP01 outcome and
  binding decisions" D1–D5 and the "Exact target and conventions" quantifier
  block were used as the comparison objects.
- Nothing in either repository was edited, committed, or pushed. The
  compile below was run on a scratch copy.

## Verdict

**PASS.** No blocking issue was found. The assembled manuscript resolves
every reference, uses one set of conventions, cites the regularity package
correctly, states the two theorem shapes as PLAN and the proof graph
require, carries the manuscript's quantifiers on all four hypotheses,
justifies no step by programme notes, asserts no HIGH-PRESSURE,
HIGH-STRAIN, CRITICAL, ABSORPTION, or NS-R3 result, and the three
spot-checked proofs are complete after assembly. Ten minor issues (prose,
mis-pointers, one under-specified import list) are recorded below with
replacement text; none changes a statement, a constant, or a proof step.

## Checks in dependency order

### (1) References, citations, build

- Scratch build: `latexmk -pdf -interaction=nonstopmode -halt-on-error
  main.tex`, exit 0, `Output written on main.pdf (81 pages)`. Log: 0
  undefined references, 0 undefined citations, 0 multiply-defined labels,
  0 `LaTeX Warning` lines; BibTeX 15 entries, no warning. Overfull
  `\hbox`: 7, all below 10pt (7.31, 6.40, 6.39, 6.12, 5.44, 3.87, 1.21).
- 226 `\label`s, no duplicate (`sort | uniq -d` empty). Every
  `\ref`/`\eqref` target exists (`comm -23 refs labels` empty). Fifteen
  cite keys used, all present in `references.bib`; no key in the
  bibliography is unused.
- Semantic resolution: every cross-section pointer inspected resolves to
  the intended object. Three pointers name a true but wrong source for a
  fact proved elsewhere (M2, M3, M4 below); none affects validity.
- No `\input`/`\include`; single file as the verifier requires.

### (2) Conventions D1

Identical in every section that fixes them (§2 Conventions, §3
Conventions, §5 Conventions and `def:lp`, §6 Conventions paragraph, §8
`subsec:quotient-conventions` and Notation):

- Fourier: `f̂(ξ)=∫e^{-2πix·ξ}f(x)dx`, Tao's convention, in all five places.
- Riesz sign: symbols `-iξ_j/|ξ|`, so `R_iR_j` has symbol `-ξ_iξ_j/|ξ|^2`
  (§2 `lem:pressure-convention`, §3 `rem:scaling-pressure`, §5
  `eq:riesz-symbol`, §6, §8).
- Pressure: `p=R_iR_j(u_iu_j)=-Δ^{-1}∂_i∂_j(u_iu_j)` with `Δ^{-1}` the
  multiplier `-(4π^2|ξ|^2)^{-1}` of Tao (14); proved once in
  `lem:pressure-convention`(b),(d), restated (not re-proved) in §3, §5, §6,
  §8 (`rem:qe-pressure-normalisation`).
- Littlewood–Paley: one fixed real even bump `φ` (`def:lp`), `S_J =
  T_{φ(2^{-J}·)} = P_{≤2^J}`, homogeneous sum reconciled on `L^2` by
  `lem:lp-coincide`; §8 uses the same `S_L` and cites `def:lp`,
  `lem:lowpass-kernel`, `lem:bernstein`.
- `H^s` norm `‖(1+|ξ|^2)^{s/2}f̂‖_2` and the exact identity
  `‖f‖_{H^1}^2=‖f‖_2^2+(2π)^{-2}‖∇f‖_2^2` agree in §2 (`lem:sobolev-norms`),
  §3 (`eq:h1-norm`), §6, §8 (`eq:qe-sobolev-norm`). Heat kernel
  `(4πs)^{-3/2}e^{-|x|^2/4s}` with symbol `e^{-4π^2s|ξ|^2}` agrees in §2
  (`lem:heat`) and §8 (`def:quotient`(d)).
- D4 form of `D_3`, `P_3` through `(∇u)^T u` with zero integrands on the
  zero set: `def:D3P3`; `def:pressure-work` identifies `Γ(v)=W(v,∇v)`, so
  `P_3` is defined once.

### (3) Regularity package

- Every consumer cites `prop:localtheory` and/or `cor:Lq`: §3
  "Consequences of the local theory" and `lem:R-consequences`; §5 (R1)–(R2);
  §6 (R1)–(R4); §8 package (R) (R1)–(R3); `lem:gamma`(c),(d),
  `prop:lowpressure`, `prop:existential-equivalence`,
  `lem:quotient-lowstrain`, `prop:quotient-conditional`.
- No consumer asks for more than compact-interval `C^j([0,T];H^k)` and the
  `C([0,T];L^q)` memberships of `cor:Lq`. The `Q_{T_*}`-uniform memberships
  come from `prop:energy` only: `rem:continuation-shape` says so
  explicitly; `lem:nu-normalisation`(v) and `lem:leray-hopf` Step 0
  derive `sup‖v‖_2≤‖a‖_2` and `∫_0^{S_*}‖∇v‖_2^2≤½‖a‖_2^2` from
  `prop:energy`; `lem:serrin-enstrophy` works on `[0,T']`, `T'<T`, and takes
  the supremum; `lem:l3-to-l5` gets continuity of `‖v(s)‖_3` on `[0,S_*)`
  from compact intervals and the uniform `L^3` bound from the hypothesis;
  `prop:existential-equivalence`(A⇒B) and `cor:absorption-consequence`
  take `τ<T_*` and let the hypothesis supply the uniform remainder;
  `prop:quotient-conditional` works on `[0,τ_1]`, `τ_1<min{H,T_*}`, then
  takes the supremum; `lem:quotient-lowstrain` uses `prop:energy` for
  `‖u(t)‖_2≤‖u_0‖_2`.

### (4) Statement shapes

- `thm:continuation` (line 4551): "If `T_*<∞`, then
  `sup_{0<t<T_*}‖u(t)‖_{L^3}=∞`", with the contrapositive `eq:endpoint ⇒
  T_*=∞`. This is PLAN D3 verbatim and proof-graph node CONTINUATION
  ("If the maximal time … is finite then the supremum of its L3 norm over
  [0,Tstar) is infinite; equivalently a finite uniform L3 bound forces a
  global branch"). Proof route: `lem:nu-normalisation` → `lem:leray-hopf`
  → `thm:ess` (Theorem 1.3, numbered, verbatim) → `lem:l3-to-l5` →
  `lem:serrin-enstrophy` → (R4). No `L^3` uniqueness theorem is imported;
  `rem:gkp` is corroboration and says so. Graph `depends_on: [LOCAL,
  LERAY-HOPF, ESS, SERRIN]` matches.
- `thm:conditional` (line 4614): "If `hyp:critical` holds, then
  `def:target` holds." Proof Steps 0–5 verify Fefferman (1), (2), (3),
  (4), (6), (7) with `f≡0`, using `prop:localtheory`, `lem:global-smooth`,
  `prop:energy`, `thm:continuation`, `hyp:critical`. Graph CONDITIONAL
  `depends_on: [LOCAL, ENERGY, CONTINUATION, CRITICAL]` matches; PLAN
  table row "CONDITIONAL | thm:conditional | conditional on CRITICAL"
  matches.

### (5) Hypothesis quantifiers

Exactly four `hypothesis` environments (lines 3531, 3545, 4588, 6717).

- `hyp:highpressure`: ∃θ∈[0,1) outermost; ∀ν, ∀ divergence-free Schwartz
  `u_0`, ∀`0<H<∞`; ∃ integer `J=J(ν,u_0,H)`, ∃ finite `A_high≥0`;
  ∀`0<τ<min{H,T_*}`; "same `J` and `A_high` for the entire interval".
  Identical to PLAN "Exact target and conventions" and to graph
  HIGH-PRESSURE.
- `hyp:absorption`: ∃θ∈[0,1); ∀ν,u_0,H; ∃`A(ν,u_0,H)`; ∀τ. Matches graph
  ABSORPTION. `lem:absorption-split` produces `A=A_low(ν,u_0,H,J)+A_high`
  with `J=J(ν,u_0,H)`, so `A` depends on `(ν,u_0,H)` only, with the same θ.
- `hyp:critical`: ∀ν,u_0,H; ∃`M(ν,u_0,H)`; `sup_{0<t<min{H,T_*}}‖u‖_3≤M`.
  Matches graph CRITICAL and `eq:missing`.
- `hyp:highstrain`: ∃θ∈[0,1]; ∀ν,u_0,H; ∃`L=L(ν,u_0,H)`, ∃
  `A_input(ν,u_0,H,L)`; ∀τ. Graph HIGH-STRAIN ("theta at most one",
  input-selected cutoff, input-only remainder) matches; the manuscript
  notes that θ=1 is permitted so the θ quantifier is immaterial.
- `prop:existential-equivalence` (B⇒A) exhibits θ=0, `J=0`, and
  `A_high=∫_0^H|Q_0|`, respecting the quantifier order;
  `rem:highstrain-scope` does the same for `hyp:highstrain`.

### (6) No programme notes as justification

`grep -n -i 'evidence|PLAN.md|audited|hf[0-9][0-9]|cp0[0-9]'` returns one
hit, line 4740, in the prose introduction of §8: "This section records an
independently audited analytic mechanism, not a regularity theorem." It
is not inside a proof and justifies no step, but it appeals to an audit
the manuscript cannot exhibit (M6). No proof cites an evidence file,
PLAN, or a review. The Lean names in `rem:lean`, `rem:lean-majorant`,
`def:sobolev-constant`(b), `lem:fourier` source note and `rem:mismatch`
are cross-references, each accompanied by a paper source or a paper
proof, and `rem:lean-majorant` says the development "is not used as a
source here" (M9).

### (7) Abstract, introduction, proof boundary

- Abstract: every listed result is proved in the body at the stated
  strength (local package with `C^j([0,T];H^k)`, `H^1` blow-up; energy
  identity; scaling and `rem:mismatch`; enstrophy inequality; `prop:ode`;
  integrated cubic balance with zero-set integrands; explicit low-frequency
  bound; continuation via ν-normalisation, Leray–Hopf membership, ESS 1.3,
  Serrin-type bound; conditional Clay A; quotient functional properties and
  pressure-free evolution). It states "No arbitrary-data critical bound is
  proved here", names both unproved hypotheses, records their equivalence
  to global continuation, and says plainly "this article does not solve the
  Navier–Stokes Millennium problem, and no unconditional regularity claim
  is made." One wording tension (M1).
- §1: "This article does not prove Theorem def:target" kept verbatim;
  the purpose sentence claims one missing step, consistent with
  `hyp:critical` being the single consumer-side gap.
- §9 Proof boundary: proved / imported / open, closing with "No
  high-pressure, high-strain, critical, or absorption estimate is asserted
  anywhere in this paper, and the conditional theorems are not a solution
  of the Navier–Stokes Millennium problem." Two descriptions of imports
  are inaccurate (M7, M8) and one textbook import that the proof graph
  lists as a node is not named (M10).

### (8) Duplicates and renamed lemmas

- `lem:pressure-convention`: one, line 865 (§2). Referenced from §2
  (1064, 1125, 1231, 1235), §3 (2219), §5 (2495, 2499, 2697), §9 (6829);
  all intend the §2 lemma.
- `thm:conditional`: one statement (4614) and one proof; no second proof
  survives anywhere.
- `lem:duality` (§2, line 248, `H^k` duality): referenced only at 604,
  636, 640, 655, 679, all inside `lem:upgrade`. `lem:density` (§8, line
  4980, two density facts): referenced only at 5249, 5256, 5334, all inside
  `lem:leray`. `lem:h1-density` (§3, referenced at 1998 only) and
  `lem:solenoidal-density` (§6, referenced at 4225, 4410, 4429) carry
  distinct names.
- Other near-duplicates are section-local in every reference:
  `lem:sobolev` (2037, 2054, 2330: §3–4) vs `lem:sobolev-h1` (3856, 4160,
  4512: §6); `lem:div-zero` (1758, 2103, 2109: §3) vs `lem:divergence`
  (2773, 2955: §5); `lem:embedding` (§2 only) vs `lem:qe-embedding` (§8
  only); `lem:mollify` (§3 only) vs `lem:qe-mollify` (§8 only); `lem:heat`
  (§2) vs `lem:quotient-heat`, `lem:heat-generator` (§8).
- `eq:quotient-gap` defined once, inside `hyp:highstrain`; `sec:quotient`
  defined once.

### (9) Related work

`rem:quotient-related` attributes the mechanism to nonlinear Hodge theory
(Sibner–Sibner, Scott, Iwaniec–Scott–Stroffolini) and Kato's `L^p`
Lyapunov functionals, states that the bounded search not locating the
shifted quotient "is a statement about the reach of the search and not a
novelty claim, and no priority is claimed". `rem:highstrain-scope` and
§9 repeat "no novelty".

### (10) Three proofs end to end

**Local theory** (`lem:sobolev-norms` … `prop:localtheory`, `cor:Lq`,
`lem:sup-esssup`, `lem:global-smooth`). Steps 1–4 (ν=1, `H^1` data) build
`𝒯`, glue the `C^0_tH^1` representatives by `thm:tao54`(i),(iii) and
`lem:restriction`, obtain the blow-up alternative from `thm:tao58` applied
to `(v_0,0,S_*+1)`, and prove `𝒯=(0,S_*)`; each use of a Tao statement is
within its transcribed hypotheses. Step 5 checks Schwartz ⇒ every `H^k`
with an explicit decay integral, applies `thm:tao54`(iv), and upgrades
through `lem:upgrade`, whose five steps (scalar pairings, Lipschitz off a
null set via `lem:duality`, extension, `H^k`-differentiability, joint
smoothness via `lem:embedding`) are complete. Step 6 uses
`lem:mild-classical` with exactly the memberships Step 5 provides;
`lem:mild-classical`'s two-sided derivative of `m_ψ` on the triangle is
carried out in full. Steps 7–9 give almost-smooth uniqueness via
`thm:tao43`, pair uniqueness, and the ν-rescaling via `lem:nu-scaling`.
`cor:Lq` follows from (iii), `lem:sobolev-norms` and `lem:embedding`(a),(c).
No assembly gap.

**Continuation** (`lem:nu-normalisation` → `lem:hardy` →
`lem:solenoidal-density` → `lem:leray-hopf` → `thm:ess`/`rem:ess-norm` →
`lem:l3-to-l5` → `lem:sobolev-h1` → `lem:serrin-enstrophy` →
`thm:continuation`). ESS (1.3)–(1.7) are transcribed and verified one by
one, including the weak endpoint value `v_*∈J̊` and (1.6) at `t_0=S_*` by
lower semicontinuity; `L_{3,∞}=L^∞_tL^3_x` is fixed by the quoted (1.13)
norm. In `lem:serrin-enstrophy`: Hölder `1/5+3/10+1/2=1`; interpolation
`‖∇u‖_{10/3}≤‖∇u‖_2^{2/5}‖∇u‖_6^{3/5}` (exponents 3/2, 3 recomputed);
Sobolev on each `∂_ju_i` via `lem:sobolev-h1`; Young with 5/4, 5 giving
`C_*=(1/5)(4/5)^4C_S^3=256C_S^3/3125` (recomputed); Gronwall on `[0,T')`;
the `H^1` conclusion with the fixed norm. `thm:continuation` then
contradicts (R4). No assembly gap.

**Quotient evolution** (`lem:qe-embedding` → `lem:quotient-chainrule`
→ `lem:quotient-pressure` → `lem:heat-generator` →
`lem:quotient-heatsign` → `lem:flow` → `lem:qe-pullback` →
`lem:quotient-transport` → `prop:quotient-evolution` →
`lem:quotient-lowstrain` → `prop:quotient-conditional`). The chain rule
uses `u∈C^1([0,T];H^2)` from (R1) and `eq:qe-embedding` to get
`C^1([0,T];L^3)`, then the Fréchet remainder `eq:cp-derivative-remainder`;
`∇p∈𝒢_3` by cutoff and `lem:qe-mollify`; the heat sign by differentiating
the contraction `lem:quotient-heat`(d) at `s=0` with the generator limit
`eq:qe-generator`; the transport identity by the volume-preserving flow of
the frozen field (Liouville via `lem:qe-jacobi`), the envelope
`𝒬(u_s)≤F(w+E_sq)` with `E_s=DΦ_s^{-T}-I`, and a two-sided comparison at
`s=0`, with the signs in `eq:qe-right-expansion` and
`eq:qe-left-expansion` checked. `M_L=3(1+C_ℙ)C_B2^{5L/2}‖u_0‖_2` and
`eq:qe-M` recomputed. No assembly gap.

## Non-claim audit

The four hypotheses are the only `hypothesis` environments; each is
stated as unproved with the sentence that finiteness is the unresolved
assertion. `thm:continuation`, `thm:conditional`,
`cor:absorption-consequence`, `prop:quotient-conditional` carry their
hypotheses in the statement. `prop:existential-equivalence` and
`rem:highstrain-scope` are equivalences, not producers. `rem:quotient-scope`,
`rem:qe-heatsign-scope`, `rem:qe-evolution-scope`, `rem:highstrain-scope`
and §9 each disclaim HIGH-PRESSURE / HIGH-STRAIN / critical / absorption /
Millennium. No NS-R3 result is asserted; `def:target` is stated as a
target and "This article does not prove Theorem def:target" is retained.

## Blocking issues

None.

## Minor issues (exact location and replacement text)

M1. Abstract, line 30: "and we isolate exactly one open estimate on which
it depends" is followed by two unproved hypotheses. Replace by: "and we
isolate the one open estimate on which it depends, the finite-horizon
critical bound of Hypothesis~\ref{hyp:critical}, together with two
unproved sufficient conditions for it."

M2. Line 3684, proof of `prop:existential-equivalence`, Step 4: "By
Proposition~\ref{prop:localtheory} and Lemma~\ref{lem:gamma}(b),
$D_3(t)\le2\int|u||\nabla u|^2$" — the bound is `eq:D3P3-bounds`, not
`lem:gamma`(b). Replace by "By \eqref{eq:D3P3-bounds} and
Corollary~\ref{cor:Lq},".

M3. Line 3419, proof of `prop:lowpressure`: "(Definition~\ref{def:lp};
this is the normalised pressure of Proposition~\ref{prop:pressure})".
Replace by "(Definition~\ref{def:lp}; this is the normalised pressure of
Proposition~\ref{prop:localtheory}(iv) and
Lemma~\ref{lem:pressure-convention}(d))".

M4. Line 5616, `rem:quotient-scope`: "that proposition gives
$u\in C([0,T];L^q)$ for $2\le q\le\infty$" — the `L^q` continuity is
`cor:Lq`. Replace "that proposition gives" by "that proposition with
Corollary~\ref{cor:Lq} gives". Same pointer in `lem:gamma`(c) (line
3458 region, "By Proposition~\ref{prop:localtheory}, $u(t)\in C^1$ with
$u\in C([0,T];L^2\cap L^6)$"): insert "and Corollary~\ref{cor:Lq}" after
the proposition.

M5. Lines 4159 and 4409: `lem:solenoidal-density` Step 3 points to
"Step~1 of the proof of Lemma~\ref{lem:sobolev-h1}" and
`lem:sobolev-h1` Step 1 points to "Step~1 of the proof of
Lemma~\ref{lem:solenoidal-density}". Each proof states the computation
inline, so nothing is circular, but the mutual pointer reads as a loop.
Replace both pointers by a reference to the §2 lemma that already proves
the fact: in line 4409 replace "the computation of Step~1 of the proof of
Lemma~\ref{lem:solenoidal-density}---Cauchy--Schwarz … $\pi^2$, and
$|\xi|^m\le(1+|\xi|^2)^{m/2}$---gives" by "Lemma~\ref{lem:embedding}(a)
applied to $\partial^\alpha f$ (Cauchy--Schwarz with the weight
$(1+|\xi|^2)^{-2}$, whose integral is $\pi^2$) gives"; in line 4159
replace "this is Step~1 of the proof of Lemma~\ref{lem:sobolev-h1} applied
to each component of $v$" by "this is Lemma~\ref{lem:embedding}(a),(b)
applied to each component of $v$".

M6. Line 4740, §8 introduction: "This section records an independently
audited analytic mechanism, not a regularity theorem." Replace by "This
section records an analytic mechanism, not a regularity theorem."

M7. Lines 6862–6863, §9: "Corollary~5.8 of Tao \cite[pp.~56--57]{Tao2013}
on the maximal Cauchy development" contradicts `rem:tao-scope`(a), which
states that Corollary 5.8 contains no maximal development and that the
passage to one maximal time is the manuscript's Steps 1–4. Replace "on the
maximal Cauchy development" by "on the per-horizon blow-up dichotomy, from
which the maximal time is constructed in
Proposition~\ref{prop:localtheory}".

M8. Line 6864, §9: "its companion Corollary~4.3 \cite[p.~47]{Tao2013} on
higher regularity" — `thm:tao43` says an almost smooth `H^1` solution is a
mild solution with the normalised pressure. Replace "on higher regularity"
by "identifying almost smooth $H^1$ solutions as mild solutions with the
normalised pressure". Line 6859 "Three literature statements" then reads
better as "Four literature statements".

M9. Lines 1490–1497, 1920–1921, 2395 (and `rem:lean-majorant`): Mathlib
commit `0df444a` and companion-Lean declaration names are cited without a
bibliography entry. Either add an entry for the Mathlib snapshot to
`references.bib` (outside the approved key list; requires the controller's
consent) or keep them as they are, since each is paired with a paper
source and none is load-bearing. No text change required for PASS.

M10. §9 "Imported, not reproved": the `L^3` boundedness of the Leray
projection ((F5) of §8, Tao p. 38 and Stein 1970), which
`lem:quotient-coercive` and hence `prop:quotient-conditional` need, is a
proof-graph node (LERAY-L3, `kind: imported`) but is covered in §9 only
by the generic "standard textbook facts" clause. Append to the imported
paragraph, after "(Theorem~\ref{thm:ess}).": "The quotient section also
imports the $L^p$ boundedness of the Leray projection for $p\in\{3,3/2\}$
((F5) of \S\ref{subsec:quotient-conventions}, Calder\'on--Zygmund theory
\cite{Stein1970}), used in Lemma~\ref{lem:leray}(b)."

Presentational, no replacement required: the tags (F1)–(F6) and
(R1)–(R4) are re-used with different meanings in §5, §6 and §8 (each
section defines its own list; no LaTeX label collision, but a reader
skimming across sections may confuse §6 (F1) "Fourier package" with §8
(F1) "reflexivity"). Prefixing, e.g. (C-F1) in §6 and (Q-F1) in §8, would
remove the ambiguity.

## Proof-graph notes (repository side, not manuscript defects)

- EXISTENTIAL `depends_on: [LOW-PRESSURE, CONDITIONAL, LOCAL]`: the
  manuscript's (A⇒B) uses `lem:absorption-split` (LOW-PRESSURE,
  HIGH-PRESSURE), `prop:pressure` (PRESSURE) and `thm:continuation`
  (CONTINUATION) directly, not `thm:conditional`. Suggest `[LOW-PRESSURE,
  PRESSURE, CONTINUATION, LOCAL]`.
- QUOTIENT-EVOLUTION `depends_on: [LOCAL, QUOTIENT-FUNCTIONAL]`: the
  low-strain clause of its statement uses `prop:energy` and
  `lem:bernstein`; suggest adding ENERGY (and noting the Bernstein instance
  from LOW-PRESSURE's lemma set).
- `research/verify.py` was not re-run here; the integration notes report
  PASS at the same manuscript revision, and the sixteen structural labels
  are present once each (checked by grep).
