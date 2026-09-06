# HF22-B: is the nonlinear projection `u -> q(u)` Lipschitz in `L^3` at the nonlinear-Hodge class?

Lane HF22-B, MODE: **DISCOVER with a falsifier arm**, 2026-09-06. **UNAUDITED.**
Owned file; nothing else in the repository is edited, and nothing is committed.
Nothing here is promoted; the manuscript is untouched. **No HIGH-PRESSURE,
HIGH-STRAIN, CRITICAL or NS-R3 result is asserted, and the target (G) is not
closed.**

Inputs [DI]: `PLAN.md` ("Beyond the checkpoint", "Frontier packet", "HF18",
"HF20", "HF21", "Ordered next actions"); `../navier-paper/main.tex`
`sec:quotient` (`def:quotient`, `lem:cubic-pointwise` with `eq:cp-lipschitz`,
`eq:cp-taylor`, `eq:cp-monotone`, `eq:cp-strict`; `lem:cubic-frechet` with
`eq:cp-F-taylor`, `eq:cp-F-lipschitz`, `eq:cp-F-monotone`;
`lem:quotient-minimizer`, `lem:gradient-closure`, `lem:quotient-coercive`,
`lem:quotient-scaling`, `lem:quotient-heat`, `lem:quotient-stability`,
`prop:quotient-derivative`, `rem:quotient-scope`, `lem:quotient-pressure`,
`lem:quotient-chainrule`, `lem:heat-generator`, `lem:quotient-heatsign`,
`lem:quotient-transport`, `prop:quotient-evolution`, `lem:quotient-lowstrain`,
`hyp:highstrain`, `rem:highstrain-normalisation`, `rem:highstrain-scope`,
`rem:distance-balance`, `rem:no-monotone`, `prop:quotient-conditional`) and,
outside it, `prop:localtheory`, `lem:upgrade`, `prop:energy`, `prop:scaling`
with `eq:L4L3`, `prop:pressure` with `def:D3P3`, `prop:lowpressure`,
`hyp:highpressure`, `hyp:absorption`;
`research/evidence/hf21-crossing-sign-structure.md` (§1.2, §1.3, §3.1, §3.2,
§4.5) and `hf21-review-crossing-sign-structure.md` (§1.1, §2, R1, R2);
`research/evidence/hf21-shifted-hodge-regularity.md` (Theorem 1, Theorem 2,
Corollary 2.1, Corollary 2.2, Theorem 3, §6.2) and its review;
`research/evidence/hf18-hodge-regularity.md`, `hf18-divergence-speed-link.md`
(§2.3 and the open weighted items) [DI headline statements only].

---

## 0. Answer, in one paragraph

The lane's question is **not decided**, but the interval it lives in is cut in
half by an unconditional theorem proved here, and its remaining content is
identified exactly. **Theorem A** (§2): for *every* `u,h in L^3` the minimizer
displacement obeys the *weighted Lipschitz* bound
`int (|w|+|w'|)|w'-w|^2 <= 4 int (|w|+|w'|)|h|^2` — Lipschitz with constant `2`
in the weighted `L^2` norm carried by the field itself. Its unweighted corollary
is `||w'-w||_3 <= (4W)^{1/3}||h||_3^{2/3}`, i.e. **Hölder exponent `2/3`, not
`1/2`**, at every base point. Consequences: (a) the falsifier arm's assigned
target — an explicit family realising rate exactly `1/2` — **does not exist**,
so item (3) of the brief is answered negatively by proof rather than by a
construction; (b) in the exponent lattice, `alpha > 3/2` is refuted on the
`rem:no-monotone` family under the same three hypotheses the audited HF21
Lemma R2 uses, narrowing the open window from `(1,2]` to `(1,3/2]`; (c) any
witness for non-Lipschitz continuity must have rate `beta in [2/3,1)`.
Linearisation (§4) reduces Lipschitz continuity at `U in M` to **one scalar
degenerate elliptic problem**, `-div(a grad phi) = div(a h)` with
`a = |U|(I + U^ U^ )`, `U^ = U/|U|`; that operator is invertible in its weighted
energy space (Lax–Milgram, with exactly the constant of Theorem A), is
**never** invertible in the `L^3` norm at a compactly supported `U in M`, and
at `U` with `|U| > 0` a.e. its `L^3` invertibility is precisely a weighted
Calderón–Zygmund estimate — the same open item recorded in HF18-B. The
linearisation's kernel is, however, *not* a source of non-Lipschitz behaviour:
on it the exact problem is `1`-homogeneous and therefore exactly Lipschitz
(§4.4). The lane therefore ends at a named external input, not at a decision.

---

## 1. The audited stability estimate, exactly, and why `1/2`

### 1.1 Statement as audited [DI, `lem:quotient-stability`]

For `u,h in L^3(R^3;R^3)`, `w = w(u)`, `w' = w(u+h)`, `A = A(u) = j(w)`,
`A' = A(u+h)`, with `j(z) = |z|z`:

```
 | ||w'||_3 - ||w||_3 | <= ||h||_3                                   (eq:cp-contraction)
 (1/2)||w'-w||_3^3 <= <A'-A, h>,   ||w'-w||_3 <= 2(||w||_3+||h||_3)^{1/2}||h||_3^{1/2}   (eq:cp-strong)
 ||A'-A||_{3/2} <= 4(||w||_3+||h||_3)^{3/2}||h||_3^{1/2}             (eq:cp-continuity)
```

Since `q(u) = w(u) - u`, the same rate holds for the projection:
`||q(u+h)-q(u)||_3 <= ||w'-w||_3 + ||h||_3`. This is the only modulus of
continuity for `u -> q(u)` in the audited record.

### 1.2 Proof mechanism [DI, proof of `lem:quotient-stability`]

Two ingredients, both exact:

* **Cancellation.** `w'-w-h = q(u+h)-q(u) in G_3`, and both minimizers annihilate
  `G_3` (`lem:quotient-minimizer`(c)), so
  `<A'-A, w'-w> = <A'-A, h>` exactly. This is what makes the estimate a
  *stability* estimate rather than a monotonicity estimate; note that no
  derivative of the minimizer is taken anywhere.
* **Uniform convexity of the cubic.** `eq:cp-F-monotone`,
  `<j(v)-j(v'), v-v'> >= (1/2)||v-v'||_3^3`, applied with `v = w'`, `v' = w`.

Combining and using `eq:cp-F-lipschitz` gives
`(1/2)||z||_3^3 <= ||A'-A||_{3/2}||h||_3 <= (||w||_3+||w'||_3)||z||_3||h||_3`,
`z := w'-w`; dividing by `||z||_3` leaves `||z||_3^2 <~ ||h||_3`, hence `1/2`.

### 1.3 Where the exponent `1/2` actually comes from — and why it is not sharp

`eq:cp-F-monotone` is the *integrated and weakened* form of the exact pointwise
identity `eq:cp-monotone` [DI, `lem:cubic-pointwise`]:

```
 (j(a)-j(b))·(a-b) = (|a|+|b|)( (1/2)(|a|-|b|)^2 + (1/2)|a-b|^2 ) >= (1/2)|a-b|^3 .
```

The last step replaces the weight `|a|+|b|` by the *worst possible* value
`|a-b|`, which is legitimate (`|a|+|b| >= |a-b|`) but is an equality **only in
the total-cancellation regime `|a-b| = |a|+|b|`, i.e. `a` and `b` antiparallel**.
That regime is a large perturbation, not a small one. In the regime the lane
cares about — `h` small, `w'` close to `w` — the true weight is
`|a|+|b| ~ 2|w| >> |a-b|`, and the correct modulus of convexity is the
*weighted quadratic* one, not the cubic one. So the exponent `1/2` is an
artefact of using a modulus tuned to sign reversal of the field. Restoring the
weight is the whole content of §2. (`1/2` is exactly the exponent one also
reaches through the audited distance lattice, `d_1 <= 2 d_4^{1/2}` with `d_4`
Lipschitz [DI, hf21-crossing §1.3]; §2 beats that route too.)

---

## 2. Theorem A: the projection is Lipschitz in the field-weighted `L^2` norm

Notation throughout: `u,h in L^3(R^3;R^3)`, `w = w(u)`, `w' = w(u+h)`,
`z = w'-w`, and

```
 S := |w| + |w'| (pointwise),   N^2 := int S|z|^2,   M_h^2 := int S|h|^2,   W := ||S||_3 .
```

All three are finite: `S in L^3`, `|z|^2, |h|^2 in L^{3/2}`, Hölder. By Minkowski
`W <= ||w||_3+||w'||_3 <= 2||w||_3+||h||_3` (`eq:cp-contraction`).

> **Theorem A (weighted Lipschitz stability).** For every `u, h in L^3(R^3;R^3)`,
> ```
>    int (|w|+|w'|) |w(u+h)-w(u)|^2 dx  <=  4 int (|w|+|w'|) |h|^2 dx ,
> ```
> i.e. `N <= 2 M_h`. The constant is absolute; no hypothesis on `u`, `h`, on
> solenoidality, or on any regularity of the minimizers is used.

*Proof.* Three displayed manuscript facts and Cauchy–Schwarz.

1. *(cancellation)* `z - h = q(u+h)-q(u) in G_3`, so by
   `lem:quotient-minimizer`(c) applied to both minimizers,
   `<A', z-h> = 0 = <A, z-h>`, hence `<A'-A, z> = <A'-A, h>`. Both pairings are
   finite (`A, A' in L^{3/2}`, `z, h in L^3`).
2. *(lower bound)* By the pointwise identity `eq:cp-monotone` with `a = w'(x)`,
   `b = w(x)`, integrated (integrand nonnegative),
   `<A'-A, z> >= (1/2) int S|z|^2 = N^2/2`.
3. *(upper bound)* By the pointwise `eq:cp-lipschitz`,
   `|A'-A| <= S|z|` a.e.; hence, by Cauchy–Schwarz in `L^2(S dx)`,
   `<A'-A, h> <= int S|z||h| <= N M_h`.

