# Audit of HF24-A: an input-only modulus of continuity for the distance to the nonlinear-Hodge class

**AUDIT STATUS (2026-09-06).** Independent proof-audit of
`research/evidence/hf24-modulus-of-continuity.md`, MODE: **proof-audit**.
This review owns exactly one file, the present one. Nothing else in the
repository is edited; nothing is committed, pushed or promoted; the
manuscript is untouched.

**Frozen target.**

```
file    research/evidence/hf24-modulus-of-continuity.md
sha256  ed5e2a56e093862a73909a02f2ce617f97d523b2ce95f3020599dcd32f130cb6
lines   683
HEAD    a91fe79a10f810b81c9560186ef0f657a622f589   (branch main, clean)
```

**Audited background used as premises** (as licensed by the audit brief, each
used strictly inside its audited scope): `../navier-paper/main.tex`
`sec:quotient` in full, including `prop:quotient-divcurl` \eqref{eq:qdc-w}
\eqref{eq:qdc-q} \eqref{eq:qdc-sobolev} \eqref{eq:qdc-interp}
\eqref{eq:qdc-sobolev-field}, `lem:trace-control`, `cor:quotient-defect`
\eqref{eq:qdc-sigma} \eqref{eq:qdc-sigmaid} \eqref{eq:qdc-potential},
`cor:quotient-vorticity-zero`, `lem:quotient-mixed-pressure`,
`cor:quotient-budgets`, `rem:quotient-divcurl-scope`,
`prop:quotient-evolution`, `def:qe-dissipation`, `lem:quotient-lowstrain`,
`hyp:highstrain`, `rem:highstrain-normalisation`, `rem:highstrain-scope`,
`rem:no-monotone`, `prop:quotient-conditional`; outside that section
`prop:localtheory` (iii)/(v), `cor:Lq`, `prop:energy`, `prop:scaling`(iii)
\eqref{eq:L4L3}, `lem:leray`, `def:sobolev-constant`, `rem:mismatch`,
`hyp:critical`, `thm:conditional`, `thm:continuation`. Evidence base:
HF18-A (`hf18-hodge-regularity.md`, Theorem 2: `D_Q = D_3(w)`), HF18-B
(`hf18-divergence-speed-link.md`, `int |w| sigma^2 <= (1/2) D_3(w)`),
HF21-A/HF21-B as repaired (`hf21-crossing-sign-structure.md`, Prop. 3.1,
Lemma 4.3, Theorem 4.5), HF20 and HF22 as repaired — in particular
**`hf22-projection-regularity.md` Theorem A / Corollary A1 with its audit
`hf22-review-projection-regularity.md` §3.1–3.2**, `hf22-direct-attack.md`
(H-mod), Lemma R1, Remarks 3.6–3.7, `hf22-good-set-dissipation.md` Theorem B
— and HF23 Scope A. **HF25 is not used anywhere in this review.**

---

## 0. VERDICT

**REPAIR.** The lane's two load-bearing new theorems — the modulus
(Theorem 3.3) and the unconditional traversal-cost constraint (Theorem 4.1) —
are **correct as displayed**, with every constant, exponent and scaling weight
recomputed here and confirmed. Lemma 3.2 is correct. The audit finds:

1. **Prop. 2.1's "equivalence" is false** (first bad bridge in document
   order, **not load-bearing**). The two displayed inequalities after the
   identity are the *same* inequality; no reverse bound is proved, and none is
   true. Refuted below by an explicit family, with numerics.
2. **Corollary 4.3's component count is not derivable and its proof has two
   independent gaps** (first bad bridge in the *load-bearing* chain). A
   repaired statement, proved in full, is supplied in §4; the repaired form
   still covers the bad set of (G), so the lane's conditional suffix survives.
3. **Lemma 3.1 is not new.** It is `hf22-projection-regularity.md`
   Theorem A + Corollary A1 verbatim — same statement, same constant `4`,
   same three-step proof — already **audited PASS**. The lane's Inputs list
   omits that note. The novelty label must be withdrawn.
4. **The decisive question is resolved, in the lane's favour, and sharply.**
   Hypothesis (C) is **NOT circular**: it is implied by the Clay conclusion
   but does **not** imply it. §5 gives an exact characterisation of when (C)
   holds (Proposition R1), proved from the audited record alone. The lane's
   §5.1(3) "not decided here" is thereby upgraded to decided. The route is
   **not** retired.
5. **The exponent `1/4` cannot be raised inside the currency the lane names**;
   `(3/4,1/4)` is the *unique* scaling-admissible monomial in `(G,mu)`
   (§6). The note's own second `needs review` bullet is therefore already
   answered by its own §5.2(1) — and that §5.2(1) is in turn slightly
   overstated once `nu` is admitted as an ingredient (§6.2). The bullet also
   **mis-cites** the audited HF22 correction, which concerns the exponent
   `alpha` in `|K| <= C d_1^alpha D_3(w)`, not a modulus exponent.

Nothing in the note uses `w in L^2`, `sigma in L^{3/2}`, the residual
hypothesis (H2), a time or space derivative of the minimiser, uniform
convexity, a Clarkson inequality, or HF25. Those scope declarations are
**verified**. No smallness hypothesis, no periodic/forced/hyperdissipative
substitute, no representative in `L^2`: verified.

(G) is neither proved nor refuted by the note, and is not proved or refuted
here.

---

## 1. REVIEWED SCOPE

Every numbered statement of the target was reconstructed from its first
nontrivial implication. Recomputed independently: the Frobenius-norm symbol
computation of Prop. 2.1; the HLS exponent pair and the `Hdot^{-1}`
characterisation of Prop. 2.2 / Remark 2.3; the two-parameter monomial
solve of Remark 2.3; all four steps of Lemma 3.1 (cancellation, integrated
`eq:cp-monotone`, weighted Cauchy–Schwarz, finiteness); every symbol
computation, both time-Hölder steps and both scaling weights of Lemma 3.2;
both interpolation exponents, the `(1/6,5/6)` Hölder pair, the constant
`(5/4)^{1/2} = sqrt5/2`, the constant `(2 sqrt 5)^{1/3}` and the numeric
`kappa_0 = 1 + (2 sqrt5)^{1/3} = 2.6476... < 2.65` of Theorem 3.3; the
algebra of (3.8) in Remark 3.4; the substitution and disjointness of
Theorem 4.1; the counting of Corollary 4.2; the component bookkeeping,
the endpoint placement and the Chebyshev constant of Corollary 4.3; the
seven-line dimensional table and the saturation identity of §5.2; the two
supercritical time integrals of §5.3; and all eight rows of the §5.4 table.

Not in scope, not assessed: NS-R3; (G) itself; the correctness of
`hf24-badset-restriction.md` (the sibling lane); HF25.

---

## 2. FIRST BAD BRIDGE

### 2.1 In document order: §2.1, Proposition 2.1 — "the transfer is an equivalence" is FALSE

The displayed proposition reads

```
   ||grad(q'-q)||_2 = ||sigma'-sigma||_2 ,
   C_S^{-1} ||q'-q||_6  <=  ||sigma'-sigma||_2 ,
   ||q'-q||_6  <=  C_S ||sigma'-sigma||_2 .
```

The second and third displays are **the same inequality written twice**
(multiply the second by `C_S`). The proof text confirms this: it attributes
one of them to \eqref{eq:qdc-sobolev-field} on `q'-q` and the other to "the
trivial converse `||grad z||_2 >= C_S^{-1}||z||_6`", which *is*
\eqref{eq:qdc-sobolev-field} again. So the proposition contains exactly two
distinct statements, both correct:

* the identity `||grad(q'-q)||_2 = ||sigma'-sigma||_2` — **verified**. From
  \eqref{eq:qdc-potential}, `d_k q_j = R_jR_k sigma`, linear in `sigma`, so
  `d_k(q'-q)_j = R_jR_k(sigma'-sigma)`; by Plancherel and
  \eqref{eq:riesz-symbol} the matrix symbol is `(-xi_j xi_k/|xi|^2)_{j,k}`,
  whose squared Frobenius norm is
  `(sum_j xi_j^2)(sum_k xi_k^2)/|xi|^4 = 1` at every `xi != 0`. Consistent
  with \eqref{eq:qdc-q} (`||grad q||_2 = ||div w||_2` and `sigma = -div w`);
* the one-sided bound `||q'-q||_6 <= C_S ||sigma'-sigma||_2`. Legitimacy of
  \eqref{eq:qdc-sobolev-field} on the difference is **confirmed**: the cutoff
  argument at the end of Step 5 of `prop:quotient-divcurl`'s proof establishes
  `||z||_6 <= C_S||grad z||_2` for *every* `z in L^6` with `grad z in L^2`,
  and `q'-q` is such a field. (The note's citation of "Step 4 of
  `cor:quotient-defect`" is the wrong pointer; the correct pointer is the
  cutoff paragraph of Step 5 of `prop:quotient-divcurl`. Cosmetic.)

The **bad bridge** is the prose immediately after:

> "time regularity of `q` in `L^6` and time regularity of `sigma` in `L^2`
> are the same statement, with constant `C_S` in both directions"

