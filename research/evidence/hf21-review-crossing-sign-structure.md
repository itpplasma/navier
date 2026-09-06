# Independent audit of HF21-B: distance to the nonlinear-Hodge class and the sign structure of the time-integrated transport term

**VERDICT: REPAIR.**

Frozen candidate: `research/evidence/hf21-crossing-sign-structure.md`,
SHA-256 `f8bb9ab5d31551abd96ae99d4cdc1d9d9abee17f75bf14da035c2949869944a9`.
Base commit `1c0f68ec34d4987d5345bf048d4c628fc16a8816`.
Mode: REVIEW, proof-audit discipline. Manuscript read at
`../navier-paper/main.tex` in the same working tree.
Audited background used as premises and not re-proved: HF17 (both PASS),
HF18-A (`hf18-review-hodge-regularity.md`, PASS), HF18-B
(`hf18-review-divergence-speed-link-r2.md`, PASS with S1–S4), HF20
(`hf20-review-harmonic-strain-test.md`, REPAIR applied). The three HF19 notes
were not used, matching the candidate's own discipline.
All constants, exponents and scaling weights below were recomputed
independently; two small numerical experiments of my own are reported and are
bounded evidence only.

Every displayed result of §§1, 2, 3.1, 4.1–4.3, 4.5, 4.6 recomputes and
survives. Three defects are found, two of them errors and one a novelty
misattribution that changes what the controller should integrate:

- **B1 (first bad bridge, §3.2 prose box).** The first-order expansion of
  `K(U+\varepsilon h)` at a point of `\mathcal M` omits a term of order
  `\varepsilon`, and the conditional it supports —
  *"an `\alpha>1` bound is compatible with the audited record only if the
  nonlinear projection is Lipschitz"* — is **logically inverted**. Lipschitz
  continuity of `q` at `\mathcal M` is exactly what would *refute* `\alpha>1`;
  an `\alpha>1` bound *forces* the projection to be non-Lipschitz. The
  candidate's own record item **(iv)** states the correct direction, so the
  note is internally inconsistent. Replacement lemmas R1, R2 below.
- **B2 (§4.4, Theorem 4.5 item 3, second display).** The claim
  `\nu\int_{\mathcal G_\tau}D_3(w)\,dt\le\mathcal Q(0)+C_\sharp\int_{\mathcal B_\tau}d_1D_3(w)\,dt`
  does not follow from the stated proof and is not derivable from the
  ingredients: on the good set the deficit `\nu D_3(w)-K` may be arbitrarily
  small relative to `\nu D_3(w)`. The good-set index must be `\mathcal B_\tau`
  (in which case the statement is vacuous) or the good set must be thickened
  to `C_\sharp d_1\le(1-\delta)\nu`. Replacement lemma R3 below.
- **B3 (§4.3, Proposition 4.3 / result (R3)).** Correct, but **not new**: it is
  `prop:scaling`(iii) `\eqref{eq:L4L3}` of the manuscript plus one time-Hölder
  step, with the same `E_0,\nu,\tau` weights and a slightly worse constant. The
  candidate does not cite `prop:scaling` anywhere. Consequences are favourable,
  not adverse: Corollary 4.4 needs **no new lemma at all**, and Theorem 4.5(1)
  can be **upgraded to a `\tau`-uniform bound**, `|\mathcal B_\tau|\le
  24C_S^2C_\sharp^4E_0^2\nu^{-5}`, which is strictly stronger than the
  candidate's `\tau^{1/4}`-growing bound and is the form the controller should
  record. Replacement lemma R4 below.

None of B1–B3 touches Theorem 4.1, Corollary 4.2, Corollary 4.4, Theorem
4.5(1)(2)(3-first-display), O1 or O2. In particular the two items the audit
brief singles out as manuscript-changing — Corollary 4.2 (route dictionary) and
Corollary 4.4 (removability of `M` and of the cutoff `L`) — are **correct as
stated**, and Corollary 4.4 becomes cheaper after B3.

---

## REVIEWED SCOPE

§0 (transcription of audited inputs (Q1)–(Q7), (P1)–(P3), the `D_3(u)` vs
`D_3(w)` warning, the scaling conventions); §1.1–§1.4 (Lemma 1.1,
Propositions 1.2, 1.3, 1.4, the scaling table and its consequence); §2
(Proposition 2.1, Remarks 2.2 and 2.3 including the independent derivation
through `K=-\langle j(w)-j(u),(u\cdot\nabla)u\rangle`); §3.1–§3.3
(Proposition 3.1 with `C_\sharp`, Proposition 3.2 lattice, the `\alpha>1`
paragraph, Proposition 3.3); §4.1–§4.6 (Theorem 4.1, Corollary 4.2,
Proposition 4.3, Corollary 4.4, Theorem 4.5, O1, O2 with Proposition 4.6, the
gauge discussion); §5 self-check table; §6 frontier record.

Manuscript statements re-read in full for this audit and verified as cited:
`lem:cubic-pointwise` (`eq:cp-lipschitz`, `eq:cp-taylor`, `eq:cp-monotone`),
`lem:cubic-frechet` (`eq:cp-F-taylor`, `eq:cp-F-lipschitz`,
`eq:cp-F-monotone`), `lem:density`, `lem:quotient-minimizer`,
`lem:gradient-closure`, `lem:leray`(a)–(d) with Steps 1–4 of (d),
`lem:quotient-coercive`, `lem:quotient-scaling`, `lem:quotient-stability`,
`prop:quotient-derivative`, `def:qe-dissipation`, `lem:quotient-transport`,
`prop:quotient-evolution`, `lem:quotient-lowstrain`, `hyp:highstrain`,
`prop:quotient-conditional`, `rem:highstrain-scope`, `rem:no-monotone`,
`def:D3P3`, `prop:pressure`, `prop:energy`, `prop:scaling`,
`hyp:highpressure`, `hyp:absorption`, `lem:absorption-split`,
`cor:absorption-consequence`, `hyp:critical`.

---

## 1. What was checked and confirmed

### 1.1 The distance comparison lattice (audit item 1) — CONFIRMED

**Proposition 1.2.** The Bregman representation `d_2=\int B(w,-q)` is correct:
`F(u)=F(w)+\langle j(w),-q\rangle+\int B(w,-q)` with
`\langle A,q\rangle=0` by `lem:quotient-minimizer`(c), all three pieces finite.
The two pointwise lower bounds recompute. With
`(j(a+\theta d)-j(a))\cdot(\theta d)=\frac{|a+\theta d|+|a|}{2}(\theta^2|d|^2+(|a+\theta d|-|a|)^2)`
— the identity `eq:cp-monotone`, which I verified symbolically
(`(x+y)(x^2+y^2-xy)=x^3+y^3`) and numerically to machine precision — one gets
`\ge\frac12\theta^3|d|^3` from `|a+\theta d|+|a|\ge\theta|d|` and
`\ge\frac12|a|\theta^2|d|^2`; dividing by `\theta` and using
`\int_0^1\theta^2=\frac13`, `\int_0^1\theta=\frac12` gives
`B\ge\frac16|d|^3` and `B\ge\frac14|a||d|^2`. The upper bound is
`eq:cp-taylor`. Hence
`\max\{\tfrac16\|q\|_3^3,\tfrac14\int|w||q|^2\}\le d_2\le(\|w\|_3+\|q\|_3)\|q\|_3^2\le(2+C_{\mathbb P})(3\mathcal Q)^{1/3}d_1^2`,
the last step from `\|q\|_3\le(1+C_{\mathbb P})\|w\|_3=(1+C_{\mathbb P})(3\mathcal Q)^{1/3}`
(`eq:cp-coercive`). All three constants `1/6`, `1/4`, `2+C_{\mathbb P}` are
valid. A `2\times10^5`-sample random test over three amplitude decades gave
`\min B/(|d|^3/6)=1.172`, `\min B/(|a||d|^2/4)=2.000`,
`\min (|a|+|d|)|d|^2/B=1.0001`: the two lower constants are not sharp (`1/4`
can be `1/2`, `1/6` can be about `1/5.1`), the upper one is essentially
attained. Non-sharpness is harmless; nothing downstream uses sharpness.

