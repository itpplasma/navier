# CP02 review: over-claim and citation audit of `subsec:related`

Status: independent review, 2026-09-05 (Europe/Vienna).
Object: the working-tree state of `/home/ert/proj/navier-paper/main.tex` and
`references.bib` (uncommitted, diffed against git HEAD `b0cebe3` /
`46541ba`), specifically the new `\subsection{Related work and the scope of
what is new}` (`subsec:related`, lines 110--206), the abstract (lines
27--68), Section 9 (`Proof boundary`, lines 6926--7000), and the diff
outside those places.
Record: `cp02-prior-art-related-work.md` (the [DI]/[MO] source table) and
`prior-art-2026-09-05-user-literature-audit.md` (unverified lead, not a
source).

MODE: editorial and bibliographic audit.  No mathematical claim of the
programme is proved, strengthened or weakened here.  No novelty or priority
is asserted; no HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION or NS-R3
result is asserted.

## VERDICT: REPAIR

Nothing in the subsection asserts priority, a "first", or a "new method";
the narrowed novelty sentence is not stronger than the record; no repository
and no ResearchGate manuscript is cited; the only self-posted manuscript
cited (`Taghizadeh2026`) is cited for existence and vocabulary with an
explicit disclaimer, not as a mathematical source; every distinction is
stated by objects (solution class, domain, what is localised, what is
absorbed vs. removed) and quantifiers (fixed vs. moving cutoff, witnesses
before $\forall\tau$); and the diff outside the subsection is exactly M1--M8
and M10 of `cp02-review-integration.md` plus one abstract rewording.  Seven
sentences overreach the [DI] record by a clause, and the three arXiv entries
lose their identifiers under `plain`.  All repairs are one-line
replacements; none changes a mathematical statement.

## 1. Claim-by-claim check of `subsec:related` against the record

Tag column: the record's own tag for the content the sentence uses.
"OK" = the sentence says no more than the tagged evidence.

