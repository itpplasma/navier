# HF22-A: is the quotient dissipation at most the velocity dissipation?

**AUDITED: REPAIR** (`hf22-review-dissipation-comparison.md`, 2026-09-06);
repairs applied by the controller, 2026-09-06.

The independent audit returns **REPAIR**. It reconstructed §§1-4 rather than
read them, and certifies them: Lemma 1.1, Propositions 1.2-1.3, Lemma 2.3,
Proposition 2.4, Corollaries 2.5-2.7, Lemmas 3.1-3.2 (within their declared
conditional scope), Lemma 3.3, Proposition 3.4, Corollary 3.5 and Lemma 3.6 all
survive; the negative answer to sub-question (a) stands; the third derivation
of the audited HF19-D identity (3.3) is real and reproduces it exactly,
constant and power included (the auditor added a fourth route); the inversion
is a bijection onto the nonlinear-Hodge class as claimed; and the constant `2`
of the unconditional bound is correct. The **first bad bridge** is §5,
consequence 2, with its headline in MODE/RESULT item 6: the claim that an
affirmative answer to (a) would **not** have closed (G), because it would only
have moved (G) onto the pressure route. The audit finds three independent
defects there -- (D1) a dropped factor `||q||_3`, so that the two spacetime
integrals compared do not even carry the same amplitude weight
(`(a^4,lambda^0)` against `(a^3,lambda^0)`); (D2) the one-way implication
"an input-only bound for `int D_3(u)` is *exactly* `hyp:absorption`" read as a
biconditional; and (D3) non-derivability along one route read as falsity of the
whole branch. The controller has **replaced** that consequence by the audit's
weaker repaired form -- Lemma R1, Proposition R2, Corollary R3 with their
proofs -- rather than patching it, and has applied the audit's narrowings and
cosmetic items: the pointwise-replacement claim is narrowed to constant `1`
(the constant-`C` replacement is question (C1), open); the first-order
differentiation of the merely-`L^3` minimizer in §2.1 is deleted; Corollary
3.5's "is equivalent to" is narrowed to "restricts to"; Proposition 2.4 carries
the sign convention; the MODE/RESULT item 2 notation clash is fixed; the
optional dependency reductions are taken; and the novelty of Lemma 3.6 is
narrowed to its weighted middle form, the outer form being the audited HF18-A
Theorem 2 (2.3). Nothing in §§0-4 changed in substance, and nothing downstream
depended on the bad bridge. The FIRST GAP is unchanged and is not closed. (G),
HIGH-STRAIN, HIGH-PRESSURE and NS-R3 remain open; no result here is a
producer, and the numerics below are bounded evidence, never proof.

Lane HF22-A, sub-question (a) of the attack on (G), **MODE: DISCOVER with a
falsifier arm**, 2026-09-06. Owned file:
`research/evidence/hf22-dissipation-comparison.md`. Nothing else in the
repository is edited; nothing is committed; the manuscript is untouched and no
node is promoted.

**Inputs** [DI]: `PLAN.md` ("Beyond the checkpoint" l.222-250, "Frontier
packet" l.247-280, "HF18" l.888-921, "HF19" l.924-956, "HF20" l.957-1005,
"Ordered next actions" l.1006-1051, "HF21" l.1052-1119).
`../navier-paper/main.tex` at the working tree read today, `sec:quotient`
(l.4841): `lem:quotient-minimizer` (l.5118), `lem:gradient-closure` (l.5221),
`lem:leray` (l.5264),
`lem:quotient-coercive` (l.5454), `lem:quotient-scaling` (l.5478),
`lem:quotient-heat` (l.5518), `lem:quotient-stability` (l.5590),
`prop:quotient-derivative` (l.5650), `rem:quotient-scope` (l.5710),
`lem:quotient-pressure` (l.5953), `lem:quotient-chainrule` (l.5996),
`lem:heat-generator` (l.6126), `def:qe-dissipation` (l.6216),
`lem:quotient-heatsign` (l.6229), `rem:qe-heatsign-scope` (l.6258),
`lem:quotient-transport` (l.6545), `prop:quotient-evolution` (l.6698),
`rem:qe-evolution-scope` (l.6740), `rem:distance-balance` (l.6768),
`lem:quotient-lowstrain` (l.6786), `hyp:highstrain` (l.6843),
`rem:highstrain-normalisation` (l.6875), `prop:quotient-conditional` (l.6901),
`rem:highstrain-scope` (l.6953), `rem:no-monotone` (l.6983); outside that
section `def:D3P3` (l.2677), `prop:pressure` with \eqref{eq:pressure-balance}
and \eqref{eq:D3P3-bounds} (l.2799), `prop:scaling` with \eqref{eq:L4L3}
(l.2227), `hyp:absorption` with \eqref{eq:absorption} (l.3652, l.3656), and
\eqref{eq:quotient-gap} (l.6857). Read but cited by statement only, not
re-derived: `prop:localtheory` (l.1195), `lem:upgrade` (l.674), `prop:energy`
(l.2164), `prop:lowpressure` (l.3492), `hyp:highpressure` (l.3638) [MO].
Evidence notes [DI]: `hf19-difference-functional.md` (**audited REPAIR,
repairs applied**; §0, §1, §3 Lemma 3.1, Theorem 3.2, Propositions 3.3-3.4,
Corollary 3.5, §4.1) and its audit `hf19-review-difference-functional.md`
(VERDICT block l.24-31, checklist l.45-51, l.186-201, l.472-494: §§1-3
reconstructed independently, identity (3.3) re-derived twice and confirmed
exactly); `hf18-hodge-regularity.md` and `hf21-shifted-hodge-regularity.md`
§4 l.640-670 for the audited facts quoted in §0 below; HF18-A
`hf18-hodge-regularity.md` Corollary 1(d) (1.11) and Theorem 2 (2.1)-(2.3) and
§4 item 3, quoted by statement [DI]. This lane's own audit
`hf22-review-dissipation-comparison.md` (VERDICT **REPAIR**; REPLACEMENT
ARGUMENT R1-R3; EXACT EDITS 1-10), applied throughout [DI].

---

## MODE / RESULT

**DISCOVER. The lane question is answered: NO. `D_3(w) <= D_3(u)` is false at
fixed time, and so is its reverse; both directions were already settled
negatively in the audited `hf19-difference-functional.md` §3, whose decisive
computation this lane re-derives independently and confirms exactly. Four new
exact results are added -- item 5 only in its weighted middle form, its
Hölder'd form being the audited HF18-A Theorem 2 (2.3) -- and none of them is a
producer.**

1. **Answer to (a): no.** For solenoidal Schwartz `u` neither
   `D_3(w) <= D_3(u)` nor `D_3(w) >= D_3(u)` holds; both signs occur along a
   single heat trajectory (audited: HF19-D Theorem 3.2, Propositions 3.3-3.4,
   Corollary 3.5). The affirmative branch the lane statement hoped for does
   not exist, so no term may be deleted from `rem:distance-balance` and the
   quotient dissipation is not the smaller quantity.
2. **Independent verification (new).** Lemma 2.3 identifies the object that
   HF19-D differentiates as `N(v) := div(Dj(v) Lap v)`, the divergence of the
   linearised cubic flux, and proves `d/ds|_0 (v_s . grad |v_s|^2) = 2|v| N(v)`
   on `M`. Proposition 2.4 computes `N` in closed form for the elliptic-swirl
   class in the Frenet/eikonal frame by a route different from both of the
   auditor's: `N = -2 b^2 kappa kappa_s`. Composed with Lemma 2.3 this is
   exactly HF19-D (3.3), `R = -4 kappa_0 kappa_{0,t} phi^3 / J^4`
   (`kappa_0, kappa_{0,t}` the base-curve quantities of HF19-D; §2 below uses
   `kappa, kappa_s` for the *level-curve* quantities `kappa_0/J` and
   `kappa_{0,t}/J^3`, so the two notations differ by `J^{-4}`), including the
   constant. This is a third independent derivation of that identity -- an
   independent *computation* of the same quantity by a different route and
   frame, not an independent proof of a different statement (audit, (E1) at
   Corollary 2.5).
3. **Equality on `M`, and the equality set is strictly larger (new).**
   `q=0` gives `w=u` and `D_3(w)=D_3(u)` trivially. Proposition 1.3 proves
   that the converse fails: on the elliptic-swirl heat trajectory there is a
   time `s*` with `D_3(w(v_{s*})) = D_3(v_{s*})` and `v_{s*}` not in `M`. So
   the two dissipations agree on a strictly larger set than `M`, and equality
   is not a defect-detector.
