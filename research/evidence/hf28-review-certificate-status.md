# HF28 audit: existential status of the discounted spectral certificate, the log-vs-quadratic crux, and the three dependency removals

Auditor lane: Sections 1--4 and 6--7 of the frozen candidate. Adversarial,
independent, source-metadata only.

## Freeze

- Candidate: `research/evidence/hf28-weighted-spectral-continuation.tex`,
  1078 lines, SHA-256
  `80c6b1339704261d5540ce9620e5799f0e9c9ea7c78cd1af412d075ea8699055`
  (recomputed here; matches the index note).
- The candidate's quoted attachment TeX hash
  `3898e9a0…1bf97488` is the SHA-256 of our own
  `hf27-critical-residual-continuation.tex` (recomputed here). The index note's
  claim that it "correctly hashes the HF27 artifact we hold" is confirmed.
- Nothing was edited outside this file. No commit, no push, no promotion.

## Scope

In scope (audited line by line, every constant recomputed):

- §1 target, imports and the one-display summary (`eq:mainintro`,
  `eq:HEintro`), lines 69--143;
- §2 conventions and the direct enstrophy continuation estimate
  (`lem:serrin`, `eq:energy`), lines 144--183;
- §3 the quotient dissipation without an unweighted div--curl premise
  (`lem:Qbasic`, `eq:naturaldistance`, `thm:natural`, `lem:transport`),
  lines 184--324;
- §4 the critical residual certificate with direct `H^1` continuation
  (`eq:constants`, `prop:relative`, `thm:certificate`), lines 325--468;
- §6 the weighted/discounted residual estimate (`lem:highpass`,
  `eq:weightedconstants`, `thm:weightedF`, `thm:onebudget`, `cor:log`),
  lines 522--648;
- §7 the single-horizon reduction (`lem:smallEY`, `thm:finitehorizon`,
  the scaling check), lines 649--701.

Verified as load-bearing inputs although formally another lane's (§5, lines
469--521): `prop:spectral`, `eq:FN`, `lem:weightedY`. §8 (`thm:complete`) was
read and used for context; I supply my own independent replacement for the
one direction of it that my verdict needs, so my determination does not rest
on another lane's result.

Out of scope: §5 as a whole, §8--§11 (conditional completeness, the
countermodel `thm:capped`, the handoff, both appendices), the prior-art
citations, the imported local package.

---

# VERDICT

**PASS WITH SCOPE.**

Every mathematical step in Sections 1--4 and 6--7 is correct. I attempted
eleven refutations of the estimates and all eleven failed; every displayed
constant reproduces exactly under independent symbolic recomputation
(`eq:constants`, `eq:weightedconstants`, `eq:betaoverk`, `eq:Fpoint`,
`eq:weightedF`, `eq:UN`/`eq:VN`, `eq:HEintro`, the scaling table). The two
new mechanisms — the natural-variable dissipation without `∇w`, and the
`1/N` discounted stress bound — are real and correctly derived.

The scope on the PASS is three-fold and it is severe.

1. **Existential status: the certificate is EQUIVALENT to global
   continuation.** It is the fifth member of the class, not a second escape.
   The `v = u` witness of `hf27-review-certificate.md` Proposition A is
   genuinely *unavailable* here — that structural difference is real — but
   equivalence is re-established by a different and cheap route (Proposition
   A below). At the quantifiers of `hyp:producer` (`eq:missing`), the boxed
   unproved statement **is Clay alternative A**, not a lemma towards it.

2. **The "arithmetic gap" is the whole problem, and the document's own
   framing of it is too generous to itself in one direction and too harsh in
   another.** Too generous: `sec:boundary` presents `eq:missing` as "the
   remaining sufficient statement", which invites the reading that a
   quantitative estimate is missing; it is the theorem. Too harsh: the
   quadratic bound `eq:crudea` is *not* the best available from the stated
   ingredients — the document's own `eq:specenergy` + `eq:weightedY` give an
   **`N`-uniform** bound on `a_N(H)` (finding F4 below).

3. **The certificate's currently verifiable region is exactly the region in
   which an elementary two-line argument already proves global regularity**,
   with the identical constant (finding F5). As of this note the certificate
   has zero verified content beyond `lem:serrin` + `eq:energy` applied
   directly to `u`. This is not a defect in a proof; it is the honest measure
   of what has been gained.

None of this makes any statement in my scope false. The document is unusually
honest — more honest than HF26 or HF27 were at the same stage — and it
explicitly states `eq:equivalence` and calls it "the exact logical strength of
the producer". What it does not do is take the last step and name that
strength.

---

# Q1. EXISTENTIAL STATUS, answered first

## Determination

> `hyp:producer` (`eq:missing`) is **logically equivalent to Clay alternative
> A**. The one-budget spectral certificate is in the existential-equivalence
> class, alongside HF25, HF24-B, HF26 and HF27. It does **not** escape by the
> HF24-A corridor mechanism, and it does not escape by any other mechanism.

The prompt's flagged structural difference is real and I confirm it: the
`v = u` witness is **not available**. In HF27 the certificate was a bare
existential over an unconstrained comparison class, so the solution itself was
a legal witness and the necessity direction was one line. Here the comparison
is *canonically determined* by `(N, u_0, ν)`: `v_N` solves `eq:spectral`, and
`a_N(H)` is a determinate function of the input alone. No member of the
witness class is the solution, and the certificate's testable quantity
genuinely contains no norm of `u`. Equivalence therefore has to be established
by a theorem rather than by substitution — and it can be.

## Proposition A (auditor's; forward direction is the document's, backward is mine)

> Fix `ν > 0`, a nonzero divergence-free Schwartz datum `u_0`, and
> `0 < H < ∞`. Let `u` be the selected maximal classical branch on `[0,T_*)`
> and let `v_N` be the global comparisons of `prop:spectral`. Then
>
> > `∃ N ≥ 1 : 𝔙_N(H) = K_∞ (κ_0/N) e^{β a_N(H)} < r_*²`
>
> **if and only if** `T_* > H`.

*Proof of (⇒).* This is `thm:onebudget` composed with `thm:certificate`,
audited below and correct. ∎

*Proof of (⇐), independent of §8.* Assume `T_* > H`. Then `[0,H]` is a compact
subinterval of `[0,T_*)`, so the imported local package gives
`Γ_j := sup_{[0,H]} ||u(t)||_{H^j} < ∞` for every `j`.

Write `d_N = v_N − u` and `θ_N = (I − J_N)u`, so
`(I − J_N)d_N = −θ_N` because `J_N v_N = v_N`. Subtracting `eq:NS` from
`eq:spectral` and testing with `−Δ d_N`, using that `J_N` and `ℙ` are
self-adjoint and that `−Δ d_N` differs from an element of `ran J_N ∩ ran ℙ`
by `Δθ_N`, one obtains on any interval where the bootstrap
`Y_N ≤ 2Γ_1²` holds