| # | Manuscript sentence (paraphrased) | Record entry | Tag | Result |
|---|---|---|---|---|
| 1 | Target is Fefferman's unforced whole-space alternative; Clay lists it unsolved | §1.7 (Clay page read 2026-09-05) | [DI] | OK |
| 2 | ESS Thm 1.3 endpoint; GKP corroboration only; Tao local theory; Kato small critical data | §1.7, pre-existing; `literature/critical-criteria.md` (primary/arXiv texts opened) | [DI] | OK, unchanged from HEAD |
| 3 | Chae--Lee and Berselli--Galdi: Leray--Hopf solution with $p\in L^r_tL^s_x$, $2/r+3/s\le2$, $s>3/2$, is smooth and extends | §1.6: BG content via Pineau--Yu Thm 1 (Leray--Hopf, $u_0\in H\cap L^n$, $2/r+n/s\le2$, $s>n/2$, smooth, extends); CL content via TYD (1.6) (criterion $\int\|p\|_s^{2s/(2s-3)}<\infty$, $s>3/2$, attributed jointly) | [DI] via citing sources | **Minor over-specification** (I6): the BG data hypothesis $u_0\in L^2\cap L^3$ is dropped, and the solution class and "extends" are attributed to CL, for which the record has only the criterion form |
| 4 | Zhou 2004 gives criteria in terms of the pressure in a generic domain | §1.6: identity only, body not read | [MO] | OK at title level: the sentence restates the verified title and nothing more; the record's own instruction ("cite Math. Ann. 328 for the general fact that pressure criteria exist") is followed; the $\nabla p$ condition is correctly *not* attributed |
| 5 | Beirão da Veiga 1995: velocity-gradient class $\nabla u\in L^q_tL^p_x$, $2/q+3/p\le2$ | §1.6: content via arXiv:2102.06152, with $p\in(3/2,\infty)$ | [DI] via citing source | OK; the range $p\in(3/2,\infty)$ is omitted (optional add, I6) |
| 6 | Beirão da Veiga--Yang 2021, 2022: mixed pressure--velocity conditions in Lorentz spaces | §1.6: Part I [DI] (`hf01-source-table.md`, Thm 5.2); Part II [MO] | [DI]/[MO] | OK at title level for Part II |
| 7 | "Every statement in this line assumes finiteness or smallness of an absolute norm of $p$, $\nabla p$ or $\nabla u$ along the solution and concludes regularity" | §1.6 relation paragraph asserts this for the line, but Zhou 2004 and BdV--Yang Part II bodies were **not read** | [MO] for two of six | **Over-reach** (I4): a universal content claim over two unread bodies |
| 8 | Bradshaw--Grujić: two LP-localised criteria for Leray--Hopf weak solutions, one an LPS refinement on a window whose lower edge diverges at an initial singular time | §1.5 abstract verbatim | [DI] abstract | OK |
| 9 | "Their localised object is the velocity, and their window moves with $t$" | §1.5: the LPS-type criterion is a velocity criterion; the second criterion's object is not recorded; body [MO] | [DI] abstract / [MO] body | **Minor over-reach** (I7): "their" covers both criteria; only the LPS-type one is supported |
| 10 | TYD eq. (2.2) for $q\ge3$; at $q=3$ exactly $\tfrac13X'+\nu D_3=P_3$ at unit viscosity | §1.4 (2.2) read; checked: $(q-2)\int p\,u\cdot\nabla|u|-\int|u||\nabla|u||^2-\int|u||\nabla u|^2$ at $q=3$ | [DI] | OK |
| 11 | TYD split $\R^3$ by velocity amplitude, absorb low-velocity part into dissipation, threshold implicit in the solution's own norms, conditional criteria with a correlation coefficient | §1.4 (3.2)--(3.3), Thm 3.1 | [DI] | OK |
| 12 | "What Section 5 adds is a proof of that identity on the classical branch, in integrated form, with integrands vanishing on $\{u=0\}$" | internal; record (P) | -- | OK; descriptive, not a novelty claim |
| 13 | Yu 2026a: suitable weak solutions on parabolic cylinders; resolution lemma; exact fixed-chain depletion theorem for $G^\ell$; weighted telescoping over a finite chain | §1.1 body read | [DI] | OK |
| 14 | Yu 2026a "states that the result is unconditional **only** at fixed chain length and fixed filter length" | §1.1 Remark 4.2 verbatim: "unconditional at fixed $N$, fixed $\ell>0$, and fixed active profiles. It does not assert that … summable as $N\to\infty$" | [DI] | **Paraphrase drift** (I2): "only" is the manuscript's word, not Yu's, and "fixed active profiles" is dropped |
| 15 | Yu 2026c conditional local defect-cascade reduction; Yu 2026b audit: no unconditional single-scale domination by a signed combined-work detector | §1.3, §1.2 abstracts verbatim | [DI] abstract | OK |
| 16 | "Those results … make no assertion about $L^3(\R^3)$" | §1.1 says so for 2606.25322 (body read); for 25341 and 12756 only abstracts were read | [DI] body / [DI] abstract only | **Over-reach** (I3): a negative claim about the full content of two papers read at abstract level |
| 17 | Quotient route prior art is in `rem:quotient-related` | remark read: Sibner--Sibner, Scott, Iwaniec--Scott--Stroffolini, Kato 1990, Manna--Sritharan; "not a novelty claim … no priority" | pre-existing, `cp01-prior-art-quotient.md` | OK; the one-line summary matches the remark |
| 18 | "Several self-published manuscripts and public repositories … announce reductions of, or solutions to, the … problem, some with overlapping vocabulary such as **pressure cancellation** or a single remaining barrier \cite{Taghizadeh2026}" | §1.8 Zenodo record: title "… Reduction … to a Single Remaining Barrier"; description mentions "pressure nonlocality", not "pressure cancellation"; "cancellation/pressure absorption" comes from the **user audit**, which is not a source | [DI] record for the title only | **Unsupported attribution** (I5): the citation sits after both vocabulary items; "pressure cancellation" is not in the [DI] record for Taghizadeh |
| 19 | "None is used anywhere in this paper, none is relied on for any statement, and none is treated here as accepted mathematics" | -- | -- | OK; this is what makes the Zenodo citation admissible |
| 20 | Narrowed sentence: "To the best of our knowledge, the reduction … was not located in this form. That is a statement about the reach of a bounded literature search, not a claim of priority, and no component of the route is claimed to be new …" | §2 finding (iv): "(iv) is an absence in a bounded search and is not evidence of priority" | -- | OK; weaker than the user audit's "has not previously been isolated" and than its "plausibel originell"; every listed component is in fact cited above |

Checks on the internal side of the distinctions:

- "witnesses $J$ and $A_{\rm high}$ are quantified before $\tau$": `hyp:highpressure` (line 3635) has $J=J(\nu,u_0,H)$, $A_{\rm high}(\nu,u_0,H,J)$, "for every $0<\tau<\min\{H,T_*\}$ … the same $J$ and $A_{\rm high}$ must work for the entire interval".  Matches.
- "may not be defined through any continuation norm": not in the hypothesis statement itself but in the paragraph after `hyp:absorption` (lines 3660--3664: "A proof must establish finiteness without assuming the unknown continuation bound.  Merely defining a remainder through that supremum is circular").  Consistent; no change needed.
- "a single integer $J$ selected from $(\nu,u_0,H)$ and held fixed for the whole interval": matches `hyp:highpressure` and `def:pressure-work`.
- "$Q_J=\int p_{>J}\,\Gamma(u)$ … kept as one signed number rather than a chain, and no telescoping law for it is proved in this paper": matches `def:pressure-work` and the text after `lem:absorption-split`.

## 2. Priority language

`grep` over the whole of `main.tex` for `first`, `novel`, `new method`,
`for the first time`, `priority`, `we introduce`: the only hits outside
proof-internal ordinal uses are "not a claim of priority" (line 202), "is
not new" (lines 148, 4838 in `rem:quotient-related`), "no component of the
route is claimed to be new" (line 203), "no priority is claimed" (line
4874), "no novelty or Millennium solution is asserted" (line 6923).  The
Section 9 closing paragraph is unchanged apart from M7/M8/M10 and still
disclaims every high-pressure, high-strain, critical and absorption
estimate.

One residual: the subsection **title** "Related work and the scope of what
is new" presupposes that something is new, while its last paragraph says no
component is claimed new.  Cosmetic, but it is the one place a skimming
reader sees a novelty frame (I8).

## 3. Sources that must not be cited

- Cox (ResearchGate 397174185): not in `references.bib`, not in the text.
- `johnrobertlawson/brc-navier-stokes`, `davidkny22/navier-stokes-conditional`, `lizizatt/scratch`, `vporton/navier-stokes`, `ricalanis/navier-stokes-playresearch`: none cited; "public repositories" is mentioned generically without a reference.
- DeepMind arXiv:2509.14185: not cited.
- `Taghizadeh2026` (Zenodo, self-posted): cited once, in the "Publicly claimed proofs" paragraph, with the disclaimer of row 19.  Admissible as an existence citation; see I5 for the vocabulary clause.

## 4. Diff outside the subsection (against HEAD)

| Hunk (new line) | Content | Approved item | Match |
|---|---|---|---|
| 30--33 | abstract: "isolate the one open estimate … Hypothesis~\ref{hyp:critical}, together with two unproved sufficient conditions for it" | M1 | verbatim; `hyp:critical` exists; §9 "Open" lists exactly two hypotheses |
| 45--47 | abstract: "the cubic pressure balance, in integrated form, whose differential expression is $\frac13X'+\nu D_3=P_3$" | abstract wording | allowed; removes the duplicated "integrated … in its integrated form" |
| 110--206 | `subsec:related` | this audit | -- |
| 3451 | `lem:gamma`(c): "and Corollary~\ref{cor:Lq}" | M4 (second pointer) | verbatim |
| 3522--3523 | `prop:lowpressure` proof: normalised pressure of `prop:localtheory`(iv) and `lem:pressure-convention`(d) | M3 | verbatim |
| 3788 | `prop:existential-equivalence` Step 4: "By \eqref{eq:D3P3-bounds} and Corollary~\ref{cor:Lq}" | M2 | verbatim |
| 4263--4264 | `lem:solenoidal-density`: "this is Lemma~\ref{lem:embedding}(a),(b) applied to each component" | M5 | verbatim |
| 4513--4517 | `lem:sobolev-h1` Step 1: `lem:embedding`(a) applied to $\partial^\alpha f$, Cauchy--Schwarz parenthetical | M5 | same content, parenthetical moved after the display |
| 4844 | §8 intro: "records an analytic mechanism" | M6 | verbatim |
| 5720--5721 | `rem:quotient-scope`: "that proposition with Corollary~\ref{cor:Lq} gives" | M4 | verbatim |
| 6964--6975 | §9: "Four literature statements"; Cor 5.8 "per-horizon blow-up dichotomy …"; Cor 4.3 "identifying almost smooth $H^1$ solutions as mild solutions with the normalised pressure" | M7, M8 | verbatim |
| 6980--6983 | §9: Leray projection import, (F5), `Stein1970`, `lem:leray`(b) | M10 | verbatim; `Stein1970` exists in the bib |

No other hunk.  M9 (Mathlib entry) untouched, as permitted.  All labels
referenced by the diff (`hyp:critical`, `cor:Lq`, `eq:D3P3-bounds`,
`lem:embedding`, `lem:pressure-convention`, `subsec:quotient-conventions`,
`rem:gkp`, `rem:quotient-related`, `prop:existential-equivalence`) exist
exactly once.  `main.log` (83 pages) reports no undefined citation or
reference; `main.blg` reports 0 warnings.

