# HF24-A: an input-only modulus of continuity for the distance to the nonlinear-Hodge class

**STATUS (2026-09-06).** Lane HF24-A, **MODE: DISCOVER**, **UNAUDITED**. Owned
file: `research/evidence/hf24-modulus-of-continuity.md`. Nothing else in the
repository is edited, nothing is committed, nothing is promoted, and the
manuscript is untouched.

**RESULT IN ONE LINE.** The modulus asked for is obtained *in a different
currency*: `t -> ||q(u(t))||_3` is Hölder-1/4 continuous with respect to an
input-only spacetime measure, with an explicit input-only constant, **except
for a factor built from the enstrophy at the two endpoints**; this yields a new
unconditional constraint on the bad set (Theorem 4.1) and a crossing count
conditional on one precisely named quantity. The exact obstruction is
identified and is a single scalar: a `tau`-uniform bound for `||grad u(t)||_2`
at the times when `C_sharp||q(t)||_3` sits in the critical corridor. (G) is
neither proved nor refuted, and no continuation statement is claimed.

**Inputs** [DI]: `PLAN.md` ("Frontier packet", "Beyond the checkpoint",
"HF18"–"HF23", "Ordered next actions"); `../navier-paper/main.tex`
`sec:quotient` in full — in particular `def:quotient`, `lem:cubic-pointwise`
\eqref{eq:cp-monotone} \eqref{eq:cp-lipschitz}, `lem:cubic-frechet`,
`lem:quotient-minimizer`, `lem:quotient-coercive`, `lem:quotient-scaling`,
`lem:quotient-stability` \eqref{eq:cp-contraction} \eqref{eq:cp-strong},
`prop:quotient-derivative`, **`prop:quotient-divcurl`** \eqref{eq:qdc-w}
\eqref{eq:qdc-q} \eqref{eq:qdc-sobolev} \eqref{eq:qdc-interp}
\eqref{eq:qdc-sobolev-field}, **`cor:quotient-defect`** \eqref{eq:qdc-sigma}
\eqref{eq:qdc-sigmaid} \eqref{eq:qdc-potential},
`cor:quotient-vorticity-zero`, `lem:quotient-mixed-pressure`,
**`cor:quotient-budgets`**, `rem:quotient-divcurl-scope`, `rem:quotient-scope`,
`prop:quotient-evolution`, `def:qe-dissipation`, `lem:quotient-lowstrain`,
`hyp:highstrain`, `rem:highstrain-normalisation`, `rem:highstrain-scope`,
`rem:distance-balance`, `rem:no-monotone`, `prop:quotient-conditional`; outside
that section `prop:localtheory` (R1)–(R3), `cor:Lq`, `prop:energy`,
`prop:scaling`(iii) \eqref{eq:L4L3}, `lem:interp`, `def:sobolev-constant`,
`def:lp` with \eqref{eq:riesz-symbol}, `lem:leray`, `rem:mismatch`,
`hyp:critical`, `thm:conditional`, `thm:continuation`;
`research/evidence/hf21-crossing-sign-structure.md` (audited REPAIR, repairs
applied) §§3.1, 4.3–4.4 (`C_sharp = (3/2)C_9C_S`, Lemma 4.3, Theorem 4.5);
`research/evidence/hf22-direct-attack.md` §3 (H-mod), Lemma R1, Remarks 3.6–3.7;
`research/evidence/hf22-good-set-dissipation.md` §6 (the open question) and its
Theorem B (the good set is free in (G));
`research/evidence/hf23-divcurl-continuation.md`.

---

## 1. Frontier packet

```text
TERMINAL CLAIM (unchanged, not addressed here): NS-R3.

TARGET OF THIS LANE (not (G) itself): an input-only modulus of continuity for
  d_1(t) := ||q(u(t))||_3 along the classical branch at the level nu/C_sharp,
  uniformly for tau < min{H,T_*}; equivalently an input-only lower bound on
  the time (or on some input-only spacetime cost) of a passage of C_sharp d_1
  across the corridor [(1-2eps)nu, (1-eps)nu].

ESTABLISHED AND USED: (E1) lem:quotient-minimizer(b),(c) and the two pointwise
  cubic identities eq:cp-lipschitz, eq:cp-monotone; (E2) the cancellation
  <A'-A, w'-w> = <A'-A, h> of lem:quotient-stability's proof; (E3)
  prop:quotient-divcurl with eq:qdc-sobolev: ||w||_6 <= (5/4)^{1/2}C_S||grad u||_2,
  and cor:quotient-defect eq:qdc-potential: d_k q_j = R_j R_k sigma; (E4)
  prop:energy: sup_t ||u||_2^2 <= E_0 and int_0^tau ||grad u||_2^2 <= E_0/(2nu);
  (E5) prop:localtheory (R1)-(R3) and the pressure form p = R_iR_j(u_iu_j);
  (E6) eq:qdc-interp and eq:qdc-sobolev-field; (E7) HF21-B Thm 4.5
  (crossing measure) and Prop 3.1 (|K| <= C_sharp d_1 D_3(w)); (E8) HF22-C
  Theorem B (the good set is free in (G)).

FIRST GAP (this lane): a tau-uniform input-only upper bound for
  ||grad u(t)||_2 restricted to the corridor times. Nothing else is missing
  from the crossing-count argument below.

FALSIFIER: an inequality whose two sides have different scaling weights; a
  bound whose constant contains sup_t ||u||_3, sup_t Q, sup_t ||grad u||_2 or
  sup_t ||d_t u||_3; any differentiation of the merely-L^3 minimizer; any
  step using w in L^2 or sigma in L^{3/2}.

FORBIDDEN INFERENCES (this lane): a modulus in the measure mu is NOT a modulus
  in t; a crossing-count bound is NOT (G); a bound on the number of components
  of the bad set does NOT bound sup_t Q; non-derivability is not falsity.

CHECK: two-parameter scaling weights displayed for every new inequality; every
  constant traced to an input quantity or declared trajectory-dependent.
```

