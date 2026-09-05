# CP02-2 REVIEW: audit of `research/evidence/cp02-continuation.md` (round 1)

MODE: REVIEW with the proof-audit discipline. Date: 2026-09-05. Owner: audit
lane for CP02-2. File written: this one only. Nothing in the audited file, in
`main.tex`, or in any other evidence file was edited.

## 0. Frozen candidate

| item | value |
|---|---|
| audited file | `/home/ert/proj/navier/research/evidence/cp02-continuation.md` |
| sha256 | `c0f2bcd86b4e00c42eca7e63ab19cef9ec760adb8cec9ce75217b52950f153bf` |
| `git -C /home/ert/proj/navier rev-parse HEAD` | `715ce84ec78d64c510e150360a354b5d55648b9c` |
| manuscript compared against | `/home/ert/proj/navier-paper/main.tex`, 562 lines, read in full |
| records read in full | `research/evidence/cp01-manuscript-obligations.md`, `research/evidence/cp01-literature-statements.md` |

The author's own summary was treated as untrusted and is not relied on
anywhere below; every claim was reconstructed from the LaTeX block itself.

Primary sources opened **in this audit** (not taken from the candidate or from
the CP01 records):

* Escauriaza–Seregin–Šverák, *Russian Math. Surveys* **58**:2 (2003) 211–250,
  English translation PDF from
  `https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&paperid=609&what=fullteng&option_lang=eng`
  (10-page free portion, pp. 211–220; the URL needs a `Referer:` of
  `https://www.mathnet.ru/eng/rm609`, otherwise mathnet returns its
  "page not found" HTML). Pages **211, 212, 213, 214** read as page images.
* Rudin, *Real and Complex Analysis*, 3rd ed., McGraw–Hill 1987, pp. **80–83**
  read as page images.
* Lieb–Loss, *Analysis*, 2nd ed., AMS GSM 14, 2001, front matter and full
  **table of contents** (pp. ix–xv) read as page images.

---

## 1. VERDICT

**REPAIR.**

