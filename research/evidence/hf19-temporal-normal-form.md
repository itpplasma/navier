# HF19-A: temporal normal forms for the transport term on the quotient route

**STATUS (2026-09-06).**  Independently audited by
`research/evidence/hf19-review-temporal-normal-form.md`, verdict **REPAIR**
(no invalid mathematics in the surviving core; two bad bridges, an
input-constant slip in Lemma 0.1(a) and a false boundary-term estimate in
Corollary 1.1(a)).  This is the repaired version: the controller applied the
audit's replacement arguments R1 and R2, its scope tightening R3 (the
quantifier on (C)), its missing-hypothesis correction R4, and every editorial
and dependency item of its EVIDENCE and UNNECESSARY DEPENDENCIES lists.
Proposition 0.2 is demoted to a change-of-variables Remark with its
absolute-continuity hypothesis restored; (NF) is defined in integrated form;
the route-level "temporal normal forms are exhausted" conclusion is replaced
by the summary of the three computed classes that the audit certifies.  The
first gap is unchanged and NS-R3 remains OPEN.

Lane HF19-A, MODE: DISCOVER (with an obstruction proved for each of the three
classes computed), 2026-09-05, repaired 2026-09-06.  Base commit `5aefa82`
(navier), manuscript `navier-paper` at `39ccb66`, section `sec:quotient`.
Audited inputs used without re-proof: `hf17-quotient-functional.md`,
`hf17-quotient-evolution.md` (both PASS), `hf18-hodge-regularity.md` (SHA-256
`e5fdbc39…2db61`, PASS with S1–S3 applied), `hf18-divergence-speed-link.md`
(SHA-256 `409421f2…62a66`, PASS r2 with S1–S4 applied).  Source tags: [DI]
directly inspected in this programme, [MO] metadata only, never load-bearing.
No primary web source was needed: every imported statement is a manuscript
lemma or an audited note.

