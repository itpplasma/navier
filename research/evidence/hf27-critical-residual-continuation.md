# HF27: a full-equation critical residual certificate

Status: **UNAUDITED candidate**, imported 2026-09-06. Nothing is promoted, the
manuscript is untouched, and no graph node changes until independent audits
return.

Provenance. A fourth LaTeX continuation arrived on the work capture surface,
996 lines, dropped 2026-09-06 11:49. The source is committed verbatim beside
this note as `hf27-critical-residual-continuation.tex`; the original is filed at
`~/Nextcloud/navier/navier-critical-residual-continuation-2026-09-06.tex`. Both
are frozen by SHA-256
`3898e9a020d31c4fc58c9f1289ea4794ec9f787b885086e411b98b0cb1f97488`.

Both pinned revisions were checked with `git rev-parse` and match exactly,
including `navier-paper` `c435bee`, which is our own HF25 import from earlier
the same day. This document is tracking the repository closely and has read the
HF25 audit and the HF26 import record.

## Why it changes direction

It abandons the object the previous three continuations worked on. Instead of
the quotient of the solution, it studies the quotient of the **error against a
comparison flow**, `Q(u - v)`, where `v` is supplied on the whole requested
horizon and its equation defect is retained and estimated. Its stated reason is
our own audited record: the temporal route needs a uniform bound on a strong
vector residual that integration in time does not supply, small measure of the
exceptional set does not bound the dissipation accumulated there, and the
concentrating curve shows scalar balances can miss a nonzero residual. So this
is a response to what the HF26 audits found, not a continuation of it.

## What it claims

1. **A critical stress-residual certificate** (`thm:certificate`). If the
   comparison flow's residual is a projected divergence of an `L^2_t L^3_x`
   stress and a single explicit critical quantity stays below an absolute
   multiple of the viscosity, then the original solution is global past the
   horizon, with explicit bounds on the error quotient, the critical norm and
   the dissipation integral.
2. **A positive test that certifies genuinely large data** (`thm:oscillation`).
   An explicit real solenoidal Schwartz family with **unbounded** critical norm
   is proved globally smooth by the certificate, for every viscosity and every
   exponent in a range, with an explicit threshold.
3. **A comparison hierarchy** (`prop:Galerkin`, `cor:index`, `thm:complete`):
   global band-limited comparisons exist for every datum, one successful index
   suffices, and certification is complete in the regular case.
4. **What energy actually supplies** (`prop:weakresidual`): unconditional
   residual convergence, but at energy level.
5. **A rigorous obstruction** (`thm:concentration`, `cor:weaksmall`): exact
   energy balance does not control the critical residual, and an arbitrarily
   small energy-level residual is still insufficient. Plus a quantitative
   dichotomy that every certificate must fail in a specific way if the solution
   is singular (`cor:necessary`).

## Controller observations (not an audit)

**It reuses HF26's curve, and the citation requirement is far stronger than
this note first said.** I recorded that the curve is the backward self-similar
ansatz and that Nečas, Růžička and Šverák and Tsai must therefore be cited.
**The audit found that understated.** The curve is not merely an instance of
that ansatz: its defining equation is *literally* the Nečas–Růžička–Šverák and
Tsai equation in the same normalisation, its profile residual is character for
character the Leray-projected Leray profile equation, and the critical time this
note tunes is exactly the energy identity every Leray profile must satisfy,
confirmed symbolically and to machine precision on a spectral computation. The
requirement is therefore not an acknowledgement of a known ansatz but of the
identical object. The audit found **zero** occurrences of the ansatz, either
author, or the profile equation in all 996 lines, and neither paper in the
bibliography. That is a prior-art defect, not an omission of courtesy.

The results also bear on the content in two ways. The published theorem that an
`L^3` weak solution of the profile equation vanishes gives the note's nonzero
residual by a one-line contrapositive, whereas the note derives it through a
heavier route resting on a source it admits it could not fetch. And the
logarithmic divergence at the critical exponent is the textbook signature of
this ansatz, so the note's message — that the energy identity is a balance and
not a rigidity — is a rediscovery of what that literature exists to
demonstrate.