The block is, with one exception, a correct and genuinely self-contained proof
of C-0, of C-2 along the (D3) route, and of the assembly half of C-3. Every
identity, exponent and constant was recomputed independently and all of them
are right (details in §4). The single defect is a citation bridge that is
*logically circular as written* although its conclusion is true: the Sobolev
inequality is imported for the class $D^1(\R^3)$ and then applied to
$H^1(\R^3)$ on the strength of an asserted inclusion $D^1(\R^3)\supset
H^1(\R^3)$ which is itself the Sobolev embedding. This is exactly the
outstanding obligation **S-1** ("needs the H¹ version, i.e. density extension
of the $C^1_c$ inequality", cp01-manuscript-obligations §1.5, §4 Minor). A
complete three-line replacement, using only material already present in the
block, is given in §5. Nothing downstream changes; the constant
$C_*=\tfrac{256}{3125}C_S^3$ and the power $\nu^{-4}$ are unaffected.

## 2. REVIEWED SCOPE

Reconstructed from its first nontrivial implication and checked in full:

* the Conventions and Standard-facts preamble ((F1)–(F6), (R1)–(R4));
* `lem:nu-normalisation` (i)–(vi);
* `lem:hardy` (ray form of Hardy on $\R^3$, constant 2);
* `lem:solenoidal-density` (Biot–Savart potential, $\operatorname{curl}A=v$,
  cutoff, $W^1_2$ convergence);
* `lem:leray-hopf` Steps 0–6, against the **printed** ESS definition
  (1.3)–(1.7);
* `thm:ess` and `rem:ess-norm` (transcription fidelity);
* `lem:l3-to-l5`;
* `lem:serrin-enstrophy` Steps 1–4 (enstrophy identity, Hölder, interpolation,
  componentwise Sobolev, Plancherel, Young, Gronwall);
* `thm:continuation` and its equivalence/`ess sup` clause;
* `thm:conditional` Steps 1–5 against Fefferman (1)–(7);
* `rem:gkp`;
* LaTeX/interface consistency with `main.tex` (preamble, labels, `\newtheorem`,
  bib keys, retained-verbatim paragraphs).

Out of scope (untouched by the candidate and not audited here): `prop:energy`,
`prop:scaling`, `prop:enstrophy`, `prop:ode`, `prop:pressure`,
`prop:lowpressure`, `hyp:highpressure`, `hyp:absorption`, `sec:compactness`,
`sec:quotient`, the X-1 paragraph, and `prop:localtheory` itself.

## 3. FIRST BAD BRIDGE

**Standard fact (F3), as used in Step 2 of the proof of
`lem:serrin-enstrophy`.** The block writes

> (F3) *Sobolev inequality.* There is an absolute constant $C_S$ such that
> $\|g\|_6\le C_S\|\nabla g\|_2$ for every $g\in H^1(\R^3)$ (Lieb–Loss,
> *Analysis*, 2nd ed., Theorem 8.3, for the class $D^1(\R^3)\supset H^1(\R^3)$;
> $C_S=S_3^{-1/2}$ with $S_3=3(\pi/2)^{4/3}$).

and then applies it to $g_{ij}=\partial_ju_i\in H^1(\R^3)$.

Why the bridge fails. Lieb–Loss state Sobolev's inequality for gradients in
§8.3 (p. 202) for the class $D^1(\R^n)$ defined in §8.2 (p. 201) — confirmed
here at table-of-contents level: "8.2 Definition of $D^1(\R^n)$ and
$D^{1/2}(\R^n)$ … 201; 8.3 Sobolev's inequality for gradients … 202". Under the
book's definition ($f\in L^{2n/(n-2)}$ with distributional $\nabla f\in L^2$),
the asserted inclusion $H^1(\R^3)\subset D^1(\R^3)$ *is* the statement
$H^1(\R^3)\hookrightarrow L^6(\R^3)$, i.e. the conclusion being derived; the
step assumes what it proves. Under the alternative reading ($D^1$ = completion
of $C_c^\infty$ in the $\|\nabla\cdot\|_2$ seminorm) the inclusion is again not
immediate and needs the same density argument. The finding is therefore robust
to which definition Lieb–Loss actually uses — and the block itself flags E10 as
**[MO]**, so no reading of the primary text settles it either way.

Severity: the inequality is true, the constant is right, and the repair is
three lines. No other step in the block depends on the inclusion. The bridge is
nevertheless the first place where D5 ("no 'standard', 'well known', 'it is easy
to see' without the argument") is violated by an actual logical gap rather than
by an [MO] tag.

Nothing earlier fails. In particular the four bridges most exposed to this kind
of defect were checked and are sound: the $\nu$-normalisation algebra; the ray
form of Hardy with constant $2$; $\operatorname{curl}A=v$ under
$\xi\cdot\hat v=0$; and the vanishing of $\langle\Delta u,\nabla p\rangle$.

## 4. EVIDENCE

### 4.1 Source verification (all [DI] claims that carry weight)

**ESS (E1–E4) — confirmed verbatim, page by page.** The candidate's block
transcribes p. 212 and p. 214 correctly, including the two points where a
paraphrase would have changed the mathematics:

* p. 212, verbatim: "By a *Leray–Hopf weak solution* of the Cauchy problem
  (1.1), (1.2) in $Q_T$ we mean a vector field $v\colon\overline{Q_T}\to\R^3$
  such that". The **closure** $\overline{Q_T}$ is in the printed text. The
  candidate is right and `cp01-literature-statements` §3.1 is **wrong** on this
  point (it writes "`v : Q_T → R^3`"). This is a correction the integrator
  should carry back into the CP01 record; it is also what forces the endpoint
  construction in `lem:leray-hopf` Step 1, so the CP01 wording would have made
  that step look gratuitous.
* p. 212, (1.6) verbatim ends "$\forall\,t_0\in[0,T]$" — closed interval, so
  the endpoint value is required by the definition independently of the
  $\overline{Q_T}$ point.
* p. 212, definitions of $\dot C_0^\infty$, $\mathring J$, $\mathring J{}^1_2$,
  $Q_T=\R^3\times{]0,T[}$, and (1.3), (1.4), (1.5), (1.7): all four displayed
  conditions in the block agree with the printed text sign for sign, including
  $v\otimes v:\nabla w$ in (1.5) and the test class $\dot C_0^\infty(Q_T)$.
* p. 212 also carries "The definition still makes sense for $T=+\infty$ if we
  replace the closed interval $[0,T]$ by $[0,\infty[$ everywhere" and
  **Theorem 1.1** with (1.8) $a\in\mathring J$ — both reported correctly.
* p. 213, the mixed norm: the block's `eq:ess-norm` reproduces the printed
  two-case display exactly, including
  $\operatorname*{ess\,sup}_{t\in]0,T[}\|f(\cdot,t)\|_s$ for $l=+\infty$ and
  the sentence "If $s=l$, then we briefly write $\|f\|_{s,Q_T}$ instead of
  $\|f\|_{s,s,Q_T}$."
* p. 213, **Theorem 1.2** with (1.10) $\tfrac3s+\tfrac2l=1$,
  $s\in{]3,+\infty]}$ — as quoted in `rem:gkp`; $s=l=5$ does satisfy it.
* p. 214, **Theorem 1.3**, printed text: "Suppose that $v$ is a weak Leray–Hopf
  solution of the Cauchy problem (1.1), (1.2) in $Q_T$ and $v$ satisfies the
  additional condition (1.13). Then $v\in L_5(Q_T)$, and hence it is smooth and
  unique on $Q_T$." The block's `thm:ess` is **verbatim**.
* p. 214, the prose classical form before Theorem 1.3 is quoted verbatim, and
  the block's decision to import only the numbered theorem (because the prose
  fixes no solution class) is correct and is the same judgement as
  cp01-literature-statements §3.2.
* p. 211, (1.1)–(1.2) with unit viscosity — as quoted.

**Rudin (E11) — confirmed verbatim [DI].** 3rd ed., **Theorem 4.11 on p. 80**:
"Let $M$ be a closed subspace of a Hilbert space $H$. (a) Every $x\in H$ has
then a unique decomposition $x=Px+Qx$ into a sum of $Px\in M$ and $Qx\in
M^\perp$. (b) $Px$ and $Qx$ are the nearest points to $x$ in $M$ and in
$M^\perp$, respectively. (c) The mappings $P\colon H\to M$ and $Q\colon H\to
M^\perp$ are linear. (d) $\|x\|^2=\|Px\|^2+\|Qx\|^2$." **Theorem 4.12 on
p. 81**: "If $L$ is a continuous linear functional on $H$, then there is a
unique $y\in H$ such that $Lx=(x,y)$ ($x\in H$)." Both page numbers and both
quotations in the block are exact. The block's own derivation of
$(M^\perp)^\perp=M$ from 4.11 was rechecked and is valid.

**Lieb–Loss (E9, E10) — corroborated further than the block claims.** The
2nd-edition table of contents (read here) gives: "2.16 Approximation by
$C^\infty$-functions … 64", "2.19 Approximation by $C_c^\infty$-functions …
69", "8.2 Definition of $D^1(\R^n)$ and $D^{1/2}(\R^n)$ … 201", "8.3 Sobolev's
inequality for gradients … 202". So the section numbers **and page numbers**
used for E9 are right, and E10's "Theorem 8.3 = Sobolev's inequality for
gradients" is right as a *number*; only the constant and the exact class remain
unread. Independently: the block's $S_3=3(\pi/2)^{4/3}$ is algebraically
identical to the standard sharp value $\tfrac{n(n-2)}{4}|S^n|^{2/n}$ at $n=3$,
i.e. $\tfrac34(2\pi^2)^{2/3}$, since
$\tfrac34\cdot2^{2/3}\pi^{4/3}=3\cdot2^{-4/3}\pi^{4/3}$; numerically both
equal $5.4785\ldots$ So E10's constant is corroborated by an independent
computation even though the page was not read.

**Fefferman (E7).** Re-read from the CP01 verbatim block; (1)–(7) and
alternative (A) are used exactly as printed. Fefferman's (4) "for any $\alpha$
and $K$" is indeed the Schwartz condition.

**GKP (E6).** The `rem:gkp` quotation of Theorem 4 and of the following
$L_{3,\infty}$ sentence agrees word for word with the verbatim transcript in
cp01-literature-statements §2.2. Not load-bearing.

### 4.2 Independent recomputation (every number in the block)

All of the following were derived from scratch and agree with the block.

*$\nu$-normalisation.* $\partial_sv=\nu^{-2}(\partial_tu)$,
$(v\cdot\nabla)v=\nu^{-2}(u\cdot\nabla)u$, $\nabla q=\nu^{-2}\nabla p$,
$\Delta v=\nu^{-1}\Delta u=\nu^{-2}(\nu\Delta u)$; hence the unit-viscosity
equation. $q=R_iR_j(v_iv_j)$ from $v_iv_j=\nu^{-2}u_iu_j$ and linearity.
Energy transport: $\nu\int_0^{s/\nu}\|\nabla u\|_2^2\,d\tau
=\nu\cdot\nu^{-1}\!\int_0^s\|\nabla u(\sigma/\nu)\|_2^2 d\sigma
=\nu^2\!\int_0^s\|\nabla v\|_2^2 d\sigma$, and dividing the identity by $\nu^2$
gives (v) exactly. $\int_0^{S_*}\|v\|_5^5\,ds=\nu\cdot\nu^{-5}\int_0^{T_*}
\|u\|_5^5\,dt=\nu^{-4}\int_0^{T_*}\|u\|_5^5\,dt$ — the $\nu^{-4}$ is right.

*Hardy.* $F_\omega(r)=\int_r^\infty g_\omega\le r^{-1/2}M_\omega$ by
Cauchy–Schwarz with $\int_r^\infty s^{-2}ds=r^{-1}$;
$\frac{d}{dr}(rF^2)=F^2-2rFg$ gives
$\int_\alpha^RF^2=[rF^2]_\alpha^R+2\int_\alpha^R rFg$; dropping
$-\alpha F(\alpha)^2\le0$, bounding $RF(R)^2\le\int_R^\infty s^2g^2=
\varepsilon_R\to0$ and Cauchy–Schwarz on $\int rFg$ give
$X^2\le\varepsilon_R+2M_\omega X$, hence
$X\le M_\omega+\sqrt{M_\omega^2+\varepsilon_R}\to2M_\omega$. Constant $2$ is
the sharp $2/(n-2)$ at $n=3$; the hypothesis $A\to0$ is genuinely used (it
fails for $A\equiv c\ne0$, which is the natural attempted counterexample and is
correctly excluded).

*Biot–Savart.* $2\pi i\,\xi\times\hat A=-\xi\times(\xi\times\hat v)/|\xi|^2
=-(\xi(\xi\cdot\hat v)-|\xi|^2\hat v)/|\xi|^2=\hat v$ a.e. under
$\xi\cdot\hat v=0$. $\int_{\R^3}(1+|\xi|^2)^{-2}d\xi=4\pi\int_0^\infty
r^2(1+r^2)^{-2}dr=4\pi\cdot\tfrac\pi4=\pi^2$, so
$\int|\xi|^m|\hat v|\le\pi\|v\|_{H^{m+2}}$ (using
$|\xi|^{2m}(1+|\xi|^2)^{-(m+2)}\le(1+|\xi|^2)^{-2}$), and
$\int_{|\xi|<1}|\xi|^{-2}d\xi=4\pi$, giving
$\|\hat A\|_1\le(2\pi)^{-1}((4\pi)^{1/2}\|v\|_2+\pi\|v\|_{H^2})$. All three
numbers are as printed. $\|\nabla A\|_2^2\le\sum_j\int\xi_j^2|\hat v|^2/|\xi|^2
=\|v\|_2^2$. Reality of $A$ from $\hat A(-\xi)=\overline{\hat A(\xi)}$: correct.
Cutoff: $v_R-v=(\chi_R-1)v+\nabla\chi_R\times A$; on
$\{R\le|x|\le2R\}$, $|A|\le2R|A|/|x|$, so the four gradient error terms are
$O(\eta(R))$, $O(R^{-1})$, $O(R^{-1})$, $O(R^{-1})$ as claimed, and the
Hardy bound is indispensable (a mere $\|A\|_\infty$ bound gives
$R^{-1}\cdot R^{3/2}\to\infty$ on the annulus).

*Leray–Hopf verification.* Testing $\partial_sv+(v\cdot\nabla)v+\nabla q
-\Delta v=0$ against $w\in\dot C_0^\infty(Q_T)$ reproduces (1.5) term by term
with the printed signs, using $\int v_j(\partial_jv_i)w_i=-\int v_iv_j
\partial_jw_i$ (valid because $\partial_jv_j=0$) and $\int\nabla q\cdot w=
-\int q\,\nabla\!\cdot\!w=0$. The Lipschitz constant
$L_\varphi=\|a\|_2\|\Delta\varphi\|_2+\|a\|_2^2\|\nabla\varphi\|_\infty$ is
correct, and the $\varepsilon$/$L_\varphi$ splitting to general $w\in L_2$ via
$\Pi$ and density of $\dot C_0^\infty$ in $\mathring J$ is valid. $v_*\in
\mathring J$ via $(\mathring J^\perp)^\perp=\mathring J$, and
$\|v_*\|_2\le\liminf\|v(s)\|_2$, are both correct; (1.6) at $t_0=S_*$ then
follows from the monotone limit of the energy identity.

*Enstrophy identity.* $Y'=2\langle\nabla u,\nabla\partial_tu\rangle$;
Plancherel gives $\langle\nabla u,\nabla\partial_tu\rangle=
\operatorname{Re}\sum_{i,j}\int4\pi^2\xi_j^2\hat u_i\overline{(\partial_tu)^\wedge_i}
=-\langle\Delta u,\partial_tu\rangle$. The pressure term:
$\langle\Delta u,\nabla p\rangle=\operatorname{Re}\int4\pi^2|\xi|^2
\overline{\hat p}\,(\nabla\!\cdot\!u)^\wedge=0$ — rechecked including the
complex conjugation of $2\pi i\xi_i$, and the sign works out. Hence
$\tfrac12Y'+\nu\|\Delta u\|_2^2=\langle(u\cdot\nabla)u,\Delta u\rangle$.

*Exponents and constants.* $\tfrac15+\tfrac3{10}+\tfrac12=1$.
$\tfrac3{10}=\tfrac\theta2+\tfrac{1-\theta}6$ at $\theta=\tfrac25$; the Hölder
pair $(\tfrac32,3)$ applied to $f^{4/3}\cdot f^2$ gives
$\|\nabla u\|_{10/3}\le\|\nabla u\|_2^{2/5}\|\nabla u\|_6^{3/5}$.
$\|\nabla u\|_6^2=\|\sum g_{ij}^2\|_3\le\sum\|g_{ij}\|_6^2
\le C_S^2\|\nabla^2u\|_2^2$. Plancherel:
$\sum_{i,j,k}(2\pi\xi_j)^2(2\pi\xi_k)^2=(4\pi^2|\xi|^2)^2$, so
$\|\nabla^2u\|_2=\|\Delta u\|_2$. Young with $(\tfrac54,5)$:
$\tfrac45a^{5/4}=\nu\|\Delta u\|_2^2$ and
$\tfrac15b^5=\tfrac15(\tfrac4{5\nu})^4C_S^3\|u\|_5^5Y
=\tfrac{256}{3125}C_S^3\nu^{-4}\|u\|_5^5Y$, i.e.
$C_*=\tfrac{256}{3125}C_S^3$ — exactly as printed. Gronwall via
$(Ye^{-G})'\le0$ with $G_T=2C_*\nu^{-4}\int_0^T\|u\|_5^5$ gives
$\sup\|\nabla u\|_2\le\|\nabla u_0\|_2e^{G_T/2}
=\|\nabla u_0\|_2\exp(C_*\nu^{-4}\int_0^T\|u\|_5^5)$ — the halving of the
exponent is handled correctly. Finally
$\|u\|_{H^1}^2=\|u\|_2^2+(2\pi)^{-2}\|\nabla u\|_2^2$ is the exact identity for
the block's own convention $\|f\|_{H^k}=\|(1+|\xi|^2)^{k/2}\hat f\|_2$, and
$(2\pi)^{-2}<1$ is used only to simplify; correct.

*Pressure identification.* $R_iR_j$ has multiplier
$(-i\xi_i/|\xi|)(-i\xi_j/|\xi|)=-\xi_i\xi_j/|\xi|^2$; $-\Delta^{-1}
\partial_i\partial_j$ has multiplier
$-(-(4\pi^2|\xi|^2)^{-1})(-4\pi^2\xi_i\xi_j)=-\xi_i\xi_j/|\xi|^2$. Identical,
as (D1) and cp01-literature-statements §7.3 require. Consistent with
$-\Delta p=\partial_i\partial_j(u_iu_j)$ derived from `eq:NS` with
$\nabla\!\cdot\!u=0$.

### 4.3 Refutation attempts that failed (i.e. the steps held)

1. **Hardy with the wrong constant.** Attempted counterexample: drop $A\to0$
   and take $A\equiv c$. The block's hypothesis excludes it, and the printed
   constant $2$ is the sharp $2/(n-2)$ at $n=3$, so no constant-level
   refutation exists.
2. **Cutoff error in `lem:solenoidal-density` Step 3.** Attempted refutation:
   replace the Hardy bound by $\|A\|_\infty$. On $\{R\le|x|\le2R\}$ this gives
   $\|\nabla\chi_R\times A\|_2\lesssim R^{-1}\|A\|_\infty R^{3/2}=R^{1/2}
   \to\infty$, so the naive route genuinely fails — and the block does not take
   it. The Hardy detour is necessary, not decorative.
3. **Endpoint of `lem:leray-hopf`.** Attempted refutation: claim Step 1 is
   unnecessary because the ESS class is defined on the open cylinder. The
   printed text says $v\colon\overline{Q_T}\to\R^3$ and (1.4), (1.6) quantify
   over $t_0\in[0,T]$; Step 1 is required. Refutation fails.
4. **Preserved Schwartz decay in time**, which (D2) forbids. Every use of the
   branch's spatial decay was traced: `lem:solenoidal-density` and
   `lem:hardy` are applied to $v(s)\in\bigcap_kH^k$ and to the potential $A$
   built from it, never to a Schwartz field at $t>0$; $\mathcal S$ appears only
   at $t=0$ (`lem:nu-normalisation`(i), `thm:conditional`). No violation.
5. **Circularity through ESS.** Only the conclusion $v\in L_5(Q_T)$ of
   Theorem 1.3 is used; its "smooth and unique on $Q_T$" clause is explicitly
   not used, and the return path to the classical branch is the
   manuscript-owned `lem:serrin-enstrophy`. No circularity.
6. **Uniqueness smuggled in.** Searched for any implicit identification of $v$
   with "the" unit-viscosity branch for $(a,1)$: there is none; every lemma
   speaks about the transported branch itself. `rem:gkp` is the only place
   uniqueness is discussed, and only to explain why GKP Theorem 4 is *not*
   used. Clean.
7. **Sobolev on $H^1$.** This one **succeeded** — see §3.

## 5. REPLACEMENT ARGUMENT (complete)

Replace the standard fact (F3) by the following statement plus a lemma. This
uses nothing beyond what the block already establishes: the cutoff $\chi_R$ of
`lem:solenoidal-density` Step 3, the $L^1$-Fourier bound of Step 1 there, and
Fatou's lemma. Add `\newtheorem{lemma}[theorem]{Lemma}` (already required by the
block) — no further environment is needed. Insert `lem:sobolev-h1` immediately
before §"A Serrin-type enstrophy bound", and cite it in place of (F3) in
Step 2 of `lem:serrin-enstrophy`.

