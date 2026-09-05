# Final integration audit of the conditional dossier

**VERDICT: REPAIR for exact integration fidelity; PASS for the mathematical
conditional chain after the statement repairs below; FAIL WITH SCOPE for the
Clay claim.**

## Reviewed scope

This audit compares immutable manuscript commit
3545e1726762556b672f320c8fae9cb711443692 in navier-paper with research,
graph, documentation, and evidence commit
afa92968a629617938cdbcb90242453e78c0d959 in navier. It checks faithful
composition, quantifier matching, imported-premise wiring, graph trust labels,
and the declared formalization boundary. It does not re-audit the
low-frequency lemma, which received the independent frozen audit recorded in
research/evidence/review-frequency.md.

The reviewed claim is only:

> if the stated finite-horizon critical estimate holds for every admissible
> datum, then Clay alternative A on \(\mathbb R^3\) follows.

The manuscript expressly does not prove the critical estimate or its refined
signed high-frequency producer.

## Dependency-order findings

### 1. Local solution and target: PASS

The manuscript fixes arbitrary \(\nu>0\), unforced Navier--Stokes on
\(\mathbb R^3\), and real divergence-free Schwartz data. Its target is global
smooth \(u,p\) through \(t=0\) with one time-uniform kinetic-energy bound.
This agrees with the whole-space positive Clay alternative used in the
dossier.

Tao's Theorem 5.4 is used at the directly audited strength: whole-space local
mild existence and uniqueness and, for Schwartz data, smooth velocity and
pressure through the initial time. Tao's theorem is normalized to unit
viscosity; the manuscript's displayed change
\[
 v(x,s)=\nu^{-1}u(x,s/\nu),\qquad
 q(x,s)=\nu^{-2}p(x,s/\nu)
\]
normalizes the entire equation and preserves the Schwartz data class.
Although introduced in the endpoint section, the same formula also resolves
the viscosity convention for local theory.

### 2. Paper-owned identities and pressure proof: PASS

The energy, scaling, interpolation, enstrophy, and scalar-ODE claims match
their graph nodes and paper labels. The repaired pressure proof tests against
\((|u|^2+\varepsilon)^{1/2}u\), subtracts the nonintegrable constant from the
time primitive, identifies both diffusion terms, supplies compact-interval
Sobolev integrability for the cutoff limit, and then sends
\(\varepsilon\downarrow0\). It proves exactly
\[
 {1\over3}{d\over dt}\|u\|_3^3+\nu D_3=P_3.
\]
No persistence of Schwartz decay is used.

The graph labels ENERGY, SCALE, ENSTROPHY, ODE, PRESSURE, and LOW-PRESSURE as
paper-owned claims. It labels local theory and endpoint continuation as
imported. Those trust labels agree with the manuscript and the frozen
component audits.

### 3. Low/high pressure composition: PASS

The paper proves the low-output estimate for every integer \(J\), every
finite \(H\), and every \(0<\tau<\min\{H,T_*\}\):
\[
 \left|\int_0^\tau L_Jdt\right|
 \le C2^{3J}\|u_0\|_2^4\sqrt{H/(2\nu)}.
\]
The graph's LOW-PRESSURE node records the same horizon, cutoff dependence,
power of the initial norm, and viscosity factor.

The paper then assumes, rather than proves, the following producer:
\[
 \forall(\nu,u_0,H)\ \exists(J,A_{\rm high})\
 \forall\tau<\min\{H,T_*\}:\quad
 \int_0^\tau Q_Jdt
 \le\theta\nu\int_0^\tau D_3dt+A_{\rm high},
\]
where \(J\) is finite, \(\theta\in[0,1)\) is one universal constant, and the
bound is uniform in \(\tau\). The graph's HIGH-PRESSURE node has the same
quantifier order and is correctly marked as a gap.

