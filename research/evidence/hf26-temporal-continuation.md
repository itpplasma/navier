# HF26: weighted linearization, actual-flow defect creation, and a temporal criterion

Status: **UNAUDITED candidate**, imported 2026-09-06. Nothing is promoted, the
manuscript is untouched, and no graph node changes until independent audits
return.

Provenance. A third LaTeX continuation arrived on the work capture surface,
1432 lines, dropped 2026-09-06 10:55. The source is committed verbatim beside
this note as `hf26-temporal-continuation.tex`; the original is filed at
`~/Nextcloud/navier/navier-temporal-continuation-2026-09-06.tex`. Both are
frozen by SHA-256
`24b538280c8639b81a1f6f86d4c72370362625ca8a52d1d81a99b29236a540ab`.

It pins `navier` `a3e85f2`, `navier-paper` `34cdffd` and `navier-formal`
`54f8e89`. **All three concatenated hashes were checked against `git rev-parse`
and match exactly.** It declares its own boundary on the title page and again
in a closing subsection: the arbitrary-data endpoint-uniform producer is not
proved, the one-scale temporal residual remains an added hypothesis, and the
weaker estimate it does prove from energy does not imply it.

**Three corrections to this note, from the audit of the temporal scope
(`hf26-review-temporal-producer.md`, PASS WITH SCOPE).** First, the residue is
not "the dissipation accumulated on a small-measure exceptional set", as this
note first said, but the dissipation *weighted by the residual norm*, whose
weight is unbounded precisely there; and the measure bound holds only away from
the initial averaging layer, which contributes to the remainder with no
estimate at all. Second, the three alternatives of the conditional theorem are
not three independent routes: all three are equivalent to the target. Third,
this note's audit checklist asked only how the scale is selected; the audit
found that the hypothesis *itself* is an endpoint supremum, which is the prior
and more serious question.

## What it claims

1. **A rigorous weighted linearization** (`thm:weightedresponse`,
   `thm:Aderivative`). The difference quotients of the minimizing
   representative converge *strongly* in a fixed, possibly degenerate, weighted
   Hilbert space at the base point, and the dual field `A = |w|w` has a strong
   Hadamard derivative in `L^{3/2}`, `∂_h A(v) = M_w L_w h`. This replaces the
   *formal* linearization that the repaired HF22 projection note could only
   treat formally. The topology is part of the statement: it is not the
   unweighted `L^3` topology of the correction.
2. **Defect creation under the actual Navier–Stokes flow** (`thm:NSdeparture`).
   For the inherited explicit ellipse field, at every viscosity and every
   amplitude, data in the nonlinear-Hodge class leave it immediately under the
   *original equation*, with an explicit `t^2` rate. A corollary refutes any
   homogeneous defect-feedback law that would preserve a zero gap.

   **Audited PASS WITH SCOPE, and strengthened by the auditor**
   (`hf26-review-actual-flow-departure.md`). The document's own hedge, "except
   possibly one amplitude", is deleted: an exceptional amplitude would force a
   parity identity between an odd and an even field, hence the identically zero
   case, which the explicit nonzero value contradicts. Verified symbolically, so
   the theorem holds for *every* positive amplitude and the hedge should not be
   carried forward as a limitation. The nonzero heat-normal component, on which
   the whole theorem rests, was recomputed from scratch and agrees to forty
   digits.

   **Correction to this note.** I called this a genuine strengthening of HF19-D
   and of HF25's `thm:counter`. That is true only of the *departure* half. The
   ellipse field itself, the relevant scalar and the constant are all inherited
   from HF19-D, and HF25 supplied the quadratic rate; what is new is that the
   flow is the actual classical branch rather than a heat proxy, which
   discharges HF19-D's own stated next action, together with an exact
   coefficient in place of a single-competitor bound and explicit dependence on
   viscosity and amplitude. The dissipation-comparison half of `thm:counter` is
   untouched, since that used heat-flow identities. Reassuringly, the exact
   coefficient specialised to the heat instance reproduces HF25's constant and
   dominates it, so the two audited records agree.

   One robustness repair matters for import order: as written this section
   inherits the risk of the still-unaudited weighted linearization, but the
   auditor supplied a two-line proof of the only half the conclusion uses, so
   the section can be re-based to stand independently of it.