```
  (1/2) d/dt ||∇d_N||_2^2 + ν ||Δ d_N||_2^2
      ≤ C ||Δ d_N||_2 ( ||∇d_N||_3 ||v_N||_6 + ||d_N||_6 ||∇v_N||_3
                        + ||∇u||_3 ||d_N||_6 + ||u||_6 ||∇d_N||_3 )
        + C ( ||∇θ_N||_2 + ||Δθ_N||_2 ) ( 1 + Γ_2^2 + ||Δ d_N||_2 ) .
```

Under the bootstrap, `||v_N||_6 ≤ S(2Γ_1²)^{1/2}` and
`||∇v_N||_3 ≤ Y_N^{1/4}P_N^{1/4} ≤ (2Γ_1²)^{1/4} P_N^{1/4}`; absorbing every
`||Δ d_N||_2` by Young leaves a Gronwall inequality whose coefficient is
`c(Γ_1,Γ_2,ν)(1 + P_N^{1/2})`, and `∫_0^H P_N dt` is finite under the
bootstrap because `eq:specY` gives
`ν ∫_0^H P_N ≤ Y_0 + kν^{-3}·sup f_N^4 ·sup Y_N· H < ∞`. Since `u_0` is
Schwartz and `u ∈ C([0,H];H^{j})` for every `j`, Plancherel gives
`||∇d_N(0)||_2 + sup_{[0,H]}(||∇θ_N||_2 + ||Δθ_N||_2) ≤ C_ℓ N^{-ℓ}` for
every `ℓ ≥ 1`. Gronwall therefore returns
`sup_{[0,H]} ||∇d_N||_2 ≤ C(Γ,ν,H,ℓ) N^{-ℓ}`, which is `< Γ_1` for `N` large,
closing the bootstrap by first exit.

Hence `f_N = ||v_N||_6 ≤ ||u||_6 + S||∇d_N||_2 → ||u||_6` uniformly on
`[0,H]`, so

```
  a_N(H) ⟶ a_∞(H) := ν^{-3} ∫_0^H ||u(t)||_6^4 dt < ∞ .
```

Since `κ_0/N → 0` and `e^{β a_N(H)} → e^{β a_∞(H)} < ∞`, we get
`𝔙_N(H) → 0 < r_*²`, so some `N` works. ∎

This is an `H^1`-level replacement for §8's `H^{m≥3}` algebra argument; either
route suffices, and the conclusion is the classical fact that spectral
Galerkin flows converge on a regular interval. My verdict therefore does not
depend on another lane's audit of `thm:complete`.

## Corollary A1 — the boxed hypothesis is the Clay problem

`thm:finitehorizon` gives `T_* > H_E ⟹ T_* = ∞` for `u_0 ≠ 0`, and `u_0 = 0`
is global outright. Combining with Proposition A at `H = H_E`:

```
  hyp:producer  ≡  ∀ν>0 ∀u_0∈S_σ\{0} ∃N≥1 : eq:missing
                ⟺  ∀ν>0 ∀u_0∈S_σ : T_*(ν,u_0) = ∞
                ⟺  Clay alternative A  (with eq:energytarget supplied by eq:energy).
```

Both directions are proved; the equivalence is exact, not one-sided. There is
therefore **zero logical progress toward the target** in `eq:missing`, and
`sec:boundary`'s sentence "The requested terminal result remains blocked
specifically at `eq:missing`" is true only in the sense that a theorem is
blocked at itself.

## Why the HF24-A corridor escape is unavailable

`hf24-review-modulus-of-continuity.md` Proposition R1 escapes because the
corridor set `Corr` can be *vacated* near a singular time: alternative (ii)
there is a blow-up compatible with the hypothesis, because the hypothesis only
restricts `sup` over a set that the blow-up empties. Nothing in `eq:missing`
has that shape. `a_N(H_E)` is a finite integral of a globally defined smooth
`v_N`, defined for every `N` and every input, on a horizon fixed by `E_0`
alone; `κ_0`, `N`, `β`, `K_∞`, `r_*` are all determined before any solution is
mentioned. There is no set for a blow-up to vacate and no branch in which the
statement holds vacuously. Both branches are non-vacuous and Proposition A
closes them against each other.

## What *is* structurally new, stated precisely

Credit where due — this is materially better than HF27 and should be recorded:

- HF27's producer was equivalent **by trivial witness**; substituting the
  unknown solution satisfied it. Attempting to prove it was therefore
  circular in form.
- HF28's producer is equivalent **by theorem**, and is *non-circular in
  form*: it is a quantitative assertion about a canonical, always-defined,
  globally smooth family of nonlinear ODEs in a spectral space, mentioning no
  norm of `u`. One can attempt to prove it without presupposing what one is
  proving.

That is a genuine change of currency, and it is exactly what CCRT/Pham-style
a posteriori criteria provide; the document says so and claims no novelty for
it. The change of currency is not a change of logical strength.

---

# Q2. THE ARITHMETIC CRUX

## (0) The exact requirement, computed independently

`thm:onebudget` fires iff `K_∞ (κ_0/N) e^{β a_N(H)} < r_*²`. Taking
logarithms, with `r_N = N/κ_0 = Nν²/Y_0`:

```
  a_N(H)  <  (1/β) [ log(Nν²/Y_0) + log(r_*²/K_∞) ] .                (★)
```

This confirms the prompt's characterisation exactly: the certificate needs
`a_N(H)` at most **logarithmic in `N`**, with coefficient `1/β` and a fixed
negative offset. The requirement is affine in `log N`, so no polynomial bound
of any positive degree can satisfy it for large `N`.

Numerically, with the sharp Sobolev constant
`S = (π²/4)^{1/6}/(3π²/4)^{1/2} = 0.4272605…` (Aubin--Talenti extremal
`(1+|x|²)^{-1/2}`, recomputed here) and the most favourable admissible
multiplier constants `C_3 = C_{9/2} = C_9 = 1`:

| quantity | value |
|---|---|
| `k = 27S²/16` | `0.308056` |
| `β = 2c_b/3` | `898.29` |
| `δ = β − k` | `897.98` |
| `β/k` | `2916 = 36·3^4` exactly |
| `r_*` | `0.135234` |
| `r_*²` | `0.0182882` |
| `K_∞` | `0.238540` |
| `1/β` (a_N-budget per e-fold of N) | `1.113 × 10^{-3}` |
| `log(r_*²/K_∞)` | `−2.5683` |
| `N_min/κ_0 = K_∞/r_*²` | `13.04` |

So (★) is vacuous below `N = 13.04 κ_0`, and each `e`-fold of `N` above that
buys only `1.1 × 10^{-3}` nats of `a_N`. To certify a datum whose true value
is `a_∞(H_E) = 1` one needs `N/κ_0 > 10^{391}`. With `C_p = 2` the exponent
becomes `10^{3012}`. **The exchange rate between the `1/N` gain and the
`e^{βa_N}` amplification is catastrophically bad**, and this is a fixed
property of the constants, not of the data.