4. **Exact inversion of the minimizer map (new, Proposition 3.4).** The map
   `B |-> w = |B|^{-1/2} B` is a bijection from solenoidal `B in L^{3/2}` onto
   the nonlinear-Hodge fields `{w in L^3 : div(|w|w)=0}`, and `u = P w`,
   `q = (I-P) w` recovers the velocity and the defect **exactly**, with no PDE
   solve and no perturbation. Every admissible pair `(u, w(u))` arises this
   way. The comparison of the lane question therefore has a fully
   minimizer-free form (Corollary 3.5), and the opaque nonlinear projection
   defect `q(u)` becomes the *linear* Helmholtz gradient part of an explicit
   algebraic function of a free solenoidal field.
5. **Weighted unconditional bound (Lemma 3.6).**
   `D_3(w) <= 2 int |w| |grad u|^2 <= 2 ||w||_3 ||grad u||_3^2
   <= 2 ||u||_3 ||grad u||_3^2`, scaling-consistent, minimizer-free on the
   right after Hölder, and exactly the extension to `w` of the manuscript's own
   \eqref{eq:D3P3-bounds} `D_3(u) <= 2 int |u| |grad u|^2`, with the same
   constant `2`. Only the **weighted middle form** is new: the outer form
   `D_3(w) = D_Q(u) <= 2||w||_3||grad u||_3^2` is the audited HF18-A Theorem 2
   (2.3), and is cited here, not claimed.
6. **What it changes (§5).** The negative answer closes the class of attacks
   on (G) that replace `D_3(w)` by `D_3(u)` pointwise in time **with constant
   `1`**; the replacement up to a finite constant is question (C1) of §4 and
   remains open. It also shows the affirmative branch would not by itself have
   been a shortcut: the majorant it supplies is the velocity-side spacetime
   quantity `int ||u||_3 D_3(u) dt`, which is not the pressure-route quantity
   `int D_3(u) dt` (different amplitude weight, and `||u||_3` is input-bounded
   only in time-integrated form), while an input-only bound on
   `int D_3(u) dt` is, at these quantifiers, equivalent to global continuation
   -- the same status `rem:highstrain-scope` records for `hyp:absorption`.
   Whether some other use of an affirmative (a) would close (G) is **not
   decided** (audit, replacement Corollary R3; the pre-audit version of this
   item asserted the stronger negative and was the first bad bridge).
7. **Open, honestly (§4).** Whether `D_3(w) <= C D_3(u)` or
   `D_3(u) <= C D_3(w)` holds with some finite `C>1` is not settled here;
   `C=1` is refuted for both. Neither is refuted by scaling. An explicit
   witness with all quantities computed is not delivered: the audited
   counterexample is an existence argument through the mean value theorem, and
   the inversion of item 4 reduces an explicit witness to two integrals and one
   Leray projection but I did not evaluate them.

HIGH-STRAIN and HIGH-PRESSURE remain open; (G) is untouched; NS-R3 remains
open. No novelty or priority is claimed for anything below.

---

## 0. Objects, conventions, audited inputs

`(u,p)` is the classical branch of `prop:localtheory` on a compact
`[0,T] subset [0,T_*)` with the regularity package (R1)-(R3) used throughout
`sec:quotient`; at a *fixed* time everything below is a statement about one
smooth solenoidal field with all derivatives in every `L^r`, `2<=r<=oo`. Write
`j(z)=|z|z`, `f(z)=|z|^3/3` (so `grad f = j`, `f` convex),
`F(v)=(1/3)||v||_3^3`, `Dj(z) = |z| I + z (x) z/|z|` (symmetric, eigenvalues
`|z|,|z|,2|z|`, Lipschitz in `z`), `G_s = e^{s Lap}`, `P` the Leray projection
(`lem:leray`), `G_3` the closed `L^3` gradient space (`def:quotient`(a)).

Audited and used without re-proof:

* (Q1) `w = w(u) = u + q(u)` is the unique `L^3` minimizer of `F` over
  `u + G_3`; `A = |w|w in L^{3/2}` and `div A = 0` in `D'`
  (`lem:quotient-minimizer`(a)-(c)). For solenoidal `u`, `P w = u` and
  `q = w - P w` (`lem:quotient-coercive`).
* (Q2) `D_Q(u) := -<A, Lap u> >= 0` (`def:qe-dissipation`,
  `lem:quotient-heatsign`), and `D_Q(u) = D_3(w) = int(|grad V|^2 -
  (1/9)|grad|V||^2)` with `V = |w|^{1/2} w in H^1(R^3)` and
  `A = |V|^{1/3} V in W^{1,3/2}(R^3)` (HF18-A Theorem 2, audited PASS; quoted
  in HF19-D §0 l.87-89).
* (Q3) `D_3(u) = int(|u||grad u|^2 + |(grad u)^T u|^2/|u|)` (`def:D3P3`
  \eqref{eq:D3-def}) `= int(|u||grad u|^2 + |u||grad|u||^2)
  = -<j(u), Lap u> = int(|grad V_u|^2 - (1/9)|grad|V_u||^2)`, `V_u=|u|^{1/2}u`
  (HF19-D Lemma 2.1, audited; the pointwise algebra is checked again in §1).
* (Q4) `M = {v in L^3 : div(|v|v)=0 in D'}`; a solenoidal `v` lies in `M` iff
  `q(v)=0` iff `w(v)=v`; for smooth solenoidal `v`,
  `div(|v|v) = v . grad|v|`, so `v in M` iff the speed is constant along the
  streamlines of `v` (HF18-B Prop. 1.4, audited; HF19-D §0).
* (Q5) `Delta(u) := F(u) - Q(u) >= 0`, `= 0` iff `u in M` (for solenoidal
  `u`); `(1/6)||q||_3^3 <= Delta <= (||w||_3+||u||_3)||q||_3^2` (HF19-D §1,
  audited). This is the distance functional of the lane statement.
* (Q6) `curl w = curl u` in `D'` (HF21-A Theorem 1, audited after the
  rank-stratified repair); `grad V = 0` a.e. on `{V=0}` (HF21-A Prop. 4.1).
* (Q7) `int_0^tau ||u||_3^3 dt` is input-bounded, by \eqref{eq:L4L3} and
  Hölder in time (`rem:highstrain-normalisation`).

Scaling bookkeeping (amplitude `a`, dilation `lambda`, as in HF18-B §0):
`Q, F, Delta, ||q||_3^3 ~ (a^3, lambda^0)`; `D_3(u), D_3(w) ~ (a^3,
lambda^2)`; `int|w||grad u|^2 ~ (a^3, lambda^2)`. Both sides of the lane
question therefore have the same weight, and a comparison with a dimensionless
constant is scaling-consistent -- which is why the question had to be decided
by content, not by scaling.

---

## 1. The two objects, and equality on `M`

**Lemma 1.1 (four forms of `D_3`; pointwise algebra).** For a `C^1` field `g`
with the `def:D3P3` convention that the integrands vanish on `{g=0}`, and with
`V_g = |g|^{1/2} g`:
```
 |(grad g)^T g|^2/|g| = |g| |grad |g||^2 ,
 |grad V_g|^2 = |g||grad g|^2 + (5/4)|g||grad|g||^2 ,
 (1/9)|grad|V_g||^2 = (1/4)|g||grad|g||^2 ,
```
so that pointwise `|grad V_g|^2 - (1/9)|grad |V_g||^2 = |g|(|grad g|^2 +
|grad|g||^2)`, which is the `def:D3P3` integrand; integrating and integrating
by parts once gives `D_3(g) = -<j(g), Lap g>` for decaying `g`.

*Proof.* `((grad g)^T g)_k = g_i partial_k g_i = |g| partial_k |g|` gives the
first line. `partial_k (V_g)_i = |g|^{1/2} partial_k g_i +
(1/2)|g|^{-1/2}(partial_k|g|) g_i`; squaring and summing, the cross term is
`sum_k (partial_k|g|) g_i partial_k g_i = |g| |grad|g||^2` and the last term is
`(1/4)|g||grad|g||^2`, which is the second line. `|V_g| = |g|^{3/2}` gives
`grad|V_g| = (3/2)|g|^{1/2} grad|g|`, hence the third. For the last claim,
`-int j(g).Lap g = int partial_k(|g|g_i) partial_k g_i = int(|g||grad g|^2 +
|(grad g)^T g|^2/|g|)`. `[]`