```latex
% --- REPLACES the item (F3) in the "Standard facts used" list -------------
\item[(F3)] \emph{Sobolev inequality for compactly supported fields.}
 There is an absolute constant $C_S$ such that
 $\norm g_6\leq C_S\norm{\nabla g}_2$ for every $g\in C_c^\infty(\R^3)$
 (Lieb--Loss, \emph{Analysis}, 2nd ed., Theorem~8.3, ``Sobolev's inequality
 for gradients'', stated there for the class $D^1(\R^3)$, which contains
 $C_c^\infty(\R^3)$ because a compactly supported bounded function lies in
 $L^6$ and its gradient in $L^2$; the sharp constant is
 $C_S=S_3^{-1/2}$ with $S_3=\tfrac{3}{4}(2\pi^2)^{2/3}=3(\pi/2)^{4/3}$).
 We do \emph{not} assume $H^1(\R^3)\subset D^1(\R^3)$: the extension of the
 inequality from $C_c^\infty$ to the fields we need is
 Lemma~\ref{lem:sobolev-h1}.

% --- NEW LEMMA, to be placed before the Serrin-type enstrophy bound -------
\begin{lemma}[Sobolev inequality on $\bigcap_kH^k$]\label{lem:sobolev-h1}
Let $f\in H^k(\R^3)$ for every integer $k\geq0$, with $f$ real-valued.  Then
$f\in L^6(\R^3)$ and
\[
 \norm f_6\leq C_S\norm{\nabla f}_2 ,
\]
with $C_S$ the constant of \textup{(F3)}.
\end{lemma}

\begin{proof}
\emph{Step 1: $f\in C^\infty$ with bounded derivatives.}  For every $m\geq0$,
the computation of Step~1 of the proof of
Lemma~\ref{lem:solenoidal-density}---Cauchy--Schwarz with the weight
$(1+|\xi|^2)^{-2}$, whose integral is $\pi^2$---gives
$\int_{\R^3}|\xi|^m|\hat f(\xi)|\,d\xi\leq\pi\norm f_{H^{m+2}}<\infty$.
Hence $(2\pi i\xi)^\alpha\hat f\in L^1$ for every multi-index $\alpha$, so by
differentiation under the integral sign \textup{(F5)} the function
$x\mapsto\int e^{2\pi ix\cdot\xi}\hat f(\xi)\,d\xi$ is in $C^\infty(\R^3)$ with
all derivatives bounded, and by \textup{(F1)(c)} (applicable since
$\hat f\in L^1\cap L^2$) it coincides with $f$ almost everywhere.  We identify
$f$ with this representative.

\emph{Step 2: truncation.}  Let $\chi_R$ be the cutoff of Step~3 of the proof
of Lemma~\ref{lem:solenoidal-density}: $\chi\in C_c^\infty(\R^3)$,
$0\leq\chi\leq1$, $\chi=1$ on $\{|x|\leq1\}$, $\chi=0$ on $\{|x|\geq2\}$, and
$\chi_R(x)=\chi(x/R)$, so $|\nabla\chi_R|\leq R^{-1}\norm{\nabla\chi}_\infty$.
Then $\chi_Rf\in C_c^\infty(\R^3)$, and \textup{(F3)} gives
\[
 \norm{\chi_Rf}_6\leq C_S\norm{\nabla(\chi_Rf)}_2
 \leq C_S\bigl(\norm{\chi_R\nabla f}_2+\norm{f\nabla\chi_R}_2\bigr)
 \leq C_S\Bigl(\norm{\nabla f}_2
 +\frac{\norm{\nabla\chi}_\infty}{R}\norm f_2\Bigr).
\]

\emph{Step 3: limit.}  $\chi_Rf\to f$ pointwise on $\R^3$ as $R\to\infty$, so
Fatou's lemma \textup{(F5)} applied to $|\chi_Rf|^6$ gives
$\norm f_6\leq\liminf_{R\to\infty}\norm{\chi_Rf}_6$.  Letting $R\to\infty$ in
the display of Step~2 yields $\norm f_6\leq C_S\norm{\nabla f}_2<\infty$; in
particular $f\in L^6$.
\end{proof}
```