So `N^2/2 <= N M_h`. If `N = 0` the claim is trivial; otherwise divide by `N`. ∎

> **Corollary A1 (unconditional Hölder exponent `2/3`).** For every `u,h in L^3`,
> ```
>    ||w(u+h)-w(u)||_3^3  <=  int S|z|^2  <=  4 int S|h|^2  <=  4 W ||h||_3^2 ,
> ```
> hence `||w(u+h)-w(u)||_3 <= (4W)^{1/3} ||h||_3^{2/3}` with
> `W <= 2||w(u)||_3 + ||h||_3`, and
> `||q(u+h)-q(u)||_3 <= (4W)^{1/3}||h||_3^{2/3} + ||h||_3`.

*Proof.* `|z| = |w'-w| <= |w'|+|w| = S` pointwise, so `int|z|^3 <= int S|z|^2`;
then Theorem A; then Hölder with exponents `3` and `3/2` on `int S|h|^2`. ∎

Both statements are **scaling-consistent**: under `u -> D_lambda u` of
`lem:quotient-scaling` the minimizer transforms by `D_lambda` and every
displayed quantity (`N^2`, `M_h^2`, `W||h||_3^2`) is invariant; under
`u -> alpha u` each side is homogeneous of the same degree (`3` in Theorem A,
`3` in A1). Corollary A1 is strictly stronger than `eq:cp-strong` for all
`||h||_3 < 4(||w||_3+...)`, and never weaker by more than the constant
`4^{1/3} < 2` for large `||h||_3`.

> **Corollary A2 (the constant only sees the field on `supp h`).**
> `||w(u+h)-w(u)||_3^3 <= 4 || |w(u)|+|w(u+h)| ||_{L^3(supp h)} ||h||_3^2`.

*Proof.* `M_h^2 = int_{supp h} S|h|^2`, then Hölder on that set. ∎

> **Corollary A3 (at the nonlinear-Hodge class).** Let `U in M`, i.e. `U in L^3`
> solenoidal with `div(|U|U) = 0`, so that `w(U) = U`, `q(U) = 0`,
> `A(U) = j(U)` [DI, `lem:quotient-minimizer`(b),(c) and hf21-crossing §1.1].
> Then for every `h in L^3`, with `d_1(v) := ||q(v)||_3`,
> ```
>    d_1(U+h) <= ( 4(2||U||_3+||h||_3) )^{1/3} ||h||_3^{2/3} + ||h||_3 .
> ```
> In particular `d_1(U+eps h) = O(eps^{2/3})` as `eps -> 0`, and the true
> `L^3` distance to `M` and the defect `d_1` obey
> `d_1(v) <= C(||v||_3) dist_{L^3}(v, M)^{2/3}` locally.

> **Corollary A4 (Fréchet remainder of `Q` at `M` is `O(||h||^{4/3})`).** For
> `U in M`, `|Q(U+h) - Q(U) - <j(U),h>| <= C(||U||_3+||h||_3) ||h||_3^{4/3}`,
> improving the audited `O(||h||_3^{3/2})` of `eq:cp-derivative-remainder` at
> points of `M`.

*Proof.* By `lem:cubic-frechet` `eq:cp-F-taylor`,
`|F(U+h)-F(U)-<j(U),h>| <= (||U||_3+||h||_3)||h||_3^2`. By the audited Bregman
comparison [DI, hf21-crossing §1.2, confirmed in its review §1.1],
`d_2(v) := F(v)-Q(v) <= (||w(v)||_3+||q(v)||_3)||q(v)||_3^2`. At `v = U+h`,
`||q(v)||_3 = O(||h||_3^{2/3})` by A3, so `d_2(U+h) = O(||h||_3^{4/3})`. Since
`F(U) = Q(U)` and `j(U) = A(U)`, subtract the two expansions. ∎

**Independent check (bounded evidence, not proof).** The proof of Theorem A uses
only the pointwise identity, the Euler–Lagrange cancellation, and Cauchy–Schwarz,
all of which hold verbatim over any measure space; so a finite counting-measure
instance is a legitimate oracle for the algebra. Over `200` random instances
(`12` cells in `R^3`, random `10`-dimensional "gradient" subspaces, `||h||_3`
spanning three decades, minimizers by L-BFGS with Euler–Lagrange residual
`< 1e-6`), the cancellation identity, Theorem A, `||z||_3^3 <= N^2`,
Corollary A1 and the audited `eq:cp-strong` all held, with **zero** violations
(scratchpad `chk.py`). This tests the algebra, nothing about `R^3`.

---

## 3. Falsifier arm: the rate `1/2` is not attainable

The brief's item (3) asks for an explicit family showing the rate is *exactly*
one half, ideally the `rem:no-monotone` harmonic-strain configuration. **No such
family exists.**

> **Corollary A5.** There is no `u in L^3` and no sequence `h_n -> 0` in `L^3`
> with `||w(u+h_n)-w(u)||_3 >= c ||h_n||_3^{1/2}`, `c > 0`. More generally, if
> `||w(u+h_n)-w(u)||_3 = ||h_n||_3^{beta+o(1)}` then `beta >= 2/3`; and a
> witness for the failure of Lipschitz continuity must have `beta in [2/3, 1)`.