Adding the proved low estimate gives pressure absorption with
\(A=A_{\rm low}+A_{\rm high}\). Integrating the exact pressure balance gives
the finite-horizon \(L^\infty_tL^3_x\) bound and, because
\(\theta<1\), weighted dissipation. Strict \(\theta<1\) is unnecessary for
the critical norm alone: \(\theta=1\) still yields that bound. The manuscript
states this correctly. Retaining strict inequality is faithful to the
stronger absorption mechanism recorded in the graph.

### 4. Endpoint continuation and conditional theorem: PASS

Gallagher--Koch--Planchon Theorem 4 is imported at its actual whole-space
scope: for \(u_0\in L^3(\mathbb R^3)\), a finite uniform \(L^3\) bound on the
maximal unit-viscosity strong solution forces infinite maximal time.
Schwartz data lie in \(L^3\), local uniqueness identifies the classical and
maximal mild branches, and the displayed viscosity normalization sends
\(T_*\) to \(\nu T_*\) while multiplying the \(L^3\) norm by
\(\nu^{-1}\). The premise therefore applies exactly.

If \(T_*<\infty\), choose any finite \(H>T_*\). The universally quantified
finite-horizon critical estimate then bounds
\(\sup_{t<T_*}\|u(t)\|_3\), contradicting endpoint continuation. Energy gives
the global uniform kinetic-energy bound after \(T_*=\infty\), and Tao's local
smoothness/persistence plus elliptic pressure recovery gives smooth \(u,p\).
This proves the manuscript's conditional theorem and nothing stronger.

The sentence in docs/proof.md that takes \(H=T_*\) is also logically
sufficient because the hypothesis is quantified over every finite \(H\).
Using \(H>T_*\), as the manuscript does, is clearer and should be used
consistently.

### 5. Graph structure and phase boundary: PASS

The mathematical dependency chain is represented faithfully:
\[
\mathrm{ENERGY}\Longrightarrow\mathrm{LOW\mbox{-}PRESSURE},
\quad
\mathrm{LOW\mbox{-}PRESSURE}+\mathrm{HIGH\mbox{-}PRESSURE}
\Longrightarrow\mathrm{ABSORPTION},
\]
\[
\mathrm{PRESSURE}+\mathrm{ABSORPTION}
\Longrightarrow\mathrm{CRITICAL},
\quad
\mathrm{ENERGY}+\mathrm{CRITICAL}+\mathrm{ESS}
\Longrightarrow\mathrm{CONDITIONAL}.
\]
PRESSURE supplies the exact balance used by the absorption consumer; ESS
supplies endpoint continuation; ENERGY supplies the final Clay energy
conclusion. Transitive dependence through ENERGY supplies LOCAL, so omission
of a direct LOCAL edge on CONDITIONAL is not a logical gap.

The graph is acyclic, all paper-label strings and evidence paths resolve, and
the structural verifier reports 13 claim records with acyclic dependencies
and resolved evidence and paper labels. There is one semantic label defect:
LOCAL points to def:target, which labels the Clay target rather than the
local-existence assertion; NS-R3 points to the same label. This does not alter
the dependency logic, but LOCAL needs its own manuscript label (or an explicit
source-only marker) before the graph is an exact claim-to-paper map.

HIGH-PRESSURE, ABSORPTION, CRITICAL, and NS-R3 remain visibly marked as gaps.
CONDITIONAL alone is marked conditional. The plan says phase I is not started
and awaits the user; no formal proof is represented as having begun. A clean
build of the frozen manuscript succeeds without undefined citations or
references.

## Quantifier-language correction recommended

The conditional mathematics is sound, but the live manuscript should correct
one piece of proof-discipline language before treating paper, graph, and docs
as exact statement matches.

For fixed \((\nu,u_0,H)\), the assertion that there exists a finite
\(A(\nu,u_0,H)\) uniformly controlling every
\(\tau<\min\{H,T_*\}\) is mathematically nontrivial. It is not vacuous merely
because a deterministic solution trajectory is determined by \(u_0\).
Indeed, at a finite singular time the relevant supremum may be infinite, in
which case no finite witness exists.