## (a) Is the `1/N` gain real and correctly derived? YES.

Recomputed end to end.

- `lem:highpass`: `||(I−J_N)G||_3² ≤ ||·||_2 ||·||_6 ≤ (N^{-1}||∇G||_2)·
  (S||∇G||_2) = (S/N)||∇G||_2²`. Correct; `|ξ|_∞ ≥ N ⟹ |ξ| ≥ N` outside the
  cube. `eq:dN` follows.
- `eq:Fpoint`: `|∇(v_N⊗v_N)| ≤ 2|v_N||∇v_N|`,
  `∫|v|²|∇v|² ≤ ||v||_6²||∇v||_3²`, `||∇v||_3² ≤ ||∇v||_2||∇v||_6 ≤
  S Y_N^{1/2}P_N^{1/2}`. Gives `4S²N^{-1} f_N² Y_N^{1/2}P_N^{1/2}`. Correct.
- `thm:weightedF`: substituting `Y_N ≤ Y_0 e^{k a_N}` and splitting the
  weight as `e^{-βa_N}e^{ka_N/2} = e^{-δ a_N}(e^{-k a_N})^{1/2}` is exact;
  Cauchy--Schwarz then meets `ν∫e^{-ka_N}P_N ≤ Y_0` (`eq:weightedY`) and the
  exact primitive `∫_0^H f_N^4 e^{-2δ a_N} = ν³(1−e^{-2δ a_N(H)})/(2δ)`
  (`eq:exacttimeintegral`; valid with flat pieces, no change of variables).
  Product: `(4S²√Y_0/N)·ν^{3/2}Φ·(Y_0/ν)^{1/2} = (4S²νY_0/N)Φ`. **Exactly
  `eq:weightedF`.** The bound is genuinely independent of `a_N(H)` because
  `Φ ≤ (2δ)^{-1/2}`.
- Assembly in `thm:onebudget`: `m(t) = c_b ν^{-3} f_N^4 = c_b a_N'(t)` so
  `M(t) = c_b a_N(t)` and the certificate weight `e^{-2M/3}` is *exactly*
  `e^{-β a_N}` with `β = 2c_b/3`. `Q_0^{2/3} ≤ 3^{-2/3}d_N² ≤ 3^{-2/3}SY_0/N`.
  Dividing `Z_H²` by `ν²` and using `κ_0 = Y_0/ν²` reproduces `eq:UN` and
  `eq:VN` verbatim. Correct.

The `1/N` is real. The `δ = β − k > 0` mechanism is real: the certificate's
own discount strictly dominates the enstrophy amplification rate, and
`eq:unweightedB` (also recomputed, correct) shows what is lost without it.

**But note the pin.** The `N^{-1}` rate is set by the *residual* term, not the
initial-error term. The initial-error term `d_N²` can be improved to
`S N^{-(2ℓ-1)}||∇^ℓ u_0||_2²` for any `ℓ` because `u_0` is Schwartz. The
residual term cannot: pushing `lem:highpass` to `ℓ = 2` needs
`||∇²(v_N⊗v_N)||_2² ≲ Y_N^{1/2}P_N^{3/2}`, and the weighted enstrophy budget
controls only the *first* power of `P_N`. So the log coefficient in (★) is
`1/β` and stays `1/β`; the tempting "get `m log N` for free" route is closed.
(Numerically the two terms in `K_∞` are `S = 0.427` from `Q_0` and
`16S²/√(2δ) = 0.069` from the residual — the initial error dominates the
*constant*, the residual pins the *rate*.)

## (b) Is the quadratic bound the best available? NO — the document concedes too much.

`eq:crudea` itself is correct: `Y_N ≤ 3N²E_0` on the cube,
`∫_0^H Y_N ≤ E_0/(2ν)`, so `a_N(H) ≤ (3S^4/2ν^4)N²E_0²`, `H`-independent.
(An alternative route through `||v||_6^4 ≤ S^4 E_0 P_N` and
`∫P_N ≤ 3N²E_0/(2ν)` gives the identical constant — a sign the quadratic
bound is a genuine ceiling of "energy + Fourier support".)

But two strictly better bounds follow from the document's own displayed
ingredients, both **uniform in `N`**, and the document states neither.

**F3 (short horizon, unconditional).** From `eq:specY` and `f_N^4 ≤ S^4Y_N²`,
`Y_N' ≤ kS^4ν^{-3}Y_N³`, hence for
`H < H_max := 8ν³/(27 S^6 Y_0²) = ν³/(2kS^4Y_0²)`

```
  a_N(H) ≤ −(1/2k) log(1 − H/H_max)      for every N .
```

So `𝔙_N(H) → 0` as `N → ∞` for every `H < H_max`, and the certificate
*unconditionally proves* `T_* ≥ H_max`.

**F4 (all horizons, small-data closure).** From `eq:specenergy` and
`eq:weightedY`,

```
  a_N(H) ≤ ν^{-3}S^4 (sup_{[0,H]} Y_N)(∫_0^H Y_N)
        ≤ c e^{k a_N(H)} ,      c := S^4 E_0 Y_0 /(2ν^4) ,
```

for every `N` and every `H`. If `c k e ≤ 1` the map `A ↦ ce^{kA} − A` has a
smallest root `A_-`, `a_N(0) = 0`, and `a_N(·)` is continuous, so a first-exit
argument gives `a_N(H) ≤ A_-` **for every `N` and every `H`**. The condition
is

```
  E_0 Y_0 / ν^4  ≤  32/(27 e S^6)  =  71.6696…
```

Hence for every such datum, `𝔙_N(H_E) < r_*²` for all `N` large, and
`eq:missing` holds. This is not quadratic, not logarithmic — it is bounded.

So the sentence "What energy and Sobolev supply is quadratic growth" is
accurate only if the enstrophy inequality `eq:specY` — which the document
proves two pages earlier — is excluded from "the stated ingredients". It
should not be.

One further correction of the document's own pessimism: `eq:crudea` is *not*
useless. Optimising (★) against the quadratic bound (the maximum of
`log y / y²` at `y = √e`) gives, in closed form, that `eq:crudea` alone
satisfies (★) whenever

```
  E_0 Y_0/ν^4  <  [ 2 e β · (3/2) S^4 (K_∞/r_*²)² ]^{-1/2}  =  4.907 × 10^{-3},
```

confirmed numerically by scanning `N`. Small, but nonzero. The claim "This
does not imply `eq:logtest`" is true as a general implication and false as a
statement about every datum.

## (c) Is the shortfall bridgeable in principle, or structural?

**Neither, in the sense the question suggests: the shortfall is the Clay
problem.** By Corollary A1 the required bound (★) at `H = H_E` is *true for
every datum if and only if* Clay alternative A is true, and if Clay-A is true
it holds with enormous margin, since `a_N(H_E) → a_∞(H_E) < ∞`, i.e. bounded
rather than merely logarithmic. Conversely `cor:log`'s `eq:lowerlog` says a
hypothetical blow-up before `H` forces `a_N(H) ≥ (1/β)log r_N + O(1)` for
*every* `N` — exactly logarithmic growth, no more.