*Proof.* Corollary A1 gives `||z||_3 <= (4W)^{1/3}||h||_3^{2/3}` with `W`
bounded as `h_n -> 0`; `eps^{2/3} = o(eps^{1/2})`. ∎

So the falsifier arm returns a **negative structural result**, not a
construction. Two further constraints on any future witness are recorded:

* *(admissibility)* If the witness is required to be the minimizer of a datum
  satisfying the classical hypotheses (0.1) of HF21-A, then by
  Theorem 2 and Corollary 2.2 of `hf21-shifted-hodge-regularity.md` [DI] every
  zero of `A' = |w'|w'` must be **degenerate** (`DA'= 0` there): a solenoidal
  `A'` vanishing linearly forces `|sk grad w'| >= c_0 d^{-1/2}` on a cone, hence
  `curl u' = curl w' notin L^inf_loc`, contradicting smoothness of the datum.
  Every construction the programme has produced so far vanishes linearly.
* *(the `rem:no-monotone` configuration is admissible but useless here)* `U` is
  an azimuthal swirl in `C_c^inf` with `div(|U|U) = 0`, so `U in M`,
  `w(U) = U` [DI, `rem:no-monotone`]. Its zeros of `A = |U|U` are *quadratic*
  (`U ~ c rho e_theta` near the axis gives `A ~ c^2 rho^2 e_theta`,
  `DA = 0`), so it passes the rigidity constraint; but by A5 it cannot exhibit
  rate `1/2`, and by A3 its defect obeys `d_1(U + eps h) = O(eps^{2/3})`.

---

## 4. Linearisation at `M`: one scalar degenerate elliptic problem

### 4.1 The linearised Euler–Lagrange operator

Let `U in M`, so `w(U) = U`, `q(U) = 0`, and the exact Euler–Lagrange condition
is `div(|U|U) = 0` in `D'` [DI, `lem:quotient-minimizer`(c)]. Write
`u_eps = U + eps h`, `w(u_eps) = U + eps h + q_eps`, `q_eps in G_3`. The exact
condition is `div( A(w(u_eps)) ) = 0`, `A(v) = |v|v`. Since
`Dj(v)[zeta] = |v|( zeta + v^ (v^·zeta) ) = |v|(I + v^ ⊗ v^ ) zeta`, `v^ = v/|v|`,
the formal linearisation at `U` in the direction `h`, with
`q_eps = eps grad phi + o(eps)`, is the scalar divergence-form equation

```
      - div( a grad phi ) = div( a h ),        a := |U| ( I + U^ ⊗ U^ )        (LIN)
```

with `a` symmetric, `|U| I <= a <= 2|U| I` a.e., and `a := 0` on `{U = 0}`. The
eigenvalues are `|U|` (twice, transverse) and `2|U|` (along `U^`). Two structural
remarks: `a` is homogeneous of degree `1` in `U`, so multiplying `U` by a
constant does not change `phi` — the Lipschitz constant at `U`, if finite, is a
**scale- and translation-invariant functional of the shape of `U` alone**
(consistent with `lem:quotient-scaling` and with `q(lambda u) = lambda q(u)`);
and `(LIN)` sees `U` only through `|U|` and the line field `U^ ⊗ U^`.

### 4.2 What is unconditionally true about `(LIN)`

* *(boundedness)* `B(phi,psi) := int a grad phi · grad psi` satisfies
  `|B| <= 2||U||_3 ||grad phi||_3 ||grad psi||_3` (Hölder with `3,3,3`), and
  `psi -> int a h·grad psi` is bounded on `G_3` by `2||U||_3||h||_3`. So
  `L_U : G_3 -> G_3^*` is bounded.
* *(solvability in the weighted space)* Let `H_U` be the completion of
  `{grad phi : phi in C_c^inf}` under `B`. `B` is an inner product on `H_U`, and
  `|int a h·grad psi| <= (int a h·h)^{1/2} B(psi,psi)^{1/2}`, so Lax–Milgram
  gives a **unique** `grad phi in H_U` with
  `B(phi,phi)^{1/2} <= (int a h·h)^{1/2} <= (2 int |U| |h|^2)^{1/2}`.
  This is exactly the linear shadow of Theorem A: both say the response is
  bounded by the datum **in the field-weighted `L^2` norm**, with an absolute
  constant. The agreement is a consistency check on both.
* *(kernel)* `B(phi,phi) = 0` iff `grad phi = 0` a.e. on `{U != 0}`. Hence
  `ker L_U|_{G_3} = { grad phi in G_3 : grad phi = 0 a.e. on {U != 0} }`, which
  is **nontrivial whenever `{U = 0}` has nonempty interior** (take
  `phi in C_c^inf` of that interior).

### 4.3 The literal answer to the lane's item (2)

