# Review of HF19-D `hf19-difference-functional.md`: difference functional, its evolution, and the sign structure of $D_3(u)-D_3(w)$

Independent proof audit, 2026-09-06. Reviewer lane: proof-audit (adversarial,
reconstruct-from-first-implication).

**Frozen candidate.**
`research/evidence/hf19-difference-functional.md`,
sha256 `c88f90b9843a06dffbccbc47690c200175e5466857f4688070c0c8be09dca5d5`,
629 lines. Repository `/home/ert/proj/navier` at
`1014e7e3c33af4a341a5f46156a22b808170257b`. Manuscript
`/home/ert/proj/navier-paper/main.tex` at `39ccb66` (clean tree, 7007 lines).
Audited background read in full and used as given (all PASS):
`hf18-hodge-regularity.md` (§0 hypothesis (0.1), (1.12), Theorem 2 Steps 1–4,
(0.3), (F1), (F5)–(F7), (4.2)), `hf18-divergence-speed-link.md` (§1 (1.6),
Prop. 1.4, §2.3 Prop. 2.2 witness family and Lemma B), and the manuscript
statements `def:D3P3`, `prop:pressure`, `prop:localtheory`, `lem:cubic-pointwise`,
`lem:cubic-frechet`, `lem:quotient-minimizer`, `lem:quotient-coercive`,
`lem:quotient-stability`, `prop:quotient-derivative`, `lem:quotient-pressure`,
`lem:quotient-chainrule`, `lem:heat-generator`, `lem:qe-heat-continuity`,
`lem:quotient-heatsign`, `lem:quotient-transport`, `prop:quotient-evolution`.

---

## VERDICT

**REPAIR.** §§1–3 and §4.1 are correct as stated and were reconstructed
independently, including a from-scratch re-derivation of the Fermi-chart
identity (3.3) that agrees exactly. §4.2 — the classification of candidate
$\Delta$-weighted bounds — contains the first bad bridge: its selection of
(4.3) as "the strongest candidate" is unjustified, and its assertion that "no
scaling family violates (4.3)" is unsupported for the second half of (4.3)
and is, on the scaling heuristic, **false** on precisely the HF18-B witness
family the note's own NEXT ACTION (2) proposes to test. A replacement lemma
(sharp two-sided defect control, R1 below, with proof) is supplied; it repairs
the classification, sharpens (1.2)/(4.1) by a factor $(\Delta/\mathcal Q)^{1/6}$,
and identifies the correct monomial. None of this weakens the note's two
obstructions or its retirement decision; it strengthens both.

---

## REVIEWED SCOPE

Reconstructed and checked from the first nontrivial implication:

* §0 setting; the identification of $D_3(u)$, $P_3$ with `def:D3P3`.
* §1: Lemma 1.1, Proposition 1.2, both scaling lines.
* §2: Lemma 2.1 (including the legitimacy of the pointwise/$C^1$ upgrade of
  `prop:pressure`(ii)), Theorem 2.2 (2.2)–(2.5), Corollary 2.3, Remarks (i)–(iii).
* §3: Lemma 3.1, Theorem 3.2 (both ends of the improper integral, the explicit
  Schwartz witness), Proposition 3.3, Proposition 3.4 (a)–(e) with an
  independent symbolic recomputation of (3.3), Corollary 3.5, Remarks (i)–(iii).
* §4: Proposition 4.1(a),(b),(c) including the constant $C_{**}$ and every
  exponent in its proof; Proposition 4.2(i),(ii),(iii); the constant-speed remark.
* §5: the declared range of the numerics; consistency of the reported numbers
  with §1–§4 (used only as corroboration).
* §6, §7: self-check, CLAIM AND SCOPE, FIRST GAP, NON-CLAIMS.

Not re-proved (imported as audited): HF18-A Theorem 2 ($D_{\mathcal Q}=D_3(w)$),
HF18-A (4.2) ($|K|\le C_*\mathcal Q^{1/3}D_3(w)$), HF18-B Prop. 1.4 and (1.6),
and the manuscript lemmas listed above.

---

## PRELIMINARY: the two balances may be subtracted (the question posed)

The worry that `prop:pressure` and `prop:quotient-evolution` live in different
solution classes is **resolved, and the note does not paper over the one real
asymmetry.**

1. *Same object, same interval.* `prop:pressure` is stated for "the classical
   branch of `prop:localtheory` with normalised pressure $p=R_iR_j(u_iu_j)$",
   using package (R1)–(R2) of the section preamble (main.tex:2615–2626).
   `prop:quotient-evolution` is stated "with the notation and package (R) of
   Section `subsec:qe-trajectories`" (main.tex:5736–5760), which fixes
   $u_0\in\mathcal S$ divergence-free, $\nu>0$, $(u,p)$ *the maximal classical
   solution selected by* `prop:localtheory`, and $[0,T]\subset[0,T_*)$ compact.
   Both packages are explicitly derived from `prop:localtheory`(iii),(iv); the
   quotient package (R1)–(R3) is strictly larger and includes everything the
   pressure package uses. There is one solution, one interval, one pressure
   normalisation. The subtraction is legitimate.

