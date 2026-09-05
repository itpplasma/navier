# CP02 integration notes: the CP1 manuscript

Wave: CP02 (seven proof lanes, independently audited, one repair round).
Role: integrator. Date: 2026-09-05.

Input: the seven reviewed lane fragments in the wave scratchpad
(`local-theory.tex`, `energy-enstrophy.tex`, `pressure.tex`,
`lowpressure.tex`, `continuation.tex`, `quotient-functional.tex`,
`quotient-evolution.tex`).
Output: `../navier-paper/main.tex` (single file, all fragments **inlined**;
no `\input`, so the structural verifier scans one file) and
`../navier-paper/references.bib`.
Nothing was committed or pushed. `proof_map.tex` and
`docs/proof-graph.yaml` were not touched.

## 1. Section map

| § | Title in `main.tex` | Source |
| --- | --- | --- |
| 1 | Equation, data, and target | pre-CP02 `main.tex` §1, with the `premise:local` paragraph replaced by Part A of the local-theory lane; `eq:NS`, `def:target` unchanged |
| 2 | Local theory: the classical branch and its maximal time (`sec:localtheory`) | local-theory lane, Part B (whole) |
| 3 | Energy and scaling | energy-enstrophy lane, first section (whole) |
| 4 | The enstrophy estimate | energy-enstrophy lane, second section (whole) |
| 5 | The signed critical balance and its low-frequency part (`sec:pressure`) | pressure lane (through `rem:differential-form`), then low-pressure lane (through `lem:bernstein`), then `hyp:highpressure` / `hyp:absorption` / "These existential assertions" verbatim from pre-CP02 `main.tex`, then `lem:absorption-split` and the split paragraph (low-pressure lane) with the two surviving pre-CP02 sentences, then `prop:existential-equivalence` and `rem:existential-scope` (low-pressure lane), then `cor:absorption-consequence` with `eq:pressure-consequence` and its closing paragraph (pressure lane) |
| 6 | Endpoint continuation and the conditional theorem (`sec:continuation`) | continuation lane (whole), including the D4-protected verbatim block `hyp:critical`, `eq:missing` and the two paragraphs after it, `thm:continuation`, `thm:conditional`, `rem:gkp` |
| 7 | Compactness does not supply the bound (`sec:compactness`) | pre-CP02 `main.tex`, unchanged |
| 8 | The cubic gradient quotient (`sec:quotient`) | quotient-functional lane (whole), then quotient-evolution lane (whole) |
| 9 | Proof boundary | rewritten by the integrator (what is proved, what is imported, the two open hypotheses) |

Abstract: rewritten by the integrator. Title, author, date: unchanged.

Ordering inside §5 follows the two placement markers the lanes left: the
low-pressure lane's "the hypotheses stand here" marker and the pressure
lane's "the corollary belongs after Hypothesis absorption and the two prose
paragraphs following it".

## 2. Duplicate resolution

- **`lem:pressure-convention`**: exactly one, in §2 (local theory). The
  pressure lane had already deleted its copy in its repair round and now
  imports parts (b)-(d) plus `prop:localtheory`(iii),(iv) and `cor:Lq`.
- **`thm:conditional`**: exactly one statement and one proof, in §6
  (continuation lane). The local-theory lane's §2.3 sentence-level
  insertions into the old proof were already dropped by that lane; the new
  proof cites `lem:global-smooth` and `lem:pressure-convention`.
- **`sec:quotient`**: defined once (quotient-functional lane); the
  quotient-evolution fragment mentions it only in a stripped comment.
- **`eq:quotient-gap`**: defined once, inside `hyp:highstrain`; the
  pre-CP02 display of that label was deleted with the old §8.
- `main.tex` contains 226 `\label`s and **no duplicate label** (checked by
  `grep -o '\\label{[^}]*}' | sort | uniq -d`), and the build reports no
  multiply-defined label.

Deliberately retained near-duplicates (distinct labels, both proved, no
collision; recorded here as candidates for a later editorial pass, not as
defects):

- `lem:divergence` (§5) beside `lem:div-zero` (§3) — the same integration
  by parts, each lane self-contained.
- `lem:sobolev` (§3, all of `H^1(R^3)^m`) beside `lem:sobolev-h1` (§6,
  scalar, on the intersection of all `H^k`). `C_*` in `eq:serrin-bound` is
  the same either way.