Consequences, stated sharply:

- The gap is **not** an arithmetic shortfall that a sharper Sobolev or
  multiplier constant could close: sharpening constants moves `β`, `K_∞`,
  `r_*` and therefore the coefficient and offset in (★), but any proof of
  (★) for arbitrary data *is* a proof of the Clay problem. There is no
  intermediate result to aim at inside this formulation.
- The gap is **not** structural in the sense of "the inequality is false":
  it is true if and only if the conjecture is true, and no countermodel
  inside this formulation can exist unless NS-R3 blows up.
- The only honest description: the document has converted the Clay problem
  into a uniform-in-`N` Serrin bound for spectral Galerkin flows. That is a
  clean and non-circular reformulation, and it is a known one.

## Can the `1/N` gain ever beat the amplification?

**Yes — exactly when `T_* > H`, and never provably more than that.** Fixed
datum, fixed horizon: by Proposition A the two statements coincide. What can
be proved today, unconditionally, is F3 and F4 above, and that is *precisely*
what an elementary argument on `u` already gives (Q-crux finding F5, below).

---

# F5. The certificate's verifiable region is exactly the already-trivial region

This is the sharpest thing I found, and it is not stated anywhere in the
document.

Apply the F4 closure **directly to `u`** using only `lem:serrin`,
`eq:energy` and `eq:Sobolev` — all in the candidate, §2:

```
  a(t) = ν^{-3}∫_0^t ||u||_6^4 ≤ ν^{-3}S^4 (sup Y)(∫ Y) ≤ c e^{k a(t)} ,
  c = S^4 E_0 Y_0/(2ν^4) ,      Y(t) ≤ Y_0 e^{k a(t)} ,   ∫_0^{T_*} Y ≤ E_0/(2ν) .
```

If `cke ≤ 1`, i.e. `E_0Y_0/ν^4 ≤ 32/(27eS^6) = 71.67`, then `a ≤ A_-` on
`[0,T_*)`, so `Y ≤ Y_0e^{kA_-}` is bounded, so `T_* = ∞` by `eq:H1alternative`.

Compare the three thresholds, all in units of `E_0Y_0/ν^4` (sharp `S`):

| route | threshold | needs the certificate? |
|---|---|---|
| document's `lem:smallEY` at `t=0`, `1/(16S^6)` | `10.27` | no |
| elementary local time covers `H_E`, `1/(√54 S^6)` | `22.37` | no |
| **F4 closure, `32/(27eS^6)`** | **`71.67`** | **no** |
| certificate + F4 (the only unconditional route to `eq:missing` known today) | `71.67` | yes, but same set |
| certificate + `eq:crudea` | `4.9 × 10^{-3}` | yes, strict subset |

The certificate's currently provable firing set is `{E_0Y_0/ν^4 ≤ 71.67}`,
because F4 is the only `N`-uniform bound available and its condition is
*identical* to the condition under which the same two lines applied to `u`
already give `T_* = ∞`. Likewise F3's horizon `H_max = 8ν³/(27S^6Y_0²)` is
*exactly* the elementary `H^1` local-existence time obtained by integrating
`Y' ≤ kS^4ν^{-3}Y³`, so the short-horizon firing of the certificate
reproduces local existence and nothing more.

**Conclusion.** As a proved matter, the one-budget certificate currently
certifies no datum and no horizon that `lem:serrin` + `eq:energy` do not
already certify directly, with the same constants. Its value is entirely
prospective: it makes the target non-circular. That should be said in
`sec:boundary`.

---

# Per-question findings

## Q3. The single-horizon reduction (`lem:smallEY`, `thm:finitehorizon`)

**Verified correct.** Recomputed:

- `(1/2)Y' + νP ≤ ||u||_3||∇u||_6||Δu||_2 ≤ S||u||_3 P` (Hölder `1/3+1/6+1/2`;
  `||∇u||_6 ≤ S||∇²u||_2 = S||Δu||_2` by Plancherel for the full Hessian).
- `||u||_3 ≤ ||u||_2^{1/2}||u||_6^{1/2} ≤ S^{1/2}(EY)^{1/4}`, so
  `S^{3/2}(EY)^{1/4} ≤ ν/2 ⟺ EY ≤ ν^4/(16S^6)`, giving `Y' + νP ≤ 0`.
- The first-exit step is sound: on `[t_0,t_1]` both `E` and `Y` are
  nonincreasing, so `E(t_1)Y(t_1) ≤ E(t_0)Y(t_0) <` threshold, contradiction.
- `∫_0^{H_E}Y ≤ E_0/(2ν)`; mean value gives `t_0` with
  `Y(t_0) ≤ E_0/(2νH_E) = ν^4/(32S^6E_0)`; with `E(t_0) ≤ E_0` this is
  `ν^4/(32S^6)`, a strict factor-2 margin. Correct.
- `H_E = 16S^6E_0²/ν^5` has dimension of time (`S` is dimensionless).

**`S` is genuinely a fixed Sobolev constant.** `eq:Sobolev` is the scalar
`||f||_6 ≤ S||∇f||_2` on `ℝ³`; the extension to vectors and tensors via `|f|`
and `|∇|f|| ≤ |∇f|` a.e. is valid, so the same numerical `S` serves for
`u`, `∇u` and `v_N⊗v_N`. Nothing in `H_E` depends on the datum beyond `E_0`.
The sharp value is `S = 0.4272605…`, so `16S^6 = 0.09734`.

**Scaling verified.** Under `u_λ(t,x) = λu(λ²t,λx)`:
`E_0 ↦ λ^{-1}E_0`, `Y_0 ↦ λY_0`, `κ_0 ↦ λκ_0`, `H_E ↦ λ^{-2}H_E`,
`T_* ↦ λ^{-2}T_*`, `N ↦ λN`; `N/κ_0` and `a_N(H)` are invariant
(`||v||_6^4 ↦ λ²||v||_6^4` against `dt ↦ λ^{-2}dt`). The logarithm in
`eq:logtest` is of a dimensionless ratio. Correct, including the honest caveat
that the integer lattice is a testing convention.

**Repairable slack:** by F4, `lem:smallEY`'s threshold can be raised from
`1/(16S^6)` to `32/(27eS^6)`, a factor `6.976`, from the document's own
ingredients; `H_E` then shrinks by the same factor to
`(27e/32)S^6E_0²/ν^5 = 2.293 S^6E_0²/ν^5`. A shorter horizon is strictly
better for the certificate (it lowers `a_N(H_E)`). See R3.

## Q4(a). Continuation without the endpoint `L³` theorem — **REAL removal**