**Proposition 1.3.** Lower bound: `eq:cp-F-monotone` with `v=w`, `v'=u` gives
`\langle j(w)-j(u),q\rangle\ge\frac12\|q\|_3^3`; `\langle j(w),q\rangle=0`;
`\langle\mathbb Pj(u),q\rangle=\langle j(u),\mathbb Pq\rangle=0` by
`lem:leray`(c) and the duality; Hölder gives `\frac12 d_1^2\le d_4`. Upper
bound: `(I-\mathbb P)A=0` for the solenoidal `A\in L^{3/2}`, then
`eq:cp-F-lipschitz` and `\|u\|_3\le C_{\mathbb P}\|w\|_3`. The chain
`\|u\|_3+\|w\|_3\le2C_{\mathbb P}\|w\|_3` silently uses
`C_{\mathbb P}\ge1`, which is automatic (`\mathbb P^2=\mathbb P`,
`\mathbb P\neq0` on `L^3`). Both consequences `d_1\le2d_4^{1/2}` and the
`d_2` lower bound in `d_4` follow. **Two unstated but repairable steps**, worth
a one-line footnote if this is ever promoted:
(i) the manuscript states `\|\mathbb P\psi\|_{3/2}\le C_{3/2}\|\psi\|_{3/2}`
only for `\psi\in C_c^\infty` (`lem:leray`(b)); the extension of `\mathbb P` to
`L^{3/2}` and the duality
`\langle\mathbb Pf,g\rangle=\langle f,\mathbb Pg\rangle` for
`f\in L^{3/2}`, `g\in L^3` follow by taking `f_n\in C_c^\infty\to f` in
`L^{3/2}`, `g_n\in L^2\cap L^3\to g` in `L^3` and passing to the limit in
`lem:leray`(a); (ii) `(I-\mathbb P)\psi=\nabla\Theta\in\mathcal G_3` for
`\psi\in C_c^\infty` needs `\Theta\in L^3`, which holds because
`\Theta=\check g` with `g\in L^1\cap L^2` gives `\Theta\in L^2\cap L^\infty`,
and then `lem:gradient-closure` applies. Both steps are correct.

**Proposition 1.4 and the non-invariance of `d_3`.** `\operatorname{div}(|u|u)=u\cdot\nabla|u|`
for solenoidal `u`; the algebraic identity
`|u|^{3/2}|\nabla|u||^{3/2}=(|u||\nabla|u||^2)^{3/4}|u|^{3/4}` with Hölder
`(4/3,4)` and `\int|u||\nabla|u||^2\le D_3(u)` gives
`d_3\le D_3(u)^{1/2}\|u\|_3^{1/2}` exactly as claimed. (I confirmed the
candidate's rewriting of `def:D3P3`: `|(\nabla u)^{\mathsf T}u|^2=|u|^2|\nabla|u||^2`
so `V(u,\nabla u)=|u||\nabla|u||^2`, and `(u\otimes u):\nabla u/|u|=u\cdot\nabla|u|`,
so `P_3=\int p\,u\cdot\nabla|u|`. Both rewritings are correct.)

**Scaling table.** Independently recomputed on both parameters:
`d_1\sim(a,\lambda^0)`, `d_2\sim(a^3,\lambda^0)`, `d_4\sim(a^2,\lambda^0)`,
`d_3\sim(a^2,\lambda^1)`, `\int|w||q|^2\sim(a^3,\lambda^0)`,
`\mathcal Q\sim(a^3,\lambda^0)`, `D_3(u),D_3(w)\sim(a^3,\lambda^2)`,
`K,P_3\sim(a^4,\lambda^2)`, `E\sim(a^2,\lambda^{-1})`, `\nu\sim(a,\lambda^0)`,
`dt\sim(a^{-1},\lambda^{-2})`, `2^L\sim(a^0,\lambda)`. In particular
`\operatorname{div}(|u|u)\mapsto\lambda^3(\operatorname{div}(|u|u))(\lambda\cdot)`
and `\|f(\lambda\cdot)\|_{3/2}=\lambda^{-2}\|f\|_{3/2}`, giving
`d_3\sim\lambda`: **the claim that `d_3` is not scale-invariant and cannot
appear alone in a scaling-consistent bound for a critical quantity is
correct**, and `d_3` is indeed never used in such a bound in the note.
Inequalities (1.1), (1.2), (1.3) are each consistent on both parameters.

### 1.2 The exact distance balance (audit item 2) — CONFIRMED, this is the crux and it holds

The two balances are on the **same interval under the same hypotheses** and
may legitimately be subtracted:

- `prop:pressure`(ii) holds for every `0\le s\le t<T_*` for the classical
  branch of `prop:localtheory` with normalised pressure, with `D_3,P_3`
  measurable and bounded on compact subintervals (`prop:pressure`(i)), hence
  integrable on `[s,t]`.
- `prop:quotient-evolution` holds with the package (R) of
  `subsec:qe-trajectories`, i.e. on every compact `[0,T]\subset[0,T_*)`, for
  the same branch, and gives `\mathcal Q\circ u\in C^1([0,T])` with continuous
  `D_{\mathcal Q}` and continuous right side.

Both are therefore available on any `[s,t]\subset[0,T_*)`; the **integrated
forms** are exactly what the manuscript proves (`eq:pressure-balance` is
integrated by statement, `eq:quotient-evolution` is a `C^1` identity whose
integrated form is used verbatim in the proof of
`prop:quotient-conditional`). **Absolute continuity of `d_2` is established,
not assumed**: `F\circ u=\frac13X` is an indefinite integral of the `L^1`
function `P_3-\nu D_3(u)` by `eq:pressure-balance`, hence absolutely continuous
on compacts, and `\mathcal Q\circ u\in C^1` is a fortiori absolutely
continuous. Subtracting gives, for `0\le s\le t<T_*`,
```
 d_2(t)-d_2(s)=\int_s^t[P_3-K+\nu(D_3(w)-D_3(u))]d\tau ,
```
with `K=-\int q\cdot((A\cdot\nabla)u)` the manuscript's right side. The sign
conventions match: `prop:quotient-evolution` is `\mathcal Q'+\nu D_{\mathcal Q}=K`
and `eq:pressure-balance` is `\frac13X(t)-\frac13X(s)+\nu\int D_3=\int P_3`.
`D_{\mathcal Q}=D_3(w)` is the audited (Q6) of HF18-A. **Proposition 2.1 is
correct.** No derivative of the minimizer is taken anywhere, and Remark 2.2's
reason for evolving `d_2` rather than `d_1` is right: `eq:cp-strong` gives
only `\|w(t')-w(t)\|_3\le2(\|w(t)\|_3+\|u(t')-u(t)\|_3)^{1/2}\|u(t')-u(t)\|_3^{1/2}`,
i.e. Hölder-`1/2` in `t`.

**The independent cross-check of Remark 2.3 verifies.** I re-derived it from
scratch. `\langle j(u),(u\cdot\nabla)u\rangle=\int u\cdot\nabla(|u|^3/3)=0` for
solenoidal `u\in H^m` (integration by parts, `\operatorname{div}u=0`), and
`lem:quotient-transport` gives `K=-\langle A,(u\cdot\nabla)u\rangle`; hence
`K=-\langle j(w)-j(u),(u\cdot\nabla)u\rangle`. Inserting
`(u\cdot\nabla)u=\nu\Delta u-\nabla p-\partial_tu` and using
`\langle A,\nabla p\rangle=0` (`lem:quotient-pressure`),
`-\langle j(u),\nabla p\rangle=\int p\operatorname{div}(|u|u)=P_3`,
`\langle A,\Delta u\rangle=-D_{\mathcal Q}`, `\langle j(u),\Delta u\rangle=-D_3(u)`,
`\langle j(w)-j(u),\partial_tu\rangle=\mathcal Q'-F'=-d_2'` returns
`d_2'=P_3-K+\nu(D_3(w)-D_3(u))`. Identical. The note is right that this route
needs the instantaneous identification `\langle j(u),\Delta u\rangle=-D_3(u)`
at velocity zeros, which the integrated route avoids; it correctly uses the
integrated route as primary and this as a check only.

**Theorem 4.1 and (4.2) follow immediately and are correct**, including
`d_2(0)\le F(u_0)=\frac13\|u_0\|_3^3` and the term-by-term `(a^3,\lambda^0)`
scaling. The two signed terms `-d_2(\tau)\le0` and `-\nu\int D_3(u)\le0` are
genuinely signed, and the note's own honest reading — that the remainder is
exactly the pressure-route flux and supplies no new sign — is the correct
disposition.

