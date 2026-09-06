# HF22-C: the dissipation on the good set of times

**STATUS (2026-09-06).** Audited by `research/evidence/hf22-review-good-set-dissipation.md`,
verdict **REPAIR**. The controller has applied that audit's prescribed repairs
to this note, in place, on 2026-09-06. Theorems A, B and D survive verbatim
with their constants; Theorem C was **defective as displayed** — its constraint
list was incomplete and its family violated an omitted but genuine constraint
on most of the time axis and on every smoothing ramp — and has been replaced by
the audit's repaired **Theorem C′**, with the audit's two additional
constraints (T8), (T9) added to the list. The negative result is now stated as
**non-derivability from the explicitly listed constraints (T1)–(T9)**, not from
"the audited record" as such; the exhaustiveness claim is withdrawn as false.
The falsity overclaim in MODE/RESULT item 1 is withdrawn. Theorem D is recorded
as **not new**: it is the manuscript's own `rem:highstrain-scope`. The wording
downgrade "at least as strong as" that the HF21-B audit imposed and this note
had reverted is restored.

Lane HF22-C, sub-question (c) of the attack on (G), **MODE: DISCOVER**,
2026-09-06. Owned file: `research/evidence/hf22-good-set-dissipation.md`.
Nothing else in the repository is edited and nothing is committed. Nothing is
promoted; the manuscript is untouched.

**Inputs** [DI]: `PLAN.md` ("Frontier packet", "Beyond the checkpoint",
"HF18", "HF20", "HF21", "HF22", "HF23", "Ordered next actions");
`../navier-paper/main.tex`
`sec:quotient` (`lem:quotient-minimizer`, `lem:quotient-coercive`,
`lem:quotient-scaling`, `lem:quotient-heat`, `lem:quotient-stability`,
`prop:quotient-derivative`, `lem:quotient-pressure`, `lem:quotient-chainrule`,
`lem:heat-generator`, `lem:quotient-heatsign`, `lem:quotient-transport`,
`prop:quotient-evolution`, `lem:quotient-lowstrain`, `hyp:highstrain`,
`rem:highstrain-normalisation`, `rem:highstrain-scope`, `rem:distance-balance`,
`rem:no-monotone`, `prop:quotient-conditional`) and, outside that section,
`prop:localtheory`, `lem:upgrade`, `prop:energy`, `prop:scaling` with
\eqref{eq:L4L3}, `rem:mismatch`, `prop:pressure` with `def:D3P3`,
`prop:lowpressure`, `hyp:highpressure`, `hyp:absorption`, `hyp:critical`,
`thm:continuation`, `thm:conditional`;
`research/evidence/hf21-crossing-sign-structure.md` (audited REPAIR, repairs
applied) §§0, 2, 3.1, 4.3–4.5 with Theorem 4.5, Lemma R3, Lemma 4.3 = audit
R4, obstructions O1, O2, O3; and
`research/evidence/hf21-review-crossing-sign-structure.md` (the audit that
supplies R3 and R4). Read as background but **not used as a premise**:
`hf18-hodge-regularity.md` (audited PASS) beyond the facts (Q6) quoted below,
`hf18-divergence-speed-link.md`, `hf19-*.md` (unaudited),
`hf20-harmonic-strain-test.md`, and `hf23-*` (no (H1)-type regularity is used
anywhere here). This note ran no numerics; the audit reports a
segment-by-segment numerical confirmation of the repaired family of §4, which
is bounded evidence and never proof, and nothing below rests on it.

---

## MODE / RESULT

**DISCOVER. The lane question is decided in the negative *for derivability from
an explicitly listed constraint set*, with an exact obstruction, and one usable
inequality comes out of the decision.**

1. **Not derivable.** No input-only bound for
 \(\int_{\mathcal G_\delta}D_3(w)\,dt\) follows from the listed consequences
 (T1)–(T9) of the audited record; by Theorem B(3) such a bound *is* implied by
 (G), so it cannot be false unless (G) is. Theorem C′ (§4) exhibits an explicit
 family that satisfies every constraint in the displayed list (T1)–(T9) on the
 triple \((\mathcal Q,\;C_\sharp\|q\|_3,\;D_3(w))\) — the exact balance,
 \(\mathcal Q\ge0\), \(|K|\le C_\sharp\|q\|_3D_3(w)\), the \(\tau\)-uniform
 input bound on \(\int\|q\|_3^4\), the input bounds on \(\int\mathcal Q\) and
 \(\int\mathcal Q^{4/3}\), the pointwise coupling
 \(C_\sharp\|q\|_3\le\kappa\mathcal Q^{1/3}\), the input bound on
 \(\mathcal Q(0)\), and the lower bounds \(D\ge\frac{8}{9S^2C_9^3}\|u\|_9^3\)
 and \(D\ge\gamma\mathcal Q^{7/3}\) — and along which
 \(\int_{\mathcal G_\delta}D_3\to\infty\) for every \(\delta\in(0,1]\) while the
 bad set has measure \(\to0\) and \(\int c^4\to0\). The negative is therefore
 not a gap of technique **relative to those constraints**. It strictly
 strengthens obstruction O3 of HF21-B (which asserted unavailability) and it
 simultaneously answers the second half of the lane's item (3): **smallness of
 the bad set, in measure and in the audited distance norm, does not help**,
 because in the family the bad set is arbitrarily small in both and still
 carries all of the excess. The list is **not** claimed exhaustive; whether some
 other consequence of the audited record suffices is not decided here.
2. **But the good set is free in (G).** Theorem B (§3) is an exact,
 non-circular, scaling-consistent inequality: for every \(\delta\in(0,1)\) and
 every \(\tau<T_*\),
 \[
  C_\sharp\!\int_0^\tau\!\|q\|_3D_3(w)\,dt
  \le\frac{\delta}{1-\delta}\,\mathcal Q(u_0)
  +\frac1{1-\delta}\,C_\sharp\!\int_{\mathcal B_\delta}\!\|q\|_3D_3(w)\,dt ,
 \]
 with \(\mathcal Q(u_0)\le\frac13\|u_0\|_3^3\) an input quantity and
 \(|\mathcal B_\delta|\le24C_S^2C_\sharp^4E_0^2\delta^{-4}\nu^{-5}\) input-bounded
 uniformly in \(\tau\). Hence **(G) is equivalent to its own restriction to
 the bad set** \(\mathcal B_\delta=\{C_\sharp\|q\|_3>\delta\nu\}\), for one and
 hence for every \(\delta\in(0,1)\), with explicit constants. The good set
 needs no new estimate and contributes nothing to the difficulty of (G). This
 is the lane's one genuinely usable output and it is untouched by the defect
 the audit found in Theorem C.
3. **What the good set buys, exactly** (lane item (2)): the master inequality
 (Theorem A, §2)
 \[
  \int_0^\tau\bigl(\nu-C_\sharp\|q\|_3\bigr)_+D_3(w)\,dt
  \ \le\ \mathcal Q(u_0)+\int_0^\tau\bigl(C_\sharp\|q\|_3-\nu\bigr)_+D_3(w)\,dt ,
 \]
 a bound on the *deficit-weighted* dissipation, never on the dissipation
 itself, whose weight degenerates to zero exactly at the good/bad boundary.
 It is sharp: the family of Theorem C′ attains it with ratio \(\to1\).
 It is the positive-part form of Lemma R3(2)–(3) of HF21-B, sharpened in two
 respects (the remainder is supported on \(\{C_\sharp\|q\|_3>\nu\}\), not on the
 larger \((\mathcal G^\delta_\tau)^c\), and carries the weight
 \((C_\sharp\|q\|_3-\nu)_+\), not \(C_\sharp\|q\|_3\)).
