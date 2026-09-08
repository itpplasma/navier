# CP02: prior-art source check for the pressure route and the related-work subsection

Status: bounded prior-art source audit, 2026-09-05 (Europe/Vienna).
Scope: every external work named in
`prior-art-2026-09-05-user-literature-audit.md` (the user-supplied external
audit; its `citeturn…` / `fileciteturn…` markers are artifacts of the tool
that produced it and carry no evidential weight), checked against the primary
text or the official abstract page, and compared with the objects the
manuscript `../navier-paper/main.tex` actually fixes.

MODE: SOURCE AUDIT.  No mathematical claim of the programme is proved,
strengthened or weakened here.  **No novelty is claimed anywhere in this
note.**  An "unlocated" verdict is a statement about the reach of this bounded
search, *not* evidence of priority, and no HIGH-PRESSURE, HIGH-STRAIN,
CRITICAL, ABSORPTION or NS-R3 result is asserted.

Tags: **[DI]** = statement read directly in the cited source in this lane;
**[MO]** = metadata only (bibliographic identity verified, content not read, or
content verified only through a directly inspected citing source — said
explicitly where that is the case).

Companion notes: `cp01-prior-art-quotient.md` (quotient route, already source
checked; not repeated here), `literature/current-status.md`,
`literature/critical-criteria.md`, `hf01-source-table.md`, `hf02-prior-art.md`.

---

## 0. The manuscript's objects, as fixed for comparison

Read from `main.tex` at the state of this lane (Sections 1, 5, 6, 8, 9).

- (T) **Target.** `def:target`: for every $\nu>0$ and every divergence-free
  Schwartz $u_0$, a global smooth $(u,p)$ on $\R^3\times[0,\infty)$ with
  $\sup_t\|u(t)\|_2^2<\infty$ — Fefferman's unforced whole-space positive
  alternative.  Not proved.
- (B) **Branch.** `prop:localtheory`: the unique maximal *classical* branch
  $(u,p)$ on $[0,T_*)$ from Tao's Theorem 5.4 / Corollaries 4.3, 5.8, with
  normalised pressure $p=R_iR_j(u_iu_j)$ and $H^1$ blowup at $T_*<\infty$.
  Everything below lives on this branch; no weak or Leray--Hopf solution is
  the *subject* of any hypothesis.
- (P) **Cubic balance.** `prop:pressure`, integrated:
  $\tfrac13X'+\nu D_3=P_3$ with $X=\|u\|_3^3$,
  $D_3=\int(|u||\nabla u|^2+|u|\,|\nabla|u||^2)$,
  $P_3=\int p\,\Gamma(u)$, $\Gamma(u)=(u_iu_j\partial_ju_i)/|u|$ off
  $\{u=0\}$ and $0$ on it, i.e. $\Gamma(u)=u\cdot\nabla|u|$ where $u\neq0$.
- (S) **Fixed inhomogeneous low-pass split.** `def:pressure-work`:
  $p_{\le J}=S_Jp$, $p_{>J}=p-p_{\le J}$, $P_3=L_J+Q_J$ with
  $L_J=\int p_{\le J}\Gamma(u)$, $Q_J=\int p_{>J}\Gamma(u)$.  One cutoff $J$,
  not a shell sum; the tail is kept as one **signed** number.
- (L) **Energy-only low-output removal.** `prop:lowpressure`(iii),
  $\bigl|\int_0^\tau L_J\bigr|\le C2^{3J}\|u_0\|_2^4(H/2\nu)^{1/2}
  =:A_{\rm low}$, $C=32\pi/3$, for every $0<\tau<\min\{H,T_*\}$.  Proved; the
  only inputs are $\|u_0\|_2$, $\nu$, $H$, $J$.
- (H) **The open hypothesis.** `hyp:highpressure`:
  $\exists\theta\in[0,1)\ \forall(\nu,u_0,H)\ \exists(J,A_{\rm high})\
  \forall\,0<\tau<\min\{H,T_*\}$:
  $\int_0^\tau Q_J\le\theta\nu\int_0^\tau D_3+A_{\rm high}$, the *same*
  $J,A_{\rm high}$ for the whole interval, and finiteness must not be argued
  through $\sup_{t<T_*}\|u(t)\|_3$ or any equivalent continuation value.
- (E) **Existential equivalence.** `prop:existential-equivalence`: (H) is
  *equivalent* to $T_*=\infty$ for every $(\nu,u_0)$.  Hence (H) is not a
  technical lemma; the manuscript says so.
- (C) **Endpoint.** `thm:continuation` / `thm:conditional`: $T_*<\infty$
  forces $\sup_{t<T_*}\|u(t)\|_3=\infty$, through viscosity normalisation,
  Leray--Hopf membership of the classical branch, ESS Theorem 1.3 and a
  manuscript-owned Serrin-type enstrophy bound; GKP is corroboration only
  (`rem:gkp`).
- (Q) **Quotient route.** `sec:quotient`, `rem:quotient-related`,
  `hyp:highstrain`, `eq:quotient-gap`.  Source-checked separately in
  `cp01-prior-art-quotient.md`; not re-audited here.

---

## 1. Source records

### 1.1 Runlong Yu, `arXiv:2606.25322` — signed pressure--flux work, local, finite chain

**R. Yu, "Coarse-Grained Resolution and Pressure-Flux Work Depletion for
Navier-Stokes CKN Badness", arXiv:2606.25322 [math.AP], submitted 24 June
2026; MSC 35Q30, 35B65, 35B45, 76D05, 76F05.**  **[DI]** — abstract page and
the arXiv HTML body read in this lane.

Objects (eq. (2.5), read): for a spatial filter $S_\ell$,
$U^\ell=S_\ell u$, $P^\ell=S_\ell p$, $R^\ell=S_\ell(u\otimes u)-U^\ell\otimes
U^\ell$, $\Pi^\ell=-R^\ell:\nabla U^\ell$, and the **combined pressure--flux
work distribution**
\[
 G^\ell=\Pi^\ell+\operatorname{div}(P^\ell U^\ell).
\]
Solution class: *suitable weak solutions*, local, on parabolic cylinders
$Q_r(z_0)=B_r(x_0)\times(t_0-r^2,t_0)$ (Definition 2.1).

What it proves.
- A **resolution lemma**: for every $\ell>0$,
  $\Psi(r)\le4\Psi^\ell(r)+4\Omega^\ell(r)$, so a CKN-bad scale is either
  visible at the resolved level or carried by unresolved velocity--pressure
  oscillation (abstract, verbatim).
- An **exact fixed-chain depletion theorem** and, for finite-dimensional
  active test families with common endpoint traces, a constructive active-work
  extraction and a **weighted telescoping inequality** (Theorem 4.1, read):
  over a finite chain of $N$ adjacent slabs with weights $w_k=r_k/r_0$,
  \[
   \sum_{k=0}^{N-1}w_k\bigl(W_k^++D_k\bigr)
   \le E_0^-+\sum_{k=0}^{N-1}w_k|L_k|+\sum_{k=0}^{N-1}w_kW_k^- ,
  \]
  i.e. forward combined work and resolved dissipation are paid by initial
  localized kinetic energy, explicit localization leakage, and negative
  combined work/backscatter.

What it explicitly does **not** prove (Remark 4.2, read verbatim in this
lane): "The theorem is unconditional at fixed $N$, fixed $\ell>0$, and fixed
active profiles.  It does not assert that $I_-$ is small, that $c_k$ is
uniform in a moving-window limit, or that $\sum_kw_k|L_k|$ is summable as
$N\to\infty$."  No global regularity conclusion and no statement about
$L^3(\R^3)$ norms is claimed.

