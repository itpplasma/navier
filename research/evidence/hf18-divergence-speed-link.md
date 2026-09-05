# HF18-B: the divergence–speed link of the minimizing representative

Lane HF18-B, mode REPAIR (second version), 2026-09-05. Second independent audit `hf18-review-divergence-speed-link-r2.md`: PASS with scope corrections S1–S4, applied by the controller on 2026-09-05 (Lemma A in §1.3, Lemma B and explicit lower bounds in Prop. 2.2, hypothesis (H2) in both summaries, three constant/label slips).
Inputs: PLAN.md (frontier packet, HF16–HF17), `hf17-quotient-functional.md`,
`hf17-quotient-evolution.md`, both HF17 reviews (PASS), the frozen first
version of this note (SHA-256 `7cec9020…d545d0`, base `fd1c20e`), its audit
`hf18-review-divergence-speed-link.md` (verdict REPAIR), and the sibling lane
`hf18-hodge-regularity.md` with its audit `hf18-review-hodge-regularity.md`
(verdict PASS).  Source tags: [DI] directly inspected in this programme,
[MO] metadata only or cited from memory, never load-bearing.

**MODE / RESULT: REPAIR.**  Every bridge named in the audit is replaced, and
the note is re-based on the audited HF18-A regularity.  Unconditionally, for
the minimizing representative \(w=u+q\) of a classical solenoidal
\(u\in H^m\), \(m\ge4\): \(V=|w|^{1/2}w\in H^1(\mathbb R^3)\),
\(A=|w|w\in W^{1,3/2}(\mathbb R^3)\), \(D_{\mathcal Q}(u)=D_3(w)\) (audited
input, not re-proved), the pointwise divergence–speed identity
\(\operatorname{div}w=-\hat w\cdot\nabla|w|\) holds a.e. on \(\{w\ne0\}\) in
the approximate-gradient sense, the weighted bounds
\(\int|w|\sigma^2\le\tfrac12D_3(w)\) and
\(\int|q|^2|w|^3\le C\mathcal Q^{2/3}D_3(w)\) hold, and the family of exact
integrals \(\int|w|^\alpha\sigma=0\), \(2\le\alpha\le5\), holds.  The
remaining hypotheses are (H1) \(w\in W^{1,1}_{\rm loc}\), needed to
identify the distribution \(\operatorname{div}w\) with the function \(-\sigma\)
(Lemma A), and (H2) \(\sigma\in L^{3/2}\), which does not follow from (H1) and by
Prop. 2.2 cannot be certified by the controlled quantities; together they gate the potential formula \(q=-\nabla(\Gamma*\sigma)\) and the pairing
form \(K_L=\int\sigma\Pi_L\).  The classification of §2 states exactly which
weighted inequality between \(\|q\|_3\) or \(\int|q|^2|w|^3\) and
\((D_3,\mathcal Q,\text{input})\) is TRUE, FALSE, or OPEN, each with proof or
counterexample family and scaling check.  No control of the high-strain term
follows; the first uncontrolled term is displayed with its scaling.  Every
rewriting here is an equivalent identity and, per PLAN, discharges nothing.

## Repair record (disposition of every audit item)

| Audit item | Disposition here |
|---|---|
| (B1) Riesz sign in (1.1), (1.7), (3.1) | Convention fixed once in §0 and verified by FFT this wave; \(q=-R(R\cdot w)\), kernel sign in (1.7) corrected, \(\Pi_L\) redefined as the exact pressure analogue so that \((I-\mathbb P)F=-\nabla\Pi_L\); signs of (3.2)–(3.3) carried through.  The audit's own aside "\(p=-R_iR_j(u_iu_j)\)" is a slip: with \(R_j=\partial_j(-\Delta)^{-1/2}\), \(p=+R_iR_j(u_iu_j)\) (checked numerically, §0). |
| (B2)(i) quantifier "for any \(\Phi\)" in Prop. 2.2 | Restated for locally bounded \(\Phi\) (audit Lemma R2), which covers every power product and every continuous or monotone \(\Phi\). |
| (B2)(ii) "smooth compactly supported" family | Corrected: bounded, compactly supported, \(W^{1,1}_{\rm loc}\), not smooth (\(|\nabla w|\sim d^{-1/2}\) on the zero lines); (H1) proved for the family. |
| (B2)(iii) "false weighted Calderón–Zygmund inequality" | Reclassified OPEN (audit Lemma R3); moreover shown moot for size bounds, because HF18-A (4.2) bounds \(K\) without it. |
| Prop. 1.1 truncation \(|DF_R|\le2|z|\) | Prop. 1.1 no longer needs a truncation: the identity is now derived algebraically from the audited chain rule for \(A=\Phi(V)\). |
| Prop. 2.1 "sharp on single-scale fields" | Restated: order-sharp on single-scale fields whose gradient part is comparable to \(w\); vacuous when \(q=0\). |
| §4 items 3, 6 signs | Carried through. |
| FIRST GAP sentence | Rewritten per audit Lemma R3 and HF18-A. |
| Gilbarg–Trudinger Lemmas 7.5/7.7 [MO] | Removed; not needed. |
| CLMS and \(I_2:\mathcal H^1\to L^3\) [MO] | Removed; route (a) dies at \(\|\sigma\|_{3/2}\) alone. |
| Conditional suffix "if \(D_{\mathcal Q}\ge cD_3\)" | Discharged by audited HF18-A Theorem 2: \(D_{\mathcal Q}=D_3(w)\). |
| (H1'): \(w\in W^{1,1}_{\rm loc}\), \(w\in L^3\), \(D_3<\infty\) | Reduced to (H1): the last two are now unconditional (HF18-A). |

## 0. Setting, audited inputs, conventions

\(\mathcal G_3\), \(\mathcal Q\), \(w=u+q\), \(A=|w|w\), \(\mathbb P\) as in
HF17.  Throughout, \(u\in H^m(\mathbb R^3;\mathbb R^3)\), \(m\ge4\), solenoidal
(a frozen time of a classical solution); nothing below uses decay of \(u\)
beyond this.

**Audited HF17 input (PASS).** \(A\in L^{3/2}\), \(\int A\cdot g=0\) for
\(g\in\mathcal G_3\), \(u=\mathbb Pw\), \(q=(I-\mathbb P)w\),
\(\|q\|_3\le(1+C_3)\|w\|_3\), \(\|w\|_3^3=3\mathcal Q\),
\(D\mathcal Q(u)[h]=\int A\cdot h\), and on the classical interval
\(\mathcal Q'+\nu D_{\mathcal Q}=\mathfrak T\), \(\mathfrak T=-\int A\cdot((u\cdot\nabla)u)
=-\int q\cdot((A\cdot\nabla)u)\) (inner variation, HF17 (9)), \(D_{\mathcal Q}:=-\int A\cdot\Delta u\ge0\).

**Audited HF18-A input (PASS; cited, not re-proved).** With
\(V:=|w|^{1/2}w\), \(\Phi(V)=|V|^{1/3}V\), \(\Psi(V)=|V|^{-1/3}V\)
(\(\Psi(0)=0\)), so that \(A=\Phi(V)\), \(w=\Psi(V)\):
\[
 \text{(A1)}\quad V\in H^1(\mathbb R^3),\qquad \|V\|_2^2=3\mathcal Q,\qquad
 \|\partial_kV\|_2\le\tfrac92\|w\|_3^{1/2}\|\partial_ku\|_3 ;
\]
\[
 \text{(A2)}\quad A\in W^{1,3/2}(\mathbb R^3),\quad \nabla A=D\Phi(V)\nabla V\ \text{a.e.},\quad
 \|\nabla A\|_{3/2}\le\tfrac43\|w\|_3^{1/2}\|\nabla V\|_2,\quad \operatorname{div}A=0\ \text{a.e.};
\]
\[
 \text{(A3)}\quad w\in L^3\cap L^9\cap B^{2/3}_{3,\infty},\quad u\in L^9,\quad
 \|w\|_9^{3/2}=\|V\|_6\le S\|\nabla V\|_2 ;
\]
\[
 \text{(A4)}\quad D_{\mathcal Q}(u)=D_3(w):=\int\Big(|\nabla V|^2-\tfrac19|\nabla|V||^2\Big)dx,
 \qquad \tfrac89\|\nabla V\|_2^2\le D_3(w)\le\|\nabla V\|_2^2 ;
\]
\[
 \text{(A5)}\quad \mathcal Q'+\nu D_3(w)=K,\quad
 K=\mathfrak T=-\int q\cdot((u\cdot\nabla)A)=-\int q\cdot(I-\mathbb P)[(u\cdot\nabla)A],\quad
 |K|\le C_*\mathcal Q^{1/3}D_3(w),
\]
\(C_*=\tfrac32 3^{1/3}(1+C_3)C_9S\).  On \(\{V\ne0\}=\{w\ne0\}\) the field
\(w=\Psi(V)\) has the approximate gradient
\[
 \nabla w:=D\Psi(V)\nabla V,\qquad D\Psi(V)=|V|^{-1/3}\big(I-\tfrac13\hat V\otimes\hat V\big),
 \qquad |\nabla w|\le|w|^{-1/2}|\nabla V| ,
\]
and on \(\{w\ne0\}\) the integrand identity
\(|\nabla V|^2-\tfrac19|\nabla|V||^2=|w||\nabla w|^2+|w||\nabla|w||^2\) holds
(HF18-A (1.12)), so \(D_3(w)\) is the quantity of that name in the first
version, with \(\nabla w\) read as the approximate gradient and the integrand
\(0\) a.e. on \(\{w=0\}\) (where \(\nabla V=0\) a.e.).  Whether this
approximate gradient is a distributional gradient is exactly

**Hypothesis (H1).** \(w\in W^{1,1}_{\rm loc}(\mathbb R^3;\mathbb R^3)\).

(H1) is not proved (HF18-A NON-CLAIMS, audited).  The first version's (H1')
was "(H1) and \(w\in L^3\) and \(D_3(w)<\infty\)"; by (A1), (A4) it is now
equivalent to (H1).  Every statement below is unconditional unless marked
"under (H1)".