**Conventions.** `u_0` divergence-free Schwartz, `nu > 0`, `(u,p)` the maximal
classical branch of `prop:localtheory` on `[0,T_*)`, `E_0 = ||u_0||_2^2`,
`0 < H < infinity`, `tau < min{H,T_*}`. `w(t) = w(u(t))`, `q(t) = q(u(t))`,
`sigma(t)` the defect \eqref{eq:qdc-sigma}, `Y(t) = ||grad u(t)||_2^2`,
`d_1(t) = ||q(t)||_3`, `Q(t) = Q(u(t))`, `D_3(w)` the quotient dissipation
`def:qe-dissipation`. `C_S` is `def:sobolev-constant`;
`C_sharp = (3/2)C_9C_S` is the constant of HF21-B Prop. 3.1. Fourier
convention as in `def:lp`, and homogeneous norms
`||f||_{Hdot^s} := ||(2 pi |xi|)^s \hat f||_2`, so that
`||f||_{Hdot^1} = ||grad f||_2`, `||Delta f||_{Hdot^{-1}} = ||grad f||_2` and
`||div F||_{Hdot^{-1}} <= ||F||_2`.

**Two-parameter scaling.** With `u_{a,lambda}(x,t) = a u(lambda x, a lambda t)`
solving \eqref{eq:NS} at viscosity `nu a/lambda`, the weights `(a,lambda)` are
`nu ~ (a,lambda^{-1})`, `t ~ (a^{-1},lambda^{-1})`, `E_0 ~ (a^2,lambda^{-3})`,
`||u||_3 = ||w||_3-scale ~ (a,lambda^{-1})`, `||grad u||_2 ~ (a,lambda^{-1/2})`,
`||w||_6 ~ (a,lambda^{-1/2})`, `||sigma||_2 ~ (a,lambda^{-1/2})`,
`||f||_{Hdot^{-1}} ~ (a,lambda^{-5/2})`. The level statement
`C_sharp d_1 vs nu` is scale-invariant, as it must be, and `w(u_{a,lambda})`
scales exactly like `u_{a,lambda}` by `lem:quotient-scaling`.

---

## 2. Part (1): what the potential representation controls is exactly `L^6`

### 2.1 The defect determines `q` linearly, and the transfer is an equivalence

**Proposition 2.1.** Let `u, u'` be solenoidal `H^1` fields, `q = q(u)`,
`q' = q(u')`, `sigma`, `sigma'` their defects. Then

```
   ||grad(q' - q)||_2 = ||sigma' - sigma||_2 ,
   C_S^{-1} ||q' - q||_6  <=  ||sigma' - sigma||_2 ,
   ||q' - q||_6  <=  C_S ||sigma' - sigma||_2 .
```

*Proof.* By \eqref{eq:qdc-potential}, `d_k q_j = R_jR_k sigma` and
`d_k q'_j = R_jR_k sigma'`; the right-hand side is **linear** in the defect, so
`d_k(q'-q)_j = R_jR_k(sigma'-sigma)`. By Plancherel and \eqref{eq:riesz-symbol}
the symbol of `(R_jR_k)_{j,k}` is `(xi_j xi_k/|xi|^2)_{j,k}`, of Frobenius norm
`1` at every `xi != 0`, whence the first identity. The two others are
\eqref{eq:qdc-sobolev-field} applied to `q'-q` (legitimate by the limiting
argument of Step 4 of `cor:quotient-defect`, run on the difference of the two
approximating sequences) and the trivial converse
`||grad z||_2 >= C_S^{-1}||z||_6`. `[]`

So **time regularity of `q` in `L^6` and time regularity of `sigma` in `L^2`
are the same statement, with constant `C_S` in both directions.** This is the
precise answer to the first half of task item (1). It is a genuine consequence
of `cor:quotient-defect`: before HF23 the map `u -> q` had no linear structure
at all.

### 2.2 The two exact blockers between `L^6` and `L^3`

The level in the target is `||q||_3`, not `||q||_6`, and the gap between them
cannot be closed inside the audited record.

**Proposition 2.2 (what the Newtonian potential gives, and does not).** For
`sigma in L^2(R^3)`, the field `q` with `d_kq_j = R_jR_ksigma` lies in `L^6`
with `||q||_6 <= C_S||sigma||_2`, and this is sharp in the sense of scaling:
the Hardy--Littlewood--Sobolev exponent pair for the first-order Riesz
potential at `p = 2` is `q = 6`, and `I_1 : L^2 -> L^3` is false by scaling
(`I_1 : L^p -> L^3` forces `1/p = 1/3 + 1/3`, i.e. `p = 3/2`). Consequently:

1. `q in L^3` follows from `sigma in L^{3/2}` — which is exactly the residual
   hypothesis (H2), declared unproved in `rem:quotient-divcurl-scope`; and
2. `q in L^3` follows from `q in L^2` together with `q in L^6`, by
   `||q||_3 <= ||q||_2^{1/2}||q||_6^{1/2}` \eqref{eq:qdc-interp} — and
   `q in L^2` is equivalent to `w in L^2` (since `u in L^2`), which
   `rem:quotient-divcurl-scope` explicitly declines to assert.

