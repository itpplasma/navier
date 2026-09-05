# Independent audit of the HF18-B divergence–speed link

**VERDICT: REPAIR.**

Frozen input: `research/evidence/hf18-divergence-speed-link.md`, SHA-256
`7cec90204acb727ca83dffb1c52375f5a84c4597810760106ac813d247d545d0`,
base commit `fd1c20e4ec32d7932bb318836d02b10a073e3500`.
Mode: REVIEW, proof-audit discipline.  Reviewed against PLAN.md
("Frontier packet", "HF16–HF17"), `hf17-quotient-functional.md`,
`hf17-quotient-evolution.md`, both HF17 reviews (PASS), and `sec:quotient`
of `../navier-paper/main.tex`.

The mathematical substance survives.  Every displayed inequality and every
identity that the note asserts is correct as stated, with two classes of
defect: a systematic Riesz-transform sign convention error that propagates
through three displays (cosmetic: all downstream uses are absolute values),
and two overstatements inside boxed/recorded claims — the quantifier
"for any function \(\Phi\)" in Proposition 2.2, and the assertion that a
weighted Calderón–Zygmund inequality is *false*.  Both are repaired below with
proofs.  None of the repairs changes the note's negative conclusion, its FIRST
GAP, or its NON-CLAIMS.

## REVIEWED SCOPE