and its two downstream restatements: §5.4 row 2 ("Equivalent to a modulus for
`sigma` in `L^2` (Prop. 2.1)") and §6 CLAIM 1 ("`||q(t')-q(t)||_6` and
`||sigma(t')-sigma(t)||_2` are equivalent up to `C_S`"). No reverse bound is
proved, and none exists.

**Refutation by an explicit family.** Let `sigma` be a wave packet at
frequency `n`: `sigma_n(x) = cos(2 pi n x_1) phi(x)` with `phi` a fixed
Schwartz bump. The potential relation `d_kq_j = R_jR_k sigma` forces
`hat q(xi) = i xi hat sigma(xi) / (2 pi |xi|^2)`, hence
`|hat q| = |hat sigma|/(2 pi |xi|)` and, on the packet's support
`|xi| ~ n`, `q_n ~ (2 pi n)^{-1} e_1 sigma_n` pointwise. Therefore

```
   ||sigma_n||_2 -> ||phi||_2 / sqrt2   (fixed),
   ||q_n||_6     ~  ||phi||_6 / (2 pi n)  ->  0 ,
```

so `||sigma_n||_2 / ||q_n||_6 -> infinity` and **no** inequality
`||sigma'-sigma||_2 <= C ||q'-q||_6` can hold, with any constant. Note that
this family satisfies the potential relation exactly, so it is not evaded by
restricting to defect-generated fields; scaling does not detect the failure
(`||q||_6` and `||sigma||_2` both have weight `(a,lambda^{-1/2})`), which is
presumably why the note missed it.

**Numerical corroboration** (evidence, not proof; `N = 64` periodic grid,
`phi` a Gaussian of width `0.08`, exact spectral evaluation of
`hat q = i xi hat sigma/(2 pi |xi|^2)`):

| `n` | `||sigma||_2` | `||grad q||_2` | `||q||_6` | `||q||_6/||sigma||_2` |
|---|---|---|---|---|
| 1 | 0.05033 | 0.04982 | 0.010035 | 0.1994 |
| 2 | 0.04409 | 0.04383 | 0.008744 | 0.1983 |
| 4 | 0.03809 | 0.03807 | 0.006871 | 0.1804 |
| 8 | 0.03776 | 0.03776 | 0.004456 | 0.1180 |
| 16 | 0.03776 | 0.03776 | 0.002503 | 0.0663 |

The identity `||grad q||_2 = ||sigma||_2` is reproduced to five digits (an
independent check of the first display of Prop. 2.1), and the ratio halves
when `n` doubles, matching the predicted `1/n` decay.

**Status of the affected claims: FALSE, not merely non-derivable.** The
correct statement is the identity, which is an equivalence between
`||grad(q'-q)||_2` and `||sigma'-sigma||_2` — i.e. between `Hdot^1` regularity
of `q` and `L^2` regularity of `sigma` — together with the *one-sided*
`L^6` bound. §3 below repairs the text.

**Load-bearing?** No. §2 is a negative section; nothing in §3, §4 or §5 uses
Prop. 2.1. The Conclusion of Part (1) ("the potential representation controls
`t -> ||q(t)||_6` exactly") is the same overstatement and must be weakened to
"controls `t -> ||q(t)||_6` from above, and controls `t -> ||q(t)||_3` not at
all"; the negative half of Part (1) is untouched by the correction.

### 2.2 In the load-bearing chain: §4, Corollary 4.3 — the component count does not follow

The corollary asserts, under (C), that
`B_tau^{eps} = {t < tau : C_sharp d_1(t) > (1-2 eps) nu}` has **at most
`1 + 8 Theta Gamma^3` connected components**. Two independent defects.

**(a) Corridor-only components are never charged.** The proof's second
sentence reads: "A component that does not meet
`{C_sharp d_1 >= (1-eps)nu}` is contained in the corridor and is separated
from the next such component by a return below `(1-2eps)nu/C_sharp`, i.e. by
a traversal of the same corridor." That inference is **invalid**. By the
lane's own Definition (§4), a traversal is an interval whose two endpoints
satisfy `{d_1(t_i), d_1(t_i')} = {<= a_eps, >= b_eps}`; a return below
`a_eps` from a component that never reaches `b_eps` is *not* a traversal, and
Theorem 4.1 charges it nothing. So components lying entirely inside the
corridor are uncounted, and there is no bound on their number.

They cannot be dismissed as pathological: by Theorem 3.3 itself, an excursion
of height `delta` above `a_eps` costs only
`mu >= delta^4 kappa_0^{-4}C_S^{-2}G^{-3}`, which tends to `0` with `delta`.
A continuous `d_1` with infinitely many excursions above `a_eps` of heights
`delta_k -> 0`, all below `b_eps`, is compatible with **every** displayed
ingredient: it produces zero traversals (so (4.1) is vacuous), it satisfies
(C) vacuously or with any `Gamma`, and it satisfies the Chebyshev measure
bound. Hence the component count is **NOT DERIVABLE** from
(C) + Theorem 4.1 + continuity of `d_1`. (It is *not* thereby shown false for
actual Navier–Stokes trajectories; distinguishing the two is exactly the
brief's requirement, and this is the "not derivable" side.)

**(b) The endpoints of a traversal need not be corridor times, so (C) does
not apply to them.** The proof says a component meeting
`{C_sharp d_1 >= (1-eps)nu}` "contains a traversal, with `G_i <= 2Gamma` by
(C)". But (C) bounds `||grad u(t)||_2` only when `C_sharp d_1(t)` lies in the
**closed corridor** `[(1-2eps)nu,(1-eps)nu]`, whereas a traversal endpoint
only satisfies `d_1 <= a_eps` or `d_1 >= b_eps` and may sit arbitrarily far
outside. As written, `G_i <= 2Gamma` does not follow. This defect is
repairable (§4) by *choosing* the traversal to have both endpoints exactly on
the corridor walls; the note does not make that choice.

**Not affected:** the measure bound
`|B_tau^{eps}| <= 24 C_S^2 C_sharp^4 E_0^2 / ((1-2eps)^4 nu^5)` inside
Corollary 4.3 is **unconditional** (it never uses (C)) and is **verified**:
Chebyshev at exponent 4 at the level `(1-2eps)nu/C_sharp` against HF21-B
Lemma 4.3(3) `int_0^tau d_1^4 dt <= 24 C_S^2 E_0^2/nu` gives exactly that
constant. It should be stated separately from the conditional part.

---

## 3. EVIDENCE: what was checked and what stands

### 3.1 Lemma 3.1 — correct, but **not new**

The mathematics is **correct**, recomputed line by line:

* cancellation `<A'-A, w'-w> = <A'-A, h>` uses only
  `w'-w-h = q(u')-q(u) in G_3` and `lem:quotient-minimizer`(c) at both
  minimisers; both pairings are finite (`A,A' in L^{3/2}`, `w'-w,h in L^3`);
* the integrated \eqref{eq:cp-monotone} is an **identity** with nonnegative
  integrand, so `<A'-A,w'-w> = (1/2) int (|w|+|w'|)[(|w'|-|w|)^2 + |w'-w|^2]
  >= (1/2) rho^2`, `rho^2 := int(|w|+|w'|)|w'-w|^2`;
* the **weighted Cauchy–Schwarz** is legitimate: `(|w|+|w'|) dx` is a
  nonnegative measure and `|A'-A| <= (|w|+|w'|)|w'-w|` a.e. is
  \eqref{eq:cp-lipschitz} pointwise, so
  `<A'-A,h> <= int (|w|+|w'|)|w'-w||h| <= rho X^{1/2}`;
* **finiteness** is correct and is what licenses the division: `X <=
  (||w||_3+||w'||_3)||h||_3^2 < infinity` by Hölder `(3,3/2)`, and
  `rho^2 <= 2<A'-A,w'-w> < infinity`, so `(1/2)rho^2 <= rho X^{1/2}` may be
  divided by `rho` when `rho > 0` and is trivial otherwise. Hence (3.1);
* (3.2) is `|w'-w| <= |w|+|w'|` pointwise, so
  `||w'-w||_3^3 = int|w'-w|^2|w'-w| <= rho^2 <= 4X`.

**But**: this is `hf22-projection-regularity.md` **Theorem A** (`N <= 2M_h`,
i.e. (3.1)) and the first chain of its **Corollary A1** (i.e. (3.2)),
verbatim — identical statement, identical constant `4`, identical
three-step proof — and it is **audited PASS** in
`hf22-review-projection-regularity.md` §3.1–3.2 ("Theorem A stands",
"**Correct**"). That note is absent from the lane's Inputs list. The label
"(weighted stability; **new**)" and §6 CLAIM 2 must be withdrawn and replaced
by a citation. The audit of HF22-B also recorded two by-products the lane
would have gained for free: the discarded term
`int (|w|+|w'|)(|w'|-|w|)^2` is available at no cost, and Theorem A is a
**two-point** inequality (the weight depends on both `u` and `u'`), so it is
not a Lipschitz property of any map between fixed normed spaces.

**What *is* new** in §3 is not Lemma 3.1 but its **use** in step (ii) of
Theorem 3.3: pairing the weight against `||w||_6` (through
\eqref{eq:qdc-sobolev}) instead of against `||w||_3`. HF22-B always paired it
with `W = || |w|+|w'| ||_3`. That substitution is the genuine content of the
lane's §3 and is correctly credited by the note's own sentence "**This is the
one step that uses the new regularity, and it is the whole of the upgrade**".

**Comparison with the audited HF18-B weighted bound (brief item; the note's
first `needs review`).** HF18-B supplies `int |w| sigma^2 <= D_3^{rad}(w) <=
(1/2) D_3(w)`. Lemma 3.1's right side is `int (|w|+|w'|)|h|^2` with
`h = u(t')-u(t)`. **No comparison between the two is scaling-admissible.**
In the lane's own two-parameter convention, pointwise field values carry
weight `(a, lambda^0)`, `dx` carries `(a^0, lambda^{-3})` and one spatial
derivative carries `(a^0,lambda)`, so

```
   int (|w|+|w'|)|h|^2 dx  ~  (a^3, lambda^{-3}),
   int |w| sigma^2 dx  ~  D_3(w)  ~  (a^3, lambda^{-1}) .
```

The two differ by exactly `lambda^{-2}`, i.e. by two spatial derivatives; the
unique elementary input quantity carrying weight `(a^0,lambda^{-2})` is
`nu (t'-t)`. Hence the only scaling-consistent shape a comparison could take
is `int(|w|+|w'|)|h|^2 <~ nu (t'-t) D_3(w)`, which is a *time*-increment
statement, not a `mu`-currency one, and is not derivable from the record.
**Answer to the first `needs review` bullet: negative on scaling grounds, in
the currency the lane uses.**

### 3.2 Lemma 3.2 — correct, including the low-frequency behaviour of `d_t u`

Verified in full.

* **Symbols.** `||nu Delta u||_{Hdot^{-1}} = nu||grad u||_2` **exactly**: the
  weight `(2 pi|xi|)^{-1}` is over-compensated by `|xi|^2`, so there is *no*
  low-frequency obstruction in the viscous term. For the transport term,
  `|widehat{div F}| <= 2 pi |xi| |hat F|` gives
  `||div F||_{Hdot^{-1}} <= ||F||_2` with the weight cancelling **exactly**;
  again no low-frequency obstruction, and no cancellation at `xi = 0` needs to
  be invoked. With `|u tensor u|_F = |u|^2`, `||u tensor u||_2 = ||u||_4^2`.
  `P` has the orthogonal-projection symbol `Pi(xi)` of `lem:leray`(a), so it
  is a contraction in every weighted `L^2(|xi|^{2s})`, in particular on
  `Hdot^{-1}`. The note's sentence "both terms have vanishing symbol at
  `xi = 0` of the required order" is a **correct conclusion reached by a
  loose route**: the true reason is that the two displayed estimates are
  already finite, and the finiteness of `||(2 pi|xi|)^{-1} widehat{d_su}||_2`
  is what defines membership. Since `|s| = 1 < 3/2 = d/2`, `Hdot^{-1}(R^3)` is
  a genuine complete Hilbert space of tempered distributions, so the framing
  is sound.
* **Bochner integral.** `prop:localtheory`(iii) gives
  `u in C^j([0,T];H^k)` for all `j,k`, so
  `s -> nu Delta u(s)` and `s -> P div(u tensor u)(s)` are continuous into
  `Hdot^{-1}` (difference bounded by
  `nu||grad(u(s)-u(s'))||_2 + ||u(s) tensor u(s) - u(s') tensor u(s')||_2`),
  hence `s -> d_su` is continuous into `Hdot^{-1}` on compacta of `[0,T_*)`
  and the Bochner integral exists; it agrees with the `H^k`-valued integral
  as a tempered distribution, so `h = int_t^{t'} d_su ds` in `Hdot^{-1}`.
  **Correct.** (A cheaper route avoiding Bochner theory altogether:
  `hat h(xi) = int_t^{t'} widehat{d_su}(xi) ds` and Minkowski's integral
  inequality in `L^2((2 pi|xi|)^{-2} d xi)` give (3.3) directly. The
  controller may prefer this; both are valid.)
* **(3.4).** `int_0^tau nu||grad u||_2 <= nu H^{1/2}(E_0/2nu)^{1/2} =
  (nu E_0 H/2)^{1/2}` — **verified**. `||u||_4 <=
  ||u||_2^{1/4}||u||_6^{3/4}` (`1/4 = (1/4)(1/2)+(3/4)(1/6)`) with
  \eqref{eq:qdc-sobolev-field} gives `||u||_4^2 <= C_S^{3/2}E_0^{1/4}Y^{3/4}`;
  Hölder `(4/3,4)` in time and `prop:energy` give
  `int_0^tau ||u||_4^2 <= C_S^{3/2}E_0^{1/4}H^{1/4}(E_0/2nu)^{3/4} =
  C_S^{3/2}E_0 H^{1/4}(2nu)^{-3/4}` — **verified, exponent by exponent**.
* **Scaling.** `||f||_{Hdot^{-1}}` under `f -> a f(lambda .)` carries
  `a lambda^{-5/2}`: `hat f(xi/lambda) lambda^{-3}` in the weighted `L^2`
  gives `lambda^{-3} lambda^{3/2} lambda^{-1} = lambda^{-5/2}`. Both terms of
  `M` carry `(a,lambda^{-5/2})` — **verified**, as the note states.

### 3.3 Theorem 3.3 — correct

Both steps recomputed.

*(i)* `||h||_3 <= ||h||_2^{1/2}||h||_6^{1/2}` \eqref{eq:qdc-interp};
`||h||_6 <= C_S||grad h||_2 <= C_S G` \eqref{eq:qdc-sobolev-field} (legitimate:
`h in H^k`); `||h||_2^2 = int |hat h|^2 <= ||h||_{Hdot^1}||h||_{Hdot^{-1}} <=
G mu` by Cauchy–Schwarz in `xi` splitting the weight as
`(2 pi|xi|)(2 pi|xi|)^{-1}`. Hence (3.6),
`||h||_3 <= C_S^{1/2}G^{3/4}mu^{1/4}`. **Verified.**

*(ii)* The **difference form of \eqref{eq:qdc-sobolev-field}** flagged by the
brief is *not* used here; what is used is \eqref{eq:qdc-sobolev} at the two
separate times, `||w||_6 <= (5/4)^{1/2}C_S||grad u(t)||_2`, plus Lemma 3.1.
`(5/4)^{1/2} = sqrt5/2`, so `||w||_6+||w'||_6 <= (sqrt5/2) C_S G` —
**verified**. Hölder with `1/6+5/6 = 1` on `int(|w|+|w'|)|h|^2` gives
`(||w||_6+||w'||_6) || |h|^2 ||_{6/5} = (||w||_6+||w'||_6)||h||_{12/5}^2` —
**verified** (`|| |h|^2 ||_{6/5} = ||h||_{12/5}^2`). The interpolation exponent
is correct: `5/12 = (3/4)(1/2)+(1/4)(1/6)`, so
`||h||_{12/5}^2 <= ||h||_2^{3/2}||h||_6^{1/2} <= (G mu)^{3/4}(C_S G)^{1/2} =
C_S^{1/2}G^{5/4}mu^{3/4}`. Hence
`||w'-w||_3^3 <= 4 (sqrt5/2) C_S^{3/2} G^{9/4} mu^{3/4} = 2 sqrt5 C_S^{3/2}
G^{9/4}mu^{3/4}` and (3.7). **Verified.**

`kappa_0 = 1 + (2 sqrt5)^{1/3}`: `2 sqrt5 = 4.47214`, cube root `1.64764`, so
`kappa_0 = 2.64764 < 2.65`. **Verified.** Scaling of (3.5):
`G^{3/4}mu^{1/4} ~ (a^{3/4+1/4}, lambda^{-3/8-5/8}) = (a,lambda^{-1}) =
||q||_3`. **Verified.**

The prefixed step `| ||q(t')||_3 - ||q(t)||_3 | <= ||q(t')-q(t)||_3` is the
reverse triangle inequality; `q'-q = (w'-w)-h` since `q = w-u`. **Verified.**
Nothing differentiates the minimiser; the solution class is the maximal
classical branch throughout; no `sup_t` of any critical norm appears in the
constant. **Verified.**

### 3.4 Theorem 4.1 and Corollary 4.2 — correct

From `c <= kappa_0 C_S^{1/2}G_i^{3/4}mu_i^{1/4}`,
`mu_i >= c^4 kappa_0^{-4}C_S^{-2}G_i^{-3}`; disjointness (endpoints are a
null set and `mu` has the density `g`) gives `sum mu_i <= M`; with
`c = eps nu/C_sharp`, `sum G_i^{-3} <= kappa_0^4 C_S^2 C_sharp^4 M
eps^{-4}nu^{-4} = Theta`. **Verified.** Scaling: `G^{-3} ~ (a^{-3},
lambda^{3/2})` and `M nu^{-4} ~ (a^{-3},lambda^{3/2})`. **Verified.**
Corollary 4.2 (`N Gamma^{-3} <= sum G_i^{-3} <= Theta`). **Verified.**

Theorem 4.1 is genuinely unconditional and does not pass through the crossing
measure; that part of the lane's self-assessment stands.

### 3.5 Remarks 3.4, 4.5, and §5.2, §5.3 — correct with two small corrections

* **(3.8) has a wrong second constant.** `||w||_3 <= ||u||_3 <=
  C_S^{1/2}E_0^{1/4}Y^{1/4} <= C_S^{1/2}E_0^{1/4}G^{1/2}` is correct
  (`lem:quotient-coercive` upper half, \eqref{eq:qdc-interp},
  \eqref{eq:qdc-sobolev-field}, `prop:energy`). But `2(A+B)^{1/2}B^{1/2} <=
  2A^{1/2}B^{1/2} + 2B` with `B = ||h||_3`, and then `||q'-q||_3 <=
  ||w'-w||_3 + ||h||_3` adds a third copy: the correct second term of (3.8) is
  `3 C_S^{1/2}G^{3/4}mu^{1/4}`, not `1 x`. The leading term
  `2C_S^{1/2}E_0^{1/8}G^{5/8}mu^{1/8}` is **correct**. Remark 4.5's
  `sum G_i^{-5} <= 2^8 C_S^4 E_0 M c^{-8}` uses only the leading term, so it
  should read `4^8` after splitting `c` between the two terms; the comparison
  it draws (`c^4G^{-3}` beats `c^8G^{-5}` when `G > c^2`) is unaffected and
  **correct**.
* **"contrary to what HF22-C §6 and `hf22-direct-attack.md` §3 record"
  overstates.** What HF22-D records (block R-D, verbatim) is that HF21-B
  Remark 2.2's constant contains `sup||d_tu||_3` and `sup||w||_3`, "neither of
  which is bounded **uniformly in `tau < T_*`**", and that "the open question
  is the `tau`-uniform lower bound on the crossing time … not trajectory
  independence". Replacing both by the single `G`, which is *also* not
  `tau`-uniformly bounded, does not contradict that diagnosis; it improves the
  bookkeeping. The word "contrary" should be "refining".
* **§5.2 dimensional table — recomputed and correct.** With `A l = nu/C_sharp`
  and `T_l = l/A = C_sharp l^2/nu`: `||grad u||_2 ~ A l^{1/2} ~ nu l^{-1/2}`;
  energy `~ nu^2 l`; `int_{T_l} Y ~ nu l`; `g ~ nu^2 l^{-1/2}` with the two
  contributions `nu||grad u||_2` and `||u||_4^2 ~ A^2 l^{3/2}` of the **same**
  order; `mu(T_l) ~ nu l^{3/2}`; `|{bad}| ~ l^2/nu`. Saturation:
  `c^4 G_l^{-3} ~ nu^4 (nu l^{-1/2})^{-3} = nu l^{3/2} = mu(T_l)`.
  **Verified.** All four dyadic sums converge, and `sum_k T_{l_k} < infinity`
  so the cascade completes in finite time, consistent with `T_* < infinity`.
  The note's labelling of this as bounded evidence and not a solution is
  correct and is respected here.
* **§5.3 — correct as a derivability statement.** `Q <= (1/3)||u||_3^3 <=
  (1/3)C_S^{3/2}E_0^{3/4}Y^{3/4}`; `g <= nu Y^{1/2} +
  C_S^{3/2}E_0^{1/4}Y^{3/4}`; the product has the two claimed sizes
  `nu E_0^{3/4}Y^{5/4}` and `C_S^3 E_0 Y^{3/2}` (both up to `1/3`), and
  neither `int Y^{5/4}` nor `int Y^{3/2}` is supplied by `prop:energy`; by
  `rem:mismatch` no supercritical time integral of `Y` follows. **Verified.**
  The reading of what Corollary 3.5 of `hf22-direct-attack.md` consumes
  (`Lambda A_Q` with `A_Q = int_0^tau Q`) is **correct**, so the substitution
  `|rho'| <= Lambda g` does indeed produce `int gQ`. The conclusion — the
  `mu`-modulus does **not** discharge (H-mod) — stands.

### 3.6 §5.4 table — six rows correct, one row false, one row upgraded

Row 2 ("modulus for `||q||_6` … Equivalent to a modulus for `sigma` in `L^2`")
is **false** by §2.1; it must read "controlled from above by a modulus for
`sigma` in `L^2`; the converse fails". Row 7 ("(C) itself | Undecided") is
**upgraded to decided** by §5 below. The other six rows are correct as
written, including the careful distinction in row 1 between the false general
implication and the undecided particular one.

---

## 4. REPLACEMENT ARGUMENT for Corollary 4.3

The following replaces Corollary 4.3 in full. It is proved here, it uses only
audited facts and the lane's own Theorem 4.1, and it still covers the bad set
of (G), so the lane's SURVIVING CONDITIONAL SUFFIX is preserved.

> **Corollary 4.3' (repaired).** Fix `eps in (0,1/2)` and `tau < min{H,T_*}`,
> and put
> `B_tau^{eps} := {t in (0,tau) : C_sharp d_1(t) > (1-2eps) nu}`,
> `U_tau := {t in (0,tau) : C_sharp d_1(t) >= (1-eps) nu}` and
> `B_tau := {t in (0,tau) : C_sharp d_1(t) > nu}` (the bad set of HF21-B
> Theorem 4.5). Then:
>
> 1. **(unconditional)**
>    `|B_tau^{eps}| <= 24 C_S^2 C_sharp^4 E_0^2 ((1-2eps) nu)^{-4} nu^{-1}`,
>    uniformly in `tau`;
> 2. **(under (C) for this `eps`, with input-only `Gamma`)** the number of
>    connected components of `B_tau^{eps}` that **meet `U_tau`** is at most
>    `1 + 8 Theta Gamma^3`;
> 3. `B_tau` is contained in the union of the components counted in 2.
>
> Consequently, under (C), the bad set of (G) is covered by at most
> `1 + 8 Theta Gamma^3` intervals of total measure at most the bound in 1.
> **No bound on the total number of components of `B_tau^{eps}` is claimed.**

*Proof.* **1.** `d_1 <= 2||u||_3` (`lem:quotient-coercive` upper half gives
`||w||_3 <= ||u||_3`, then `q = w-u`), so
`int_0^tau d_1^4 <= 16 int_0^tau ||u||_3^4 <= 16 (3C_S^2E_0^2/2nu) =
24 C_S^2E_0^2/nu` by `prop:scaling`(iii) \eqref{eq:L4L3}. Chebyshev at
exponent 4 at the level `(1-2eps)nu/C_sharp` gives
`|B_tau^{eps}| ((1-2eps)nu/C_sharp)^4 <= int_0^tau d_1^4`, i.e. the stated
bound. This is HF21-B Lemma 4.3 items 3–4 at a shifted level and uses no
hypothesis.

**2.** `d_1` is continuous on `[0,tau]` (`prop:localtheory`(iii) and `cor:Lq`
give `u in C([0,T];L^3)`; `lem:quotient-stability` \eqref{eq:cp-strong} gives
continuity of `u -> w(u)` on `L^3`), so `B_tau^{eps}` is open in `(0,tau)` and
its components are open intervals. Let `K_1, K_2, ...` be those components
that meet `U_tau`, ordered by left endpoint, and let `I` be the index set of
those `K_i` with `s_i := inf K_i > 0`; at most one component is excluded (the
one with `inf K_i = 0`).

For `i in I`: since `s_i` is a boundary point of a component of the open set
`{C_sharp d_1 > (1-2eps)nu}` inside `(0,tau)` and `d_1` is continuous,
`C_sharp d_1(s_i) = (1-2eps) nu`, so `s_i` is a **corridor time**. Pick any
`r_i in K_i cap U_tau`; then `C_sharp d_1(s_i) = (1-2eps)nu < (1-eps)nu <=
C_sharp d_1(r_i)`, so by the intermediate value theorem the set
`{t in [s_i,r_i] : C_sharp d_1(t) = (1-eps)nu}` is nonempty, and it is closed,
hence has a least element `t_i`; `t_i` is a **corridor time** as well, and
`t_i in K_i`. Thus `[s_i,t_i]` is a traversal in the sense of §4 (indeed both
endpoints sit exactly on the corridor walls), and by **(C)**
`G_i = ||grad u(s_i)||_2 + ||grad u(t_i)||_2 <= 2 Gamma`.

The intervals `[s_i,t_i]`, `i in I`, are contained in the pairwise disjoint
sets `closure(K_i)`, hence meet pairwise in at most one point; since `mu` has
the density `g in L^1_{loc}`, `sum_{i in I} mu([s_i,t_i]) <= mu([0,tau]) <= M`
still holds, which is all Theorem 4.1 uses. Corollary 4.2 with `Gamma -> 2
Gamma` gives `#I <= Theta (2Gamma)^3 = 8 Theta Gamma^3`, and adding the at
most one excluded component gives 2.

**3.** `B_tau subset U_tau` because `nu > (1-eps)nu`, and `B_tau subset
B_tau^{eps}`; so every point of `B_tau` lies in a component of `B_tau^{eps}`
that meets `U_tau`. `[]`

**What is lost relative to the note's Corollary 4.3.** Only the (unprovable)
claim about components that never reach the upper wall. Since those
components contain no point of `B_tau`, the reduction of (G) is unaffected:
the note's SURVIVING CONDITIONAL SUFFIX (i) is correct **verbatim** once
Corollary 4.3 is replaced by Corollary 4.3'.

---

## 5. THE DECISIVE QUESTION: the status of (C)

Recall

```
   (C)   there is an input-only Gamma = Gamma(nu,u_0,H,eps) < infinity with
         ||grad u(t)||_2 <= Gamma for every t < min{H,T_*} such that
         C_sharp d_1(t) in [(1-2eps)nu, (1-eps)nu].
```

The note's §5.1(2) is **correct**: the *unrestricted* form
`sup_{t<min{H,T_*}}||grad u(t)||_2 <= Gamma` gives, by
\eqref{eq:qdc-interp}, \eqref{eq:qdc-sobolev-field} and `prop:energy`,
`sup ||u(t)||_3 <= C_S^{1/2}E_0^{1/4}Gamma^{1/2}`, which is `hyp:critical`
verbatim, hence the Clay target by `thm:conditional`. Recomputed and
confirmed. In this programme "input-only" means, as `hyp:critical` states
explicitly, *finite* — the trajectory is a function of `(nu,u_0)`, so any
finite trajectory quantity is trivially a function of the data. (This is
exactly the reading used by `rem:highstrain-scope` and by
`hf22-direct-attack.md` Lemma R1.)

The audit's task was to decide whether the corridor restriction genuinely
escapes that circularity. **It does.** The following is proved here from the
audited record.

> **Proposition R1 (exact status of (C); new, proved here).** Fix `nu > 0`, a
> divergence-free Schwartz `u_0`, `0 < H < infinity` and `eps in (0,1/2)`.
> Then (C) holds **if and only if** at least one of
>
> (i) `H < T_*` (in particular whenever `T_* = infinity`);
> (ii) `T_* <= H` and there is `t_0 < T_*` with
>      `C_sharp d_1(t) > (1-eps) nu` for every `t in (t_0,T_*)`.
>
> Consequently `def:target` implies (C), but **(C) does not imply
> `def:target`**: alternative (ii) is a finite-time blow-up compatible with
> (C), and nothing in the audited record excludes it. (C) is therefore
> **not circular**, and is strictly weaker than `hyp:critical`,
> `hyp:highstrain` and `hyp:absorption`, each of which
> `rem:highstrain-scope` records as equivalent to global continuation.

*Proof.* Write `J := [0, min{H,T_*})` and
`Corr := {t in J : C_sharp d_1(t) in [(1-2eps)nu,(1-eps)nu]}`.

*(sufficiency).* Under (i), `[0,H]` is a compact subset of `[0,T_*)` and
`t -> ||grad u(t)||_2` is continuous there by `prop:localtheory`(iii), so
`Gamma := max_{[0,H]}||grad u||_2 < infinity` bounds `||grad u||_2` on all of
`J`, a fortiori on `Corr`. Under (ii), `min{H,T_*} = T_*` and
`Corr subset [0,t_0]`, again a compact subset of `[0,T_*)`, so
`Gamma := max_{[0,t_0]}||grad u||_2 < infinity` works.

*(necessity).* Suppose neither (i) nor (ii). From `not (i)`, `T_* <= H <
infinity`, so `T_* < infinity` and `J = [0,T_*)`.

First suppose `T_*` is **not** a limit point of `Corr`. Then there is
`t_0 < T_*` with `Corr cap (t_0,T_*) = empty`, i.e. `C_sharp d_1` maps the
interval `(t_0,T_*)` into the disjoint union of the two open sets
`(-infinity,(1-2eps)nu)` and `((1-eps)nu,infinity)`. `C_sharp d_1` is
continuous and `(t_0,T_*)` is connected, so its image lies in one of them.
The second alternative is exactly (ii), which is excluded. So
`C_sharp d_1(t) < (1-2eps) nu` for all `t in (t_0,T_*)`. Now by
`prop:quotient-evolution`, `Q' + nu D_Q = K` on every compact subinterval,
with `D_Q = D_3(w)` (HF18-A Theorem 2) and `|K| <= C_sharp d_1 D_3(w)`
(HF21-B Prop. 3.1). Hence on `(t_0,T_*)`

```
   Q'(t) <= (C_sharp d_1(t) - nu) D_Q(t) <= -2 eps nu D_Q(t) <= 0 ,
```

so `Q` is nonincreasing there and `Q(t) <= Q(t_0)` for `t in (t_0,T_*)`. By
`lem:quotient-coercive` \eqref{eq:cp-coercive}, `||u(t)||_3^3 <= 3
C_P^3 Q(t)`, so
`sup_{0<t<T_*}||u(t)||_3 <= max{ max_{[0,t_0]}||u||_3, (3C_P^3 Q(t_0))^{1/3} }
< infinity`, using continuity of `t -> ||u(t)||_3` on the compact `[0,t_0]`.
That is \eqref{eq:endpoint}, so `thm:continuation` gives `T_* = infinity`,
contradicting `T_* < infinity`.

Therefore `T_*` **is** a limit point of `Corr`: choose `t_n in Corr`,
`t_n -> T_*`. By `prop:localtheory`(v), `||u(t)||_{H^1} -> +infinity` as
`t -> T_*` — a genuine limit, not a limsup — and by `prop:energy`
`||u(t)||_2 <= ||u_0||_2`, so `||grad u(t_n)||_2 -> infinity`. Hence
`sup_{Corr}||grad u||_2 = infinity` and (C) fails.

*(consequences).* If `def:target` holds then `T_* = infinity > H`, i.e. (i),
so `def:target => (C)`. Conversely, alternative (ii) has `T_* < infinity` and
satisfies (C), and no statement in the audited record excludes a blow-up whose
distance stays above the upper corridor wall on a final interval — indeed
HF21-B Theorem 4.5(2) shows only that `Q` is nonincreasing **off**
`{C_sharp d_1 > nu}`, which places no obstruction there. `[]`

### 5.1 What Proposition R1 means for the lane

1. **The route is NOT retired.** (C) is a genuine hypothesis, not a disguise
   for the conclusion. Contrast `hyp:highstrain` (`rem:highstrain-scope`:
   equivalent to global continuation at the problem's quantifiers) and (H-mod)
   (`hf22-direct-attack.md` Lemma R1: implied by `T_* > H`, "its whole content
   lies in the branch `T_* <= H`"). (C) is implied by `T_* > H` *and* has
   content in the branch `T_* <= H` that is satisfiable there.
2. **But (C) is not refutable short of a blow-up construction**, exactly like
   (H-mod): by R1, a counterexample to (C) requires a finite-time singularity
   whose distance re-enters the corridor at times accumulating at `T_*`. So
   (C) is of the same *falsifiability* class as (H-mod), while being of a
   strictly weaker *logical* class.
3. **The conditional payoff is bounded, and R1 says exactly how.** In the
   blow-up branch, (C) is *equivalent* to alternative (ii), in which the bad
   set contains a terminal interval and Corollary 4.3'(2)'s count is
   automatically satisfied near `T_*`. What Corollary 4.3' adds over R1 is
   therefore only the **quantitative** count `1 + 8 Theta Gamma^3` over the
   whole of `[0,tau)`, including the part bounded away from `T_*` where `d_1`
   may still oscillate across the corridor many times. That is real, and it is
   not obtainable from R1 alone; but it is less than the note's framing
   suggests.
4. **The lane's stated FIRST GAP is correctly identified but should be
   re-stated.** Under R1, "prove (C)" is equivalent to "exclude alternative
   (ii)'s negation given blow-up", i.e. to proving: *if `T_* < infinity` then
   `C_sharp d_1` re-enters `[(1-2eps)nu,(1-eps)nu]` at times accumulating at
   `T_*`* — which is false to prove, since it is exactly what (C) forbids.
   The honest formulation of the gap is: **prove (C), i.e. prove that no
   blow-up has `C_sharp d_1 > (1-eps)nu` on a final interval.** This is a
   *sharper and more falsifiable* sub-question than the note's "an input-only
   upper bound for the enstrophy at corridor times", and it is the form the
   controller should record.

---

## 6. THE EXPONENT `1/4`

### 6.1 It cannot be raised inside the `(G,mu)` currency

Let `C G^alpha mu^beta` be any monomial candidate for a bound on
`|d_1(t')-d_1(t)|` with `C` an absolute constant. With
`||q||_3 ~ (a,lambda^{-1})`, `G ~ (a,lambda^{-1/2})`, `mu ~ (a,lambda^{-5/2})`,
the two scaling equations are

```
   alpha + beta = 1 ,        alpha/2 + 5 beta/2 = 1 ,
```

whose unique solution is `(alpha,beta) = (3/4,1/4)`. **The exponent `1/4` is
forced**, and no rearrangement of `G` and `mu` alone can raise it. This
confirms the note's §5.2(1) and **answers its second `needs review` bullet
negatively**: within the currency the lane defines, `beta = 1` is not merely
underivable, it is scaling-inadmissible.

The derivation is also exponent-rigid at the analytic level: the only bridge
from `mu` to a norm of `h` in the record is
`||h||_2^2 <= ||h||_{Hdot^1}||h||_{Hdot^{-1}}`, which is an equality for a
single-frequency `h`, so no improvement is available at that step either.

### 6.2 With `nu` and `E_0` admitted, `(3/4,1/4)` is no longer unique — §5.2(1) is slightly overstated

Admitting the remaining input scalars, a candidate
`C E_0^e nu^n G^alpha mu^beta` of weight `(a,lambda^{-1})` must satisfy

```
   2e + n + alpha + beta = 1 ,     3e + n + alpha/2 + 5 beta/2 = 1 ,
```

i.e. `e = alpha/2 - 3 beta/2` and `n = 1 - 2 alpha + 2 beta`. The lane's (3.5)
is `(alpha,beta,e,n) = (3/4,1/4,0,0)` and the old-tools (3.8) leading term is
`(5/8,1/8,1/8,0)` — both **verified** against these formulas. But `beta = 1`
is admissible with `alpha = 3`: then `e = 3/2 - 3/2 = 0` and
`n = 1 - 6 + 2 = -3`, giving the candidate `C G^3 mu nu^{-3}`. Along the §5.2 viscous-eddy
family, `G^3 mu nu^{-3} ~ (nu l^{-1/2})^3 (nu l^{3/2}) nu^{-3} = nu`, i.e. it
is **exactly saturated too**, indistinguishably from (3.5). So the family does
not discriminate between them, and §5.2(1)'s "No rearrangement of the same
ingredients does better" must be qualified to "**no monomial in `G` and `mu`
alone**". Note that a `G^3 mu nu^{-3}` modulus would give
`sum_i G_i^{-3} <= C M C_sharp/(eps nu^4)` — the same `G`-exponent with
`eps^{-1}` in place of `eps^{-4}`. It is not derivable from the record; it is
recorded here only to keep the sharpness claim honest.

### 6.3 The bullet's citation of the HF22 audit is a scope error

The note writes: "the audit of HF22-B recorded that an exponent above one is
refuted, and said nothing about exponents between `1/4` and `1`". Two
corrections.

* The audited correction ("Lipschitz **refutes** `alpha > 1`; an `alpha > 1`
  bound **forces** non-Lipschitz",
  `hf22-review-projection-regularity.md` §3.7, matching HF21 Lemma R2) is
  about the exponent `alpha` in `|K| <= C d_1^alpha D_3(w)` — a bound on the
  transport work — and about the `alpha > 3/2` refutation window. It is **not**
  about any modulus exponent, in `mu` or in `t`.
* HF22-B sub-question (b) is "is `u -> q(u)` Lipschitz in `L^3` at the
  nonlinear-Hodge class", i.e. the exponent `beta` in
  `||q(u+h)-q(u)||_3 <~ ||h||_3^beta`, for which the audited record supplies
  `beta = 2/3` unconditionally (Corollary A1) and the *negative* structural
  result that the rate `1/2` is not realised as `h -> 0` (Corollary A5, whose
  non-existence half is audited correct). That is a different exponent in a
  different variable from `beta` in `mu`.

The bullet should be replaced by §6.1–6.2 above.

---

## 7. CONDITIONAL SUFFIX THAT SURVIVES

Unchanged in substance, with Corollary 4.3 replaced by Corollary 4.3' and (C)
reclassified by Proposition R1:

> (i) If (C) holds for one `eps in (0,1/2)` with a finite `Gamma`, then
> Corollary 4.3' holds and (G) reduces — using the audited
> `hf22-good-set-dissipation.md` Theorem B, which makes the good set free —
> to a bound for `int_B ||q||_3 D_3(w) dt` over at most `1 + 8 Theta Gamma^3`
> intervals of total measure at most
> `24 C_S^2 C_sharp^4 E_0^2 ((1-2eps)nu)^{-4} nu^{-1}`.
>
> (ii) If in addition such a bad-interval bound is produced with an input-only
> constant, then (G) holds, hence `hyp:highstrain` with `theta = 0` and no
> cutoff (`rem:highstrain-normalisation`), hence `hyp:critical` by
> `prop:quotient-conditional`, hence `def:target` by `thm:conditional`.
>
> (iii) **New (Proposition R1):** (C) is implied by `def:target` and does not
> imply it; the whole content of (C) is the exclusion of blow-ups whose
> distance stays above `(1-eps)nu/C_sharp` on a final interval.

Neither (i)'s hypothesis nor (ii)'s is established here or in the note.

Also surviving, unconditionally and independently of (C):

* **Theorem 3.3** (the `mu`-modulus, `kappa_0 C_S^{1/2}G^{3/4}mu^{1/4}`), the
  first modulus in the record whose constant contains no supremum of a
  critical norm — **confirmed** against HF21-B Remark 2.2 and
  `hf22-direct-attack.md` block R-D;
* **Theorem 4.1** (`sum_i G_i^{-3} <= Theta`), a new unconditional constraint
  on the bad set that does not pass through the crossing measure;
* **Lemma 3.2** (`||u(t')-u(t)||_{Hdot^{-1}} <= mu([t,t'])` with
  `mu([0,tau]) <= M(nu,E_0,H)`), which is elementary, is not in the audited
  record as far as this audit could determine, and is the only input-only
  time-integrated statement about `d_t u` currently available;
* **Corollary 4.3'(1)**, the unconditional shifted-level measure bound;
* **§5.3**, the non-derivability of (H-mod) from the `mu`-modulus;
* **§5.2**, as bounded dimensional evidence for the method obstruction.

---

## 8. UNNECESSARY DEPENDENCIES

* **Prop. 2.1, Prop. 2.2, Remark 2.3 and the whole of §2** are unused by
  §§3–5. §2 is a scoping section; its false equivalence (§2.1 above) therefore
  does not propagate. It can be corrected in place without touching anything
  else.
* **`cor:quotient-budgets`, `cor:quotient-vorticity-zero`,
  `lem:quotient-mixed-pressure`, `lem:trace-control`** are listed in the
  lane's Inputs but are **not used** in any proof. `lem:trace-control` enters
  only through `prop:quotient-divcurl`, which is used.
* **`eq:cp-contraction`** is listed but not used; the modulus is built from
  \eqref{eq:cp-monotone} and \eqref{eq:cp-lipschitz} only (plus
  \eqref{eq:cp-strong} in the comparison Remark 3.4).
* **`hf23-divcurl-continuation.md`** is listed but nothing is drawn from it
  beyond what `prop:quotient-divcurl` already supplies in the manuscript.
* **The `Hdot^{-1}` Bochner framing** of Lemma 3.2 is replaceable by
  Minkowski's integral inequality, removing the need for the continuity
  argument entirely (§3.2).
* **Missing dependency (the converse problem):**
  `hf22-projection-regularity.md` and its review are load-bearing for
  Lemma 3.1 and are **absent** from the Inputs list.

---

## 9. NON-CLAIMS OF THIS AUDIT

No claim that (G), `hyp:highstrain`, `hyp:highpressure`, `hyp:absorption`,
`hyp:critical` or NS-R3 is true or false. No claim that (C) is true or false —
Proposition R1 characterises when it holds and shows it is not equivalent to
the conclusion; it does not decide it. No claim that Corollary 4.3's component
count is **false** for Navier–Stokes trajectories: §2.2 establishes only that
it is **not derivable** from the displayed ingredients and that its proof is
invalid. No claim that a `mu`-Lipschitz modulus is impossible: §6.2 exhibits a
scaling-admissible and family-saturated candidate; it is merely not derivable.
No manuscript edit is licensed by this audit. No priority or novelty is
claimed for Proposition R1 beyond "not located in the audited repository
record"; the numerics of §2.1 are bounded evidence and prove nothing. No file
other than this one is written; nothing is committed or pushed.

---

## 10. REOPENING CONDITION

This audit's verdict is reopened if any of the following is produced.

1. A proof or refutation of alternative (ii) of Proposition R1 for some datum
   — i.e. a demonstration that a finite-time singularity must, or need not,
   have `C_sharp||q(t)||_3 > (1-eps)nu` on a final interval. Either resolves
   (C) and with it the whole lane.
2. Any `tau`-uniform upper bound for `||grad u(t)||_2` at corridor times that
   is **not** obtained by exhibiting a compact set of corridor times, since
   Proposition R1 shows the compactness route is the only one available and it
   is equivalent to alternative (ii).
3. A derivation of a modulus of the form `C E_0^e nu^n G^alpha mu^beta` with
   `beta > 1/4` (necessarily `alpha = 3 - ...` per §6.2), which would
   strengthen Theorem 4.1 and change §5.2's saturation analysis.
4. A reverse bound `||sigma'-sigma||_2 <= C(...)||q'-q||_6` valid for the
   *particular* defect differences arising along the branch — §2.1 refutes the
   general implication only, and a trajectory-restricted version would restore
   a form of §2.1's equivalence.
5. A comparison between `int (|w|+|w'|)|h|^2` and `D_3(w)` carrying the factor
   `nu (t'-t)` identified in §3.1, which would turn Lemma 3.1's right side
   into a dissipation budget and reopen the first `needs review` bullet.
6. An audited result showing that infinitely many corridor-interior
   oscillations of `d_1` are excluded, which would restore the note's original
   Corollary 4.3 in its stronger form.

---

## 11. EXACT EDITS THE CONTROLLER SHOULD MAKE IF THIS VERDICT STANDS

**A. In `research/evidence/hf24-modulus-of-continuity.md`** (lane-owner edits,
each displayed above):

1. **§2.1.** Delete the redundant second display of Proposition 2.1. Retitle
   §2.1 "The defect determines `q` linearly, and the transfer is one-sided".
   Replace the sentence beginning "So **time regularity of `q` in `L^6` …**"
   by: "So `Hdot^1` regularity of `q` and `L^2` regularity of `sigma` are the
   same statement, with constant `1`; and `L^6` regularity of `q` follows from
   `L^2` regularity of `sigma` with constant `C_S`. The converse is **false**:
   for `sigma_n = cos(2 pi n x_1) phi`, `||sigma_n||_2` is bounded below while
   `||q_n||_6 = O(1/n)`." Repair the citation "Step 4 of `cor:quotient-defect`"
   to "the cutoff paragraph at the end of Step 5 of `prop:quotient-divcurl`".
2. **§2 Conclusion of Part (1).** "controls `t -> ||q(t)||_6` exactly" ->
   "controls `t -> ||q(t)||_6` from above".
3. **§3.1.** Retitle Lemma 3.1 "(weighted stability; = HF22-B Theorem A and
   Corollary A1, audited PASS)". Delete "new". Add to Inputs:
   `research/evidence/hf22-projection-regularity.md` §2 (Theorem A,
   Corollary A1) and `research/evidence/hf22-review-projection-regularity.md`
   §3.1–3.2. Add the audit's two recording remarks (the free discarded term;
   the two-point nature of the weight). State explicitly that the **new** step
   is pairing the weight against `||w||_6` rather than `||w||_3`.
4. **§3.1, first `needs review` bullet.** Replace by the scaling computation
   of §3.1 above: the two weighted quantities differ by `lambda^{-2}`, and the
   only scaling-admissible comparison carries the factor `nu (t'-t)`.
5. **Remark 3.4.** Correct (3.8)'s second constant from `1` to `3`. Replace
   "contrary to what HF22-C §6 and `hf22-direct-attack.md` §3 record as the
   obstruction" by "refining what … record as the obstruction, which is
   `tau`-uniformity and is untouched here".
6. **Remark 4.5.** `2^8` -> `4^8`, or add "keeping only the leading term of
   (3.8)".
7. **§4.** Replace Corollary 4.3 in full by **Corollary 4.3'** of §4 above,
   with its proof, splitting item 1 out as unconditional. Update §6 CLAIM 6
   and the SURVIVING CONDITIONAL SUFFIX (i) accordingly ("at most
   `1 + 8 Theta Gamma^3` components **that meet the upper corridor wall**,
   which cover `B_tau`").
8. **§5.1.** Insert **Proposition R1** with its proof, and replace §5.1(3) by
   its consequences: (C) is implied by `def:target`, does not imply it, is not
   circular, and its whole content is the exclusion of a final-interval
   blow-up above the upper wall. Restate the FIRST GAP in that form.
9. **§5.2(1).** Qualify "No rearrangement of the same ingredients does better"
   to "no monomial in `G` and `mu` alone", and record the
   `G^3 mu nu^{-3}` candidate of §6.2.
10. **§5.4 table.** Row 2: "Equivalent to" -> "Controlled from above by
    (converse false, §2.1)". Row 7: "Undecided" -> "Not circular; characterised
    by Proposition R1; undecided in the branch it isolates".
11. **§6 second `needs review` bullet.** Replace by §6.1–6.3: the exponent
    `1/4` is scaling-forced in the `(G,mu)` currency; the cited HF22 correction
    concerns `alpha` in `|K| <= C d_1^alpha D_3(w)`, not a modulus exponent.
12. Add the audit banner: `AUDITED 2026-09-06: REPAIR, repairs applied` with a
    pointer to this file.

**B. In `PLAN.md`, §"HF24: modulus of continuity and the bad-set restriction"**
(controller edits):

13. Change "(UNAUDITED)" to "(`hf24-modulus-of-continuity.md` AUDITED: REPAIR;
    `hf24-badset-restriction.md` still unaudited)".
14. Replace the sentence "the lane records that the unrestricted form of that
    bound is the critical hypothesis verbatim, hence circular, so the corridor
    restriction is the whole distance between its hypothesis and its
    conclusion" by: "the audit decides the question the lane left open: the
    corridor restriction **does** escape the circularity. The restricted
    hypothesis is implied by the Clay conclusion and does not imply it; it
    holds precisely when the horizon is short or when a blow-up keeps the
    distance above the upper corridor wall on a final interval. It is
    therefore strictly weaker than the critical hypothesis, and unlike the
    high-strain hypothesis it is not of the existential-equivalence class,
    though like (H-mod) it cannot be refuted short of a blow-up construction."
15. Add: "The crossing count the lane claimed was corrected by the audit: only
    the components that reach the upper corridor wall are counted, which is
    what the bad set needs; components that oscillate inside the corridor are
    not countable from the record."
16. Add to the same section: "The lane's weighted stability lemma duplicates
    the audited HF22-B Theorem A; the novelty is the pairing of that weight
    against the new `L^6` bound, which is what improves the currency exponent
    from one eighth to one quarter."
17. In "**Convergence again.**", refine the shared question: it is not
    "is the enstrophy bounded by input data on the set of times far from the
    nonlinear-Hodge class" but, per Proposition R1, "must a finite-time
    singularity re-enter the corridor at times accumulating at the singular
    time" — the two are equivalent for HF24-A and the second is the falsifiable
    form.

**C. Manuscript.** None. No edit to `../navier-paper/main.tex` is licensed by
this audit.

---

## 12. FRONTIER RECORD

**MODE / RESULT:** proof-audit. **REPAIR**, with the decisive question of the
lane **decided in the lane's favour** and two displayed claims corrected.

**CLAIM AND SCOPE OF THIS AUDIT.** For the maximal classical branch of
`prop:localtheory` at arbitrary `nu > 0` and arbitrary divergence-free
Schwartz datum: Theorem 3.3, Theorem 4.1, Corollary 4.2 and Lemma 3.2 of
HF24-A are correct as displayed, with all constants and scaling weights
recomputed; Lemma 3.1 is correct but is the audited HF22-B Theorem A;
Proposition 2.1's claimed equivalence is false and is refuted by an explicit
family; Corollary 4.3's component count is not derivable and is replaced by
the proved Corollary 4.3'; and hypothesis (C) is characterised exactly by
Proposition R1, which shows it is implied by, but does not imply, the Clay
conclusion.

**FIRST BAD BRIDGE.** §2.1's "the transfer is an equivalence" (first in
document order, not load-bearing); §4's Corollary 4.3 component count (first
in the load-bearing chain).

**FIRST GAP AFTER THE REPAIR.** Unchanged in location, sharpened in form:
prove (C), equivalently prove that no finite-time singularity of the classical
branch has `C_sharp||q(t)||_3 > (1-eps)nu` on a final interval `(t_0,T_*)`.

**NON-CLAIMS.** As §9.

- needs review: Proposition R1's alternative (ii) is a new, precisely posed
  and falsifiable-in-principle sub-question — "can a singularity keep the
  distance to the nonlinear-Hodge class above the upper corridor wall on a
  final interval?" — and it has not been attacked by any lane. It is not
  equivalent to `hyp:critical`, and HF21-B Theorem 4.5(2) places no obstruction
  on that branch.
- needs review: the `G^3 mu nu^{-3}` candidate of §6.2 is scaling-admissible
  and saturated by the §5.2 family exactly like (3.5), and would improve the
  `eps`-dependence of `Theta` from `eps^{-4}` to `eps^{-1}`. Whether any route
  in the record produces it has not been examined.
- needs review: Lemma 3.2 (`Hdot^{-1}` bounded variation of the velocity) is
  elementary, appears not to be in the record, and was not tested against any
  other estimate in the programme; the audit confirms it but did not search
  for further consumers.
