# HF25: dissipation comparison, sharp defect order, and a defect criterion

Status: **UNAUDITED candidate**, imported 2026-09-06. Nothing is promoted, the
manuscript is untouched, and no graph node changes until an independent audit
returns.

Provenance. A second LaTeX continuation arrived on the work capture surface,
1293 lines, dropped 2026-09-06 10:14. The source is committed verbatim beside
this note as `hf25-beyond-hf21-continuation.tex`; the original is filed at
`~/Nextcloud/navier/navier-hf21-proof-continuation-2026-09-06.tex`. Both are
frozen by SHA-256
`3ce562bb59346fc700c522bf5e857e3500b318e283febed0c9db9b7f652c6d4f`.

It pins `navier` `b711149`, `navier-paper` `4084330` and `navier-formal`
`54f8e89`, all current at the time of writing, and it explicitly compares
against the **repaired** state of HF21-A and HF21-B rather than the superseded
versions, noting that the repository already records the removability of the
frequency split and the Gronwall term. It declares its own boundary: no
arbitrary-data endpoint-uniform bound for the target, for the signed
high-strain work, or for the new defect integral is obtained, so Clay
alternative A remains unproved by it; the components are self-checked, not
audited.

**Note for the audit.** It cites the div–curl attachment by a hash
(`12163ca4…`) that is *not* the hash of our HF23 file (`abe74421…`), and
describes it as 23 pages. The mathematical content appears to be the same
development, but the audit must not assume the two artifacts are identical,
and must check that anything HF25 attributes to the attachment matches what
our audited HF23 actually proves. HF25 states it reproves the analytic layer
it needs rather than assuming differentiability of the minimizer.

## What it claims

1. **The dissipation comparison is false, with an explicit witness**
   (`thm:counter`). A compactly supported smooth solenoidal field in the
   nonlinear-Hodge class leaves that class immediately under linear heat flow,
   giving a solenoidal Schwartz field with `D_Q(v) > D_3(v)`, and a quadratic
   lower bound on the gap over a short heat interval. This is exactly the
   explicit witness that the audited HF22-A lane identified as missing from
   its own existence argument.
2. **The superlinear defect exponent is excluded** (`thm:alpha`). The HF20
   construction rules out every exponent above one in the distance factor,
   closing the interval that HF21 and HF22-B left open, by a Lipschitz-scale
   observation.
3. **A quantitative defect criterion** (`thm:sigmacriterion`): along the
   classical branch,
   `Q' + (nu/2) D_Q <= C_sigma nu^{-3} ||div w||_2^4 Q`, with an explicit
   constant, hence an exponential bound driven by the fourth-power defect
   integral.
4. **A conditional producer for the target** (`cor:Gproducer`). If the
   fourth-power defect integral is bounded by an input-only constant,
   justified without a continuation norm, then the quotient, the dissipation
   integral and the target quantity are all bounded with explicit input-only
   constants.
5. **A critical family** (`prop:generalcriterion`) with the scaling relation
   `2/s + 3/a = 2`, a Ladyzhenskaya–Prodi–Serrin-type line stated for the
   divergence defect rather than the velocity gradient, which the note calls a
   genuine refinement in the observed quantity.
6. **The energy-only version of the target fails on actual trajectories**
   (`thm:Genergy`), ruling out an energy-only remainder but not a remainder
   depending on the full datum.

**Its own stated boundary.** The available control on the defect is
`L^2` in time from the energy identity and the div–curl estimate, while the
criterion needs `L^4` in time. The note states plainly that nothing in it
supplies that upgrade for arbitrary data, that naming the integral as an input
would be circular, and that the criterion is therefore not an unconditional
regularity theorem.

## Why this matters to the programme

If audited, it closes two of our own open sub-questions with explicit
witnesses, supplies the counterexample HF22-A could not construct, and
replaces the target inequality by a sharper and much more concrete question:
upgrade the divergence defect from square to fourth power integrability in
time. That is a single scalar quantity with a known scaling line, rather than
a joint statement about a product.

**A correction it makes to our own framing.** The plan currently says the
target inequality is "the whole of the frozen gap". HF25 points out that this
inequality is an *absolute* sufficient condition, obtained by discarding the
sign, whereas the manuscript's hypothesis is signed and permits cancellation.
So it is a stronger proof mechanism, not an algebraic restatement. The
audited HF22-D equivalence is at the level of quantifiers, where both are
equivalent to global continuation; that does not make them equivalent as
mechanisms. The plan wording should be corrected accordingly, and the audit
should confirm this reading.

## Points an audit must examine first

- The explicit witness of `thm:counter`: that the field really lies in the
  nonlinear-Hodge class, that it really leaves it under heat flow, and that
  the quadratic lower bound and its constant are as claimed. Check consistency
  with the audited HF19-D and HF22-A, which reached the same negative answer
  by a different route.
- `thm:alpha`: whether the exclusion of every superlinear exponent is
  established, and how it relates to the audited HF22-B correction that
  Lipschitz continuity refutes rather than permits such exponents.
- `thm:sigmacriterion`: the interpolation between the cubic and ninth-power
  norms, the exact Young step, the constant, and the measurability and
  integrability claims for the coefficient.
- `cor:Gproducer`: that it is genuinely conditional, that the hypothesis is
  not circular, and that the stated consequences follow with the displayed
  constants.
- `prop:generalcriterion`: the multiplier norm, the interpolation exponents,
  and the scaling relation.
- `thm:Genergy`: the uniform-in-viscosity common interval and the scaling
  back, against the audited HF20 and HF23 Scope B, which prove neighbouring
  statements; determine what is new here rather than restated.
- Whether anything attributed to the div–curl attachment matches our audited
  HF23, given the hash discrepancy noted above.

## Frontier record

**MODE / RESULT:** DISCOVER, unaudited. Two negative results with explicit
witnesses, one sharpness result, one quantitative criterion with a conditional
producer, and one trajectory-level exclusion.

**FIRST GAP:** unchanged, and sharpened. The note's own statement: the defect
is controlled in square integrability in time, the criterion needs fourth
power, and nothing here supplies the upgrade for arbitrary data.

**SURVIVING CONDITIONAL SUFFIX:** if audited, the target follows from an
input-only bound on the fourth-power defect integral, with explicit constants.

**NON-CLAIMS:** no arbitrary-data bound for the target, the signed high-strain
work, or the defect integral; no regularity or blowup result; no promotion of
any graph node; no novelty or priority claim. NS-R3 remains open.

**NEXT DISTINCT ACTION:** independent audit at a different lens, freezing the
hash above and checking the points listed above.
