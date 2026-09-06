# HF22-D: direct attack on (G), the frozen gap in product form

Lane HF22-D, MODE: DISCOVER (direct), 2026-09-06. **UNAUDITED.** Nothing here
is promoted, the manuscript is untouched, and this note owns exactly one file.
No HIGH-PRESSURE, HIGH-STRAIN, CRITICAL or NS-R3 result is asserted; the first
gap is unchanged and is **not** closed.

Inputs [DI]: `PLAN.md` ("Frontier packet", "Beyond the checkpoint", "HF18",
"HF20", "HF21", "Ordered next actions"); `../navier-paper/main.tex`
`sec:quotient` in full (`def:quotient`, `lem:cubic-pointwise`,
`lem:cubic-frechet`, `lem:quotient-minimizer`, `lem:gradient-closure`,
`lem:leray`, `lem:quotient-coercive`, `lem:quotient-scaling`,
`lem:quotient-heat`, `lem:quotient-stability`, `prop:quotient-derivative`,
`lem:quotient-pressure`, `lem:quotient-chainrule`, `lem:heat-generator`,
`def:qe-dissipation`, `lem:quotient-heatsign`, `lem:quotient-transport`,
`prop:quotient-evolution`, `lem:quotient-lowstrain`, `hyp:highstrain`,
`rem:highstrain-normalisation`, `rem:highstrain-scope`, `rem:distance-balance`,
`rem:no-monotone`, `prop:quotient-conditional`) and, outside it,
`prop:localtheory`, `lem:upgrade`, `prop:energy`, `prop:scaling` with
\eqref{eq:L4L3} and `rem:mismatch`, `def:sobolev-constant`, `def:D3P3`,
`prop:pressure`, `prop:lowpressure`, `hyp:highpressure`, `hyp:absorption`,
`lem:absorption-split`, `cor:absorption-consequence`, `thm:continuation`,
`hyp:critical`, `thm:conditional`; `hf18-hodge-regularity.md` with
`hf18-review-hodge-regularity.md` (PASS); `hf21-crossing-sign-structure.md`
with `hf21-review-crossing-sign-structure.md` (REPAIR, repairs applied);
`hf18-divergence-speed-link.md` with its two reviews (PASS after S1–S4), used
in exactly one display (§3.1) and load-bearing for nothing;
`hf21-shifted-hodge-regularity.md` with its audit (REPAIR, applied), read and
**not** used as a premise. Read but not premises: `hf19-*` (all unaudited),
`hf20-harmonic-strain-test.md` (audited; its content sits in `rem:no-monotone`).

---

## MODE / RESULT (summary)

**DISCOVER, direct. Result: (G) is not proved; four exact structural facts are
proved, and the natural first attempts are quantified rather than merely
declared to fail.**

1. **(G) in both routes (§1).** The pressure route has an exact mirror of the
   quotient route's product statement. Proved here: the unconditional
   identities \(P_3=\langle\operatorname{div}(|u|u),p\rangle
   =-\langle(I-\mathbb P)j(u),\nabla p\rangle\) (so \(P_3\), like \(K\),
   vanishes on the nonlinear-Hodge class), the coercivity
   \(D_3(u)\ge\frac{4}{5S^2}\|u\|_9^3\) of the *velocity's* dissipation, and
   the mirror size bound \(|P_3|\le C_{\rm pr}\|u\|_3D_3(u)\) with explicit
   \(C_{\rm pr}\), which reproduces the small-\(L^3\) theorem on the pressure
   route exactly as the audited \(|K|\le C_*\mathcal Q^{1/3}D_3(w)\) does on
   the quotient route. The mirror of (G) is
   \((\mathrm G_P)\ \int_0^\tau\|u\|_3D_3(u)\,dt\le A_{\rm input}\).
   **The pressure-route analogue is not easier.** Same scaling, same shape;
   the quotient route's scalar is pointwise the *smaller* one
   (\(\|q\|_3\le(1+C_{\mathbb P})\|u\|_3\)), and the two statements are not
   comparable only because the two dissipations are (audited non-claim). The
   audited ordering transfers the *flux* statements, not the product ones:
   \((\mathrm G_P)\Rightarrow(\mathrm G)\) holds **iff** HF21-B's sub-question
   (a) \(D_3(w)\le D_3(u)\) is affirmative. The low-frequency asymmetry
   ("free" on the quotient route, a genuine lemma on the pressure route) is
   bookkeeping: both low-frequency parts are input-bounded and neither touches
   the product statement.
