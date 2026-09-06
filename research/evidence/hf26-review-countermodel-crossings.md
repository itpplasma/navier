# Audit of HF26, Sections 7-8 and Appendix `app:positive`: the concentrating countermodel and the crossing claim

**AUDIT STATUS (2026-09-06).** Independent adversarial audit of one scope of the
frozen HF26 candidate. MODE: proof-audit. This review owns exactly one file,
the present one. No other file in any repository is edited; `PLAN.md`, `docs/`,
the manuscript and the claim graph are untouched; nothing is committed or
pushed; **no result is promoted and no graph node changes.**

**Frozen target.**

```
file    research/evidence/hf26-temporal-continuation.tex
sha256  24b538280c8639b81a1f6f86d4c72370362625ca8a52d1d81a99b29236a540ab
lines   1432
repo HEAD at audit start  5b2e3891f12f55b3530174bf2c1c1dc2cfca6408
```

Note: `PLAN.md` was being edited by the controller while this audit ran (it grew
from 1452 to 1556 lines mid-session, with the HF26 section renumbering twice).
Every `PLAN.md` correction below is therefore anchored to **unique wording**, not
to a line number; the line numbers given are those observed at the 1506-line
state and were re-confirmed present, verbatim, at the 1556-line state.

---

## 0. Scope

Audited here, and nothing else:

- Section 7 `sec:crossing`, "What a scalar modulus and a crossing count do not
  say" (tex lines 899-918), including `eq:scalarvector` and the smooth scalar
  example.
- Section 8 `sec:curve`, "A concentrating comparison curve with actual
  minimizing representatives" (tex lines 919-1021): `eq:balancedseed`,
  `eq:scaleobjects`-`eq:scaleK`, `eq:seedbalance`, `thm:curve`, the
  fourth-power remark, `cor:curveenstrophy`, and the subsection "Why the curve
  is not a Navier-Stokes counterexample" including `eq:residualcurve` and
  `eq:invisible`.
- Appendix `app:positive` (tex line 1286 to 1373), "The inherited compact
  positive-work field used in the comparison curve", which supplies the seed
  `W_0` with `K(W_0) > 0`.
- The countermodel rows of the controller's index note
  `hf26-temporal-continuation.md`, redone independently rather than trusted.

Used as premises inside their audited scope, not re-audited: `eq:divcurl`
(imported HF23), `eq:Didentity`/`eq:Dcontrol` (`app:weighted`, a different
scope), `eq:Qprime`, `eq:coercivity`, `eq:Kq`, the local well-posedness package,
and the ESS/GKP endpoint theorem.

Method: every scaling exponent was re-derived from `S_lambda v(x) = lambda
v(lambda x)` from scratch, symbolically in `sympy` and again by quadrature on
the explicit seed field; the controller's table was not consulted until after
my own numbers existed. Scripts are throwaway and were run in the session
scratchpad.

---

## 1. VERDICT

**PASS WITH SCOPE.**

One-line justification: every identity, the seed construction, the enstrophy
corollary, the fourth-power divergence, the invisibility relations and the
scalar crossing example are correct exactly as written and reproduce under
independent derivation; the mathematics contains no error I could find in nine
attempts, but the *exclusion it licenses is materially narrower* than the
controller's index note and `PLAN.md` currently paraphrase it, and three
scope facts that decide how narrow are absent from the document itself.

The countermodel is real. It is not "an exclusion that violates nothing at the
scalar level". It violates at least three scalar things, one of which is a
scalar identity our own record uses.

---

## 2. Per-question findings

### Q1. `thm:curve`: every claimed identity, derived independently

**VERDICT: all correct, all exact. No discrepancy with the controller's table.**

Scaling laws, derived from `S_lambda v(x) = lambda v(lambda x)` with amplitude
`b > 0`, i.e. `u = b S_lambda v`. Verified symbolically term by term (chain
rule for `grad`, `Delta`, `N`), then combined with the volume factor
`d^3x = lambda^{-3} d^3y`:

| object | pointwise factor at `lambda x` | volume | net |
|---|---|---|---|
| `u` | `b lambda` | - | - |
| `grad u` | `b lambda^2` | - | - |
| `Delta u` | `b lambda^3` | - | - |
| `N(u)` | `b^2 lambda^3` | - | - |
| `A(u) = \|w\|w` | `b^2 lambda^2` | - | - |
| `E = \|u\|_2^2` | `(b lambda)^2` | `lambda^{-3}` | `b^2 lambda^{-1}` |
| `Y = \|grad u\|_2^2` | `(b lambda^2)^2` | `lambda^{-3}` | `b^2 lambda` |
| `\|u\|_3^3` | `(b lambda)^3` | `lambda^{-3}` | `b^3`, `lambda`-invariant |
| `D = -<A, Delta u>` | `b^2 lambda^2 * b lambda^3` | `lambda^{-3}` | `b^3 lambda^2` |
| `K = -<A, N(u)>` | `b^2 lambda^2 * b^2 lambda^3` | `lambda^{-3}` | `b^4 lambda^2` |
| `Q = (1/3)\|w\|_3^3` | - | - | `b^3`, `lambda`-invariant |
| `\|q\|_3` | - | - | `b`, `lambda`-invariant |

So `E = lambda^{-1}E_W`, `Y = lambda Y_W`, `Q` invariant, `||q||_3` invariant,
`D ~ lambda^2`, `K ~ lambda^2`: all five as claimed, and `eq:scaleQD`,
`eq:scaleK` are reproduced exactly.

The four ODE-level identities, each recomputed in `sympy` and again numerically
at two independent parameter sets:

- `lambda' - lambda^3/(2T_c) = 0` exactly.
- With `T_c = E_W/(4 nu Y_W)`: `E' + 2 nu Y = 0` **identically in `t`**, and the
  integrated form `E(t) + 2 nu \int_0^t Y = E_W` holds with the correct
  constant. (This is not a coincidence of one instant; the two sides have the
  same `lambda^3` scaling, and the constant `T_c` is exactly what matches them.)
- `Q' + nu D - K = 0` exactly, with `Q' = 0` (Q is `lambda`-invariant) and
  `K(t) = lambda^2 K(W) = nu lambda^2 D(W) = nu D(t)` by `eq:seedbalance`.
  Consistency cross-check: the chain rule `eq:Qprime` gives
  `Q' = <A(v), v_t> = (lambda'/lambda) <A(W), Z>`, and I verified
  `<A(W), Z> = 0` independently, by integration by parts rather than by
  differentiating the invariance: `<A(W), W> = ||w||_3^3 = 3Q` (stationarity
  kills `q`), and `<A(W), (x.grad)W> = -3Q` (because
  `j(w).(x.grad)w = (1/3)(x.grad)|w|^3` integrates to `-||w||_3^3`, and
  `(x.grad)q + q` is again in `G_3` so its pairing vanishes). Sum zero. The two
  routes agree.