This is the algebra behind (Q2)/(Q3): the *same* expression computes `D_3(u)`
from `u` and `D_3(w) = D_Q(u)` from `w`, so the lane's premise that the two
sides are structurally alike is correct. It is not correct that `D_3(w)` is
minimizer-free as a functional of `u`: `w` is the minimizer. §3.3 repairs
this.

**Proposition 1.2 (equality on `M`).** If `u` is solenoidal and `u in M` then
`w = u` and `D_3(w) = D_3(u)`; both sides also equal `-<j(u), Lap u>`.
*Proof.* (Q4) gives `w(u)=u`; insert into (Q2), (Q3). `[]`

**Proposition 1.3 (the equality set is strictly larger than `M`; new).** There
is a solenoidal `u in C_c^oo(R^3)^3`-generated heat trajectory and a time
`s* > 0` such that `v := G_{s*} u_0` satisfies `D_3(w(v)) = D_3(v)` and
`v` is **not** in `M` (equivalently `q(v) != 0`, `Delta(v) > 0`).

*Proof.* Let `u_0` be the elliptic swirl of HF19-D Proposition 3.4 (audited),
`v_s = G_s u_0`. By HF19-D Lemma 3.1 (audited), `s |-> Delta(v_s)` is `C^1` on
`[0,oo)` with `d/ds Delta(v_s) = D_3(w(v_s)) - D_3(v_s)` and
`Delta(v_s) -> 0` as `s -> oo`. By Proposition 3.4 there, `v_s` is not in `M`
for all small `s>0`, so `Delta(v_s) > 0` there by (Q5), while
`Delta(v_0) = 0`. A continuous function on `[0,oo)` that vanishes at `0`, is
positive somewhere and tends to `0` at infinity attains a positive maximum at
some interior `s* in (0,oo)`; there `d/ds Delta = 0`, i.e.
`D_3(w(v_{s*})) = D_3(v_{s*})`, and `Delta(v_{s*}) > 0`. `[]`

So equality of the two dissipations is *not* a characterisation of the
nonlinear-Hodge class: it holds on `M` and on a set that meets the complement
of `M`. Any argument that would read `D_3(w)=D_3(u)` as `q=0` is refuted.

---

## 2. The three routes of the lane statement, and the answer

### 2.1 The variational route, and what the question really is

`w` minimizes `F`, not `D_3`; minimality gives `||w||_3 <= ||u||_3` and
nothing about derivatives. The exact translation is:

**Proposition 2.1 (reformulation; HF19-D Lemma 3.1 restated).** For solenoidal
`u in H^m`, `m>=4`,
```
 D_3(u) - D_3(w) = <j(w) - j(u), -Lap u> = -(d/ds)|_{s=0} Delta(G_s u) .
```
Hence `D_3(w) <= D_3(u)` at `u` **iff** the distance functional
`Delta = F - Q` is nonincreasing at `u` along the heat semigroup.

*Proof.* `D_3(u) = -<j(u), Lap u>` (Q3) and `D_3(w) = D_Q(u) = -<A, Lap u>`
(Q2) give the first equality. `F` and `Q` are Fréchet differentiable with
derivatives `j(u)` and `A` (`lem:cubic-frechet`, `prop:quotient-derivative`),
and `(G_s u - u)/s -> Lap u` in `L^3` (`lem:heat-generator`
\eqref{eq:qe-generator}); the chain rule gives the second. `[]`

Both `F` and `Q` decrease along the heat flow (`lem:quotient-heat`), so the
question is *which decreases faster*. Minimality supplies the one-sided
comparison `Q(u) - Q(G_s u) >= F(w) - F(G_s w)` (take `G_s w` as competitor
for the coset of `G_s u`, using `G_s G_3 subset G_3`). The left side has
derivative `D_3(w)` at `s=0` (`prop:quotient-derivative`,
`lem:heat-generator`); the right side is **not** differentiated, since that
would need the generator limit `(G_s w - w)/s -> Lap w` in `L^3`, i.e.
`Lap w in L^3`, which is the open regularity and is exactly the operation §6
declares this note never performs. Minimality produces no comparison with
`D_3(u)` at all. (Audit (N2): the pre-audit version asserted that the two sides
agree to first order in `s`, both equal to `s D_3(w)`; the right-hand half of
that assertion was unjustified and is deleted, not patched. Proposition 2.1
above is a restatement of the audited HF19-D Lemma 3.1 and carries no new
content.)

### 2.2 The heat-flow route: what it gives and what it does not

**Theorem 2.2 (audited, HF19-D Theorem 3.2).** For solenoidal `u in H^m`,
`m>=4`,
```
 int_0^oo ( D_3(G_s u) - D_3(w(G_s u)) ) ds = Delta(u) >= (1/6)||q(u)||_3^3 .
```
Consequently `D_3(w) >= D_3(u)` fails on a set of `s` of positive measure
whenever `u` is not in `M`.

This is the "averaged sign" of the lane statement, and it is genuinely a sign:
along the whole heat flow the velocity dissipates *more* than its
representative, by exactly the distance functional. What it does not give, and
cannot: (i) it is an integral over `[0,oo)`, so it constrains the difference
only in aggregate, and a set of `s` of small measure may carry the opposite
sign -- which is what happens (§2.3); (ii) it is a statement along the *heat*
semigroup, not along the Navier-Stokes trajectory, so it transfers nothing to
`prop:quotient-evolution`; (iii) as an averaged statement it is compatible with
either fixed-time inequality being false. Promoting it to a fixed-time
statement is exactly the falsifier "promoting an instantaneous fact to a
time-integrated one" read backwards, and is not done here.

### 2.3 The `M`-drift route: the decisive computation, re-derived

The `<=` direction fails for a structural reason (HF19-D Proposition 3.3,
audited): if `D_3(w) <= D_3(u)` held on the class, then `s |-> Delta(G_s u_0)`
would be nonincreasing, so `Delta(u_0)=0` would force `Delta(G_s u_0)=0`, i.e.
`M` would be invariant under the heat semigroup. It is not. The following two
statements are this lane's independent verification of the audited computation
that shows it.

**Lemma 2.3 (the drift of the `M`-defect is a divergence; new).** Let `v` be
solenoidal and Schwartz, `v_s = G_s v`, `h(s,x) = (v_s . grad|v_s|^2)(x)`, and
```
 N(v) := div( Dj(v) Lap v ) = div( |v| Lap v + (v . Lap v) v/|v| ) .
```
Then `partial_s|_{s=0} div(j(v_s)) = N(v)` pointwise on `{v != 0}`, and if
moreover `v in M`, then `partial_s h(0,x) = 2|v(x)| N(v)(x)`.

*Proof.* `partial_s v_s|_0 = Lap v` pointwise (`lem:heat-generator`, Step 3-4;
HF19-D Prop. 3.4(c)), and `j` is `C^1` with `Dj` as displayed, so
`partial_s j(v_s)|_0 = Dj(v) Lap v`; derivatives in `s` and `x` commute for
Schwartz data, giving the first claim. For solenoidal `v_s`,
`div j(v_s) = |v_s| div v_s + v_s . grad|v_s| = v_s . grad|v_s|`, and
`h = v_s . grad|v_s|^2 = 2|v_s| (v_s . grad|v_s|) = 2|v_s| div j(v_s)`. Since
`v in M` makes `div j(v) = 0`, the product rule leaves only
`partial_s h(0) = 2|v| partial_s div j(v_s)|_0 = 2|v| N(v)`. `[]`

`N` is the object whose non-vanishing refutes heat-invariance of `M`, and it is
minimizer-free: it never differentiates `w`.

**Proposition 2.4 (`N` on the elliptic-swirl class, in the Frenet frame;
new derivation).** Let `Gamma subset R^2` be a smooth closed strictly convex
curve, `d` the distance to it on the exterior, `n = grad d`, `tau = n^perp`,
`kappa = div n > 0` the curvature of the level curve through the point,
`kappa_s = tau . grad kappa`, `J = 1 + kappa_0 d`. Let `b = b(d, x_3)` be
smooth **and `b >= 0`**, supported in `{0 < d_1 <= d <= d_2} x {|x_3| <= c}`,
and `m := b(d,x_3) tau`. Then:

1. `m in C_c^oo(R^3;R^3)`, `div m = 0`, `div(|m|m) = 0`, so `m` is solenoidal
   and `m in M`, hence `w(m) = m` and `q(m) = 0`.
