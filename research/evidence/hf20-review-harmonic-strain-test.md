# Review of HF20: the local harmonic-strain sign test

Independent proof audit, 2026-09-06. Lens: reconstruct every implication from
the first nontrivial one, recompute every exponent, refute each new fact.

## Freeze

| object | identity |
|---|---|
| research HEAD | `1014e7e3c33af4a341a5f46156a22b808170257b` |
| target note | `research/evidence/hf20-harmonic-strain-test.md`, sha256 `2ab72f57234707577ff34c7f5871b92638f9ed6ccd3e6002a0d67530c67130d2` |
| immutable artifact | `<work vault, not in this repository>/navier-hf20-candidate-proof.pdf`, sha256 `4be9a53b244ba385e7b1e18bf02bee9b10db44a4329438612742ac32b7e15009` (7 pp., read in full via the PDF tool) |
| manuscript | `../navier-paper/main.tex` at `39ccb664bf055fac94b3cfac97bf00a60191373d` |

The PDF was read and compared line by line with the transcription. Two
wording discrepancies, both resolved in favour of the PDF and both harmless:

- Theorem 1.2 in the PDF quantifies over `beta >= 0`; the transcription writes
  "for every beta". Both are true (for `beta < 0` and `d >= 0` the extra term
  only helps), so nothing downstream changes.
- The transcription's (4.2) prints only the final bound; the PDF's (16) shows
  the intermediate split `2 int rho^3 |d_eps| + int rho^2 |d_eps|^2`, which is
  the step the audit had to check. The transcription is a faithful condensation
  everywhere else, including all constants, exponents and hypotheses.

## Verdict summary

The mathematical content is **correct**. Every identity, every exponent and
every constant in Sections 2–5 was reconstructed independently and confirmed;
the pointwise geometric identities were additionally confirmed numerically
(bounded evidence only, listed below). The candidate contains **one real
defect**: the displayed inequality of Theorem 1.1 is *one-sided*, is strictly
weaker than the two-sided bound its own proof establishes, and is strictly
weaker than what Section 4's own display (19) and all of Section 5 consume.
As literally stated, Theorem 1.1 does not entail the sentence printed
immediately after it ("Both signs of `K` therefore occur"), nor the first half
of (19), nor `k = K(V) > 0` in Section 5, and therefore does not entail
Theorem 1.2. The proof does entail all of them. This is a statement-level gap
between a displayed result and its use, so the verdict is REPAIR, and the
replacement display is given below with its proof.

## 1. Reviewed scope

Reconstructed and checked in full: Section 0/1 (definitions and statements),
Lemma 2.1, Lemma 2.2, Lemma 2.3, Section 3 (the swirl `U`, the cutoff `chi`,
the fields `h`, `g`, `e`), Section 4 (13)–(19), Section 5 (20)–(21) and
Corollary 5.1, and Section 6's non-claims. The external import (Tao Thm 5.4)
was checked against the manuscript's verbatim transcription
(`main.tex` lines 534–598) rather than re-fetched, because the manuscript's
import already carries six directly-inspected transcription notes for pp. 52–53.

## 2. Point-by-point findings, in the order §7 asks for them

**(a) Exactness of `Q(v_eps) <= F(U + eps e)`, and admissibility of `-eps g`.**
Correct, and the competitor is admissible without any closure argument.
`g = grad(chi phi)` with `chi phi in C_c^infty`, so `g` is literally a gradient
of a compactly supported smooth function; `G_3` is a linear space, so
`-eps g in G_3`. `v_eps + (-eps g) = U + eps h - eps g = U + eps e`, so
`Q(v_eps) <= F(U + eps e)` by definition of the infimum.

The *equality* `F(U + eps e) = F(U) + C_e |eps|^3` is exact as claimed. Verify
the support statement rather than take it: `chi(x) = eta(16-|x|^2) /
(eta(16-|x|^2) + eta(|x|^2-9))` equals 1 on `|x| <= 3` (there `eta(|x|^2-9) = 0`
and `eta(16-|x|^2) > 0`) and 0 on `|x| >= 4`; the denominator is positive
everywhere; hence on the *open* ball of radius 3, where `grad chi = 0` in a
neighbourhood of each point, `h = curl a` and `g = grad phi`, so `e = h - g = 0`
there. And `supp U` lies in `{5/4 <= r <= 7/4, |z| <= 1/2}`, contained in the
ball of radius `(49/16 + 1/4)^{1/2} = 1.82... < 3`. So `supp U` and `supp e`
are disjoint, `|U + eps e|^3 = |U|^3 + |eps|^3 |e|^3` *pointwise*, and the
integral splits exactly. `F` splits because it is the integral of a pointwise
function of the field, not because of any linearity. Confirmed.

**(b) `<j(U), d_eps> = 0`.** Correct, in both halves.
`d_eps = w_eps - U = eps h + q(v_eps)`.
- `j(U)·(eps h) = eps rho (U·h)`; `U·h = s(-yx/r + xy/r + 0) = 0` on `supp U`
  because `h = (x,y,-2z)` there and `U = s e_theta`, and `rho = 0` off `supp U`.
  So the first pairing vanishes pointwise, as claimed (stronger than needed).