- `G_v(tau) = \int_0^tau ||q||_3 D dt = d_W D(W) T_c log(1/(1 - tau/T_c))`,
  verified symbolically and numerically to 1e-8 at four values of `tau/T_c`;
  `-> +infinity` as `tau -> T_c^-`.
- `Y' = 2 nu Y^3/(E_W Y_W)` exactly (the controller's sixth row).

Additional budget checks the document asserts but does not compute, all of which
I verified and all of which hold:
`\int_0^{T_c} Y = E_W/(2 nu)` exactly (consistent with the energy identity and
with `2 T_c Y_W`); `\int_0^{T_c} ||grad q||_2^2 <= E_W/(8 nu)`;
`\int_0^{T_c} ||q||_3^4 = T_c d_W^4 <= 4 S^2 E_W^2/nu <= 8 S^2 E_W^2/nu`, i.e.
the curve satisfies `eq:qbudgets` **with the document's own constant**;
`\int_0^{T_c} ||v||_3^4 = T_c ||W||_3^4 <= S^2 E_W^2/(4 nu) <= S^2 E_W^2/(2 nu)`,
i.e. it satisfies `eq:u34` too. This matters: the countermodel is not merely
"finite" on the energy-level budgets, it obeys them with the same constants a
real trajectory does.

The controller's six-row table is **correct in every row**. I found no algebra
error in it.

### Q2. Are the slices genuine fields with actual variational objects?

**VERDICT: yes, and the commutation is a theorem, not an analogy.**

`w(b S_lambda v) = b S_lambda w(v)` follows from three facts, each of which I
checked rather than assumed:

1. `S_lambda` maps `G_3` **onto** `G_3`. Proof:
   `(S_lambda grad phi)(x) = lambda (grad phi)(lambda x) = grad_x[phi(lambda x)]`
   and `phi(lambda .) \in C_c^\infty`, so `S_lambda(grad C_c^\infty) =
   grad C_c^\infty`; `S_lambda` is an `L^3` isometry, so it maps the `L^3`
   closure onto the `L^3` closure; `S_{1/lambda}` is the inverse. Verified
   symbolically.
2. `F(z) = (1/3)||z||_3^3` is `S_lambda`-invariant and satisfies
   `F(bz) = b^3 F(z)` for `b > 0`; `G_3` is a linear subspace so `b G_3 = G_3`.
3. `F` is strictly convex on the reflexive space `L^3`, so the minimizer over
   the closed affine set `v + G_3` is unique.

Hence the bijection `z -> b S_lambda z` carries `v + G_3` onto
`b S_lambda v + G_3` and rescales `F` by the constant `b^3`, so it carries the
unique minimizer to the unique minimizer. `q`, `A`, `Q`, `D`, `K` then transform
as tabulated. Every `v(t)` is real, smooth, compactly supported and solenoidal
(the seed is, and `S_lambda` preserves all three), so `D` and `K` are finite
pairings of an `L^{3/2}` field against an `L^3` field. This is a genuine
countermodel, not a formal analogy.

The document's one-line justification ("The first two follow by applying the
invertible transformation to all competitors") is correct but compresses step 1,
which is the only step with content. See R12.

### Q3. The seed: does `app:positive` produce a compact smooth solenoidal `W_0` with `K(W_0) > 0`?

**VERDICT: yes. The construction is correct at every step I could test, and the
positivity is real. The countermodel does not collapse.**

Checked symbolically (all exact, all reproduced):

- `U_s = rho(r,z) e_theta` with `rho = b_0(4r-6) b_0(2z)` is smooth (it vanishes
  identically for `r < 5/4`, so the `e_theta` singularity on the axis is not
  reached), compactly supported in `{5/4 <= r <= 7/4, |z| <= 1/2}`, and
  `div U_s = 0`.
- `div j(U_s) = div(rho^2 e_theta) = 0`, hence `<j(U_s), grad phi> = 0` for all
  `phi \in C_c^\infty`, hence by `eq:stationarity` and convexity
  **`w(U_s) = U_s`** and `q(U_s) = 0`. This is the load-bearing fact and it is
  correct.
- `N(U_s) = -rho^2 e_r / r` exactly; `U_s . N(U_s) = 0`; `j(U_s) . N(U_s) = 0`
  pointwise, so `<A_0, N_0> = 0`.
- `curl a = (x, y, -2z) = grad phi` exactly, so `h = g` wherever `zeta = 1` and
  `e = h - g` vanishes there.
- The support geometry closes: `max |x|` on `supp U_s` is
  `sqrt((7/4)^2 + (1/2)^2) = 1.8200 < 3`, and `zeta` is identically `1` on
  `|x| <= 3`; I evaluated the explicit `zeta` formula and it returns exactly
  `1` at `|x| = 0, 1.82, 2.9, 3.0`, `0.51` at `3.5`, `0` at `4.0` and beyond.
  Its denominator never vanishes because `9 < 16`. So `supp e \subset
  {3 <= |x| <= 4}` is disjoint from `supp U_s`, which is what makes
  `F(U_s + eps e) = F(U_s) + C_e|eps|^3` an identity rather than an estimate.
- `U_s . h = 0` and `grad h = diag(1,1,-2)` and `(U_s.grad)h = U_s` exactly.
- `d_eps = w(v_eps) - U_s` lies in `eps h + G_3`, and `<j(U_s), h> = 0`
  pointwise on `supp rho`, so `<j(U_s), d_eps> = 0`: the Bregman identity
  `Q(v_eps) - Q(U_s) = \int B(U_s, d_eps)` is exact and `eq:appendgain` follows
  from `eq:Bbelow` with the stated constants `4C_e|eps|^3` and `6C_e|eps|^3`.
- First-order coefficients: `A_0 . (h.grad)U_s = h . grad(rho^3/3)` **pointwise**
  (verified symbolically), which integrates to `-\int (div h) rho^3/3 = 0` since
  `div h = 0`; and `A_0 . (U_s.grad)h = |U_s|^3` pointwise, so
  `<A_0, (U_s.grad)h> = ||U_s||_3^3 = c_0`. Both exactly as claimed.
- The refined `N_0` pairing: `|N_0| <= rho^2` uses `r >= 5/4 > 1` on the
  support, correct; the Cauchy-Schwarz split on `rho^{1/2}|d_eps|` against
  `rho^{5/2}` gives exactly `4 sqrt(C_e) ||U_s||_5^{5/2} |eps|^{3/2}`, and the
  remaining term exactly `4 C_e ||U_s||_\infty |eps|^3`. Correct.
- `||A_eps - A_0||_{3/2} <= (2M + d_0) d_0 |eps| = L|eps|` for `|eps| <= 1`,
  from `|j(x) - j(y)| <= (|x| + |y|)|x - y|` and `||d_eps||_3 <= d_0|eps|`.
  Correct.
- Term-by-term reassembly of `K(v_eps) = -<A_eps, N(v_eps)>` reproduces
  `eq:appendK` with **exactly** the displayed `C_*`; every one of the five
  remainder terms is `<= C_j |eps|^{3/2}` for `|eps| <= 1` with the constant the
  document assigns to it. Correct.
- The sign flip is legitimate: `eq:appendK` is stated for `|eps| <= 1` and every
  intermediate bound uses `|eps|`, so substituting `eps -> -eps` is licensed and
  `W_0 = U_s - eps h` gives `|K(W_0) - c_0 eps| <= C_* eps^{3/2}`. With
  `sqrt(eps) < c_0/(2 max{1, C_*})` this yields `C_* eps^{3/2} < c_0 eps/2`, so
  `K(W_0) > c_0 eps/2 > 0`. Correct.

Checked by quadrature on the explicit bump (the constants are the real ones, not
placeholders):

```
c_0 = ||U_s||_3^3            = 2.134085536e-3   > 0
E_{U_s} = ||U_s||_2^2        = 2.086635893e-2
Y_{U_s} = ||grad U_s||_2^2   = 1.293673695
D(U_s)  via  \int rho(|grad w|^2 + |grad rho|^2)   = 0.1293963582
D(U_s)  via  -<A, Delta u>                        = 0.1293963445   (rel 1.1e-7)
E_{U_s} Y_{U_s}              = 2.699425965e-2   > 0
```

The two independent evaluations of `D(U_s)` agree to finite-difference
accuracy, which is also an independent spot-check of `eq:Didentity` on a real
field. `D(U_s) > 0`, `c_0 > 0`, `E_{U_s} Y_{U_s} > 0`: all three positivity
facts the corollary needs.

One simplification worth taking (R8): the document proves `d_W > 0` through
`eq:workform`, which carries integrability side conditions. It is one line
without it: if `q(W) = 0` then `w = W`, so
`j(W).(W.grad)W = (1/3)(W.grad)|W|^3` integrates to zero by `div W = 0`, hence
`K(W) = 0`, contradicting `K(W) = nu D(W) > 0`.

### Q4. `eq:seedbalance`, `b = nu D_0/K_0`

**VERDICT: correct.** `K(bW_0) = b^4 K_0` and `D(bW_0) = b^3 D_0` (verified in
Q1), so `K(W)/(nu D(W)) = b K_0/(nu D_0) = 1` at `b = nu D_0 / K_0`. The
one-power-of-`b` gap between the two exponents is exactly what makes a single
amplitude solve the balance, and `b > 0` is guaranteed by `K_0 > 0`, `D_0 > 0`.
Because `K` and `D` share the same `lambda^2` weight, the balance then holds at
**every** time along the curve, not just at `t = 0`. This is the mechanism, and
it is sound.

### Q5. `cor:curveenstrophy`

**VERDICT: correct, and if anything understated. Two wording repairs.**

The reduction is exact: `Y' = 2 nu Y^3/(E_W Y_W)` so `Y' <= C_E nu^{-3} Y^3`
holds for all `t` iff `E_W Y_W >= 2 nu^4 / C_E`, which is verbatim the
condition the proof imposes.

The limit holds. As `eps -> 0`: `c_0`, `C_e`, `C_*`, `L`, `d_0` are all
`eps`-independent (they are built from `U_s` and `e` alone), so
`K_0 \in [c_0 eps/2, c_0 eps + C_* eps^{3/2}] -> 0^+`;
`D_0 = -<A(W_0), Delta W_0> -> -<A(U_s), Delta U_s> = D(U_s) > 0` by
`eq:Alip` (`A` Lipschitz `L^3 -> L^{3/2}`) against `Delta W_0 -> Delta U_s` in
`L^3`; hence `b = nu D_0/K_0 >= nu D(U_s)/(2 c_0 eps) -> infinity`; and
`E_{W_0} Y_{W_0} -> E_{U_s} Y_{U_s} > 0`, so
`E_W Y_W = b^4 E_{W_0} Y_{W_0} -> infinity`. The constant `C_E` is fixed first
and `eps` chosen after, so the corollary does deliver a **prescribed** constant,
not a freely adjusted or time-dependent one. That part of the claim is correct
as stated.

Note `T_c = E_{W_0}/(4 nu Y_{W_0})` is amplitude-independent and converges to
`E_{U_s}/(4 nu Y_{U_s})`, so the horizon does **not** shrink as `C_E -> 0`. The
divergence of `G` is therefore not bought by shrinking the interval.

Two repairs. (i) "the same comparison curve" is wrong wording: it is a
**different** curve, built from a different seed; `thm:curve` re-applies to it,
which is what makes the corollary work, but the sentence should say so (R6).
(ii) The corollary should be stated in the form our own record actually uses.
The standard enstrophy inequality retains the good term,
`Y' <= -2 nu ||Delta u||_2^2 + C nu^{-3} Y^3`. I checked that the curve
satisfies **that** form too, for large `b`: both sides scale as `lambda^3`, so
it reduces to `2 nu Y_W^2/E_W + 2 nu ||Delta W||_2^2 <= C_E nu^{-3} Y_W^3`,
whose left side is `O(b^2)` and right side `O(b^6)`. So the corollary is
strictly stronger than stated and should be stated in the stronger form (R5),
otherwise a reader can wrongly hope that keeping the good term escapes the
countermodel.

### Q6. The HF25 fourth-power defect integral

**VERDICT: correct, including `sigma_W != 0`.**

`w(v(t)) = S_lambda w(W)` gives `sigma(v(t))(x) = lambda^2 sigma_W(lambda x)`,
so `||sigma(v(t))||_2^2 = lambda^4 lambda^{-3} ||sigma_W||_2^2 =
lambda ||sigma_W||_2^2`, exactly as claimed, and
`\int_0^{T_c} ||sigma||_2^4 dt = ||sigma_W||_2^4 \int_0^{T_c} lambda^2 dt` is
logarithmically divergent (confirmed symbolically and numerically).

`sigma_W != 0`: if `sigma_W = 0` then `||grad q(W)||_2 = ||div w(W)||_2 = 0` by
`eq:divcurl`, so `q(W)` is constant, and `q(W) \in L^6` forces `q(W) = 0`,
contradicting `d_W > 0`. The document stops at "`q(W) = 0`" and does not name
the contradiction; add the last clause (R8).

Two consistency facts worth recording, because they show HF25 and HF26 do not
collide. First, the **square** budget stays finite on the curve:
`\int_0^{T_c} ||sigma||_2^2 = 2 T_c ||sigma_W||_2^2 <= E_W/(8 nu)`, which is
`eq:qbudgets` again. So the curve realises precisely the square-to-fourth-power
gap that `PLAN.md`'s "sharpened first gap" section names, and does so with
actual fields. Second, the curve does **not** violate HF25's proved
differential inequality `Q' <= -(nu/2)D + C_sigma nu^{-3}||sigma||_2^4 Q`: both
sides scale as `lambda^2`, so it reduces to
`(nu/2) D(W) <= C_sigma nu^{-3} ||sigma_W||_2^4 Q(W)`, i.e. `O(b^3) <= O(b^7)`,
true for the amplitudes in play. What fails on the curve is HF25's
**hypothesis**, not its theorem.

### Q7. SCOPE. What the curve excludes and what it does not

This is where the audit bites. `eq:invisible` and `eq:residualcurve` are both
correct; the document's own restraint is correct; but the exclusion is narrower
than our record currently states.

**`eq:residualcurve` verified.** `v_t = lambda' Z(lambda x)` with
`Z = W + (x.grad)W`, and `lambda'/lambda^3 = 1/(2T_c) = 2 nu Y_W/E_W = c_W`
exactly; `P` commutes with dilations (degree-zero homogeneous multiplier); so
`R(t,x) = lambda^3 R_W(lambda x)` with `R_W = c_W Z + P N(W) - nu Delta W`.
Correct.

**`eq:invisible` verified, twice.** `<W, Z> = -E_W/2` (I re-derived it from
`\int (x.grad)f = -3\int f` and confirmed it by quadrature on `U_s`:
`-1.043317946e-2` against `-E/2 = -1.043317946e-2`); `<W, P N(W)> = 0`;
`-nu<W, Delta W> = nu Y_W`; and `c_W` cancels them. `<A(W), Z> = 0` (verified
two independent ways, see Q1; quadrature on `U_s` returns `-1.6e-14`);
`<A(W), P N(W)> = -K(W)`; `-nu <A(W), Delta W> = nu D(W)`; and `eq:seedbalance`
cancels them.

**A structural fact the document does not state, and which decides the scope.**
The two invisibility relations are not extra information. They are literally the
two balances:

```
   <v, R>      =  (1/2)(E' + 2 nu Y)
   <A(v), R>   =  Q' + nu D - K
```

So `eq:invisible` **is** `eq:curveenergy` and `eq:curveQ`, restated. That is the
exact statement of what the countermodel is: a curve tuned so that the residual
is orthogonal to the two test fields `v` and `A(v)`, and to nothing else.

**The exact mechanism class excluded.** Any derivation of `eq:Gtarget` (or of
`eq:signedtarget` with `theta < 1`) whose premises are contained in the
following closed list:

- (P1) each `u(t)` is a real solenoidal Schwartz field and `w, q, A, Q, D, K`
  are its actual variational objects, with every instantaneous identity and
  inequality of `sec:foundations` (`eq:stationarity`, `eq:coercivity`,
  `eq:divcurl`, `eq:Didentity`, `eq:Dcontrol`, `eq:gradA`, `eq:Kq`,
  `eq:workform`);
- (P2) `<u(t), R(t)> = 0`, i.e. the exact energy identity `E' + 2 nu Y = 0`
  and its integrated form;
- (P3) `<A(u(t)), R(t)> = 0`, i.e. the exact quotient balance `Q' + nu D = K`;
- (P4) every energy-level spacetime budget, `eq:energy`, `eq:qbudgets`,
  `eq:u34`, with the document's own constants;
- (P5) any amount of regularity, continuity, modulus or crossing information
  about the **scalar** `t -> ||q(t)||_3` (the curve makes it constant, so it
  satisfies every modulus and has zero crossings of every level other than
  `d_W`);
- (P6) the cubic enstrophy differential inequality with any prescribed
  input-only constant, in either the plain or the good-term form;
- (P7) boundedness of the critical norm `sup_t ||u(t)||_3` and of `sup_t Q`.

I verified the curve satisfies all seven. That list is the mechanism class.

**What is NOT excluded.** Five things, each of which the curve fails, and none
of which the document mentions:

1. **Any smallness threshold on the scalar distance.** From
   `K = nu D`, `D > 0` and `eq:Kq` (`|K| <= C_sharp ||q||_3 D`), every curve of
   `thm:curve` is *forced* to satisfy

   ```
      C_sharp ||q(t)||_3  >=  nu        for every t,   hence
      ||v(t)||_3          >=  nu/(2 C_sharp)   (by ||q||_3 <= 2||v||_3).
   ```

   The countermodel therefore lives entirely inside the bad set
   `{C_sharp ||q||_3 > nu}` and can never be a small-data or near-Hodge object.
   Anything that closes the route by driving `||q||_3` below `nu/C_sharp` is
   untouched. This is a two-line consequence of the document's own `eq:Kq` and
   it is **absent from the document** (R1).
2. **A vector modulus for `t -> q(t)` in strong `L^3`.** The curve violates it,
   which is exactly why `thm:temporal` is not refuted by it. The document says
   this in `sec:crossing`; it should say it again in `sec:curve`.
3. **The enstrophy identity.** A third scalar test, `<Delta v, R>`, sees the
   residual. From `<Delta W, Z> = -Y_W/2` (differentiate `lambda Y_W`),

   ```
      <Delta W, R_W> = -nu Y_W^2/E_W + <Delta W, P N(W)> - nu ||Delta W||_2^2
                     = b^2 [ b S_0 - nu (Y_0^2/E_0 + ||Delta W_0||_2^2) ],
      S_0 := <Delta W_0, N(W_0)>            (P Delta W_0 = Delta W_0).
   ```

   For the constructed seed, `<Delta U_s, N(U_s)> = 0` pointwise (azimuthal
   against radial), so `S_0 = -eps <Delta U_s, N_1> + O(eps^2)` and
   `b S_0/nu -> -D(U_s)<Delta U_s, N_1>/c_0` as `eps -> 0`. I computed both
   sides by quadrature:

   ```
      lim b S_0 / nu                        = 110.15
      Y_0^2/E_0 + ||Delta U_s||_2^2         = 569.15   ( = 80.21 + 488.94 )
   ```

   Not equal, so `<Delta v, R> != 0` for small `eps`, i.e. **the enstrophy
   identity detects the residual on exactly the curves `cor:curveenstrophy`
   constructs.** Any argument that uses the enstrophy identity (as opposed to
   the enstrophy inequality of (P6)) is not excluded (R4).
4. **`eq:signedtarget` at `theta = 1`.** On the curve `\int K = nu \int D`
   exactly, so `eq:signedtarget` holds with `theta = 1` and `A = 0`. The curve
   refutes the signed route only for `theta < 1`. And `theta = 1` is already
   enough for the programme: `Q(tau) - Q_0 = \int K - nu \int D <= A`, so
   `sup Q < infinity`, hence `sup ||u||_3 < infinity`, hence the endpoint
   theorem. The document permits `0 <= theta <= 1` in `eq:signedtarget` and does
   not note that its own countermodel misses the endpoint case (R9).
5. **Anything that uses `R = 0` beyond the two projections `<v, .>` and
   `<A(v), .>`**: the vorticity equation, the local energy inequality, the
   pressure representation as an identity for the flow, higher projections such
   as `<partial_h A(v), .>`, or the endpoint theorem itself.

**The document's restraint is correct and must be preserved.** The closing
sentence, "This theorem makes no claim that a scalar modulus is insufficient
*together with every consequence of the full equation*; that broader assertion
has not been proved", is exactly right and is the sentence our record must
inherit. But two further restraints belong beside it:

- The curve satisfies `sup_t ||v(t)||_3 < infinity` and `sup_t Q < infinity`,
  i.e. **the very conclusion the (G)-route is trying to establish**. It is a
  countermodel to the derivability of a chosen *sufficient certificate*, not to
  the target, and not evidence of any kind about blow-up (R10).
- The curve is exactly the backward self-similar ansatz. With
  `lambda(t) = sqrt(T_c)/sqrt(T_c - t)`, `v(t,x) = (T_c - t)^{-1/2}
  Phi(x/sqrt(T_c - t))` with `Phi(y) = sqrt(T_c) W(sqrt(T_c) y)` compactly
  supported. `R != 0` therefore follows directly from Necas-Ruzicka-Sverak
  (1996) and Tsai (1998) on nonexistence of nontrivial backward self-similar
  solutions with profile in `L^3`, without the endpoint theorem. The document's
  ESS/GKP argument is correct (constant `||v||_3`, divergent `H^1`, uniqueness,
  endpoint continuation) but it is the indirect route and it cites neither NRS
  nor Tsai (R7). Naming the ansatz also clarifies *what mechanism* has been
  excluded, which is the practically useful form.

### Q8. `sec:crossing`, and what our own record must say

**The example is correct.** For `d(t) = d_* + eps e^{-1/(1-t)^2} sin(1/(1-t))`
on `[0,1)`, `d(1) = d_*`:

- Every derivative of `e^{-1/s^2} sin(1/s)` is
  `e^{-1/s^2}[P_n(1/s) sin(1/s) + Q_n(1/s) cos(1/s)]`, which tends to `0` as
  `s -> 0^+`. I confirmed `d^n/dt^n -> 0` for `n = 0..5` in `sympy`. So `d`
  extends `C^\infty` to `[0,1]`, `d'` is continuous on a compact interval, hence
  bounded: I computed `sup_{[0,1)} |d/dt (e^{-1/(1-t)^2} sin(1/(1-t)))| =
  0.714994`, so `d` is Lipschitz with constant `0.715 eps`. **Lipschitz modulus
  confirmed.**
- `d(t) = d_*` exactly at `t_k = 1 - 1/(k pi)`, `k >= 1`, all in `[0,1)`,
  accumulating at `1`; the sign of `sin(1/(1-t))` strictly alternates on
  consecutive gaps (confirmed; an earlier "False" in my own run was a
  floating-point underflow of `e^{-1/(1-t)^2}` at `t = 0.99`, not a
  mathematical failure). **Infinitely many sign-changing crossings confirmed.**
- `|d - d_*| <= eps < d_*`, so `d > 0` throughout: a legitimate distance.
- The separated-threshold statement is correct: `omega` monotone and
  `omega(l) < b - a` force every `a -> b` passage to last longer than `l`, so at
  most `H/l` disjoint completed excursions fit in `[0,H]`. The note's
  `1 + H/l` is a safe over-count.
- The converse ("a finite crossing count supplies no modulus") is correct and
  trivial.

**Is `PLAN.md`'s equivalence WRONG, IMPRECISE, or UNDERSPECIFIED? It is
WRONG as literally written, and the error is confined to `PLAN.md`.**

The sentence at issue, `PLAN.md` "Convergence worth noting." (lines 1272-1275,
stable across the session's edits), verbatim:

> "Two lanes that did not share a question arrive independently at the same next
> target: an input-only modulus of continuity for the distance along the
> trajectory at the critical level, **equivalently** an input-only bound on the
> number of crossings of that level."

Three separate defects:

1. **"equivalently" is false in both directions.** Forward: a modulus does not
   bound crossings of a single level; the example is a Lipschitz function with
   infinitely many. Backward: a finite crossing count supplies no modulus at
   all. Neither implication holds, so no reading of "equivalently" survives.
2. **"crossings of that level" is the wrong object.** What a modulus does bound
   is disjoint traversals of a corridor of positive width. The forward
   implication is true only in that form.
3. **The observed object is unspecified**, and the two candidates are not
   equivalent: `|d(t) - d(s)| <= ||q(t) - q(s)||_3` runs one way only
   (`eq:scalarvector`). HF24 observes the scalar `d_1(t) = ||q(t)||_3`;
   HF26's `thm:temporal`/`cor:modulus` consumes the vector `t -> q(t)` in strong
   `L^3`. A scalar modulus, even if proved, would not feed HF26's producer.

**But the defect is in `PLAN.md`'s summary only. HF24 is already correct, and
HF26 confirms our own audit rather than challenging it.** This is the single
most important reconciliation finding of this audit, and it reverses the framing
now in `PLAN.md` ("Two claims of ours are challenged and are held pending
audit"):

- `hf24-modulus-of-continuity.md`, frontier packet, TARGET OF THIS LANE,
  verbatim: "an input-only modulus of continuity for `d_1(t) := ||q(u(t))||_3`
  ... at the level `nu/C_sharp` ... **equivalently an input-only lower bound on
  the time (or on some input-only spacetime cost) of a passage of `C_sharp d_1`
  across the corridor `[(1-2eps)nu, (1-eps)nu]`**". That is exactly HF26's
  separated-threshold formulation, written before HF26 arrived. The lane is
  precise; the plan's paraphrase dropped the corridor.
- The lane's FORBIDDEN INFERENCES already include "a modulus in the measure `mu`
  is NOT a modulus in `t`" and "a crossing-count bound is NOT (G)".
- `hf24-review-modulus-of-continuity.md`, Repair 15, verbatim: "The crossing
  count the lane claimed was corrected by the audit: only the components that
  reach the upper corridor wall are counted, which is what the bad set needs;
  **components that oscillate inside the corridor are not countable from the
  record.**" That is HF26 `sec:crossing`'s conclusion, reached independently by
  our own auditor, in the corridor currency, before HF26 was read.
- `hf24-modulus-of-continuity.md` section 5.2 item 3, verbatim: "**A crossing
  count is not implied by any summability the record provides.**"

So HF26 `sec:crossing` is **confirmatory** of the HF24 record and
**corrective** only of `PLAN.md`. No HF24 verdict needs revision on this point.

**A second, positive reconciliation finding.** HF24-A section 5.2's viscous-eddy
family (`A l = nu/C_sharp` at `Re ~ 1`, declared "a scaling-admissibility
computation, bounded evidence, not a solution and not a proof") is the heuristic
of which HF26's curve is a rigorous realisation. On the curve, amplitude
`~ lambda`, length `~ 1/lambda`, so `A l` is constant, and I showed above that
that constant is forced to satisfy `C_sharp A l >= C_sharp d_W >= nu`, which is
HF24-A's `Re ~ 1` condition. The differences are that HF24-A takes a dyadic
*sequence* of structures each crossing the level once, whereas HF26 takes one
continuously concentrating structure with `d_1` *constant*; and that HF26's
slices carry genuine variational objects. HF26 therefore upgrades HF24-A section
5.2 from a scaling table to an exact construction, at the price of the curve not
being a trajectory. That belongs in our record and is not currently there.

**A third finding: how HF26's countermodel relates to HF22-C, which our record
does not compare it against.** `hf22-good-set-dissipation.md` (audited REPAIR,
integrated) section 5 already proves a non-derivability theorem for (G) from the
enumerated constraints (T1)-(T9), and closes with, verbatim: "Any proof of (G)
must use structure that (T1)-(T9) do not encode: **the actual equation, the
actual minimizer, or a quantitative modulus that the audited record does not yet
supply.**" I checked that HF26's curve satisfies (T1)-(T9) with input-only
constants: (T1)-(T7) are instantaneous or follow from the energy identity, and
(T8)-(T9), the two constraints the HF22-C audit added, follow from instantaneous
facts plus `sup_t E(t) <= E_W` and the `L^4_t L^3_x` budget, both of which I
verified on the curve in Q1. So HF26's countermodel is the same species as
HF22-C's Theorem C',
strictly strengthened: it **closes two of HF22-C's three escapes** (it uses
actual minimizers, and it survives a perfect scalar modulus, indeed a constant
`d_1`), and leaves open exactly the third, "the actual equation". That is the
honest comparison, and it is sharper and more useful than "a sharper exclusion
than any the programme has recorded, because unlike every previous excluded
class it violates nothing at the scalar level", which is false (see Q7).

---

## 3. Required repairs

Numbered for the candidate document. None of these is a correctness fix; all
are scope, precision or citation fixes. R1, R4, R9, R10 are load-bearing for how
our record may use the result.

- **R1.** In `sec:curve`, after `eq:seedbalance`, add the forced lower bound:
  from `K(W) = nu D(W) > 0` and `eq:Kq`, every curve of `thm:curve` satisfies
  `C_sharp ||q(t)||_3 >= nu` and `||v(t)||_3 >= nu/(2 C_sharp)` for all `t`.
  State the consequence: the countermodel lies entirely in the bad set and
  excludes nothing about smallness of the scalar distance.
- **R2.** In "Why the curve is not a Navier-Stokes counterexample", record that
  `<v, R> = (1/2)(E' + 2 nu Y)` and `<A(v), R> = Q' + nu D - K`, so
  `eq:invisible` is logically identical to `eq:curveenergy` and `eq:curveQ`.
  Present `eq:invisible` as the identification of *which two* linear functionals
  of the residual are blind, not as independent information.
- **R3.** Replace the prose description of what the curve satisfies with an
  enumerated premise list (P1)-(P7) as in Q7 above, so the exclusion can be
  quoted and checked without re-deriving it.
- **R4.** Add the third scalar test. Display
  `<Delta W, R_W> = -nu Y_W^2/E_W + <Delta W, P N(W)> - nu ||Delta W||_2^2` and
  state that it is not zero for the seeds of `cor:curveenstrophy`, so the
  enstrophy *identity* is a scalar functional of the residual that the curve
  does not hide from. Without this the reader will over-read `eq:invisible`.
- **R5.** State `cor:curveenstrophy` in the form that retains the good term,
  `Y' <= -2 nu ||Delta v||_2^2 + C_E nu^{-3} Y^3`, which the curve also
  satisfies for small `eps` (`O(b^2) <= O(b^6)`).
- **R6.** In `cor:curveenstrophy`, "the same comparison curve" -> "the
  comparison curve of Theorem 8.2 built from that seed"; and note that the
  datum's energy `E_W = b^2 E_{W_0}` diverges as `C_E -> 0`, so the exclusion at
  small `C_E` is an exclusion at large data.
- **R7.** Record that the curve is exactly the backward self-similar ansatz
  `v(t,x) = (T_c - t)^{-1/2} Phi(x/sqrt(T_c - t))` with `Phi` compactly
  supported, and cite Necas-Ruzicka-Sverak (1996) and Tsai (1998) for `R != 0`
  directly. Keep the ESS/GKP argument as the second, self-contained route.
- **R8.** Two one-line proof simplifications: `d_W > 0` follows from
  `j(W).(W.grad)W = (1/3)(W.grad)|W|^3` and `div W = 0` without invoking
  `eq:workform`; and the `sigma_W != 0` argument should close explicitly on the
  contradiction with `d_W > 0`.
- **R9.** State that the curve satisfies `eq:signedtarget` with `theta = 1` and
  `A = 0`, so it excludes the signed route only for `theta < 1`, and note that
  `theta = 1` already yields `sup Q < infinity`.
- **R10.** State that `sup_t ||v(t)||_3 < infinity` and `sup_t Q < infinity` on
  the curve: it is a countermodel to a sufficient certificate, not to the target,
  and carries no information about blow-up.
- **R11.** In `sec:crossing`, specify that the modulus in question is a modulus
  **in the time variable**; a modulus in an auxiliary spacetime measure does not
  give an excursion-time lower bound without a separate per-excursion lower
  bound on that measure. Optionally sharpen `1 + H/l` to `floor(H/l)`.
- **R12.** In `sec:curve`, replace "The first two follow by applying the
  invertible transformation to all competitors" with the explicit statement that
  `S_lambda(grad phi) = grad(phi(lambda .))` and that `S_lambda` is an `L^3`
  isometry, hence `S_lambda G_3 = G_3`; that is the only step with content.
- **R13.** In `eq:curveG`, state the limit variable: the divergence is as
  `tau -> T_c^-`.

---

## 4. Refutation attempts and outcomes

Nine genuine attempts. Eight failed; one partially succeeded, against the
paraphrase rather than the document.

1. **Break the commutation `w(b S_lambda v) = b S_lambda w(v)`** by finding a
   direction in which `S_lambda G_3 \subsetneq G_3`, or non-uniqueness of the
   minimizer. **FAILED.** `S_lambda` maps `grad C_c^\infty` onto itself and is
   an `L^3` isometry, so it maps `G_3` onto `G_3` with inverse `S_{1/lambda}`;
   `F` is invariant and strictly convex. The commutation is a theorem.
2. **Show the curve violates one of the identities it claims.** Recomputed
   `lambda'`, `E' + 2 nu Y`, `Q' + nu D - K`, `Y'`, `G_v`, `\int ||sigma||_2^4`,
   `\int Y`, `\int ||grad q||_2^2`, `\int ||q||_3^4`, `\int ||v||_3^4`, both
   symbolically and numerically at two parameter sets. **FAILED.** All exact.
   Worse for the refuter: the curve also satisfies `eq:qbudgets` and `eq:u34`
   with the document's own constants, which the document merely asserts.
3. **Show the seed cannot exist**, by attacking `w(U_s) = U_s`, the disjointness
   of `supp e` and `supp U_s`, the Bregman bounds, the `|eps|^{3/2}` remainder,
   or the sign flip `W_0 = U_s - eps h`. **FAILED.** Every step reproduced
   symbolically; `c_0 = 2.134e-3 > 0` and `D(U_s) = 0.12940 > 0` by quadrature,
   the latter cross-checked two ways.
4. **Show the curve secretly solves Navier-Stokes**, which would make it a
   blow-up counterexample and hence false. **FAILED, and instructive.** The
   curve is exactly the backward self-similar ansatz; NRS (1996) and Tsai (1998)
   forbid nontrivial such solutions with `L^3` profile, and the document's own
   ESS/GKP argument is independently valid. This produced R7.
5. **Show the curve violates a scalar test the programme actually uses.**
   **PARTIAL SUCCESS**, against the paraphrase, not the document. The enstrophy
   identity `<Delta v, R> != 0` (computed: `110.15` vs `569.15` in the
   `eps -> 0` limit), and `C_sharp ||q||_3 >= nu` is forced. The document never
   claims otherwise; the controller's note and `PLAN.md` do. This produced R1,
   R4 and the corrections in section 6.
6. **Break `cor:curveenstrophy`'s limit** by finding a hidden `eps`-dependence
   that keeps `b` bounded. **FAILED.** `c_0`, `C_e`, `C_*`, `L`, `d_0` are all
   `eps`-independent; `D_0 -> D(U_s) > 0` by `eq:Alip`; `K_0 <= c_0 eps +
   C_* eps^{3/2}`; so `b >= nu D(U_s)/(2 c_0 eps) -> infinity`. Also checked
   that `T_c` does *not* shrink in the limit, so the divergence of `G` is not
   bought by a vanishing horizon.
7. **Show HF25 and HF26 collide**, by exhibiting a violation of HF25's proved
   differential inequality on the curve. **FAILED.** Both sides scale as
   `lambda^2` and the inequality reduces to `O(b^3) <= O(b^7)`. Only HF25's
   hypothesis fails on the curve, which is the intended reading.
8. **Show the countermodel refutes the whole signed route.** **FAILED in the
   informative direction:** it refutes `eq:signedtarget` for every `theta < 1`
   but is *satisfied with equality* at `theta = 1`, `A = 0`, and `theta = 1`
   already suffices for `sup Q < infinity`. This produced R9 and is a real
   narrowing of the exclusion.
9. **Break the `sec:crossing` example** (smoothness at `t = 1`, Lipschitz
   bound, infinitude and sign-changing character of the crossings).
   **FAILED.** All confirmed; the one apparent failure in my own run was a
   floating-point underflow on my side.

---

## 5. What I did NOT check

- Sections 1-6 of the candidate: `thm:weightedresponse`, `thm:Aderivative`,
  `cor:second`, `prop:gapquadratic`, `thm:NSdeparture`, `thm:temporal`,
  `cor:modulus`, `lem:negativeincrements`, `thm:qtime`, `cor:residualmeasure`,
  `thm:fullconditional`. Other scopes.
- Appendices `app:spatial` and `app:weighted`, except that I re-derived
  `eq:Didentity` by integration by parts and confirmed it numerically on `U_s`
  to `1.1e-7`.
- `eq:divcurl` itself (imported HF23), the local well-posedness package, the
  ESS/GKP endpoint theorem, and the `L^3` Helmholtz fact that `grad p \in G_3`.
  All used as premises.
- The numerical values of `||e||_3`, `||N_1||_3`, `||N_2||_3` and hence `C_*`;
  I verified only that each is finite and `eps`-independent, which is all the
  argument needs.
- HF25's constants `C_sigma`, `B_0`, `B_sigma` beyond the shape of its criterion.
- Any re-audit of HF22-C, HF21-B or the HF24 lanes. I read
  `hf22-good-set-dissipation.md`, `hf24-modulus-of-continuity.md` and
  `hf24-review-modulus-of-continuity.md` for the reconciliation only, and quote
  them as they stand.
- The manuscript at `navier-paper` and the formal repository. Untouched.
- Section `app:checks`'s arithmetic beyond the comparison-curve row (which I
  confirmed: `lambda' = lambda^3/(2T_c)`, `E = E_W/lambda`, `Y = Y_W lambda`,
  `T_c = E_W/(4 nu Y_W)`, energy derivative exactly `-2 nu Y`).

---

## 6. REQUIRED CORRECTIONS TO OUR OWN RECORD

These are the changes I judge necessary. **I have not made them.** No file
outside this one was edited.

### 6.1 `PLAN.md`, the crossing-count equivalence ("Convergence worth noting.")

The sentence "an input-only modulus of continuity for the distance along the
trajectory at the critical level, **equivalently** an input-only bound on the
number of crossings of that level" is **wrong as written** and must be replaced.
Required replacement content:

> an input-only modulus of continuity **in time** for the **scalar** distance
> `d_1(t) = ||q(t)||_3` at the critical level, which would supply an input-only
> lower bound on the duration of a passage of `C_sharp d_1` across the corridor
> `[(1-2eps)nu, (1-eps)nu]`, and hence an input-only bound on the number of
> **disjoint corridor traversals**. The implication runs one way only: a
> crossing count supplies no modulus, and no modulus bounds crossings of a
> single level.

Also required in the same paragraph:

- Delete "equivalently". There is no equivalence in either direction.
- Name the observed object. HF24 observes the scalar `d_1`; HF26's producer
  consumes the vector `t -> q(t)` in strong `L^3`; `|d(t) - d(s)| <=
  ||q(t) - q(s)||_3` runs one way only, so the scalar target is strictly the
  weaker one and would not discharge HF26's `thm:temporal`.
- The clause "and, with the good-set result above, reduce (G) to its bad-set
  part" over-credits the crossing count: `hf24-modulus-of-continuity.md`
  Remark 4.4 and HF22-C Theorem B say that reduction "is already audited and
  needs no modulus". Reword to say the crossing count adds *structure* (finitely
  many bad intervals of input-bounded total measure), not the reduction.

### 6.2 `PLAN.md`, the HF26 countermodel paragraph

Replace "unlike every previous excluded class it violates nothing at the scalar
level; what it lacks is only the equation itself" (line 1489 at the time of
writing). It is false. Required replacement content:

> The curve satisfies exactly the two scalar projections of the residual,
> `<v, R> = 0` and `<A(v), R> = 0`, which are literally the energy identity and
> the quotient balance; together with the instantaneous variational structure,
> the energy-level budgets with our own constants, a constant scalar distance,
> and, for any prescribed `C_E`, the cubic enstrophy inequality in either form.
> It does **not** satisfy the enstrophy *identity* `<Delta v, R> = 0`; it does
> not satisfy any vector modulus for `t -> q(t)`; and it is forced to obey
> `C_sharp ||q(t)||_3 >= nu` and `||v(t)||_3 >= nu/(2 C_sharp)`, so it lies
> entirely in the bad set and excludes nothing about smallness. It refutes the
> signed route only for `theta < 1`; at `theta = 1` it satisfies
> `eq:signedtarget` with `A = 0`.

Add, in the same paragraph:

- **The correct comparison.** The countermodel is the same species as HF22-C
  Theorem C', strictly strengthened. HF22-C section 5 already closes with "Any
  proof of (G) must use structure that (T1)-(T9) do not encode: the actual
  equation, the actual minimizer, or a quantitative modulus that the audited
  record does not yet supply." HF26's curve satisfies (T1)-(T9) with input-only
  constants and closes two of those three escapes -- the actual minimizer, and a
  quantitative scalar modulus -- leaving only "the actual equation". That is the
  sharpening, and it is a sharpening within a recorded species, not a new one.