2. `Lap m = (Lap b - b kappa^2) tau - b kappa_s n`, and
   `Dj(m) Lap m = 2b(Lap b - b kappa^2) tau - b^2 kappa_s n`.
3. `N(m) = -2 b^2 kappa kappa_s`.
4. The sign hypothesis is inessential for the object Corollary 2.5 uses:
   dropping `b >= 0` and writing `sigma = sign(b)`, one has `|m| = |b|`,
   `Dj(m) Lap m = sigma[2b(Lap b - b kappa^2) tau - b^2 kappa_s n]` and
   `N(m) = -2 sigma b^2 kappa kappa_s`, so
   `R = 2|m| N(m) = 2 sigma b . (-2 sigma b^2 kappa kappa_s)
   = -4 b^3 kappa kappa_s` regardless of the sign of `b` and of the
   orientation `tau = ±T`.

*Proof.* (1) `tau` is unit with `div tau = 0` and `partial_n tau = 0`,
`partial_tau tau = -kappa n`, `partial_tau n = kappa tau`, `partial_n n = 0`
(parallel curves: the normal lines are geodesics; `Phi(t,d)=gamma(t)+dN(t)` is
a diffeomorphism on the exterior of a convex curve). `b` depends on `(d,x_3)`
only, so `partial_tau b = 0` and `div m = tau.grad b + b div tau = 0`;
`|m| = |b|`, and `div(|m|m) = partial_tau(|b|b) = 0`. By convexity of `F` and
`lem:quotient-minimizer`, a field with `div(|m|m)=0` is the minimizer of its
own coset, so `w(m)=m`.
(2) `partial_j m_i = (partial_j b) tau_i - b kappa tau_j n_i`. Differentiating
again, `(partial_j b)(partial_j tau_i) = 0` because `grad b` has no
`tau`-component, and
`partial_j(b kappa tau_j n_i) = b kappa_s n_i + b kappa^2 tau_i`, which gives
`Lap m`. Then `|m| Lap m + (m.Lap m) m/|m| = b Lap m + b(Lap b - b kappa^2) tau`
is the displayed field.
(3) `div(g tau) = partial_tau g` and `div(h n) = partial_n h + h kappa`. With
`Lap b = b_dd + kappa b_d + b_{x_3 x_3}` and `partial_tau kappa = kappa_s`,
```
 partial_tau[2b(Lap b - b kappa^2)] = 2b(b_d kappa_s - 2 b kappa kappa_s),
 partial_n[b^2 kappa_s] = 2 b b_d kappa_s - 3 b^2 kappa kappa_s,
```
the second using the Riccati identity `partial_n kappa = -kappa^2` and the
commutator `partial_n partial_tau = partial_tau partial_n - kappa
partial_tau` (from `partial_tau = J^{-1} partial_t`, `kappa = kappa_0/J`),
which give `partial_n kappa_s = partial_tau(-kappa^2) - kappa kappa_s =
-3 kappa kappa_s`. Hence
`N = 2b b_d kappa_s - 4 b^2 kappa kappa_s - (2b b_d kappa_s - 3 b^2 kappa
kappa_s) - b^2 kappa kappa_s = -2 b^2 kappa kappa_s`.
(4) Repeat (2)-(3) with `|m| = |b| = sigma b`: the factor `sigma` is constant
on each component of `{b != 0}` and passes through `Dj` and `div`, giving the
displayed forms, and it cancels in the product `2|m| N(m)`. (Audit (N4): the
sign matters because HF19-D's `phi in C_c^oo((0,oo))` is not assumed
nonnegative and the orientation `tau = ±T` is a free choice; Corollary 2.5 is
unaffected either way.) `[]`

**Corollary 2.5 (exact agreement with the audited HF19-D (3.3)).** With
`b = f(x_3) phi(d)`, HF19-D's field, Lemma 2.3 gives
`R := partial_s h(0,.) = 2|m| N(m) = -4 f^3 phi^3 kappa kappa_s` at the point.
Expressed in base-curve quantities via `kappa = kappa_0/J` and
`kappa_s = partial_tau kappa = J^{-1} partial_t(kappa_0/J) = kappa_{0,t}/J^3`,
this is
```
 R = -4 kappa_0 kappa_{0,t} phi(d)^3 / J^4      (f = 1 near the slab),
```
which is HF19-D (3.3) verbatim, including the constant `4` and the power
`J^{-4}`. The auditor of HF19-D re-derived (3.3) twice (by hand in the Fermi
frame and symbolically from scratch,
`hf19-review-difference-functional.md` l.191-201, l.493-494); the derivation
above is a third, in the divergence form
`N = div(Dj(m) Lap m)`, and agrees; the auditor of *this* note added a fourth
(`Lap m = -curl curl m` in the parallel-curve chart, reproducing (2) and (3)
and the constant). All of these are independent *computations* of the same
quantity by different routes and frames, not independent proofs of different
statements (audit, (E1) at Corollary 2.5). By Proposition 2.4(4) the display is
insensitive to the sign of `b` and to the orientation of `tau`.

**Corollary 2.6 (which members of `M` are first-order degenerate; new).**
`N(m) = 0` on the whole azimuthal-swirl class `m = g(r,z) e_theta` (there
`Dj(m) Lap m = 2|g| h e_theta` with `h = Lap g - g/r^2`, an axisymmetric
azimuthal field, hence divergence-free), on straight shears, and on any member
of the class of Proposition 2.4 whose level curves are circles or lines
(`kappa_s = 0`). In particular the swirl `U` of the manuscript's
`rem:no-monotone` and of HF20 lies in this degenerate subclass: it is exactly
the wrong witness for the present question, which is why the refutation needs
the *elliptic* swirl.

**Corollary 2.7 (the answer).** By HF19-D Corollary 3.5 (audited): there are
`0 < s' < s''` with `D_3(w(G_{s'}u_0)) > D_3(G_{s'}u_0)` and
`D_3(w(G_{s''}u_0)) < D_3(G_{s''}u_0)`. Hence **neither** `D_3(w) <= D_3(u)`
**nor** `D_3(w) >= D_3(u)` holds on the class of smooth solenoidal fields, and
`D_3(u)-D_3(w)` takes both signs along one heat trajectory. Sub-question (a) is
answered in the negative.

*Remark 2.8 (a route that is not used).* Linearising the minimizer map at
`m in M` along `u = m + eps v` gives, formally,
`D_3(w) - D_3(u) = eps int N(m) varphi_1 + O(eps^2)` with
`grad varphi_1` the first-order defect, so that `N(m) != 0` plus a sign flip
`eps -> -eps` would refute both directions. This lane does **not** use that
argument: it differentiates the merely-`L^3` minimizer, which is a listed
falsifier, and its error control is worse than its signal (only Hölder-1/2
stability is audited, `lem:quotient-stability` \eqref{eq:cp-strong}, giving
`O(eps^{1/2})` against a signal `O(eps)`). It is recorded only to say why the
degeneracy structure of Corollary 2.6 is the relevant one. The rigorous route
is HF19-D's: heat-invariance of `M`, which never touches `q`.

### 2.4 The `V`-algebra route

Lemma 1.1 shows the pointwise algebra of `V = |w|^{1/2}w` is *identical* to
that of `V_u = |u|^{1/2}u`; the two dissipations are the same functional
evaluated at two different fields. There is therefore no pointwise inequality
to be had from the algebra itself: any comparison must come from the relation
between `u` and `w`, i.e. from `q in G_3` and `div(|w|w)=0`. §3 extracts what
that relation does give.

---

## 3. New exact structure

### 3.1 The comparison is a vorticity pairing

**Lemma 3.1 (unconditional).** For solenoidal `u` in the package (R) with
`omega := curl u`,
```
 D_3(u) = <curl j(u), omega> ,   D_3(w) = <curl A, omega> ,
 D_3(u) - D_3(w) = <curl( j(u) - A ), omega> .
```
*Proof.* `div u = 0` gives `Lap u = -curl curl u`, so
`D_3(u) = -<j(u), Lap u> = <j(u), curl curl u> = <curl j(u), omega>`, the last
step by parts (`j(u) in W^{1,3/2}` for the smooth decaying `u`). For `w`:
`D_3(w) = -<A, Lap u> = <A, curl curl u> = <curl A, omega>`, legitimate because
`A in W^{1,3/2}` (Q2) and `omega in L^3`. `[]`