- `j(U) = |U|U = rho U = s^2 e_theta`, and `div(s^2 e_theta) = r^{-1} d_theta(s^2) = 0`
  by azimuthal independence. Hence `<j(U), grad varphi> = -<div j(U), varphi> = 0`
  for `varphi in C_c^infty`; since `j(U) in L^{3/2}` and `G_3 subset L^3` is the
  `L^3`-closure of those gradients, `j(U)` annihilates all of `G_3` by
  continuity of the pairing. `q(v_eps) in G_3` by definition of `w`. Confirmed.

**(c) `w(U) = U`.** Correct. It is exactly (b)'s second half plus Lemma 2.1's
sufficiency of stationarity: minimizing the convex `g |-> F(U+g)` over the
linear space `G_3`, the Gateaux derivative at `g = 0` is `<j(U), .>`, which
vanishes on `G_3`; convexity upgrades stationarity to a global minimum, and
strict convexity gives uniqueness. This is the manuscript's
`lem:quotient-minimizer` specialised, and it is *not* an assertion of locality:
`w(U) = U` is a global statement about the swirl only, and the candidate never
claims `w(v_eps)` is local (Remark 3.1 is honest about this and the estimates
in (16) are global).

**(d) The three bounds (4.1)/(14).** Correct. The chain is
`int B(U, d_eps) = F(w_eps) - F(U) - <j(U), d_eps> = Q(v_eps) - Q(U)` using
`Q(U) = F(w(U)) = F(U)` from (c) and `<j(U), d_eps> = 0` from (b). All three
integrals are finite (`j(U) in L^{3/2}`, `d_eps in L^3`). Since `B >= 0`
pointwise this gives `0 <= Q(v_eps) - Q(U)` (a conclusion, not an assumption)
and `int B <= C_e |eps|^3` from (13). Then `B >= |a||d|^2/4` gives
`int rho|d_eps|^2 <= 4 C_e |eps|^3`, and `B >= |d|^3/6` gives
`||d_eps||_3^3 <= 6 C_e |eps|^3`. Lemma 2.2 itself was re-derived: the algebraic
identity `(j(a)-j(b))·(a-b) = ((|a|+|b|)/2)(|a-b|^2 + (|a|-|b|)^2)` expands on
both sides to `|a|^3 + |b|^3 - (|a|+|b|)(a·b)`; integrating
`B(a,d) = int_0^1 (j(a+td)-j(a))·d dt >= (1/2) int_0^1 t(|a+td|+|a|)|d|^2 dt`
gives `|a||d|^2/4` by keeping `|a|`, and `|d|^3/6` by `|a+td|+|a| >= t|d|`.
Both constants are right.

Note what makes this work and is worth preserving: the gain is bought from a
*competitor*, so no differentiability of `w` in its argument is used anywhere.
That is the same device as the manuscript's `rem:qe-transport-scope`.

**(e) The `|eps|^{3/2}` rate in (4.2)/(16).** Correct, and applied on the right
set. From (7), `|A_eps - A_0| <= (2 rho + |d_eps|)|d_eps|`; with `|N_0| <= rho^2`
this gives `|<A_eps-A_0, N_0>| <= 2 int rho^3 |d_eps| + int rho^2 |d_eps|^2`.
Both integrands vanish off `supp U` because `rho` does, so the restriction is
automatic and no set is misused. Cauchy–Schwarz with the stated factors:
`int rho^3 |d_eps| = int (rho^{1/2}|d_eps|)(rho^{5/2}) <= (int rho|d_eps|^2)^{1/2}(int rho^5)^{1/2}
 <= 2 C_e^{1/2}|eps|^{3/2} · ||U||_5^{5/2}`,
so the first term is `4 C_e^{1/2} ||U||_5^{5/2} |eps|^{3/2}`. The second uses
`rho^2 <= ||U||_infty rho`, giving `4 C_e ||U||_infty |eps|^3`. Both match (16).
The norm `||U||_5^{5/2} = (int rho^5)^{1/2}` is the correct reading of
`(int rho^5)^{1/2} = (||U||_5^5)^{1/2}`. The claim `|N_0| <= rho^2` uses
`|N(U)| = rho^2/r` and `r >= 5/4 > 1` on `supp U`; correct.

**(f) The coefficient (4.3)/(17).** Correct, and both halves were recomputed.
`curl a = (y·0 - z·(-xz), z·(yz) - x·0, x·(-xz) - y·(yz)) = (x, y, -2z) = grad phi`,
and `Laplacian phi = 1 + 1 - 2 = 0`. So on a neighbourhood of `supp U`,
`h = g = (x,y,-2z)` and `grad h = diag(1,1,-2)`.
- `<A_0, (h·grad)U> = int rho U_i h_j d_j U_i = int rho h_j d_j(|U|^2/2)
   = int rho·rho d_j rho · h_j = int h · grad(rho^3/3) = -int (div h) rho^3/3 = 0`,
  using `rho^3 in C_c^infty` and `div h = 0`. This identity is generic (it holds
  for any smooth compactly supported `U` and any solenoidal `h`), not special to
  the swirl.