and in Step 2 of the proof of `lem:serrin-enstrophy` replace

```latex
Sobolev: each component $g_{ij}=\partial_ju_i$ lies in $H^1$, so by (F3)
$\norm{g_{ij}}_6\leq C_S\norm{\nabla g_{ij}}_2$;
```

by

```latex
Sobolev: each component $g_{ij}=\partial_ju_i$ lies in $H^k(\R^3)$ for every
$k\geq0$ by (R1), so Lemma~\ref{lem:sobolev-h1} gives
$\norm{g_{ij}}_6\leq C_S\norm{\nabla g_{ij}}_2$;
```

Everything after this point in the block is unchanged: the interpolation, the
Plancherel identity $\norm{\nabla^2u}_2=\norm{\Delta u}_2$, the Young step, the
constant $C_*=\tfrac{256}{3125}C_S^3$, the power $\nu^{-4}$, `eq:serrin-bound`,
`thm:continuation` and `thm:conditional`.

Two remarks for the integrator. (i) After this repair, (F3) is invoked only for
$C_c^\infty$ fields, so the outstanding **S-1** obligation shrinks to pinning
Lieb–Loss Theorem 8.3's *statement and constant* by direct inspection; the
$H^1$-extension half of S-1 is discharged by `lem:sobolev-h1`. (ii) If the
estimates lane prefers a non-sharp $C_S$ from another source, only the numerical
value of $C_*$ changes.

