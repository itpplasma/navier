> **STOPPED MID-REPAIR, 2026-09-06. DO NOT RELY ON THIS FILE.**
> This lane was halted by the controller while it was in the middle of fixing a
> defect it had itself just found: a vacuity bug in the corollary to its own
> Theorem D. That fix was never completed, so the file is an interrupted draft,
> not a finished lane report, and it has not been audited. It is preserved
> because its failed strategies have value, not because its conclusions stand.
> The adversarial half of the same wave *did* complete and is recorded in
> `hf29-corridor-obstruction.md` and in `PLAN.md`; that half already establishes
> the hypothesis is unfalsifiable here, is not derivable from the record's
> scalar closure, and is not an estimate.

# HF29: can the corridor hypothesis (C) be proved unconditionally?

**STATUS. NOTHING IN THIS FILE IS AUDITED.** Lane HF29, **MODE: DISCOVER**,
2026-09-06. This is the lane's own output, written before any independent
review; every theorem below is unreviewed, every numerical check is bounded
evidence and not proof, and nothing is promoted. No graph node changes, the
manuscript is untouched, no other repository file is edited, nothing is
committed. Owned file: `research/evidence/hf29-corridor-unconditional.md`.

**RESULT IN ONE LINE.** (C) is **not proved**. What is proved is that the
failure of (C) is exactly a *permanent oscillation of a scale-invariant shape
functional across a fixed level*, that every blow-up along which that
functional converges satisfies (C), and that no such oscillation can be
excluded by any instantaneous inequality, by any modulus of continuity in an
input-only currency, or by the closed scalar ledger the audited record
supplies — the last shown by an explicit consistent model. The sharpest
obstruction is stated as one inequality in §5.

---

## 0. The exact statement attempted

Fix `nu > 0`, a divergence-free Schwartz `u_0`, `0 < H < infinity` and
`eps in (0,1/2)`. With `(u,p)` the maximal classical branch on `[0,T_*)`,
`d_1(t) = ||q(u(t))||_3`, `C_sharp = (3/2)C_9C_S`,

```
   Corr := { t < min(H,T_*) : C_sharp d_1(t) in [(1-2eps)nu, (1-eps)nu] } ,

   (C)  there is a finite input-only Gamma = Gamma(nu,u_0,H,eps) with
        ||grad u(t)||_2 <= Gamma  for every t in Corr .
```

By Proposition R1 of `hf24-review-modulus-of-continuity.md` (audited; the one
step of its proof that this lane re-derives, in a sharper form, is Lemma 1.1
below), (C) holds if and only if either `H < T_*`, or `T_* <= H` and there
is `t_0 < T_*` with `C_sharp d_1(t) > (1-eps)nu` on `(t_0,T_*)`. The lane's
target is therefore, verbatim:

```
   TARGET (T).  If T_* < infinity, then there is t_0 < T_* with
                C_sharp d_1(t) > (1-eps) nu  for every t in (t_0,T_*).
```

Equivalently: *the trajectory cannot re-enter the corridor band at times
accumulating at `T_*`.* A proof of (T) makes (C) unconditional and the HF24-A
reduction hypothesis-free.

**MODE / RESULT: DISCOVER, negative with structure.** (T) is not proved and not
refuted. Eight results, A–H, are proved unconditionally (§2), five proof strategies
are carried out and each fails at a named point (§3), the best of them is
attacked and survives only as a partial result (§4), and the obstruction is
stated as a precise inequality and a precise missing implication (§5).

---

## 1. Setting, audited inputs, conventions

**Inputs** [DI = directly inspected in this lane]:

- `../navier-paper/main.tex`: `prop:localtheory` (R1)–(R4), `prop:energy`,
  `prop:scaling`(iii) \eqref{eq:L4L3}, `lem:serrin-enstrophy`,
  `thm:continuation` \eqref{eq:endpoint}, `hyp:critical`, `thm:conditional`,
  `lem:quotient-coercive` \eqref{eq:cp-coercive}, `lem:quotient-scaling`,
  `lem:quotient-stability` \eqref{eq:cp-strong}, `lem:quotient-minimizer`,
  `def:qe-dissipation`, `lem:qe-weighted-dissipation`
  \eqref{eq:qe-weighted-coercive}, `prop:quotient-evolution`
  \eqref{eq:quotient-evolution}, `prop:quotient-conditional`,
  `prop:quotient-divcurl`, `rem:no-monotone`, and the operator constants
  `C_P, C_6, C_9` with `||u||_9 <= C_9 ||w||_9`.
- `hf24-review-modulus-of-continuity.md` (audited): **Proposition R1**,
  Corollary 4.3'.
- `hf24-modulus-of-continuity.md` (audited REPAIR, repairs applied): Lemma 3.1,
  **Lemma 3.2** (the `mu`-currency), **Theorem 3.3** (the modulus).
- `hf21-crossing-sign-structure.md` (audited REPAIR, repairs applied):
  Proposition 3.1 (`|K| <= C_sharp d_1 D_3(w)`), Theorem 4.5, Lemma R3,
  obstructions O1–O3, Proposition 4.6 (the explicit-family method).
- `hf20-harmonic-strain-test.md` (audited REPAIR, repairs applied):
  Theorem 1.1' and §§3–4 (the swirl `U` with `w(U) = U`, the compact `h`).
- `hf18-*`, `hf23-*`, `hf25-*`, `hf26-review-actual-flow-departure.md` read as
  background; the only load-bearing items from them are the ones already listed
  through the manuscript labels. HF26-C `thm:NSdeparture` and its corollary are
  cited once, in §3.4, as evidence *against* a route, never as a step.

**Conventions.** `Q(t) = Q(u(t))`, `w(t) = w(u(t))`, `q = w - u`, `A = |w|w`,
`D_Q(t) = D_Q(u(t)) >= 0`, `K(t)` the transport term,
`E_0 = ||u_0||_2^2`, `Y(t) = ||grad u(t)||_2^2`, `G(t) = Y(t)^{1/2}`.
`M := {u solenoidal : q(u) = 0} = {div(|u|u) = 0}`. `D_lambda v := lambda v(lambda .)`.
All statements are on the maximal classical branch; `Q in C^1` and `D_Q, K`
continuous by `prop:quotient-evolution`.

**The five audited scalar relations used throughout.**

```
 (A1)  Q' + nu D_Q = K ,  D_Q >= 0                    prop:quotient-evolution
 (A2)  |K| <= C_sharp d_1 D_Q ,  C_sharp = (3/2)C_9C_S    HF21-B Prop. 3.1
 (A3)  ||u||_3^3/(3C_P^3) <= Q <= ||u||_3^3/3  and
       d_1 <= (1+C_P)(3Q)^{1/3}                       lem:quotient-coercive
 (A4)  ||w||_9^3 <= a_0 D_Q ,  a_0 = 9C_S^2/8 ;  ||u||_9 <= C_9||w||_9
                                       eq:qe-weighted-coercive + Leray on L^9
 (A5)  sup_t ||u||_2^2 <= E_0 ,  int_0^tau Y <= E_0/(2nu) ,
       int_0^tau ||u||_3^4 <= 3C_S^2E_0^2/(2nu)     prop:energy, prop:scaling(iii)
```

Two constants are used so often that they are named here:

```
 kappa_0 := 8 . 3^{1/3} / (C_S^2 C_9^3 E_0^2) ,
 Q_nu    := 8 nu^3 / (81 C_9^3 C_S^3 (1+C_P)^3)  =  nu^3/(3 C_sharp^3 (1+C_P)^3) .
```

### 1.1 The one inequality everything rests on

From (A1)+(A2), on all of `[0,T_*)`

