# Forced-insensitivity falsifier from the [OA] Lean certificate

Date: 2026-09-08. Frozen input commit: `fedb45a640ea8537aa90578f2cafda9adca01756`.
Status: EVIDENCE NOTE, not a theorem, not a proof audit of [OA], not a
canonical proof-graph or PLAN change. [OA] is author-claimed and
Lean-self-certified only; independent axiom-check replication is in progress
and NOT confirmed; no independent mathematical review of [OA] exists yet.
Nothing here promotes, retracts, or scores any node in `docs/proof-graph.yaml`
or `docs/refinement-proof-graph.yaml`.

[OA] = OpenAI, *Finite Time Blowup for Navier-Stokes*, 165 pp.,
https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf,
Theorem 1.1 (p.1): for every $\nu>0$ there exist $f\in C_c^\infty(\R^3\times(0,\infty))$,
compact $K$, and smooth $u,p$ on $\R^3\times[0,1)$ solving
$\partial_t u+(u\cdot\nabla)u-\nu\Delta u+\nabla p=f$, $\operatorname{div}u=0$,
$u(\cdot,0)=0$, with $\operatorname{supp}u,\operatorname{supp}f\subset K$,
$\sup_{t<1}\|u(t)\|_2<\infty$, $\limsup_{t\uparrow1}\|u(t)\|_\infty=\infty$.
Corollary 10.6 (p.~125) upgrades this to Clay alternatives (C)/(D). Force
construction: Section 10. Lean 4 certificate:
https://github.com/openai/NavierStokesAndEuler, commit
`8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538` (Apache-2.0, Lean v4.34.0-rc2),
self-reported axioms `propext`, `Classical.choice`, `Quot.sound` only.

## 1. The precise test

Fix any proposed a-priori estimate, continuation criterion, producer, or
mechanism M in this programme. M is **forced-insensitive** if its proof goes
through, verbatim or with only the addition of a bounded work term
$\int_0^t\!\int f\cdot u$ controlled by $f\in C_c^\infty(\R^3\times(0,\infty))$,
for the forced system $\partial_t u+(u\cdot\nabla)u-\nu\Delta u+\nabla p=f$
starting from $u(0)=0$. If M is forced-insensitive AND its stated conclusion
would (if M's route were valid) rule out [OA]'s stated behaviour
($\sup_{t<1}\|u\|_2<\infty$ together with $\|u(t)\|_\infty\to\infty$ at a
finite time from zero data), then [OA] Theorem 1.1, if correct, refutes M as
a route to NS-R3: M's proof must contain a step that fails for the forced,
zero-datum case, and that step is exactly where "unforcedness" is doing real
work. This is a consistency/falsification test, not new mathematics; it does
not touch the unforced conjecture itself.

Checklist to run against each candidate M:

1. **Where does the proof use $f=0$?** Point to the exact line: a term
   dropped because there is no forcing (e.g. no $\int f\cdot u$ in an energy
   identity, no $-\Delta^{-1}\operatorname{div}f$ term in the pressure), or
   an equation that is literally the unforced Euler/NS equation in a limit.
2. **Where does it use a *nonzero* (typically Schwartz) datum?** [OA] starts
   from $u(0)=0$ exactly. Any step that needs $u_0\neq0$, or needs
   $u_0\in\mathcal S(\R^3)$ specifically rather than merely finite energy, is
   a candidate place where M could still survive [OA] because [OA]'s zero
   datum is outside M's hypotheses.
3. **Does it survive a force term with bounded $L^2$ work $\int f\cdot u$?**
   [OA]'s solution has bounded energy on $[0,1)$ by construction (Theorem
   1.1: $\sup_{t<1}\|u(t)\|_2<\infty$), so a bounded-energy forced flow with
   a genuine finite-time $L^\infty$ blowup is exactly what [OA] supplies as a
   test case. If M's argument needs only bounded kinetic energy (not the
   *equality* energy identity, not zero force, not nonzero datum) to derive
   its conclusion, then [OA] is a direct counterexample to M's route, subject
   to [OA] being correct.