4. **The crux of the lane** (item (3), first half). The audited insufficiency
 family is *not* dismissible as "abstract only", and it is *not* a
 counterexample to (G). Theorem D (§5) is the exact dichotomy: for a fixed
 datum and a fixed horizon, the O2 profile ("\(\int c^4\) input-bounded,
 \(\int cD\) unbounded") is realized on the classical trajectory **if and only
 if** \(T_*\le H\); quantifying over horizons, it is realized **for some
 horizon \(H<\infty\)** if and only if that trajectory develops a finite-time
 singularity. The stronger good-set profile of Theorem C′, if realized,
 *implies* \(T_*\le H\) (the converse is open). So neither family can be
 excluded, nor realized, without settling the problem: they are exactly as
 strong as the open question, and their only usable content is the
 non-derivability statement they were built for. **Theorem D is not new**: it is
 the manuscript's own `rem:highstrain-scope`, transported to (G) — see §5.

**The first gap is unchanged and is not closed.** No HIGH-STRAIN,
HIGH-PRESSURE, CRITICAL or NS-R3 result is asserted here.

---

## 0. Notation and the audited facts used

\(u\) is the classical branch of `prop:localtheory` on \([0,T_*)\) from a
divergence-free Schwartz datum \(u_0\), \(\nu>0\), \(E_0=\|u_0\|_2^2\); the
regularity package (R) of `subsec:qe-trajectories` holds on every compact
subinterval (`lem:upgrade`). Write, at each \(t<T_*\),
\[
 q=q(u(t)),\quad w=u+q,\quad A=|w|w,\quad V=|w|^{1/2}w,\quad
 \mathcal Q=\mathcal Q(u(t))=\tfrac13\|w\|_3^3,\quad F=\tfrac13\|u\|_3^3,
\]
\(D_3(w)=D_{\mathcal Q}(u)\) (`def:qe-dissipation` and HF18-A), \(K\) the
transport term of `lem:quotient-transport`, and
\[
 \boxed{\;c(t):=C_\sharp\,\|q(u(t))\|_3,\qquad D(t):=D_3(w(t))\ge0,
 \qquad C_\sharp=\tfrac32C_9S\;}
\]
so that the lane's good and bad sets are, for \(\delta\in(0,1]\) and
\(\tau<T_*\),
\[
 \mathcal G_\delta:=\{t\in(0,\tau):c(t)\le\delta\nu\},\qquad
 \mathcal B_\delta:=(0,\tau)\setminus\mathcal G_\delta=\{t\in(0,\tau):c(t)>\delta\nu\},
 \qquad \mathcal B:=\mathcal B_1 .
\]
(Reconciliation with HF21-B: its \(\mathcal G^\delta_\tau\) is the present
\(\mathcal G_{1-\delta}\), and its \(\mathcal B_\tau\) is the present
\(\mathcal B=\mathcal B_1\). The present parametrisation is the lane's.)

Audited facts, each used verbatim and cited where used:

- **(A1)** `prop:quotient-evolution` [DI]: \(t\mapsto\mathcal Q(u(t))\in C^1\),
 \(D_{\mathcal Q}\) and \(K\) continuous, and
 \(\mathcal Q'+\nu D_{\mathcal Q}=K\), \(D_{\mathcal Q}\ge0\)
 (`lem:quotient-heatsign`). With HF18-A, \(D_{\mathcal Q}(u)=D_3(w)=D\).
- **(A2)** the sharpened size bound (HF21-B Prop. 3.1, audited; it is the line
 of the HF18-A Theorem 4 proof immediately before the substitution producing
 \(C_*\)): \(|K|\le C_\sharp\|q\|_3D_3(w)=cD\) at every \(t<T_*\).
- **(A3)** `lem:quotient-coercive` \eqref{eq:cp-coercive} [DI]:
 \(\frac{\|u\|_3^3}{3C_{\mathbb P}^3}\le\mathcal Q\le\frac13\|u\|_3^3\) and
 \(\|q\|_3\le(1+C_{\mathbb P})\|w\|_3=(1+C_{\mathbb P})(3\mathcal Q)^{1/3}\);
 hence the **pointwise coupling**
 \[
  c\le\kappa\,\mathcal Q^{1/3},\qquad \kappa:=3^{1/3}(1+C_{\mathbb P})C_\sharp ,
  \tag{0.1}
 \]
 and \(\|q\|_3\le\|w\|_3+\|u\|_3\le2\|u\|_3\), and
 \(\mathcal Q(u_0)\le\frac13\|u_0\|_3^3\). (Per the audit: \(\kappa=C_*\) of
 HF18-A (Q6) exactly, so (0.1) is the audited size bound and not an additional
 input.)
- **(A4)** `prop:scaling`(iii) \eqref{eq:L4L3} [DI] with the audit's Lemma R4
 of HF21-B: \(\int_0^\tau\|u\|_3^4dt\le\frac{3C_S^2E_0^2}{2\nu}\) and hence
 \[
  \int_0^\tau c^4dt\le C_\sharp^4\!\int_0^\tau\!\|q\|_3^4dt
  \le16\,C_\sharp^4\!\int_0^\tau\!\|u\|_3^4dt\le\frac{24\,C_S^2C_\sharp^4E_0^2}{\nu}
  =:A_4(\nu,E_0),
  \tag{0.2}
 \]
 \(\tau\)-uniform.
- **(A5)** `rem:highstrain-normalisation` [DI]:
 \(\int_0^\tau\mathcal Q\,dt\le\frac13H^{1/4}\bigl(\frac{3C_S^2E_0^2}{2\nu}\bigr)^{3/4}
 =:A_{\mathcal Q}(\nu,E_0,H)\) for \(\tau<\min\{H,T_*\}\), input-only.
- **(A6)** `thm:continuation` (ESS endpoint) [DI]: \(T_*<\infty\Rightarrow
 \sup_{t<T_*}\|u(t)\|_3=\infty\); `hyp:critical` and `thm:conditional` [DI]
 for the transfer to the Clay target.
- **(A7)** `lem:quotient-stability` \eqref{eq:cp-strong} [DI] and HF21-B
 Remark 2.2: \(t\mapsto\|q(t)\|_3\) is continuous, indeed
 \(\frac12\)-Hölder on compact subintervals, but **with a constant that is not
 input-only**; \(\|q\|_3\) is not known to be differentiable, and no evolution
 for it is written anywhere below (`rem:qe-transport-scope`).
- **(A8)** `prop:energy` [DI] (fact (P1) of HF21-B §0): \(\|u(t)\|_2^2\le E_0\)
 for every \(t<T_*\); and HF18-A (Q6) as quoted in HF21-B §0:
 \(\|w\|_9^{3/2}=\|V\|_6\le S\|\nabla V\|_2\), \(\|u\|_9\le C_9\|w\|_9\), and
 \(D_3(w)\ge\frac89\|\nabla V\|_2^2\). These two are the ingredients, new to
 this version of the note, of the constraints (T8), (T9) added by the audit.

The target of the programme, in the lane's normalisation:
\[
 \text{(G)}\qquad \int_0^\tau\|q(u(t))\|_3\,D_3(w(t))\,dt\ \le\ A_{\rm input}(\nu,u_0,H)
 \quad\text{uniformly for }\tau<\min\{H,T_*\} .
\]
By (A2) it implies `hyp:highstrain` with \(\theta=0\); by
`rem:highstrain-normalisation` no Gronwall term and no frequency cutoff are
needed; by `prop:quotient-conditional` and `thm:conditional` it implies the
Clay target.

---

## 1. The crossing theorem, restated exactly

This is Theorem 4.5 of `hf21-crossing-sign-structure.md` (audited; item 1 in
the \(\tau\)-uniform form supplied by the audit's Lemma R4.4), transcribed
into the present notation and with its constant displayed. Nothing is added.

**Theorem 1.1 (crossing/measure bound; audited).** Let \(u\) be the classical
branch and \(\tau<T_*\). Then

1. \(\mathcal B=\{t<\tau:c(t)>\nu\}\) is open in \((0,\tau)\), and
 \[
  |\mathcal B|\ \le\ \Bigl(\frac{C_\sharp}{\nu}\Bigr)^{4}\!\int_0^\tau\!\|q\|_3^4\,dt
  \ \le\ \frac{24\,C_S^2\,C_\sharp^4\,E_0^2}{\nu^{5}} ,
  \qquad\text{uniformly in }\tau<T_* ;
  \tag{1.1}
 \]
2. \(\mathcal Q'(t)\le-\bigl(\nu-c(t)\bigr)D(t)\le0\) for every
 \(t\in(0,\tau)\setminus\mathcal B\);
3. \(\mathcal Q(\tau)\le\mathcal Q(0)+\int_{\mathcal B}c\,D\,dt\).

*Proof.* Openness is continuity of \(\|q\|_3\) (A7). (1.1) is Chebyshev at
exponent \(4\) applied to \(c\), with (0.2). Item 2 is (A1) with (A2). Item 3
integrates (A1), drops the nonpositive contribution of the complement of
\(\mathcal B\) and uses \(D\ge0\). \(\square\)

The same Chebyshev step at the threshold \(\delta\nu\) gives the form used
below: for every \(\delta\in(0,1]\),
\[
 |\mathcal B_\delta|\ \le\ \Bigl(\frac{C_\sharp}{\delta\nu}\Bigr)^{4}\!\int_0^\tau\!\|q\|_3^4dt
 \ \le\ \frac{24\,C_S^2\,C_\sharp^4\,E_0^2}{\delta^4\nu^{5}}=:\beta(\delta,\nu,E_0),
 \qquad\text{uniformly in }\tau<T_* .
 \tag{1.2}
\]
Both (1.1) and (1.2) are **measure statements only**: they say nothing about
how much of \(\int D\,dt\) sits on \(\mathcal B_\delta\), as HF21-B states
explicitly.

Scaling check. \(c,\nu\sim(a,\lambda^0)\), \(D\,dt\sim(a^2,\lambda^0)\),
\(|\mathcal B_\delta|\sim dt\sim(a^{-1},\lambda^{-2})\), and
\(E_0^2\nu^{-5}\sim(a^{4-5},\lambda^{-2})=(a^{-1},\lambda^{-2})\) ✓ (HF21-B §0
scaling conventions, [DI]).

---

## 2. What the good set buys: the master deficit inequality

*Audit status: verified, unchanged, constants recomputed independently.*

**Theorem A (master inequality; exact, unconditional, \(\tau\)-uniform on the
left).** For every \(\tau<T_*\),
\[
 \boxed{\;\int_0^\tau\bigl(\nu-c\bigr)_+D\,dt
 \ \le\ \mathcal Q(u_0)+\int_0^\tau\bigl(c-\nu\bigr)_+D\,dt
 \ \le\ \tfrac13\|u_0\|_3^3+\int_{\mathcal B}\bigl(c-\nu\bigr)D\,dt\; }
 \tag{2.1}
\]
and consequently, for every \(\delta\in(0,1]\),
\[
 (1-\delta)\,\nu\int_{\mathcal G_\delta}D\,dt
 \ \le\ \mathcal Q(u_0)+\int_{\mathcal B}(c-\nu)D\,dt
 \ \le\ \mathcal Q(u_0)+\int_{\mathcal B}c\,D\,dt .
 \tag{2.2}
\]

*Proof.* By (A1), \(\mathcal Q\in C^1\) with all integrands continuous, so on
\([0,\tau]\subset[0,T_*)\)
\[
 \mathcal Q(u_0)-\mathcal Q(u(\tau))=\int_0^\tau\bigl(\nu D-K\bigr)dt .
\]
By (A2), \(K\le cD\) pointwise, so \(\nu D-K\ge(\nu-c)D\). Since
\(\mathcal Q(u(\tau))\ge0\),
\(\int_0^\tau(\nu-c)D\,dt\le\mathcal Q(u_0)\). Split
\((\nu-c)D=(\nu-c)_+D-(c-\nu)_+D\), both terms nonnegative and integrable
(continuous on a compact interval), and move the second to the right; the
support of \((c-\nu)_+\) is \(\mathcal B\). The last bound on
\(\mathcal Q(u_0)\) is (A3). For (2.2), on \(\mathcal G_\delta\) one has
\(c\le\delta\nu\), hence \((\nu-c)_+\ge(1-\delta)\nu\), and the integrand is
nonnegative everywhere, so the left side of (2.1) dominates
\((1-\delta)\nu\int_{\mathcal G_\delta}D\). \(\square\)

Three remarks, each of which is the content the lane's item (2) asked to be
made precise.

**2.1 It is a bound on the deficit, not on the dissipation.** The weight on
the left of (2.1) is \((\nu-c)_+\), which vanishes identically on
\(\mathcal B_1\) and degenerates continuously to \(0\) as the trajectory
approaches the good/bad boundary. At \(\delta=1\) — the lane's full good set
\(\mathcal G_1\) — (2.2) is vacuous, which is exactly obstruction O3 of
HF21-B. For \(\delta<1\) it buys \(\int_{\mathcal G_\delta}D\) at the price
\((1-\delta)^{-1}\nu^{-1}\) **and** the bad-set remainder. This is the precise
sense in which "the quotient is nonincreasing on the good set, so the
dissipation integrates against the quotient decrement": the decrement is
available, but the exchange rate between decrement and dissipation is
\((\nu-c)_+\), not \(\nu\).

**2.2 It sharpens Lemma R3 of the HF21-B audit in two respects.** R3(3) reads,
in the present notation,
\((1-\delta)\nu\int_{\mathcal G_\delta}D\le\mathcal Q(0)+\int_{\mathcal B_\delta}cD\)
with the remainder over the *larger* set \(\mathcal B_\delta\supseteq\mathcal B\)
and with the *larger* weight \(c\) in place of \((c-\nu)_+\). (2.2) has the
remainder supported on \(\mathcal B\) alone and carries \((c-\nu)\) there.
Both sharpenings are free — they are already in the proof of R3 — and neither
changes the verdict: the remainder is still a piece of (G).

**2.3 It is scaling-consistent and \(\tau\)-uniform except through the
remainder.** Each side of (2.1) has the scaling \((a^3,\lambda^0)\) of
\(\mathcal Q\); \(\mathcal Q(u_0)\le\frac13\|u_0\|_3^3\) is input-only and
independent of \(\tau\). The only \(\tau\)-dependence is in
\(\int_{\mathcal B}(c-\nu)D\), i.e.\ in the bad-set piece of (G). No horizon
\(H\) appears: Theorems A and B hold for all \(\tau<T_*\).

---

## 3. The good set is free in (G)

*Audit status: verified, unchanged, all constants recomputed.*

**Theorem B (reduction of (G) to its bad-set restriction).** For every
\(\delta\in(0,1)\) and every \(\tau<T_*\),
\[
 \boxed{\;C_\sharp\!\int_0^\tau\!\|q\|_3D_3(w)\,dt=\int_0^\tau\!cD\,dt
 \ \le\ \frac{\delta}{1-\delta}\,\mathcal Q(u_0)
 \;+\;\frac1{1-\delta}\int_{\mathcal B_\delta}\!cD\,dt\;}
 \tag{3.1}
\]
with \(\mathcal Q(u_0)\le\frac13\|u_0\|_3^3\) and
\(|\mathcal B_\delta|\le\beta(\delta,\nu,E_0)\) of (1.2), uniformly in
\(\tau<T_*\). Consequently:

1. **(G) holds if and only if its bad-set restriction holds.** If
 \(\int_{\mathcal B_\delta}cD\,dt\le A_{\mathcal B}\) for all
 \(\tau<\min\{H,T_*\}\) and one \(\delta\in(0,1)\), then (G) holds with
 \(A_{\rm input}=C_\sharp^{-1}\bigl[\frac{\delta}{3(1-\delta)}\|u_0\|_3^3
 +\frac{A_{\mathcal B}}{1-\delta}\bigr]\). The converse is trivial
 (\(\mathcal B_\delta\subset(0,\tau)\), integrand \(\ge0\)).
2. **The good-set contribution to (G) needs no new estimate:**
 \(\int_{\mathcal G_\delta}cD\,dt\le\frac{\delta}{1-\delta}\bigl[\mathcal Q(u_0)
 +\int_{\mathcal B}(c-\nu)D\,dt\bigr]\).
3. **(G) implies the good-set dissipation bound:** if (G) holds with
 \(A_{\rm input}\), then for every \(\delta\in(0,1)\) and every
 \(\tau<\min\{H,T_*\}\),
 \[
  \int_{\mathcal G_\delta}D_3(w)\,dt\ \le\
  \frac{\frac13\|u_0\|_3^3+C_\sharp A_{\rm input}}{(1-\delta)\nu} .
  \tag{3.2}
 \]

*Proof.* On \(\mathcal G_\delta\), \(c\le\delta\nu\), so by (2.2)
\[
 \int_{\mathcal G_\delta}cD\,dt\le\delta\nu\int_{\mathcal G_\delta}D\,dt
 \le\frac{\delta}{1-\delta}\Bigl[\mathcal Q(u_0)+\int_{\mathcal B}(c-\nu)D\,dt\Bigr]
 \le\frac{\delta}{1-\delta}\Bigl[\mathcal Q(u_0)+\int_{\mathcal B_\delta}cD\,dt\Bigr],
\]
using \(\mathcal B\subseteq\mathcal B_\delta\) and \(0\le(c-\nu)\le c\) on
\(\mathcal B\). Add \(\int_{\mathcal B_\delta}cD\,dt\) to both sides and
collect the coefficient
\(\frac{\delta}{1-\delta}+1=\frac1{1-\delta}\); this is (3.1), and item 2 is
the first display. Item 1 is immediate from (3.1). Item 3 is (2.2) with
\(\int_{\mathcal B}(c-\nu)D\le\int_0^\tau cD\le C_\sharp A_{\rm input}\).
\(\square\)

At \(\delta=\frac12\) the constants are
\(\int_0^\tau cD\le\mathcal Q(u_0)+2\int_{\mathcal B_{1/2}}cD\), with
\(|\mathcal B_{1/2}|\le384\,C_S^2C_\sharp^4E_0^2\nu^{-5}\). As \(\delta\uparrow1\)
the region \(\mathcal B_\delta\) shrinks towards \(\mathcal B\) while the
constant \((1-\delta)^{-1}\) blows up; the trade-off is genuine and no choice
of \(\delta\) removes it, because on the middle band
\(\{\delta\nu<c\le\nu\}\) the deficit \(\nu D-K\) is nonnegative but has no
positive lower bound in terms of \(D\).

**Scope.** Theorem B is a reduction, not progress on (G): it moves the whole
of (G) onto a set of times of input-bounded measure on which the distance to
\(\mathcal M\) is bounded below by \(\delta\nu/C_\sharp\), and it proves that
nothing is lost or gained on the good set. It uses no regularity of the
minimizer, no derivative of \(\|q\|_3\), no frequency cutoff and no Gronwall
term; it is not circular, since every constant is input-only and the only
trajectory-dependent object on the right is the bad-set piece of the very
quantity being bounded, restricted to a smaller set.

---

## 4. The decision: no input-only good-set bound is derivable from (T1)–(T9)

*Audit status: this section was the defective one. The constraint list below
now carries the two constraints (T8), (T9) that the audit derived and that the
previous version omitted; the previous version's claim that (T7) was vacuous
and that the list was exhaustive was **false** and has been withdrawn; and the
family has been replaced by the audit's repaired Theorem C′.*

The lane asks whether *any* input-only bound is available for
\(\int_{\mathcal G_\delta}D\,dt\). By Theorem B(3) such a bound is *implied
by* (G) and so is a necessary condition for regularity of the datum; it is
also strictly weaker than (G), since it controls only \(\int_{\mathcal G_\delta}cD\)
and leaves \(\int_{\mathcal B_\delta}cD\) untouched. So the question is
whether the constraints that the audited record supplies already force it. The
constraints enumerated below do not, and the failure is exact.

**The constraint list used below.** Along the classical branch the audited
record imposes, on the triple \((\mathcal Q,c,D)\) of real functions on
\((0,\tau)\), the following consequences, which are the ones used below; **the
list is not claimed to be exhaustive**:

- (T1) \(\mathcal Q\in C^1\), \(\mathcal Q\ge0\), \(c,D\) continuous,
 \(D\ge0\), \(c\ge0\) — (A1), (A7);
- (T2) \(\mathcal Q'=-\nu D+K\) with \(|K|\le cD\) — (A1), (A2);
- (T3) \(\int_0^\tau c^4dt\le A_4(\nu,E_0)\), \(\tau\)-uniform — (0.2);
- (T4) \(\int_0^\tau\mathcal Q\,dt\le A_{\mathcal Q}(\nu,E_0,H)\) — (A5);
- (T5) \(c\le\kappa\,\mathcal Q^{1/3}\) pointwise — (0.1);
- (T6) \(\mathcal Q(0)\le\frac13\|u_0\|_3^3\) — (A3);
- (T7) \(D\ge\frac{8}{9S^2C_9^3}\|u\|_9^3\ge0\) — HF18-A (Q6), (A8);
- **(T8)** (added by audit) for the classical branch, at every \(t<T_*\),
 \[
  D_3(w(t))\ \ge\ \gamma\,\mathcal Q(u(t))^{7/3},
  \qquad
  \gamma:=\frac{8\cdot3^{1/3}}{S^2C_9^3E_0^2}\ >\ 0 ;
  \tag{4.1}
 \]
- **(T9)** (added by audit) \(\int_0^\tau\mathcal Q^{4/3}dt
 \le 3^{-1/3}C_S^2E_0^2/(2\nu)=:A_{4/3}(\nu,E_0)\), \(\tau\)-uniform.

*Proof of (T8) (the audit's, reproduced).* All four ingredients are audited.
(i) (Q6) of HF21-B §0 (HF18-A, audited PASS), i.e. (A8):
\(\|w\|_9^{3/2}=\|V\|_6\le S\|\nabla V\|_2\), \(\|u\|_9\le C_9\|w\|_9\), and
\(D_3(w)\ge\frac89\|\nabla V\|_2^2\); combining,
\(D_3(w)\ge\frac{8}{9S^2C_9^3}\|u\|_9^3\), which is (T7). (ii) Log-convexity of
\(L^p\) norms with \(\frac13=\frac{4/7}{2}+\frac{3/7}{9}\):
\(\|u\|_3\le\|u\|_2^{4/7}\|u\|_9^{3/7}\), hence
\(\|u\|_9^3\ge\|u\|_3^7/\|u\|_2^4\). (iii) `prop:energy` (A8):
\(\|u(t)\|_2^2\le E_0\), hence \(\|u\|_2^4\le E_0^2\). (iv)
`lem:quotient-coercive` \eqref{eq:cp-coercive} (A3): \(\mathcal Q\le\frac13\|u\|_3^3\),
hence \(\|u\|_3^7=(\|u\|_3^3)^{7/3}\ge(3\mathcal Q)^{7/3}\). Chaining,
\(D_3(w)\ge\frac{8}{9S^2C_9^3}\cdot3^{7/3}\mathcal Q^{7/3}/E_0^2\) and
\(3^{7/3}/9=3^{1/3}\). \(\square\)

*Scaling check for (T8).* With the HF21-B §0 conventions \(u\mapsto\lambda u(\lambda\cdot)\):
\(\mathcal Q\) is invariant, \(D_3(w)\sim\lambda^2\), \(E_0\sim\lambda^{-1}\) so
\(\gamma\sim\lambda^2\). Both sides carry \(\lambda^2\), and in the amplitude
grading \(D\sim(a^3,\lambda^2)\) while
\(\gamma\mathcal Q^{7/3}\sim(a^{-4}\cdot a^{7},\lambda^{2})=(a^3,\lambda^2)\) ✓.

*Proof of (T9).* \(\mathcal Q\le\frac13\|u\|_3^3\) gives
\(\mathcal Q^{4/3}\le3^{-4/3}\|u\|_3^4\); integrate and use \eqref{eq:L4L3}
(A4): \(\int_0^\tau\mathcal Q^{4/3}\le3^{-4/3}\cdot\frac{3C_S^2E_0^2}{2\nu}
=3^{-1/3}C_S^2E_0^2/(2\nu)\), with no horizon \(H\). \(\square\)

*Redundancies recorded by the audit.* (T7) is redundant as a list entry once
(T8) is listed — (T8) is (T7) plus three audited facts, and it is (T8), not
(T7), that constrains the triple; (T7) is kept because it is the intermediate
step of the proof of (T8) and because the subcriticality bullet below uses it.
(T4) is redundant given (T9), which is the same bound before the time-Hölder
step of `rem:highstrain-normalisation` and needs no horizon \(H\); both are
kept, but only (T9) does work. (0.1)/(T5) is the audited HF18-A size bound
with \(\kappa=C_*\) exactly and is not an additional input.

**Theorem C′ (explicit family; the good-set dissipation is not controlled by
(T1)–(T9)).** Fix \(\nu=1\) and any \(\kappa>0\); put
\(\mathcal Q_0:=\max\{1,(2/\kappa)^3\}\) and \(\tau=2\). Fix any input tuple
\((\nu,u_0,H)\) with \(H>2\), \(\frac13\|u_0\|_3^3\ge3\mathcal Q_0\) and
\(E_0=\|u_0\|_2^2\) large enough that
\[
 D_\flat\ :=\ \gamma\,(3\mathcal Q_0)^{7/3}\ \le\ \tfrac14\mathcal Q_0 ,
 \qquad \gamma=\frac{8\cdot3^{1/3}}{S^2C_9^3E_0^2},
\]
which is possible because \(\gamma\downarrow0\) as \(E_0\uparrow\infty\) while
\(A_4\), \(A_{\mathcal Q}\) of (T3), (T4) increase in \(E_0\). For each integer
\(n\ge1\) put \(\ell:=n^{-2}\) and define on \((0,2)\):
\[
 \begin{aligned}
 &\text{bad phase } \mathcal I_k^-=\bigl((2k-2)\ell,(2k-1)\ell\bigr):
 && c\equiv2,\quad D\equiv \mathcal Q_0/\ell,\quad K=cD,\\
 &\text{good phase } \mathcal I_k^+=\bigl((2k-1)\ell,2k\ell\bigr):
 && c\equiv0,\quad D\equiv \mathcal Q_0/\ell,\quad K=0,\\
 &\text{tail } (2n\ell,2): && c\equiv0,\quad D\equiv D_\flat,\quad K=0,
 \end{aligned}
\]
for \(k=1,\dots,n\), and let \(\mathcal Q\) solve
\(\mathcal Q'=-\nu D+K\) with \(\mathcal Q(0):=\mathcal Q_0+2D_\flat\). Then,
for every \(\delta\in(0,1]\):

1. \(\mathcal Q\) rises by \(\mathcal Q_0\) on each \(\mathcal I_k^-\), falls by
 \(\mathcal Q_0\) on each \(\mathcal I_k^+\), and falls by \(D_\flat\) per unit
 length on the tail, so
 \(\mathcal Q_0\le\mathcal Q\le2\mathcal Q_0+2D_\flat\le2.5\mathcal Q_0<3\mathcal Q_0\)
 throughout and \(\mathcal Q>0\);
 \(\mathcal Q(0)=\mathcal Q_0+2D_\flat\le1.5\mathcal Q_0\le\frac13\|u_0\|_3^3\).
 **(T1), (T2), (T6) hold**, with \(\mathcal Q(0)\) independent of \(n\).
2. \(c\le2\le\kappa\mathcal Q_0^{1/3}\le\kappa\mathcal Q^{1/3}\): **(T5) holds**.
3. \(\int_0^2c^4dt=16/n\to0\): **(T3) holds** for all \(n\ge16/A_4\).
4. \(\int_0^2\mathcal Q\,dt\le5\mathcal Q_0\) and
 \(\int_0^2\mathcal Q^{4/3}dt\le2(2.5\mathcal Q_0)^{4/3}\), both independent of
 \(n\): **(T4), (T9) hold** for the fixed tuple above.
5. \(D\ge D_\flat=\gamma(3\mathcal Q_0)^{7/3}\ge\gamma\mathcal Q^{7/3}\)
 **everywhere**, since on the spikes \(D=\mathcal Q_0n^2\ge\mathcal Q_0>D_\flat\)
 and on the tail \(D=D_\flat\) while \(\mathcal Q<3\mathcal Q_0\):
 **(T7), (T8) hold**.
6. \(\mathcal B_\delta=\bigcup_k\mathcal I_k^-\), so \(|\mathcal B_\delta|=1/n\to0\),
 \(\int_{\mathcal B_\delta}c^4\to0\), and \(c\equiv2\) is bounded on
 \(\mathcal B_\delta\); the good set contains \(\bigcup_k\mathcal I_k^+\) and the
 tail.
7. \(\int_{\mathcal G_\delta}D\,dt\ \ge\ \sum_k\ell\cdot(\mathcal Q_0/\ell)
 =n\mathcal Q_0\to\infty\), while
 \(\int_{\mathcal B_\delta}(c-\nu)D\,dt=n\mathcal Q_0\to\infty\) carries the
 entire excess.

Hence **no bound**
\(\int_{\mathcal G_\delta}D\,dt\le\Phi(\nu,A_4,A_{\mathcal Q},A_{4/3},
\mathcal Q(0),\kappa,\gamma,\delta,H)\) follows from (T1)–(T9). \(\square\)

*Proof.* Items 1–4, 6, 7 are the previous version's arithmetic, verified
independently by the audit, with the two additive \(D_\flat\) corrections: the
tail contributes at most \(2D_\flat\le\mathcal Q_0/2\) of downward drift, which
the shifted initial value absorbs, and at most \(2D_\flat\) to
\(\int_{\mathcal G_\delta}D\), which only helps item 7. Item 5 is the choice of
\(D_\flat\) together with \(\mathcal Q<3\mathcal Q_0\) from item 1. For
\(\mathcal Q\in C^1\) and \(c\) Lipschitz, replace each jump by a linear ramp of
relative length \(\varepsilon\) on which \(D\equiv D_\flat\) (**not**
\(D\equiv0\); the previous version set \(D\equiv0\) on the ramps and thereby
violated (T8) on every one of them); this multiplies \(\int c^4\) by at most
\(1+2\varepsilon\) (the previous version's "\(1+\varepsilon\)" is off by the
factor 2, harmlessly), changes item 7 by \(1-O(\varepsilon)\), and preserves
items 1–6. \(\square\)

*Arithmetic, recomputed.* On \(\mathcal I_k^-\):
\(\mathcal Q'=-\mathcal Q_0/\ell+2\mathcal Q_0/\ell=+\mathcal Q_0/\ell\),
increment \(+\mathcal Q_0\); on \(\mathcal I_k^+\): \(\mathcal Q'=-\mathcal Q_0/\ell\),
increment \(-\mathcal Q_0\); \(|K|\le cD\) with equality on \(\mathcal I_k^-\)
and \(0=0\) on \(\mathcal I_k^+\); \(\int_0^2c^4=16n\ell=16/n\);
\(\int_0^2c^3=8/n\); \(|\mathcal B_\delta|=n\ell=1/n\) for every
\(\delta\in(0,1]\) since \(c\in\{0,2\}\). Master inequality (2.1) on this
family: left side \(=n\mathcal Q_0\) up to the tail's contribution, right side
\(=\mathcal Q(0)+n\mathcal Q_0\), ratio \(\to1\) — **Theorem A is sharp on this
family**.

*Why the previous version failed, recorded so the error is not repeated.* The
previous version declared (T7) "vacuous, since it only bounds \(D\) from below
by a quantity not otherwise constrained", and declared the list of seven
exhaustive. Both clauses are false: \(\|u\|_9\) **is** otherwise constrained
below by \(\mathcal Q\), through log-convexity of \(L^p\) norms, the energy
bound (A8) and the coercivity (A3), which is exactly (T8). The previous
family set \(c=D=K=0\) on \((2n\ell,2)\) while \(\mathcal Q\equiv\mathcal Q_0>0\),
so (T8) demanded \(0\ge\gamma\mathcal Q_0^{7/3}>0\) on an interval of length
\(2-2/n\), i.e.\ on most of the time axis, and again on each of the \(2n\)
smoothing ramps. The family was therefore not a member of the constraint set
at all. The repair is the tail value \(D_\flat\), the ramp value \(D_\flat\),
and the shifted initial value \(\mathcal Q(0)=\mathcal Q_0+2D_\flat\).

**Scope of Theorem C′, stated correctly.** No input-only bound on
\(\int_{\mathcal G_\delta}D_3(w)\,dt\) is derivable **from (T1)–(T9)**. Whether
some other consequence of the audited record suffices is *not* decided: the
exhaustiveness claim is withdrawn, it was false as stated, and it is **not
needed**. A non-derivability result relative to an explicitly displayed list is
exactly what rules out the proof strategies the lane was testing (the two
Hölder routes, the small-measure route, the threshold-tuning route), and it is
all that the upgrade of O3 requires.

**What survives of the O3 upgrade.** O3 of HF21-B asserted unavailability by a
saturation heuristic and left open "whether any input-only bound for
\(\int_{\mathcal G^\delta_\tau}D_3(w)dt\) exists for some fixed
\(\delta\in(0,1]\)". Theorem C′ closes the *derivability* half of that open
question against the nine listed constraints, including the four — (T2), (T4),
(T5), (T6) — that O2 never tested, and the two — (T8), (T9) — that the audit
added. That is a genuine advance over O3 and over O2's two-fact family. It is
**not** a decision of the lane question itself.

**What Theorem C′ settles.**

- The lane's question, relative to (T1)–(T9): **not derivable**. It is not a
 matter of finding the right Hölder split or the right threshold; the listed
 constraint set is satisfied by data whose good-set dissipation is unbounded.
 This is a statement about that list, not about trajectories, and not a claim
 that the good-set bound is false.
- The lane's item (3), first half: **the bad set cannot be handled by its
 small measure together with any constraint on the list.** In the family, the
 bad set has measure \(1/n\to0\) *and* \(\int_{\mathcal B}c^4\to0\) *and*
 \(c\equiv2\) is bounded there, and it still carries the entire excess
 \(\int_{\mathcal B}(c-\nu)D=n\mathcal Q_0\to\infty\). Smallness in measure
 is compensated exactly by concentration of \(D\); this is the same mechanism
 as O2 of HF21-B, now shown to survive the four further constraints
 (T2), (T4), (T5), (T6) that O2 never tested and the two, (T8) and (T9), that
 the audit added.
- It also disposes of the two Hölder routes explicitly. Against
 \(\int_{\mathcal B_\delta}cD\le(\int c^4)^{1/4}(\int_{\mathcal B_\delta}D^{4/3})^{3/4}\)
 the family has \(\int c^4\to0\) and \(\int D^{4/3}\to\infty\) fast enough to
 keep the product divergent — indeed the audit recomputes
 \((16/n)^{1/4}(n^{5/3}\mathcal Q_0^{4/3})^{3/4}=2n\mathcal Q_0=\int_{\mathcal B}cD\),
 so Hölder is saturated exactly, not merely asymptotically. And any a priori
 bound on \(\int_0^\tau D^{4/3}dt\) is circular by O1(c) of HF21-B, sharpened
 here: \(D\ge\frac{8}{9S^2C_9^3}\|u\|_9^3\) (T7) turns \(D\in L^{4/3}_t\) into
 \(u\in L^4_tL^9_x\), and \(\frac24+\frac39=\frac56<1\) is **strictly
 subcritical**, hence a fortiori a Ladyzhenskaya–Prodi–Serrin hypothesis **at
 least as strong as** the conclusion the gap must produce. (The wording "at
 least as strong as" is the HF21-B audit's explicit downgrade of "stronger
 than"; the previous version of this note had reverted it, and the reversion is
 withdrawn.)

---

## 5. The crux: is the insufficiency family realizable on a trajectory?

The lane states the distinction correctly: an abstract counterexample to an
implication is not a counterexample to the inequality. Here is the exact
status of both families.

**Theorem D (realization dichotomy; *not new* — see the attribution below).**
Fix \(\nu>0\), a divergence-free Schwartz datum \(u_0\), and \(0<H<\infty\);
let \(u\) be the classical branch. Then the following are equivalent:

1. \(\displaystyle\sup_{\tau<\min\{H,T_*\}}\int_0^\tau\|q\|_3D_3(w)\,dt=\infty\)
 (the trajectory realizes the O2 profile: \(\int c^4\) input-bounded by
 (0.2), \(\int cD\) unbounded);
2. \(T_*\le H\), i.e.\ the classical branch of this datum ceases to exist
 before the horizon.

*Proof.* \(\neg2\Rightarrow\neg1\): if \(T_*>H\) then \([0,H]\) is a compact
subinterval of \([0,T_*)\), on which \(\|q\|_3\) and \(D_3(w)\) are continuous
by (A7) and (A1); hence \(\int_0^\tau\|q\|_3D_3(w)dt\le\int_0^H\|q\|_3D_3(w)dt<\infty\)
for all \(\tau<H=\min\{H,T_*\}\).

\(\neg1\Rightarrow\neg2\): suppose \(\int_0^\tau\|q\|_3D_3(w)dt\le A\) for all
\(\tau<\min\{H,T_*\}\). Integrating (A1) and using (A2),
\[
 \mathcal Q(u(\tau))+\nu\!\int_0^\tau\!D_3(w)\,dt
 =\mathcal Q(u_0)+\int_0^\tau\!K\,dt\ \le\ \mathcal Q(u_0)+C_\sharp A ,
\]
so \(\mathcal Q(u(\tau))\le\frac13\|u_0\|_3^3+C_\sharp A\) for all such
\(\tau\), and by (A3) \(\sup_{\tau<\min\{H,T_*\}}\|u(\tau)\|_3^3
\le3C_{\mathbb P}^3(\frac13\|u_0\|_3^3+C_\sharp A)<\infty\). If \(T_*\le H\)
then \(\min\{H,T_*\}=T_*\) and \(T_*<\infty\), so this contradicts
`thm:continuation` (A6). Hence \(T_*>H\). \(\square\)

**Attribution (per the audit).** Theorem D is `rem:highstrain-scope` of the
manuscript, transported from `hyp:highstrain` to (G) by (A2) and
`rem:highstrain-normalisation`. No novelty is claimed; what is new here is only
the *use* made of it in Corollary D.1(ii). The manuscript's remark reads: at
the quantifiers of `hyp:highstrain` the hypothesis is equivalent to global
continuation of the selected classical branch, the forward direction being
`prop:quotient-conditional` with `thm:continuation`, and conversely, if
\(T_*=\infty\), then \(K_0\) is continuous on the compact classical interval
\([0,H]\), so \(A_{\rm input}=\int_0^H|K_0|dt\) is finite — "this converse
assumes global continuation and supplies no method for proving it". Theorem D
is that sentence with \(K_L\) replaced by \(\|q\|_3D_3(w)\).

**Corollary D.1.** (i) The O2 family's profile is realized on a Navier–Stokes
trajectory **exactly** in the singular scenario. It therefore cannot be
excluded by any argument that does not prove global regularity for that
datum, and it cannot be exhibited by any argument that does not construct a
singularity. (ii) The good-set family of Theorem C′ is *strictly stronger*: if
a trajectory has \(\sup_\tau\int_{\mathcal G_\delta}D_3(w)dt=\infty\) for some
\(\delta\in(0,1)\), then by Theorem B(3) (G) fails for that datum, hence by
Theorem D \(T_*\le H\); the converse is **open**, since a singular trajectory
could concentrate all of its divergence on \(\mathcal B_\delta\).

**What Theorem D does establish.** Because \(A_{\rm input}\) may be *any*
finite function of \((\nu,u_0,H)\), (G) restricted to one datum is equivalent
to \(T_*>H\) for that datum. So (G) is not a lemma of intermediate strength on
the way to regularity; it is regularity restated in quotient variables.

**The decision the lane asked for.** The audited insufficiency family is
neither "only an abstract obstruction" nor a counterexample to (G):

- It is an exact counterexample to a *derivability* claim — that (G), or the
 good-set bound, follows from the listed constraints (T1)–(T9) — and Theorem C′
 upgrades that from O2's two facts to the full displayed list.
- Its realization on a trajectory is *logically equivalent to* the negation of
 (G), which by Theorem D is *logically equivalent to* loss of the classical
 branch before the horizon, hence, **for some horizon \(H<\infty\)**, to
 finite-time singularity. So the two horns of the lane's distinction coincide
 here: the family's occurrence on a trajectory is neither excludable nor
 constructible short of settling the Millennium problem.
- Consequently no route that proceeds by "the family cannot occur on a
 trajectory, therefore (G)" can be non-circular. Any proof of (G) must use
 structure that (T1)–(T9) do not encode: the actual equation, the actual
 minimizer, or a quantitative modulus that the audited record does not yet
 supply.

This is a scope statement about proof strategies, not a claim that (G) is
false. **(G) survives this lane intact**; what is refuted is the derivation of
either (G) or the good-set bound from the enumerated constraints (T1)–(T9).

---

## 6. What is left, and the one structure the family exploits

The family of Theorem C′ needs \(n\to\infty\) crossings of the good/bad
boundary inside a time set of measure \(1/n\to0\), with \(\|q\|_3\) travelling
between \(0\) and \(2/C_\sharp\) each time. Every listed constraint is
insensitive to that, because by (A7) the only modulus available for
\(t\mapsto\|q(u(t))\|_3\) is \(\frac12\)-Hölder **with a constant that depends
on \(\|u(t)\|_3\) and on \(\|u(t')-u(t)\|_3\)**, neither of which is input-only
(`lem:quotient-stability` \eqref{eq:cp-strong}, and \(\partial_tu\) is not
controlled in \(L^3\) by input data). This is the single identified point at
which the family could be killed:

> **Open question (next distinct action).** Is there an input-only modulus of
> continuity \(\omega(\nu,u_0,H;\cdot)\) with
> \(\bigl|\;\|q(t')\|_3-\|q(t)\|_3\;\bigr|\le\omega(|t'-t|)\) for all
> \(t,t'<\min\{H,T_*\}\)? Any such modulus bounds the number of crossings of
> the level \(\delta\nu/C_\sharp\) inside a set of measure \(m\) by
> \(\lceil m/\omega^{-1}(\delta\nu/C_\sharp)\rceil\), and combined with (1.2)
> would convert the crossing *measure* bound into a crossing *count* bound — a
> tenth constraint (T10) that the family of Theorem C′ violates outright, which
> would void Theorem C′ and reopen the lane question in the affirmative
> direction.

Two further leads, recorded and not pursued:

- needs review: whether the bad-set restriction of (G) is implied by
 `hyp:absorption` with better constants than the generic dictionary. Corollary
 4.2 of HF21-B already transfers all of (G) from signed pressure absorption
 with \(A_{\rm input}=A+\frac13\|u_0\|_3^3\); Theorem B says only the bad-set
 part is needed, so the transfer could in principle be run on
 \(\mathcal B_\delta\) alone, a set of input-bounded measure. Whether that
 buys anything quantitative is not decided here. If that transfer produces
 \(A_{\mathcal B}\), then (G) follows by Theorem B(1) and the lane's negative
 result becomes irrelevant rather than wrong.
- needs review: whether the exchange rate \((\nu-c)_+\) of Theorem A can be
 improved by replacing the size bound (A2) with a bound whose companion is
 not \(D_3(w)^1\). By Proposition 3.2 of HF21-B two-parameter scaling pins the
 companion to \(D_3(w)^1\) within the monomial lattice, so any improvement
 must leave that lattice.
- needs review: whether a further constraint on \((\mathcal Q,c,D)\) derivable
 from the audited record is violated by the repaired family. The audit found
 two omissions in a list of seven, so a third is not unlikely. Candidates not
 settled: an upper bound on \(D\) in terms of \(\mathcal Q\) and input (none is
 known and none follows from HF18-A); any constraint from
 `lem:quotient-lowstrain` without the cutoff hypothesis; any two-sided
 refinement of \(|K|\le cD\) beyond the monomial lattice of HF21-B Prop. 3.2.

---

## Required closing block

**MODE / RESULT.** DISCOVER. Decided negatively **for derivability from the
displayed constraints (T1)–(T9)**, with an exact obstruction, plus one usable
exact inequality. No input-only bound for \(\int_{\mathcal G_\delta}D_3(w)dt\)
is derivable from the displayed constraints (T1)–(T9) (Theorem C′, explicit
family satisfying (T1)–(T9) with good-set dissipation \(\to\infty\), bad-set
measure \(\to0\) and \(\int c^4\to0\)); the good set is nevertheless *free* in
(G) (Theorem B), so (G) is equivalent to its bad-set restriction with explicit
input constants; and the insufficiency family's occurrence on a trajectory is
logically equivalent to loss of the classical branch before the horizon, hence,
for some horizon \(H<\infty\), to finite-time singularity (Theorem D, which is
the manuscript's `rem:highstrain-scope` and is not new), so it is an obstruction
to derivability only and can be neither excluded nor constructed short of
settling the problem.

**CLAIM AND SCOPE.** For the classical branch of `prop:localtheory` from an
arbitrary divergence-free Schwartz datum, for the unforced full-viscosity
equation on \(\mathbb R^3\), with \(c=C_\sharp\|q\|_3\), \(D=D_3(w)=D_{\mathcal Q}(u)\),
and every \(\tau<T_*\):
(A) \(\int_0^\tau(\nu-c)_+D\,dt\le\frac13\|u_0\|_3^3+\int_{\mathcal B}(c-\nu)D\,dt\);
(B) for \(\delta\in(0,1)\),
\(\int_0^\tau cD\,dt\le\frac{\delta}{1-\delta}\mathcal Q(u_0)+\frac1{1-\delta}\int_{\mathcal B_\delta}cD\,dt\),
with \(|\mathcal B_\delta|\le24C_S^2C_\sharp^4E_0^2\delta^{-4}\nu^{-5}\)
uniformly in \(\tau\); (C) the constraint set (T1)–(T9) does not imply any
input-only bound on \(\int_{\mathcal G_\delta}D\,dt\); (D)
\(\sup_\tau\int_0^\tau cD\,dt=\infty\iff T_*\le H\), and over all \(H<\infty\),
failure of (G) \(\iff T_*<\infty\) — this is `rem:highstrain-scope` transported,
not a new result. Scope: (A), (B), (D) are statements about the audited balances
along the true trajectory and use no regularity of the minimizer, no derivative
of \(\|q\|_3\), no frequency cutoff, no Gronwall term and no smallness; (C) is a
statement about what the displayed constraint list implies, not about
trajectories.

**EVIDENCE.** `prop:quotient-evolution`, `lem:quotient-heatsign`,
`lem:quotient-coercive` \eqref{eq:cp-coercive}, `lem:quotient-stability`
\eqref{eq:cp-strong}, `prop:energy`, `prop:scaling`(iii) \eqref{eq:L4L3},
`rem:highstrain-normalisation`, `rem:highstrain-scope` (the source of
Theorem D), `thm:continuation`, `hyp:critical`, `thm:conditional`
[DI, `../navier-paper/main.tex`];
`hf21-crossing-sign-structure.md` Theorem 4.5, Lemma R3, Lemma 4.3/R4, O1–O3,
Prop. 3.1 (3.1) [DI]; HF18-A facts (Q6) as quoted in HF21-B §0 [DI];
`hf22-review-good-set-dissipation.md` (the audit) for (T8), (T9) and Theorem C′
[DI]. Every computed quantity in Theorem C′ is displayed and checked in the
text. This note ran no numerics; the audit's segment-by-segment integration of
the repaired family for \(n\in\{1,4,16,64,256,1024\}\), which found zero
violations of (T1)–(T9), is bounded evidence and never proof, and nothing here
rests on it.

**FIRST GAP.** Unchanged and not closed. The bad-set restriction of (G):
\(\int_{\mathcal B_\delta}\|q\|_3D_3(w)\,dt\le\) input, on a set of times of
input-bounded measure on which \(C_\sharp\|q\|_3>\delta\nu\). Nothing in the
displayed constraint list bounds \(D_3(w)\) restricted to a set of small
measure, and by Theorem C′ nothing in (T1)–(T9) can. Whether some other
consequence of the audited record can is not decided here.

**SURVIVING CONDITIONAL SUFFIX.** If for one \(\delta\in(0,1)\) and one
input-only \(A_{\mathcal B}\) the bad-set bound
\(\int_{\mathcal B_\delta}\|q\|_3D_3(w)dt\le A_{\mathcal B}\) holds for all
\(\tau<\min\{H,T_*\}\), then (G) holds with
\(A_{\rm input}=\frac{\delta}{3(1-\delta)C_\sharp}\|u_0\|_3^3+\frac{A_{\mathcal B}}{1-\delta}\),
hence `hyp:highstrain` with \(\theta=0\) and no cutoff
(`rem:highstrain-normalisation`), hence `hyp:critical` by
`prop:quotient-conditional`, hence the Clay target by `thm:conditional`.
Independently, if (G) holds then (3.2) gives the good-set dissipation bound —
so the good-set statement is a necessary condition for regularity, never a
sufficient one.

**NON-CLAIMS.** No proof of (G), `hyp:highstrain`, `hyp:highpressure`,
`hyp:absorption`, `hyp:critical` or NS-R3. **No claim that (G) or the good-set
bound is false**: Theorem C′ refutes derivability from (T1)–(T9), not the
statements; and by Theorem B(3) the good-set bound *is* implied by (G), so it
cannot be false unless (G) is. **The constraint list is not claimed
exhaustive; (T8) and (T9) were added by audit**, and the previous version's
exhaustiveness claim and its declaration that (T7) is vacuous were both false
and are withdrawn. No novelty is claimed for Theorem D: it is
`rem:highstrain-scope` of the manuscript. No bound on \(\sup_t\mathcal Q\),
\(\sup_t\|u\|_3\), \(\int D\,dt\) or \(\int D^{4/3}dt\) is claimed or used. No
regularity of the minimizer, no differentiation of \(\|q\|_3\), no evolution
for \(d_1\), no (H1)-type regularity and no use of HF23 or HF18-B. No
comparison between \(D_3(u)\) and \(D_3(w)\) is used or asserted
(`rem:distance-balance`). No forced, periodic, hyperdissipative or Euler
substitute appears; no smallness hypothesis is used anywhere. The family of
Theorem C′ is a family of real functions on \((0,2)\), **not** a Navier–Stokes
solution, and is never claimed to be one; its members are indexed by \(n\) and
need not share a Hölder constant for \(\|q\|_3\). Nothing here is promoted, and
no manuscript or graph file is touched.

**NEXT DISTINCT ACTION.** Decide whether an input-only modulus of continuity
for \(t\mapsto\|q(u(t))\|_3\) exists on \([0,\min\{H,T_*\})\) — equivalently,
an input-only bound on the number of crossings of the level
\(\delta\nu/C_\sharp\). It is the unique structure the Theorem C′ family
exploits, it is not excluded by `lem:quotient-stability` (whose constant is
trajectory-dependent), and combined with (1.2) it would upgrade the audited
crossing *measure* bound to a crossing *count* bound — the first genuinely new
constraint on the bad set since HF21-B, and the one constraint that would void
Theorem C′.
