# HF26 audit: the one-scale temporal producer, what energy supplies, and the exact remainder

Independent, adversarial proof audit of one scope of the frozen HF26 candidate.
Scope only; nothing outside this file was read for the purpose of promotion, and
nothing outside this file was edited.

## Scope

| Item | Value |
|---|---|
| Audit target | `research/evidence/hf26-temporal-continuation.tex` (frozen, never edited) |
| Target SHA-256 | `24b538280c8639b81a1f6f86d4c72370362625ca8a52d1d81a99b29236a540ab` (recomputed, matches the index note) |
| Target line count | 1432 (matches the index note) |
| Controller index note | `research/evidence/hf26-temporal-continuation.md` (context only) |
| `git -C ../navier rev-parse HEAD` | `30d715d` (audit ran on `main`, clean) |
| Audit date | 2026-09-06 |

Sections audited, by label:

- **Section 5** `sec:temporal` (lines 653-779): `lem:T6` (Lemma 5.1),
  `hyp:temporal` (Hypothesis 5.2), `thm:temporal` (Theorem 5.3),
  `cor:modulus` (Corollary 5.4), and the display `eq:T3`, `eq:average`,
  `eq:Ldelta`, `eq:averageL6`, `eq:residualsmall`, `eq:Mdelta`,
  `eq:temporalQD`, `eq:temporalG`, `eq:Young34`, `eq:tempdiff`,
  `eq:vectormodulus`.
- **Section 6** `sec:increments` (lines 780-898): `eq:BUOmega`,
  `lem:negativeincrements` (Lemma 6.1), `eq:negativeinterp`, `eq:CI`,
  `thm:qtime` (Theorem 6.2), `eq:qpairpoint`, `cor:residualmeasure`
  (Corollary 6.3), `eq:residualintegrated`, `eq:residualmeasure`.
- **Section 9.1** `sec:boundary` first subsection (lines 1024-1060):
  `eq:badremainder`, `eq:badremainderintegral`, and the accompanying
  no-mechanism paragraph.

Read for context but **not** audited: Sections 1-4, 7, 8, 9.2-9.3, the ledger,
and all four appendices. Section 2's inherited displays (`eq:holder`,
`eq:coercivity`, `eq:divcurl`, `eq:Didentity`, `eq:Dcontrol`, `eq:gradA`,
`eq:Kq`, `eq:workform`, `eq:qbudgets`) were re-derived only to the extent the
audited scope consumes them; that re-derivation is recorded below and is not a
verdict on Section 2 or on the HF23 import.

Independent verification was done with sympy and randomized numerics
(`Young`, the constant assemblies, the Holder exponent sums, the interpolation
exponents, the two elementary power inequalities, and a Navier-Stokes scaling
consistency test). Every symbolic identity below was machine-confirmed.

---

## VERDICT

**PASS WITH SCOPE.**

Every inequality, constant and derivation in the audited scope is correct as
written -- I found no arithmetic error, no invalid bridge, and no continuation
norm inside any *proof*. The scope restriction is logical, not analytic:
`hyp:temporal` is itself an endpoint continuation norm (a supremum over
`[0, min{H,T*})`), and I prove below, with an elementary argument built only
from the document's own `lem:negativeincrements`, `eq:negativeinterp` and
`cor:modulus`, that it is **implied by finiteness of the `H^1` blow-up
alternative** `sup_t ||grad u(t)||_2` and, with the manuscript's imported ESS
endpoint theorem, **equivalent to it**. So `hyp:temporal` is not a weakening of
the classical criteria in any non-vacuous sense; it is the same continuation
statement in a new observable. That is the exact analogue of the earlier HF25
finding, and it must be recorded before any of Section 5 is quoted as a
"producer".

---

## Per-question findings

### Q1. Circularity: is `thm:temporal`'s proof free of any continuation norm?

**Verdict on the proof: YES, genuinely free.** **Verdict on the hypothesis: NO
-- it is a continuation norm, and the qualifying clause inside it is not a
mathematical statement.**

Constant-by-constant trace. All quantities below were re-derived from the
document's own Section 2 displays; none depends on the solution beyond the
input `(nu, u_0, H)` and the free scale `delta`.

| Constant | Origin | Depends on | Continuation norm? |
|---|---|---|---|
| `S` | scalar Sobolev `\|f\|_6 <= S\|grad f\|_2` | universal | no |
| `C_p` | `\|P\|_{L^p -> L^p}`, Leray projection | universal (`1<p<inf`) | no |
| `C_sharp = (3/2) C_9 S` | `eq:Kq`, Holder `(3,9,18,2)` + `eq:Dcontrol` | universal | no |
| `a_0 = (9/8) S^2` | `eq:Dcontrol`, from `\|V\|_6 <= S\|grad V\|_2` and `D >= (8/9)\|grad V\|_2^2` | universal | no |
| `C_{9/2}` | `\|P\|_{L^{9/2}->L^{9/2}}` in `lem:T6` | universal | no |
| `B_6 = sqrt2 * 3^{1/4} C_{9/2} a_0^{1/4}` | `lem:T6` | universal | no |
| `Y_0 = \|grad u_0\|_2^2`, `E_0 = \|u_0\|_2^2` | datum | `u_0` | no |
| `L_delta^2 = S^2(Y_0/4 + E_0/(8 nu delta))` | `eq:Ldelta`, from `int_0^t Y <= E_0/(2nu)` and `\|grad q\|_2^2 <= Y/4` | `(nu, u_0, delta)` | no |
| `M_delta = 81 C_{9/2}^4 a_0 nu^{-3} L_delta^4` | `eq:Mdelta` | `(nu, u_0, delta)` | no |
| `Q_0 = Q(u_0)` | datum | `u_0` | no |
| `A_G = 2(1+C_3)3^{1/3} nu^{-1} Q_0^{4/3} e^{4 M_delta H/3}` | `eq:temporalG` | `(nu, u_0, H, delta)` | no |

Two structural points confirm the proof is clean:

1. `eq:averageL6` uses only the **time-integrated** energy budget
   `int_0^t Y ds <= E_0/(2 nu)` (valid on all of `[0, T*)` unconditionally) and
   the pointwise-in-time spatial bound `\|grad q\|_2^2 = \|div w\|_2^2 <= Y/4`.
   No supremum over the interval is taken anywhere. The `t`-uniformity of
   `L_delta` is bought by the averaging window, not assumed.
2. The final `G` step bounds `sup_{t<=tau} Q(t)` by `eq:temporalQD`, which was
   proved for every `tau` separately. It is not a pre-assumed endpoint quantity.

**The circularity lives entirely in `hyp:temporal`, and it is real.** The
quantity assumed small,

```
sup_{0 <= t < min{H, T*}} ||r_delta(t)||_3,
```

is by definition a supremum over the whole interval up to the unknown maximal
time -- exactly the object the programme calls a continuation norm. The
hypothesis attempts to fence this off with the clause "justified without an
endpoint continuation norm" and the sentence "The scale is selected before the
stopping time". Both are **meta-statements about a hypothetical future proof,
not conditions on `delta`**. As mathematics they are empty:

- `T*` is a function of `(nu, u_0)`. So is `Lambda := sup_{t < min{H,T*}} Y(t)`.
  Any `delta` chosen as a function of `Lambda` is, verbatim, a function
  `delta(nu, u_0, H)` and satisfies the literal quantifier of `hyp:temporal`.
- Therefore the literal statement of `hyp:temporal` is *satisfied* by the route
  the clause is trying to forbid. The clause can only be enforced by a human
  reading a proof, not by the statement.

**Auditor's Proposition A** (elementary; uses only the document's own Section 6
machinery). Suppose `Lambda = sup_{0<=t<min{H,T*}} Y(t) < infinity`. Then
`hyp:temporal` holds, with an explicit input-determined scale. Proof: run
`lem:negativeincrements` with the pointwise bound `Y <= Lambda` in place of the
energy budget, giving
`||u(t+h)-u(t)||_{Hdot^-1} <= (nu Lambda^{1/2} + S^{3/2} E_0^{1/4} Lambda^{3/4}) h`.
Feed that and `J = Y(t+h)+Y(t) <= 2 Lambda` into the pointwise chain of
`thm:qtime` (i.e. `eq:qpairpoint` before the time integration). This yields the
**vector** modulus

```
||q(t+h) - q(t)||_3 <= kappa h^{1/6},
kappa^3 = 72 * 2^{3/2} S^{3/2} E_0^{1/4} Lambda
          * ( nu Lambda^{1/2} + S^{3/2} E_0^{1/4} Lambda^{3/4} )^{1/2}.
```

(Machine-checked.) Now apply `cor:modulus` with `delta = (nu/(4 C_sharp kappa))^6`.
QED.

**Auditor's Proposition B.** `hyp:temporal(nu,u_0,H)` holds **iff**
`Lambda < infinity` **iff** `T* > H`. Backward: Proposition A, together with the
manuscript's local package ("finite `T*` forces loss of the `H^1` bound"), so
`Lambda < infinity` exactly when `T* > H`. Forward: `thm:temporal` gives
`sup Q <= Q_0 e^{M_delta H}`, hence `sup ||u||_3^3 <= 3 C_3^3 sup Q < infinity`
by `eq:coercivity`; the imported ESS endpoint theorem then forbids `T* <= H`.
(The forward direction, and only that direction, uses the external ESS import
declared in `thm:fullconditional`.)

So `hyp:temporal` is *equivalent to the conclusion it is used to derive*. The
document is not naive about this in general -- Section 1.3 says plainly that
"their existential implications through global continuation do not provide a
priori witnesses" -- but Section 5 never says it about `hyp:temporal`, and the
index note does not either. **The audited scope is correct; the framing is
what needs the repair (R1, R2).**

### Q2. `thm:temporal`: Young, `B_6^4`, `M_delta`, Gronwall, `eq:temporalG`

**All correct. Verified independently, symbolically.**

- **`eq:Young34`.** `f(x) = a x^{3/4} - eps x` has `f'(x)=0` at
  `x* = (3a/(4 eps))^4 = 81 a^4/(256 eps^4)`, `f''(x*) = -64 eps^5/(81 a^4) < 0`,
  and `f(x*) = 27 a^4/(256 eps^3)` exactly. Sympy confirms. The inequality is
  sharp, not merely valid.
- **`B_6^4 = 12 C_{9/2}^4 a_0`.** `B_6 = sqrt2 * 3^{1/4} C_{9/2} a_0^{1/4}`, so
  `B_6^4 = 4 * 3 * C_{9/2}^4 a_0`. Confirmed.
- **`M_delta`.** With `a = B_6 L_delta Q^{1/4}`, `x = D`, `eps = nu/4`, the
  remainder is `27 a^4/(256 (nu/4)^3) = (27/4) B_6^4 L_delta^4 Q nu^{-3}
  = 81 C_{9/2}^4 a_0 nu^{-3} L_delta^4 Q = M_delta Q`. Exact, no slack lost or
  gained. Confirmed symbolically.
- **The split.** `K = T_u(r_delta) + T_u(qbar_delta)` is legitimate: `T_u` is
  linear in its argument (`eq:workform` + the remark after `eq:Kq`),
  `r_delta(t) in L^3` and `qbar_delta(t) in L^3 cap L^6`, and both integrals
  converge absolutely by the two Holder chains. `T_u(r_delta) <= nu D/4` by
  `eq:T3` + `eq:residualsmall`; `|T_u(qbar_delta)| <= B_6 L_delta Q^{1/4} D^{3/4}`
  by `lem:T6` + `eq:averageL6`. Summing in `eq:balance`:
  `Q' = K - nu D <= -nu D + nu D/4 + nu D/4 + M_delta Q`, i.e. `eq:tempdiff`.
  Correct.
- **Gronwall.** `(e^{-M t} Q)' + (nu/2) e^{-M t} D <= 0`; integrate and multiply
  by `e^{M tau}` to get `Q(tau) + (nu/2) int_0^tau e^{M(tau-t)} D dt <= Q_0 e^{M tau}`,
  then `e^{M(tau-t)} >= 1`. `eq:temporalQD` is correct, and slightly weaker than
  what the calculation gives (the retained exponential weight is discarded).