```
   Q'(t) <= ( C_sharp d_1(t) - nu ) D_Q(t) .                              (1.1)
```

This is HF21-B Theorem 4.5(2). Combined with `thm:continuation` it gives the
statement that drives Proposition R1 and this whole lane:

> **Lemma 1.1 (no final interval below the level `nu`).** If `T_* < infinity`
> then there is no `t_0 < T_*` with `C_sharp d_1 <= nu` on `(t_0,T_*)`.
> Consequently `limsup_{t -> T_*} C_sharp d_1(t) >= nu`.

*Proof.* If `C_sharp d_1 <= nu` on `(t_0,T_*)` then `Q' <= 0` there by (1.1)
and `D_Q >= 0`, so `Q <= Q(t_0)` on `(t_0,T_*)`; with `Q` continuous on the
compact `[0,t_0]` and (A3), `sup_{t<T_*}||u(t)||_3 < infinity`, so `T_* = infinity`
by `thm:continuation` \eqref{eq:endpoint}. For the consequence: if
`limsup C_sharp d_1 < nu`, then `C_sharp d_1 <= (limsup + nu)/2 < nu` on some
final interval. `[]`

Note the level: Lemma 1.1 is at `nu`, not at `(1-2eps)nu` as in R1's proof.
That one-line strengthening is what makes Theorem A below sharp.

---

## 2. What is proved here

### Theorem A (exact failure mode: a factor-two oscillation)

> Let `T_* < infinity` and `T_* <= H`. Then **(C) fails if and only if**
>
> ```
>    there is a sequence t_n -> T_*  with  C_sharp d_1(t_n) <= (1-eps) nu . (2.1)
> ```
>
> (2.1) implies `liminf_{t->T_*} C_sharp d_1 <= (1-eps)nu`, and the strict
> inequality `liminf < (1-eps)nu` implies (2.1); at `liminf = (1-eps)nu`
> exactly, both alternatives are possible and (2.1) decides.
>
> Moreover, if (C) fails then `limsup_{t->T_*} C_sharp d_1(t) >= nu`, and for
> every `t_0 < T_*` there are `t_0 < alpha < beta < T_*` with
>
> ```
>    C_sharp d_1(alpha) = (1-eps) nu ,   C_sharp d_1(beta) = nu ,
>    (1-eps)nu <= C_sharp d_1 <= nu   on [alpha,beta] .                   (2.2)
> ```
>
> Such a pair `[alpha,beta]` is called a **traversal**; every traversal carries
> `|d_1(beta) - d_1(alpha)| = eps nu / C_sharp`. Failure of (C) therefore
> requires infinitely many disjoint traversals accumulating at `T_*`.

*Proof.* By R1, in the branch `T_* <= H < infinity`, (C) holds iff alternative
(ii) holds, i.e. iff `C_sharp d_1 > (1-eps)nu` on some final interval; the
negation of that is literally (2.1). (`d_1` is continuous by
`lem:quotient-stability` \eqref{eq:cp-strong} and `u in C([0,T];L^3)`; the
`liminf` remarks are immediate, and the borderline case is genuine: `d_1`
decreasing strictly to `(1-eps)nu/C_sharp` has `liminf = (1-eps)nu` and
satisfies (ii), while `d_1` oscillating with minima at the wall violates it.)
The `limsup` statement is Lemma 1.1. For (2.2): given `t_0`, pick
`t_1 in (t_0,T_*)` with `C_sharp d_1(t_1) <= (1-eps)nu` by (2.1), and
`t_2 in (t_1,T_*)` with `C_sharp d_1(t_2) > nu` by Lemma 1.1 applied on
`(t_1,T_*)`. Put `beta := inf{ t > t_1 : C_sharp d_1(t) = nu }`; the set is
nonempty (intermediate value theorem on `[t_1,t_2]`) and closed, and
`C_sharp d_1 < nu` on `[t_1,beta)`. Put
`alpha := sup{ t in [t_1,beta] : C_sharp d_1(t) = (1-eps)nu }`; the set is
nonempty (it contains a point of `[t_1,beta)` by the intermediate value
theorem, since `C_sharp d_1(t_1) <= (1-eps)nu < nu = C_sharp d_1(beta)`;
if `C_sharp d_1(t_1) = (1-eps)nu` take `t_1` itself) and closed. By
maximality of `alpha` and minimality of `beta`, `(1-eps)nu <= C_sharp d_1 <= nu`
on `[alpha,beta]`. `[]`

**Reading.** Failure of (C) is not "re-entry into a band". It is a *permanent
oscillation of `d_1` across the fixed interval `[(1-eps)nu, nu]/C_sharp`*, with
amplitude at least `eps nu/C_sharp` and with infinitely many complete
traversals accumulating at `T_*`. Both walls are at fixed multiples of
`nu/C_sharp`: the oscillation cannot shrink.

### Corollary A' (the target in its weakest useful form)

> Let `T_* < infinity` and `T_* <= H`. Then (C) holds for **some**
> `eps in (0,1/2)` if and only if
>
> ```
>    liminf_{t -> T_*} C_sharp d_1(t)  >  nu/2 .
> ```
>
> Consequently the whole content of the corridor route is:
>
> ```
>   at a finite-time singularity, does  C_sharp d_1  stay eventually above
>   nu/2, given that it must exceed nu infinitely often (Lemma 1.1)?
> ```

*Proof.* If `liminf C_sharp d_1 = rho nu` with `rho > 1/2` (`rho = infinity`
included), pick `eps in (1-rho, 1/2)`, a nonempty interval; then
`(1-eps)nu < rho nu`, so `C_sharp d_1 > (1-eps)nu` on a final interval, which
is R1(ii), so (C) holds at that `eps`. Conversely (C) at `eps in (0,1/2)` gives
R1(ii), hence `liminf >= (1-eps)nu > nu/2`. `[]`