### 1.3 The refined bound `|K|\le C_\sharp\|q\|_3D_3(w)` (audit item 3) — CONFIRMED

It **is** genuinely a line of the audited HF18-A Theorem 4 proof. That proof
reads, verbatim,
`|K|\le\frac43\|q\|_3\||u||w|^{1/2}\|_6\|\nabla V\|_2` and then
`\||u||w|^{1/2}\|_6\le C_9S\|\nabla V\|_2`, and only afterwards substitutes
`\|q\|_3\le(1+C_3)\|w\|_3`. The candidate's (3.1) is exactly the line before
that substitution. `hf18-review-hodge-regularity.md` R8 verified this chain
"including every constant".

Recomputed independently: `|\nabla A|\le\frac43|V|^{1/3}|\nabla V|` (operator
norm of `|V|^{1/3}(I+\frac13\hat V\otimes\hat V)` is `\frac43|V|^{1/3}`) with
`|V|^{1/3}=|w|^{1/2}`; Hölder `(3,6,2)` with `\frac13+\frac16+\frac12=1`;
`\||u||w|^{1/2}\|_6^6=\int|u|^6|w|^3\le\|u\|_9^6\|w\|_9^3` by Hölder `(3/2,3)`;
`\|u\|_9\le C_9\|w\|_9`; `\|w\|_9^{3/2}=\|V\|_6\le S\|\nabla V\|_2`;
`\|\nabla V\|_2^2\le\frac98D_3(w)`. Hence
`|K|\le\frac43C_9S\|q\|_3\|\nabla V\|_2^2\le\frac43\cdot\frac98C_9S\,d_1D_3(w)=\frac32C_9S\,d_1D_3(w)`.
`C_\sharp=\frac32C_9S`. ✓

**Substituting the audited `\|q\|_3\le(1+C_3)(3\mathcal Q)^{1/3}` reproduces
`C_*` exactly**: `\frac32C_9S\cdot(1+C_3)3^{1/3}=\frac32 3^{1/3}(1+C_3)C_9S=C_*`. ✓
Scaling: `d_1D_3\sim(a^4,\lambda^2)=K`. ✓

**Proposition 3.2 (the lattice) recomputes.** With
`|K|\le Cd_1^\alpha\mathcal Q^bD_3(w)^cE^e2^{Ld}`, amplitude gives
`\alpha+3b+3c+2e=4` and dilation gives `2c-e+d=2`; with `e=d=0`, `c=1` and
`\alpha+3b=1`, so `\alpha=0,b=1/3` is the audited endpoint and `\alpha=1,b=0`
is (3.1), and `\alpha>1` forces `b<0`. ✓ Both equations and the endpoint claim
are correct. The interpolated members `0\le\alpha\le1` exist: geometric
interpolation of `|K|\le C_*\mathcal Q^{1/3}D_3` with (3.1) gives
`|K|\le C_*^{1-\alpha}C_\sharp^\alpha d_1^\alpha\mathcal Q^{(1-\alpha)/3}D_3`.

**Proposition 3.3** is correct and correctly scoped: `\mathcal Q'\le-(1-\theta)\nu D_3(w)\le0`,
`\sup\|u\|_3^3\le3C_{\mathbb P}^3\mathcal Q(u_0)\le C_{\mathbb P}^3\|u_0\|_3^3`,
`thm:continuation` (ESS) then gives `T_*=\infty`; and `D_3(w)\ge\frac{8}{9S^2C_9^3}\|u\|_9^3`
(audited, `hf18-review-hodge-regularity.md` line 370) gives `u\in L^3_tL^9_x`.
The hypothesis is not input-only and the note says so in the strongest terms.
The observation that `\mathcal M_{\rm sol}` contains fields of arbitrarily large
critical norm, so that the hypothesis class strictly contains the
critical-smallness class, is supported by (Q7) Prop. 1.4 of the audited HF18-B.

### 1.4 The input-only spacetime bound (audit item 4) — CORRECT, but see B3

`\|u\|_3\le\|u\|_2^{1/2}\|u\|_6^{1/2}` (interpolation exponent `\theta=1/2`
from `\frac13=\frac{\theta}2+\frac{1-\theta}6`), `\|u\|_6\le S\|\nabla u\|_2`,
`\|u\|_2^2\le E_0`, so `\|u\|_3^3\le E_0^{3/4}S^{3/2}\|\nabla u\|_2^{3/2}`;
time-Hölder `(4,4/3)` and `\int_0^{T_*}\|\nabla u\|_2^2\le E_0/(2\nu)`
(`prop:energy`) give
`\int_0^\tau\|\nabla u\|_2^{3/2}\le\tau^{1/4}(E_0/2\nu)^{3/4}`, hence
`\int_0^\tau\|u\|_3^3dt\le2^{-3/4}S^{3/2}E_0^{3/2}\nu^{-3/4}\tau^{1/4}`. ✓
Every exponent checks; scaling `(a^2,\lambda^{-2})` on both sides checks.
`\|q\|_3\le\|w\|_3+\|u\|_3\le2\|u\|_3` gives `\int d_1^3\le8\int\|u\|_3^3`. ✓
"Strictly below the Serrin line" is correct: the pair `(s,r)=(3,3)` has
`2/s+3/r=\frac23+1=\frac53>1`, so no `\sup_t\|u\|_3` is implied. ✓
See **B3** for what is wrong with the *novelty* of this proposition.

### 1.5 The crossing/measure theorem (audit item 5) — CONFIRMED for items 1 and 2

Chebyshev: on `\mathcal B_\tau`, `d_1>\nu/C_\sharp`, so
`|\mathcal B_\tau|(\nu/C_\sharp)^3\le\int_{\mathcal B_\tau}d_1^3\le\int_0^\tau d_1^3`,
hence `|\mathcal B_\tau|\le(C_\sharp/\nu)^3\int_0^\tau d_1^3dt\le
8\cdot2^{-3/4}S^{3/2}C_\sharp^3E_0^{3/2}\nu^{-15/4}\tau^{1/4}`. The power of
`\nu` is `-3-\frac34=-\frac{15}4`. ✓ Openness of `\mathcal B_\tau` follows from
continuity of `t\mapsto\|q(t)\|_3` (`lem:quotient-stability` plus
`u\in C([0,T];L^3)`). ✓ Item 2 is (Q5) with (3.1). ✓
Item 3, first display, is correct:
`\mathcal Q(\tau)-\mathcal Q(0)=\int_0^\tau(K-\nu D_3(w))\le\int_{\mathcal B_\tau}(K-\nu D_3(w))\le C_\sharp\int_{\mathcal B_\tau}d_1D_3(w)`,
dropping the nonpositive good-set integrand. Item 3, second display: **see B2**.

### 1.6 The route-level dictionary (audit item 6) — CONFIRMED

`hyp:absorption` gives `\int_0^\tau P_3\le\theta'\nu\int_0^\tau D_3(u)+A` with
`\theta'\in[0,1)`, `A=A(\nu,u_0,H)` finite, uniformly for `\tau<\min\{H,T_*\}`.
Inserting into (4.2):
```
 \int_0^\tau K\le d_2(0)+\nu\int_0^\tau D_3(w)-(1-\theta')\nu\int_0^\tau D_3(u)+A
 \le\nu\int_0^\tau D_{\mathcal Q}+A+\tfrac13\|u_0\|_3^3 ,
```
using `D_3(u)\ge0` and `\theta'\le1`. ✓ So the gap holds with `\theta=1`,
`M=0`, `A_{\rm input}=A+\frac13\|u_0\|_3^3`. For `K_L`: `\int K_L=\int K-\int K_{\rm low}`
and `|\int K_{\rm low}|\le M_L\int\mathcal Q` is input-bounded (Corollary 4.4),
so `hyp:highstrain` holds with `\theta=1` and any `L`. ✓ `\theta=1` is
permitted by `hyp:highstrain` and `prop:quotient-conditional` explicitly
("Because `\theta=1` is permitted"). ✓ No circularity: nothing in the
derivation assumes a continuation bound.