**Its prior-art posture is better than its predecessors'.** It names
Chernyshenko, Constantin, Robinson and Titi for robustness and conditional
eventual verification by Galerkin approximation, and states that the version it
inspected works on a periodic cube in high Sobolev regularity, explicitly
declining to import a torus theorem to the whole space. It names Chemin and
Gallagher for oscillatory large data and calls its own family a test of the
certificate rather than a novelty claim. **This is exactly the discipline the
earlier continuations lacked, and the audit should verify it is substantive
rather than decorative.**

**It settles its own logical strength, and this note under-recorded that.** I
wrote that it merely declines to claim the criterion is weaker than regularity,
and treated the question as open for the audit. **That loses the document's
strongest honest finding.** It does not disclaim: it *proves* the certificate
hypothesis equivalent to the target, and the equivalence is immediate in one
direction because taking the comparison flow to be the solution itself makes
the critical quantity vanish. So the certificate joins the
existential-equivalence class alongside the HF25 defect hypothesis, the HF24
bad-set hypothesis and the HF26 temporal criterion, and the document says so
itself rather than being caught at it.

## Points an audit must examine first

- **The decisive prior-art question.** Is `thm:certificate` genuinely distinct
  from the Chernyshenko–Constantin–Robinson–Titi robustness principle
  transplanted to the whole space with a critical rather than a high-regularity
  norm? If it is that transplant, that must be said, and the novelty is at most
  the choice of norm and the quotient machinery.
- **The existential status of `eq:certsmall`.** Every hypothesis this programme
  has produced except one turned out equivalent to global continuation at the
  quantifiers. Determine which side this falls on, and do not accept the
  document's disclaimer as an answer.
- `thm:oscillation`: whether the family is genuinely certified by the
  certificate rather than by an argument that already implies regularity, the
  explicit threshold, and how it stands against Chemin–Gallagher, whose
  oscillatory global existence results may already cover it.
- `thm:certificate`: the Young step, the constant, and above all whether the
  argument stays inside the permitted region rather than assuming the bound it
  derives — the proof's own Step 1 says it derives the scalar inequality "only
  inside the permitted region", which is a continuation-style bootstrap and
  must be checked for circularity.
- `thm:complete` and `cor:index`: whether eventual certification is proved only
  in the regular case, as the note says, and whether the high-regularity
  convergence proof is genuinely unavailable at a hypothetical singular
  endpoint, as it also says.
- `thm:concentration` and `cor:weaksmall`: the residual's membership in the
  weak space and the divergence of both critical integrals; check against our
  audited HF26 countermodel review, which computed the same curve's scaling.
- `cor:necessary`: whether the dichotomy is genuine or vacuous.
- The appendix's weighted dissipation reconstruction against our audited HF23
  and HF18-A, noting that the HF26 audit found the analogous appendix there
  reconstructs **HF18-A**, not HF23.

## Frontier record

**MODE / RESULT:** DISCOVER, unaudited. One conditional certificate with
explicit constants, one positive certification of an unbounded-critical-norm
data family, one completeness result for a comparison hierarchy, one unconditional energy-level convergence, and two obstructions.

**Three further corrections to this note, from the audit.** Its account of the
unconditional energy-level convergence omitted that the result is available only
for exponents strictly above the one at which the obstruction is stated, and
homogeneous Sobolev spaces do not nest, so there is a genuine logical gap
between them; the audit judges it repairable, since the residual's vanishing
mean forces membership over a range that covers the needed exponent. This note
also repeated the document's description of its dichotomy as "quantitative",
which the audit found self-destructs: the bound's right side tends to zero
exactly in the only regime the document's own estimate permits. The dichotomy is
genuine but not quantitative.

**FIRST GAP:** restated in a new currency. Construct, for arbitrary data, a
comparison flow whose critical residual defeats its stability cost. The note
states plainly that "choose an accurate enough comparison" without estimating
both would assume the conclusion.

**SURVIVING CONDITIONAL SUFFIX:** if audited, one admissible comparison pair
satisfying the smallness inequality gives global regularity for that datum.

**NON-CLAIMS:** no arbitrary-data comparison; no
regularity or blowup result for general data; no promotion of any graph node;
no novelty claim for oscillatory large-data global existence or for robustness
principles. NS-R3 remains open.

**NEXT DISTINCT ACTION:** independent audits at a different lens, freezing the
hash above, with the prior-art comparison against CCRT and Chemin–Gallagher as
the first question rather than the last.
