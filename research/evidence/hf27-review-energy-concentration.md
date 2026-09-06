# HF27 audit — Section 6 (energy-level attempt), Section 7 (concentration test), Section 8 (completion boundary)

Independent adversarial audit. Nothing here promotes any result. No file other
than this one was created or modified; no commit, no push.

## 1. Scope

| Item | Value |
|---|---|
| Candidate (frozen, not edited) | `research/evidence/hf27-critical-residual-continuation.tex` |
| SHA-256 recomputed | `3898e9a020d31c4fc58c9f1289ea4794ec9f787b885086e411b98b0cb1f97488` — **matches** the index note |
| Lines audited | 673–863 (Sections 6, 7, 8) plus every earlier object they consume |
| Objects in scope | `prop:weakresidual`, subsection "What the same energy estimate gives in the needed norms" (`eq:crudeA`, `eq:crudeB`, `eq:missingpair`), `cor:necessary` (`eq:necessary`), `thm:concentration` (`eq:conccurve`–`eq:concstress`), `cor:weaksmall`, the Section 7 closing remark, and the Section 8 completion-boundary table |
| Consumed but not re-audited | `thm:certificate`, `cor:index`, `cor:direct`, `prop:Galerkin`, `thm:complete`, `thm:oscillation`, Appendix A, the constant dictionary |
| Method | Independent re-derivation of every displayed identity; `sympy` for exponents and constants; a 128³ spectral computation of an explicit residual profile; a bounded literature check of Nečas–Růžička–Šverák and Tsai |

## 2. Verdict

**REPAIR.**

No invalid step was found anywhere in Sections 6–8. Every algebraic claim I
checked is correct, and several are correct to the last constant. Two things
block a PASS:

1. **A prior-art defect that is worse than the one the controller anticipated.**
   `thm:concentration` is not merely "the same curve as HF26". Its curve *is*
   Nečas–Růžička–Šverák (1.2) / Tsai (1.2) verbatim under `a = 1/(2T)`; its
   `eq:profileR` *is* the Leray-projected Leray profile equation (1.3); and its
   choice `T = E_W/(4 nu Y_W)` *is* exactly the energy identity
   `nu ||grad U||_2^2 = (a/2)||U||_2^2` that every Leray profile must satisfy.
   The step the note proves at length ("It cannot be zero") is the contrapositive
   of NRS Theorem 1, a 1996 *Acta Mathematica* result, re-derived through a
   heavier and self-admittedly unverified import. The note contains **zero**
   occurrences of "self-similar", "Nečas", "Leray equation" or "Tsai".

2. **A genuine logical gap in the obstruction chain.** `prop:weakresidual`
   delivers smallness only for `s > 1`; `thm:concentration` and `cor:weaksmall`
   are stated only at `s = 1`. Homogeneous Sobolev spaces do not nest, so as
   written the obstruction does not refute an upgrade from the norm the note's
   own positive result actually controls. This is repairable in two sentences
   (R4) — the curve does work for all `1 < s < 5/2` — but it is not currently
   proved.

Everything else is disclosure and labelling. The mathematics survives.

---

## 3. The backward-self-similar prior-art question, answered first

### 3.1 The identification is exact, not analogous

NRS and Tsai both study (their (1.2), identical in the two papers)

```
u(x,t) = lambda(t) U(lambda(t) x),   p(x,t) = lambda(t)^2 P(lambda(t) x),
lambda(t) = 1/sqrt(2a(T-t)),   a > 0,
```

with profile equation (their (1.3))

```
-nu Lap U + a U + a (y.grad)U + (U.grad)U + grad P = 0,   div U = 0  on R^3.
```

Set `a = 1/(2T)`. Then `2a(T-t) = 1 - t/T`, so

```
lambda(t) = (1 - t/T)^{-1/2}   and   x/sqrt(2a(T-t)) = lambda(t) x.
```

`eq:conccurve` is therefore **not conjugate to** the NRS/Tsai ansatz; it is that
ansatz, in the same normalisation, with `U = W` and `a = 1/(2T)`.

Applying the Leray projection to (1.3) kills `grad P`, fixes `Lap U` and fixes
`Lambda U = U + (y.grad)U` (which is solenoidal when `U` is), leaving

```
-nu Lap U + a Lambda U + P((U.grad)U) = 0.
```

With `a = 1/(2T)` this is **character for character** the note's `eq:profileR`:

```
R_W = (1/(2T)) Lambda W + P((W.grad)W) - nu Lap W.
```

So `R_W` is the Leray-projected residual of Leray's 1934 profile equation, and
`R_W = 0` is precisely "`W` is a weak solution of (1.3)". The note's `eq:scaledR`,
`R_v(t,x) = lambda^3 R_W(lambda x)`, is the standard statement that the residual
of a self-similar curve is the profile residual transported by the scaling.

### 3.2 The note's choice of `T` is the Leray profile energy identity

I re-derived, independently of the note, `<Lambda W, W> = -E_W/2` in three
dimensions (from `int x_j d_j W_i W_i = -(3/2) int |W|^2`), and
`<P((W.grad)W), W> = 0` by `div W = 0`. Hence

```
<R_W, W> = -E_W/(4T) + nu Y_W,     which vanishes  iff  T = E_W/(4 nu Y_W).
```

Confirmed numerically to machine precision (`<R_W,W>/(||R_W||_2 ||W||_2) = -7e-17`)
on an explicit 128³ spectral computation with `W = curl(0,0,e^{-|x|^2/2})`, `nu = 0.7`.

NRS record on p. 291 that multiplying (1.3) by `U` gives exactly
`nu ||grad U||_2^2 = (a/2) ||U||_2^2`. With `a = 1/(2T)` that is
`nu Y_W = E_W/(4T)`, i.e. **`T = E_W/(4 nu Y_W)` — the note's tuning, verified
symbolically.**

Consequence for the reading of `thm:concentration`: the "exact unforced scalar
energy identity" `eq:conce` is not an incidental property of a cleverly tuned
curve. It is the statement that `W` satisfies **the one scalar identity every
Leray self-similar profile must satisfy**, imposed by choosing the single free
parameter `T`. And NRS's own paper is the canonical demonstration that this
identity is a *balance, not a rigidity*: it took the maximum principle for
`Pi = |U|^2/2 + P + a y.U` plus CKN-derived decay to get from that identity to
`U = 0`. The note's message — "exact energy balance does not control the
critical residual" — is a re-derivation, in a different currency, of the reason
Leray's 1934 question stayed open until 1996.

