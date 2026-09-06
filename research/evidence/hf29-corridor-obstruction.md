# HF29: adversarial attack on the corridor hypothesis (C)

**NOTHING IN THIS FILE IS AUDITED.** It is a single DISCOVER lane running the
adversarial side against hypothesis (C) of `hf24-modulus-of-continuity.md` as
characterised by Proposition R1 of `hf24-review-modulus-of-continuity.md`. No
independent auditor has reconstructed any statement below. Nothing is promoted;
`PLAN.md`, `docs/`, the manuscript, the graph and every other evidence file are
untouched; nothing is committed or pushed. Every result here is a claim of this
lane only, and several of them are explicitly *non-derivability* claims, not
falsity claims — the distinction that three of the four HF22 audits had to
enforce, and it is enforced here at the point of statement.

**Frozen inputs.**

```
research HEAD  9c5def29be04e0d0e723677feae0437a0ea61300   (branch main, clean)
paper HEAD     065a962d6c6672dcf4bed2db17eb004081014a68
hf24-modulus-of-continuity.md          sha256 8b929a49d83cb1853987fb81b2a4cb7e8865ac89f6da572b4afb36935b8a5c47
hf24-review-modulus-of-continuity.md   sha256 5671db30e1f8b35b9894d4fe6321ccbc53954895cff108f28fa7612bee3358a0
hf26-review-countermodel-crossings.md  sha256 52ae04d15e6eb8a88abf315355a451a7ad9c5206103e64a7d9ac5512638b9654
hf27-review-energy-concentration.md    sha256 973c85849fcf05051d1678bd5dcc907949ddd1aa0e92c990798b7d3a2116f1ad
```

**Audited record used as premises**, each strictly inside its audited scope:
`prop:localtheory`(iii),(v), `prop:energy`, `prop:scaling`(iii)
\eqref{eq:L4L3}, `thm:continuation`, `lem:quotient-scaling`,
`lem:quotient-coercive` \eqref{eq:cp-coercive}, `lem:quotient-stability`
\eqref{eq:cp-strong} \eqref{eq:cp-continuity}, \eqref{eq:cp-F-monotone},
\eqref{eq:cp-F-taylor}, `lem:quotient-minimizer`(c),
`prop:quotient-divcurl` \eqref{eq:qdc-interp} \eqref{eq:qdc-sobolev-field},
`cor:quotient-defect`, `cor:quotient-budgets`, `def:qe-dissipation`,
`lem:qe-weighted-dissipation` \eqref{eq:qe-weighted-coercive},
`prop:quotient-evolution`; HF18-A Theorem 2 (`D_Q = D_3(w)`); HF21-B
Proposition 3.1 (`|K| <= C_sharp d_1 D_3(w)`, `C_sharp = (3/2)C_9 S`) and
Lemma 4.3(3); HF24-A Lemma 3.2, Theorem 3.3, Theorem 4.1 (unaudited, used only
as *additional* constraints against the countermodel, never as support);
HF24-B audit Proposition R1; HF26 audit §2 Q7 and §2 Q8; HF27 audit §3.

---

## 0. MODE / RESULT

**MODE: DISCOVER, adversarial.** **RESULT: (C) is NOT refuted, and cannot be
refuted short of constructing a finite-time singularity. (C) is, however,
NOT DERIVABLE from the audited record**, certified by an explicit scalar
countermodel that satisfies every audited scalar relation including the two
newest tools (HF24-A Theorems 3.3 and 4.1) and the HF18-A `L^9` coercivity.
Three further findings, in descending order of sharpness:

1. **The instantaneous form of (C) is FALSE** (Proposition A, §7). At fixed
   viscosity, fixed kinetic energy, fixed `eps`, and *at time zero on actual
   classical trajectories*, the corridor condition `C_sharp d_1 in [(1-2eps)nu,
   (1-eps)nu]` carries **no** upper bound whatsoever on `||grad u||_2`. This
   answers, negatively, the exact question HF24-A's own NEXT DISTINCT ACTION 1
   posed ("whether the corridor condition carries **any** information about
   `||grad u(t)||_2`"). Consequence: `Gamma` in (C) can never be made a function
   of `(nu, E_0, H, eps)`, so the crossing count `1 + 8 Theta Gamma^3` of
   Corollary 4.3 is **not effectivisable** in the input data.
2. **The `eps`-quantifier reading is settled and the parameter is a red
   herring** (§8). In the blow-up branch, `(C)_eps` is equivalent to
   `liminf_{t->T_*} C_sharp d_1(t) >= (1-eps)nu`; the family is monotone
   increasing in `eps`; "for all `eps in (0,1/2)`" is exactly
   `liminf >= nu`, and "for some `eps`" is exactly `liminf > nu/2`. The record
   forces only `limsup >= nu`. So the whole `eps`-family is squeezed between one
   proved limsup and one unproved liminf at the *same* level, and the entire
   content of (C), for every `eps`, is the upgrade of that limsup to a liminf
   within a factor two. `eps` cannot be chosen adversarially to defeat (C), and
   cannot be chosen favourably to trivialise it.
3. **Two of the programme's own audited countermodels sit on the sibling
   lane's side, not on mine** (§4, §5). HF26's concentrating Leray curve is
   *forced* to satisfy `C_sharp d_1 >= nu` at every time (HF26 audit §2 Q7,
   item 1), hence lies strictly above the upper corridor wall for every
   `eps in (0,1/2)`, hence **satisfies (C)** by alternative (ii). The
   HF24/HF26 smooth crossing function `d_* + eps e^{-1/(1-t)^2}sin(1/(1-t))`
   cannot be adapted at all: a *convergent* `d_1` whose limit lies in the
   corridor forces `T_* = infinity` by the record's own Lyapunov step.

The natural mechanism the brief names — discretely self-similar blow-up — is
**self-excluded by the programme's own `thm:continuation`** (§3), and the reason
is instructive: exact log-periodicity of a scale-invariant quantity forces
*every* scale-invariant quantity to be log-periodic, `||u(t)||_3` included, and
a log-periodic critical norm is bounded. Only the *inexact* version survives,
and it is exactly what the countermodel of §6 encodes.

---

## 1. THE EXACT STATEMENT ATTACKED

Fix `nu > 0`, a divergence-free Schwartz `u_0`, `0 < H < infinity`, and
`eps in (0,1/2)`. Let `(u,p)` be the maximal classical branch on `[0,T_*)`,
`Q(t) = Q(u(t))`, `w(t) = w(u(t))`, `q(t) = w(t) - u(t)`,
`d_1(t) = ||q(t)||_3`. Write

```
   Corr_eps := { t < min{H,T_*} : C_sharp d_1(t) in [(1-2eps)nu, (1-eps)nu] } .
```

> **(C)_eps.** There is an input-only `Gamma = Gamma(nu,u_0,H,eps) < infinity`
> with `||grad u(t)||_2 <= Gamma` for every `t in Corr_eps`.

**Proposition R1** (`hf24-review-modulus-of-continuity.md` §5, quoted, not
re-proved here; I reconstructed both directions and found no error):
`(C)_eps` holds **iff** (i) `H < T_*`, or (ii) `T_* <= H` and there is
`t_0 < T_*` with `C_sharp d_1(t) > (1-eps)nu` for every `t in (t_0,T_*)`.

The sibling lane is attempting to prove `(C)_eps` unconditionally. By R1 that is
the assertion: *no finite-time singularity re-enters the corridor at times
accumulating at `T_*`*. This lane attacks that assertion.

**What "input-only" means here.** The audit records it as *finite* (a trajectory
is a function of the data, so any finite trajectory quantity is trivially a
function of the data). Under that reading, and using
`prop:localtheory`(v) with `prop:energy` (`||grad u(t)||_2 -> infinity` as
`t -> T_*` when `T_* < infinity`), one has immediately:

> **Observation 1.1 (this lane).** `(C)_eps` is equivalent to
> "`Corr_eps` is relatively compact in `[0,T_*)`". In particular `Gamma` may
> always be taken as `max_{[0,t_0]}||grad u||_2` for some `t_0 < T_*`, so **(C)
> is not an estimate**: it contains no quantitative information beyond that
> topological statement, and every quantity derived from it inherits a `Gamma`
> for which the record supplies no bound.

This is not a defect the lane hid — R1's sufficiency proof constructs `Gamma`
exactly this way — but it is not stated as a limitation anywhere, and it is the
reason finding 1 of §0 matters: the count `1 + 8 Theta Gamma^3` is finite and
never computable.

---

## 2. PRELIMINARIES DERIVED FROM THE RECORD

### 2.1 `d_1` is scale-invariant (verified)

`lem:quotient-scaling` gives `w(D_lambda u) = D_lambda w(u)` with
`D_lambda u(x) = lambda u(lambda x)`, and `D_lambda` an `L^3` isometry
(re-verified symbolically). Hence
`q(D_lambda u) = D_lambda q(u)` and

```
   d_1(D_lambda u) = d_1(u) ,        d_1(alpha u) = |alpha| d_1(u) .
```

So `d_1` has the same scaling signature as `||u||_3` and as `nu`: weight `0`
under the critical dilation, weight `1` under amplitude. The corridor
`C_sharp d_1 in [(1-2eps)nu, (1-eps)nu]` is therefore a **scaling-invariant**
condition. **The band's position is not an artifact of a normalisation**: it is
the unique scaling-consistent placement, and it is placed at the one level the
dynamics selects, namely the level `nu/C_sharp` at which the Lyapunov step of
`prop:quotient-conditional` turns off.

The band's *height* does depend on `C_sharp`, and in a direction worth
recording: `(C)_eps` asks for `d_1 > (1-eps)nu/C_sharp` near `T_*`, so a
**sharper (smaller) `C_sharp` makes (C) strictly harder**, while the same
sharper `C_sharp` widens the Lyapunov range the programme wants. Improving
HF21-B Proposition 3.1's constant therefore helps one half of the route and
hurts the other.

### 2.2 The one asymptotic fact the record does force

> **Lemma 2.1 (this lane; two lines from the record).** If `T_* < infinity`
> then `limsup_{t->T_*} C_sharp d_1(t) >= nu`.

*Proof.* Suppose not: there are `t_0 < T_*` and `delta > 0` with
`C_sharp d_1 <= nu - delta` on `(t_0,T_*)`. By `prop:quotient-evolution` with
HF18-A Theorem 2 and HF21-B Proposition 3.1,
`Q' = K - nu D_Q <= (C_sharp d_1 - nu)D_Q <= -delta D_Q <= 0` on `(t_0,T_*)`, so
`Q <= Q(t_0)` there; by \eqref{eq:cp-coercive},
`||u(t)||_3 <= (3C_P^3 Q(t_0))^{1/3}` on `(t_0,T_*)`, and `||u||_3` is
continuous on the compact `[0,t_0]`. So `sup_{t<T_*}||u(t)||_3 < infinity`,
and `thm:continuation` gives `T_* = infinity`. `[]`

This is the *only* lower bound on `d_1` near a singularity in the record, and it
is a **limsup**. Everything below turns on the gap between it and the **liminf**
that (C) requires.

### 2.3 A strong-convexity link between `d_1` and the quotient gap (new here)

> **Lemma 2.2 (this lane).** For every `u in L^3`, with `w = w(u)`,
> `q = w - u`, `d_1 = ||q||_3`,
>
> ```
>    (1/6) d_1^3  <=  (1/3)||u||_3^3 - Q(u)  <=  ||u||_3^2 d_1 ,
>    and          d_1 <= sqrt(2) ||u||_3 .
> ```

*Proof.* Put `phi(theta) = F(w - theta q)`, `F(v) = (1/3)||v||_3^3`, so
`phi(0) = Q(u)`, `phi(1) = F(u)`. By \eqref{eq:cp-F-taylor}, `F` is
Gateaux-differentiable with `phi'(theta) = <j(w - theta q), -q>`, and
`phi'(0) = <A, -q> = 0` by `lem:quotient-minimizer`(c) since `q in G_3`. By
\eqref{eq:cp-F-monotone} applied to `v = w - theta q`, `v' = w`,
`<j(w-theta q) - j(w), -theta q> >= (1/2)theta^3 d_1^3`, i.e.
`phi'(theta) - phi'(0) >= (1/2)theta^2 d_1^3`; integrating over `[0,1]` gives
the left inequality. For the right, convexity gives
`F(u) - Q <= <j(u), u - w> = <j(u), -q> <= ||j(u)||_{3/2} d_1 = ||u||_3^2 d_1`.
Combining the two, `(1/6)d_1^3 <= ||u||_3^2 d_1`, i.e. `d_1 <= sqrt6 ||u||_3`;
the sharper `sqrt2` follows from \eqref{eq:cp-F-monotone} with `v = u`,
`v' = w`: `(1/2)d_1^3 <= <j(u) - A, -q> = <j(u), -q> <= ||u||_3^2 d_1`. `[]`

Lemma 2.2 is used below as a *constraint on the adversary*, not as support: it
is the tightest link the record supplies between `d_1` and the pair
`(||u||_3, Q)`, and any countermodel must respect it. I did not locate it in the
repository record; it is elementary and no novelty is claimed.

---

## 3. CONSTRUCTION 1 — EXACT (DISCRETELY) SELF-SIMILAR BLOW-UP. **FAILED, and the failure is a theorem.**

**Target.** Realise a trajectory whose `d_1` has a nonconstant log-periodic
profile crossing the band, so that `Corr` accumulates at `T_*`.

**Set-up.** A backward DSS solution with factor `L > 1` about `(0,T_*)` is
`u(x,t) = mu^{-1} U(x/mu, s)`, `mu = (T_*-t)^{1/2}`, `s = -log(T_*-t)`, with
`U(., s+S) = U(., s)`, `S = 2 log L`; `L = 1` is the exactly self-similar
(Leray) case. In the notation of §2.1, `u(.,t) = D_{1/mu} U(., s)`.

**What scale invariance gives.** By `lem:quotient-scaling`,

```
   d_1(t) = ||q(D_{1/mu}U(.,s))||_3 = ||D_{1/mu} q(U(.,s))||_3 = ||q(U(.,s))||_3 =: f(s),
```

so `f` is `S`-periodic: a nonconstant `f` whose range meets the band produces
band times `s_k = s_0 + kS`, i.e. `t_k = T_* - e^{-s_k} -> T_*`. **The
mechanism works exactly as the brief predicts.** But the *same* computation
applies to `||u(.,t)||_3 = ||U(.,s)||_3` and to `Q(t) = Q(U(.,s))`, because
both are scale-invariant:

> **Proposition 3.1 (this lane; self-exclusion).** Along an exact DSS (or
> exactly self-similar) blow-up whose profile lies in `L^3` uniformly in `s`,
> every scale-invariant quantity is `S`-periodic in `s`; in particular
> `sup_{t<T_*}||u(t)||_3 = max_s ||U(.,s)||_3 < infinity`, contradicting
> `thm:continuation`. Hence the record **excludes** exact DSS blow-up with
> profile in `L^3`, and with it this construction.

This is the programme's own continuation theorem doing the work; it reproves,
by a different route, the `L^3` half of Nečas–Růžička–Šverák (1996) recorded in
`literature/blowup-barriers.md` §3, and extends it to every `L` at once, which
is more than Chae–Wolf give (they remove DSS singularities only for `L`
sufficiently near `1`). No novelty is claimed: the argument is the observation
that a periodic function of `s` is bounded.

**Two by-products that are not thrown away.**

> **Corollary 3.2.** If a (D)SS-type blow-up existed at all, its log-periodic
> profile would be forced to satisfy `C_sharp max_s f(s) >= nu`. Indeed if
> `C_sharp max_s f < nu` then `Q' <= (C_sharp f - nu)D_Q <= 0` on all of
> `[0,T_*)`, so `||u||_3` is bounded and `T_* = infinity`.

> **Corollary 3.3 (the exactly self-similar case satisfies (C)).** For `L = 1`,
> `f` is constant, so `C_sharp f >= nu > (1-eps)nu` for every `eps in (0,1/2)`:
> `Corr_eps` is empty and alternative (ii) of R1 holds. **A Leray self-similar
> singularity would confirm (C), not refute it.**

**What survives the failure.** The obstruction is to *exactness*, not to the
mechanism. What Proposition 3.1 forbids is `||u(t)||_3` being log-periodic; it
forbids nothing about `d_1` being log-periodic while `||u(t)||_3` grows. That is
the Type-II picture — the profile drifts in amplitude while its *shape*
oscillates log-periodically — and `literature/blowup-barriers.md` §3 records
explicitly that NRS/Tsai/Chae–Wolf "do not exclude type-II, oscillatory,
multi-scale, or non-self-similar singularity formation". Nothing in the audited
record excludes it either. This is the object §6 encodes at the scalar level.

*(Literature scope: the session's web-search budget was exhausted before this
lane ran, so the DSS/Type-II literature check is limited to the repository's own
dossier `literature/blowup-barriers.md` §3 and the primary sources it names,
plus HF26/HF27's audited prior-art findings. No new external source was
consulted, and no claim about the current state of the DSS literature beyond
those is made.)*

---

## 4. CONSTRUCTION 2 — ADAPT HF26's CONCENTRATING COUNTERMODEL. **FAILED: it satisfies (C).**

HF26's `thm:curve` produces a concentrating comparison curve with `d_1`
**constant**; `hf26-review-countermodel-crossings.md` §2 Q7 identifies it as
exactly the backward self-similar (Leray) ansatz and, in item 1 of "What is NOT
excluded", proves from `K = nu D` and `|K| <= C_sharp ||q||_3 D` that the curve
is *forced* to satisfy

```
   C_sharp ||q(t)||_3 >= nu   for every t .
```

Therefore `C_sharp d_1(t) >= nu > (1-eps)nu` for every `eps in (0,1/2)`:
`Corr_eps = empty`, alternative (ii) holds vacuously, and **(C) is true on
HF26's curve.** The same holds for HF27's `thm:concentration` family, which the
HF27 audit §3.1 identifies as literally the same Leray ansatz.

**Can the constant be lowered into the band?** No, without destroying the
object: the audit's inequality is an identity-plus-bound consequence of the
curve's own tuning `K = nu D`, and lowering `C_sharp d_1` below `nu` would make
`K < nu D`, i.e. `Q' < 0`, i.e. exactly the Lyapunov branch. **Both audited
countermodel families of this programme are pinned on or above the upper
corridor wall.** They are evidence *for* alternative (ii), not against it, and
this lane records that as a genuine strengthening of the sibling lane's
position, obtained while trying to do the opposite.

Scope, taken from those audits and not weakened here: neither family solves
Navier–Stokes (`R != 0` by NRS/Tsai), so neither is a trajectory, and neither
says anything about whether an actual singularity behaves this way.

---

## 5. CONSTRUCTION 3 — ADAPT THE SMOOTH LEVEL-CROSSING FUNCTION. **FAILED, for a reason that constrains every future attempt.**

`hf26-review-countermodel-crossings.md` §2 Q8 verifies the scalar function

```
   d(t) = d_* + eps e^{-1/(1-t)^2} sin(1/(1-t))   on [0,1),
```

`C^infinity` up to `t = 1`, Lipschitz with constant `0.715 eps`, crossing the
level `d_*` at `t_k = 1 - 1/(k pi) -> 1`. It is the natural candidate for a
`d_1` that re-enters the corridor infinitely often near a finite time.

**It cannot be used.** Its oscillation amplitude tends to `0`, so
`d(t) -> d_*`. Two cases:

* `C_sharp d_*` in the closed band. Then `C_sharp d(t) <= (1-eps)nu + o(1)`, so
  on a final interval `C_sharp d_1 <= nu - (eps nu/2)`, and Lemma 2.1's argument
  gives `T_* = infinity`. No blow-up, so (C) holds by branch (i).
* `C_sharp d_*` outside the band. Then the band is entered only finitely often,
  `Corr` is bounded away from `T_*`, and (C) holds by (ii) or by (i).

> **Proposition 5.1 (this lane).** If `T_* < infinity` and
> `lim_{t->T_*} C_sharp d_1(t)` exists, then `(C)_eps` holds for every
> `eps in (0,1/2)`. Equivalently: **any counterexample to (C) must have
> `d_1` oscillating with amplitude bounded below near `T_*`**, spanning from
> at most `(1-eps)nu/C_sharp` up to at least `nu/C_sharp` infinitely often.

*Proof.* Let `l = lim C_sharp d_1`. By Lemma 2.1, `l >= nu` if the limit exists
(a convergent sequence has `limsup = lim`). Then `l >= nu > (1-eps)nu`, so (ii)
holds. `[]`

That is a sharp structural constraint, and it is *exactly* the log-periodic
shape of §3: sustained, non-decaying oscillation of a scale-invariant quantity,
which is the signature of discrete self-similarity. So the three failed
constructions converge on one surviving shape.

---

## 6. CONSTRUCTION 4 — A SCALAR COUNTERMODEL. **SUCCEEDS as a non-derivability certificate.**

### 6.1 The constraint list

I enumerated every relation between the scalars
`(E, Y, ||u||_3, ||u||_4, Q, D_Q, K, d_1)` that the audited record supplies
along the maximal classical branch, plus the two unaudited HF24-A theorems
(included so that the countermodel is not cheap):

| tag | constraint | source |
|---|---|---|
| S1 | `E' = -2 nu Y`, `E > 0`, `int_0^{T_*} Y dt <= E_0/(2nu)` | `prop:energy` |
| S2 | `Y(t) -> +infinity` as `t -> T_*` (genuine limit) | `prop:localtheory`(v) + `prop:energy` |
| S3 | `T_* < infinity  =>  sup_{t<T_*}||u||_3 = infinity` | `thm:continuation` |
| S4 | `Q' + nu D_Q = K`, `Q in C^1` | `prop:quotient-evolution` + HF18-A Thm 2 |
| S5 | `D_Q >= 0`, `|K| <= C_sharp d_1 D_Q` | `def:qe-dissipation`, HF21-B Prop. 3.1 |
| S6 | `||u||_3^3/(3C_P^3) <= Q <= ||u||_3^3/3` | \eqref{eq:cp-coercive} |
| S7 | `(1/6)d_1^3 <= (1/3)||u||_3^3 - Q <= ||u||_3^2 d_1` | Lemma 2.2 |
| S8 | `d_1 <= sqrt2 ||u||_3` | Lemma 2.2 |
| S9 | `||u||_3 <= C_S^{1/2} E^{1/4} Y^{1/4}`, `||u||_4^2 <= C_S^{3/2}E^{1/4}Y^{3/4}` | \eqref{eq:qdc-interp}, \eqref{eq:qdc-sobolev-field} |
| S10 | `int_0^tau ||u||_3^4 dt <= C_S^2 E_0^2/(2nu)` | `prop:scaling`(iii) \eqref{eq:L4L3} |
| S11 | `D_Q >= (8/(9C_S^2 C_9^3)) ||u||_3^7 / E^2` | \eqref{eq:qe-weighted-coercive} + `L^2`–`L^9` interpolation |
| S12 | `\|d_1(t')-d_1(t)\| <= kappa_0 C_S^{1/2} G^{3/4} mu([t,t'])^{1/4}` | HF24-A Thm 3.3 (**unaudited**) |
| S13 | `sum_i G_i^{-3} <= Theta` over disjoint traversals | HF24-A Thm 4.1 (**unaudited**) |
| S14 | `\|{t<tau : C_sharp d_1 > (1-2eps)nu}\| <= 24C_S^2C_sharp^4E_0^2/((1-2eps)^4 nu^5)` | HF21-B Lemma 4.3(3) |

`mu` has density `g = nu Y^{1/2} + ||u||_4^2` and total mass `M(nu,E_0,H)`
(HF24-A Lemma 3.2); `cor:quotient-budgets` (`int||grad w||_2^2 <= 5E_0/(8nu)`,
`int||sigma||_2^2 <= E_0/(8nu)`) is implied pointwise by S1 and imposes nothing
extra on this list. The record supplies **no** upper bound on `D_Q`, **no**
input-only bound on `int D_Q dt`, and — this is the load-bearing gap —
**no lower bound on `d_1` in terms of any quantity that blows up**. The last is
not an oversight: §7 shows there cannot be one.

### 6.2 The countermodel

Fix any admissible `(nu, C_S, C_P, C_9, C_sharp, E_0)` and any
`eps in (0,1/2)`. Put `D = nu/C_sharp`, `delta = 0.15`, `gamma = 0.8`,
`kappa = 0.3`, `S = 1`,

```
   f_min = D max{0.02, (1-2eps) - 0.15},   mean = (1+delta)D,   B = mean - f_min,
   f_max = mean + B,   b = B/D,   R = kappa/(nu delta),   omega = kappa b/(2 pi delta),
   Q_0   = max{ 1.05 f_max^3 e^{omega} / (6(C_P^3-1)) ,  10 f_max^3 } ,
   N_0   = ( 3 Q_0 e^{omega} + f_max^3/2 )^{1/3} ,
   Lambda = 4 N_0^4/(C_S^2 E_0) ,        T_* = E_0(1-gamma)/(4 nu Lambda) ,
```

and, with `s = -log(1 - t/T_*)` on `t in [0,T_*)`,

```
   d_1(t) = f(s)  = mean + B cos(2 pi s/S)                                (log-periodic)
   Q(t)           = Q_0 exp( R nu delta s + R C_sharp B (S/2pi) sin(2 pi s/S) )
   D_Q(t)         = (R/T_*) e^{s} Q(t) ,        K(t) = C_sharp f(s) D_Q(t)
   ||u(t)||_3     = ( 3Q(t) + f(s)^3/2 )^{1/3}
   ||grad u(t)||_2^2 = Y(t) = Lambda e^{gamma s}
   ||u(t)||_2^2   = E(t) = E_0 - 2 nu T_* Lambda (1 - e^{-(1-gamma)s})/(1-gamma)
   ||u(t)||_4^2   = C_S^{3/2} E(t)^{1/4} Y(t)^{3/4}
```

The balance is an identity, not an approximation:
`Q'(t) = Q R (C_sharp f - nu) e^{s}/T_* = (C_sharp f - nu) D_Q`, so
`Q' + nu D_Q = C_sharp f D_Q = K` with `|K| = C_sharp d_1 D_Q` exactly on the
HF21-B ceiling. `Q` increases exactly where `C_sharp d_1 > nu` and decreases
exactly where `C_sharp d_1 < nu`, as HF21-B Theorem 4.5(2) demands, with net
growth `e^{kappa s}` per unit `s`; `||u||_3 -> infinity`, `Y -> infinity`,
`T_* < infinity`, and `C_sharp d_1` re-enters the band twice per log-period, at
times accumulating at `T_*`, with `||grad u||_2 -> infinity` along them.

> **Result 6.1 (this lane).** The functions above satisfy **all of S1–S14**,
> together with `T_* < infinity` and `Corr_eps` accumulating at `T_*`. Hence
> `(C)_eps` is **not derivable** from S1–S14.

**Verification.** All eighteen checks pass on the canonical instance
`nu = 1`, `C_S = 0.4272` (the sharp `L^6`/`Hdot^1` constant), `C_P = 2`,
`C_9 = 3`, `C_sharp = 2`, `E_0 = 1`, `eps = 1/4`, giving `T_* = 1.90e-5`,
`Lambda = 2638`, `Q_0 = 9.27`; and on a randomised scan of **600** admissible
constant sets with `nu, C_S, C_sharp, E_0` over four decades,
`C_P, C_9 in (1, 11)` and `eps in (0.02, 0.49)`: **0 failures**. Binding
constraints, i.e. the ones that actually shape the parameters, are S9 (which
fixes `Lambda` from `Q_0`), S1 (which fixes `T_*` from `Lambda`), S11 (which
forces `Q_0` to be taken large rather than at the S6 floor) and S6 (the floor).
S12 and S13 are satisfied with large slack — HF24-A Theorem 3.3 is
*asymptotically vacuous* along this family, because `G` grows like `e^{gamma s/2}`
while the required `d_1`-increment stays at `O(nu/C_sharp)`, exactly the
saturation HF24-A §5.2 predicted for its viscous-eddy family.

### 6.3 What this is and what it is not

**It is** a certificate that (C) does not follow from the scalar closure of the
audited record. It is the same species as `hf22-good-set-dissipation.md`
Theorem C' and as HF26's curve, and I place it against them honestly:

* HF22-C's non-derivability theorem is for **(G)** from its constraints
  (T1)–(T9); this one is for **(C)** from S1–S14, a strictly larger list that
  includes HF18-A's `L^9` coercivity, the strong-convexity link S7, and the two
  newest HF24-A theorems.
* HF26's curve closes two of HF22-C's three escapes (actual minimisers; survives
  a perfect scalar modulus) but has `d_1` **constant** and no `T_*`; it
  therefore cannot address (C), and indeed satisfies it (§4). This countermodel
  closes the escape HF26 leaves open in the corridor currency — it produces the
  accumulation R1 needs — at the price of reopening the one HF26 closed: it is
  a system of scalars, with **no field realising them simultaneously asserted or
  known**.
* **The escape it does not close is the same one HF22-C named: the actual
  equation.** Nothing here is a Navier–Stokes solution, a Leray–Hopf solution,
  a curve of fields, or evidence of any kind that a singularity exists. **(C) is
  not refuted.**

By R1 that limitation is unavoidable and should be stated as a theorem rather
than a caveat:

> **Observation 6.2.** Any refutation of `(C)_eps` for any `eps` requires
> exhibiting a finite-time singularity of the unforced equation on `R^3` with
> Schwartz data. Hence (C) is unfalsifiable in this programme unless the Clay
> alternative is settled negatively, and the only honest adversarial verdicts
> available are "non-derivable" and "instantaneously false".

---

## 7. OBSTRUCTION A — THE INSTANTANEOUS FORM OF (C) IS FALSE

This is the sharpest result of the lane, and it answers HF24-A's own next
question.

> **Proposition A (this lane).** Let `nu > 0`, `eps in (0,1/2)`, `E > 0` and
> `Gamma < infinity`. There is a divergence-free `u in S(R^3)^3` with
>
> ```
>    ||u||_2^2 = E ,   C_sharp d_1(u) in [(1-2eps)nu, (1-eps)nu] ,   ||grad u||_2 > Gamma .
> ```
>
> Consequently there is **no** function `Gamma(nu,E,eps)` such that the corridor
> condition implies `||grad u||_2 <= Gamma`, and — taking such a `u` as initial
> datum, so that `t = 0 < min{H,T_*}` is a corridor time on its own classical
> trajectory — **(C) with `Gamma` depending only on `(nu, E_0, H, eps)` is false
> along actual classical trajectories at fixed kinetic energy.**

*Proof.* Three explicit ingredients, all checked.

1. *A field off the nonlinear-Hodge class.* Let `b = curl(x_1 e^{-|x|^2} e_3)`.
   Then `b` is Schwartz, `div b = 0` (verified symbolically), and
   `div(|b|b) = b.grad|b|` is not identically zero: it equals `0.29913` at
   `(0.3,0.2,0.1)` and `-0.0071834` at `(0.7,-0.4,0.2)` (both signs, verified
   symbolically). By `lem:quotient-minimizer`(c), `q(b) = 0` would force
   `div(|b|b) = 0`; hence `d_1(b) > 0`.
   *(For contrast, and used nowhere below: every pure axisymmetric swirl
   `u = v(r,z)e_theta` is solenoidal with `div(|u|u) = 0` exactly — verified
   symbolically on `e^{-|x|^2}(-x_2,x_1,0)` — so the nonlinear-Hodge class
   contains Schwartz solenoidal fields of arbitrary critical norm with
   `d_1 = 0`. This is why no lower bound `d_1 >= phi(||u||_3)` can exist.)*
2. *Pinning `d_1` in the band.* Set `alpha = (1 - 1.5 eps)nu/(C_sharp d_1(b))`.
   By `lem:quotient-scaling`, `d_1(alpha D_lambda b) = alpha d_1(b)` for
   **every** `lambda > 0`, so `C_sharp d_1(alpha D_lambda b) = (1-1.5eps)nu`,
   the midpoint of the band, independently of `lambda`.
3. *A high-frequency solenoidal packet.* Put
   `p_N = curl( N^{-3/2} e^{-|x|^2} sin(N x_1) e_3 )`. It is Schwartz,
   `div p_N = 0` identically, and numerically (Riemann sums on `[-5,5]^3`,
   `170^3` points; successive-ratio test against the predicted `2^{-1/2}`,
   `2^{-1/2}`, `2^{1/2}`):

   | `N` | `||p_N||_2` | `||p_N||_3` | `||grad p_N||_2` |
   |---|---|---|---|
   | 16 | 0.24900 | 0.19263 | 4.038 |
   | 32 | 0.17556 | 0.13608 | 5.637 |
   | 64 | 0.12405 | 0.09611 | 7.946 |
   | 128 | 0.08770 | 0.06797 | 11.228 |

   ratios `0.7070, 0.7072, 1.4130` at the last step, matching
   `||p_N||_2, ||p_N||_3 ~ N^{-1/2}` and `||grad p_N||_2 ~ N^{1/2}`.

Now set `u_{N,lambda} = alpha D_lambda b + p_N`. For fixed `N` with
`||p_N||_2^2 < E`, the map `lambda -> ||u_{N,lambda}||_2^2` is continuous, tends
to `||p_N||_2^2 < E` as `lambda -> infinity` and to `+infinity` as
`lambda -> 0` (since `||D_lambda b||_2^2 = lambda^{-1}||b||_2^2`), so by the
intermediate value theorem there is `lambda_N` with energy exactly `E`; the
triangle inequality bounds `lambda_N` above by
`alpha^2||b||_2^2/(E^{1/2}-||p_N||_2)^2`, which is finite and bounded in `N`.
By \eqref{eq:cp-strong} with `h = p_N` and
`||w(alpha D_{lambda}b)||_3 <= alpha||b||_3` (scale-invariant, hence uniform in
`lambda`),
`|d_1(u_{N,lambda_N}) - alpha d_1(b)| <= 2(alpha||b||_3+||p_N||_3)^{1/2}||p_N||_3^{1/2} + ||p_N||_3 -> 0`,
so `C_sharp d_1(u_{N,lambda_N}) -> (1-1.5eps)nu`, which lies in the open band;
hence it is in the band for `N` large. Finally
`||grad u_{N,lambda_N}||_2 >= ||grad p_N||_2 - alpha lambda_N^{1/2}||grad b||_2 -> infinity`.
`[]`

**Consequences, stated with their exact scope.**

1. **The corridor condition carries no instantaneous information about the
   enstrophy.** The record's only link runs the other way
   (`d_1 <= sqrt2||u||_3 <= sqrt2 C_S^{1/2}E_0^{1/4}Y^{1/4}` gives a *lower*
   bound `Y >= (1-2eps)^4 nu^4/(4C_S^2C_sharp^4 E_0)` on the corridor). HF24-A's
   NEXT DISTINCT ACTION 1 asked whether an upper bound is available. **It is
   not, in the strongest sense: not even at fixed energy, not even at time
   zero.**
2. **`Gamma` is not effectivisable**, so neither is the count
   `1 + 8 Theta Gamma^3` of Corollary 4.3. Combined with Observation 1.1, the
   corridor route yields at best "finitely many bad components, with no bound on
   how many", inside a total measure that *is* effectively bounded by S14.
3. **What Proposition A does NOT do.** It does **not** refute `(C)_eps` as
   stated, because (C) permits `Gamma` to depend on the whole datum `u_0`, and
   each field above is one datum. This is precisely the "for every cutoff, some
   datum" pattern the programme flagged at HF14 and again at HF23 Scope B, and
   it is not papered over here. What it establishes is that any proof of (C)
   must be a genuine trajectory-compactness argument — by R1, a proof of
   alternative (ii) — with no instantaneous ingredient available.

Structurally this is the corridor-route analogue of the audited HF03 fixed-energy
obstruction and of `rem:no-monotone`; it is a new instance of an established
pattern, not a new pattern, and no novelty is claimed for the method.

---

## 8. THE DECISIVE FINDING ON THE `eps`-QUANTIFIER

> **Proposition B (this lane).** Fix `nu, u_0, H` and suppose `T_* <= H`
> (the branch where (C) has content). Then, for `eps in (0,1/2)`:
>
> 1. `liminf_{t->T_*} C_sharp d_1(t) > (1-eps)nu  =>  (C)_eps  =>  liminf >= (1-eps)nu`;
> 2. `(C)_eps` is **monotone increasing in `eps`**: `eps < eps'` and `(C)_eps`
>    imply `(C)_{eps'}`;
> 3. `(C)_eps` for **all** `eps in (0,1/2)`  `<=>`  `liminf_{t->T_*} C_sharp d_1(t) >= nu`;
> 4. `(C)_eps` for **some** `eps in (0,1/2)`  `<=>`  `liminf_{t->T_*} C_sharp d_1(t) > nu/2`.

*Proof.* (1) and (2) are immediate from R1's alternative (ii), which reads
`C_sharp d_1 > (1-eps)nu` on a final interval and is weaker for larger `eps`.
(3) `<=`: `liminf >= nu > (1-eps)nu` gives (ii) for each `eps`. `=>`:
`liminf >= (1-eps)nu` for all `eps in (0,1/2)`, let `eps -> 0`. (4) `<=`: pick
`eps < 1/2` with `(1-eps)nu < liminf`. `=>`: (ii) gives
`liminf >= (1-eps)nu > nu/2`. `[]`

**Reading.** The lane's SURVIVING CONDITIONAL SUFFIX says "if (C) holds for one
`eps in (0,1/2)`"; the audit's R1 fixes `eps` throughout and its alternative (ii)
is `eps`-dependent. **Lane and audit agree, and both are correct**: the
operative reading is *for one `eps`*, because Corollary 4.3 consumes (C) at the
same `eps` as its corridor. Neither states Proposition B, and the consequences
are worth having:

* **`eps` cannot be chosen adversarially to defeat the hypothesis.** For a fixed
  trajectory, `{eps : (C)_eps holds}` is an up-set in `(0,1/2)`; an adversary
  choosing `eps` small only strengthens the statement the prover must prove, and
  cannot turn a true instance into a false one.
* **`eps` cannot be chosen favourably to trivialise it.** The weakest member,
  `eps -> 1/2`, still demands `liminf C_sharp d_1 > nu/2`, a factor `2` below the
  level the record already forces as a `limsup` (Lemma 2.1). Nothing collapses.
* **The `eps`-parameter is a red herring: the target is `eps`-free.** The
  natural statement behind the whole family is
  `liminf_{t->T_*} C_sharp d_1(t) >= nu`, which is exactly Lemma 2.1 with
  `limsup` replaced by `liminf`. **This lane's recommendation to the controller
  is that the sibling lane's target be restated in that form**, since it is the
  `eps`-free statement, it makes the distance to the record visible in one line,
  and it is what Proposition B(3) says "(C) for all `eps`" means.
* **There is an interior optimum.** `Theta ∝ eps^{-4}` (the count degrades as
  `eps -> 0`) and `|B^eps_tau| ∝ (1-2eps)^{-4}` (the measure degrades as
  `eps -> 1/2`); minimising the product over `eps` gives, exactly,
  `eps = 1/4`, band `[nu/2, 3nu/4]`, at which `(C)` demands
  `liminf C_sharp d_1 >= (3/4)nu`. This is a quantitative remark, not a theorem
  about (C).

**Is the band an artifact?** No. §2.1 shows the corridor is scaling-invariant
and centred on the dynamically selected level `nu/C_sharp`; §3 Corollary 3.2
shows that any log-periodic profile of `d_1` along a would-be self-similar
singularity is *forced* to reach that level. The `eps`-window is an artifact
only in the sense that its width is a free bookkeeping parameter with an
interior optimum; its **location** is not free.

---

## 9. VACUITY TEST

Four ways (C) could be content-free were tested.

1. **Global branch.** If `T_* = infinity`, or merely `T_* > H`, then (i) holds
   and (C) is automatic. So **(C) has content only in the blow-up branch**,
   where R1 makes it exactly (ii). This is not a defect — it is the source of
   the asymmetry the plan calls promising — but it means (C) is *true for every
   datum for which the Clay conclusion holds*, and so can never be used to
   distinguish data.
2. **Small data.** Suppose `sqrt2 C_P C_sharp ||u_0||_3 < (1-2eps)nu`. On the
   relatively open and closed subset of `[0,T_*)` where `C_sharp d_1 < nu`, the
   balance gives `Q' <= 0`, hence `Q <= Q(0) <= ||u_0||_3^3/3` and, by
   \eqref{eq:cp-coercive} and Lemma 2.2,
   `C_sharp d_1 <= sqrt2 C_sharp ||u||_3 <= sqrt2 C_P C_sharp ||u_0||_3 < (1-2eps)nu`.
   By continuous induction that subset is all of `[0,T_*)`, so `Corr_eps` is
   empty, (C) holds vacuously and `T_* = infinity`. So **(C) is genuinely
   vacuous on the small-data class** (this is the audited recovery of Kato's
   small-`L^3` theorem recorded in HF18-A, restated in the corridor currency),
   which is already settled.
3. **Empty corridor at large times in the blow-up branch.** Not possible for
   trivial reasons: `d_1` is continuous (`prop:localtheory` + `cor:Lq` +
   `lem:quotient-stability`), so a corridor-free final interval forces
   `C_sharp d_1` into one of the two open complementary rays, and the lower ray
   forces `T_* = infinity` (Lemma 2.1). The upper ray *is* alternative (ii).
   **R1 already exhausts this**, and there is no fourth possibility.
4. **Content-free by non-effectivity.** This is the one that bites, and it is
   Observation 1.1 with Proposition A: (C) is not vacuous, but it is equivalent
   to a topological statement with no computable constant, and its only recorded
   consequence (Corollary 4.3's count) inherits that. HF24-A's own Remark 4.4
   already records that "**No part of (G) is closed by Corollary 4.3,
   conditionally or otherwise.**" Combining: **even a successful proof of (C)
   would leave (G), `hyp:highstrain` and the first gap exactly where they are**,
   and would add only a non-effective component count to an already effective
   measure bound. That is a scope fact about the route, not an objection to the
   sibling lane's mathematics.

---

## 10. FRONTIER RECORD

**MODE / RESULT.** DISCOVER, adversarial. **(C) not refuted; (C) shown not
derivable from the audited record; the instantaneous form of (C) shown false;
the `eps`-quantifier settled.** Five constructions or obstructions attempted,
three failed, two succeeded; all reported.

**CLAIM AND SCOPE.** For the maximal classical branch of `prop:localtheory`
at arbitrary `nu > 0` and arbitrary divergence-free Schwartz datum:

1. (§2.1) `d_1` is invariant under the critical dilation and `1`-homogeneous in
   amplitude; the corridor is a scaling-invariant condition at the dynamically
   selected level `nu/C_sharp`. A sharper `C_sharp` makes (C) strictly harder.
2. (Lemma 2.1) `T_* < infinity  =>  limsup_{t->T_*} C_sharp d_1(t) >= nu`.
   This is the only asymptotic lower bound on `d_1` in the record.
3. (Lemma 2.2) `(1/6)d_1^3 <= (1/3)||u||_3^3 - Q <= ||u||_3^2 d_1` and
   `d_1 <= sqrt2 ||u||_3`, for every `u in L^3`.
4. (Proposition 3.1) Exact discretely-self-similar and exactly self-similar
   blow-up with `L^3` profile is excluded by `thm:continuation`, because every
   scale-invariant quantity — `||u(t)||_3` included — is then log-periodic hence
   bounded. (Corollary 3.3) An exactly self-similar singularity would **satisfy**
   (C).
5. (§4) HF26's and HF27's concentrating Leray curves satisfy `C_sharp d_1 >= nu`
   at every time, hence satisfy (C). Both audited countermodel families support
   alternative (ii).
6. (Proposition 5.1) If `T_* < infinity` and `d_1` converges as `t -> T_*`, then
   (C) holds for every `eps`. Any counterexample must have `d_1` oscillating with
   amplitude bounded below — the log-periodic shape.
7. (Result 6.1) An explicit scalar countermodel satisfies S1–S14 with
   `T_* < infinity` and `Corr_eps` accumulating at `T_*`; verified on a canonical
   instance and on 600 randomised admissible constant sets, 0 failures. Hence
   `(C)_eps` is not derivable from the scalar closure of the record.
8. (Proposition A) At fixed `(nu, E, eps)` the corridor condition implies **no**
   upper bound on `||grad u||_2`, already at time zero on actual classical
   trajectories. `Gamma` is not effectivisable in `(nu, E_0, H, eps)`.
9. (Proposition B) `(C)_eps` is monotone in `eps`; for all `eps` it is
   `liminf C_sharp d_1 >= nu`; for some `eps` it is `liminf C_sharp d_1 > nu/2`;
   the product of the count and measure degradations is minimised at `eps = 1/4`.

**EVIDENCE.** Proofs above from the listed audited premises. Symbolic checks:
`div b = 0` and `div(|b|b) != 0` for `b = curl(x_1e^{-|x|^2}e_3)` with both
signs at explicit points; `div U = 0` and `div(|U|U) = 0` for the swirl
`e^{-|x|^2}(-x_2,x_1,0)`; `div p_N = 0`; `||D_lambda v||_3 = ||v||_3`;
`lim_{t->1} d(t) = d_*` for the HF26 crossing function; `argmin_eps
(eps(1-2eps))^{-4} = 1/4`. Numerical: packet norms on `[-5,5]^3`, `170^3`
Riemann sums, successive ratios `0.7070/0.7072/1.4130` against predicted
`0.7071/0.7071/1.4142`; countermodel constraint sweep, 18 checks on the
canonical instance and 600 randomised constant sets, all passing, with the
balance residual `|Q' + nu D_Q - K|/(|K| + nu D_Q) < 1e-12`. **Numerics are
bounded evidence at finite resolution, not proof**; every load-bearing statement
above has an analytic proof and the numerics only corroborate it.

**FIRST GAP.** Unchanged and untouched: the arbitrary-data signed spacetime
absorption, HIGH-PRESSURE or HIGH-STRAIN. Within the corridor route the gap is
now stated `eps`-free: **prove that `T_* < infinity` implies
`liminf_{t->T_*} C_sharp ||q(t)||_3 >= nu`** — the upgrade of Lemma 2.1's
limsup to a liminf. Every `(C)_eps` is implied by it, and by Proposition B(4)
even the weakest member requires the liminf to exceed `nu/2`. No instantaneous
argument can contribute (Proposition A), and no argument using only S1–S14 can
(Result 6.1).

**SURVIVING CONDITIONAL SUFFIX.** (i) If a future lane proves
`liminf_{t->T_*} C_sharp d_1 >= (1-eps)nu` for one `eps in (0,1/2)` at a finite
`T_*`, then `(C)_eps` holds and HF24-A Corollary 4.3 follows — with a `Gamma`
that, by Proposition A and Observation 1.1, is finite but not computable from
`(nu,E_0,H,eps)`. (ii) Even then, by HF24-A Remark 4.4, no part of (G) is
closed. Nothing in this lane is conditional on anything else.

**NON-CLAIMS.** No refutation of (C), (G), `hyp:highstrain`, `hyp:highpressure`,
`hyp:absorption`, `hyp:critical` or NS-R3, and no proof of any of them. No
Navier–Stokes solution, no Leray–Hopf solution, no curve of fields, and no
evidence that a singularity exists: the object of §6 is a system of scalar
functions and **no field realising them is asserted or known**. No claim that
(C) is false — only that it is not derivable from S1–S14, that its
instantaneous and energy-only forms are false, and that it is unfalsifiable
short of a blow-up construction. No claim about the DSS or Type-II literature
beyond `literature/blowup-barriers.md` §3 and the audited HF26/HF27 prior-art
findings; the session's web-search budget was exhausted before this lane ran and
no external source was consulted. No novelty or priority claim for anything
here: Lemma 2.2 is elementary uniform convexity, Proposition 3.1 is the
observation that a periodic function is bounded, and Propositions A and B are
new instances of patterns the programme already records (HF03/HF14/HF23-B for
the fixed-energy species; HF22-C/HF26 for the non-derivability species). No
smallness hypothesis; no forced, periodic, hyperdissipative or Euler
substitute; all statements are for the unforced branch on `R^3` at arbitrary
`nu > 0` and arbitrary divergence-free Schwartz datum. The minimiser is never
differentiated in time or space; `w in L^2` and `sigma in L^{3/2}` are never
used. HF24-A Theorems 3.3 and 4.1 are **unaudited** and were used only as
additional constraints against the countermodel, never as support for any
claim. Nothing is promoted; no manuscript, graph or status file is touched;
nothing is committed or pushed.

**NEXT DISTINCT ACTION.** Three, in order.

1. **Audit this lane**, in three separable scopes: (a) Lemma 2.2 and
   Proposition 3.1 with Corollaries 3.2–3.3; (b) Proposition A, in particular
   the intermediate-value step fixing `lambda_N`, the uniform bound on
   `lambda_N`, and the use of \eqref{eq:cp-strong} across the packet
   perturbation; (c) the constraint list S1–S14 for **completeness** — the
   HF22-C audit's finding was precisely that an incomplete constraint list makes
   a countermodel void, and the same failure mode applies here. Any relation
   between `(E,Y,||u||_3,||u||_4,Q,D_Q,K,d_1)` that the record supplies and
   that S1–S14 omits potentially kills Result 6.1.
2. **Decide whether the liminf statement of the FIRST GAP is attackable at
   all.** The two live sub-questions this lane leaves: does the record support
   any *rate* for how fast `Q` must grow across an excursion above `nu/C_sharp`
   (the countermodel needs `int (C_sharp d_1 - nu)_+ D_Q dt = infinity`, which is
   forced by blow-up and is essentially the negation of (G), so it is not a
   handle); and is there a *field-level* obstruction to `d_1` returning to the
   band while `||u||_3 -> infinity`, i.e. a lower bound for `d_1` in terms of
   any norm that blows up? §7 shows there is none in `||u||_3`, and the pure
   swirls show there is none at all pointwise in the class; a *dynamic* version
   is untested.
3. **Independently, decide whether the corridor route is worth continuing** in
   view of §9 item 4: even proved, (C) adds a non-effective component count and
   closes no part of (G). That is a controller decision, not a mathematical one,
   and this lane does not make it.

- needs review: whether S1–S14 is a complete enumeration of the record's scalar
  relations along the classical branch; Result 6.1 is void if it is not.
- needs review: whether Lemma 2.2's lower bound `(1/6)d_1^3 <= F(u) - Q` is
  already in the manuscript in another form (I did not locate it, but the
  section's convexity machinery makes it a two-line corollary and it may be
  implicit in `lem:quotient-stability`'s proof).
- needs review: whether Proposition 3.1's exclusion of exact DSS blow-up for
  every scaling factor `L`, obtained from `thm:continuation` alone, is
  consistent with the scope Chae–Wolf claim (near-one `L`) and whether the `L^3`
  profile hypothesis is doing hidden work — in particular whether a DSS profile
  merely in `L^{3,infinity}` escapes it, since `lem:quotient-scaling` needs
  `L^3` for `Q` to be defined at all.
- needs review: whether the tension recorded in §2.1 — a sharper `C_sharp`
  strengthens the Lyapunov step but strictly strengthens (C) — has a quantitative
  optimum, and whether the programme should therefore *not* pursue a sharper
  `C_sharp` while the corridor route is live.