**Remark 2.3 (uniqueness of the admissible interpolation, and why route 2
fails at the stated generality).** Among monomials `||sigma||_2^alpha ||u||_2^beta`,
matching the weights of `||q||_3 ~ (a,lambda^{-1})` against
`||sigma||_2 ~ (a,lambda^{-1/2})` and `||u||_2 ~ (a,lambda^{-3/2})` forces
`alpha + beta = 1` and `alpha/2 + 3beta/2 = 1`, i.e. `alpha = beta = 1/2`: the
interpolation of 2. above is the **unique** scaling-admissible route from the
new `L^2` control of the defect to the critical norm. Its missing input is
`||q||_2`. And that input cannot be supplied in general: `d_kq_j = R_jR_ksigma`
gives `|\hat q(xi)| = |\hat sigma(xi)|/(2 pi |xi|)`, so `q in L^2` is exactly
`sigma in Hdot^{-1}`, a low-frequency condition, and `L^2 \not\subset Hdot^{-1}`.
Hence the implication "`sigma in L^2` implies `q in L^2`" is **false** as a
statement about general `L^2` functions; whether the particular `sigma(t)`
produced by the minimiser lies in `Hdot^{-1}` is **not decided** by the audited
record. This is the one place in this note where a falsity, rather than a
non-derivability, is asserted, and it is asserted only about the general
implication.

**Conclusion of Part (1).** The potential representation controls
`t -> ||q(t)||_6` exactly, through `t -> ||sigma(t)||_2`, and controls
`t -> ||q(t)||_3` not at all. A modulus for the target therefore cannot be
produced from `sigma` alone; the critical norm has to be reached by an
argument that keeps the *cubic* variational structure. That is Part (2). Note
also that `||q||_6` cannot replace `||q||_3` in the level statement: `||q||_6`
has weight `(a,lambda^{-1/2})` and `nu` has weight `(a,lambda^{-1})`, so no
scaling-consistent comparison `C ||q||_6 vs nu` exists.

---

## 3. Part (2): the new gradient control does upgrade the stability

Nothing below differentiates the minimiser. Only finite differences, the
Euler--Lagrange orthogonality, and the pointwise cubic identities are used.

### 3.1 A weighted stability estimate

**Lemma 3.1 (weighted stability; new).** Let `u, u' in L^3(R^3)^3`,
`h = u' - u`, `w = w(u)`, `w' = w(u')`. Then, with all integrals finite,

```
   int (|w| + |w'|) |w' - w|^2 dx   <=   4 int (|w| + |w'|) |h|^2 dx ,     (3.1)
   ||w' - w||_3^3  <=  4 int (|w| + |w'|) |h|^2 dx .                        (3.2)
```

*Proof.* Write `A = |w|w`, `A' = |w'|w'`. The cancellation step in the proof of
`lem:quotient-stability` gives `<A' - A, w' - w> = <A' - A, h>`, using only
`w' - w - h = q(u') - q(u) in G_3` and `lem:quotient-minimizer`(c) for both
minimisers. Integrating the identity \eqref{eq:cp-monotone} pointwise,

```
   <A' - A, w' - w> = (1/2) int (|w|+|w'|)[ (|w'|-|w|)^2 + |w'-w|^2 ]
                    >= (1/2) int (|w|+|w'|) |w'-w|^2  =: (1/2) rho^2 .
```

For the right side, \eqref{eq:cp-lipschitz} gives `|A' - A| <= (|w|+|w'|)|w'-w|`
pointwise, so by Cauchy--Schwarz with the weight `(|w|+|w'|)`,

```
   <A' - A, h> <= int (|w|+|w'|) |w'-w| |h| <= rho * X^{1/2},
   X := int (|w|+|w'|) |h|^2 .
```

Hence `(1/2)rho^2 <= rho X^{1/2}`, i.e. `rho <= 2X^{1/2}`, which is (3.1); and
`|w'-w| <= |w|+|w'|` gives `||w'-w||_3^3 <= rho^2`, which is (3.2).
Finiteness: `X <= (||w||_3+||w'||_3)||h||_3^2 < infinity` by Hölder. `[]`

Taking `X <= (||w||_3+||w'||_3)||h||_3^2` in (3.2) returns
`lem:quotient-stability` \eqref{eq:cp-strong} up to the constant, so Lemma 3.1
is a refinement, not a competitor: it **keeps the weight**, and the weight is
where the new regularity enters, because `prop:quotient-divcurl` controls
`||w||_6` — never `||w||_3` — by input-side derivative information.

### 3.2 An input-only bounded-variation bound for the velocity in `Hdot^{-1}`

**Lemma 3.2 (input-only spacetime cost measure).** Put

```
   g(s) := nu ||grad u(s)||_2 + ||u(s)||_4^2 ,     mu(I) := int_I g(s) ds .
```

Then for every `0 <= t <= t' < T_*`, with `h = u(t') - u(t)`,

```
   ||h||_{Hdot^{-1}}  <=  mu([t,t']) ,                                       (3.3)
```

and for every `tau < min{H,T_*}`,

```
   mu([0,tau])  <=  M(nu,E_0,H) := (nu E_0 H/2)^{1/2}
                                 + C_S^{3/2} E_0 H^{1/4} (2nu)^{-3/4} .      (3.4)
```