### 3.3 Does the note meet the citation requirement? **No.**

`grep -n -i "self-similar|selfsimilar|Necas|Tsai|Ruzicka"` over all 996 lines
returns nothing. The bibliography has eleven entries (Clay, Tao, ESS, CCRT,
Chemin–Gallagher, Stein, Brezis, and four repository records). Neither NRS nor
Tsai appears, and neither does the word "self-similar" anywhere in the prose.

The requirement was already established in this repository by
`research/evidence/hf26-review-countermodel-crossings.md` (its repair **R7**),
for the same curve with the same `lambda`, the same `T_c = E_W/(4 nu Y_W)` and
the same `Z = W + (x.grad)W`. HF27 reuses all three and cites neither. The
Section 7 closing remark distances the note from HF26's *seed* ("not claimed to
satisfy every scalar identity of HF26's more specially tuned curve"), which is
accurate about the choice of `W` and irrelevant to the ansatz.

This is a **prior-art defect**, and — because Section 1.4 is explicitly a
"Prior-art boundary" subsection that does creditable work on CCRT and
Chemin–Gallagher — an *asymmetric* one: the note is disciplined about the prior
art it noticed and silent about the prior art embedded in its own construction.

### 3.4 Do NRS/Tsai bear on the validity or the interpretation? **Both.**

**On validity — they make the note's longest sub-proof redundant.** NRS Theorem 1
(verbatim): *"Let U be a weak solution of (1.3) belonging to L^3(R^3). Then
U ≡ 0 in R^3."* The only hypotheses are: `U ∈ W^{1,2}_loc`, `div U = 0`, the
pressure-free weak formulation, and `U ∈ L^3(R^3)`. Decay is *derived*, not
assumed. A nonzero solenoidal Schwartz `W` satisfies all of these with room to
spare. The contrapositive is one line:

> `W` solenoidal Schwartz, `W != 0`  ⟹  `W` is not a weak solution of (1.3)
> ⟹ the Leray-projected residual `R_W != 0` as a distribution.

Tsai Theorem 1 gives the same for `W ∈ L^q`, `q ∈ (3, ∞]`, and Tsai Theorem 2
gives it under purely *local* energy estimates with no boundary condition.