Relation to (S),(H).  **Different object, different domain, different
quantifiers.**  $G^\ell$ is a *local, coarse-grained, filtered-in-space* work
density built from $S_\ell$ applied to $u$, $p$ and $u\otimes u$, paired
against $\nabla U^\ell$; $Q_J$ is the *global* pairing of the exact
high-frequency pressure $p_{>J}$ against the exact cubic integrand
$\Gamma(u)$ of the $L^3$ balance, with no filtering of $u$.  Yu's chain is a
finite family of nested space-time slabs with $N$ fixed and a scale weight
$w_k$; the manuscript has one cutoff $J$ and no chain.  Yu's inequality is
paid by *localized* initial energy plus leakage plus backscatter, at fixed
$N,\ell$; (H) requires witnesses $J,A_{\rm high}$ chosen before $\forall\tau$
and valid up to a possible finite $T_*$.  A telescoping law for $Q_J$ is not
supplied by Theorem 4.1 and Yu does not claim it is.  **Prior art for
"signed pressure--flux work with scale decomposition, budget and weighted
telescoping" as a mechanism**; not prior art for (H), and (H) is not implied
by it.

### 1.2 Runlong Yu, `arXiv:2606.25341` — the author's own statement of the remaining gap

**R. Yu, "A Structural Audit of Navier-Stokes Obstruction Calculus",
arXiv:2606.25341 [math.AP], submitted 24 June 2026; MSC 35Q30, 35B65, 35B45,
76D05.**  **[DI]** — official abstract page read.

Verbatim from the abstract: the critical ledgers, coarse-grained defect
decompositions, pressure--flux work identities, quotient cleanings and
bad-scale counting mechanisms "form an obstruction calculus … but they do not
by themselves provide a coercive estimate excluding a surviving obstruction";
the paper proves a resolution lemma "and show[s] that no unconditional
single-scale domination by a signed combined-work detector is available"; the
next necessary target is identified as "a filtered stretching--diffusion
estimate".

Relation.  This is the closest published *negative* statement to the
manuscript's own position: a coercive estimate for a signed combined-work
detector is exactly what (H) would be, in the local coarse-grained setting.
It is a statement about Yu's detector on parabolic cylinders, not about $Q_J$
on $\R^3$, so it neither proves nor refutes (H).  It does show that the
mechanism-level idea is public and that its authors regard the coercive step
as open.

### 1.3 Runlong Yu, `arXiv:2606.12756` — conditional local cascade reduction

**R. Yu, "Invisible Defect Cascades for Navier-Stokes Regularity",
arXiv:2606.12756 [math.AP], submitted 10 June 2026; MSC 35Q30, 35B65, 35B45,
76D05.**  **[DI]** — official abstract page read.

A *conditional* scale-critical defect-cascade reduction for the **local**
regularity problem: at putative singular points where no sufficiently small
dyadic scale satisfies the CKN smallness criterion, such points must produce
either ineffective moving-window observability or "an NS-realizable, cleaned,
scale-critical defect cascade invisible to the combined active-pressure, flux,
energy, and adjoint-trace tests"; tools are dyadic rescaling, pressure
splitting, Reynolds covariance and local energy-flux identities.

Relation.  Local CKN object, conditional conclusion about singular points.
The manuscript's (H)→(C)→(T) chain is a whole-space, arbitrary-data,
finite-horizon statement about a classical branch.  Different object,
different quantifiers, no overlap at theorem level.

Also located and recorded, not cited: **R. Yu, "Finite-Chain CKN-Bad Scale
Counting for Navier-Stokes: Standard PDE Closure and Canonical Detector
Realization", arXiv:2606.21783, 19 June 2026** **[MO]** (title, author, date
and first abstract sentences read): a finite-chain counting theorem bounding
the weighted size of a finite set of CKN-bad scales by nonnegative channel
costs.  Same local programme.

### 1.4 Tran--Yu--Dritschel 2021 — the same $q=3$ identity, and an amplitude split with absorption

**C. V. Tran, X. Yu and D. G. Dritschel, "Velocity--pressure correlation in
Navier--Stokes flows and the problem of global regularity", J. Fluid Mech.
911 (2021), A18, DOI 10.1017/jfm.2020.1033.**  **[DI]** — the accepted
manuscript (St Andrews repository copy of the JFM article, and the author
preprint) read in full for §§1--3.

Note on identity: the "Yu" here is **Xinwei Yu** (Alberta), not Runlong Yu.
The two lines are unrelated.

What it states and proves, in its own notation ($\nu=1$, $\hat u=u/|u|$).
- Equation (2.2):
  \[
   \frac1q\frac{d}{dt}\|u\|_{L^q}^q=(q-2)\int_{\R^3}p|u|^{q-3}u\cdot\nabla|u|\,dx
   -(q-2)\bigl\||u|^{(q-2)/2}\nabla|u|\bigr\|_{L^2}^2
   -\bigl\||u|^{(q-2)/2}\nabla u\bigr\|_{L^2}^2 .
  \]
  **At $q=3$ this is exactly the manuscript's (P)** with $\nu=1$: the driving
  term is $\int p\,u\cdot\nabla|u|$, i.e. $P_3$, and the two dissipation terms
  are $\int|u|\,|\nabla|u||^2$ and $\int|u|\,|\nabla u|^2$, i.e. $D_3$.  This
  is the single most important correction this lane makes to the internal
  record: the cubic balance itself is published, in a peer-reviewed journal,
  for $L^q$ with $q\ge3$.  The manuscript's contribution at that point is the
  *proof on its own solution class* (regularisation of $|u|$, cutoff limit,
  integrated form, integrands vanishing on $\{u=0\}$), not the identity.
- A **spatial amplitude split with absorption**: $\Omega=\{|u|>U\}$,
  $\Omega^c=\R^3\setminus\Omega$, and (3.2)
  $\int_{\Omega^c}p|u|^{q-2}\hat u\cdot\nabla|u|
  \le\frac12\||u|^{(q-2)/2}\nabla|u|\|_{L^2}^2$, where (3.3)
  $U:=\bigl(R\||u|^{(q-2)/2}\nabla|u|\|_{L^2}/(2\|p\|_{L^2})\bigr)^{2/(q-2)}$
  and $R\ge1$ is the ratio of total dissipation to dissipation on $\Omega^c$.
  A second reduction by a pressure threshold $P$ gives $\Omega_0$ and (3.11)
  with a $q/4$ dissipation margin.
- Theorem 3.1 (read verbatim): let $\{u,p\}$ be a Leray--Hopf solution, smooth
  on $(0,T)$; it remains smooth up to and beyond $T$ if one of
  (a) $\int_0^T\Gamma_s R_0^{-2}\|u\|_{L^s}^{2s/(s-3)}dt<\infty$ for some
  $s\in(3,\infty)$, (b) the $s\in(3,5]$ variant with
  $\Gamma_3R_0^{-2}\|u\|_{L^3}^{-3}$ raised to $(9-s)/(2s-6)$, (c) the $s>5$
  variant with $\Gamma_3R_0^{-2}\|u\|_{L^3}^{-6/(s-3)}$, where
  $\Gamma_q:=\int_{\Omega_0}p^2|u|^{q-2}dx\big/\|u\|_{L^{q+2}}^{q+2}$ and
  $R_0\ge1$.

Relation to (S),(L),(H).  Three exact differences, at objects and
quantifiers.
1. **Where the split lives.**  TYD split *physical space by velocity
   amplitude*; the manuscript splits the *pressure in frequency* at one
   integer cutoff $J$.  $\Omega$ and $\Omega_0$ are level sets of $|u|$ and
   $|p|$; $p_{\le J},p_{>J}$ are Fourier multiplier pieces of $p$ alone.