2. *The asymmetry that matters, and how it is handled.* `prop:pressure`(ii) is
   an **integrated** identity on $[s,t]$, and `prop:pressure`(i) claims only
   that $t\mapsto D_3(t),P_3(t)$ are *measurable and bounded* — deliberately
   not continuous — whereas `prop:quotient-evolution` is a genuine pointwise
   $C^1$ identity on $[0,T]$. Subtracting an a.e.-differential consequence of
   an integrated identity from a pointwise one would be a defect.
   The note does not do this. Lemma 2.1 **re-derives** the cubic balance in
   pointwise $C^1$ form, from `lem:cubic-frechet` (Fréchet differentiability of
   $F$ on $L^3$), $u\in C^1([0,T];L^3)$ (Step 1 of `lem:quotient-chainrule`,
   via $H^2\hookrightarrow L^3$), and three fixed-time identifications. As a
   by-product it *proves* what the manuscript does not claim: $X\in C^1([0,T])$
   and $t\mapsto D_3(t),P_3(t)$ continuous, since
   $-\langle j(u),\Delta u\rangle$ and $-\langle j(u),\nabla p\rangle$ are
   continuous in $t$ by (R3) plus `eq:cp-F-lipschitz`. **Theorem 2.2 therefore
   does not depend on `prop:pressure` at all**; it is strictly stronger, and
   the audit question "may they be subtracted" is answered by the note's having
   made the subtraction unnecessary. Checked in detail:

   * $\nabla j(u)=Dj(u)\nabla u$ with $|Dj(z)|\le2|z|$: $j\in C^1(\mathbb R^3)$
     with $Dj(z)=|z|I+z\otimes z/|z|$ ($z\ne0$), $Dj(0)=0$; so
     $j(u)\in C^1\cap W^{1,3/2}$ since $|u|\in L^3$, $|\nabla u|\in L^3$. ✓
   * $-\langle j(u),\Delta u\rangle=\int\nabla j(u):\nabla u$: this is exactly
     the explicit cutoff version in HF18-A Theorem 2 **Step 3** (with $A$
     replaced by $j(u)$), whose error term is
     $R^{-1}\|\nabla\eta\|_\infty\|j(u)\|_{3/2}\|\nabla u\|_{L^3(R\le|x|\le2R)}\to0$.
     The citation is accurate (Step 1 is the cutoff-free difference-quotient
     argument; Step 3 is the cutoff one). ✓
   * $\int\nabla j(u):\nabla u=\int(|u||\nabla u|^2+u_j\partial_i|u|\,\partial_iu_j)
     =\int(|u||\nabla u|^2+|u||\nabla|u||^2)$ by $u_j\partial_iu_j=|u|\partial_i|u|$
     a.e. This is `def:D3P3` verbatim: the manuscript's
     $V(u,\nabla u)=|(\nabla u)^{\mathsf T}u|^2/|u|$ has
     $((\nabla u)^{\mathsf T}u)_i=u_j\partial_iu_j=|u|\partial_i|u|$, so
     $V=|u||\nabla|u||^2$, with the same $0$-on-$\{u=0\}$ convention. ✓
   * $P_3$: the manuscript's $\int p\,(u\otimes u):\nabla u/|u|=\int p\,u\cdot\nabla|u|$;
     identical. ✓
   * $\langle j(u),(u\cdot\nabla)u\rangle=0$: $j(u)\cdot(u\cdot\nabla)u
     =u\cdot\nabla(|u|^3/3)$ with $|u|^3\in W^{1,1}$
     ($\nabla|u|^3=3|u|^2\nabla|u|$, $|u|^2\in L^{3/2}$, $|\nabla u|\in L^3$),
     so HF18-A (0.3) applies. ✓
   * $-\langle j(u),\nabla p\rangle=\int p\operatorname{div}j(u)$: same cutoff,
     error $\le R^{-1}\|\nabla\eta\|_\infty\|p\|_3\|j(u)\|_{3/2}\to0$. ✓

**Integration item.** Lemma 2.1 is a strict upgrade of `prop:pressure`(ii)
(from an integrated identity with merely measurable integrands to
$X\in C^1$ with continuous $D_3,P_3$) obtained from the manuscript's own
package. This is a manuscript-grade improvement and should be recorded as such
rather than left in an evidence note.

---

## WHAT PASSES

### §1
* **Lemma 1.1** ($f(a+h)-f(a)-j(a)\cdot h\ge\frac16|h|^3$). Verified:
  `eq:cp-monotone` applied to the pair $(a+\theta h,a)$ gives
  $(j(a+\theta h)-j(a))\cdot h\ge\frac12\theta^2|h|^3$ for $\theta>0$;
  $\int_0^1\frac12\theta^2\,d\theta=\frac16$. ✓
* **Proposition 1.2.** Both applications of Lemma 1.1 checked
  ($a=w,h=-q$ with $\langle A,q\rangle=0$ from `lem:quotient-minimizer`(c);
  $a=u,h=q$), and (1.2) from `eq:cp-F-lipschitz`. All pairings are
  $L^{3/2}\times L^3$. The chain $\|u\|_3\le C_{\mathbb P}\|w\|_3$,
  $\|w\|_3=(3\mathcal Q)^{1/3}$ is `lem:quotient-coercive`. Scaling verified. ✓
  (Also $\|w\|_3\le\|u\|_3$ from $\mathcal Q(u)\le F(u)$ — used implicitly
  in §4.2(ii); correct.)

### §2
* **Theorem 2.2.** Reconstructed line by line. $\Delta'=\langle j(u)-A,u_t\rangle$
  from `lem:quotient-chainrule` minus Lemma 2.1; substitution of
  $u_t=\nu\Delta u-(u\cdot\nabla)u-\nabla p$; the three cancellations
  ($\langle A,\nabla p\rangle=0$ by `lem:quotient-pressure`;
  $\langle j(u),(u\cdot\nabla)u\rangle=0$;
  $-\langle A,\Delta u\rangle=D_{\mathcal Q}=D_3(w)$ by HF18-A Thm 2). Signs
  in (2.4), (2.5) all check. The Leray normalisation is right:
  $p=-\Delta^{-1}\partial_i\partial_j(u_iu_j)$ gives
  $(I-\mathbb P)[(u\cdot\nabla)u]=-\nabla p$, hence
  $(u\cdot\nabla)u+\nabla p=\mathbb P[(u\cdot\nabla)u]$. ✓
  Vanishing on $\mathcal M$: at $q=0$, $A=j(u)$ pointwise, so all of
  $\Delta,\Delta',D_3(u)-D_3(w),P_3,K$ vanish. (Note $P_3=0$ on $\mathcal M$
  independently: $\operatorname{div}j(u)=0$ there.) ✓
* **Corollary 2.3.** Quotient rule recomputed; both displays correct. ✓
* **Remark (ii)** — that $\mathcal Q\le F(u)\le C_{\mathbb P}^3\mathcal Q$ makes
  $F$, $\mathcal Q$, $\Delta$ mutually redundant as controlled quantities — is
  exact and is the strongest part of the retirement argument (see below). ✓