4. **Does the argument use the exact double-Riesz pressure
   $p=R_iR_j(u_iu_j)$?** Under forcing this becomes
   $p=R_iR_j(u_iu_j)-\Delta^{-1}\operatorname{div}f$ (PLAN.md Section 3); any
   step relying on the unforced formula specifically is a legitimate
   unforced-only step, not automatically refuted.
5. **Does the conclusion, if it held for the forced zero-datum case, actually
   contradict [OA]'s stated conclusion?** Some producers conclude something
   [OA] does not address (e.g. a *rate* or a *specific class* excluded from
   [OA]'s construction); check this before declaring refutation.

## 2. Application to the current programme

### 2a. The reviewed positive consumer chain (PLAN.md Section 1)

Chain: input-only producer $\to$ RF-q $\to$ RF-LQ-SYNTHESIS $\to$ finite
$L^{3,q}$ $\to$ RF-LOCAL-ID / Lorentz Fatou $\to$ RF-LQ-CONTINUATION $\to$
LOCAL / ENERGY / canonical pressure $\to$ NS-R3.

- **RF-R3-FLOW / RF-CUBIC-SYNTHESIS / RF-LQ-SYNTHESIS**
  (`docs/refinement-proof-graph.yaml`, `research/evidence/2026-09-07-whole-space-cubic-refinement.md`,
  `research/evidence/2026-09-07-lorentz-synthesis.md`): these are purely
  algebraic/analytic facts about Fourier-ball-projected flows and their L2
  increments. They never write $f$ or use $u(0)=0$; they take an abstract
  bandlimited solenoidal flow as given. **Forced-insensitive as literally
  stated** (they say nothing about the source of the flow), but they are
  not themselves a producer of the missing bound — they are pure synthesis
  lemmas. Not directly refuted by [OA] because they assert no closure of the
  unknown nonlinear estimate.
- **RF-LOCAL-ID** (same file, Section 4): identifies the projected flow limit
  with "the canonical original-NS branch" via LOCAL, i.e. it explicitly
  invokes the *unforced* classical branch (`research/evidence/2026-09-07-whole-space-cubic-refinement.md`
  line ~236-242: "LOCAL then supplies normalized smooth pressure and velocity
  through t=0 ... original unforced equation"). This step is written to be
  unforced-specific by design; it is not a place where OA-style forcing would
  silently slip in, because the comparison target is defined as the unforced
  branch.
- **RF-LQ-PRODUCER / RF-CUBIC-PRODUCER** (the actual missing gap nodes): these
  are OPEN — there is no proof to test for f=0 usage. Not applicable.
- **RF-LQ-CONTINUATION** (`research/evidence/2026-09-07-lorentz-continuation.md`):
  an adapter of Phuc's local theorem into the canonical continuation
  chain; per `docs/refinement-proof-graph.yaml` its `canonical_inputs` are
  `[LOCAL, ENERGY, CONTINUATION]`, all stated for the unforced Schwartz-data
  classical branch (`docs/proof-graph.yaml` nodes LOCAL, ENERGY,
  CONTINUATION, ESS all state "Schwartz datum", "unit-viscosity rescaling of
  the classical branch", no force term). **This is unforced-specific**: the
  ESS endpoint theorem (`docs/proof-graph.yaml` node ESS, `thm:ess`) is
  imported verbatim from Escauriaza-Seregin-Sverak for the (unforced)
  Leray-Hopf class, and LERAY-HOPF (`lem:leray-hopf`) constructs that class
  from the unforced LOCAL+ENERGY package. A forced analogue of CONTINUATION
  would need a forced ESS/Serrin pair, which is not imported here.
- **Canonical pressure $p=R_iR_j(u_iu_j)$** (`prop:pressure`, main.tex line
  2799, and `docs/proof-graph.yaml` node PRESSURE/LOW-PRESSURE/HIGH-PRESSURE):
  the whole pressure-work estimate is written for the exact unforced
  double-Riesz representative. Under forcing $-\Delta p=\partial_i\partial_j(u_iu_j)-\operatorname{div}f$
  (PLAN.md Section 3), so `prop:pressure`, `hyp:highpressure`,
  `hyp:absorption`, `hyp:critical` (main.tex lines 3638, 3652, 4695) would all
  need an added, uncontrolled force-pressure cross term. **This is the single
  largest unforced-specific dependency in the whole chain.**
- **ENERGY (`prop:energy`, main.tex line 2164)**: the proof derives the exact
  equality $\|u(t)\|_2^2+2\nu\int\|\nabla u\|_2^2=\|u_0\|_2^2$ from
  $E'(\tau)=\int u\cdot u_t=\nu\int u\cdot\Delta u-\int u\cdot(u\cdot\nabla)u-\int u\cdot\nabla p$
  (main.tex eq:energy-derivative), with no $\int u\cdot f$ term. Adding a
  bounded-work force gives only an *inequality*
  $\sup_t\|u(t)\|_2^2\le\|u_0\|_2^2+2\int_0^t f\cdot u$, still finite for
  $C_c^\infty$ $f$ (consistent with [OA]'s $\sup_{t<1}\|u\|_2<\infty$) —
  **so ENERGY's boundedness conclusion survives forcing; only its exact
  equality form is unforced-specific.** This means bounded energy is NOT by
  itself a place where unforcedness is essential — it is exactly the
  conserved quantity that [OA]'s construction also keeps bounded, which is
  what makes [OA] a live test case for anything downstream that uses only
  boundedness of energy.

**Verdict on the positive chain**: the surviving positive route to NS-R3 is
NOT threatened by [OA] as a whole, because its terminal link (CONTINUATION,
via ESS + Serrin + the exact unforced pressure identity) is explicitly
unforced-specific, not merely "assumes bounded energy". The chain does not
claim "any bounded-energy flow from zero data is globally bounded in
$L^\infty$"; it claims the unforced, Schwartz-datum classical branch is. This
is the correct place to record precisely why the chain is not forced-
insensitive: at ESS/pressure, not at ENERGY.

### 2b. `hyp:critical`, `hyp:absorption`, `hyp:highpressure`

All three (main.tex lines 4695, 3652, 3638; `docs/proof-graph.yaml` nodes
CRITICAL, ABSORPTION, HIGH-PRESSURE) are stated for "the classical branch"
arising from a divergence-free Schwartz datum $u_0$, with no force, and their
quantities $D_3,P_3,Q_J$ are built from the exact unforced pressure. **A
forced flow with $u_0=0$ is simply outside these hypotheses' domain of
discourse as written** — they are not violated by [OA], because [OA]'s flow
is not "the classical branch" in this programme's sense (nonzero datum,
zero force) at all. So [OA] does not falsify `hyp:critical` et al.; it shows
only that an *unrestricted* analogue of `hyp:critical` — dropping "arising
from a Schwartz datum with $f=0$" — is false, since [OA]'s forced,
zero-datum flow has bounded energy on $[0,1)$ (satisfying the "energy-normal"
side of the hypothesis pattern) yet $\|u\|_\infty\to\infty$ at finite time
(violating any $L^3$- or $L^\infty$-boundedness conclusion one would hope to
derive from bounded energy alone). **This tells us precisely where the
missing estimate must use unforcedness**: any future proof of `hyp:critical`
that proceeds only from bounded kinetic energy plus generic Navier-Stokes
structure (nonlinear term shape, Leray projection, viscosity) — without ever
using $f=0$ or the Schwartz *and nonzero* datum — cannot be correct, because
the same argument, if it went through, would apply to [OA]'s forced
construction and contradict Theorem 1.1. Concretely: any signed pressure
bound (`hyp:highpressure`) or absorption estimate (`hyp:absorption`) whose
proof consists only of (i) Hölder/interpolation on $u,\nabla u,p$ with $p$
treated through the generic Calderón-Zygmund bound $\|p\|_\infty\lesssim\|u\|_\infty\|u\|_2$
(prop:pressure bounds, main.tex eq:D3P3-bounds), and (ii) the energy
inequality, is automatically forced-insensitive and must be refuted by [OA]
if [OA] is correct — because none of (i)-(ii) needs $f=0$. Such a proof MUST
additionally use either the exact double-Riesz identity's dependence on the
initial datum through the full nonlinear evolution and its Duhamel/heat
smoothing from $t=0$ under $f=0$, or some other place where $f=0$ genuinely
enters (e.g. a Duhamel representation
$u(t)=e^{t\nu\Delta}u_0-\int_0^t e^{(t-s)\nu\Delta}P\operatorname{div}(u\otimes u)\,ds$,
which for the forced case would carry an added $\int_0^t e^{(t-s)\nu\Delta}f\,ds$
term of a priori unbounded-in-$L^3$-norm size even though bounded in energy).
**Not located**: this programme's evidence files do not yet contain an
attempted proof of `hyp:highpressure`/`hyp:absorption`/`hyp:critical`
detailed enough to check whether it in fact uses $f=0$ anywhere (both are
listed `kind: gap`, `status: Open` in `docs/proof-graph.yaml`); there is
nothing to falsify yet. The consequence is prescriptive, not retrospective:
any future attempt should be checked against this test before being trusted.

### 2c. PLAN Section 5 retained mechanisms

For each mechanism named in PLAN.md Section 5, apply the checklist of
Section 1 above.

- **Type-I / no-atom** (`research/evidence/2026-09-08-no-atom-regenerative-blocks.md`):
  Lemma 1 (Section 1) is stated for "a smooth original NS solution $v$ on
  $[-1,0]$ with viscosity $\eta$" (line ~44) with local-energy identity
  eq.(1.5) `partial_s |v_j|^2 + div[...] = eta_j Delta |v_j|^2 - 2 eta_j |grad v_j|^2`
  — **no forcing term appears; $f=0$ enters exactly at (1.5)** and again in
  the passage to the vanishing-viscosity Euler limit (no $f$ term to pass to
  the limit). The whole vanishing-viscosity compactness argument (Rellich +
  H1 bound + pressure splitting) never needs $u_0\neq0$ per se; it works with
  any sequence of smooth NS solutions on a fixed backward time window,
  independent of how they arose. **Classification: explicitly uses $f=0$ at
  the local energy identity (1.5), file line ~region "1.5", and at every
  subsequent Euler-limit pressure/energy passage; does not use a nonzero
  datum anywhere (it is stated on a backward window $[-1,0]$, not from
  $t=0$).** Because it truly needs zero forcing (dropping $f=0$ breaks
  (1.5) and the Euler-limit energy trace, adding an unbounded-in-the-limit
  $\int f\cdot v$ defect term), it is NOT forced-insensitive and is not
  threatened by [OA] as stated. However, note the caveat of Section 3 below:
  this also means the argument gives no information about the forced case
  one way or the other.
- **Full-state return** (`research/evidence/2026-09-08-full-state-vorticity-return.md`):
  Section 1's augmented return map and Theorem 3's material-vorticity
  identity are built on "the material vorticity equation... plus the
  positive Laplacian defect" (line ~361) for original (unforced) NS; the
  discriminator argument at lines 361-371 explicitly compares against Tao's
  averaged operator and shows an "additional material curl forcing" would be
  needed for that operator to match the true NS vorticity source — i.e. the
  proof's validity for the true equation depends on there being no such
  extra term, which is the unforced vorticity-stretching identity.
  **Classification: explicitly uses $f=0$ in the vorticity-stretching
  identity underlying (2.1) and Theorem 3, file lines ~355-371.** No use of
  nonzero datum beyond real solenoidal Schwartz input generically. Not
  forced-insensitive; not refuted by [OA].
- **Integrated background-strain cost** (`research/evidence/2026-09-08-integrated-background-strain-cost.md`):
  Section 0 states "Let $u$ and $b$ solve original NS at the same viscosity"
  (both unforced) and Section 1's endpoint lemma again uses the local
  relative-energy identity with no forcing term
  (`partial_t |v|^2 + div[...] = nu Delta|v|^2 - 2nu|grad v|^2 - 2 v_i v_j partial_j b_i`,
  Section 0 display). **$f=0$ enters at the relative-energy identity
  (Section 0, and again in the vanishing-viscosity Euler limit of Section
  1)** exactly as in the no-atom case; if $u$ or $b$ carried a $C_c^\infty$
  force, an extra $\int(v\cdot f_u - v\cdot f_b)$ term (or a mixed pressure
  contribution from $f_u,f_b$ through the pressure identity of Section 0)
  would appear, and its sign/size is not controlled by the theorem's proof.
  **Classification: explicitly uses $f=0$ (twice: in the exact relative
  pressure identity $-\Delta\pi=\ldots$ with no $-\operatorname{div}f$ term,
  and in the local relative-energy identity display in Section 0); not
  forced-insensitive.** PLAN.md itself flags this file's status as
  "author-claim-scope-audit-pending" — the audit gap is about scope
  (arbitrary-data extraction), not about forcing.
- **Relative background return** (`research/evidence/2026-09-08-relative-background-return.md`):
  Section 2, line ~131: "There is no acceleration force in (2.3): $R$ is the
  difference of velocities" — this is the file's OWN statement that its
  comparison identity has no forcing, precisely because it compares two
  *unforced* NS solutions $U,B$ (line ~45: "two smooth finite-energy
  solenoidal ORIGINAL unforced R3 NS" solutions). **Classification:
  explicitly uses $f=0$ (both $U$ and $B$ unforced), stated by the file
  itself at line ~131 and ~45; not forced-insensitive.** Note this
  mechanism's whole point is a *relative* (two-solution) construction, a
  structurally different object from a single forced flow; [OA]'s single
  forced trajectory does not supply a comparable pair.
- **Mesoscopic obstruction** (`research/evidence/2026-09-08-mesoscopic-relative-energy-obstruction.md`):
  builds two unforced NS evolutions from Schwartz data ("initial datum
  $w(0)+H$... real solenoidal and Schwartz", line ~55; "ordinary positive
  viscosity and no forcing", line ~121 — the file states this explicitly).
  Line ~290, "All forcing differences are zero", refers to the difference of
  the *two solutions'* right-hand sides being equal (both solve the same
  unforced equation), not to an external physical force in [OA]'s sense — a
  terminology note, not evidence about OA-style forcing. **Classification:
  explicitly uses $f=0$, self-declared at line ~121; not forced-insensitive.
  Also: it is itself already a NEGATIVE result (a no-go against automatic
  fixed-background energy coercivity), so the falsification test does not
  apply to it as a positive candidate — "not applicable (already a
  no-go/falsifier)" in addition to being unforced-specific.**
- **Tao packet repair** (`research/evidence/2026-09-08-tao-packet-audit-and-repair.md`):
  Section 2's repaired obstruction is stated for the projected Euler system
  $d_tv_N=\Delta v_N+P_NC(v_N,v_N)$ at unit viscosity with $v_N(0)=P_Nd$
  (Section 2 display) — a genuinely unforced averaged system; there is no
  place a force term is dropped because the object under study (the averaged
  operator $C$) is a separate model, not physical NS with $f$. **This file
  is itself a no-go/falsifier against a proposed averaging shortcut, not a
  positive producer. Classification: not applicable (already a
  no-go/falsifier); its unforced status is incidental (the averaged operator
  has no forcing term to begin with, so the $f=0$ checklist question does
  not meaningfully apply).**

Other PLAN Section 5 files (`2026-09-08-narrow-packet-escape.md`,
`2026-09-08-full-duration-mixing-cascade.md`,
`2026-09-08-source-cycles-and-newborn-efficiency.md`,
`2026-09-08-exact-circuit-obstructions.md`,
`2026-09-08-phase-locked-full-ring.md`,
`2026-09-08-convex-cone-linearity.md`, `2026-09-08-fourier-cone-obstruction.md`,
`2026-09-08-remote-pressure-control.md`, `2026-09-08-retained-bulk-full-flow.md`)
are, per PLAN's own description of them, obstruction/no-go/falsification
results against specific proposed positive mechanisms (spectral transfer,
static Fourier cones, instantaneous restoring pressure, dynamically-invisible
bulk), not themselves candidate producers of a critical estimate. All are
worked in the unforced original-NS equation (spot-checked: `2026-09-08-retained-bulk-full-flow.md`
Section 2 uses "the original full energy identity", no force term; not
re-verified line-by-line for the rest). **Classification: not applicable
(already a no-go/falsifier)** for the purposes of this test.

## 3. What [OA] does NOT refute

- Anything using a genuinely **nonzero Schwartz datum** together with
  **zero force**, where the proof structurally needs the flow to originate
  from smooth, rapidly-decreasing, nonzero data at $t=0$ under the unforced
  equation: backward uniqueness / ESS (`docs/proof-graph.yaml` node ESS,
  imported verbatim from Escauriaza-Seregin-Sverak for the unforced
  Leray-Hopf class), weak-strong uniqueness identifications with the
  classical branch (used throughout `research/kinetic-clay-hilbert-contracts.md`
  Section 2), and the exact Leray projection of the true nonlinearity
  $p=R_iR_j(u_iu_j)$ with **no** $-\Delta^{-1}\operatorname{div}f$ correction
  (`prop:pressure`, main.tex line 2799; PLAN.md Section 3).
- The **vanishing of $\int f\cdot u$** specifically (as opposed to
  boundedness of that work term): the exact energy identity
  $\|u(t)\|_2^2+2\nu\int\|\nabla u\|_2^2=\|u_0\|_2^2$ (`prop:energy`) is an
  equality that fails under any nonzero force, however small its work; any
  mechanism relying on this *equality*, not merely on boundedness, is
  unforced-specific regardless of whether it separately mentions $f$.
- Anything about the **original whole-space unforced Cauchy problem's**
  actual solution set for a *specific* nonzero datum: [OA]'s Theorem 1.1
  gives no information whatsoever about what happens from any particular
  nonzero Schwartz $u_0$ under $f=0$. It is a statement about a different
  equation (forced) and a different datum (zero), and [CMI, p.2] states
  alternative A precisely with zero force — [OA]'s force is explicitly
  permitted only in alternative (C)/(D), not (A)/(B).

**Caveat (converse direction)**: a mechanism's proof *failing* to extend to
the forced, zero-datum case does not, by itself, prove the corresponding
unforced estimate. Absence of an OA-style counterexample to a given argument
is not evidence for the argument's unforced conclusion; it only means the
argument has not (yet) been shown vacuous. Symmetrically, an argument that
*does* extend verbatim to the forced case and would (if valid) contradict
[OA] is refuted only to the extent [OA] itself is correct — which is
explicitly NOT established here (author-claimed, Lean-self-certified,
independent review pending).

## 4. Consequences for allocation

| Candidate / node | Forced-insensitive? | Disposition |
|---|---|---|
| `hyp:critical`, `hyp:absorption`, `hyp:highpressure` if attempted via bounded-energy + generic Hölder/Calderon-Zygmund pressure bounds only, with no Duhamel-from-$t{=}0$ or exact unforced pressure step | Yes, as far as such a proof shape goes | Deprioritize / require an explicit unforced-only step (e.g. Duhamel from $u_0$, or the exact double-Riesz identity with no force correction) before further investment; record this requirement in any future attempt, do not promote a "bounded energy implies $\hyp{critical}$" argument without locating such a step |
| RF-LQ-PRODUCER / RF-CUBIC-PRODUCER (open gaps) | Not yet checkable (no proof exists) | No change; nothing to falsify |
| RF-LQ-CONTINUATION, ESS, LERAY-HOPF, SERRIN, CONTINUATION | No (verbatim unforced-only imports/derivations) | Keep as is; this is the correct place the chain relies on unforcedness |
| No-atom regenerative blocks, integrated background-strain cost, full-state vorticity return, relative background return | No (each explicitly zero-force in its local/relative energy identity) | Keep; not threatened, but also not strengthened, by [OA] |
| Mesoscopic obstruction, Tao packet repair, and the other PLAN Section 5 no-go files | Not applicable (already negative results) | Keep as falsification tools; no reallocation needed |

No currently listed positive-route producer is shown to be forced-insensitive
by this audit; the one place a *hypothetical future* proof of
`hyp:critical`/`hyp:absorption`/`hyp:highpressure` could accidentally become
forced-insensitive (and hence be at risk from [OA], if correct) is any
argument that uses only bounded kinetic energy and generic pressure bounds
without an explicit unforced step. This is a warning for future work, not a
finding against any file currently in the repository.