**Scope correction the controller must apply if this is integrated.** The
*implication* `hyp:absorption\Rightarrow hyp:highstrain` is already available
in the manuscript by composition:
`cor:absorption-consequence`(ii) gives `hyp:critical`,
`thm:conditional` gives `T_*=\infty`, and the converse direction of
`rem:highstrain-scope` (take `L=0`, `\theta=0`,
`A_{\rm input}=\int_0^H|K_0|`) then gives `hyp:highstrain`. What Corollary 4.2
adds is only the **direct, explicit and quantitative transfer**
`A_{\rm input}=A+\frac13\|u_0\|_3^3` that does not route through the Clay
conclusion. The candidate says as much ("route-level fact, not progress"), but
its abstract wording "asserts one open hypothesis implies another" would
mislead a reader into thinking the implication itself is new. Present it as a
dictionary with an explicit constant, never as a new implication.

### 1.7 Removability of `M` and of the cutoff `L` (audit item 7) — CONFIRMED

This is the item requiring the strictest scrutiny and it holds.

`\mathcal Q\le F=\frac13\|u\|_3^3` (`lem:quotient-coercive`), so for
`\tau<\min\{H,T_*\}`
```
 M\int_0^\tau\mathcal Q\,dt\le\tfrac M3\int_0^\tau\|u\|_3^3dt
 \le\tfrac M3\,2^{-3/4}S^{3/2}E_0^{3/2}\nu^{-3/4}H^{1/4} ,
```
input-only in `(\nu,u_0,H)`; and `|K_{\rm low}|\le M_L\mathcal Q` with
`M_L=3(1+C_{\mathbb P})C_B2^{5L/2}\|u_0\|_2` (`eq:qe-lowstrain`) gives the same
for `|\int_0^\tau K_{\rm low}|` with `M` replaced by `M_L`, which is input-only
in `(\nu,u_0,H,L)` — exactly the dependence `hyp:highstrain` permits.
Both directions of both equivalences then follow by adding or subtracting a
constant, and the fixed universal `\theta` is preserved in both directions.
For the `L`-equivalence: from `hyp:highstrain` with its `L`, the full-`K`
statement holds with `A'=A_{\rm input}+\frac{M_L}3(\cdot)`; conversely from
the full-`K` statement, take `L=0` and `A'=A+\frac{M_0}3(\cdot)`. ✓
**Corollary 4.4 is correct.** It is a statement simplification of
`hyp:highstrain`, not a weakening, and it is the note's most consequential
output. After **B3** it costs nothing: `prop:scaling`(iii) `\eqref{eq:L4L3}`
already sits in the manuscript and supplies the required input bound directly.

### 1.8 Obstructions O1 and O2 (audit item 8)

**O2 is sound.** Proposition 4.6's construction verifies:
`R=\max\{2\theta\nu,(A_1/\tau)^{1/3}\}` gives `R>\theta\nu` (also when
`\theta=0`, since then `R=(A_1/\tau)^{1/3}>0`) and `A_1R^{-3}\le\tau`;
`c=R\mathbf1_{\mathcal E}`, `D=N\mathbf1_{\mathcal E}`,
`|\mathcal E|=A_1R^{-3}` give `\int c^3=A_1`,
`\int cD-\theta\nu\int D=NA_1R^{-3}(R-\theta\nu)\to\infty`. ✓ The computed
instance is right. The scope statement is the correct one: this refutes the
implication `(\text{F-a})+(\text{F-b})\Rightarrow`~gap at the level of the two
abstract functions, not the gap itself. The `M\int\mathcal Q` term of the gap
is absorbable into `A` by Corollary 4.4, so its omission from Proposition 4.6
is legitimate. O2 also survives the strengthening of (F-b) to `L^4` supplied by
**B3/R4**: repeating the construction with `R=\max\{2\theta\nu,(A_1/\tau)^{1/4}\}`
and `|\mathcal E|=A_1R^{-4}` gives `\int c^4=A_1` and the same divergence
(checked numerically: `\tau=\nu=\theta=1`, `A_1=8`, `R=2`, `|\mathcal E|=0.5`,
`\int cD-\int D=N/2\to\infty`).

**O1 is sound in substance, with two defects of statement.**
The Hölder exponents are right: `d_1^\alpha\in L^{3/\alpha}` pairs with
`r=\frac3{3-\alpha}>1` for `\alpha\in(0,3)`; and any uniform bound on
`\int_0^\tau D_3(w)^rdt` with `r>1` yields, via
`D_3(w)\ge\frac8{9S^2C_9^3}\|u\|_9^3` and time-Hölder,
`\int_0^\tau\|u\|_9^3dt<\infty` uniformly, i.e. `u\in L^3_tL^9_x`, the
Ladyzhenskaya–Prodi–Serrin class `\frac2s+\frac3r=\frac23+\frac13=1`, which
already forces the continuation the gap is meant to produce. The route is
therefore circular. Defects:
- **O1a (constant slip).** The displayed constant is `(\frac{9S^2C_9^3}8)^3`;
  it must be `(\frac{9S^2C_9^3}8)^1`, since
  `\|u\|_9^{3r}\le(\frac{9S^2C_9^3}8)^rD_3(w)^r` and the `1/r`-th root removes
  the exponent. With the exponent `3` the inequality is not established
  (it happens to be true when `\frac{9S^2C_9^3}8\ge1`, which is the expected
  regime, but that is not argued).
- **O1b (omitted factor and an overstatement).** For `\alpha\in(0,1)` the
  lattice member carries `\mathcal Q^{(1-\alpha)/3}` with a *positive* power,
  and the displayed Hölder split silently drops it. Restoring it makes O1
  *stronger*, since `\sup_t\mathcal Q` is precisely what the gap is meant to
  produce; the corrected sentence is "the split additionally requires
  `\sup_{t<\tau}\mathcal Q`, which is the conclusion itself". Separately,
  "a hypothesis strictly stronger than its conclusion" should read
  "a hypothesis at least as strong as its conclusion": what is proved is that
  the hypothesis *implies* the conclusion, not that the implication is strict.
- Also worth stating in the note: the lattice members with `\alpha\in(1,3)`
  invoked in O1 are **not** established anywhere (they need `b<0`), so O1
  covers them only hypothetically. This does not weaken O1's use, which is to
  rule out a proof strategy.

### 1.9 §4.6 (the gauge) — CONFIRMED, correctly gated

`\int|w|^\alpha\sigma\,dx=0` for `\alpha\in[2,5]` is HF18-B Remark 1.3,
unconditional in the audited r2 note. The weighted Cauchy–Schwarz
`|\int\sigma g|\le(\int|w|\sigma^2)^{1/2}(\int|w|^{-1}g^2)^{1/2}\le(\frac12D_3(w))^{1/2}(\int|w|^{-1}g^2)^{1/2}`
is correct, and the subtracted profiles are admissible:
`\int|w|^{-1}|w|^{2\alpha}=\int|w|^{2\alpha-1}<\infty` for `2\alpha-1\in[3,9]`
by `w\in L^3\cap L^9` and interpolation. ✓ The dependence on the OPEN (H1),(H2)
is flagged at every occurrence, and the conclusion — a gauge, not a sign — is
the right one. The observation that time-integrating a fixed-time identity with
no time derivative produces no boundary term, so `d_2` is the only available
corrector, is correct as stated for the audited record.

---

## 2. FIRST BAD BRIDGE

**§3.2, the paragraph "What an `\alpha>1` bound would require, exactly", and the
boxed conditional that closes it.**

The candidate writes, for `U\in\mathcal M_{\rm sol}\cap C_c^\infty`,
`h` smooth solenoidal compactly supported, `u_\varepsilon=U+\varepsilon h`:

> `K(u_\varepsilon)=-\varepsilon\langle j(U),(h\cdot\nabla)U+(U\cdot\nabla)h\rangle+O(\varepsilon^{3/2})+O(\varepsilon\cdot\varepsilon^{1/2})`
> *provided* `\|j(w(u_\varepsilon))-j(U)\|_{3/2}=o(1)` is upgraded to `O(\varepsilon)`.

and concludes

> An `\alpha>1` bound is compatible with the audited record only if the
> nonlinear projection `u\mapsto q(u)` is **Lipschitz in `L^3` at points of
> `\mathcal M`**.

**Both are wrong.**