**Notation.** \(\hat w=w/|w|\) on \(\{w\ne0\}\);
\[
 \sigma:=\hat w\cdot\nabla|w|=\hat w_i\hat w_j\partial_iw_j\ \text{ on }\{w\ne0\},\qquad
 \sigma:=0\ \text{ on }\{w=0\},
\]
the *radial speed derivative*, with \(\nabla|w|:=\hat w\cdot\nabla w\) the
approximate gradient of \(|w|=|V|^{2/3}\).  Also
\(D_3^{\rm rad}(w):=\int|w||\nabla|w||^2=\tfrac49\|\nabla|V|\|_2^2\).

**Riesz convention (fixed once; verified numerically this wave).**
\(\hat f(\xi)=\int fe^{-ix\cdot\xi}\); \(R_j=\partial_j(-\Delta)^{-1/2}\) has
symbol \(i\xi_j/|\xi|\); hence \((R_iR_j)^\wedge=-\xi_i\xi_j/|\xi|^2\),
\(R_iR_j=\partial_i\partial_j(-\Delta)^{-1}\),
\[
 \mathbb P_{jk}=\delta_{jk}+R_jR_k,\qquad (I-\mathbb P)_{jk}=-R_jR_k
 =\partial_j\Delta^{-1}\partial_k,\qquad
 p_{\rm NS}=R_iR_j(u_iu_j),\quad -\nabla p_{\rm NS}=(I-\mathbb P)[(u\cdot\nabla)u].
\]
(FFT check on \(u=(\sin y,\sin x,0)\): \((u\cdot\nabla)u=\nabla(-\cos x\cos y)\),
\(p=\cos x\cos y=\sum R_iR_j(u_iu_j)\) to \(10^{-15}\); \(-R(R\cdot g)=g\) on a
gradient \(g\) to \(10^{-15}\).  Scratch `riesz_sign.py`.)  The audit's
Lemma R1 is correct for \(q\), \(\Pi_L\) and the kernel, and its closing aside
on \(p\) has the wrong sign.