This matters because the HF24-A reduction (Corollary 4.3') is stated for one
fixed `eps in (0,1/2)`, so the *easiest* admissible target is `eps` near `1/2`.
The gap between what is proved (Lemma 1.1: exceeds `nu` infinitely often) and
what is needed (stays above `nu/2` eventually) is exactly a factor of two and
an upgrade from "infinitely often" to "eventually".

### Theorem B (a trapping threshold: the critical norm has a floor)

> Put `Q_nu = nu^3/(3 C_sharp^3 (1+C_P)^3)`. Then for every `Q_1 < Q_nu` the
> sublevel set `{Q <= Q_1}` is forward invariant along the classical branch,
> and
>
> ```
>   T_* < infinity   ==>   Q(t) >= Q_nu   and
>                          ||u(t)||_3 >= (3Q_nu)^{1/3} = 2 nu /(3 C_9 C_S (1+C_P))
>   for every t in [0,T_*) .                                              (2.3)
> ```

*Proof.* Fix `Q_1 < Q_nu` and put `eta := 1 - (Q_1/Q_nu)^{1/3} in (0,1]`. By
(A3), `Q(t) <= Q_1` implies
`C_sharp d_1(t) <= C_sharp(1+C_P)(3Q_1)^{1/3} = nu (Q_1/Q_nu)^{1/3} = (1-eta)nu`,
so by (1.1) and Theorem C(i) below (whose proof is independent of this one),

```
   Q(t) <= Q_1   ==>   Q'(t) <= -eta nu D_Q(t) <= -eta nu kappa_0 Q(t)^{7/3} < 0
```

as long as `Q(t) > 0` (and if `Q(t) = 0` then `u(t) = 0` by (A3), the branch is
trivial and `T_* = infinity`). Suppose `Q(t_1) <= Q_1` and `Q(s) > Q_1` for
some `s > t_1`. Put `r := sup{ t in [t_1,s] : Q(t) <= Q_1 }`. Then `r < s`,
`Q(r) = Q_1` by continuity, and `Q(t) > Q(r)` for `t in (r,s]`, so
`Q'(r) >= 0`; but `Q(r) <= Q_1` gives `Q'(r) < 0`. Contradiction. Hence
`{Q <= Q_1}` is forward invariant, and on it `Q` is strictly decreasing, so
`Q(t) <= Q(t_1)` for all `t in [t_1,T_*)`. With (A3) and continuity of `Q` on
the compact `[0,t_1]`, `sup_{t<T_*}||u||_3 < infinity`, so `T_* = infinity` by
`thm:continuation` \eqref{eq:endpoint}. Contrapositive: `T_* < infinity` forces
`Q(t) > Q_1` for every `Q_1 < Q_nu` and every `t`, i.e. `Q >= Q_nu`; (A3)
converts this into the `L^3` statement. `[]`

**Attribution.** This is the quotient-route form of the critical small-data
theorem, which the audited HF18-A already records as recovered (`Q` is a
Lyapunov functional under critical smallness, with ESS). Nothing here is
claimed as new except the explicit threshold `2nu/(3C_9C_S(1+C_P))` and the
forward-invariance form, both of which are one-line consequences of audited
statements. The threshold is *sharp within this argument* only insofar as the
constant `(1+C_P)` in (A3) is: the best constant
`c_* := sup{ d_1(v)/||v||_3 : v solenoidal, v != 0 } <= 2` is not determined in
the record, and any improvement of `c_*` raises the floor to `nu/(c_* C_sharp)`.

### Theorem C (instantaneous forgetting on the good set, and its two corollaries)

> **(i) Dissipation is superlinear in the quotient.** At every `t < T_*`,
>
> ```
>    D_Q(t) >= kappa_0 Q(t)^{7/3} ,   kappa_0 = 8 . 3^{1/3}/(C_S^2C_9^3E_0^2). (2.4)
> ```
>
> **(ii) Forgetting.** If `C_sharp d_1 <= (1-delta) nu` on `[a,b] subset [0,T_*)`
> for some `delta in (0,1]`, then
>
> ```
>    Q(t) <= ( Q(a)^{-4/3} + (4/3) delta nu kappa_0 (t-a) )^{-3/4}
>         <= ( (4/3) delta nu kappa_0 (t-a) )^{-3/4} ,  t in (a,b] ,       (2.5)
> ```
>
> the second bound being independent of `Q(a)`.
>
> **(iii) Density of near-critical times.** If `T_* < infinity` then every
> subinterval of `(0,T_*)` of length exceeding
>
> ```
>    L_delta := 729 C_S^6 C_9^7 (1+C_P)^4 E_0^2 / (512 delta nu^5)          (2.6)
> ```
>
> contains a time with `C_sharp d_1 > (1-delta)nu`.

*Proof.* (i) By (A4), `D_Q >= ||w||_9^3/a_0 >= ||u||_9^3/(C_9^3a_0)`. Lebesgue
interpolation with `1/3 = (4/7)(1/2) + (3/7)(1/9)` gives
`||u||_3 <= ||u||_2^{4/7}||u||_9^{3/7}`, i.e.
`||u||_9^3 >= ||u||_3^7/||u||_2^4 >= ||u||_3^7/E_0^2` by (A5). By (A3),
`||u||_3^3 >= 3Q`, so `||u||_3^7 >= (3Q)^{7/3}`. Collecting,
`D_Q >= 3^{7/3}Q^{7/3}/(C_9^3a_0E_0^2)` and `3^{7/3}/a_0 = 8 . 3^{1/3}/C_S^2`.

(ii) On `[a,b]`, (1.1) gives `Q' <= -delta nu D_Q <= -delta nu kappa_0 Q^{7/3}`
by (i). `Q > 0` there (if `Q(t) = 0` then `u(t) = 0` by (A3) and the branch is
trivial with `T_* = infinity`), so `y := Q^{-4/3}` is `C^1` with
`y' = -(4/3)Q^{-7/3}Q' >= (4/3)delta nu kappa_0`. Integrating and inverting
gives (2.5).

(iii) If `C_sharp d_1 <= (1-delta)nu` on `[a,b]` with `b-a > L_delta`, then by
(2.5) and `(4/3)delta nu kappa_0 L_delta = Q_nu^{-4/3}` (verified symbolically:
see §7), `Q(b) < Q_nu`, so `T_* = infinity` by Theorem B. `[]`

**Reading.** (2.5) is a genuine smoothing statement in the quotient variable:
on the good set the trajectory forgets its quotient at rate `t^{-3/4}`,
uniformly in the initial value. It is the strongest positive tool this lane
found, and §3.1 shows exactly why it does not close (T).

### Theorem D (every shape-convergent blow-up satisfies (C))

> Let `T_* < infinity` and suppose the limit `d_infinity := lim_{t->T_*}d_1(t)`
> exists in `[0,+infinity]`. Then `C_sharp d_infinity >= nu`, and (C) holds
> (indeed R1 alternative (ii) holds) for **every** `eps in (0,1/2)`.

*Proof.* Suppose `C_sharp d_infinity < nu`. Then `C_sharp d_1 <= (C_sharp
d_infinity + nu)/2 < nu` on some final interval, contradicting Lemma 1.1.
Hence `C_sharp d_infinity >= nu > (1-eps)nu`, and by convergence
`C_sharp d_1 > (1-eps)nu` on a final interval, which is R1(ii).

`[]`

**Remark D.1 (the naive shape-convergence hypothesis is vacuous, and that is
ESS).** One would like to apply Theorem D to "asymptotically self-similar"
blow-ups through `|| u(t) - D_{lambda(t)}tau_{x(t)}U ||_3 -> 0` for a fixed
`U in L^3`. That hypothesis is **empty** at a finite-time singularity: it
forces `||u(t)||_3 -> ||U||_3 < infinity`, hence `T_* = infinity` by
`thm:continuation`. The correct hypothesis must therefore carry the amplitude,
which is Corollary D' below. Recording this explicitly because it is the first
thing one tries and because the vacuity *is* the endpoint theorem.

### Corollary D' (normalized shapes, and what a counterexample must look like)

Write `rho(t) := d_1(t)/||u(t)||_3 in [0,2]`, the **relative** distance to `M`;
`rho` is invariant under both `D_lambda` and amplitude scaling, and
`rho = 0` exactly on `M`.

> Let `T_* < infinity`. Suppose the normalized shape converges: there are
> `a(t) > 0`, `lambda(t) > 0`, `x(t)` and a fixed solenoidal `V in L^3`,
> `||V||_3 = 1`, with
> `|| u(t) - a(t) D_{lambda(t)} tau_{x(t)} V ||_3 / ||u(t)||_3 -> 0`.
> Then `rho(t) -> d_1(V)` and `d_1(t) = ||u(t)||_3 (d_1(V) + o(1))`. Hence:
>
> (a) if `d_1(V) > 0` and
> `liminf_{t->T_*}||u(t)||_3 > (1-eps)nu/(C_sharp d_1(V))`, then (C) holds;
>
> (b) if `d_1(V) = 0`, **nothing follows** — and this is exactly the
> undetermined case, since `d_1 = ||u||_3 . o(1)` is an indeterminate product
> when `||u||_3` is unbounded.
>
> Consequently, if (C) fails there are `t_n -> T_*` with
>
> ```
>    rho(t_n) . ||u(t_n)||_3  =  d_1(t_n)  <=  (1-eps) nu / C_sharp ,       (2.7')
> ```
>
> i.e. the trajectory returns infinitely often to *relative* distance at most
> `(1-eps)nu/(C_sharp ||u(t_n)||_3)` from the nonlinear-Hodge class, while by
> Lemma 1.1 it also leaves relative distance `nu/(C_sharp||u||_3)` infinitely
> often.

*Proof.* Write `u(t) = a(t)D_{lambda}tau_x (V + r(t))` with
`||r(t)||_3 -> 0`; this is the hypothesis after absorbing the isometries
(`D_lambda`, `tau_x` are `L^3` isometries and `d_1` is invariant under both by
`lem:quotient-scaling`). By homogeneity `d_1(alpha z) = alpha d_1(z)`
(`lem:quotient-scaling` with `w(alpha u) = alpha w(u)`) and continuity of `d_1`
on `L^3` (`lem:quotient-stability` \eqref{eq:cp-strong}, whose constant is
uniform on `L^3`-bounded sets and `||V + r||_3 -> 1`),
`d_1(u(t)) = a(t)(d_1(V) + o(1))` and `||u(t)||_3 = a(t)(1 + o(1))`, giving
`rho(t) -> d_1(V)`. (a) then gives
`C_sharp d_1(t) = C_sharp||u(t)||_3(d_1(V)+o(1)) > (1-eps)nu` on a final
interval, which is R1(ii). (2.7') is Theorem A (2.1) divided by `||u(t_n)||_3`.
`[]`

**Reading, and the answer to the lane's structural question 2.** `d_1` is a
*critical* functional: invariant under the parabolic rescaling, `1`-homogeneous
in the amplitude. Three consequences, in increasing order of interest.

1. Whenever `d_1` itself converges, alternative (ii) is **automatic**, and for
   a reason with no slack: a convergent `d_1` with `C_sharp d_infinity < nu`
   would make `Q` eventually nonincreasing and kill the singularity outright
   (Lemma 1.1). So (ii) is *generic*, not delicate, on the convergent class.
2. Criticality also makes the convergent class *nonempty but not the obvious
   one*: `L^3`-shape convergence without amplitude is vacuous (Remark D.1), so
   the natural class is the normalized one of Corollary D', where `d_1`
   converges only when the amplitude does.
3. The undetermined case is exactly Corollary D'(b): a normalized shape whose
   relative distance to `M` tends to zero at the rate `1/||u||_3`, oscillating
   about it. So the whole content of (T) is the exclusion of a blow-up whose
   shape approaches the nonlinear-Hodge class at *exactly* the critical rate,
   from both sides, for ever. Excluding permanent oscillation of a blow-up
   shape is structurally a uniqueness-of-blow-up-profile statement.
   *(This positioning against the literature is not source-checked in this
   lane and is not load-bearing.)*

### Proposition E (no instantaneous inequality can produce (T))

> For every `c > 0` and every `N, Lambda > 0` there is a divergence-free
> `v in C_c^infinity(R^3)^3` with
>
> ```
>    d_1(v) = c ,      ||v||_3 >= N ,     ||grad v||_2 >= Lambda .         (2.7)
> ```
>
> Consequently no lower bound `d_1(v) >= F(||v||_3, ||grad v||_2, ||v||_2, nu)`
> that is unbounded as `||v||_3 -> infinity`, or as `||grad v||_2 -> infinity`,
> can hold on solenoidal Schwartz fields; more generally no pointwise-in-time
> relation can force `d_1` upward from the fact that the trajectory is
> singular. Any proof of (T) must be dynamical.

*Proof.* Let `U, h` be the audited HF20 fields (§§3–4 of
`hf20-harmonic-strain-test.md`): `U, h in C_c^infinity`, solenoidal, `U != 0`,
`w(U) = U` (so `q(U) = 0`, `U in M`), and, with `C_e = ||e||_3^3/3` from that
construction, `||w(U + eps h) - U||_3^3 <= 6 C_e eps^3` for `0 < eps <= 1`.
Since `q(U+eps h) = (w(U+eps h) - U) - eps h`,

```
   d_1(U + eps h) <= ( (6C_e)^{1/3} + ||h||_3 ) eps  ->  0 ,
   ||U + eps h||_3 -> ||U||_3 > 0 .
```

Also `d_1(U + eps h) > 0` for `0 < eps < eps_0`: the transport term satisfies
`K(v) = -int q(v).((A(v).grad)v)`, so `q(v) = 0` implies `K(v) = 0`, while
HF20 Theorem 1.1' with (4.5) gives `K(U + eps h) <= -eps c_0/2 < 0` for
`0 < eps < eps_0`. Fix such an `eps` with
`||U+eps h||_3 / d_1(U+eps h) >= N/c`, possible since the ratio tends to
`+infinity`. Put `v := alpha D_lambda (U + eps h)` with `alpha := c/d_1(U+eps h)`.
By `lem:quotient-scaling`, `d_1(alpha D_lambda z) = alpha d_1(z)`, so
`d_1(v) = c`; `||v||_3 = alpha||U+eps h||_3 >= N`; and
`||grad v||_2 = alpha lambda^{1/2}||grad(U+eps h)||_2 -> infinity` as
`lambda -> infinity`. `v` is smooth, compactly supported and solenoidal. `[]`

**Reading, and the answer to the lane's structural question 3.** The endpoint
theorem gives *no* lower bound for `d_1`. The set `M` itself contains fields of
arbitrarily large critical norm and arbitrarily large enstrophy (rescale one
nonzero element of `M`, e.g. HF20's swirl: `d_1(D_lambda U) = 0`,
`||grad D_lambda U||_2 = lambda^{1/2}||grad U||_2`), and the level set
`{d_1 = c}` is unbounded in `L^3` and in `Hdot^1`. The only link in the record,
`d_1 <= (1+C_P)(3Q)^{1/3}`, is one-sided in the wrong direction. The
`||u||_3 -> infinity` mechanism therefore cannot force `d_1` up; only
Lemma 1.1's *dynamical* argument does, and it delivers "infinitely often",
never "eventually".

### Theorem F (no admissible currency for a modulus of continuity)

Call a pair `(X, nu_*)` a **currency** if `X` is a normed space of tempered
distributions, `nu_*` is a non-atomic Borel measure on `[0,min(H,T_*))` with
input-only total mass `N_tot(nu,u_0,H) < infinity`, and, for every classical
branch and all `0 <= t <= t' < min(H,T_*)`,

```
   ||u(t') - u(t)||_X  <=  Psi( nu_*([t,t']) )                             (2.8)
```

with `Psi` nondecreasing and `Psi(0+) = 0`. HF24-A Lemma 3.2 supplies exactly
one such currency: `X = Hdot^{-1}`, `nu_* = mu`, `Psi = id`.

> **(a)** Suppose `X` is scale-covariant with a strictly positive weight:
> `||D_lambda f||_X = lambda^{-theta}||f||_X` with `theta > 0` (`theta = 3/2`
> for `Hdot^{-1}`). Then `d_1` is **not** uniformly continuous with respect to
> `||.||_X` on `L^3`-bounded solenoidal sets: for any `v` with `d_1(v) = c > 0`,
> the family `D_lambda v` has `d_1(D_lambda v) = c` for all `lambda`,
> `||D_lambda v||_3 = ||v||_3`, and `||D_lambda v - 0||_X -> 0`. Hence no bound
> `|d_1(a) - d_1(b)| <= Phi(||a-b||_X)` with `Phi(0+) = 0` holds on such sets,
> and (2.8) cannot be converted into a modulus for `d_1` by continuity of the
> projection alone.
>
> **(b)** Suppose instead `X` embeds continuously in `L^3`, with constant
> `c_X`. Then at a finite-time singularity **no** currency `(X,nu_*)` exists:
> fix `n`, and since `s -> nu_*([0,s])` is continuous (non-atomicity) and
> `nu_*([0,tau]) <= N_tot`, choose `0 = s_0 < ... < s_n = tau` with
> `nu_*([s_{i},s_{i+1}]) <= N_tot/n`; then (2.8) and the triangle inequality
> give `||u(tau)||_3 <= ||u_0||_3 + c_X n Psi(N_tot/n) < infinity`, uniformly
> in `tau < T_*`, so `T_* = infinity` by `thm:continuation`.
>
> **(c)** Consequently every modulus for `d_1` derivable from the record must
> carry a factor that is a *supercritical* function of the trajectory at the
> endpoints. HF24-A Theorem 3.3 carries `G^{3/4}` with
> `G = ||grad u(t)||_2 + ||grad u(t')||_2`, and by (R4) that factor diverges
> exactly where (T) is needed.
>
> **(d)** The one escape not excluded by (a)–(c) is a modulus whose
> supercritical factor is *input-only*, e.g.
> `|d_1(t') - d_1(t)| <= C ||grad u_0||_2^{3/4} mu([t,t'])^{1/4}`, which is
> scaling-admissible (weights `(a,lambda^{-1})` on both sides) and would prove
> (T) by Proposition G. No step of the audited derivation produces it, and it
> is strictly stronger than the audited Theorem 3.3.

*Proof.* (a) is the displayed computation, using `lem:quotient-scaling` for
`d_1(D_lambda v) = d_1(v)` and the isometry of `D_lambda` on `L^3`. (b) is the
displayed partition argument; superadditivity of `N` gives the partition, and
`c_X` is the embedding constant. (c) is (a)+(b): the currency actually
available is `Hdot^{-1}` with `theta = 3/2 > 0`, so by (a) the passage to `d_1`
must go through a norm in which the concentration family does **not** vanish,
i.e. through a quantity that is not controlled by the input data alone; in
HF24-A's proof that quantity is `||h||_{Hdot^1} <= G`, entering through
`||h||_2^2 <= ||h||_{Hdot^1}||h||_{Hdot^{-1}}`. For (d), the scaling weights are
those of `hf24-review-modulus-of-continuity.md` §6.2 with `G` replaced by the
initial enstrophy, which has the same weights. `[]`

**Relation to the audit.** The review's §6.1 shows the exponent pair
`(3/4,1/4)` is forced *within monomials in `G` and `mu`*. Theorem F is the
route-level version: the *presence* of a positive power of a supercritical
endpoint quantity is forced, in every currency, by scaling alone.

### Proposition G (the traversal ledger: the exact residue of the crossing route)

> Let `T_* < infinity`, `T_* <= H`, and suppose (C) fails. Let `I_j =
> [alpha_j, beta_j]`, `j = 1,2,...`, be pairwise disjoint traversals given by
> Theorem A with `beta_j -> T_*`, and put
> `G_j := ||grad u(alpha_j)||_2 + ||grad u(beta_j)||_2`. Then
>
> ```
>    sum_j G_j^{-3}  <=  ( C_sharp kappa_mod C_S^{1/2} / (eps nu) )^4 . M(nu,E_0,H)
>                    < infinity ,                                          (2.9)
> ```
>
> with `kappa_mod = 1 + (2 sqrt5)^{1/3}` and `M` the HF24-A (3.4) budget.
> Equivalently, for every `Lambda > 0`,
> `#{ j : G_j <= Lambda } <= Lambda^3 (C_sharp kappa_mod C_S^{1/2}/(eps nu))^4 M`.
> Hence **(T) follows from, and only from, an input-only upper bound for
> `||grad u||_2` at the traversal endpoints** — which is (C) itself.

*Proof.* Apply HF24-A Theorem 3.3 on `I_j`: `eps nu/C_sharp = |d_1(beta_j) -
d_1(alpha_j)| <= kappa_mod C_S^{1/2} G_j^{3/4} mu(I_j)^{1/4}`, so
`mu(I_j) >= (eps nu/(C_sharp kappa_mod C_S^{1/2}))^4 G_j^{-3}`. The `I_j` are
pairwise disjoint and `mu` has an `L^1_loc` density, so
`sum_j mu(I_j) <= mu([0,T_*)) <= M` by (3.4). The counting form is Chebyshev.
For the last sentence: if `G_j <= Gamma` for all `j` then (2.9) bounds the
number of traversals, contradicting their infinitude; and `Gamma` bounding the
enstrophy at traversal endpoints is (C) at those times. `[]`

### Proposition H (the audited scalar ledger is consistent with failure of (T))

Let the **scalar ledger** be the following list, which contains every relation
of the audited record that constrains the corridor question and involves only
the scalar functions `Q, d_1, D_Q, ||u||_3, ||u||_2, ||grad u||_2` of time:

```
 (S1) Q in C^1, Q > 0; D_Q >= 0; d_1 >= 0 continuous;
      Q' + nu D_Q = K with |K| <= C_sharp d_1 D_Q                      [(A1),(A2)]
 (S2) 3Q <= ||u||_3^3 <= 3C_P^3 Q ;  d_1 <= (1+C_P)(3Q)^{1/3}                [(A3)]
 (S3) D_Q >= kappa_0 Q^{7/3}                                       [Theorem C(i)]
 (S4) ||u||_3^4 <= C_S^2 E_0 ||grad u||_2^2 ; ||u||_2^2 <= E_0             [(A5)]
 (S5) int_0^{T_*} ||grad u||_2^2 <= E_0/(2nu) ;
      int_0^{T_*} ||u||_3^4 <= 3C_S^2E_0^2/(2nu) ;
      int_0^{T_*} Q^{4/3} <= 3^{-1/3}C_S^2E_0^2/(2nu) =: M_Q                [(A5)]
 (S6) mu([0,T_*)) <= M(nu,E_0,H), dmu = (nu||grad u||_2 + ||u||_4^2)dt  [HF24-A 3.2]
 (S7) |d_1(t') - d_1(t)| <= kappa_mod C_S^{1/2}(G(t)+G(t'))^{3/4}mu([t,t'])^{1/4}
                                                                    [HF24-A 3.3]
 (S8) blow-up: limsup_{t->T_*}||u||_3 = infinity  [thm:continuation];
      ||grad u(t)||_2 -> infinity  [(R4)];  int_0^{T_*} D_Q = infinity
      [else int ||u||_9^3 < infinity, an LPS criterion: prop:quotient-conditional]
 (S9) Q(t) > Q_nu for all t                                        [Theorem B]
```

> There exist explicit scalar functions `Q, d_1, D_Q, ||u||_3, ||grad u||_2` on
> `[0,1)` satisfying **every** item of (S1)–(S9) with `T_* = 1`, in which
> `C_sharp d_1` takes the value `0.6 nu` (inside the corridor band for
> `eps = 1/4`) and the value `1.2 nu` (above `nu`) on infinitely many disjoint
> intervals accumulating at `T_* = 1`. Hence (T) is **not derivable** from
> (S1)–(S9).

*Construction.* Constants `nu = 1`, `C_S = C_9 = C_P = 1` (the hardest
admissible choice: it maximises both `kappa_0` and `Q_nu`), `E_0 = 10`,
`H = 1`, `eps = 1/4`; then `C_sharp = 3/2`, band `= [1/3,1/2]` in `d_1`,
`nu/C_sharp = 2/3`, `kappa_0 = 0.11538`, `Q_nu = 0.012346`.
Cycles `J_n = [1-2^{-n}, 1-2^{-n-1})`, `n = 1,2,...`, `l_n = 2^{-n-1}`. On
`J_n`, with `x = (t - (1-2^{-n}))/l_n`, set

```
   d_1 = 0.4                       for x in [0,0.5) u [0.8,1)   (corridor: C#d1=0.6)
   d_1 = 0.4 + 4(x-0.5)            for x in [0.5,0.6)           (rise)
   d_1 = 0.8                       for x in [0.6,0.7)           (C#d1 = 1.2 > nu)
   d_1 = 0.8 - 4(x-0.7)            for x in [0.7,0.8)           (fall)
```

and define `Q` by: on `{C_sharp d_1 <= nu}` let `Q` solve
`Q' = (C_sharp d_1 - nu) kappa_0 Q^{7/3}` (the slowest decay the ledger
permits, i.e. `D_Q = kappa_0 Q^{7/3}` and `K` saturating (A2)); on the bad
phase `x in [0.6,0.7)` let `Q` increase geometrically to
`Q_n := (B n^{-2}/l_n)^{3/4}`, `B = 3`, and set
`D_Q := max( kappa_0 Q^{7/3}, Q'/(C_sharp d_1 - nu) )` there, `K := Q' + nu D_Q`.
Finally `||u||_3 := (3Q)^{1/3}` and `||grad u||_2 := ||u||_3^2/(C_S E_0^{1/2})`.

*Verification.* All of (S1)–(S9) are checked in §7 at resolution `4000` points
per cycle over `40` cycles; every item passes with the margins listed there.
The essential margins: `int Q^{4/3} = 5.6 <= 34.7`; `int ||grad u||_2^2 =
2.43 <= 5`; `mu([0,1)) = 3.97 <= 8.18`; the worst ratio in (S7) over all
`80` traversals is `0.23 <= 1`; `min Q = 5.58 > Q_nu = 0.0123`;
`max Q = 1.2 . 10^7`; `int D_Q = 6.2 . 10^7` and divergent as `n -> infinity`
(the cycle-`n` contribution grows like `2^{3n/4}n^{-7/2}`). `[]`

**Scope, stated in the form the HF22 audits demand.** Proposition H does **not**
say (T) is false, and it exhibits no Navier–Stokes solution. It says: any proof
of (T) must use information beyond (S1)–(S9) — that is, beyond the balance, the
transport bound, coercivity, the `L^9` dissipation bound, the three input-only
spacetime budgets, the audited modulus, and the blow-up alternatives. It is the
corridor analogue of HF21-B Proposition 4.6 (obstruction O2), with a longer
constraint list.

---

## 3. The four strategies, and where each failed

### 3.1 Strategy 1 — differential inequality and trapping (partial, then dead)

*Idea.* (1.1) makes `Q` nonincreasing off `{C_sharp d_1 > nu}` and, by
Theorem C, strictly and universally contracting on the good set. Try to force
`Q` below the trapping level `Q_nu` of Theorem B by charging each corridor
visit against a finite budget.

*What it produced.* Theorems B and C, and Theorem A's proof.

*Where it fails, quantitatively.* Let `y = Q^{-4/3} in (0, Q_nu^{-4/3})` at a
singularity (Theorem B). The good set raises `y` at the fixed rate
`(4/3)delta nu kappa_0` (Theorem C(ii)); reaching the trap requires
`Delta y = Q_nu^{-4/3}`. The *total* rise available over the whole life of the
solution is

```
   (4/3) delta nu kappa_0 |{good}| <= (4/3) delta nu kappa_0 T_*
      <= (4/3) delta nu kappa_0 M_Q / Q_nu^{4/3}
       = (16 delta / (3 C_9^3)) . Q_nu^{-4/3} ,                          (3.1)
```

using `T_* <= M_Q/Q_nu^{4/3}` (Theorem B with (S5)) and the exact identity
`nu kappa_0 M_Q = 4/C_9^3` (verified symbolically, §7). So the entire good-set
contraction budget of the entire trajectory amounts to at most
`16 delta/(3C_9^3)` full descents to the trap — **fewer than one whenever
`C_9 >= (16/3)^{1/3} = 1.75`**, which is the expected range for the Leray
projector on `L^9`. And even when the factor exceeds one, the bad set can undo
each descent at unbounded rate, because (1.1) gives no upper bound for `D_Q`
and none is available: an upper bound `D_Q <= F(Q)` is scaling-inadmissible
(`D_Q` has weight `(a^4,lambda^2)`, `Q` has `(a^3,lambda^0)`; the audited record
records that no monomial in `Q` and `D_3` closes).

*Verdict.* Dead as a route to (T), with an explicit deficit factor
`16 delta/(3C_9^3)`. Retained: Theorems B and C, which are used everywhere
else in this note.

### 3.2 Strategy 2 — crossing count through a modulus of continuity (dead)

*Idea.* Theorem A gives infinitely many traversals of fixed amplitude
`eps nu/C_sharp`; charge each against the input-only budget `mu`.

*What it produced.* Proposition G, which is the sharpest form of the residue,
and Theorem F.

*Where it fails.* Proposition G's ledger converges as soon as `G_j -> infinity`
fast enough, and (R4) guarantees `G_j -> infinity`. Theorem F shows this is not
an artefact of HF24-A's particular estimate: **every** currency in which the
velocity increment has an input-only modulus is strictly subcritical
(`Hdot^{-1}`, `theta = 3/2`), and in every such currency `d_1` is not even
continuous, by the concentration family `D_lambda v`. So a supercritical
endpoint factor is forced, and the only version with an input-only factor
(Theorem F(d)) is not derivable from any step of the audited proof.

*Verdict.* Dead, at route level, not at estimate level.

### 3.3 Strategy 3 — compactness/rigidity at corridor times (dead at step one)

*Idea.* Take corridor times `t_n -> T_*`; the corridor pins the scale-invariant
`d_1(t_n)` in a compact band, so extract a limiting profile and contradict
Lemma 1.1 or `rem:no-monotone`.

*Where it fails.* Concentration-compactness needs a bound on a critical norm
along `u(t_n)`. The corridor supplies none: by Proposition E the set
`{v : d_1(v) = c}` contains fields with `||v||_3` and `||grad v||_2`
arbitrarily large, and the only relation in the record between `d_1` and
`||u||_3` is the one-sided `d_1 <= (1+C_P)(3Q)^{1/3}`. Renormalising by `d_1`
is useless because `d_1` is invariant under the very symmetry one would quotient
by. The step that would supply a bound — "at corridor times the enstrophy is
bounded" — is (C).

*Verdict.* Dead. Recorded because the R1 audit names compactness as the only
remaining route; this lane finds its first step unavailable.

### 3.4 Strategy 4 — a lower bound for `d_1` from the endpoint theorem (dead)

*Idea.* `sup ||u||_3 = infinity` and `||grad u||_2 -> infinity`; extract a
lower bound `d_1 >= f(||u||_3)` or `d_1 >= f(||grad u||_2)`.

*Where it fails.* Proposition E: `M` and every level set `{d_1 = c}` contain
fields of arbitrarily large critical and supercritical norms; `M` is
parametrised by all solenoidal fields through `v -> v/|v|^{1/2}` (HF22-A) and
is invariant under `D_lambda`, so it is unbounded in every norm that blows up.
There is no instantaneous lower bound, and the only dynamical one is
Lemma 1.1, which is "infinitely often", never "eventually". HF26-C's departure
theorem is a *lower* bound only at a point where `d_1 = 0` and only of order
`t^2` (`eq:NSgaplower`), so it produces departure, never non-return; its own
corollary (no universal source-free gap inequality with `L^1_loc` coefficient)
is evidence *against* any Gronwall-type control of `d_1` in either direction.

*Verdict.* Dead; the negative answer is exactly the content of Proposition E.

### 3.5 Strategy 5 — refute (T) (not available, as predicted by the audit)

A counterexample to (T) is by Theorem A a finite-time singularity whose
critical shape oscillates for ever across the level `nu/C_sharp`. Constructing
one requires constructing a singularity. This confirms the R1 audit's §5.1(2):
(C) is of the same *falsifiability* class as (H-mod), while of a strictly
weaker *logical* class. Proposition H is the closest available substitute, and
it is a statement about the ledger, not about the equation.

---

## 4. Refuting the lane's own best attempt

The best positive output is Theorem D ("`d_1` convergent implies (C)"), with
Corollary D'. Four attacks:

0. **Is Theorem D's hypothesis nonempty?** Its naive reading is empty, and
   catching that is the main correction this lane made to itself: see
   Remark D.1 — `L^3`-shape convergence forces a bounded critical norm and
   hence `T_* = infinity`. What survives is the hypothesis on `d_1` itself,
   which is not empty (it holds, for instance, whenever the normalized shape
   and the amplitude both converge), and Corollary D', whose case (b) is the
   honest statement of what is left undecided.
1. **Does Theorem D extend to convergence along a subsequence?** No, and the
   failure is instructive. `d_1(t_n) -> d_infinity` along one sequence
   `t_n -> T_*` gives nothing: Theorem A's failure mode has `d_1` converging along two different
   subsequences to `0.4` and `0.8` (in the units of Proposition H). The proof
   of Theorem D uses the full limit at the single point where it converts a
   pointwise limit into a *final interval*, and no subsequential hypothesis
   does that.
2. **Can Theorem B's trap be raised to cover the corridor?** No. The trap level
   `Q_nu` is *exactly* the level at which growth becomes possible: `Q > Q_nu`
   is necessary for `C_sharp d_1 > nu` by (A3), and (1.1) permits growth only
   there. Raising the trap therefore requires improving `c_*` in
   `d_1 <= c_* ||u||_3` below `(1+C_P)`, which changes the constant in (2.3)
   but never the *structure*: for any `c_*`, the trap sits at
   `nu/(c_* C_sharp)` in `d_1`-units, and the corridor is *above* it whenever
   `(1-2eps)nu/C_sharp > nu/(c_* C_sharp)`, i.e. for all `eps` once
   `c_* > 1/(1-2eps)`. The corridor and the trap do not interact.
3. **Is Theorem C(ii) sharp enough to be pushed?** The deficit (3.1) is not a
   loose estimate: `nu kappa_0 M_Q = 4/C_9^3` is an identity, and both factors
   are audited. Improving it needs either a better `L^9`-coercivity constant
   `a_0` or a better spacetime budget than `int ||u||_3^4 <= 3C_S^2E_0^2/(2nu)`;
   the latter is the energy identity and cannot improve.

Theorem D therefore survives exactly as stated, and no more.

---

## 5. The sharpest obstruction

Stated as an inequality, and as a missing implication.

> **OBSTRUCTION (HF29).** Let `T_* < infinity` and suppose (C) fails. By
> Theorem A there are infinitely many disjoint traversals `I_j = [alpha_j,
> beta_j]`, `beta_j -> T_*`, each with `|Delta d_1| = eps nu/C_sharp`. Every
> route in the audited record charges these against an input-only budget and
> arrives at exactly one inequality,
>
> ```
>    sum_j ( ||grad u(alpha_j)||_2 + ||grad u(beta_j)||_2 )^{-3}
>          <=  ( C_sharp kappa_mod C_S^{1/2} / (eps nu) )^4 M(nu,E_0,H) ,   (5.1)
> ```
>
> and (T) follows from (5.1) **if and only if** that series is forced to
> diverge. The missing implication is therefore, exactly:
>
> ```
>   (MI)   T_* < infinity  ==>  sum_j G_j^{-3} = infinity  for every sequence
>          of disjoint traversal intervals with beta_j -> T_* ,
> ```
>
> equivalently an input-only `Gamma` with `G_j <= Gamma` — which is (C) — or any
> input-only growth restriction on `||grad u||_2` along a sequence of times
> tending to `T_*`, e.g. `G_j <= C j^{1/3}`.
>
> **Why (MI) is not a technical gap.** (i) No instantaneous inequality can
> supply it (Proposition E: `d_1` and the enstrophy are independent at a point,
> since `d_1` is invariant and the enstrophy is not, under `D_lambda`).
> (ii) No change of currency can remove the supercritical factor from (5.1)
> (Theorem F: the only input-only trajectory modulus lives in `Hdot^{-1}`, and
> `d_1` is discontinuous there on `L^3`-balls, again by `D_lambda`).
> (iii) The differential-inequality route cannot reach it: the good-set
> contraction budget of the whole trajectory is at most `16/(3C_9^3)` descents
> to the trap (3.1), and the bad set undoes descents at unbounded rate because
> `D_Q` admits no upper bound in `Q` by scaling. (iv) The whole scalar ledger
> (S1)–(S9) is consistent with the negation of (MI) (Proposition H).
>
> **One inequality would close it, and it is scaling-admissible:**
>
> ```
>    | d_1(t') - d_1(t) |  <=  C ||grad u_0||_2^{3/4} mu([t,t'])^{1/4}      (5.2)
> ```
>
> for all `0 <= t <= t' < min(H,T_*)`. (5.2) has the correct two-parameter
> weights `(a,lambda^{-1})` on both sides, is **not** refuted by the
> concentration family that refutes every input-only modulus without a
> supercritical factor, implies (MI) and hence (C) by Proposition G, and does
> **not** by itself imply the Clay conclusion (by R1, (C) is strictly weaker).
> No step of the audited derivation produces (5.2): HF24-A's proof produces the
> endpoint enstrophy at exactly one step,
> `||h||_2^2 <= ||h||_{Hdot^1}||h||_{Hdot^{-1}}`, and replacing
> `||h||_{Hdot^1}` by an input-only quantity there is equivalent to bounding
> the enstrophy, i.e. to the conclusion. Whether (5.2) is true is open; §6
> records what it would cost.

---

## 6. FRONTIER RECORD

```text
TERMINAL CLAIM (unchanged, not addressed here): NS-R3.

TARGET OF THIS LANE: (T) — every finite-time singularity of the classical
  branch has C_sharp d_1 > (1-eps)nu on a final interval — equivalently (C)
  unconditionally, by the audited Proposition R1.

RESULT: NOT PROVED, NOT REFUTED. Proved unconditionally here (all UNAUDITED):
  A  failure of (C) <=> liminf C_sharp d_1 <= (1-eps)nu, and then C_sharp d_1
     oscillates for ever across [(1-eps)nu, nu] with infinitely many complete
     traversals accumulating at T_*; limsup C_sharp d_1 >= nu always.
  A' (C) holds for some admissible eps <=> liminf C_sharp d_1 >= nu/2
     (borderline case aside): the residue is a factor of two plus the upgrade
     from "infinitely often" to "eventually".
  B  {Q <= Q_nu} is forward invariant; at a finite-time singularity
     ||u(t)||_3 > 2nu/(3C_9C_S(1+C_P)) for every t < T_*.
  C  D_Q >= kappa_0 Q^{7/3}; on {C_sharp d_1 <= (1-delta)nu} the quotient obeys
     Q(t) <= ((4/3)delta nu kappa_0 (t-a))^{-3/4}, independently of Q(a); every
     interval of length > L_delta contains a time with C_sharp d_1 > (1-delta)nu.
  D  If d_1(t) has a limit as t -> T_* then (C) holds, and that limit is
     >= nu/C_sharp. L^3-shape convergence without amplitude is vacuous at a
     singularity (that vacuity is ESS); in the normalized class (Cor. D') (C)
     holds whenever the limiting normalized shape is off M and ||u||_3 has a
     matching lower bound, and the undetermined case is exactly a normalized
     shape approaching M at the rate 1/||u||_3.
  E  For every c,N,Lambda there is a smooth compact solenoidal v with
     d_1(v) = c, ||v||_3 >= N, ||grad v||_2 >= Lambda: no instantaneous route.
  F  No currency admits a modulus for d_1 without a supercritical endpoint
     factor; the only input-only trajectory modulus is in Hdot^{-1}, where d_1
     is discontinuous on L^3-balls.
  G  The crossing ledger is exactly sum_j G_j^{-3} <= input, and (T) is exactly
     the divergence of that series.
  H  The whole audited scalar ledger (S1)-(S9) is consistent with the failure
     of (T): an explicit model is given and checked.

FIRST GAP (this lane): the missing implication (MI) of §5 — at a finite-time
  singularity, the enstrophies at the endpoints of the traversal intervals
  cannot grow fast enough to make sum_j G_j^{-3} converge. Equivalently, the
  scaling-admissible modulus (5.2) with the INITIAL enstrophy in place of the
  endpoint enstrophy.

SURVIVING CONDITIONAL SUFFIX: everything downstream of (C) in the audited
  record is untouched and remains available under (C): HF24-A Corollary 4.3'
  (bad set of (G) covered by 1 + 8 Theta Gamma^3 intervals) and the reduction
  of (G) to its bad-set part with HF22-C Theorem B. Additionally, and
  unconditionally, the class of blow-ups for which (C) must be assumed has
  shrunk: by Theorem D it excludes every blow-up along which d_1 converges, so
  any counterexample to (C) has a permanently oscillating critical shape whose
  relative distance to M oscillates about nu/(C_sharp ||u||_3).

NON-CLAIMS. (T) is not proved. (C) is not proved and not refuted. No blow-up,
  no counterexample, no regularity criterion, no continuation theorem, and no
  bound on sup_t Q is claimed. Proposition H is non-derivability from an
  enumerated list, NOT falsity of (T) — the species of overclaim the HF22
  audits struck, and it is avoided deliberately. Theorem B is the quotient-route
  form of a known critical small-data theorem, already recorded as recovered in
  audited HF18-A; only its explicit threshold and forward-invariance form are
  written here, and neither is claimed as new. Theorem C(i) is elementary
  interpolation from two audited inequalities. The positioning of Theorem D
  against the uniqueness-of-blow-up-profile literature is NOT source-checked and
  is not load-bearing. HIGH-PRESSURE, HIGH-STRAIN, hyp:critical and NS-R3 are
  exactly where they stood. Nothing in this file is audited.

FALSIFIER for this note: an inequality whose two sides have different scaling
  weights; any use of sup_t Q, sup_t ||u||_3 or sup_t ||grad u||_2 inside a
  constant; any differentiation of the L^3 minimizer; any claim that the scalar
  model is a solution.

NEXT DISTINCT ACTION (one, and it is not a repetition of any HF19-HF28 lane):
  decide (5.2). Concretely: is there an interpolation route from
  ||h||_{Hdot^{-1}} <= mu to ||h||_3 that spends only the INITIAL enstrophy?
  The audited proof spends ||h||_{Hdot^1} <= G once, at
  ||h||_2^2 <= ||h||_{Hdot^1}||h||_{Hdot^{-1}}. Two concrete sub-questions,
  both new: (a) does the weighted stability Lemma 3.1 of HF24-A admit a form in
  which the weight ||w||_6 + ||w'||_6 is replaced by a spacetime average, which
  IS input-controlled by cor:quotient-budgets, rather than by its endpoint
  values? (b) is there a second, independent bound for |d_1(t')-d_1(t)| through
  the DEFECT sigma (cor:quotient-defect: d_k q_j = R_jR_k sigma, ||sigma||_2
  input-bounded in L^2_t by cor:quotient-budgets) that bypasses the velocity
  increment entirely? Both are questions about the currency, which Theorem F
  identifies as the single load-bearing choice. A negative answer to both,
  proved, would close the corridor route for good and should be recorded as
  such; that would be as valuable as (T).
```

---

## 7. Numerical and symbolic checks (bounded evidence, not proof)

All checks were run in this session; no numeric is load-bearing for any proof
above. Scripts are session scratch (not committed).

**Symbolic identities** (sympy), all verified exactly:

```
   theta = 4/7 solves 1/3 = theta/2 + (1-theta)/9                  [Theorem C(i)]
   kappa_0 = 3^{7/3}/(a_0 C_9^3 E_0^2) = 8.3^{1/3}/(C_S^2C_9^3E_0^2)
   Q_nu = nu^3/(3C_sharp^3(1+C_P)^3) = 8nu^3/(81C_9^3C_S^3(1+C_P)^3)
   (3Q_nu)^{1/3} = 2nu/(3C_9C_S(1+C_P))                              [Theorem B]
   L_delta = (3/4)(delta nu kappa_0)^{-1}Q_nu^{-4/3}
           = 729C_S^6C_9^7(1+C_P)^4E_0^2/(512 delta nu^5)          [Theorem C(iii)]
   nu kappa_0 M_Q = 4/C_9^3   and   M_Q/Q_nu^{4/3}
           = 243C_9^4C_S^6(1+C_P)^4E_0^2/(32 nu^5)                       [(3.1)]
   (4/3)delta nu kappa_0 . (M_Q/Q_nu^{4/3}) . Q_nu^{4/3} = 16delta/(3C_9^3)
```

**The model of Proposition H**, 40 cycles x 4000 steps, constants
`nu = C_S = C_9 = C_P = 1`, `E_0 = 10`, `H = 1`, `eps = 1/4`:

```
  (S1) Q' <= (C# d1 - nu)D_Q          PASS  max relative violation 6.9e-17
  (S3) D_Q >= kappa_0 Q^{7/3}         PASS
  (S2) d1 <= (1+C_P)(3Q)^{1/3}        PASS  min slack 4.31
  (S9) Q > Q_nu                       PASS  min Q = 5.575  vs  Q_nu = 0.01235
  (S5) int Q^{4/3} <= M_Q             PASS  5.61 <= 34.67
  (S5) int ||grad u||_2^2 <= E_0/2nu  PASS  2.43 <= 5
  (S5) int ||u||_3^4 <= 3C_S^2E_0^2/2nu PASS 24.25 <= 150
       int d_1^4                            0.0453  (bound 24C_S^2E_0^2/nu = 2400)
  (S6) mu([0,1)) <= M(nu,E_0,H)       PASS  3.97 <= 8.18
  (S7) HF24-A modulus on all 80 traversals PASS worst LHS/RHS ratio 0.226
  (S8) max Q = 1.23e7, max||u||_3 = 333, G_end = 3.5e4, int D_Q = 6.2e7
       corridor times and {C# d1 > nu} times both accumulate at T_* = 1
```

The model is a triple of scalar functions, not a solution; see the scope
paragraph of Proposition H.

---

## 8. Sources

All mathematical inputs are repository objects, listed in §1 with their exact
labels. External literature was neither retrieved nor cited in this lane, and
the one comparison to the blow-up-profile literature (§2, Theorem D reading) is
explicitly flagged as unverified and non-load-bearing. No third-party PDF was
retained and no person was contacted.