## 6. CONDITIONAL SUFFIX THAT SURVIVES

With the §5 repair inserted, and given

* `prop:localtheory` delivering clauses (R1)–(R4) of (D2) (local-theory lane),
  and
* `prop:energy` (energy lane),

the following is proved by the block, for the unforced system on $\R^3$ with
arbitrary $\nu>0$ and divergence-free Schwartz datum, on the classical branch:

1. the $\nu$-normalised branch $v$ is a Leray–Hopf weak solution in the exact
   printed ESS sense (1.3)–(1.7) on every $Q_T$ with $T\le S_*=\nu T_*<\infty$,
   endpoint included;
2. $T_*<\infty$ and $\sup_{t<T_*}\|u(t)\|_3<\infty$ imply
   $u\in L^5(\R^3\times(0,T_*))$, via ESS Theorem 1.3 (the only imported
   theorem, its hypothesis class verified line by line against the printed
   definition, no uniqueness theorem imported);
3. $\int_0^T\|u\|_5^5<\infty$ implies
   $\sup_{t<T}\|\nabla u(t)\|_2\le\|\nabla u_0\|_2\exp\bigl(\tfrac{256}{3125}
   C_S^3\nu^{-4}\int_0^T\|u\|_5^5\bigr)$;
4. hence `thm:continuation` in the C-0 shape
   "$T_*<\infty\Rightarrow\sup_{0<t<T_*}\|u(t)\|_3=\infty$", with
   $\sup=\operatorname{ess\,sup}$ justified from $u\in C([0,T];L^3)$;
5. hence `hyp:critical` $\Rightarrow$ `def:target`, with Fefferman's (1), (2),
   (3), (5) [$f\equiv0$], (6), (7) each checked and the datum class (4)
   identified with $\mathcal S$.

The suffix imports **no** uniqueness statement for $L^3$ mild solutions, and the
case $T^*(a)>\nu T_*$ that blocked the old C-2 route does not arise. `hyp:critical`
remains an unproved hypothesis.