*(a) The expansion omits a first-order term.* By `lem:quotient-transport`,
`K(v)=-\langle A(v),(v\cdot\nabla)v\rangle` exactly. With `w(U)=U`,
`A(U)=j(U)`, `q(U)=0`, write `A_\varepsilon:=A(u_\varepsilon)`. Then, exactly,
```
 K(u_\varepsilon)=-\langle A_\varepsilon-j(U),(U\cdot\nabla)U\rangle
  -\varepsilon\langle j(U),(h\cdot\nabla)U+(U\cdot\nabla)h\rangle
  -\varepsilon\langle A_\varepsilon-j(U),(h\cdot\nabla)U+(U\cdot\nabla)h\rangle
  -\varepsilon^2\langle A_\varepsilon,(h\cdot\nabla)h\rangle ,
```
using `\langle j(U),(U\cdot\nabla)U\rangle=0`. The **first** term is dropped by
the candidate. Under the very upgrade the candidate assumes
(`\|A_\varepsilon-j(U)\|_{3/2}=O(\varepsilon)`) that term is `O(\varepsilon)`,
i.e. **exactly the same order as the term the candidate keeps**, not
`O(\varepsilon^{3/2})`. It does not vanish identically: writing
`(U\cdot\nabla)U=\mathbb P((U\cdot\nabla)U)+\nabla p_U` and using
`\langle A_\varepsilon,\nabla p_U\rangle=\langle j(U),\nabla p_U\rangle=0`
(Euler–Lagrange, `lem:quotient-minimizer`(c)), the term equals
`-\langle A_\varepsilon-j(U),\mathbb P((U\cdot\nabla)U)\rangle`, whose
first-order coefficient is the first variation of the minimizer paired with the
solenoidal part of the self-transport of `U`. It happens to be higher order in
the `rem:no-monotone` family — there `h` agrees with a harmonic gradient near
`\operatorname{supp}U` and the competitor gradient is supported away from `U`,
which is exactly why `rem:no-monotone` can afford an `O(\varepsilon^{3/2})`
error — but that is a property of that construction, not a general fact. I
verified the consistency of the surviving coefficient with `rem:no-monotone`:
for an azimuthal swirl `U` and `h=\nabla\Phi` near `\operatorname{supp}U` with
`\nabla\Phi=(x,y,-2z)`, one has `\langle j(U),(h\cdot\nabla)U\rangle=\int h\cdot\nabla(|U|^3/3)=0`
and `\langle j(U),(U\cdot\nabla)h\rangle=\int|U|U^{\mathsf T}\!\operatorname{diag}(1,1,-2)U=\|U\|_3^3`,
reproducing `K(U+\varepsilon h)\approx-\varepsilon\|U\|_3^3`. So the candidate's
coefficient is the right one *in that family only*, and the general expansion is
incomplete.