The note instead proves `R_W != 0` by: assuming `R_W = 0`, invoking local
uniqueness to identify `v` with the selected classical branch, using constant
`||v||_3` and the imported endpoint theorem `eq:endpoint` to force `T_* > T`,
and contradicting `||grad v(t)||_2^2 = lambda Y_W -> infinity`. That argument
is **valid** — I checked each step and found no error — but it is the indirect
route, and it routes through `eq:endpoint`, whose primary source the note itself
flags as unverified ("The primary ESS PDF could not be fetched successfully in
this session"). Citing NRS would replace a dependence the note admits it could
not check with a directly checkable 1996 theorem. Keep the ESS route as the
second, self-contained argument, exactly as HF26's audit recommended.

**On interpretation — they make the construction unsurprising, though not
previously written down in this exact form.**

- Backward self-similar scaling is *exactly borderline* for every critical
  quantity, and log-divergence at the critical exponent is the textbook
  signature. For a self-similar `u`, `||u(t)||_3` is constant while the
  Ladyzhenskaya–Prodi–Serrin integral `int ||u(t)||_p^q dt` with `2/q + 3/p = 1`
  equals `int (T-t)^{-1} dt`: log-divergent. The note's `eq:lambdaints`
  (`int_0^tau lambda^2 dt = T log(T/(T-tau))`) is the same logarithm, for the
  residual instead of the velocity. This is the mechanism that defines Type I
  blow-up and saturates Leray's own lower bound
  `||u(t)||_p >= C (T-t)^{-(1-3/p)/2}`.
- The general arithmetic: for a forcing, the scaling-critical class is
  `L^r_t L^p_x` with `3/p + 2/r = 3`, and on that whole line the time integral is
  `int (1-t/T)^{-1} dt = +infinity`, while every strictly subcritical pair is
  finite. `eq:concstrong` (at `(p,r) = (3,1)` and `(3/2,2)`) and `eq:concweak`
  are two points and one subcritical point on that one-parameter picture.
- A literature check found **no** paper performing this exact write-up (arbitrary
  non-solution profile → self-similar curve → record that the residual's critical
  norms log-diverge while a subcritical one stays finite). That absence is weak
  evidence and must **not** be read as novelty: the computation is a few lines of
  the scaling that defines the problem. The search was also bounded — no general
  web search was available, and zbMATH/MathSciNet refused automated access.
- The nearest documented notion of "Leray profile equation carrying a residual"
  is **Scheffer's question**, recorded verbatim in Tsai's Remark 5.5: nontrivial
  solutions of `-nu Lap U + aU + a y.grad U + U.grad U + grad P = g` with a
  "speed-reducing" force, `U.g <= 0`. Tsai reports partial results and calls the
  general case open (as of 1998). **This is directly on point**: the note's
  tuning makes `<R_W, W> = 0` exactly, i.e. its residual sits precisely on the
  *boundary* of Scheffer's speed-reducing condition. A note whose entire Section 7
  is about the Leray profile equation with a nonzero residual should cite that.

**One caveat the note silently relies on.** Tsai Remark 5.4 exhibits nonzero
profiles with *zero* residual: `U = grad Phi` with `Phi` harmonic (any constant
vector included), `P = -|U|^2/2 - a y.U`. So "nonzero profile ⟹ nonzero residual"
is **false** without an integrability hypothesis. `thm:concentration` is safe
because `W ∈ S_sigma(R^3)`, but the note nowhere records that Schwartz-ness is
load-bearing here rather than merely convenient.

**One thing NRS/Tsai do *not* give.** They are Liouville theorems: `R_W != 0`
and nothing more. There is no quantitative lower bound on any norm of `R_W`, no
rate, no stability. The note needs only `R_W != 0`, so this costs it nothing —
but any future attempt to make `cor:weaksmall` quantitative at fixed data cannot
borrow from these papers.

---

## 4. Per-question findings

### Q(a) `thm:concentration` scaling, re-derived from scratch

All of the following were derived independently (not copied from the HF26
review) and cross-checked in `sympy`; the residual profile was additionally
computed spectrally on a 128³ grid.

| Claim in `thm:concentration` | Independent result | Status |
|---|---|---|
| `lambda' = lambda^3/(2T)` | `sqrt(T)/(2(T-t)^{3/2})` both sides | **exact** |
| `\|v\|_2^2 = lambda^{-1} E_W` | `\|v\|_p = lambda^{1-3/p}\|W\|_p`; `p=2` gives `lambda^{-1/2}` | **exact** |
| `\|grad v\|_2^2 = lambda Y_W` | `lambda^{4-3} Y_W` | **exact** |
| `eq:conce` energy identity | `d/dt(lambda^{-1}E_W) + 2 nu lambda Y_W = 0` iff `T = E_W/(4 nu Y_W)` | **exact** |
| `int_0^T lambda dt = 2T` | `2T` | **exact** |
| `R_v = lambda^3 R_W(lambda x)`, `R_W` as in `eq:profileR` | re-derived term by term from `v_t`, `(v.grad)v`, `Lap v`, using degree-zero homogeneity of `P` | **exact** |
| `R_W` solenoidal | `div(x.grad W) = div W + x.grad(div W) = 0` | **correct** |
| `R_W ∈ L^3 ∩ L^{3/2} ∩ Hdot^{-1}` | Schwartz terms are in `Hdot^{-1}` iff `d > 2` (the note's "in three dimensions" is exactly right); `\|P div(W⊗W)\|_{Hdot^{-1}} <= \|W⊗W\|_2` | **correct** |
| `R_W != 0` | valid via the note's ESS route; **also immediate from NRS Thm 1**; and confirmed numerically (`\|R_W\|_3 = 7.895` for an explicit `W`) | **correct** |
| `\|R_v\|_3 = lambda^2\|R_W\|_3`, `\|R_v\|_{3/2} = lambda\|R_W\|_{3/2}`, `\|R_v\|_{Hdot^{-1}} = lambda^{1/2}\|R_W\|_{Hdot^{-1}}` | `\|R_v\|_p = lambda^{3-3/p}\|R_W\|_p`; `\|f_lambda\|_{Hdot^{-s}} = lambda^{(3-2s)/2}\|f\|_{Hdot^{-s}}` | **exact** |
| `int_0^tau lambda^2 = T log(T/(T-tau))` | identical (sympy's branch-cut form agrees numerically) | **exact** |
| `int_0^T lambda^{2/3} = 3T/2` | `3T/2` | **exact** |
| `eq:concstrong`: both critical integrals `= infinity` | both reduce to `int_0^T lambda^2 dt` | **confirmed** |
| `eq:concweak`: `\|R_v\|^{4/3}_{L^{4/3}Hdot^{-1}} = (3T/2)\|R_W\|^{4/3}_{Hdot^{-1}}` | identical | **exact** |
| `v_t ∈ L^{4/3}(0,T;Hdot^{-1})` | `v_t = lambda^3 (Lambda W/(2T))(lambda x)`, same scaling | **correct** |
| `\|v(t)\|_3`, `\|q(v(t))\|_3` constant | `S_lambda f = lambda f(lambda.)` is an `L^3` isometry mapping `grad C_c^inf` onto itself, hence `G_3` onto `G_3`; so `w(S_lambda f) = S_lambda w(f)` | **correct** |
| `eq:concstress` (every `L^3` stress) | duality against `phi_lambda = (P psi)(lambda .)`, `\|grad phi_lambda\|_{3/2} = lambda^{-1}\|grad phi\|_{3/2}`, giving `\|F(t)\|_3 >= \|c\| lambda(t)/\|grad phi\|_{3/2}` | **correct, and the strongest part of the theorem** |

`eq:concstress` deserves explicit credit: `eq:concstrong` alone does not suffice,
because a stress representation is not determined by `R_v`. The duality argument
closes that hole and I could not break it (see refutation 5).

**Answer to (a): confirmed.** The residual lies in `L^{4/3}(0,T;Hdot^{-1})` with
the exact constant claimed, and both critical integrals diverge — logarithmically.

### Q2 `prop:weakresidual` — derived independently

Re-derivation, step by step:

- `R_{v_N} = (I - J_N) P div(v_N ⊗ v_N) = P div F_N` with `F_N = (I-J_N)(v_N⊗v_N)`,
  since `J_N` commutes with `P` and `div`. Matches `eq:FN`.
- Symbol bound: `|(xi_j \hat F_{ij})_i| <= |xi| |\hat F|_F` and `\|P\| <= 1` at each
  frequency. Correct with the note's Frobenius convention.
- Support: outside `[-N,N]^3` one has `max_i|xi_i| > N`, hence `|xi| > N`. Correct.
- `\|R\|_{Hdot^{-s}}^2 <= int |xi|^{2-2s}|\hat F|^2 <= N^{2-2s}\|F\|_2^2` **needs
  `s >= 1`**; the statement's `s > 1` covers it.
- `\|F_N\|_2 <= \|v_N⊗v_N\|_2 = \|v_N\|_4^2` by `L^2` orthogonality of the sharp
  cube. Correct.
- Interpolation `1/4 = theta/2 + (1-theta)/6` gives `theta = 1/4`, so
  `\|v\|_4^2 <= \|v\|_2^{1/2}\|v\|_6^{3/2}`. Verified in sympy.
- Sobolev and `eq:Genergy`: `\|v_N\|_4^2 <= S^{3/2} E_0^{1/4} Y_N^{3/4}`, and
  `\| Y_N^{3/4} \|_{L^{4/3}(0,H)} = (int_0^H Y_N)^{3/4} <= (E_0/(2nu))^{3/4}`.

This reproduces `eq:weakresidual` **exactly, constant included**.

- **Genuinely unconditional?** Yes. Every input is `E_0 = ||u_0||_2^2`, `nu`, `N`,
  `s`. No norm of the exact solution appears, no continuation hypothesis, and the
  bound is *uniform in `H`* (because `int_0^infinity Y_N <= E_0/(2 nu)`).
- **Genuinely at energy level?** Yes, and provably so. Under
  `f -> lambda f(lambda^2 t, lambda x)` the norm `L^{4/3}_t Hdot^{-s}_x` of the
  residual carries scaling exponent `(3-2s)/2 - 3/2 = -s` (sympy-verified). It is
  subcritical by exactly `s` powers. Nothing in the proof leaves the energy class.
- **Depth.** The whole content is: `F_N` is bounded in `L^{4/3}_t L^2_x` by energy,
  and is supported at frequencies `>= N`, so one negative derivative buys
  `N^{1-s}`. That is a one-line frequency-localisation observation. Correct, but
  the note's framing ("a genuine small full-vector residual") should not be read
  as depth. The note's own follow-up sentences are appropriately deflationary.
- **The trap the note does not name.** `N^{1-s}` is a *truncation* gain, not a
  scaling gain. Pushing `s` up buys faster `N`-decay but moves *further* from
  criticality; the decay degenerates to `N^0` exactly at `s = 1`, the borderline.
  Smallness is available only strictly away from the norm that matters.

**Verdict: correct, unconditional, energy-level, and elementary.**

### Q3 The shortfall subsection — verified, honest, but incomplete

Every estimate checks out:

- `Y_N(t) <= 3N^2 E_0`: `|xi|^2 <= 3N^2` on `[-N,N]^3`. **Exact.**
- `eq:crudeA`: `S^4 (3N^2E_0)(E_0/(2nu)) = (3S^4/(2nu)) N^2 E_0^2`. **Exact** (sympy).
- `eq:crudeB`: `\|F_N\|_3 <= (1+B_3)\|v_N\|_6^2`. **Exact.**
- `eq:missingpair` exponent matches `eq:CN`: `M_H = c_b nu^{-3} A_N`, so
  `e^{2M_H/3} = e^{2c_b A_N/(3 nu^3)}`. **Consistent.**
- `d_N -> 0` faster than any power for Schwartz data: via
  `d_N <= \|(I-J_N)u_0\|_2^{1/2}\|(I-J_N)u_0\|_6^{1/2}` and rapid decay of
  `\hat u_0`. **Correct.**
- I checked whether the note's crude route hides a better one: Bernstein on the
  shell `N < max|xi| <= 2N` gives `\|F_N\|_3 <= C N^{1/2}\|F_N\|_2`, hence
  `B_N <~ N int Y_N^{3/2} <~ N^2 E_0^{3/2}/nu` — the **same `N^2` growth**. The
  note's estimate is not artificially crude.
- The note's observation that rapid `d_N` decay does not beat the exponential is
  correct even for analytic data: `\hat u_0 ~ e^{-a|xi|}` gives `d_N ~ e^{-aN}`
  against `e^{cN^2}`. **Honest.**

**Exactly what is missing, stated precisely** (this is the thing the note does
not say):

Under `u -> lambda u(lambda^2 t, lambda x)` on horizon `H/lambda^2`, the exponent
of `\|.\|_{L^p_t L^q_x}` is `1 - 3/q - 2/p`. Then (all sympy-verified):

| Quantity | Exponent | Status |
|---|---|---|
| `A_N = \|v_N\|^4_{L^4_t L^6_x}` — **needed** | `0` | critical (invariant) |
| `\|v_N\|_{L^2_t L^6_x}` — **what energy gives** (Sobolev on `L^2_t Hdot^1_x`) | `-1/2` | subcritical by **half a power** |
| `B_N = \|F_N\|^2_{L^2_t L^3_x}` — **needed** | `0` | critical (invariant) |
| `\|R_v\|_{L^1_t L^3_x}` — **needed** by `cor:direct` | `0` | critical (invariant) |
| `\|R_{v_N}\|_{L^{4/3}_t Hdot^{-s}_x}` — **what `prop:weakresidual` gives** | `-s` | subcritical by **`s` full powers** |

So the shortfall is: **half a power of scaling in the comparison norm, and `s >= 1`
full powers in the residual norm.** The half-power in `L^p_t L^6_x` is precisely
the classical Ladyzhenskaya–Prodi–Serrin supercriticality gap of 3D Navier–Stokes
— the same gap that separates Leray–Hopf existence from regularity.

**Is the note's account honest?** Yes. It states the estimates, states that they
grow with `N`, states that they do not control the exponential, and states that
neither result proves `eq:missing`. I found no concealment and no unexploited
route.

**Is it complete?** No, in three respects:

1. It never names the deficit as a *scaling* deficit or quantifies it (`-1/2`,
   `-s`). Credit where due: the note is scaling-aware elsewhere — `eq:criticalspaces`
   lists the four invariant quantities, and Appendix B carries the checks
   `1 - 3/6 - 2/4 = 0` and `2 - 3/3 - 2/2 = 0`. It has the arithmetic and does not
   apply it to the gap.
2. It never says that the comparison-norm half of the shortfall **is** the LPS
   gap. A reader is left with the impression of a note-specific obstruction
   ("The new obstruction is then explicit", Section 1.3) where the operative
   deficit is the classical one.
3. It says "This section tests the strongest immediate energy-level route". I
   checked the obvious alternatives (Gagliardo–Nirenberg in place of Sobolev
   gives nothing better in 3D; Bernstein gives the same `N^2`), so the claim is
   defensible — but "strongest" is a judgement the note does not support, and
   local-energy / CKN-type routes are not discussed at all.

### Q4 `cor:necessary` — **genuine, not vacuous; but the quantitative half self-destructs**

*Algebra.* `3^{-2/3} d_N^2 + 4 B_N/(3^{2/3} nu) = 3^{-2/3}(d_N^2 + 4B_N/nu)`
(sympy-confirmed), so failure of `eq:indexcertificate` for every `N` rearranges
to `eq:necessary` exactly, constant `3^{2/3}` included. **Correct.**

*Logical status of `eq:necessary`.* It is the contrapositive of `cor:index` with
the bracket multiplied out. It contains no information `cor:index` did not.

*The defect the note does not disclose.* The right-hand side is
`3^{2/3} r_*^2 nu^2 exp(-(2c_b/(3nu^3)) A_N(H))`. It **tends to zero whenever
`A_N(H) -> infinity`** — which is precisely the regime the dichotomy contemplates
and the only regime the note's own `eq:crudeA` permits (`A_N <~ N^2`). So as a
*quantitative* lower bound `eq:necessary` is asymptotically empty exactly where
it would be needed. The theorem's title, "Quantitative necessary failure of every
certificate", is not earned by `eq:necessary`; the quantification is entirely
inherited from `cor:index`'s explicit constants.

*The subsequence claim is where the content is, and it is genuine.* Proof
checked: `A_N` bounded on a subsequence ⟹ exponential bounded; `B_N -> 0` and
`d_N -> 0` ⟹ bracket `-> 0`; product `-> 0`, contradicting `>= r_*^2 nu^2 > 0`.
Valid. (Minor: the proof silently reuses `d_N -> 0` from the previous
subsection.)

*Is the dichotomy vacuous?* **No.** A vacuous dichotomy would be a restatement in
terms of `T_*` alone. This one is not: `A_N(H)`, `B_N(H)` and `d_N` are
determined entirely by `u_0`, `nu`, `N`, `H` and the *global* band-limited flow
`v_N` — they are well-defined and in principle computable **whether or not the
exact solution blows up**. The dichotomy names which computable quantity must
misbehave. Combined with `thm:complete` (which gives `A_N -> int_0^H \|u\|_6^4`
and `B_N -> 0` in the regular case) it is a genuine two-sided characterisation:

```
T_* > H   <=>   A_N(H) bounded along a subsequence and B_N(H) -> 0 along it.
```

*But that is also its ceiling.* Being an equivalence, it cannot be used to prove
regularity without independent work — it is `eq:equiv` in asymptotic clothing,
not new leverage. The note says exactly this ("It is not a proof that the
alternative behavior is impossible"), which is the correct posture.

**Verdict: genuine, correct, not vacuous, not independent content, and mislabelled
as quantitative.**

### Q5 `cor:weaksmall` — correct, but weaker than its title

*Scaling, re-derived.* For `f_kappa(x) = kappa^3 f(kappa x)`,
`\|f_kappa\|_{Hdot^{-s}} = kappa^{(3-2s)/2}\|f\|_{Hdot^{-s}}`, giving `kappa^{1/2}`
at `s=1`; the time-measure factor `kappa^{-2}` raised to `3/4` gives `kappa^{-3/2}`;
product `kappa^{-1}`. **`eq:weakscale` exact.** (General `s`: `kappa^{-s}`.)

*Invariance of the critical quantities*, all re-derived and confirmed:
`\|kappa^3 f(kappa.)\|_3 = kappa^2\|f\|_3` against `dt -> kappa^{-2}dt` (so
`L^1_t L^3_x` invariant); `\|.\|_{3/2}` squared likewise; `F_kappa = kappa^2 F(kappa^2 t, kappa x)`
gives `\|F\|_3 = kappa\|F\|_3`, squared against `kappa^{-2}` (so `L^2_t L^3_x`
invariant). **Correct.**

*Energy.* Both sides of the identity scale by `kappa^{-1}`; the note's wording
("the exact energy identity persists and the initial `L^3` norm is unchanged") is
literally accurate.

*What the title conceals.* Smallness is bought purely from the scaling deficit,
and the same dilation **shrinks the horizon to `T/kappa^2 -> 0` and the energy to
`kappa^{-1} E_W -> 0`**. Neither is mentioned. So the corollary does *not*
exhibit an arbitrarily small energy-level residual **at fixed horizon and fixed
energy**. I checked whether the two-parameter family `W -> a W(b .)` can fix both:
`E' = a^2 b^{-3} E_W` and `T' = b^{-2} T` force `b = 1, a = 1`, so it cannot.
Achieving smallness at fixed data would require a profile close to a Leray
profile in `Hdot^{-1}`, and NRS/Tsai are purely qualitative — they give no
almost-rigidity statement, so nothing in the literature supplies it either.

*Does that damage the obstruction?* No. `thm:concentration` alone already refutes
any inequality `\|F\|_{L^2L^3} <= Phi(\|R\|_{L^{4/3}Hdot^{-1}}, E_0, nu, H)` at
*fixed* data, because the left side is `+infinity` and the right side finite. So
`cor:weaksmall` adds only rhetorical reach beyond `thm:concentration` plus
dimensional analysis. **Correct; oversold by its title; disclosure missing.**

*One further nuance the note omits.* The divergence in `eq:concstrong` and
`eq:concstress` is only **logarithmic**: on any `[0,H]` with `H < T` every
quantity is finite, `int_0^H \|R_v\|_3 dt = \|R_W\|_3 T log(T/(T-H))`, and I
verified the curve *is* an admissible comparison there (Definition 3.1 holds on
`[0,H]`, and a stress exists — `F_W = -grad(-Lap)^{-1}R_W ∈ L^3` by
Hardy–Littlewood–Sobolev from `R_W ∈ L^{3/2}`). The obstruction is exactly
borderline, which is informative and should be stated rather than left for a
reader to discover.

### Q6 Section 8 completion boundary — row by row

| Row | Assessment |
|---|---|
| Local classical branch and endpoint continuation — *"Explicitly imported"* | **Honest.** Section 1.1 additionally discloses the failed ESS fetch. Good practice. |
| Unweighted div–curl regularity — *"Explicitly imported audited project lemma"* | **Honest.** `hf25-review-defect-criterion.md` does cover `thm:divcurl` / `sec:divcurl`. |
| Weighted dissipation, relative identity, critical certificate — *"Detailed proofs supplied; self-checked candidates"* | **Honest**, and correctly refuses to call them audited. |
| Global regularity for the oscillatory family — *"Proved using the certificate..."* | **Status inconsistency.** "Proved" from a row-3 "self-checked candidate" is still a self-checked candidate. Also (cross-scope, flagged not adjudicated): the hypothesis `eq:heatcriterion` is smallness of `int \|e^{nu t Lap}u_0\|_6^4 dt`, which is the classical Fujita–Kato–Weissler / Cannone smallness criterion and already yields global existence by Picard iteration without this certificate. The Section 5 auditor should decide whether row 4 needs a prior-art qualifier. |
| Global spectral comparisons and conditional eventual certification — *"not a finite-dimensional validated computation"* | **Honest**, and backed by the remark after `prop:Galerkin`. |
| **Arbitrary-data successful index or comparison — "Not proved: equation (6.1)"** | **True but under-disclosed.** The note *proves* the equivalence `eq:equiv`, so `eq:missing` is not a sub-goal en route to the target — it **is** the target. Stronger: I verified that if `T_* > H` then `v = u` is admissible under Definition 3.1 (the imported branch is `C^j([0,H];H^k)` for all `j,k`), `R_v = 0`, `F = 0 ∈ L^2(0,H;L^3)`, `Q_0 = 0`, hence `Z_H = 0 < r_* nu`. So even the *general-comparison* existential is exactly equivalent to `T_* > H`. The row should say "equivalent to the target", not merely "not proved". Credit: the remark after `thm:complete` does say "Existence of a successful index is equivalent to continuation"; the table does not carry it forward. |
| Full NS-R3 / Clay alternative A — *"Not established by this continuation"* | **Honest.** |
| **Missing rows** | The table has no row for `prop:weakresidual`, none for `thm:concentration`/`cor:weaksmall`, and none for prior-art distinctness from CCRT. For a table billed as *the* completion boundary, omitting the two obstruction theorems — the only results whose prior-art status is defective — is a material gap. |

**The `"choose an accurate enough comparison"` sentence.** *"Conversely, writing
'choose an accurate enough comparison' without estimating its critical residual
and its stability cost would merely assume the desired conclusion. No such
selection is proved here for arbitrary input."*

This is **correct, and in fact understated**. Because the existential is provably
equivalent to `T_* > H` (`v = u` above), such a phrase would not merely *risk*
assuming the conclusion — it would *be* the conclusion, verbatim. The note is
entitled to say so outright, and should.

Section 8's opening prose repeats the row-4 problem: *"a fully proved oscillatory
data class"*, *"a rigorous obstruction"*. Against row 3's own "self-checked
candidates", "fully proved" and "rigorous" are inconsistent register.

---

## 5. Numbered repairs

**R1 (prior-art, mandatory).** In `thm:concentration`, state that `eq:conccurve`
is the backward self-similar (Leray) ansatz — literally NRS/Tsai (1.2) with
`a = 1/(2T)`, `U = W` — and that `eq:profileR` is the Leray-projected Leray
profile equation (1.3). Cite:
- J. Nečas, M. Růžička, V. Šverák, *On Leray's self-similar solutions of the
  Navier–Stokes equations*, Acta Math. **176** (1996), 283–294,
  DOI `10.1007/BF02551584`.
- T.-P. Tsai, *On Leray's self-similar solutions of the Navier–Stokes equations
  satisfying local energy estimates*, Arch. Ration. Mech. Anal. **143** (1998),
  29–51, DOI `10.1007/s002050050099`; erratum ibid. **147** (1999), 363.

**R2 (prior-art, mandatory).** Replace the ESS-based "It cannot be zero" argument
with a one-line appeal to NRS Theorem 1 (*"Let U be a weak solution of (1.3)
belonging to `L^3(R^3)`. Then `U ≡ 0`"*), whose hypotheses a nonzero solenoidal
Schwartz `W` satisfies with room, and keep the existing endpoint argument as a
second, self-contained route — explicitly labelled as such. This removes a
dependence on `eq:endpoint`, whose primary source the note admits it could not
fetch. Record Tsai's Remark 5.4 caveat (`U = grad Phi`, `Phi` harmonic, is a
nonzero profile with zero residual) so the reader sees that `W ∈ L^3` is
load-bearing, not decorative.

**R3 (interpretation, mandatory).** Record that `T = E_W/(4 nu Y_W)` is exactly
the Leray profile energy identity `nu\|grad U\|_2^2 = (a/2)\|U\|_2^2` with
`a = 1/(2T)`, equivalently `<R_W, W> = 0`; and that NRS is the canonical
demonstration that this identity is a balance rather than a rigidity. Add that
the log-divergence at the critical exponent is the standard borderline behaviour
of the self-similar ansatz (Serrin saturation; Leray's lower bound
`\|u(t)\|_p >= C(T-t)^{-(1-3/p)/2}`; the Type I literature), so that the
construction is presented as a correct instantiation of a known mechanism rather
than as a new phenomenon. Cite Tsai's Remark 5.5 (Scheffer's question on Leray's
equation with a speed-reducing force `U.g <= 0`) as the nearest prior notion of a
Leray profile carrying a residual, and note that the tuning places `<R_W,W> = 0`
on the boundary of that condition.

**R4 (logical gap, mandatory).** `prop:weakresidual` gives smallness only for
`s > 1`; `thm:concentration` and `cor:weaksmall` are stated at `s = 1`. Since
homogeneous Sobolev spaces do not nest, extend the obstruction to `s > 1`
explicitly. It goes through: solenoidality of Schwartz `W` forces `\hat W(0) = 0`
(from `xi . \hat W(xi) = 0` and continuity), hence `\hat R_W(xi) = O(|xi|)` near
the origin and `R_W ∈ Hdot^{-s}` for **all `0 < s < 5/2`**; the time integral
`int_0^T lambda^{2(3-2s)/3} dt` is finite for every `s > 0`; and the
`cor:weaksmall` scaling is `kappa^{-s} -> 0`. Two sentences.

**R5.** Rename `cor:necessary` (drop "Quantitative"), and state that the right
side of `eq:necessary` tends to zero whenever `A_N(H) -> infinity`, so that the
inequality carries no quantitative content in the regime it contemplates; the
surviving content is the subsequence statement. Point the proof at the
`d_N -> 0` fact it uses.

**R6.** In `cor:weaksmall`, disclose that the dilation also shrinks the horizon
to `T/kappa^2` and the energy to `kappa^{-1}E_W`, and that smallness at *fixed*
horizon and *fixed* energy is **not** established (and is not available from
NRS/Tsai, which are qualitative). State that `thm:concentration` alone already
refutes any fixed-data functional inequality, so nothing is lost.

**R7.** In the Section 7 remark, add that the divergence in `eq:concstrong` and
`eq:concstress` is only logarithmic, that on every `[0,H]` with `H < T` the curve
*is* an admissible comparison in the sense of Definition 3.1 with a finite
`L^2_t L^3_x` stress, and that the obstruction is therefore exactly borderline.

**R8.** In Section 6, quantify the shortfall by scaling exponent: `A_N` and `B_N`
are invariant (exponent 0); energy gives `L^2_t L^6_x` at `-1/2` and
`L^{4/3}_t Hdot^{-s}_x` at `-s`. State that the half-power in `L^p_t L^6_x` is the
classical Ladyzhenskaya–Prodi–Serrin supercriticality gap, so the reader is not
left believing the obstruction is specific to this note's machinery. Note also
that `prop:weakresidual`'s `N^{1-s}` is a truncation gain, not a scaling gain,
and degenerates to `N^0` exactly at the borderline `s = 1`.

**R9.** Section 8 table: (i) qualify row 4's "Proved" as conditional on the
self-checked certificate of row 3, and align the opening prose ("fully proved",
"rigorous") with the same register; (ii) rewrite row 6 to say that the missing
statement is provably **equivalent** to the target — for the hierarchy by
`eq:equiv`, and for general comparisons because `v = u` is admissible with
`Z_H = 0` whenever `T_* > H` — rather than only "Not proved"; (iii) add rows for
`prop:weakresidual` and for `thm:concentration`/`cor:weaksmall`, the latter
carrying the prior-art status from R1–R3; (iv) add a row recording that
distinctness from the CCRT robustness principle is not established here.

**R10.** Strengthen the "choose an accurate enough comparison" sentence from
*"would merely assume the desired conclusion"* to the fact the note has proved:
such a phrase **is** the conclusion, by `eq:equiv` together with the `v = u`
certificate. Also state once in Section 8 that `Definition 3.1` admits `v = u`,
which is what makes the existential equivalent rather than merely not-weaker.

**R11 (minor, precision).** In `thm:concentration`, say that "measurable stress
representation" means the identity `R_v = P div F` holds in `D'(R^3)` for a.e.
`t` (a time-independent test function plus Fubini gives this from a space-time
identity), so the pointwise-in-time duality bound is licensed without comment.

---

## 6. Refutation attempts and outcomes

Fourteen genuine attempts. **Thirteen failed. One partially succeeded** (attempt
7, which produced R4).

1. **Break the curve's scaling laws** — recompute `lambda'`, `\|v\|_p`,
   `\|grad v\|_2^2`, `eq:conce`, `int lambda`, `int lambda^2`, `int lambda^{2/3}`,
   `R_v = lambda^3 R_W(lambda x)`, and all three residual norm exponents, from
   scratch in sympy without consulting the HF26 review. **FAILED.** Every one
   exact. The `int_0^tau lambda^2` "mismatch" was a sympy branch-cut artifact
   (`log(-T) - log(-T+tau)`); it agrees with `T log(T/(T-tau))` numerically to
   `1e-123`.
2. **Show `R_W ∉ Hdot^{-1}`,** by finding a low-frequency obstruction. **FAILED.**
   A Schwartz field is in `Hdot^{-1}(R^d)` iff `d > 2`; the note's parenthetical
   "in three dimensions" is exactly the right caveat, and
   `\|P div(W⊗W)\|_{Hdot^{-1}} <= \|W⊗W\|_2` is correct.
3. **Show the curve secretly solves Navier–Stokes,** which would make
   `thm:concentration` false. **FAILED, and instructive.** It cannot: by NRS
   Theorem 1 a nonzero `L^3` Leray profile does not exist. I also computed `R_W`
   spectrally for `W = curl(0,0,e^{-|x|^2/2})`, `nu = 0.7`: `\|R_W\|_3 = 7.895`,
   `\|R_W\|_{3/2} = 34.10`, `\|R_W\|_{Hdot^{-1}} = 12.62`, `max|R_W| = 4.63` —
   manifestly nonzero, confirming the note's indirect argument directly. This
   produced R1 and R2.
4. **Break the constant-norm claims** `\|v(t)\|_3`, `\|q(v(t))\|_3` by finding a
   direction where `S_lambda G_3 != G_3` or the minimiser is non-unique.
   **FAILED.** `S_lambda` is an `L^3` isometry mapping `grad C_c^inf` onto itself,
   and the objective is strictly convex.
5. **Evade `eq:concstress`** with a clever stress `F` — concentrating it, or
   exploiting the non-uniqueness of `F` given `R_v`. **FAILED.** The bound is a
   duality bound against a single explicit test field, applied at each time with
   the correct dilation; there is nothing to evade. I checked `phi = P psi ∈ W^{1,3/2}`,
   `div phi = 0`, `<R_W, P psi> = <P R_W, psi> = c` by solenoidality,
   `\|grad phi_lambda\|_{3/2} = lambda^{-1}\|grad phi\|_{3/2}`, and
   `grad phi = 0 => phi = 0` (a nonzero constant is in no `L^p(R^3)`). All correct.
6. **Find a better energy-level bound on `B_N`** than `eq:crudeB`, which would make
   the note's account of the shortfall dishonest. **FAILED.** Bernstein on the
   shell `N < max|xi| <= 2N` gives `B_N <~ N^2 E_0^{3/2}/nu` — the same growth.
   Gagliardo–Nirenberg offers nothing over Sobolev in 3D. The note's account is
   not hiding a route.
7. **Attack the `s`-mismatch between `prop:weakresidual` (`s > 1`) and
   `thm:concentration` (`s = 1`).** **PARTIAL SUCCESS.** Homogeneous Sobolev
   spaces do not nest, so as written the obstruction does not refute an upgrade
   from the norm the note actually controls. The gap is real but repairable: I
   proved `\hat W(0) = 0` for solenoidal Schwartz `W`, hence
   `\hat R_W(xi) = O(|xi|)` and `R_W ∈ Hdot^{-s}` for `0 < s < 5/2`, and the time
   integral converges for all `s > 0`. (Numerically the low-frequency decay for my
   test profile was even faster than `O(|xi|)`, but the `O(|xi|)` bound is what is
   provable in general.) This produced **R4**.
8. **Show `cor:necessary` is vacuous** — a restatement in terms of `T_*` alone.
   **FAILED.** `A_N`, `B_N`, `d_N` are determined by `(u_0, nu, N, H)` and the
   *global* flow `v_N`, and are well-defined whether or not `u` blows up. The
   dichotomy has testable content. But the attempt exposed that the *quantitative*
   half degenerates (RHS `-> 0` when `A_N -> infinity`), which produced **R5**.
9. **Show `cor:weaksmall` is false** by checking that the critical norms really
   stay infinite and the energy identity really persists under the `kappa`
   dilation. **FAILED.** All four invariances re-derived and confirmed. But the
   attempt exposed the undisclosed shrinking of horizon and energy, and I proved
   the two-parameter family `a W(b.)` cannot hold both fixed. This produced **R6**.
10. **Find a `W` with `R_W ∉ L^3` or `∉ L^{3/2}`,** which would break
    `eq:concstrong`. **FAILED.** All three terms of `eq:profileR` are Schwartz or
    a bounded `L^p` multiplier applied to a Schwartz field.
11. **Contradict `thm:certificate` with the curve.** **FAILED**, and the note
    already anticipates it: `int_0^T \|v\|_6^4 = \|W\|_6^4 int lambda^2 = infinity`,
    so `A(H)` diverges too. I confirmed the curve *is* admissible on `[0,H]`,
    `H < T`, with a genuine `L^3` stress (`F_W = -grad(-Lap)^{-1}R_W`, in `L^3` by
    Hardy–Littlewood–Sobolev), and everything is finite there. Consistent. This
    produced **R7**.
12. **Break `prop:weakresidual`'s claim of `H`-uniformity.** **FAILED.**
    `int_0^infinity Y_N <= E_0/(2nu)` from `eq:Genergy`; the bound really is
    horizon-free.
13. **Find a hidden use of the exact solution in `prop:weakresidual`.**
    **FAILED.** Only `E_0`, `nu`, `N`, `s` appear, and `v_N` is global by
    `prop:Galerkin`.
14. **Show that Section 8's `"choose an accurate enough comparison"` warning is
    itself an overstatement.** **FAILED, in the opposite direction.** I verified
    `v = u` is admissible with `Z_H = 0` whenever `T_* > H`, so the existential is
    exactly equivalent to the conclusion and the note's warning is if anything too
    mild. This produced **R10**.

---

## 7. Controller errors and omissions in the index note

`research/evidence/hf27-critical-residual-continuation.md`:

1. **Correct and confirmed.** "It reuses HF26's curve, and inherits a citation
   requirement we have already established." Verified exactly: HF26 and HF27 share
   `lambda(t) = (1-t/T_c)^{-1/2}`, `T_c = E_W/(4 nu Y_W)`, and
   `Z = Lambda W = W + (x.grad)W`. The instruction to check rather than assume was
   the right call, and the answer is that the requirement is **not met**.
2. **Understated.** The requirement is stronger than "cite NRS/Tsai for a known
   ansatz". `eq:profileR` **is** the Leray profile equation, and the note's tuning
   of `T` **is** that equation's energy identity. The controller record should say
   so, and should add Scheffer's speed-reducing-force question (Tsai Remark 5.5)
   as directly-on-point prior art.
3. **Error of under-recording, in "NON-CLAIMS".** The entry reads "no proof that
   the criterion is weaker than regularity at the existential level, and none
   claimed". But the note **proves the criterion is equivalent** to continuation:
   `eq:equiv` for the hierarchy, and `v = u` with `Z_H = 0` for general
   comparisons. Recording only the absence of a weakness claim loses the note's
   own strongest honest finding. The frontier record should read: *the existential
   is provably equivalent to the target, by the note's own `eq:equiv`.*
4. **Propagated overclaim.** Claim 5 repeats the note's word "quantitative"
   ("a quantitative dichotomy"). Per R5 the quantitative half is asymptotically
   empty; the dichotomy is genuine, the quantification is not.
5. **Omission.** Claim 4 describes `prop:weakresidual` without recording the
   `s > 1` restriction. That restriction is what creates the R4 gap against the
   `s = 1` obstruction, so it belongs in the index.
6. **Frozen hash confirmed.** `sha256sum` of the `.tex` reproduces
   `3898e9a0...f97488` exactly as recorded. No discrepancy.
7. No other controller error found. The audit-priority list is well aimed, and
   the item "check against our audited HF26 countermodel review, which computed
   the same curve's scaling" led directly to the decisive finding.

---

## 8. What I did NOT check

- **Out of scope, not examined:** `thm:certificate` and its Young/first-exit
  steps, `cor:direct`, `lem:three`, `prop:identity`, `prop:weighted`,
  `prop:Galerkin`'s Picard construction, `thm:complete`'s bootstrap
  `eq:convergence`, `thm:oscillation` and `cor:heat`, Appendix A, Appendix B
  beyond the two scaling identities I reused, and the constant dictionary
  `eq:constants1`–`eq:rstar`. Where Sections 6–8 consume these I took them as
  given and said so.
- **Prior-art distinctness of `thm:certificate` from CCRT** — the controller's
  "decisive prior-art question" — is not in this scope and I did not adjudicate it.
- **The `cor:heat` / Cannone overlap** flagged under row 4 is raised, not decided;
  it belongs to the Section 5 auditor.
- **Primary sources.** NRS 1996 and Tsai 1998 statements were established through
  a bounded literature check reading published text and metadata. Per the task
  constraints I retained **no third-party PDF** — only metadata, quoted theorem
  statements, and my own notes. The ESS endpoint theorem was not independently
  verified (the note itself says its PDF fetch failed); I only noted that R2 would
  remove `thm:concentration`'s reliance on it.
- **Numerics are confirmatory, not probative.** The 128³ spectral computation of
  `R_W` runs on a periodic box, so its low-frequency behaviour is only indicative;
  every conclusion I drew from it (`R_W != 0`, `<R_W,W> = 0`, `\hat W(0) = 0`) also
  has an independent analytic proof recorded above.
- **No Lean, no formal check, no kernel replay.**
- **Nothing here is promoted.** No graph node changes, no manuscript edit, no
  claim that any Section 6–8 result is audited beyond this document.
