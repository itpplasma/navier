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

**It states its own gap concretely, and the gap is arithmetic rather than
conceptual.** The certificate needs the discounted stress integral to obey a
*logarithmic* bound in the truncation index. What energy and Sobolev supply is
*quadratic* growth. The document says plainly that the discounted estimate
cannot fix this alone, because the outer amplification factor survives. It then
gives a countermodel of globally smooth band-limited curves sharing one datum
which satisfy the exact energy identity and the same enstrophy inequality while
concentrating logarithmically, so the scalar budgets do not decide the question.

**The obvious first audit question, given every prior wave.** Every producer
this programme has generated is equivalent to global continuation at the
quantifiers except the HF24 corridor hypothesis. Determine where this
certificate falls, and do not accept a disclaimer as an answer. The claim that
the left side contains no norm of the unknown solution is exactly the kind of
statement that has previously survived inspection of the *proof* while failing
at the *quantifiers*.

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

**FIRST GAP:** stated by the document itself and arithmetic in form. The
certificate needs a logarithmic bound in the truncation index; energy and
Sobolev give quadratic.

**NON-CLAIMS:** the document states it does not prove the certificate succeeds
for every input; no regularity or blowup result for general data; no promotion
of any graph node; and it disclaims novelty in the underlying mechanisms. NS-R3
remains open.

**NEXT DISTINCT ACTION:** independent audits at a different lens, freezing the
hash above, with the existential status as the first question.