HF27 (`hf27-critical-residual-continuation.tex`, lines 85--90, 393) reached
its conclusion through the imported `L^∞_t L^3_x` endpoint continuation, which
the manuscript proves via Leray--Hopf + **Escauriaza--Seregin--Šverák** + a
Serrin estimate. HF28 replaces this in `thm:certificate` Steps 4--5:

1. Step 4 integrates `eq:QODE` to `τ < min(H,T_*)` and keeps the dissipation:
   `(ν/4)∫D ≤ Q_0 + M(H)Z_H³ + (2·3^{1/3}/ν)Z_H||F||²_{L²L³}`, τ-uniform.
   Verified.
2. `eq:eSerrin`: `||e||_6^4 ≤ ||e||_3||e||_9³` (interpolation exponent
   `θ = 1/4`, verified), then `||e||_3 ≤ 3^{1/3}C_3 Z_H` and
   `||e||_9³ ≤ C_9³||w||_9³ ≤ C_9³a_0 D`. Verified.
3. `e ∈ L^4_tL^6_x` up to the endpoint; `v_N ∈ L^4_tL^6_x` by smoothness on a
   compact; `(x+y)^4 ≤ 8(x^4+y^4)`.
4. `lem:serrin` (Gronwall) + `eq:energy` + `eq:H1alternative` closes.

The replacement import is the `H^1` maximal-development alternative, which
comes from the local `H^1` theory alone (Tao Thm 5.4 / Cor 5.8) and is not
where ESS enters. `L^4_tL^6_x` is a *non-endpoint* Serrin condition
(`2/4 + 3/6 = 1` with `q = 6 > 3`), and the non-endpoint case has the
elementary proof the document gives. **The dependency is removed, not
relocated: a deep theorem is replaced by an elementary Gronwall, and the
remaining import is strictly weaker than the one dropped.**

*Price paid:* the certificate must retain `∫D` (already available), and needs
the `L^9` bound `eq:w9` and the multiplier constant `C_9` — both already in
`eq:constants`, so no new import. I could not find a hidden cost.

*Circularity check (attempted refutation, failed):* Step 1 derives `eq:QODE`
only inside `{Q^{1/3} ≤ r_*ν}`; Step 2 derives `eq:timeZ` from it; Step 3
closes by first exit using continuity of `t ↦ 𝒬(e(t))` on `L³` and
`Q_0^{1/3} ≤ Z_H < r_*ν` (which holds since `M ≥ 0`). Standard, not circular.

## Q4(b). The quotient dissipation without an unweighted div--curl premise — **REAL removal**

Our audited HF23 (`hf23-divcurl-continuation.md`, PASS both scopes) supplies
`w ∈ L^6 ∩ W^{1,2}_loc`, `∇w ∈ L²`, `||∇w||_2² ≤ (5/4)Y`. HF28 §3 states it
does not use this, and I confirm that it does not.

Trace of the argument, all steps checked:

- `lem:Qbasic` is pure convexity: existence by reflexivity + weak lsc,
  uniqueness by strict convexity, `⟨A,g⟩ = 0` for `g ∈ 𝒢₃` hence `div A = 0`,
  differentiability from the Bregman sandwich `eq:Bregman` (both sides
  verified from `eq:monotone`/`eq:jLip` by segment integration), continuity of
  `w` and `A`, and `a = ℙw`, `||a||_3 ≤ 3^{1/3}C_3Q^{1/3}`,
  `||q||_3 ≤ c_q Q^{1/3}`, `𝒬(a) ≤ ||a||_3³/3`. No derivative of `w` anywhere.
- `thm:natural` Step 1 bounds `M_h = ∫δ_hA·δ_hw = ∫δ_hA·δ_ha =
  −∫A·δ_{-h}δ_h a` using translation invariance of `𝒢₃`; `A ∈ L^{3/2}`
  (`||A||_{3/2} = ||w||_3²`) and `a ∈ W^{2,3}` make this uniformly bounded.
  Then `(8/9)||δ_hV||_2² ≤ M_h` and `V ∈ L²` give `V ∈ H^1` by the
  difference-quotient characterisation. **`∇w` is never formed.**
- Step 2 differentiates only `f(z) = |z|^{1/3}z`, locally Lipschitz with
  `|Df| ≤ (4/3)|z|^{1/3}`; the weak chain rule + truncation gives
  `A ∈ W^{1,3/2}` and `eq:gradA`. No chain rule for `g` at `0` is claimed.
- Step 3's matrix identity is exact:
  `Df(z) = |z|^{1/3}(I + e⊗e/3)`, `Dg(z) = |z|^{-1/3}(I − e⊗e/3)`,
  `Df^T Dg = I − e⊗e/9` (verified symbolically, `(e⊗e)² = e⊗e`). Zero-set
  handling is via the Sobolev level-set property plus the two-point
  inequality, and the tails are handled by generalised (Pratt) dominated
  convergence with `L¹`-convergent majorants `2|δ_hV|²` — legitimate, since
  `δ_hV → ∂_kV` strongly in `L²`.
- `lem:transport`: `g(V)·∂_k f(V) = (4/3)V·∂_kV = (2/3)∂_k|V|²` (recomputed),
  so `∫w·(b·∇)A = (2/3)∫b·∇|V|² = 0`. Cutoff error `≲ ||b||_∞ R^{-1}∫_{|x|>R}|V|²
  → 0`. Correct.