- **`eq:temporalG`.** `G(tau) <= sup_{t<=tau}||q||_3 * int_0^tau D
  <= (1+C_3)(3 Q_0 e^{M tau})^{1/3} * (2/nu) Q_0 e^{M tau}
  = 2(1+C_3) 3^{1/3} nu^{-1} Q_0^{4/3} e^{4 M tau/3}`, and `tau < H`. The
  exponent `4/3` and the factor `e^{4 M_delta H/3}` are both exactly right
  (`1/3` from the `Q^{1/3}` in `eq:coercivity`, `1` from `int D`). Confirmed
  symbolically. The witness is uniform in `tau`, so conditional on
  `hyp:temporal` this *is* a legitimate `A_G(nu,u_0,H)` in the sense of
  `eq:Gtarget`.
- **Degenerate case.** `Q_0 = 0 => u_0 = 0` by `eq:coercivity` is correct.

### Q3. `lem:T6`, the two work bounds, and `eq:averageL6`

**Both bounds correct; the "no unavailable `L^2` norm of `q`" claim is TRUE.**

- **`eq:T3` (`C_sharp = (3/2) C_9 S`).** Re-derived: `|T_u(g)| <= (4/3) int |g||u||w|^{1/2}|grad V|`
  by `eq:gradA`; Holder `(3, 9, 18, 2)` with reciprocals
  `1/3 + 1/9 + 1/18 + 1/2 = 1` (confirmed); `|| |w|^{1/2} ||_18 = ||w||_9^{1/2}`;
  `||u||_9 <= C_9 ||w||_9` since `u = P w`; `||w||_9^{3/2} <= (a_0 D)^{1/2}`;
  `||grad V||_2 <= sqrt(9/8) D^{1/2}`. Product:
  `(4/3) C_9 (9/8)^{1/2} S (9/8)^{1/2} = (3/2) C_9 S`. Confirmed symbolically.
- **`lem:T6`.** Holder `(6, 9/2, 9, 2)`, reciprocals `1/6 + 2/9 + 1/9 + 1/2 = 1`
  (confirmed -- note the `L^{9/2}` slot carries `2/9`, so the document's
  sentence "the four reciprocal exponents sum to one" is correct only with that
  reading, which is the intended one). Interpolation `||w||_{9/2} <=
  ||w||_3^{1/2}||w||_9^{1/2}` has `theta = 1/2` (confirmed by solving
  `2/9 = theta/3 + (1-theta)/9`), so `||w||_{9/2}^{3/2} <= (3Q)^{1/4}(a_0 D)^{1/4}`.
  `(4/3) sqrt(9/8) = sqrt2` exactly. `B_6` is right.
- **`eq:averageL6`, the substantive claim.** The temporal average *does*
  genuinely create a uniformly controlled spatial `L^6` coefficient, and the
  mechanism is honest. What energy supplies is `int_0^{T*} ||q||_6^2 dt <=
  S^2 E_0/(8 nu)`, an `L^2`-in-time bound with **no** pointwise-in-time
  content. Averaging over a window of length `delta` converts it into a
  genuine `L^infty`-in-time bound at cost `delta^{-1}`:
  `||qbar_delta(t)||_6^2 <= (1/delta) int_{t-delta}^t ||qtilde||_6^2 ds
  <= (S^2/delta)((delta-t)_+ Y_0/4 + E_0/(8 nu)) <= L_delta^2`.
  Every step re-derived and correct, including the `(delta-t)_+` bookkeeping for
  the frozen negative-time extension (the negative part of `(t-delta,t)` has
  length exactly `(delta-t)_+`) and the two-step Jensen/Cauchy-Schwarz
  (`||avg||_6 <= avg ||.||_6` then `(avg x)^2 <= avg x^2`).
- **The `L^2` claim.** `eq:divcurl` explicitly declines to assert `w in L^2`,
  and the whole chain uses only (i) `q(t) in L^6`, (ii) `grad q in L^2` with
  `||grad q||_2^2 = ||div w||_2^2 <= Y/4`, i.e. homogeneous `Hdot^1`, and (iii)
  `q in C(L^3)`. The Sobolev step `||q||_6 <= S ||grad q||_2` is the
  homogeneous one, valid on `{f in L^6 : grad f in L^2}`, which is exactly what
  `eq:divcurl` provides. **No `L^2` norm of `q` is used anywhere in the audited
  scope.** The ledger's self-audit line on this point is accurate.
- **Measurability.** The `L^6`-Bochner argument (mollify, use Young
  `||rho_eps * g||_6 <= ||rho_eps||_{6/5} ||g||_3` for continuity, then
  pointwise convergence) is correct, and local Bochner integrability follows
  from `int ||q||_6^2 dt < infinity` by Cauchy-Schwarz. No gap.

### Q4. `lem:negativeincrements` and `Omega(h)`

**Correct; both terms verified; the Fourier remark is right.**

Derived independently from `u_t = nu Delta u - P div(u tensor u)`:

- `||nu Delta u||_{Hdot^-1} = nu ||grad u||_2 = nu Y^{1/2}` exactly.
- The symbol of `(-Delta)^{-1/2} P div` is `T -> P(xihat)(T xihat)` with
  `P(xihat) = I - xihat tensor xihat`. Hence
  `|m(xi) T| <= |T xihat| <= |T|_op <= |T|_F`, so the multiplier norm is `<= 1`
  from Frobenius tensor norm to vector norm. The document's one-line claim is
  correct. Consequently `||P div(u tensor u)||_{Hdot^-1} <= ||u tensor u||_2 =
  || |u|^2 ||_2 = ||u||_4^2`.
- `||u||_4^2 <= ||u||_2^{1/2} ||u||_6^{3/2}` has `theta = 1/4` (confirmed), and
  `<= S^{3/2} E_0^{1/4} Y^{3/4}`.
- Time Holder: `int_s^t Y^{1/2} <= (t-s)^{1/2} B_u^{1/2}` and
  `int_s^t Y^{3/4} <= (t-s)^{1/4} B_u^{3/4}` (exponents `2` and `4/3` / `4`),
  with `B_u = E_0/(2 nu) >= int_0^{T*} Y` from `eq:energy`. Both terms of
  `Omega` reproduced exactly.