- `(U·grad)h = (grad h) U = diag(1,1,-2) U = (U_1, U_2, -2U_3) = (U_1, U_2, 0) = U`
  **exactly**, because `U = s e_theta` is azimuthal and has no third component,
  so the `-2` entry never acts. The audit's specific worry is answered: the
  identity is exact, not approximate. Hence
  `<A_0, (U·grad)h> = int rho U·U = int rho^3 = ||U||_3^3 = c_0 > 0`.
- `<A_0, N_0> = int rho U · (-(rho^2/r) e_r) = 0` since `e_theta ⊥ e_r`.

Cross-check with the manuscript: `K(U) = 0` also follows from
`lem:quotient-transport`, `K = -int q·((A·grad)u)`, because `q(U) = 0` when
`w(U) = U`. The two routes agree.

**(g) `C_*` in (4.4)/(18) and the threshold `eps_0`.** Correct.
`N(v_eps) = N_0 + eps N_1 + eps^2 N_2` exactly (the nonlinearity is quadratic),
and the expansion
`K(v_eps) + eps c_0 = -<A_eps-A_0, N_0> - eps<A_eps-A_0, N_1> - eps^2<A_0, N_2> - eps^2<A_eps-A_0, N_2>`
is an identity given `<A_0,N_0> = 0` and `<A_0,N_1> = c_0`. The Hölder bounds
are right: `||A_0||_{3/2} = || |U|U ||_{3/2} = ||U||_3^2 = M^2`;
`||A_eps - A_0||_{3/2} <= 2M||d_eps||_3 + ||d_eps||_3^2 <= (2M + d_0)d_0|eps| = L|eps|`
for `|eps| <= 1`, with `d_0 = (6C_e)^{1/3}`. Collecting, and using
`|eps|^3 <= eps^2 <= |eps|^{3/2}` for `|eps| <= 1`, gives exactly (18).
`eps_0 = min{1, (c_0/(2 max{1,C_*}))^2}` is the correct threshold for
`C_* eps^{3/2} <= eps c_0 / 2`; it is positive because `c_0 > 0` and `C_* < infty`.

Non-defect worth recording: `eps_0` is explicit but astronomically small. With
the fields as written, a numerical evaluation gives `c_0 = 2.13e-3`,
`M = 0.1287`, `||U||_5^{5/2} = 5.14e-3`, `||U||_infty = 0.1353`,
`||N_1||_3 = 1.46`, `C_e = 1.75e5`, `d_0 = 102`, `L = 1.04e4`,
`||N_2||_3 = 1.34e3`, hence `C_* ≈ 1.4e7` and `eps_0 ≈ 5.8e-21`. This is
bounded evidence only and changes nothing: the claims are qualitative. It does
mean the "computable constant" is not a usable quantitative object, and the
size is driven entirely by `C_e` and `||N_2||_3`, i.e. by the far shell
`3 <= |x| <= 4` where `h` and `g` are large and disagree.

**(h) The scaling table (5.1)/(20).** All four exponents recomputed from
scratch with `T_lambda v(x) = lambda v(lambda x)` and confirmed:
- `w(b T_lambda V) = b T_lambda w(V)` (Lemma 2.1; `T_lambda grad varphi = grad(varphi(lambda ·))`,
  so `T_lambda G_3 = G_3`).
- `||T_lambda v||_3^3 = int lambda^3 |v(lambda x)|^3 dx = ||v||_3^3`, so
  `Q(b T_lambda V) = b^3 Q(V)`.
- `||b T_lambda V||_2^2 = b^2 int lambda^2 |V(lambda x)|^2 dx = b^2 lambda^{2-3} E_V = b^2 lambda^{-1} E_V`. Confirmed.
- `j(w) |-> b^2 lambda^2 (·)(lambda x)`, `N(v) |-> b^2 lambda^3 (·)(lambda x)`,
  `dx |-> lambda^{-3}`: `K |-> b^4 lambda^{5-3} k = b^4 lambda^2 k`.
- `Delta(T_lambda V) = lambda^3 (Delta V)(lambda x)`: `D_Q |-> b^{2+1} lambda^{5-3} d = b^3 lambda^2 d`.

Consistency with the manuscript's `lem:quotient-scaling` (main.tex 5477–5486,
with `(D_lambda u)(x) = lambda u(lambda x)` at line 4976): the manuscript states
`Q(alpha u) = |alpha|^3 Q(u)`, `Q(D_lambda u) = Q(u)`, `w(alpha u) = alpha w(u)`,
`w(D_lambda u) = D_lambda w(u)` — identical operator, identical homogeneities.
The candidate's Lemma 2.1 restricts the amplitude law to `b > 0`; the manuscript
proves it for all `alpha in R`. That difference matters only for the repair
below, which uses `alpha = -1`.