## 7. UNNECESSARY DEPENDENCIES

None found that could be removed without cost. Specifically:

* `lem:hardy` is used only inside `lem:solenoidal-density`, and refutation
  attempt 2 above shows it cannot be replaced by a boundedness bound.
* `lem:solenoidal-density` is needed because Galdi's characterisation of
  $\mathring J{}^1_2$ on $\R^3$ was not verifiable; proving it is the right
  call, and restricting it to $\bigcap_kH^k$ is the correct minimal scope.
* (F4) (Riesz representation) is used only in `lem:leray-hopf` Step 1; it could
  be replaced by weak-$*$ sequential compactness, but not more cheaply.
* `rem:gkp` and the `Kato1984` citation are decorative, as the brief requires
  ((g) and the retained-verbatim paragraph respectively).
* One genuine trim is available: the block's sentence "The existence theorem
  \cite[Theorem~1.1]{ESS2003} assumes $a\in\mathring J$ (their (1.8)); our
  datum will satisfy this" is beside the point, since Theorem 1.3 does **not**
  restate (1.8) (Theorem 1.2 does). Keep it, but say why: it shows the
  hypotheses under which Theorem 1.3 is applied here are at least as strong as
  those of its neighbours.

## 8. NON-CLAIMS (of this audit)

No HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION, or NS-R3 result is
asserted, approached, or judged closer. `hyp:critical`, `hyp:absorption` and
`hyp:highpressure` remain unproved hypotheses; `eq:quotient-gap` is untouched.
This audit does not verify `prop:localtheory`, `prop:energy`, `prop:pressure`,
`prop:lowpressure`, `prop:enstrophy`, `sec:quotient`, or the X-1 paragraph. No
claim is made that the audited block solves any part of the Millennium problem;
it is a conditional continuation section. Lieb–Loss Theorem 8.3's text
(statement and constant) and the definition of $D^1(\R^3)$ were **not** read in
the primary source by this audit either; the corroboration in §4.1 is a table
of contents plus an independent algebraic check of the constant. Stein–Weiss
Chapter I and Folland's theorem numbers were not opened. Galdi was not opened.

## 9. REOPENING CONDITION

Reopen this audit if any of the following changes:

1. `prop:localtheory` is written with a package weaker than (R1)–(R4) of (D2) —
   in particular if the normalised pressure is not included in the $C^j_tH^k$
   statement (used in `lem:nu-normalisation`(ii), `lem:leray-hopf` Steps 1 and
   4, and `lem:serrin-enstrophy` Step 1), or if the blow-up alternative is
   stated for a norm not equivalent to $H^1$;
2. the local-theory lane names its clauses other than (R1)–(R4), or splits
   (R2) differently — the block cites (R2) as that lane's C-3 smoothness lemma;
3. the estimates lane (S-1) pins a Sobolev source with a different class or
   constant, which changes $C_*$ (not the $\nu^{-4}$);
4. the pressure lane changes `eq:pressure-consequence` away from the integrated
   P-3 form used by the retained paragraph after `hyp:critical`;
5. the ESS translation pagination used here (pp. 211–214 of the *Russian Math.
   Surveys* English translation) is superseded by the Russian original's
   numbering, in which case all `\cite[p.~…]{ESS2003}` page numbers must be
   re-pinned.

## 10. MINOR EDITORIAL ISSUES FOR THE INTEGRATOR

1. **CP01 record correction (do this).** `cp01-literature-statements` §3.1
   states the ESS Leray–Hopf domain as "`v : Q_T → R^3`". The printed text is
   $v\colon\overline{Q_T}\to\R^3$ (p. 212). Fix the record; the candidate's
   block is the correct one.
2. `\dot C_0^\infty(Q_T)` is used by ESS in (1.5) but is **never defined in
   their paper** (only $\dot C_0^\infty$ on $\R^3$ is). The block presents its
   reading ("$x$-solenoidal, $C^\infty$, compact support in $Q_T$") inside the
   sentence that reports ESS's own conventions. Mark it explicitly as the
   block's (standard) reading of ESS's notation, so a referee is not misled
   into thinking it is quoted.
3. `lem:leray-hopf` Step 1 produces $v_*\in L_2$, i.e. an equivalence class,
   while ESS's definition asks for a map on $\overline{Q_T}$. Add "fix any
   Lebesgue representative of $v_*$" so that $v\colon\overline{Q_{S_*}}\to\R^3$
   is literally a function; (1.4) and (1.6) are unaffected by the choice.