- **Fourier convention remark.** Correct and non-cosmetic. `(-Delta)^{-1/2}` is
  a convention-independent operator, so `||f||_{Hdot^-1} = ||(-Delta)^{-1/2}f||_2`
  is convention-independent; only the *symbol* changes between `|xi|^{-1}` and
  `(2 pi |xi|)^{-1}`. The disclaimer that individual `u(t)` need not lie in
  `Hdot^{-1}` is a genuine and correct caution: `H^k(R^3)` does not embed in
  `Hdot^{-1}(R^3)`, and the proof only ever needs the increments, which are
  produced by integrating the equation.

### Q5. `thm:qtime`: `eq:negativeinterp`, the Holder chain, `C_I`, and "no continuation norm"

**All correct, including the constant, and the no-continuation-norm claim is
TRUE.** This is the strongest result in the audited scope.

- **`eq:negativeinterp`.** `||f||_2^2 <= ||f||_{Hdot^-1} ||grad f||_2` (Fourier
  Cauchy-Schwarz on `|xi|^{-1}|fhat| * |xi||fhat|`), then `||f||_3 <=
  ||f||_2^{1/2}||f||_6^{1/2}` (`theta = 1/2`, confirmed) and `||f||_6 <=
  S||grad f||_2`. Assembling gives exactly
  `S^{1/2} ||f||_{Hdot^-1}^{1/4} ||grad f||_2^{3/4}`. Confirmed symbolically.
- **Chain.** `q(u_1)-q(u_0) = d - f` with `d = w(u_1)-w(u_0)`; `(a+b)^3 <=
  4(a^3+b^3)` (200000 random trials, 0 violations); `eq:holder` with `||w||_3 <=
  ||u||_3`; arithmetic `4*(6 X f^2 + 2 f^3) + 4 f^3 = 24 X f^2 + 12 f^3`;
  absorption into `36(||u_1||_3+||u_0||_3)||f||_3^2` via
  `||f||_3 <= ||u_1||_3 + ||u_0||_3`. All correct.
- `||u||_3 <= E_0^{1/4} S^{1/2} Y^{1/4}` and `a+b <= 2^{3/4}(a^4+b^4)^{1/4}`
  (200000 random trials, 0 violations) give the `2^{3/4} S^{1/2} E_0^{1/4} J^{1/4}`
  factor. `||grad f||_2 <= sqrt(2J)` from `(a+b)^2 <= 2(a^2+b^2)`.
- **`eq:qpairpoint` and `C_I`.** The product is
  `36 * 2^{3/4} * 2^{3/4} S^{3/2} E_0^{1/4} Omega^{1/2} J = 36 * 2^{3/2}
  S^{3/2} E_0^{1/4} Omega^{1/2} J`; then `int_0^{tau-h}(Y(t+h)+Y(t)) dt <= 2 B_u`
  gives `C_I = 72 * 2^{3/2} S^{3/2} E_0^{1/4} B_u`. Confirmed symbolically.
- **"No continuation norm occurs on the right side": CONFIRMED.** `C_I` depends
  only on `(S, E_0, nu)`; `Omega(h)` only on `(nu, S, E_0, h)`. Crucially the
  left side is `int_0^{tau-h}` with the bound **uniform in `tau`**, so this is a
  genuine endpoint-uniform statement of the kind `eq:Gtarget` demands -- just in
  the wrong time norm. This is the one place in the audited scope where the
  document delivers exactly what it advertises.
- **Independent criticality check (not in the document).** Under the
  Navier-Stokes scaling `u -> lambda u(lambda x, lambda^2 t)`, `||q||_3` is
  invariant, `dt -> lambda^{-2} dt`, so the left side scales as `lambda^{-2}`.
  Symbolic evaluation of `C_I Omega(h)^{1/2}` under `E_0 -> E_0/lambda`,
  `h -> h/lambda^2` gives exactly `lambda^{-2}`. **`eq:qtime` is
  scaling-consistent**, which is a nontrivial check on both terms of `Omega`
  simultaneously and on `C_I`. `hyp:temporal` is likewise scaling-covariant
  (`||r_delta||_3` invariant, `delta` transforming as a time), so it is a
  *critical* criterion, not a subcritical one.
- The asymptotic remarks (`O(h^{1/8})` for the right side, `O(h^{1/24})` for the
  `L^3_t` norm of the increment) are both correct.

### Q6. `cor:residualmeasure`: Jensen, Tonelli, the `(delta,tau)` restriction, Chebyshev

**Correct.**

- **Jensen.** For `t >= delta`, `r_delta(t) = (1/delta) int_0^delta (q(t)-q(t-s)) ds`,
  and Jensen for `x -> x^3` against the probability measure `ds/delta` gives
  `||r_delta(t)||_3^3 <= delta^{-1} int_0^delta ||q(t)-q(t-s)||_3^3 ds`. Correct
  (Minkowski first, then Jensen on the scalar average).
- **Tonelli.** The integrand is nonnegative and jointly measurable
  (`q in C(L^3)` on compact classical intervals), so the interchange is legal.
  After `t' = t - s` the inner integral runs over `(delta-s, tau-s) subset
  (0, tau-s)`, which is precisely the interval `thm:qtime` controls at `h = s`.
  Correct.
- **Monotonicity.** `Omega` is increasing, so `(1/delta) int_0^delta
  Omega(s)^{1/2} ds <= Omega(delta)^{1/2}`. The first bound is strictly sharper
  (by a factor near `8/9` in the `h^{1/4}`-dominated regime); the document keeps
  both, correctly.
- **Chebyshev.** `|{||r_delta||_3 > nu/(4 C_sharp)}| <= (4 C_sharp/nu)^3
  int ||r_delta||_3^3`. The cube matches the cube on the left of
  `eq:residualintegrated`. Correct.
- **The `(delta, tau)` restriction is necessary, not stylistic.** For `t < delta`
  the average contains the frozen value `q(0)`, and the Jensen bound would
  require the *fixed-time* quantity `||q(t)-q(0)||_3^3`, which no increment
  integral over `t` controls. The document's sentence "no unstated estimate on
  negative-time increments or on an unknown initial lifespan is used" is exactly
  right, and I could not find any place where the restriction is later forgotten
  *inside* the corollary. It **is** partially forgotten in Section 9.1: see Q7
  and R3.

