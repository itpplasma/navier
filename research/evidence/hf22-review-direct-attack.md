# Audit of HF22-D: direct attack on (G), the frozen gap in product form

Lane HF22-D, MODE: AUDIT (proof-audit protocol), 2026-09-06. This file is the
only file written by this audit. Nothing is promoted; the manuscript is
untouched; no commit or push is made.

**Frozen target.** `research/evidence/hf22-direct-attack.md`,
`sha256 = 4945036f17c325353175c8667b180ac02a53552090888a48f50a70e1743fc38f`
(984 lines), at repository HEAD `e36fec455e970a004519e5c91b856a3e1bba28bc`
(`/home/ert/proj/navier`, branch `main`, clean). Manuscript read at
`/home/ert/proj/navier-paper` HEAD `4084330f6b8130241c7afbde3878861229c4cceb`,
`main.tex` (7098 lines).

**Directly inspected [DI].** `main.tex`: `lem:upgrade` (674),
`prop:localtheory` (1195), `lem:div-zero` (1830), `def:sobolev-constant`
(2007), `lem:sobolev` (2093), `lem:interp` (2126), `prop:energy` (2164),
`prop:scaling` with \eqref{eq:L4L3}, \eqref{eq:L4L3-constant} (2227),
`rem:mismatch` (2345), the convention line 2542
(\((\nabla u)^{\mathsf T}u=|u|\nabla|u|\)), `lem:integrands` (2640),
`def:D3P3` (2677), `prop:pressure` (2799), lines 3080–3085 (the identification
\(V(u,\nabla u)=|u||\nabla|u||^2\), \(W(u,\nabla u)=u\cdot\nabla|u|\)),
`prop:lowpressure` (3492), `hyp:highpressure` (3638), `hyp:absorption` (3652),
`lem:absorption-split` (3669), `prop:existential-equivalence` (3708),
`rem:existential-scope` (3808), `cor:absorption-consequence` (3823),
`thm:continuation` (4664), `hyp:critical` (4695), `thm:conditional` (4721),
`subsec:quotient-conventions` with import (F5) (4881, 4940),
`lem:leray` (5264), `lem:quotient-coercive` (5454), `lem:quotient-stability`
(5590), `lem:quotient-pressure` (5953), `lem:quotient-chainrule` (5996),
`def:qe-dissipation` (6216), `lem:quotient-heatsign` (6229),
`prop:quotient-evolution` (6698), `rem:qe-evolution-scope`,
`rem:distance-balance` (6768), `hyp:highstrain` (6843),
`rem:highstrain-normalisation` (6875), `prop:quotient-conditional` (6901),
`rem:highstrain-scope` (6953), `rem:no-monotone` (6983).
Repository: `hf18-hodge-regularity.md` (§ around lines 222, 285, 430–463, 507),
`hf21-crossing-sign-structure.md` (Remark 2.2, Prop. 3.1, Prop. 3.2, Prop. 3.3
and its scope paragraph, Thm. 4.1, Thm. 4.5, Lemma R3, O1, O2, O3),
`hf18-divergence-speed-link.md` (Prop. 3.1 strain form, (3.2), (3.6)).

---

## VERDICT

**REPAIR.** The note's new mathematics is, with one constant-tracking
exception, correct: every displayed identity and inequality of §1.1–§1.3, §2,
§3.1, §3.2 (the identity itself), §3.3 and §3.4 reconstructs. What does **not**
survive is a layer of *scope* claims that the note promotes to results and puts
in its MODE/RESULT summary and its CLAIM AND SCOPE block. Three of these are
false as stated, and one of the three is the note's own headline result 3.
Specifically:

- **B1 (first bad bridge, §1.4).** "(G) is strictly stronger than the frozen
  gap along a fixed trajectory … Proving (G) therefore proves more than the gap
  needs." Non-derivability of the converse is proved; strictness is not, and
  the supporting parenthetical does not survive inspection.
- **B2 (§2, Proposition 2.4).** "\(\sup_{t<\tau}\|q(t)\|_3<\infty\), which by
  (E3) is equivalent to \(\sup_{t<\tau}\|u(t)\|_3<\infty\)" is **false**, and
  is refuted by a fact the note itself cites (HF21-B §3.3). (E3) supplies one
  direction only. The correct blocking of the \(s\to\infty\) endpoint is at the
  *other* factor.
- **B3 (§3.2, decisive).** "Exactly two scalar functionals of the trajectory
  are differentiable in time at the audited level" and "every exact
  time-integration by parts available is the chain rule for
  \(G(\mathcal Q,F,t)\)" are **false**: \(E(t)=\tfrac12\|u(t)\|_2^2\) is a
  third, its exact balance is `prop:energy`, and the note lists that very
  balance as its own audited input (E4). Theorem 3.2 is a correct closure
  statement about the *displayed family* \(G(\mathcal Q,F,t)\) and nothing
  more; the note's "retires a mechanism class" is not established.