- **The restraint.** The curve has `sup_t ||v(t)||_3 < infinity` and
  `sup_t Q < infinity`, i.e. it satisfies the conclusion the (G)-route is trying
  to reach. It is a countermodel to the derivability of a chosen sufficient
  certificate, not to the target, and it is not evidence of any kind about
  blow-up.
- **The identification.** The curve is exactly the backward self-similar ansatz;
  `R != 0` follows from Necas-Ruzicka-Sverak (1996) / Tsai (1998) directly, and
  the ESS/GKP route is the document's independent second argument.

### 6.3 `PLAN.md`, the framing of the challenge to HF24

The sentence "Two claims of ours are challenged and are held pending audit"
must be narrowed. Required content:

> One claim of ours is wrong: this plan's own summary of the HF24 target, which
> said "equivalently ... crossings of that level". The HF24 record is **not**
> challenged. `hf24-modulus-of-continuity.md`'s frontier packet already states
> the target in the corridor form HF26 asks for, its FORBIDDEN INFERENCES
> already separate a `mu`-modulus from a `t`-modulus, its section 5.2 item 3
> already states that a crossing count is not implied by any summability in the
> record, and `hf24-review-modulus-of-continuity.md` Repair 15 already restricts
> the count to corridor-wall traversals and records that intra-corridor
> oscillations are not countable. HF26 `sec:crossing` **confirms** our HF24
> audit independently. No HF24 verdict changes on this point, and the two waves
> need no joint re-adjudication for this reason.