4. `lem:nu-normalisation`(vi), last sentence: "the integrands are continuous on
   $[0,S)$, resp.\ $[0,T)$, for every $S<S_*$, $T<T_*$" — the intervals should
   read $[0,S]$ and $[0,T]$ (or the sentence should say "on $[0,S_*)$ and
   $[0,T_*)$"). Cosmetic.
5. The lemma title "Density of compactly supported solenoidal fields"
   over-promises: the statement is only for $v\in\bigcap_kH^k$. Retitle, e.g.
   "Smooth solenoidal fields lie in $\mathring J{}^1_2$", and keep the
   restriction visible in the statement.
6. `main.tex` line 51–52 (inside `premise:local`) still reads "Persistence of
   higher Sobolev regularity and uniqueness identify this branch with the
   maximal mild solutions used in the continuation theorem below." Under the
   (D3) route this sentence is **false as a description of the proof** and must
   be deleted or rewritten by the local-theory lane. Flag it so the two lanes do
   not both leave it standing.
7. The block drops the manuscript sentence "The backward-uniqueness proof is
   imported rather than reproduced here." That statement is still true and
   useful; reinstate it in `rem:ess-norm` or in the "Proof boundary" section.
8. "Proof boundary" (`main.tex` line 548ff) lists the manuscript-owned results.
   After integration it should also name the Serrin-type enstrophy bound
   `lem:serrin-enstrophy` and the Leray–Hopf membership `lem:leray-hopf`, which
   are now manuscript-owned and load-bearing.
9. `thm:ess` is an imported statement inside a `theorem` environment; its
   automatic number (e.g. "Theorem 5.7") sits next to the quoted "Theorem 1.3".
   The attribution line handles it, but consider `\begin{theorem}[ESS,
   Theorem~1.3]` plus an explicit "quoted, not proved here" sentence.
10. (F1)(b): for real $f,g\in L^2$ the $\operatorname{Re}$ in
    $\langle f,g\rangle=\operatorname{Re}\int\hat f\overline{\hat g}$ is
    redundant (the integral is automatically real). Harmless; keep or drop.
11. `lem:serrin-enstrophy` closing line uses the exact identity
    $\norm{u}_{H^1}^2=\norm u_2^2+(2\pi)^{-2}\norm{\nabla u}_2^2$, valid for the
    block's Fourier-weight convention. Since (R4) is a divergence statement it
    is convention-independent, but add half a sentence saying so, otherwise a
    referee has to check that `prop:localtheory` uses an equivalent $H^1$ norm.
12. `thm:conditional`, Step 3: "The force $f\equiv0$ trivially satisfies his
    (5)." Under Fefferman's alternative (A) the force is *given* as identically
    zero, so (5) is not a clause to verify. Reword to "alternative (A) fixes
    $f\equiv0$, so (5) is vacuous".
13. `thm:conditional`, opening: the equivalence "Fefferman's (4) for all
    $\alpha,K$ $\iff$ $u_0\in\mathcal S(\R^3)^3$" is asserted in one clause.
    Under (D5) give the two lines (both directions are immediate from
    $\sup_x(1+|x|)^K|\partial^\alpha f|<\infty$).
14. `rem:gkp`: "Applied to the normalised branch $v$ …, this corroborates
    Theorem~\ref{thm:continuation}" is loose, because GKP Theorem 4 speaks about
    $NS(a)$, not about $v$, and the identification is exactly what the remark
    goes on to say is missing. Reword to "…corroborates the *statement* of
    Theorem~\ref{thm:continuation} for the maximal $L^3$ branch with datum $a$".
15. Preamble: `\newtheorem{lemma}[theorem]{Lemma}` is required, as the block
    says. No `definition` environment is needed. All `\cite` keys used
    (`Tao2013`, `ESS2003`, `GKP2013`, `Fefferman2000`, `Kato1984`) exist in
    `/home/ert/proj/navier-paper/references.bib`. `\R`, `\norm` exist;
    `\operatorname*`, `\mathring`, `\mathbb C`, `\qedhere` are all available
    from the `amsmath`/`amssymb`/`amsthm` already loaded.
16. Label inventory checked against (D4): `prop:energy`, `prop:scaling`,
    `prop:enstrophy`, `prop:ode`, `prop:pressure`, `prop:lowpressure`,
    `hyp:highpressure`, `hyp:absorption`, `hyp:critical`, `thm:continuation`,
    `thm:conditional`, `def:target`, `premise:local`, `sec:quotient`,
    `eq:quotient-evolution`, `eq:quotient-gap` all still resolve after the
    splice; `eq:nu-normalization`, `eq:endpoint`, `eq:missing` are retained by
    the block. Structural verifier should pass.

17. **Concrete (R1)–(R4) alignment (checked against the local-theory lane's
    own draft, `research/evidence/cp02-local-theory.md`, read here only for
    interface purposes).** That lane states `prop:localtheory` with clauses
    (i)–(vi), not (R1)–(R4). The mapping the integrator should install is:
    (R1) $\to$ clause **(iii)** (Regularity: $u,p\in C^j([0,T];H^k)$ for all
    $j,k$, all $x$- and $t$-derivatives bounded on $[0,T]\times\R^3$) together
    with that lane's `cor:Lq` for the $L^q$-continuity consequences, $2\le
    q\le\infty$, which clause (iii) does **not** itself assert; (R2) $\to$ the
    proposition's preamble ("a unique pair $(u,p)$ of smooth functions on
    $[0,T_*)\times\R^3$") together with clause **(iv)** (equation pointwise,
    $\nabla\cdot u=0$, $p=R_iR_j(u_iu_j)$); (R3) $\to$ clause **(iv)**
    ($u(0,x)=u_0(x)$); (R4) $\to$ clause **(v)** (which gives the stronger
    $\lim_{t\uparrow T_*}\|u(t)\|_{H^1}=+\infty$, so the audited block's use
    of it is legitimate). Either renumber the block's clause list to
    (iii)/(iv)/(v) or add an explicit "we abbreviate
    Proposition~\ref{prop:localtheory}(iii),(iv),(v) and
    Corollary~\ref{cor:Lq} as (R1)--(R4)" sentence. Note in particular that
    the block's (R1) silently bundles the $L^q$ statement, which lives in a
    different result in that lane.