*Price paid:* the route yields **no** information about `∇w` or about
`σ = −div w`. Anything downstream that needed HF23's `σ ∈ L²`, the Newtonian
potential representation, or the unconditional mixed-pressure pairing
`K_b = ∫σΠ_b` is unavailable from HF28's route. Within *this* continuation
nothing needs them, so the removal is complete here; it is a route-local
removal, not a replacement of HF23. The document says exactly this ("removes
an imported hypothesis used in the attachment's Appendix A"), which is
accurate.

## Q4(c). The direct enstrophy continuation estimate (`lem:serrin`) — **REAL, and it is the load-bearing one**

`lem:serrin` is what makes Q4(a) possible. Recomputed:
`(1/2)Y' + νP ≤ ||u||_6||∇u||_3||Δu||_2 ≤ S^{1/2}||u||_6 Y^{1/4}P^{3/4}`,
then Young `a x^{3/4} ≤ εx + 27a^4/(256ε³)` at `ε = ν/2` and doubling gives
`Y' + νP ≤ (27S²/16)ν^{-3}||u||_6^4 Y`, i.e. **`k = 27S²/16` exactly**. Both
Young constants were re-derived by maximisation (sympy) and match.

What it removes: the Ladyzhenskaya--Prodi--Serrin `L^4_tL^6_x` criterion is
here proved outright rather than imported, and the "no endpoint `L³` theorem
is involved" remark is justified. What is paid: nothing — this is a textbook
estimate with an explicit constant. It is correctly not claimed as novel.

## Q5. The two-point inequality and the constants

**`eq:naturaldistance` verified, both constants.** Writing `r=|x|`, `s=|y|`,
`c = cos∠(x,y)`: the middle expression is `r³+s³ − rsc(r+s)` and
`|V(x)−V(y)|² = r³+s³ − 2(rs)^{3/2}c`, both affine in `c`, so `c = ±1`
suffices — the document's reduction is valid.

- `c = 1`: `(r+s)(r−s)²` vs `(r^{3/2}−s^{3/2})²`. Lower bound from
  Cauchy--Schwarz on `(3/2)∫_s^r t^{1/2}dt`, giving `≤ (9/8)(r+s)(r−s)²`.
  Upper from `r^{3/2}−s^{3/2} ≥ √r(r−s)` and `r+s ≤ 2r`.
- `c = −1`: `(r+s)(r²+s²)` vs `(r^{3/2}+s^{3/2})²`. Lower from AM--GM
  `r+s ≥ 2√(rs)`; upper from `rs(r+s) ≤ r³+s³`, i.e. `(r−s)²(r+s) ≥ 0`.

Randomised check, `4×10^5` samples over 6 decades of scale: ratio range
`[0.88994, 1.05154]`, against the claimed `[8/9, 2] = [0.88889, 2]`. Both
bounds hold. **The lower constant `8/9` is sharp** (attained as `c→1`,
`s→r`). **The upper constant `2` is not sharp** — the true supremum is
`≈ 1.0516`, at `c = −1`, `s/r ≈ 0.17`. Harmless (it is used only as a
majorant in Step 3), but worth recording since the note says the constants
"are not optimized".

**`eq:constants` and `eq:weightedconstants` recomputed symbolically. All
correct.**

| claim | independent value |
|---|---|
| `a_0 = (9/8)S²` | as stated |
| `C_♯ = √2 C_9 a_0^{1/2}` | `= (3/2)C_9 S`; derived from Hölder `(3,9,18,2)` (sums to 1) and `||V||_6^{1/3} = ||w||_9^{1/2}` |
| `c_q = 3^{1/3}(1+C_3)` | correct from `q = (I−ℙ)w` |
| `b = √2·3^{1/4}a_0^{1/4}(1+2C_{9/2})` | correct; Hölder `(6,9/2,9,2)` (sums to 1 — note the document's text says "exponents `(6,9/2,9,2)`", which is right; `18` would not sum to 1) |
| `b^4 = 12a_0(1+2C_{9/2})^4` | `= 27S²(1+2C_{9/2})^4/2` ✓ |
| `27b^4/[256(ν/4)³] = c_bν^{-3}`, `c_b = 81a_0(1+2C_{9/2})^4` | `= 729S²(1+2C_{9/2})^4/8` ✓ both sides |
| `r_* = (4C_♯c_q)^{-1}` | consistent with `|K| ≤ νD/4` inside the bootstrap |
| `eq:Fbound` prefactor `√2·3^{1/6}` | `(4/3)√(9/8) = √2` ✓ |
| `β/k = 36(1+2C_{9/2})^4` | exact ✓ (so `δ > 0` since `C_{9/2} ≥ 1`, in fact `β/k ≥ 2916`) |
| `K_∞ = 3^{-2/3}(S + 16S²/√(2δ))` | reproduces `𝔘_N ≤ 𝔙_N` ✓ |

`eq:QODE`'s two Young steps at `ε = ν/4` were re-derived and give exactly the
stated `mQ` and `(2·3^{1/3}/ν)||F||_3²Q^{1/3}`. Step 2's regularisation
(`(2/3)(Q+ε)^{-1/3}`, integrating factor, `ε↓0`) is correct and the two
monotonicity claims used for `≤ Z_H²` hold.

**`prop:relative` is exact.** The subtraction, the disappearance of `ℙ` (from
`ℙA = A` and self-adjointness in `L^{3/2}`--`L³` duality), the three
integrations by parts (signs re-derived: `−∫A·(e·∇)e = +∫e·(e·∇)A`,
`−∫A·(e·∇)v = +∫v·(e·∇)A`, `−⟨A,ℙ div F⟩ = +∫∇A:F` with
`(div F)_i = ∂_jF_{ij}`, `(∇A)_{ij} = ∂_jA_i`), and the two applications of
`lem:transport` all check.

## Q6. The weighted/discounted residual estimate and "no independent stress bound remains"

**The claim is accurate as stated, and it is the document's real technical
contribution in my scope.** `thm:weightedF` bounds the *only* quantity that
the certificate needs from the stress, unconditionally, by
`4S²νY_0/(N√(2δ))` — no norm of `u`, no dependence on `a_N`, valid for every
datum, every `N`, every finite `H`. `eq:unweightedB` (verified) shows the
same computation without the discount carries an extra `e^{k a_N(H)}`, so the
remark "the certificate's discount defeats that cost because `β > k`" is
correct.

Two qualifications that `sec:weightedresidual` should carry:

- The removal is of an *independent* stress bound, not of the stress's
  influence: `a_N(H)` still governs the outer factor `e^{βa_N}` in `eq:VN`,
  and the document says so in §9. The abstract's "The stress residual is no
  longer an independent quantity to estimate" is precise; a reader skimming
  the boxed `eq:weightedF` could over-read it.
- **The gain and the loss come from the same constant.** `δ > 0` holds
  because `c_b` (hence `β = 2c_b/3`) is large; but `β` large is exactly what
  makes (★) hard, since the `a_N` budget is `1/β`. Sharpening `c_b` towards
  `(3/2)k` would make (★) easier by a linear factor while costing only
  `−(1/2)log(β−k)` in the offset through `K_∞ ∝ (2δ)^{-1/2}` — a strongly
  favourable trade that the document does not take. See R2.

---

# Required repairs

Numbered, in decreasing importance. None of these is a correction of a false
statement in my scope; R1 and R6 are missing determinations, R2--R5 are
improvements available from the document's own ingredients, R7--R8 are
presentational.

**R1. Name the logical strength of `eq:missing`.** `eq:equivalence` and the
remark at line 758--760 state the equivalence for a *fixed* datum and call it
"the exact logical strength of the producer". The one-line consequence is
never drawn: universally quantifying `eq:equivalence` over `(ν,u_0)` shows
`hyp:producer ⟺ Clay alternative A`. `sec:boundary` should say this
explicitly, in place of or beside "The requested terminal result remains
blocked specifically at `eq:missing`", which as written suggests a lemma is
missing. Recommended sentence: *"`eq:missing` is not a lemma towards
alternative A; by `thm:onebudget`, `thm:finitehorizon` and `thm:complete` it
is logically equivalent to it. What has changed is the currency, not the
strength: the target is now a non-circular statement about globally defined
comparison flows."*

**R2. Rebalance the Young parameters; `β` drops by a factor of 8.** In
`thm:certificate` Step 1 the cross term is absorbed at `ε = ν/4`. Taking
`ε = ν/2` for the cross term and `ν/8` for the residual (with `|K| ≤ νD/4`,
total `7ν/8 < ν`, so `νD/8` of dissipation is retained for `eq:integratedD`)
replaces `27b^4/[256(ν/4)³]` by `27b^4/[256(ν/2)³]`, giving

```
  c_b ↦ c_b/8 ,   β ↦ β/8 = 112.29 ,   β/k = 364.5 > 1 (δ > 0 preserved) ,
```

at the cost of doubling the residual coefficient (i.e. `16S² ↦ 32S²` in
`K_∞`, an offset change of about `log 2`). The `a_N` budget in (★) improves
eightfold, `1/β: 1.11×10^{-3} → 8.91×10^{-3}`, and the `N` needed to certify
`a_∞ = 1` falls from `10^{391}κ_0` to `10^{50}κ_0`. Further optimisation of
`c_b` towards `(3/2)k` is available on the same principle.

**R3. Raise `lem:smallEY`'s threshold and shorten `H_E` by a factor `6.976`.**
Replace the pointwise smallness argument by the closure of F4: from
`lem:serrin`, `eq:energy` and `eq:Sobolev` alone,
`a(t) ≤ c e^{k a(t)}` with `c = S^4E_0Y_0/(2ν^4)`; if `cke ≤ 1`, i.e.
`E_0Y_0/ν^4 ≤ 32/(27eS^6) = 71.67`, then `a` is bounded by the smallest root
and `T_* = ∞`. The document's `1/(16S^6) = 10.27` is a factor `6.976`
smaller. Consequently `H_E` can be replaced by
`H_E' = (27e/32)S^6E_0²/ν^5 = 2.293 S^6E_0²/ν^5`, which is strictly better
for the certificate because `a_N(H_E') ≤ a_N(H_E)`.

**R4. Correct §9's concession: energy and Sobolev do *not* only give
quadratic.** Add F3 and F4 to `sec:attempt`:
(i) `a_N(H) ≤ −(1/2k)log(1 − H/H_max)` for every `N`, with
`H_max = 8ν³/(27S^6Y_0²)`, unconditionally;
(ii) `a_N(H) ≤ A_-(E_0Y_0/ν^4)` for every `N` and every `H` whenever
`E_0Y_0/ν^4 ≤ 32/(27eS^6)`.
Both use only `eq:specenergy`, `eq:weightedY` and `eq:Sobolev`, all already
displayed. The current sentence "What energy and Sobolev supply is quadratic
growth" is true only if `eq:specY` is excluded from the ingredient list, which
would be arbitrary. This does not change the verdict on `eq:missing`, but it
changes what the countermodel of §10 has to defeat: the scalar budgets do
force an `N`-uniform bound in a nontrivial data range, so the countermodel's
scope statement should exclude that range explicitly.

**R5. State the honest content of the certificate (finding F5).** The set of
data for which the certificate is *provably* known to fire today is exactly
`{E_0Y_0/ν^4 ≤ 32/(27eS^6)}`, which is exactly the set on which the two-line
argument of R3 applied directly to `u` already gives `T_* = ∞`; and the
short-horizon firing region `H < H_max` is exactly the elementary `H^1`
local-existence time. `sec:boundary` should record that the certificate's
value is prospective (non-circularity of the target) rather than a proved
extension of the regularity class. Also record the positive complement:
`eq:crudea` *alone* does certify `E_0Y_0/ν^4 < 4.907×10^{-3}`, so
"This does not imply `eq:logtest`" should read "does not imply `eq:logtest`
for arbitrary data".

**R6. Record where the `N^{-1}` rate is pinned.** Add a remark: the initial
error `d_N²` can be improved to `O(N^{-(2ℓ-1)})` for every `ℓ` (Schwartz
datum), but the residual cannot, because `ℓ = 2` in `lem:highpass` requires
`||∇²(v_N⊗v_N)||_2² ≲ Y_N^{1/2}P_N^{3/2}` and `eq:weightedY` controls only the
first power of `P_N`. The coefficient of `log N` in (★) is therefore `1/β` and
cannot be raised by regularity of the datum. This forestalls an obvious and
wrong repair attempt.

**R7. `eq:naturaldistance`'s upper constant.** `2` is valid but the sharp
value is `≈ 1.0516` (attained at `c = −1`, `s/r ≈ 0.17`). If any downstream
constant is ever optimised, note that this one has a factor `1.9` of slack.
The lower constant `8/9` *is* sharp.

**R8. Front-matter precision.** "The proof also removes the unweighted
div--curl lemma and the endpoint `L³` theorem from this particular
continuation route" is correct, but the title page should add that the local
`H^1` theory and its blow-up alternative `eq:H1alternative` remain imported —
`thm:certificate` says so, the abstract does not.

---

# Refutation attempts and outcomes

Eleven genuine attempts. All failed to break a stated result; three produced
the findings above.

**A1. Break the equivalence: find regular data for which no `N` works
(would make the producer *stronger* than Clay-A).** FAILED. The `H^1`-level
bootstrap of Proposition A(⇐) closes for every regular horizon, giving
`a_N(H) → a_∞(H) < ∞` and `𝔙_N(H) → 0`. Independent of §8's `H^{m≥3}` route.

**A2. Find a corridor-style escape (a set a blow-up can vacate).** FAILED,
and provably so: every object in `eq:missing` is defined for every input
independently of `T_*`, and `thm:onebudget` closes the other direction. Both
branches are non-vacuous. This is the *only* known escape mechanism in the
programme and it does not apply.

**A3. Break the `1/N` gain by exploiting that `v_N⊗v_N` is band-limited in
`[-2N,2N]³`.** FAILED, and the alternative is worse: on the annulus
`N ≤ |ξ|_∞ ≤ 2N` one gets
`||(I−J_N)G||_3² ≤ 2√3 (S/N)||∇G||_2²`, a factor `2√3` *worse* than
`lem:highpass`. The document's route is the better one.

**A4. Improve the `N` rate to `N^{-(2ℓ-1)}` and buy `ℓ log N` of budget.**
FAILED. Only the initial-error term improves; the residual is pinned at
`N^{-1}` by the missing `∫P_N^{3/2}` budget (see R6). Recorded as a finding.

**A5. Find a sign or convention error in `prop:relative`.** FAILED. All four
integrations by parts, `ℙA = A`, the `L^{3/2}`--`L³` duality and
`−⟨A, ℙ div F⟩ = +∫∇A:F` re-derived independently with the document's index
conventions; all correct.

**A6. Find circularity in `thm:certificate`'s bootstrap (Steps 1--3).**
FAILED. The first-exit argument uses only continuity of `t ↦ 𝒬(e(t))` in
`L³`, `Q_0^{1/3} ≤ Z_H` (which holds because `M ≥ 0`) and strictness of
`Z_H < r_*ν`. `eq:QODE` is only ever used inside the region where it was
derived.

**A7. Break `thm:natural` at `V = 0` or at spatial infinity.** FAILED. The
zero set is handled by the Sobolev level-set property plus the two-point
inequality (both limits are `0`); the tails by generalised dominated
convergence with `L¹`-convergent majorants `2|δ_hV|²`, legitimate because
`δ_hV → ∂_kV` strongly in `L²`. The matrix identity `Df^TDg = I − e⊗e/9`
verified symbolically.

**A8. Show `thm:natural` secretly re-imports HF23 (`∇w ∈ L²`).** FAILED.
`M_h` is built entirely from difference quotients of `A` and `a`; `A ∈ L^{3/2}`
and `a ∈ W^{2,3}` suffice. No weak derivative of `w` appears anywhere in §3.

**A9. Show `thm:certificate` secretly re-imports ESS.** FAILED. The
replacement is `L^4_tL^6_x` (non-endpoint Serrin, `2/p+3/q = 1`, `q = 6 > 3`)
plus `lem:serrin`'s Gronwall plus the `H^1` blow-up alternative, which comes
from the local `H^1` theory, not from ESS. Genuine removal.

**A10. Show the two-point inequality fails somewhere.** FAILED. Analytic proof
re-derived at `c = ±1` (the affine reduction is valid), and `4×10^5` random
samples over six decades give ratios in `[0.88994, 1.05154] ⊂ [8/9, 2]`.
Byproduct: the upper constant is not sharp (R7).

**A11. Show the quadratic bound `eq:crudea` is the true ceiling, so the
document is right to concede.** FAILED — this is where F3, F4 and F5 came
from. Two `N`-uniform bounds follow from the document's own displayed
inequalities. This does not rescue `eq:missing` (nothing short of Clay-A can),
but it invalidates "energy and Sobolev give quadratic" as a description of the
ingredient set, and it produced the sharp statement that the certificate's
verifiable region equals the already-trivial region.

---

# Controller errors in the index note

`research/evidence/hf28-weighted-spectral-continuation.md`:

1. **"It states its own gap concretely, and the gap is arithmetic rather than
   conceptual."** — *Wrong, and it is the load-bearing error.* By the
   document's own `eq:equivalence` (and by Proposition A/Corollary A1 here),
   the gap `eq:missing` is logically equivalent to Clay alternative A. Calling
   it "arithmetic rather than conceptual" understates it by the entire
   problem, and it is in tension with the same note's later, correct
   instruction to decide the existential status first. Repeated verbatim in
   the Frontier record: *"FIRST GAP: stated by the document itself and
   arithmetic in form."*

2. **Omission: the note does not record that the document self-identifies as
   equivalence-class.** "What it claims" is silent on `thm:complete`,
   `eq:equivalence` and the remark at line 758 that names "the exact logical
   strength of the producer". This matters for the audit ledger, because
   HF26 and HF27 both had to be *repaired* for exactly this omission, and
   HF28 mostly does not need that repair — it needs only R1, the last
   quantifier step. The note's framing ("do not accept a disclaimer as an
   answer", "the kind of statement that has previously survived inspection of
   the proof while failing at the quantifiers") is good guidance but
   mis-describes this document, which concedes the point rather than
   disclaiming it.

3. **"What energy and Sobolev supply is quadratic growth."** — inherited from
   the document and, per F3/F4/R4, not the best available from the stated
   ingredients. The note repeats it as fact in both the observations and the
   Frontier record.

4. **"the audit should determine whether the shortfall is bridgeable in
   principle or structural"** — the dichotomy is false, and an audit that
   answered it as posed would answer wrongly. The shortfall is neither: the
   required inequality is true iff the conjecture is true (Corollary A1).

Verified correct in the note: the SHA-256 freeze (recomputed, matches); the
1078-line count; that the document correctly hashes our HF27 artifact
(recomputed, matches); the description of the `1/N` gain as coming from
retaining a discounted stress integral (confirmed, `thm:weightedF`); the
characterisation of the three dependency removals as removals rather than new
machinery (confirmed for all three); the statement that the document says
plainly the discounted estimate cannot fix the gap alone because the outer
amplification survives (confirmed, `sec:attempt`).

---

# What I did NOT check

- **§5 as a lane** (lines 469--521). I verified `prop:spectral`,
  `eq:specenergy`, `eq:FN` and `lem:weightedY` because §6 cannot be audited
  without them, and found them correct; I did not audit the `L^p`
  boundedness discussion of `J_N` or the Hilbert-space ODE construction in
  detail beyond confirming that nothing in my scope uses the `L^p` bound.
- **§8 `thm:complete`** as a proof. I read it, judged its structure sound,
  and then *replaced* the direction I needed with my own `H^1`-level argument
  so that my verdict does not depend on it. Its constants, the `H^{m-1}`
  algebra estimate `eq:product` and the bootstrap details belong to another
  lane.
- **§10 the countermodel `thm:capped`** — another lane. Note for that lane:
  R4 above means the countermodel must be checked to live *outside*
  `{E_0Y_0/ν^4 ≤ 32/(27eS^6)}`, since inside that range the scalar budgets do
  force an `N`-uniform bound on `a_N` and no logarithmically concentrating
  family satisfying `eq:cappedenergy` and `eq:cappedens` with a common datum
  can exist there.
- **§9's handoff table and §11's appendices** beyond the two claims that
  touch my scope (the `J_N` `L^p` non-use, which I confirmed for §§1--4, 6--7;
  and the reproducibility checklist, which I did not execute — the
  accompanying `check_weighted_spectral.py` is not in this repository).
- **Prior art.** CCRT, Pham, Diening--Kreuzer, Tao, ESS were not consulted;
  no third-party PDF was retained, per the task constraints. I verified only
  that HF27 (which we hold) used the ESS-backed endpoint statement and that
  HF28 does not.
- **The three pinned remote revisions** (`itpplasma/navier`,
  `navier-paper`, `navier-formal`) — not resolvable from this checkout, and
  no network contact was made.
- **Numerical values of `C_p = ||ℙ||_{L^p→L^p}`.** Every numeric table above
  uses `C_p = 1`, which is a lower bound (`ℙ` is a nonzero idempotent) and
  therefore the most favourable case for the certificate. Larger `C_p` makes
  `β` larger, `r_*` smaller and (★) strictly harder; the `C_p = 2` column of
  my computation is in the crux section.
- **The imported local package** and `eq:H1alternative` — explicit project
  imports, not re-derived.
- **No Lean, no formal check, no build.**

## Open Questions

- needs review: whether R2's rebalanced Young parameters interact with
  `eq:integratedD`'s retained dissipation in any way I have not traced —
  I checked only that `νD/8` survives, not that every downstream constant in
  `eq:eSerrin` and Step 5 is unaffected.
- needs review: the exact sharp constant in `eq:naturaldistance`'s upper
  bound (`≈1.0516`) if constant optimisation is ever undertaken.
- needs review (other lane): whether `thm:capped`'s countermodel family lies
  outside the `N`-uniform range `E_0Y_0/ν^4 ≤ 32/(27eS^6)` established in F4.
