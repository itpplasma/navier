# HF20: a local harmonic-strain sign test for the cubic gradient quotient

Status: **audited, REPAIR applied by the controller**, 2026-09-06. The
independent audit `hf20-review-harmonic-strain-test.md` found no invalid
mathematics and one statement-level defect: Theorem 1.1 was displayed
one-sidedly and so did not literally entail the two-sign conclusion that its
own proof gives. The controller applied the audit's repair R1 below
(Theorem 1.1', absolute value, same constant, proof unchanged) and its
citation action for the regularity step. Everything else was verified,
including by the auditor's independent numerics.

Provenance. The candidate arrived as a typeset PDF on the work capture
surface, not as a repository note. It was produced on 2026-09-05 20:13 UTC
(pdfTeX, 7 pages) and dropped at `<vault path, not in this repository>`
on 2026-09-06 07:33; the controller moved it to
`<work vault, not in this repository>/navier-hf20-candidate-proof.pdf`. Frozen by
SHA-256 `4be9a53b244ba385e7b1e18bf02bee9b10db44a4329438612742ac32b7e15009`.
The PDF is the immutable artifact; this file is the controller's transcription
of its mathematics into the repository's evidence format, because generated
PDFs are not committed. Wording is condensed; every displayed statement,
constant, and hypothesis is reproduced as written. Discrepancies between this
note and the frozen PDF are resolved in favour of the PDF.

The candidate states that it was written against research revision
`30d715d20bc3ec4760929b8d598cf05e31d5fcfc` and paper revision
`39ccb664bf055fac94b3cfac97bf00a60191373d`, which are the current heads. It
describes itself as self-checked, with no independent component or
integration review performed, and promotes nothing.

MODE: FALSIFY, against instantaneous and monotone mechanisms on the quotient
route. The datum-dependent signed spacetime hypothesis is explicitly not
attacked.

## 0. Setting

All integrals are over \(\mathbb R^3\). With
\[
 \mathcal G_3=\overline{\{\nabla\phi:\phi\in C_c^\infty\}}^{L^3},\qquad
 F(z)=\tfrac13\|z\|_3^3,\qquad j(z)=|z|z,
\]
write \(w(v)=v+q(v)\) for the unique minimizer of \(F\) on \(v+\mathcal G_3\) and
\[
 \mathcal Q(v)=F(w(v)),\quad N(v)=(v\cdot\nabla)v,\quad
 K(v)=-\langle j(w(v)),N(v)\rangle,\quad
 D_{\mathcal Q}(v)=-\langle j(w(v)),\Delta v\rangle. \tag{0.1}
\]
Pairings are between \(L^{3/2}\) and \(L^3\). No differentiability of \(w\), in
space or in its argument, is part of the definition. These are the objects of
the manuscript's `sec:quotient`.

## 1. Claimed conclusions

**Theorem 1.1' (explicit transport sign test; two-sided form, audit repair R1).**
There are \(U,h\in C_c^\infty(\mathbb R^3)^3\) with
\(\operatorname{div}U=\operatorname{div}h=0\), \(U\neq0\), and a computable finite
\(C_*\), such that for every \(|\varepsilon|\le1\)
\[
 \bigl|K(U+\varepsilon h)+\varepsilon\|U\|_3^3\bigr|\le C_*|\varepsilon|^{3/2}. \tag{1.1}
\]
Both signs of \(K\) therefore occur on smooth compactly supported solenoidal
fields.

The candidate displayed (1.1) without the absolute value, which is one-sided
and does not entail the sentence after it, nor the lower bound in (4.5), nor
\(k=K(V)>0\) in §5. Its proof does entail all of them: in the expansion of
\(K(v_\varepsilon)+\varepsilon c_0\) below, each of the four terms is bounded in
absolute value by (4.2), by \(\|A_\varepsilon-A_0\|_{3/2}\le L|\varepsilon|\), and by
Hölder, and \(|\varepsilon|^3\le\varepsilon^2\le|\varepsilon|^{3/2}\) for
\(|\varepsilon|\le1\), so the triangle inequality gives the two-sided bound with the
same \(C_*\) of (4.4). No new hypothesis and no new constant. The rest of the
note is read against this form.

**Theorem 1.2 (actual solutions at prescribed energy).** For each \(\nu>0\) and
\(E>0\) there is a solenoidal \(v_0\in C_c^\infty\) with \(\|v_0\|_2^2=E\) whose
local classical solution of the original unforced equation satisfies
\(\tfrac{d}{dt}\mathcal Q(v(t))\big|_{0^+}>0\); and, for every \(\beta\),
\[
 \sup\{K(v)-\beta\nu D_{\mathcal Q}(v)\;:\;v\in C_c^\infty,\ \operatorname{div}v=0,\ \|v\|_2^2=E\}=+\infty. \tag{1.2}
\]
Here \(E\) is the squared \(L^2\) norm, not half of it. The solution is the
ordinary Schwartz-data classical branch, not a weak nonunique, Euler, forced,
or modified-viscosity substitute; only local existence is used.

**Corollary 5.1 (scope of the obstruction).** Neither \(\mathcal Q\) nor any
strictly increasing scalar function of it is nonincreasing along every
unforced classical trajectory. There is no finite energy-only
\(B(E,\nu,\beta)\) making \(K(v)\le\beta\nu D_{\mathcal Q}(v)+B\) hold pointwise
over all smooth solenoidal \(v\) of fixed squared \(L^2\) norm.

## 2. Variational preliminaries used

The candidate reproves what it needs rather than importing the unaudited
HF19 linearization.

**Lemma 2.1.** The minimizer exists and is unique; \(\langle j(w(v)),g\rangle=0\)
for \(g\in\mathcal G_3\) and \(\|w(v)\|_3\le\|v\|_3\); if \(j(v)\) annihilates
\(\mathcal G_3\) then \(w(v)=v\); and for \(b>0\), \(T_\lambda v(x)=\lambda v(\lambda x)\),
\[
 w(bv)=b\,w(v),\qquad w(T_\lambda v)=T_\lambda w(v). \tag{2.1}
\]
Proof by reflexivity, weak closedness of \(\mathcal G_3\), weak lower
semicontinuity, strict convexity, and invariance of \(\mathcal G_3\) under both
maps.

**Lemma 2.2 (two convexity bounds).** With
\(B(a,d)=\tfrac13|a+d|^3-\tfrac13|a|^3-j(a)\cdot d\),
\[
 B(a,d)\ge\tfrac14|a||d|^2,\qquad B(a,d)\ge\tfrac16|d|^3,\qquad
 |j(a+d)-j(a)|\le(2|a|+|d|)|d|, \tag{2.2}
\]
from the identity
\((j(a)-j(b))\cdot(a-b)=\tfrac{|a|+|b|}2\big(|a-b|^2+(|a|-|b|)^2\big)\).

**Lemma 2.3 (derivative, heat sign, evolution).** \(\mathcal Q\) is continuously
Fréchet differentiable on \(L^3\) with \(D\mathcal Q(v)[z]=\langle j(w(v)),z\rangle\);
for \(v\in C_c^\infty\), \(0\le D_{\mathcal Q}(v)\le\|v\|_3^2\|\Delta v\|_3\); and
along a classical branch with \(v\in C^1_tL^3\), \(\Delta v,N(v),\nabla p\in L^3\),
\(p\in W^{1,3}\),
\[
 \tfrac{d}{dt}\mathcal Q(v(t))=-\nu D_{\mathcal Q}(v(t))+K(v(t)). \tag{2.3}
\]
The pressure drops out because a gradient of a \(W^{1,3}\) function lies in
\(\mathcal G_3\). This is the manuscript's `prop:quotient-evolution` re-derived
for the compactly supported setting.

## 3. The swirl and the localized harmonic gradient

With \(b(t)=\exp(-1/(1-t^2))\) for \(|t|<1\) and zero otherwise, and
\(s(r,z)=b(4r-6)b(2z)\), set \(U=s(r,z)e_\theta\), \(e_\theta=(-y/r,x/r,0)\),
extended by zero near the axis. Its support has \(5/4\le r\le7/4\), \(|z|\le1/2\).
With \(\rho=|U|=s\), azimuthal independence gives
\[
 \operatorname{div}U=0,\quad \operatorname{div}(\rho U)=0,\quad
 N(U)=-\tfrac{\rho^2}{r}e_r,\quad U\cdot N(U)=0, \tag{3.1}
\]
so \(w(U)=U\): the swirl already lies on the nonlinear-Hodge class. The
identities are checkable in Cartesian coordinates, so no coordinate
singularity enters.

Let \(\chi\in C_c^\infty\) equal one on the ball of radius 3 and vanish outside
the ball of radius 4, given explicitly by
\(\chi(x)=\eta(16-|x|^2)/(\eta(16-|x|^2)+\eta(|x|^2-9))\) with \(\eta(t)=e^{-1/t}\)
for \(t>0\). With
\[
 a=(yz,-xz,0),\quad \phi=\tfrac12(x^2+y^2)-z^2,\quad
 h=\operatorname{curl}(\chi a),\quad g=\nabla(\chi\phi),\quad e=h-g, \tag{3.2}
\]
both \(h,g\) are smooth and compactly supported, \(\operatorname{div}h=0\),
\(g\in\mathcal G_3\), and on a neighbourhood of \(\operatorname{supp}U\)
\[
 h=g=(x,y,-2z),\qquad \nabla h=\operatorname{diag}(1,1,-2), \tag{3.3}
\]
because \(\operatorname{curl}a=\nabla\phi=(x,y,-2z)\) and \(\Delta\phi=0\). The
field \(e\) vanishes on the ball of radius 3, so its support is disjoint from
that of \(U\); also \(U\cdot h=0\) on \(\operatorname{supp}U\).

The candidate's Remark 3.1 stresses that no locality of the nonlinear
minimizer is asserted: the compact curl and the compact gradient agree
exactly near the swirl, their difference lives outside it, and the
subsequent estimates are global and include any tail of the actual
minimizing representative.

## 4. The competing gradient and the coefficient

For \(v_\varepsilon=U+\varepsilon h\) put \(w_\varepsilon=w(v_\varepsilon)\),
\(d_\varepsilon=w_\varepsilon-U\), \(C_e=\tfrac13\|e\|_3^3\). The competitor
\(q=-\varepsilon g\) gives, exactly because the supports are disjoint,
\(\mathcal Q(v_\varepsilon)\le F(U+\varepsilon e)=F(U)+C_e|\varepsilon|^3\).
Moreover \(\langle j(U),d_\varepsilon\rangle=0\): the pairing with
\(\varepsilon h\) vanishes pointwise, and the pairing with \(q(v_\varepsilon)\)
vanishes since \(\operatorname{div}j(U)=0\). Integrating Lemma 2.2,
\[
 0\le\mathcal Q(v_\varepsilon)-\mathcal Q(U)\le C_e|\varepsilon|^3,\quad
 \int\rho|d_\varepsilon|^2\le4C_e|\varepsilon|^3,\quad
 \|d_\varepsilon\|_3^3\le6C_e|\varepsilon|^3. \tag{4.1}
\]
The candidate calls this the decisive gain, and stresses that it follows from
a special competitor, not from any derivative of the minimizer.

With \(A_\varepsilon=j(w_\varepsilon)\), \(A_0=j(U)\),
\(N_0=N(U)\), \(N_1=(h\cdot\nabla)U+(U\cdot\nabla)h\), \(N_2=(h\cdot\nabla)h\),
one has \(N(v_\varepsilon)=N_0+\varepsilon N_1+\varepsilon^2N_2\). Put
\(d_0=(6C_e)^{1/3}\), \(M=\|U\|_3\), \(L=(2M+d_0)d_0\). Then
\(\|A_\varepsilon-A_0\|_{3/2}\le L|\varepsilon|\), and since \(r>1\) on
\(\operatorname{supp}U\) gives \(|N_0|\le\rho^2\),
\[
 |\langle A_\varepsilon-A_0,N_0\rangle|
 \le 4\sqrt{C_e}\,\|U\|_5^{5/2}|\varepsilon|^{3/2}+4C_e\|U\|_\infty|\varepsilon|^3. \tag{4.2}
\]
The coefficient of \(\varepsilon\) is elementary:
\(\langle A_0,(h\cdot\nabla)U\rangle=\int h\cdot\nabla(\rho^3/3)=0\) by compact
support and \(\operatorname{div}h=0\), while \((U\cdot\nabla)h=U\) on the swirl
by (3.3), so
\[
 \langle A_0,N_1\rangle=\int\rho|U|^2=\|U\|_3^3=:c_0>0,\qquad
 \langle A_0,N_0\rangle=0. \tag{4.3}
\]
Expanding the pairing gives
\(K(v_\varepsilon)+\varepsilon c_0=-\langle A_\varepsilon-A_0,N_0\rangle
-\varepsilon\langle A_\varepsilon-A_0,N_1\rangle-\varepsilon^2\langle A_0,N_2\rangle
-\varepsilon^2\langle A_\varepsilon-A_0,N_2\rangle\), whence Theorem 1.1 with
\[
 C_*=4\sqrt{C_e}\|U\|_5^{5/2}+4C_e\|U\|_\infty+M^2\|N_2\|_3
 +L(\|N_1\|_3+\|N_2\|_3), \tag{4.4}
\]
all norms of explicitly given compact smooth fields. For
\(0<\varepsilon<\varepsilon_0:=\min\{1,(c_0/(2\max\{1,C_*\}))^2\}\),
\[
 K(U-\varepsilon h)\ge\varepsilon c_0/2>0,\qquad
 K(U+\varepsilon h)\le-\varepsilon c_0/2<0, \tag{4.5}
\]
which the candidate presents as an analytic sign certificate rather than a
sign read off a numerical minimization.

## 5. Transfer to actual solutions at any fixed energy

Fix such an \(\varepsilon\), let \(V=U-\varepsilon h\), \(k=K(V)>0\),
\(d=D_{\mathcal Q}(V)\ge0\), \(E_V=\|V\|_2^2>0\). By (2.1),
\[
 \mathcal Q(bT_\lambda V)=b^3\mathcal Q(V),\quad
 \|bT_\lambda V\|_2^2=b^2\lambda^{-1}E_V,\quad
 K(bT_\lambda V)=b^4\lambda^2k,\quad
 D_{\mathcal Q}(bT_\lambda V)=b^3\lambda^2d. \tag{5.1}
\]
Given \(\nu,E>0\), choose \(b\) with \(bk>\nu d\), for instance the
minimizer-free \(b=1+2\nu\|V\|_3^2\|\Delta V\|_3/(\varepsilon c_0)\) using
Lemma 2.3 and (4.5), set \(\lambda=b^2E_V/E\) and \(v_0=bT_\lambda V\); then
\(v_0\) is compact, smooth, solenoidal, with squared \(L^2\) norm exactly \(E\).
Tao Theorem 5.4(ii),(iv) supplies the local smooth branch at unit viscosity;
for general \(\nu\) apply it to \(v_0/\nu\) and rescale by
\(v(t,x)=\nu\tilde v(\nu t,x)\), \(p(t,x)=\nu^2\tilde p(\nu t,x)\), which is exactly
the inverse of the manuscript's `eq:nu-normalization`. The candidate then
sketches, from the high-Sobolev and higher-time-derivative bounds, that
\(v\in C^1_tL^3\) up to zero and \(p\in W^{1,3}\) on a short interval, which are
exactly the hypotheses of Lemma 2.3. **Audit integration action:** that sketch
is a one-sentence compression of a multi-step manuscript lemma and is replaced
by a citation of `prop:localtheory`(iii),(iv) and `lem:upgrade`, which prove
it. Tao 5.4(ii)'s smallness condition is available because only a short
interval for one fixed datum is needed. No continuation theorem is used. Then (2.3) at zero gives
\[
 \tfrac{d}{dt}\mathcal Q(v(t))\big|_{0^+}=\lambda^2b^3(bk-\nu d)>0, \tag{5.2}
\]
hence strict increase for small positive times, and letting \(b\to\infty\) with
\(\lambda=b^2E_V/E\) gives
\(K-\beta\nu D_{\mathcal Q}=(E_V^2/E^2)b^7(bk-\beta\nu d)\to+\infty\), which is
(1.2).

## 6. What the candidate says it does not prove

The counterexample is to universal monotonicity and to a specified
instantaneous energy-only estimate. It is not a singular solution. It does
not give an unbounded critical norm on one fixed trajectory: the fields used
for the fixed-energy supremum have unbounded initial critical norms as
\(b\to\infty\). It does not contradict
\[
 \int_0^\tau K\,dt\le\theta\nu\int_0^\tau D_{\mathcal Q}\,dt+A(u_0,\nu,H),
 \qquad 0\le\theta<1, \tag{6.1}
\]
uniformly for \(\tau<\min(H,T_*)\) with a remainder depending on the entire
datum, which is the manuscript's `hyp:highstrain`; that hypothesis and the
precise fixed-cutoff form remain open, and no new cutoff or witnesses are
identified. The field \(h\) is a direction in the space of data, not the
Navier–Stokes time derivative at \(U\), so (1.1) is not a computation of
\(dK(u(t))/dt\) along the trajectory from \(U\); the actual-flow argument starts
at the perturbed, amplified datum \(v_0\).

## 7. Controller assessment (superseded by the independent audit)

The audit `hf20-review-harmonic-strain-test.md` verified every point listed
below and added independent numerical falsification attempts against each
pointwise input, all of which failed to refute. It also confirmed
compatibility with the audited HF18-A bound: on the family \(bT_\lambda V\) the
ratio of the two sides is exactly scale-invariant, and HF18-A's
\(\dot{\mathcal Q}\le(C_*\mathcal Q^{1/3}-\nu)D_{\mathcal Q}\) forces any increase to
live at supercritical \(\mathcal Q^{1/3}>\nu/C_*\), which is exactly where this
candidate's amplification parameter puts it. The two agree.

## 7. Controller assessment (not an audit)

Relation to the repository at the revisions the candidate names.

- It is consistent with, and sharper than, the unaudited HF19-B lane, whose
  non-claims already recorded that monotonicity of \(\mathcal Q\) fails at
  large amplitude at time zero. HF19-B found the favourable sign on its swirl
  class; HF20 perturbs off that class in a direction where the sign reverses,
  and supplies an analytic certificate rather than numerics.
- It does not import HF19; §2 reproves its inputs. Its only external theorem
  is Tao 5.4(ii),(iv), already an imported node (TAO-LOCAL) with pages 52–53
  directly inspected in `cp01-literature-statements.md`.
- Structurally it is the quotient-route analogue of the audited HF03/HF04
  fixed-energy obstructions on the pressure route, and it carries the same
  scope: an obstruction to instantaneous and energy-only mechanisms, not to
  the datum-dependent spacetime hypothesis.
- If it survives audit, the manuscript's `sec:quotient` gains a scope remark
  (no monotone or instantaneous energy-only mechanism is available for
  \(\mathcal Q\)), and the graph's HIGH-STRAIN review text records one more
  excluded mechanism class. Nothing in it would promote or close a node.

Points an audit must examine first, in reading order: the exactness of
\(\mathcal Q(v_\varepsilon)\le F(U+\varepsilon e)\) under disjoint supports and
whether the competitor is admissible in \(\mathcal G_3\) rather than merely in
the smooth compact gradients; the vanishing \(\langle j(U),d_\varepsilon\rangle=0\),
which uses \(\operatorname{div}j(U)=0\) for the *unperturbed* field and the
definition of \(\mathcal G_3\) for the minimizer's own gradient part; the
\(|\varepsilon|^{3/2}\) rate in (4.2) and whether Cauchy–Schwarz with weights
\(\rho^{1/2}|d_\varepsilon|\), \(\rho^{5/2}\) is applied on the right set; the
claim \(w(U)=U\), i.e. that the swirl is exactly its own minimizer; the
regularity chain from Tao 5.4 to \(v\in C^1_tL^3\) and \(p\in W^{1,3}\) claimed
in §5, which is the same upgrade the manuscript proves as `lem:upgrade` and
should be cited rather than re-derived; and whether the scaling exponents in
(5.1) are consistent with the manuscript's `lem:quotient-scaling`.

## Frontier record

**MODE / RESULT:** FALSIFY, **audited REPAIR, repair applied**. Established:
an analytic two-sign certificate for the transport term of the cubic gradient
quotient on smooth compactly supported solenoidal fields, and a transfer
showing the quotient strictly increases on actual classical trajectories at
every viscosity and every prescribed squared \(L^2\) norm, with the
fixed-energy supremum of \(K-\beta\nu D_{\mathcal Q}\) infinite.

**CLAIM AND SCOPE:** as stated in Theorems 1.1, 1.2 and Corollary 5.1, for
the original unforced equation on \(\mathbb R^3\), arbitrary \(\nu>0\), smooth
compactly supported solenoidal data, using only local existence.

**FIRST GAP:** unchanged. The input-only spacetime bound (6.1) uniformly for
\(\tau<\min(H,T_*)\) is neither proved nor refuted here.

**SURVIVING CONDITIONAL SUFFIX:** if the candidate passes audit, the excluded
class grows by universal monotonicity of \(\mathcal Q\) and by instantaneous
energy-only absorption; the conditional consumer
`prop:quotient-conditional` is untouched, since it consumes the spacetime
hypothesis and not a monotonicity statement.

**NON-CLAIMS:** no singular solution; no unbounded critical norm on a fixed
trajectory; no refutation of `hyp:highstrain` or `hyp:highpressure`; no
regularity or blowup result; no novelty claim; no promotion of any graph
node. NS-R3 remains open.

**NEXT DISTINCT ACTION:** done for this note. The audit returned REPAIR, the
repair is applied above, and the controller has integrated the result: a scope
remark in `sec:quotient` and an extended HIGH-STRAIN review in the graph. The
research question it leaves is the one the audit names: the excluded class now
covers universal monotonicity and instantaneous energy-only absorption, so the
surviving direction is the time-integrated sign structure of the transport
term, pursued in wave HF21.