3. **A one-scale temporal criterion** (`thm:temporal`). If the strong `L^3`
   temporal residual of `q` against its own backward average is smaller than
   `ν/(4C♯)` at a *single* input-selected scale `δ`, then `Q`, the dissipation
   integral and the full target quantity `G` are bounded with explicit
   constants. `cor:modulus` notes that a strong **vector** modulus for
   `t ↦ q(t)` in `L^3` supplies that scale.
4. **What energy actually gives** (`thm:qtime`). An unconditional,
   input-uniform *integrated* translation estimate, **uniform in the stopping
   time**, which the audit identifies as the whole content of the estimate,
   `∫‖q(t+h) − q(t)‖_3^3 dt ≤ C_I Ω(h)^{1/2}`, with no continuation norm on the
   right. `cor:residualmeasure` converts it to a bound on the *measure* of the
   exceptional set. The note is explicit that this is an integrated bound, not
   the supremum the criterion needs, and that it does not control the
   dissipation accumulated on the exceptional set.
5. **A concentrating comparison curve** (`thm:curve`) — see the controller
   check below, which is the most consequential item for our own plan.

## Controller check of the countermodel (not an audit)

Every time slice of the curve `v(t) = S_{λ(t)} W`, `λ(t) = (1 − t/T_c)^{-1/2}`,
is a genuine solenoidal Schwartz field whose `w, q, A, Q, D, K` are its actual
variational objects. I verified its scaling algebra symbolically:

| identity | result |
|---|---|
| `λ' = λ^3/(2T_c)` | exact |
| energy identity `E' + 2νY = 0` at `T_c = E_W/(4νY_W)` | exact |
| quotient identity `Q' + νD = K` | exact, residual zero |
| `G(τ) = d_W D_W T_c log(T_c/(T_c − τ))` | diverges |
| enstrophy law `Y' = 2νY^3/(E_W Y_W)` | exact |
| HF25's `∫‖σ‖_2^4 dt` | diverges |

So the curve satisfies the exact kinetic-energy identity, the exact quotient
identity, has **constant** scalar distance `‖q(t)‖_3`, and (by
`cor:curveenstrophy`) can be made to satisfy any prescribed cubic enstrophy
bound — and yet both the target quantity `G` **and** HF25's fourth-power defect
integral diverge on it. It is not a Navier–Stokes solution; the note proves this
from the endpoint theorem and gives the explicit nonzero PDE residual, which is
invisible to both scalar tests, `⟨v, R⟩ = ⟨A(v), R⟩ = 0`.

## Why this matters to the programme

**It excludes a mechanism class we were actively pursuing.** The audit
(`hf26-review-countermodel-crossings.md`, PASS WITH SCOPE) confirmed the
algebra table above in every row and found the exclusion real but **materially
narrower than this note first stated**. Two prose overclaims of mine are
withdrawn.

*Withdrawn: "it violates nothing at the scalar level."* It violates three
things. It fails the enstrophy *identity*, which the audit computed explicitly
and which is a third scalar test that does see the residual, so the curve is
not invisible to every scalar probe. It fails any vector modulus. And it is
*forced* to keep the scaled distance at or above the viscosity, so it lives
entirely in the bad set.

*Withdrawn: the instantaneous structure plus energy plus "any scalar distance
information" cannot imply the target.* A scalar smallness threshold does
exclude the curve. The correct scope is any scalar distance *regularity,
modulus or crossing* information.

The exclusion that survives, stated exactly. No derivation of the target, or of
the signed estimate below the endpoint value of its parameter, follows from
genuine variational objects and all instantaneous identities, the two scalar
projections of the residual, energy-level budgets, any scalar modulus or
crossing information, the cubic enstrophy inequality in either form, and a
bounded critical norm. Four things are **not** excluded and one of them matters
a great deal: the signed estimate at the endpoint parameter value, which the
curve itself satisfies with zero remainder and which already suffices for the
programme. Also unexcluded are scalar smallness thresholds, vector moduli, the
enstrophy identity, and any use of the equation beyond those two projections.
Two further scope facts from the audit: the two vanishing projections are not
independent facts but the two balances restated, and the curve keeps both its
critical norm and its quotient bounded, so it refutes a *certificate* rather
than the target.

**Prior art the audit identified.** The curve is exactly the backward
self-similar ansatz; Nečas, Růžička and Šverák and later Tsai must be cited
before any import. It is also the rigorous realisation of the viscous-eddy
family sketched in the HF24 modulus lane, and the same species as the audited
HF22-C construction, which it strictly strengthens by closing two of that
construction's three named escapes and leaving only the actual equation.