*(b) The conditional is inverted.* Suppose a lattice member
`|K(v)|\le Cd_1(v)^\alpha\mathcal Q(v)^{(1-\alpha)/3}D_3(w(v))` holds with
`\alpha>1` on a family with `|K(u_\varepsilon)|\ge c_0\varepsilon`,
`\mathcal Q(u_\varepsilon)\ge q_0>0` and `D_3(w(u_\varepsilon))\le\bar D<\infty`.
Then `d_1(u_\varepsilon)^\alpha\ge c_0q_0^{(\alpha-1)/3}\varepsilon/(C\bar D)`,
i.e. `d_1(u_\varepsilon)\gtrsim\varepsilon^{1/\alpha}` with `1/\alpha<1`: an
`\alpha>1` bound **forces the projection to be strictly non-Lipschitz** at `U`.
Conversely, Lipschitz continuity `\|q(U+z)\|_3\le C(U)\|z\|_3` together with
`c_0>0` gives `|K|/d_1^\alpha\ge c_0\varepsilon/(C(U)\|h\|_3\varepsilon)^\alpha\to\infty`,
so **no** `\alpha>1` bound exists. The candidate's own record item **(iv)**
("If the nonlinear projection is `L^3`-Lipschitz at points of `\mathcal M`,
then `\alpha=1` in (3.1) is sharp and no member with `\alpha>1` exists") states
this correct direction, and therefore contradicts the boxed sentence in §3.2.

*(c) What the audited record actually gives.* With the audited Hölder-`1/2`
rate alone, `d_1(u_\varepsilon)=O(\varepsilon^{1/2})` and (granting
`|K|\sim\varepsilon`) `|K|/d_1^\alpha\sim\varepsilon^{1-\alpha/2}`, which
diverges only for `\alpha>2`. **The audited record refutes `\alpha>2` on this
family and leaves `\alpha\in(1,2]` open.** The sharpness of `\alpha=1` is
strictly conditional on Lipschitz continuity, as the candidate's item (iv)
already says.

This is a scoping paragraph, not a load-bearing lemma: nothing in §4 uses it,
Proposition 3.2 is unaffected, and the record item (iv) is correct. But it is
the first place in the note where a displayed claim does not follow from its
proof, and it is stated in a box, so it must be replaced before any reader
takes it as a fact about the audited record.

---

## 3. REPLACEMENT ARGUMENT

### R1 (exact expansion at `\mathcal M`; replaces the candidate's display)

**Lemma R1.** Let `U\in\mathcal M_{\rm sol}\cap C_c^\infty(\R^3)^3` be
solenoidal with `\operatorname{div}(|U|U)=0`, let `h\in C_c^\infty(\R^3)^3` be
solenoidal, `u_\varepsilon=U+\varepsilon h`, `A_\varepsilon=A(u_\varepsilon)`,
`p_U` the normalised pressure of `U`. Then `w(U)=U`, `q(U)=0`, `A(U)=j(U)`, and
for every `\varepsilon\in\R`
```
 K(u_\varepsilon)=-\langle A_\varepsilon-j(U),\ \mathbb P\big((U\cdot\nabla)U\big)\rangle
  -\varepsilon\langle j(U),(h\cdot\nabla)U+(U\cdot\nabla)h\rangle
  -\varepsilon\langle A_\varepsilon-j(U),(h\cdot\nabla)U+(U\cdot\nabla)h\rangle
  -\varepsilon^2\langle A_\varepsilon,(h\cdot\nabla)h\rangle .
```
Moreover `\|A_\varepsilon-j(U)\|_{3/2}\le4(\|U\|_3+\varepsilon\|h\|_3)^{3/2}(\varepsilon\|h\|_3)^{1/2}`,
so unconditionally `K(u_\varepsilon)=O(\varepsilon^{1/2})`, and the coefficient
of `\varepsilon` contains the term
`-\langle\frac{d}{d\varepsilon}A_\varepsilon|_{0},\mathbb P((U\cdot\nabla)U)\rangle`
whenever `\varepsilon\mapsto A_\varepsilon` is differentiable at `0` in
`L^{3/2}`.

*Proof.* `q(U)=0` and `w(U)=U` by Lemma 1.1 of the candidate (whose proof is
verified above), so `A(U)=j(U)`. `lem:quotient-transport` gives
`K(v)=-\langle A(v),(v\cdot\nabla)v\rangle` for the fields in question.
Expand `(u_\varepsilon\cdot\nabla)u_\varepsilon=(U\cdot\nabla)U+\varepsilon[(h\cdot\nabla)U+(U\cdot\nabla)h]+\varepsilon^2(h\cdot\nabla)h`,
insert, and add and subtract `j(U)` in the first slot; the term
`-\langle j(U),(U\cdot\nabla)U\rangle` vanishes because
`\langle j(U),(U\cdot\nabla)U\rangle=\int U\cdot\nabla(|U|^3/3)=0` for
solenoidal `U`. In the first bracket replace `(U\cdot\nabla)U` by
`\mathbb P((U\cdot\nabla)U)+\nabla p_U` and drop `\nabla p_U`, using
`\langle A_\varepsilon,\nabla p_U\rangle=0` and `\langle j(U),\nabla p_U\rangle=\langle A(U),\nabla p_U\rangle=0`
(`lem:quotient-minimizer`(c) with `\nabla p_U\in\mathcal G_3` by
`lem:gradient-closure`). The norm bound is `eq:cp-continuity` of
`lem:quotient-stability` with `h\to\varepsilon h`. `\square`

### R2 (correct direction of the Lipschitz dichotomy; replaces the boxed sentence)

**Lemma R2.** Let `(v_\varepsilon)_{0<\varepsilon\le\varepsilon_0}` be
solenoidal fields in `L^3` with
(i) `|K(v_\varepsilon)|\ge c_0\varepsilon`, (ii) `\mathcal Q(v_\varepsilon)\ge q_0>0`,
(iii) `D_3(w(v_\varepsilon))\le\bar D<\infty`, for constants
`c_0,q_0,\bar D>0`. Then:
1. If `|K|\le Cd_1^\alpha\mathcal Q^{(1-\alpha)/3}D_3(w)` holds on this family
   with `\alpha>1`, then
   `d_1(v_\varepsilon)\ge\big(c_0q_0^{(\alpha-1)/3}/(C\bar D)\big)^{1/\alpha}\varepsilon^{1/\alpha}`,
   with `1/\alpha<1`; in particular `q` is **not** Lipschitz along the family.
2. Conversely, if `v_\varepsilon=U+\varepsilon h` and
   `\|q(U+z)\|_3\le C(U)\|z\|_3`, then no bound with `\alpha>1` holds on the
   family, and `\alpha=1` is sharp.
3. Under only the audited rate `d_1(v_\varepsilon)=O(\varepsilon^{1/2})`
   (`eq:cp-strong`), the family refutes `\alpha>2` and leaves
   `\alpha\in(1,2]` undecided.

*Proof.* 1. `\mathcal Q\ge q_0` and `\frac{1-\alpha}3<0` give
`\mathcal Q^{(1-\alpha)/3}\le q_0^{(1-\alpha)/3}`; combine with (i), (iii) and
solve for `d_1^\alpha`. 2. `d_1(v_\varepsilon)\le C(U)\|h\|_3\varepsilon`, so
`|K|/d_1^\alpha\ge c_0\varepsilon(C(U)\|h\|_3\varepsilon)^{-\alpha}\to\infty`
for `\alpha>1`; `\alpha=1` is attained by (3.1). 3.
`|K|/d_1^\alpha\gtrsim\varepsilon^{1-\alpha/2}`. `\square`

The replacement text for §3.2 is therefore: *"Lipschitz continuity of the
nonlinear projection at points of `\mathcal M`, together with a nonvanishing
first-order coefficient, would prove `\alpha=1` sharp; conversely any
`\alpha>1` bound would force the projection to be strictly non-Lipschitz there.
The audited Hölder-`1/2` rate refutes only `\alpha>2` on this family."*

### R3 (repairs Theorem 4.5 item 3, second display)

**Lemma R3.** With the notation of Theorem 4.5, for `\tau<T_*`:
1. `\nu\int_{\mathcal B_\tau}D_3(w)\,dt\le\mathcal Q(0)+C_\sharp\int_{\mathcal B_\tau}d_1D_3(w)\,dt`
   (this is what the candidate's proof yields; it is vacuous, since
   `C_\sharp d_1>\nu` on `\mathcal B_\tau`);
2. `\int_{\mathcal G_\tau}\big(\nu D_3(w)-K\big)dt\le\mathcal Q(0)+C_\sharp\int_{\mathcal B_\tau}d_1D_3(w)\,dt`
   — a bound on the good-set *deficit*, not on `\int_{\mathcal G_\tau}D_3(w)`;
3. for fixed `\delta\in(0,1]`, with
   `\mathcal G^\delta_\tau:=\{t<\tau:C_\sharp d_1(t)\le(1-\delta)\nu\}`,
   `\delta\nu\int_{\mathcal G^\delta_\tau}D_3(w)\,dt\le\mathcal Q(0)+C_\sharp\int_{(\mathcal G^\delta_\tau)^c}d_1D_3(w)\,dt`,
   with `|(\mathcal G^\delta_\tau)^c|\le(1-\delta)^{-3}(C_\sharp/\nu)^3\int_0^\tau d_1^3dt`.

*Proof.* `\mathcal Q(0)-\mathcal Q(\tau)=\int_0^\tau(\nu D_3(w)-K)`.
1. Bound `\int_{\mathcal G_\tau}K\le\nu\int_{\mathcal G_\tau}D_3(w)` (valid since
`C_\sharp d_1\le\nu` there) and `\int_{\mathcal B_\tau}K\le C_\sharp\int_{\mathcal B_\tau}d_1D_3(w)`,
then cancel `\nu\int_{\mathcal G_\tau}D_3(w)` and use `\mathcal Q(\tau)\ge0`.
2. Split the identity and use `\nu D_3(w)-K\ge-(C_\sharp d_1-\nu)D_3(w)` on
`\mathcal B_\tau` and `\mathcal Q(\tau)\ge0`.
3. On `\mathcal G^\delta_\tau`, `K\le C_\sharp d_1D_3(w)\le(1-\delta)\nu D_3(w)`,
so `\nu D_3(w)-K\ge\delta\nu D_3(w)`; insert into 2 with `\mathcal G^\delta_\tau`
in place of `\mathcal G_\tau`; the measure bound is Chebyshev. `\square`

**No bound of the form `\nu\int_{\mathcal G_\tau}D_3(w)\le\text{input}` is
available**, and this is not a defect of technique: the good set only guarantees
`K\le\nu D_3(w)`, and a trajectory saturating (3.1) on `\mathcal G_\tau` has
`\nu D_3(w)-K\approx0` there while `\int_{\mathcal G_\tau}D_3(w)` is
unconstrained. This is worth recording, because it is a second obstruction of
the same type as O2, localised on the *good* set rather than the bad one.

### R4 (repairs and strengthens Proposition 4.3 and Theorem 4.5(1))

**Lemma R4.** For the classical branch and every `\tau<T_*`:
1. `\int_0^\tau\|u\|_3^4dt\le\frac{3C_S^2\|u_0\|_2^4}{2\nu}=\frac{3C_S^2E_0^2}{2\nu}`
   — this is `prop:scaling`(iii), `\eqref{eq:L4L3}`, **already in the
   manuscript**, and it is `\tau`-uniform;
2. hence `\int_0^\tau\|u\|_3^3dt\le\tau^{1/4}\big(\tfrac{3C_S^2E_0^2}{2\nu}\big)^{3/4}`
   by time-Hölder `(4,4/3)` — the candidate's (4.4), with the same
   `E_0^{3/2}\nu^{-3/4}\tau^{1/4}` weights;
3. `\int_0^\tau d_1^4dt\le16\int_0^\tau\|u\|_3^4dt\le\frac{24C_S^2E_0^2}{\nu}`;
4. **`\tau`-uniform crossing bound.**
   `|\mathcal B_\tau|\le(C_\sharp/\nu)^4\int_0^\tau d_1^4dt\le24\,C_S^2\,C_\sharp^4\,E_0^2\,\nu^{-5}`,
   uniformly in `\tau<T_*` — in particular the total measure of the set of
   times at which `\mathcal Q` can increase is finite up to the putative
   blow-up time, with no `\tau^{1/4}` growth.

*Proof.* 1 is `prop:scaling`(iii). 2 is Hölder in time. 3 uses
`d_1\le2\|u\|_3` (`lem:quotient-coercive`) and `16\cdot\frac32=24`. 4 is
Chebyshev at exponent `4`: `|\mathcal B_\tau|(\nu/C_\sharp)^4\le\int_{\mathcal B_\tau}d_1^4\le\int_0^\tau d_1^4`.
`\square`

Scaling check of R4.4: `|\mathcal B_\tau|\sim dt\sim(a^{-1},\lambda^{-2})`;
`E_0^2\nu^{-5}\sim(a^{4-5},\lambda^{-2})=(a^{-1},\lambda^{-2})`. ✓ Consistent.

R4.4 is strictly stronger than the candidate's (4.5) for
`\tau>24^{4}\!\cdot(\dots)` and, more importantly, is the only form that
survives the limit `\tau\uparrow T_*`. **This is the crossing statement the
controller should record**, not (4.5). O1 and O2 are unaffected: O1 runs with
`r=4/3` instead of `r=3/(3-\alpha)` and reaches the same LPS conclusion; O2's
family adapts to `\int c^4\le A_1` verbatim (verified).

---

## 4. CONDITIONAL SUFFIX THAT SURVIVES

Everything below survives unchanged, for the classical branch of
`prop:localtheory` from an arbitrary divergence-free Schwartz datum on `\R^3`
with arbitrary `\nu>0`, on every `[0,\tau]\subset[0,T_*)`:

- **Lemma 1.1, Propositions 1.2, 1.3, 1.4, §1.4 table** — the full comparison
  lattice `d_1,d_2,d_3,d_4`, including the non-invariance of `d_3` and its
  consequent unusability. (R1 of the candidate.)
- **Proposition 2.1 and Theorem 4.1** — the exact distance balance
  `d_2'=P_3-K+\nu(D_3(w)-D_3(u))` and the spacetime identity (4.1)/(4.2), with
  the two signed terms `-d_2(\tau)\le0`, `-\nu\int D_3(u)\le0`, absolute
  continuity established, and the independent cross-check of Remark 2.3.
- **Proposition 3.1** — `|K|\le C_\sharp\|q\|_3D_3(w)`, `C_\sharp=\frac32C_9S`,
  genuinely a line of the audited HF18-A Theorem 4, reproducing `C_*` on
  substitution. (R2 of the candidate.)
- **Proposition 3.2** — the monomial lattice `\alpha+3b+3c+2e=4`,
  `2c-e+d=2`, and `\alpha=1,b=0` as the `b\ge0` endpoint. The claim that
  `\alpha=1` is *sharp* is conditional on Lipschitz continuity of `q` at
  `\mathcal M` (candidate's record item (iv), corrected §3.2 per R2).
- **Proposition 3.3** — the regularity criterion in the distance to
  `\mathcal M`: `C_\sharp\sup_{t<T_*}\|q(t)\|_3\le\nu\Rightarrow T_*=\infty`;
  hypothesis on the unknown trajectory, closes nothing, strictly contains the
  critical-smallness class.
- **Corollary 4.2** — `hyp:absorption` with `\theta'\in[0,1)` implies the
  quotient gap with `\theta=1`, `M=0`, `A_{\rm input}=A+\frac13\|u_0\|_3^3`,
  and `hyp:highstrain` for every `L`. Correct; present as a dictionary with an
  explicit constant, not as a new implication (§1.6).
- **Corollary 4.4** — the `M\int\mathcal Q` term and the Littlewood–Paley
  cutoff `L` are removable from the frozen gap and from `hyp:highstrain` at the
  cost of an input-only change of `A_{\rm input}`. Correct, and after R4 it
  follows from `prop:scaling`(iii) with no new lemma. (R4 of the candidate.)
- **Theorem 4.5 items 1 and 2 and item 3's first display**, with item 1
  upgraded by R4.4 to the `\tau`-uniform `|\mathcal B_\tau|\le24C_S^2C_\sharp^4E_0^2\nu^{-5}`;
  item 3's second display replaced by R3.
- **O1** (with corrections O1a, O1b) and **O2** with Proposition 4.6 —
  the pair (F-a)+(F-b) is provably insufficient for the gap at the level of the
  two abstract functions, and the only Hölder split that uses them is circular.
- **(G)** as the correct reduced target: an input-only bound for
  `\int_0^\tau\|q\|_3D_3(w)\,dt`, uniformly for `\tau<\min\{H,T_*\}`, implies
  the gap with `\theta=0`, no `M` term and no cutoff. Scaling-consistent.
- **§4.6** — the gauge improvement of HF18-B (3.8) under the OPEN (H1),(H2);
  no sign is created by `\operatorname{div}A=0`.

**The first gap is not closed, and the note does not claim it is.** The
candidate's own reading — that (4.1)'s remainder *is* HIGH-PRESSURE, so the
crossing structure of `\mathcal M` supplies the boundary term and nothing else
— is correct and is the honest disposition.

---

## 5. UNNECESSARY DEPENDENCIES

- **HF18-B is not needed** for any displayed result of §§1, 2, 3.1, 3.2, 4.1–4.5.
  It enters only through (Q7) Prop. 1.4 in one scope sentence of §3.3 (that
  `\mathcal M_{\rm sol}` contains fields of arbitrarily large critical norm) and
  through §4.6. Listing it among the note's premises overstates the dependency
  surface of the surviving results.
- **HF17 is not needed as a separate premise**: everything the note uses from it
  is available through the manuscript labels `prop:quotient-evolution`,
  `lem:quotient-transport`, `def:qe-dissipation`.
- **`d_3` and Proposition 1.4 are decorative**: nothing downstream uses (1.3).
  They are correct and belong in R1 as a completeness statement, but they carry
  no weight.
- **`prop:scaling` is a *missing* dependency**, not an unnecessary one: the note
  should cite `eq:L4L3` instead of re-deriving a weaker form (B3/R4).
- The unaudited HF19 and HF20 notes are correctly quarantined and are never
  used as steps; the audited HF20 REPAIR (`rem:no-monotone` in the manuscript)
  is consistent with everything the note claims and, as shown in §2(a), is the
  special family in which the omitted first-order term happens to vanish.

---

## 6. NON-CLAIMS OF THIS REVIEW

This review does not prove or disprove the first gap, `hyp:highstrain`,
`hyp:highpressure`, `hyp:absorption`, `hyp:critical`, or NS-R3. It does not
decide whether `D_3(w)\le D_3(u)` or the reverse, nor whether `q` is Lipschitz
at `\mathcal M`, nor whether the first-order coefficient of `K` at `\mathcal M`
vanishes in general. It supplies no bound on `\sup_t\|u\|_3`,
`\int_0^\tau D_3(w)dt`, `\int_0^\tau D_3(w)^rdt` (`r>1`), or
`\int_0^\tau\|q\|_3D_3(w)dt`. It makes no progress on (H1), (H2), (W), or
`\|w(u)\|_2\le C\|u\|_2`. R4.4 is a strengthening of a measure bound only and
implies nothing about where the dissipation sits. The two random-sampling
computations reported (Bregman constants; O2 arithmetic) are bounded evidence,
not proof, and neither is load-bearing. No novelty claim is made for any
statement here.

---

## 7. EXACT EDITS THE CONTROLLER SHOULD MAKE IF THIS VERDICT STANDS

**Manuscript `../navier-paper/main.tex`** — three edits, all in the
already-audited part of the paper, none of which changes a proved theorem:

- **M1.** After `hyp:highstrain`, insert a remark (proposed label
  `rem:highstrain-normalisation`) recording Corollary 4.4: *the Gronwall term
  and the cutoff are cosmetic.* Statement: with
  `\mathcal Q\le\frac13\|u\|_3^3`, `\eqref{eq:L4L3}` and time-Hölder,
  `\int_0^\tau\mathcal Q\,dt\le\frac13H^{1/4}(3C_S^2\|u_0\|_2^4/2\nu)^{3/4}`
  for `\tau<\min\{H,T_*\}`; consequently `\eqref{eq:quotient-gap}` for `K_L`
  with a datum-selected `L` is equivalent, with an input-only change of
  `A_{\rm input}`, to the same inequality for the full `K` with no
  Littlewood–Paley split, and any additional `M\int_0^\tau\mathcal Q\,dt` term
  is absorbable into `A_{\rm input}`. Cite `lem:quotient-lowstrain`
  (`eq:qe-lowstrain`) for the `K_{\rm low}` half. **Do not** rewrite
  `hyp:highstrain` itself — the `L`-form is what `prop:quotient-conditional`
  consumes, and the remark makes the normalisation explicit without touching a
  proved implication.
- **M2.** In `rem:highstrain-scope`, add one sentence with the explicit
  dictionary of Corollary 4.2: *`hyp:absorption` implies
  `\eqref{eq:quotient-gap}` directly, with `\theta=1` and
  `A_{\rm input}=A(\nu,u_0,H)+\frac13\|u_0\|_3^3+\frac{M_L}3(\cdot)`, by
  subtracting `eq:pressure-balance` from the integrated
  `eq:quotient-evolution`; this is a quantitative form of the composition
  `cor:absorption-consequence` → `thm:conditional` →
  (converse of this remark), and shows the quotient route is not harder than
  the pressure route.* Do **not** present it as a new implication.
- **M3 (optional, cheap).** After `prop:quotient-evolution`, state the exact
  distance balance of Proposition 2.1 as a remark: `F-\mathcal Q` is absolutely
  continuous with `(F-\mathcal Q)'=P_3-K+\nu(D_3(w)-D_3(u))` a.e., obtained by
  subtracting `eq:pressure-balance` from the integrated
  `eq:quotient-evolution`. It costs three lines, needs nothing new, and is the
  cleanest statement of how the two routes differ. Flag explicitly that
  `D_3(u)` (`def:D3P3`) and `D_3(w)=D_{\mathcal Q}` (`def:qe-dissipation`)
  are different objects, comparable only on `\mathcal M`.

**Claim graph** (`docs/` or wherever the graph lives):

- **G1.** Add node `hf21-distance-balance` = Proposition 2.1 / Theorem 4.1,
  depending on `prop:pressure`, `prop:quotient-evolution`, HF18-A (Q6).
  Status: PASS (this review).
- **G2.** Add node `hf21-alpha-one` = Proposition 3.1
  (`|K|\le C_\sharp\|q\|_3D_3(w)`), depending on HF18-A Theorem 4. Status:
  PASS. Mark it as a *strengthening of an existing audited line*, not a new
  theorem.
- **G3.** Add node `hf21-gap-normalisation` = Corollary 4.4, depending on
  `prop:scaling`(iii) and `lem:quotient-lowstrain`. Status: PASS. Attach M1.
- **G4.** Add node `hf21-crossing-measure` = R4.4 (`\tau`-uniform bad-set
  measure), depending on `prop:scaling`(iii) and Proposition 3.1. Status: PASS.
  Mark the candidate's `\tau^{1/4}` version (4.5) as superseded.
- **G5.** Add obstruction nodes `hf21-O1` (circularity of the Hölder split;
  every `\alpha`) and `hf21-O2` (insufficiency of (F-a)+(F-b)) as *negative*
  results attached to the first gap, with the corrections O1a, O1b applied.
  Add `hf21-O3` = R3 (no input bound on `\int_{\mathcal G_\tau}D_3(w)`).
- **G6.** Do **not** add a node for the candidate's §3.2 boxed conditional. If
  a sharpness node is wanted, add `hf21-alpha-sharpness` in the R2 form:
  *Lipschitz at `\mathcal M` + nonvanishing first-order coefficient ⇒
  `\alpha=1` sharp; audited Hölder-`1/2` refutes only `\alpha>2`.* Status:
  CONDITIONAL, open.
- **G7.** Do **not** add a node for Proposition 4.3 as a new result; point
  `hf21` at the existing `prop:scaling`(iii) node instead.

**`PLAN.md`:**

- **P1.** Under "Ordered next actions", replace the HF21 follow-up with the
  candidate's own NEXT DISTINCT ACTION, sharpened: attack **(G)**,
  `\int_0^\tau\|q\|_3D_3(w)\,dt\le A_{\rm input}`, since Corollary 4.4 shows it
  is the whole of the frozen gap with `\theta=0`.
- **P2.** Record the two sub-questions the note isolates, in this order:
  (a) is `D_{\mathcal Q}(u)=D_3(w)\le D_3(u)` at fixed time? — minimizer-free,
  scaling-consistent `(a^3,\lambda^2)` on both sides, and an affirmative answer
  deletes `\nu\int(D_3(w)-D_3(u))` from (4.1) and gives the gap with
  `\theta=0` from the pressure flux alone;
  (b) is `u\mapsto q(u)` `L^3`-Lipschitz at points of `\mathcal M`? — decides
  `\alpha=1` sharpness **in the R2 direction**, i.e. Lipschitz *refutes*
  `\alpha>1`.
- **P3.** Add a third: R3's good-set obstruction, i.e. whether any input-only
  bound for `\int_{\mathcal G^\delta_\tau}D_3(w)dt` is available for some fixed
  `\delta`, since R3.3 is the only good-set statement that survives.
- **P4.** Record that the HF20 audit is consistent with HF21's §3.2 only in the
  corrected R2 direction, and that `rem:no-monotone`'s family is the special
  configuration in which the minimizer's first-order contribution to `K`
  vanishes.

**The note itself** (to be edited by its owner, not by this review):
replace the §3.2 box and the preceding expansion by R1 and R2; replace
Theorem 4.5 item 3's second display by R3; replace Proposition 4.3 by a
citation of `prop:scaling`(iii) plus R4, and upgrade Theorem 4.5 item 1 to
R4.4; fix O1a (constant power `3\to1`), O1b (restore the
`\mathcal Q^{(1-\alpha)/3}` factor and downgrade "strictly stronger" to
"at least as strong"); drop the claim that (R3) is new; and delete HF18-B from
the premise list of everything except §3.3's scope sentence and §4.6.

---

## 8. REOPENING CONDITION

This verdict is reopened, and the whole note must be re-audited, if any one of
the following occurs.

1. **A proof that `\varepsilon\mapsto A(U+\varepsilon h)` is differentiable at
   `\varepsilon=0` in `L^{3/2}` with
   `\langle\frac{d}{d\varepsilon}A_\varepsilon|_0,\mathbb P((U\cdot\nabla)U)\rangle=0`
   for all `U\in\mathcal M_{\rm sol}`, `h` solenoidal** — then the candidate's
   §3.2 expansion is correct after all as an expansion (though the boxed
   conditional remains inverted and R2 still applies), and B1 collapses to the
   logical inversion alone.
2. **A proof or refutation of `L^3`-Lipschitz continuity of `q` at
   `\mathcal M`** — either settles R2 and turns Proposition 3.2's endpoint claim
   unconditional in one direction or the other, and decides the status of
   `\alpha\in(1,2]`.
3. **Any repair of HF19-B/HF19-D or a second audit of HF20 that changes the
   first-order behaviour of `K` at `\mathcal M`** — §3.2 and record item (iv)
   must then be rewritten against the new audited fact.
4. **A change to `prop:pressure`, `prop:quotient-evolution`,
   `def:qe-dissipation` or `prop:scaling`(iii) in the manuscript** — Proposition
   2.1, Theorem 4.1, Corollary 4.4 and R4 all rest on those four and on nothing
   else of substance.
5. **A proof of `D_3(w)\le D_3(u)` or of its failure** — the former deletes a
   term from (4.1) and changes the dictionary of Corollary 4.2 materially; the
   latter would need re-examination of whether (4.1) is still the right shape.
6. **Any input-only bound on `\int_0^\tau D_3(w)^rdt` for some `r>1`, or on
   `\int_0^\tau\|q\|_3D_3(w)dt`** — the first would contradict O1's circularity
   reading (it would be the LPS conclusion, so the gap would be closed by other
   means and O1 becomes moot); the second is (G) and closes the gap.
7. **Discovery that `C_{\mathbb P}<1`** (it is not, but the note's §1.3 upper
   bound silently assumes `C_{\mathbb P}\ge1`) — Proposition 1.3's right-hand
   constant would need the explicit `\max\{1,C_{\mathbb P}\}`.

---

## 9. RECORD

**VERDICT:** REPAIR. Three defects (B1 first bad bridge, B2, B3), all repaired
above with displayed replacement lemmas R1–R4; no result of the note is lost,
one (Theorem 4.5(1)) is strengthened, one (Proposition 4.3) is demoted from new
to a corollary of an existing manuscript proposition.

**FIRST BAD BRIDGE:** §3.2, the first-order expansion of
`K(U+\varepsilon h)` at `\mathcal M` and the boxed conditional
"an `\alpha>1` bound is compatible with the audited record only if the
nonlinear projection is Lipschitz". The expansion omits the
`O(\varepsilon)` term `-\langle A_\varepsilon-j(U),\mathbb P((U\cdot\nabla)U)\rangle`;
the conditional is logically inverted (Lipschitz *refutes* `\alpha>1`), and it
contradicts the note's own record item (iv). Replaced by R1 and R2.

**EVIDENCE:** every constant and exponent of §§1–4 recomputed from the
manuscript sources named in REVIEWED SCOPE; the Bregman inequalities checked
symbolically and on `2\times10^5` random samples; the `(a,\lambda)` weights
recomputed independently for every displayed inequality; the O2 family checked
in both its `L^3` and `L^4` forms; `prop:scaling`(iii) `\eqref{eq:L4L3}` read in
full and used to supersede Proposition 4.3 and to upgrade Theorem 4.5(1);
`hf18-review-hodge-regularity.md` R8 and `hf18-review-divergence-speed-link-r2.md`
consulted for faithfulness of citation only.

**NEXT DISTINCT ACTION FOR THE PROGRAMME:** (G),
`\int_0^\tau\|q(t)\|_3D_3(w(t))\,dt\le A_{\rm input}(\nu,u_0,H)`, together with
the fixed-time question `D_3(w)\le D_3(u)?`, as in P1–P3.