`references.bib`: the twelve added keys are exactly the record's §4 block
(`Yu2026a/b/c`, `TranYuDritschel2021`, `BradshawGrujic2017`, `Zhou2004`,
`BeiraoDaVeiga1995`, `BerselliGaldi2002`, `ChaeLee2001`,
`BeiraoDaVeigaYang2021`, `BeiraoDaVeigaYang2022`, `Taghizadeh2026`), fields
verbatim.  No `Cox2025`.

## 5. Issues and exact replacements

Ordered by weight.  I1 is a bibliographic defect visible in the compiled
PDF; I2--I5 are clauses that exceed the [DI] record; I6--I8 are precision
and framing nits.  Line numbers refer to the working-tree `main.tex`.

**I1 — arXiv identifiers are not printed (`references.bib`, `Yu2026a`,
`Yu2026b`, `Yu2026c`).**  `\bibliographystyle{plain}` ignores `eprint`,
`archivePrefix` and `primaryClass`; `main.bbl` prints "Runlong Yu.
Coarse-grained resolution … {\em arXiv preprint}, 2026. Submitted 24 June
2026." with no number, so the reference is not locatable from the PDF.
Replace, in each of the three entries, the `journal` and `note` fields:

```bibtex
  journal      = {arXiv preprint},
  note         = {Submitted 24 June 2026}
```
by
```bibtex
  journal      = {arXiv preprint arXiv:2606.25322 [math.AP]},
  note         = {Submitted 24 June 2026}
```
for `Yu2026a`;
```bibtex
  journal      = {arXiv preprint arXiv:2606.25341 [math.AP]},
  note         = {Submitted 24 June 2026}
```
for `Yu2026b`;
```bibtex
  journal      = {arXiv preprint arXiv:2606.12756 [math.AP]},
  note         = {Submitted 10 June 2026}
```
for `Yu2026c`.  Keep the `eprint`/`archivePrefix`/`primaryClass` fields (harmless under `plain`, used by other styles).

**I2 — Yu Remark 4.2 paraphrase (line 174--176).**  Replace

```latex
of scales, and states that the result is unconditional only at fixed chain
length and fixed filter length.  Companion papers give a conditional local
```
by
```latex
of scales, and notes that the theorem is unconditional at fixed chain
length, fixed filter length and fixed active profiles and does not assert
summability as the chain length grows.  Companion papers give a
conditional local
```

**I3 — negative content claim about two abstract-only sources (lines
180--182).**  Replace

```latex
available in that framework \cite{Yu2026b}.  Those results concern a
filtered, local observable on space-time cylinders and make no assertion
about $L^3(\mathbb R^3)$; the object here is the unfiltered pairing
```
by
```latex
available in that framework \cite{Yu2026b}.  Those results concern a
filtered, local observable on space-time cylinders; the object here is the
unfiltered pairing
```
(The distinction survives intact: local filtered observable vs. global unfiltered pairing.)

**I4 — universal content claim over unread bodies (lines 131--133).**
Replace

```latex
\cite{BeiraoDaVeigaYang2021,BeiraoDaVeigaYang2022}.  Every statement in this
line assumes finiteness or smallness of an \emph{absolute} norm of $p$,
$\nabla p$ or $\nabla u$ along the solution and concludes regularity.
```
by
```latex
\cite{BeiraoDaVeigaYang2021,BeiraoDaVeigaYang2022}.  Each statement in this
line that we have consulted assumes finiteness or smallness of an
\emph{absolute} norm of $p$, $\nabla p$ or $\nabla u$ along the solution
and concludes regularity.
```

**I5 — "pressure cancellation" attributed to Taghizadeh by citation
placement (lines 194--196).**  Replace

```latex
the three-dimensional regularity problem, some with overlapping vocabulary
such as pressure cancellation or a single remaining barrier
\cite{Taghizadeh2026}.  None is used anywhere in this paper, none is relied
```
by
```latex
the three-dimensional regularity problem, some with overlapping vocabulary
such as a reduction to a single remaining barrier \cite{Taghizadeh2026}.
None is used anywhere in this paper, none is relied
```

**I6 — Chae--Lee / Berselli--Galdi and Beirão da Veiga precision (lines
122--128).**  Replace