**Scaling bookkeeping.** \((a,\lambda)\) denotes amplitude \(w\mapsto aw\)
and dilation \(w\mapsto\lambda w(\lambda\cdot)\); both map \(\mathcal M\)
(§1.4) to itself.  \(\mathcal Q\sim(a^3,\lambda^0)\), \(D_3\sim(a^3,\lambda^2)\),
\(E=\|u\|_2^2\sim(a^2,\lambda^{-1})\), \(\|q\|_3^3\sim(a^3,\lambda^0)\),
\(\|\sigma\|_{3/2}^{3/2}\sim(a^{3/2},\lambda^0)\),
\(\int|w|\sigma^2\sim(a^3,\lambda^2)\), \(\int|q|^2|w|^3\sim(a^5,\lambda^2)\),
\(\int|w|^5\sim(a^5,\lambda^2)\), \(\|\nabla A\|_{3/2}\sim(a^2,\lambda)\),
\(\|\nabla V\|_2\sim(a^{3/2},\lambda)\), \(\|\nabla u\|_3\sim(a,\lambda)\),
\(2^L\sim(1,\lambda)\); for the evolution \(\nu\sim(a,\lambda^0)\) (amplitude
is a Navier–Stokes symmetry only with \(\nu\mapsto a\nu\)), rates
\(\mathcal Q',K,K_L,\nu D_3\sim(a^4,\lambda^2)\).  For *static* inequalities
on \(\mathcal M\), \(\nu\) and \(H\) are inert constants: \(\mathcal M\) is a
cone and dilation-invariant, so a static inequality must hold along both
one-parameter families with the same constant.

## 1. The pointwise identity: exact scope

### 1.1 Distributional statement (no hypothesis)

The audited Euler condition is \(\operatorname{div}A=0\) in \(\mathcal D'\)
with \(A\in L^{3/2}\).  Since \(\operatorname{div}u=0\),
\[
 \operatorname{div}q=\operatorname{div}w\in W^{-1,3}(\mathbb R^3),\qquad
 q=(I-\mathbb P)w=\nabla\Delta^{-1}\operatorname{div}w=-R(R\cdot w).   \tag{1.1}
\]
This is the whole content at the \(L^3\) level.  A pointwise identity with
\(\nabla w\) needs a gradient of \(w\) in some sense; (A1)–(A2) provide the
approximate gradient on \(\{w\ne0\}\), and (H1) would provide the distributional
one.  Mollification produces neither, because
\(\operatorname{div}(|w_\varepsilon|w_\varepsilon)\ne(\operatorname{div}(|w|w))_\varepsilon\).

### 1.2 The identity on \(\{w\ne0\}\) (unconditional)

**Proposition 1.1.** Let \(F(z)=|z|z\), \(DF(z)=|z|I+z\otimes\hat z\).
Then a.e. on \(\{w\ne0\}\), with \(\nabla w\) the approximate gradient:
\[
 \partial_iA_j=|w|\,\partial_iw_j+w_j\,\partial_i|w|,\qquad
 \partial_i|w|=\hat w_k\partial_iw_k=\tfrac23|V|^{-1/3}\partial_i|V|,        \tag{1.2}
\]
\[
 \boxed{\ \operatorname{div}w=-\hat w\cdot\nabla|w|=-\sigma,\qquad
 \text{equivalently}\quad\operatorname{tr}\big((I+\hat w\otimes\hat w)\nabla w\big)=0\ }
                                                                    \tag{1.3}
\]
where \(\operatorname{div}w:=\operatorname{tr}\nabla w\).  Moreover
\[
 |w|^{1/2}\sigma=\tfrac23\,\hat V\cdot\nabla|V|\in L^2,\qquad
 \int|w|\sigma^2\,dx\le\tfrac49\|\nabla|V|\|_2^2=D_3^{\rm rad}(w)\le\tfrac12D_3(w).
                                                                    \tag{1.3'}
\]
*Proof.* On \(\mathbb R^3\setminus\{0\}\), \(\Phi=F\circ\Psi\) with both maps
\(C^1\), so \(D\Phi(V)=DF(\Psi(V))\,D\Psi(V)\) as matrices; by (A2),
\(\nabla A=D\Phi(V)\nabla V=DF(w)\,(D\Psi(V)\nabla V)=DF(w)\nabla w\) a.e. on
\(\{V\ne0\}\), which is (1.2) componentwise; the second form of
\(\partial_i|w|\) is \(|w|=|V|^{2/3}\) with \(\nabla|V|=\hat V\cdot\nabla V\)
(Lipschitz composition, \(|V|\in H^1\)), and it agrees with
\(\hat w\cdot\partial_iw=|V|^{-1/3}(1-\tfrac13)\hat V\cdot\partial_iV\).
Taking the trace of (1.2): \(\operatorname{div}A=|w|\operatorname{div}w+w\cdot\nabla|w|
=|w|(\operatorname{div}w+\sigma)\), and \(\operatorname{div}A=0\) a.e. by (A2);
divide by \(|w|\).  The trace form is \(\hat w\cdot\nabla|w|=\hat w_i\hat w_k\partial_iw_k\).
For (1.3'): \(|w|^{1/2}\sigma=|V|^{1/3}\cdot\tfrac23|V|^{-1/3}\hat V\cdot\nabla|V|\);
then \(\int|w|\sigma^2\le\tfrac49\int|\nabla|V||^2\le\tfrac49\|\nabla V\|_2^2
\le\tfrac49\cdot\tfrac98D_3\) by (A4). \(\square\)

Scaling of (1.3'): both sides \((a^3,\lambda^2)\).  Independent checks on
exact solutions of \(\operatorname{div}(|w|w)=0\) (local, away from the
origin; not in \(L^3\)): \(w=Cx/|x|^2\) has \(|w|w=C|C|x/|x|^3\),
\(\operatorname{div}w=C/|x|^2\), \(\sigma=\partial_r(|C|/r)\operatorname{sgn}C=-C/r^2\)
✓; constant speed \(|w|\equiv c\) forces \(\operatorname{div}w=0\) ✓.

**Remark 1.2 (zero set).** (1.3) carries no information on \(\{w=0\}\), where
\(\nabla V=0\) a.e. and the approximate gradient of \(w\) is not defined by
(A1)–(A2).  Nothing prevents \(\{w=0\}\) from containing hypersurfaces: if
\(A=\operatorname{curl}(\psi e_3)\) with \(\psi=-x_1^3/3\) near \(x_1=0\) then
\(A=(0,x_1^2,0)\), \(\operatorname{div}A=0\), \(|w|=|x_1|\).  Near a
codimension-one zero with \(|w|\sim\operatorname{dist}^\beta\), local finiteness
of \(\int|w||\nabla|w||^2\sim\int d^{3\beta-2}\) and of
\(\int|\sigma|^{3/2}\sim\int d^{3(\beta-1)/2}\) have the same threshold
\(\beta>1/3\); the failure of control in §2.3 is not a zero-set effect.

**Remark 1.3 (exact integrals, unconditional).** For \(2\le\alpha\le5\),
\[
 \int_{\{w\ne0\}}|w|^\alpha\,\sigma\,dx=0,\qquad\text{equivalently}\quad
 \int|w|^\alpha\operatorname{div}w\,dx=0 .                          \tag{1.4}
\]
*Proof.* \(|w|^\alpha w=|V|^\beta V=:\Phi_\beta(V)\), \(\beta=(2\alpha-1)/3\in[1,3]\).
\(\Phi_\beta\in C^1\), \(|D\Phi_\beta(V)|\le(1+\beta)|V|^\beta\), and
\(|V|^\beta\in L^2\), \(|V|^{\beta+1}\in L^1\) because \(V\in L^2\cap L^6\);
the same mollification argument as HF18-A Corollary 1(c) (audited there for \(\beta=\tfrac13\)), re-run for \(\beta\in[1,3]\) where \(|V|^\beta\) converges in \(L^2_{\rm loc}\) because \(2\beta\le6\), gives (with absolute convergence \(|w|^{\alpha-1/2}\in L^2\iff\alpha\in[2,5]\))
\(\Phi_\beta(V)\in W^{1,1}(\mathbb R^3)\) with \(\nabla\Phi_\beta(V)=D\Phi_\beta(V)\nabla V\)
a.e., and \(\int\partial_if=0\) for \(f\in W^{1,1}(\mathbb R^3)\).  On
\(\{w\ne0\}\), by (1.2)–(1.3),
\(\operatorname{div}(|w|^\alpha w)=|w|^\alpha\operatorname{div}w+\alpha|w|^{\alpha-1}w\cdot\nabla|w|
=|w|^\alpha(\operatorname{div}w+\alpha\sigma)=(\alpha-1)|w|^\alpha\sigma\);
on \(\{w=0\}\) the gradient vanishes a.e. \(\square\)

The case \(\alpha=3\) is used in §3.2.  (The first version stated (1.4) under
(H1) with integrability hypotheses; both are now unnecessary.)

### 1.3 What (H1) adds

By Lemma A below, under (H1) the weak gradient of \(w\) equals \(D\Psi(V)\nabla V\)
a.e. on \(\{w\ne0\}\) and vanishes a.e. on \(\{w=0\}\), the distributional
divergence of \(w\) is its a.e. divergence, and therefore
\[
 \operatorname{div}w=-\sigma\quad\text{in }\mathcal D'(\mathbb R^3),\qquad
 \sigma\in L^1_{\rm loc}.                                          \tag{1.3''}
\]

**Lemma A (identification of the weak gradient under (H1); supplied by the second audit).**
Let \(w\in L^3(\mathbb R^3;\mathbb R^3)\) with \(V=|w|^{1/2}w\in H^1(\mathbb R^3)\)
(audited (A1)), and assume (H1) \(w\in W^{1,1}_{\rm loc}\). Then the weak gradient
\(\nabla^{\!w}w\) satisfies \(\nabla^{\!w}w=D\Psi(V)\nabla V\) a.e. on \(\{w\ne0\}\)
and \(\nabla^{\!w}w=0\) a.e. on \(\{w=0\}\); hence \(\operatorname{div}w=-\sigma\)
a.e. and, \(w\) being \(W^{1,1}_{\rm loc}\), also in \(\mathcal D'(\mathbb R^3)\),
with \(\sigma\in L^1_{\rm loc}\).

*Proof.* Put \(\Theta(z)=|z|^{1/2}z\), so \(V=\Theta(w)\), \(w=\Psi(V)\),
\(D\Theta(z)=|z|^{1/2}(I+\tfrac12\hat z\otimes\hat z)\) with eigenvalues
\(|z|^{1/2},|z|^{1/2},\tfrac32|z|^{1/2}\); a direct multiplication gives
\(D\Psi(\Theta(z))=D\Theta(z)^{-1}\) for \(z\ne0\). By the Calderón–Zygmund
theorem a \(W^{1,1}_{\rm loc}\) function is approximately differentiable a.e.,
with approximate differential equal to its weak gradient a.e.; apply this to
\(w\) and to \(V\in H^1\subset W^{1,1}_{\rm loc}\), and let \(x_0\) be a point of
approximate differentiability and approximate continuity of both with
\(w(x_0)\ne0\) (a.e. point of \(\{w\ne0\}\) is such). Since \(\Theta\) is \(C^1\),
hence Lipschitz, on a neighbourhood of \(w(x_0)\), and \(\{|w-w(x_0)|>\eta\}\) has
density \(0\) at \(x_0\), the composition \(V=\Theta(w)\) is approximately
differentiable at \(x_0\) with approximate differential
\(D\Theta(w(x_0))\nabla^{\!w}w(x_0)\). Approximate differentials are unique, so
\(\nabla V(x_0)=D\Theta(w(x_0))\nabla^{\!w}w(x_0)\), i.e.
\(\nabla^{\!w}w(x_0)=D\Psi(V(x_0))\nabla V(x_0)\). On \(\{w=0\}\), a.e. point is a
point of density one, and at such a point of approximate differentiability with
\(w(x_0)=0\) the approximate differential vanishes. Taking the trace of the first
identity and using Prop. 1.1 gives \(\operatorname{div}w=-\sigma\) a.e.; for
\(w\in W^{1,1}_{\rm loc}\) the distributional divergence is the a.e. trace of the
weak gradient. \(\square\)
Without (H1), (1.3) is a statement about \(D\Psi(V)\nabla V\) and says nothing
about the distribution \(\operatorname{div}w\in W^{-1,3}\) of (1.1).  This is
the only place where (H1) enters the note.

### 1.4 The minimizer class is linear in \(A\)

**Proposition 1.4.** Let \(\mathcal M:=\{w\in L^3:\operatorname{div}(|w|w)=0\text{ in }\mathcal D'\}\).
Then
\[
 \mathcal M=\{\,|A|^{-1/2}A:\ A\in L^{3/2}(\mathbb R^3;\mathbb R^3),\ \operatorname{div}A=0\text{ in }\mathcal D'\,\},
                                                                    \tag{1.6}
\]
and every \(w\in\mathcal M\) is the minimizing representative of the solenoidal
field \(u=\mathbb Pw\), with \(q=(I-\mathbb P)w\) and
\(\mathcal Q(\mathbb Pw)=\tfrac13\|A\|_{3/2}^{3/2}\).  Conversely
\(w(u)\in\mathcal M\) for every solenoidal \(u\in L^3\).

*Proof* (audited ✓ in the first version; reproduced).  \(z\mapsto|z|z\) is a
bijection \(L^3\to L^{3/2}\) with inverse \(a\mapsto|a|^{-1/2}a\) and
\(\|w\|_3^3=\|A\|_{3/2}^{3/2}\), giving (1.6).  For \(w\in\mathcal M\) put
\(u=\mathbb Pw\), \(q=(I-\mathbb P)w\).  Claim: \((I-\mathbb P)L^3\subset\mathcal G_3\).
For \(f\in C_c^\infty\), \((I-\mathbb P)f=\nabla\psi\) with
\(\psi=\partial_i(\Gamma*f_i)\), \(\Gamma=-1/(4\pi|x|)\); \(\psi\) is smooth,
\(\psi=O(|x|^{-2})\), \(\nabla\psi=O(|x|^{-3})\), so \(\psi,\nabla\psi\in L^3\)
and the HF17 cutoff argument (\(\|\psi\nabla\chi_R\|_3\le CR^{-1}\|\psi\|_{L^3(R\lesssim|x|\lesssim2R)}\to0\))
gives \(\nabla\psi\in\mathcal G_3\); density of \(C_c^\infty\) in \(L^3\) and
\(L^3\)-boundedness of \(I-\mathbb P\) extend this.  Hence \(q\in\mathcal G_3\),
\(u=w-q\) is solenoidal, and \(\int|w|w\cdot g=0\) for all \(g\in\mathcal G_3\)
(compact gradients, then density, \(|w|w\in L^{3/2}\)).  The functional
\(q'\mapsto\tfrac13\int|u+q'|^3\) is convex and Gâteaux differentiable on
\(\mathcal G_3\); a stationary point is a global minimizer, and HF17 gives
uniqueness.  The converse is HF17 (5). \(\square\)

**Scope note.** The one-form, *closed*-form analogue — the unique
\(L^p\)-minimizer \(h\) in a reduced cohomology class satisfies
\(d^*(|h|^{p-2}h)=0\) — is Stern, *\(L_p\)-cohomology and the geometry of
\(p\)-harmonic forms*, arXiv:2403.19481v2, Lemma 2.2 and Theorem 2.9
(Nonlinear Hodge Theorem) [DI, pp. 3–4; labelling confirmed by the audit], who
credits Scott 1995 and Iwaniec–Scott–Stroffolini 1999 [MO].  Our \(w\) is not
closed (\(\operatorname{curl}w=\operatorname{curl}u\ne0\)), so Prop. 1.4 is
not an instance of Stern's theorem; only the convexity mechanism is shared, and
no novelty is claimed.  Stern §3 records (via Uhlenbeck [MO]) smoothness of
\(p\)-harmonic forms where nonzero, for forms that are *both* closed and
\(p\)-coclosed; \(w\) is only the latter, so no regularity transfers.  The
Iwaniec–Martin \(L^p\) Hodge decomposition [MO] is not needed: the splitting
\(L^3=\mathbb PL^3\oplus\mathcal G_3\) is proved above through Riesz transforms.

Practical consequence of (1.6): test fields in the minimizer class are
produced *linearly* by choosing any solenoidal \(A\) (e.g.
\(A=\operatorname{curl}\Psi\), \(\Psi\in C_c^\infty\)); this is how §2.3
builds its family, and \((a,\lambda)\) act on \(\mathcal M\) through
\(A\mapsto a^2A\), \(A\mapsto\lambda^2A(\lambda\cdot)\).

### 1.5 The link \(q\leftrightarrow\sigma\) (under (H1))

Under (H1) and \(\sigma\in L^{3/2}\): by (1.3''), \(\operatorname{div}w=-\sigma\in L^{3/2}\), and
\[
 q=\nabla\Delta^{-1}\operatorname{div}w=-\nabla(\Gamma*\sigma)
 =-\frac1{4\pi}\int\frac{x-y}{|x-y|^3}\,\sigma(y)\,dy,\qquad \Gamma=-\frac1{4\pi|x|},\ \nabla\Gamma=\frac{x}{4\pi|x|^3},
                                                                    \tag{1.7}
\]
as \(L^3\) functions.  The right side lies in \(L^3\) by Hardy–Littlewood–Sobolev
(\(I_1:L^{3/2}(\mathbb R^3)\to L^3\), exponent \(\tfrac13=\tfrac23-\tfrac13\);
Lieb–Loss *Analysis* Thm 4.3 / Stein *Singular Integrals* Ch. V §1 [MO]; the
exponent is forced by scaling and the same bound follows from Calderón–Zygmund
\(\|\nabla^2\Delta^{-1}\sigma\|_{3/2}\le C\|\sigma\|_{3/2}\) plus Sobolev
\(W^{1,3/2}\subset L^3\)), is a gradient, and has divergence
\(-\sigma=\operatorname{div}q\); the difference with \(q\) is a curl-free,
divergence-free \(L^3\) field, hence zero.  Sign check on the exact example
\(w=Cx/|x|^2\) (\(u=0\), \(q=w\), \(\sigma=-C/r^2\)): the kernel in (1.7)
returns the Newtonian field of the density \(+C/|y|^2\), which by Gauss is
\(Cx/|x|^2=q\) ✓; the first version's kernel returned \(-q\).  Hence
\[
 \|q\|_3\le C_{\rm HLS}\|\sigma\|_{3/2}\qquad[(a,\lambda)\text{: both sides }(a,\lambda^0)].
                                                                    \tag{1.8}
\]
Under (1.6): \(q\) is the gradient part of the "square root" \(|A|^{-1/2}A\) of a
solenoidal field, driven by the transport of the speed along its own
direction, \(|w|\sigma=(w\cdot\nabla)|w|\).

## 2. Weighted inequalities: exact classification

The controlled quantities are \(\mathcal Q\) (the functional), \(D_3(w)\)
(the dissipation, \(=D_{\mathcal Q}\) by (A4)), and the inputs \(E_0\ge\|u\|_2^2=:E\),
\(\nu\), \(H\), \(2^L\).  A static inequality on \(\mathcal M\) can involve
only \(\mathcal Q,D_3,E,2^L\) nontrivially (§0).  Throughout, a "witness" is
any \(w_\star\in\mathcal M\) with \(q_\star\ne0\), \(0<D_3(w_\star)<\infty\),
\(E(w_\star)<\infty\); the family of §2.3 at any fixed \(\delta\) is one
(it satisfies (H1) and \(\sigma\not\equiv0\), so \(\operatorname{div}q=\operatorname{div}w=-\sigma\not\equiv0\)).

### 2.1 \(\|q\|_3\)

Exponent lattice for \(\|q\|_3^3\le CD_3^a\mathcal Q^bE^c2^{Ld}\):
\((3,0)=a(3,2)+b(3,0)+c(2,-1)+d(0,1)\), i.e. \(3a+3b+2c=3\), \(2a-c+d=0\).

* **TRUE (trivial).** \(\|q\|_3\le(1+C_3)\|w\|_3=(1+C_3)(3\mathcal Q)^{1/3}\)
  (audited HF17).  Scaling \((a,\lambda^0)\) both sides.
* **FALSE: every bound without \(E\) that vanishes as \(D_3\to0\).**  For any
  \(\Phi:[0,\infty)^2\to[0,\infty]\) with \(\|q\|_3^3\le\Phi(D_3(w),\mathcal Q(\mathbb Pw))\)
  on \(\mathcal M\) one has \(\liminf_{D\downarrow0}\Phi(D,\mathcal Q_\star)\ge\|q_\star\|_3^3>0\).
  *Proof.* Dilate the witness: \(w_\lambda=\lambda w_\star(\lambda\cdot)\in\mathcal M\),
  \(\|q_\lambda\|_3=\|q_\star\|_3\), \(\mathcal Q\) fixed,
  \(D_3(w_\lambda)=\lambda^2D_3(w_\star)\to0\) as \(\lambda\to0\). \(\square\)
  In particular every monomial with \(a>0\), \(c=0\) (any \(d\), since \(2^L\)
  is fixed by the input and does not move with \(\lambda\)) is false, and the
  dissipation gives no improvement over the trivial bound at coarse scales.
* **OPEN: the mixed family \(a>0\), \(c=2a\), \(7a+3b=3\).**  Its extreme
  member is Gagliardo–Nirenberg on \(g=|w|^{3/2}=|V|\in H^1\)
  (\(\|g\|_2\le\|g\|_{4/3}^{4/7}\|g\|_6^{3/7}\), interpolation identity
  \(\tfrac12=\tfrac47\cdot\tfrac34+\tfrac37\cdot\tfrac16\)):
  \[
   \|w\|_3^3\le C\,\|w\|_2^{12/7}\,(D_3^{\rm rad})^{3/7}\qquad
   [(a^3,\lambda^0)=(a^{12/7},\lambda^{-6/7})(a^{9/7},\lambda^{6/7})\ ✓],   \tag{2.1}
  \]
  true whenever \(w\in L^2\), but with \(\|w\|_2\), not \(\|u\|_2\).  Only
  \(\|u\|_2\le\|w\|_2\) is available (\(\mathbb P\) is \(L^2\)-orthogonal).
  Whether \(\|w(u)\|_2\le C\|u\|_2\) — an \(L^2\) bound for the nonlinear
  projection, or even \(w\in L^2\) — is open; no proof or counterexample was
  found.  (Where to look for a counterexample: outside \(\operatorname{supp}u\),
  \(q=\nabla\phi\) with \(\operatorname{div}(|\nabla\phi|\nabla\phi)=0\), an
  exterior 3-Laplace problem in \(\mathbb R^3\); \(L^2\) of \(q\) needs gradient
  decay faster than \(|x|^{-3/2}\), and the decay exponents of exterior
  3-harmonic gradients were not checked this wave.)  Even if true, (2.1)
  integrated in time gives \(\int\mathcal Q^{7/3}dt\lesssim\sup\|w\|_2^4\int D_3\,dt\),
  a supercritical bound of the same type as \(u\in L^{10/3}_{t,x}\) from energy;
  it would not supply a critical coefficient.

### 2.2 \(\int|q|^2|w|^3\)

Exponent lattice: \((5,2)=a(3,2)+b(3,0)+c(2,-1)\) gives \(a=1+c/2\),
\(b=\tfrac23-\tfrac76c\), \(0\le c\le\tfrac47\) (for \(b\ge0\)).

* **TRUE (unconditional): the energy-free member.**

  **Proposition 2.1.**
  \[
   \boxed{\ \int|q|^2|w|^3\,dx\ \le\ (1+C_3)^2S^2\,\|w\|_3^2\,\|\nabla V\|_2^2
   \ \le\ \tfrac98(1+C_3)^2S^2\,(3\mathcal Q)^{2/3}\,D_3(w),\ }                \tag{2.2}
  \]
  and also \(\le\tfrac94(1+C_3)^2S^2(3\mathcal Q)^{2/3}D_3^{\rm rad}(w)\).
  *Proof.* \(\int|q|^2|w|^3=\|q|V|\|_2^2\le\|q\|_3^2\||V|\|_6^2
  \le(1+C_3)^2\|w\|_3^2S^2\|\nabla|V|\|_2^2\), Hölder \(\tfrac23+\tfrac13=1\),
  Sobolev on \(|V|\in H^1\), \(\|\nabla|V|\|_2\le\|\nabla V\|_2\), (A4). \(\square\)
  Scaling \((a^5,\lambda^2)\) on both sides ✓.  Remarks. (a) No divergence
  structure is used: (2.2) holds for every \(w\in L^3\) with \(|w|^{3/2}\in H^1\)
  and any \(q\) with \(\|q\|_3\le C\|w\|_3\); it is not evidence about
  \(\mathcal M\).  (b) Order-sharp on single-scale fields whose gradient part is
  comparable to \(w\) (\(|w|\sim\varepsilon\), \(|q|\sim\varepsilon\), scale
  \(R\): both sides \(\sim\varepsilon^5R^3\)); vacuous when \(q=0\).
  (c) (2.2) is the second factor of the Cauchy–Schwarz split of \(K_L\)
  (§3.3(c)); its consequence there is a small-data closure only.
* **FALSE: every monomial off the line \(a=1+c/2\), \(b=\tfrac23-\tfrac76c\)**, by
  the two-parameter scaling of the witness (\(a\to0,\infty\) or \(\lambda\to0,\infty\)
  refutes any exponent mismatch, since the left side is \(>0\) and finite).
* **OPEN: members with \(c>0\)**, for the reason of §2.1 (they need
  \(\|w\|_2\lesssim\|u\|_2\)).

### 2.3 \(\|\sigma\|_{3/2}\): FALSE for every locally bounded majorant

Exponent lattice: \((\tfrac32,0)=a(3,2)+b(3,0)+c(2,-1)\): \(c=2a\), \(7a+3b=\tfrac32\).
All members, and every other locally bounded function of \((D_3,\mathcal Q,E)\),
are refuted:

**Proposition 2.2 (audit Lemma R2 form).** There is a family
\(w_\delta\in\mathcal M\), \(\delta\downarrow0\), of bounded, compactly
supported fields satisfying (H1) — but *not* smooth: \(|\nabla w_\delta|\sim d^{-1/2}\)
at the zero lines of \(A_\delta\) — with
\[
 D_3(w_\delta)\le C,\qquad \tfrac1C\le\mathcal Q(\mathbb Pw_\delta)\le C,\qquad
 \|\mathbb Pw_\delta\|_2^2\le C,\qquad
 \|\sigma_\delta\|_{3/2}^{3/2}\ \ge\ c\,\delta^{-5/4}\to\infty .
\]
Consequently there is **no locally bounded** \(\Phi:(0,\infty)^3\to[0,\infty)\)
with \(\|\sigma\|_{3/2}\le\Phi(D_3,\mathcal Q,\|u\|_2^2)\) on \(\mathcal M\);
in particular no power product (either sign of \(b\)) and no continuous or
monotone \(\Phi\).  (The first version's quantifier "for any function
\(\Phi\)" is not obtained by this family: the triples move in a compact set
but are not pinned, and an arbitrary finite-valued \(\Phi\) may be unbounded
there.  "Locally bounded" is the honest and sufficient class.)

*Construction.* Bulk: \(A_0=\operatorname{curl}(\phi_0e_3)\), \(\phi_0=(1-|x|^2)^4_+\),
so \(A_0=8(1-|x|^2)^3_+(-x_2,x_1,0)\), \(|A_0|=8(1-|x|^2)^3_+\rho\) (\(\rho\) the
cylindrical radius) and
\(w_0=|A_0|^{-1/2}A_0=\sqrt8(1-|x|^2)^{3/2}_+\rho^{-1/2}(-x_2,x_1,0)\), an
azimuthal field with \(\varphi\)-independent speed: \(w_0\) is solenoidal,
\(q_0=0\), \(\sigma_0\equiv0\), \(u_0=w_0\), \(\mathcal Q(u_0)=\tfrac13\|w_0\|_3^3>0\).
Oscillation: at a centre \(x_0\) with \(B_R(x_0)\cap B_1=\emptyset\),
\[
 A_1=\operatorname{curl}(\psi e_3),\qquad
 \psi(x)=\delta^2(2+\cos kx_1)\frac{\sin kx_2}{k}\,\chi\Big(\frac{x-x_0}{R}\Big),
\]
so that away from the cutoff annulus
\(A_1=\delta^2\big((2+\cos kx_1)\cos kx_2,\ \sin kx_1\sin kx_2,\ 0\big)\)
(\(\operatorname{curl}(\psi e_3)=(\partial_2\psi,-\partial_1\psi,0)\) ✓).
Set \(A_\delta=A_0+A_1\), \(w_\delta=|A_\delta|^{-1/2}A_\delta\in\mathcal M\) by (1.6);
on the disjoint supports \(w_\delta=w_0+w_1\).

*Regularity, (H1).* \(A_\delta\) is smooth and compactly supported;
\(z\mapsto|z|^{-1/2}z\) is smooth off \(0\) and \(\tfrac12\)-Hölder at \(0\).
Zero set: (i) the axis \(\rho=0\) and the sphere \(|x|=1\) for the bulk,
where \(w_0\sim\rho^{1/2}\) (codimension two, \(|\nabla w_0|\sim\rho^{-1/2}\in L^1_{\rm loc}\))
and \(w_0\sim(1-|x|)^{3/2}\) (\(C^1\) across the sphere); (ii) the lines
\(\{\sin kx_1=0\}\cap\{\cos kx_2=0\}\) for the oscillation, where \(|A_1|\sim kd\)
vanishes linearly, so \(|w_1|\sim\delta(kd)^{1/2}\), \(|\nabla w_1|\sim\delta k(kd)^{-1/2}\in L^1_{\rm loc}\)
and \(|w_1||\nabla w_1|^2\sim\delta^3k^2(kd)^{-1/2}\in L^1_{\rm loc}\).  A
continuous function with \(L^1_{\rm loc}\) gradient off a closed set of
Hausdorff codimension \(\ge2\) lies in \(W^{1,1}_{\rm loc}\); hence (H1), and
\(w_\delta\in L^\infty\) compactly supported gives \(w_\delta\in L^3\cap L^2\).

*Orders.* On the oscillation \(A_1=\delta^2F(kx)\) exactly, so \(w_1=\delta G(kx)\)
and per unit volume of \(B_R\): \(\int|\sigma|^{3/2}=(\delta k)^{3/2}\langle|\Sigma|^{3/2}\rangle\),
\(\int|w||\nabla w|^2=\delta^3k^2\langle\cdot\rangle\), \(\int|w|^3=\delta^3\langle\cdot\rangle\),
\(\int|w|^2=\delta^2\langle\cdot\rangle\), all cell averages finite by the
vanishing orders above, and \(\langle|\Sigma|^{3/2}\rangle>0\) because on
\(\{\psi=0\}=\{\sin y_2=0\}\) one has \(\hat F\parallel\nabla^\perp\psi\) and
\(|F|=|\nabla\psi|=2+\cos y_1\), non-constant along \(\hat F\), so
\(\Sigma=\hat F\cdot\nabla|F|\not\equiv0\).  The cutoff annulus contributes
\(O((kR)^{-1})\) relative corrections.  \(\|\mathbb Pw\|_2\le\|w\|_2\), and
\(\mathcal Q(\mathbb Pw_\delta)=\tfrac13\|w_\delta\|_3^3=\tfrac13(\|w_0\|_3^3+\|w_1\|_3^3)\)
is bounded below by the bulk.  Choose
\[
 R^3=\delta^{-2},\qquad k=\delta^{-1/2}\quad(\Rightarrow kR=\delta^{-7/6}\to\infty):
\]
\(\int|w||\nabla w|^2\sim\delta^3k^2R^3=1\), \(\int|w|^3\sim\delta\),
\(\int|w|^2\sim1\), \(\int|\sigma|^{3/2}\sim(\delta k)^{3/2}R^3=\delta^{-5/4}\).

**Lemma B (lower bounds for the family; supplied by the second audit).** With
\(w_\delta=w_0+w_1\) on disjoint supports,
\(D_3(w_\delta)=D_3(w_0)+D_3(w_1)\ge D_3(w_0)>0\) and
\(\|\mathbb Pw_\delta\|_2\ge\|w_0\|_2>0\). *Proof.* Additivity of \(D_3\) is
disjointness of the supports of \(V_\delta=V_0+V_1\), and \(0<D_3(w_0)<\infty\)
by the vanishing orders above. For the second bound, \(w_0\) is solenoidal and in
\(L^2\), so \(\mathbb Pw_0=w_0\) and, \(\mathbb P\) being an \(L^2\)-orthogonal
projection, \(\langle w_0,\mathbb Pw_\delta\rangle=\langle\mathbb Pw_0,w_\delta\rangle
=\langle w_0,w_0+w_1\rangle=\|w_0\|_2^2\); Cauchy–Schwarz gives
\(\|\mathbb Pw_\delta\|_2\ge\|w_0\|_2\). \(\square\)

*Conclusion.* If \(\Phi\) is locally bounded and dominates \(\|\sigma\|_{3/2}\)
on \(\mathcal M\), then by the orders above and Lemma B there is \(C\) with
\(\tfrac1C\le D_3(w_\delta)\le C\), \(\tfrac1C\le\mathcal Q(\mathbb Pw_\delta)\le C\),
\(\tfrac1C\le\|\mathbb Pw_\delta\|_2^2\le C\), so the triples
\((D_3,\mathcal Q,\|u\|_2^2)(w_\delta)\) lie in a
fixed compact \(K\subset(0,\infty)^3\), \(\Phi\) is bounded on \(K\) (finite
subcover), and \(\|\sigma_\delta\|_{3/2}\le\sup_K\Phi<\infty\) contradicts
\(\|\sigma_\delta\|_{3/2}^{3/2}\ge c\delta^{-5/4}\). \(\square\)

**Numerical check** (bounded computation, not part of the proof).  First
version: periodic cell of the oscillatory profile, \(N=384^2\), central
differences; audit, independently: \(N=1024^2\), agreeing to \(<1\%\).

| \(\delta\) | \(k\) | \(\int|\sigma|^{3/2}\) | \(D_3\) | \(\int|w|^3\) | rel. err. of \(\operatorname{div}w+\sigma=0\) |
|---|---|---|---|---|---|
| 1 | 1 | 1.890e-1 | 2.186 | 1.848 | 1.3e-3 |
| 1 | 2 | 5.347e-1 | 8.743 | 1.848 | 1.3e-3 |
| 1 | 4 | 1.512 | 34.97 | 1.848 | 1.3e-3 |
| 0.5 | 1 | 6.683e-2 | 2.732e-1 | 2.310e-1 | 1.3e-3 |
| 0.25 | 1 | 2.363e-2 | 3.415e-2 | 2.887e-2 | 1.3e-3 |

Ratios \(2^{1.5},4^{1.5}\) in \(k\) for the \(\sigma\)-integral, \(4,16\) for
\(D_3\), \((\tfrac12)^{1.5},(\tfrac14)^{1.5}\) and \((\tfrac12)^3,(\tfrac14)^3\)
in \(\delta\): exact homogeneity \(w_1=\delta G(kx)\), a one-line identity; the
only non-trivial content is \(\langle|\Sigma|^{3/2}\rangle>0\), proved above.

**Mechanism.** \(|\sigma|^{3/2}=(|w|^{1/2}|\sigma|)^{3/2}|w|^{-3/4}\): the
dissipation weight \(|w|\) is small precisely where the family oscillates.
The loss is at *low amplitude with many oscillations*, not at the zero set
(Remark 1.2) and not at high frequency alone.  The Hölder route
\(\int|\sigma|^{3/2}\le(\int|w|\sigma^2)^{3/4}(\int|w|^{-3})^{1/4}\) needs the
non-integrable weight \(|w|^{-3}\), consistent with Prop. 2.2.  Consequently
(1.7)–(1.8) is an exact representation of \(q\) but not an estimate in terms of
the dissipation: any use of \(\|\sigma\|_{3/2}\) is a hidden hypothesis.

### 2.4 Weighted forms that are TRUE (unconditional)

From (A1)–(A4), with \(g=|V|=|w|^{3/2}\in H^1\), \(\|g\|_2^2=3\mathcal Q\),
\(\|\nabla g\|_2^2=\tfrac94D_3^{\rm rad}\le\tfrac98D_3\):
\[
 \int|w|\sigma^2\le\tfrac12D_3,\quad
 \|\nabla A\|_{3/2}\le\tfrac43\,3^{1/6}\,\mathcal Q^{1/6}\|\nabla V\|_2\le C\mathcal Q^{1/6}D_3^{1/2},\quad
 \int|w|^5\le\tfrac94S^2(3\mathcal Q)^{2/3}D_3^{\rm rad},\quad
 \|w\|_{9/2}^3\le C\,\mathcal Q^{1/2}(D_3^{\rm rad})^{1/2},
                                                                    \tag{2.3}
\]
(Gagliardo–Nirenberg \(\|g\|_{10/3}^{10/3}\le\|g\|_2^{4/3}\|g\|_6^2\), exponent
\(\theta=3/5\) is the \(L^6\) share, the \(L^2\) share is \(2/5\); \(\|g\|_3^2\le\|g\|_2\|g\|_6\), \(\theta=1/2\)).  Scalings:
\((a^3,\lambda^2)\), \((a^2,\lambda)\), \((a^5,\lambda^2)\), \((a^3,\lambda)\) on
both sides ✓.  What these do **not** give: any unweighted integrability of
\(\sigma\) or \(\nabla w\); only \(|w|^{1/2}\sigma\in L^2\) and
\(|w|^{1/2}|\nabla w|\le|\nabla V|\in L^2\).  This is the exact point where the
divergence–speed link stops being quantitative (§2.3).

### 2.5 The weighted Calderón–Zygmund inequality (W): OPEN and moot

\[
 \int|w|\,|\nabla(I-S_L)\mathbb Pw|^2dx\ \le\ C\int|w|\,|\nabla w|^2dx\qquad(w\in\mathcal M\cap(\mathrm{H1}))
 \tag{W}
\]
is **neither proved nor refuted** (audit Lemma R3).  The \(A_2\) condition is
sufficient, not necessary, for weighted bounds; its failure for \(|w|\) does
not refute (W), which is a bound for the specific input \(w\) that also defines
the weight.  The first version's witness (\(A\equiv0\) on a ball, so \(|w|\equiv0\)
there) annihilates both sides on that ball and refutes nothing.  The unweighted
analogue is an identity-level truth (Fourier multipliers of norm \(\le1\)), so a
counterexample must come from the weight alone; none is exhibited.  (W) is
moreover *moot for size bounds*: (A5) bounds \(K\) by \(C_*\mathcal Q^{1/3}D_3\)
through \(\|u\|_9\le C_9\|w\|_9\) and Sobolev, without any weighted
Calderón–Zygmund step (§3.3(c)).  Its only remaining role would be a sharper
constant.

### 2.6 Summary table

| Inequality | Status | Reason | Scaling |
|---|---|---|---|
| \(\|q\|_3\le(1+C_3)(3\mathcal Q)^{1/3}\) | TRUE | HF17, Leray on \(L^3\) | \((a,1)\) |
| \(\|q\|_3^3\le\Phi(D_3,\mathcal Q)\) with \(\Phi(0+,\mathcal Q_\star)<\|q_\star\|_3^3\); any \(a>0,c=0\) | FALSE | coarse dilation of a witness | \(D_3\to0\), \(\|q\|_3\) fixed |
| \(\|q\|_3^3\le CD_3^a\mathcal Q^bE^{2a}\), \(7a+3b=3\), \(a>0\) | OPEN | needs \(\|w\|_2\lesssim\|u\|_2\); (2.1) true with \(\|w\|_2\) | consistent |
| \(\|q\|_3\le C\|\sigma\|_{3/2}\) | TRUE under (H1), \(\sigma\in L^{3/2}\); never better than trivial in controlled quantities | (1.7)–(1.8) | \((a,1)\) |
| \(\int|q|^2|w|^3\le C\mathcal Q^{2/3}D_3\) | TRUE | Prop. 2.1 | \((a^5,\lambda^2)\) |
| \(\int|q|^2|w|^3\le CD_3^{1+c/2}\mathcal Q^{2/3-7c/6}E^c\), \(0<c\le4/7\) | OPEN | same \(L^2\) question | consistent |
| \(\int|q|^2|w|^3\le CD_3^a\mathcal Q^bE^c\) off that line | FALSE | two-parameter scaling of a witness | mismatch |
| \(\|\sigma\|_{3/2}\le\Phi(D_3,\mathcal Q,E)\), \(\Phi\) locally bounded | FALSE | Prop. 2.2 | — |
| \(\int|w|\sigma^2\le\tfrac12D_3\) | TRUE | (1.3') | \((a^3,\lambda^2)\) |
| \(\int|w|^\alpha\sigma=0\), \(2\le\alpha\le5\) | TRUE | Remark 1.3 | identity |
| (W) | OPEN, moot for size bounds | §2.5 | \((a^3,\lambda^2)\) |
| \(\int|w|^{-1}\Pi_L^2<\infty\) or input bound | OPEN | §3.3(b) | \((a^5,\lambda^2)\) |
| \(\|w(u)\|_2\le C\|u\|_2\) | OPEN | §2.1 | \((a,\lambda^{-1/2})\) |

## 3. The high-strain term through the link

Throughout: \(v=S_Lu\), \(u^{hi}=u-v\in H^m\subset C^2_b\),
\(\operatorname{div}u^{hi}=0\), \(\omega=\operatorname{curl}u\),
\(K_L:=-\int q\cdot((A\cdot\nabla)u^{hi})\) (PLAN), \(K=\mathfrak T\) as in (A5).

### 3.1 Exact rewriting with no regularity of \(w\)

Let \(F:=(A\cdot\nabla)u^{hi}\in L^{3/2}\) and \(T_{ij}:=A_iu^{hi}_j\in L^{3/2}\).
Since \(\operatorname{div}A=0\) in \(\mathcal D'\) and \(u^{hi}\in C^1_b\),
\(F_j=\partial_iT_{ij}\) in \(\mathcal D'\) (for \(\varphi\in C_c^\infty\):
\(-\int T_{ij}\partial_i\varphi=-\int A_i\partial_i(u^{hi}_j\varphi)+\int A_i(\partial_iu^{hi}_j)\varphi\),
and the first integral vanishes because \(\operatorname{div}A=0\) tests against
\(C^1_c\) by mollification).  Define the *pressure-type potential of the pair*,
in exact analogy with \(p_{\rm NS}=R_iR_j(u_iu_j)\):
\[
 \Pi_L:=R_iR_j\big(A_iu^{hi}_j\big)=(-\Delta)^{-1}\partial_i\partial_jT_{ij}\in L^{3/2},\qquad
 (I-\mathbb P)F=\nabla\Delta^{-1}\partial_i\partial_jT_{ij}=-\nabla\Pi_L\in L^{3/2},
                                                                    \tag{3.1}
\]
so \(\Pi_L\in W^{1,3/2}\subset L^3\) with \(\|\Pi_L\|_3\le S'\|\nabla\Pi_L\|_{3/2}\le C\|A\|_{3/2}\|\nabla u^{hi}\|_\infty\).
(Relative to the audit's Lemma R1 normalisation, \(\Pi_L^{\rm here}=-\Pi_L^{\rm audit}\);
no sign of \(K_L\) is used anywhere.)  Because \(q\in\mathcal G_3\) is
annihilated by the solenoidal part \(\mathbb PF\in L^{3/2}\),
\[
 \boxed{\ K_L=-\int q\cdot(I-\mathbb P)F=\int q\cdot\nabla\Pi_L\,dx
 =-\big\langle\operatorname{div}w,\ \Pi_L\big\rangle_{W^{-1,3}\times W^{1,3/2}} .\ }
                                                                    \tag{3.2}
\]
This is rigorous at the audited \(L^3\) level and displays the link: the
high-strain form is the pairing of the divergence of the representative, i.e.
of the speed-transport source, with a pressure.  Under (H1) and
\(\sigma\in L^{3/2}\), by (1.3'') and density of \(C_c^\infty\) in \(W^{1,3/2}\),
\[
 K_L=\int\sigma\,\Pi_L\,dx=\int_{\{w\ne0\}}(\hat w\cdot\nabla|w|)\,\Pi_L\,dx .   \tag{3.3}
\]
Using \(\operatorname{div}u^{hi}=0\) once more and (A2),
\(\nabla\Pi_L=-(I-\mathbb P)[(u^{hi}\cdot\nabla)A]\) (both sides reduce to
\(-\nabla\Delta^{-1}\partial_i\partial_jT_{ij}\)); this is the \(u^{hi}\)-part of
the mixed pressure \(\Pi_{u,A}\) of HF18-A (F7).

### 3.2 Two exact identities for the full flux

**Proposition 3.1.** With \(\mathfrak T=-\int A\cdot((u\cdot\nabla)u)=\mathcal Q'+\nu D_3(w)\):
\[
 \text{(Lamb form)}\qquad
 \mathfrak T=-\int A\cdot(\omega\times u)=\int|w|\,\omega\cdot(q\times u)\,dx,
                                                                    \tag{3.4}
\]
\[
 \text{(orthogonality)}\qquad \int A\cdot\big((q\cdot\nabla)u\big)dx=0,
                                                                    \tag{3.5}
\]
\[
 \boxed{\ \text{(strain form)}\qquad
 \mathfrak T=-\int A\cdot\big((w\cdot\nabla)u\big)dx
 =-\int|w|\;w\cdot S(u)\,w\;dx,\qquad S(u)=\tfrac12(\nabla u+\nabla u^T).\ }
                                                                    \tag{3.6}
\]
No derivative of \(w\) or \(q\) is taken.

*Proof* (audited ✓; reproduced).  (3.4): \((u\cdot\nabla)u=\nabla(|u|^2/2)+\omega\times u\)
pointwise; \(|u|^2\in W^{1,3}\), so \(\nabla|u|^2\in\mathcal G_3\) (HF17 cutoff,
= HF18-A (E5)) and \(\int A\cdot\nabla|u|^2=0\).  Then
\(A\cdot(\omega\times u)=A\cdot(\omega\times w)-A\cdot(\omega\times q)=-A\cdot(\omega\times q)\)
because \(A\parallel w\); all terms are in \(L^1\) (\(A\in L^{3/2}\),
\(\omega\in L^\infty\), \(q\in L^3\)).  Finally
\(A\cdot(\omega\times q)=|w|\,\omega\cdot(q\times w)=|w|\,\omega\cdot(q\times u)\).
(3.5): \((A\times\omega)_j=A_k\partial_ju_k-A_k\partial_ku_j\)
(\(\varepsilon_{jkl}\varepsilon_{lmn}=\delta_{jm}\delta_{kn}-\delta_{jn}\delta_{km}\))
gives \(q\cdot(A\times\omega)=A\cdot((q\cdot\nabla)u)-q\cdot((A\cdot\nabla)u)\), and
\(\int q\cdot(A\times\omega)=\int A\cdot(\omega\times q)=\mathfrak T\) by (3.4);
the reviewed HF17 (9) is \(\mathfrak T=-\int q\cdot((A\cdot\nabla)u)\); subtract.
(3.6): \(-\int A\cdot((u\cdot\nabla)u)=-\int A\cdot((w\cdot\nabla)u)+\int A\cdot((q\cdot\nabla)u)\)
and (3.5); \(A\cdot((w\cdot\nabla)u)=|w|w_iw_j\partial_iu_j\) is symmetric in \(ij\). \(\square\)

Cross-check of (3.5) under (H1): \(\int|w|w_iq_j\partial_ju_i
=\int|w|^2q\cdot\nabla|w|-\int A\cdot\nabla(|q|^2/2)=-\tfrac13\int|w|^3\operatorname{div}w-0=0\),
using symmetry of \(\nabla q\) and \(\nabla|q|^2\in\mathcal G_3\) (HF18-A Prop. 3',
Step A, audited under (H1)), then (1.4) with \(\alpha=3\), which is now
unconditional.  The two routes agree; the cross-check remains conditional only
through the \(q\)-derivative step.  HF18-A's (F5)–(F6), \(\mathfrak T=\int u\cdot((u\cdot\nabla)A)=-\int q\cdot((u\cdot\nabla)A)\),
are the dual forms in which the derivative falls on \(A\in W^{1,3/2}\).

**Reading of (3.6).** For the standard cubic energy the analogous term
\(\int|u|u\cdot S(u)u=\int u\cdot\nabla(|u|^3/3)\) vanishes and the whole
nonlinearity sits in the pressure; for the quotient functional the pressure
vanishes and the whole nonlinearity is the strain of \(u\) along the direction
of the non-solenoidal representative, weighted by the cube of its speed:
\(\mathfrak T=-\int|w|^3\,\hat w\cdot S(u)\hat w\).  Under (H1), with
\(q=\nabla\varphi\), \(\varphi\in W^{2,1}_{\rm loc}\), \(\Delta\varphi=\operatorname{div}w=-\sigma\):
\(\hat w\cdot S(u)\hat w=\hat w\cdot\nabla w\,\hat w-\partial_{\hat w\hat w}\varphi
=-\operatorname{div}w-\partial_{\hat w\hat w}\varphi=-\operatorname{tr}\big((I+\hat w\otimes\hat w)\nabla^2\varphi\big)\)
by (1.3), and with (1.4), \(\alpha=3\): \(\mathfrak T=\int|w|^3\partial_{\hat w\hat w}\varphi\)
— the \(\hat w\hat w\)-component of the Hessian of the potential of \(q\), whose
source is \(-\sigma\).  The analogy with vortex stretching
\(\int|\omega|^2\hat\omega\cdot S\hat\omega\) is exact in form and opposite in sign.

**Split.** With \(K^S_L:=-\int|w|\,w\cdot S(u^{hi})\,w\),
\[
 K_L-K^S_L=\int q\cdot((A\cdot\nabla)v)-\int A\cdot((w\cdot\nabla)v),\qquad
 |K_L-K^S_L|\le (2+C_3)\|\nabla v\|_\infty\|w\|_3^3\le C2^{5L/2}E_0^{1/2}\mathcal Q ,
                                                                    \tag{3.7}
\]
(Bernstein \(\|\nabla S_Lu\|_\infty\le C2^{5L/2}\|u\|_2\); scaling \((a^4,\lambda^2)\) ✓),
so the frozen gap may be posed for \(K^S_L\) with the same quantifiers.  Also
\(K_L=K+\int q\cdot((A\cdot\nabla)v)\), so by (A5)
\[
 |K_L|\le C_*\mathcal Q^{1/3}D_3(w)+C2^{5L/2}E_0^{1/2}\mathcal Q .              \tag{3.7'}
\]
(3.4)–(3.7') are equivalent identities and size bounds; PLAN's rule that an
equivalent identity alone discharges nothing applies to every one of them.

### 3.3 Attempts to control \(K_L\); the first uncontrolled term

Target: \(K_L\le\theta\nu D_3+M\mathcal Q+(\text{input})\) pointwise in time,
\(\theta\le1\), or its integrated form.  Each attempt is displayed with the
exact point of failure and its \((a,\lambda)\) scaling.

(a) *Unweighted link.* Under (H1), \(\sigma\in L^{3/2}\): from (3.3),
\(|K_L|\le\|\sigma\|_{3/2}\|\Pi_L\|_3\le\|\sigma\|_{3/2}\,C\|A\|_{3/2}\|\nabla u^{hi}\|_\infty\).
Dies at the first factor: \(\|\sigma\|_{3/2}\) is not dominated by any locally
bounded function of the controlled quantities (Prop. 2.2).  (The first
version's Hardy-space refinement of the second factor via CLMS [MO] is
unnecessary and removed; the second factor \(\|\nabla u^{hi}\|_\infty\sim(a,\lambda)\)
is in any case a supercritical sup bound.)

(b) *Weighted link.* Under (H1), \(\sigma\in L^{3/2}\):
\(\int\sigma\Pi_L=\int(|w|^{1/2}\sigma)(|w|^{-1/2}\Pi_L)\), so by (1.3')
\[
 |K_L|\le\big(\tfrac12D_3\big)^{1/2}\Big(\int|w|^{-1}\Pi_L^2dx\Big)^{1/2},\qquad
 \int|w|^{-1}\Pi_L^2\sim(a^5,\lambda^2).                              \tag{3.8}
\]
(\(\Pi_L\) is an order-zero image of \(A\otimes u^{hi}\sim a^3\lambda^3\);
\(\int|w|^{-1}\Pi_L^2\sim a^{-1}\lambda^{-1}a^6\lambda^6\lambda^{-3}\).)
**First uncontrolled term of the link route:** \(\int|w|^{-1}\Pi_L^2\).  It is
a weighted \(L^2\) norm of a Riesz-transform image with the weight \(|w|^{-1}\),
which is not locally integrable across a codimension-one zero of \(w\) with
\(|w|\sim\operatorname{dist}\) (Remark 1.2), while \(\Pi_L\) is nonlocal and has
no reason to vanish there.  Its finiteness on \(\mathcal M\cap(\mathrm{H1})\) is
**not proved and not refuted** (no example with \(\Pi_L\ne0\) on such a zero
set is exhibited).  Where finite, Young gives
\(K_L\le\theta\nu D_3+(2\theta\nu)^{-1}\int|w|^{-1}\Pi_L^2\); heuristically
\(\Pi_L\sim|w|^2|u^{hi}|\), so the remainder is \(\sim\nu^{-1}\int|w|^3|u^{hi}|^2\),
and absorbing that into \(\theta\nu\int|w||\nabla w|^2\) needs
\(|u^{hi}|\lesssim\nu2^L\) pointwise: a supercritical sup bound on the high
frequencies (\(\|u^{hi}\|_\infty\sim(a,\lambda)\)), i.e. a regularity
criterion — the packet's forbidden "bound by the norm to be controlled".

(c) *Strain form* (unconditional).  \(|K^S_L|\le\int|w|^3|S(u^{hi})|
\le(\int|w||\nabla u^{hi}|^2)^{1/2}(\int|w|^5)^{1/2}\), and by (2.3)
\[
 |K^S_L|\le C\,\mathcal Q^{1/3}(D_3^{\rm rad})^{1/2}\Big(\int|w||\nabla u^{hi}|^2\Big)^{1/2}
 \sim(a^4,\lambda^2).                                                 \tag{3.9}
\]
(Equivalently, (2.2) on the Cauchy–Schwarz split of \(K_L\):
\(|K_L|\le(\int|w||\nabla u^{hi}|^2)^{1/2}(\int|q|^2|w|^3)^{1/2}\), same bound.)
Two obstructions, in order: (i) replacing \(\int|w||\nabla u^{hi}|^2\) by
\(CD_3\) is the OPEN inequality (W); (ii) even granting (W), Young leaves
\(K^S_L\le\theta\nu D_3+C\theta^{-1}\nu^{-1}\mathcal Q^{2/3}D_3\), which closes
only if \(\mathcal Q^{2/3}\lesssim\theta\nu^2\), i.e. \(\|u\|_3\lesssim\nu\):
hidden smallness, the classical small-\(L^3\) regime.  The audited (A5) reaches
the same endpoint *without* (W): \(|K_L|\le C_*\mathcal Q^{1/3}D_3+C2^{5L/2}E_0^{1/2}\mathcal Q\)
absorbs into \(\theta\nu D_3\) exactly when \(C_*\mathcal Q^{1/3}\le\theta\nu\).
So obstruction (i) is moot and obstruction (ii) is the whole content of the
size route: by scaling, \(\mathcal Q^{1/3}D_3\) is the unique monomial in
\((\mathcal Q,D_3)\) with the weight \((a^4,\lambda^2)\) of \(K\), and no size
bound in \(\mathcal Q\), \(D_3\) can do better (HF18-A §4, audited, with the
audit's correction S2: an input-only *spacetime* remainder is not excluded by
this instantaneous argument).

(d) *Sign.* None of (3.2)–(3.6) has a sign: \(\hat w\cdot S\hat w\) ranges over
\([\lambda_{\min}(S),\lambda_{\max}(S)]\) with \(\operatorname{tr}S=0\), so
\(\lambda_{\min}\le0\le\lambda_{\max}\); \(\Pi_L\) is a Riesz image without
pointwise sign; averaging over directions is unavailable because \(\hat w\) is
fixed by \(A\).  (HF18-A audit R9: \(K\equiv0\) on \(\{u:\operatorname{div}(|u|u)=0\}\),
so any cancellation must be sought on families driving \(\|q\|_3/\|w\|_3\)
towards its supremum, not on generic smooth fields.)

**Conclusion of §3.** The divergence–speed link converts \(K_L\) into
\(-\langle\operatorname{div}w,\Pi_L\rangle\) and \(\mathfrak T\) into a pure
strain form, with every factor identified; after any Hölder/Young split the
first term not controlled by \((D_3,\mathcal Q,\text{input})\) is
\(\int|w|^{-1}\Pi_L^2\) in route (b), and the small-data factor
\(C_*\mathcal Q^{1/3}/\nu\) in route (c).  These are the same critical
obstruction as HIGH-PRESSURE in a different coordinate system, as the packet
predicts for any equivalent rewriting.

## 4. Structural facts (exact scope)

1. (Prop. 1.1, unconditional) a.e. on \(\{w\ne0\}\), with the approximate
   gradient \(\nabla w=D\Psi(V)\nabla V\): \(\operatorname{div}w=-\hat w\cdot\nabla|w|\),
   equivalently \(\operatorname{tr}((I+\hat w\otimes\hat w)\nabla w)=0\);
   \(|w|^{1/2}\sigma=\tfrac23\hat V\cdot\nabla|V|\in L^2\), \(\int|w|\sigma^2\le\tfrac12D_3(w)\).
   Under (H1) the identity holds for the distributional divergence, (1.3'').
   Without (H1) only (1.1) holds at the distributional level.
2. (Remark 1.3, unconditional) \(\int|w|^\alpha\sigma=0\) for \(2\le\alpha\le5\).
3. (Prop. 1.4) \(\mathcal M=\{|A|^{-1/2}A:A\in L^{3/2}\text{ solenoidal}\}\);
   the minimizing representative of \(u\) is the unique \(w\in\mathcal M\) with
   \(\mathbb Pw=u\); \(\mathcal Q(u)=\tfrac13\|A\|_{3/2}^{3/2}\).  Closed-form
   analogue in Stern Thm 2.9 [DI]; vector variant here; enables linear
   construction of test fields.
4. ((1.7)–(1.8), under (H1) and \(\sigma\in L^{3/2}\)) \(q=-\nabla(\Gamma*\sigma)\),
   \(\|q\|_3\le C_{\rm HLS}\|\sigma\|_{3/2}\), never better than the trivial bound
   in controlled quantities.
5. (Prop. 2.1, unconditional) \(\int|q|^2|w|^3\le\tfrac98(1+C_3)^2S^2(3\mathcal Q)^{2/3}D_3(w)\);
   exponents forced by scaling; order-sharp on single-scale fields with
   nondegenerate gradient part.
6. (Prop. 2.2) \(\|\sigma\|_{3/2}\) is not dominated by any locally bounded
   function of \((D_3,\mathcal Q,\|u\|_2^2)\) on \(\mathcal M\); explicit family
   satisfying (H1), orders confirmed numerically twice.
7. (§2.1) \(\|q\|_3^3\) admits no bound by \((D_3,\mathcal Q)\) alone that
   improves on the trivial one as \(D_3\to0\); bounds involving \(E\) reduce to
   the OPEN \(L^2\) question for \(u\mapsto w(u)\).
8. ((3.2)) \(K_L=\int q\cdot\nabla\Pi_L=-\langle\operatorname{div}w,\Pi_L\rangle\),
   \(\Pi_L=R_iR_j(A_iu^{hi}_j)\), \((I-\mathbb P)F=-\nabla\Pi_L\), rigorous at the
   \(L^3\) level; \(=\int\sigma\Pi_L\) under (H1), \(\sigma\in L^{3/2}\).
9. (Prop. 3.1, no regularity of \(w\)) \(\int A\cdot((q\cdot\nabla)u)=0\) and
   \(\mathcal Q'+\nu D_3(w)=-\int|w|\,w\cdot S(u)\,w=\int|w|\,\omega\cdot(q\times u)\).
   Depends on the reviewed HF17 (9) and audited (A4).
10. ((3.7), (3.7')) The frozen gap is equivalent, up to the input Gronwall
    coefficient, to the same bound for \(K^S_L\); and
    \(|K_L|\le C_*\mathcal Q^{1/3}D_3+C2^{5L/2}E_0^{1/2}\mathcal Q\).

## 5. Frontier record

**MODE / RESULT:** REPAIR.  All audit items disposed (table above); the note
re-based on audited HF18-A regularity.  Unconditional: pointwise identity on
\(\{w\ne0\}\), weighted bounds (1.3'), (2.2), (2.3), exact integrals (1.4),
linear description of \(\mathcal M\), strain and Lamb forms, pairing form (3.2).
Conditional on (H1) alone (Lemma A): distributional identification (1.3''). Conditional on (H1) and (H2) \(\sigma\in L^{3/2}\): potential formula
(1.7)–(1.8), pairing form (3.3), Hessian reading of (3.6).  Exact
TRUE/FALSE/OPEN classification of the weighted inequalities in §2.6.  No
estimate for the gap.

**CLAIM AND SCOPE:** Items 1–10 of §4 with the hypotheses displayed there,
for every fixed time of a classical solenoidal \(u\in H^m\), \(m\ge4\), on
\(\mathbb R^3\) (§3), or for every \(w\in\mathcal M\) (§1–2), with HF17 (9)
and HF18-A (A1)–(A5) as audited inputs.  Prop. 2.2 refutes static inequalities
on \(\mathcal M\) only.

**EVIDENCE:** Matrix chain rule \(D\Phi=DF\circ D\Psi\) on the audited
\(\nabla A=D\Phi(V)\nabla V\) for §1.2; the audited mollification chain rule for
Remark 1.3; convexity and Riesz-transform Helmholtz splitting for Prop. 1.4;
HLS or Calderón–Zygmund plus Sobolev for (1.8), sign verified on an exact
example; two-parameter scaling of a witness for the FALSE entries;
Hölder–Sobolev on \(|V|\in H^1\) for (2.2)–(2.3); the explicit solenoidal-potential
family with \(R^3=\delta^{-2}\), \(k=\delta^{-1/2}\), (H1) proved by the
codimension-two removability argument, positivity of \(\langle|\Sigma|^{3/2}\rangle\)
proved analytically, orders confirmed numerically (first version \(384^2\),
audit \(1024^2\)); distributional product rule and \(L^{3/2}\) Helmholtz
splitting for (3.2); vector identities plus HF17 (9) for Prop. 3.1.  Riesz
convention verified by FFT this wave (`riesz_sign.py`).
Sources: Stern arXiv:2403.19481v2 Lemma 2.2, Thm 2.9 [DI]; Lindqvist *Notes on
the p-Laplace equation* through HF18-A and its audit [DI]; Lieb–Loss Thm 4.3 /
Stein Ch. V for HLS [MO, exponent scaling-forced, alternative proof given];
Iwaniec–Martin, CLMS, Scott, Iwaniec–Scott–Stroffolini, Uhlenbeck [MO, none
load-bearing]; Gilbarg–Trudinger no longer cited.

**FIRST GAP:** the implication "\(K_L=-\langle\operatorname{div}w,\Pi_L\rangle\)
(or \(K^S_L=-\int|w|w\cdot S(u^{hi})w\)) admits a bound
\(\int_0^\tau K_L\,dt\le\theta\nu\int_0^\tau D_3(w)\,dt+M\int_0^\tau\mathcal Q\,dt+A_{\rm input}\)
uniformly for \(\tau<\min(H,T_*)\), \(\theta\le1\)".  After the weighted split
the first uncontrolled term is \(\int|w|^{-1}\Pi_L^2\,dx\sim(a^5,\lambda^2)\),
of unknown finiteness on \(\mathcal M\cap(\mathrm{H1})\); after the strain or
direct split it is the small-data factor: the size bound
\(|K_L|\le C_*\mathcal Q^{1/3}D_3+C2^{5L/2}E_0^{1/2}\mathcal Q\) absorbs only under
\(C_*\mathcal Q^{1/3}\le\theta\nu\), i.e. \(\|u\|_3\lesssim\nu\), with or without
the OPEN weighted inequality (W).

**SURVIVING CONDITIONAL SUFFIX:** \(D_{\mathcal Q}=D_3(w)\) is now audited, so
the earlier proviso "if \(D_{\mathcal Q}\ge cD_3\)" is discharged.  If any
one-sided spacetime bound
\(\int_0^\tau(-\int|w|w\cdot S(u^{hi})w)\,dt\le\theta\nu\int_0^\tau D_3(w)\,dt+A_{\rm input}\)
were proved with \(\theta\le1\) and input-only finite \(A_{\rm input}\), then
(3.7), HF17 (13)–(14) and Gronwall give
\(\mathcal Q(\tau)+(1-\theta)\nu\int_0^\tau D_3\le e^{C2^{5L/2}E_0^{1/2}\tau}(\mathcal Q(0)+A_{\rm input})\),
hence \(\sup_t\|u\|_3\) and \(u\in L^3_tL^9_x\) up to \(\min(H,T_*)\), and
continuation by the imported ESS node.  Equivalent to the frozen gap; not
proved.

**NON-CLAIMS:** no \(W^{1,1}_{\rm loc}\), continuity, or higher regularity of
\(w\) ((H1) remains a hypothesis; HF18-A's audited NON-CLAIMS stand); no bound
or sign for \(K\), \(K_L\), \(K^S_L\), or \(\mathfrak T\) beyond the size bound
(A5); no time-integrated absorption; no \(L^2\) bound for the nonlinear
projection \(u\mapsto w(u)\); no truth or falsity of (W); no finiteness or
infinitude of \(\int|w|^{-1}\Pi_L^2\); no applicability of \(p\)-Laplace or
\(p\)-harmonic-form regularity theorems; no continuation criterion, HIGH-STRAIN
or HIGH-PRESSURE theorem, or regularity result; no novelty for the nonlinear
Hodge construction (Stern/Scott/Iwaniec–Scott–Stroffolini).  Prop. 2.2 says
nothing about which \(w\) occur along Navier–Stokes trajectories.  The
numerical checks are bounded evidence at finite resolution, not proof.
NS-R3 remains OPEN.

**NEXT DISTINCT ACTION:** FALSIFY the static closability of the strain form:
on the linear family \(A=\operatorname{curl}\Psi\) (Prop. 1.4), with
\(\|q\|_3/\|w\|_3\) driven towards its supremum (HF18-A audit R9), search for
\(w\in\mathcal M\) with \(\hat w\) aligned to the expanding eigenvector of
\(S(\mathbb Pw)\) at high frequency and
\(-\int|w|^3\hat w\cdot S(\mathbb Pw)\hat w\gg\nu D_3(w)\) at bounded
\(\mathcal Q\); such a family would show that no static inequality closes the
gap and that the dynamics must be used.  Independently, attack (H1) through
the nonlinear Hodge literature for \(\delta(\rho(Q)\omega)=0\) with prescribed
nonzero \(d\omega\) (Sibner–Sibner; Otway math-ph/9806007, [DI] via the HF18-A
audit), whose structure condition degenerates here exactly at \(k=0\); a proof
of (H1) would make (1.3''), (1.7)–(1.8), (3.3) and the Hessian reading of (3.6)
unconditional, and a disproof would retire them.