- `eq:nu-map` (§2, arguments `(s,x)`) beside `eq:nu-normalization` (§6,
  arguments `(x,s)`); §6 states explicitly that they are the same
  substitution. `lem:nu-normalisation`(i)-(iv) restates
  `lem:nu-scaling`(a)-(d).
- Two Lean remarks, `rem:lean` (§4) and `rem:lean-majorant` (§5). Neither
  cites a bibliography key, since no key for the companion Lean development
  exists in the approved list.
- One Conventions block per section (§2, §3, §5, §6, §8). Each is used by
  its own section; they agree (Tao's Fourier convention, D1).

## 3. Deviations from the fragments

Every item below is prose, layout, or an internal-consistency pointer. **No
mathematical statement, constant, exponent, hypothesis, or proof step was
altered anywhere.**

### 3.1 Instructed by the integration spec

1. **Section titles.** §5 is "The signed critical balance and its
   low-frequency part" (lane title: "A signed critical balance"); §6 is
   "Endpoint continuation and the conditional theorem" (lane title:
   "Endpoint continuation and the missing estimate"); §8 is "The cubic
   gradient quotient" (lane title: "A quotient functional and its remaining
   strain estimate"). Bodies and labels unchanged.
2. **Abstract** rewritten to state what is proved in full and to state
   explicitly that no arbitrary-data critical bound is proved and that the
   Millennium problem is not solved.
3. **§9 Proof boundary** rewritten: proved / imported (Tao Theorem 5.4,
   Corollaries 4.3 and 5.8; ESS Theorem 1.3) / the two open hypotheses
   `hyp:highpressure` and `hyp:highstrain` with `eq:quotient-gap`.
4. **Preamble** additions only: `\newtheorem{lemma}[theorem]{Lemma}`,
   `\newtheorem{corollary}[theorem]{Corollary}`,
   `\theoremstyle{definition}\newtheorem{definition}[theorem]{Definition}\theoremstyle{plain}`,
   and `\allowdisplaybreaks` (page-breaking of long displays only).
   Existing packages and the macros `\R`, `\norm` are unchanged; no new
   macro was needed.

### 3.2 Integrator edits inside fragment text

5. **§1 closing sentence** after `def:target`: "Its purpose is to prove, in
   full, every step of a route to that conclusion except one, and to state
   the remaining estimate exactly." (pre-CP02: "identify the additional
   estimate that would turn known continuation theory into that
   conclusion"). The non-claim "This article does not prove
   Theorem~\ref{def:target}" is kept verbatim in front of it.
6. **`rem:usage`** (energy lane) pointed at "the paragraph beginning ``At
   these existential quantifiers''", which the low-pressure lane replaced
   by `prop:existential-equivalence`; and it credited `lem:sobolev` for the
   converse half, whereas the CP02 converse uses only the regularity
   package of `prop:localtheory` (Step 2 bounds `||u||_6` by continuity, not
   by Sobolev). The remark now names `def:sobolev-constant` and
   `eq:serrin-bound` as the energy-section input to the conditional chain,
   states that the converse half of `prop:existential-equivalence` does not
   use the Sobolev inequality, and points at that proposition. No result
   changed; this is a navigational statement.
7. **`def:pressure-work`** (low-pressure lane) re-displays `P_3`, which
   `def:D3P3` (pressure lane) already defines. One clause was added:
   comparing `eq:gamma` with `lem:integrands` gives `Gamma(v) = W(v, grad v)`
   pointwise, so the displayed `P_3` is the `P_3` of `def:D3P3` and not a
   second definition, while `L_J` and `Q_J` are new. This closes the pressure
   lane's open integrator item F-1/5 with the "state W = Gamma" option; no
   symbol was renamed and no display was deleted.
8. **Two lane comment lines** (`% RETAINED VERBATIM ... lane CP02-2.`,
   `% END RETAINED VERBATIM.`) removed; the text they bracketed is
   unchanged and was re-checked against pre-CP02 `main.tex` lines 393-418.
   All other fragment header comments were stripped at assembly.

### 3.3 Typographic fixes for the overfull-box budget (< 10pt)

Nine wide displays were reflowed into `gathered`/`aligned` (line breaks
substituted for `\qquad` separators or inserted at a relation symbol); the
mathematics, the order of the terms, and every symbol are identical:

- energy lane: the mollifier Cauchy-Schwarz/Tonelli display (was 18.1pt
  over);
- pressure lane: the section-constants display (16.4pt), `eq:D3P3-bounds`
  (23.7pt), the diffusion integration by parts (101.1pt), the diffusion
  assembly definitions `D_{eps,R}`, `E^d_{eps,R}` (122.5pt), the
  `|E^d_{eps,R}|` chain (42.2pt), the pressure identity with
  `P_{eps,R}`, `E^p_{eps,R}` (124.7pt), the `|E^p_{eps,R}|` chain (10.3pt).

Loose-spacing wrappers (no wording change): `\sloppy` inside `lem:compat`
(11.2pt), `sloppypar` around the §5 "regularity used" paragraph (16.3pt),
around Step 6(b) of `prop:pressure` (10.9pt), and around
`rem:lean-majorant` (14.6/39.9/21.1pt); in that remark `\allowbreak` was
inserted after each `\_` of the nine Lean identifier names and after
`(i)--`, so the identifiers can break across lines.

## 4. Bibliography

`references.bib` keeps its five entries (`Fefferman2000`, `ESS2003`,
`Kato1984`, `GKP2013`, `Tao2013`) and adds ten, all from the approved key
list and all actually cited: `Grafakos2014`, `Rudin1987`,
`SteinWeiss1971`, `Stein1970`, `Brezis2011`, `SibnerSibner1970`,
`Scott1995`, `IwaniecScottStroffolini1999`, `Kato1990`,
`MannaSritharan2007`. BibTeX processed all 15 entries with no warning and
no missing field; the printed reference list was inspected in the PDF.
No key outside the approved list is used, and no entry was invented for the
companion Lean development.

## 5. Labels defined in `main.tex` (226, by section)

**§1 (3).** `eq:NS`, `premise:local`, `def:target`

**§2 Local theory (37).** `sec:localtheory`, `subsec:conventions`,
`lem:sobolev-norms`, `lem:embedding`, `lem:duality`, `lem:heat`,
`subsec:tao`, `eq:tao-ns`, `def:tao-data`, `def:tao-mild`,
`eq:tao-pressure`, `eq:tao-duhamel`, `thm:tao54`, `thm:tao58`,
`thm:tao43`, `rem:tao-scope`, `lem:restriction`, `lem:upgrade`,
`eq:weak-scalar`, `eq:pair-fte`, `eq:lip-offN`, `eq:pair-fte-all`,
`lem:mild-classical`, `eq:mild-paired`, `eq:classical-paired`,
`eq:difference`, `eq:m-derivative`, `lem:pressure-convention`,
`lem:nu-scaling`, `eq:nu-map`, `eq:nu-duhamel`, `def:nu-mild`,
`prop:localtheory`, `cor:Lq`, `lem:sup-esssup`, `lem:global-smooth`,
`rem:continuation-shape`

**§3 Energy and scaling (27).** `lem:fourier`, `lem:parseval`,
`lem:sprime-rules`, `lem:mollify`, `lem:compat`, `lem:hk`, `eq:h1-norm`,
`lem:div-zero`, `lem:classical`, `lem:R-consequences`, `lem:plancherel`,
`def:sobolev-constant`, `eq:sobolev-cc`, `lem:h1-density`, `lem:sobolev`,
`lem:interp`, `lem:GN`, `prop:energy`, `eq:energy`,
`eq:energy-derivative`, `prop:scaling`, `eq:scaling-norm`, `eq:L4L3`,
`eq:L4L3-constant`, `rem:scaling-pressure`, `rem:mismatch`, `eq:LPS`

**§4 Enstrophy (6).** `prop:enstrophy`, `eq:enstrophy`,
`eq:enstrophy-identity`, `prop:ode`, `rem:lean`, `rem:usage`

**§5 Signed critical balance and low-frequency part (40).**
`sec:pressure`, `lem:integrands`, `def:D3P3`, `eq:D3-def`, `eq:P3-def`,
`lem:reg-calculus`, `eq:HEps-majorant`, `lem:divergence`,
`lem:diff-under-integral`, `prop:pressure`, `eq:D3P3-bounds`,
`eq:pressure-balance`, `eq:cutoff-identity`, `eq:eps-identity`,
`rem:old-form`, `rem:lean-majorant`, `rem:differential-form`, `def:lp`,
`eq:riesz-symbol`, `eq:lp-symbol`, `lem:lp-coincide`, `lem:fourier-tools`,
`lem:lowpass-kernel`, `lem:riesz-kernel`, `def:pressure-work`, `eq:gamma`,
`lem:gamma`, `prop:lowpressure`, `eq:lowpressure`,
`rem:lowpressure-constant`, `lem:bernstein`, `hyp:highpressure`,
`eq:highpressure`, `hyp:absorption`, `eq:absorption`,
`lem:absorption-split`, `prop:existential-equivalence`,
`rem:existential-scope`, `cor:absorption-consequence`,
`eq:pressure-consequence`

**§6 Endpoint continuation and the conditional theorem (25).**
`sec:continuation`, `lem:nu-normalisation`, `eq:nu-normalization`,
`eq:ess-13`, `eq:ess-14`, `eq:ess-15`, `eq:ess-16`, `eq:ess-17`,
`lem:hardy`, `lem:solenoidal-density`, `lem:leray-hopf`, `thm:ess`,
`rem:ess-norm`, `eq:ess-norm`, `lem:l3-to-l5`, `lem:sobolev-h1`,
`lem:serrin-enstrophy`, `eq:serrin-bound`,
`eq:serrin-enstrophy-identity`, `thm:continuation`, `eq:endpoint`,
`hyp:critical`, `eq:missing`, `thm:conditional`, `rem:gkp`

**§7 Compactness (1).** `sec:compactness`

**§8 The cubic gradient quotient (87).** `sec:quotient`,
`rem:quotient-related`, `subsec:quotient-conventions`, `def:quotient`,
`lem:cubic-pointwise`, `eq:cp-lipschitz`, `eq:cp-taylor`,
`eq:cp-monotone`, `eq:cp-strict`, `lem:cubic-frechet`, `eq:cp-F-taylor`,
`eq:cp-F-lipschitz`, `eq:cp-F-monotone`, `lem:density`,
`lem:quotient-minimizer`, `lem:gradient-closure`, `lem:leray`,
`eq:cp-sol-fourier`, `eq:cp-duality`, `eq:cp-gradient-rep`,
`lem:quotient-coercive`, `eq:cp-coercive`, `lem:quotient-scaling`,
`lem:quotient-heat`, `eq:cp-heat`, `lem:quotient-stability`,
`eq:cp-contraction`, `eq:cp-strong`, `eq:cp-continuity`,
`prop:quotient-derivative`, `eq:cp-derivative`,
`eq:cp-derivative-remainder`, `rem:quotient-scope`,
`subsec:qe-trajectories`, `eq:qe-sobolev-norm`, `eq:qe-frobenius`,
`eq:qe-jacobian`, `lem:qe-embedding`, `eq:qe-embedding`, `lem:qe-average`,
`lem:qe-gronwall`, `lem:qe-mollify`, `lem:quotient-pressure`,
`eq:qe-cutoff-error`, `rem:qe-pressure-normalisation`,
`lem:quotient-chainrule`, `eq:qe-chainrule`, `subsec:qe-heat`, `eq:qe-eta`,
`lem:qe-heat-continuity`, `lem:heat-generator`, `eq:qe-heat-integral`,
`eq:qe-generator`, `eq:qe-kernel-dominant`, `def:qe-dissipation`,
`lem:quotient-heatsign`, `rem:qe-heatsign-scope`, `subsec:qe-transport`,
`lem:qe-jacobi`, `lem:flow`, `eq:qe-flow-first`, `eq:qe-flow-second`,
`eq:qe-flow-inverse`, `eq:qe-taylor-b`, `rem:qe-flow-inputs`,
`lem:qe-pullback`, `lem:quotient-transport`, `eq:qe-transport`,
`eq:qe-contraction`, `eq:qe-envelope`, `eq:qe-right-expansion`,
`eq:qe-left-bounds`, `eq:qe-left-expansion`, `rem:qe-transport-scope`,
`prop:quotient-evolution`, `eq:quotient-evolution`,
`rem:qe-evolution-scope`, `subsec:qe-highstrain`, `eq:qe-bernstein`,
`lem:quotient-lowstrain`, `eq:qe-split`, `eq:qe-lowstrain`,
`hyp:highstrain`, `eq:quotient-gap`, `prop:quotient-conditional`,
`eq:qe-M`, `rem:highstrain-scope`

**§9 Proof boundary.** No new label.

All sixteen structural verifier labels survive, each exactly once:
`premise:local`, `def:target`, `prop:energy`, `prop:scaling`,
`prop:enstrophy`, `prop:ode`, `prop:pressure`, `prop:lowpressure`,
`hyp:highpressure`, `hyp:absorption`, `hyp:critical`, `thm:continuation`,
`thm:conditional`, `sec:quotient`, `eq:quotient-evolution`,
`eq:quotient-gap`. `research/verify.py` prints
`PASS: 13 claim records, acyclic dependencies, evidence and paper labels.`

## 6. Build log summary

Command: `cd ../navier-paper && latexmk -pdf -interaction=nonstopmode
-halt-on-error main.tex`.

- exit status 0; `Output written on main.pdf (81 pages, 837460 bytes)`;
  `main.tex` is 6892 lines.
- **0** undefined references, **0** undefined citations, **0**
  multiply-defined labels, **0** `LaTeX Warning` lines, **0** overfull or
  underfull `\vbox`, **0** pdfTeX warnings.
- BibTeX: 15 entries, no warning.
- Overfull `\hbox` (7, all below the 10pt budget, all inherited from the
  reviewed lane text): 7.31pt (lines 2212-2238), 6.40pt (3901-3906),
  6.39pt (3590-3599), 6.12pt (detected at 4490), 5.44pt (6321-6330),
  3.87pt (3956-3964), 1.21pt (1879-1884).
- Underfull `\hbox` (3, from the loose-spacing wrappers): badness 1019
  (2928-2935), 2762 and 4013 (2989-3002).
- Pages 1, 32, 33, 37 and 80 were inspected in the rendered PDF: title and
  abstract, the reflowed pressure displays, a low-pressure lemma page, and
  the reference list all typeset correctly.

## 7. Non-claim audit of the integrated file

- `hyp:highpressure`, `hyp:absorption`, `hyp:critical`, `hyp:highstrain`
  are the only four hypotheses, each a `hypothesis` environment, each
  stated as unproved; §9 says so again.
- No HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION, or NS-R3 result is
  asserted; the two conditional theorems (`thm:continuation`,
  `thm:conditional`) and the two conditional consequences
  (`cor:absorption-consequence`, `prop:quotient-conditional`) carry their
  hypotheses explicitly.
- `prop:existential-equivalence` and `rem:highstrain-scope` record that
  each open hypothesis is, at its own quantifiers, equivalent to the global
  continuation it is meant to produce.
- Imported literature: Tao Theorem 5.4, Corollary 4.3, Corollary 5.8; ESS
  Theorem 1.3. GKP Theorem 4 is corroboration only (`rem:gkp`). No `L^3`
  uniqueness theorem is imported.
- The quotient section carries `rem:quotient-related` (prior art) and
  claims no novelty and no priority.

## 8. Open items for the next pass (not defects)

1. Deduplicate the near-duplicates of §2 above (`lem:divergence` /
   `lem:div-zero`, `lem:sobolev` / `lem:sobolev-h1`, `eq:nu-map` /
   `eq:nu-normalization`, `lem:nu-normalisation`(i)-(iv)) if a shorter
   manuscript is wanted; each deletion needs the single-use rewrites the
   lane reports specify.
2. Decide whether both Lean remarks (`rem:lean`, `rem:lean-majorant`)
   should stay; if either is kept as a citable claim, a repository plus
   commit record must be added to `references.bib`.
3. `def:tao-mild`(b) speaks of "a smooth finite energy solution" where
   item (a) defines "smooth solution" and its `H^1` variant; the wording is
   the local-theory review's own and no mathematics depends on it.
4. The `[MO]` (metadata-only) status of the textbook facts is unchanged and
   is documented in the lane evidence files: Lieb-Loss Theorem 8.3's
   constant, Stein-Weiss chapter theorem numbers, Folland's numbers,
   Nirenberg 1959 p. 125 (2.2) behind `def:sobolev-constant`, and the
   chapter-level citations of `Rudin1987`. Only the existence of `C_S` is
   load-bearing.