```latex
Lee \cite{ChaeLee2001} and Berselli and Galdi \cite{BerselliGaldi2002} prove
that a Leray--Hopf solution with $p\in L^r_tL^s_x$, $2/r+3/s\le2$, $s>3/2$,
is smooth and extends; Zhou \cite{Zhou2004} gives criteria in terms of the
pressure in a generic domain; Beir\~ao da Veiga \cite{BeiraoDaVeiga1995}
proves the companion velocity-gradient class $\nabla u\in L^q_tL^p_x$,
$2/q+3/p\le2$; and mixed pressure--velocity conditions in Lorentz spaces are
```
by
```latex
Lee \cite{ChaeLee2001} and Berselli and Galdi \cite{BerselliGaldi2002} give
the criterion $p\in L^r_tL^s_x$, $2/r+3/s\le2$, $s>3/2$, under which a weak
solution is smooth (for Leray--Hopf solutions with $u_0\in L^2\cap L^3$ in
the latter, which then extend past the given time); Zhou \cite{Zhou2004}
gives criteria in terms of the pressure in a generic domain; Beir\~ao da
Veiga \cite{BeiraoDaVeiga1995} proves the companion velocity-gradient class
$\nabla u\in L^q_tL^p_x$, $2/q+3/p\le2$, $3/2<p<\infty$; and mixed
pressure--velocity conditions in Lorentz spaces are
```

**I7 — Bradshaw--Grujić "their localised object" (lines 144--146).**
Replace

```latex
lower edge diverges as $t$ approaches an initial singular time.  Their
localised object is the velocity, and their window moves with $t$; the object
```
by
```latex
lower edge diverges as $t$ approaches an initial singular time.  In that
criterion the localised object is the velocity, and the window moves with
$t$; the object
```

**I8 — subsection title (line 110).**  Replace

```latex
\subsection{Related work and the scope of what is new}
```
by
```latex
\subsection{Related work and scope}
```

## 6. Non-issues, recorded so they are not re-raised

- Zhou 2004 is cited at title level only; the record's instruction to cite it "for the general fact that pressure … criteria exist" and not for the $\nabla p$ condition is followed.
- Beirão da Veiga--Yang Part II is cited alongside Part I at title level; the manuscript does not assert a whole-space statement for Part II.
- The `Taghizadeh2026` entry's `note` ("Self-published preprint … not peer reviewed") is supported by the Zenodo record [DI].
- `BradshawGrujic2017` `note = {Published online 21 November 2016}` is from the Crossref record [DI metadata].
- The narrowed sentence's list of components "all prior work cited above" is accurate after I2--I5: endpoint theory (row 2), pressure criteria (rows 3--7), frequency-localised criteria (row 8), cubic balance at $q=3$ (row 10), signed pressure--flux telescoping for coarse-grained observables (row 13).
- The abstract's "two unproved sufficient conditions" matches §9 "Open" (`hyp:highpressure`, `hyp:highstrain`), each implying `hyp:critical`.

## 7. Frontier record

CLAIM AND SCOPE: bibliographic and editorial.  The related-work subsection,
abstract and Section 9 were checked sentence by sentence against the [DI]/[MO]
record; the diff outside the subsection was matched hunk by hunk to M1--M8,
M10 and the abstract wording.  No mathematical statement is touched.

EVIDENCE: `git diff HEAD` of `main.tex` (11 hunks) and `references.bib`
(12 entries); `main.bbl`, `main.blg`, `main.log` of the 21:00 build;
`cp02-prior-art-related-work.md` §§0--4; `cp02-review-integration.md`
M1--M10; `hf01-source-table.md` rows for Beirão da Veiga--Yang 2021;
`literature/critical-criteria.md` for the endpoint layer; `main.tex`
`hyp:highpressure`, `hyp:absorption` and its following paragraph,
`def:pressure-work`, `rem:quotient-related`, `lem:embedding`.

FIRST GAP: I1 (arXiv numbers absent from the printed bibliography) is the
only defect a reader of the PDF would hit; I2--I5 are the only clauses that
exceed the record.  None blocks the mathematics.

NON-CLAIMS: no novelty, no priority; no HIGH-PRESSURE, HIGH-STRAIN,
CRITICAL, ABSORPTION or NS-R3 result; nothing about the content of Zhou
2004, Beirão da Veiga--Yang Part II, the Bradshaw--Grujić body, or the Cox
manuscript is asserted here beyond their verified bibliographic identity.

NEXT DISTINCT ACTION: apply I1--I8 (eight literal replacements), rebuild,
re-check `main.bbl` prints the three arXiv identifiers, then re-run
`research/verify.py`.
