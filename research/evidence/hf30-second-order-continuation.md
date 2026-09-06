# HF30: a second-order stress estimate and a defect–enstrophy resolution

Status: **UNAUDITED candidate**, imported 2026-09-06. Nothing is promoted; the
manuscript is read-only from today and is not touched.

Provenance. A sixth LaTeX continuation, 1317 lines, dropped 2026-09-06 13:20.
Committed verbatim as `hf30-second-order-continuation.tex`; original filed at
`~/Nextcloud/navier/navier-second-order-continuation-2026-09-06.tex`. Frozen by
SHA-256 `d9b92ed2eec83042fa26a869097748933e3753fb32efa35cb244f80b24a38668`.
All three pinned revisions verify with `git rev-parse`; the manuscript pin is
our own attribution commit from earlier today.

## The standing prior-art check passes, for the first time

The check instituted this morning, after the same defect recurred three times,
is **satisfied here**. This document cites Nečas, Růžička and Šverák and Tsai
with DOIs for the backward self-similar ansatz, states that it extends the
uploaded construction rather than introducing another uncredited one, and adds
that it proves the nonzero equation defect directly so that **no self-similar
nonexistence theorem is needed** — a scope statement finer than we required. It
also cites the whole-space treatment and the 2025 critical-`L^3` preprint that
our HF27 certificate audit found missing, retains our manuscript's attribution
repair, and explicitly declines to reverse our decision not to import HF27. The
feedback loop from audit to source is working.

## What it claims

1. An explicit second-derivative identity and an `N^{-3}` weighted stress
   estimate, improving the predecessor's `N^{-1}`, with a rebalanced error
   certificate.
2. A closure attempt using that budget, with an exact smallness boundary, and
   an extension of the predecessor's countermodel to a *capped* form.
3. **A quantitative resolution of the defect–enstrophy comparison** — the
   question our HF26 temporal audit raised as a lead and which the manuscript's
   scope remark leaves open in both directions. It answers **negatively on
   finite classical lifespans**: a branch cannot have finite fourth-power defect
   integral with divergent squared-enstrophy integral. It presents this as a
   consequence of the already-audited defect criterion, not a new regularity
   theorem, and proves it with direct continuation rather than the endpoint
   theorem.

## Why this one matters to our own records

If item 3 survives audit it touches the claim graph directly. The `DEFECT-L4`
gap node's review text currently records that question as "unsettled in both
directions", and that sentence would become false. The manuscript's own remark
says only that the matter is not settled *there*, which stays true, and the
manuscript is read-only in any case. **The graph is ours and would need the
repair.**

Item 3 is also the only part of the document that imports the audited
unweighted div–curl result; the main spectral development deliberately does not.
That separation should be checked rather than assumed.

## Points an audit must examine first

- The defect–enstrophy resolution: whether it genuinely follows from the audited
  criterion, whether "on finite classical lifespans" is doing hidden work, and
  whether the direct continuation route really avoids the endpoint theorem.
- Whether the `N^{-3}` estimate is real and correctly rebalanced, and whether
  the improvement over `N^{-1}` changes the arithmetic the HF28 audits settled:
  those established that the index-free bound exists precisely below an explicit
  energy–enstrophy threshold and is vacuous above it, and that the quadratic
  estimate is rate-sharp.
- The capped countermodel, against the audited predecessor: does capping
  preserve the five verified clauses, and does the parity argument for the
  nonzero defect hold?
- The existential status of the rebalanced certificate. Five of six producers
  so far are equivalent to global continuation at the quantifiers.

## Frontier record

**MODE / RESULT:** DISCOVER, unaudited. One improved weighted estimate, one
closure attempt with an exact boundary, one capped countermodel, one claimed
resolution of a previously open comparison.

**NON-CLAIMS:** the document asserts no novelty for its estimates, does not
reverse our HF27 decision, and does not claim the arbitrary-data bound. NS-R3
remains open.

**NEXT DISTINCT ACTION:** audit the defect–enstrophy resolution first, since it
alone would change the claim graph.