§0 scaling bookkeeping; §1.1–1.5 (Prop. 1.1, Rmk. 1.2, Rmk. 1.3/(1.4),
(H1'), (1.5), Prop. 1.4, (1.7)–(1.8)); §2.1–2.4 ((2.1), Prop. 2.1, exponent
analyses, Prop. 2.2 with its numerical table); §3.1–3.3 ((3.1)–(3.3),
Prop. 3.1 with (3.4)–(3.6), split (3.7), attempts (a)–(d)); §4 items 1–8;
§5 frontier record.  Inputs treated as previously reviewed and not re-proved:
HF17 (5), (13)–(15) of `hf17-quotient-evolution.md` (both HF17 reviews PASS).
Sibling lane `hf18-hodge-regularity.md` (HF18-A) is *not* audited here; it is
referenced only to record dependency status.

## FIRST BAD BRIDGE

Two, in reading order.

**(B1), cosmetic and non-propagating — (1.1).**  With the note's own
definition \(R_j=\partial_j(-\Delta)^{-1/2}\) (symbol \(i\xi_j/|\xi|\)),
\[
 (R_iR_j)^{\wedge}=-\xi_i\xi_j/|\xi|^2,\qquad
 \mathbb P_{jk}=\delta_{jk}+R_jR_k,\qquad (I-\mathbb P)_{jk}=-R_jR_k ,
\]
so \(q=(I-\mathbb P)w=-R(R\cdot w)\), not \(+R(R\cdot w)\).  The same slip
recurs in (1.7) (the kernel sign) and in (3.1) (the Riesz formula for
\(\Pi_L\) and the parenthetical "\(p=R_iR_j(u_iu_j)\)").  It is *not* a slip
in (3.2)/(3.3), which are correct as displayed once \(\Pi_L\) is fixed by
\(\nabla\Pi_L=(I-\mathbb P)F\); see Lemma R1.  Nothing downstream uses the
sign, and §3.3(d) correctly reports that no sign is available anyway.

**(B2), substantive — Prop. 2.2 and §3.3(c)(i)/FIRST GAP.**
(i) The conclusion "no inequality \(\|\sigma\|_{3/2}\le\Phi(D_3,\mathcal Q,E)\)
holds on \(\mathcal M\), for any function \(\Phi\)" does not follow from the
family: the triples \((D_3,\mathcal Q,E)(\delta)\) stay in a compact subset of
\((0,\infty)^3\) but need not be constant, and an arbitrary finite-valued
\(\Phi\) may be unbounded there.  Repaired in Lemma R2 (locally bounded
\(\Phi\); this covers every power product of §2.3 and every continuous or
monotone \(\Phi\)).
(ii) The description of the family as "smooth compactly supported fields" is
false: \(w_\delta=|A|^{-1/2}A\) has \(|\nabla w_\delta|\sim\mathrm{dist}^{-1/2}\)
at the zero lines of \(A\).  What is needed and true is (H1'); Lemma R2 proves it.
(iii) "a *false* weighted Calderón–Zygmund inequality" (§3.3(c)(i) and the
FIRST GAP record) is not proved.  Failure of the \(A_2\) condition is failure
of a *sufficient* hypothesis, and the note's own witness (\(A\equiv0\) on a
ball) does not refute the inequality, because the weight \(|w|\) annihilates
both sides on that ball.  Repaired in Lemma R3: the correct status is
"unavailable", not "false" — and the route fails regardless, at obstruction (ii).

## EVIDENCE

Checked independently, item by item.  "✓" = re-derived here.

**§1.**
1. Prop. 1.1 ✓.  \(F(z)=|z|z\in C^1\), \(DF(z)=|z|I+z\otimes\hat z\),
   \(|DF(z)|\le2|z|\); truncation + chain rule for \(C^1\) maps with bounded
   derivative on \(W^{1,1}_{\rm loc}\), dominated convergence with the (H1)
   majorant \(2|w||\nabla w|\).  One phrasing fix: the truncation must satisfy
   \(|DF_R|\le2\min(|z|,R)\) (bounded derivative *and* the majorant); the note
   writes only \(|DF_R|\le2|z|\).  Trace: \(\operatorname{div}A=|w|\operatorname{div}w+w\cdot\nabla|w|
   =|w|(\operatorname{div}w+\sigma)\), so \(\operatorname{div}w=-\sigma\) a.e. on
   \(\{w\ne0\}\) and \(\operatorname{div}w=0\) a.e. on \(\{w=0\}\) by
   \(\nabla w=0\) a.e. there.  Trace form
   \(\operatorname{tr}((I+\hat w\otimes\hat w)\nabla w)=\partial_iw_i+\hat w_i\hat w_k\partial_iw_k\) ✓.
   *Independent test on an exact nonzero solution.*  \(w=Cx/|x|^2\) solves
   \(\operatorname{div}(|w|w)=0\) away from the origin
   (\(|w|w=C^2x/|x|^3\)); \(\operatorname{div}w=+C/|x|^2\),
   \(\sigma=\partial_r(C/r)=-C/r^2\); the identity holds with the stated sign ✓.
   *Second test:* constant speed \(|w|\equiv c\) forces
   \(\operatorname{div}w=0\), consistent with \(\operatorname{div}A=c\operatorname{div}w\) ✓.
2. Rmk. 1.2 ✓.  \(\psi=-x_1^3/3\Rightarrow A=(0,x_1^2,0)\),
   \(\operatorname{div}A=0\), \(|w|=|x_1|\): codimension-one zeros do occur in
   \(\mathcal M\).  Thresholds: with \(|w|\sim d^\beta\), both
   \(\int|w||\nabla|w||^2\sim d^{3\beta-2}\) and \(\int|\sigma|^{3/2}\sim
   d^{3(\beta-1)/2}\) are transversally integrable exactly for \(\beta>1/3\) ✓.
3. Rmk. 1.3 ✓.  \(\operatorname{div}(|w|^\alpha w)=(1-\alpha)|w|^\alpha\operatorname{div}w\)
   from (1.3); the stated hypotheses give \(|w|^\alpha w\in W^{1,1}(\mathbb R^3)\),
   for which \(\int\partial_i f=0\) ✓.  For \(\alpha=3\) the hypotheses follow
   from (H1') by \(\int|w|^4\le(\int|w|^3)^{1/2}(\int|w|^5)^{1/2}\) and
   \(\int|w|^3|\nabla w|\le(\int|w|^5)^{1/2}(\int|w||\nabla w|^2)^{1/2}\) ✓.
4. (H1')\(\Rightarrow\)(H1) ✓ (\(L^6\cdot L^2\subset L^{3/2}\)).
   (1.5) ✓ all four, with \(g=|w|^{3/2}\), \(\|g\|_2^2=3\mathcal Q\),
   \(\|\nabla g\|_2^2=\tfrac94D_3^{\rm rad}\): \(\|\nabla A\|_{3/2}\le
   \||w|^{1/2}|\nabla w|\|_2\||w|^{1/2}\|_6\); \(\int|w|^5=\|g\|_{10/3}^{10/3}\)
   with Gagliardo–Nirenberg exponent \(\theta=3/5\); \(\|w\|_{9/2}^3=\|g\|_3^2\)
   with \(\theta=1/2\); \(|\sigma|\le|\nabla|w||\).
   The formal \(D_{\mathcal Q}=-\int A\cdot\Delta u=D_3(w)\) computation ✓ reproduces
   \(\int|w||\nabla w|^2+\int|w||\nabla|w||^2\), i.e. the note's \(D_3\); correctly
   *not* claimed here.
5. Prop. 1.4 ✓.  \(z\mapsto|z|z\) is a bijection \(L^3\to L^{3/2}\) with
   \(\|w\|_3^3=\|A\|_{3/2}^{3/2}\), giving (1.6) at once.  The nontrivial half —
   every \(w\in\mathcal M\) *is* the minimizer for \(u=\mathbb Pw\) — is correct:
   \((I-\mathbb P)C_c^\infty\subset\mathcal G_3\) via \(\psi=\partial_i(\Gamma*f_i)
   =O(|x|^{-2})\in L^3\), \(\nabla\psi=O(|x|^{-3})\in L^3\) and the HF17 cutoff
   \(\|\psi\nabla\chi_R\|_3\le CR^{-1}\|\psi\|_{L^3(R\lesssim|x|\lesssim2R)}\to0\);
   density plus \(L^3\)-boundedness of \(I-\mathbb P\); then stationarity of a
   convex Gâteaux-differentiable functional is global minimality, and HF17
   uniqueness closes.  *Refutation attempt:* a \(w\in\mathcal M\) that is not the
   minimizer of its own \(\mathbb Pw\) would contradict convexity — none exists.
6. Citation check, **directly inspected**: Stern, arXiv:2403.19481v2, p. 3–4:
   Lemma 2.2 (existence of a \(p\)-coclosed primitive \(\beta_\infty\) with
   \(d^*(|\beta_\infty|^{p-2}\beta_\infty)=0\), uniqueness by strict convexity)
   and Theorem 2.9 "(Nonlinear Hodge Theorem)": for
   \(\varphi\in H^k_{p,\rm red}(M)\) there is a unique \(h\in Z^k_p(M)\) with
   \([h]_{\rm red}=\varphi\) and \(d^*(|h|^{p-2}h)=0\), norm-minimizing in its
   class; [Sco95] and [ISS99] are credited exactly as the note says.  The note's
   labelling is accurate, and its scope note is the right one: Stern's theorem
   quantifies over **closed** forms in a reduced cohomology class, whereas
   \(w\) is not closed, so Prop. 1.4 is not an instance of Thm. 2.9 — only the
   convexity/first-variation mechanism is shared.  The note claims exactly this.
   Additional confirmation of a NON-CLAIM: Stern §3 records (via Uhlenbeck,
   [Uhl77]) that \(p\)-harmonic forms are smooth where nonzero — but that is for
   forms satisfying *both* \(dh=0\) and \(d^*(|h|^{p-2}h)=0\); \(w\) satisfies only
   the second, so no such regularity transfers.  This supports the packet's
   falsifier list and the note's refusal to invoke Tolksdorf/DiBenedetto/
   Lieberman/Uraltseva.
7. (1.7)–(1.8): the middle expression \(q=-\nabla(\Gamma*\sigma)\) is right;
   the explicit kernel carries the wrong sign (Lemma R1, verified below on an
   exact example).  \(\|q\|_3\le C_{\rm HLS}\|\sigma\|_{3/2}\) ✓
   (\(I_1:L^{3/2}(\mathbb R^3)\to L^3\)), scaling-consistent ✓.

**§2.**
8. §2.1 exponent algebra ✓ (\(c=2a\), \(7a+3b=3\)).  (2.1) ✓ re-derived:
   \(\|g\|_2\le\|g\|_{4/3}^{4/7}\|g\|_6^{3/7}\) (interpolation identity
   \(\tfrac12=\tfrac47\cdot\tfrac34+\tfrac37\cdot\tfrac16\) ✓) gives
   \(\|w\|_3^3\le C\|w\|_2^{12/7}(D_3^{\rm rad})^{3/7}\), with \(\|w\|_2\)
   — the note is right that \(\|w(u)\|_2\lesssim\|u\|_2\) is not available
   (only \(\|u\|_2\le\|w\|_2\) by \(L^2\)-orthogonality of \(\mathbb P\)),
   and right to leave it open.
9. Prop. 2.1 ✓.  \(\int|q|^2|w|^3=\|qg\|_2^2\le\|q\|_3^2\|g\|_6^2\le
   C\|w\|_3^2\|\nabla g\|_2^2\).  Scaling \((a^5,\lambda^2)\) on both sides ✓.
   Minor: "sharp on single-scale fields" needs \(|q|\sim|w|\) on the family
   (false if \(w\) is solenoidal, where the left side vanishes); the order
   check itself is correct for fields with a nondegenerate gradient part.
   Remark (a) is correct and important: no divergence structure is used, so
   (2.2) is not evidence about \(\mathcal M\).
10. §2.3 exponent algebra ✓ (\(\|\sigma\|_{3/2}^{3/2}\sim(a^{3/2},\lambda^0)\) ✓).
11. Prop. 2.2 ✓ *as a mechanism*, with the two corrections of (B2)(i)–(ii).
    Verified independently: \(\operatorname{curl}(\psi e_3)=(\partial_2\psi,-\partial_1\psi,0)\)
    reproduces the displayed \(A_1\) ✓; zeros of \(A_1\) are the lines
    \(\{\sin ky_1=0\}\cap\{\cos ky_2=0\}\), codimension two, with \(|A_1|\)
    vanishing linearly, hence \(|w|\sim d^{1/2}\), \(|\nabla w|\sim d^{-1/2}\) ✓;
    the bulk \(A_0=\operatorname{curl}(\phi_0e_3)\) gives
    \(|A_0|=8(1-|x|^2)^3_+\rho\) ✓, and \(w_0\) is the azimuthal field
    \(c(1-|x|^2)^{3/2}\rho^{-1/2}(-x_2,x_1,0)\), which is itself solenoidal, so
    \(q_0=0\), \(\sigma_0\equiv0\), \(u_0=w_0\), \(\mathcal Q(\mathbb Pw_0)>0\) ✓.
    Exact homogeneity: \(A=\delta^2F(kx)\Rightarrow w=\delta G(kx)\), so per unit
    volume \(\int|\sigma|^{3/2}=(\delta k)^{3/2}\langle|\Sigma|^{3/2}\rangle\),
    \(\int|w||\nabla w|^2=\delta^3k^2\langle\cdot\rangle\),
    \(\int|w|^3=\delta^3\langle\cdot\rangle\), \(\int|w|^2=\delta^2\langle\cdot\rangle\) ✓.
    Arithmetic at \(R^3=\delta^{-2}\), \(k=\delta^{-1/2}\):
    \(D_3\sim1\), \(\int|w|^3\sim\delta\), \(\int|w|^2\sim1\),
    \(\int|\sigma|^{3/2}\sim\delta^{-5/4}\) ✓.
    Nondegeneracy of the constant (the one non-homogeneity fact): with
    \(\psi\propto(2+\cos y_1)\sin y_2\), \(F=\nabla^\perp\psi\) and
    \(\sigma\propto\hat F\cdot\nabla|F|=\hat F\cdot\nabla|\nabla\psi|\); on the
    level set \(\{\psi=0\}=\{\sin y_2=0\}\) one has \(|\nabla\psi|=2+\cos y_1\),
    non-constant, so \(\sigma\not\equiv0\) ✓.
    *Independent numerics* (my own script, \(N=1024^2\), central differences,
    one periodic cell): \(\langle|\sigma|^{3/2}\rangle=0.1898\), \(D_3=2.188\),
    \(\int|w|^3=1.848\) at \(\delta=k=1\), with exact ratios \(k^{3/2}\), \(k^2\),
    \(\delta^{3/2}\), \(\delta^3\) across \((\delta,k)\in\{1,\tfrac12,\tfrac14\}
    \times\{1,2,4\}\), and \(\|\operatorname{div}w+\sigma\|/\|\sigma\|=2.9\times10^{-4}\)
    away from the zero lines.  This reproduces the note's table to <1% and
    confirms the pointwise identity on the family.
    *Refutation attempt (failed):* is the \(\sigma\)-blow-up a zero-set artifact,
    so that a "regular part" bound could survive?  No: the vanishing order is
    \(1/2\) on codimension-two lines, both \(\int|w||\nabla w|^2\) and
    \(\int|\sigma|^{3/2}\) converge absolutely there, and the divergence is
    produced by the low-amplitude/high-oscillation regime, exactly as the note's
    "Mechanism" paragraph says.
    *Consistency cross-check:* the natural Hölder route
    \(\int|\sigma|^{3/2}=\int(|w|\sigma^2)^{3/4}|w|^{-3/4}\le(\int|w|\sigma^2)^{3/4}(\int|w|^{-3})^{1/4}\)
    requires the non-integrable weight \(|w|^{-3}\) — consistent with, and
    explained by, Prop. 2.2 ✓.

**§3.**
12. (3.1)/(3.2) ✓ modulo (B1).  \(F=\partial_i(A_iu^{hi})\) in \(\mathcal D'\)
    is correct: for \(\varphi\in C_c^\infty\),
    \(-\int A_iu^{hi}_j\partial_i\varphi=-\int A_i\partial_i(u^{hi}_j\varphi)+\int A_i(\partial_iu^{hi}_j)\varphi\)
    and the first integral vanishes because \(\operatorname{div}A=0\) tests against
    \(C_c^1\) by mollification ✓.  \(\int q\cdot\mathbb PF=0\) for \(q\in\mathcal G_3\),
    \(\mathbb PF\in L^{3/2}\) ✓ (compact gradients, then density).  Hence
    \(K_L=-\int q\cdot(I-\mathbb P)F=-\int q\cdot\nabla\Pi_L=\langle\operatorname{div}w,\Pi_L\rangle\)
    ✓ with \(\Pi_L\) defined by \(\nabla\Pi_L=(I-\mathbb P)F\); the Riesz formula
    needs the sign of Lemma R1.  \(\Pi_L\in W^{1,3/2}\subset L^3\) ✓.
    \(\nabla\Pi_L=(I-\mathbb P)[(u^{hi}\cdot\nabla)A]\) ✓ (both reduce to
    \(\nabla\Delta^{-1}\partial_i\partial_j(A_iu^{hi}_j)\)).
13. Prop. 3.1 ✓, all three identities re-derived.
    (3.4): \(\nabla|u|^2\in\mathcal G_3\) is legitimate for \(u\in H^m\), \(m\ge4\)
    (\(|u|^2\in L^3\), \(\nabla|u|^2\in L^2\cap L^\infty\subset L^3\)) ✓;
    \(A\cdot(\omega\times w)=|w|\,w\cdot(\omega\times w)=0\) ✓;
    \(A\cdot(\omega\times q)=|w|\omega\cdot(q\times w)=|w|\omega\cdot(q\times u)\) ✓.
    (3.5): \((A\times\omega)_j=A_k\partial_ju_k-A_k\partial_ku_j\) ✓ by
    \(\varepsilon_{jkl}\varepsilon_{lmn}=\delta_{jm}\delta_{kn}-\delta_{jn}\delta_{km}\);
    \(q\cdot(A\times\omega)=A\cdot((q\cdot\nabla)u)-q\cdot((A\cdot\nabla)u)\) ✓;
    \(\int q\cdot(A\times\omega)=\int A\cdot(\omega\times q)=\mathfrak T\) ✓ and HF17 (9)
    \(\mathfrak T=-\int q\cdot((A\cdot\nabla)u)\) ✓, so
    \(\mathfrak T=\int A\cdot((q\cdot\nabla)u)+\mathfrak T\) ✓.  All pairings are
    \(L^{3/2}\!\cdot\!L^3\!\cdot\!L^\infty\subset L^1\) ✓.
    (3.6): \(u=w-q\) and (3.5) ✓; \(A\cdot((w\cdot\nabla)u)=|w|w_iw_j\partial_iu_j\)
    is symmetric in \(ij\), hence the strain form ✓.
    *Independent second route:* the note's formal cross-check reproduces
    \(\int A\cdot((q\cdot\nabla)u)=-\tfrac13\int|w|^3\operatorname{div}w=0\) by (1.4)
    with \(\alpha=3\) ✓ — I re-derived both steps; they agree with the rigorous
    route, which is genuine (weak) evidence that no sign was dropped in (3.5).
    Its extra hypotheses (\(\nabla|q|^2\in\mathcal G_3\), i.e. \(q\in L^6\)) are not
    available under (H1'), and the note correctly labels it formal.
    The "reading" paragraph ✓: \(\int|u|u\cdot S(u)u=\int u\cdot\nabla(|u|^3/3)=0\);
    \(\hat w\cdot S(u)\hat w=-\operatorname{div}w-\partial_{\hat w\hat w}\varphi
    =-\operatorname{tr}((I+\hat w\otimes\hat w)\nabla^2\varphi)\) ✓; and
    \(\mathfrak T=\int|w|^3\partial_{\hat w\hat w}\varphi\) ✓ using
    \(\int|w|^3\Delta\varphi=\int|w|^3\operatorname{div}w=0\) from (1.4).
14. (3.7) ✓.  Subtracting the \(v\)-parts of (3.5)–(3.6) leaves exactly
    \(\int q\cdot((A\cdot\nabla)v)-\int A\cdot((w\cdot\nabla)v)\); both are bounded
    by \(\|\nabla v\|_\infty\|w\|_3^3\le C2^{5L/2}E_0^{1/2}\cdot3\mathcal Q\) ✓
    with Bernstein \(\|\nabla S_Lu\|_\infty\le C2^{5L/2}\|u\|_2\) ✓.
15. §3.3(a) ✓ as far as it goes.  \(\Delta\Pi_L=-(\partial_jA_i)(\partial_iu^{hi}_j)\)
    ✓ (using \(\operatorname{div}A=\operatorname{div}u^{hi}=0\)), and each term
    \(\nabla A_i\cdot\partial_iu^{hi}\) is curl-free \(\cdot\) divergence-free ✓,
    so CLMS applies in form.  I could reach CLMS (J. Math. Pures Appl. 72 (1993)
    247–286) only as **metadata**, as the note says; the companion fact
    \(I_2:\mathcal H^1(\mathbb R^3)\to L^3\) is the classical Stein–Weiss
    \(I_\alpha:\mathcal H^1\to L^{n/(n-\alpha)}\), confirmed here from **secondary**
    sources only.  Non-load-bearing: route (a) dies at two uncontrolled factors
    regardless, and the cheap bound \(\|\Pi_L\|_{3/2}\le C\|A\|_{3/2}\|u^{hi}\|_\infty\)
    makes the same point without any citation.
16. §3.3(b) ✓.  The weighted Cauchy–Schwarz and \(\int|w|\sigma^2\le D_3^{\rm rad}\)
    are correct; \(\{w=0\}\) contributes nothing since \(\sigma=0\) there ✓.
    Scaling \((a^5,\lambda^2)\) ✓.  Possible infinitude of \(\int|w|^{-1}\Pi_L^2\)
    across the codimension-one zeros of Rmk. 1.2 ✓ (\(\int_0^1t^{-1}dt=\infty\)),
    and the heuristic absorption condition \(|u^{hi}|\lesssim\nu2^L\) is indeed
    a supercritical sup bound ✓ — correctly flagged as the forbidden inference.
17. §3.3(c) ✓ arithmetic: \(|K^S_L|\le(\int|w||\nabla u^{hi}|^2)^{1/2}(\int|w|^5)^{1/2}
    \le C\mathcal Q^{1/3}(D_3^{\rm rad})^{1/2}(\int|w||\nabla u^{hi}|^2)^{1/2}\) ✓,
    and the closure condition \(\mathcal Q^{1/3}\lesssim\theta\nu\), i.e.
    \(\|u\|_3\lesssim\nu\), is hidden smallness ✓.  Obstruction (i) is
    mis-labelled — see Lemma R3.
18. §3.3(d) ✓: \(\operatorname{tr}S=0\) gives \(\lambda_{\min}\le0\le\lambda_{\max}\),
    so \(\hat w\cdot S\hat w\) has no sign; \(\hat w\) is frozen by \(A\), so no
    direction averaging is available ✓.
19. Scaling bookkeeping of §0 ✓ re-derived line by line, including
    \(\nu\sim(a,\lambda^0)\) (amplitude is a symmetry only with \(\nu\mapsto a\nu\))
    and \(\mathcal Q',K_L,\nu D_3\sim(a^4,\lambda^2)\).
20. Circularity sweep: no bound in the note uses \(\|\nabla u\|_\infty\),
    \(\|u\|_\infty\), or \(\sup_t\|u\|_3\) to *prove* anything; where such
    quantities appear (§3.3(a)(b)(c)) they are displayed as the failure ✓.
    No identity is presented as an estimate; the note states three times that
    equivalent rewritings discharge nothing, per PLAN ✓.

## REPLACEMENT ARGUMENT

**Lemma R1 (sign normalisation).**  With \(R_j=\partial_j(-\Delta)^{-1/2}\),
\(\Gamma=-1/(4\pi|x|)\), \(w\in L^3\), \(q=(I-\mathbb P)w\),
\(F=(A\cdot\nabla)u^{hi}\), \(T_{ij}=A_iu^{hi}_j\in L^{3/2}\):
\[
 q=-R(R\cdot w),\qquad
 (I-\mathbb P)F=\nabla\Pi_L\ \text{ with }\
 \Pi_L:=\Delta^{-1}\partial_i\partial_jT_{ij}=-R_iR_jT_{ij},
\]
and, under (H1) with \(\sigma\in L^{3/2}\),
\[
 q=-\nabla(\Gamma*\sigma)=-\frac1{4\pi}\int\frac{x-y}{|x-y|^3}\sigma(y)\,dy .
\]
Consequently (3.2), (3.3) and everything downstream stand **verbatim**, and the
Navier–Stokes aside reads \(p=-R_iR_j(u_iu_j)\) in this convention.

*Proof.*  In the convention \(\hat f(\xi)=\int fe^{-ix\cdot\xi}\), \(R_j\) has
symbol \(i\xi_j/|\xi|\), hence \((R_iR_j)^\wedge=-\xi_i\xi_j/|\xi|^2\) and
\(\mathbb P_{jk}=\delta_{jk}-\xi_j\xi_k/|\xi|^2=\delta_{jk}+R_jR_k\); therefore
\((I-\mathbb P)_{jk}=-R_jR_k\) and \(q=(I-\mathbb P)w=-R(R\cdot w)\).  For the
second, \(\hat F_j=i\xi_i\hat T_{ij}\), so
\([(I-\mathbb P)F]^\wedge_j=(\xi_j\xi_k/|\xi|^2)(i\xi_i\hat T_{ik})
=i\xi_j\,\xi_i\xi_k\hat T_{ik}/|\xi|^2\), which is \((\nabla\Pi_L)^\wedge_j\)
with \(\hat\Pi_L=\xi_i\xi_k\hat T_{ik}/|\xi|^2=-(R_iR_kT_{ik})^\wedge\).  For the
third, \(\Delta\Gamma=\delta\) and \(\operatorname{div}w=-\sigma\) give
\(q=\nabla\Delta^{-1}\operatorname{div}w=-\nabla(\Gamma*\sigma)\), and
\(\nabla\Gamma(x)=x/(4\pi|x|^3)\).  *Check on an exact example:* for
\(w=Cx/|x|^2\) (a gradient, \(u=0\)) one has \(\sigma=-C/|x|^2\); the corrected
kernel returns the Newtonian field of the density \(+C/|y|^2\), which by Gauss
is \(Cx/|x|^2=q\) ✓; the uncorrected kernel returns \(-q\). \(\square\)

**Lemma R2 (corrected Prop. 2.2).**  Let \(w_\delta=|A_\delta|^{-1/2}A_\delta\)
with \(A_\delta=A_0+A_1\) as in the note (\(R^3=\delta^{-2}\), \(k=\delta^{-1/2}\)).
Then for all small \(\delta>0\):
\(w_\delta\in\mathcal M\), \(w_\delta\) is compactly supported, bounded, and
satisfies (H1') — \(w_\delta\in W^{1,1}_{\rm loc}\cap L^3\), \(D_3(w_\delta)<\infty\)
— but is **not** smooth (\(|\nabla w_\delta|\sim d^{-1/2}\) at the zero set of
\(A_\delta\)); and
\[
 D_3(w_\delta)\le C,\quad \tfrac1C\le\mathcal Q(\mathbb Pw_\delta)\le C,\quad
 \|\mathbb Pw_\delta\|_2^2\le C,\quad
 \|\sigma_\delta\|_{3/2}^{3/2}\ge c\,\delta^{-5/4}.
\]
Consequently: **there is no locally bounded** \(\Phi:(0,\infty)^3\to[0,\infty)\)
with \(\|\sigma\|_{3/2}\le\Phi(D_3,\mathcal Q,\|u\|_2^2)\) on \(\mathcal M\).
In particular every power product of §2.3 is refuted, as is every continuous or
monotone \(\Phi\).

*Proof.*  Membership in \(\mathcal M\) is Prop. 1.4 with the smooth compactly
supported solenoidal \(A_\delta=\operatorname{curl}(\cdot\,e_3)\).  Regularity:
\(A_\delta\) is smooth, and \(z\mapsto|z|^{-1/2}z\) is smooth away from \(0\) and
\(\tfrac12\)-Hölder at \(0\); the zero set of \(A_0+A_1\) is (i) the axis
\(\rho=0\) and the sphere \(|x|=1\) for the bulk, (ii) the lines
\(\{\sin kx_1=0\}\cap\{\cos kx_2=0\}\) for the oscillation.  Near (ii)
\(|A_1|\sim k\,d\), so \(|w|\sim(kd)^{1/2}\delta\) and \(|\nabla w|\sim\delta k(kd)^{-1/2}\):
\(|\nabla w|\in L^1_{\rm loc}\) (\(\int_0 d^{-1/2}d\,dd<\infty\)) and
\(|w||\nabla w|^2\sim d^{-1/2}\in L^1_{\rm loc}\); near the axis and near the
sphere the vanishing orders are \(\rho^{1/2}\) and \((1-|x|)^{3/2}\), both above
the \(\beta>1/3\) threshold of Rmk. 1.2.  A continuous function with
\(L^1_{\rm loc}\) gradient off a closed set of Hausdorff codimension \(\ge2\) lies
in \(W^{1,1}_{\rm loc}\); with \(w_\delta\in L^\infty\) compactly supported this
gives (H1') and \(w_\delta\in L^3\).  The four displayed bounds follow from the
exact homogeneity \(w=\delta G(kx)\) on the oscillation (all four cell averages
\(\langle|G|^2\rangle,\langle|G|^3\rangle,\langle|\nabla G|^2|G|\rangle,
\langle|\Sigma|^{3/2}\rangle\) are finite and, for the last, positive because
\(|\nabla\psi|\) is non-constant on \(\{\psi=0\}\)) together with the disjointness
of the two supports and \(\|\mathbb Pw\|_2\le\|w\|_2\).  Finally, suppose
\(\Phi\) is locally bounded and dominates \(\|\sigma\|_{3/2}\) on \(\mathcal M\).
The triples \((D_3,\mathcal Q,\|u\|_2^2)(w_\delta)\) lie in a fixed compact
\(K\subset(0,\infty)^3\); a locally bounded function is bounded on \(K\) (finite
subcover), so \(\|\sigma_\delta\|_{3/2}\le\sup_K\Phi<\infty\), contradicting
\(\|\sigma_\delta\|_{3/2}^{3/2}\ge c\delta^{-5/4}\to\infty\). \(\square\)

*(Why the note's stronger quantifier is not repairable by this family: the
scaling group has two parameters and the constraint set three coordinates, so
the triple cannot be pinned exactly along the family; an arbitrary finite-valued
\(\Phi\) may be unbounded on a compact set.  "Locally bounded" is the honest and
sufficient class.)*

**Lemma R3 (status of the weighted Calderón–Zygmund inequality).**  The
statement
\[
 \int|w|\,|\nabla(I-S_L)\mathbb Pw|^2dx\le C\int|w|\,|\nabla w|^2dx
 \qquad(w\in\mathcal M\cap(\mathrm{H1'}))
 \tag{W}
\]
is **neither proved nor refuted** by the note's argument, and must be recorded
as unavailable rather than false.  (i) The \(A_2\) condition is *sufficient* for
weighted \(L^2\) bounds of Calderón–Zygmund operators; its failure for \(|w|\)
does not refute (W), which is moreover not a bound for an arbitrary input but
for the specific input \(w\) that also defines the weight.  (ii) The note's
witness — \(A\equiv0\) on a ball \(B\), hence \(|w|\equiv0\) on \(B\) — cannot
refute (W): the weight annihilates the integrand of *both* sides on \(B\), so no
inequality is violated there.  (iii) The unweighted analogue is an identity-level
truth (\(\mathbb P\) and \(I-S_L\) are Fourier multipliers of norm \(\le1\), so
\(\int|\nabla(I-S_L)\mathbb Pw|^2\le\int|\nabla w|^2\)), which is why a
counterexample must be produced by the weight alone; I did not find one, and
none is displayed in the note.

*Consequence for the record:* nothing changes.  Even granting (W), the note's
own obstruction (ii) leaves \(|K^S_L|\le C\mathcal Q^{1/3}D_3\), which absorbs into
\(\theta\nu D_3\) only under \(\|u\|_3\lesssim\nu\) — hidden smallness, hence a
falsifier.  Route (c) therefore fails whether or not (W) holds, and the FIRST
GAP sentence should read "…requiring the unproved weighted Calderón–Zygmund
inequality (W) *and* the smallness \(\|u\|_3\lesssim\nu\)". \(\square\)

**Editorial repairs (no proof needed).**  (a) Prop. 1.1 proof: truncate with
\(|DF_R|\le2\min(|z|,R)\).  (b) Prop. 2.1 Remark (b): "sharp" holds on
single-scale fields whose gradient part is comparable to \(w\); it is vacuous
when \(q=0\).  (c) §4 item 3 and item 6 inherit the Lemma R1 signs.

## CONDITIONAL SUFFIX THAT SURVIVES

All of it, with the three corrections above.  Precisely, the following survive
this audit as proved statements with their hypotheses displayed:

* Under (H1): \(\operatorname{div}A=0\) a.e., \(\operatorname{div}w=-\hat w\cdot\nabla|w|\)
  a.e. on \(\{w\ne0\}\), \(\operatorname{div}w=0\) a.e. on \(\{w=0\}\), equivalently
  \(\operatorname{tr}((I+\hat w\otimes\hat w)\nabla w)=0\) a.e.; and (1.4) under its
  integrability hypotheses.  Without (H1), only \(\operatorname{div}w\in W^{-1,3}\)
  and \(q=\nabla\Delta^{-1}\operatorname{div}w\).
* \(\mathcal M=\{|A|^{-1/2}A:A\in L^{3/2},\operatorname{div}A=0\}\) and: \(w\in\mathcal M\)
  \(\iff\) \(w\) is the minimizing representative of \(\mathbb Pw\); \(\mathcal Q(\mathbb Pw)
  =\tfrac13\|A\|_{3/2}^{3/2}\).  (Not an instance of Stern Thm. 2.9; same mechanism.)
* Under (H1) and \(\sigma\in L^{3/2}\): \(q=-\nabla(\Gamma*\sigma)\),
  \(\|q\|_3\le C_{\rm HLS}\|\sigma\|_{3/2}\) (Lemma R1 sign), never better than
  the trivial \(\|q\|_3\le C(3\mathcal Q)^{1/3}\) in controlled quantities.
* Under (H1'): (1.5) and \(\int|q|^2|w|^3\le C\mathcal Q^{2/3}D_3^{\rm rad}(w)\).
* Lemma R2: \(\|\sigma\|_{3/2}\) is not dominated by any locally bounded function
  of \((D_3,\mathcal Q,\|u\|_2^2)\) on \(\mathcal M\).
* At the audited \(L^3\) level, \(u\in H^m\) solenoidal, \(m\ge4\), frozen time:
  \(K_L=\langle\operatorname{div}w,\Pi_L\rangle\) with \(\nabla\Pi_L=(I-\mathbb P)((A\cdot\nabla)u^{hi})\);
  \(\int A\cdot((q\cdot\nabla)u)=0\);
  \(\mathcal Q'+\nu D_{\mathcal Q}=-\int|w|\,w\cdot S(u)\,w=\int|w|\,\omega\cdot(q\times u)\);
  \(|K_L-K^S_L|\le C2^{5L/2}E_0^{1/2}\mathcal Q\).
* The note's own conditional suffix stands as written: **if** \(D_{\mathcal Q}\ge cD_3(w)\)
  **and** \(\int_0^\tau K^S_L\,dt\le\theta\nu\int_0^\tau D_3(w)\,dt+A_{\rm input}\)
  uniformly for \(\tau<\min(H,T_*)\), then HF17 (13)–(14) plus (3.7) and Gronwall
  bound \(\mathcal Q\), hence \(\|u\|_3\).  Neither hypothesis is proved here.
  Dependency status at this commit: \(D_{\mathcal Q}=D_3(w)\) is asserted in the
  sibling lane `hf18-hodge-regularity.md`, which is **not audited** by this
  review; and (H1) is *not* delivered by that lane, whose NON-CLAIMS explicitly
  exclude \(W^{1,1}_{\rm loc}\) regularity of \(w\).  Every (H1)/(H1')-conditional
  item above therefore remains conditional after this wave.

## UNNECESSARY DEPENDENCIES

* CLMS (metadata only) and \(I_2:\mathcal H^1\to L^3\) in §3.3(a): route (a) is
  killed by \(\|\sigma\|_{3/2}\) (Lemma R2) and by \(\|\nabla u^{hi}\|_3\)
  independently of any Hardy-space refinement; the elementary
  \(\|\Pi_L\|_{3/2}\le C\|A\|_{3/2}\|u^{hi}\|_\infty\) makes the same point.
* The numerical table: it verifies exact homogeneity \(w=\delta G(kx)\), which is
  a one-line identity.  Its only non-trivial content is
  \(\langle|\Sigma|^{3/2}\rangle>0\), which I proved analytically above
  (\(|\nabla\psi|\) non-constant on \(\{\psi=0\}\)).  Nothing in Prop. 2.2 depends
  on the computation.
* Prop. 2.1 is not used in any conclusion; §3.3(c) reaches the same bound
  directly from (1.5).  It is a standalone remark.
* Gilbarg–Trudinger Lemmas 7.5/7.7 (from memory) can be replaced by the
  standard \(W^{1,1}_{\rm loc}\) chain rule and \(\nabla f=0\) a.e. on level sets;
  both are textbook and neither is load-bearing beyond (H1).

## NON-CLAIMS

This audit establishes no bound, no sign, and no time-integrated absorption for
\(K_L\), \(K^S_L\) or \(\mathfrak T\); no identification \(D_{\mathcal Q}=D_3(w)\);
no regularity of \(w\) (in particular (H1) and (H1') remain hypotheses, and
Uhlenbeck-type \(p\)-harmonic regularity does not apply because \(w\) is not
closed); no \(L^2\) bound for \(u\mapsto w(u)\); no truth or falsity of the
weighted inequality (W); no continuation criterion, HIGH-STRAIN or
HIGH-PRESSURE theorem, and no global regularity result.  Prop. 2.2/Lemma R2
refutes static inequalities on \(\mathcal M\) only; it says nothing about which
\(w\) occur along Navier–Stokes trajectories.  NS-R3 remains OPEN.

## REOPENING CONDITION

Any one of: (1) a proof or refutation of (W) with the weight tied to the input
(Lemma R3), which would settle route (c) at the level of structure rather than
smallness; (2) an input-only bound for \(\int|w|^{-1}\Pi_L^2\), or a proof that
it is infinite for some \(w\in\mathcal M\cap(\mathrm{H1'})\) with
\(\Pi_L\ne0\) on the codimension-one zero set, which would close route (b) in
one direction or the other; (3) execution of the note's NEXT DISTINCT ACTION —
a family \(A=\operatorname{curl}\Psi\) with \(\hat w\) aligned to the expanding
eigenvector of \(S(\mathbb Pw)\) and \(-\int|w|^3\hat w\cdot S\hat w\gg\nu D_3\)
at bounded \(\mathcal Q\) — which would show no static inequality can close the
gap; (4) an audited proof of (H1) for the minimizer, which would convert every
conditional item above into an unconditional one.