### Q7. The gap itself, and the honesty of `eq:badremainderintegral`

**`eq:badremainder` and `eq:badremainderintegral` are both correct and honest.
The no-mechanism paragraph is correct. Two precision defects (R3, R4).**

Re-derivation: `C_sharp ||r_delta||_3 D <= (nu/4) D + C_sharp 1_{B_delta}
||r_delta||_3 D` (on `B_delta^c` the first term dominates by definition of
`B_delta`), the averaged term costs `(nu/4)D + M_delta Q` as in `thm:temporal`,
so `Q' + (nu/2) D <= M_delta Q + C_sharp 1_{B_delta} ||r_delta||_3 D`. Gronwall
with `e^{-M t} <= 1` on the source gives `eq:badremainderintegral`. Correct.

**What precisely stands between the integrated bound and the criterion.** The
document says "an integrated bound, not the supremum" and "the gap is the
dissipation accumulated on the exceptional set". Both are right but understate
the structure. The precise statement is:

1. The unbounded object is not `D` on a small set, it is the **product**
   `1_{B_delta} ||r_delta||_3 D`, in which the weight `||r_delta||_3` is
   unbounded exactly where the indicator is 1. Measure smallness of `B_delta`
   therefore does not even reduce the problem to controlling `D`.
2. `D` is **not a priori integrable in time at all**. `int_0^tau D` is precisely
   the quantity `thm:temporal` produces; unconditionally, `eq:balance` gives
   `Q(tau) + nu int D = Q_0 + int K`, so `int D` is bounded only once `int K`
   is. Hence no Holder pairing can work: with the two available time budgets --
   `int ||q||_3^4 <= 8 S^2 E_0^2/nu` (`eq:qbudgets`, so `||r_delta||_3 in L^4_t`
   with an input bound) and `int_delta^tau ||r_delta||_3^3 <= C_I
   Omega(delta)^{1/2}` (`cor:residualmeasure`) -- closing the pairing would need
   `D in L^{4/3}_t` or `D in L^{3/2}_t` respectively, and **neither is available,
   even conditionally**.
3. The only pairing that does close is `sup_{B_delta} ||r_delta||_3 * int_{B_delta} D`,
   i.e. exactly the `L^infty`-in-time control that `hyp:temporal` postulates.
   So the gap is not "integrated vs supremum" as a matter of taste: the
   supremum is the *unique* exponent at which the available `int D` (itself
   conditional) suffices.
4. Absolute continuity of the integral does not rescue it. For a fixed classical
   branch and fixed `tau < T*`, `D` is continuous on `[0,tau]`, so
   `int_{B_delta} D -> 0` as `|B_delta| -> 0`. But the modulus of that
   convergence depends on the solution, and it degenerates as `tau -> min{H,T*}`.
   The needed statement is uniform in `tau` and across data; nothing supplies it.

The document's own list -- "No reverse Holder estimate in time, no such
uniform-integrability statement, and no signed cancellation for this remainder
has been proved here" -- is **correct and, as far as I can construct, complete**.
I attempted all four closures above and each fails for the stated reason.

Two precision defects:

- **R3.** `B_delta` in Section 9.1 is defined on all of `[0, tau]`, but
  `cor:residualmeasure` controls only `B_delta cap (delta, tau)`. The initial
  averaging layer `[0, delta]` contributes to the remainder in
  `eq:badremainderintegral` with **no** estimate whatsoever, not even a measure
  bound. The prose ("small in measure away from the initial averaging layer")
  is technically honest but a reader will carry the measure bound into
  `eq:badremainderintegral` where it does not apply on `[0,delta]`.