> **The linearised operator is not invertible in the relevant norm at every
> compactly supported `U in M`** — in particular at the azimuthal swirl of
> `rem:no-monotone`, since `R^3 \ supp U` is open and `U = 0` there. At a
> `U in M` with `|U| > 0` a.e. the kernel is trivial, and Lipschitz continuity
> reduces to the **surjectivity/closed-range half**, i.e. to the weighted
> Calderón–Zygmund estimate
> ```
>    || grad phi ||_3 <= C(U) || h ||_3     for   -div(a grad phi) = div(a h),  a = |U|(I+U^ ⊗U^ ),
> ```
> which is an instance of exactly the class of weighted inequalities recorded as
> **open** in HF18-B (`hf18-divergence-speed-link.md`), and which HF21-A's
> Theorem 6/§6.2 reports cannot be reached by Gehring from the available
> Caccioppoli inequality [DI, headline statements].

So sub-question (b) is not independent of the HF18-B gap: it inherits it. This
is route information: the size-route ceiling and the (H1)/(H2) regularity
question are governed by the same scalar weighted-elliptic item.

### 4.4 Why the kernel does **not** refute Lipschitz continuity

A non-invertible linearisation would ordinarily nominate a non-Lipschitz point.
Here it does not, and the reason is exact:

* On the kernel block the nonlinear problem is **`1`-homogeneous**. Let
  `Omega_0` be an open subset of `{U = 0}`. For gradients supported in
  `Omega_0` the exact functional increment is
  `F(U + eps h + grad phi) - F(U + eps h) = (1/3) int_{Omega_0}( |eps h + grad phi|^3 - |eps h|^3 )`,
  jointly homogeneous of degree `3` in `(eps h, grad phi)`; its minimiser
  therefore satisfies `||grad phi||_{L^3(Omega_0)} = eps ||grad phi_1||_{L^3(Omega_0)}`
  exactly, with `phi_1` the minimiser for `h` itself. Rate exactly `1`.
* Equivalently in the linear picture: the *forcing* on the degenerate directions
  is quadratic, not linear, in the perturbation. `j` is `2`-homogeneous and
  `j(U) = 0` on `{U = 0}`, so the first variation there is `O(eps^2)`, while the
  cost is cubic; balancing `eps^2 t` against `t^3` gives `t ~ eps`. The two
  degeneracies cancel **exactly at first order**: the question is borderline by
  structure, which is why neither the audited rate nor a cheap counterexample
  settles it.

This also disposes of the natural "far-field" refutation: at a compactly
supported `U in M` the exterior of `supp U` is a kernel block, and a purely
exterior gradient has *zero* first-order gain (the gain
`<j(U+eps h)-j(U), grad phi>` is supported where `U` or `h` is), so no
`eps^{1/2}`-amplitude exterior excursion is bought. (A separate structural fact
points the same way: `p = n = 3` is the borderline at which the `3`-capacity of a
compact set in `R^3` vanishes, so exterior boundary excursions cost arbitrarily
little in amplitude but nothing forces `L^3` mass.) Theorem A forbids the
`eps^{1/2}` exterior mechanism outright.

**Bounded evidence, nominating only.** A finite-dimensional model of exactly this
configuration — `30` cells, the last `15` a "vanishing region", a `20`-dimensional
gradient subspace chosen inside `j(U)^perp` so that `U` is *its own* minimizer
(`U in M`), `U = 0` on the vanishing region, `h` supported in the other half —
gives `||z||_3/eps` and `||z_ext||_3/eps` **constant to four digits** over
`eps in [1e-6, 1e-2]` in every trial (values `0.87`–`1.34`), and
`||z_ext||_3/eps^{1/2} -> 0` like `eps^{1/2}` (scratchpad `chk3.py`). That
nominates Lipschitz continuity and refutes the `eps^{1/2}` exterior mechanism in
the model. It proves nothing about `R^3`: a finite-dimensional model has no
far field, no zero set of positive measure with infinitely many scales, and no
Calderón–Zygmund content.

---

## 5. The lattice: which `alpha` survive, and what it means for (G)

The lattice of candidate size bounds is [DI, hf21-crossing §3, review R2]

```
   L(alpha):   |K(v)| <= C d_1(v)^alpha Q(v)^{(1-alpha)/3} D_3(w(v))     (scaling-consistent for every alpha)
```

with `d_1 = ||q||_3`. The test family is `v_eps = U + eps h` of `rem:no-monotone`
[DI], for which the audited two-sided display gives
`|K(v_eps) + eps||U||_3^3| <= C_*|eps|^{3/2}`. The three hypotheses of the
audited Lemma R2 are: (i) `|K(v_eps)| >= c_0 eps` — holds for
`eps <= eps_1(U,h,C_*)` by the audited display; (ii) `Q(v_eps) >= q_0 > 0` —
holds unconditionally by `eq:cp-continuity` and `Q(U) = ||U||_3^3/3 > 0`;
(iii) `D_3(w(v_eps)) <= D` uniformly in `eps` — **a hypothesis, not audited**:
finiteness at each fixed `eps` follows from HF18-A for a smooth compactly
supported datum, but uniformity in `eps` needs a continuity of `D_3 ∘ w` that
the record does not contain. The audited Lemma R2 assumes it too; nothing below
is stronger than that assumption.

