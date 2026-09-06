# Audit of HF22-B: `hf22-projection-regularity.md`

**MODE: proof-audit. VERDICT: REPAIR.** 2026-09-06.

Owned file: `research/evidence/hf22-review-projection-regularity.md`. Nothing
else in the repository is edited and nothing is committed. No result is
promoted; the manuscript is untouched. No HIGH-PRESSURE, HIGH-STRAIN, CRITICAL
or NS-R3 result is asserted here, and the first gap (G) is not closed by
anything in the target or in this audit.

## 0. Frozen target

| Object | Freeze |
|---|---|
| Target | `research/evidence/hf22-projection-regularity.md`, sha256 `aca699e3bb9e3b810d50612074a582c8fc9c5615b0c457b9a8e50773ac2d659f` |
| Repository HEAD | `e36fec455e970a004519e5c91b856a3e1bba28bc` (`main`, clean) |
| Manuscript | `../navier-paper` HEAD `4084330f6b8130241c7afbde3878861229c4cceb`, `main.tex` sha256 `7a59b9cb3b3178c44da978f403f6397c7c44cd6a863429549b13280dddfe8671` |

Audited background used as premises, each within the scope the brief grants:
the manuscript `sec:quotient` displays (`lem:cubic-pointwise`
\eqref{eq:cp-lipschitz}, \eqref{eq:cp-taylor}, \eqref{eq:cp-monotone};
`lem:cubic-frechet`; `lem:quotient-minimizer`(a)–(d); `lem:quotient-scaling`;
`lem:quotient-stability`; `prop:quotient-derivative`; `rem:no-monotone`), the
repaired HF21-A (`hf21-shifted-hodge-regularity.md` Theorem 2, Corollary 2.1,
Corollary 2.2, Theorem 6', §6.2), the repaired HF21-B
(`hf21-crossing-sign-structure.md` §§1.1–1.3, §3, and its review's Lemmas
R1–R4), and HF18-B (`hf18-divergence-speed-link.md` §2.5, §2.6) at headline
level. HF23 is **not** used, and no step of this audit assumes (H1), (H2), or
any regularity of the minimizer beyond `L^3` membership.

---

## 1. VERDICT

**REPAIR.** The mathematical core of the note is correct and survives the
audit in full:

* **Theorem A is proved.** Reconstructed from the first nontrivial implication
  and recomputed line by line, its three steps are exactly right, its constant
  is right, its quantifiers are right, it uses no regularity of the minimizer,
  no solenoidality, no HF18-B item, and no (H1)-type hypothesis. It is
  unconditional for all `u,h in L^3(R^3;R^3)`.
* **Corollaries A1–A4 are proved**, with one citation to repair (D6) that does
  not touch the mathematics; the exponent `2/3` is correct and is strictly
  better than the audited `1/2` at every base point.
* **Corollary A5's non-existence claim is proved**, with the quantifiers
  checked; one clause of it is false as stated and is repaired below (D1).
* **The new lattice row (`alpha > 3/2` refuted) is correct** under exactly the
  three hypotheses the audited HF21 review Lemma R2 uses, one of which
  (uniform `D_3(w(v_eps))`) the note correctly flags as unaudited. The
  endpoint `alpha = 3/2` is correctly left open. The direction of the
  Lipschitz dichotomy is stated correctly, matching the audited correction.
* **The route-level conclusion is correct**: (G) is untouched, and the size
  route's ceiling is confirmed rather than removed.

Six defects are found. One is a bad bridge that carried into `PLAN.md`; five
are over-statements, mis-citations or a reversed sentence. None invalidates
Theorem A or any corollary of it. All six have displayed repairs.

| # | Location | Defect | Class |
|---|---|---|---|
| **D1** | §3 Corollary A5, echoed in §0(c) and §7 (B) | "a witness for the failure of Lipschitz continuity must have `beta in [2/3,1)`" — the proof supports only `beta >= 2/3`; `beta = 1` with a divergent subpolynomial factor is non-Lipschitz and is not excluded | claim stronger than its proof (first defect in document order; supports nothing) |
| **D2** | §4.3, second display and the sentence after it | **FIRST BAD BRIDGE.** The residual `L^3` estimate is asserted to be "an instance of exactly the class of weighted inequalities recorded as open in HF18-B", whence "sub-question (b) is not independent of the HF18-B gap: it inherits it". Neither the instance relation nor the inheritance is established, and the HF18-B item invoked carries a hypothesis ((H1)) the target does not assume | unsupported bridge; propagated to `PLAN.md` |
| **D3** | §4.4 headline and §7 claim (D) | "the kernel is **provably** not a source of non-Lipschitz behaviour" — the displayed argument minimises over a *subspace* of `G_3` and says nothing about the coupled minimiser | claim stronger than its proof |
| **D4** | §5, last paragraph | "`d_1` at `M` is now known to be `o(eps^{1/2})`-small, i.e. the good set near `M` is *smaller* … which strengthens the crossing-measure statement's inputs" — sign reversed, and no strengthening follows | reversed statement + unsupported consequence |
| **D5** | §0, §4.2, §7 claim (D) | "Lax–Milgram-invertible … with **exactly the constant of Theorem A**" — the constants are `sqrt2` and `2`, and the compared objects differ; also `B` is only a *semi*-inner product before quotienting | arithmetic/technical over-statement |
| **D6** | §2 Corollary A4 proof; §3 admissibility bullet; §7 FIRST GAP and SURVIVING SUFFIX | citation of `hf21-crossing` Prop. 1.2 (stated for *solenoidal* `u`) at the possibly non-solenoidal point `U+h`; use of HF21-A Theorem 2 without its `C^1` hypothesis; two unjustified "equivalently"s | scope/citation |

---

## 2. REVIEWED SCOPE

Reconstructed and recomputed in full, from the first nontrivial implication:

1. §1.1–§1.3: the audited stability estimate, its proof mechanism, and the
   diagnosis of where `1/2` comes from.
2. §2: Theorem A and Corollaries A1, A2, A3, A4, including finiteness of every
   pairing, both flagged steps (the pointwise comparison `|z| <= S` and the
   Cauchy–Schwarz step in `L^2(S dx)`), the scaling consistency claim, and the
   comparison with `eq:cp-strong`.
3. §3: Corollary A5 with its quantifiers, the admissibility bullet, the
   `rem:no-monotone` bullet.
4. §4.1–§4.4: the linearisation algebra, the boundedness and Lax–Milgram
   statements, the kernel computation, the `L^3`-invertibility claim, the
   identification of the residual with HF18-B, and the homogeneity argument.
5. §5: the lattice, its three hypotheses against the audited Lemma R2, the new
   row's derivation, both conditional refinements, and the (G) paragraph.
6. §6, §7 and the Appendix: non-claims, cycle output, and the reproducibility
   of both probes.

Independent numerical work done for this audit (evidence, never proof):
`400` adversarially seeded finite-dimensional instances (varying cell count,
gradient-subspace dimension, cells driven to `10^{-6}`, `h` concentrated where
`|w|` is smallest, `||h||_3` over seven decades): `0` violations of Theorem A,
of `||z||_3^3 <= N^2`, of Corollary A1, or of the cancellation identity; worst
observed `N^2/(4M_h^2) = 0.449`, worst `||z||_3^3/(4W||h||_3^2) = 0.152`. The
note's `chk.py` was re-run verbatim: `failures: 0`, reproducible. The note's
`chk3.py` configuration was re-run and extended by placing `h` **inside** the
vanishing block (the note places it outside): `||z||_3/eps` is `0.9965 ->
1.00000` across `eps in [10^{-2},10^{-6}]`, i.e. rate exactly `1` there too.
All of this nominates Lipschitz behaviour in the finite-dimensional model and
proves nothing about `R^3`.

---

## 3. What survives, verified

### 3.1 Theorem A: correct as stated

For `u,h in L^3`, `w = w(u)`, `w' = w(u+h)`, `z = w'-w`, `S = |w|+|w'|`,
`N^2 = int S|z|^2`, `M_h^2 = int S|h|^2`. All are finite: `S in L^3` by
`lem:quotient-minimizer`(b) and Minkowski, `|z|^2, |h|^2 in L^{3/2}`, Hölder.

*Step 1 (cancellation).* `w(v) = v + q(v)` with `q(v) in G_3`
(`lem:quotient-minimizer`(b)), so `z - h = q(u+h) - q(u) in G_3` because `G_3`
is a linear space. `lem:quotient-minimizer`(c) applied to **both** minimizers
gives `<A, z-h> = <A', z-h> = 0`, hence `<A'-A, z> = <A'-A, h>`. Both pairings
are finite (`A, A' in L^{3/2}`, `z, h in L^3`). **Correct**, and it is the
same cancellation the manuscript's own proof of `eq:cp-strong` uses — no new
input, no derivative of the minimizer, no circularity.

*Step 2 (lower bound).* \eqref{eq:cp-monotone} is an **identity**, not an
estimate: `(j(a)-j(b))·(a-b) = (|a|+|b|)( (1/2)(|a|-|b|)^2 + (1/2)|a-b|^2 )`.
With `a = w'(x)`, `b = w(x)` the integrand is pointwise nonnegative and equals
`S( (1/2)(|w'|-|w|)^2 + (1/2)|z|^2 ) >= (1/2)S|z|^2`. Integration is legitimate
(nonnegative integrand; the integral equals the finite pairing `<A'-A,z>`).
So `<A'-A,z> >= N^2/2`. **Correct.** This is the step the note diagnoses
correctly in §1.3: the manuscript's `eq:cp-F-monotone` discards the weight
`|a|+|b|` in favour of `|a-b|`, which is equality only in the antiparallel
regime; keeping the weight is the whole gain, and the diagnosis is right.

*Step 3 (upper bound, the two flagged steps).* Both flagged steps are correct.
`|A'-A| <= S|z|` a.e. is \eqref{eq:cp-lipschitz} verbatim with `a = w'(x)`,
`b = w(x)`. `S dx` is a nonnegative measure (`S >= 0` measurable), so
Cauchy–Schwarz in `L^2(S dx)` applies to the pair `(|z|, |h|)`:
`<A'-A,h> <= int |A'-A||h| <= int S|z||h| <= N M_h`, all three quantities
finite. **Correct.**

Combining, `N^2/2 <= N M_h`, so `N <= 2M_h`, i.e.
`int (|w|+|w'|)|w'-w|^2 <= 4 int (|w|+|w'|)|h|^2`. **Theorem A stands.**

Two remarks the note does not make and which the controller should record.
(i) The full identity gives the *stronger* `int S(|w'|-|w|)^2 + N^2 <= 4M_h^2`;
the discarded term is free. (ii) The statement is a **two-point** inequality:
the weight `S` depends on both `u` and `u+h`, so "Lipschitz in the weighted
`L^2` norm" (§0) is a figure of speech, not a Lipschitz property of a map
between two fixed normed spaces. §2 states it correctly; §0 should not be read
as more.

### 3.2 Corollary A1 and the exponent `2/3`: correct

`|z| = |w'-w| <= |w'|+|w| = S` pointwise (the first flagged step), so
`int|z|^3 = int |z|^2|z| <= int S|z|^2 = N^2 <= 4M_h^2 <= 4||S||_3 || |h|^2 ||_{3/2}
= 4W||h||_3^2` by Hölder with exponents `3, 3/2`. Hence
`||z||_3 <= (4W)^{1/3}||h||_3^{2/3}`, `W <= 2||w||_3+||h||_3` by
\eqref{eq:cp-contraction} and Minkowski, and
`||q(u+h)-q(u)||_3 <= ||z||_3 + ||h||_3`. **Correct.**

Scaling: under `u -> D_lambda u`, `w(D_lambda u) = D_lambda w(u)`
(`lem:quotient-scaling`), and each of `N^2`, `M_h^2`, `W||h||_3^2` is invariant
(change of variables, `D_lambda` an `L^3` isometry); under `u -> alpha u` both
sides are homogeneous of degree `3`. **Verified on both parameters.**

Comparison with the audited `eq:cp-strong`: with `R := ||w||_3+||h||_3` and
`W <= 2R`, the ratio of the A1 bound to the `eq:cp-strong` bound is at most
`(8R)^{1/3}||h||_3^{1/6}/(2R^{1/2}) = (||h||_3/R)^{1/6} <= 1`. So A1 is
**always at least as strong**, with equality only at `||w||_3 = 0`. The note's
sentence "strictly stronger for all `||h||_3 < 4(||w||_3+…)` … never weaker by
more than `4^{1/3}`" is garbled but errs on the conservative side; it should
simply be replaced by the computation just given (see E5b).

### 3.3 Corollaries A2, A3, A4: correct, one citation to repair

A2 and A3 are immediate and were recomputed. A3's last clause, `d_1(v) <=
C(||v||_3) dist_{L^3}(v,M)^{2/3}` locally, is correct via near-minimisers of
the distance (no attainment needed) — verified.

A4 is correct. Cleanly: `Q(U+h)-Q(U)-<j(U),h> = [F(U+h)-F(U)-<j(U),h>] -
d_2(U+h)` since `d_2 = F - Q` and `d_2(U) = 0`, `Q(U) = F(U)`, `A(U) = j(U)`
for `U in M`. The bracket is `O(||h||_3^2)` by \eqref{eq:cp-F-taylor}, and
`d_2(U+h) = O(||h||_3^{4/3})` by A3. **D6 applies to the route, not the
result**: the note obtains the bound `d_2(v) <= (||w(v)||_3+||q(v)||_3)
||q(v)||_3^2` by citing `hf21-crossing` Prop. 1.2, whose statement is
restricted to *solenoidal* `u`, while `v = U+h` need not be solenoidal. The
inequality is nevertheless true at every `v in L^3`, and the repair is to cite
the manuscript directly (E7): `d_2(v) = int B(w,-q)` by
`lem:quotient-minimizer`(c) (which needs no solenoidality), and `B(a,d) <=
(|a|+|d|)|d|^2` is \eqref{eq:cp-taylor}; integrate and apply Hölder.

**Auditor by-product** (proved here, not in the note; not load-bearing, not
promoted): the same route improves the audited \eqref{eq:cp-continuity}
exponent as well. From `|A'-A| <= S|z|` and Cauchy–Schwarz with exponents `2,2`
on `int S^{3/2}|z|^{3/2}`,
```
   ||A'-A||_{3/2} <= W ||z||_3 <= 4^{1/3} W^{4/3} ||h||_3^{2/3},
```
against the manuscript's `4(||w||_3+||h||_3)^{3/2}||h||_3^{1/2}`. Better for
small `h`, and it is the natural companion of A1.

### 3.4 Corollary A5: the non-existence claim is correct; one clause is not (D1)

*The non-existence part is proved and its quantifiers check out.* Suppose
`u in L^3`, `h_n -> 0` in `L^3`, `h_n != 0`. Then `W_n <= 2||w(u)||_3+||h_n||_3`
is bounded, so `||z_n||_3/||h_n||_3^{1/2} <= (4W_n)^{1/3}||h_n||_3^{1/6} -> 0`,
contradicting `>= c > 0`. So no base point and no null sequence realises the
rate `1/2`, and the falsifier arm's assigned target **provably does not
exist**. This is a genuine negative structural result and it is correctly
scoped: it is a statement about `h_n -> 0`, not about large `h`, where
`eq:cp-strong` remains the better bound. One pedantic gap: as literally
written the statement is false for the trivial sequence `h_n = 0` (both sides
vanish); add `h_n != 0` (E2).

*The second clause is false as stated (D1).* "A witness for the failure of
Lipschitz continuity must have `beta in [2/3,1)`" does not follow, and is not
true, under the note's own ansatz `||z||_3 = ||h||_3^{beta+o(1)}`: the map
`||z||_3 = ||h||_3 log(1/||h||_3)` has `beta = 1` and is not Lipschitz. The
proof paragraph proves only `beta >= 2/3`; the upper end is asserted. Repair
in §4.2 below. Note that the *conditional* version in §5 — under an `alpha>1`
lattice bound the rate is forced into `[2/3,1/alpha] subset [2/3,1)` — **is**
correct, because there the strict upper bound comes from the lattice
hypothesis and not from "non-Lipschitz".

### 3.5 §4.1, §4.2 and the kernel statements: correct as formal statements

`Dj(v)[zeta] = |v|(zeta + v^(v^·zeta))`, so `a = |U|(I + U^ ⊗ U^)` with
eigenvalues `|U|` (twice) and `2|U|`, and `|U|I <= a <= 2|U|I`: **recomputed,
correct**. `(LIN)` is the correct formal linearisation of
`div(j(U+eps h+q_eps)) = 0` at `eps = 0`. Boundedness of `B` and of the datum
functional: correct (Hölder `3,3,3`). Lax–Milgram: correct in substance, with
the technical caveat of D5 — `B` is a *semi*-inner product on
`{grad phi : phi in C_c^inf}` (it annihilates gradients supported in the
interior of `{U=0}`), so `H_U` is the completion of the **quotient**, its
elements are equivalence classes and need not be gradient fields; the
resulting `grad phi` cannot be compared to `q_eps` without an extra argument.
Kernel: `B(phi,phi) = 0` iff `grad phi = 0` a.e. on `{U != 0}`, and
`ker L_U|_{G_3}` is nontrivial whenever `{U=0}` has nonempty interior, since
`grad phi` for `phi in C_c^inf` of that interior lies in `G_3` and is nonzero.
**Correct.** Hence the `L^3` non-invertibility at every compactly supported
`U in M` is correct.

### 3.6 §5: the lattice row is correct

Hypotheses. (i) `|K(v_eps)| >= c_0 eps` for `eps <= (||U||_3^3/(2C_*))^2`:
follows from `rem:no-monotone`'s two-sided display
`|K(U+eps h) + eps||U||_3^3| <= C_*|eps|^{3/2}` — **verified against the
manuscript**. (ii) `Q(v_eps) >= q_0 > 0`: follows from
\eqref{eq:cp-continuity} and `Q(U) = ||U||_3^3/3 > 0` — **verified,
unconditional**. (iii) `D_3(w(v_eps)) <= D` uniformly in `eps`: **assumed, not
audited**, and the note says so, correctly, in three places; the audited
Lemma R2 assumes exactly the same, so the new row is no weaker.

Derivation. `L(alpha)` with `alpha > 1` and (ii) gives
`Q^{(1-alpha)/3} <= q_0^{(1-alpha)/3}`; with (i) and (iii),
`c_0 eps <= C' d_1(v_eps)^alpha`. By A3, `d_1(v_eps) <= C eps^{2/3}` (the
`+ eps` term of A3 is lower order), so `c_0 eps <= C'' eps^{2alpha/3}`, which
fails as `eps -> 0` exactly when `2alpha/3 > 1`, i.e. `alpha > 3/2`. The
endpoint `alpha = 3/2` is **correctly left open** (there the powers match and
only constants compete). **The row is correct**, and the window `(1,2] ->
(1,3/2]` is right.

Direction of the dichotomy: the note states it in the corrected HF21 direction
(Lipschitz **refutes** `alpha > 1`; an `alpha > 1` bound **forces**
non-Lipschitz), matching the audited Lemma R2 items 1–2. **Correct.**

Route conclusion: (G) is the `alpha = 1` statement integrated in time and is
untouched; the size route's ceiling is confirmed. **Correct.**

---

## 4. FIRST BAD BRIDGE

### 4.1 D2 (§4.3): the residual is not an HF18-B item, and (b) is not shown to inherit HF18-B's gap

The note writes, of the estimate

```
   || grad phi ||_3 <= C(U) || h ||_3   for   -div(a grad phi) = div(a h),
   a = |U|(I + U^ ⊗ U^),
```

that it "is an instance of exactly the class of weighted inequalities recorded
as **open** in HF18-B", and concludes: "So sub-question (b) is not independent
of the HF18-B gap: it inherits it." **This bridge does not hold.** `PLAN.md`
already carries the conclusion ("the same open item class as HF18-B. So (b) is
not independent of an already-open question"), so the defect has propagated.

What HF18-B actually records as OPEN (`hf18-divergence-speed-link.md` §2.5,
§2.6, read directly): the weighted Calderón–Zygmund inequality

```
 (W)   int |w| |grad (I-S_L) P w|^2 dx  <=  C int |w| |grad w|^2 dx
       for  w in M ∩ (H1),
```

the `L^2` projection bound `||w(u)||_2 <= C||u||_2`, the negative-moment item
`int |w|^{-1} Pi_L^2 < infinity`, and two monomial families that reduce to the
`L^2` projection bound. Compare with the note's residual:

| | HF18-B (W) | HF22-B §4.3 residual |
|---|---|---|
| exponent | weighted `L^2` on both sides | **unweighted `L^3`** on both sides |
| operator | a Fourier multiplier (`(I-S_L)P`) applied to `w` | the **solution operator** of a degenerate divergence-form equation |
| unknown | the minimizer `w` itself, one point | the **linearised response** to a perturbation, a two-point object |
| hypothesis | presupposes **(H1)** | assumes no regularity |
| weight | `|w|` on both sides | `|U|` inside the operator, **absent from both norms** |

The residual is therefore not an instance of (W), nor of any other item on the
HF18-B open list; and no implication in either direction between the two is
displayed anywhere in the note or derivable from the audited record. Worse,
(W) is a **conditional** item: it is stated for `w in M ∩ (H1)`. Invoking it
as the residual of a question that assumes no regularity is precisely the use
of a conditional HF18-B item outside its hypothesis that the audit brief
singles out. The note's own §6 non-claim ("§4.3 asserts only that Lipschitz
continuity … *reduces to* an estimate of that class") is the correct hedge for
the taxonomy, but it does not license the dependency conclusion in §4.3's last
sentence, which is a claim about the *logical* relation between two open
questions.

A second, independent weakness of the same sentence: the reduction it reports
is **formal**. §4 derives `(LIN)` by writing `q_eps = eps grad phi + o(eps)`,
which presupposes differentiability of `eps -> q(U + eps h)` in `L^3` at
`eps = 0` — exactly the object whose regularity is in question. The note's own
non-claims say `(LIN)` is not justified. So "Lipschitz continuity … reduces to
the weighted Calderón–Zygmund estimate" is at best "the formal linearisation's
solution operator is `L^3`-bounded iff …", and even the `iff` requires the
justification. §7 claim (D) does carry the hedge "modulo justifying the
linearisation"; §4.3's prose drops it.

**Non-derivability, not falsity.** Nothing here asserts that the two questions
are unrelated — only that no relation has been shown, so the routing
conclusion may not be drawn. Distinguishing the two is the point: the note may
say the residual *resembles* HF18-B's items; it may not say (b) inherits their
gap.

### 4.2 The other five defects, with their repairs

**D1 (§3, §0(c), §7(B)).** Replace
"a witness for the failure of Lipschitz continuity must have `beta in [2/3,1)`"
by:

> and any witness for the failure of Lipschitz continuity has
> `beta in [2/3,1]`, where `beta = 1` is possible only through a divergent
> subpolynomial factor (e.g. `||z||_3 ≍ ||h||_3 log(1/||h||_3)`, which is
> non-Lipschitz with `beta = 1`). The strict upper bound `beta < 1` is
> available only in the *conditional* form of §5, where it is forced by an
> assumed `alpha > 1` lattice bound and not by non-Lipschitz behaviour alone.

**D3 (§4.4, §7(D)).** The displayed argument minimises
`F(U+eps h+grad phi)` over the **subspace** `{grad phi in G_3 : grad phi = 0
a.e. off Omega_0}`, on which the increment is jointly `3`-homogeneous in
`(eps h, grad phi)` and the restricted minimiser scales exactly like `eps`.
That is correct, and so is the second bullet's balance `eps^2 t` against `t^3`
as a heuristic. But `G_3` admits no decomposition into "supported in `Omega_0`"
and "supported off `Omega_0`" summands, so the restricted minimiser is not the
restriction of the true minimiser `q_eps`, and nothing about the coupled
problem follows. Replace the headline claim by what is proved:

> The kernel does not produce the `eps^{1/2}` mechanism: Corollary A1 bounds
> `||z||_3` by `C eps^{2/3}` globally, hence on `Omega_0` as well, so no
> `eps^{1/2}`-amplitude exterior excursion is available. Restricted to the
> kernel block *in isolation* the problem is exactly `1`-homogeneous and its
> minimiser scales exactly like `eps`. Whether the coupled minimiser inherits
> that rate is **open**: `G_3` does not split along `Omega_0`.

Delete "provably" from §7 claim (D).

**D4 (§5, last paragraph).** A3 makes `d_1` *smaller* near `M`, hence the good
set `{C_# d_1 <= nu}` *larger*, not smaller; and no strengthening of the
crossing-measure bound follows, because that bound consumes
`int_0^tau d_1^4 dt` along a **trajectory**, which A3 does not control (the
trajectory need not remain in an `L^3`-neighbourhood of `M`, and A3 is a
statement about perturbations of a fixed `U in M`). Replace the sentence by:

> The one new leverage point is that `d_1` is `o(eps^{1/2})` on
> `L^3`-neighbourhoods of `M`, so the sublevel sets `{d_1 <= delta}` extend
> further from `M` than the audited record allowed. This does **not** improve
> the crossing-measure bound, which consumes `int_0^tau d_1^4 dt` along a
> trajectory and is not controlled by a neighbourhood statement, and it does
> not remove obstruction O3.

**D5 (§0, §4.2, §7(D)).** The Lax–Milgram bound reads
`(int |U||grad phi|^2)^{1/2} <= B(phi,phi)^{1/2} <= (2 int |U||h|^2)^{1/2}`,
constant `sqrt2`; Theorem A's linear shadow at `U in M` is
`int 2|U| |h + grad phi|^2 <= 4 int 2|U||h|^2`, constant `2`, and the two
bound different objects (`grad phi` versus `z ≍ eps(h + grad phi)`). Replace
"with exactly the constant of Theorem A" by "with constant `sqrt2` against
Theorem A's `2`, on the related but distinct quantity `grad phi` rather than
`z`; the agreement is qualitative — both are bounded in the field-weighted
`L^2` norm with an absolute constant — and it is a consistency check, not an
identity of constants". Add, in §4.2, that `B` is a semi-inner product and
`H_U` is the completion of the quotient by its null space.

**D6 (§2 A4 proof; §3 admissibility bullet; §7).** (a) Cite
`lem:quotient-minimizer`(c) and \eqref{eq:cp-taylor} directly for
`d_2(v) <= (||w(v)||_3+||q(v)||_3)||q(v)||_3^2`, instead of `hf21-crossing`
Prop. 1.2 whose statement is restricted to solenoidal `u`. (b) The
admissibility bullet must carry HF21-A Theorem 2's hypothesis: the rigidity
statement applies to `A` that is **`C^1` on a neighbourhood of the zero**, so
the correct sentence is "any witness *constructed by the standard route* — a
solenoidal `A' in C^1 ∩ L^{3/2}` from which `w' = |A'|^{-1/2}A'` is read off —
must have every zero of `A'` degenerate", which is exactly HF21-A
Corollary 2.2's own scope. It is not a constraint on arbitrary minimizers,
whose `C^1` regularity is the open question. (c) Delete the two
"equivalently"s in §7 (`FIRST GAP`: the `L^q` higher-integrability route is a
*sufficient* alternative, not an equivalent; `SURVIVING CONDITIONAL SUFFIX`:
the weighted estimate implies `L^3`-Lipschitz only through the unjustified
linearisation).

---

## 5. REPLACEMENT ARGUMENT (for D2, the first bad bridge)

Replace §4.3's second display, the paragraph after it, and the closing
sentence, by the following. It keeps everything that is proved and deletes only
the dependency claim.

> **The literal answer to the lane's item (2).** The linearised operator
> `L_U : G_3 -> G_3^*`, `L_U(grad phi)(grad psi) = int a grad phi · grad psi`,
> has `ker L_U|_{G_3} = {grad phi in G_3 : grad phi = 0 a.e. on {U != 0}}`,
> which is nontrivial whenever `{U = 0}` has nonempty interior — in particular
> at **every compactly supported `U in M`**, including the azimuthal swirl of
> `rem:no-monotone`. At a `U in M` with `|U| > 0` a.e. the kernel is trivial,
> and the `L^3`-boundedness of the solution operator of `(LIN)` is the estimate
> ```
>    || grad phi ||_3 <= C(U) || h ||_3,
>    -div(a grad phi) = div(a h),  a = |U|(I + U^ ⊗ U^),  |U| in L^3.
> ```
> Equivalently, since `(LIN)` unconditionally admits the weighted energy bound
> `int |U| |grad phi|^2 <= 2 int |U| |h|^2` (Lax–Milgram, §4.2 — the linear
> shadow of Theorem A), the estimate is a **higher-integrability gain from the
> degenerate energy space `L^2(|U|dx)` to `L^3`** for a divergence-form
> operator whose coefficient matrix degenerates like `|U| in L^3` — a weight
> that is neither bounded, nor bounded below, nor `A_2`.
>
> **This is a new open item, and its relation to HF18-B is not known.** It is
> *not* an instance of HF18-B's open weighted Calderón–Zygmund inequality (W):
> (W) is a weighted-`L^2` bound for a Fourier multiplier applied to the
> minimizer itself and presupposes (H1), whereas the estimate above is an
> unweighted-`L^3` bound for the solution operator of a degenerate elliptic
> equation and assumes no regularity. No implication in either direction
> between the two has been displayed, here or in the audited record.
> Consequently **sub-question (b) is not shown to inherit the HF18-B gap**, and
> the lane must not be recorded as dependent on it. What is true is only the
> taxonomic statement: both are questions about singular integrals with a
> weight built from the field itself, and neither is reachable from `A_p`
> theory. Separately, HF21-A §6.2 records that the single-minimizer
> Caccioppoli inequality (Theorem 6') cannot start a Gehring iteration; that
> obstruction is stated for a different object (the minimizer of a fixed
> datum, under (0.1)) and is not known to apply to the two-point inequality
> proved here — as the note's own NEXT DISTINCT ACTION correctly observes.
>
> **Route consequence, corrected.** Sub-question (b) ends at a *named new*
> external input, which is neither the HF18-B pair nor the (H1)/(H2) question.
> Whether the size-route ceiling and the regularity question are governed by
> one scalar weighted-elliptic item is an open question, not a finding.

With this replacement, §4 asserts only what it proves and the lane's honest
summary is: *(b) is undecided; its residual is a new, precisely stated
degenerate-elliptic higher-integrability question; its independence from
HF18-B is open in both directions.*

---

## 6. Prior-art flag (not a defect; controller obligation before any promotion)

The note makes no novelty claim, correctly. The controller should nevertheless
record, before any manuscript promotion of Theorem A or Corollary A1, that the
mechanism is the standard **`V`-function two-point monotonicity estimate** of
`p`-Laplacian regularity theory at `p = 3`: with `V(v) = |v|^{(p-2)/2}v`
(here `V = |w|^{1/2}w`, the very field the audited HF18-A already uses),
`(j(a)-j(b))·(a-b) ≍ |V(a)-V(b)|^2 ≍ (|a|+|b|)^{p-2}|a-b|^2`, and the argument
of §2 is the textbook continuous-dependence proof for `A(xi) = |xi|^{p-2}xi`.
It generalises verbatim: for `p >= 2`,
`||z||_p^p <= int S^{p-2}|z|^2 <= 4 int S^{p-2}|h|^2 <= 4||S||_p^{p-2}||h||_p^2`,
i.e. Hölder exponent `2/p`, which is `2/3` at `p = 3`. This audit did **not**
open the literature, so this is an unverified prior-art flag, not a
non-novelty finding; it must be checked against the `p`-Laplace
continuous-dependence literature (Giaquinta; Diening–Ettwein; Kuusi–Mingione)
before Theorem A is described anywhere as new. It also *raises* confidence in
correctness: the estimate is a known-shaped object correctly specialised.

---

## 7. CONDITIONAL SUFFIX THAT SURVIVES

Everything below stands after the repairs, with its hypotheses displayed.

1. **Unconditional, no hypothesis at all** (`u,h in L^3` only): Theorem A;
   Corollaries A1, A2, A3, A4; the auditor by-product
   `||A'-A||_{3/2} <= 4^{1/3}W^{4/3}||h||_3^{2/3}`; Corollary A5's
   non-existence statement with `h_n != 0`, i.e. **the falsifier arm's
   assigned target provably does not exist and item (3) of the brief is
   answered negatively by proof**; and `beta >= 2/3` for any power-law rate.
2. **Conditional on (i)–(iii) of the audited Lemma R2** (of which only (iii),
   `D_3(w(v_eps)) <= D` uniformly, is unaudited): `L(alpha)` is refuted for
   `alpha > 3/2` on the `rem:no-monotone` family; the open window is
   `alpha in (1,3/2]` with the endpoint included; any surviving `alpha > 1`
   forces `d_1(v_eps) >~ eps^{1/alpha}` with `1/alpha in [2/3,1)`, i.e. forces
   the projection to be non-Lipschitz at `M` and to nearly saturate A1.
3. **Conditional on `q` being `L^3`-Lipschitz at `U in M` and on (i)**:
   `alpha = 1` is sharp and no `alpha > 1` member of the lattice exists (this
   is the audited Lemma R2 item 2, unchanged).
4. **Formal, and flagged as such**: `(LIN)`; its Lax–Milgram solvability in the
   weighted energy space; the kernel computation and the `L^3`
   non-invertibility at compactly supported `U in M`; the identification of the
   `|U|>0`-a.e. residual with a degenerate-elliptic higher-integrability
   estimate. Not conditional on HF18-B, and not shown to depend on it.
5. **Unchanged**: (G) is untouched; the size route's ceiling is confirmed, not
   removed; the standing verdict "(G) needs the time-integrated cancellation
   inside `K`" stands.

---

## 8. UNNECESSARY DEPENDENCIES

* **HF18-B is not a dependency of anything in the note** and should be removed
  from its premise surface. It appears only in §4.3, where it is
  mis-identified (D2). Theorem A and every corollary use only `sec:quotient`
  displays.
* **HF21-A (shifted-Hodge) is not a dependency of any displayed result.** It
  supports only the §3 admissibility bullet, which is a recorded constraint on
  hypothetical future witnesses and supports no step.
* **`hf21-crossing` Prop. 1.2 is not needed** for Corollary A4 (E7 replaces it
  with two manuscript displays), and its use at a non-solenoidal point is out
  of its stated scope.
* **§4 is not a dependency of §2, §3 or §5.** The note states this and the
  audit confirms it: Theorem A, A1–A5 and the lattice row never differentiate
  the minimizer and never mention `(LIN)`.
* **The numerics are load-bearing nowhere.** Both probes reproduce; both are
  finite-dimensional counting-measure instances; the note says so.
* **HF23 is not used**, correctly, and no step of the note assumes (H1) or
  (H2). This is a genuine strength: Theorem A is the first quantitative
  improvement in this lane that is independent of the open regularity
  hypothesis.

---

## 9. NON-CLAIMS OF THIS AUDIT

* No claim that `u -> q(u)` is or is not Lipschitz at `M`. The lane's question
  remains undecided and this audit does not decide it.
* No claim that the §4.3 residual estimate is true, false, easy, or hard; only
  that it is not shown to be an HF18-B item and that (b) is not shown to
  inherit HF18-B's gap. Non-derivability of the dependency, not falsity of it.
* No claim about (H1), (H2), (W), the `L^2` projection bound, or HF23.
* No claim that Theorem A is new. §6 is a prior-art *flag* requiring a
  literature check, not a non-novelty finding.
* No claim that hypothesis (iii) (uniform `D_3(w(v_eps))`) holds or fails.
* The numerics of §2 above are bounded evidence at finite dimension and finite
  precision; they nominate and never prove. Nothing in this audit rests on
  them: every verdict is a closed-form recomputation of a displayed step.
* No result is promoted, no manuscript edit is licensed by this audit, and (G)
  is not closed.

---

## 10. REOPENING CONDITION

The REPAIR verdict on the core (Theorem A, A1–A4, A5's non-existence half, the
lattice row) reopens only if \eqref{eq:cp-monotone}, \eqref{eq:cp-lipschitz} or
`lem:quotient-minimizer`(b),(c) is itself withdrawn, or if a base point `u` and
a null sequence `h_n != 0` in `L^3` is exhibited with
`||w(u+h_n)-w(u)||_3 > (4W_n)^{1/3}||h_n||_3^{2/3}`.

D2 reopens — and the note's original §4.3 sentence becomes licensable — as soon
as **either** an implication is displayed, in either direction and with matching
hypotheses, between
`||grad phi||_3 <= C(U)||h||_3` for `-div(a grad phi) = div(a h)` and one of
HF18-B's OPEN items ((W), or `||w(u)||_2 <= C||u||_2`), **or** the
linearisation `(LIN)` is justified (differentiability of
`eps -> q(U+eps h)` in `L^3` at `eps = 0`, which would also upgrade §4.3's
"reduces to" from formal to actual). Until one of those is displayed, the lane
is recorded as ending at a **new** open item.

D1, D3, D4, D5, D6 close on application of the edits below; none of them can
reopen the core.

---

## 11. EXACT EDITS THE CONTROLLER SHOULD MAKE IF THIS VERDICT STANDS

All in `research/evidence/hf22-projection-regularity.md` unless stated.

* **E1.** Prepend an audit-status block: "**AUDIT STATUS (2026-09-06).**
  Independently audited: `hf22-review-projection-regularity.md`, **VERDICT:
  REPAIR**. Theorem A and Corollaries A1–A5 survive unchanged; six defects
  (D1–D6) are repaired below; the first bad bridge was §4.3's identification of
  the residual with an HF18-B open item and the inference that sub-question (b)
  inherits the HF18-B gap, both of which are withdrawn."
* **E2.** §3 Corollary A5: insert `h_n != 0` into the hypothesis.
* **E3.** §3 Corollary A5, §0 (c), §7 CLAIM AND SCOPE (B): apply the D1
  replacement text of §4.2 above (`beta in [2/3,1]`, with the `log`
  counterexample and the note that `beta < 1` is available only conditionally).
* **E4.** §4.3: replace the second display, the paragraph after it, and the
  closing "So sub-question (b) is not independent…" sentence by the block
  displayed in §5 above, verbatim.
* **E5a.** §4.4 headline bullet and §7 claim (D): apply the D3 replacement
  text; delete "provably".
  **E5b.** §2, after Corollary A2: replace the "strictly stronger … never
  weaker by more than `4^{1/3}`" sentence by "With `R := ||w||_3+||h||_3` and
  `W <= 2R`, the ratio of the A1 bound to the `eq:cp-strong` bound is
  `(||h||_3/R)^{1/6} <= 1`: A1 is at least as strong at every `u,h`, strictly
  so unless `||w||_3 = 0`."
* **E6.** §5 final paragraph: apply the D4 replacement text.
* **E7.** §2 Corollary A4 proof: replace the citation of `hf21-crossing` §1.2
  by "`d_2(v) = int B(w(v),-q(v))` by `lem:quotient-minimizer`(c), and
  `B(a,d) <= (|a|+|d|)|d|^2` is \eqref{eq:cp-taylor}; integrate and apply
  Hölder — no solenoidality of `v` is used, which matters because `U+h` need
  not be solenoidal."
* **E8.** §3 admissibility bullet: apply the D6(b) scope repair (the rigidity
  constraint binds witnesses *constructed* from a `C^1` solenoidal `A`, per
  HF21-A Corollary 2.2, not arbitrary minimizers).
* **E9.** §0, §4.2, §7 (D): apply the D5 repair (constants `sqrt2` vs `2`;
  `B` a semi-inner product; `H_U` the completion of the quotient).
* **E10.** §7: delete the two "equivalently"s (FIRST GAP, SURVIVING
  CONDITIONAL SUFFIX) per D6(c); restate FIRST GAP as "a **new** open item: an
  `L^3` higher-integrability estimate for the degenerate operator
  `-div(|U|(I+U^⊗U^) grad ·)`, not known to be related to the HF18-B items".
* **E11.** Append to `## Open Questions`:
  - `- needs review: prior art for Theorem A — it is the p=3 case of the
    standard V-function two-point monotonicity estimate of p-Laplacian
    regularity theory, and the 2/p Hölder exponent for the solution map is
    standard there; check the literature before describing it as new or
    promoting it to the manuscript.`
  - `- needs review: whether the §4.3 residual estimate is related to HF18-B's
    (W) or to the L^2 projection bound in either direction; the audit found no
    implication and recorded the residual as a new open item.`
* **E12.** `PLAN.md`, "HF22" section, sub-question (b) bullet: replace "its
  residual is identified as one named external input, the weighted
  Calderón–Zygmund estimate, which is the same open item class as HF18-B. So
  (b) is not independent of an already-open question." by "its residual is
  identified as one named external input: an `L^3` higher-integrability
  estimate for the degenerate elliptic operator `-div(|U|(I+U^⊗U^) grad ·)`.
  The audit (`hf22-review-projection-regularity.md`) found this is **not** an
  HF18-B item and that no implication either way has been shown, so (b) ends
  at a **new** open question, independent of HF18-B on the present record.
  Unconditionally, the lane proves the two-point weighted estimate
  `int (|w|+|w'|)|w'-w|^2 <= 4 int (|w|+|w'|)|h|^2`, hence Hölder exponent
  `2/3` for the projection, hence that no family realises the rate `1/2`, and
  hence — under the audited Lemma R2's three hypotheses — that the lattice
  window narrows from `alpha in (1,2]` to `alpha in (1,3/2]`."
* **E13.** `PLAN.md`, "Ordered next actions" item 5: the list of open items
  should record, beside "the weighted Calderon-Zygmund and `L^2`-projection
  questions recorded in HF18-B", the new and separate item "an `L^3` gradient
  estimate for the degenerate operator `-div(|U|(I+U^⊗U^) grad ·)` at
  `U in M`, the residual of HF22-B".
* **E14.** No manuscript edit is licensed. Corollary A1 (exponent `2/3` in
  `lem:quotient-stability`), Corollary A4 (remainder `4/3` in
  `prop:quotient-derivative` at `M`), and the auditor by-product
  (`||A'-A||_{3/2} <= 4^{1/3}W^{4/3}||h||_3^{2/3}`, improving
  \eqref{eq:cp-continuity}) are all correct and all *candidates*; they must
  clear E11's prior-art check before promotion, and the manuscript's existing
  statements are correct upper bounds, so nothing there is erroneous.

---

## 12. Cycle output

**VERDICT:** REPAIR. Theorem A, its corollaries, the falsifier arm's negative
result, and the lattice row all survive; the dependency claim on HF18-B does
not.

**FIRST BAD BRIDGE:** §4.3 — "an instance of exactly the class of weighted
inequalities recorded as open in HF18-B … So sub-question (b) is not
independent of the HF18-B gap: it inherits it." (D1, in §3, is the first
*defect* in document order but is a terminal mis-statement supporting nothing.)

**EVIDENCE:** closed-form recomputation of every step of §§1–5 against
`main.tex` at `4084330f`; the audited Lemma R2 and `rem:no-monotone` read
directly; HF18-B §2.5–§2.6 read directly and tabulated against the residual;
`400` adversarial finite-dimensional instances with `0` violations; the note's
`chk.py` re-run verbatim (`failures: 0`) and its `chk3.py` configuration
re-run and extended — all numerics bounded evidence, none load-bearing.

**REPLACEMENT ARGUMENT:** §5 above, replacing §4.3 in full.

**CONDITIONAL SUFFIX THAT SURVIVES:** §7 above.

**UNNECESSARY DEPENDENCIES:** §8 above — HF18-B, HF21-A and `hf21-crossing`
Prop. 1.2 are all removable from the note's premise surface.

**NON-CLAIMS:** §9 above.

**REOPENING CONDITION:** §10 above.