So the difference of the two dissipations is the pairing of the vorticity with
the curl of the Hodge defect `A - j(u)`; by (Q6) the vorticity is common to `u`
and `w`. This is the same object as HF19-D (2.4) `<A-j(u), Lap u>` after one
integration by parts, but it exhibits `omega` rather than `Lap u`, which is
what makes §3.2 possible.

### 3.2 A master formula with a common vorticity

**Lemma 3.2 (master formula).** For a `C^1` field `g` with enough decay,
```
 D_3(g) = int |g||omega_g|^2 + int grad|g| . (g x omega_g)
          + int |g|(div g)^2 + int (div g)(g . grad|g|) ,   omega_g = curl g .
```
Consequently: for solenoidal `g` the last two terms vanish; and for
nonlinear-Hodge `g` (`div(|g|g)=0`, i.e. `g.grad|g| = -|g| div g`) the last
two terms **cancel each other exactly**. Hence, whenever `w` is regular enough
for the identity to apply to it,
```
 D_3(u) - D_3(w) = int (|u|-|w|)|omega|^2
                  + int [ grad|u|.(u x omega) - grad|w|.(w x omega) ] ,
```
with the *same* `omega = curl u = curl w` in both terms.

*Proof.* `|grad g|^2 = partial_k g_i partial_i g_k + |curl g|^2` pointwise; two
integrations by parts give
`int |g| partial_k g_i partial_i g_k = -int grad|g|.((g.grad)g) + int|g|(div
g)^2 + int (div g)(g.grad|g|)`. Adding `int |g||grad|g||^2` and using the
pointwise identity `g x curl g = |g| grad|g| - (g.grad)g`, i.e.
`grad|g|.(g x omega_g) = |g||grad|g||^2 - grad|g|.((g.grad)g)`, gives the
display. The cancellation for nonlinear-Hodge `g` is
`(div g)(g.grad|g|) = -|g|(div g)^2`. `[]`

Two readings. (i) The naive heuristic "`w` has the same curl as `u` but a
nonzero divergence, so it carries extra Dirichlet energy" -- which is a theorem
in the unweighted `L^2` case, `int|grad w|^2 = int|curl u|^2 + int|div w|^2 >=
int|grad u|^2` -- is **exactly neutralised** in the cubic case: the two
divergence terms cancel against each other by the nonlinear-Hodge relation.
There is no sign from the divergence. (ii) What remains is a comparison of the
two *speeds* `|u|` and `|w|` against the enstrophy density `|omega|^2`, plus a
defect of the same shape one order lower. Minimality controls `||w||_3 <=
||u||_3` -- an integral comparison against the weight `1`, not against
`|omega|^2` -- which is why no sign follows, in agreement with §2.

*Scope.* The formula is unconditional for `u`. For `w` it uses
`w in W^{1,2}_loc` with `|w|^{1/2}|grad w| in L^2`, which is precisely the open
(H1)-type regularity of HF18-B/HF21-A; it is therefore recorded as a
**conditional** statement and is not used in any claim of this note. Under the
same hypothesis the identification of `D_3(w) := D_Q(u)` with the `def:D3P3`
integral of `w` follows from the a.e. chain rule
`grad V = |w|^{1/2} grad w + (1/2)|w|^{-1/2}(grad|w|) w`; this step is part of
the conditional and is **not** proved here (audit, integration item 9). The
unconditional substitute for the whole display is Lemma 3.1 together with
`curl A = |V|^{1/3} curl V + grad(|V|^{1/3}) x V`, valid since `V in H^1`.

### 3.3 Exact inversion of the minimizer map

**Lemma 3.3 (the Helmholtz gradient part lies in `G_3`).** For every
`f in L^3(R^3;R^3)`, `(I-P)f in G_3`.
*Proof.* `P` is bounded on `L^3` (`lem:leray`(b)) and `G_3` is a closed
subspace, so it suffices to treat `f in C_c^oo`, dense in `L^3`. There
`div f in C_c^oo` with `int div f = 0`, and `psi := N * div f` (`N` the
Newtonian potential) satisfies `grad psi = (I-P)f` (the multiplier of
`grad Delta^{-1} div` is `xi (x) xi/|xi|^2 = I - Pi(xi)`), with the multipole
decay `psi = O(|x|^{-2})`, `grad psi = O(|x|^{-3})` [MO] because the monopole
moment vanishes. Hence `psi in L^3` and `grad psi in L^3`, and
`lem:gradient-closure` (which states exactly: `psi in L^3` with distributional
`grad psi in L^3` implies `grad psi in G_3`) gives `grad psi in G_3`. `[]`

*(The pre-audit version proved the closure by hand with a cutoff estimate
`||psi grad chi_R||_3 = O(R^{-2})`; the audit records that half of the proof as
redundant against `lem:gradient-closure`, and it has been deleted. The estimate
was correct; it is simply not needed.)*

**Proposition 3.4 (inversion; new).** Let
`H := {w in L^3(R^3;R^3) : div(|w|w) = 0 in D'}` (the nonlinear-Hodge class)
and `S_p := {B in L^p : div B = 0 in D'}`. Then:

1. `Lambda(B) := |B|^{-1/2} B` (`:=0` where `B=0`) is a bijection
   `S_{3/2} -> H`, with inverse `w |-> |w|w`. Indeed `|Lambda(B)| = |B|^{1/2}`,
   `|Lambda(B)|Lambda(B) = B`, and `int|Lambda(B)|^3 = int|B|^{3/2}`.
2. For `B in S_{3/2}` put `w := Lambda(B)`, `u := P w`, `q := (I-P)w`. Then `u`
   is solenoidal in `L^3`, `q in G_3` (Lemma 3.3), and `w = w(u)`,
   `q = q(u)`, `A(u) = B`, `Q(u) = (1/3)||w||_3^3`.
3. Conversely, for solenoidal `u in L^3`, `B := A(u) = |w(u)|w(u)` lies in
   `S_{3/2}` and `w(u) = Lambda(B)`, `u = P Lambda(B)`.
4. Hence `B |-> P Lambda(B)` is a bijection from `S_{3/2}` onto the solenoidal
   fields of `L^3`, and the whole pair `(u, w(u), q(u), A(u))` is an explicit
   algebraic-plus-Leray function of the free field `B`.

*Proof.* (1) is the displayed algebra plus `div(|w|w) = div B = 0`; the inverse
map lands in `S_{3/2}` by `lem:quotient-minimizer`(c) applied to any `u` with
that minimizer, or directly. (2) `w in L^3`; for every `g in G_3`,
`<j(w), g> = <B, g> = 0` since `div B = 0` and `B in L^{3/2}` pairs with the
`L^3`-limits of `grad C_c^oo`. Convexity of `F` gives
`F(w+g) >= F(w) + <j(w), g> = F(w)`, so `w` minimizes `F` over `w + G_3`; and
`w + G_3 = u + G_3` because `w - u = (I-P)w in G_3`. Uniqueness
(`lem:quotient-minimizer`(b)) gives `w = w(u)`. (3) is
`lem:quotient-minimizer`(c) and `lem:quotient-coercive` (`P w = u`). (4)
Surjectivity is (3); injectivity: if `P Lambda(B_1) = P Lambda(B_2) = u`, both
`Lambda(B_i)` are minimizers of the same coset, hence equal, hence
`B_1 = |Lambda(B_1)|Lambda(B_1) = B_2`. `[]`

*By-product (made explicit by the audit).* (2) and (3) together give
`H = {w(u) : u in L^3 solenoidal}`: the nonlinear-Hodge class **is** the set of
cubic minimizers, not merely contained in it.

**Corollary 3.5 (minimizer-free form of the lane question).** Sub-question (a)
**restricts to** the following question over the strictly larger class
`S_{3/2}`: *for every solenoidal `B in L^{3/2}` for which both sides are
finite, is `D_3(Lambda(B)) <= D_3(P Lambda(B))`?* Both sides are explicit
functionals of `B`: no minimization, no PDE solve, and the defect is the
**linear** object `q = (I-P)Lambda(B)`. By Corollary 2.7 the answer is no --
this is the direction that is used, a smooth counterexample being a
counterexample in the larger class. The two questions are **not** equivalent:
`{P Lambda(B) : B in S_{3/2}}` is *all* solenoidal `L^3` fields, strictly
larger than the smooth solenoidal class of sub-question (a) (audit (N3); the
"Scope and cost" paragraph below already said this in different words, and the
headline now matches it).