| `alpha` | status before this lane | status after |
|---|---|---|
| `alpha = 1` | audited true: `|K| <= C_# d_1 D_3(w)`, `C_# = (3/2)C_9 S` [DI hf21 (3.1)] | unchanged |
| `1 < alpha <= 3/2` | open | **open** (unchanged) |
| `3/2 < alpha <= 2` | open | **refuted** on any family satisfying (i)–(iii) |
| `alpha > 2` | refuted [DI, review R2.3] | refuted (subsumed) |

*Derivation of the new row.* By Corollary A3, `d_1(v_eps) <= C eps^{2/3}` with
`C = C(||U||_3, ||h||_3)`, unconditionally. Under (i)–(iii), `L(alpha)` forces
`c_0 eps <= C' d_1^alpha <= C'' eps^{2 alpha/3}`, i.e.
`eps^{1 - 2 alpha/3} <= const` as `eps -> 0`, impossible for `alpha > 3/2`. ∎

Two conditional refinements, both directions stated as the audit corrected them:

* If `u -> q(u)` **is** Lipschitz at `U in M` (`d_1(U+z) <= C(U)||z||_3`) and the
  first-order coefficient is nonzero (hypothesis (i)), then **no** `alpha > 1`
  bound exists and `alpha = 1` is sharp.
* Conversely, any `alpha in (1, 3/2]` bound would **force**
  `d_1(v_eps) >~ eps^{1/alpha}` with `eps^{2/3} >= eps^{1/alpha}`, i.e. would
  force the projection to be non-Lipschitz *and* to saturate Corollary A1 up to
  the exponent `2/3` when `alpha` is near `3/2`. The finite-dimensional probe
  found no saturation anywhere; that is nomination, not evidence against.

**What this does to (G).** Nothing directly: (G),
`int_0^tau ||q(u(t))||_3 D_3(w(t)) dt <= A_input(nu,u_0,H)`, is the `alpha = 1`
statement integrated in time, and it is untouched. What the lane fixes is the
**ceiling of the size route**: the best conceivable pointwise size improvement
over the audited `alpha = 1` is now confined to `alpha in (1,3/2]`, and even
that requires the projection to be non-Lipschitz at `M` with a rate in
`[2/3,1)`. Since (i) the audited HF20/`rem:no-monotone` obstruction already
excludes instantaneous energy-only absorption and universal monotonicity, and
(ii) HF18-A excludes closing by any monomial in `Q` and `D_3` by scaling, the
lane confirms rather than removes the standing route-level verdict: **(G) will
not be produced by improving the exponent in the size bound; it needs the
time-integrated cancellation inside `K`.** The one new leverage point is that
`d_1` at `M` is now known to be `o(eps^{1/2})`-small, i.e. the "good set" near
`M` is *smaller* than the audited record allowed, which strengthens the
crossing-measure statement's inputs but does not by itself remove the audited
obstruction O3.

---

## 6. NON-CLAIMS

* No claim that `u -> q(u)` is Lipschitz at `M`, or that it is not. The lane
  ends undecided, at a named external input.
* No claim about `(H1)`, `(H2)`, the weighted Calderón–Zygmund inequality, or
  the `L^2` projection bound of HF18-B. §4.3 asserts only that Lipschitz
  continuity at `|U|>0`-a.e. points *reduces to* an estimate of that class.
* No claim that `D_3(w(v_eps))` is uniformly bounded on the test family; the new
  lattice row is conditional on that, exactly as the audited Lemma R2 is.
* No claim that the linearisation `(LIN)` is *justified*: §4 derives it formally
  and then uses only statements about the linear operator itself. Nothing in §2,
  §3 or §5 depends on `(LIN)`; Theorem A and its corollaries never differentiate
  the minimizer and use only `L^3` membership.
* Corollary A1 improves the exponent displayed in `lem:quotient-stability` and
  Corollary A4 improves the remainder in `prop:quotient-derivative` **at points
  of `M`**. Neither is promoted, and the manuscript is not edited: both are
  candidates for audit first. No error in the manuscript is asserted — the
  audited statements are correct upper bounds, merely not sharp for small `h`.
* The numerics of §2 and §4.4 are bounded evidence at finite dimension and
  finite precision. They nominate; they never prove. Nothing load-bearing rests
  on them: Theorem A is proved in closed form from displayed manuscript
  inequalities.
* No priority or novelty claim of any kind, and no HIGH-STRAIN, HIGH-PRESSURE,
  CRITICAL, or NS-R3 result.

---

## 7. Cycle output

**MODE / RESULT:** DISCOVER with a falsifier arm / partial positive result plus a
negative structural result; the lane's question is **not decided**.

