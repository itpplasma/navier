# HF28: a discounted spectral certificate with no unknown-solution norm

Status: **UNAUDITED candidate**, imported 2026-09-06. Nothing is promoted, the
manuscript is untouched, and no graph node changes until independent audits
return.

Provenance. A fifth LaTeX continuation arrived on the work capture surface,
1078 lines, dropped 2026-09-06 12:26. The source is committed verbatim beside
this note as `hf28-weighted-spectral-continuation.tex`; the original is filed at
`~/Nextcloud/navier/navier-weighted-spectral-continuation-2026-09-06.tex`. Both
are frozen by SHA-256
`80c6b1339704261d5540ce9620e5799f0e9c9ea7c78cd1af412d075ea8699055`.

All three pinned revisions verify with `git rev-parse`. The research pin is our
own commit from earlier the same day recording the prior-art lane's negative
headline, and the document's reads include that record, the temporal-producer
audit and the structural verifier. It also correctly hashes the HF27 artifact we
hold.

## What it claims

A certificate whose testable quantity contains **no norm of the unknown exact
solution**: for the globally defined cube-truncated comparison, an explicit
inequality in the truncation index implies continuation past the horizon, and
for nonzero data a single explicit horizon suffices for global regularity. The
gain over the previous continuation is a factor of one over the truncation
index, obtained by retaining a *discounted* stress integral rather than
estimating two factors separately.

It also gives a direct enstrophy continuation estimate, the quotient dissipation
without an unweighted div–curl premise, and continuation without the endpoint
critical-norm theorem — three dependency removals rather than new machinery.

## Controller observations (not an audit)

**It answers two of our audit findings directly.** Our HF27 certificate audit
found the entire critical-norm and whole-space branch of the robustness
literature missing; this document cites a whole-space treatment combining a
finite comparison horizon with an eventual-regularity argument, and says it is
more directly relevant than the periodic result. Our prior-art lane found the
weighted objects already named in the `p`-Laplace literature; this document
cites that framework for the natural distance, and states that the research
record warns against novelty claims for the weighted linearization. It disclaims
novelty in the underlying mechanisms explicitly.

**It states its own gap concretely. This note called that gap "arithmetic
rather than conceptual", and the audit found that wrong and load-bearing: the
gap is Clay alternative A itself.** The certificate needs the discounted stress
integral to obey a logarithmic bound in the truncation index, and the audit
computed the exact requirement. But it also proved that the inequality holds
exactly when continuation past the horizon holds, so the shortfall is neither
arithmetic nor structural — the inequality is true if and only if the conjecture
is true, and when true it holds with the integral *bounded*, not merely
logarithmic. This note also repeated as fact the document's statement that
energy and Sobolev supply only quadratic growth; the audit found that excludes
the document's own spectral enstrophy inequality, which does better. The document says plainly that the discounted estimate
cannot fix this alone, because the outer amplification factor survives. It then
gives a countermodel of globally smooth band-limited curves sharing one datum
which satisfy the exact energy identity and the same enstrophy inequality while
concentrating logarithmically, so the scalar budgets do not decide the question.

**Existential status, audited: EQUIVALENT, a fifth member of the class.** The
structural difference this note flagged is **real** — the audit confirmed that
the witness used against every previous certificate, taking the comparison to be
the solution itself, is genuinely unavailable here, because the comparison is
canonically fixed by the datum and the index and no member of the witness class
is the solution. The test really does contain no norm of the unknown solution.
Equivalence was nonetheless re-established, by theorem rather than by
substitution: the audit proved directly that some index succeeds if and only if
the branch continues past the horizon, via a bootstrap on the difference between
comparison and solution. The corridor escape is unavailable here, since every
object is defined for every input, so there is no set a singularity can vacate.

**A framing error of mine.** I wrote that the audit should "not accept a
disclaimer as an answer". That mis-describes the document, which does not
disclaim but **concedes**: it states the equivalence itself and identifies its
own membership in the class. What it omits is only the final quantifier step to
the Clay statement. It is the most honest of the five continuations on this
point, and my framing implied the opposite.

## Points an audit must examine first

- The existential status of the certificate, decided and proved, against the
  pattern above.
- Whether the factor of one over the truncation index is real, and whether it
  can ever beat the amplification factor: the document's own estimate permits
  quadratic growth where logarithmic is needed, so the audit should determine
  whether the shortfall is bridgeable in principle or structural.
- The countermodel: whether the curves really are globally smooth, band-limited,
  share the datum, satisfy the exact energy identity and the stated enstrophy
  inequality, and really concentrate logarithmically. Check it against our
  audited HF26 countermodel and HF27 concentration test, both of which used the
  backward self-similar family; this one claims to be stronger precisely by
  *not* being a curve undefined after a concentration time, so the comparison
  matters.
- The three dependency removals: continuation without the endpoint critical-norm
  theorem, the quotient dissipation without the unweighted div–curl premise, and
  the direct enstrophy estimate. Each removes a load-bearing import, so each
  must be checked to have genuinely removed it rather than relocated it.
- The prior-art claims, which are better than its predecessors' but must still
  be verified substantive rather than decorative, and the single-horizon
  reduction, which is the strongest-sounding claim in the document.

## Frontier record

**MODE / RESULT:** DISCOVER, unaudited. One certificate with no unknown-solution
norm on its testable side, three dependency removals, and one countermodel
against the scalar budgets.

**FIRST GAP:** Clay alternative A, per the audit. The certificate needs a
logarithmic bound in the truncation index, and that bound holds exactly when the
branch continues, so the gap is the target and not an arithmetic shortfall. The
audit adds that the certificate's provably-firing region today is exactly the
region where the same two estimates applied directly to the solution already
give global regularity, with the identical constant, so as a proved matter it
certifies nothing new. What is genuinely new in form is that the test quantity
is free of the unknown solution, which no previous producer achieved.

**NON-CLAIMS:** the document states it does not prove the certificate succeeds
for every input; no regularity or blowup result for general data; no promotion
of any graph node; and it disclaims novelty in the underlying mechanisms. NS-R3
remains open.

**NEXT DISTINCT ACTION:** independent audits at a different lens, freezing the
hash above, with the existential status as the first question.