*Scope and cost.* The parametrization is exact but does not preserve
regularity: `Lambda` is only Hölder at zeros of `B`, so `u = P Lambda(B)` is in
general not smooth, and a witness produced this way must be checked against the
regularity the trajectory setting needs (`prop:localtheory`(iii),(iv),
`lem:upgrade`). Read in the other direction, this is a reformulation of the
open (H1) question of HF18-B/HF21-A: *for which solenoidal `B` is
`P Lambda(B)` smooth, and is `Lambda(B)` then Sobolev?* That reformulation is
offered to lane (b) and to HF18-B; it is not settled here.

### 3.4 An unconditional upper bound for `D_3(w)`

**Lemma 3.6 (the weighted form is new; see the novelty scope below).** For the
fixed-time data of the package (R),
```
 D_3(w) <= 2 int_{R^3} |w| |grad u|^2 dx <= 2 ||w||_3 ||grad u||_3^2
        <= 2 ||u||_3 ||grad u||_3^2 .
```
Equality of the first bound with `D_3(u) <= 2 int |u||grad u|^2`, the
manuscript's \eqref{eq:D3P3-bounds}, occurs at `w = u`: the weighted bound is
the exact extension of that audited bound to the minimizer, with the same
constant. **Novelty scope.** Only the weighted middle form is new here: the
outer form `D_3(w) = D_Q(u) <= 2||w||_3||grad u||_3^2` is the audited HF18-A
Theorem 2 (2.3) (`hf18-hodge-regularity.md`), which is cited, not reproved, and
the last inequality is minimality.

*Proof.* All inputs are audited HF18-A facts; no new chain rule is needed.
By HF18-A Corollary 1(c),(d), `A = Phi(V) in W^{1,1}_loc cap W^{1,3/2}` with
`grad A = D Phi(V) grad V` a.e. and the **pointwise** bound (1.11)
```
 |grad A| <= (4/3)|V|^{1/3}|grad V| = (4/3)|w|^{1/2}|grad V| ,
```
and by HF18-A Theorem 2 (2.2), `D_3(w) = D_Q(u) = -<A, Lap u> = <grad A, grad
u>`. By HF18-A (2.1), `D_3(w) = a - (1/9)b >= (8/9)a` with `a = int|grad V|^2`
and `b = int|grad|V||^2 <= a` (pointwise `|grad|V|| <= |grad V|`), so
`a <= (9/8) D_3(w)`. Cauchy-Schwarz with the split
`|grad A| = (|grad A|/|w|^{1/2}) . |w|^{1/2}`, legitimate because `grad V = 0`
a.e. on `{V=0}` (Q6) so that the `0/0` set contributes nothing, gives
```
 D_3(w) <= ( int |grad A|^2/|w| )^{1/2} ( int |w||grad u|^2 )^{1/2}
        <= ( (16/9) a )^{1/2} ( int |w||grad u|^2 )^{1/2}
        <= ( 2 D_3(w) )^{1/2} ( int |w||grad u|^2 )^{1/2} ,
```
since `(16/9)(9/8) = 2`. Hence `D_3(w)^2 <= 2 D_3(w) int|w||grad u|^2`, which
gives the first bound (`D_3(w) = 0` being trivial). The Hölder steps use
`|| |grad u|^2 ||_{3/2} = ||grad u||_3^2` and `||w||_3 <= ||u||_3` (minimality,
`q=0` admissible). `[]`

*Remark 3.7 (the exact pointwise identity; correct, and not needed above).*
With the same audited chain rule,
`partial_k A_i = |V|^{1/3} partial_k V_i + (1/3)|V|^{-2/3}(partial_k|V|)V_i`
a.e., the right side read as `0` on `{V=0}`; squaring and summing as in
Lemma 1.1 gives
```
 |grad A|^2 = |V|^{2/3}( |grad V|^2 + (7/9)|grad|V||^2 )
            = |w|( |grad V|^2 + (7/9)|grad|V||^2 ) ,
```
sharper than `(16/9)|w||grad V|^2`, and it yields the same constant `2` through
`a + (7/9)b <= 2(a - (1/9)b)`, i.e. through `b <= a`. The audit verified this
identity and the arithmetic; it is displayed because it may be wanted later,
but the proof above avoids it and with it the `[MO]` Lipschitz-truncation
remark that the pre-audit version invoked (audit, UNNECESSARY DEPENDENCIES).

*Scaling* `int|w||grad u|^2 ~ (a^3, lambda^2)`, matching `D_3` exactly; the
bound uses no norm it must control, but the right-hand side contains
`||grad u||_3`, which is supercritical for the input data, so the lemma is
**not** a producer. Its value is that it bounds `D_3(w)`, the quotient-route
dissipation, by an integral of `u` against the *weight* `|w|` -- the same
weighted-substitution shape as the open HF18-B inequalities.

---

## 4. The two-sided question with a constant

`C = 1` is refuted in both directions (Corollary 2.7). The scaled questions

* **(C1)** is there `C < oo` with `D_3(w) <= C D_3(u)` for all solenoidal
  Schwartz `u`?
* **(C2)** is there `C < oo` with `D_3(u) <= C D_3(w)`?

are **not settled here**, and no sign is nominated. What is available:

1. Neither is refuted by scaling: both sides carry `(a^3, lambda^2)`
   (`lem:quotient-scaling` and §0), so a dimensionless constant is admissible.
2. By Lemma 3.6, (C1) follows from the weighted substitution inequality
   `int |w||grad u|^2 <= (C/2) D_3(u)`, i.e. from replacing the weight `|u|` in
   `def:D3P3` by `|w|` at a fixed cost. This is an inequality of exactly the
   HF18-B family (weighted comparisons between minimizer data and velocity
   data), and HF18-B records that family's central members as open.
3. The refutation of `C=1` is quantitatively weak: HF19-D Corollary 3.5
   produces the wrong-sign time `s'` by a mean value theorem and gives no lower
   bound for the ratio, and near `M` the difference vanishes with the distance,
   so nothing in the audited record forces `C` to be large.
4. `M` itself gives `C >= 1` and no more.

An explicit witness with all quantities computed (task item 3) is therefore
**not delivered**. The concrete route to one is Corollary 3.5: choose a
solenoidal `B` supported near the elliptic-swirl geometry of §2.3, form
`w = Lambda(B)`, `u = P w` by one Fourier multiplier, and evaluate the two
integrals of Lemma 1.1. This needs no minimization and no perturbation
argument; it needs a numerical quadrature, and numerics nominate, they never
prove. It was not carried out in this lane.

---

## 5. What the answer changes

**In the distance balance (`rem:distance-balance`).** The identity
```
 d/dt ( (1/3)||u||_3^3 - Q(u) ) = P_3 - K + nu ( D_Q(u) - D_3(u) )
```
keeps its last term, and no one-sided version of it may be used: by Corollary
2.7 the factor `D_Q - D_3 = D_3(w) - D_3(u)` has no sign on the admissible
class. This *confirms* the manuscript rather than correcting it:
`rem:distance-balance` already warns that "the two dissipations are different
objects ... and supplies no bound for either", and `rem:qe-heatsign-scope`
already declines any comparison of `D_Q` with `D_3`. Nothing in `sec:quotient`
asserted the comparison, so no correction is licensed. The only edit this lane
would license, if the controller wants it at all, is one sentence in
`rem:qe-heatsign-scope` recording that **no comparison with constant `1` holds
in either direction**, citing the audited HF19-D witness. That sentence must
**not** say that the comparison is refuted, since (C1)/(C2) with `C>1` are open
(audit, NON-CLAIMS and integration item 12). **Not applied here**; integration
is a controller action.

**In (G).** The frozen gap is
`int_0^tau ||q(t)||_3 D_3(w(t)) dt <= A_input(nu,u_0,H)`. Three consequences:

1. The class of attacks that first replace `D_3(w)` by `D_3(u)` pointwise in
   `t` **with constant `1`** is closed; the replacement up to a finite constant
   is question (C1) of §4 and remains open, and such a replacement would serve
   any of those attacks equally well (audit (N1)). This includes the natural
   reading of the lane's own motivation ("an affirmative answer deletes a term
   ... and makes the quotient dissipation the smaller, hence the harder,
   quantity"): there is no such ordering with constant `1`.