2. **The exact deficit of the interpolation attempt (§2).** All audited
   input-only spacetime bounds for \(u\) lie on the single line
   \(\lambda(r,q):=\frac2r+\frac3q=\frac32\) — \(L^\infty_tL^2\),
   \(L^2_tL^6\), and \(L^4_tL^3\), the last being exactly the midpoint of the
   first two — and \(\lambda\) is affine under Hölder interpolation. The
   Serrin line is \(\lambda=1\). **The deficit is exactly \(\frac12\) and it is
   the same at every point of the hull**: there is no best interpolation and no
   partial progress. The coercivity puts \(u\) in \(L^3_tL^9\), which is
   \(\lambda=1\) exactly, but only with the norm \(\nu^{-1}(\mathcal Q(0)+\int K)\),
   i.e. the conclusion; interpolating it against the input line at weight
   \(\theta\) gives \(\lambda=\frac32-\frac\theta2\), so \(\theta=1\) is forced.
   Sharpest quantitative form: the Hölder split of \(\int d_1D_3(w)\) using
   \(\int_0^\tau d_1^s\,dt\le A_s\) demands \(u\in L^{3s'}_tL^9\),
   \(s'=\frac{s}{s-1}\), whose LPS value is \(1-\frac{2}{3s}\): **the split
   overshoots criticality by exactly \(\frac{2}{3s}\)** — \(\frac29\) at the
   audited \(s=3\), \(\frac16\) at the audited \(s=4\) — and reaches
   criticality only as \(s\to\infty\), where the distance factor becomes
   \(\sup_t\|q\|_3\), the conclusion itself. This is the exact numerical
   content of the audited obstruction O1.
3. **Closure of the time-integration-by-parts class (§3).** The audited record
   supplies exactly two functionals differentiable along the trajectory,
   \(\mathcal Q\) and \(F=\frac13\|u\|_3^3\) (\(d_1\) is only
   \(\tfrac12\)-Hölder in time, audited Remark 2.2 of HF21-B). Hence every
   exact time-integration by parts available is the chain rule for
   \(G(\mathcal Q,F,t)\), and it always weights \(\mathcal Q'=K-\nu D_3(w)\) by
   \(\partial_{\mathcal Q}G\) and \(F'=P_3-\nu D_3(u)\) by \(\partial_FG\).
   Three consequences, all exact: **(i) the weight of the dissipation always
   equals the weight of its own flux**, so weighting never improves absorption,
   only localises it; **(ii) a weight that is not a function of \(\mathcal Q\)
   alone necessarily activates the pressure flux \(F'\)** — this is why every
   localisation in the distance has fallen back on the pressure route, and it
   upgrades HF21-B §4.2's observation about one identity to a theorem about the
   whole family; **(iii) a weight that is a function of \(\mathcal Q\) alone
   absorbs exactly on \(\{C_*\mathcal Q^{1/3}\le(1-\varepsilon)\nu\}\), the
   audited Corollary-4 (Kato) region, which is forward invariant and already
   yields global regularity** — so it is empty of new content.
4. **The one surviving freedom, and a conditional reduction (§3.4).** Weights
   that depend on \(t\) through the trajectory escape (i)–(iii) at the cost of
   \(\operatorname{Lip}(\rho)\int_0^\tau\mathcal Q\,dt\), which is input-bounded
   by `rem:highstrain-normalisation`. This gives an exact conditional
   reduction: **if the good set admits a cutoff with input-only Lipschitz
   constant — equivalently, if \(t\mapsto\|q(t)\|_3\) has an input-only modulus
   of continuity at the level \(\nu/C_\sharp\) — then the good-set dissipation
   is input-bounded, settling the audited obstruction O3, and (G) reduces to
   its bad-set part alone.** The audited modulus (Hölder-\(\frac12\)) has
   constant containing \(\sup_t\|\partial_tu\|_3\) and is not input-only, so
   the hypothesis is open. A sharp-cutoff version instead costs
   \(2N_\tau\sup_{t<\tau}\mathcal Q\), where \(N_\tau\) is the **number of
   crossings** (connected components of the bad set); the audited crossing
   theorem bounds the bad set's *measure* uniformly in \(\tau\) but supplies no
   bound on \(N_\tau\). That is the exact price of the "cancelling signs at
   crossings" idea.

---

## 0. Setting, notation, audited inputs

\(u\) is the classical branch of `prop:localtheory` on \([0,T_*)\) from a
divergence-free Schwartz datum \(u_0\), \(\nu>0\), \(E_0:=\|u_0\|_2^2\);
package (R) of `subsec:qe-trajectories` holds on every compact
\([0,T]\subset[0,T_*)\), so \(u(t)\in H^m\), \(m\ge4\), solenoidal, and
\(u(t)\in C^\infty\) with \(p(t)\in C^\infty\), \(p,\nabla p\in L^3\)
(`prop:localtheory`(iii),(iv), `lem:upgrade`). Write
\(j(z)=|z|z\), \(F(v)=\frac13\|v\|_3^3\), \(\mathcal Q=\mathcal Q(u)\),
\(q=q(u)\), \(w=u+q\), \(A=j(w)\), \(V=|w|^{1/2}w\),
\(d_1=\|q\|_3\), \(d_2=F(u)-\mathcal Q(u)\ge0\),
\(d_3=\|\operatorname{div}(|u|u)\|_{3/2}\),
\(d_4=\|(I-\mathbb P)j(u)\|_{3/2}\) (HF21-B §1.1),
\(D_3(u)\) of `def:D3P3`, \(D_3(w)=D_{\mathcal Q}(u)\) of
`def:qe-dissipation` and HF18-A Theorem 2, \(P_3\) of `def:D3P3`,
\(K=\mathcal Q'+\nu D_3(w)\). \(\mathbb P\) is the Leray projection,
\(C_{\mathbb P}=C_3\), \(C_9\) its \(L^9\) bound, \(S\) the Sobolev constant
\(\|f\|_6\le S\|\nabla f\|_2\) (`def:sobolev-constant`; the manuscript writes
\(C_S\)), \(C_{\rm CZ}(r)\) the Calderón–Zygmund bound
\(\|R_iR_jf\|_r\le C_{\rm CZ}(r)\|f\|_r\), \(1<r<\infty\) (import (F5) and
\cite{Stein1970}, as in `subsec:quotient-conventions`).
\(\mathcal M=\{v\in L^3:\operatorname{div}(|v|v)=0\}\),
\(\mathcal M_{\rm sol}=\mathcal M\cap\{\operatorname{div}v=0\}\).
Scaling weights \((a,\lambda)\) as in HF21-B §1.4.

Audited facts used, all [DI]:

- (E1) `prop:quotient-evolution`: \(\mathcal Q\circ u\in C^1\),
  \(\mathcal Q'+\nu D_{\mathcal Q}(u)=K\), \(D_{\mathcal Q}\ge0\),
  \(K=-\int q\cdot((A\cdot\nabla)u)\), all integrands continuous in \(t\).
- (E2) `prop:pressure`(ii),(iii): \(\frac13X(t)-\frac13X(s)+\nu\int_s^tD_3(u)
  =\int_s^tP_3\), \(X=\|u\|_3^3\) continuous, \(D_3(u),P_3\) measurable and
  bounded on compact subintervals; \(D_3(u)\ge0\).
- (E3) `lem:quotient-coercive`: \(\mathcal Q\le F(u)\), \(\mathbb Pw=u\),
  \(\|u\|_3^3\le3C_3^3\mathcal Q\), \(\|q\|_3\le(1+C_3)\|w\|_3\), and
  \(\|w\|_3\le\|u\|_3\).
- (E4) `prop:energy`: \(\sup_t\|u\|_2^2\le E_0\),
  \(\int_0^{T_*}\|\nabla u\|_2^2dt\le E_0/(2\nu)\).
- (E5) `prop:scaling`(iii) \eqref{eq:L4L3}: \(\int_0^\tau\|u\|_3^4dt\le
  3S^2E_0^2/(2\nu)\), \(\tau\)-uniform; `rem:mismatch` for its supercriticality.
- (E6) `rem:highstrain-normalisation`: \(\int_0^\tau\mathcal Q\,dt\le
  \frac13H^{1/4}(3S^2E_0^2/2\nu)^{3/4}=:A_{\mathcal Q}(\nu,E_0,H)\) for
  \(\tau<\min\{H,T_*\}\), input-only; hence the Gronwall term and the
  Littlewood–Paley cutoff in `hyp:highstrain` are removable (HF21-B Cor. 4.4).
- (E7) HF18-A (audited PASS): \(V\in H^1\), \(\|V\|_2^2=3\mathcal Q\),
  \(A\in W^{1,3/2}\) with \(\nabla A=D\Phi(V)\nabla V\),
  \(D_{\mathcal Q}(u)=D_3(w)=\int(|\nabla V|^2-\frac19|\nabla|V||^2)\),
  \(\frac89\|\nabla V\|_2^2\le D_3(w)\le\|\nabla V\|_2^2\),
  \(\|w\|_9^{3/2}=\|V\|_6\le S\|\nabla V\|_2\), \(\|u\|_9\le C_9\|w\|_9\),
  \(D_3(w)\ge\frac{8}{9S^2C_9^3}\|u\|_9^3\); \(K=-\int q\cdot((u\cdot\nabla)A)\);
  \(|K|\le C_*\mathcal Q^{1/3}D_3(w)\), \(C_*=\frac32 3^{1/3}(1+C_3)C_9S\);
  Corollary 4 (Kato regime): \(C_*\mathcal Q(t_0)^{1/3}<\nu\) makes
  \(\mathcal Q\) nonincreasing for \(t\ge t_0\), hence \(T_*=\infty\).
- (E8) HF21-B (audited REPAIR, applied): Prop. 1.2
  \(\frac16d_1^3\le d_2\le(2+C_3)(3\mathcal Q)^{1/3}d_1^2\); Prop. 1.3
  \(\frac12d_1^2\le d_4\); Prop. 2.1 (distance balance)
  \(d_2'=P_3-K+\nu(D_3(w)-D_3(u))\) a.e., \(d_2\) absolutely continuous, which
  is `rem:distance-balance`; Prop. 3.1
  \(|K|\le C_\sharp d_1D_3(w)\), \(C_\sharp=\frac32C_9S\), and
  \(C_*=3^{1/3}(1+C_3)C_\sharp\); Lemma 4.3 \(\int_0^\tau d_1^3dt\le A_1\),
  \(\int_0^\tau d_1^4dt\le24S^2E_0^2/\nu=:A_1^{(4)}\); Thm. 4.5
  \(|\mathcal B_\tau|\le24S^2C_\sharp^4E_0^2\nu^{-5}\) uniformly in \(\tau\),
  \(\mathcal B_\tau=\{t<\tau:C_\sharp d_1>\nu\}\); Thm. 4.1 the exact identity
  \(\int_0^\tau K=d_2(0)-d_2(\tau)+\nu\int(D_3(w)-D_3(u))+\int P_3\);
  Remark 2.2 (\(d_1\) is only \(\frac12\)-Hölder in \(t\), never
  differentiated); obstructions O1, O2, O3.
- (E9) Manuscript non-claims kept: no inequality between \(D_3(w)\) and
  \(D_3(u)\) in either direction (`rem:distance-balance`,
  `rem:qe-heatsign-scope`); no sign for \(K(t)\) or \(P_3(t)\)
  (`rem:qe-evolution-scope`, `rem:no-monotone`).

**Target.** \((\mathrm G)\): \(\int_0^\tau\|q(t)\|_3D_3(w(t))\,dt\le
A_{\rm input}(\nu,u_0,H)\) uniformly for \(\tau<\min\{H,T_*\}\). By (E8)
Prop. 3.1 it implies \(\int_0^\tau K\le0\cdot\nu\int_0^\tau D_3(w)+C_\sharp
A_{\rm input}\), i.e. `hyp:highstrain` with \(\theta=0\), and by (E6) with no
Gronwall term and no cutoff; `prop:quotient-conditional` and
`thm:conditional` then give `def:target`.

---

## 1. (G) in both routes

### 1.1 The pressure flux is a distance pairing too

**Lemma 1.1 (mirror identities; unconditional).** For every \(t\in[0,T_*)\),
with \(\sigma_u:=\operatorname{div}(|u|u)=u\cdot\nabla|u|\in L^{3/2}\) (the
convention of `lem:integrands`, \(0\) on \(\{u=0\}\)):
\[
 \boxed{\ P_3=\langle\sigma_u,\,p\rangle=-\langle(I-\mathbb P)j(u),\,\nabla p\rangle,\ }
 \qquad\text{hence}\qquad
 |P_3|\le\min\{\,d_3\,\|p\|_3,\ d_4\,\|\nabla p\|_3\,\}.                 \tag{1.1}
\]
In particular \(P_3=0\) at every instant at which \(u(t)\in\mathcal M\), the
same class on which \(K=0\); and \(\int_0^\tau\|p\|_3\,dt\le
C_{\rm CZ}(3)S^2E_0/(2\nu)\) is input-only, uniformly in \(\tau<T_*\).

*Proof.* \(P_3=\int p\,W(u,\nabla u)=\int p\,u\cdot\nabla|u|\) by `def:D3P3`
(\((u\otimes u):\nabla u=|u|\,u\cdot\nabla|u|\)). For solenoidal \(u\in H^m\),
\(u\cdot\nabla|u|=\operatorname{div}(|u|u)\) a.e., and
\(|\sigma_u|\le|u||\nabla u|\in L^{3/2}\), so the first equality holds with
both factors paired in \(L^{3/2}\times L^3\) (\(p\in L^3\) by (R3)). For the
second, \(\langle\operatorname{div}j(u),p\rangle=-\langle j(u),\nabla p\rangle\)
(integration by parts, legitimate since \(j(u)\in L^{3/2}\cap W^{1,1}_{\rm loc}\)
and \(p,\nabla p\in L^3\); or by density of \(C_c^\infty\) in \(W^{1,3}\) with
the cutoff of `lem:quotient-pressure`), and
\(\langle\mathbb Pj(u),\nabla p\rangle=\langle j(u),\mathbb P\nabla p\rangle=0\)
because \(\nabla p\in\mathcal G_3\) (`lem:quotient-pressure`) and
\(\mathbb P\) annihilates \(\mathcal G_3\) (`lem:leray`(c)), using the duality
\(\langle\mathbb Pf,g\rangle=\langle f,\mathbb Pg\rangle\) for \(f\in L^{3/2}\),
\(g\in L^3\) recorded in HF21-B (Q4). The two Hölder bounds are immediate.
Vanishing on \(\mathcal M\) is Lemma 1.1 of HF21-B ((a)\(\iff\)(d)). For the
last claim, \(p=R_iR_j(u_iu_j)\) (`rem:qe-pressure-normalisation`), so
\(\|p\|_3\le C_{\rm CZ}(3)\|\,|u|^2\|_3=C_{\rm CZ}(3)\|u\|_6^2\le
C_{\rm CZ}(3)S^2\|\nabla u\|_2^2\), and (E4) integrates it. \(\square\)

This is the exact mirror of the quotient route's audited form
\(K_L=\int q\cdot\nabla\Pi_L=-\langle\operatorname{div}w,\Pi_L\rangle\)
(HF18-B (3.2), used here only as a comparison, not as a step): both fluxes are
a *pairing of a divergence-type distance with a pressure*, and both vanish
exactly on \(\mathcal M\). Scaling: \(d_3\sim(a^2,\lambda)\),
\(\|p\|_3\sim(a^2,\lambda)\), product \((a^4,\lambda^2)=P_3\) ✓;
\(d_4\sim(a^2,\lambda^0)\), \(\|\nabla p\|_3\sim(a^2,\lambda^2)\) ✓.

### 1.2 Coercivity and the mirror size bound

**Lemma 1.2 (coercivity of the velocity dissipation).** Let
\(W:=|u|^{1/2}u=\Phi(u)\), \(\Phi(z)=|z|^{1/2}z\). Then \(\Phi\in C^1(\mathbb R^3)\)
with \(D\Phi(z)h=|z|^{1/2}(h+\frac12(\hat z\cdot h)\hat z)\) and
\(D\Phi(0)=0\); \(W\in H^1(\mathbb R^3;\mathbb R^3)\) with
\[
 |\nabla W|^2=|u|\,|\nabla u|^2+\tfrac54\,|u|\,|\nabla|u||^2
 \quad\text{pointwise, so}\quad
 D_3(u)\le\|\nabla W\|_2^2\le\tfrac54D_3(u),                              \tag{1.2}
\]
and consequently
\[
 \boxed{\ \|u\|_9^3\le\tfrac54S^2D_3(u),\qquad\text{i.e.}\qquad
 D_3(u)\ \ge\ \tfrac{4}{5S^2}\,\|u\|_9^3 .\ }                             \tag{1.3}
\]

*Proof.* \(\Phi\) is smooth away from \(0\) with the stated derivative, and
\(|D\Phi(z)|\le\frac32|z|^{1/2}\to0\), so \(\Phi\in C^1\) with \(D\Phi(0)=0\);
hence \(W=\Phi\circ u\in C^1\) with \(\nabla W=D\Phi(u)\nabla u\). Then
\(|\partial_kW|^2=|u|\bigl(|\partial_ku|^2+\frac54(\hat u\cdot\partial_ku)^2\bigr)\)
and \(\hat u\cdot\partial_ku=\partial_k|u|\) a.e., which is (1.2) after summing
over \(k\) and comparing with
\(D_3(u)=\int(|u||\nabla u|^2+|u||\nabla|u||^2)\) of `def:D3P3` (the second
integrand being \(|(\nabla u)^{\mathsf T}u|^2/|u|\)). \(W\in L^2\) because
\(\|W\|_2^2=\|u\|_3^3<\infty\), and \(\nabla W\in L^2\) by (1.2) and
\(\|u\|_\infty<\infty\), \(\nabla u\in L^2\); so \(W\in H^1\) and
`lem:sobolev` gives \(\|u\|_9^{3/2}=\|W\|_6\le S\|\nabla W\|_2\). \(\square\)

(1.3) is the pressure-route mirror of the audited
\(D_3(w)\ge\frac{8}{9S^2C_9^3}\|u\|_9^3\) (E7), with a better constant and no
Leray factor, since no projection intervenes. It is elementary; no novelty is
claimed for it.

**Proposition 1.3 (mirror size bound).** For every \(t\in[0,T_*)\),
\[
 \boxed{\ |P_3|\ \le\ C_{\rm pr}\,\|u\|_3\,D_3(u),\qquad
 C_{\rm pr}:=\bigl(\tfrac54\bigr)^{1/2}S\,C_{\rm CZ}(9/4).\ }             \tag{1.4}
\]

*Proof.* By `def:D3P3`, \(|P_3|\le\int|p||u|^{1/2}\cdot|u|^{1/2}|\nabla|u||\)
and Cauchy–Schwarz give
\(|P_3|\le(\int p^2|u|)^{1/2}(\int|u||\nabla|u||^2)^{1/2}
\le(\int p^2|u|)^{1/2}D_3(u)^{1/2}\). Hölder with exponents
\((\frac98,9)\) gives \(\int p^2|u|\le\|p\|_{9/4}^2\|u\|_9\). Calderón–Zygmund
at \(r=\frac94\) and the interpolation \(\|u\|_{9/2}\le\|u\|_3^{1/2}\|u\|_9^{1/2}\)
(\(\frac29=\frac12\cdot\frac13+\frac12\cdot\frac19\)) give
\(\|p\|_{9/4}\le C_{\rm CZ}(9/4)\|u\|_{9/2}^2\le C_{\rm CZ}(9/4)\|u\|_3\|u\|_9\).
Hence \(|P_3|\le C_{\rm CZ}(9/4)\|u\|_3\|u\|_9^{3/2}D_3(u)^{1/2}\), and
\(\|u\|_9^{3/2}\le(\frac54)^{1/2}S\,D_3(u)^{1/2}\) by (1.3). \(\square\)

Scaling: \(\|u\|_3D_3(u)\sim(a^4,\lambda^2)=P_3\) ✓, so (1.4) is the unique
scaling-consistent monomial in \((\|u\|_3,D_3(u))\), exactly as (E7)'s
\(|K|\le C_*\mathcal Q^{1/3}D_3(w)\) is on the quotient side (HF18-A §4 item 1).

**Corollary 1.4 (consistency: Kato on the pressure route).** If
\(C_{\rm pr}\|u(t_0)\|_3<\nu\) at some \(t_0<T_*\), then \(t\mapsto\|u(t)\|_3\)
is nonincreasing for \(t\ge t_0\) on the classical interval and \(T_*=\infty\).

*Proof.* \(\frac13X'=-\nu D_3(u)+P_3\le-(\nu-C_{\rm pr}\|u\|_3)D_3(u)\le0\)
wherever \(C_{\rm pr}\|u\|_3\le\nu\); the continuity argument of HF18-A
Corollary 4 (with \(X\in C([0,T_*))\), `prop:pressure`(iii)) propagates it, and
`thm:continuation` closes. \(\square\)

This is Kato's small-\(L^3\) theorem again and claims nothing new; it is the
check that the constant chain of Proposition 1.3 is not lossy in amplitude —
the same check HF18-A Corollary 4 performs for the quotient route.

### 1.3 The two product statements, side by side

By (E8) Prop. 3.1 and Proposition 1.3 above, each route's flux is bounded by
(critical scalar) \(\times\) (its own dissipation), and each route therefore has
one minimal product statement sufficient for its gap with \(\theta=0\):
\[
 (\mathrm G)\quad \int_0^\tau\|q\|_3\,D_3(w)\,dt\le A_{\rm input},
 \qquad\qquad
 (\mathrm G_P)\quad \int_0^\tau\|u\|_3\,D_3(u)\,dt\le A_{\rm input}.      \tag{1.5}
\]
\((\mathrm G)\Rightarrow\) `hyp:highstrain` with \(\theta=0\) (E8, E6);
\((\mathrm G_P)\Rightarrow\) `hyp:absorption` with \(\theta=0\) by (1.4), hence
`hyp:critical` by `cor:absorption-consequence`(ii) and `def:target` by
`thm:conditional`.

| | quotient route | pressure route |
|---|---|---|
| flux | \(K=-\langle\operatorname{div}w,\Pi_{u,A}\rangle\) (HF18-B (3.2)) | \(P_3=\langle\operatorname{div}(|u|u),p\rangle\) (Lemma 1.1) |
| vanishes on \(\mathcal M_{\rm sol}\) | yes | yes |
| size bound | \(|K|\le C_*\mathcal Q^{1/3}D_3(w)\) (E7) | \(|P_3|\le C_{\rm pr}\|u\|_3D_3(u)\) (1.4) |
| refined scalar | \(d_1=\|q\|_3\) (E8), critical, vanishes on \(\mathcal M\) | \(d_4\), critical and vanishing on \(\mathcal M\), but paired with \(\|\nabla p\|_3\) (Rem. 1.7) |
| scalar's input control | \(\int d_1^4dt\le A_1^{(4)}\), \(\tau\)-uniform (E8) | \(\int\|u\|_3^4dt\le3S^2E_0^2/2\nu\) (E5) |
| dissipation coercive | \(D_3(w)\ge\frac{8}{9S^2C_9^3}\|u\|_9^3\) (E7) | \(D_3(u)\ge\frac{4}{5S^2}\|u\|_9^3\) (1.3) |
| dissipation input-bounded | no | no |
| low-frequency part | free, by (E6) | `prop:lowpressure`, a genuine lemma |
| product statement | \((\mathrm G)\) | \((\mathrm G_P)\) |
| scaling of the product | \((a^3,\lambda^0)\) | \((a^3,\lambda^0)\) |

**Proposition 1.5 (the comparison, exactly).**
1. Both statements of (1.5) have the scaling of \(\mathcal Q\),
   \((a^3,\lambda^0)\), so an input-only right side is scaling-consistent for
   both, with the same admissible monomials \(E_0^x\nu^yH^z\),
   \(2x+y-z=3\), \(x+2z=0\) (HF21-B §4.5).
2. The quotient scalar is pointwise the smaller one:
   \(d_1\le(1+C_{\mathbb P})\|w\|_3\le(1+C_{\mathbb P})\|u\|_3\) by (E3), and it
   vanishes on \(\mathcal M\) whereas \(\|u\|_3\) does not.
3. Nevertheless \((\mathrm G_P)\Rightarrow(\mathrm G)\) is **not** available:
   it holds if and only if the two integrands can be compared, i.e. it follows
   from HF21-B's open sub-question (a), \(D_3(w)\le D_3(u)\) pointwise in \(t\),
   and no inequality between the two dissipations is audited in either
   direction (E9). Under (a), \((\mathrm G_P)\Rightarrow(\mathrm G)\) with
   constant \(1+C_{\mathbb P}\).
4. The audited ordering (`rem:highstrain-scope`, HF21-B Cor. 4.2)
   transfers the *flux* statements — `hyp:absorption` \(\Rightarrow\)
   `hyp:highstrain` with \(A_{\rm input}=A+\frac13\|u_0\|_3^3\) — and says
   nothing about (1.5): a bound on \(\int P_3\) is not a bound on
   \(\int\|u\|_3D_3(u)\), because only one inequality direction is available.

*Proof.* 1 is the table of HF21-B §1.4 together with
\(D_3(u)\sim(a^3,\lambda^2)\) (`def:D3P3` under `prop:scaling`(i)). 2 is (E3).
3 is immediate and is exactly the missing comparison. 4 is the cited results.
\(\square\)

**Answer to the lane's question (1): the pressure-route analogue is not
easier.** The two product statements are mirror images with identical scaling
and identical shape; the quotient route's scalar is pointwise smaller and
vanishes on \(\mathcal M\), which is the entire content of "the distance
replaces the critical norm"; and no implication runs between them without
HF21-B sub-question (a). The asymmetry that motivated the question — that
`prop:lowpressure` is a genuine estimate while the quotient's low-frequency
work is free (E6) — is bookkeeping and does not reach the product statements:
both low-frequency parts are input-bounded (one from `prop:scaling`(iii), one
from the band-limited kernel bound), and in both routes the open part is the
high-frequency/product statement. Two further remarks make the "not easier"
verdict quantitative.

**Remark 1.6 (a coarser pressure chain is strictly lossy).** Using the
input-bounded factor of Lemma 1.1 instead of (1.4):
\(|P_3|\le\|p\|_3d_3\le\|p\|_3\|u\|_3^{1/2}D_3(u)^{1/2}\) by HF21-B (1.3), so
Young's inequality absorbs the dissipation with no smallness at all and leaves
\[
 \int_0^\tau P_3\,dt\le\tfrac{\theta\nu}2\int_0^\tau D_3(u)\,dt
 +\tfrac1{2\theta\nu}\int_0^\tau\|p\|_3^2\|u\|_3\,dt .                     \tag{1.6}
\]
This is a genuine structural advantage of the pressure route — the quotient
route's audited bounds carry \(D_3(w)\) to the *first* power, so no Young
absorption is available there without smallness of \(d_1\). But the residual is
worse than critical: by \(\|p\|_3\le C_{\rm CZ}(3)S^2\|\nabla u\|_2^2\) and
\(\|u\|_3\le(3S^2E_0)^{1/4}\|\nabla u\|_2^{1/2}\) (\eqref{eq:L4L3-constant} with
(E4)), the residual is controlled by \(\int_0^\tau\|\nabla u\|_2^{9/2}dt\),
i.e. by \(\nabla u\in L^{9/2}_tL^2_x\); the critical demand for \(\nabla u\) in
\(L^r_tL^2_x\) is \(r=4\) (the exponent \(2-\frac3q-\frac2r\) vanishes at
\(q=2\), \(r=4\)) and the audited input is \(r=2\). So (1.6) overshoots
criticality by half an exponent and undershoots the input by \(\frac52\); the
route through \(\|p\|_3\) is lossy, which is precisely why
`prop:lowpressure` uses \(\|p_{\le J}\|_\infty\le C2^{3J}E_0\) at the cost of a
length scale instead.

**Remark 1.7 (what the mirror does *not* give).** Lemma 1.1 exhibits a critical
distance on the pressure side, \(d_4\), but pairs it with \(\|\nabla p\|_3\),
for which no input bound exists at any exponent
(\(\|\nabla p\|_3\lesssim\|u\|_\infty\|\nabla u\|_3\) is Serrin-type). The
scale-invariant pairing therefore has its unbounded factor on the pressure
side, and the non-invariant pairing \(d_3\|p\|_3\) has it on the distance side.
Each route has exactly one factor with an input-only time bound and never
both, and in each route the factor without one is the one carrying the
dissipation. This is the structural statement of the impasse, and it is
identical on both sides.

### 1.4 What (G) is, at its quantifiers

**Proposition 1.8 (existential equivalence; scope, not progress).** Consider,
at the quantifiers of `hyp:highstrain` (for every \(\nu>0\), every
divergence-free Schwartz \(u_0\), every \(0<H<\infty\), with one finite
\(A_{\rm input}\) valid for all \(0<\tau<\min\{H,T_*\}\)):
(A) \((\mathrm G)\); (B) \((\mathrm G_P)\); (C) `hyp:highstrain`;
(D) `hyp:absorption`; (E) `hyp:highpressure`; (F) \(T_*=\infty\) for every
datum. Then (A)–(F) are equivalent.

*Proof.* (A)\(\Rightarrow\)(C)\(\Rightarrow\)(F) is (E8) Prop. 3.1 with (E6),
`prop:quotient-conditional`, `thm:conditional`. (B)\(\Rightarrow\)(D) is (1.4),
and (D)\(\Rightarrow\)(F) is `cor:absorption-consequence`(ii) with
`thm:conditional`. (E)\(\iff\)(F) is `prop:existential-equivalence`, and
(E)\(\Rightarrow\)(D) is `lem:absorption-split`. For (F)\(\Rightarrow\)(A) and
(F)\(\Rightarrow\)(B): if \(T_*=\infty\) then \([0,H]\) is a compact classical
interval, on which \(t\mapsto d_1(t)\) is continuous (`lem:quotient-stability`
with \(u\in C([0,H];L^3)\)), \(t\mapsto D_3(w(t))=D_{\mathcal Q}(u(t))\) is
continuous (`lem:quotient-heatsign`), and \(t\mapsto\|u\|_3\), \(D_3(u)\) are
continuous resp. bounded measurable (`prop:pressure`(i),(iii)); so both
integrands are integrable on \([0,H]\) and \(A_{\rm input}:=\int_0^H(\cdot)\,dt\)
is finite and depends only on \((\nu,u_0,H)\). \(\square\)

So (G) is not a technical lemma: like `hyp:highstrain` and `hyp:highpressure`
it is, at these quantifiers, *equivalent* to the Clay conclusion, and its
converse direction supplies no method (`rem:highstrain-scope`). Two scope
consequences that the record should carry:

- **(G) is strictly stronger than the frozen gap along a fixed trajectory.**
  \((\mathrm G)\Rightarrow\) `hyp:highstrain`, but the converse per trajectory
  is not available: only \(|K|\le C_\sharp d_1D_3(w)\) is audited, one
  direction, and \(K\) may vanish where \(d_1D_3(w)\) does not (\(K\) is a
  contraction of \(S(u)\) against \(\hat w\otimes\hat w\), HF18-B (3.6), which
  vanishes on a codimension-one set of strains). Proving (G) therefore proves
  more than the gap needs. The PLAN's phrase "the frozen gap is exactly (G)"
  should be read as the audited HF21-B statement — (G) with \(\theta=0\)
  suffices, and no cutoff or Gronwall term is needed — not as an equivalence
  per trajectory.
- The equivalence of Proposition 1.8 means the question "which route is
  easier" cannot be settled by implications; it can only be settled by the
  shape of the estimates available, which §1.3 does.

---

## 2. The interpolation attempt, and its exact deficit

This section answers "how far short does the audited integrated information
fall from a Serrin exponent", once and for all, with numbers.

Write \(\lambda(r,q):=\frac2r+\frac3q\) for \(u\in L^r_tL^q_x\). Under
\(u\mapsto u_\lambda\) of `prop:scaling`(i), \eqref{eq:LPS} gives
\(\|u_\lambda\|_{L^r_tL^q_x}=\lambda^{1-\lambda(r,q)}\|u\|_{L^r_tL^q_x}\); the
Ladyzhenskaya–Prodi–Serrin class is \(\lambda(r,q)=1\), \(q>3\), and
\(1-\lambda\) is the scaling exponent computed in `rem:mismatch`.

**Proposition 2.1 (the audited input hull is one segment of \(\lambda=\frac32\)).**
The audited input-only spacetime bounds for \(u\) are
\[
 \|u\|_{L^\infty_tL^2}\le E_0^{1/2},\qquad
 \|u\|_{L^2_tL^6}\le S\Bigl(\frac{E_0}{2\nu}\Bigr)^{1/2},\qquad
 \|u\|_{L^4_tL^3}\le\Bigl(\frac{3S^2E_0^2}{2\nu}\Bigr)^{1/4},
\]
(E4) with `lem:sobolev`, and (E5). All three have \(\lambda=\frac32\); the
third is the \(\theta=\frac12\) Hölder interpolant of the first two, so the
audited information about \(u\) is exactly the segment
\(\{(\frac1r,\frac1q)=(\frac\theta2,\frac{1-\theta}2+\frac\theta6):\theta\in[0,1]\}\).
Moreover \(\lambda\) is affine along Hölder interpolation
(\(\|u\|_{L^{r_\theta}L^{q_\theta}}\le\|u\|_{L^{r_0}L^{q_0}}^{1-\theta}
\|u\|_{L^{r_1}L^{q_1}}^{\theta}\) with \(\frac1{r_\theta},\frac1{q_\theta}\)
the convex combinations), so **every** interpolant of the audited inputs has
\(\lambda=\frac32\).

*Proof.* \(\lambda(\infty,2)=\frac32\), \(\lambda(2,6)=1+\frac12=\frac32\),
\(\lambda(4,3)=\frac12+1=\frac32\). For the midpoint claim, \(\theta=\frac12\)
gives \(\frac1r=\frac14\), \(\frac1q=\frac14+\frac1{12}=\frac13\); this is
exactly the route by which \eqref{eq:L4L3} is proved (`lem:interp` with
`prop:energy`). Affineness of \(\lambda\) is immediate from the two convex
combinations. \(\square\)

**Corollary 2.2 (the deficit is exactly \(\frac12\), everywhere on the hull).**
No interpolation of the audited inputs lies in any LPS class: each is exactly
\(\frac12\) above the Serrin line in \(\lambda\), equivalently each scales like
\(\lambda^{-1/2}\). There is no best choice and no partial progress: the
deficit is a constant of the input, not of the interpolation. To reach
\(\lambda=1\) by interpolating the hull with a further space of LPS value
\(\lambda_*\) at weight \(\theta\) one needs
\((1-\theta)\frac32+\theta\lambda_*=1\), i.e. \(\lambda_*\le1\) and
\(\theta\ge\frac{1}{2(3/2-\lambda_*)}\); with the best conceivable critical
\(\lambda_*=1\) this forces \(\theta=1\), the additional space alone.

**Proposition 2.3 (where the ninth power actually lives).** The audited
coercivity (E7) and Lemma 1.2 give
\(\|u\|_9^3\le\frac{9S^2C_9^3}8D_3(w)\) and \(\|u\|_9^3\le\frac54S^2D_3(u)\),
and \(\lambda(3,9)=\frac23+\frac13=1\) exactly. So the ninth-power space is
*critical*, not supercritical — but it is available only against
\(\int_0^\tau D_3(w)\,dt\) resp. \(\int_0^\tau D_3(u)\,dt\), for which the only
identities are (E1) and (E2):
\[
 \nu\int_0^\tau D_3(w)\,dt=\mathcal Q(0)-\mathcal Q(\tau)+\int_0^\tau K\,dt,
 \qquad
 \nu\int_0^\tau D_3(u)\,dt=F(0)-F(\tau)+\int_0^\tau P_3\,dt .
\]
Both right sides contain exactly the open flux integral. Hence: **the audited
integrated coercivity does not place \(u\) in an integrated ninth-power space;
it states that the (unbounded) dissipation integral *would* place it there,
and that statement is the conclusion**. By Corollary 2.2 no interpolation with
the input hull recovers any part of it: the conditional critical space must be
used at full weight \(\theta=1\).

**Proposition 2.4 (the exact overshoot of the Hölder split; sharpening of the
audited O1).** Suppose \(\int_0^\tau d_1^s\,dt\le A_s<\infty\) is available for
some \(s\in[1,\infty]\) (audited: \(s=3\) and, \(\tau\)-uniformly, \(s=4\),
by (E8) Lemma 4.3). Then Hölder in time gives
\[
 \int_0^\tau d_1D_3(w)\,dt\le A_s^{1/s}\Bigl(\int_0^\tau D_3(w)^{s'}dt\Bigr)^{1/s'},
 \qquad s'=\tfrac{s}{s-1},
\]
and by (E7) the finiteness of the last factor implies
\(u\in L^{3s'}_tL^9_x\), whose LPS value is
\[
 \lambda(3s',9)=\frac{2}{3s'}+\frac13=\frac{2(s-1)}{3s}+\frac13
 =1-\frac{2}{3s} .                                                        \tag{2.1}
\]
So the split demands a **strictly subcritical** space for every finite \(s\),
overshooting the Serrin line by exactly \(\frac{2}{3s}\):
\(\frac29\) at \(s=3\), \(\frac16\) at \(s=4\), and \(\to0\) only as
\(s\to\infty\), where the hypothesis degenerates to
\(\sup_{t<\tau}\|q(t)\|_3<\infty\), which by (E3) is equivalent to
\(\sup_{t<\tau}\|u(t)\|_3<\infty\) — the conclusion itself
(`hyp:critical`). This is the audited obstruction O1 with its exact numerical
size, and it is unchanged if \(d_1\) is replaced by \(\|u\|_3\) and \(D_3(w)\)
by \(D_3(u)\) via (1.3)–(1.4): the pressure route overshoots by the same
\(\frac2{3s}\) with the same audited \(s=4\).

**Summary of §2.** The three numbers are: the input hull sits at
\(\lambda=\frac32\) (deficit \(\frac12\), uniform); the target sits at
\(\lambda=1\); and the natural Hölder split lands at \(1-\frac2{3s}\), i.e.
*past* the target, for every exponent the audited record supplies. The natural
first attempt therefore fails not by a little and not by an unquantified
amount: at the audited \(s=4\) it demands \(u\in L^4_tL^9_x\) (and at \(s=3\), \(u\in L^{9/2}_tL^9_x\)), which is
strictly stronger than Serrin, while the inputs give a space that is
\(\frac12\) weaker than Serrin.

---

## 3. Integration by parts in time: the whole class, and where it closes

### 3.1 The transport term is exactly a difference of cubic fluxes

**Lemma 3.1 (first order in the distance, exactly).** Put
\(T(v):=|v|\,v\otimes v\) and \(S(u)=\frac12(\nabla u+\nabla u^{\mathsf T})\).
At every \(t\in[0,T_*)\),
\[
 \boxed{\ K=-\int_{\mathbb R^3}\bigl(T(w)-T(u)\bigr):S(u)\,dx\ },
 \qquad |T(w)-T(u)|\le3\bigl(|w|+|u|\bigr)^2|q| .                        \tag{3.1}
\]
In particular \(K=0\) whenever \(q=0\), and the integrand vanishes pointwise
where \(w=u\).

*Proof.* HF18-B Prop. 3.1 (audited PASS) gives the strain form
\(K=-\int|w|\,w\cdot S(u)\,w=-\int T(w):S(u)\), no derivative of \(w\) or \(q\)
being taken. For solenoidal \(u\in H^m\),
\(\int T(u):S(u)=\int|u|u_iu_j\partial_iu_j=\int u\cdot\nabla\frac{|u|^3}3=0\)
(`lem:div-zero`; the integrand is \(L^1\) since \(|u|^3\in W^{1,1}\)).
Subtract. For the pointwise bound, \(T\) is \(C^1\) with
\(DT(v)h=(\hat v\cdot h)v\otimes v+|v|(h\otimes v+v\otimes h)\), so
\(|DT(v)|\le3|v|^2\); integrate along the segment from \(u\) to \(w\).
\(\square\)

(3.1) is a one-line consequence of an audited identity and is recorded only to
make "odd and first order in the distance" exact and unconditional: the flux is
the *difference* between the cubic momentum flux of the representative and that
of the velocity, contracted with the strain, and it changes sign with \(q\).
Nothing below depends on it; it is the motivation for §3.2 and is not a step
in any proof there.

### 3.2 Every exact time-integration by parts, and its invariant

By `lem:quotient-chainrule` and `prop:pressure`, exactly two scalar functionals
of the trajectory are differentiable in time at the audited level:
\(\mathcal Q(t)\in C^1\) and \(F(t)=\frac13\|u(t)\|_3^3\), absolutely
continuous with \(F'=P_3-\nu D_3(u)\) a.e. by (E2). The distance \(d_1\) is
only \(\frac12\)-Hölder and is never differentiated (E8, Remark 2.2), and
\(d_2=F-\mathcal Q\) is a function of the two. Hence:

**Theorem 3.2 (closure of the class, and the weight invariant).** Let
\(G\in C^1(\mathbb R_{\ge0}^2\times[0,H])\) and put \(m:=\partial_1G\),
\(n:=\partial_2G\), evaluated at \((\mathcal Q(t),F(t),t)\). Then
\(t\mapsto G(\mathcal Q(t),F(t),t)\) is absolutely continuous on every compact
\([0,\tau]\subset[0,T_*)\) and
\[
 \boxed{\ G\bigl|_0^\tau=\int_0^\tau\Bigl[\partial_tG
 +m\bigl(K-\nu D_3(w)\bigr)+n\bigl(P_3-\nu D_3(u)\bigr)\Bigr]dt .\ }      \tag{3.2}
\]
Equivalently
\[
 \nu\int_0^\tau\!\bigl[mD_3(w)+nD_3(u)\bigr]dt
 =G(0)-G(\tau)+\int_0^\tau\!\partial_tG\,dt
 +\int_0^\tau\!\bigl[mK+nP_3\bigr]dt .                                     \tag{3.3}
\]
Consequences.
1. **(Weight invariance.)** The weight of \(D_3(w)\) equals the weight of
   \(K\), and the weight of \(D_3(u)\) equals the weight of \(P_3\), for every
   \(G\). Consequently, absorbing the quotient flux against the quotient
   dissipation through the audited \(|K|\le C_\sharp d_1D_3(w)\) requires
   \(C_\sharp d_1\le(1-\varepsilon)\nu\) **on the support of \(m\)** and
   nowhere else: weighting can localise the absorption but never improve it.
2. **(Forced pressure coupling.)** \(n\equiv0\) holds iff \(G\) is independent
   of its second argument, iff \(m\) is a function of \((\mathcal Q,t)\) alone.
   Hence *any* weight for the quotient balance that depends on the distance
   (equivalently on \(F\), equivalently on \(d_2\)) activates the pressure
   flux \(P_3\) with a weight \(n\not\equiv0\).
3. **(The \(\mathcal Q\)-only weights are empty.)** If \(m=m(\mathcal Q)\ge0\)
   is Lipschitz with \(\operatorname{supp}m\subset[0,\mathcal Q_0]\) and
   \(C_*\mathcal Q_0^{1/3}\le(1-\varepsilon)\nu\), then (3.3) gives
   \(\varepsilon\nu\int_0^\tau m(\mathcal Q)D_3(w)\,dt\le
   \int_0^{\mathcal Q(0)}m\le\min\{\mathcal Q(0),\mathcal Q_0\}\); but the
   admissible region \(\{C_*\mathcal Q^{1/3}\le(1-\varepsilon)\nu\}\) is
   exactly the audited Corollary-4 (Kato) region of (E7), which is forward
   invariant and on which \(T_*=\infty\) already holds. The bound is therefore
   true and empty.

*Proof.* Absolute continuity: \(\mathcal Q\in C^1\), \(F\) is absolutely
continuous by (E2), both have compact range on \([0,\tau]\), and \(G\) is
\(C^1\) hence Lipschitz there; the chain rule for absolutely continuous
functions gives \(\frac{d}{dt}G=\partial_tG+m\mathcal Q'+nF'\) a.e., and
\(\mathcal Q'=K-\nu D_3(w)\) (E1), \(F'=P_3-\nu D_3(u)\) (E2). All four
integrands are in \(L^1(0,\tau)\): \(K,D_3(w)\) are continuous (E1),
\(P_3,D_3(u)\) are bounded measurable (E2), and \(m,n,\partial_tG\) are bounded
on the compact range. Integrating gives (3.2), and (3.3) is a rearrangement.
1 is read off (3.3). 2: \(n=\partial_2G\equiv0\) iff \(G=G(\mathcal Q,t)\), and
then \(m=\partial_1G\) is a function of \((\mathcal Q,t)\); conversely if
\(m\) depends on \(F\) then \(\partial_2\partial_1 G\ne0\), so \(\partial_2G\)
is not identically zero. 3: with \(G(x)=\int_0^xm\), (3.3) reads
\(\nu\int m(\mathcal Q)D_3(w)=G(\mathcal Q(0))-G(\mathcal Q(\tau))
+\int m(\mathcal Q)K\); on \(\operatorname{supp}m\) one has
\(C_\sharp d_1\le C_*\mathcal Q^{1/3}\le(1-\varepsilon)\nu\) by (E3) and
\(C_*=3^{1/3}(1+C_3)C_\sharp\) (E8), so
\(\int m K\le(1-\varepsilon)\nu\int mD_3(w)\); \(G\ge0\) and \(G\) is
nondecreasing. The identification of the region with (E7) Corollary 4 is the
identity \(C_\sharp(1+C_3)3^{1/3}=C_*\). \(\square\)

**Reading.** Theorem 3.2 is a closure statement, not an estimate: it says that
the *entire* stock of exact time-integrations by parts available from the
audited record is (3.2), and that in every member the dissipation one wants to
bound carries the same weight as the flux one cannot sign. The three known
members are \(G=\mathcal Q\) (the quotient balance), \(G=F\) (the pressure
balance) and \(G=F-\mathcal Q\) (the distance balance
`rem:distance-balance`, whose integrated form is HF21-B Theorem 4.1); the
theorem says nothing else exists. Consequence 2 explains, at the level of the
mechanism rather than case by case, why every attempt to localise near
\(\mathcal M\) has landed on the pressure route: HF21-B §4.2 observed this for
the single identity (4.1); here it is a property of the whole family.

**Corollary 3.3 (the exact price of a distance cutoff).** Let
\(\varphi:[0,\infty)\to[0,1]\) be Lipschitz, nonincreasing, \(\varphi=1\) on
\([0,y_0]\), \(\varphi=0\) on \([2y_0,\infty)\), and take
\(G(\mathcal Q,F)=\mathcal Q\,\varphi(F-\mathcal Q)\), so that
\(m=\varphi-\mathcal Q\varphi'\ge0\) and \(n=\mathcal Q\varphi'\le0\). If
\[
 y_0\ \le\ \frac{(1-\varepsilon)^3\nu^3}{12\,C_\sharp^3}
 \qquad\text{(so that }C_\sharp d_1\le C_\sharp(6\cdot2y_0)^{1/3}\le(1-\varepsilon)\nu
 \text{ on }\{d_2\le2y_0\}\text{ by (E8) Prop. 1.2)},
\]
then
\[
 \varepsilon\nu\int_{\{t<\tau:\ d_2(t)\le y_0\}}\!\!D_3(w)\,dt
 \ \le\ \mathcal Q(0)\ +\ \int_0^\tau\mathcal Q(t)\,|\varphi'(d_2(t))|\,
 \bigl(\nu D_3(u)-P_3\bigr)(t)\,dt
 \ =\ \mathcal Q(0)-\int_0^\tau\mathcal Q\,|\varphi'(d_2)|\,F'\,dt .       \tag{3.4}
\]
The residual is supported in the transition layer \(\{y_0\le d_2\le2y_0\}\),
carries the weight \(\mathcal Q|\varphi'|\ (\approx\mathcal Q/y_0)\), and is
exactly the pressure-route balance: it has no sign, and no input bound for it
is available (it contains \(\sup_t\mathcal Q\) as a factor as soon as
\(\int|\varphi'(d_2)|\,|F'|\,dt\) is estimated crudely). Letting
\(\varphi'\to0\) removes the residual and also the localisation.

*Proof.* Insert \(G\) into (3.3), note \(G(\tau)\ge0\),
\(G(0)\le\mathcal Q(0)\), and absorb \(\int mK\le(1-\varepsilon)\nu\int mD_3(w)\)
using \(m\ge\varphi\ge0\), \(\operatorname{supp}m\subset\{d_2\le2y_0\}\) and
the displayed smallness; \(d_1\le(6d_2)^{1/3}\) is (E8) Prop. 1.2. Finally
\(n(P_3-\nu D_3(u))=\mathcal Q\varphi'F'\). \(\square\)

Corollary 3.3 is the concrete new integration by parts the lane asked for. Its
content is negative and exact: the good-set localisation *does* work
inside the layer \(\{d_2\le y_0\}\) — with \(y_0\) a critical-smallness
threshold on the *distance*, not on the norm, so the layer contains fields of
arbitrarily large \(\|u\|_3\) (HF21-B §3.3) — but the price is a transition
term which is precisely the pressure flux, weighted by the unknown
\(\mathcal Q\). Theorem 3.2(2) says this price is unavoidable for any state
weight.

### 3.4 The one freedom left: time weights, and a conditional reduction

A weight that depends on \(t\) through the trajectory rather than through the
state escapes Theorem 3.2(2) — it is not of the form \(G(\mathcal Q,F)\) — and
its cost is exactly one term, which the audited record can pay.

**Proposition 3.4 (time-weighted quotient balance).** Let
\(\rho:[0,\tau]\to[0,1]\) be Lipschitz with constant \(\Lambda\). Then
\[
 \nu\int_0^\tau\rho\,D_3(w)\,dt
 \ \le\ \mathcal Q(0)+\Lambda\!\int_0^\tau\!\mathcal Q\,dt+\int_0^\tau\rho K\,dt
 \ \le\ \mathcal Q(0)+\Lambda A_{\mathcal Q}(\nu,E_0,H)+\int_0^\tau\rho K\,dt, \tag{3.5}
\]
with \(A_{\mathcal Q}\) the input quantity of (E6). If moreover
\(\operatorname{supp}\rho\subset\mathcal G^\varepsilon_\tau
:=\{t<\tau:\ C_\sharp\|q(t)\|_3\le(1-\varepsilon)\nu\}\), then
\[
 \varepsilon\nu\int_0^\tau\rho\,D_3(w)\,dt\ \le\
 \mathcal Q(0)+\Lambda\,A_{\mathcal Q}(\nu,E_0,H).                        \tag{3.6}
\]

*Proof.* Multiply \(\mathcal Q'+\nu D_3(w)=K\) (E1) by \(\rho\), integrate,
and integrate by parts:
\(\int\rho\mathcal Q'=\rho(\tau)\mathcal Q(\tau)-\rho(0)\mathcal Q(0)
-\int\rho'\mathcal Q\), all terms finite (\(\mathcal Q\in C^1\), \(\rho\)
Lipschitz). Drop \(\rho(\tau)\mathcal Q(\tau)\ge0\), use \(\rho(0)\le1\),
\(|\rho'|\le\Lambda\) a.e. and \(\mathcal Q\ge0\); (E6) bounds
\(\int_0^\tau\mathcal Q\). For (3.6) use \(\rho K\le C_\sharp\rho d_1D_3(w)
\le(1-\varepsilon)\nu\rho D_3(w)\) pointwise on \(\operatorname{supp}\rho\).
\(\square\)

The identity is exact and the only new cost, \(\Lambda\int\mathcal Q\,dt\), is
input-bounded — this is a second use of the audited normalisation (E6), whose
first use was the removal of the Gronwall term from `hyp:highstrain`. What is
*not* supplied by the audited record is an admissible \(\Lambda\).

**Corollary 3.5 (conditional reduction of O3, hypotheses displayed).** Fix
\(\varepsilon\in(0,1)\) and write
\(\mathcal G^{2\varepsilon}_\tau\subset\mathcal G^{\varepsilon}_\tau\) for the
two good sets at levels \((1-2\varepsilon)\nu\) and \((1-\varepsilon)\nu\).
Assume:

> **(H-mod)** There are \(\Lambda=\Lambda(\nu,u_0,H)<\infty\), input-only, and
> for every \(\tau<\min\{H,T_*\}\) a Lipschitz \(\rho:[0,\tau]\to[0,1]\) with
> \(\operatorname{Lip}\rho\le\Lambda\), \(\rho=1\) on
> \(\mathcal G^{2\varepsilon}_\tau\) and
> \(\operatorname{supp}\rho\subset\mathcal G^{\varepsilon}_\tau\).

Then
\(\varepsilon\nu\int_{\mathcal G^{2\varepsilon}_\tau}D_3(w)\,dt\le
\mathcal Q(0)+\Lambda A_{\mathcal Q}\), an input-only bound: **(H-mod) settles
the audited obstruction O3 affirmatively**, and consequently
\[
 \int_{\mathcal G^{2\varepsilon}_\tau}\!\!d_1D_3(w)\,dt
 \ \le\ \frac{(1-2\varepsilon)\nu}{C_\sharp}\cdot
 \frac{\mathcal Q(0)+\Lambda A_{\mathcal Q}}{\varepsilon\nu}
 \ =\ \frac{(1-2\varepsilon)}{\varepsilon\,C_\sharp}
 \bigl(\mathcal Q(0)+\Lambda A_{\mathcal Q}\bigr),
\]
so that **(G) reduces to its bad-set part**
\(\int_{(\mathcal G^{2\varepsilon}_\tau)^c}d_1D_3(w)\,dt\le A_{\rm input}\)
alone. (H-mod) is equivalent to an input-only modulus of continuity for
\(t\mapsto\|q(t)\|_3\) at the level \(\nu/C_\sharp\): a Lipschitz cutoff with
constant \(\Lambda\) exists as soon as every passage of \(C_\sharp d_1\) from
\((1-2\varepsilon)\nu\) to \((1-\varepsilon)\nu\) takes time at least
\(1/\Lambda\). The audited modulus is **not** of this kind: by (E8) Remark 2.2,
\(|d_1(t')-d_1(t)|\le2(\|w(t)\|_3+\|u(t')-u(t)\|_3)^{1/2}\|u(t')-u(t)\|_3^{1/2}\),
whose constant contains \(\sup_t\|\partial_tu\|_3\) through
\(\|u(t')-u(t)\|_3\), and neither factor is input-bounded. **(H-mod) is open,
and it is a new, precisely posed sub-question**: it is a time-regularity
statement about the nonlinear projection, not an estimate for \(K\).

**Remark 3.6 (the exact price of "cancelling signs at crossings").** Replacing
the Lipschitz \(\rho\) by the sharp cutoff
\(\rho=\mathbf 1_{\mathcal G_\tau}\) is legitimate only through the
bounded-variation form of (3.5): \(\int\rho'\mathcal Q\) becomes a sum over the
endpoints of the connected components of \(\mathcal G_\tau\), bounded by
\(2N_\tau\sup_{t<\tau}\mathcal Q\), where \(N_\tau\) is the number of
components of the bad set \(\mathcal B_\tau\) — the number of crossings. Two
facts of the audited record then meet: \(|\mathcal B_\tau|\le
24S^2C_\sharp^4E_0^2\nu^{-5}\) uniformly in \(\tau\) (E8 Thm. 4.5), so the
*measure* of the crossing set is input-bounded; but no bound on \(N_\tau\) is
available, and \(\sup_t\mathcal Q\) is the conclusion. **So the crossing
structure is available per crossing and is defeated by their number**: a
trajectory that oscillates across the level \(\nu/C_\sharp\) infinitely often
pays \(N_\tau=\infty\) while keeping \(|\mathcal B_\tau|\) small. That is the
exact obstruction to the "trajectories crossing \(\mathcal M\) contribute with
cancelling signs" mechanism at the audited level; (H-mod) is precisely the
hypothesis that forbids it.

**Remark 3.7 (why no lower bound for \(|K|\) can be inserted).** All of §3
bounds \(\int mK\) from above by \(C_\sharp\int md_1D_3(w)\). The reverse — an
inequality \(|K|\ge c\,d_1D_3(w)\) that would turn a bound on \(\int K\) into
(G) — is false: by (3.1) \(K\) is the contraction of \(T(w)-T(u)\) with
\(S(u)\), and \(S(u)\) is trace-free, so \(K\) vanishes on a nontrivial set of
strain configurations at fixed \(d_1D_3(w)>0\). This is why (G) is strictly
stronger per trajectory than the frozen gap (§1.4), and it is also why the
audited HF20 two-sign certificate (`rem:no-monotone`) cannot be used in the
opposite direction.

---

## 4. Self-check against the packet's falsifiers

| Falsifier | Where it could have entered | Disposition |
|---|---|---|
| A bound using the norm it must control | (1.4), (1.5), Prop. 2.4, Thm. 3.2(3) | (1.4) is an estimate, not a closure; Cor. 1.4 is labelled a smallness criterion and is used nowhere else; Prop. 2.4 *displays* the circularity as the exact overshoot \(2/(3s)\); Thm. 3.2(3) is explicitly declared empty because its region is the audited Kato region |
| Scaling-inconsistent absorption | (1.1)–(1.6), (1.5), (2.1), (3.4)–(3.6) | \((a,\lambda)\) weights are displayed for every new inequality: (1.1) \((a^4,\lambda^2)\); (1.3) \((a^3,\lambda^2)\); (1.4) \((a^4,\lambda^2)\); (1.5) \((a^3,\lambda^0)\) on both routes; (3.4)–(3.6) are weighted forms of (E1) and inherit its weights |
| Hidden smallness | Cor. 1.4, Thm. 3.2(3), Cor. 3.3 | all three carry an explicit smallness hypothesis, and each is labelled: Cor. 1.4 is Kato; 3.2(3) is Kato again and is declared empty; Cor. 3.3's \(y_0\) is smallness of the *distance*, which is not smallness of the norm (HF21-B §3.3) but is still a hypothesis and is never assumed to hold |
| Differentiating the merely-\(L^3\) minimizer | §3 throughout | only \(\mathcal Q\) and \(F\) are differentiated, both audited (`lem:quotient-chainrule`, `prop:pressure`); Thm. 3.2 is stated *because* these are the only two, and Remark 2.2 of HF21-B is cited each time \(d_1\) appears in time |
| Instantaneous fact promoted to a time-integrated one | (1.4) \(\to\) (1.5); (3.1) \(\to\) §3.2 | (1.5) is stated as a *hypothesis* \((\mathrm G_P)\), never as a result; (3.1) is used only as motivation and is a step in nothing |
| Forced/periodic/hyperdissipative/Euler substitute | throughout | all statements are for the unforced classical branch of `prop:localtheory` on \(\mathbb R^3\), arbitrary \(\nu>0\), arbitrary divergence-free Schwartz datum |
| Numerics used as proof | — | no numerics anywhere in this note |
| Re-deriving a recorded result and claiming it as new | (1.3), Cor. 1.4, (3.1), Prop. 1.8 | (1.3) is elementary and marked as such; Cor. 1.4 is Kato and is marked as a consistency check; (3.1) is one subtraction from HF18-B Prop. 3.1 and is marked as such; Prop. 1.8 is the converse argument of `rem:highstrain-scope` applied to two further statements, and is marked as scope, not progress |
| A displayed claim not following from its proof | Thm. 3.2, Cor. 3.3, Prop. 3.4 | each proof is complete from (E1), (E2), (E3), (E6), (E8) and the chain rule for absolutely continuous functions; every integrability hypothesis is checked in the proof of Thm. 3.2 |
| Promoting an open hypothesis | (H-mod), \((\mathrm G_P)\), HF21-B (a) | all three are displayed as hypotheses, and every consequence drawn from them is written as an implication |

---

## 5. Frontier record

**MODE / RESULT:** DISCOVER (direct attack on (G)), **UNAUDITED**. Result:
(G) is **not** proved and not refuted. Four exact structural results are
obtained — the pressure-route mirror of the product statement with its
identities, coercivity and size bound (§1); the exact interpolation deficit
\(\frac12\) of the audited input hull together with the exact overshoot
\(\frac2{3s}\) of the Hölder split (§2); the closure of the class of exact
time-integrations by parts, with its weight invariant and the forced pressure
coupling (§3.2–3.3); and one conditional reduction, (H-mod) \(\Rightarrow\) O3
\(\Rightarrow\) (G) reduces to its bad-set part, together with the exact price
of the crossing mechanism, \(2N_\tau\sup\mathcal Q\) (§3.4).

**CLAIM AND SCOPE:** For the classical branch of `prop:localtheory` from an
arbitrary divergence-free Schwartz datum on \(\mathbb R^3\) with arbitrary
\(\nu>0\), on every \([0,\tau]\subset[0,T_*)\):
Lemma 1.1 (\(P_3=\langle\operatorname{div}(|u|u),p\rangle
=-\langle(I-\mathbb P)j(u),\nabla p\rangle\), \(P_3=0\) on \(\mathcal M\),
\(\int_0^\tau\|p\|_3dt\le C_{\rm CZ}(3)S^2E_0/2\nu\));
Lemma 1.2 ((1.2), \(D_3(u)\ge\frac4{5S^2}\|u\|_9^3\));
Proposition 1.3 (\(|P_3|\le C_{\rm pr}\|u\|_3D_3(u)\),
\(C_{\rm pr}=(\frac54)^{1/2}SC_{\rm CZ}(9/4)\)) with Corollary 1.4 (Kato on the
pressure route, a consistency check, not new);
Proposition 1.5 and Remarks 1.6–1.7 (the two-route comparison; the pressure
analogue is not easier; \((\mathrm G_P)\Rightarrow(\mathrm G)\) iff HF21-B
sub-question (a));
Proposition 1.8 (existential equivalence of \((\mathrm G)\), \((\mathrm G_P)\),
`hyp:highstrain`, `hyp:absorption`, `hyp:highpressure`, \(T_*=\infty\)), with
the scope correction that (G) is strictly stronger than the frozen gap per
trajectory;
Propositions 2.1–2.4 and Corollary 2.2 (the input hull is one segment of
\(\lambda=\frac32\); deficit exactly \(\frac12\), uniform; the ninth-power
space is critical but conditional; the Hölder split overshoots by exactly
\(\frac2{3s}\));
Lemma 3.1 (difference-of-cubic-fluxes form of \(K\), from HF18-B Prop. 3.1);
Theorem 3.2 with consequences 1–3 (closure, weight invariance, forced pressure
coupling, emptiness of \(\mathcal Q\)-only weights);
Corollary 3.3 (the exact residual of a distance cutoff);
Proposition 3.4, Corollary 3.5 and Remarks 3.6–3.7 (time weights; the
conditional reduction under (H-mod); the crossing-number price; no reverse
inequality for \(|K|\)).
Premises: `prop:localtheory`, `lem:upgrade`, `prop:energy`, `prop:scaling`,
`def:D3P3`, `prop:pressure`, `lem:sobolev`, `lem:leray`,
`lem:gradient-closure`, `lem:quotient-minimizer`, `lem:quotient-coercive`,
`lem:quotient-stability`, `prop:quotient-derivative`, `lem:quotient-pressure`,
`lem:quotient-chainrule`, `lem:quotient-heatsign`, `lem:quotient-transport`,
`prop:quotient-evolution`, `lem:quotient-lowstrain`,
`rem:highstrain-normalisation`, `rem:distance-balance`,
`prop:quotient-conditional`, `cor:absorption-consequence`, `thm:conditional`,
`thm:continuation` [all DI]; audited HF18-A and audited-and-repaired HF21-B
[DI]; HF18-B Prop. 3.1 and (3.2) [DI] in exactly two displays (Lemma 3.1 and
the comparison line of §1.3), load-bearing for nothing.

**EVIDENCE:** Hölder \((\frac98,9)\) with Calderón–Zygmund at \(r=\frac94\) and
the interpolation \(\|u\|_{9/2}\le\|u\|_3^{1/2}\|u\|_9^{1/2}\) for
Proposition 1.3; the pointwise chain rule for \(\Phi(z)=|z|^{1/2}z\), which is
\(C^1\) with \(D\Phi(0)=0\), plus `lem:sobolev`, for Lemma 1.2; the Leray
duality \(\langle\mathbb Pf,g\rangle=\langle f,\mathbb Pg\rangle\) and
\(\nabla p\in\mathcal G_3\) for Lemma 1.1; affineness of
\(\lambda(r,q)=\frac2r+\frac3q\) under Hölder interpolation for §2, with the
identification of \(L^4_tL^3\) as the midpoint of \(L^\infty_tL^2\) and
\(L^2_tL^6\) (which is how \eqref{eq:L4L3} is proved); the chain rule for
absolutely continuous functions applied to \(G(\mathcal Q,F,t)\), together with
the audited fact that \(\mathcal Q\) and \(F\) are the only differentiable
functionals available, for Theorem 3.2; integration by parts in \(t\) against a
Lipschitz weight plus the audited \(\int_0^\tau\mathcal Q\,dt\) bound for
Proposition 3.4. No numerics, no CAS, no external source beyond those already
imported by the manuscript.

**FIRST GAP:** unchanged and not closed. It is (G),
\(\int_0^\tau\|q\|_3D_3(w)\,dt\le A_{\rm input}\) uniformly for
\(\tau<\min\{H,T_*\}\). The first unsupported implication if one tried to close
it here is at Corollary 3.5: **(H-mod)** — an input-only Lipschitz cutoff
adapted to the good set, equivalently an input-only modulus of continuity for
\(t\mapsto\|q(t)\|_3\) at the level \(\nu/C_\sharp\) — is not supplied by the
audited record, whose only modulus (HF21-B Remark 2.2) has a constant
containing \(\sup_t\|\partial_tu\|_3\). Everything before that point is proved;
nothing after it is asserted.

**SURVIVING CONDITIONAL SUFFIX:**
(i) If (H-mod) holds for some \(\varepsilon\in(0,\frac12)\), then
\(\varepsilon\nu\int_{\mathcal G^{2\varepsilon}_\tau}D_3(w)\,dt\le
\mathcal Q(0)+\Lambda A_{\mathcal Q}\) — obstruction O3 is settled — and (G)
reduces to \(\int_{(\mathcal G^{2\varepsilon}_\tau)^c}d_1D_3(w)\,dt\le
A_{\rm input}\).
(ii) If HF21-B sub-question (a), \(D_3(w)\le D_3(u)\), holds pointwise in time,
then \((\mathrm G_P)\Rightarrow(\mathrm G)\) with constant
\(1+C_{\mathbb P}\), and the audited ordering extends from the fluxes to the
product statements.
(iii) If \((\mathrm G_P)\), i.e. \(\int_0^\tau\|u\|_3D_3(u)\,dt\le
A_{\rm input}\), holds, then `hyp:absorption` holds with \(\theta=0\) and
\(A=C_{\rm pr}A_{\rm input}\), hence `def:target`.
(iv) If \(\sup_{t<\tau}\|q(t)\|_3\le(1-\varepsilon)\nu/C_\sharp\), then (G)
holds with \(A_{\rm input}=(1-\varepsilon)\mathcal Q(0)/(\varepsilon C_\sharp)\)
— the criterion of HF21-B Prop. 3.3, restated in product form; its hypothesis
is on the unknown trajectory.
None of (i)–(iv) is proved here.

**NON-CLAIMS:** no proof or refutation of (G), \((\mathrm G_P)\),
`hyp:highstrain`, `hyp:highpressure`, `hyp:absorption`, `hyp:critical`, or
NS-R3; no bound on \(\sup_t\|u\|_3\), on \(\int_0^\tau D_3(w)\,dt\), on
\(\int_0^\tau D_3(u)\,dt\), on \(\int_{\mathcal G_\tau}D_3(w)\,dt\)
unconditionally, or on \(\int_0^\tau d_1D_3(w)\,dt\); no inequality between
\(D_3(w)\) and \(D_3(u)\) in either direction, and none is used; no sign for
\(K(t)\), \(P_3(t)\), or their time integrals; no lower bound for \(|K|\), and
Remark 3.7 records why none is available; no time-differentiability of \(d_1\),
\(q\), \(w\) or \(A\), and no differentiation of the minimizer anywhere; no
regularity of \(w\) beyond \(L^3\cap L^9\) and \(V\in H^1\) as audited; no
progress on (H1), (H2), the weighted Calderón–Zygmund inequality, the \(L^2\)
projection bound, or the Lipschitz question at \(\mathcal M\); no novelty
claimed for (1.3), for Corollary 1.4 (Kato), for Lemma 3.1 (one subtraction
from an audited identity), for Proposition 1.8 (the converse argument of
`rem:highstrain-scope`), or for the nonlinear-Hodge construction; the numbers
of §2 quantify audited obstructions (O1, `rem:mismatch`) and do not weaken or
strengthen them; Theorem 3.2 retires a *mechanism class* (state-weighted exact
time-integration by parts) and refutes no statement about the equations;
Corollary 3.3's smallness threshold \(y_0\) is a hypothesis on the trajectory,
never an input fact; nothing in this note is promoted, the manuscript is
untouched, and no file but this one is written.

**NEXT DISTINCT ACTION:** two distinct, non-overlapping continuations, in the
order of information gained.
1. **Attack (H-mod)** — an input-only modulus of continuity for
   \(t\mapsto\|q(u(t))\|_3\), equivalently an input-only lower bound on the
   time a trajectory needs to cross the level \(\nu/C_\sharp\). This is a new
   sub-question, distinct from HF21-B's (a), (b), (c): it is time-regularity of
   the nonlinear projection along the flow, not an estimate for \(K\). Note
   that it is *weaker* than Lipschitz-in-time regularity of \(q\), which would
   need \(\partial_tu\in L^3\) uniformly; the audited \(\frac12\)-Hölder
   estimate is one route, and a route through the *integrated* balance
   \(d_2'=P_3-K+\nu(D_3(w)-D_3(u))\) together with
   \(\frac16d_1^3\le d_2\le(2+C_3)(3\mathcal Q)^{1/3}d_1^2\) is a second,
   since \(d_2\) is absolutely continuous while \(d_1\) is not known to be.
2. **Attack HF21-B sub-question (a)**, \(D_3(w)\le D_3(u)\), which by
   Proposition 1.5(3) is exactly what would make the two routes comparable at
   the product level, and by HF21-B §4.1 would delete the term
   \(\nu\int(D_3(w)-D_3(u))\) from the master identity. It is fixed-time,
   minimizer-free in its statement, and scaling-consistent on both sides.
Both are falsifiable by construction, and neither is the question this lane
answered.

---

## 6. Sources

Manuscript labels are from `../navier-paper/main.tex` at the current head,
directly inspected this wave [DI]: `sec:quotient` in full together with
`prop:localtheory`, `lem:upgrade`, `prop:energy`, `prop:scaling` with
\eqref{eq:L4L3} and \eqref{eq:L4L3-constant}, `rem:mismatch`, `lem:interp`,
`lem:sobolev`, `def:sobolev-constant`, `def:D3P3`, `prop:pressure`,
`lem:integrands`, `prop:lowpressure`, `hyp:highpressure`, `hyp:absorption`,
`lem:absorption-split`, `cor:absorption-consequence`,
`prop:existential-equivalence`, `thm:continuation`, `hyp:critical`,
`thm:conditional`, `lem:div-zero`. Repository evidence used as premises [DI]:
`hf18-hodge-regularity.md` with `hf18-review-hodge-regularity.md` (PASS);
`hf21-crossing-sign-structure.md` with
`hf21-review-crossing-sign-structure.md` (REPAIR, repairs applied). Used in
exactly two displays and load-bearing for nothing [DI]:
`hf18-divergence-speed-link.md` (Prop. 3.1, (3.2)) with its two reviews (PASS
after S1–S4). Read, not premises [DI]: `hf21-shifted-hodge-regularity.md` with
its audit; `hf19-temporal-normal-form.md`, `hf19-second-order-falsifier.md`,
`hf19-difference-functional.md` (unaudited); `hf20-harmonic-strain-test.md`
(audited; integrated as `rem:no-monotone`); `PLAN.md`. External facts are only
those already imported by the manuscript (Brezis; Grafakos; Stein,
Calderón–Zygmund and Riesz-transform \(L^r\) bounds; Tao 2013; ESS 2003),
through the labels above; none is used outside the scope in which the
manuscript verifies it.