*Proof.* By (R2), `d_su = nu Delta u - P div(u tensor u)` with `P` the Leray
projection, whose Fourier symbol is an orthogonal projection at every `xi`, so
`P` is a contraction on `Hdot^{-1}`. Then
`||nu Delta u||_{Hdot^{-1}} = nu ||grad u||_2` and
`||div(u tensor u)||_{Hdot^{-1}} <= ||u tensor u||_2 <= ||u||_4^2`, giving
`||d_su||_{Hdot^{-1}} <= g(s)`; both terms have vanishing symbol at `xi = 0`
of the required order, so `d_su in Hdot^{-1}` genuinely. By (R1),(R3),
`s -> d_su` is continuous into `Hdot^{-1}` on `[0,T] subset [0,T_*)`, and
`h = int_t^{t'} d_su ds` as a Bochner integral there; the triangle inequality
gives (3.3). For (3.4): by Cauchy--Schwarz in time and `prop:energy`,
`int_0^tau nu ||grad u||_2 dt <= nu H^{1/2}(E_0/2nu)^{1/2} = (nu E_0 H/2)^{1/2}`;
and `||u||_4 <= ||u||_2^{1/4}||u||_6^{3/4}` with
\eqref{eq:qdc-sobolev-field} gives
`||u||_4^2 <= E_0^{1/4} C_S^{3/2} Y^{3/4}`, so by Hölder in time with
exponents `(4/3,4)` and `prop:energy`,
`int_0^tau ||u||_4^2 dt <= C_S^{3/2}E_0^{1/4}H^{1/4}(E_0/2nu)^{3/4}`. `[]`

`mu` is the natural currency here: it is the only input-only spacetime measure
in which the *velocity increment* can be priced, because the only input-only
spacetime budget in the record is `int Y <= E_0/(2nu)` (`prop:energy`) together
with `int ||u||_3^4` (`prop:scaling`(iii)), and both enter (3.4). Scaling
check: `mu ~ (a,lambda^{-5/2})` on both sides of (3.3) and (3.4)
(`(nu E_0 H)^{1/2} ~ (a^{(1+2-1)/2}, lambda^{(-1-3-1)/2}) = (a,lambda^{-5/2})`;
`E_0 H^{1/4}nu^{-3/4} ~ (a^{2-1/4-3/4},lambda^{-3-1/4+3/4}) = (a,lambda^{-5/2})`). OK.

### 3.3 The modulus

**Theorem 3.3 (input-only modulus in the `mu`-currency, modulo endpoint
enstrophy; new).** Let `0 <= t <= t' < T_*`, put

```
   G := ||grad u(t)||_2 + ||grad u(t')||_2 ,     mu := mu([t,t']) ,
   kappa_0 := 1 + (2 sqrt 5)^{1/3} < 2.65 .
```

Then

```
   | ||q(t')||_3 - ||q(t)||_3 |  <=  ||q(t') - q(t)||_3
                                 <=  kappa_0 C_S^{1/2} G^{3/4} mu^{1/4} .    (3.5)
```

*Proof.* Write `h = u(t')-u(t)`, `w = w(t)`, `w' = w(t')`. Since
`q = w - u`, `q' - q = (w'-w) - h` and it suffices to bound the two terms.

*(i) The velocity increment.* By \eqref{eq:qdc-interp} applied to `|h|`,
`||h||_3 <= ||h||_2^{1/2}||h||_6^{1/2}`; by \eqref{eq:qdc-sobolev-field},
`||h||_6 <= C_S||grad h||_2 <= C_S G`; and by Plancherel and Cauchy--Schwarz,
`||h||_2^2 <= ||h||_{Hdot^1} ||h||_{Hdot^{-1}} <= G mu` using (3.3). Hence

```
   ||h||_3 <= (G mu)^{1/4} (C_S G)^{1/2} = C_S^{1/2} G^{3/4} mu^{1/4} .      (3.6)
```

*(ii) The minimiser increment.* By Lemma 3.1 and Hölder with `1/6 + 5/6 = 1`,

```
   ||w'-w||_3^3 <= 4 (||w||_6 + ||w'||_6) ||h||_{12/5}^2 .
```

By \eqref{eq:qdc-sobolev}, `||w||_6 <= (5/4)^{1/2}C_S||grad u(t)||_2` and
likewise at `t'`, so `||w||_6 + ||w'||_6 <= (sqrt5/2) C_S G`. **This is the one
step that uses the new regularity, and it is the whole of the upgrade.** By
Lebesgue interpolation applied to `|h|` with `5/12 = (3/4)(1/2) + (1/4)(1/6)`,

```
   ||h||_{12/5}^2 <= ||h||_2^{3/2} ||h||_6^{1/2} <= (G mu)^{3/4} (C_S G)^{1/2}
                   = C_S^{1/2} G^{5/4} mu^{3/4} .
```

Therefore `||w'-w||_3^3 <= 4 (sqrt5/2) C_S^{3/2} G^{9/4} mu^{3/4}`, i.e.

```
   ||w'-w||_3 <= (2 sqrt 5)^{1/3} C_S^{1/2} G^{3/4} mu^{1/4} .               (3.7)
```

Adding (3.6) and (3.7) and using the triangle inequality twice gives (3.5). `[]`

**Scaling check of (3.5).** `||q||_3 ~ (a,lambda^{-1})`;
`G^{3/4}mu^{1/4} ~ (a^{3/4+1/4}, lambda^{-3/8-5/8}) = (a,lambda^{-1})`. OK.
Both sides are critical, as they must be.

**Remark 3.4 (exactly what the new regularity bought).** Without
`prop:quotient-divcurl` one can still eliminate `sup_t ||w||_3` from the
audited modulus, contrary to what HF22-C §6 and `hf22-direct-attack.md` §3 (the block
following Lemma R1) record as the obstruction: by `lem:quotient-coercive` and \eqref{eq:qdc-interp},

```
   ||w(t)||_3 <= ||u(t)||_3 <= C_S^{1/2} E_0^{1/4} Y(t)^{1/4} <= C_S^{1/2}E_0^{1/4}G^{1/2},
```

so `lem:quotient-stability` \eqref{eq:cp-strong} with (3.6) already gives the
*old-tools modulus*

```
   | d_1(t') - d_1(t) |  <=  2 C_S^{1/2} E_0^{1/8} G^{5/8} mu^{1/8}
                            + C_S^{1/2}G^{3/4}mu^{1/4}   (leading term first). (3.8)
```