- **R4.** "Arbitrarily high dissipation can in principle concentrate on sets of
  arbitrarily small time measure" is loose. On any compact `[0,tau] subset
  [0,T*)`, `D` is continuous (by `eq:Alip` and classical regularity) hence
  bounded, so no such concentration occurs at fixed `tau`. The genuine failure
  is the absence of a bound uniform in `tau` and in the datum.

One further honest-but-worth-flagging point: `eq:badremainderintegral` is not a
closed estimate, because `D` appears on both sides. Alternative (ii) of
`thm:fullconditional` ("a finite input bound for the remainder") is therefore,
by the same argument as Proposition B, also equivalent to the target -- a
regular branch has `sup Y < infinity`, hence by Proposition A a `delta` making
`B_delta` **empty** and the remainder exactly `0`. The same holds for
alternative (iii). All three alternatives in `thm:fullconditional` are
equivalent to the conclusion. Section 1.3 anticipates this in general terms;
Section 9.2 does not repeat it.

### Q8. `cor:modulus`, and the scalar/vector distinction

**Correct, and correctly distinguished.**

- The proof is airtight. `r_delta(t) = (1/delta) int_{t-delta}^t (q(t)-qtilde(s)) ds`,
  Minkowski, and then two cases: for `s >= 0`, `|t-s| <= delta` and monotonicity
  gives `omega(delta)`; for `s < 0` (which occurs only when `t < delta`) the
  compared pair is `(t, 0)` with separation `t < delta`, again `<= omega(delta)`.
  So `||r_delta(t)||_3 <= omega(delta)` for **all** `t`, including the initial
  layer. The one-sentence proof is complete; I could not break it.
- The hypothesis is stronger than needed (a modulus for all pairs, where only
  pairs within `delta` and the pairs `(t,0)` are used). Harmless.
- **Scalar vs vector.** `eq:scalarvector` (`|d(t)-d(s)| <= ||q(t)-q(s)||_3`,
  `d = ||q||_3`) is the reverse triangle inequality and is correct; the converse
  fails. So the vector modulus **implies** the scalar one, i.e. the scalar
  statement is strictly weaker, exactly as the document says. Section 7's
  concentrating curve makes the gap non-vacuous: constant `d(t)` with
  `G -> infinity`. The final sentence of Section 5 ("A modulus for the scalar
  function `t -> ||q(t)||_3` is a different and weaker statement") is correct as
  stated.
- Caveat that should be recorded (R2): `cor:modulus` requires the modulus on
  `[0, min{H,T*})`, so it is itself a continuation hypothesis, and by
  Proposition A the only known source of such a modulus is `sup_t Y < infinity`.
  `cor:modulus` is therefore *the* place where the circularity becomes visible,
  and the document presents it as a strengthening route rather than as the
  equivalence it is.

### Q9. Relation to Ladyzhenskaya-Prodi-Serrin, Beirao da Veiga, and HF25

**Plainly: `hyp:temporal` is NOT weaker than the literature. It is implied by
the classical criteria and, given the manuscript's own ESS import, equivalent to
them. This is the exact analogue of the earlier HF25 finding, and here it is
sharper because the implication needs no new machinery at all.**

- **vs. the `H^1` blow-up alternative.** By Proposition A,
  `sup_{t<min{H,T*}} ||grad u(t)||_2 < infinity  ==>  hyp:temporal`,
  by an elementary, fully quantitative argument that uses only the document's
  own `lem:negativeincrements`, `eq:negativeinterp`, the `thm:qtime` chain, and
  `cor:modulus`. So `hyp:temporal` is a **weakening** of the manuscript's own
  local-package continuation criterion. By Proposition B it is in fact
  **equivalent** to it. This is the same status the earlier HF25 audit assigned
  to `hyp:highstrain`.
- **vs. LPS / BdV.** Every admissible LPS pair (`u in L^p_t L^q_x`,
  `2/p + 3/q = 1`, `q > 3`), the ESS endpoint `L^infty_t L^3_x`, and every BdV
  pair (`grad u in L^p_t L^q_x`, `2/p + 3/q = 2`, `q > 3/2`) implies regularity
  on `[0,H]`, hence `sup Y < infinity`, hence (Proposition A) `hyp:temporal`.
  Conversely `hyp:temporal` implies regularity (Proposition B), hence all of
  those norms are finite. **All are logically equivalent as continuation
  criteria for the maximal classical branch.** `hyp:temporal` is not weaker in
  any non-vacuous sense; the honest description is "a different observable on
  the same equivalence class", which is precisely the wording the HF25 audit
  reached (its R3).
- **vs. HF25's `int ||div w||_2^4 dt < infinity`.** Here I found something the
  document does not state, and it is the cleanest structural fact in the scope.
  **Auditor's Proposition C.** Apply `lem:T6` directly with `g = q` (no
  averaging) and Young at `eps = nu/2`:
  ```
  Q' + (nu/2) D <= (81/8) C_{9/2}^4 a_0 nu^{-3} ||q||_6^4 Q
               <= (729/64) C_{9/2}^4 S^6 nu^{-3} ||sigma||_2^4 Q,
  ```
  using `||q||_6 <= S ||grad q||_2 = S ||div w||_2 = S ||sigma||_2` from
  `eq:divcurl`. This **is** HF25's `thm:sigmacriterion`, re-derived from HF26's
  own Lemma 5.1 in two lines. Consequently:
  - HF26 Section 5 is *not* a new mechanism relative to HF25. It is HF25's
    criterion with the unavailable factor `||q(t)||_6` replaced by the
    time-averaged surrogate `||qbar_delta(t)||_6 <= L_delta`. The trade is
    exact and visible in the constants: energy gives
    `int ||q||_6^2 dt <= S^2 E_0/(8 nu)` (an `L^2_t` bound), `L_delta^2` is
    literally that budget divided by the window `delta` plus the frozen initial
    term, and `M_delta ~ delta^{-2}` is the price. HF25 needed `L^4_t`; HF26
    buys `L^infty_t` of the average from the available `L^2_t`, and pays with
    `hyp:temporal` on the residual.
  - HF25's hypothesis implies HF26's conclusion **without** `hyp:temporal`
    (Proposition C + Gronwall + `eq:coercivity`). So the two hypotheses are
    equivalent to each other and to regularity.
- **Bonus, offered as a lead only.** Proposition C settles the HF25 audit's
  open question "whether a trajectory with `int Y^2 = infinity` but
  `int ||sigma||_2^4 < infinity` exists": **no**, on the maximal classical
  branch. If `int_0^{min{H,T*}} ||sigma||_2^4 dt < infinity` then Proposition C
  bounds `sup Q`, hence `sup ||u||_3`, hence (ESS) `T* > H`, hence
  `sup_{[0,H]} Y = Lambda < infinity`, hence `int_0^H Y^2 <= H Lambda^2 <
  infinity`. This rests on the ESS import and on `eq:divcurl` (an HF23 result
  audited elsewhere, not re-audited here), so it is a lead for the HF25 open
  queue, not a promotion.

---

## Required repairs

Numbered R1..R6. R1 and R2 are blocking for any use of Section 5 as a
"producer"; R3-R6 are precision repairs.

**R1 (blocking). `hyp:temporal` must state its own logical status.** The clause
"justified without an endpoint continuation norm" is a meta-condition on a
future proof, not a condition on `delta`, and it is not enforceable: `T*` and
`Lambda = sup_{t<min{H,T*}} Y(t)` are functions of `(nu,u_0)`, so a `delta`
chosen from `Lambda` literally satisfies the quantifier. Move the clause out of
the numbered Hypothesis into surrounding prose, and add to the Hypothesis a
remark of the following content:

> The quantity assumed small in `eq:residualsmall` is a supremum over
> `[0, min{H,T*})` and is therefore itself an endpoint continuation norm. By
> `lem:negativeincrements`, `eq:negativeinterp` and `cor:modulus`, finiteness of
> `sup_{t<min{H,T*}} ||grad u(t)||_2` implies this hypothesis with an explicit
> scale; combined with `thm:temporal` and the ESS endpoint import, the
> hypothesis is *equivalent* to `T* > H`. Like every other member of that class
> it therefore supplies no logical reduction of the target; its value is the
> explicit constants and the new observable, not a weakening.

**R2 (blocking). Same disclosure for `cor:modulus` and for the closing
paragraph of Section 5.** The corollary requires the vector modulus on the whole
interval up to `min{H,T*}`, and the only known source of such a modulus is the
`H^1` bound. State that. The sentence "This theorem does not require the
magnitude of `q` itself to be small" is true but, unaccompanied, invites the
reading that the hypothesis is cheaper than an endpoint norm.

**R3. Section 9.1: flag the initial layer explicitly.** `B_delta` is defined on
`[0,tau]`; `cor:residualmeasure` bounds only `|B_delta cap (delta,tau)|`. Add
one sentence saying that the contribution of `B_delta cap [0,delta]` to
`eq:badremainderintegral` carries no estimate at all, not even a measure bound.

**R4. Section 9.1: correct "arbitrarily high dissipation can concentrate on
sets of arbitrarily small time measure".** On each compact `[0,tau] subset
[0,T*)`, `D` is continuous and bounded, so this cannot happen at fixed `tau`.
Replace with: "no bound on this remainder that is uniform in `tau` and in the
datum is available; the fixed-`tau` absolute continuity of `int D` degenerates
as `tau -> min{H,T*}`."

**R5. Sharpen the statement of the gap.** Add to Section 9.1 the exponent
argument: the two available time budgets are `||r_delta||_3 in L^4_t`
(`eq:qbudgets`) and `||r_delta||_3 in L^3_t` on `(delta,tau)`
(`cor:residualmeasure`); closing the pairing by Holder would need `D in L^{4/3}_t`
or `D in L^{3/2}_t`, and unconditionally not even `D in L^1_t` is available,
since `int D` is the quantity being produced. The `L^infty_t` exponent of
`hyp:temporal` is thus the unique one at which the conditional `int D` suffices.

**R6. Add the comparison to HF25 and to the classical line.** Section 5 or the
ledger must record Proposition C: `lem:T6` applied directly to `g = q`, with
`||q||_6 <= S||sigma||_2`, reproduces HF25's `thm:sigmacriterion`; Section 5 is
that criterion with `||q||_6` replaced by the `delta`-averaged surrogate
`L_delta`. Record also that `hyp:temporal` is implied by every LPS/BdV/ESS
criterion and by HF25's hypothesis, and is equivalent to all of them. The
ledger currently says only "It also makes no claim that the temporal criterion
is the first criterion of its kind", which does not cover the implication
direction.

### Controller (index note) corrections

**C1.** The FIRST GAP line -- "the gap is precisely the dissipation accumulated
on a small-measure exceptional set" -- is imprecise in two ways. The unbounded
object is the `||r_delta||_3`-**weighted** dissipation (the weight is unbounded
exactly on that set), and the measure bound holds only on `(delta,tau)`, so the
initial layer `[0,delta]` is not covered at all. Suggested replacement: "the
`||r_delta||_3`-weighted dissipation on the exceptional set, whose measure is
controlled only away from the initial averaging layer, and against which no
time-integrability of `D` beyond the conditional `L^1` is available."

**C2.** Claim 3 of "What it claims" and the audit-questions bullet on
`thm:temporal` ask only "whether the scale is genuinely selected before the
stopping time rather than from a continuation norm". That is the right question
but it is the *second* question. Add the first: the hypothesis is itself a
supremum over `[0, min{H,T*})`, and it is equivalent to the `H^1` continuation
criterion. Without that, the note reads as if the only risk were in the
selection of `delta`.

**C3.** Claim 4 omits the two features that make `thm:qtime` valuable: the left
side is `int_0^{tau-h}`, and the bound is **uniform in `tau`**. That
endpoint-uniformity is the whole content; it should be stated.

**C4.** The note's "SURVIVING CONDITIONAL SUFFIX" presents the three
alternatives of `thm:fullconditional` as three routes. All three are equivalent
to the target (Proposition B and the remark in Q7). The note should say so, as
`PLAN.md`-adjacent framing depends on it.

**C5 (not an error, confirmed).** I recomputed the target SHA-256
(`24b5382...a540ab`) -- matches. Line count 1432 -- matches. All three pinned
revisions resolve: `a3e85f2d75fb01f1421e95f51ec6f8eedab0ec50` is a commit in
`navier` ("Import the HF25 continuation as an unaudited candidate"),
`34cdffd2fe2bd8a35068e96f907302e00c10850f` in `navier-paper`, and
`54f8e89119e90399044bae8dcd404dc405a381f9` in `navier-formal`. The controller's
hash claim is correct.

---

## Refutation attempts and outcomes

Nine genuine attempts; two succeeded (both against framing, not against the
mathematics), seven failed.

**A1. Construct a circularity in the constants of `thm:temporal`. FAILED.**
Traced `C_sharp`, `a_0`, `C_{9/2}`, `B_6`, `L_delta`, `M_delta`, `Q_0`, `C_3`,
`A_G` to their origins. Every one reduces to a universal constant or to
`(nu, u_0)` plus the free parameter `delta`. In particular `eq:averageL6` uses
only the time-integrated energy budget, never a supremum. The proof is clean.

**A2. Construct a circularity in `hyp:temporal`. SUCCEEDED.** Proposition A
(built entirely from the document's own Section 6 lemmas) shows the hypothesis
is implied by the endpoint `H^1` norm, and Proposition B upgrades that to an
equivalence with `T* > H`. The "input-selected `delta`" quantifier does not
block this, because `Lambda` is a function of the input. See Q1, R1.

**A3. Break the Young step or the constant assembly. FAILED.** `eq:Young34` is
sharp (the stationary point and value were computed symbolically);
`B_6^4 = 12 C_{9/2}^4 a_0`, `M_delta`, `C_sharp = (3/2)C_9 S`,
`C_I = 72*2^{3/2} S^{3/2} E_0^{1/4} B_u`, the Gronwall, and the `4/3` exponent
in `eq:temporalG` all reproduce exactly. No slack was smuggled in either
direction.

**A4. Find a hidden `L^2(q)` dependence in `eq:averageL6`. FAILED.** The
`L^6`-Bochner construction, the Jensen/Cauchy-Schwarz pair, and the Sobolev step
use only `q in L^6` and `grad q in L^2`, both supplied by `eq:divcurl`. The
`(delta-t)_+` bookkeeping for the frozen extension is correct. The ledger's
self-audit line on this point survives.

**A5. Close the exceptional-set remainder with the tools already in the
document. FAILED, and the failure confirms the document.** Tried four closures:
(i) Holder `L^3_t x L^{3/2}_t` using `cor:residualmeasure`; (ii) Holder
`L^4_t x L^{4/3}_t` using `eq:qbudgets`; (iii) `sup x int D`; (iv) absolute
continuity of `int D` against the measure bound. (i) and (ii) fail for want of
any super-`L^1` time integrability of `D`; (iii) is the hypothesis itself; (iv)
has a solution-dependent modulus that degenerates as `tau -> min{H,T*}`. The
document's "no reverse Holder, no uniform integrability, no signed cancellation"
is correct and appears complete.

**A6. Break `cor:modulus` at the negative-time seam. FAILED.** The `t < delta`
case compares `(t,0)` with separation `t < delta`; monotonicity of `omega`
covers it. The bound `||r_delta(t)||_3 <= omega(delta)` holds for all `t`
including the initial layer, so `cor:modulus` is strictly stronger than
`cor:residualmeasure` in reach. No seam.

**A7. Break `lem:negativeincrements` at the multiplier. FAILED.** The symbol of
`(-Delta)^{-1/2} P div` is `T -> P(xihat)(T xihat)`, with norm `<= 1` from
Frobenius to vector norm; `||u tensor u||_2 = ||u||_4^2`; both time Holder
exponents check. The `Hdot^{-1}` caution and the `2 pi` convention remark are
both correct.

**A8. Break `eq:qtime` by scaling. FAILED, and the check is a positive result.**
Both sides scale as `lambda^{-2}` under `u -> lambda u(lambda x, lambda^2 t)`
(verified symbolically on `C_I Omega(h)^{1/2}` with `E_0 -> E_0/lambda`,
`h -> h/lambda^2`). This simultaneously validates both terms of `Omega` and the
constant `C_I`. `hyp:temporal` is likewise scaling-covariant.

**A9. Show `hyp:temporal` is vacuous, or provable from energy alone. FAILED
both ways.** It is satisfied by `u_0 = 0` and, by Proposition A, by every
globally regular branch, so it is not vacuous. (Heuristically it should also
fail on Section 7's concentrating curve, whose `q(t) = lambda(t) q(W)(lambda(t)x)`
moves through mutually near-disjoint scales, so that `||q(t)-q(s)||_3 ->
2^{1/3} d_W` and `r_delta` stays of size `~ d_W`; I did not verify this, and the
curve is not a Navier-Stokes trajectory, so it is not evidence either way for a
branch.) It is not provable from energy: large `delta` makes `qbar_delta` small
but leaves `r_delta ~ q`, small `delta` needs precisely the modulus, and
`cor:residualmeasure` gives measure, never supremum. So it is a genuine extra
hypothesis -- one that happens to be equivalent to the conclusion.

**A10 (bonus, succeeded as a lead, not a refutation).** Proposition C:
`lem:T6` with `g = q` reproduces HF25's `thm:sigmacriterion`, and settles the
HF25 audit's open question negatively. See Q9.

---

## What I did NOT check

- Sections 1-4 (`sec:frontier`, `sec:foundations` beyond the displays consumed
  here, `sec:linear`, `sec:departure`), Sections 7 and 8 (`sec:crossing` beyond
  `eq:scalarvector`, `sec:curve`), Sections 9.2-9.3, the ledger, and all four
  appendices. In particular `thm:weightedresponse`, `thm:Aderivative`,
  `thm:NSdeparture`, `thm:curve`, `cor:curveenstrophy`, and the seed field `W_0`
  are untouched by this audit.
- The Section 2 inherited displays were re-derived only where consumed:
  `eq:Didentity` (I did verify `|grad V|^2 - (1/9)|grad|V||^2 = rho(|grad w|^2 +
  |grad rho|^2)` symbolically), `eq:Dcontrol` (`a_0 = (9/8)S^2` from
  `||V||_6 = ||w||_9^{3/2}`), `eq:gradA` (`A = |V|^{1/3} V`), `eq:Kq`,
  `eq:holder`, `eq:coercivity`, `eq:qbudgets`, `eq:u34`. I did **not** audit
  `eq:divcurl` (the HF23 import), `eq:workform`'s integration by parts and
  cutoff argument, `eq:balance`'s Banach chain rule, or Appendix
  `app:weighted`'s limiting identity. `eq:divcurl` in particular carries the
  whole `||grad q||_2^2 <= Y/4` step on which `L_delta` rests.
- The ESS endpoint import, GKP, and the local regularity package. Proposition B
  and the Q9 bonus both depend on ESS as imported by `thm:fullconditional`; I
  did not replay it.
- No Lean, no formal repository, no manuscript file, no `PLAN.md`. No graph node
  is promoted or changed by this audit, and no result in the audited scope is
  recommended for promotion in its current framing.
- I did not attempt to *prove* `hyp:temporal` for arbitrary data, and by
  Proposition B no such attempt short of the full target can succeed.

## Open Questions

- needs review: whether any route to an input-selected `delta` exists that does
  not pass through `sup_{t<min{H,T*}} ||grad u(t)||_2`. Proposition B says such
  a route would be a proof of the target, so this is the frozen gap restated,
  not a new sub-question.
- needs review: Proposition C's identification of HF26 Section 5 with HF25's
  `thm:sigmacriterion` was derived from `lem:T6` alone; the constant-level match
  with HF25's `C_sigma` and the identification of HF25's `D_Q` with HF26's `D`
  were not checked.
- needs review: the negative answer to HF25's open question (no trajectory with
  `int Y^2 = infinity` and `int ||sigma||_2^4 < infinity`) rests on the ESS
  import and on `eq:divcurl`; it should be re-derived by the HF25 lane before
  the HF25 open-question line is closed.
- needs review: `eq:divcurl`'s `||grad q||_2^2 = ||div w||_2^2 <= Y/4` is
  load-bearing for `L_delta`, `M_delta` and hence for every constant in
  `thm:temporal`; it is an HF23 import and was not re-audited here.
- needs review: Sections 7 and 8 are cited in Q8's scalar/vector conclusion only
  qualitatively; the concentrating curve itself is unaudited by me.
