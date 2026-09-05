# Independent audit (round 2) of the repaired HF18-B divergence–speed link

**VERDICT: PASS, with four mandatory scope corrections (S1–S4).**

Frozen input: `research/evidence/hf18-divergence-speed-link.md`, SHA-256
`921f6513158c50b012708f4315134cefbfb7aa1d379cf6d57ebc1b33adc08b0e`
(working-tree state, uncommitted; last committed version of the file is the
round-1 candidate at `cee98a7`), base commit
`715ce84ec78d64c510e150360a354b5d55648b9c`.
Mode: REVIEW (round 2), proof-audit discipline.  Reviewed against PLAN.md
("Frontier packet", "HF16–HF17"), `hf17-quotient-functional.md`,
`hf17-quotient-evolution.md`, the round-1 audit
`hf18-review-divergence-speed-link.md` (verdict REPAIR), and the sibling lane
`hf18-hodge-regularity.md` with `hf18-review-hodge-regularity.md`
(verdict PASS), whose (A1)–(A5) are used as audited inputs and are **not**
re-proved here (their audit is checked only for faithfulness of citation).

Every bridge named in round 1 is repaired, and the repairs are correct.  The
sign convention is now internally consistent and I confirmed it independently
by FFT (my own script, not the author's): in the stated convention
\(R_j=\partial_j(-\Delta)^{-1/2}\) the Navier–Stokes aside is
\(p=+R_iR_j(u_iu_j)\), so the round-1 audit's closing aside
"\(p=-R_iR_j(u_iu_j)\)" was itself a slip and the candidate is right to say so.
No displayed identity or inequality in the repaired note is false, no TRUE
entry of §2.6 could be refuted, and every scaling exponent recomputes.  The
four corrections below are a missing (standard, supplied) justification inside
the (H1)-gated step, a hypothesis dropped in two summary lines, two missing
one-line lower bounds in the proof of a negative result, and two constant/label
slips.  None of them changes a result, the FIRST GAP, or the NON-CLAIMS.

## REVIEWED SCOPE

§0 (audited-input transcription, Riesz convention, scaling bookkeeping);
§1.1–§1.5 (Prop. 1.1 with (1.2), (1.3), (1.3'), Rmk. 1.2, Rmk. 1.3/(1.4),
§1.3 on (H1), Prop. 1.4/(1.6), (1.7)–(1.8)); §2.1–§2.6 (exponent lattices,
(2.1), Prop. 2.1/(2.2), Prop. 2.2 with its construction, orders and numerical
table, (2.3), (W), summary table); §3.1–§3.3 ((3.1)–(3.3), Prop. 3.1 with
(3.4)–(3.6) and the Hessian reading, splits (3.7), (3.7'), routes (a)–(d),
(3.8)–(3.9)); §4 items 1–10; §5 frontier record; the repair-record table.
Treated as previously audited and not re-proved: HF17 (5), (9), (13)–(15)
(both HF17 reviews PASS) and HF18-A (A1)–(A5) = Theorem 1, Corollary 1(a)–(f),
Theorem 2, (F6)–(F7), Theorem 4 (`hf18-review-hodge-regularity.md`, PASS).

Faithfulness of the audited-input transcription, checked line by line against
HF18-A: (A1) = (1.9) ✓; (A2) = (1.11) + Cor. 1(c),(d) including
\(\operatorname{div}A=0\) a.e. ✓; (A3) = Cor. 1(a),(b) ✓; (A4) = Thm. 2 with
(2.1) of HF18-A ✓; (A5) = (F6), (F7), (4.1), (4.2) with
\(C_*=\tfrac32 3^{1/3}(1+C_3)C_9S\) ✓ (constant identical).  The approximate
gradient \(D\Psi(V)\nabla V\), the bound \(|\nabla w|\le|w|^{-1/2}|\nabla V|\)
and the integrand identity (1.12) are quoted exactly ✓.  The two citations of
the HF18-A **audit** are also faithful: R9 (\(K\equiv0\) on
\(\{\operatorname{div}(|u|u)=0\}\), so a saturation search must drive
\(\|q\|_3/\|w\|_3\) up) ✓ and S2 (an input-only *spacetime* remainder is not
excluded by the instantaneous monomial argument) ✓.

## FIRST BAD BRIDGE

**None.**  No implication in the note is invalid, and no statement is false.
The first defect in reading order is a *missing justification*, not a bad
bridge:

**§1.3, first clause: "Under (H1) the approximate gradient is the weak
gradient."**  This is asserted with no proof and no citation, and it carries
the whole (H1) branch: (1.3''), (1.7)–(1.8), (3.3), the Hessian reading of
(3.6), and routes (a),(b).  It is *true*, but it needs the a.e. approximate
differentiability of \(W^{1,1}_{\rm loc}\) functions plus uniqueness of
approximate differentials; the round-1 version reached the same conclusion by
an explicit truncation chain rule (which round 1 accepted with a phrasing fix),
and the repair deleted that argument without replacing it.  Lemma A below
supplies the two-paragraph proof.  Because the statement holds and the fix is
local, this is S1 rather than a REPAIR verdict.

## EVIDENCE

Re-derived item by item.  "✓" = checked here, independently of the note.

**Convention and signs (round-1 item (B1)).**
1. \(R_j\) has symbol \(i\xi_j/|\xi|\), hence \((R_iR_j)^\wedge=-\xi_i\xi_j/|\xi|^2\),
   \(R_iR_j=\partial_i\partial_j(-\Delta)^{-1}\), \(\mathbb P_{jk}=\delta_{jk}+R_jR_k\),
   \((I-\mathbb P)_{jk}=-R_jR_k=\partial_j\Delta^{-1}\partial_k\) ✓; so
   \(q=(I-\mathbb P)w=\nabla\Delta^{-1}\operatorname{div}w=-R(R\cdot w)\), which is (1.1) ✓.
2. \(p_{\rm NS}=-\Delta^{-1}\partial_i\partial_j(u_iu_j)=+R_iR_j(u_iu_j)\) ✓.
   *My own FFT check* (my script, \(256^2\) periodic, spectral symbols):
   for \(u=(\sin y,\sin x,0)\), \((u\cdot\nabla)u=\nabla(-\cos x\cos y)\) and
   \(\max|R_iR_j(u_iu_j)-\cos x\cos y|=7.8\times10^{-16}\), while
   \(\max|R_iR_j(u_iu_j)+\cos x\cos y|=2.0\); and \(-R(R\cdot\nabla f)=\nabla f\)
   to \(4\times10^{-15}\), \(-R(R\cdot h)=0\) to \(2\times10^{-15}\) for
   \(h\) solenoidal ✓.  The note's §0 convention block, its claim that the
   round-1 aside on \(p\) has the wrong sign, and its statement that Lemma R1
   is correct for \(q\), the kernel and \(\Pi_L\) are all confirmed.
3. (1.7): \(\Gamma=-1/(4\pi|x|)\), \(\Delta\Gamma=\delta\), \(\nabla\Gamma=x/(4\pi|x|^3)\),
   so \(q=\nabla\Delta^{-1}\operatorname{div}w=-\nabla(\Gamma*\sigma)
   =-\tfrac1{4\pi}\int\frac{x-y}{|x-y|^3}\sigma(y)dy\) ✓, i.e. the Newtonian
   field of the density \(-\sigma\).  Exact-example check on \(w=Cx/|x|^2\)
   (\(|w|=|C|/r\), \(A=|C|Cx/r^3\), \(\operatorname{div}A=0\),
   \(\operatorname{div}w=C/r^2\), \(\sigma=-C/r^2\)): the density is \(+C/r^2\),
   Gauss gives \(E_r=C/r\), i.e. \(E=Cx/r^2=q\) ✓.  The kernel sign is now right.
4. (3.1): \(\Pi_L=R_iR_j T_{ij}=(-\Delta)^{-1}\partial_i\partial_jT_{ij}\) and
   \((I-\mathbb P)F=\nabla\Delta^{-1}\partial_i\partial_jT_{ij}=-\nabla\Pi_L\) ✓;
   hence \(\Pi_L^{\rm here}=-\Pi_L^{\rm audit}\) ✓ exactly as the note records,
   and (3.2) \(K_L=-\int q\cdot(I-\mathbb P)F=\int q\cdot\nabla\Pi_L
   =-\langle\operatorname{div}w,\Pi_L\rangle_{W^{-1,3}\times W^{1,3/2}}\) ✓
   (duality is correct: \((W^{1,3/2})^*=W^{-1,3}\), \(\operatorname{div}w\in W^{-1,3}\)).
   \(F_j=\partial_iT_{ij}\) in \(\mathcal D'\) ✓ (re-derived; \(\operatorname{div}A=0\)
   tests against \(C^1_c\) by mollification).  \(\|\Pi_L\|_3\le C\|A\|_{3/2}\|\nabla u^{hi}\|_\infty\)
   ✓ (\(L^{3/2}\)-boundedness of \(I-\mathbb P\), then \(W^{1,3/2}(\mathbb R^3)\subset L^3\)).
   The sign chain (3.2)→(3.3) is consistent with round-1 Lemma R1 ✓.

**§1 (the identity).**
5. Prop. 1.1, now unconditional, ✓ and the new proof is correct.  \(\Phi=F\circ\Psi\)
   with \(F(z)=|z|z\in C^1\) and \(\Psi\) \(C^1\) off \(0\), so
   \(D\Phi(V)=DF(\Psi(V))D\Psi(V)\); I verified the matrix product explicitly,
   \(|w|(I+P)\cdot|V|^{-1/3}(I-\tfrac13P)=|V|^{1/3}(I+\tfrac13P)=D\Phi(V)\)
   with \(P=\hat V\otimes\hat V\), \(P^2=P\) ✓ — it reproduces HF18-A Cor. 1(c)
   exactly, so (1.2) follows from the audited \(\nabla A=D\Phi(V)\nabla V\)
   with no truncation and no Gilbarg–Trudinger lemma ✓.  Trace:
   \(\operatorname{div}A=|w|\operatorname{div}w+w\cdot\nabla|w|=|w|(\operatorname{div}w+\sigma)\)
   and \(\operatorname{div}A=0\) a.e. by (A2) ✓, so (1.3) holds a.e. on \(\{w\ne0\}\);
   trace form \(\operatorname{tr}((I+\hat w\otimes\hat w)\nabla w)=\operatorname{div}w+\sigma\) ✓.
   Consistency of the two expressions for \(\partial_i|w|\) ✓
   (\(\hat w\cdot\partial_iw=|V|^{-1/3}(1-\tfrac13)\hat V\cdot\partial_iV=\partial_i(|V|^{2/3})\)).
6. (1.3') ✓.  \(|w|^{1/2}\sigma=\tfrac23\hat V\cdot\nabla|V|\) ✓ re-derived;
   \(\int|w|\sigma^2\le\int|w||\nabla|w||^2=D_3^{\rm rad}=\tfrac49\|\nabla|V|\|_2^2
   \le\tfrac49\|\nabla V\|_2^2\le\tfrac49\cdot\tfrac98D_3=\tfrac12D_3\) ✓, so
   both the intermediate \(D_3^{\rm rad}\le\tfrac12D_3\) and the stated constant
   are right.  Scaling \((a^3,\lambda^2)\) on both sides ✓.
   *Cross-check of the audited integrand identity, independently:* with
   \(\partial_iV=a_i\hat V+b_i\), \(b_i\perp\hat V\), one gets
   \(|w||\nabla w|^2=|\nabla V|^2-\tfrac59|\nabla|V||^2\) and
   \(|w||\nabla|w||^2=\tfrac49|\nabla|V||^2\), summing to
   \(|\nabla V|^2-\tfrac19|\nabla|V||^2\) ✓ = HF18-A (1.12), and
   \(|\nabla V|^2=|w||\nabla w|^2+\tfrac54|w||\nabla|w||^2\) ✓.
   *Numerical check (my own script, \(1024^2\), central differences,
   the note's oscillation profile at \(\delta=k=1\)):* relative error of
   \(\operatorname{div}w+\sigma=0\) away from the zero lines \(1.4\times10^{-3}\);
   relative error of (1.12) \(1.3\times10^{-3}\);
   \(\langle|w|\sigma^2\rangle=0.121\le D_3^{\rm rad}=0.358\le D_3/2=1.094\) ✓;
   \(\tfrac89\|\nabla V\|_2^2=2.025\le D_3=2.188\le\|\nabla V\|_2^2=2.278\) ✓.
7. Rmk. 1.2 ✓ unchanged from round 1 (\(A=(0,x_1^2,0)\) gives a codimension-one
   zero in \(\mathcal M\); the two integrability thresholds coincide at \(\beta>1/3\)).
8. Rmk. 1.3/(1.4), now unconditional, ✓.  \(|w|^\alpha w=|V|^\beta V\),
   \(\beta=(2\alpha-1)/3\) ✓; \(\beta\in[1,3]\iff\alpha\in[2,5]\) ✓; the two
   integrability constraints are exactly \(|V|^{\beta+1}\in L^1\) (\(\beta\le5\))
   and \(|V|^\beta\in L^2\) (\(\beta\le3\)) for \(V\in L^2\cap L^6\), so the range
   is sharp for this argument ✓.  The pointwise algebra
   \(\operatorname{div}(|w|^\alpha w)=(\alpha-1)|w|^\alpha\sigma\) ✓ (re-derived
   from \(DF_\alpha(w)\nabla w\) with the same chain rule).  Absolute
   convergence of \(\int|w|^\alpha\sigma\) also holds exactly on \([2,5]\):
   \(|w|^{\alpha-1/2}\in L^2\iff|w|^{2\alpha-1}\in L^1\iff2\alpha-1\in[3,9]\),
   using \(w\in L^3\cap L^9\) ✓ (worth displaying; see S4).
   *Numerical check:* on the periodic cell,
   \(\int|w|^\alpha\sigma=O(10^{-19})\) against \(\int|w|^\alpha|\sigma|\sim0.4\)–\(0.8\)
   for \(\alpha=2,3,5\) ✓ (the periodic test confirms the pointwise identity,
   not the \(\mathbb R^3\) range).
9. §1.3: the second and third clauses are fine — \(\nabla w=0\) a.e. on
   \(\{w=0\}\) is the density/approximate-differentiability property of Sobolev
   functions ✓, and the distributional divergence of a \(W^{1,1}_{\rm loc}\)
   field is the a.e. trace of its weak gradient ✓.  The **first** clause is the
   unsupported one (see FIRST BAD BRIDGE and Lemma A).
10. Prop. 1.4/(1.6) ✓ unchanged and audited in round 1; the Stern
    arXiv:2403.19481v2 Lemma 2.2 / Thm. 2.9 scope note is unchanged and was
    confirmed [DI] in round 1 ✓.  The retirement of (H1') is correct: by
    (A1), (A3) the clauses \(w\in L^3\), \(D_3<\infty\) are unconditional ✓.
11. (1.8) ✓ (\(I_1:L^{3/2}\to L^3\); the CZ+Sobolev alternative is given, so
    the [MO] HLS citation is not load-bearing) ✓, scaling \((a,\lambda^0)\)
    on both sides ✓.

**§2 (classification).**  All exponent lattices recomputed from scratch.
12. §0 bookkeeping ✓ line by line: \(\mathcal Q\sim(a^3,\lambda^0)\),
    \(D_3\sim(a^3,\lambda^2)\), \(E\sim(a^2,\lambda^{-1})\),
    \(\|\sigma\|_{3/2}^{3/2}\sim(a^{3/2},\lambda^0)\),
    \(\int|w|\sigma^2\sim(a^3,\lambda^2)\), \(\int|q|^2|w|^3\sim(a^5,\lambda^2)\),
    \(\int|w|^5\sim(a^5,\lambda^2)\), \(\|\nabla A\|_{3/2}\sim(a^2,\lambda)\),
    \(\|\nabla V\|_2\sim(a^{3/2},\lambda)\), \(\|\nabla u\|_3\sim(a,\lambda)\),
    \(\nu\sim(a,\lambda^0)\), \(\mathcal Q',K,K_L,\nu D_3\sim(a^4,\lambda^2)\) ✓.
    \(\mathcal M\) is a cone and dilation-invariant ✓ (\(|aw|aw=a^2A\),
    \(|\lambda w(\lambda\cdot)|\lambda w(\lambda\cdot)=\lambda^2A(\lambda\cdot)\),
    both solenoidal) ✓.
13. §2.1 lattice \(3a+3b+2c=3\), \(2a-c+d=0\) ✓.  The FALSE entry ✓: the
    dilation \(w_\lambda=\lambda w(\lambda\cdot)\) fixes \(\mathcal Q\) and
    \(\|q\|_3\) and sends \(D_3\to\lambda^2D_3\) ✓, so
    \(\liminf_{D\downarrow0}\Phi(D,\mathcal Q_\star)\ge\|q_\star\|_3^3>0\) ✓.
    (2.1) ✓ re-derived with the interpolation identity
    \(\tfrac12=\tfrac47\cdot\tfrac34+\tfrac37\cdot\tfrac16\) and
    \(\|g\|_{4/3}^{8/7}=\|w\|_2^{12/7}\) ✓; scaling
    \((a^3,\lambda^0)=(a^{12/7},\lambda^{-6/7})(a^{9/7},\lambda^{6/7})\) ✓.
    The OPEN status of the mixed family is honest: only \(\|u\|_2\le\|w\|_2\)
    is available ✓.  *Supporting observation (mine, not in the note):* the
    degenerate route to a counterexample is closed — if \(u=0\) then HF17
    uniqueness forces \(q=0\), i.e. \(w=0\), so \(\|w\|_2/\|u\|_2\) cannot be
    driven up by letting \(u\to0\) at fixed \(w\); the note's suggested
    exterior 3-harmonic decay computation remains the right test.
14. §2.2 lattice: \(3a+3b+2c=5\), \(2a-c=2\), i.e. \(a=1+c/2\),
    \(b=\tfrac23-\tfrac76c\), \(0\le c\le\tfrac47\) ✓ (equivalently \(7a+3b=9\)).
    Prop. 2.1/(2.2) ✓ re-derived: \(\int|q|^2|w|^3=\|q|V|\|_2^2\le\|q\|_3^2\||V|\|_6^2
    \le(1+C_3)^2S^2\|w\|_3^2\|\nabla|V|\|_2^2\), then
    \(\|\nabla|V|\|_2\le\|\nabla V\|_2\), \(\|\nabla V\|_2^2\le\tfrac98D_3\),
    \(\|w\|_3^2=(3\mathcal Q)^{2/3}\) ✓ — the displayed constant \(\tfrac98\) and
    the \(D_3^{\rm rad}\) variant with \(\tfrac94\) are both right ✓; scaling
    \((a^5,\lambda^2)\) ✓.  *Refutation attempt:* none possible — no divergence
    structure is used, and remark (a) says so; the corrected remark (b)
    ("order-sharp on single-scale fields whose gradient part is comparable to
    \(w\); vacuous when \(q=0\)") is now accurate ✓.  The FALSE entry off the
    line ✓ (two-parameter scaling of a witness with \(0<\text{LHS}<\infty\),
    \(0<E<\infty\); the §2.3 family at fixed \(\delta\) qualifies, since
    \(\sigma\not\equiv0\Rightarrow q\ne0\) and
    \(\int|q|^2|w|^3\le\|q\|_3^2\|w\|_9^3<\infty\)) ✓.
15. §2.3 lattice \(c=2a\), \(7a+3b=\tfrac32\) ✓.  Prop. 2.2 in the audit's
    Lemma R2 form ✓; the round-1 defects (B2)(i),(ii) are repaired.  I
    re-verified the construction end to end:
    \(\operatorname{curl}(\phi_0e_3)=(\partial_2\phi_0,-\partial_1\phi_0,0)\)
    gives \(A_0=8(1-|x|^2)^3_+(-x_2,x_1,0)\), \(|A_0|=8(1-|x|^2)^3_+\rho\) ✓;
    \(w_0=\sqrt8(1-|x|^2)^{3/2}_+\rho^{-1/2}(-x_2,x_1,0)=f(\rho,x_3)e_\varphi\)
    is azimuthal with \(\varphi\)-independent speed, hence
    \(\operatorname{div}w_0=(1/\rho)\partial_\varphi f=0\) and \(\sigma_0\equiv0\),
    \(q_0=0\), \(u_0=w_0\) ✓ (the note's identification of the bulk as
    solenoidal is correct, and \(D_3(w_0)\in(0,\infty)\): \(V_0\sim\rho^{3/4}\),
    \(\int|\nabla V_0|^2\sim\int\rho^{-1/2}\rho\,d\rho<\infty\)) ✓.
    \(A_1=\delta^2((2+\cos kx_1)\cos kx_2,\sin kx_1\sin kx_2,0)\) ✓ away from
    the cutoff; the zero set is \(\{\sin kx_1=0\}\cap\{\cos kx_2=0\}\) ✓
    (codimension two, since \(2+\cos\ge1\)), with linear vanishing, hence
    \(|w_1|\sim\delta(kd)^{1/2}\), \(|\nabla w_1|\sim\delta k(kd)^{-1/2}\in L^1_{\rm loc}\),
    \(|w_1||\nabla w_1|^2\sim\delta^3k^2(kd)^{-1/2}\in L^1_{\rm loc}\) ✓; the
    codimension-two removability step is legitimate (a line in \(\mathbb R^3\)
    has \(\mathcal H^{2}=0\)) ✓.  Cutoff bookkeeping ✓: with
    \(\psi\ni\chi((x-x_0)/R)\), the correction term is
    \(\delta^2(2+\cos kx_1)(\sin kx_2)k^{-1}\nabla^\perp\chi\), i.e. a *uniform*
    relative \(O((kR)^{-1})\) correction where \(\chi\sim1\), and where
    \(\chi\ll1\) the field is proportionally smaller, so no integral is
    disturbed ✓.  Exact homogeneity \(A_1=\delta^2F(kx)\Rightarrow w_1=\delta G(kx)\),
    \(\sigma_1=\delta k\Sigma(kx)\) ✓, and at \(R^3=\delta^{-2}\), \(k=\delta^{-1/2}\):
    \(D_3\sim\delta^3k^2R^3=1\), \(\int|w|^3\sim\delta\), \(\int|w|^2\sim1\),
    \(\int|\sigma|^{3/2}\sim(\delta k)^{3/2}R^3=\delta^{-5/4}\) ✓, \(kR=\delta^{-7/6}\to\infty\) ✓.
    Positivity of \(\langle|\Sigma|^{3/2}\rangle\) ✓ proved analytically and
    correctly: on \(\{\sin y_2=0\}\), \(F=\pm(2+\cos y_1)e_1\) so
    \(\hat F\cdot\nabla|F|=\mp\sin y_1\not\equiv0\), and
    \(\Sigma=\tfrac12|F|^{-1/2}\hat F\cdot\nabla|F|\), locally integrable
    (\(|\Sigma|^{3/2}\sim d^{-3/4}\)) ✓.  *My own numerics* (\(1024^2\), one
    periodic cell) reproduce the note's table row to \(<0.2\%\):
    \(\langle|\sigma|^{3/2}\rangle=0.1897\) (note \(1.890\times10^{-1}\)),
    \(D_3=2.1877\) (note \(2.186\)), \(\int|w|^3=1.8477\) (note \(1.848\)),
    identity residual \(1.4\times10^{-3}\) (note \(1.3\times10^{-3}\)) ✓.
    The conclusion "no locally bounded \(\Phi\)" is correct **once the two
    lower bounds of Lemma B are inserted** (see S2); the honest retirement of
    the round-1 quantifier is right, and the class covers every power product
    (either sign of \(b\)), every continuous and every monotone \(\Phi\) ✓.
16. (2.3) ✓ all four, re-derived with constants:
    \(\int|w|\sigma^2\le\tfrac12D_3\) ✓;
    \(\|\nabla A\|_{3/2}\le\tfrac43 3^{1/6}\mathcal Q^{1/6}\|\nabla V\|_2\) ✓;
    \(\int|w|^5=\|g\|_{10/3}^{10/3}\le\|g\|_2^{4/3}\|g\|_6^2\le\tfrac94S^2(3\mathcal Q)^{2/3}D_3^{\rm rad}\)
    ✓; \(\|w\|_{9/2}^3=\|g\|_3^2\le\|g\|_2\|g\|_6\le C\mathcal Q^{1/2}(D_3^{\rm rad})^{1/2}\) ✓.
    Scalings \((a^3,\lambda^2)\), \((a^2,\lambda)\), \((a^5,\lambda^2)\),
    \((a^3,\lambda)\) ✓.  (Label slip only: the Hölder-interpolation exponent
    for \(\|g\|_{10/3}\) is \(2/5\) on \(\|g\|_2\) and \(3/5\) on \(\|g\|_6\);
    the displayed inequality is right.  See S4.)
17. §2.5 (W): the reclassification FALSE → OPEN follows round-1 Lemma R3 ✓ and
    the reasoning is reproduced correctly (\(A_2\) is sufficient, not necessary;
    the \(A\equiv0\)-on-a-ball witness annihilates both sides; the unweighted
    analogue is a multiplier bound of norm \(\le1\)).  *My own refutation
    attempt:* to break (W) the weight must be small exactly where
    \(\nabla(I-S_L)\mathbb Pw\) is large; a distant high-frequency packet
    produces only a rapidly decaying nonlocal tail inside a low-amplitude
    region, and a zero set of order \(\beta>1/3\) makes both sides converge
    together (Rmk. 1.2).  I found no counterexample; OPEN is the correct status.
    "Moot for size bounds" ✓: (A5) reaches the same endpoint without (W).
18. §2.6 summary table ✓ every row matches the section it cites, with the
    scaling column correct, including \(\int|w|^{-1}\Pi_L^2\sim(a^5,\lambda^2)\)
    and \(\|w(u)\|_2\le C\|u\|_2\sim(a,\lambda^{-1/2})\).

**§3 (the high-strain term).**
19. (3.2)–(3.3) ✓ (item 4 above); the note's own remark that no sign of
    \(K_L\) is used anywhere is accurate ✓.
    \(\nabla\Pi_L=-(I-\mathbb P)[(u^{hi}\cdot\nabla)A]\) ✓ (both sides reduce to
    \(-\nabla\Delta^{-1}\partial_i\partial_jT_{ij}\)), matching HF18-A (F7) ✓.
20. Prop. 3.1 ✓ all three identities re-derived independently, including the
    cyclic step \(q\cdot(\omega\times u)=\omega\cdot(u\times q)\) in (3.4),
    the \(\varepsilon\varepsilon\) identity in (3.5), and the \(ij\)-symmetry
    in (3.6) ✓; all pairings \(L^{3/2}\cdot L^3\cdot L^\infty\subset L^1\) ✓.
    The Hessian reading ✓ (\(\hat w\cdot S(u)\hat w=\sigma-\partial_{\hat w\hat w}\varphi\),
    \(\operatorname{div}w=\Delta\varphi\), then (1.4) with \(\alpha=3\)); the
    relabelling of the cross-check as "conditional only through the
    \(q\)-derivative step" is now accurate, since (1.4) is unconditional ✓.
    The sign remark against vortex stretching ✓.
21. (3.7) ✓ re-derived: \(K_L-K^S_L=\int q\cdot((A\cdot\nabla)v)-\int A\cdot((w\cdot\nabla)v)\)
    ✓ and Bernstein \(\|\nabla S_Lu\|_\infty\le C2^{5L/2}\|u\|_2\) ✓; constant
    slip only (\(2\to2+C_3\), see S4).  (3.7') ✓ from (A5) plus the same
    estimate; scaling \((a^4,\lambda^2)\) on both sides ✓.
22. Route (a) ✓ (Hölder \(\tfrac23+\tfrac13\); dies at \(\|\sigma\|_{3/2}\) by
    Prop. 2.2; the removal of CLMS and \(I_2:\mathcal H^1\to L^3\) is correct —
    round 1 had already listed them as unnecessary).
23. Route (b) ✓ (3.8) weighted Cauchy–Schwarz with (1.3') ✓; scaling
    \(\int|w|^{-1}\Pi_L^2\sim a^{-1}\lambda^{-1}\cdot a^6\lambda^6\cdot\lambda^{-3}=(a^5,\lambda^2)\)
    ✓; the downgrade from round 1's "can be \(+\infty\)" to "not proved finite,
    not refuted" is the honest status ✓; the heuristic absorption condition
    \(|u^{hi}|\lesssim\nu2^L\) is indeed a supercritical sup bound ✓.
24. Route (c) ✓ (3.9) arithmetic and scaling \((a^4,\lambda^2)\) ✓; the
    Young step and the closure condition \(\mathcal Q^{2/3}\lesssim\theta\nu^2\iff\|u\|_3\lesssim\nu\)
    ✓; obstruction (i) correctly demoted to moot and (ii) correctly identified
    as the whole content, with the S2 caveat carried ✓.
25. Route (d) ✓ (\(\operatorname{tr}S=0\Rightarrow\lambda_{\min}\le0\le\lambda_{\max}\);
    \(\hat w\) frozen by \(A\); R9 quoted faithfully) ✓.
26. Circularity sweep ✓: no bound is used to prove anything from
    \(\|\nabla u\|_\infty\), \(\|u\|_\infty\), \(\|u\|_9\), \(\|\nabla u\|_3\)
    or \(\sup_t\|u\|_3\); where they appear they are displayed as the failure.
    No identity is presented as an estimate; the "equivalent rewriting
    discharges nothing" rule is stated three times ✓.  No HIGH-STRAIN,
    HIGH-PRESSURE or NS-R3 claim appears ✓.  All numerics are declared as
    bounded evidence, not proof ✓.
27. §4 items 1–10 ✓ each matches its section with the corrected signs
    (items 4 and 8 now carry Lemma R1/§0 signs ✓), and §5 matches §§1–3 —
    **except** the two summary lines corrected in S3.

## REPLACEMENT ARGUMENT

**Lemma A (the missing step of §1.3; supplies S1).**  Let \(w\in L^3(\mathbb R^3;\mathbb R^3)\)
with \(V=|w|^{1/2}w\in H^1(\mathbb R^3)\) (audited (A1)), and assume (H1)
\(w\in W^{1,1}_{\rm loc}\).  Then the weak gradient \(\nabla^{\!w}w\) satisfies
\[
 \nabla^{\!w}w=D\Psi(V)\nabla V\ \text{ a.e. on }\{w\ne0\},\qquad
 \nabla^{\!w}w=0\ \text{ a.e. on }\{w=0\},
\]
so \(\operatorname{div}w=-\sigma\) a.e. and, \(w\) being \(W^{1,1}_{\rm loc}\),
also in \(\mathcal D'(\mathbb R^3)\), with \(\sigma\in L^1_{\rm loc}\).  Hence
(1.3'') holds, and every (H1)-conditional item of the note ((1.7)–(1.8), (3.3),
the Hessian reading, routes (a),(b)) is licensed.

*Proof.*  Put \(\Theta(z)=|z|^{1/2}z\), so \(V=\Theta(w)\), \(w=\Psi(V)\),
\(D\Theta(z)=|z|^{1/2}(I+\tfrac12\hat z\otimes\hat z)\) with eigenvalues
\(|z|^{1/2},|z|^{1/2},\tfrac32|z|^{1/2}\); a direct multiplication gives
\(D\Psi(\Theta(z))=D\Theta(z)^{-1}\) for \(z\ne0\)
(\(|V|^{-1/3}|z|^{1/2}=1\) on \(\hat z^\perp\) and
\(\tfrac23|V|^{-1/3}\cdot\tfrac32|z|^{1/2}=1\) along \(\hat z\)).
By the Calderón–Zygmund theorem, a \(W^{1,1}_{\rm loc}\) function is
approximately differentiable a.e., with approximate differential equal to its
weak gradient a.e.; apply this to \(w\) and to \(V\in H^1\subset W^{1,1}_{\rm loc}\),
and let \(x_0\) be a point of approximate differentiability and approximate
continuity of both with \(w(x_0)\ne0\) (a.e. point of \(\{w\ne0\}\) is such).
Since \(\Theta\) is \(C^1\), hence Lipschitz, on a neighbourhood \(N\) of
\(w(x_0)\), and \(\{|w-w(x_0)|>\eta\}\) has density \(0\) at \(x_0\), the
composition \(V=\Theta(w)\) is approximately differentiable at \(x_0\) with
approximate differential \(D\Theta(w(x_0))\nabla^{\!w}w(x_0)\).  Approximate
differentials are unique, so \(\nabla V(x_0)=D\Theta(w(x_0))\nabla^{\!w}w(x_0)\),
i.e. \(\nabla^{\!w}w(x_0)=D\Psi(V(x_0))\nabla V(x_0)\).  On \(\{w=0\}\): a.e.
point of a measurable set is a point of density \(1\), and at such a point of
approximate differentiability with \(w(x_0)=0\) the approximate differential
must vanish.  Taking the trace of the first display and using Prop. 1.1 gives
\(\operatorname{div}w=-\sigma\) a.e.; for \(w\in W^{1,1}_{\rm loc}\) the
distributional divergence is the a.e. trace of the weak gradient. \(\square\)

(Equivalently, one may keep the round-1 truncation chain rule
\(|DF_R|\le2\min(|z|,R)\) on \(A=F(w)\); Lemma A is shorter and does not need a
majorant for \(|w||\nabla w|\).)

**Lemma B (the two missing lower bounds in Prop. 2.2; supplies S2).**  For the
note's family, with \(w_\delta=w_0+w_1\) on disjoint supports:
\[
 D_3(w_\delta)=D_3(w_0)+D_3(w_1)\ \ge\ D_3(w_0)>0,\qquad
 \|\mathbb Pw_\delta\|_2\ \ge\ \|w_0\|_2>0 .
\]
*Proof.*  Additivity of \(D_3\) is disjointness of the supports of
\(V_\delta=V_0+V_1\), and \(0<D_3(w_0)<\infty\) was checked in Evidence 15.  For
the second bound, \(w_0\) is solenoidal and in \(L^2\), so \(\mathbb Pw_0=w_0\)
and, \(\mathbb P\) being an \(L^2\)-orthogonal projection,
\(\langle w_0,\mathbb Pw_\delta\rangle=\langle\mathbb Pw_0,w_\delta\rangle
=\langle w_0,w_0+w_1\rangle=\|w_0\|_2^2\) (disjoint supports); Cauchy–Schwarz
gives \(\|\mathbb Pw_\delta\|_2\ge\|w_0\|_2\). \(\square\)
With Lemma B the triples \((D_3,\mathcal Q,\|u\|_2^2)(w_\delta)\) do lie in a
fixed compact \(K\subset(0,\infty)^3\), which is what the finite-subcover step
of Prop. 2.2 needs; without a lower bound on \(\|u\|_2^2\) a locally bounded
\(\Phi\) could blow up as \(E\downarrow0\) and the contradiction would fail.

**Scope corrections required before integration (no proof needed).**

* **S1.**  §1.3: replace "Under (H1) the approximate gradient is the weak
  gradient" by Lemma A (or by the round-1 truncation argument).  As written,
  the whole (H1) branch rests on an unproved identification.
* **S2.**  §2.3, "Conclusion" paragraph: insert Lemma B before the compactness
  step, and state the two lower bounds explicitly in the display of Prop. 2.2
  (\(\tfrac1C\le D_3\le C\), \(\tfrac1C\le\|\mathbb Pw_\delta\|_2^2\le C\)).
* **S3.**  Hypothesis hygiene: the abstract ("The only remaining hypothesis,
  (H1) … gates the potential formula \(q=-\nabla(\Gamma*\sigma)\) and the
  pairing form \(K_L=\int\sigma\Pi_L\)") and the §5 line "Conditional on (H1):
  … potential formula (1.7)–(1.8), pairing form (3.3)" both drop the second
  hypothesis \(\sigma\in L^{3/2}\), which §1.5, §3.2, §3.3(a),(b) and §4 items
  4, 8 state correctly.  \(\sigma\in L^{3/2}\) does **not** follow from (H1)
  (which yields only \(\sigma\in L^1_{\rm loc}\)) and, by the note's own
  Prop. 2.2, cannot be certified by the controlled quantities; so those items
  are conditional on (H1) **and** (H2) \(\sigma\in L^{3/2}\).  Correct both
  summary statements (this is the same class of defect as S1 in the HF18-A
  audit: the body is right, the summary drops the caveat).
* **S4.**  Three small slips, none affecting a conclusion: (i) (3.7)'s constant
  is \((2+C_3)\|\nabla v\|_\infty\|w\|_3^3\), not \(2\|\nabla v\|_\infty\|w\|_3^3\),
  since \(\|q\|_3\le(1+C_3)\|w\|_3\); (ii) in (2.3) the Gagliardo–Nirenberg
  label "\(\theta=3/5\)" is the \(L^6\) share — the \(L^2\) share is \(2/5\)
  (the displayed inequality is correct); (iii) Rmk. 1.3 cites "the
  mollification argument of HF18-A Corollary 1(c) (audited)", but Cor. 1(c) is
  proved for \(\beta=\tfrac13\) only; say "the same mollification argument,
  re-run for \(\beta\in[1,3]\)" (I verified it goes through: \(|V|^\beta\to\)
  in \(L^2_{\rm loc}\) needs \(2\beta\le6\)), and display the absolute
  convergence \(|w|^{\alpha-1/2}\in L^2\iff\alpha\in[2,5]\).
* **S5 (optional, bookkeeping).**  §0 declares \(2^L\sim(1,\lambda)\) (needed
  for the scaling check of (3.7)–(3.7')), while the FALSE entry of §2.1 holds
  \(L\) fixed under dilation.  Both are legitimate, but say which: the §2.1
  refutation applies to inequalities claimed **uniformly in \(L\)** with \(L\)
  independent of the field; it does not refute a bound in which \(2^L\) is
  allowed to depend on \(w\) (e.g. \(2^L\gtrsim(D_3/\mathcal Q)^{1/2}\)).

## CONDITIONAL SUFFIX THAT SURVIVES

Everything the note claims survives, with S1–S4 applied and the hypothesis
sets read as follows.

*Unconditional* (fixed time of a classical solenoidal \(u\in H^m\), \(m\ge4\),
or every \(w\in\mathcal M\); on the audited (A1)–(A5)):

* Prop. 1.1: a.e. on \(\{w\ne0\}\), with \(\nabla w=D\Psi(V)\nabla V\),
  \(\operatorname{div}w=-\hat w\cdot\nabla|w|=-\sigma\), equivalently
  \(\operatorname{tr}((I+\hat w\otimes\hat w)\nabla w)=0\); and
  \(|w|^{1/2}\sigma=\tfrac23\hat V\cdot\nabla|V|\in L^2\) with
  \(\int|w|\sigma^2\le D_3^{\rm rad}\le\tfrac12D_3(w)\).
* \(\int|w|^\alpha\sigma=0\) for \(2\le\alpha\le5\) (Rmk. 1.3), in particular
  \(\alpha=3\) as used in §3.2.
* \(\mathcal M=\{|A|^{-1/2}A:A\in L^{3/2},\operatorname{div}A=0\}\), each
  \(w\in\mathcal M\) is the minimizer of \(\mathbb Pw\),
  \(\mathcal Q(\mathbb Pw)=\tfrac13\|A\|_{3/2}^{3/2}\) (Prop. 1.4).
* \(\int|q|^2|w|^3\le\tfrac98(1+C_3)^2S^2(3\mathcal Q)^{2/3}D_3(w)\) (Prop. 2.1),
  and the four bounds (2.3).
* \(K_L=\int q\cdot\nabla\Pi_L=-\langle\operatorname{div}w,\Pi_L\rangle\) with
  \(\Pi_L=R_iR_j(A_iu^{hi}_j)\), \((I-\mathbb P)F=-\nabla\Pi_L\) (3.1)–(3.2);
  \(\int A\cdot((q\cdot\nabla)u)=0\);
  \(\mathcal Q'+\nu D_3(w)=-\int|w|w\cdot S(u)w=\int|w|\omega\cdot(q\times u)\)
  (Prop. 3.1); \(|K_L-K^S_L|\le C2^{5L/2}E_0^{1/2}\mathcal Q\) and
  \(|K_L|\le C_*\mathcal Q^{1/3}D_3+C2^{5L/2}E_0^{1/2}\mathcal Q\).
* The classification of §2.6, with the TRUE rows proved, the FALSE rows
  refuted by the displayed scaling families (the \(\|\sigma\|_{3/2}\) row in
  the locally-bounded class only, and with Lemma B inserted), and the OPEN
  rows genuinely open.

*Conditional on (H1)* (Lemma A): \(\operatorname{div}w=-\sigma\) in
\(\mathcal D'\), \(\sigma\in L^1_{\rm loc}\) (1.3'').

*Conditional on (H1) and (H2) \(\sigma\in L^{3/2}\)*:
\(q=-\nabla(\Gamma*\sigma)\), \(\|q\|_3\le C_{\rm HLS}\|\sigma\|_{3/2}\)
(never better than the trivial bound in controlled quantities),
\(K_L=\int\sigma\Pi_L\), the Hessian reading of (3.6), and routes (a),(b).

*The frozen-gap suffix*, correctly stated by the note: the round-1 proviso
"if \(D_{\mathcal Q}\ge cD_3\)" **is discharged** by audited HF18-A Theorem 2
(\(D_{\mathcal Q}=D_3(w)\)); what remains is exactly one hypothesis — if
\(\int_0^\tau\!\big(-\int|w|w\cdot S(u^{hi})w\big)dt\le\theta\nu\int_0^\tau D_3(w)\,dt+A_{\rm input}\)
uniformly for \(\tau<\min(H,T_*)\) with \(\theta\le1\) and input-only finite
\(A_{\rm input}\), then (3.7), HF17 (13)–(14) and Gronwall give
\(\mathcal Q(\tau)+(1-\theta)\nu\int_0^\tau D_3\le e^{C2^{5L/2}E_0^{1/2}\tau}(\mathcal Q(0)+A_{\rm input})\),
hence \(\sup_t\|u\|_3\), \(u\in L^3_tL^9_x\), and continuation by the imported
ESS node.  Not proved; equivalent to the frozen gap.

## UNNECESSARY DEPENDENCIES

* HLS (Lieb–Loss / Stein) [MO] for (1.8): the note itself gives the
  CZ + Sobolev alternative, so nothing is load-bearing on a metadata-only
  source ✓.  Stern [DI] is a scope disclaimer, not a step.  Iwaniec–Martin,
  Scott, Iwaniec–Scott–Stroffolini, Uhlenbeck, CLMS, \(I_2:\mathcal H^1\to L^3\),
  Gilbarg–Trudinger: correctly removed or explicitly non-load-bearing.
* \((\mathrm{H2})\ \sigma\in L^{3/2}\) is **not** needed in route (b): the
  integrand splits as \((|w|^{1/2}\sigma)(|w|^{-1/2}\Pi_L)\) and the first
  factor is unconditionally in \(L^2\) by (1.3'), so (3.8) needs only (H1)
  plus finiteness of \(\int|w|^{-1}\Pi_L^2\) (modulo an approximation step for
  the pairing).  Route (b) can be stated one hypothesis lighter.
* Prop. 2.1 remains standalone: §3.3(c) reaches the same bound from (2.3), and
  the note says so.  Its remark (a) (no divergence structure used) is the
  honest limitation.
* The numerical table of §2.3: still not load-bearing — the homogeneity is a
  one-line identity and \(\langle|\Sigma|^{3/2}\rangle>0\) is proved
  analytically.  It is now corroborated three times (author \(384^2\), round-1
  audit \(1024^2\), this audit \(1024^2\), agreeing to \(<0.2\%\)).
* §2.5 (W) is informative only: by (A5) it is moot for size bounds, as the
  note states.

## NON-CLAIMS

This audit proves no theorem beyond Lemmas A and B, which are elementary and
serve only to close S1 and S2.  It establishes: no \(W^{1,1}_{\rm loc}\),
continuity or higher regularity of \(w\) — (H1) remains a hypothesis and
HF18-A's audited NON-CLAIMS stand; no \(\sigma\in L^{3/2}\); no bound, sign or
time-integrated absorption for \(K\), \(K_L\), \(K^S_L\) or \(\mathfrak T\)
beyond the audited size bound (A5); no truth or falsity of (W); no finiteness
or infinitude of \(\int|w|^{-1}\Pi_L^2\); no \(L^2\) bound for the nonlinear
projection \(u\mapsto w(u)\); no applicability of \(p\)-Laplace or
\(p\)-harmonic-form regularity theorems; no continuation criterion, no
HIGH-STRAIN and no HIGH-PRESSURE theorem; no NS-R3 result.  Prop. 2.2 and its
repaired form refute static inequalities on \(\mathcal M\) only and say nothing
about which \(w\) occur along Navier–Stokes trajectories.  My numerics
(\(256^2\) FFT sign checks, \(1024^2\) profile checks) are bounded evidence at
finite resolution, not proof.  NS-R3 remains OPEN.

## REOPENING CONDITION

Any one of: (1) an audited proof or disproof of (H1) for the minimizer — a
proof makes (1.3''), (1.7)–(1.8) (with (H2)), (3.3) and the Hessian reading
unconditional, a disproof retires them and leaves only (1.1) at the
distributional level; (2) a proof that \(\sigma\in L^{3/2}\) either always
holds or can fail on \(\mathcal M\cap(\mathrm{H1})\), which settles (H2) and
therefore routes (a),(b); (3) an input-only bound for \(\int|w|^{-1}\Pi_L^2\),
or an example in \(\mathcal M\cap(\mathrm{H1})\) with \(\Pi_L\ne0\) on a
codimension-one zero of \(w\) making it infinite, which closes route (b) one
way or the other; (4) a proof or refutation of (W) with the weight tied to the
input, which would settle the structure (not the smallness) of route (c);
(5) execution of the note's NEXT DISTINCT ACTION — a family
\(A=\operatorname{curl}\Psi\) with \(\|q\|_3/\|w\|_3\) driven up (HF18-A audit
R9) and \(\hat w\) aligned to the expanding eigenvector of \(S(\mathbb Pw)\),
with \(-\int|w|^3\hat w\cdot S(\mathbb Pw)\hat w\gg\nu D_3\) at bounded
\(\mathcal Q\) — which would show that no static inequality closes the gap;
(6) a decision on \(\|w(u)\|_2\le C\|u\|_2\), which converts every OPEN row of
§2.6 with \(c>0\) into TRUE or FALSE (note that \(u=0\Rightarrow w=0\), so the
degenerate route to a counterexample is closed).