Both (3.5) and (3.8) are new relative to the audited record, and both replace
the two trajectory-dependent quantities of HF21-B Remark 2.2
(`sup_t ||w||_3` and `sup_t ||d_t u||_3`) by the *single* quantity `G`. The new
regularity improves the exponent of the currency from `mu^{1/8}` to `mu^{1/4}`
and deletes the `E_0` weight. Since the corridor width `c` below is small
(`c ~ eps nu / C_sharp`) and `G` is large exactly in the dangerous regime, the
improvement is not cosmetic: the traversal cost improves from `c^8 G^{-5}` to
`c^4 G^{-3}` (Theorem 4.1 and Remark 4.5).

**Remark 3.5 (what is *not* claimed).** (3.5) is a modulus with respect to
`mu`, not with respect to `t`. `mu([t,t'])` is small when `t' - t` is small
*for a fixed trajectory*, but no input-only function of `t'-t` bounds it:
`g(s) <= nu Y^{1/2} + C_S^{3/2}E_0^{1/4}Y^{3/4}` and `Y` has no input-only
sup bound. Consequently (3.5) does **not** produce the Lipschitz-in-`t` cutoff
that `hf22-direct-attack.md` (H-mod) consumes; see Remark 5.4.

---

## 4. The new constraint on the bad set

Fix `eps in (0,1/2)`, and set

```
   a_eps := (1-2eps) nu / C_sharp ,  b_eps := (1-eps) nu / C_sharp ,
   c := b_eps - a_eps = eps nu / C_sharp .
```

A **traversal** is an interval `[t_i, t_i'] subset [0,tau]` with
`{d_1(t_i), d_1(t_i')} = {<= a_eps, >= b_eps}` in either order. `d_1` is
continuous on `[0,tau]` (`u in C([0,T];L^3)` by `prop:localtheory` with
`cor:Lq`, composed with the continuity of `w` from `lem:quotient-stability`,
exactly as in the measurability step of `cor:quotient-budgets`), so successive
traversals in alternating directions may be chosen pairwise disjoint.

**Theorem 4.1 (traversal-cost constraint; new, unconditional).** Let
`{[t_i,t_i']}_{i=1..N}` be pairwise disjoint traversals in `[0,tau]`,
`tau < min{H,T_*}`, and put `G_i := ||grad u(t_i)||_2 + ||grad u(t_i')||_2`.
Then

```
   sum_{i=1}^{N} G_i^{-3}  <=  Theta ,
   Theta := kappa_0^4 C_S^2 C_sharp^4 M(nu,E_0,H) / (eps^4 nu^4) ,           (4.1)
```

with `M` from (3.4). `Theta` depends only on `(nu, E_0, H, eps)`.

*Proof.* By Theorem 3.3, `c <= kappa_0 C_S^{1/2} G_i^{3/4} mu_i^{1/4}` with
`mu_i = mu([t_i,t_i'])`, so `mu_i >= c^4 kappa_0^{-4} C_S^{-2} G_i^{-3}`.
The intervals are disjoint and `mu` is a positive measure, so
`sum_i mu_i <= mu([0,tau]) <= M` by (3.4). Substitute `c = eps nu/C_sharp`. `[]`

**Scaling check.** `G^{-3} ~ (a^{-3},lambda^{3/2})`; and
`M nu^{-4} ~ (a^{1-4},lambda^{-5/2+4}) = (a^{-3},lambda^{3/2})`. OK.

**Corollary 4.2 (a count on moderate-enstrophy crossings).** For every
`Gamma > 0`, the number of pairwise disjoint traversals with `G_i <= Gamma`
is at most `Theta Gamma^3`. Equivalently: if infinitely many disjoint
traversals occur before `T_*`, then `G_i -> infinity` along them, fast enough
that `sum_i G_i^{-3} <= Theta`.

**Corollary 4.3 (conditional crossing count and bad-set structure).** Suppose
there is an input-only `Gamma = Gamma(nu,u_0,H,eps) < infinity` with

```
   ||grad u(t)||_2 <= Gamma  for every t < min{H,T_*} with
                             C_sharp d_1(t) in [(1-2eps)nu, (1-eps)nu] .     (C)
```

Then for every `tau < min{H,T_*}` the set
`B_tau^{eps} := {t < tau : C_sharp d_1(t) > (1-2eps) nu}` has at most
`1 + 8 Theta Gamma^3` connected components, and

```
   |B_tau^{eps}|  <=  24 C_S^2 C_sharp^4 E_0^2 / ((1-2eps)^4 nu^5)
```

uniformly in `tau` (HF21-B Lemma 4.3(3) with Chebyshev at the level
`(1-2eps)nu/C_sharp`). Since `B_tau subset B_tau^{eps}`, the bad set of (G) is
covered by an input-bounded **number** of intervals of input-bounded **total
measure**.

*Proof.* Each component of `B_tau^{eps}` that meets `{C_sharp d_1 >= (1-eps)nu}`
contains a traversal, with `G_i <= 2Gamma` by (C); by Corollary 4.2 there are
at most `Theta (2Gamma)^3 = 8 Theta Gamma^3` such disjoint traversals. A
component that does not meet `{C_sharp d_1 >= (1-eps)nu}` is contained in the
corridor and is separated from the next such component by a return below
`(1-2eps)nu/C_sharp`, i.e. by a traversal of the same corridor; at most one
component can fail to be preceded by one. The measure bound is Chebyshev with
`d_1 <= 2||u||_3` and \eqref{eq:L4L3} exactly as in HF21-B. `[]`