### §3
* **Lemma 3.1.** The two-sided differentiability of $s\mapsto G_su$ in $L^3$
  is correct (for $h\uparrow0$, $(v_{s+h}-v_s)/h=G_{s+h}[(G_{|h|}u-u)/|h|]$
  with $L^3$ contraction and `lem:qe-heat-continuity`(b)). $m\ge4$ is exactly
  what `lem:heat-generator` needs: $H^4\hookrightarrow C^2_b$ and
  $\Delta u\in H^2\subset L^3\cap C^{0,\alpha}_b$. HF18-A (0.1) is a static
  hypothesis on any solenoidal $H^m$ field, so Theorem 2 applies at each $v_s$. ✓
  Decay: $\|k_s\|_2=(8\pi s)^{-3/4}$ (recomputed), interpolation
  $\|v\|_3\le\|v\|_2^{2/3}\|v\|_\infty^{1/3}$, hence
  $\|v_s\|_3\le(8\pi s)^{-1/4}\|u\|_2\to0$ and $0\le\Delta(v_s)\le F(v_s)\to0$. ✓
* **Theorem 3.2 (the heat-flow identity).** *Both ends check.* At $s=0$ the
  integrand is finite ($D_3(v)\le\|v\|_\infty\|\nabla v\|_2^2\cdot2$) and
  continuous, so there is no improper endpoint at $0$; at $s=\infty$ the
  improper Riemann integral converges because the primitive
  $\Delta(u)-\Delta(v_S)$ converges. (Absolute convergence in fact also holds —
  $D_3(v_s)\lesssim s^{-7/4}\|u\|_2^3$ for large $s$ — but the note wisely does
  not need it.) The Schwartz witness was recomputed:
  $u=e^{-|x|^2}(-2x_1x_2,2x_1^2-1,0)$, at $(0,1,0)$ one has $u_2=-e^{-1}$,
  $\partial_2|u|^2=-4e^{-2}$, $u\cdot\nabla|u|^2=4e^{-3}\ne0$. ✓
  **This is the note's one new unconditional theorem and it stands.**