**CLAIM AND SCOPE:** (A) For every `u,h in L^3(R^3;R^3)`,
`int (|w(u)|+|w(u+h)|)|w(u+h)-w(u)|^2 <= 4 int (|w(u)|+|w(u+h)|)|h|^2`
(Theorem A), whence `||w(u+h)-w(u)||_3 <= (4W)^{1/3}||h||_3^{2/3}` and
`d_1(U+h) = O(||h||_3^{2/3})` at `U in M` — unconditional, scaling-consistent, no
regularity of the minimizer used, no derivative of the minimizer taken.
(B) Consequently no family realises the rate `1/2`; any non-Lipschitz witness has
rate in `[2/3,1)`. (C) Under the three hypotheses of the audited Lemma R2, the
lattice window narrows from `alpha in (1,2]` to `alpha in (1,3/2]`.
(D) Lipschitz continuity at `U in M` is equivalent, at points where `|U|>0` a.e.
and modulo justifying the linearisation, to an `L^3` gradient estimate for the
single scalar degenerate elliptic operator `-div(|U|(I+U^ ⊗U^ ) grad ·)`; that
operator is Lax–Milgram-invertible in its weighted energy space with exactly the
constant of Theorem A, and is non-invertible in `L^3` at every compactly
supported `U in M`, though its kernel is provably not a source of non-Lipschitz
behaviour.

**EVIDENCE:** closed-form proofs from `eq:cp-monotone`, `eq:cp-lipschitz`,
`lem:quotient-minimizer`(c), Cauchy–Schwarz and Hölder [all DI in
`../navier-paper/main.tex` `sec:quotient`]; the audited two-sided display of
`rem:no-monotone` [DI]; the audited Bregman comparison of hf21-crossing §1.2 and
its review §1.1 [DI]; HF21-A Theorem 2 / Corollary 2.2 for admissibility [DI];
two independent finite-dimensional oracles (`chk.py`, `chk3.py`, scratchpad),
bounded evidence only.

**FIRST GAP:** the weighted Calderón–Zygmund estimate
`||grad phi||_3 <= C(U)||h||_3` for `-div(a grad phi) = div(a h)`,
`a = |U|(I+U^ ⊗U^ )`, `|U| in L^3` — equivalently, any higher integrability
(`L^q`, `q>3`, or a localised reverse Hölder) for the minimizer displacement `z`.
Without it, Theorem A cannot be converted from the weighted `L^2` norm to `L^3`,
and the exponent stops at `2/3`.

**SURVIVING CONDITIONAL SUFFIX:** *if* the weighted estimate above holds at
`U in M` (equivalently, if `q` is `L^3`-Lipschitz at `U`), *and* the
`rem:no-monotone` family satisfies (i)–(iii), then `alpha = 1` in the size
lattice is sharp, no `alpha>1` member exists, and the size route is closed at
the audited bound `|K| <= C_# d_1 D_3(w)`; (G) is unaffected either way.

**NON-CLAIMS:** §6 in full.

**NEXT DISTINCT ACTION:** attack the first gap directly as a *localised* problem:
prove or refute a Caccioppoli-plus-reverse-Hölder inequality for `z = w'-w` in
the weighted norm of Theorem A, on balls where `|U|` is comparable to its mean —
i.e. ask whether Theorem A localises. HF21-A §6.2 records that Gehring cannot be
started from the *single-minimizer* Caccioppoli inequality; the two-point
weighted inequality proved here is a different object and has not been tested
against that obstruction. A second, cheaper distinct action: decide hypothesis
(iii), the uniform bound on `D_3(w(v_eps))` along the `rem:no-monotone` family,
which currently conditions both this lane's lattice row and the audited R2.

---

## Appendix: the two bounded-evidence probes, reproducibly