**MODE / RESULT: DISCOVER, negative in the three classes computed, with two
exact by-products.**  For every functional \(B\) whose composition
\(B\circ u\) is absolutely continuous on compact classical intervals, a
temporal normal form \(K=\tfrac d{dt}B(u)+R\) with the boundary condition (C)
is *the same statement* as the existence of a coercive critical
Lyapunov-type functional \(\Phi=\mathcal Q-B\) — a change of variables, not a
theorem (Remark 0.2); so the only content of any normal form lies in the
explicit \(B\) for which \(\Phi'\) can be computed.  Three explicit classes
are computed in full.  (i) \(B=\mathcal Q-X/3\) (the distance to the plain
cubic norm) gives the exact identity
\(K-P_3=\tfrac d{dt}(\mathcal Q-X/3)+\nu\,(D_3(w)-D_3(u))\) (Theorem 1).  It
yields an **unconditional instantaneous** transfer in one direction only,
pressure \(\Rightarrow\) strain (Corollary 1.1(b), exact constant
\(X(0)/3\)); the reverse direction holds only *after* a Gronwall closure and
with a degraded constant, and does not deliver `hyp:absorption` as the
manuscript states it (Corollary 1.1(a)', Remark 1.1.1).  (ii) The heat
inverse \(B_h(u)=-\int_0^\infty K(G_su)\,ds\) is rigorously defined with the
exact bound \(|B_h|\le\tfrac{3C_*}{4\nu}\mathcal Q^{4/3}\) and the rigorous
heat-direction identity \(\tfrac d{dt}B_h(G_tu)=K(G_tu)\); every \(C^1\)
scalar \(F(\mathcal Q,B_h)\) with coefficientwise cancellation of \(K\) is
\(f(\mathcal Q-B_h)\), and \(\mathcal Q-B_h\) is not coercive on fixed energy
shells unless \(K\equiv0\) on solenoidal Schwartz fields (Theorem 2); the
saturation and truncation repairs fail exactly as in HF01/HF04, and the
transport-direction chain rule for \(B_h\) is in any case unjustified because
it differentiates the \(L^3\) minimizer.  (iii) Every heat-smoothed modified
energy \(\Phi_m=\int_{(0,\infty)}\mathcal Q(G_su)\,m(ds)\) with \(m\)
**atomless at \(0\)** is non-coercive relative to any locally bounded
function of the energy (Theorem 3); the hypothesis is necessary, and the
atom-carrying mixtures fail instead for the Corollary 2.4(a) reason
(Remark 3.2).  The coercivity failures of Theorems 2(ii) and 3 are failures
of (C) **for the universal reading of (C)** (Section 0.3); they exclude
nothing about a corrector satisfying (C) only along the trajectories of a
given datum.  No functional built from \(q,A,V,\Pi_{u,A},\sigma\) that is not
a value function of the coset is known to admit a justified time derivative
(Section 4, a classification of the mechanisms available, not a theorem about
all functionals), and value functions fall under Remark 0.2.  The first gap
is unchanged; its exact position in each candidate is displayed with scaling.

## 0. Setting, and what a normal form must accomplish

Throughout, \((u,p)\) is the classical branch of `prop:localtheory` on a
compact interval \([0,T]\subset[0,T_*)\), package (R) of `sec:quotient`;
\(q=q(u)\in\mathcal G_3\), \(w=u+q\), \(A=|w|w\), \(V=|w|^{1/2}w\);
\(\mathcal Q(u)=\tfrac13\|w\|_3^3\), \(X=\|u\|_3^3\) (`def:D3P3`, so the plain
cubic functional is \(X/3\)), \(G_s=e^{s\nu\Delta}\) (note: the manuscript's
\(G_s\) has \(\nu=1\); here \(G_s=k_{\nu s}*\), which changes nothing in the
cited lemmas).  Audited facts used:

- (Q1) `prop:quotient-evolution` + HF18-A Thm 2: \(\mathcal Q\circ u\in C^1([0,T])\),
  \(\mathcal Q'+\nu D_3(w)=K\), \(D_{\mathcal Q}(u)=D_3(w)=\int(|\nabla V|^2-\tfrac19|\nabla|V||^2)\ge0\).
- (Q2) `lem:quotient-transport`, HF18-A Prop. 3: \(K=-\int q\cdot((A\cdot\nabla)u)=-\langle A,(u\cdot\nabla)u\rangle=\int A\cdot(u\times\omega)=-\int q\cdot((u\cdot\nabla)A)\);
  in particular \(K=-D\mathcal Q(u)[(u\cdot\nabla)u]\).
- (Q3) HF18-A (4.2): \(|K|\le C_*\mathcal Q^{1/3}D_3(w)\), \(C_*=\tfrac32 3^{1/3}(1+C_3)C_9S\).
- (Q4) `lem:quotient-coercive`: \(\tfrac{X}{3C_{\mathbb P}^3}\le\mathcal Q\le\tfrac X3\) on solenoidal fields.
- (Q5) `lem:quotient-heat` (with \(\nu\)): \(\mathcal Q(G_su)\le F(G_sw)\le\mathcal Q(u)\), \(G_s\mathcal G_3\subset\mathcal G_3\).
- (P1) `prop:pressure`(ii): \(\tfrac13X(t)-\tfrac13X(s)+\nu\int_s^tD_3(u)\,d\tau=\int_s^tP_3\,d\tau\),
  with \(D_3(u)=\int(|u||\nabla u|^2+|u||\nabla|u||^2)\) (`eq:D3-def`, since
  \(|(\nabla u)^{\mathsf T}u|^2/|u|=|u||\nabla|u||^2\)), \(P_3=\int p\,u\cdot\nabla|u|\)
  (`eq:P3-def`), both bounded measurable on \([0,T]\), \(X\in C([0,T_*))\).
  The paper's \(D_3(u)\) equals HF18-A's \(D_3\) evaluated at \(v=u\): for smooth
  \(u\), \(V_u=|u|^{1/2}u\in H^1\) and HF18-A (1.12) holds on \(\{u\ne0\}\), while
  \(\nabla V_u=0\) a.e. on \(\{u=0\}\).
- (P2) `prop:lowpressure`, HF14–HF15: the low-output part of \(P_3\) is bounded by
  energy; the high-output part is the HIGH-PRESSURE gap `hyp:highpressure`.

Not used anywhere below: HF18-A (F3)–(F4), which HF18-A §3.2 quarantines
behind the hypothesis \(w\in W^{1,1}_{\rm loc}\).

**Scaling bookkeeping** (HF18-B §0): amplitude \(a\), dilation \(\lambda\), \(\nu\)
fixed unless stated: \(\mathcal Q,X\sim(a^3,\lambda^0)\), \(D_3\sim(a^3,\lambda^2)\),
\(K,P_3\sim(a^4,\lambda^2)\), \(E=\|u\|_2^2\sim(a^2,\lambda^{-1})\).  The
amplitude map is a Navier–Stokes symmetry only together with \(\nu\mapsto a\nu\).

**The target, stated precisely.**  The frozen gap is
\[
 \int_0^\tau K\,dt\le\theta\nu\int_0^\tau D_3(w)\,dt+M\int_0^\tau\mathcal Q\,dt+A_{\rm input},
 \qquad 0<\tau<\min(H,T_*),\ \theta\le1,                              \tag{G}
\]
with \(M,A_{\rm input}\) depending only on \((\nu,u_0,H)\).  A *temporal
normal form* is a functional \(B\) with \(t\mapsto B(u(t))\) absolutely
continuous on compact classical intervals such that, **in the integrated
sense**, for all \(0\le s\le t\le T\),
\[
 \int_s^tK\,d\tau\le B(u(t))-B(u(s))+\theta\nu\int_s^tD_3(w)\,d\tau
 +M\int_s^t\mathcal Q\,d\tau+\int_s^tr\,d\tau,
 \quad r\ge0\ \text{input-integrable},                                \tag{NF}
\]
together with a boundary condition on \(B\).  (Writing \(K=\tfrac
d{dt}B(u)+R\) with \(R\le\theta\nu D_3(w)+M\mathcal Q+r\) a.e. gives (NF) by
absolute continuity; only the integrated form (NF) is used below, and it is
the only form Theorem 1 supplies.)

**Lemma 0.1 (what the boundary condition must be).**  (a) Let (NF) hold in
integrated form on \([0,\tau]\) for every \(0<\tau<\min(H,T_*)\), with
\(\theta\le1\), \(M\ge0\), \(r\ge0\) input-integrable, and let
\[
 B(u(\tau))\le(1-c)\,\mathcal Q(u(\tau))+a_{\rm input}\qquad\text{for some }c\in(0,1],\ a_{\rm input}<\infty \tag{C}
\]
hold at \(u(\tau)\) for every such \(\tau\).  Put
\(A_0:=a_{\rm input}+|B(u_0)|+\int_0^Hr\).  Then
\[
 c\,\mathcal Q(\tau)+(1-\theta)\nu\int_0^\tau D_3(w)\,dt
 \le\mathcal Q(0)+A_0+M\int_0^\tau\mathcal Q\,dt,                      \tag{R1.1}
\]
hence, dropping the nonnegative dissipation term (\(\theta\le1\),
\(D_3(w)\ge0\) by `lem:quotient-heatsign`) and applying `lem:qe-gronwall` to
the continuous \(y=\mathcal Q\circ u\) on each
\([0,\tau_1]\subset[0,\min(H,T_*))\),
\[
 \mathcal Q(\tau)\le\mathcal Q_{\max}:=c^{-1}\bigl(\mathcal Q(0)+A_0\bigr)e^{(M/c)H}
 \qquad\text{for all }0\le\tau<\min(H,T_*),                            \tag{R1.2}
\]
and (G) holds with the same \(\theta\), the same \(M\), and
\[
 A_{\rm input}:=A_0+(1-c)\,\mathcal Q_{\max}.                          \tag{R1.3}
\]
(b) The condition \(|B|\le C\mathcal Q\) with \(C\ge1\) is not sufficient:
\(B=\mathcal Q\), \(R=\nu D_3(w)\), \(\theta=1\) satisfies (NF) and
\(|B|\le\mathcal Q\) and yields nothing.

*Proof.* (a) Integrating (Q1),
\(\mathcal Q(\tau)+\nu\int_0^\tau D_3(w)=\mathcal Q(0)+\int_0^\tau K\);
integrating (NF) and inserting (C) at \(u(\tau)\) gives
\[
 \int_0^\tau K\le(1-c)\mathcal Q(\tau)+A_0+\theta\nu\int_0^\tau D_3(w)+M\int_0^\tau\mathcal Q .
\]
Subtracting yields (R1.1); Gronwall gives (R1.2); feeding (R1.2) back into the
same bound on \(\int_0^\tau K\) gives (G) with (R1.3).  For \(c=1\) the term
\((1-c)\mathcal Q_{\max}\) is absent and
\(A_{\rm input}=a_{\rm input}+|B(u_0)|+\int_0^Hr\).  (b) is (Q1). \(\square\)

The displayed constant \(A_{\rm input}=A_0\) alone is available only at
\(c=1\): for \(c<1\) the term \((1-c)\mathcal Q(\tau)\) must first be removed,
and writing \(\mathcal Q(\tau)\) into \(A_{\rm input}\) without the Gronwall
step (R1.2) would be circular, since \(\mathcal Q(\tau)\) is exactly what the
lemma bounds.  The only instantiation of Lemma 0.1(a) below is Theorem 1,
where \(c=1\).

So the lane's "\(|B|\le C\mathcal Q\)" must be read as (C).  The next remark
shows that (NF)+(C) is not a reformulation that could be easier than the
Lyapunov problem: it *is* the Lyapunov problem, written in other letters.

**Remark 0.2 (the change of variables \(\Phi=\mathcal Q-B\); not a theorem).**
Let \(B\) be any functional with \(B\circ u\) **absolutely continuous on
compact classical intervals** — this hypothesis is not decorative, it is what
makes \(B'\) exist and (NF) meaningful — and put \(\Phi:=\mathcal Q-B\).
Since \(R\) is *defined* as \(K-B'\) and \(\mathcal Q'=K-\nu D_3(w)\) is (Q1),
\[
 R=\Phi'+\nu D_3(w)
\]
identically, so the a.e. pointwise form of (NF) with \((\theta,M,r)\) holds if
and only if
\[
 \tfrac d{dt}\Phi(u)+(1-\theta)\nu D_3(w)\le M\mathcal Q+r\quad\text{a.e. on }[0,T], \tag{L}
\]
and (C) holds if and only if \(\Phi\ge c\,\mathcal Q-a_{\rm input}\) at the
points where (C) is imposed.  Consequently a temporal normal form for \(K\)
with boundary condition (C) exists if and only if there is a functional
\(\Phi\), coercive in the sense \(\Phi\ge c\mathcal Q-a_{\rm input}\),
satisfying the Lyapunov-type inequality (L).

This is a substitution, not a result: it assumes nothing it concludes, and it
carries no mathematical content beyond notation.  It is recorded because of
what it forbids, not because of what it proves; it must not be reported as a
by-product of the same weight as Theorem 1.  Two quantifier points are part
of the statement: the absolute continuity of \(B\circ u\) is a hypothesis and
may not be dropped, and the equivalence above is at the level of a.e.
pointwise inequalities, while (G) and (NF) are time-integrated.

Two consequences frame everything below.  First, no obstruction theorem for
the *general* class of normal forms is provable without deciding the terminal
claim.  Precisely: suppose NS-R3 holds, so \(T_*=\infty\) and \(u\) is
classical on \([0,H]\); then \(K\) is continuous on \([0,H]\)
(`prop:quotient-evolution`), so \(\Phi=\mathcal Q\) itself satisfies (L)
pointwise with \(\theta=0\), \(M=0\) and \(r=K^+\in L^\infty(0,H)\), which is
input-integrable — the same device as the converse in `rem:highstrain-scope`
(\(L=0\), \(A_{\rm input}=\int_0^H|K_0|\)).  Hence "no coercive \(\Phi\)
satisfies (L)" would refute NS-R3.  Second, therefore, the only honest content
of a normal form is an *explicit* \(\Phi\) whose derivative can be computed and
whose sign problem is displaced to an explicit place.  Sections 1–4 compute
the explicit classes suggested by the lane and identify where the sign
problem lands.

### 0.3 The quantifier on (C), stated explicitly

(C) is a property of the functional \(B\); the quantifier over \(u\) has to be
fixed, and the choice matters:

- *Trajectory-local reading.*  (C) is required only at the trajectory points
  \(u(\tau)\), \(0<\tau<\min(H,T_*)\), with \(a_{\rm input}\) permitted to
  depend on \((\nu,u_0,H)\).  This is all that Lemma 0.1(a) uses, and it is
  the reading under which (C) enters (G).
- *Universal reading.*  (C) is required at all solenoidal Schwartz fields
  (equivalently, by density and continuity where applicable, at all
  solenoidal \(H^m\) fields), or at least on a fixed energy shell, with one
  pair \((c,a_{\rm input})\).

**Theorem 2(ii) and Theorem 3 below refute (C) for the universal reading
only.**  They are unproved for the trajectory-local reading, and the
fixed-energy-shell construction of Theorem 2(ii) narrows but does not close
that gap: energy is an input, but a trajectory issuing from one fixed \(u_0\)
need not visit the fields \(u_a\) constructed there.  Every statement of
Theorems 2–3 and every route-level sentence resting on them therefore carries
the phrase *for the universal reading of (C)*.  Which reading the programme
intends is not decided in this note, and deciding it changes what Sections 2
and 3 exclude; that decision is recorded as an open question in Section 6.

## 1. The distance \(\Phi=X/3\): one exact identity, one one-sided transfer

**Theorem 1 (exact identity between the strain and pressure balances).**
On every compact classical interval \([0,T]\), for \(0\le s\le t\le T\),
\[
 \boxed{\;\int_s^t\bigl(K-P_3\bigr)\,d\tau
 =\Bigl[\mathcal Q(u)-\tfrac13X\Bigr]_s^t
 +\nu\int_s^t\bigl(D_3(w)-D_3(u)\bigr)\,d\tau .\;}                     \tag{1.1}
\]
Every term is finite: \(K\), \(D_3(w)\) are continuous (Q1); \(P_3\), \(D_3(u)\)
bounded measurable and \(X\) continuous (P1); \(0\le\mathcal Q\le X/3\) (Q4).
Equivalently, in the normal-form language of Section 0 with
\(B=\mathcal Q-X/3\le0\), \(\Phi=X/3\):
\[
 K=\tfrac d{dt}B(u)+R,\qquad R=P_3+\nu\bigl(D_3(w)-D_3(u)\bigr),\qquad
 -\bigl(C_{\mathbb P}^3-1\bigr)\mathcal Q\le B\le0,                     \tag{1.2}
\]
in the integrated sense, and (C) holds with \(c=1\), \(a_{\rm input}=0\).
(\(X\) is Lipschitz on compacts by (P1) with bounded integrands, so
\(B\circ u\) is absolutely continuous as (NF) requires.)

*Proof.* Integrate (Q1) over \([s,t]\): \(\mathcal Q(t)-\mathcal Q(s)+\nu\int_s^tD_3(w)=\int_s^tK\).
Subtract (P1).  The bounds on \(B\) are (Q4). \(\square\)

Theorem 1 is a subtraction of two audited balances.  Its proof is one line and
it establishes no new estimate; its value is the exact location of the
pressure/strain difference.

**Corollary 1.1 (what transfers between the two producers).**
Fix \(\nu,u_0,H\).

(a)' Assume (G) for \(K\) with \(\theta_s\le1\), \(M\ge0\), \(A<\infty\), for
all \(0<\tau<\min(H,T_*)\).  Put
\[
 \mathcal Q_{\max}:=\bigl(\mathcal Q(0)+A\bigr)e^{MH},\qquad
 A':=A+C_{\mathbb P}^3\,\mathcal Q_{\max}.
\]
Then for every \(0<\tau<\min(H,T_*)\)
\[
 \int_0^\tau P_3\,dt
 \le\nu\int_0^\tau D_3(u)\,dt-(1-\theta_s)\nu\int_0^\tau D_3(w)\,dt
 +M\int_0^\tau\tfrac X3\,dt+A'
 \le\nu\int_0^\tau D_3(u)\,dt+M\int_0^\tau\tfrac X3\,dt+A',
\]
and with `prop:pressure`(ii) and `lem:qe-gronwall` this gives `hyp:critical`:
\(\sup_{0\le\tau<\min(H,T_*)}\|u(\tau)\|_3^3\le(\|u_0\|_3^3+3A')e^{MH}\).

(b) Conversely, if `hyp:absorption` holds with \((\theta_p\le1,A)\), then
\[
 \int_0^\tau K\le\nu\int_0^\tau D_3(w)-(1-\theta_p)\nu\int_0^\tau D_3(u)+A+\tfrac13X(0),
\]
i.e. (G) with \(\theta_s=1\), \(M=0\), \(A_{\rm input}=A+X(0)/3\).  This
direction is unconditional and instantaneous: one line from (1.1), with the
exact constant \(X(0)/3\).

(c) A strict transfer \(\theta<1\) in either direction requires a comparison
\(D_3(w)\ge cD_3(u)\) (for (a)') or \(D_3(u)\ge cD_3(w)\) (for (b)); neither is
proved, see Remark 1.3.

*Proof.* (a)' Integrate (Q1) on \([0,\tau]\), insert (G), and drop
\((1-\theta_s)\nu\int_0^\tau D_3(w)\ge0\) (\(\theta_s\le1\), \(D_3(w)\ge0\)):
\(\mathcal Q(\tau)\le\mathcal Q(0)+A+M\int_0^\tau\mathcal Q\), so
\(\mathcal Q(\tau)\le\mathcal Q_{\max}\) by `lem:qe-gronwall`; by (Q4),
\(Y(\tau):=X(\tau)/3-\mathcal Q(\tau)\le X(\tau)/3\le C_{\mathbb P}^3\mathcal Q_{\max}\).
Now (1.1) at \(s=0\) reads
\(\int_0^\tau P_3=\int_0^\tau K+\bigl(Y(\tau)-Y(0)\bigr)+\nu\int_0^\tau\bigl(D_3(u)-D_3(w)\bigr)\);
bound \(\int_0^\tau K\) by (G), drop \(-Y(0)\le0\), bound \(Y(\tau)\) as above,
and use \(\mathcal Q\le X/3\) in the Gronwall term.  The last sentence is
`prop:pressure`(ii) plus `lem:qe-gronwall` on \(X/3\).
(b) Here the boundary term is
\(-[X/3-\mathcal Q]_0^\tau=Y(0)-Y(\tau)\le Y(0)\le X(0)/3\), because
\(Y(\tau)\ge0\) by (Q4).
(c) is read off the displayed middle terms. \(\square\)

**Remark 1.1.1 (what the repair costs, and a terminology correction).**  The
two directions are **not** symmetric, and the asymmetry is exactly at the
boundary term \(Y=X/3-\mathcal Q\ge0\) of (Q4).  In direction (b) one needs an
upper bound for \(Y(0)-Y(\tau)\), which \(Y\ge0\) supplies with the exact
constant \(X(0)/3\).  In direction (a) one needs an upper bound for
\(Y(\tau)-Y(0)\); the facts \(\mathcal Q(\tau)\le X(\tau)/3\) and
\(\mathcal Q(0)\ge0\) give only the **lower** bound \(Y(\tau)-Y(0)\ge-X(0)/3\)
and cannot be used the other way.  (Values admissible under (Q4) with
\(C_{\mathbb P}^3\ge3\), e.g. \(X(\tau)=90,\ \mathcal Q(\tau)=10,\ X(0)=3,\
\mathcal Q(0)=1\), give \(Y(\tau)-Y(0)=20\) against \(X(0)/3=1\).)  The
genuinely unbounded object is \(Y(\tau)\le X(\tau)/3\), of the same
criticality \((a^3,\lambda^0)\) as the conclusion, so (Q4) alone cannot bound
it; the only route is the Gronwall closure used in (a)'.

Two consequences, both of which restrict what may be claimed:

- In (a)' the constant \(A'\) is produced only *after* the Gronwall closure of
  (G).  That closure is already `prop:quotient-conditional`, i.e. already
  `hyp:critical`.  So direction (a) is a corollary of the conclusion, not an
  independent instantaneous transfer.  Only direction (b) is an unconditional
  instantaneous transfer through the identity (1.1).
- What (a)' delivers is **not** `hyp:absorption` as the manuscript states it:
  `hyp:absorption` requires a *fixed* \(\theta\in[0,1)\) and carries **no**
  Gronwall term, whereas (a)' has \(\theta_p=1\) together with
  \(M\int_0^\tau X/3\).  That is a strictly different, weaker statement and
  must not be read as instantiating the manuscript hypothesis.  Direction (b)
  is unaffected: it *assumes* `hyp:absorption` with \(\theta_p\le1\), which is
  implied by the manuscript's \(\theta_p<1\).

Accordingly the summary "the HIGH-STRAIN and HIGH-PRESSURE gaps are
equivalent at \(\theta\le1\)" is withdrawn and replaced by the two items
displayed above.

**Remark 1.2 (where the first gap sits in this normal form).**  In (1.2) the
remainder is \(R=P_3+\nu(D_3(w)-D_3(u))\).  Its low-output pressure part is
energy-controlled (P2).  The first term not controlled by \((D_3(w),\mathcal Q,\text{input})\)
is the high-output pressure work \(\int_0^\tau(P_3)_{>J}\,dt\), scaling
\((a^4,\lambda^2)\): exactly `hyp:highpressure`.  Thus the distance functional
does not move the gap.  What it does establish is the *exact* relation (1.1)
between the two balances, together with the one-sided transfer of
Corollary 1.1(b); the reverse transfer is post-Gronwall and hence has no
independent force (Remark 1.1.1).  The packet's statement that both producers
are "equivalent to continuation" is not strengthened to an instantaneous
two-way equivalence here.

**Remark 1.3 (the dissipation difference).**  \(D_3(u)-D_3(w)\) has no proved
sign.  What is known: both vanish together at \(u=0\); on
\(\mathcal M=\{\operatorname{div}(|u|u)=0\}\) one has \(q=0\) and the difference
is \(0\); heat monotonicity gives no comparison, because differentiating
\(\mathcal Q(G_su)\le F(G_sw)\) at \(s=0\) reproduces \(D_{\mathcal Q}=D_3(w)\)
(HF18-A) and never involves \(D_3(u)\); and the variational characterisation
of \(w\) is in the \(L^3\) norm, not in the dissipation.  Bounded evidence
(Section 5): \(D_3(u)-D_3(w)>0\), about \(2\%\) of \(D_3\), on all four
sampled fields — finite-resolution evidence, not proof.  If \(D_3(w)\le D_3(u)\)
held in general, the strain route would be the *sharper* of the two: (1.1)
would read \(\int K\le\int P_3+X(0)/3\) with no dissipation loss.  A proof or a
counterexample is a distinct, well-posed static question on \(\mathcal M\)
(Prop. 1.4 of HF18-B supplies the test class \(w=|A|^{-1/2}A\), \(u=\mathbb Pw\);
that citation is a source of test fields only and is load-bearing for no claim
in this note).

## 2. The heat inverse \(B_h\): rigorous parts, and the transferred HF04 obstruction

Define, for solenoidal \(u\in H^m(\mathbb R^3)\), \(m\ge4\), and \(\nu>0\),
\[
 B_h(u):=-\int_0^\infty K(G_su)\,ds,\qquad
 K(v):=\int A(v)\cdot\bigl(v\times\operatorname{curl}v\bigr)\,dx=-\int q(v)\cdot((A(v)\cdot\nabla)v)\,dx, \tag{2.1}
\]
where \(K(v)\) is the static functional of (Q2) (both forms agree for every
solenoidal \(v\in H^m\) by HF18-A Prop. 3, which uses only (0.1) there).

**Lemma 2.1 (the heat orbit).**  Let \(u\in H^m\), \(m\ge4\), solenoidal.
(a) \(s\mapsto G_su\) is in \(C([0,\infty);H^m)\cap C^1((0,\infty);H^m)\) with
\(\partial_sG_su=\nu\Delta G_su\), and \(G_su\) is solenoidal.
(b) \(s\mapsto\mathcal Q(G_su)\) is continuous on \([0,\infty)\), \(C^1\) on
\((0,\infty)\), nonincreasing, with
\(\tfrac{d}{ds}\mathcal Q(G_su)=-\nu D_3(w(G_su))\) and \(\mathcal Q(G_su)\to0\) as \(s\to\infty\).
(The restriction of \(C^1\) to \((0,\infty)\) is conservative: for \(m\ge4\)
the curve is \(C^1\) into \(H^{m-2}\subset L^3\) on all of \([0,\infty)\).
Nothing below depends on the sharper statement.)
(c) \(s\mapsto K(G_su)\) is continuous on \([0,\infty)\) and
\(|K(G_su)|\le C_*\,\mathcal Q(G_su)^{1/3}D_3(w(G_su))\).
(d) \(K\) is odd and of degree four: \(K(av)=a^3|a|\,K(v)\); and dilation-covariant:
\(K(\lambda v(\lambda\cdot))=\lambda^2K(v)\).

*Proof.* (a) Standard for the heat semigroup on \(H^m\); solenoidality is preserved
since \(G_s\) is a Fourier multiplier.  (b) Continuity: \(G_su\to u\) in \(L^3\)
as \(s\downarrow0\) (`lem:qe-heat-continuity`) and \(\mathcal Q\) is continuous on \(L^3\)
(`lem:quotient-stability`).  Differentiability: the curve is
\(C^1\) into \(H^{m-2}\subset L^3\), so Step 2 of `lem:quotient-chainrule` applies verbatim
and gives \(\tfrac d{ds}\mathcal Q(G_su)=\langle A(G_su),\nu\Delta G_su\rangle
=-\nu D_{\mathcal Q}(G_su)=-\nu D_3(w(G_su))\) by HF18-A Thm 2 applied at the
solenoidal \(H^m\) field \(G_su\).  Monotonicity is (Q5) iterated.  The limit:
\(\mathcal Q(G_su)\le\tfrac13\|G_su\|_3^3\le C(\nu s)^{-3/4}\|u\|_2^3\to0\)
(heat kernel \(L^2\to L^3\) bound \(\|k_{\nu s}\|_{6/5}\) by Young).
(c) Continuity: \(v\mapsto A(v)\) is continuous \(L^3\to L^{3/2}\)
(`lem:quotient-stability`) and \(v\mapsto v\times\operatorname{curl}v\) is continuous
\(H^m\to L^3\) (\(\|v\times\operatorname{curl}v-v'\times\operatorname{curl}v'\|_3
\le\|v-v'\|_3\|\operatorname{curl}v\|_\infty+\|v'\|_3\|\operatorname{curl}(v-v')\|_\infty\)),
and \(s\mapsto G_su\) is continuous into \(H^m\).  The bound is (Q3) at \(G_su\).
(d) \(A(av)=a|a|A(v)\), \(av\times\operatorname{curl}(av)=a^2\,v\times\operatorname{curl}v\);
under dilation \(A\mapsto\lambda^2A(\lambda\cdot)\), \(v\times\operatorname{curl}v\mapsto\lambda^3(\cdot)(\lambda\cdot)\),
and \(dx\mapsto\lambda^{-3}dx\). \(\square\)

**Proposition 2.2 (exact size of the heat inverse).**  For solenoidal
\(u\in H^m\), \(m\ge4\), the integral (2.1) converges absolutely and
\[
 \boxed{\;|B_h(u)|\le\int_0^\infty|K(G_su)|\,ds\le\frac{3C_*}{4\nu}\,\mathcal Q(u)^{4/3}.\;}  \tag{2.2}
\]
\(B_h\) is odd, \(B_h(au)=a^3|a|B_h(u)\), and dilation invariant,
\(B_h(\lambda u(\lambda\cdot))=B_h(u)\).

*Proof.* Put \(\mathcal Q_s=\mathcal Q(G_su)\).  By Lemma 2.1(b),(c),
\(|K(G_su)|\le C_*\mathcal Q_s^{1/3}D_3(w(G_su))=-\tfrac{C_*}{\nu}\mathcal Q_s^{1/3}\tfrac{d\mathcal Q_s}{ds}\)
for \(s>0\), so
\(\int_0^\infty|K(G_su)|ds\le\tfrac{C_*}\nu\bigl[-\tfrac34\mathcal Q_s^{4/3}\bigr]_0^\infty=\tfrac{3C_*}{4\nu}\mathcal Q(u)^{4/3}\),
the antiderivative argument needing only that \(s\mapsto\mathcal Q_s\) is \(C^1\)
on \((0,\infty)\) with \(\mathcal Q_s\to0\); monotonicity is not needed.
Oddness and homogeneity are Lemma 2.1(d); dilation invariance uses
\(G_s(\lambda u(\lambda\cdot))=\lambda(G_{\lambda^2s}u)(\lambda\cdot)\)
and the substitution \(s\mapsto\lambda^2s\). \(\square\)

Scaling of (2.2): \(B_h\sim(a^4/\nu,\lambda^0)\) versus \(\mathcal Q\sim(a^3,\lambda^0)\).
This is the same quartic-versus-cubic mismatch as HF04's \(|\mathcal B|\le C\nu^{-1}U^4\),
now with an explicit constant and an exact one-line proof through the
audited sharp bound (Q3) and the heat monotonicity of \(\mathcal Q\).  The
boundary condition (C) for \(B=B_h\) reads
\(B_h\le(1-c)\mathcal Q+a\), which (2.2) supplies only where \(\tfrac{3C_*}{4\nu}\mathcal Q^{1/3}\le1-c\),
i.e. under the critical smallness \(\|u\|_3\lesssim\nu\): the hidden-smallness
falsifier, already the obstruction of HF18-A Corollary 4.  This says what
*(2.2)* supplies, not that (C) fails; \(B_h\le0\) would give (C) with \(c=1\)
for free.  (Section 5 reports \(B_h>0\) on all four sampled fields, as bounded
evidence only.)

**Proposition 2.3 (heat direction, rigorous).**  For solenoidal \(u\in H^m\),
\(m\ge4\), and \(t\ge0\): \(B_h(G_tu)=-\int_t^\infty K(G_su)\,ds\), and
\(t\mapsto B_h(G_tu)\) is \(C^1\) on \([0,\infty)\) with
\[
 \tfrac d{dt}B_h(G_tu)=K(G_tu).                                         \tag{2.3}
\]
*Proof.* Semigroup property \(G_sG_t=G_{s+t}\) (`lem:quotient-heat`, remark) and the
fundamental theorem of calculus for the continuous integrand of Lemma 2.1(c). \(\square\)

So along *heat* orbits the heat inverse cancels \(K\) exactly.  Along
Navier–Stokes trajectories one would want
\(\tfrac d{dt}B_h(u(t))=K(u(t))-DB_h(u)[\mathbb P(u\cdot\nabla)u]\); this
requires \(B_h\), hence \(K\), to be differentiable in \(u\), i.e. the map
\(u\mapsto q(u)\) to be differentiable.  The audited stability lemma
gives only \(\|w(u+h)-w(u)\|_3\le2(\|w\|_3+\|h\|_3)^{1/2}\|h\|_3^{1/2}\), a
Hölder-\(\tfrac12\) modulus, and no derivative of the minimizer is available
(HF17, HF18-A non-claims).  **The transport-direction chain rule for \(B_h\)
is therefore unjustified — the packet's falsifier "differentiating the
merely-\(L^3\) minimizer".**  Everything labelled (2.4) below is formal for
that reason, and no rigorous conclusion of this note rests on it: the content
of Theorem 2 is the coercivity failure of \(\mathcal Q-B_h\), proved by static
scaling and needing no chain rule at all.

**Theorem 2 (no coercive exactly cancelling scalar functional of \((\mathcal Q,B_h)\)).**
Work on the ambient scalar domain \(\Omega=(0,\infty)\times\mathbb R\) with
coordinates \((\mathcal Q,B)\), and let \(F\in C^1(\Omega)\).  Say \(F\) *cancels
\(K\) coefficientwise* if, in the formal chain rule
\[
 \tfrac d{dt}F(\mathcal Q,B_h)=F_{\mathcal Q}\bigl(K-\nu D_3(w)\bigr)+F_B\bigl(K-\rho\bigr),
 \qquad \rho:=DB_h(u)[\mathbb P(u\cdot\nabla)u],                         \tag{2.4}
\]
the coefficient \(F_{\mathcal Q}+F_B\) of \(K\) vanishes at every point of \(\Omega\).
(i) Then \(F(\mathcal Q,B)=f(\mathcal Q-B)\) for some \(f\in C^1(\mathbb R)\).
(ii) Suppose \(B_h(\phi)\ne0\) for some solenoidal \(\phi\in\mathcal S(\mathbb R^3)^3\).
Then for every \(E>0\) there is a family \(u_a\), \(a\to\infty\), of solenoidal
Schwartz fields with \(\|u_a\|_2^2=E\), \(\mathcal Q(u_a)-B_h(u_a)=0\) and
\(\mathcal Q(u_a)\to\infty\).  Hence no \(f(\mathcal Q-B_h)\) is coercive in
\(\mathcal Q\), even on a fixed energy shell, and no \(f(\mathcal Q-B_h,\|u\|_2^2)\) is either;
so no such \(F\) satisfies (C) **for the universal reading of (C)** (Section 0.3).
(iii) \(B_h\not\equiv0\) on solenoidal Schwartz fields if and only if
\(K\not\equiv0\) there, if and only if \(K\not\equiv0\) on solenoidal \(H^m\) fields.
If instead \(K\equiv0\) on solenoidal \(H^m\) fields, then (G) holds with
\(\theta=0\), \(M=0\), \(A=0\) and the terminal claim follows from
`prop:quotient-conditional`; so the alternative to the obstruction is the
theorem itself.

*Proof.* (i) is the characteristic argument of `hf04-review-saturation.md`
(REPAIR form, accepted there), applied coefficientwise on the ambient
\(\Omega\): the fibres \(\mathcal Q-B=y\), \(\mathcal Q>0\) of
\(\partial_{\mathcal Q}F+\partial_BF=0\) are connected, so \(F\) is constant along
each and \(F=f(\mathcal Q-B)\), where \(f(y):=F(Q_0,Q_0-y)\) for any \(Q_0>0\) (independent of the choice); \(f\in C^1\) because near each \(y\) a fixed \(Q_0\) serves for all nearby \(y\).

(ii) *Sign.*  \(B_h\) is odd (Prop. 2.2), so replacing \(\phi\) by \(-\phi\) we may
take \(B_h(\phi)>0\).  *Path.*  Choose a solenoidal Schwartz \(\chi\) linearly
independent of \(\phi\) and put \(\psi_\sigma=\cos(\pi\sigma)\phi+\sin(\pi\sigma)\chi\),
\(0\le\sigma\le1\): a path of solenoidal Schwartz fields from \(\phi\) to \(-\phi\)
that never vanishes, continuous into every \(H^k\).  *Continuity of \(B_h\) along
the path.*  \((\sigma,s)\mapsto K(G_s\psi_\sigma)\) is continuous on \([0,1]\times[0,\infty)\)
(Lemma 2.1(c), since \((\sigma,s)\mapsto G_s\psi_\sigma\) is continuous into \(H^m\)),
and it has the integrable majorant
\[
 |K(G_s\psi_\sigma)|\le C_*\|\psi_\sigma\|_3\cdot2\|\psi_\sigma\|_3\|\nabla G_s\psi_\sigma\|_3^2
 \le C(\phi,\chi)\min\bigl(1,(\nu s)^{-3/2}\bigr),
\]
from (Q3), \(\mathcal Q_s^{1/3}\le\|G_s\psi_\sigma\|_3\le\|\psi_\sigma\|_3\), HF18-A (2.3)
\(D_3(w(v))\le2\|v\|_3\|\nabla v\|_3^2\), \(\|\nabla G_sv\|_3\le\|\nabla v\|_3\) and
\(\|\nabla G_sv\|_3\le C(\nu s)^{-3/4}\|v\|_2\); dominated convergence gives
\(\sigma\mapsto B_h(\psi_\sigma)\in C([0,1])\).  Also \(\sigma\mapsto\mathcal Q(\psi_\sigma)\)
is continuous and, by (Q4) and \(\psi_\sigma\ne0\), \(\inf_\sigma\mathcal Q(\psi_\sigma)=:m_0>0\).
*Amplitude.*  For \(a>0\), \(h_a(\sigma):=a\,B_h(\psi_\sigma)-\mathcal Q(\psi_\sigma)\) is
continuous with \(h_a(0)=aB_h(\phi)-\mathcal Q(\phi)>0\) for large \(a\) and
\(h_a(1)=-aB_h(\phi)-\mathcal Q(\phi)<0\); pick \(\sigma_a\) with \(h_a(\sigma_a)=0\).
By Prop. 2.2 and Lemma 2.1(d), \(\mathcal Q(a\psi_{\sigma_a})-B_h(a\psi_{\sigma_a})=a^3(\mathcal Q(\psi_{\sigma_a})-aB_h(\psi_{\sigma_a}))=0\)
and \(\mathcal Q(a\psi_{\sigma_a})\ge a^3m_0\to\infty\).  *Energy shell.*  Put
\(N_a=a^2\|\psi_{\sigma_a}\|_2^2/E\) and \(u_a=aN_a\psi_{\sigma_a}(N_a\cdot)\); then
\(\|u_a\|_2^2=E\), and \(\mathcal Q\), \(B_h\) are dilation invariant (`lem:quotient-scaling`,
Prop. 2.2), so the two displayed relations persist.  Finally \(f(\mathcal Q-B_h)(u_a)=f(0)\)
while \(\mathcal Q(u_a)\to\infty\); with the energy as a passive second argument the
same family has \(f(0,E)\).

(iii) If \(B_h\equiv0\) on solenoidal Schwartz fields then, by Prop. 2.3 applied
to \(\phi\) (each \(G_t\phi\) is solenoidal Schwartz), \(K(G_t\phi)=0\) for all \(t>0\),
and continuity at \(t=0\) (Lemma 2.1(c)) gives \(K(\phi)=0\).  Conversely
\(K\equiv0\) on Schwartz fields gives \(B_h\equiv0\) by (2.1).  \(K\) is continuous
on solenoidal \(H^m\) fields in the \(H^m\) topology (proof of Lemma 2.1(c)) and
Schwartz fields are dense, so the two vanishing statements agree.  If \(K\equiv0\)
on solenoidal \(H^m\) fields then (Q1) reads \(\mathcal Q'=-\nu D_3(w)\le0\) on every
compact classical interval, which is (G) with \(\theta=M=A=0\). \(\square\)

**Remark 2.3.1 (part (ii) does not need part (i)).**  Only constancy of \(F\)
along the single fibre \(\{\mathcal Q-B=0\}\) is used in (ii).  This matters
because the attainable set of pairs \((\mathcal Q,B_h)\) is contained in
\(\{|B|\le\tfrac{3C_*}{4\nu}\mathcal Q^{4/3}\}\subsetneq\Omega\), on which a
fibre \(\{\mathcal Q-B=y\}\) with \(y>0\) need not be connected; but the fibre
used by (ii) is \(y=0\), whose trace on that set is
\(\{\mathcal Q\ge c^{-3}\}\), still connected.  So (ii) survives whether the
coefficientwise premise is imposed on all of \(\Omega\) or only on the
attainable set.  Part (iii) is likewise independent of (i).

**Corollary 2.4 (saturation and truncation do not repair the class).**
(a) *Saturation.*  For \(0<\delta\le\tfrac12\), \(F_\delta:=\mathcal Q-\delta\,B_h/(1+\mathcal Q^{1/3}/\nu)\)
satisfies, by (2.2), \(|F_\delta-\mathcal Q|\le\delta\tfrac{3C_*}{4}\mathcal Q\cdot\tfrac{\mathcal Q^{1/3}/\nu}{1+\mathcal Q^{1/3}/\nu}\le\tfrac{3C_*}{4}\delta\,\mathcal Q\),
so it is coercive for \(\delta<\tfrac{4}{3C_*}\); but the \(K\)-coefficient in (2.4)
is \(1-\delta g(\mathcal Q)-\delta g'(\mathcal Q)B_h\) with \(g(x)=(1+x^{1/3}/\nu)^{-1}=\nu/(\nu+x^{1/3})\).
Since \(|g'(x)|=\tfrac\nu3x^{-2/3}(\nu+x^{1/3})^{-2}\), (2.2) gives
\[
 |g'(\mathcal Q)B_h|\le\frac{3C_*}{4\nu}\mathcal Q^{4/3}\cdot\frac{\nu}{3}\mathcal Q^{-2/3}\bigl(\nu+\mathcal Q^{1/3}\bigr)^{-2}
 =\frac{C_*}{4}\cdot\frac{\mathcal Q^{2/3}}{(\nu+\mathcal Q^{1/3})^2}\le\frac{C_*}{4},
\]
so the coefficient is at least \(1-\delta(1+C_*/4)\ge\tfrac12\) for \(\delta\le\tfrac1{2(1+C_*/4)}\).
The residual \(\tfrac12K\) is then bounded only by (Q3), a coefficient
\(C_*\mathcal Q^{1/3}\) that is not absorbable into \(\nu D_3(w)\) for arbitrary
data.  This is HF04 (15) with \(C_B=3C_*/4\).
(b) *Truncation.*  For an input-selected \(a_L=\nu^{-1}2^{-2L}\) put
\(B_{a}(u)=-\int_{a}^\infty K(G_su)\,ds\).  Then, by (Q3), HF18-A (2.3) and the heat
bounds \(\|G_su\|_3\le C(\nu s)^{-1/4}\|u\|_2\), \(\|\nabla G_su\|_3\le C(\nu s)^{-3/4}\|u\|_2\),
\[
 |K(G_su)|\le C\,(\nu s)^{-2}\|u\|_2^4,\qquad
 |B_{a}(u)|\le C\,\frac{\|u_0\|_2^4}{\nu^2a}=C\,\frac{2^{2L}}{\nu}\|u_0\|_2^4,           \tag{2.5}
\]
an input bound (HF01 (7) transferred), using energy monotonicity `prop:energy`;
and \(B_a\) satisfies (C) with \(c=1\).
The formal normal form is \(K(u)=\tfrac d{dt}B_a(u)+\bigl[K(u)-K(G_au)\bigr]+\rho_a\),
\(\rho_a=DB_a(u)[\mathbb P(u\cdot\nabla)u]\).  The subtracted heat term is
**unconditionally input-controlled**: (2.5) gives
\(|K(G_au)|\le C(\nu a)^{-2}\|u_0\|_2^4\) pointwise in \(t\), hence
\[
 \int_0^\tau|K(G_au)|\,dt\le C\,H\,(\nu a)^{-2}\|u_0\|_2^4
\]
for every input-selected \(a>0\), an input constant; no heat monotonicity of
\(D_3(w)\) is needed for this, and none is assumed.  What remains is therefore
\(K(u)\) itself up to input-controlled terms: the truncation removes only the
low-output part, exactly as HF01 §5.1 found for the pressure work.  The
transport correction \(\rho_a\) is the HF01 §5.2 term, not energy-controlled,
and in any case unjustified here (chain rule).  Scaling of the formal
\(\rho\): \(DB_h\sim B_h/u\sim a^3/\nu\) against \(\mathbb P(u\cdot\nabla)u\sim a^2\lambda\),
so \(\rho\sim(a^5/\nu,\lambda^2)\) versus \(\nu D_3\sim(\nu a^3,\lambda^2)\): the ratio is
\((a/\nu)^2\sim(\mathcal Q^{1/3}/\nu)^2\), two powers supercritical.

## 3. Heat-smoothed value functionals: rigorous evolution, no coercivity

The lane also names "heat- or Riesz-smoothed corrections".  Riesz-smoothed
corrections of \(\mathcal Q\) are not known to have a justified derivative
unless they are value functions (Section 4); heat-smoothed *value* functions
are \(\mathcal Q(G_su)\), whose derivative is rigorous:

**Lemma 3.1.**  For \(s>0\), \(t\mapsto\mathcal Q(G_su(t))\in C^1([0,T])\) with
\[
 \tfrac d{dt}\mathcal Q(G_su(t))+\nu D_3\bigl(w(G_su)\bigr)=K_s(u):=-\bigl\langle A(G_su),\,G_s\bigl((u\cdot\nabla)u\bigr)\bigr\rangle,
 \qquad 0\le\mathcal Q(G_su)\le\min\Bigl(\mathcal Q(u),\ C(\nu s)^{-3/4}\|u_0\|_2^3\Bigr). \tag{3.1}
\]
*Proof.* \(G_su\in C^1([0,T];H^2)\subset C^1([0,T];L^3)\), so `lem:quotient-chainrule`
Step 2 gives \(\tfrac d{dt}\mathcal Q(G_su)=\langle A(G_su),G_su_t\rangle\); insert
(R2), use \(G_s\nabla p\in\mathcal G_3\) (`lem:quotient-heat`(c) with `lem:quotient-pressure`),
which is annihilated by \(A(G_su)\) (`lem:quotient-minimizer`(c) applied at the
field \(G_su\)), and
\(\langle A(G_su),\nu\Delta G_su\rangle=-\nu D_3(w(G_su))\) (HF18-A Thm 2 at \(G_su\)).
The bounds are (Q5) and the \(L^2\to L^3\) heat bound with `prop:energy`. \(\square\)

**Theorem 3 (heat-smoothed modified energies with atomless \(m\) are not coercive).**
Let \(m\) be a finite positive Borel measure on \((0,\infty)\) — in particular
**no atom at \(0\)** — and \(\Phi_m(u):=\int_{(0,\infty)}\mathcal Q(G_su)\,m(ds)\).
Then for every \(c>0\) and every locally bounded \(a:[0,\infty)\to[0,\infty)\)
there are solenoidal Schwartz fields \(u\) with
\(\Phi_m(u)<c\,\mathcal Q(u)-a(\|u\|_2^2)\).  In particular
\(B=\mathcal Q-\Phi_m\) (which includes \(B=\mathcal Q-\mathcal Q(G_{a}u)\))
violates (C) for every \(c\), \(a_{\rm input}\) **in the universal reading of
(C)** (Section 0.3), although Lemma 3.1 gives it an exact evolution.

*Proof.* Fix a solenoidal Schwartz \(u_0\ne0\), \(\alpha>0\), and \(u_{\alpha,\lambda}=\alpha\lambda u_0(\lambda\cdot)\).
Then \(\mathcal Q(u_{\alpha,\lambda})=\alpha^3\mathcal Q(u_0)\) (`lem:quotient-scaling`),
\(\|u_{\alpha,\lambda}\|_2^2=\alpha^2\lambda^{-1}\|u_0\|_2^2\), and
\(\mathcal Q(G_su_{\alpha,\lambda})=\alpha^3\mathcal Q(G_{\lambda^2s}u_0)\le\alpha^3C(\nu\lambda^2s)^{-3/4}\|u_0\|_2^3\to0\)
as \(\lambda\to\infty\) for each \(s>0\); dominated by \(\alpha^3\mathcal Q(u_0)\in L^1(m)\),
so \(\Phi_m(u_{\alpha,\lambda})\to0\).  Choose \(\alpha\) with
\(c\,\alpha^3\mathcal Q(u_0)>2\sup_{[0,1]}a\), then \(\lambda\) so large that
\(\alpha^2\lambda^{-1}\|u_0\|_2^2\le1\) and \(\Phi_m(u_{\alpha,\lambda})<\tfrac12c\alpha^3\mathcal Q(u_0)\). \(\square\)

The mechanism is the low-output phenomenon of HF14–HF15 in functional form:
a heat-smoothed critical functional sees only the scales below the
smoothing scale, and those are energy-controlled (3.1) and therefore cannot
be coercive.

**Remark 3.2 (the atom hypothesis is necessary, and what happens without it).**
The hypothesis "no atom at \(0\)" is not cosmetic.  If \(m=\beta\delta_0+m'\)
with \(\beta>0\), then \(\Phi_m\ge\beta\mathcal Q\) (since
\(\mathcal Q(G_0u)=\mathcal Q(u)\)), so (C) holds for \(B=\mathcal Q-\Phi_m\)
with \(c=\beta\) — Theorem 3 is false for such \(m\), and the mixtures
\[
 \Phi=\beta\mathcal Q+(1-\beta)\mathcal Q(G_au),\qquad 0<\beta<1,\ a>0,
\]
are exactly the class that is both coercive and rigorously differentiable
(Lemma 3.1).  They fail for the *other* reason, the one of Corollary 2.4(a).
With \(B=\mathcal Q-\Phi\), (Q1) and (3.1) give the exact remainder
\[
 R=K-B'=\beta K+(1-\beta)K_a+\nu(1-\beta)\bigl(D_3(w)-D_3(w(G_au))\bigr),
 \qquad K_a:=K_a(u)\ \text{of }(3.1),
\]
in which the dissipation term is absorbable with \(\theta=1-\beta\le1\) and
\(K_a\) is input-controlled for input-selected \(a\) by the (2.5)-type bound
of Corollary 2.4(b), but a fixed fraction \(\beta>0\) of the *unsmoothed*
\(K\) always survives, bounded only by (Q3).  So letting \(m\to\delta_0\)
interpolates continuously between Theorem 3's non-coercivity and the
tautology of Lemma 0.1(b): coercivity is bought back exactly in proportion to
the fraction of \(K\) left uncancelled.

## 4. Functionals built from \(q\), \(A\), \(V\), \(\Pi_{u,A}\), \(\sigma\)

The new structural objects (\(\operatorname{div}A=0\), \(V\in H^1\),
\(\sigma=\hat w\cdot\nabla|w|\), \(\Pi_{u,A}=R_iR_j(A_iu_j)\)) are all functions of
the minimizer \(w(u)\).  This section is a **classification of the mechanisms
by which a functional \(B(u)=\Psi(u,w(u))\) is currently known to have a
justified time derivative along the classical branch**.  It is not a theorem
that no other mechanism exists; no exhaustiveness is claimed or proved below.
Two mechanisms are available:

(a) *Envelope (value functions).*  If \(B(u)=\inf_{g\in\mathcal G_3}\Psi(u+g)\) with
\(\Psi\) convex, Fréchet differentiable, and strictly convex enough for a unique
minimizer with a stability estimate, then the proof of `prop:quotient-derivative`
is expected to transfer (upper bound from the competitor \(w+h\), lower bound from
\(w'-h\), remainder from stability), giving \(DB(u)[h]=D\Psi(w_\Psi(u))[h]\).
**This transfer is a sketch: it is carried out in the audited literature only
for \(\Psi=F\), and it is not carried out here for general \(\Psi\).**  Nothing
in this note depends on it: by Remark 0.2 every such \(B\) is subject to the
same Lyapunov reformulation regardless.  Examples of the shape intended:
\(\Psi=F\) (this is \(\mathcal Q\)); \(\Psi(v)=F(G_sv)\), whose value function is
\(\mathcal Q(G_su)\) because \(G_s\mathcal G_3\subset\mathcal G_3\) and \(G_s\) is
\(L^3\)-contractive (Section 3, where the derivative is proved directly and does
not rely on this sketch); \(\Psi(v)=\tfrac13\int\rho|v|^3\) with a fixed weight;
\(\Psi(v)=F(v)+\langle v,\mu\rangle\) with a fixed \(\mu\in L^{3/2}\).  For every such
\(B\), Remark 0.2 applies to \(\Phi=\mathcal Q-B\): the normal form is the
Lyapunov problem for \(\Phi\), and nothing in the envelope mechanism produces a
sign.  (One could also let \(\Psi\) depend on \(u\) itself, e.g. weights
\(\rho=\rho(u)\); then \(DB(u)[h]=\partial_u\Psi+D\Psi[h]\) at the minimizer, and the
\(\partial_u\Psi\) term is an explicit functional of \(u\) — again Remark 0.2.)

(b) *Inner variation.*  `lem:quotient-transport` differentiates \(\mathcal Q\) along
the flow of \(u\) without differentiating \(w\): with \(u_s=u\circ\Phi_{-s}\),
\(\mathcal Q(u_s)=\mathcal Q(u)+sK+o(|s|)\) (proof, Step 4, with \(K=-\langle A,(u\cdot\nabla)u\rangle\)).
So \(K\) is the *Lagrangian* derivative of \(\mathcal Q\) along its own velocity.
A normal form built on this would be \(B_\varepsilon(u)=\varepsilon^{-1}\int_0^\varepsilon\mathcal Q(u\circ\Phi^u_{-s})\,ds\),
which is a functional of \(u\) alone, but its *time* derivative along Navier–Stokes
involves \(\partial_t\) of the flow map \(\Phi^u\), i.e. the Lagrangian acceleration
\(\nu\Delta u-\nabla p\) composed with the flow, and the pressure gradient is no
longer annihilated after composition with \(\Phi^u_{-s}\) (the pulled-back
gradient \(D\Phi^{\mathsf T}\nabla p\circ\Phi\) is a gradient, but \(\mathcal Q\) is
evaluated at \(u\circ\Phi_{-s}\), not at a coset-invariant object).  The
pressure re-enters: one is back on the pressure route of Section 1.

(c) *Anything else* — \(\int q\cdot\Pi_{u,A}\), \(\int|w|\sigma^2\), \(\int|q|^2|w|^3\),
\(\|V\|_{H^1}^2\)-type corrections — has **no justified time derivative at the
present state of knowledge**, because \(t\mapsto w(u(t))\) is known only to be
\(\tfrac12\)-Hölder into \(L^3\) (`lem:quotient-stability`) and
\(t\mapsto V(u(t))\) only bounded in \(H^1\) (HF18-A (1.9)).  A normal form
using such a \(B\) hits the falsifier "differentiating the merely-\(L^3\)
minimizer" at its first step, before any estimate.  This is a statement about
what is known, not a proof that no derivative exists.  Proving
differentiability of \(u\mapsto w(u)\) (an \(L^3\)-implicit function theorem for
the degenerate \(3\)-Laplace-type equation HF18-A (1.1)) is a distinct open
problem; HF18-A §1.3 records why the standard theory does not apply.

Within the mechanisms (a) and (b), no candidate beyond those computed in
Sections 1–3 was found.  That is a report on this search, not an
exhaustiveness theorem; (c) is explicitly open.

## 5. Bounded numerical evidence (periodic proxy; static problem only)

Scratch `hf19_probe.py` (session scratchpad, ephemeral; **not part of the
record and not present in this repository**): on a \(2\pi\)-periodic box,
\(N^3\) grid, a random solenoidal \(u=\operatorname{curl}\psi\) with modes
\(|k|\le3\), unit mean-square amplitude; \(q=\nabla\phi\) by L-BFGS
minimisation of \(\tfrac13\int|u+\nabla\phi|^3\) in the full
\(N^3\)-dimensional \(\phi\)-space (spectral derivatives); converged
Euler–Lagrange residual \(\max|\operatorname{div}A|/\max|A|\le6\times10^{-7}\).
The periodic problem is a proxy for the variational problem only, never for
the evolution; the numbers are finite-resolution evidence, not proof.  The
heat inverse is computed with \(\nu=1\) on 28 log-spaced heat times up to
\(s=3\) (where \(|K|\le3\times10^{-7}\)), re-minimising at each \(s\).

**Reproducibility defect (recorded by the audit).**  Because the script is not
in the repository, the four runs below are *not reproducible from this
repository*.  The only reproducible independent support for \(K\not\equiv0\)
is the HF18-A audit's \(48^3\) computation, and that is itself recorded only as
printed output.  Nothing in Sections 0–4 depends on these numbers: by
Theorem 2(iii) the alternative to \(K\not\equiv0\) is NS-R3 itself.

| run | \(\mathcal Q\) | \(X/3\) | \(D_3(w)\) | \(D_{\mathcal Q}-D_3(w)\) | \(D_3(u)-D_3(w)\) | \(K\) (F1) | \(K\) (F2) | \(K/(\mathcal Q^{1/3}D_3)\) | \(\|q\|_3/\|w\|_3\) | \(B_h\) | \(B_h/\mathcal Q^{4/3}\) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| \(16^3\), seed 0 | 96.97 | 99.33 | 789.0 | \(+0.35\) | \(+20.7\) | \(-1.098\) | \(-1.100\) | \(-3.0\times10^{-4}\) | 0.118 | \(+0.159\) | \(3.6\times10^{-4}\) |
| \(16^3\), seed 1 | 100.76 | 103.42 | 829.5 | \(+0.51\) | \(+18.4\) | \(-0.0616\) | \(-0.0645\) | \(-1.6\times10^{-5}\) | 0.122 | \(+0.0667\) | \(1.4\times10^{-4}\) |
| \(16^3\), seed 2 | 98.59 | 100.95 | 765.9 | \(+0.40\) | \(+18.3\) | \(-1.338\) | \(-1.336\) | \(-3.8\times10^{-4}\) | 0.120 | \(+0.227\) | \(5.0\times10^{-4}\) |
| \(24^3\), seed 0 | 94.09 | 95.70 | 791.9 | \(+0.11\) | \(+14.1\) | \(-0.1490\) | \(-0.1490\) | \(-4.1\times10^{-5}\) | 0.101 | \(+0.0392\) | \(9.2\times10^{-5}\) |

Readings, with declared range (four low-mode fields, \(\|q\|_3/\|w\|_3\approx0.1\),
two resolutions):
1. \(D_{\mathcal Q}=D_3(w)\) to \(1\)–\(6\times10^{-4}\) relative (discretisation),
   consistent with the audited HF18-A Thm 2; the two transport forms agree to
   the same accuracy.
2. \(K\ne0\) robustly (\(|K|\) exceeds the form-to-form discrepancy by 2–3
   orders in three of four runs and by a factor \(20\) in the fourth), so the
   hypothesis of Theorem 2(ii)–(iii) is supported; this corroborates the
   HF18-A audit's \(48^3\) value \(K=-0.0422\).
3. \(K<0\) in all four runs and along the whole heat orbit until \(|K|\lesssim10^{-4}\);
   hence \(B_h>0\) on these fields, which *supports* the hypothesis
   \(B_h(\phi)\ne0\) of Theorem 2(ii).  It does not supply the field \(\phi\):
   these are \(2\pi\)-periodic fields and Theorem 2(ii) is stated for
   solenoidal Schwartz fields on \(\mathbb R^3\); that transfer is not made
   here.  The ratio \(B_h/\mathcal Q^{4/3}\) is \(10^{-4}\)–\(10^{-3}\), far
   below \(3C_*/(4\nu)\): (2.2) is a size bound, not sharp on these fields.
   No sign of \(K\) is claimed in general (HF18-B §3.3(d)).
4. \(D_3(u)-D_3(w)>0\) in all four runs (\(1.8\)–\(2.6\%\) of \(D_3\)); Remark 1.3.

## 6. Frontier record

**MODE / RESULT:** DISCOVER, negative in each of the three classes computed,
with the obstruction proved per class.  Positive by-products: Theorem 1 (exact
identity \(\int(K-P_3)=[\mathcal Q-X/3]+\nu\int(D_3(w)-D_3(u))\), a subtraction
of two audited balances, with the unconditional one-sided transfer
`hyp:absorption` \(\Rightarrow\) (G) of Corollary 1.1(b), exact constant
\(X(0)/3\)); Proposition 2.2 (\(|B_h|\le\tfrac{3C_*}{4\nu}\mathcal Q^{4/3}\),
exact); Theorem 2 (HF04 obstruction transferred to the quotient route, with
the sign step made correct through the oddness of \(K\)); Theorem 3
(heat-smoothed modified energies with atomless \(m\) are not coercive).
Remark 0.2 is recorded as a change of variables, not as a by-product of the
same weight as these.

**CLAIM AND SCOPE:** Lemma 0.1 (with the constant (R1.3); the note uses it
only at \(c=1\)), Remark 0.2, Theorem 1, Cor. 1.1(a)',(b),(c) on every compact
classical interval of the branch of `prop:localtheory`, using only the audited
(Q1)–(Q5), (P1)–(P2); Cor. 1.1(b) unconditional and instantaneous, Cor. 1.1(a)'
only post-Gronwall and **not** an instance of `hyp:absorption` as the
manuscript states it (Remark 1.1.1).  Lemma 2.1, Prop. 2.2–2.3 for every
solenoidal \(u\in H^m\), \(m\ge4\), \(\nu>0\).  Theorem 2 on the ambient scalar
domain \(\Omega\) with coefficientwise cancellation as defined in (2.4), part
(ii) under the hypothesis \(B_h\not\equiv0\) (equivalently \(K\not\equiv0\),
part (iii)) and, as a statement about (C), **only for the universal reading of
(C)**; part (ii) needs only the fibre \(y=0\), hence is independent of part (i)
(Remark 2.3.1).  Cor. 2.4 formal for the chain rule, rigorous for the bounds
(2.5) and for the unconditional input control of \(K(G_au)\).  Lemma 3.1
unconditional; Theorem 3 unconditional for atomless \(m\) and, as a statement
about (C), **only for the universal reading of (C)**; Remark 3.2 records the
atom-carrying mixtures and their exact remainder.  Section 4 is a
classification of the mechanisms by which a functional is currently known to
admit a justified derivative, not a theorem about all functionals; no
exhaustiveness is claimed.

**EVIDENCE:** `prop:quotient-evolution`, `lem:quotient-transport`,
`lem:quotient-chainrule`, `lem:quotient-heat`, `lem:quotient-stability`,
`lem:quotient-scaling`, `lem:quotient-coercive`, `lem:quotient-heatsign`,
`prop:pressure`, `prop:lowpressure`, `prop:energy`, `lem:qe-gronwall`,
`prop:quotient-conditional`, `rem:highstrain-scope` [DI, manuscript];
HF18-A Thm 2, Prop. 3, (2.3), (4.2) and HF18-B §0, Prop. 1.4 [audited notes;
Prop. 1.4 is a source of test fields only, load-bearing for nothing];
the HF04 review's characteristic argument [DI]; Young's inequality for the
heat kernel; four converged periodic minimisations (scratch `hf19_probe.py`,
declared range in Section 5, **not reproducible from this repository**).
Audit: `research/evidence/hf19-review-temporal-normal-form.md`, verdict
REPAIR, repairs R1–R4 and its editorial items applied here on 2026-09-06.

**FIRST GAP:** unchanged, and now located precisely in each normal form.  In
the distance form (1.2) it is the high-output pressure work
\(\int_0^\tau(P_3)_{>J}\), scaling \((a^4,\lambda^2)\) — `hyp:highpressure`
verbatim; in the heat-inverse form it is, in order, the unjustified
transport-direction chain rule for \(B_h\) and then the boundary condition
(C), which (2.2) supplies only under \(\tfrac{3C_*}{4\nu}\mathcal Q^{1/3}\le1-c\)
(hidden smallness); in the heat-smoothed form it is (C) itself (Theorem 3),
and in the atom-carrying mixtures it is the surviving fraction \(\beta K\)
(Remark 3.2).  At the level of Remark 0.2 the first unsupported implication is
the existence of a coercive \(\Phi\) with (L), which is the packet's statement
that any closing mechanism is a regularity proof.  Nothing in this note
closes, weakens, or reformulates
\(\int_0^\tau K\le\theta\nu\int_0^\tau D_3(w)+M\int_0^\tau\mathcal Q+A_{\rm input}\)
at its quantifiers.

**SURVIVING CONDITIONAL SUFFIX:** (i) If `hyp:absorption` holds with
\(\theta_p\le1\), then (G) holds for \(K\) with \(\theta_s=1\), \(M=0\),
\(A_{\rm input}=A+X(0)/3\) — unconditional and instantaneous, Cor. 1.1(b).
Conversely, if (G) holds for \(K\) with \(\theta_s\le1\), then after the
Gronwall closure one obtains the *Gronwall-form* pressure bound of
Cor. 1.1(a)' with \(\theta_p=1\) and constant degraded by
\(C_{\mathbb P}^3e^{MH}\), together with `hyp:critical`; this is a consequence
of the closure, not an independent transfer, and is not `hyp:absorption` in
the manuscript's sense.  A strict \(\theta<1\) in either direction needs a
comparison between \(D_3(u)\) and \(D_3(w)\) (Remark 1.3); neither direction is
proved.  (ii) If \(u\mapsto w(u)\) were shown differentiable (an
implicit-function theorem for HF18-A (1.1)), the formal chain rule of (2.4)
would become rigorous; Theorem 2 shows this would not help the class
\(F(\mathcal Q,B_h)\), but it would open the classes of Section 4(c), which
this note has not examined for content beyond the differentiability
obstruction.

**NON-CLAIMS:** no sign of \(K\), \(P_3\), or \(D_3(u)-D_3(w)\) in general (only
bounded numerical evidence at four fields); no differentiability of
\(u\mapsto w(u)\); no rigorous transport-direction chain rule for \(B_h\); (2.4)
is formal throughout; no obstruction for the general class of functionals
(Remark 0.2 shows none is provable without deciding NS-R3); no HIGH-STRAIN,
HIGH-PRESSURE, critical, continuation, or regularity result; no novelty claim
for the heat-inverse device (HF01/HF04) or the characteristic argument (HF04
review); no statement about which \(w\) occur along trajectories from the
periodic numerics.  Added with the audit: Remark 0.2 is a change of variables
\(\Phi=\mathcal Q-B\) with \(R:=K-B'\) by definition, not a theorem about
normal forms; Theorems 2 and 3 do **not** exclude a corrector satisfying (C)
only along the trajectories of a given datum — they exclude universal
coercivity over solenoidal Schwartz fields (Theorem 3) and over a fixed energy
shell (Theorem 2(ii)), and since Lemma 0.1(a) uses (C) only at \(u(\tau)\) the
obstruction is strictly weaker than a route-level reading of it; Theorem 1 is
a subtraction of two audited balances and establishes no new estimate; the
numerics of Section 5 are not reproducible from this repository; the
"exhaustion" of temporal normal forms on this route is **not** claimed
(see NEXT DISTINCT ACTION).  Nothing here is a Millennium result and nothing
here changes the claim graph.  NS-R3 remains OPEN.

**OPEN QUESTIONS**

- needs review: the quantifier on (C) is not fixed anywhere in this note or in
  the programme record.  If (C) is read trajectory-locally (over
  \(\{u(\tau):0<\tau<\min(H,T_*)\}\) for each \((\nu,u_0,H)\), with
  \(a_{\rm input}\) datum-dependent), Theorems 2(ii) and 3 exclude nothing and
  the heat-inverse and heat-smoothed classes must be re-examined from
  scratch.  If (C) is fixed universally, they stand as proved.  This choice
  should be made explicitly by the programme.
- needs review: whether the boundary term \(Y(\tau)=X(\tau)/3-\mathcal Q(\tau)\)
  of Corollary 1.1(a)' can be bounded by input data *without* first closing
  (G) by Gronwall.  (Q4) alone cannot: \(Y\) and \(X/3\) have the same
  criticality \((a^3,\lambda^0)\).  A such bound would restore the
  instantaneous two-way reading of (1.1).
- needs review: `hf19_probe.py` is not in the repository; restoring it and
  reproducing the four runs would discharge the reproducibility defect of
  Section 5.

**NEXT DISTINCT ACTION:** two well-posed static questions fall out of
Theorem 1 and Remark 1.3, both on the linear test class of HF18-B Prop. 1.4
(\(w=|A|^{-1/2}A\), \(u=\mathbb Pw\), \(A\) solenoidal): (1) FALSIFY or prove
\(D_3(w(u))\le D_3(u)\) for solenoidal \(u\); a counterexample kills the
"strain route is sharper" reading of (1.1), a proof makes the strain gap
formally weaker than the pressure gap by exactly \(\nu\int(D_3(u)-D_3(w))\ge0\);
(2) FALSIFY or prove heat monotonicity \(D_3(w(G_su))\le CD_3(w(u))\) — a
distinct static question, but no longer needed by Corollary 2.4(b), whose
subtracted term is unconditionally input-controlled by (2.5).
Neither closes the gap.  The route-level conclusion that may be recorded is
**not** that temporal normal forms are exhausted on the quotient route, but
the summary of what was computed: *no candidate survived in the three classes
computed — \(B=\mathcal Q-X/3\); \(F(\mathcal Q,B_h)\) with coefficientwise
cancellation on \(\Omega\); \(\Phi_m\) with atomless \(m\) — under the
universal reading of (C).*  An exhaustion statement is not proved here and is
in tension with Remark 0.2, which shows that no obstruction theorem for the
general class is provable without deciding NS-R3.  The mechanism that remains
open is a genuine cancellation inside \(K=\int q\cdot\nabla\Pi_{u,A}\) on
families with \(\|q\|_3/\|w\|_3\) driven up (HF18-A audit R9), i.e. the
FALSIFY action already recorded in HF18-B, together with the classes of
Section 4(c) and the trajectory-local reading of (C).