**Remark 4.4 (what a count does and does not buy).** By HF22-C Theorem B (the
good set is free in (G)) the reduction of (G) to its bad-set restriction is
already audited and needs no modulus. What Corollary 4.3 adds is *structure*:
finitely many bad intervals, of input-bounded total measure. It does **not**
bound `int_{B} d_1 D_3(w) dt`, and it does not bound `sup_t Q`, which is what
the bounded-variation cutoff of `hf22-direct-attack.md` Remark 3.6 would
additionally need. **No part of (G) is closed by Corollary 4.3, conditionally
or otherwise.**

**Remark 4.5 (the old-tools constraint, for comparison).** Running the same
argument on (3.8) gives `sum_i G_i^{-5} <= 2^8 C_S^4 E_0 M c^{-8}`, which is
weaker for small `c` and large `G_i`. So the `L^6` bound of
`prop:quotient-divcurl` genuinely improves the constraint, in exactly the
regime where it matters.

---

## 5. The exact obstruction

### 5.1 The residual is a single scalar

Assembling: the crossing-count route now consists of Theorem 3.3,
Theorem 4.1 and Corollary 4.3, and its *only* unproved input is (C), a
`tau`-uniform bound for `||grad u(t)||_2` **at corridor times**.

**Proposition 5.1 (localisation of the obstruction).** Modulo the audited
record, (C) implies an input-only crossing count and the bad-set structure of
Corollary 4.3. Conversely, nothing in the audited record supplies (C):

1. The only input-only spacetime budget for the enstrophy is
   `int_0^tau Y dt <= E_0/(2nu)` (`prop:energy`). It gives
   `|{t < tau : Y(t) > Lambda}| <= E_0/(2 nu Lambda)`, a **measure** bound; the
   corridor times form a set on which no such bound is informative, since a
   traversal is an interval whose endpoints are single instants.
2. The unrestricted form of (C), `sup_{t<min{H,T_*}} ||grad u(t)||_2 <= Gamma`
   with `Gamma` input-only, is **not admissible as a hypothesis** here: by
   \eqref{eq:qdc-interp}, \eqref{eq:qdc-sobolev-field} and `prop:energy` it
   gives `sup_{t<min{H,T_*}} ||u(t)||_3 <= C_S^{1/2}E_0^{1/4}Gamma^{1/2}`,
   which is `hyp:critical` verbatim, hence the Clay target by
   `thm:conditional`. Assuming it would therefore be circular. This is why (C)
   is stated with the corridor restriction, and it is also a warning: the
   corridor restriction is the entire distance between (C) and the conclusion,
   and an audit should test whether the restriction is real.
3. Whether (C) follows from the record, or is false, is **not decided here**.
   No implication (C) `=>` regularity is displayed, and none is claimed; nor
   is a counterexample to (C) exhibited.

### 5.2 Why the constraint cannot be improved to a count: the viscous-eddy family

The following is a **scaling-admissibility computation, bounded evidence, not a
solution and not a proof**. It shows that Theorem 4.1 is saturated, and that
every input-only budget in the record is compatible with infinitely many
crossings.

Consider a structure of length scale `l`, amplitude `A`, at Reynolds number
one, `A l = nu / C_sharp` — which is forced, since a crossing requires
`d_1 ~ nu/C_sharp` and `d_1 <= 2||u||_3 ~ A l`. Then, on its own time scale
`T_l = l/A = l^2 nu^{-1} C_sharp` (advective and viscous times coincide at
`Re ~ 1`):

```
   ||grad u||_2 ~ A l^{1/2} ~ nu l^{-1/2} =: G_l ,
   energy       ~ A^2 l^3   ~ nu^2 l ,
   int_{T_l} Y  ~ nu^2 l^{-1} * l^2 nu^{-1} = nu l ,
   g            ~ nu * nu l^{-1/2} + A^2 l^{3/2} ~ nu^2 l^{-1/2} ,
   mu(T_l)      ~ nu^2 l^{-1/2} * l^2 nu^{-1} = nu l^{3/2} ,
   |{bad}|      ~ T_l ~ l^2/nu ,
   d_1 change   ~ A l ~ nu / C_sharp .
```

Every one of these is summable over a dyadic sequence `l_k = 2^{-k}`: the
energies `sum nu^2 l_k`, the enstrophy budget `sum nu l_k`, the bad-set measure
`sum l_k^2/nu`, and the cost `sum mu_k = sum nu l_k^{3/2}` all converge. And
Theorem 4.1 is **exactly saturated**: `c^4 G_l^{-3} ~ nu^4 (nu l^{-1/2})^{-3}
= nu l^{3/2} ~ mu(T_l)`, while `sum_k G_{l_k}^{-3} = nu^{-3} sum_k l_k^{3/2}`
converges. So a sequence of crossings at scales `l_k -> 0`, one per structure
as it decays through `Re = 1`, violates no budget in the audited record and
none of the new ones.

Three consequences, stated separately because they have different strengths.

1. **(3.5) is scaling-sharp**: the `G^{3/4}mu^{1/4}` combination reproduces the
   family's `d_1`-change exactly, `(nu l^{-1/2})^{3/4}(nu l^{3/2})^{1/4} = nu`.
   No rearrangement of the same ingredients does better.
2. **No input-only modulus in `mu` alone exists** — i.e. the factor `G` in
   (3.5) cannot be deleted — *provided* such structures occur, since along the
   family `mu -> 0` while the `d_1`-change stays at `nu/C_sharp`. Whether they
   occur on an actual trajectory of a fixed Schwartz datum is precisely the
   blow-up question, so this is an obstruction to the *method*, not a
   refutation of the statement. It is, however, decisive for the method: any
   proof of a `G`-free modulus would have to exclude `Re ~ 1` structures at
   small scales, which no input-only budget does.