2. **The affirmative branch would not by itself have been a shortcut.** This
   is the audit's replacement for the pre-audit consequence 2, which claimed
   that the affirmative branch would not have been a *producer* because an
   affirmative (a) "would only have moved (G) onto the pressure route". That
   claim was the first bad bridge: it dropped the factor `||q||_3`, so the two
   spacetime integrals compared did not even carry the same amplitude weight;
   it read the one-way implication "`hyp:absorption` implies an input-only
   bound for `int D_3(u)`" as a biconditional ("exactly"); and it read
   non-derivability along one route as falsity of the branch. It is **replaced**, not patched,
   by the following three statements of
   `hf22-review-dissipation-comparison.md` (REPLACEMENT ARGUMENT), which are
   the auditor's and are reproduced with their proofs.

   **Lemma R1 (Serrin coercivity of the velocity dissipation; unconditional).**
   For every smooth solenoidal `u` in the package (R) at a fixed time,
   ```
    D_3(u) >= c ||u||_9^3 ,      c = (8/9) S^{-1} ,
   ```
   with `S` the Sobolev constant of `dot H^1(R^3) -> L^6` in the normalisation
   `||f||_6^2 <= S ||grad f||_2^2`.

   *Proof.* By Lemma 1.1 with `g = u` and `V_u = |u|^{1/2}u`,
   `D_3(u) = int(|grad V_u|^2 - (1/9)|grad|V_u||^2)`. Pointwise
   `|grad|V_u|| <= |grad V_u|`, so
   `D_3(u) >= (8/9) int|grad V_u|^2 >= (8/9) S^{-1} ||V_u||_6^2`. Since
   `|V_u| = |u|^{3/2}`, `||V_u||_6^2 = (int|u|^9)^{1/3} = ||u||_9^3`. `[]`

   This is the `u`-side analogue of the audited HF18-A bound
   `D_Q(u) = D_3(w) >= c'||u||_9^3` (HF18-A Theorem 2, with
   `c' = 8/(9 S^2_{HF18} C_9^3)` in that note's normalisation
   `||f||_6 <= S_{HF18}||grad f||_2`); it is proved here directly and is
   **not** quoted from HF18-A, whose statement is about `w`.

   **Proposition R2 (what an input-only bound on `int D_3(u)` is worth).** Fix
   `nu > 0`, a divergence-free Schwartz datum `u_0`, and `0 < H < oo`, and let
   `u` be the classical branch of `prop:localtheory`. The following are
   equivalent.
   1. There is a finite `B(nu,u_0,H)` with
      `int_0^tau D_3(u(t)) dt <= B` for every `0 < tau < min{H, T_*}`.
   2. `T_* > H` (the branch survives the horizon).

   *Proof.* (1)`=>`(2). By Lemma R1, `int_0^tau ||u(t)||_9^3 dt <= B/c` for all
   `tau < min{H,T_*}`, i.e. `u in L^3_t L^9_x` on that interval with
   `2/3 + 3/9 = 1`: the Ladyzhenskaya-Prodi-Serrin criterion at a
   subcritical-in-time exponent pair. With the blow-up characterisation of
   `prop:localtheory` this excludes `T_* <= H`. (2)`=>`(1). `t |-> D_3(t)` is
   measurable and bounded on the compact classical interval `[0,H]` by
   `prop:pressure`(i), hence integrable there, so `B = int_0^H D_3` is finite.
   `[]`

   The (1)`=>`(2) direction is, up to the switch from the velocity side to the
   quotient side, already recorded in the audited HF18-A §4 item 3
   (`nu int_0^tau D_3(w) dt >= (8 nu/(9 S^2_{HF18} C_9^3)) int_0^tau ||u||_9^3
   dt`, so
   an input-only bound puts `u` in a Ladyzhenskaya-Prodi-Serrin class); no
   novelty is claimed for it here. The Ladyzhenskaya-Prodi-Serrin criterion is
   an **external classical input**, flagged as such.

   **Corollary R3 (the corrected counterfactual).** Suppose, contrary to
   Corollary 2.7, that `D_3(w) <= D_3(u)` held at every fixed time on the
   admissible class. Then the majorant it supplies for (G) is
   `int_0^tau ||q(t)||_3 D_3(u(t)) dt`, and by `lem:quotient-coercive`
   `||q||_3 <= (1+C_P)||w||_3 <= (1+C_P)||u||_3`, so the target becomes the
   velocity-side spacetime quantity `int_0^tau ||u||_3 D_3(u) dt`. Three things
   are then true and no more:

   1. This is **not** the pressure-route quantity `int_0^tau D_3(u) dt`. The
      two differ by the factor `||u(t)||_3`, which the audited record controls
      only in the time-integrated form \eqref{eq:L4L3}, never pointwise; and
      they carry different amplitude weights, `(a^4, lambda^0)` against
      `(a^3, lambda^0)`. Neither bound implies the other.
   2. The pressure route does control the second quantity, **in one direction
      only**: `hyp:absorption` with its `theta < 1` gives
      `(1-theta) nu int_0^tau D_3 <= (1/3)||u_0||_3^3 + A(nu,u_0,H)` through
      \eqref{eq:pressure-balance}. The converse implication does not follow
      from that identity, which also carries `(1/3)X(tau)` and would need an
      input bound on `X(tau) = ||u(tau)||_3^3`.
   3. By Proposition R2, an input-only bound on `int_0^tau D_3(u)` is, *at the
      quantifiers of (G) and of `hyp:absorption`*, equivalent to global
      continuation on the horizon -- exactly the status
      `rem:highstrain-scope` records for `hyp:absorption` itself. So the
      pressure-route quantity is not a softer target than (G); it is the same
      difficulty in different variables.

   Consequently the licensed statement is: *the affirmative answer to (a) would
   have replaced (G) by a velocity-side spacetime quantity of the same
   difficulty class as the pressure route's, and would therefore not by itself
   have been a shortcut.* It is **not** licensed to say that the affirmative
   branch "would not have been a producer": that would require excluding every
   argument from the affirmative answer, and the obvious surviving one --
   combining it with smallness of `||q||_3` off a small set, i.e. the shape of
   lane (c) -- is not excluded by anything in this note or in the audited
   record. It is not claimed that no argument from an affirmative (a) closes
   (G); the good-set shape of lane (c) is not excluded.

   The audited ordering quoted by the pre-audit version survives as a quotation
   and nothing more: `rem:highstrain-scope` does state that `hyp:absorption`
   implies \eqref{eq:quotient-gap} with `theta = 1` and an explicit remainder,
   "so the high-strain hypothesis is not harder than the high-pressure one".
   What does not follow from that ordering is the counterfactual: it says
   nothing about what an affirmative (a) would or would not reduce (G) to.
3. What survives untouched: the averaged sign of Theorem 2.2 (along the heat
   flow only, no transfer to the trajectory), the audited sharp transport bound
   `|K| <= C_sharp ||q||_3 D_3(w)`, the crossing-measure bound, and the
   normalisation `rem:highstrain-normalisation` by which (G) is the whole gap.
   None of these is affected by the sign of `D_3(w) - D_3(u)`.

**New objects the programme gains.** The inversion (Prop. 3.4, Cor. 3.5) --
every admissible pair `(u,w)` is `(P Lambda(B), Lambda(B))` for a free
solenoidal `B`, so `q(u)` is a linear projection of an explicit algebraic
field, and `H` is *exactly* the set of cubic minimizers (a by-product the audit
makes explicit from Prop. 3.4(2)+(3)); and the weighted middle form of
Lemma 3.6, an unconditional scaling-consistent upper bound for the quotient
dissipation in terms of `u` and the weight `|w|` (its Hölder'd form being the
audited HF18-A Theorem 2 (2.3)). Neither is a producer; both are
minimizer-free handles where the programme previously had only the opaque
minimizer.

---

## 6. Discipline