2. **How the low part is disposed of.**  TYD *absorb* the $\Omega^c$ part into
   the dissipation with constant $\tfrac12$; the manuscript *removes* the low
   part by an energy-only bound $A_{\rm low}$ that costs no dissipation at all
   and depends only on $(\nu,\|u_0\|_2,H,J)$.  These are different operations
   with different budgets.
3. **What the witnesses may depend on.**  TYD's threshold $U$ is defined
   implicitly through the solution's own $\|p\|_{L^2}$ and weighted
   dissipation at time $t$ (3.3)--(3.5) — a solution-dependent, time-dependent
   quantity; the manuscript's $J$ must be selected from $(\nu,u_0,H)$ before
   $\forall\tau$, and (H) forbids arguing finiteness through a continuation
   norm.  TYD's conclusion is a conditional criterion of the form "if this
   time integral of solution quantities is finite, regularity persists"; the
   manuscript's (H) is an assertion *about every solution* with witnesses
   quantified before the time variable.
Verdict: **the closest published relative of (P) and of the low/high split
idea**, sharing the identity outright at $q=3$; it is not (L), not (H), and
its criteria are not implied by, and do not imply, either.

### 1.5 Bradshaw--Grujić 2017 — frequency-localised criteria, on the velocity

**Z. Bradshaw and Z. Grujić, "Frequency Localized Regularity Criteria for the
3D Navier--Stokes Equations", Arch. Ration. Mech. Anal. 224 (2017), no. 1,
125--133, DOI 10.1007/s00205-016-1069-9; arXiv:1501.01043 (v1 5 Jan 2015,
v2 21 Nov 2016).**  **[DI]** for the arXiv abstract and version dates;
**[MO]** for the article body (Springer landing page returns HTTP 303 to an
identity provider and was not readable in this lane); volume, issue, pages and
author order verified on the Crossref record.

Abstract, verbatim: "Two regularity criteria are established to highlight
which Littlewood-Paley frequencies play an essential role in possible
singularity formation in a Leray-Hopf weak solution … One of these is a
frequency localized refinement of known Ladyzhenskaya-Prodi-Serrin-type
regularity criteria restricted to a finite window of frequencies the lower
bound of which diverges to $+\infty$ as $t$ approaches an initial singular
time."

Relation.  Prior art for "a Littlewood--Paley window carries the regularity
question" — the manuscript claims nothing about that idea.  The object is
frequency-localised *velocity* in an LPS-type criterion for Leray--Hopf weak
solutions, and the window's lower edge moves with $t$.  The manuscript's
object is the signed pairing of the frequency-localised *pressure* against the
cubic integrand of the $L^3$ balance, with **one fixed** $J$ chosen from the
inputs and held for the whole interval.  Different object; the "moving
window" and "fixed cutoff" quantifier structures are incompatible rather than
comparable.

### 1.6 The classical pressure-criterion line

- **L. C. Berselli and G. P. Galdi, "Regularity criteria involving the
  pressure for the weak solutions to the Navier--Stokes equations", Proc.
  Amer. Math. Soc. 130 (2002), no. 12, 3585--3595, DOI
  10.1090/S0002-9939-02-06697-2.**  **[MO]** for identity (Crossref);
  content **[DI]** through a directly inspected citing source, Pineau--Yu,
  arXiv:1910.08911v1, Theorem 1: *Leray--Hopf $u$ with
  $u_0\in H(\R^n)\cap L^n(\R^n)$; if $p\in L^r(0,T;L^s(\R^n))$ with
  $2/r+n/s\le2$, $s>n/2$, then $u$ is smooth on $(0,T]\times\R^n$ and extends
  beyond $T$.*
- **D. Chae and J. Lee, "Regularity criterion in terms of pressure for the
  Navier--Stokes equations", Nonlinear Anal. 46 (2001), no. 5, 727--735, DOI
  10.1016/S0362-546X(00)00163-2.**  **[MO]** for identity (Crossref); content
  **[DI]** through Tran--Yu--Dritschel §1, eq. (1.6): the criterion
  $\int_0^T\|p\|_{L^s(\R^3)}^{2s/(2s-3)}dt<\infty$, $s>3/2$, "was derived by
  Chae & Lee (2001) and Berselli & Galdi (2002)".
- **H. Beirão da Veiga, "A new regularity class for the Navier--Stokes
  equations in $\R^n$", Chinese Ann. Math. Ser. B 16 (1995), no. 4,
  407--412.**  **[MO]** for identity; the entry was read verbatim in two
  independently inspected reference lists (Pineau--Yu arXiv:1910.08911, ref.
  [8]; arXiv:2102.06152, ref. [B]).  Content **[DI]** through the arXiv HTML
  of 2102.06152: regularity holds if
  $\nabla u\in L^q_tL^p_x$ with $2/q+3/p\le2$ and $p\in(3/2,\infty)$.
  **Correction to the user audit:** this is a *velocity-gradient* Serrin class,
  not a pressure criterion.  It belongs to the pressure line only through the
  scaling coincidence between $\nabla u$ and $p$; it should not be described
  as an early pressure criterion.
- **Y. Zhou, "Regularity criteria in terms of pressure for the 3-D
  Navier--Stokes equations in a generic domain", Math. Ann. 328 (2004), no.
  1--2, 173--192, DOI 10.1007/s00208-003-0478-x.**  **[MO], identity only.**
  The Springer landing page returns HTTP 303 to an identity provider; the
  Semantic Scholar record carries the note that the abstract field was elided
  by the publisher.  **The content was not read in this lane.**
  **Correction to the user audit:** the $\nabla p$ criterion the audit
  attributes to "Zhou 2004" is stated verbatim in a directly inspected source,
  Cai--Zhai, arXiv:math/0611843v1, §1 — "$\nabla p\in L^\alpha(0,T;
  L^\gamma(\R^3))$ with $2/\alpha+3/\gamma\le3$, $2/3<\alpha<\infty$,
  $1<\gamma<\infty$, or $\nabla p\in L^{2/3}(0,T;L^\infty(\R^3))$, or else
  $\|\nabla p\|_{L^\infty(0,T;L^\infty)}$ sufficiently small" — but that
  source's reference [2] is **Y. Zhou, Proc. Amer. Math. Soc. 134 (2006), no.
  1, 149--156** (DOI 10.1090/S0002-9939-05-08312-7), a *different* paper.  A
  third Zhou paper in the same line is ZAMP 57 (2005), no. 3, 384--392.  Any
  manuscript sentence must therefore either cite Math. Ann. 328 (2004) for
  the general fact that pressure and pressure-gradient criteria exist, or cite
  the PAMS paper for the displayed $\nabla p$ condition.  Attributing the
  displayed condition to the Math. Ann. paper is not verified here.
- **H. Beirão da Veiga and J. Yang, "On Mixed Pressure-Velocity Regularity
  Criteria to the Navier--Stokes Equations in Lorentz Spaces, Part II: The
  Non-slip Boundary Value Problem", Chin. Ann. Math. Ser. B 43 (2022), no. 1,
  51--58, DOI 10.1007/s11401-022-0303-z.**  **[MO]**, Crossref record.
  **Scope warning:** Part II is the *non-slip boundary value problem*, i.e. a
  bounded domain with boundary, a different domain from the manuscript's
  $\R^3$.  The whole-space/torus statement of that line is **Part I**, Chin.
  Ann. Math. Ser. B 42 (2021), no. 1, 1--16, DOI 10.1007/s11401-021-0242-0,
  already recorded **[DI]** in `hf01-source-table.md` from arXiv:2007.02089
  (Theorem 5.2: $\pi/(e^{-|x|^2}+|v|)^\theta$ in a Lorentz class,
  $0\le\theta\le1$, $2/p+3/q=2-\theta$; Lemma 6.1: the $p=4$ weighted
  identity).  If the manuscript wants a mixed pressure--velocity criterion on
  $\R^3$, Part I is the correct citation.