3. **A crossing count is not implied by any summability the record provides.**
   The record bounds `sum_k` of the crossing *measures* and `sum_k G_k^{-3}`;
   both converge for a divergent number of crossings. This is the exact
   obstruction the lane was asked to prove, and it is stronger than saying "no
   count is derivable": the specific summable structure of the family shows
   *why* every currency available (time measure, enstrophy budget, `mu`-cost)
   is a convergent series along a crossing cascade.

### 5.3 One direction that is genuinely closed off

The `mu`-currency cannot be traded back for time. Suppose one tries to feed the
`mu`-modulus into the (H-mod) consumer of `hf22-direct-attack.md` by replacing
the Lipschitz cutoff `|rho'| <= Lambda` with `|rho'(t)| <= Lambda g(t)`. The
consumer needs `int_0^tau |rho'| Q dt` input-bounded, i.e.
`int_0^tau g(t) Q(t) dt` input-bounded. But
`Q <= (1/3)||u||_3^3 <= (1/3)C_S^{3/2}E_0^{3/4}Y^{3/4}` and
`g <= nu Y^{1/2} + C_S^{3/2}E_0^{1/4}Y^{3/4}`, so `gQ` is of size
`nu E_0^{3/4} Y^{5/4} + C_S^{3} E_0 Y^{3/2}`, and neither `int Y^{5/4}` nor
`int Y^{3/2}` is input-bounded: `prop:energy` supplies only `int Y`, and by
`rem:mismatch` no supercritical time integral of `Y` follows from it. So the
`mu`-modulus of Theorem 3.3 **does not** discharge (H-mod), and the route
through the Lipschitz-in-`t` cutoff remains exactly as open as HF22-D left it.
This is a derivability statement about the displayed consumer, not a claim that
(H-mod) is false; by HF22-D Lemma R1, (H-mod) is implied by the conclusion and
so cannot be refuted by any construction short of a blow-up.

### 5.4 Non-derivability versus falsity, itemised

| Statement | Status here |
|---|---|
| `q in L^3` from `sigma in L^2` via the potential | **Not derivable**; the general implication `sigma in L^2 => q in L^2` is **false** (Remark 2.3), and `sigma in L^{3/2}` is the unproved (H2) |
| Input-only modulus for `t -> ||q(t)||_6` | Equivalent to a modulus for `sigma` in `L^2` (Prop. 2.1); **not derivable**, no modulus for `sigma` exists in the record |
| Input-only modulus for `d_1` in `t` | **Not derivable**; not shown false; by HF22-D Lemma R1 it is implied by the conclusion |
| Input-only modulus for `d_1` in `mu` with the `G` factor | **PROVED**, Theorem 3.3 (unaudited) |
| Input-only modulus for `d_1` in `mu` without `G` | **Not derivable**, and refuted along the viscous-eddy family in the sense of §5.2(2); not refuted for a fixed datum |
| Input-only crossing count | **Not derivable**; conditional on (C), Corollary 4.3; not shown false |
| (C) itself | **Undecided**; its unrestricted form is inadmissible (circular), §5.1(2) |
| (G) | **Untouched**: neither proved nor refuted |

---

## 6. Frontier record

**MODE / RESULT:** DISCOVER. Partial positive result plus an exact obstruction.

**CLAIM AND SCOPE.** For the maximal classical branch of `prop:localtheory` at
arbitrary `nu > 0` and arbitrary divergence-free Schwartz datum, with
`mu` and `M` as in Lemma 3.2 and `G` as in Theorem 3.3:

1. (Prop. 2.1) `||q(t')-q(t)||_6` and `||sigma(t')-sigma(t)||_2` are equivalent
   up to `C_S`; the potential representation controls `L^6` and nothing
   sharper, and reaching `L^3` needs `sigma in L^{3/2}` (unproved (H2)) or
   `w in L^2` (not asserted; and `sigma in L^2 => q in L^2` is false in
   general).
2. (Lemma 3.1) `||w(u')-w(u)||_3^3 <= 4 int (|w|+|w'|)|u'-u|^2` — a weighted
   refinement of `lem:quotient-stability`, minimiser-free on the right up to
   the weight, obtained without differentiating the minimiser.
3. (Lemma 3.2) `||u(t')-u(t)||_{Hdot^{-1}} <= mu([t,t'])` with
   `mu([0,tau]) <= M(nu,E_0,H)` input-only, uniformly in `tau < min{H,T_*}`.
4. (Theorem 3.3) `| ||q(t')||_3 - ||q(t)||_3 | <= kappa_0 C_S^{1/2} G^{3/4}
   mu([t,t'])^{1/4}`, `kappa_0 < 2.65`, scaling-critical on both sides. This
   removes both trajectory-dependent quantities of the audited modulus
   (HF21-B Remark 2.2) and replaces them by the endpoint enstrophy alone; the
   `L^6` estimate of `prop:quotient-divcurl` is what improves the exponent from
   `mu^{1/8}` to `mu^{1/4}`.
5. (Theorem 4.1) For pairwise disjoint corridor traversals,
   `sum_i (||grad u(t_i)||_2 + ||grad u(t_i')||_2)^{-3} <= Theta(nu,E_0,H,eps)`.
   This is a new unconditional constraint on the bad set, the first since
   HF21-B, and it is scaling-consistent.
6. (Cor. 4.3) Conditional on (C) — a `tau`-uniform input-only bound for
   `||grad u||_2` **at corridor times only** — the bad set is covered by
   `1 + 8 Theta Gamma^3` intervals of total measure
   `<= 24 C_S^2 C_sharp^4 E_0^2 ((1-2eps)nu)^{-4} nu^{-1}`.