### 6.4 `PLAN.md`, one addition to the HF24 record

Add, to the HF24 section or the sharpened-gap section:

> HF24-A section 5.2's viscous-eddy family (`A l = nu/C_sharp` at `Re ~ 1`),
> which that lane could offer only as "bounded evidence, not a solution and not
> a proof", is realised rigorously by HF26 `thm:curve`: the curve has amplitude
> `~ lambda` and length `~ 1/lambda`, so `A l` is constant, and `eq:Kq` forces
> `C_sharp A l >= nu`, which is the family's `Re ~ 1` condition. HF26 replaces
> the dyadic sequence of single crossings with one continuously concentrating
> structure of constant `d_1`, and its slices carry genuine variational objects.
> This upgrades section 5.2 from a scaling table to an exact construction, at the
> price of the curve not being a trajectory. It also explains why the curve is
> confined to the bad set, which is consistent with HF22-C Theorem B.

Also worth recording in the sharpened-gap section: on the curve the square
defect budget `\int ||sigma||_2^2` is finite while `\int ||sigma||_2^4` diverges,
so the curve is an explicit realisation of the square-to-fourth-power gap that
section names, with actual fields, and it shows that gap is not closable from
(P1)-(P7).

### 6.5 `hf26-temporal-continuation.md`, the controller's index note