What is invalid is a purported proof that defines \(A\) circularly using the
unknown critical supremum, the pressure-work supremum it is meant to bound,
or a higher continuation norm. That restriction belongs in the proof
obligation and audit criteria. It should not be justified by calling the
existential assertion itself vacuous.

Likewise, “depends on \(u_0\) but not on \(T_*\)” is not literally an
extensional distinction because \(T_*\) is itself determined by \(u_0\).
The rigorous content is the quantifier order: for every finite input horizon
\(H\), one finite \(A\) and cutoff \(J\) must work uniformly for all allowed
\(\tau\), without assuming the desired continuation bound. If an effective
formula using finitely many named seminorms is intended, that is a stronger
claim and its allowed functional form must be defined.

Currently the manuscript asks for an “explicitly prescribed” bound using
named initial-data norms, while the graph states the ordinary finite
datum-dependent existential bound. The former implies the latter, so this
does not break the conditional theorem, but they are not exact matching
statements. The exact replacement for the critical hypothesis is
\[
 \forall\nu>0\ \forall u_0\in\mathcal S_\sigma\
 \forall H\in(0,\infty)\
 \exists M<\infty\ \forall t\in[0,\min\{H,T_*\}):
 \|u(t)\|_3\le M.
\]
The exact high-pressure replacement has the same prefix followed by
\(\exists J\in\mathbb Z\,\exists A_{\rm high}<\infty\) and then the displayed
inequality for every \(\tau<\min\{H,T_*\}\), with one universal
\(\theta<1\). State separately that any proof defining these witnesses from
the desired supremum or another continuation norm is circular. This makes
the mathematical statement match the graph without weakening its content.

Also replace docs/proof.md's \(H=T_*\) wording by \(H>T_*\) for fidelity to
the manuscript, and give LOCAL a dedicated manuscript proposition and label
(for example prop:local) rather than pointing it to def:target. These are the
smallest exact integration repairs.

## Verdicts in proof-audit form

**VERDICT FOR REVIEWED CONDITIONAL MATHEMATICS: PASS after the exact
statement and label repairs above.**

**FIRST BAD BRIDGE:** none inside
\[
\text{HIGH-PRESSURE hypothesis}
\Longrightarrow\text{critical bound}
\Longrightarrow\text{conditional Clay conclusion}.
\]

**VERDICT FOR THE TERMINAL CLAIM: FAIL WITH SCOPE.**

**FIRST BAD BRIDGE:** HIGH-PRESSURE. No argument proves the universal signed
time-integrated high-output pressure estimate for arbitrary unforced
whole-space Schwartz-data trajectories.

**REPLACEMENT ARGUMENT:** the quantifier and graph-label replacements above
repair integration fidelity. There is no replacement proof for
HIGH-PRESSURE; the exact low-frequency lemma only narrows that gap.

**CONDITIONAL SUFFIX THAT SURVIVES:** assuming HIGH-PRESSURE, the proved
low-frequency estimate yields ABSORPTION; the exact pressure balance yields
CRITICAL; normalized GKP Theorem 4 yields infinite lifespan; local
smoothness and energy yield the conditional Clay alternative A.

**UNNECESSARY DEPENDENCIES:** the enstrophy inequality, scalar ODE
counterexample, and compactness discussion diagnose failed routes but are not
needed in the selected conditional implication. Strict \(\theta<1\) is not
needed unless weighted \(D_3\) control is also claimed.

**NON-CLAIMS:** this audit proves no high-frequency absorption estimate, no
new critical bound, no global regularity theorem, and no blow-up example. It
does not start Phase I or certify the imported theorems beyond their recorded
source audits.

**REOPENING CONDITION:** independently prove and audit HIGH-PRESSURE with the
uniform finite-horizon quantifiers above, or supply a distinct non-circular
a priori producer of the critical \(L^3\) bound.