**EVIDENCE.** Proofs above from `lem:quotient-minimizer`(c),
\eqref{eq:cp-lipschitz}, \eqref{eq:cp-monotone}, the cancellation step of
`lem:quotient-stability`, \eqref{eq:qdc-sobolev}, \eqref{eq:qdc-interp},
\eqref{eq:qdc-sobolev-field}, \eqref{eq:qdc-potential},
\eqref{eq:riesz-symbol}, `prop:energy`, `prop:scaling`(iii), (R1)–(R3), and
Plancherel; scaling weights displayed for (3.3)–(3.5) and (4.1). The
viscous-eddy computation of §5.2 is dimensional bounded evidence and is
labelled as such; it proves nothing and constructs no solution.

**FIRST GAP.** (C): a `tau`-uniform, input-only upper bound for
`||grad u(t)||_2` at the times `t < min{H,T_*}` with
`C_sharp ||q(t)||_3 in [(1-2eps)nu, (1-eps)nu]`. Given (C) the crossing count
and the bad-set structure follow by Theorem 4.1; without it, §5.2 shows that
every input-only budget in the record is a convergent series along a crossing
cascade at `Re ~ 1` and scales `l_k -> 0`, so no count follows.

**SURVIVING CONDITIONAL SUFFIX.** (i) If (C) holds for one `eps in (0,1/2)`
with an input-only `Gamma`, then Corollary 4.3 holds and (G) reduces — using
the audited HF22-C Theorem B for the good set — to a bound for
`int_{B} ||q||_3 D_3(w) dt` over at most `1 + 8 Theta Gamma^3` intervals of
input-bounded total measure. (ii) If in addition such a bad-interval bound is
produced with an input-only constant, then (G) holds, hence `hyp:highstrain`
with `theta = 0` and no cutoff (`rem:highstrain-normalisation`), hence
`hyp:critical` by `prop:quotient-conditional`, hence the Clay target by
`thm:conditional`. Neither hypothesis is established here.

**NON-CLAIMS.** No proof of (G), `hyp:highstrain`, `hyp:highpressure`,
`hyp:absorption`, `hyp:critical`, or NS-R3, and no claim that any of them is
false. No input-only modulus of continuity in the time variable: Theorem 3.3 is
a modulus in the measure `mu` only, and §5.3 shows it does **not** discharge
(H-mod) of `hf22-direct-attack.md`. No unconditional crossing count. No bound
on `sup_t Q`, `sup_t ||u||_3`, `sup_t ||grad u||_2`, `int D_3(w) dt`,
`int Y^{5/4} dt` or `int Y^{3/2} dt` is claimed or used. The minimiser is never
differentiated in time or space; `w in L^2` and `sigma in L^{3/2}` are never
used or asserted; no Clarkson inequality and no uniform convexity is used. No
smallness hypothesis appears anywhere; no forced, periodic, hyperdissipative or
Euler substitute appears; all statements are for the unforced branch on `R^3`
at arbitrary `nu > 0` and arbitrary divergence-free Schwartz datum. The family
of §5.2 is a dimensional computation, **not** a Navier--Stokes solution and
never claimed to be one; nothing is inferred from it except non-derivability of
the method. Priority and novelty are not claimed for anything here beyond
"not located in the audited repository record". Nothing is promoted; no
manuscript, graph, or status file is touched.

**NEXT DISTINCT ACTION.** Two, in order.

1. Decide (C). The cheapest sub-question is whether the corridor condition
   `C_sharp||q(t)||_3 ~ nu` carries **any** information about `||grad u(t)||_2`.
   The audited record supplies one implication in the wrong direction —
   `d_1 <= 2||u||_3 <= 2C_S^{1/2}E_0^{1/4}Y^{1/4}`, i.e. a *lower* bound
   `Y >= (nu/(2 C_sharp C_S^{1/2}E_0^{1/4}))^4 (1-2eps)^4` on the corridor —
   and Corollary `cor:quotient-vorticity-zero` plus
   `lem:quotient-mixed-pressure` are the only further links between the
   minimiser data and derivative norms of `u`. Whether an upper bound is
   available, or whether (C) can be shown to imply the Clay conclusion (which
   would retire the route as circular), is the decisive question.
2. Independently, audit Theorem 3.3 and Theorem 4.1. They are the reusable
   objects here even if (C) fails: Theorem 3.3 is, as far as the audited record
   shows, the first modulus here whose constant contains no supremum of a
   critical norm, and
   Theorem 4.1 is a constraint on the bad set that does not pass through the
   crossing measure. Scopes for the audit: (a) the Bochner-integral and
   `Hdot^{-1}` steps of Lemma 3.2, including the low-frequency behaviour of
   `d_t u`; (b) the weighted Cauchy--Schwarz and the finiteness claims in
   Lemma 3.1; (c) the difference form of \eqref{eq:qdc-sobolev-field} used in
   Proposition 2.1 and step (ii) of Theorem 3.3; (d) the disjointness and
   component-counting bookkeeping in Corollary 4.3.

- needs review: whether Lemma 3.1 has independent value for the **bad-set**
  part of (G): its right side `int(|w|+|w'|)|h|^2` is a weighted `L^2` object
  of the same shape as the audited `int |w| sigma^2 <= D_3(w)/2` of HF18-B, and
  a comparison between the two weighted quantities has not been attempted here.
- needs review: whether the exponent `1/4` in Theorem 3.3 can be raised to `1`
  (Lipschitz in `mu`), which is HF22-B sub-question (b) in the `mu`-currency and
  would improve the traversal cost from `c^4G^{-3}` to `c G^{-1}` — the
  audit of HF22-B recorded that an exponent above one is refuted, and said
  nothing about exponents between `1/4` and `1`.
- needs review: whether the `Hdot^{-1}` bounded-variation Lemma 3.2 improves
  any other estimate in the programme; it is elementary and appears not to be
  in the record, and it is the only input-only *pointwise-in-time-integrated*
  statement about `d_t u` currently available.