- **B4 (summary items 3(ii) and 4).** The summary misstates Theorem 3.2(2) by
  dropping the variable \(t\) ("a weight that is not a function of
  \(\mathcal Q\) alone necessarily activates the pressure flux"), and then
  claims §3.4 "escapes (i)–(iii)". Both are wrong: Proposition 3.4 is the
  member \(G=\rho(t)\mathcal Q\) of the very family of Theorem 3.2, it
  satisfies \(n\equiv0\) with \(m=\rho(t)\) a function of \((\mathcal Q,t)\)
  alone, and it obeys (i). It escapes (iii) only.
- **B5 (§3.4, Corollary 3.5).** (H-mod) is not circular — that check passes —
  but the note's account of *why* it is open is misdiagnosed, and (H-mod) is
  **implied by \(T_*>H\)**, hence by the Clay conclusion. A proof is supplied
  below (Lemma R1). Consequently the NEXT DISTINCT ACTION's assertion that
  (H-mod) is "falsifiable by construction" is wrong: no construction short of
  a blow-up can falsify it.
- **B6 (constants).** \(C_{\rm pr}\) and the \(\int_0^\tau\|p\|_3\,dt\) bound
  are stated with \(C_{\rm CZ}(r)\) defined for a *single* \(R_iR_j\), while
  \(p=R_iR_j(u_iu_j)\) is a nine-term sum; the proved constants carry an extra
  factor \(\le9\). Three further small slips are listed under EVIDENCE.

Everything in §1.1–§1.3, §2 (except the endpoint sentence), §3.1, §3.2's
identity (3.2)–(3.3) with consequences 1–3 read as statements about the family
\(G(\mathcal Q,F,t)\), §3.3 and §3.4's arithmetic survives, with the constant
corrections of B6. The first gap is unchanged; the note does not close it and
does not claim to.

---

## REVIEWED SCOPE

Reconstructed from the first nontrivial implication, with every constant and
exponent recomputed independently:

§0 audited-fact table (E1)–(E9); §1.1 Lemma 1.1 and (1.1); §1.2 Lemma 1.2
((1.2), (1.3)) and Proposition 1.3 ((1.4)) and Corollary 1.4; §1.3 the
comparison table, Proposition 1.5, Remarks 1.6–1.7; §1.4 Proposition 1.8 and
both scope bullets; §2 Propositions 2.1, 2.3, 2.4, Corollary 2.2 and the
summary; §3.1 Lemma 3.1 and (3.1); §3.2 Theorem 3.2 with consequences 1–3;
§3.3 Corollary 3.3 and (3.4); §3.4 Proposition 3.4, Corollary 3.5 with (H-mod),
Remarks 3.6–3.7; §4 self-check table; §5 frontier record.

Not re-proved (used inside audited scope): HF17 functional and evolution;
HF18-A; HF18-B Prop. 3.1 and (3.2) only; HF21-A; HF21-B as repaired; the
manuscript labels listed above. HF23 is **not** used as a premise by the note
and is not used here. No note in the reviewed chain assumes (H1) or any other
open regularity of \(w\): the note uses HF18-B only through Prop. 3.1's strain
form (unconditional) and (3.2) (comparison only), and never upgrades an
approximate-gradient statement to a weak-derivative one. That check passes.

---

## FIRST BAD BRIDGE

**§1.4, second paragraph, first bullet.**

> **(G) is strictly stronger than the frozen gap along a fixed trajectory.**
> \((\mathrm G)\Rightarrow\) `hyp:highstrain`, but the converse per trajectory
> is not available: only \(|K|\le C_\sharp d_1D_3(w)\) is audited, one
> direction, and \(K\) may vanish where \(d_1D_3(w)\) does not (\(K\) is a
> contraction of \(S(u)\) against \(\hat w\otimes\hat w\), HF18-B (3.6), which
> vanishes on a codimension-one set of strains). Proving (G) therefore proves
> more than the gap needs.

The sentence up to "one direction" is correct and is a *non-derivability*
statement. The bracket and the concluding sentence convert it into *falsity of
the converse*, i.e. strictness, and neither step holds.

1. The bracket treats \(S(u)\) and \((\hat w,d_1,D_3(w))\) as independently
   variable. They are not: \(w=u+q(u)\) is the nonlinear-Hodge minimizer of
   \(u\) and \(S(u)\) is the symmetric gradient of the same \(u\). "A
   codimension-one set of strains" is a statement about the algebraic map
   \(S\mapsto\hat w\cdot S\hat w\) at frozen \(\hat w\); it is not a statement
   about the set of admissible fields \(u\), and no field \(u\) with
   \(K(u)=0<d_1(u)D_3(w(u))\) is exhibited anywhere in the note or in the
   audited record. (Such fields plainly exist — see the swirl family below,
   which has \(K=0\) *and* \(d_1=0\) — but that family does not separate the
   two quantities.)
2. Even granting the bracket pointwise, an instantaneous inequality
   \(K(t)<C_\sharp d_1(t)D_3(w(t))\) on a set of times does not make the
   time-integrated statement \((\mathrm G)\) strictly stronger than
   `hyp:highstrain`. By the note's *own* Proposition 1.8, \((\mathrm G)\) and
   `hyp:highstrain` are **equivalent** at the quantifiers at which both are
   posed (both are equivalent to \(T_*=\infty\)). So "strictly stronger" is
   false at the stated quantifiers and unproved at any other. This is exactly
   the instantaneous-to-time-integrated promotion the protocol asks to hunt
   for, running in the direction of a claimed obstruction rather than a claimed
   theorem.

The bridge is **unsupported**, not load-bearing (nothing in §2–§3 uses it), and
repairable by deletion of the strictness clause; the audit continued past it.
The identical fallacy recurs in Remark 3.7 ("The reverse … is **false**"), which
should read "is not available".

---

## EVIDENCE

### E1. What reconstructs exactly (recomputed independently)

**Conventions.** The manuscript's \(V(a,\mathsf G)=|\mathsf G^{\mathsf T}a|^2/|a|\)
is identified at `main.tex` line 2542 and lines 3080–3083 as
\(|u|\,|\nabla|u||^2\), and \(W(u,\nabla u)=u\cdot\nabla|u|\). Hence
\(D_3(u)=\int(|u||\nabla u|^2+|u||\nabla|u||^2)\) and \(P_3=\int p\,u\cdot\nabla|u|\).
The note's readings of `def:D3P3` are correct; I verified them a second time by
re-deriving `prop:pressure`'s viscous term
\(-\nu\int r_\varepsilon u\cdot\Delta u\to\nu\int(|u||\nabla u|^2+|u||\nabla|u||^2)\).

**Lemma 1.1.** \(P_3=\int p\,u\cdot\nabla|u|=\int p\,\operatorname{div}(|u|u)\)
for solenoidal \(u\) ✓. \(|u|u\) is \(C^1\) with \(\nabla(|u|u)=|u|\nabla u+u\otimes\nabla|u|\),
vanishing where \(u=0\), so \(\sigma_u\) is the continuous function the note
uses ✓. \(\langle\operatorname{div}j(u),p\rangle=-\langle j(u),\nabla p\rangle\)
is legitimate: \(j(u)\in L^{3/2}\), \(\nabla p\in L^3\), \(\sigma_u\in L^{3/2}\),
\(p\in L^3\) ✓. \(\langle\mathbb Pj(u),\nabla p\rangle=\langle j(u),\mathbb P\nabla p\rangle=0\)
by `lem:quotient-pressure` and `lem:leray`(c) ✓. So
\(P_3=-\langle(I-\mathbb P)j(u),\nabla p\rangle\) ✓, and both Hölder bounds ✓.
Vanishing on \(\mathcal M\) ✓. Scaling \((a^4,\lambda^2)\) confirmed by direct
substitution of \(u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t)\) ✓.

**Lemma 1.2.** \(D\Phi(z)h=|z|^{1/2}(h+\tfrac12(\hat z\cdot h)\hat z)\) ✓;
\(|\partial_kW|^2=|u|(|\partial_ku|^2+\tfrac54(\hat u\cdot\partial_ku)^2)\) —
the cross term contributes \(2\cdot\tfrac12=1\) and the square term
\(\tfrac14\), total \(\tfrac54\) ✓; \(\hat u\cdot\partial_ku=\partial_k|u|\) ✓;
hence \(|\nabla W|^2=|u||\nabla u|^2+\tfrac54|u||\nabla|u||^2\) and
\(D_3(u)\le\|\nabla W\|_2^2\le\tfrac54D_3(u)\) ✓ (both comparisons are the
coefficient comparison \(1\le\tfrac54\) term by term). \(\|W\|_6=\|u\|_9^{3/2}\),
\(\|W\|_2^2=\|u\|_3^3\) ✓. So \(D_3(u)\ge\frac4{5S^2}\|u\|_9^3\) ✓ — (1.3) is
correct and is, as the note says, elementary.

**Proposition 1.3.** \(|P_3|\le(\int p^2|u|)^{1/2}D_3(u)^{1/2}\) ✓;
Hölder \((\tfrac98,9)\) gives \(\int p^2|u|\le\|p\|_{9/4}^2\|u\|_9\) ✓
(\(\tfrac89+\tfrac19=1\)); \(\tfrac29=\tfrac12\cdot\tfrac13+\tfrac12\cdot\tfrac19\)
so \(\|u\|_{9/2}\le\|u\|_3^{1/2}\|u\|_9^{1/2}\) ✓; and
\(\|u\|_9^{3/2}\le(\tfrac54)^{1/2}S\,D_3(u)^{1/2}\) ✓. The exponent chain of
(1.4) is exact. Its constant is not (see B6). Scaling
\(\|u\|_3D_3(u)\sim(a^4,\lambda^2)=P_3\) ✓, and (1.4) is indeed the unique
scaling-consistent monomial in \((\|u\|_3,D_3(u))\) ✓.