With `lambda = b^2 E_V / E`, `||v_0||_2^2 = b^2 (E/(b^2 E_V)) E_V = E` exactly,
and `K - beta nu D_Q = lambda^2 b^3 (bk - beta nu d) = (E_V^2/E^2) b^7 (bk - beta nu d)`,
matching the PDF and diverging as `b -> infinity` because `k > 0`.

**(i) The regularity chain in §5.** Correct, but it is a compressed
re-derivation of a lemma the manuscript already proves, and should cite it.
- The viscosity rescaling matches the manuscript exactly. The candidate applies
  Tao at unit viscosity to `v_0/nu` and sets `v(t,x) = nu v~(nu t, x)`,
  `p(t,x) = nu^2 p~(nu t, x)`. The manuscript's `eq:nu-normalization` is the
  inverse map `v~(x,s) = nu^{-1} u(x, s/nu)`, `q~(x,s) = nu^{-2} p(x, s/nu)` with
  `a = nu^{-1} u_0`. These are the same substitution; the residual check
  `nu^{-2}(d_t u + (u·grad)u + grad p - nu Laplacian u)(x, s/nu) = 0` is what
  `lem:nu-normalisation`(i) records. No mismatch.
- Tao Thm 5.4(ii) does carry a smallness condition
  `(||u_0||_{H^1} + ||f||)^4 T <= c`, but its final clause is "local existence
  whenever `T` is sufficiently small depending on `H^1(u_0,f,T)`", and the
  candidate only ever needs a short interval for a *fixed* datum. So the
  smallness hypothesis is genuinely available where it is used. (The
  manuscript's Step 1 prefers Cor. 5.8 only because it needs `T = 1` there.)
- Tao 5.4(iv) yields `d_t^j v, d_t^j p in L^infty_t H^k`, *not* `C^0_t H^k`
  (this is exactly `rem:tao-scope`(c)). The candidate's one sentence — "bounds
  for the next time derivative give strong continuity of the preceding one in
  `H^k` by the fundamental theorem of calculus" — is the correct *idea*, and it
  is the manuscript's `lem:upgrade`, a lemma whose actual proof runs several
  steps (scalar pairings against a countable dense set, a distributional FTC
  claim, Lipschitz continuity off a null set, extension to all times). The
  candidate's sketch is not wrong, but it is not a proof at the tier the rest
  of the note is written at.
- Consequence, once `lem:upgrade` is in hand: `prop:localtheory`(iii) gives
  `v in C^j([0,T]; H^k)` for all `j,k`, hence `v in C^1_t L^3` by Sobolev
  embedding on the closed interval including `t = 0`; `p in C^0([0,T]; H^k)`
  gives `p(t) in W^{1,3}` (`H^1 subset L^2 cap L^6 subset L^3` for `p` and for
  `grad p`); and `prop:localtheory`(iv) gives the pointwise equation with the
  normalised pressure `p = R_i R_j(u_i u_j)`. These are exactly Lemma 2.3's
  hypotheses. No continuation theorem is used, as claimed.
  **Integration action: replace the §5 sketch by a citation of
  `prop:localtheory`(iii),(iv) and `lem:upgrade`.**

**(j) The right derivative at `0+`.** Legitimate. `Q` is `C^1` Fréchet on `L^3`
(Lemma 2.3, which reproduces the manuscript's `prop:quotient-derivative`), and
`t |-> v(t)` is right-differentiable at `0` in `L^3` with
`d_t v(0) = nu Laplacian v_0 - N(v_0) - grad p_0 in L^3`. Hence
`Q(v(t)) - Q(v_0) = <j(w(v_0)), v(t) - v_0> + o(||v(t)-v_0||_3)
 = t <j(w(v_0)), d_t v(0)> + o(t)`,
so the right derivative exists and equals
`nu<A_0', Laplacian v_0> - <A_0', N(v_0)> - <A_0', grad p_0> = -nu D_Q + K + 0`,
the pressure dropping out because `grad p_0 in G_3` (`p_0 in W^{1,3}`, cut off
and mollified — the manuscript's `lem:quotient-pressure`). One-sided regularity
is enough because the chain rule argument is a one-sided Taylor expansion. The
sign conventions match the manuscript: `def:qe-dissipation` has
`D_Q = -<A, Laplacian u>`, and `prop:quotient-evolution` reads
`d/dt Q + nu D_Q = -int q·((A·grad)u) = -<A, (u·grad)u> = K` via
`lem:quotient-transport`. Identical.

**(k) The `b -> infinity` family and whether `d` can vanish.** The energy is
held exactly at `E` (see (h)) and the supremum diverges. Whether `d = D_Q(V)`
vanishes is irrelevant to the candidate's argument: `bk > nu d` is arranged
with `b = 1 + 2 nu ||V||_3^2 ||Delta V||_3 / (eps c_0)`, which works because
`d <= ||V||_3^2 ||Delta V||_3` (Lemma 2.3) and `k >= eps c_0 / 2`, giving
`bk >= eps c_0 / 2 + nu d > nu d` strictly; and `b^7(bk - beta nu d) -> +infinity`
because `k > 0` regardless of `d`. Separately, the audited HF18-A coercivity
`D_Q(u) = D_3(w) >= c ||u||_9^3` forces `d > 0` for `V != 0`, so the question is
moot in both directions. The candidate's `d >= 0` is sufficient and honest.

## 3. First bad bridge

**`research/evidence/hf20-harmonic-strain-test.md` §1, Theorem 1.1, display
(1.1) [= PDF (2)], and its consumption at (4.5) [= PDF (19)] first inequality.**

The display asserts, for every `|eps| <= 1`,

    K(U + eps h) + eps ||U||_3^3 <= C_* |eps|^{3/2} .

This is an *upper* bound for both signs of `eps`. Substituting `eps -> -delta`
with `delta > 0` gives `K(U - delta h) <= delta c_0 + C_* delta^{3/2}`, again an
upper bound. Nothing in the displayed statement bounds `K` from below.
Consequently the display does not support:

- the sentence printed immediately after it, "Both signs of `K` therefore
  occur on compactly supported smooth solenoidal fields";
- (4.5)/(19) first inequality, `K(U - eps h) >= eps c_0 / 2 > 0`;
- Section 5's `k = K(V) > 0` with `V = U - eps h`, hence (5.2)/(21), hence
  Theorem 1.2, hence Corollary 5.1.

This is the first place where a claimed statement fails to entail its use. It
is not an error in the mathematics: the proof of Theorem 1.1 bounds each of the
four terms of the expansion in *absolute value*, so it proves the two-sided
estimate. It is a defect of statement, and at the tier this programme demands
(a displayed theorem is what downstream text may use) it must be fixed rather
than read charitably.

## 4. Replacement argument

Two independent repairs. Either alone is sufficient; the first is minimal.

**R1 (restate the theorem two-sidedly).**

> **Theorem 1.1'.** There are `U, h in C_c^infty(R^3)^3` with
> `div U = div h = 0`, `U != 0`, and a finite computable `C_*` such that for
> every `|eps| <= 1`
>
>     | K(U + eps h) + eps ||U||_3^3 |  <=  C_* |eps|^{3/2} .

*Proof.* Unchanged from the candidate's Section 4, read as it is actually
written. With `A_eps = j(w_eps)`, `A_0 = j(U)`, and
`N(v_eps) = N_0 + eps N_1 + eps^2 N_2` (exact, the nonlinearity being
quadratic), `<A_0, N_0> = 0` by (10) and `<A_0, N_1> = c_0 = ||U||_3^3` by (17)
give the identity

    K(v_eps) + eps c_0 = -<A_eps - A_0, N_0> - eps<A_eps - A_0, N_1>
                         - eps^2<A_0, N_2> - eps^2<A_eps - A_0, N_2>.

Each of the four terms is bounded in absolute value by (16), (15) and Hölder:
`4 C_e^{1/2} ||U||_5^{5/2} |eps|^{3/2} + 4 C_e ||U||_infty |eps|^3`,
`L ||N_1||_3 eps^2`, `M^2 ||N_2||_3 eps^2`, and `L ||N_2||_3 |eps|^3`
respectively. For `|eps| <= 1`, `|eps|^3 <= eps^2 <= |eps|^{3/2}`, so the
triangle inequality gives the two-sided bound with the *same* `C_*` of (18).
No new hypothesis, no new constant. ∎

With Theorem 1.1', (19) is immediate in both halves for
`0 < eps < eps_0 = min{1, (c_0 / (2 max{1, C_*}))^2}`, and the rest of the note
stands verbatim.

**R2 (avoid the lower bound entirely, by oddness of `K`).** This repair is worth
recording because it shortens the note and shows the two-sided estimate is not
actually needed.

> **Lemma A.** `K(-v) = -K(v)` and `D_Q(-v) = D_Q(v)` for every `v in L^3`.
>
> *Proof.* `w(-v) = -w(v)` (manuscript `lem:quotient-scaling` with
> `alpha = -1`; the candidate's own Lemma 2.1 states the homogeneity only for
> `b > 0` and must be widened to `alpha in R`, which its proof already gives:
> `q |-> alpha q` is a bijection of `G_3` for every `alpha != 0` and
> `F(alpha z) = |alpha|^3 F(z)`). Hence `j(w(-v)) = |-w(v)|(-w(v)) = -j(w(v))`.
> Since `N(-v) = ((-v)·grad)(-v) = N(v)` and `Laplacian(-v) = -Laplacian v`,
> `K(-v) = -<-j(w(v)), N(v)> = -K(v)` and
> `D_Q(-v) = -<-j(w(v)), -Laplacian v> = D_Q(v)`. ∎

Given Lemma A, the *one-sided* display (1.1) already suffices: for
`0 < eps < eps_0` it gives `K(U + eps h) <= -eps c_0 + C_* eps^{3/2} <= -eps c_0/2 < 0`,
so `V := -(U + eps h)` is smooth, compactly supported, solenoidal, nonzero, and
satisfies `k := K(V) >= eps c_0 / 2 > 0` with `d := D_Q(V) = D_Q(U + eps h) >= 0`
and `E_V = ||U + eps h||_2^2 > 0`. Section 5 then runs unchanged with this `V`
(the `b`-formula only uses `k >= eps c_0/2` and `d <= ||V||_3^2 ||Delta V||_3`,
and `||V||_3 = ||U + eps h||_3`).

Lemma A also settles the headline sentence of Theorem 1.1 outright: since `K` is
odd, "both signs of `K` occur" is equivalent to "`K` is not identically zero on
`C_c^infty` solenoidal fields", and the candidate's real contribution is exactly
that non-vanishing, certified analytically.

## 5. Refutation attempts, all failed

1. **Explicit counter-field against the two-sign certificate.** None found. All
   pointwise inputs were checked by direct Cartesian differentiation on 2000
   random points of `supp U` (bounded evidence, `h`-step `1e-5`):
   `max|h - (x,y,-2z)| = 1.1e-11`, `max|g - (x,y,-2z)| = 2.9e-11`,
   `max|U·h| = 1.8e-13`, `max|div U| = 1.7e-8`, `max|div h| = 1.1e-11`,
   `max|(U·grad)h - U| = 1.8e-8`, `max|N(U) + (rho^2/r) e_r| = 1.1e-10`,
   `max|U·N(U)| = 3.6e-12`, `max|div(rho U)| = 5.7e-10`. Integral identities by
   cylindrical Gauss–Legendre quadrature: `<A_0,(h·grad)U> = 1.0e-13` (claimed 0)
   and `<A_0,(U·grad)h> = 2.134085535714796e-3 = c_0` to 16 digits (claimed `c_0`).
   These confirm, they do not prove; the analytic derivations above are the proof.
2. **Scaling family against (1.1).** The estimate is not scale-invariant (it is a
   statement about one fixed pair `U, h` and small `eps`), so there is no scaling
   family to run against it. Under `v |-> b T_lambda v` the certificate simply
   transports with the exponents of (h).
3. **Independent upper bound on `K`.** Via `lem:quotient-transport`,
   `|K(v_eps)| = |int q(v_eps)·((A_eps·grad)v_eps)| <= ||q(v_eps)||_3 ||A_eps||_{3/2} ||D v_eps||_infty`,
   and `||q(v_eps)||_3 <= ||d_eps||_3 + |eps| ||h||_3 = O(|eps|)`. This gives an
   independent `K(v_eps) = O(|eps|)`, the same order as the claimed `-eps c_0`,
   with a numerically much larger constant. Consistent; no contradiction.
4. **Hidden circularity.** None. `K` and `D_Q` are never bounded using `Q`, the
   quantity to be controlled; the only inequality used on `Q` is the competitor
   upper bound (13), whose right side is an explicit constant times `|eps|^3`,
   computed from fields fixed before `eps` is chosen. No norm of the unknown
   minimizer `w_eps` is used except through (14), which is derived from (13).
5. **Identity mistaken for an estimate.** The reverse risk is present and handled:
   (13)'s equality really is an identity (disjoint supports), and (14)'s first
   line converts it into the two genuine estimates via `B >= 0`.
6. **Instantaneous fact promoted to a time-integrated one.** The candidate does
   *not* do this, and says so in §6. (5.2) is instantaneous at `t = 0+` and is
   used only to conclude strict increase on a short interval, which is the
   definition of a positive right derivative — no integration of an unproved
   inequality occurs.
7. **Consistency with the audited HF18-A bound `|K| <= C_* Q^{1/3} D_3(w)`.**
   Compatible; neither is wrong. On the family `b T_lambda V`,
   `|K| = b^4 lambda^2 |k|` and `C_* Q^{1/3} D_3(w) = C_* (b^3 Q(V))^{1/3} b^3 lambda^2 d
   = C_* b^4 lambda^2 Q(V)^{1/3} d`. The ratio is *exactly scale-invariant*, so
   the whole HF20 family tests HF18-A only at the single field `V`, where
   HF18-A asserts `|k| <= C_* Q(V)^{1/3} d` with a universal constant. No
   tension. Sharper: HF18-A gives `d/dt Q <= (C_* Q^{1/3} - nu) D_Q`, so an
   increase of `Q` requires `Q^{1/3} > nu / C_*` — supercritical size — and
   HF20's data satisfy `Q(v_0) = b^3 Q(V)` with `b` forced large by
   `b >= 1 + 2 nu ||V||_3^2 ||Delta V||_3 / (eps c_0)`. The two results agree
   quantitatively about *where* the increase must live. This also shows HF20
   cannot be strengthened to produce an increase at small `Q`: HF18-A forbids it.

## 6. Conditional suffix that survives

Everything, once R1 (or R2) is applied. Specifically:

- **Theorem 1.1'** (two-sided, `C_*` of (18)) — survives, proof as written.
- **Theorem 1.2**, both halves, for the original unforced equation on `R^3`,
  every `nu > 0`, every `E > 0`, smooth compactly supported solenoidal data,
  local existence only — survives, with the §5 regularity sketch replaced by a
  citation of `prop:localtheory`(iii),(iv) and `lem:upgrade`.
- **Corollary 5.1**, both halves — survives.
- Lemmas 2.1, 2.2, 2.3 — survive; they are the manuscript's
  `lem:quotient-minimizer`, the convexity inequalities behind
  `lem:quotient-stability`, and `prop:quotient-derivative` +
  `lem:quotient-heatsign` + `prop:quotient-evolution`, re-proved for compact
  data. No new content, no conflict.

## 7. Unnecessary dependencies

- **The two-sided estimate is not needed** if Lemma A (oddness of `K`) is used:
  the one-sided display plus oddness gives everything. Recording Lemma A also
  demotes the sentence "both signs of `K` therefore occur" from a result to a
  triviality *conditional on* `K` not vanishing identically — which is the real
  content and which the candidate genuinely establishes.
- **`h` need not be a harmonic gradient near `supp U`.** The proof uses only:
  `h` solenoidal and compactly supported; `h = grad(compactly supported smooth)`
  on a neighbourhood of `supp U`; `U·h = 0` there; and `grad h = S` constant
  there. Harmonicity of `phi` is exactly `tr S = 0`, i.e. `div h = 0` near
  `supp U`, which is already implied. The leading coefficient is
  `<j(U), (U·grad)h> = int |U| U·S U` for any such `S`; the swirl makes
  `U·SU = |U|^2` because `S = diag(1,1,-2)` and `U_3 = 0`. So the general
  statement is: *for any smooth compactly supported solenoidal `U` with
  `div(|U|U) = 0`, and any traceless symmetric `S` with `int |U| U·SU != 0`,
  the same certificate holds with `c_0 = int |U| U·S U`.* This is a cleaner
  lemma than the one written and costs nothing.
- **`w(U) = U` is not needed for the certificate**, only for the clean
  `Q(U) = F(U)` and `<j(U), d_eps> = 0` bookkeeping. It is however what makes
  the competitor argument exact, so keep it.
- **HF19 is genuinely not used.** Confirmed: §2 reproves its inputs and the only
  external theorem is Tao 5.4. The unaudited HF19 notes are motivation only.

## 8. Non-claims (unchanged, and correct as the candidate states them)

- No singular solution, no blowup, no regularity theorem, NS-R3 remains open.
- No unbounded critical norm on a *fixed* trajectory: `||v_0||_3 = b ||V||_3 -> infinity`
  along the family, so the fixed-energy supremum is not a statement about one flow.
- No refutation of `hyp:highstrain` or `hyp:highpressure`. Three independent
  reasons, and the third is one the candidate does not state:
  1. `hyp:highstrain` is a *spacetime* integral bound, not instantaneous;
  2. its remainder `A_input` depends on the entire datum, viscosity, horizon and
     cutoff, not on `E` alone;
  3. **its integrand is `K_L`, the high-frequency piece
     `-int q·((A·grad)(u - S_L u))`, not the full `K`.** Corollary 5.1's second
     half excludes an energy-only bound on the full `K`; it says nothing about
     `K_L`, and the family `b T_lambda V` does not transfer, because the fixed
     low-pass `S_L` is not equivariant under `T_lambda` (the cutoff would have to
     move with `lambda`). This limitation should be stated explicitly wherever
     the result is recorded.
- No novelty claim. Note for the record that the manuscript never asserted
  monotonicity: `rem:qe-evolution-scope` already says the evolution identity
  "supplies neither a sign nor a bound for its right side". So HF20 removes a
  mechanism from the search space; it corrects nothing in the manuscript.

## 9. What this would and would not license in the manuscript

**Would license**, as a scope remark in `sec:quotient` (natural home: next to
`rem:qe-evolution-scope`, or as a second paragraph of `rem:highstrain-scope`):

> There is no monotone mechanism and no instantaneous energy-only absorption
> for `Q`. There exist `U, h in C_c^infty` solenoidal with
> `|K(U + eps h) + eps ||U||_3^3| <= C_* |eps|^{3/2}` for `|eps| <= 1`, hence a
> smooth compactly supported solenoidal field with `K > 0`; by
> `lem:quotient-scaling` and `prop:quotient-evolution`, for every `nu > 0` and
> every `E > 0` there is a divergence-free `v_0 in C_c^infty` with
> `||v_0||_2^2 = E` whose classical branch satisfies `(d/dt) Q(v(t))|_{0+} > 0`,
> and `sup{K(v) - beta nu D_Q(v) : v in C_c^infty solenoidal, ||v||_2^2 = E} = +infinity`
> for every `beta >= 0`. Consequently no strictly increasing function of `Q`
> decreases along all classical trajectories, and no finite `B(E, nu, beta)`
> satisfies `K(v) <= beta nu D_Q(v) + B(E, nu, beta)` pointwise at fixed energy.

**Would not license**, and must be said in the same breath:

- nothing about `hyp:highstrain` (spacetime, datum-dependent remainder, `K_L`
  not `K`) or `hyp:highpressure`; `prop:quotient-conditional` is untouched
  because it consumes the spacetime hypothesis, not a monotonicity statement;
- no change to any lemma, no promotion or demotion of any graph node, no change
  to `hyp:critical`, `thm:conditional`, or `def:target`;
- no claim that the certificate is quantitatively usable: `eps_0 ≈ 6e-21` for
  the fields as written.

The graph change is limited to the HIGH-STRAIN review text gaining one excluded
mechanism class: *universal monotonicity of `Q`, and instantaneous absorption of
the full `K` with an energy-only remainder.*

## 10. Reopening condition

Reopen this audit if any of the following occurs:

1. The two-sided form of Theorem 1.1' is *not* adopted and the note continues to
   use (19)'s first inequality from the one-sided display, without invoking
   Lemma A. That is the defect this review names; a redraft that leaves it in
   place is not repaired.
2. The exclusion is ever stated for `K_L` rather than `K`, or for a spacetime
   rather than an instantaneous inequality, or with a remainder allowed to
   depend on more than `(E, nu, beta)`. Any of those is a strictly stronger
   claim that this argument does not support.
3. `lem:upgrade` or `prop:localtheory`(iii),(iv) is weakened or restated in the
   manuscript, since §5's `v in C^1_t L^3`, `p in W^{1,3}` and pointwise equation
   at `t = 0` rest entirely on them.
4. The manuscript's `lem:quotient-scaling` amplitude law is ever narrowed from
   `alpha in R` to `alpha > 0`, which would remove repair R2's Lemma A.
5. A field `U` with `div(|U|U) = 0` is claimed for which the numerical checks of
   §5.1 above fail at higher precision, or an exact symbolic derivation of
   `<A_0, (h·grad)U> = 0` and `<A_0, (U·grad)h> = c_0` disagrees with §2(f).

---

**VERDICT:** REPAIR
**REVIEWED SCOPE:** §0–§6 of `research/evidence/hf20-harmonic-strain-test.md` and
the frozen PDF in full; Theorems 1.1, 1.2, Corollary 5.1, Lemmas 2.1–2.3,
constructions (9)–(12), estimates (13)–(19), scaling (20)–(21); cross-checked
against `main.tex@39ccb66` `lem:quotient-minimizer`, `lem:quotient-coercive`,
`lem:quotient-scaling`, `lem:quotient-heat`, `prop:quotient-derivative`,
`lem:quotient-pressure`, `lem:quotient-heatsign`, `lem:quotient-transport`,
`prop:quotient-evolution`, `hyp:highstrain`, `prop:quotient-conditional`,
`prop:localtheory`, `lem:upgrade`, `lem:nu-normalisation`, `thm:tao54`.
**FIRST BAD BRIDGE:** Theorem 1.1's display (1.1)/(PDF 2) is one-sided and does
not entail its own corollary sentence, (4.5)/(19) first inequality, or `k > 0`
in §5; the proof establishes the two-sided bound, the statement does not.
**EVIDENCE:** the four-term expansion of `K(v_eps) + eps c_0` is bounded in
absolute value by (15)+(16)+Hölder; substituting `eps -> -delta` into (1.1) as
displayed yields only `K(U - delta h) <= delta c_0 + C_* delta^{3/2}`.
**REPLACEMENT ARGUMENT:** R1, Theorem 1.1' with
`|K(U + eps h) + eps ||U||_3^3| <= C_* |eps|^{3/2}`, same `C_*` of (18), proof as
in §4 of this review; alternatively R2, Lemma A (`K(-v) = -K(v)`,
`D_Q(-v) = D_Q(v)`) with `V := -(U + eps h)`, which needs only the one-sided
display but requires widening the candidate's Lemma 2.1 amplitude law from
`b > 0` to `alpha in R` (the manuscript already proves it there).
**CONDITIONAL SUFFIX THAT SURVIVES:** all of Theorems 1.1', 1.2 and Corollary
5.1, and Lemmas 2.1–2.3, at the candidate's own stated scope, once R1 or R2 is
applied and the §5 regularity sketch is replaced by a citation of
`prop:localtheory`(iii),(iv) and `lem:upgrade`.
**UNNECESSARY DEPENDENCIES:** the two-sided estimate (removable by Lemma A);
harmonicity of `phi` (only `tr(grad h) = 0` is used, already implied by
`div h = 0`); the specific swirl (any smooth compactly supported solenoidal `U`
with `div(|U|U) = 0` and `int |U| U·SU != 0` works, with
`c_0 = int |U| U·S U`); the §5 re-derivation of the local-theory upgrade.
**NON-CLAIMS:** no singular solution; no unbounded critical norm on a fixed
trajectory; no refutation of `hyp:highstrain` (spacetime, datum-dependent
remainder, and `K_L` rather than `K`) or `hyp:highpressure`; no regularity or
blowup result; no novelty claim; no promotion or demotion of any graph node; no
correction to the manuscript, which never asserted monotonicity. NS-R3 remains
open, and the FIRST GAP is unchanged.
**REOPENING CONDITION:** any of §10.1–§10.5 above; principally, adoption of the
result without the two-sided restatement or Lemma A, or any restatement of the
exclusion for `K_L`, for a spacetime integral, or with a remainder depending on
more than `(E, nu, beta)`.