**It bears directly on HF24, whose audits are in flight.** Section
`sec:crossing` argues the plan's claimed modulus/crossing-count equivalence
needs both a precise notion of crossing and an explicit choice of observed
object. It gives a smooth scalar function with a Lipschitz modulus that crosses
a fixed level infinitely often, so a modulus does **not** bound single-level
crossings; it bounds excursions between *separated* thresholds, and conversely
a finite crossing count supplies no modulus. Its producer observes the
**vector-valued** field in strong `L^3`, and `eq:scalarvector` records that the
scalar bound is the weaker one. The HF24 verdicts must be reconciled with this
before anything from that wave is promoted.

## Points an audit must examine first

- `thm:weightedresponse`: strong convergence in the degenerate weighted space,
  both signs of the perturbation, the zero-weight case, and whether the limit is
  legitimately interpreted before any `L^3` statement is made. The note warns
  that the weighted differential of `q` does **not** control its unweighted
  `L^3` differential near `w = 0`; check no step quietly uses it.
- `thm:Aderivative`: the Hadamard (not Fréchet) claim into `L^{3/2}`, and the
  density/approximation steps in `H_U`.
- `thm:NSdeparture`: the initial tangent from the projected equation, the
  `C^2(L^3)` time regularity drawn from the local package, the amplitude
  argument, and the inherited ellipse field. **This checklist omitted the prior
  question**, namely that the quadratic gap proposition depends on the weighted
  linearization of the previous section, so a failure there would propagate
  here; and it pointed the auditor at the wrong appendix, which holds the
  axisymmetric swirl seed for the comparison curve and no ellipse field at all.
- `thm:temporal`: the Young step `eq:Young34`, the constant `M_δ`, and whether
  the scale is genuinely selected before the stopping time rather than from a
  continuation norm.
- `thm:qtime`: the `dot H^{-1}` increment lemma, the interpolation
  `eq:negativeinterp`, and the claim that no continuation norm enters.
- `cor:residualmeasure`: the Jensen/Tonelli step and the deliberate restriction
  to `(δ, τ)`.
- `thm:curve`: independently of my algebra check, whether the seed field `W_0`
  with `K(W_0) > 0` in the appendix is correct, since the whole countermodel
  rests on it; and whether `cor:curveenstrophy`'s limit argument holds.
- The appendices. **Correction, from the audit: this note originally said both
  appendices reconstruct HF23 and should be checked against it. That is wrong
  for one of them.** Only the spatial appendix reconstructs HF23; the weighted
  dissipation appendix reconstructs the audited **HF18-A Theorem 2**, and
  HF23's own text disclaims needing that identity, so following the original
  instruction would have compared the appendix against a document that
  explicitly does not assert it. What is genuinely new there is narrower and
  worth stating: HF18-A's identity held only in an approximate-gradient sense
  under the then-open hypothesis (H1), and HF23's discharge of (H1) turns it
  into a genuine weak-derivative identity.
- **A notation collision to fix before any import.** The audited HF22-B already
  uses the symbol this document writes for its weighted Hilbert space to mean
  the completion of the *gradient quotient*, which is a different object here
  and corresponds to this document's other symbol. Since the linearization
  remark links the two documents, an import that preserves both notations will
  be misread.

## Frontier record

**MODE / RESULT:** DISCOVER, unaudited. One analytic upgrade (formal → strong
linearization), one actual-flow negative result, one conditional temporal
producer, one unconditional integrated modulus, and one exclusion of a
mechanism class by an exact countermodel.

**FIRST GAP:** unchanged, and re-expressed. The producer needs a supremum in
time of the strong `L^3` residual at one fixed scale; energy supplies only an
integrated version, and the gap is precisely the dissipation accumulated on a
small-measure exceptional set.

**SURVIVING CONDITIONAL SUFFIX:** if audited, the target follows from any one of
three hypotheses (`thm:fullconditional`): the one-scale residual bound, a finite
input bound for the exceptional-set remainder, or the original signed estimate.

**NON-CLAIMS:** no arbitrary-data witness for any of the three alternatives; no
regularity or blowup result; no singularity claim from the departure theorem; no
promotion of any graph node; no novelty claim for the weighted derivative, which
the note itself flags against prior art on directional differentiability of
metric projections. NS-R3 remains open.

**NEXT DISTINCT ACTION:** independent audits at a different lens, freezing the
hash above; then reconcile with the in-flight HF24 verdicts.