* **Proposition 3.3.** Immediate from (3.1) and $\Delta\ge0$. ✓
* **Proposition 3.4 (elliptic swirl).** Membership: $\operatorname{div}T=
  \operatorname{div}\nabla^\perp d=0$ and $|\varphi|\varphi$ depends only on $d$,
  so $\operatorname{div}(|u_0|u_0)=f|f|\operatorname{div}(|\varphi|\varphi\,T)=0$
  **exactly**, and $|u_0|u_0\in C^1$; $u_0\in\mathcal M$. ✓
  Identity (3.3) **independently re-derived twice**: (a) by hand via the
  orthogonal Fermi frame ($h_t=J=1+\kappa d$, $h_d=1$), giving
  $\Delta a=P\,T-(\varphi\kappa_s/J^3)N$ with
  $P=\varphi''+\kappa\varphi'/J-\kappa^2\varphi/J^2$, and then
  $R_2=-2\varphi^2\varphi'\kappa_s/J^3+2\varphi^2\varphi'\kappa_s/J^3
  -4\varphi^3\kappa\kappa_s/J^4$; (b) symbolically from scratch (sympy, my own
  script, Cartesian components $\varphi(d)(\cos\theta,\sin\theta)$,
  $\theta'=\kappa$, curvilinear Laplacian), which returns
  $a\cdot\Delta a=\varphi(\varphi''+\kappa\varphi'/J-\kappa^2\varphi/J^2)$,
  $(\Delta a)\cdot N=-\varphi\kappa_s/J^3$, and
  $R_2+4\kappa\kappa_s\varphi^3/J^4\equiv0$. **(3.3) is exact.** ✓
  The $s$-differentiation (c) and the locality step (d) are correct for
  $u_0\in C_c^\infty$. The conclusion "$G_su_0\notin\mathcal M$ for all small
  $s>0$" is correct with $s_0=s_0(x)$ after fixing one $x$ with
  $\kappa\kappa_s\varphi\ne0$; the note's phrasing is accurate.
* **Corollary 3.5.** Correct: $\Delta(G_su_0)>0=\Delta(u_0)$ for small $s$
  forces a positive derivative somewhere; $\Delta(G_su_0)\to0$ forces a negative
  one later.

  **Answer to the posed question "is the sign proved or only tested":
  the *no-sign* statement is a theorem, in both directions,** and it does not
  rest on any numerics. §5.1's twelve bulk fields ($D_3(w)<D_3(u)$) and §5.2's
  near-$\mathcal M$ family ($D_3(w)>D_3(v_s)$) are corroboration only, correctly
  declared as such.

### §4.1
* (a) The parity argument is correct: $\mathcal G_3$ is a linear space, so
  $q(-u)=-q(u)$, $A(-u)=-A(u)$, while $(u\cdot\nabla)u$ and $p=R_iR_j(u_iu_j)$
  are even; hence $P_3,K,P_3-K$ are odd on the class of smooth solenoidal
  fields, and a one-sided dissipation bound is equivalent to the two-sided one
  (the dissipations are even). Correctly scoped to "at every fixed time". ✓
* (b) (4.1) is Hölder against (1.2); the supercriticality of each right factor
  is correctly displayed. ✓
* (c) **(4.2) verified in full, constant included.** Chain:
  $|P_3|\le(\int p^2|u|)^{1/2}D_3(u)^{1/2}$;
  $\int p^2|u|\le\|p\|_3^2\|u\|_3\le C_{CZ}^2\|u\|_6^4\|u\|_3$;
  $\|u\|_6\le\|u\|_3^{1/4}\|u\|_9^{3/4}$ (interpolation
  $\frac16=\frac14\cdot\frac13+\frac34\cdot\frac19$ ✓), so
  $\|u\|_6^4\|u\|_3\le\|u\|_3^2\|u\|_9^3$;
  $\|u\|_9^3=\|V_u\|_6^2\le S^2\|\nabla V_u\|_2^2\le\frac98S^2D_3(u)$.
  The last step uses HF18-A (1.12) as *pointwise algebra*, which I verified
  independently for an arbitrary $C^1$ field: with $r=|u|$,
  $|\nabla V|^2=r|\nabla u|^2+\frac54 r|\nabla r|^2$ and
  $|\nabla|V||^2=\frac94r|\nabla r|^2$, so
  $|\nabla V|^2-\frac19|\nabla|V||^2=r|\nabla u|^2+r|\nabla r|^2$ exactly.
  Hence $C_{**}=(9/8)^{1/2}SC_{CZ}=\frac{3}{2\sqrt2}SC_{CZ}$. ✓
  Scaling $(a^4,\lambda^2)$ both sides. ✓ The "closes only under
  $\|u\|_3\lesssim\nu$" caveat is stated.

---

## FIRST BAD BRIDGE

**Proposition 4.2, preamble and item (i)** (lines 425–436 of the candidate):

> "the only monomials $\Delta^\alpha\mathcal Q^\beta D$ with the weight
> $(a^4,\lambda^2)$ of $P_3-K$ have $\alpha+\beta=\tfrac13$; **the strongest
> candidate is** (4.3) …"
> "(i) *Status: OPEN, not refuted.* … **no scaling family violates (4.3)**"

Two distinct defects, in order.

### B1. "the strongest candidate is (4.3)" — unjustified, and false as an ordering claim

The constraint $\alpha+\beta=\frac13$ is correct (recomputed: $\Delta,\mathcal Q
\sim(a^3,\lambda^0)$, $D\sim(a^3,\lambda^2)$, so $3(\alpha+\beta)+3=4$). But the
one-parameter family it defines is **not totally ordered**: on $\Delta/\mathcal Q\to0$
(the near-$\mathcal M$ regime, which is the only regime where such a bound has
content) larger $\alpha$ is *stronger*, on $\Delta/\mathcal Q\to C_{\mathbb P}^3-1$
smaller $\alpha$ is stronger. Nothing in §4.2 selects $(\alpha,\beta)=(\frac13,0)$.
Worse, the member the defect estimate actually delivers is
$(\alpha,\beta)=(\frac12,-\frac16)$, not $(\frac13,0)$ — see the replacement
lemma. The selection of (4.3) is an artefact of the lossy cube-root in (1.2),
not of the structure.

### B2. "no scaling family violates (4.3)" — unsupported, and refuted for the second inequality

(4.3) is a **pair** of inequalities. Both probes offered in §4.2(i) — the
near-$\mathcal M$ heuristic and the high-frequency family $u_0+\varepsilon h_k$ —
are computations of $|P_3-K|$ only. The second inequality,
$|D_3(u)-D_3(w)|\le C(\Delta/\mathcal Q)^{1/3}(D_3(u)+D_3(w))$, is never probed,
and the blanket claim covers it without evidence. It is not merely untested:

**Refutation (scaling-heuristic, on the HF18-B witness family — the family the
note's own NEXT ACTION (2) proposes).** Take $w_\delta=w_0+w_1$ of
`hf18-divergence-speed-link.md` §2.3 Prop. 2.2: $w_0=|A_0|^{-1/2}A_0$ the
azimuthal bulk ($w_0\in\mathcal M$, $q_0=0$, $\mathbb Pw_0=w_0$), and
$w_1=|A_1|^{-1/2}A_1=\delta\,G(kx)\chi((x-x_0)/R)$ the oscillatory piece on a
ball disjoint from the bulk, with the note's own choice $R^3=\delta^{-2}$,
$k=\delta^{-1/2}$. Put $u_\delta:=\mathbb Pw_\delta$. Since
$w_\delta\in\mathcal M$ and $w_\delta-\mathbb Pw_\delta\in\mathcal G_3$,
HF18-B (1.6) gives $w(u_\delta)=w_\delta$ and $q(u_\delta)=(I-\mathbb P)w_1$.
Orders (all from the note's own cell bookkeeping, $\langle\cdot\rangle$ = cell
averages of the fixed profile $G$, $kR=\delta^{-7/6}\to\infty$ so cutoff
corrections are $O((kR)^{-1})$):

| quantity | order |
|---|---|
| $\|w_1\|_3^3\sim\delta^3R^3$ | $\delta$ |
| $\|q_\delta\|_3^3\le(1+C_3)^3\|w_1\|_3^3$ | $\lesssim\delta$ |
| $\mathcal Q(u_\delta)=\frac13\|w_\delta\|_3^3\ge\frac13\|w_0\|_3^3$ | $\asymp1$ |
| $\Delta(u_\delta)\asymp\int|w||q|^2\sim\delta\cdot\delta^2\cdot R^3$ | $\asymp\delta$ (R1(a) below, and (1.1) above) |
| $D_3(w_\delta)=D_3(w_0)+D_3(w_1)$, $D_3(w_1)\sim\delta^3k^2R^3$ | $\asymp1$ |
| $D_3(u_\delta)=D_3(w_0+\mathbb Pw_1)$, $D_3(\mathbb Pw_1)\sim\delta^3k^2R^3$ | $\asymp1$ |

Hence $(\Delta/\mathcal Q)^{1/3}\sim\delta^{1/3}\to0$ while
$D_3(u_\delta)+D_3(w_\delta)\asymp1$, so the right side of (4.3)-second tends
to $0$. The left side does not: the bulk contributes exactly $0$ to it
($\mathbb Pw_0=w_0$), and the oscillation contributes
$D_3(\mathbb Pw_1)-D_3(w_1)\to\langle\mathbb PG\rangle_{D_3}-\langle G\rangle_{D_3}$,
a difference of two cell functionals of the *fixed* profile $G$ and its cell
Leray projection $\mathbb PG$. These differ unless $G$ is exceptional: $w_1$ is
not solenoidal ($\operatorname{div}w_1=-\sigma_1$ with
$\langle|\Sigma|^{3/2}\rangle>0$ by the note's own construction), and
$(I-\mathbb P)w_1$ has amplitude $\sim\delta k/k=\delta$, i.e. comparable to
$w_1$ itself, so $\mathbb PG\ne G$ at leading order. The note's own §5.1 table
is the direct evidence that these two functionals differ in practice:
twelve fields with $w\in\mathcal M$, $u=\mathbb Pw$, and
$D_3(w)/D_3(u)\in[0.978,0.994]$, i.e. bounded away from $1$.

So (4.3)-second fails by a factor $\delta^{-1/3}$. Note also that the same
family kills every $\Delta$-weighted version of the second inequality with a
positive power of $\Delta$, including the sharpened
$(\Delta/\mathcal Q)^{1/2}$ member.

*Why the first inequality survives this family:* on the oscillation region
$|A-j(u)|\sim|w||q|\sim\delta^2$ and $|(u\cdot\nabla)u|\sim\delta^2k$, so
$|P_3-K|\lesssim\delta^4kR^3=\delta^2k=\delta^{3/2}$, against
$\Delta^{1/3}(D_3(u)+D_3(w))\sim\delta^{1/3}$. No violation. The bulk
contributes nothing ($q\approx0$ there). **So (4.3)-first remains OPEN and
(4.3)-second is refuted** — a strictly more informative outcome than the
note's "(4.3) OPEN, not refuted".

*Status of this refutation.* It is a scaling computation on an audited
family, not a completed proof: it assumes the two cell functionals differ,
which is generic and consistent with §5.1 but was not evaluated here. One
bounded computation settles it (see REOPENING CONDITION). I therefore record it
as a **refutation candidate with an explicit, cheap decision procedure**, and I
record the note's blanket "no scaling family violates (4.3)" as **unsupported**
regardless of how that computation comes out.

### B3 (minor, same proposition). The display in 4.2(iii)

From $|\Delta'|\le C(\nu(\Delta/\mathcal Q)^{1/3}+\Delta^{1/3})(D_3(u)+D_3(w))$
the note correctly derives
$(\Delta^{2/3})'\le\frac23C(1+\nu\mathcal Q^{-1/3})(D_3(u)+D_3(w))$ and then
displays
$\Delta(\tau)^{2/3}\le\Delta(0)^{2/3}+C\int_0^\tau(D_3(u)+D_3(w))dt$.
The displayed line is the $\nu$-free part only; the $\nu\mathcal Q^{-1/3}$
coefficient is disposed of by the sentence "large only where $\mathcal Q$ is
small (the harmless regime)", which is a judgement, not an estimate
($\mathcal Q^{-1/3}$ is unbounded a priori, and the reader has no lower bound
on $\mathcal Q$). The *conclusion* of 4.2(iii) is unaffected — any bound of
$\Delta'$ by dissipation integrates to a bound of $\Delta$ by $\int D_3\,dt$ —
but the display should be labelled as the $\nu$-free part, or the $\nu$-term
handled by Grönwall with $\nu\mathcal Q^{-1/3}$ carried.

---

## REPLACEMENT ARGUMENT

The repair is a sharpening of (1.1)–(1.2) which (a) is exactly what the
near-$\mathcal M$ behaviour requires, (b) fixes the monomial classification, and
(c) is what the numerics of §5.1 already exhibit ($\frac16\|q\|_3^3=0.0068$
against $\Delta=0.79$ — a factor $10^2$ of slack in the cube-root bound, whereas
$\frac14\int|w||q|^2$ is the right order).

> **Lemma R1 (sharp two-sided control of the Hodge defect by $\Delta$).**
> Let $u\in L^3(\mathbb R^3;\mathbb R^3)$, $q=q(u)$, $w=w(u)=u+q$, $A=j(w)$.
> Then
> $$\Delta(u)\;\ge\;\tfrac14\int_{\mathbb R^3}|w|\,|q|^2\,dx, \tag{R1a}$$
> and if in addition $u$ is solenoidal,
> $$\|A-j(u)\|_{3/2}\;\le\;C_1\,\Delta(u)^{1/2}\,\mathcal Q(u)^{1/6},
> \qquad C_1=\bigl(14\,(3+C_{\mathbb P})\bigr)^{1/2}3^{1/6}. \tag{R1b}$$
> (R1b) never exceeds the note's (1.2) by more than a fixed factor and improves
> it by $(\Delta/\mathcal Q)^{1/6}$; in particular it is strictly sharper in the
> near-$\mathcal M$ regime, where it is order-correct.

*Proof of (R1a).* By `lem:quotient-minimizer`(c), $\langle A,q\rangle=0$, so
$$\Delta(u)=F(u)-F(w)=\int\bigl(f(w-q)-f(w)+j(w)\cdot q\bigr)dx
=\int\!\!\int_0^1\bigl(j(w-\theta q)-j(w)\bigr)\cdot(-q)\,d\theta\,dx,$$
using $f\in C^1$ with $\nabla f=j$ (`lem:cubic-pointwise`). Apply the
*identity* half of `eq:cp-monotone` to the pair $a=w-\theta q$, $b=w$, so
$a-b=-\theta q$:
$$\bigl(j(w-\theta q)-j(w)\bigr)\cdot(-\theta q)
=\bigl(|w-\theta q|+|w|\bigr)\Bigl(\tfrac12\bigl(|w-\theta q|-|w|\bigr)^2
+\tfrac12\theta^2|q|^2\Bigr)\;\ge\;\tfrac12|w|\,\theta^2|q|^2 ,$$
where both discarded terms are nonnegative. Dividing by $\theta>0$ and
integrating $\int_0^1\tfrac12\theta\,d\theta=\tfrac14$ gives a nonnegative
integrand $\ge\tfrac14|w||q|^2$ pointwise; Tonelli permits the exchange. $\square$

*Proof of (R1b).* By `eq:cp-lipschitz`,
$|A-j(u)|=|j(w)-j(w-q)|\le(|w|+|w-q|)|q|\le(2|w|+|q|)|q|$. Write
$$\bigl((2|w|+|q|)|q|\bigr)^{3/2}
=\bigl[(2|w|+|q|)|q|^2\bigr]^{3/4}\,(2|w|+|q|)^{3/4}$$
and apply Hölder with exponents $\tfrac43$ and $4$:
$$\int|A-j(u)|^{3/2}\le\Bigl(\int(2|w|+|q|)|q|^2\Bigr)^{3/4}
\Bigl(\int(2|w|+|q|)^3\Bigr)^{1/4}.$$
For the first factor, (R1a) and the first inequality of (1.1) give
$\int(2|w|+|q|)|q|^2=2\int|w||q|^2+\int|q|^3\le8\Delta+6\Delta=14\Delta$.
For the second, Minkowski and $\|q\|_3\le(1+C_{\mathbb P})\|w\|_3$
(`lem:quotient-coercive`, solenoidal $u$) give
$\int(2|w|+|q|)^3\le(3+C_{\mathbb P})^3\|w\|_3^3=(3+C_{\mathbb P})^3\,3\mathcal Q$.
Hence
$\|A-j(u)\|_{3/2}^{3/2}\le(14\Delta)^{3/4}(3+C_{\mathbb P})^{3/4}(3\mathcal Q)^{1/4}$,
i.e. $\|A-j(u)\|_{3/2}\le(14(3+C_{\mathbb P}))^{1/2}\Delta^{1/2}(3\mathcal Q)^{1/6}$. $\square$

*Scaling.* $\Delta^{1/2}\mathcal Q^{1/6}\sim(a^{3/2},\lambda^0)(a^{1/2},\lambda^0)
=(a^2,\lambda^0)$, the weight of $\|A-j(u)\|_{3/2}$ — the same as (1.2), as it
must be. Comparison: (R1b)/(1.2) $=(\Delta/\mathcal Q)^{1/6}\le(C_{\mathbb P}^3-1)^{1/6}$.

**Consequences that replace §4.2.**

1. (4.1) becomes, with $C_\Delta':=C_1\Delta^{1/2}\mathcal Q^{1/6}$ in place of
   $C_\Delta=(1+C_{\mathbb P})(3\mathcal Q)^{1/3}(6\Delta)^{1/3}$:
   $$|P_3|\le C_\Delta'\|\nabla p\|_3,\quad |K|\le C_\Delta'\|(u\cdot\nabla)u\|_3,
   \quad |P_3-K|\le C_\Delta'\|\mathbb P[(u\cdot\nabla)u]\|_3,\quad
   |D_3(u)-D_3(w)|\le C_\Delta'\|\Delta u\|_3 .$$
   The right factors remain supercritical; the note's conclusion "exact but not
   a closing mechanism" is unchanged, now with the correct power of $\Delta$.
2. The monomial in the family $\alpha+\beta=\frac13$ that the defect bound
   actually delivers is $(\alpha,\beta)=(\frac12,-\frac16)$:
   $$|P_3-K|\;\le\;C\,\Delta^{1/2}\mathcal Q^{-1/6}\bigl(D_3(u)+D_3(w)\bigr) .
   \tag{4.3$'$}$$
   This, not (4.3), is the candidate the structure suggests. It survives the
   note's own two probes (near-$\mathcal M$: $\varepsilon$ against $\varepsilon$;
   high-frequency $u_0+\varepsilon h_k$: $\varepsilon+\varepsilon^2k$ against
   $\varepsilon(1+\varepsilon^2k^2)$, which holds for all $k$ by AM–GM) and it
   survives the HF18-B family ($\delta^{3/2}$ against $\delta^{1/2}$). It should
   replace (4.3)-first as the recorded open side-question.
3. The second half of (4.3) — and (4.3$'$)'s analogue for
   $|D_3(u)-D_3(w)|$ — is refuted by the HF18-B family as above and should be
   recorded as CLOSED-FALSE (pending the one cell computation), not OPEN.
4. §4.2(iii)'s non-closing conclusion is unaffected by any of this: inserting
   (4.3$'$) into (2.3) gives
   $|\Delta'|\le C(\nu+\mathcal Q^{1/3})\mathcal Q^{-1/6}\Delta^{1/2}(D_3(u)+D_3(w))$,
   hence $(\Delta^{1/2})'\lesssim(\ldots)(D_3(u)+D_3(w))$ and again a bound of
   $\Delta$ by the spacetime dissipation. The forbidden-inference display stands.

---

## "RETIRED AS A PRODUCER": THEOREM OR JUDGEMENT?

**Judgement, resting on two exact facts, with one overstated sentence.**

*Exact (theorem-grade):*
* $\Delta$ is not coercive on $u$: $\Delta(u)=0\iff u\in\mathcal M$
  (Prop. 1.2), and $\mathcal M$ contains nonzero compactly supported smooth
  solenoidal fields — the note's own elliptic swirl is one. So no bound on
  $\Delta$ alone bounds any norm of $u$.
* $\Delta$ is redundant given either audited functional: $\mathcal Q\le F(u)
  \le C_{\mathbb P}^3\mathcal Q$ and $F=\mathcal Q+\Delta$, so a bound on
  $\mathcal Q$ (the object of the FIRST GAP) bounds $F$ and hence $\Delta$, and
  conversely a bound on $\Delta$ alone bounds nothing. Remark 2(ii) states this
  correctly; it is the sharpest form of the obstruction.

*Judgement (not a theorem):*
* The abstract's "**Every** $\Delta$-weighted bound of $P_3-K$ or
  $D_3(u)-D_3(w)$ that is dissipation-controlled would integrate to a bound of
  $\Delta$ by $\int(D_3(u)+D_3(w))dt$" quantifies over an unspecified class.
  The supporting classification in §4.2 covers only exact monomials
  $\Delta^\alpha\mathcal Q^\beta D$, whereas the shape the programme actually
  needs — $\int_0^\tau K\,dt\le\theta\nu\int D_3+M\int\mathcal Q+A_{\rm input}$
  — is *not* a monomial (it carries $\nu$ and a dimensional $M$). The
  conclusion happens to survive for that shape too (any bound of $\Delta'$ by
  dissipation Grönwalls into a bound of $\Delta$ by $\int D_3\,dt$), but the
  note does not say so, and as written the "every" is broader than what is
  proved.
* "Two exact obstructions, no new producer": the *obstructions* (§3's two
  no-sign theorems, and non-coercivity) are exact. "No new producer" is a
  survey result over the candidates examined, not a non-existence theorem.

*Recommendation.* The retirement decision is sound and should stand; the
wording should be demoted from "exact obstruction: … no new producer" to
"exact obstruction: $\Delta$ vanishes on $\mathcal M\ne\{0\}$ and is redundant
given $\mathcal Q$; no producer found among the bounds surveyed".

---

## EVIDENCE

* Manuscript labels resolved and read at `39ccb66`: `def:D3P3` (main.tex:2677),
  `prop:pressure` (2799) with package (R1)–(R2) (2615), `prop:localtheory`
  (1195), `lem:cubic-pointwise` (4988), `lem:cubic-frechet` (5049),
  `lem:quotient-minimizer` (5118), `lem:quotient-coercive` (5454),
  `lem:quotient-stability` (5590), `prop:quotient-derivative` (5650),
  package (R1)–(R3) (5736), `lem:quotient-pressure` (5953),
  `lem:quotient-chainrule` (5996), `lem:qe-heat-continuity` (6069),
  `lem:heat-generator` (6126), `lem:quotient-heatsign` (6229),
  `prop:quotient-evolution` (6698).
* Recomputed by hand: Lemma 1.1's $\frac16$; both halves of (1.1); (1.2);
  every sign in (2.2)–(2.5); the Leray normalisation
  $(I-\mathbb P)[(u\cdot\nabla)u]=-\nabla p$ from $p=R_iR_j(u_iu_j)$;
  Corollary 2.3 by the quotient rule; $\|k_s\|_2=(8\pi s)^{-3/4}$ and
  $\|v_s\|_3\le(8\pi s)^{-1/4}\|u\|_2$; the Schwartz witness at $(0,1,0)$;
  every exponent and the constant $\frac3{2\sqrt2}SC_{CZ}$ in (4.2), including
  an independent derivation of the pointwise algebra
  $|\nabla V|^2-\frac19|\nabla|V||^2=|u||\nabla u|^2+|u||\nabla|u||^2$;
  the scaling lattice $\alpha+\beta=\frac13$; the orders of the HF18-B family.
* Recomputed symbolically, from scratch, in an independent script (sympy,
  curvilinear Laplacian in the Fermi frame, Cartesian components with
  $\theta'=\kappa$): $a\cdot\Delta a$, $(\Delta a)\cdot N$, and
  $R_2(a)+4\kappa\kappa_s\varphi^3/(1+\kappa d)^4\equiv0$. **(3.3) confirmed
  exactly**, independently of the note's `fermi_R.py`.
* Refutation attempts that FAILED (i.e. the note survived them):
  * parity $u\to-u$ against Theorem 2.2 — consistent, and it is the note's own
    §4.1(a);
  * near-$\mathcal M$ expansion against Prop. 1.2 — the second-order form
    $D^2f(z)[h,h]=|z||h|^2+(z\cdot h)^2/|z|$ is nondegenerate off $\{z=0\}$, so
    $\Delta\asymp\int|w||q|^2\asymp\varepsilon^2$ and $\|q\|_3\asymp\varepsilon$;
    (1.1)–(1.2) hold (lossily), and R1 is order-correct. No contradiction;
  * high-frequency perturbation against (4.3)-first — survives, and survives
    (4.3$'$) too;
  * heat-flow identity (3.2) against a shear flow / axisymmetric swirl in
    $\mathcal M$ — both sides vanish, consistent;
  * Theorem 3.2 against the possibility $\int_0^\infty$ diverging — the
    integrand is $O(s^{-7/4})$ at infinity, so it in fact converges absolutely;
  * Prop. 3.4 against the circle — $\kappa_s\equiv0$ gives $R_2\equiv0$, the
    correct degeneracy (azimuthal fields are heat-invariant in $\mathcal M$).
* Refutation attempt that SUCCEEDED: the HF18-B §2.3 family against
  (4.3)-second, above.
* Numerics in §5 were not re-run; they are declared as bounded evidence and are
  consistent with the theorems (§5.1's $D_3(w)/D_3(u)\in[0.978,0.994]$ is in
  fact the input the (4.3)-second refutation uses).

---

## CONDITIONAL SUFFIX THAT SURVIVES

Everything downstream of the first bad bridge survives, because the bad bridge
is in a *negative* section that discharges nothing.

* **Unconditional and new:** Theorem 2.2 (exact evolution
  $\Delta'+\nu(D_3(u)-D_3(w))=P_3-K$ with every term a pairing of the Hodge
  defect), Corollary 2.3, Lemma 3.1, **Theorem 3.2** (the heat-flow identity
  $\int_0^\infty(D_3(G_su)-D_3(w(G_su)))ds=\Delta(u)$, for solenoidal
  $u\in H^m$, $m\ge4$), Propositions 3.3–3.4 and Corollary 3.5 (both signs of
  $D_3(u)-D_3(w)$ occur, along a single heat trajectory), Prop. 4.1(a),(b),(c).
  Add Lemma R1 above.
* **Manuscript-grade by-product:** Lemma 2.1's upgrade of `prop:pressure`(ii)
  to $X\in C^1([0,T])$ with $D_3,P_3$ continuous.
* **Unchanged:** the HF17/HF18 conditional suffix. An input-only spacetime
  bound for $K$ (or for $P_3$, or for $P_3-K$ together with one for $K$) gives
  $\mathcal Q$, hence $\|u\|_3$ and $L^3_tL^9_x$, hence continuation by ESS.
  The FIRST GAP is untouched. Nothing in HF19-D moves it, and the note says so.
* **Newly closed (negatively):** the second inequality of (4.3), by the HF18-B
  family; the "strongest candidate" selection, replaced by (4.3$'$).

---

## UNNECESSARY DEPENDENCIES

* §2 does **not** need `prop:pressure`. Lemma 2.1 reproves the cubic balance in
  a stronger form from `lem:cubic-frechet` + (R1)–(R3) + HF18-A Thm 2 Step 3.
  The sentence "This is the pointwise form of `prop:pressure`(ii) … the $H^m$
  regularity of (R1) makes it pointwise" understates what was actually done and
  should not be read as a dependency.
* §3 does not need the approximate-gradient reading of $D_3(w)$; the note
  correctly declares that "$D_3(w)$" always means $-\langle A,\Delta u\rangle$.
* §3 does not need `lem:quotient-transport` or `prop:quotient-evolution` (only
  `prop:quotient-derivative` and `lem:heat-generator`).
* Remark 3(ii)'s formal linearisation is used nowhere and is correctly labelled
  heuristic. Remark 3(iii)'s explanation of the §5.1 sign ("the sign that (3.2)
  forces on average") is loose — the §5.1 fields do not sit on a heat trajectory
  — but is a remark about numerics, not a step.
* The constant-speed remark at the end of §4 ("No use was found") is honest and
  load-free.

---

## NON-CLAIMS OF THIS REVIEW

* No claim that (4.3)-second is refuted **as a proof**: the refutation is a
  scaling computation on an audited family, contingent on the two cell
  functionals of $G$ and $\mathbb PG$ differing. It is a refutation *candidate*
  with a decisive bounded test.
* No claim about (4.3)-first / (4.3$'$): OPEN, unrefuted by every family tried
  here.
* No claim that the difference route is or is not a producer as a theorem; only
  that the note's exact facts (non-coercivity, redundancy) are exact and its
  "every … bound" sentence is broader than what is proved.
* No re-audit of HF18-A Theorem 2, HF18-A (4.2), HF18-B Prop. 1.4/(1.6), or of
  any manuscript lemma; those were used as audited.
* No claim about the manuscript's checkpoint, `hyp:highstrain`,
  `prop:quotient-conditional`, or `lem:upgrade`; none of them is touched by
  HF19-D and none was re-audited.
* The §5 numerics were not reproduced.
* Cosmetic items, recorded but not weighed: the abstract says "for every smooth
  solenoidal $u\notin\mathcal M$" where Theorem 3.2 needs $u\in H^m$, $m\ge4$
  (§7 CLAIM AND SCOPE is correct); the §5.1 table prints the upper bound of
  (1.1) as $(\|w\|_3+\|q\|_3)\|q\|_3^2$ instead of $(\|w\|_3+\|u\|_3)\|q\|_3^2$;
  the §1 remark's "every axisymmetric swirl and every shear flow" should be
  restricted to decaying representatives, since $\mathcal M\subset L^3$.

---

## REOPENING CONDITION

The REPAIR verdict is settled — R1 and its consequences hold unconditionally.
The refutation of (4.3)-second reopens under exactly one condition:

> Evaluate, on one periodic cell of the HF18-B oscillatory profile
> $F=\bigl((2+\cos y_1)\cos y_2,\ \sin y_1\sin y_2,\ 0\bigr)$,
> $G=|F|^{-1/2}F$, the two cell integrals
> $\mathcal D[G]=\int_{\rm cell}|G|\bigl(|\nabla G|^2+|\nabla|G||^2\bigr)$ and
> $\mathcal D[\mathbb PG]$ with $\mathbb P$ the cell Leray projection.
> If $\mathcal D[\mathbb PG]\ne\mathcal D[G]$, (4.3)-second is FALSE and should
> be recorded as closed-negative. If they agree for this $G$ (a nongeneric
> coincidence), repeat with any other admissible profile; only if
> $\mathcal D[\mathbb PG]=\mathcal D[G]$ for *every* solenoidal-source profile
> — i.e. only if $\mathcal D$ were $\mathbb P$-invariant, which §5.1's own
> twelve fields already contradict — does (4.3)-second return to OPEN.

Secondary reopening: if a Navier–Stokes-side computation on the elliptic swirl
(the note's NEXT ACTION (1)) produces a nonzero Euler defect, the resulting
analytic family with $K\ne0$ and controlled $\|q\|_3/\|w\|_3$ should be run
against (4.3$'$) before that candidate is promoted.

---

## RECORD

**VERDICT:** REPAIR.
**REVIEWED SCOPE:** §§0–7 of `hf19-difference-functional.md` in full; every
displayed inequality recomputed for scaling; (3.3) re-derived independently by
hand and symbolically; the manuscript labels and the HF18-A/HF18-B inputs read
at the frozen revisions.
**FIRST BAD BRIDGE:** Proposition 4.2 — the unjustified selection of (4.3) as
"the strongest candidate" in the family $\alpha+\beta=\frac13$, and item (i)'s
unsupported "no scaling family violates (4.3)", whose second half is refuted
(scaling-heuristic) on the HF18-B §2.3 witness family.
**EVIDENCE:** as listed above; the decisive items are the independent symbolic
confirmation of (3.3), the independent verification of the pointwise algebra
behind (4.2), and the order table for the HF18-B family.
**REPLACEMENT ARGUMENT:** Lemma R1 ($\Delta\ge\frac14\int|w||q|^2$ and
$\|A-j(u)\|_{3/2}\le C_1\Delta^{1/2}\mathcal Q^{1/6}$), with proof; the
corrected candidate (4.3$'$)
$|P_3-K|\le C\Delta^{1/2}\mathcal Q^{-1/6}(D_3(u)+D_3(w))$; and the
closed-negative status of the $|D_3(u)-D_3(w)|$ half of (4.3).
**CONDITIONAL SUFFIX THAT SURVIVES:** all of §§1–3 and §4.1 unconditionally,
including the new heat-flow identity (3.2) and the two no-sign theorems; the
HF17/HF18 conditional suffix unchanged; the FIRST GAP untouched.
**UNNECESSARY DEPENDENCIES:** `prop:pressure` (§2 reproves a stronger
statement); the approximate-gradient reading of $D_3(w)$; `lem:quotient-transport`
and `prop:quotient-evolution` in §3; the formal linearisation of Remark 3(ii).
**NON-CLAIMS:** no proof-grade refutation of (4.3)-second; no verdict on
(4.3)-first / (4.3$'$); no non-existence theorem for a difference-route
producer; no re-audit of the imported HF18 results or manuscript lemmas; the
§5 numerics were not reproduced.
**REOPENING CONDITION:** the one-cell computation
$\mathcal D[\mathbb PG]$ vs $\mathcal D[G]$ specified above.