18. **The block's open item 4 is already covered elsewhere.** The audited file
    lists as not discharged: "Uniqueness of the normalised branch as 'the'
    unit-viscosity branch for datum $a=\nu^{-1}u_0$ is not asserted." The
    local-theory lane's `prop:localtheory` clause **(vi)** does assert exactly
    that ("the pair $(v,q)$ ... is the branch of $v_0$ for $\nu=1$, and
    $T_*(\nu,u_0)=\nu^{-1}T_*(1,\nu^{-1}u_0)$"). Nothing in the continuation
    section needs it, so no change is required; but the integrator should drop
    that item from the residual-obligation list rather than carry a
    non-obligation forward.
19. The block's `lem:nu-normalisation` overlaps the local-theory lane's
    `lem:nu-scaling` / `eq:nu-map` / clause (vi). The two must not both be
    stated; the integrator should keep whichever is cited more widely and have
    the other reference it. The block's version additionally transports the
    energy identity and the $\int\|v\|_5^5=\nu^{-4}\int\|u\|_5^5$ identity,
    which the local-theory version does not, so the likely resolution is to
    keep the block's items (v), (vi) as a short corollary of the lane's
    clause (vi).
20. Both `main.tex` label `eq:nu-normalization` (block) and the local-theory
    lane's `eq:nu-map` name the same substitution. Pick one; (D4) does not
    protect either name, but the block's is the one already in `main.tex`.

---

## 11. Obligations status after this audit

Discharged by the candidate (subject to the §5 repair):

* **C-0** — `thm:continuation` restated in the required shape, contrapositive
  displayed as `eq:endpoint`, $\operatorname{ess\,sup}\to\sup$ justified from
  $u\in C([0,T];L^3)$.
* **C-2** — replaced by the (D3) route and fully written: the ill-formed
  "uniqueness in the mild class identifies it with the maximal $L^3$ solution"
  sentence is gone, and with it the two blocking sub-items of
  cp01-manuscript-obligations §4 ("named uniqueness theorem", "case
  $T^*(v_0)>\nu T_*$"). The $\nu$-normalisation is now a lemma with the energy
  identity and the $H^1$ alternative transported.
* **C-3, assembly half** — Fefferman's clauses checked one by one.
* **§8 item 3** of the literature note — ESS p. 213 cited for
  $L_{3,\infty}=L^\infty_tL^3_x$.
* **N-1, partial** — the enstrophy identity
  $\tfrac12Y'+\nu\|\Delta u\|_2^2=\langle(u\cdot\nabla)u,\Delta u\rangle$ is
  written out from the exact memberships, reusable verbatim by the enstrophy
  lane; and the $\|\nabla^2u\|_2=\|\Delta u\|_2$ Plancherel step is supplied.
* **S-1, $H^1$-extension half** — only after the §5 repair is inserted.

Still open (unchanged by this audit):

* **C-3, the smoothness lemma** (Tao 5.4(iv) $\Rightarrow u,p\in
  C^\infty([0,T]\times\R^3)$) — owned by the local-theory lane, cited as (R2).
* **S-1, source half** — Lieb–Loss Theorem 8.3's statement and constant remain
  unread in the primary text ([MO] here too, corroborated only by the table of
  contents and by the algebraic identity
  $3(\pi/2)^{4/3}=\tfrac34(2\pi^2)^{2/3}$).
* **E8, E12** — Stein–Weiss Chapter I and Folland's theorem numbers remain
  [MO].
* Galdi Chapter III remains unverified and uncited.
* **P-3**, **X-1**, and everything in `sec:quotient` are untouched.

---

## 12. Frontier record

**MODE / RESULT.** REVIEW (proof audit), round 1, of
`research/evidence/cp02-continuation.md` at repository HEAD
`715ce84ec78d64c510e150360a354b5d55648b9c`. Result: **REPAIR** — one bad
citation bridge found and repaired in full; everything else in the block
survives verification, including all constants and exponents and the fidelity
of the single imported theorem.

**CLAIM AND SCOPE.** This audit claims only that the audited block, with the
three-line insertion of §5, is a complete proof of the five statements listed
in §6, conditional on `prop:localtheory` (R1)–(R4), on `prop:energy`, and on
the imported ESS Theorem 1.3. It claims nothing about any other section of the
manuscript and nothing about `hyp:critical` being provable.

**EVIDENCE.** ESS pp. 211–214 read directly as page images and compared
character by character with the block's transcriptions (all verbatim, including
$v\colon\overline{Q_T}\to\R^3$, (1.3)–(1.7), the mixed norm, Theorem 1.2's
LPS range, Theorem 1.3, and the unnumbered classical-form prose); Rudin RCA 3rd
ed. pp. 80–83 read directly (Theorems 4.11 p. 80 and 4.12 p. 81 confirmed
verbatim at the cited pages); Lieb–Loss 2nd ed. table of contents read directly
(§2.16 p. 64, §2.19 p. 69, §8.2 p. 201, §8.3 p. 202 confirmed). Independent
recomputation of the $\nu$-normalisation and its $\nu^{-4}$; of the Hardy
constant $2$ and its boundary terms; of $\int(1+|\xi|^2)^{-2}=\pi^2$,
$\int_{|\xi|<1}|\xi|^{-2}=4\pi$, $\|\nabla A\|_2\le\|v\|_2$ and
$2\pi i\,\xi\times\hat A=\hat v$; of every cutoff error in $W^1_2$; of the
Leray–Hopf test-function identity term by term against the printed (1.5); of
the enstrophy identity and $\langle\Delta u,\nabla p\rangle=0$; of
$\tfrac15+\tfrac3{10}+\tfrac12=1$, $\theta=\tfrac25$,
$\|\nabla^2u\|_2=\|\Delta u\|_2$, Young at $(\tfrac54,5)$ giving
$C_*=\tfrac{256}{3125}C_S^3$, and the Gronwall halving; of
$3(\pi/2)^{4/3}=\tfrac34(2\pi^2)^{2/3}=5.4785\ldots$. Seven refutation attempts,
six failed, one succeeded (§4.3).

**FIRST GAP.** Standard fact (F3): the Sobolev inequality is imported for
$D^1(\R^3)$ and applied to $H^1(\R^3)$ via an asserted inclusion
$D^1(\R^3)\supset H^1(\R^3)$ that is itself the Sobolev embedding. Repaired in
§5 by restricting (F3) to $C_c^\infty$ and adding `lem:sobolev-h1` (truncation
by the block's own $\chi_R$ plus Fatou). After the repair the first remaining
gap is documentary, not logical: Lieb–Loss Theorem 8.3's statement and constant
are still [MO]; behind that, Stein–Weiss (E8) and Folland (E12). The first
remaining *structural* dependency is clause (R2) of `prop:localtheory`.

**SURVIVING CONDITIONAL SUFFIX.** As in §6: given (R1)–(R4) and `prop:energy`,
`hyp:critical` $\Rightarrow$ `def:target`, through `lem:nu-normalisation`,
`lem:hardy`, `lem:solenoidal-density`, `lem:leray-hopf`, ESS Theorem 1.3,
`lem:l3-to-l5`, `lem:sobolev-h1`, `lem:serrin-enstrophy`, `thm:continuation`,
`thm:conditional`. One imported literature theorem; no imported uniqueness
theorem.

**NON-CLAIMS.** As in §8. In particular: no HIGH-PRESSURE, HIGH-STRAIN,
CRITICAL, ABSORPTION or NS-R3 result is asserted; no part of this audit brings
the Millennium problem nearer; Lieb–Loss 8.3, Stein–Weiss Ch. I, Folland
2.14–2.49 and Galdi Ch. III were not read in their primary texts by this audit;
GKP Theorem 4 is corroboration only.

**NEXT DISTINCT ACTION.** Return the block to lane CP02-2 (or hand it to the
integrator) with the §5 insertion applied and the fifteen editorial items of
§10 resolved; separately, the literature lane should read Lieb–Loss pp. 201–204
to upgrade E10 to [DI] and close the source half of S-1, and the CP01 record's
§3.1 domain typo ($Q_T$ vs $\overline{Q_T}$) should be corrected. Then round 2
of this audit need only re-check the inserted lemma and the local-theory lane's
clause names.