Relation of the whole line to (H).  Every one of these is a **conditional
criterion**: *assume* a space-time integrability or smallness property of
$p$, $\nabla p$, $\nabla u$ or a mixed quantity, *conclude* regularity.  The
quantifier shape is "if a norm of the solution is finite, then regularity".
(H) is not of that shape: it asserts, for every datum, a bound on a **signed,
time-integrated pairing** $\int_0^\tau Q_J$ against $\theta\nu\int_0^\tau D_3$
plus a remainder whose witnesses are fixed before $\forall\tau$ and may not be
defined through any continuation norm.  No absolute-value norm of $p_{>J}$ is
assumed anywhere, and `lem:absorption-split` explicitly notes that
absolute-value Calderón--Zygmund estimates shell by shell discard the signed
cancellation.  Conversely, no criterion in this line yields (H) or (C).  The
manuscript must claim nothing about "pressure-based regularity criteria" as a
class.

### 1.7 Endpoint and target layer

Already cited in `main.tex` and re-verified only for status: **Clay
Mathematics Institute, Navier--Stokes problem page**, accessed 2026-09-05,
status "**Unsolved**", official statement by **Charles L. Fefferman**
(`claymath.org/wp-content/uploads/2022/06/navierstokes.pdf`) **[DI]**.
`ESS2003`, `GKP2013`, `Tao2013`, `Kato1984` are unchanged and were audited in
`literature/critical-criteria.md`.  Nothing in this lane changes the
manuscript's use of ESS Theorem 1.3 or its treatment of GKP as corroboration.

### 1.8 Self-published preprints and public claimed proofs