**Corollary 1.4.** \(\tfrac13X'=-\nu D_3(u)+P_3\) is `prop:pressure`(ii) in
differentiated form; the continuity argument is HF18-A Corollary 4 verbatim ✓.
Correctly labelled "not new".

**Proposition 1.5, Remarks 1.6–1.7.** 1 ✓ (\(D_3(u)\sim(a^3,\lambda^2)\),
\(\|u\|_3\sim(a,\lambda^0)\), product \((a^3,\lambda^0)=\mathcal Q\) ✓). 3 ✓ —
this is the honest statement, and it is the right one. 4 ✓. Remark 1.6:
\(d_3\le\|u\|_3^{1/2}D_3(u)^{1/2}\) re-derived (\(\||u|^{1/2}\|_6=\|u\|_3^{1/2}\),
\(\||u|^{1/2}\nabla|u|\|_2\le D_3(u)^{1/2}\), \(\tfrac16+\tfrac12=\tfrac23\)) ✓;
Young ✓; \(\|p\|_3^2\|u\|_3\lesssim\|\nabla u\|_2^{4}\cdot\|\nabla u\|_2^{1/2}
=\|\nabla u\|_2^{9/2}\) ✓ using \eqref{eq:L4L3-constant}; and the critical
exponent for \(\nabla u\in L^r_tL^2_x\) is \(2-\tfrac32-\tfrac2r=0\Rightarrow r=4\) ✓,
audited input \(r=2\) ✓. Remark 1.7 ✓.

**Proposition 1.8.** All six implications check against the cited labels.
(F)\(\Rightarrow\)(A),(B) uses only compactness of \([0,H]\), continuity of
\(d_1\) (`lem:quotient-stability`), continuity of \(D_{\mathcal Q}\)
(`lem:quotient-heatsign`), and `prop:pressure`(i),(iii) ✓; the integrands are
nonnegative so \(\int_0^\tau\le\int_0^H\) ✓. (A)\(\Rightarrow\)(C) needs the
\(K_L/K_{\rm low}\) split, supplied by `rem:highstrain-normalisation` ✓; note
`hyp:highstrain` permits \(\theta\in[0,1]\) and `hyp:absorption` requires
\(\theta\in[0,1)\), and \(\theta=0\) is admissible for both ✓. This proposition
is correct and is the note's most useful piece of scope hygiene.

**§2.** \(\lambda(\infty,2)=\lambda(2,6)=\lambda(4,3)=\tfrac32\) ✓;
\(L^4_tL^3\) is the \(\theta=\tfrac12\) interpolant ✓ (\(\tfrac1r=\tfrac14\),
\(\tfrac1q=\tfrac14+\tfrac1{12}=\tfrac13\)); \(\lambda\) affine ✓; the
\(L^r_tL^q_x\) scaling exponent is \(1-\lambda(r,q)\) ✓ (recomputed:
\(\lambda^{1-3/q}\cdot\lambda^{-2/r}\)). Corollary 2.2: deficit \(\tfrac12\)
uniform ✓; the mixing relation \((1-\theta)\tfrac32+\theta\lambda_*=1\) forces
\(\theta=\frac1{2(3/2-\lambda_*)}\), equal to \(1\) at \(\lambda_*=1\) ✓ (the
note writes "\(\ge\)", harmless). Proposition 2.3: \(\lambda(3,9)=1\) ✓; both
identities are (E1) and (E2) ✓; the reading is correct. Proposition 2.4:
\(\lambda(3s',9)=\frac{2(s-1)}{3s}+\frac13=1-\frac2{3s}\) ✓; \(\tfrac29\) at
\(s=3\), \(\tfrac16\) at \(s=4\) ✓; the pressure-route mirror at the same
\(s=4\) ✓. **This is a genuine sharpening of HF21-B's O1**, which only reached
"\(u\in L^3_tL^9\) on a finite interval, i.e. at least as strong as the
conclusion"; the note's \(L^{3s'}_tL^9\) is the sharper space and the
\(\tfrac2{3s}\) is correct. It is also the natural attempt: the only audited
integrated control of the scalar factor is \(\int d_1^s\) at \(s\in\{3,4\}\),
and Hölder in \(t\) is the only split that uses it.

**§3.1 Lemma 3.1.** \(\int T(u):S(u)=\int u\cdot\nabla\frac{|u|^3}3=0\) by
`lem:div-zero` ✓; \(|DT(v)h|\le|v|^2|h|+2|v|^2|h|=3|v|^2|h|\) ✓, and along the
segment \(|u+sq|\le|u|+|w|\) ✓. Correctly labelled "one subtraction".

**§3.2 identity.** (3.2)/(3.3) is a correct chain rule for absolutely
continuous compositions; every integrability hypothesis is checked in the note
and re-checked here ✓. Consequences **as statements about the family
\(G(\mathcal Q,F,t)\)**: 1 ✓; 2 ✓ (the "conversely" clause needs no \(C^2\):
\(\partial_2G\equiv0\) on a connected domain already gives \(G=G(\mathcal Q,t)\));
3 ✓ (on \(\operatorname{supp}m\), \(C_\sharp d_1\le C_\sharp(1+C_3)3^{1/3}\mathcal Q^{1/3}=C_*\mathcal Q^{1/3}\)
by (E3), matching the audited \(C_*\) exactly ✓; the region is HF18-A
Corollary 4's, so the bound is true and empty ✓). Its final inequality
\(\int_0^{\mathcal Q(0)}m\le\min\{\mathcal Q(0),\mathcal Q_0\}\) silently uses
\(m\le1\), which the hypothesis does not state.

**§3.3 Corollary 3.3.** \(m=\varphi-\mathcal Q\varphi'\ge0\), \(n=\mathcal Q\varphi'\le0\) ✓;
\(m=1\) on \(\{d_2\le y_0\}\) ✓; \(\operatorname{supp}m\subset\{d_2\le2y_0\}\) ✓;
\(d_1\le(6d_2)^{1/3}\le(12y_0)^{1/3}\) and
\(y_0\le(1-\varepsilon)^3\nu^3/(12C_\sharp^3)\) is exactly the threshold ✓;
\(n(P_3-\nu D_3(u))=\mathcal Q\varphi'F'\) ✓. (3.4) is correct, and its reading
(a residual that *is* the pressure balance, weighted by the unknown
\(\mathcal Q\)) is correct.

**§3.4 Proposition 3.4, Corollary 3.5.** (3.5) ✓ (integration by parts against
a Lipschitz \(\rho\), \(\rho(\tau)\mathcal Q(\tau)\ge0\) dropped, \(\rho(0)\le1\),
\(|\rho'|\le\Lambda\), (E6)); (3.6) ✓; Corollary 3.5's arithmetic
\(\frac{(1-2\varepsilon)\nu}{C_\sharp}\cdot\frac{\mathcal Q(0)+\Lambda A_{\mathcal Q}}{\varepsilon\nu}\) ✓.
\(A_{\mathcal Q}=\tfrac13H^{1/4}(3S^2E_0^2/2\nu)^{3/4}\) re-derived from
`rem:highstrain-normalisation` ✓. The "\(\Lambda\)-cutoff exists iff every
passage takes time \(\ge1/\Lambda\)" equivalence ✓ (both directions
elementary). **(H-mod) is not circular**: it does not imply, and is not implied
by, \(\sup_t\|u\|_3<\infty\) by any displayed step, and the reduction to the
bad-set part is a genuine strict weakening of (G). That check passes.

### E2. Refutation of B2 (§2, Proposition 2.4's endpoint sentence)

The note writes: "\(s\to\infty\), where the hypothesis degenerates to
\(\sup_{t<\tau}\|q(t)\|_3<\infty\), which **by (E3)** is equivalent to
\(\sup_{t<\tau}\|u(t)\|_3<\infty\) — the conclusion itself (`hyp:critical`)."

(E3) = `lem:quotient-coercive` gives \(\|q\|_3\le(1+C_{\mathbb P})\|w\|_3\le(1+C_{\mathbb P})\|u\|_3\):
**one direction only**, \(\|u\|_3\) bounded \(\Rightarrow\) \(d_1\) bounded. The
converse is false pointwise, and the note's own §3.3 cites the fact that
refutes it.

*Explicit refutation.* Let \(\psi\in C_c^\infty((0,\infty)\times\mathbb R)\) and
put, in cylindrical coordinates \((r,\theta,z)\),
\(u=v(r,z)\,e_\theta\) with \(v=\psi(r,z)\). Then \(\operatorname{div}u=0\)
(pure swirl, \(\partial_\theta\) of nothing), \(|u|=|v(r,z)|\) is
\(\theta\)-independent, so
\(\operatorname{div}(|u|u)=u\cdot\nabla|u|=\frac{v}{r}\partial_\theta|v|=0\).
Hence \(u\in\mathcal M_{\rm sol}\), so \(w=u\), \(q=0\), \(d_1=0\), while
\(\|u\|_3=\|\psi\|_{L^3(r\,dr\,d\theta\,dz)}\) is arbitrary (replace \(\psi\) by
\(c\psi\)). This is precisely the statement HF21-B §3.3 records — "the criterion
is satisfied at every instant at which \(u(t)\in\mathcal M\), no matter how
large \(\|u(t)\|_3\) is, and \(\mathcal M_{\rm sol}\) contains fields of
arbitrarily large critical norm" — which the note cites elsewhere and
contradicts here.

*What the endpoint actually is.* At \(s=\infty\) (\(s'=1\)) the split reads
\(\int_0^\tau d_1D_3(w)\le(\sup_{t<\tau}d_1)\int_0^\tau D_3(w)\,dt\), and the
factor that is not input-bounded is \(\int_0^\tau D_3(w)\,dt\), not the
supremum of \(d_1\). By (E7) an input bound on \(\int_0^\tau D_3(w)\,dt\) puts
\(u\in L^3_tL^9_x\), the LPS endpoint, which by `thm:continuation` is the
conclusion. So the endpoint is blocked, but by the *dissipation* factor and at
exactly criticality (\(\lambda=1\)), not below it. The note's own Proposition
2.3 says this correctly two pages earlier; the endpoint sentence contradicts it
by attributing the blockage to the distance factor.

Consequence for the record: the family is blocked *at both factors* — strictly
subcritically by the dissipation factor for every finite \(s\) (overshoot
\(\tfrac2{3s}\)), and exactly critically at \(s=\infty\). The overshoot number
\(\tfrac2{3s}\) itself is unaffected and stands.

### E3. Refutation of B3 (§3.2, the exhaustion claim) — decisive

The note asserts, before Theorem 3.2:

> By `lem:quotient-chainrule` and `prop:pressure`, exactly two scalar
> functionals of the trajectory are differentiable in time at the audited
> level: \(\mathcal Q(t)\in C^1\) and \(F(t)=\frac13\|u(t)\|_3^3\) …

and after it:

> Theorem 3.2 is a closure statement … the *entire* stock of exact
> time-integrations by parts available from the audited record is (3.2) … the
> theorem says nothing else exists.

Both are false, and the counterexample is one of the note's own audited inputs.

*Counterexample.* `prop:energy` (`main.tex` 2164) is an exact balance,
\(\tfrac12\|u(t)\|_2^2+\nu\int_s^t\|\nabla u\|_2^2=\tfrac12\|u(s)\|_2^2\), and
its proof (Step 1) shows explicitly that \(E(t):=\tfrac12\|u(t)\|_2^2\) is
differentiable on \([0,T]\) with \(E'=-\nu\|\nabla u\|_2^2\). The note lists this
as (E4) and uses \(\int_0^{T_*}\|\nabla u\|_2^2\le E_0/2\nu\) in §2. So there
are at least **three** audited exactly-differentiable functionals, and the
admissible class is at least
\[
 G\in C^1(\mathbb R_{\ge0}^3\times[0,H]),\qquad
 G\bigl|_0^\tau=\int_0^\tau\Bigl[\partial_tG+m(K-\nu D_3(w))+n(P_3-\nu D_3(u))
 -\ell\,\nu\|\nabla u\|_2^2\Bigr]dt ,
\]
\(m=\partial_1G\), \(n=\partial_2G\), \(\ell=\partial_3G\) at
\((\mathcal Q(t),F(t),E(t),t)\). (Under package (R) the branch is
\(C^1([0,T];H^m)\), so \(\|u\|_{H^k}^2\) is differentiable for every
\(k\le m-1\) as well; the energy suffices to refute the claim and is the only
one with an audited exact balance in the manuscript.)

*What breaks.* Take \(G(\mathcal Q,F,E)=\mathcal Q\,\phi(E)\) with \(\phi\)
Lipschitz. Then \(m=\phi(E)\) is **not** a function of \((\mathcal Q,t)\) alone
and yet \(n=\partial_FG\equiv0\): the pressure flux is **not** activated. So the
note's headline (ii) — "a weight that is not a function of \(\mathcal Q\) alone
necessarily activates the pressure flux \(F'\)" — is false outside the family
\(G(\mathcal Q,F,t)\), and the claim that the theorem "upgrades HF21-B §4.2's
observation about one identity to a theorem about the whole family" over-reaches:
it is a theorem about *one* family, the one the note wrote down.

*What survives.* Theorem 3.2 remains true and useful as a closure statement over
the **displayed** family. That family does contain the three known members
(\(G=\mathcal Q\), \(G=F\), \(G=F-\mathcal Q\)) and the new members of §3.3–§3.4;
consequences 1–3 hold within it. What must go is the quantifier over "every exact
time-integration by parts available from the audited record". As the protocol
warns, an exhaustion claim over an informally specified class is not a theorem,
and this one is not merely informal — it is false at the first functional one
checks.

I did **not** find that the energy variable buys anything: the extra term
\(\ell\,\nu\|\nabla u\|_2^2\) with \(\ell=\mathcal Q\phi'(E)\) costs
\(\nu\sup|\phi'|\int_0^\tau\mathcal Q\|\nabla u\|_2^2\,dt\), which needs
\(\sup_t\mathcal Q\) and is therefore the conclusion. That is a *negative*
result about the enlarged class and should be recorded as such, not as an
exhaustion.

### E4. B4 (the summary misstates its own theorem)

MODE/RESULT item 3(ii) reads "a weight that is not a function of \(\mathcal Q\)
alone necessarily activates the pressure flux \(F'\)"; Theorem 3.2(2) reads
"\(n\equiv0\) … iff \(m\) is a function of \((\mathcal Q,t)\) alone". Dropping
\(t\) makes the summary false *within the note's own family*: Proposition 3.4 is
the member \(G(\mathcal Q,F,t)=\rho(t)\mathcal Q\), with \(m=\rho(t)\),
\(n\equiv0\), \(\partial_tG=\rho'(t)\mathcal Q\), and indeed (3.5) is exactly
(3.3) for that \(G\). Hence:

- §3.4's opening ("A weight that depends on \(t\) through the trajectory …
  escapes Theorem 3.2(2) — it is not of the form \(G(\mathcal Q,F)\)") is wrong
  twice: Proposition 3.4 is of the form \(G(\mathcal Q,F,t)\), and it *satisfies*
  consequence 2 rather than escaping it.
- MODE/RESULT item 4's "Weights that depend on \(t\) through the trajectory
  escape (i)–(iii)" is wrong for (i) — the weight of \(D_3(w)\) is \(\rho\), the
  weight of \(K\) is \(\rho\) — and wrong for (ii). It escapes **(iii)** only,
  because \(m=\rho(t)\) is not of the form \(m(\mathcal Q)\) with compact support
  in a Kato region, and it pays exactly \(\Lambda\int\mathcal Q\,dt\) for that.

This is the correct and interesting statement and it is not diminished by the
correction; it is the one genuinely new degree of freedom the note found.

### E5. B5 ((H-mod): the openness diagnosis is wrong, and (H-mod) is implied by the conclusion)

*(a) The stated reason is not the operative one.* The note says the audited
modulus "is not of this kind" because "its constant contains
\(\sup_t\|\partial_tu\|_3\) … and neither factor is input-bounded", and the
NEXT DISTINCT ACTION calls this a "trajectory-dependent constant". But (H-mod)
as displayed allows \(\Lambda=\Lambda(\nu,u_0,H)\), and \((\nu,u_0)\) determines
the trajectory. Trajectory dependence is therefore *permitted*. The operative
failure is different and should be stated as such: the constant
\(\sup_{t<\tau}\|\partial_tu(t)\|_3\) (and \(\sup_{t<\tau}\|w(t)\|_3\), through
HF21-B Remark 2.2) is not bounded **uniformly in \(\tau<T_*\)** when
\(T_*<\infty\). (H-mod) is a \(\tau\)-uniformity statement, exactly like
`hyp:highstrain` and `hyp:absorption`, not a trajectory-independence statement.

*(b) (H-mod) is implied by global existence on the horizon.* This is new and
must be recorded, because it fixes the note's forward plan.

> **Lemma R1.** Fix \(\nu>0\), a divergence-free Schwartz \(u_0\), \(0<H<\infty\)
> and \(\varepsilon\in(0,\tfrac12)\). If \(T_*>H\), then (H-mod) holds for that
> datum with a finite \(\Lambda=\Lambda(\nu,u_0,H,\varepsilon)\).
>
> *Proof.* \(t\mapsto d_1(t)=\|q(u(t))\|_3\) is continuous on the compact
> \([0,H]\) (`lem:quotient-stability` with \(u\in C([0,H];L^3)\); HF21-B
> Remark 2.2). Put \(A:=\{t\in[0,H]:C_\sharp d_1(t)\le(1-2\varepsilon)\nu\}\) and
> \(B:=\{t\in[0,H]:C_\sharp d_1(t)\ge(1-\varepsilon)\nu\}\); both are closed and
> \(A\cap B=\emptyset\). If \(A=\emptyset\) take \(\rho\equiv0\); if
> \(B=\emptyset\) take \(\rho\equiv1\); in both cases \(\Lambda=0\). Otherwise
> \(\delta:=\operatorname{dist}(A,B)>0\) by compactness, and
> \(\rho(t):=\max\{0,\,1-2\operatorname{dist}(t,A)/\delta\}\) is
> \((2/\delta)\)-Lipschitz, maps into \([0,1]\), equals \(1\) on \(A\), and
> vanishes wherever \(\operatorname{dist}(t,A)\ge\delta/2\), so
> \(\operatorname{supp}\rho\subset\{\operatorname{dist}(\cdot,A)\le\delta/2\}\),
> which is disjoint from \(B\). For \(\tau<\min\{H,T_*\}=H\), the restriction
> \(\rho|_{[0,\tau]}\) satisfies \(\rho=1\) on \(\mathcal G^{2\varepsilon}_\tau\)
> and \(\operatorname{supp}\rho\subset\mathcal G^{\varepsilon}_\tau\), with the
> same \(\Lambda=2/\delta\) for every \(\tau\). \(\square\)

Consequences the note must carry:

1. \(T_*=\infty\) for the datum \(\Rightarrow\) (H-mod) for that datum at every
   \(H\). Combined with the note's own Proposition 1.8, \((\mathrm G)\Rightarrow(\mathrm{H\text{-}mod})\).
   So (H-mod) sits **below** the conclusion, which is the right place for a
   hypothesis and confirms it is not circular — but also means it inherits the
   existential-equivalence pathology of `hyp:highstrain`: its entire content
   lies in the hypothetical \(T_*\le H\) branch.
2. **(H-mod) is not falsifiable by construction.** The NEXT DISTINCT ACTION
   states "Both are falsifiable by construction" of (H-mod) and of HF21-B
   sub-question (a). By Lemma R1, any counterexample to (H-mod) is a
   finite-time blow-up solution. HF21-B sub-question (a) (\(D_3(w)\le D_3(u)\))
   *is* falsifiable by construction, being a fixed-time statement about a single
   field. The lane's two continuations are therefore of completely different
   epistemic type and must not be presented as a matched pair.
3. The right form of the open question is quantitative:
   *is there \(\Lambda(\nu,u_0,H)\) bounding the reciprocal passage time
   \(1/\delta_\tau\) uniformly in \(\tau<\min\{H,T_*\}\)?* — equivalently, an
   input-only lower bound on the time \(C_\sharp d_1\) needs to cross from
   \((1-2\varepsilon)\nu\) to \((1-\varepsilon)\nu\), uniform up to the putative
   blow-up time.

*(c) Remark 3.6.* The crossing-number price is correctly identified and its
status ("no bound on \(N_\tau\) is available") is a non-derivability claim,
correctly labelled. Two small corrections: the endpoint sum runs over the
components of \(\mathcal G_\tau\), so the bound is \(2(N_\tau+1)\sup\mathcal Q\)
in general; and \(\mathbf 1_{\mathcal G_\tau}\) is of bounded variation only if
\(N_\tau<\infty\), which the remark should state as a hypothesis of its own
display rather than as a conclusion.

### E6. Constants (B6) and minor slips

1. **\(C_{\rm CZ}\) is applied to a nine-term sum.** The note defines
   \(C_{\rm CZ}(r)\) by \(\|R_iR_jf\|_r\le C_{\rm CZ}(r)\|f\|_r\) for a single
   pair \((i,j)\), then writes \(\|p\|_3\le C_{\rm CZ}(3)\|\,|u|^2\|_3\) and
   \(\|p\|_{9/4}\le C_{\rm CZ}(9/4)\|u\|_{9/2}^2\). But
   \(p=\sum_{i,j}R_iR_j(u_iu_j)\) (`rem:scaling-pressure`, import (F5)), so the
   triangle inequality gives \(\|p\|_r\le C_{\rm CZ}(r)\sum_{i,j}\|u_iu_j\|_r\)
   and \(\sum_{i,j}\|u_iu_j\|_r\le9\|\,|u|^2\|_r\) (from
   \(|u_iu_j|\le\tfrac12(|u_i|^2+|u_j|^2)\) and \(\||u_i|^2\|_r\le\|\,|u|^2\|_r\)).
   *Repair (either is acceptable, the first is cleaner):* redefine
   \(C_{\rm CZ}(r)\) as the operator norm of
   \(\mathsf F\mapsto\sum_{i,j}R_iR_j\mathsf F_{ij}\) on \(L^r(\mathbb R^3;\mathbb R^{3\times3})\)
   restricted to \(\mathsf F=u\otimes u\); or keep the single-pair definition and
   replace
   \(C_{\rm pr}=(\tfrac54)^{1/2}SC_{\rm CZ}(9/4)\) by
   \(C_{\rm pr}=9(\tfrac54)^{1/2}S\,C_{\rm CZ}(9/4)\) and
   \(\int_0^\tau\|p\|_3\,dt\le C_{\rm CZ}(3)S^2E_0/(2\nu)\) by
   \(\int_0^\tau\|p\|_3\,dt\le9\,C_{\rm CZ}(3)S^2E_0/(2\nu)\).
   The factor 9 is not claimed sharp. Nothing structural depends on it:
   Corollary 1.4 remains a smallness criterion of the same shape, and
   \((\mathrm G_P)\Rightarrow\)`hyp:absorption` is unaffected.
2. **"The quotient scalar is pointwise the smaller one" (Prop. 1.5(2)).** The
   displayed inequality is \(d_1\le(1+C_{\mathbb P})\|u\|_3\) with
   \(1+C_{\mathbb P}\ge2\); "smaller" is not proved and \(d_1\le\|u\|_3\) is not
   available. (The sharp elementary bound is \(d_1\le\|w\|_3+\|u\|_3\le2\|u\|_3\),
   which is what HF21-B Lemma 4.3's constant \(24S^2E_0^2/\nu\) uses; I verified
   \(16\cdot\tfrac32=24\).) Replace "pointwise the smaller one" by "pointwise
   comparable, with a constant, and vanishing on \(\mathcal M\) where
   \(\|u\|_3\) does not".
3. **Theorem 3.2(3)** uses \(\int_0^{\mathcal Q(0)}m\le\min\{\mathcal Q(0),\mathcal Q_0\}\),
   which needs \(m\le1\); add that normalisation to the hypothesis.
4. **Remark 3.7** states the reverse inequality "is false"; only "is not
   available" is proved (same fallacy as B1).

### E7. Checks that PASS (recorded so the controller does not redo them)

- No use of HF18-B beyond Prop. 3.1's strain form (unconditional, no (H1)) and
  (3.2) as a comparison line. **No silent upgrade of an approximate-gradient
  statement to a weak-derivative one anywhere**, and no use of the OPEN items of
  HF18-B (the weighted Calderón–Zygmund inequality, the \(L^2\) projection
  bound). The HF23 candidate is not used.
- No differentiation of \(d_1\), \(q\), \(w\), \(A\) anywhere; §3 differentiates
  only \(\mathcal Q\) and \(F\), both audited.
- No hidden circularity in Corollary 3.5: (H-mod) does not contain
  \(\sup_t\|u\|_3\) and does not imply (G).
- Scaling consistency of every new inequality, recomputed independently:
  (1.1) \((a^4,\lambda^2)\); (1.3) \((a^3,\lambda^2)\); (1.4) \((a^4,\lambda^2)\);
  (1.5) \((a^3,\lambda^0)\) both routes; (3.4)–(3.6) inherit (E1).
- Quantifiers of (G), \((\mathrm G_P)\), `hyp:highstrain`, `hyp:absorption`
  match the manuscript's (\(\theta\in[0,1]\) vs \([0,1)\) checked).
- Solution class is the classical branch of `prop:localtheory` on
  \(\mathbb R^3\), unforced, arbitrary \(\nu>0\), arbitrary divergence-free
  Schwartz datum, throughout. No periodic/forced/hyperdissipative substitute.
- No numerics are used as proof anywhere in the note; none were needed here.

---

## REPLACEMENT ARGUMENT

Three replacements; each is displayed with its proof.

**R-A (replaces the §1.4 bullet and Remark 3.7's "is false").**

> The converse of \((\mathrm G)\Rightarrow\) `hyp:highstrain` **per trajectory**
> is not derivable from the audited record: only the one-sided
> \(|K|\le C_\sharp d_1D_3(w)\) (HF21-B Prop. 3.1) is available, and no lower
> bound \(|K|\ge c\,d_1D_3(w)\) is audited or proved here. This is
> non-derivability, not falsity: no field with \(K=0<d_1D_3(w)\) is exhibited,
> and \(S(u)\), \(\hat w\), \(d_1\) and \(D_3(w)\) are all determined by the same
> \(u\) and cannot be varied independently. At the quantifiers of
> `hyp:highstrain`, Proposition 1.8 shows \((\mathrm G)\) and `hyp:highstrain`
> are in fact **equivalent**, so no strictness claim is available at those
> quantifiers either. The PLAN's phrase "the frozen gap is exactly (G)" is the
> audited HF21-B statement: (G) with \(\theta=0\) suffices, and no cutoff or
> Gronwall term is needed.

*Proof.* One-sidedness is HF21-B Prop. 3.1. The equivalence is the note's
Proposition 1.8, whose proof I verified. \(\square\)

**R-B (replaces the endpoint sentence of Proposition 2.4).**

> … and \(\to0\) only as \(s\to\infty\), where \(s'=1\) and the split reads
> \(\int_0^\tau d_1D_3(w)\,dt\le(\sup_{t<\tau}d_1)\int_0^\tau D_3(w)\,dt\). At
> that endpoint the demanded space is exactly \(L^3_tL^9_x\), \(\lambda=1\):
> criticality is reached, and the obstruction moves from the exponent to the
> factor. The blocking factor at \(s=\infty\) is the **dissipation** integral:
> an input bound on \(\int_0^\tau D_3(w)\,dt\) puts \(u\in L^3_tL^9_x\) by (E7),
> which is the LPS endpoint and gives \(T_*=\infty\) by `thm:continuation` — the
> conclusion itself. The distance factor is *not* the obstruction there:
> \(\sup_{t<\tau}\|q(t)\|_3<\infty\) is strictly weaker than
> \(\sup_{t<\tau}\|u(t)\|_3<\infty\), since (E3) bounds \(d_1\) by \(\|u\|_3\)
> and not conversely, and \(\mathcal M_{\rm sol}\) contains fields with
> \(d_1=0\) and arbitrarily large \(\|u\|_3\) (HF21-B §3.3). So the family
> \(\{s\in[1,\infty]\}\) is blocked at every member: strictly subcritically by
> the dissipation factor for finite \(s\) (overshoot exactly \(\tfrac2{3s}\)),
> and exactly critically at \(s=\infty\).

*Proof.* The exponent computation \(\lambda(3s',9)=1-\tfrac2{3s}\) is unchanged
and verified. \(\lambda(3,9)=1\) at \(s'=1\). The non-equivalence is the swirl
family \(u=\psi(r,z)e_\theta\) of E2: \(\operatorname{div}u=0\),
\(\operatorname{div}(|u|u)=\frac{\psi}{r}\partial_\theta|\psi|=0\), so \(u\in\mathcal M_{\rm sol}\),
\(q=0\), \(d_1=0\), \(\|u\|_3\) arbitrary. \(\square\)

**R-C (replaces the §3.2 preamble, the "Reading" paragraph, and MODE/RESULT
items 3 and 4).**

> Two of the functionals whose exact balances the audited record supplies are
> attached to the quotient and pressure routes: \(\mathcal Q\in C^1\) with
> \(\mathcal Q'=K-\nu D_3(w)\) (`lem:quotient-chainrule`,
> `prop:quotient-evolution`) and \(F=\frac13\|u\|_3^3\), absolutely continuous
> with \(F'=P_3-\nu D_3(u)\) (`prop:pressure`). The distance \(d_1\) is only
> \(\tfrac12\)-Hölder and is never differentiated (HF21-B Remark 2.2), and
> \(d_2=F-\mathcal Q\) is a function of the two. **Theorem 3.2 below is a closure
> statement over the family \(G(\mathcal Q,F,t)\) generated by these two
> functionals, and over nothing else.** It is not an exhaustion of "all exact
> time-integrations by parts": the audited record supplies at least one further
> exactly-differentiable functional, \(E=\frac12\|u\|_2^2\) with
> \(E'=-\nu\|\nabla u\|_2^2\) (`prop:energy`, quoted as (E6.0)), and under
> package (R) every \(\|u\|_{H^k}^2\), \(k\le m-1\), is differentiable as well.
> The enlarged family \(G(\mathcal Q,F,E,t)\) obeys
> \[
>  G\bigl|_0^\tau=\int_0^\tau\Bigl[\partial_tG+m(K-\nu D_3(w))+n(P_3-\nu D_3(u))
>   -\ell\,\nu\|\nabla u\|_2^2\Bigr]dt,\quad
>  (m,n,\ell)=(\partial_1G,\partial_2G,\partial_3G),
> \]
> and it does **not** obey consequence 2: \(G=\mathcal Q\,\phi(E)\) has
> \(m=\phi(E)\), which is not a function of \((\mathcal Q,t)\) alone, while
> \(n\equiv0\), so the pressure flux is not activated. What the enlarged family
> costs instead is \(\nu\int_0^\tau|\ell|\,\|\nabla u\|_2^2\,dt\) with
> \(\ell=\mathcal Q\phi'(E)\), i.e. \(\sup_t\mathcal Q\) times the audited
> \(\int\|\nabla u\|_2^2\le E_0/2\nu\) — the conclusion. **So the energy variable
> is available and is negative, not absent.** The claim retired here is therefore
> the narrower and true one: *within the two-functional family, weighting can
> localise absorption but never improve it, and a weight depending on \(F\)
> necessarily activates \(P_3\).*
>
> Correspondingly, Proposition 3.4 is the member \(G(\mathcal Q,F,t)=\rho(t)\mathcal Q\)
> of that same family, with \(m=\rho\), \(n\equiv0\), \(\partial_tG=\rho'\mathcal Q\):
> it obeys consequences 1 and 2 and escapes **only** consequence 3, because
> \(m=\rho(t)\) is not of the form \(m(\mathcal Q)\) supported in a Kato region.
> Its cost \(\Lambda\int_0^\tau\mathcal Q\,dt\) is input-bounded by (E6), and that
> is the one genuinely new degree of freedom this lane found.

*Proof.* The identity for the enlarged family is the chain rule for absolutely
continuous compositions, exactly as in the note's proof of Theorem 3.2, with the
third component supplied by `prop:energy` Step 1 (\(E\) differentiable,
\(E'=-\nu\|\nabla u\|_2^2\), \(\|\nabla u\|_2^2\in L^1(0,\tau)\) by (E4)). The
counterexample to consequence 2 is the displayed \(G=\mathcal Q\phi(E)\). The
identification of Proposition 3.4 as \(G=\rho(t)\mathcal Q\) is immediate:
substituting into (3.3) reproduces (3.5) term by term. \(\square\)

**R-D (replaces the closing paragraph of Corollary 3.5 and NEXT DISTINCT
ACTION item 1).** State Lemma R1 of E5(b) verbatim, then:

> (H-mod) is therefore implied by \(T_*>H\), hence by `def:target`; it is not
> circular (it does not imply the conclusion by any displayed step), but it is
> of the existential-equivalence type: its whole content lies in the branch
> \(T_*\le H\), and it cannot be refuted by any construction that is not itself
> a finite-time blow-up. The audited record fails to supply it not because its
> only modulus has a trajectory-dependent constant — \(\Lambda\) is permitted to
> depend on \((\nu,u_0,H)\) — but because HF21-B Remark 2.2's constant contains
> \(\sup_{t<\tau}\|\partial_tu\|_3\) and \(\sup_{t<\tau}\|w\|_3\), neither of
> which is bounded **uniformly in \(\tau<T_*\)**. The open question is the
> \(\tau\)-uniform lower bound on the crossing time of the level
> \(\nu/C_\sharp\), not trajectory independence.

---

## CONDITIONAL SUFFIX THAT SURVIVES

With R-A–R-D applied, the following survive unchanged and may be quoted by the
controller:

1. **Lemma 1.1, Lemma 1.2, Proposition 1.3, Corollary 1.4** (with the constant
   correction B6.1) — the pressure-route mirror of the product statement, its
   unconditional identities, the velocity-dissipation coercivity
   \(D_3(u)\ge\frac4{5S^2}\|u\|_9^3\), and the size bound
   \(|P_3|\le C_{\rm pr}\|u\|_3D_3(u)\).
2. **Proposition 1.5, Remarks 1.6–1.7** (with B6.2) — the two-route comparison;
   \((\mathrm G_P)\Rightarrow(\mathrm G)\) iff HF21-B sub-question (a); the
   pressure route is not easier; the \(\|p\|_3\) chain is lossy by exactly the
   stated amount.
3. **Proposition 1.8** — (G), \((\mathrm G_P)\), `hyp:highstrain`,
   `hyp:absorption`, `hyp:highpressure` and \(T_*=\infty\) are equivalent at
   their quantifiers.
4. **Propositions 2.1, 2.3, 2.4 and Corollary 2.2**, with R-B replacing the
   endpoint sentence — the input hull is one segment of \(\lambda=\frac32\), the
   deficit is exactly \(\frac12\) and uniform, the ninth-power space is critical
   but conditional, and the Hölder split overshoots by exactly \(\frac2{3s}\)
   for finite \(s\) and lands exactly on criticality at \(s=\infty\).
5. **Lemma 3.1** — \(K=-\int(T(w)-T(u)):S(u)\), with \(|T(w)-T(u)|\le3(|w|+|u|)^2|q|\).
6. **Theorem 3.2 identity (3.2)–(3.3) and consequences 1–3**, restricted to the
   family \(G(\mathcal Q,F,t)\) (R-C), with B6.3.
7. **Corollary 3.3** — the exact residual of a distance cutoff, with threshold
   \(y_0\le(1-\varepsilon)^3\nu^3/(12C_\sharp^3)\).
8. **Proposition 3.4 and Corollary 3.5** — the time-weighted balance, its
   input-bounded cost \(\Lambda\int\mathcal Q\), and: (H-mod)
   \(\Rightarrow\) obstruction O3 settled affirmatively
   \(\Rightarrow\) (G) reduces to \(\int_{(\mathcal G^{2\varepsilon}_\tau)^c}d_1D_3(w)\,dt\le A_{\rm input}\).
9. **Remark 3.6** (with the \(2(N_\tau+1)\) and BV corrections) — the exact price
   of the crossing mechanism.
10. **New, from this audit: Lemma R1** — \(T_*>H\Rightarrow\) (H-mod); hence
    \((\mathrm G)\Rightarrow(\mathrm{H\text{-}mod})\) and (H-mod) is not
    falsifiable by construction.
11. **New, from this audit: the enlarged family \(G(\mathcal Q,F,E,t)\) is
    available and is negative** — it evades consequence 2 but pays
    \(\sup_t\mathcal Q\cdot E_0/2\nu\), the conclusion. This closes off the
    obvious first attempt to exploit the gap in the exhaustion claim.

The note's items (ii)–(iv) of its own SURVIVING CONDITIONAL SUFFIX (HF21-B
sub-question (a); \((\mathrm G_P)\Rightarrow\)`hyp:absorption`; the small-\(d_1\)
criterion) all check and survive.

---

## UNNECESSARY DEPENDENCIES

- **Lemma 3.1 is used by nothing.** The note says so; the controller should
  treat §3.1 as motivational and not carry HF18-B Prop. 3.1 into any dependency
  edge. With R-A, HF18-B (3.6) is no longer cited even rhetorically.
- **Corollary 1.4 and Remark 1.6 are used by nothing**; keep them as consistency
  checks, not as premises.
- The note's premise list names `lem:gradient-closure`, `lem:quotient-minimizer`,
  `lem:heat-generator`, `lem:quotient-transport`, `lem:quotient-scaling`,
  `lem:cubic-pointwise`, `lem:cubic-frechet`, `prop:quotient-derivative`,
  `lem:quotient-heat`, `def:quotient`. None of these appears in any displayed
  step; they enter only through the audited (E1)–(E8). The dependency edge
  should be to (E1)–(E8), not to the individual lemmas.
- `hf21-shifted-hodge-regularity.md` and the HF19 notes are correctly listed as
  read-not-premises; I confirmed no HF19 content is used.
- \eqref{eq:L4L3} enters twice, both times through (E5)/(E6); the direct
  citation in Remark 1.6 is the only other use and is not load-bearing.

---

## NON-CLAIMS (of this audit)

This audit proves nothing about (G), \((\mathrm G_P)\), `hyp:highstrain`,
`hyp:highpressure`, `hyp:absorption`, `hyp:critical`, or NS-R3, and does not
close, weaken or strengthen the first gap. It supplies no bound on
\(\sup_t\|u\|_3\), on \(\int D_3(w)\,dt\), on \(\int D_3(u)\,dt\), on \(N_\tau\),
or on any modulus of continuity for \(d_1\). It does not decide HF21-B
sub-question (a) (\(D_3(w)\le D_3(u)\)) in either direction, and does not decide
(H-mod). Lemma R1 is *not* progress on (H-mod): it shows (H-mod) is implied by
the conclusion, which is a scope fact and a warning about falsifiability, not an
estimate. The swirl family of E2 refutes only the stated pointwise equivalence
between \(\sup d_1\) and \(\sup\|u\|_3\); it is a static field, not a solution,
and says nothing about trajectories. The counterexample of E3 refutes only the
exhaustion claim, not Theorem 3.2's identity or its consequences within the
two-functional family. The factor \(9\) in B6.1 is an upper bound, not a sharp
constant. No numerics were computed and none would have been evidence. No file
other than this one was written; nothing was committed or pushed; the manuscript
is untouched.

---

## REOPENING CONDITION

This verdict should be reopened if any of the following is produced:

1. **A field \(u\in L^3\cap H^m\), solenoidal, with \(K(u)=0\) and
   \(d_1(u)D_3(w(u))>0\)** — this would restore the *pointwise* half of B1 (it
   still would not restore the time-integrated strictness claim, which
   Proposition 1.8 forbids at the stated quantifiers).
2. **A per-trajectory implication \(\sup_{t<\tau}d_1<\infty\Rightarrow\sup_{t<\tau}\|u\|_3<\infty\)
   for the classical branch** — this would restore B2's endpoint sentence. It
   would have to use the evolution; the static implication is refuted in E2.
3. **An audited enumeration theorem** that pins down the class of functionals
   with exact balances at the audited level, together with a proof that the
   energy and the \(H^k\) norms cannot enter any useful weighted balance — this
   would restore a (correctly quantified) version of B3's closure claim. Absent
   such a theorem, "closure of the mechanism class" must not be asserted.
4. **A \(\tau\)-uniform lower bound on the crossing time of the level
   \(\nu/C_\sharp\) by \(C_\sharp d_1\)** depending only on \((\nu,u_0,H)\) —
   this proves (H-mod) and, by Corollary 3.5 (which survives), settles O3 and
   reduces (G) to its bad-set part. This is the one item on which the lane's
   conditional suffix actually turns.
5. **A resolution of HF21-B sub-question (a)** in either direction, which
   changes Proposition 1.5(3) from conditional to decided.

---

## EXACT EDITS THE CONTROLLER SHOULD MAKE IF THIS VERDICT STANDS

All edits are to `research/evidence/hf22-direct-attack.md` (the audited note);
none to the manuscript, and none to any other evidence file. The note's status
becomes **AUDITED, REPAIR (repairs applied)** once E1–E8 below are made.

- **E-1 (§1.4, first bullet).** Replace the bullet, from "**(G) is strictly
  stronger…**" to "…proves more than the gap needs.", by block **R-A** above.
  Change the bullet heading to "**The converse of (G) ⟹ `hyp:highstrain` is not
  derivable per trajectory (non-derivability, not strictness).**"
- **E-2 (§3.4, Remark 3.7).** Replace "The reverse … is **false**:" by "The
  reverse … is **not available**:" and delete the clause "so \(K\) vanishes on a
  nontrivial set of strain configurations at fixed \(d_1D_3(w)>0\)", replacing
  it by "and no field with \(K=0<d_1D_3(w)\) is exhibited in the audited
  record". Delete the sentence "This is why (G) is strictly stronger per
  trajectory than the frozen gap (§1.4)".
- **E-3 (§2, Proposition 2.4).** Replace the sentence beginning "and \(\to0\)
  only as \(s\to\infty\), where the hypothesis degenerates…" through
  "(`hyp:critical`)." by block **R-B**. Update the §2 summary's last sentence to
  say the family is blocked at every member, strictly subcritically for finite
  \(s\) and exactly critically at \(s=\infty\).
- **E-4 (§3.2).** Replace the preamble paragraph ("By `lem:quotient-chainrule`
  and `prop:pressure`, exactly two scalar functionals…") and the "**Reading.**"
  paragraph by block **R-C**. Retitle Theorem 3.2 to "**Theorem 3.2 (closure of
  the two-functional family, and the weight invariant)**". Add \(m\le1\) to the
  hypothesis of consequence 3.
- **E-5 (§3.4 opening and Corollary 3.5).** Delete "escapes Theorem 3.2(2) — it
  is not of the form \(G(\mathcal Q,F)\)" and replace by "is the member
  \(G=\rho(t)\mathcal Q\) of the family of Theorem 3.2; it satisfies
  consequences 1 and 2 and escapes only consequence 3". Insert **Lemma R1** and
  block **R-D** after the (H-mod) display.
- **E-6 (§3.4, Remark 3.6).** Add "(assuming \(N_\tau<\infty\), without which
  \(\mathbf 1_{\mathcal G_\tau}\) is not of bounded variation)" and change
  \(2N_\tau\sup\mathcal Q\) to \(2(N_\tau+1)\sup\mathcal Q\) at both occurrences.
- **E-7 (constants).** In §0, redefine \(C_{\rm CZ}(r)\) as the operator norm of
  \(\mathsf F\mapsto\sum_{i,j}R_iR_j\mathsf F_{ij}\) on
  \(L^r(\mathbb R^3;\mathbb R^{3\times3})\); or, keeping the single-pair
  definition, insert the factor \(9\) in Lemma 1.1's last display and in
  \(C_{\rm pr}\) (§1.2 (1.4), the CLAIM AND SCOPE block, and the
  \((\mathrm G_P)\Rightarrow\)`hyp:absorption` constant in the conditional
  suffix (iii)). In Proposition 1.5(2) replace "pointwise the smaller one" by
  "pointwise comparable up to \(1+C_{\mathbb P}\), and vanishing on
  \(\mathcal M\) where \(\|u\|_3\) does not".
- **E-8 (frontier record).** In MODE/RESULT: rewrite item 3 to say "closure of
  the **two-functional** integration-by-parts family, with its weight invariant
  and the forced pressure coupling **inside that family**", and rewrite item 4's
  "escape (i)–(iii)" to "escape (iii)". In CLAIM AND SCOPE, replace "Theorem 3.2
  with consequences 1–3 (closure, …)" accordingly. In **NON-CLAIMS**, replace
  "Theorem 3.2 retires a *mechanism class*…" by "Theorem 3.2 characterises the
  two-functional family only; the audited record supplies at least one further
  exactly-differentiable functional (the energy), and the enlarged family is
  shown to be negative rather than absent". In **NEXT DISTINCT ACTION**, delete
  "Both are falsifiable by construction" and replace by "Sub-question (a) is
  falsifiable by construction (a fixed-time statement about a single field);
  (H-mod) is **not**, being implied by \(T_*>H\) (Lemma R1), so it can only be
  attacked, not refuted." Restate item 1 as the \(\tau\)-uniform crossing-time
  question of R-D(3).
- **E-9 (PLAN.md, controller's file, one line).** Under "Ordered next actions",
  record that HF22-D is AUDITED/REPAIR, that the frozen gap is unchanged, that
  (H-mod) is a new *conditional* sub-question of the existential-equivalence
  type (not falsifiable by construction), and that HF21-B sub-question (a)
  remains the only falsifiable-by-construction continuation this lane produced.