Recorded here in full because a probe that lives only in session scratch is not
reproducible (the defect recorded against HF19's Section 5). Both are
finite-dimensional counting-measure instances of the same abstract lemma; they
test algebra and nominate a rate, and neither is load-bearing.

**A. Algebra oracle for Theorem A (`chk.py`).** `n=12` cells in `R^3`, random
`10`-dimensional subspace `G` of `R^{36}` playing the role of `G_3`, random `u`,
random `h` with `||h||_3` log-uniform over three decades; minimizers by L-BFGS on
`c -> F(u+Gc)` with analytic gradient `G^T j(u+Gc)`; `200` trials. Checked each
trial: Euler–Lagrange residual `< 1e-6`; the cancellation identity
`<j(w')-j(w), z-h> = 0`; `N^2 <= 4 M_h^2` (Theorem A); `||z||_3^3 <= N^2`;
`||z||_3^3 <= 4 W ||h||_3^2` (Corollary A1); and the audited
`||z||_3^2 <= 2(||w||_3+||w'||_3)||h||_3` (`eq:cp-strong`). Result: `0` failures.

**B. Rate probe at a model point of `M` (`chk3.py`).** `n=30` cells, cells
`15..29` a "vanishing region"; `U` random on cells `0..14` and `0` elsewhere;
`G` a random `20`-dimensional subspace of `{g : <j(U),g> = 0}`, so that `U`
satisfies the Euler–Lagrange condition exactly and `w(U)=U` (verified to
`1e-8`), i.e. `U` is a model point of `M` vanishing on an open region while the
"gradient" directions still reach into that region; `h` supported on cells
`0..14`; `eps in {1e-2,...,1e-6}`. Reported per trial: `||z||_3/eps`,
`||z_ext||_3/eps`, `||z_ext||_3/eps^{1/2}`, `N^2/(4M_h^2)`,
`||z||_3^3/(4M_h^2)`. Observed over four trials: the first two ratios constant
to four significant figures across five decades of `eps` (values `0.87`–`1.34`),
the third decaying like `eps^{1/2}`, `N^2/(4M_h^2) ~ 0.14` (Theorem A not
saturated), `||z||_3^3/(4M_h^2) = O(eps)` (Corollary A1 not saturated, as
Lipschitz behaviour requires).

Scripts (Python 3, numpy + scipy):

```python
# A
import numpy as np
from scipy.optimize import minimize
rng=np.random.default_rng(0); n,d,m=12,3,10
F=lambda v: np.sum(np.linalg.norm(v,axis=1)**3)/3.0
j=lambda v: np.linalg.norm(v,axis=1)[:,None]*v
L3=lambda v:(np.sum(np.linalg.norm(v,axis=1)**3))**(1/3)
def minim(u,G):
    f=lambda c: F(u+(G@c).reshape(n,d)); g=lambda c: G.T@j(u+(G@c).reshape(n,d)).reshape(-1)
    r=minimize(f,np.zeros(G.shape[1]),jac=g,method='L-BFGS-B',
               options={'ftol':1e-16,'gtol':1e-14,'maxiter':20000})
    return u+(G@r.x).reshape(n,d)
bad=0
for _ in range(200):
    G=rng.standard_normal((n*d,m)); u=rng.standard_normal((n,d))
    h=10.0**rng.uniform(-3,0)*rng.standard_normal((n,d))
    w=minim(u,G); w2=minim(u+h,G); z=w2-w
    S=np.linalg.norm(w,axis=1)+np.linalg.norm(w2,axis=1)
    N2=np.sum(S*np.linalg.norm(z,axis=1)**2); Mh2=np.sum(S*np.linalg.norm(h,axis=1)**2)
    W=(np.sum(S**3))**(1/3)
    ok=(N2<=4*Mh2*(1+1e-8)) and (L3(z)**3<=N2*(1+1e-8)) and (L3(z)**3<=4*W*L3(h)**2*(1+1e-8)) \
       and (L3(z)**2<=2*(L3(w)+L3(w2))*L3(h)*(1+1e-8)) \
       and abs(np.sum((j(w2)-j(w))*(z-h)))<1e-6 and np.abs(G.T@j(w).reshape(-1)).max()<1e-6
    bad+= (not ok)
print("failures:",bad)

# B
from scipy.linalg import null_space
rng=np.random.default_rng(3); n,d,IN=30,3,15
def minim2(u,G):
    f=lambda c: F(u+(G@c).reshape(n,d)); g=lambda c: G.T@j(u+(G@c).reshape(n,d)).reshape(-1)
    r=minimize(f,np.zeros(G.shape[1]),jac=g,method='L-BFGS-B',
               options={'ftol':1e-20,'gtol':1e-18,'maxiter':200000})
    return u+(G@r.x).reshape(n,d)
for trial in range(4):
    U=np.zeros((n,d)); U[:IN]=rng.standard_normal((IN,d))
    NS=null_space(j(U).reshape(-1)[None,:]); G=NS@rng.standard_normal((NS.shape[1],20))
    assert np.abs(minim2(U,G)-U).max()<1e-8
    hd=np.zeros((n,d)); hd[:IN]=rng.standard_normal((IN,d)); hd/=L3(hd)
    for eps in [1e-2,1e-3,1e-4,1e-5,1e-6]:
        w2=minim2(U+eps*hd,G); z=w2-U
        S=np.linalg.norm(U,axis=1)+np.linalg.norm(w2,axis=1)
        N2=np.sum(S*np.linalg.norm(z,axis=1)**2); Mh2=np.sum(S*(eps*np.linalg.norm(hd,axis=1))**2)
        print(eps, L3(z)/eps, L3(z[IN:])/eps, L3(z[IN:])/eps**0.5, N2/(4*Mh2), L3(z)**3/(4*Mh2))
```

## Open Questions

- needs review: Corollary A1 improves the exponent displayed in
  `lem:quotient-stability` (`eq:cp-strong`) from `1/2` to `2/3` and Corollary A4
  improves the remainder of `prop:quotient-derivative` at points of `M` from
  `3/2` to `4/3`. Both are proved here from displayed manuscript inequalities and
  neither is promoted; an independent audit is required before any manuscript
  edit, and the audit should check in particular the step `|z| <= S` and the
  Cauchy–Schwarz step in `L^2(S dx)`.
- needs review: hypothesis (iii) of §5, the uniform bound
  `D_3(w(U+eps h)) <= D` along the `rem:no-monotone` family, is assumed and not
  audited; it conditions both the new lattice row and the audited Lemma R2.
- needs review: whether Theorem A localises to balls (a two-point weighted
  Caccioppoli inequality), which is the stated first gap and is a different
  object from the single-minimizer Caccioppoli inequality that HF21-A §6.2
  reports Gehring cannot be started from.