The six-row algebra table is **correct in every row**; I reproduced all six
independently and found no error in it. Two prose corrections are required, and
one optional addition:

- "This one violates nothing at the scalar level" -> false; replace as in 6.2.
- "the instantaneous variational structure together with the energy identity and
  ***any* scalar distance information** cannot imply the target" -> false as
  written. A scalar-distance *smallness* threshold is scalar distance
  information and it does exclude the curve (`C_sharp ||q||_3 >= nu` is forced,
  and `C_sharp ||q||_3 <= theta nu` immediately gives `Q' <= -(1-theta) nu D`).
  The correct claim is "any scalar distance *regularity, modulus or crossing*
  information".
- Optional: record that `<v, R> = 0` and `<A(v), R> = 0` are literally the
  energy identity and the quotient balance, so "invisible to both scalar tests"
  is a restatement of the two balances rather than an additional property; and
  that a third scalar test, the enstrophy identity, is not blind.

### 6.6 Nothing to promote

No graph node changes. `thm:curve`, `cor:curveenstrophy` and `app:positive`
remain unaudited candidate content of an unaudited external document until the
controller integrates this audit; this review licenses no manuscript edit, no
claim-graph edit, and no promotion. NS-R3 and the first gap are untouched by
anything in this scope.

---

## 7. Frontier record

**MODE / RESULT:** proof-audit, **PASS WITH SCOPE**. The countermodel is real,
its seed exists, and every identity is exact; the exclusion it licenses is
strictly narrower than our record states, and the crossing section corrects
`PLAN.md` while confirming HF24.

**FIRST BAD BRIDGE (in this scope):** none. No step in Sections 7-8 or
`app:positive` is invalid.

**FIRST OVERCLAIM (not in the document, in our record):** `PLAN.md` and the
index note's "violates nothing at the scalar level" and "any scalar distance
information", both refuted by `C_sharp ||q(t)||_3 >= nu` and by
`<Delta v, R> != 0`.

**NON-CLAIMS:** no regularity or blow-up result; no promotion; no claim that the
scalar route is dead, only that `eq:Gtarget` and `eq:signedtarget` for
`theta < 1` are not derivable from (P1)-(P7); no re-audit of HF24, HF22-C or
HF25; NS-R3 remains open.

**NEXT DISTINCT ACTION (for the controller, not taken here):** apply 6.1-6.5;
then decide whether the `theta = 1` endpoint of `eq:signedtarget` and the
enstrophy *identity* are worth a lane, since they are the two scalar-level
mechanisms this countermodel provably does not exclude.