**FALSIFIER checks** (state after the audit's repairs). No bound below uses the
norm it must control (Lemma 3.6 uses `||grad u||_3`, and is explicitly labelled
a non-producer for that reason). No absorption is claimed, so no
scaling-inconsistent absorption; every displayed relation was checked against
the `(a, lambda)` table of §0, and the audit used that same table to expose the
dropped factor `||q||_3` in the pre-audit §5 (the two spacetime integrals there
carry `(a^4,lambda^0)` and `(a^3,lambda^0)`). No smallness hypothesis appears
anywhere. The merely-`L^3` minimizer is never differentiated: the only place
where such a derivative would be natural (Remark 2.8) is explicitly excluded
from the argument; the refutation runs through heat-invariance of `M`, which
touches only `Delta` and `G_s`; and the first-order comparison that the
pre-audit §2.1 drew from minimality, which would have needed `Lap w in L^3`,
has been deleted on the audit's instruction (N2). No instantaneous fact is
promoted to a time-integrated one; conversely, Theorem 2.2 (a time-integrated
fact along the heat flow) is explicitly **not** read at a fixed time, which is
the whole content of §2.2. The equation is never changed: no forcing, no
periodicity, no hyperdissipation, no Euler.

**Non-derivability is not falsity** (the falsifier the pre-audit version
tripped). `C = 1` in either direction is **false**, on an explicit audited
witness class (Cor. 2.7 via HF19-D Cor. 3.5). By contrast the following are
merely **not derivable from the listed facts**, and are nowhere asserted to be
false: (C1) and (C2) with some `C > 1` (§4, open); an input-only bound for
`int_0^tau ||q||_3 D_3(u) dt` from one for `int_0^tau D_3(u) dt`, or
conversely (Cor. R3.1); \eqref{eq:absorption} from an input-only bound on
`int_0^tau D_3(u) dt` (Cor. R3.2, the converse the pre-audit version asserted
with the word "exactly"); and the proposition that no argument from an
affirmative (a) closes (G) (Cor. R3, closing paragraph). The pre-audit §5
consequence 2 wrote the last of these as a falsity result; it has been replaced
at reduced strength, not patched.

**Blacklisted implication** (audit, REOPENING CONDITION). The implication *"an
input-only bound for `int_0^tau D_3(u) dt` is what an affirmative
sub-question (a) reduces (G) to, and it is exactly `hyp:absorption`, hence the
affirmative branch is not a producer"* is blacklisted. It reopens only on one
of: (i) an input-only pointwise-in-time bound for `||q(t)||_3`, or a proof that
`int_0^tau ||q||_3 D_3(u) dt` and `int_0^tau D_3(u) dt` are comparable with
input-only constants; (ii) an estimate-level converse to Corollary R3.2, i.e.
an input-only bound for `X(tau) = ||u(tau)||_3^3` derived from an input-only
bound on `int_0^tau D_3(u)`; or (iii) a proof that *no* argument from an
affirmative (a) closes (G), which -- lane (c)'s good-set shape being the
obvious surviving candidate -- would itself be a substantial theorem.

**CLAIM AND SCOPE.** For every smooth solenoidal field of the class of
`prop:localtheory` at a fixed time, the inequality `D_3(w) <= D_3(u)` is false
in general, and so is `D_3(w) >= D_3(u)`; equality holds on `M` and on a
strictly larger set. The exact identities of §3 (Lemmas 3.1, 3.6, Prop. 3.4)
hold for the stated classes with the stated audited inputs. Nothing here bears
on `hyp:highstrain`, `hyp:highpressure`, `hyp:absorption`, or (G) except by
closing the pointwise-replacement route **with constant `1`** and by the
observation of Corollary R3 that an affirmative (a) would not by itself have
been a shortcut, because it converts (G) into a velocity-side spacetime
quantity whose input-only control is, at these quantifiers, equivalent to
global continuation. It is **not** claimed that no argument from an
affirmative (a) closes (G), and (C1)/(C2) are not decided.

**EVIDENCE.** Audited: HF19-D §§1-3 (`hf19-difference-functional.md`, audit
`hf19-review-difference-functional.md`, VERDICT REPAIR with §§1-3 reconstructed
independently and (3.3) re-derived twice) [DI]; HF18-A Theorem 2 and the
`W^{1,3/2}`/`H^1` regularity of `A`, `V` [DI via HF19-D §0 and
`hf18-hodge-regularity.md`]; HF21-A Theorem 1 and Prop. 4.1 [DI]; manuscript
labels as listed in the header [DI]. Proved here: Lemma 1.1, Props. 1.2, 1.3,
2.1 (restatement), Lemma 2.3, Prop. 2.4, Cors. 2.5-2.7 (2.7 quoting the audited
Cor. 3.5), Lemmas 3.1, 3.2 (with its conditional scope), 3.3, Prop. 3.4, Cor.
3.5, Lemma 3.6 (weighted form; its Hölder'd form is quoted from HF18-A (2.3),
not proved here) and Remark 3.7. Machine check (algebra only, nomination-level, not evidence for
any theorem): the master formula of Lemma 3.2 and its pointwise half were
verified against `def:D3P3` and against `-<j(g), Lap g>` for a generic
non-solenoidal Gaussian-modulated field on `[-4,4]^3` at `161^3` points, sympy
1.14 exact differentiation plus trapezoid quadrature: `5.99727136`,
`5.99727135`, `5.99727136` for the three forms, pointwise residual
`6.4e-16` (scratch `check_master.py`, session scratchpad, not committed).
Numerics are bounded evidence and nominate only; they prove nothing.
Audit-supplied and reproduced here with their proofs: Lemma R1, Proposition R2,
Corollary R3 of `hf22-review-dissipation-comparison.md`, replacing §5
consequence 2. The audit also independently reconstructed §§1-4, added a fourth
derivation of HF19-D (3.3) (`Lap m = -curl curl m` in the parallel-curve
chart), and corroborated the master formula and the general form of Lemma 2.3
numerically -- again as evidence, not proof. Quoted, not claimed: HF18-A
Theorem 2 (2.1)-(2.3) and Corollary 1(c),(d) (1.11) (used in Lemma 3.6 and
noted as already containing its Hölder'd form), and HF18-A §4 item 3 (already
containing the quotient-side analogue of Proposition R2's (1)`=>`(2)).

**FIRST GAP (unchanged by the audit and by these repairs; not closed).** An
explicit witness with computed quantities. The audited refutation is an
existence argument (mean value theorem in `s`), and this lane supplies the
machinery for an explicit one (Cor. 3.5) but not the evaluation; the size of
the failure, i.e. questions (C1)/(C2) of §4, is untouched. The repairs above
change no part of this: they replace one downstream consequence of §5 and
narrow or re-attribute several statements; §§0-4 are unchanged in substance.

**SURVIVING CONDITIONAL SUFFIX.** (i) If `w in W^{1,2}_loc` with
`|w|^{1/2}|grad w| in L^2` -- the open (H1)-type regularity -- then the master
formula of Lemma 3.2 applies to `w`, the two divergence terms cancel exactly by
`div(|w|w)=0`, and the difference of the dissipations is the displayed
common-vorticity expression. Part of that conditional, and not proved here, is
the a.e. chain rule identifying `D_3(w) := D_Q(u)` with the `def:D3P3` integral
of `w` (§3.2 Scope). This suffix is used in no claim of the note, and it
reopens the moment some audited route delivers that regularity; HF23 is not
admitted here. (ii) If the weighted substitution inequality
`int|w||grad u|^2 <= C' D_3(u)` holds, then (C1) holds with `C = 2C'`.

**NON-CLAIMS.** No proof or disproof of (G), `hyp:highstrain`,
`hyp:highpressure`, or NS-R3. No regularity of the minimizer. No Lipschitz
property of the nonlinear projection (lane (b)). No claim that the inversion of
Prop. 3.4 is new to the literature; it is elementary, and no priority is
claimed for anything here. No manuscript edit is applied and no graph node is
promoted or demoted. The numerical check verifies algebra, not a theorem. No
novelty is claimed for Lemma R1, Proposition R2 or Corollary R3, which are the
auditor's; Proposition R2's (1)`=>`(2) direction uses the
Ladyzhenskaya-Prodi-Serrin criterion as an external classical input, and its
quotient-side analogue is already in the audited HF18-A §4 item 3. No novelty
is claimed for the outer form of Lemma 3.6, which is HF18-A Theorem 2 (2.3).
The equivalence of Proposition R2 is at the level of quantifiers, not of
estimates: it supplies no input-only bound for anything, and in particular it
is not a step towards (G). Nothing here asserts HIGH-PRESSURE, HIGH-STRAIN,
CRITICAL or NS-R3.

**NEXT DISTINCT ACTION.** Either (i) evaluate Corollary 3.5 on one explicit
solenoidal `B` adapted to the elliptic-swirl geometry -- one Leray projection
and two quadratures, no minimization -- to convert the audited existence
statement into an explicit witness with computed quantities and a numerical
lower bound for the ratio, which would also give the first data point on
(C1)/(C2); or (ii) attack the weighted substitution inequality
`int|w||grad u|^2 <= C' D_3(u)` of §4 item 2 directly, in the HF18-B weighted
family, since by Lemma 3.6 it is the exact remaining content of (C1). Neither
needs lane (b)'s Lipschitz question.