- **S. Taghizadeh, "A Local Monotonicity Reduction of the 3D Navier--Stokes
  Regularity Problem to a Single Remaining Barrier", Zenodo preprint, v3,
  3 February 2026, DOI 10.5281/zenodo.18468477, CC-BY-4.0.**  **[DI]** —
  Zenodo record page read.  Description: a scale-invariant **local**
  monotonicity framework; advective flux, pressure nonlocality and
  localization errors are treated; global regularity is reduced to "a single
  explicit local condition: the behavior of a monotonicity functional in the
  limit of vanishing scales"; one precisely defined barrier remains.  Stated
  as submitted to Communications in Mathematical Physics.  Not peer reviewed
  as of the cut-off.  Relation: terminologically close ("reduction to a single
  remaining barrier"), architecturally different — a local vanishing-scale
  monotonicity limit versus a global finite-horizon signed pressure-work
  estimate with an input-selected frequency cutoff.  Not used.
- **J. T. Cox, "Resolving Global Regularity for the 3D Navier--Stokes
  Equations at the Critical Endpoint", ResearchGate publication 397174185
  (2025).**  **NOT VERIFIED.**  The ResearchGate page returned HTTP 403
  Forbidden in this lane; no title page, author affiliation, date, licence or
  abstract could be read from the primary record, and no DOI, arXiv identifier
  or journal record was located.  **Excluded from the BibTeX list and from the
  LaTeX block.**  Nothing about its content is asserted here.

### 1.9 Public repositories — README statements only

These are recorded as *repository facts*, never as mathematical sources, and
none is cited in the manuscript.

- **`github.com/johnrobertlawson/brc-navier-stokes`** (pushed 2026-07-27)
  **[DI]** README: "This repository is a plain-language map of the
  three-dimensional incompressible Navier--Stokes Millennium Problem, backed
  by a proof lab that treats every serious claim as something to audit, test,
  or falsify"; "The current status is simple: the problem is unsolved";
  "Passing checks do not certify a theorem.  They certify bookkeeping and the
  algebraic parts explicitly covered by the tests."
- **`github.com/davidkny22/navier-stokes-conditional`** (pushed 2026-07-29)
  **[DI]** README: author David Kogan, May 2026; states the conditional
  criterion "If $\int_0^TD_2(t)^{2/3}dt<\infty$, then the solution remains
  regular on $[0,T]$" with $D_2=\int|\omega|^2|\nabla\xi|^2$,
  $\xi=\omega/|\omega|$; states LLM assistance (Claude, GPT-5.5 Pro), an
  internal literature review of 913 sources, that "expert review would be
  needed to settle the question definitively", and "All rights reserved".
  Vorticity-geometry object; no pressure work, no $L^3$ budget.
- **`github.com/lizizatt/scratch`**, subproject `navier_stokes_millennium`
  (repo pushed 2026-09-04; subproject README status line 2026-08-18)
  **[DI]** README: "It does **not** claim to contain a solution"; two
  conditional theorems `LOCAL-L3-CONTINUATION` and
  `LOCAL-L3-RECORD-CENTERS`; "The validator checks structure and references,
  not mathematical truth"; the latest recorded round concerns a scale-critical
  localized kinetic-enstrophy functional with a blocked fixed-time annular
  tail.  **The user audit's description of this repository — a localized
  $\int\chi_{R,a}|u|^3$ functional whose interior pressure pairing is declared
  sign-indefinite and the route "blocked" — is *not* confirmed by the README
  at the state read on 2026-09-05.**  Recorded as unconfirmed; no inference
  either way.
- **`github.com/vporton/navier-stokes`** (pushed 2026-06-04) **[DI]** README:
  claims "A solution of Navier-Stokes Clay Math Millennium Prize Problem"
  derived from the author's own extension theorem "in collaboration with
  LLM", links a ResearchGate PDF and a Lean formalization attempt.  Clay
  lists the problem as unsolved; not accepted, not used.
- **`github.com/ricalanis/navier-stokes-playresearch`** (pushed 2026-01-14)
  **[MO]**, GitHub API description only ("Playing around claude code with
  navier stokes"); README not read.

### 1.10 AI-assisted fluid-singularity programme (context only)

**"Discovery of Unstable Singularities", arXiv:2509.14185, 17 September 2025,
by a large collaboration including J. Gómez-Serrano and Google DeepMind
(individual authorship not read in this lane)** **[MO]** — identity, date and
subject verified through indexed records and reporting; the object is
neural-network discovery of *unstable self-similar singularities* for
incompressible porous media, Boussinesq and Euler-type equations, not a
regularity theorem for 3D Navier--Stokes.  Different direction entirely;
context only, not cited.

---

## 2. Verified comparison table

Compared at the level of objects and quantifiers, not vocabulary.  "—" means
the parameter does not occur in that work.

| Work | Solution class and domain | Object it estimates | Quantifier shape of its main statement | Relation to (S),(L),(H) | Tag |
|---|---|---|---|---|---|
| **This manuscript** | maximal *classical* branch from Schwartz data, $\R^3$ | $\int_0^\tau Q_J$, $Q_J=\int p_{>J}\Gamma(u)$, signed, against $\theta\nu\int_0^\tau D_3$ | $\exists\theta<1\ \forall(\nu,u_0,H)\ \exists(J,A_{\rm high})\ \forall\tau<\min\{H,T_*\}$; witnesses non-circular | (P),(L),(C),(E) proved; **(H) open**, and equivalent to $T_*=\infty$ | — |
| Tran--Yu--Dritschel 2021 | Leray--Hopf, smooth on $(0,T)$, $\R^3$ | $\int_{\Omega_0}p|u|^{q-2}\hat u\cdot\nabla|u|$ after an amplitude split; correlation $\Gamma_q$ | if a time integral of $\Gamma_s R_0^{-2}\|u\|_{L^s}^{2s/(s-3)}$ is finite, then smooth past $T$ | **(2.2) at $q=3$ is (P)**; low part *absorbed*, not removed; split in space by $|u|$, threshold solution-defined | [DI] |
| Yu, 2606.25322 | suitable weak, local, $Q_r(z_0)$ | $G^\ell=\Pi^\ell+\div(P^\ell U^\ell)$, filtered | unconditional at fixed $N$, fixed $\ell$, fixed active profiles; explicitly not summable as $N\to\infty$ | signed flux + scale chain + telescoping as a *mechanism*; different object, local, no $L^3$ or global claim | [DI] |
| Yu, 2606.25341 | suitable weak, local | signed combined-work detector | "no unconditional single-scale domination … is available" | author's own statement that the coercive step is open in his setting | [DI] |
| Yu, 2606.12756 | suitable weak, local, putative singular points | cleaned scale-critical defect cascade | conditional reduction | local CKN; no global finite-horizon statement | [DI] |
| Bradshaw--Grujić 2017 | Leray--Hopf weak, $\R^3$ | frequency-localised **velocity** in an LPS-type norm | if the criterion holds on a frequency window whose lower edge $\to+\infty$ as $t\uparrow$ singular time | frequency localisation is prior art; window *moves*, manuscript's $J$ is **fixed** and input-selected; object is velocity, not pressure work | [DI] abstract / [MO] body |
| Berselli--Galdi 2002 | Leray--Hopf, $u_0\in H\cap L^n$, $\R^n$ | $\|p\|_{L^s}$, absolute | if $p\in L^r_tL^s_x$, $2/r+n/s\le2$, $s>n/2$, then smooth | absolute norm assumption; no signed pairing, no dissipation absorption budget | [MO] id / [DI] via Pineau--Yu Thm 1 |
| Chae--Lee 2001 | weak solutions, $\R^3$ | $\|p\|_{L^s}$, absolute | if $\int_0^T\|p\|_{L^s}^{2s/(2s-3)}dt<\infty$, $s>3/2$ | same shape as above | [MO] id / [DI] via TYD (1.6) |
| Beirão da Veiga 1995 | weak solutions, $\R^n$ | $\nabla u$, absolute | if $\nabla u\in L^q_tL^p_x$, $2/q+3/p\le2$, $p\in(3/2,\infty)$ | **velocity-gradient** class, not a pressure criterion | [MO] id / [DI] via arXiv:2102.06152 |
| Zhou 2004 | weak solutions, generic domain | $p$ and/or $\nabla p$ | conditional criterion (exact hypotheses **not read in this lane**) | pressure-criterion prior art at class level only; the displayed $\nabla p$ condition belongs to Zhou, PAMS 134 (2006), 149--156 | [MO] identity only |
| Beirão da Veiga--Yang 2022 (Part II) | weak solutions, **bounded domain, non-slip boundary** | mixed pressure--velocity in Lorentz spaces | conditional criterion | different domain; the $\R^3$ statement is Part I (2021) | [MO] |
| Taghizadeh 2026 | local framework | monotonicity functional as scale $\to0$ | reduction to one local vanishing-scale condition | local, not (H); shared vocabulary only | [DI] record |
| Cox 2025 | — | — | — | **identity not verified**; excluded | — |
| Kogan 2026 (repo) | — (README) | $D_2=\int|\omega|^2|\nabla\xi|^2$ | if $\int_0^TD_2^{2/3}dt<\infty$ then regular | vorticity geometry; not a pressure or $L^3$ object | [DI] README |
| BRC/Lawson, lizizatt, vporton, ricalanis (repos) | — (README) | — | READMEs state, respectively: unsolved and checks do not certify theorems; no solution claimed; a claimed solution; play research | workflow/landscape only; never a mathematical source | [DI] / [MO] |
| DeepMind, arXiv:2509.14185 | Euler/IPM/Boussinesq-type | unstable self-similar singularity profiles | numerical/neural discovery | different equations and direction | [MO] |

**Findings of this table.**  (i) The cubic balance (P) is *published* at
$q=3$ in Tran--Yu--Dritschel (2.2); no novelty may be claimed for the identity
itself.  (ii) Signed pressure--flux work with a scale decomposition, a budget
and a weighted telescoping inequality is public prior art at mechanism level
(Yu 2026), for a *different, local, filtered* observable.  (iii) A high/low
split of the cubic driving term with absorption of the low part into the
dissipation is public prior art (TYD §3), *in physical space with a
solution-defined threshold*.  (iv) No located work states (L) — the removal of
the entire low output by an energy-only bound at a fixed frequency cutoff —
nor (H) with its quantifier order and non-circularity requirement, nor the
equivalence (E).  (iv) is an absence in a bounded search and is not evidence
of priority.

---

## 3. LaTeX block for `main.tex` (end of Section 1, `subsec:related`)

Insert after the paragraph following Theorem~\ref{def:target}, before
`\section{Local theory…}`.  Keys must be added to `references.bib` from §4.

```latex
\subsection{Related work and the scope of what is new}
\label{subsec:related}

\emph{Target and endpoint theory.}  The target is Fefferman's official
unforced whole-space alternative \cite{Fefferman2000}, which the Clay
Mathematics Institute lists as unsolved.  The endpoint used in
Section~\ref{sec:continuation} is Theorem~1.3 of Escauriaza, Seregin, and
\v Sver\'ak \cite{ESS2003}, with Gallagher, Koch, and Planchon
\cite{GKP2013} as corroboration only (Remark~\ref{rem:gkp}); the local
theory is Tao's \cite{Tao2013}, and the small-critical-data theory is
Kato's \cite{Kato1984}.  None of this layer is claimed here.

\emph{Pressure criteria.}  Conditional regularity under an integrability or
smallness assumption on the pressure or its gradient is a long line: Chae and
Lee \cite{ChaeLee2001} and Berselli and Galdi \cite{BerselliGaldi2002} prove
that a Leray--Hopf solution with $p\in L^r_tL^s_x$, $2/r+3/s\le2$, $s>3/2$,
is smooth and extends; Zhou \cite{Zhou2004} gives criteria in terms of the
pressure in a generic domain; Beir\~ao da Veiga \cite{BeiraoDaVeiga1995}
proves the companion velocity-gradient class $\nabla u\in L^q_tL^p_x$,
$2/q+3/p\le2$; and mixed pressure--velocity conditions in Lorentz spaces are
treated by Beir\~ao da Veiga and Yang
\cite{BeiraoDaVeigaYang2021,BeiraoDaVeigaYang2022}.  Every statement in this
line assumes finiteness or smallness of an \emph{absolute} norm of $p$,
$\nabla p$ or $\nabla u$ along the solution and concludes regularity.
Hypothesis~\ref{hyp:highpressure} is not of that form: it assumes no norm of
$p_{>J}$, it constrains the \emph{signed} time integral $\int_0^\tau Q_J$
against $\theta\nu\int_0^\tau D_3$, and its witnesses $J$ and
$A_{\rm high}$ are quantified before $\tau$ and may not be defined through
any continuation norm.  Nothing about pressure-based criteria as a class is
claimed here.

\emph{Frequency-localised criteria.}  Bradshaw and Gruji\'c
\cite{BradshawGrujic2017} prove two Littlewood--Paley localised criteria for
Leray--Hopf weak solutions, one of them a frequency-localised refinement of
the Ladyzhenskaya--Prodi--Serrin criteria on a window of frequencies whose
lower edge diverges as $t$ approaches an initial singular time.  Their
localised object is the velocity, and their window moves with $t$; the object
in Section~\ref{sec:pressure} is the pressure, localised once at a single
integer $J$ selected from $(\nu,u_0,H)$ and held fixed for the whole
interval.

\emph{Velocity--pressure correlation and the cubic balance.}  The identity
behind Proposition~\ref{prop:pressure} is not new.  Tran, Yu, and Dritschel
\cite[eq.~(2.2)]{TranYuDritschel2021} record, for $q\ge3$, the evolution of
$\|u\|_q^q$ with driving term $(q-2)\int p\,|u|^{q-3}u\cdot\nabla|u|$ and
the two weighted dissipation terms; at $q=3$ this is exactly
$\tfrac13X'+\nu D_3=P_3$ at unit viscosity.  What Section~\ref{sec:pressure}
adds is a proof of that identity on the classical branch of
Proposition~\ref{prop:localtheory}, in integrated form, with integrands
defined to vanish on $\{u=0\}$.  The same authors split $\mathbb R^3$ into
high- and low-velocity regions and absorb the low-velocity part of the
driving term into the dissipation, with a threshold defined implicitly
through the solution's own norms, and obtain conditional criteria involving
a velocity--pressure correlation coefficient.  Their split is in physical
space by amplitude and their threshold depends on the solution at time $t$;
the split used here is in frequency, the low part is removed by the
energy-only bound of Proposition~\ref{prop:lowpressure} rather than absorbed
into $D_3$, and the cutoff is selected from the data alone.

\emph{Signed flux and telescoping.}  Yu \cite{Yu2026a} proves, for suitable
weak solutions on parabolic cylinders, a coarse-grained resolution lemma and
an exact fixed-chain depletion theorem for the combined pressure--flux work
$G^\ell=\Pi^\ell+\operatorname{div}(P^\ell U^\ell)$ built from a spatial
filter, together with a weighted telescoping inequality over a finite chain
of scales, and states that the result is unconditional only at fixed chain
length and fixed filter length.  Companion papers give a conditional local
defect-cascade reduction \cite{Yu2026c} and an audit concluding that no
unconditional single-scale domination by a signed combined-work detector is
available in that framework \cite{Yu2026b}.  Those results concern a
filtered, local observable on space-time cylinders and make no assertion
about $L^3(\mathbb R^3)$; the object here is the unfiltered pairing
$Q_J=\int p_{>J}\,\Gamma(u)$ on the whole space, kept as one signed number
rather than a chain, and no telescoping law for it is proved in this paper.

\emph{The quotient route.}  The prior art for
Section~\ref{sec:quotient} — nonlinear Hodge theory for closed data and
bounded densities, and Kato's $L^p$ Lyapunov and monotonicity lemmas — is
discussed in Remark~\ref{rem:quotient-related} and is not repeated here.

\emph{Publicly claimed proofs.}  Several self-published manuscripts and
public repositories from 2025--2026 announce reductions of, or solutions to,
the three-dimensional regularity problem, some with overlapping vocabulary
such as pressure cancellation or a single remaining barrier
\cite{Taghizadeh2026}.  None is used anywhere in this paper, none is relied
on for any statement, and none is treated here as accepted mathematics.

To the best of our knowledge, the reduction of the arbitrary-data whole-space
critical problem to one signed, time-integrated high-output pressure-work
estimate after an energy-only elimination of all fixed low outputs, with one
input-selected cutoff and endpoint-uniform witnesses, together with its exact
equivalence to continuation (Proposition~\ref{prop:existential-equivalence}),
was not located in this form.  That is a statement about the reach of a
bounded literature search, not a claim of priority, and no component of the
route is claimed to be new: the endpoint theory, the pressure and
frequency-localised criteria, the cubic balance at $q=3$, and signed
pressure--flux telescoping for coarse-grained observables are all prior work
cited above.
```

Word/length check: the block is nine short paragraphs; at the manuscript's
current 11pt/`\baselineskip` it typesets within one page.  If it overruns,
delete the two sentences beginning "Companion papers give" and "Their split
is in physical space" without changing any claim.

---

## 4. BibTeX entries

Verified entries follow.  Provenance is stated per entry.  `Kato1990`,
`MannaSritharan2007`, `SibnerSibner1970`, `Scott1995` and
`IwaniecScottStroffolini1999` are **already present in
`../navier-paper/references.bib`**; their fields were re-checked
against Crossref in this lane and are correct as written, with two optional
additions noted.  `Cox2025` is **not supplied**: see §1.8.

```bibtex
@article{Yu2026a,
  author       = {Runlong Yu},
  title        = {Coarse-Grained Resolution and Pressure-Flux Work Depletion
                  for {Navier--Stokes} {CKN} Badness},
  journal      = {arXiv preprint},
  year         = {2026},
  eprint       = {2606.25322},
  archivePrefix= {arXiv},
  primaryClass = {math.AP},
  note         = {Submitted 24 June 2026}
}

@article{Yu2026b,
  author       = {Runlong Yu},
  title        = {A Structural Audit of {Navier--Stokes} Obstruction Calculus},
  journal      = {arXiv preprint},
  year         = {2026},
  eprint       = {2606.25341},
  archivePrefix= {arXiv},
  primaryClass = {math.AP},
  note         = {Submitted 24 June 2026}
}

@article{Yu2026c,
  author       = {Runlong Yu},
  title        = {Invisible Defect Cascades for {Navier--Stokes} Regularity},
  journal      = {arXiv preprint},
  year         = {2026},
  eprint       = {2606.12756},
  archivePrefix= {arXiv},
  primaryClass = {math.AP},
  note         = {Submitted 10 June 2026}
}

@article{TranYuDritschel2021,
  author  = {Chuong V. Tran and Xinwei Yu and David G. Dritschel},
  title   = {Velocity--pressure correlation in {Navier--Stokes} flows and the
             problem of global regularity},
  journal = {Journal of Fluid Mechanics},
  volume  = {911},
  year    = {2021},
  pages   = {A18},
  doi     = {10.1017/jfm.2020.1033}
}

@article{BradshawGrujic2017,
  author  = {Zachary Bradshaw and Zoran Gruji\'c},
  title   = {Frequency Localized Regularity Criteria for the {3D}
             {Navier--Stokes} Equations},
  journal = {Archive for Rational Mechanics and Analysis},
  volume  = {224},
  number  = {1},
  year    = {2017},
  pages   = {125--133},
  doi     = {10.1007/s00205-016-1069-9},
  note    = {Published online 21 November 2016}
}

@article{Zhou2004,
  author  = {Yong Zhou},
  title   = {Regularity criteria in terms of pressure for the {3-D}
             {Navier--Stokes} equations in a generic domain},
  journal = {Mathematische Annalen},
  volume  = {328},
  number  = {1--2},
  year    = {2004},
  pages   = {173--192},
  doi     = {10.1007/s00208-003-0478-x}
}

@article{BeiraoDaVeiga1995,
  author  = {Hugo Beir{\~a}o da Veiga},
  title   = {A new regularity class for the {Navier--Stokes} equations in
             {$\mathbb{R}^n$}},
  journal = {Chinese Annals of Mathematics, Series B},
  volume  = {16},
  number  = {4},
  year    = {1995},
  pages   = {407--412}
}

@article{BerselliGaldi2002,
  author  = {Luigi C. Berselli and Giovanni P. Galdi},
  title   = {Regularity criteria involving the pressure for the weak solutions
             to the {Navier--Stokes} equations},
  journal = {Proceedings of the American Mathematical Society},
  volume  = {130},
  number  = {12},
  year    = {2002},
  pages   = {3585--3595},
  doi     = {10.1090/S0002-9939-02-06697-2}
}

@article{ChaeLee2001,
  author  = {Dongho Chae and Jihoon Lee},
  title   = {Regularity criterion in terms of pressure for the
             {Navier--Stokes} equations},
  journal = {Nonlinear Analysis: Theory, Methods \& Applications},
  volume  = {46},
  number  = {5},
  year    = {2001},
  pages   = {727--735},
  doi     = {10.1016/S0362-546X(00)00163-2}
}

@article{BeiraoDaVeigaYang2021,
  author  = {Hugo Beir{\~a}o da Veiga and Jiaqi Yang},
  title   = {On Mixed Pressure-Velocity Regularity Criteria to the
             {Navier--Stokes} Equations in {L}orentz Spaces},
  journal = {Chinese Annals of Mathematics, Series B},
  volume  = {42},
  number  = {1},
  year    = {2021},
  pages   = {1--16},
  doi     = {10.1007/s11401-021-0242-0}
}

@article{BeiraoDaVeigaYang2022,
  author  = {Hugo Beir{\~a}o da Veiga and Jiaqi Yang},
  title   = {On Mixed Pressure-Velocity Regularity Criteria to the
             {Navier--Stokes} Equations in {L}orentz Spaces, {P}art {II}:
             The Non-slip Boundary Value Problem},
  journal = {Chinese Annals of Mathematics, Series B},
  volume  = {43},
  number  = {1},
  year    = {2022},
  pages   = {51--58},
  doi     = {10.1007/s11401-022-0303-z}
}

@misc{Taghizadeh2026,
  author       = {Siamak Taghizadeh},
  title        = {A Local Monotonicity Reduction of the {3D}
                  {Navier--Stokes} Regularity Problem to a Single Remaining
                  Barrier},
  year         = {2026},
  howpublished = {Zenodo preprint, version 3},
  doi          = {10.5281/zenodo.18468477},
  note         = {Self-published preprint, 3 February 2026; not peer reviewed}
}
```

Already in `references.bib`, re-verified in this lane, no change required:

```bibtex
@incollection{Kato1990, ... }   % Springer LNM 1450, 53--63, DOI 10.1007/BFb0084898 -- verified
@article{MannaSritharan2007, ...}% Differential Integral Equations 20 (2007), no. 5 -- verified;
                                 % optional addition: doi = {10.57262/die/1356039440}
@article{SibnerSibner1970, ... } % Acta Math. 125 (1970), 57--73, DOI 10.1007/BF02392330 -- verified
@article{Scott1995, ... }        % Trans. AMS 347 (1995), no. 6, 2075--2096 -- verified
@article{IwaniecScottStroffolini1999, ...} % Ann. Mat. Pura Appl. 177 (1999), 37--115 -- verified
```

Verification provenance for the new entries.

| Key | Fields verified from | Tag |
|---|---|---|
| `Yu2026a`, `Yu2026b`, `Yu2026c` | arXiv abstract pages (title, single author, dates, primary class); `Yu2026a` body also read as arXiv HTML | [DI] |
| `TranYuDritschel2021` | Crossref record (authors with given names, volume 911, article number A18, DOI); full text read from the St Andrews open-access copy | [DI] |
| `BradshawGrujic2017` | Crossref record (volume 224, no. 1, pp. 125--133, DOI, online date); arXiv:1501.01043 for versions and abstract | [DI] metadata |
| `Zhou2004` | Crossref record only; body not read (§1.6) | [MO] |
| `BeiraoDaVeiga1995` | two independently inspected citing reference lists; no DOI exists in Crossref | [MO] identity |
| `BerselliGaldi2002` | Crossref record | [MO] identity, [DI] content via Pineau--Yu Thm 1 |
| `ChaeLee2001` | Crossref record | [MO] identity, [DI] content via TYD (1.6) |
| `BeiraoDaVeigaYang2021/2022` | Crossref records | [MO] |
| `Taghizadeh2026` | Zenodo record page | [DI] |
| `Cox2025` | **unverifiable in this lane (HTTP 403)** — omitted | — |

---

## 5. Addition for `literature/current-status.md`

Append as a new section, in the dossier's voice.

```markdown
## Prior-art comparison, 2026-09-05

This section records what a bounded prior-art source check on 5 September 2026
established about the works nearest to the pressure route of this programme.
Each source below was opened at its primary text, arXiv abstract page,
publisher record, Zenodo record, or repository README; the tag [DI] means the
statement was read there, [MO] means only the bibliographic identity was
verified. Failure to find a match is not evidence of priority, and no priority
is claimed.

The cubic balance itself is published. Tran, Yu, and Dritschel,
"Velocity–pressure correlation in Navier–Stokes flows and the problem of
global regularity," *Journal of Fluid Mechanics* 911 (2021), A18,
[DOI](https://doi.org/10.1017/jfm.2020.1033), record in their equation (2.2)
the evolution of the $L^q$ norm for $q\ge3$ with driving term
$(q-2)\int p|u|^{q-3}u\cdot\nabla|u|$ and two weighted dissipation terms; at
$q=3$ and unit viscosity this is the identity $\frac13X'+\nu D_3=P_3$ used
here [DI, full text read]. They also split the space into high- and
low-velocity regions, absorb the low-velocity part of the driving term into
the dissipation with constant $\frac12$, and prove conditional criteria
(Theorem 3.1) involving a velocity–pressure correlation coefficient
$\Gamma_q$. Their threshold is defined implicitly through the solution's own
norms at each time; ours is a frequency cutoff chosen from the data, and the
low part is removed by an energy-only bound rather than absorbed. The "Yu" in
this paper is Xinwei Yu (Alberta), not the Runlong Yu of the 2026 preprints
below.

Signed pressure–flux work with a scale chain and telescoping is public prior
art at the level of mechanism. Runlong Yu,
[arXiv:2606.25322](https://arxiv.org/abs/2606.25322) (24 June 2026), proves for
suitable weak solutions on parabolic cylinders a coarse-grained resolution
lemma and an exact fixed-chain depletion theorem for
$G^\ell=\Pi^\ell+\operatorname{div}(P^\ell U^\ell)$, with a weighted
telescoping inequality over a finite chain of scales; its Remark 4.2 states
that the theorem is unconditional only at fixed chain length and fixed filter
length and does not assert summability as the chain grows [DI, abstract and
HTML body]. The companion audit
[arXiv:2606.25341](https://arxiv.org/abs/2606.25341) states that the framework
"do[es] not by themselves provide a coercive estimate excluding a surviving
obstruction" and that "no unconditional single-scale domination by a signed
combined-work detector is available" [DI, abstract], and
[arXiv:2606.12756](https://arxiv.org/abs/2606.12756) gives a conditional local
defect-cascade reduction [DI, abstract]. All three are local CKN statements;
none makes an assertion about $L^\infty_tL^3_x$ on $\mathbb R^3$.

Frequency-localised criteria are older. Bradshaw and Grujić, "Frequency
Localized Regularity Criteria for the 3D Navier–Stokes Equations," *Archive
for Rational Mechanics and Analysis* 224 (2017), no. 1, 125–133,
[DOI](https://doi.org/10.1007/s00205-016-1069-9),
[arXiv:1501.01043](https://arxiv.org/abs/1501.01043), prove two
Littlewood–Paley localised criteria for Leray–Hopf weak solutions, one of them
restricted to a finite frequency window whose lower bound diverges as $t$
approaches an initial singular time [DI abstract; article body not reachable,
Springer returns an authentication redirect]. Their localised object is the
velocity and their window moves in time.

Pressure criteria are older still and are all conditional on an absolute norm.
Chae and Lee, *Nonlinear Analysis* 46 (2001), 727–735,
[DOI](https://doi.org/10.1016/S0362-546X(00)00163-2), and Berselli and Galdi,
*Proceedings of the AMS* 130 (2002), 3585–3595,
[DOI](https://doi.org/10.1090/S0002-9939-02-06697-2), give the criterion
$\int_0^T\|p\|_{L^s}^{2s/(2s-3)}dt<\infty$, $s>3/2$ [identities from Crossref;
content read in citing primary sources]. Zhou, *Mathematische Annalen* 328
(2004), 173–192, [DOI](https://doi.org/10.1007/s00208-003-0478-x), gives
criteria in terms of the pressure in a generic domain; its body was not
reachable in this search, and the pressure-gradient condition often quoted
under the year 2004 is stated in citing sources for a different Zhou paper,
*Proceedings of the AMS* 134 (2006), 149–156,
[DOI](https://doi.org/10.1090/S0002-9939-05-08312-7). Beirão da Veiga,
*Chinese Annals of Mathematics, Series B* 16 (1995), 407–412, is a
velocity-gradient class, $\nabla u\in L^q_tL^p_x$ with $2/q+3/p\le2$ and
$p\in(3/2,\infty)$, not a pressure criterion. Mixed pressure–velocity criteria
in Lorentz spaces are Beirão da Veiga and Yang, *Chinese Annals of
Mathematics, Series B* 42 (2021), 1–16, for the whole space and torus, and 43
(2022), 51–58, for the non-slip boundary value problem on a bounded domain;
only the 2021 paper matches the domain used here.

Self-published claims and public repositories were checked for identity and
scope only. Taghizadeh, "A Local Monotonicity Reduction of the 3D
Navier–Stokes Regularity Problem to a Single Remaining Barrier," Zenodo
preprint v3, 3 February 2026,
[DOI](https://doi.org/10.5281/zenodo.18468477), reduces global regularity to
the behaviour of a local monotonicity functional as the scale vanishes; it is
a self-published preprint, stated as submitted to a journal, and is not used
here [DI, record page]. A ResearchGate manuscript by Cox announcing global
regularity at the critical endpoint could not be opened (HTTP 403) and is
therefore recorded as unverified, with no statement about its content. Public
repositories were read at their READMEs only, never as mathematical sources:
`johnrobertlawson/brc-navier-stokes` states that the problem is unsolved and
that passing checks do not certify a theorem; `davidkny22/navier-stokes-conditional`
(David Kogan) states a conditional criterion in an enstrophy-weighted
directional Fisher information and notes that expert review would be needed;
the `navier_stokes_millennium` subproject of `lizizatt/scratch` states that it
does not claim a solution and that its validator checks structure, not
mathematical truth; `vporton/navier-stokes` claims a solution obtained with an
LLM from the author's own extension theorem. Clay still lists the problem as
unsolved, so no such claim is treated as accepted. The DeepMind and
Gómez-Serrano programme on unstable singularities
([arXiv:2509.14185](https://arxiv.org/abs/2509.14185), 17 September 2025)
concerns self-similar singularity profiles for Euler-type and model equations,
not a Navier–Stokes regularity theorem, and is recorded as context.

Verification gaps in this comparison: the Bradshaw–Grujić article body, the
Zhou 2004 article body, the Beirão da Veiga 1995 article, and the Cox
manuscript were not reachable; MathSciNet and zbMATH full records require
authentication and were not used. The comparison is therefore a bounded
search, and its negative findings support no priority claim.
```

---

## 6. Five-line note for `PLAN.md`

Insert under "External opinions and prior-art audit".

```markdown
The 2026-09-05 audit's research priorities are now sorted by
`cp02-prior-art-related-work.md`. Done: the explicit divergence-free profile
with nonzero pressure work (HF02, `hf02-r3-profile.md`). Folded into Track B:
a partial HF theorem under a natural Type-I or critical-concentration class; a
telescoping law for the L3 pressure flux, to be built and stated as distinct
from Yu's local coarse-grained G^ell; and a constructive J_0 / A in named
initial-data norms. Out of scope: publication-strategy forecasts, workflow
comparisons with public AI proof labs, and any priority or "first" claim; the
manuscript's related-work subsection states distinctions by objects and
quantifiers only, and the audit's Zhou-2004 and Beirao-da-Veiga-1995
attributions are corrected there.
```

---

## 7. Frontier record

CLAIM AND SCOPE: bibliographic only.  Every external work named in the
user-supplied audit was checked against a primary text or an official record,
and the manuscript's objects (T),(B),(P),(S),(L),(H),(E),(C) were compared
with them at the level of objects and quantifiers.  No mathematical statement
of the programme is added, removed, strengthened or weakened.

EVIDENCE: Tran--Yu--Dritschel, JFM 911 (2021) A18, full text §§1--3 including
eq. (2.2), the split (3.1)--(3.11) and Theorem 3.1 [DI]; Yu arXiv:2606.25322
abstract and HTML body including Theorem 4.1 and Remark 4.2 [DI]; Yu
arXiv:2606.25341 and arXiv:2606.12756 abstract pages [DI]; Bradshaw--Grujić
arXiv:1501.01043 abstract and Crossref record [DI/MO]; Pineau--Yu
arXiv:1910.08911v1 Theorems 1--2 and reference list [DI]; Cai--Zhai
arXiv:math/0611843v1 §1 and reference list [DI]; arXiv:2102.06152 HTML for the
Beirão da Veiga 1995 statement [DI]; Crossref records for Zhou 2004, Zhou
PAMS 2006, Berselli--Galdi, Chae--Lee, Beirão da Veiga--Yang I and II,
Sibner--Sibner, Scott, Iwaniec--Scott--Stroffolini, Kato 1990,
Manna--Sritharan [MO]; Zenodo record 10.5281/zenodo.18468477 [DI]; Clay
Navier--Stokes page [DI]; GitHub API and README text for
`johnrobertlawson/brc-navier-stokes`, `davidkny22/navier-stokes-conditional`,
`lizizatt/scratch`, `vporton/navier-stokes` [DI] and
`ricalanis/navier-stokes-playresearch` [MO].

FIRST GAP (for this lane): four bodies were not reachable — Bradshaw--Grujić
ARMA 224 (Springer HTTP 303 to an identity provider), Zhou, Math. Ann. 328
(same, abstract elided at Semantic Scholar), Beirão da Veiga, Chinese Ann.
Math. Ser. B 16 (no electronic record located), and the Cox ResearchGate
manuscript (HTTP 403).  Only the last of these blocks a decision: without it,
no statement about that manuscript's content, and hence no comparison with
it, is possible.  MathSciNet and zbMATH full records need authentication and
were not used, so this remains a bounded search.

NON-CLAIMS: no novelty, no priority, no "first" claim; no assertion that any
unlocated item is new; no HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION or
NS-R3 result; no mathematical consequence of any cited theorem is imported
into the programme by this note; repository READMEs are recorded as repository
facts and are never mathematical sources.

NEXT DISTINCT ACTION: obtain the Bradshaw--Grujić and Zhou 2004 article bodies
through institutional access and record their exact hypotheses; if Zhou 2004
does state a $\nabla p$ criterion, correct §1.6 and the LaTeX block
accordingly.  Independently, read Yu arXiv:2606.25322 §4 in full and record
whether any part of its weighted telescoping construction transfers to
$\int\Delta_j(|u|u)\cdot(I-\mathbb P)(u\cdot\nabla u)$, which is the Track B
$B_j$ question.
