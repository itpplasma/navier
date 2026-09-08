# Review of HF25, Scope A: the two counterexamples and the sharpness result

Independent proof audit, 2026-09-06. Lens: reconstruct every implication from
the first nontrivial one, recompute every constant, exponent and scaling
relation independently, and try to refute each claimed new fact with an
explicit example, a scaling family or a direct numerical evaluation. Scope A
only. Sections `sec:divcurl`, `sec:weighted`, `sec:criterion` and
`sec:budgets` belong to a different lens and are **not** certified here;
where a Scope A statement consumes one of them this review says so and marks
the consumption explicitly.

## Freeze

| object | identity |
|---|---|
| research HEAD at audit | `a3e85f2d75fb01f1421e95f51ec6f8eedab0ec50` |
| target | `research/evidence/hf25-beyond-hf21-continuation.tex`, sha256 `3ce562bb59346fc700c522bf5e857e3500b318e283febed0c9db9b7f652c6d4f` (1293 lines, read in full) |
| index note | `research/evidence/hf25-beyond-hf21-continuation.md` |
| manuscript | `../navier-paper/main.tex` at `34cdffd2fe2bd8a35068e96f907302e00c10850f` (clean) |
| manuscript revision the candidate pins | `4084330f6b8130241c7afbde3878861229c4cceb` |
| research revision the candidate pins | `b711149aea11d6147c9144fb5431eca4dc1d83af` (resolves in this repository) |
| cited attachment | 23-page **PDF** `navier-divcurl-proof-continuation-2026-09-06.pdf`, sha256 `12163ca4d214c953a097bc9ad24377a54cbf19efab962ae9c6dc629d73ef286b` |
| our HF23 artifact | `research/evidence/hf23-divcurl-continuation.tex`, sha256 `abe74421ef6a8a7bacc108c0c08834e32f2a6116530fceb00368c8e67b129075` |
| audited HF23 Scope B review | `hf23-review-reconstruction-boundary.md` (PASS WITH SCOPE, four repairs) |
| audited HF19-D | `hf19-difference-functional.md` + `hf19-review-difference-functional.md` |
| audited HF20 | `hf20-harmonic-strain-test.md` (post-repair) + its review |
| audited HF21-B | `hf21-crossing-sign-structure.md` (post-repair), Prop. 3.1, Lemmas R1/R2 |
| audited HF22-A/B | `hf22-dissipation-comparison.md`, `hf22-projection-regularity.md` (post-repair) |
| own numerics | reproduced verbatim in Appendix A below (session scratch is not durable); evidence, never proof |

Reviewed scope: `sec:variational` (`lem:minimum`, `lem:cubic`,
`lem:derivative`, the heat/NS subsection, `eq:scaling`), `sec:heatcounter`
(`thm:counter` in full), `sec:sharp` (`eq:swirl`--`eq:Kpositive`,
`thm:alpha` and its remark), `sec:actual` (`thm:Genergy` in full), plus
`cor:Kbounds` and `eq:heatsign`, which Scope A consumes.

## VERDICT SUMMARY

**No invalid or unsupported mathematical bridge was found in Scope A.** Every
construction, constant, exponent, scaling factor and quantifier in
`thm:counter`, `thm:alpha` and `thm:Genergy` was reconstructed independently
and reproduces. The elliptic witness of `thm:counter` was additionally
verified by direct numerical evaluation of the field and of the linearised
cubic flux divergence, to seven digits.

Three **statement-level** defects, none of them invalid mathematics, all
about novelty and attribution against this repository's own audited record,
are recorded with displayed replacements in §7:

- **S1** the ledger row "Dissipation comparison | **New** candidate
  counterexample" and the index note's sentence "exactly the explicit witness
  that the audited HF22-A lane identified as missing" are both wrong. The
  audited **HF19-D Proposition 3.4 + Corollary 3.5**, present in the tree at
  the revision HF25 pins, already constructs an explicit compactly supported
  smooth solenoidal member of `M` that leaves `M` under linear heat flow, by
  the same mechanism and the same identity, and already concludes
  `D_3(w) > D_3(v)` at a fixed time. What is new in HF25 is only the
  **quantitative** early-time rate.
- **S2** HF25 still produces the witnessing *time* by an averaging/mean-value
  existence step, and `c_*` is not exhibited numerically. HF22-A's stated
  first gap ("an explicit witness with all quantities computed", plus a lower
  bound for the ratio) is therefore **narrowed, not closed**.
- **S3** `cor:Kbounds`' second estimate `|K| <= C_# d_1 D`, `C_# = (3/2)C_9 S`,
  is presented as this note's own corollary. It is verbatim the audited
  **HF21-B Proposition 3.1 (3.1)**, constant included. `thm:Genergy` and
  `thm:alpha` both consume it, so the attribution matters.

Two further findings, both favourable:

- `thm:alpha` **is** genuinely new against the audited record and is stronger
  than HF25 itself realises: the audited HF22-B already cut the open interval
  from `(1,2]` to `(1,3/2]` by the same `2/3`-Hölder bound HF25 rederives as
  `eq:twothirds`; `thm:alpha` closes `(1,3/2]` as well, so after this note
  **every** `alpha > 1` in the monomial class is refuted.
- `eq:dual-lip` (`A : L^3 -> L^{3/2}` is locally **Lipschitz**, constant
  `2(||w_1||_3+||w_0||_3)`) is a strict improvement on the manuscript's
  audited `lem:quotient-stability` rate, proved without differentiating the
  minimizer. It is a by-product of Scope A that Scope B should pick up.

**Verdict: PASS WITH SCOPE (three attribution repairs required before any
integration; no mathematical repair required).**

---

## 0. The hash cross-check demanded by the controller

HF25 cites the div--curl source as a **23-page PDF**,
`navier-divcurl-proof-continuation-2026-09-06.pdf`, file id
`file_00000000e830824398374f7112f73179`. Our HF23 artifact is a `.tex` source.
A PDF and its LaTeX source never share a SHA-256, so the hash discrepancy is
**explained** and is not evidence of two different documents. It is also not
proof of identity, and this review did not assume identity.

What can be checked is the internal numbering and content HF25 attributes to
the attachment. Every attribution used in Scope A resolves exactly:

| HF25 attribution | our `hf23-divcurl-continuation.tex` | match |
|---|---|---|
| "Theorem 3.1: candidate unweighted div--curl estimate" | `sec:regularity` is §3, `thm:main` is its first theorem, "Unweighted regularity and quantitative bounds" | yes |
| "Theorem 4.2: mixed-pressure identity" | `sec:mixed` is §4, `cor:sigma` is 4.1, `thm:mixed` is 4.2 | yes |
| "Theorem 7.1: fixed-energy spacetime obstruction" | `sec:spacetime` is §7, `thm:spacetime` is its only theorem, "Fixed-energy spacetime excess" | yes |
| "[Attachment, Section 6]" for the harmonic-strain construction | `sec:hf20` is §6, "Reconstruction and scope review of the attached HF20 proof" | yes |
| the fields `b`, `s(r,z)`, `U=s e_theta`, `zeta`, `a=(yz,-xz,0)`, `phi`, `h=curl(zeta a)`, `g=grad(zeta phi)`, `e=h-g` | identical, item by item, per the HF23 Scope B review table §1.1 | yes |
| `C_e=||e||_3^3/3`; `int rho|d|^2<=4C_e|eps|^3`; `||d||_3^3<=6C_e|eps|^3` | identical | yes |
| `C_*=4 sqrt(C_e)||U||_5^{5/2}+4C_e||U||_inf+M^2||N_2||_3+L(||N_1||_3+||N_2||_3)` | identical | yes |
| `c_0=||U||_3^3`, `<A_0,N_0>=0`, `eps_0=min{1,(c_0/(2 max{1,C_*}))^2}` | identical | yes |
| "its arbitrary-data signed estimate remains explicitly open" | `sec:frontier` §"The hypothesis that is still not proved" | yes |

**No attribution to the attachment used anywhere in Scope A exceeds what our
audited HF23 actually proves.** Two calibration notes:

- HF25 calls Theorem 3.1 a *candidate* estimate and says "Inherited candidate
  proof reconstructed ... if independently accepted". That is *more*
  conservative than our record: HF23 Scope A is audited PASS and the result
  now sits in the manuscript as `prop:quotient-divcurl` with
  `lem:trace-control`. No correction needed; the candidate simply did not
  know.
- HF25 does **not** import Theorem 7.1 as a black box. It reproves the entire
  common-interval / commutator / scaling chain of `thm:Genergy` from scratch.
  So the attachment identity question is not load-bearing for Scope A at all:
  removing every citation to `\cite{Attachment}` from `sec:sharp` and
  `sec:actual` leaves both proofs complete, because `sec:sharp` also restates
  the whole construction. This is recorded under UNNECESSARY DEPENDENCIES.

One inherited defect. `eq:evolution`'s justification ("On a compact classical
interval the normalized pressure is in `W^{1,3}`, so `grad p` in `G`, by
cutoffs and mollification") is the same one-sentence compression that the
HF20 audit ruled "not a proof at this tier" and that the HF23 Scope B review
recorded as repair **R1**. HF25 repeats it and does not carry the citation
repair to `prop:localtheory`(iii),(iv) and `lem:upgrade`. **It is not
load-bearing in Scope A**: `thm:counter` uses only `e^{t Delta}`, and
`thm:Genergy` never differentiates `Q` along a trajectory. Recorded, not
charged.

---

## 1. Check (1): does the explicit field really lie in the nonlinear-Hodge class?

This is the load-bearing new object, so it was rebuilt from scratch and then
evaluated numerically.

### 1.1 The construction, reconstructed

`gamma(theta)=(2 cos theta, sin theta)`, `m(theta)=(4 sin^2+cos^2)^{1/2}`.
Recomputed: `gamma'=(-2 sin, cos)`, `|gamma'|=m`,
`kappa=|gamma' x gamma''|/m^3 = (2 sin^2+2 cos^2)/m^3 = 2/m^3` ✓.
With `m^2 = 1+3 sin^2 theta`, `m' = 3 sin cos/m`, so
`dkappa/dtheta = -18 sin cos/m^5` and `kappa_s = (1/m) dkappa/dtheta =
-18 sin theta cos theta/m^6` ✓, exactly `eq:frenet`. The orientation
convention is consistent: at `theta=0`, `n=(1,0)` is outward and
`T=Jn=(0,1)=gamma'/m`, and for a counterclockwise convex curve with outward
`n` the Frenet pair is `T_s=-kappa n`, `n_s=kappa T` ✓.

`d` is the signed distance in a two-sided tube, `grad d = n`, `T = J grad d`.
Then, with `U = f(d) g(z) (T,0)`:

- `div U = g[f'(d) n.T + f div(J grad d)] = 0`, because `n.T=0` and
  `div(J grad d) = -partial_x partial_y d + partial_y partial_x d = 0` ✓;
- `|U| = f g |grad d| = f g` since `|grad d| = 1`, and `f,g >= 0` ✓;
- `div(|U|U) = div(f^2 g^2 T) = g^2 grad(f^2).T + f^2 g^2 div T = 0`, both
  terms vanishing for the same two reasons, the third component of `|U|U`
  being identically zero ✓.

So `U in M`, hence by `lem:minimum` (stationarity is sufficient by convexity)
`w(U)=U`, `q(U)=0`, `F(U)=Q(U)` ✓. Smoothness and compact support: `chi` is
the standard flat plateau (`eta(1-r^2)` vanishes to infinite order at
`r=+-1`, denominator `>= eta(3/4)>0`), so `f(d)=chi(d/delta)` is flat at
`|d|=delta` and the extension by zero across the tube boundary is `C^infty`;
the tube itself is a genuine normal-coordinate neighbourhood by the
compactness/injectivity argument, which is correct as written ✓.

### 1.2 Independent numerical evaluation

The script of Appendix A builds `U` from the *exact* signed distance (Newton on
`(p-gamma(theta)).gamma'(theta)=0`), with `delta=0.1`, and evaluates by
fourth-order finite differences.

At `theta=pi/4, d=0, z=0`:

    div U            = 9.9e-12
    |U|              = 1.0000000
    |grad U|^2       = 0.255999999999  vs kappa^2 = 0.256000000000
    div(|U|U)        = 9.9e-12

Over 6 random points of the tube with `f`, `g` both varying, refining
`h = 1e-3, 3e-4, 1e-4`, both `|div U|` and `|div(|U|U)|` fall at fourth order
to `1e-9` and below; e.g. one point gives
`1.65e-03 -> 1.35e-05 -> 1.67e-07`. That is clean discretisation error
converging to zero, not a residual.

**Refutation attempt 1 (class membership) fails.** The field is genuinely
compactly supported, smooth, solenoidal and in `M`, exactly.

---

## 2. Check (2): does it leave the class under heat flow, and is the quadratic
bound right?

### 2.1 The linearised flux divergence

`Dj(z) = |z|(I + zhat (x) zhat)`, so on the plateau `|U|=1` and
`Dj(U) = I + U (x) U` ✓ as `eq:heatH` states. Then

    H = div(Dj(U) Lap U) = div(Lap U) + div((U.Lap U) U)
      = Lap(div U) + U.grad(U.Lap U) = -U.grad|grad U|^2,

using `div U = 0` and, where `|U|^2 = 1`, `Lap|U|^2 = 0 => U.Lap U =
-|grad U|^2` ✓. Both the algebra and the restriction of the second identity
to the plateau are correct; nothing about an evolution of the minimizer is
used.

In normal coordinates the tangential scale factor is `1+d kappa(s)` and `T`
depends on `s` only, so `partial_{e_1} T = -kappa n/(1+d kappa)` and
`partial_{e_2} T = 0`, giving `|grad U|^2 = kappa(s)^2/(1+d kappa(s))^2` ✓
(confirmed numerically to twelve digits at `d=0`). At `d=z=0`,
`U.grad = partial_s`, so `H = -partial_s(kappa^2) = -2 kappa kappa_s` ✓.
At `theta=pi/4`, `sin cos = 1/2`, `m^2=5/2`:

    H = 72 sin cos/m^9 = 36 (2/5)^{9/2} = 0.5828710183 > 0.

Numerically, `div(Dj(U) Lap U)` evaluated directly at that point by nested
fourth-order differences gives **0.5828710787**, agreeing to `1e-7`
relative. **Refutation attempt 2 fails.**

### 2.2 Cross-check against the audited HF19-D identity

This is the decisive independent confirmation, and it also settles the
novelty question. Audited **HF19-D Proposition 3.4** gives, for
`u_0 = f(x_3) phi(d) T` on a strictly convex curve,

    R(u_0) := partial_s(v_s . grad|v_s|^2)|_{s=0} = -4 kappa kappa_s phi^3/J^4,
    J = 1 + kappa d,

verified there twice by hand and once symbolically, and re-derived by a third
route in audited **HF22-A** and a fourth in its audit. Audited HF22-A
Lemma 2.3 gives `R = 2|v| N(v)` on `M`, with `N(v) = div(Dj(v) Lap v)`, i.e.
exactly HF25's `H`. Substituting `|v| = phi`:

    H = R/(2 phi) = -2 kappa kappa_s phi^2/J^4,

which at the plateau (`phi = 1`) and `d = 0` (`J = 1`) is **`-2 kappa
kappa_s`**, HF25's value on the nose. HF25 and the audited record agree
exactly, by three prior independent derivations plus this audit's numerics.

### 2.3 The quadratic gap and its constant

`div j(v(t)) = t H + o(t)` uniformly on compact subsets of `O`: `v(t) =
e^{t Lap}U = U + t Lap U + o(t)` in every `C^k`, `v(t)` is bounded away from
zero on `O`, and `j` is smooth off the origin, so `t |-> j(v(t))` is `C^1`
into `C^1(closure O)` with derivative `Dj(U) Lap U` at `0` ✓. Nonvanishing
then gives non-stationarity, hence `v(t) != w(v(t))` by uniqueness of the
minimizer, hence `F(v(t)) - Q(v(t)) > 0` ✓.

The competitor step. `psi in C_c^infty(O)`, `psi >= 0`, `psi != 0`;
`c = int H psi > 0` because `H > 0` on `O`; `B = int Dj(U) grad psi . grad psi
> 0` because `I + U (x) U >= I` and `grad psi != 0` ✓; `a = c/B`.
`int j(v(t)).grad psi = -int div j(v(t)) psi = -ct + o(t)` ✓. The competitor
`v(t) + a t grad psi` is admissible, `grad psi in G` ✓. Second-order Taylor
of `F` at `v(t)`:

    F(v+h) - F(v) = int j(v).h + (1/2) int Dj(v) h.h + R,   |R| <~ int |h|^3/|v|,

the remainder bound because the third derivative of `|z|^3/3` is `O(1/|z|)`
and `|v(t)| >= 1/2` on `supp psi` for small `t`. With `h = a t grad psi` this
is `O(t^3) = o(t^2)` ✓, and `Dj(v(t)) -> Dj(U)` uniformly on `supp psi` ✓.
Hence

    F(v(t)+a t grad psi) - F(v(t)) = -a c t^2 + (a^2 B/2) t^2 + o(t^2)
                                   = -(c^2/(2B)) t^2 + o(t^2),

so `F(v(t)) - Q(v(t)) >= (c^2/(4B)) t^2` for small `t`, `c_* = c^2/(4B)` ✓.
Recomputed; correct.

The order is sharp, not inflated. Two independent order checks:
`Q(v) >= (1/6)||q(v)||_3^3` (audited HF19-D Prop. 1.2) would give only `t^3`
from the linear response `||q(v(t))||_3 = O(t)`, so `t^2` is *stronger* than
the audited coercivity supplies; and the linear-response heuristic
`F - Q ~ (1/2) int Dj(U) q.q ~ ||q||^2 ~ t^2` gives exactly `t^2`. The two
brackets are consistent (`t^3 <= t^2`). **Refutation attempt 4 (order
inflation) fails.**

The dissipation reversal. `dF(v(t))/dt = int j(v).Lap v = -D_3(v)` with
`D_3(v) = int|v|(|grad v|^2 + |grad|v||^2)`, which is *exactly* the
manuscript's `def:D3P3` (there written `int(|u||grad u|^2 +
|(grad u)^T u|^2/|u|)`, the two forms agreeing since
`grad|u| = (grad u)^T u/|u|`, with the audited `0` convention on `{u=0}`) ✓.
`dQ(v(t))/dt = <A(v),Lap v> = -D_Q(v)` by `lem:derivative` ✓. Since
`F(U)=Q(U)`, integration gives `int_0^t (D_Q - D_3) ds = F(v(t)) - Q(v(t))
>= c_* t^2`, so some `s in (0,t)` has `D_Q(v(s)) - D_3(v(s)) >= c_* t > 0` ✓.
`v_* = e^{s Lap}U` is real, solenoidal and Schwartz ✓.

**`thm:counter` is proved, both halves.**

### 2.4 Is the constant "specified by the test functions"?

Partly. `c_*` is *determined* once `delta`, the patch `O` and `psi` are
fixed, and the theorem says so honestly ("specified by compact smooth test
functions in the proof"). But `delta`, `O` and `psi` are only asserted to
exist; no `psi` is exhibited, and the smallness threshold on `t` is not
quantified. So `c_*` is **not an explicit number**, and the note should not
be read as supplying one. This is the precise sense in which HF22-A's gap is
narrowed rather than closed (§4 below). The only quantity actually computed
in this construction is `H(pi/4,0,0) = 36(2/5)^{9/2}`.

---

## 3. Check (3): heat path versus Navier--Stokes trajectory

No confusion anywhere in Scope A.

- `thm:counter`'s statement carries "The heat path is an auxiliary test, not
  asserted to solve Navier--Stokes", and its scope remark repeats that the
  auxiliary path is not an NS trajectory and that nothing follows about the
  growth of `F - Q` along NS trajectories. Correct and sufficient.
- The conclusion drawn is `D_Q(v_*) > D_3(v_*)` for a **single real
  solenoidal Schwartz field at a fixed time**. That is exactly the shape of
  HF21 sub-question (a) as the plan poses it ("is the quotient dissipation at
  most the velocity dissipation at fixed time") and as audited HF19-D poses
  it ("on the class of Schwartz solenoidal fields, equivalently of initial
  data of classical solutions"). The direction refuted is `<=`, which is the
  direction the plan hoped for. ✓
- `sec:variational` keeps the two evolutions separate explicitly:
  `eq:heatsign` is the heat-generator sign, `eq:evolution` is the actual NS
  identity with the original pressure, and the text says "This equation uses
  the original pressure and velocity, not an auxiliary nonlinear diffusion".
- `thm:Genergy` uses only genuine solutions of the original unforced equation
  (at viscosity `mu`, then rescaled to exactly `nu`); no heat path enters.

**Refutation attempt 12 (a heat path smuggled in as a trajectory) fails.**

---

## 4. Check (4): consistency with the audited HF19-D and HF22-A

### 4.1 No contradiction anywhere; HF25 is strictly weaker qualitatively

Audited **HF19-D Corollary 3.5** already proves that *both* `D_3(w) <= D_3(u)`
and `D_3(w) >= D_3(u)` fail on the class of Schwartz solenoidal fields, both
signs occurring along one heat trajectory started at the elliptic swirl.
HF25's `thm:counter` proves only the failure of `<=`. So HF25 is a proper
sub-statement of an audited result, and there is nothing to adjudicate.

A sharper consistency test, and it passes. Audited HF19-D **Theorem 3.2**
gives `int_0^infty (D_3(G_s u_0) - D_3(w(G_s u_0))) ds = Delta(u_0)`. For
`u_0 in M` the right side is **zero**. HF25's second inequality in
`eq:heatgap` asserts `int_0^t (D_Q - D_3) ds >= c_* t^2 > 0` for small `t`.
These are compatible only if the early positive excess is exactly cancelled
later along the same trajectory — which is precisely the mechanism of
HF19-D's Corollary 3.5 (`Delta` rises off `0`, then decays back to `0`). The
two results interlock rather than compete. **Refutation attempt 5 fails.**

### 4.2 The novelty claim is wrong, and this is finding S1

The candidate's ledger row reads "Dissipation comparison | **New** candidate
counterexample", and its `sec:literature` bounded-search paragraph says no
exact prior match was found for "the two counterexample conclusions". The
repository record says otherwise, at the very revision HF25 pins:

    git show b711149:research/evidence/hf19-difference-functional.md
      380: Proposition 3.4 (the elliptic swirl leaves M)
      456: Corollary 3.5 (the "<=" direction fails; both signs along one trajectory)

and `hf19-review-difference-functional.md` was already in that tree. The
construction is the *same object*: a compactly supported smooth solenoidal
tangent field on a tube around a non-circular strictly convex plane curve,
times a cutoff in `x_3`, shown to be in `M`, shown to leave `M` under
`e^{s Lap}`, by an identity that reduces to `-2 kappa kappa_s` at the core
curve. HF25's ellipse is a specialisation of HF19-D's `Gamma`; HF25's
two-sided plateau tube versus HF19-D's exterior annulus is a cosmetic
difference.

HF25 could not see this from `PLAN.md` at `b711149` (the HF19 summary there
describes only the difference-functional evolution, and the HF22 section did
not yet exist), and HF25's declared reads are `PLAN.md`, `docs/proof.md` and
the two HF21 notes. The miss is understandable. The claim is still false
against our record and must be corrected before integration.

### 4.3 What actually is new, precisely

Three things, all real but all smaller than the index note says:

1. **A quantitative early-time rate.** `F(v(t)) - Q(v(t)) >= c_* t^2`, hence
   `D_Q(v(s)) - D_3(v(s)) >= c_* t` for some `s in (0,t)`. HF19-D has only
   `Delta(G_s u_0) > 0`, with no rate, and its audit records no rate. This is
   the single genuinely new mathematical fact in `sec:heatcounter`.
2. **One computed quantity**, `H(pi/4,0,0) = 36(2/5)^{9/2} ~ 0.5829`, on a
   fully specified curve. HF19-D leaves `Gamma` generic.
3. A clean statement of the competitor mechanism (`Q(v(t)) <=
   F(v(t) + a t grad psi)`) that yields the rate without differentiating the
   minimizer.

### 4.4 HF22-A's gap is narrowed, not closed — finding S2

Audited HF22-A states its first gap exactly:

> "An explicit witness with all quantities computed (task item 3) is
> therefore **not delivered**. The audited refutation is an existence
> argument (mean value theorem in `s`), and this lane supplies the machinery
> for an explicit one (Cor. 3.5) but not the evaluation; the size of the
> failure, i.e. questions (C1)/(C2) of §4, is untouched."

Measured against that sentence, HF25 delivers:

| HF22-A's deficiency | HF25 |
|---|---|
| witnessing time `s` obtained by a mean value theorem | **still existential** — "Its positive average implies that for some `s in (0,t)`" |
| no quantity computed | one computed: `H` at one point. `c_*`, `delta`, `O`, `psi` and the `t`-threshold remain unexhibited |
| no lower bound for the ratio `D_Q/D_3` | **none supplied**; only an additive lower bound at an unknown time |
| questions (C1)/(C2), i.e. comparison with a constant `C > 1` | **untouched**, and `thm:counter`'s remark says so correctly |

So the index note's "This is exactly the explicit witness that the audited
HF22-A lane identified as missing from its own existence argument" and
`PLAN.md`'s "with a constructed field rather than an existence argument,
which is exactly the witness the audited HF22-A said it had not delivered"
are both **overclaims on both halves**: the field was already constructed
(HF19-D), and the argument is still existential in `s`.

### 4.5 No conflict with the audited scoping

HF22-A's applied repair insists that the licensed manuscript sentence must
say "no comparison with constant `1` holds in either direction" and must
**not** say the comparison is refuted, since `C > 1` is open. HF25's own
scope remark says "The construction also does not refute comparison estimates
with a larger constant or an additional term". The two agree. ✓

---

## 5. Check (5): the sharpness result and the Lipschitz direction

### 5.1 The competitor gain, recomputed

`U = s(r,z) e_theta`, `s = b(4r-6)b(2z)`: `div U = 0` and `div(|U|U) = 0` by
azimuthal independence with `|U| = s >= 0`; `N(U) = (U.grad)U =
(rho/r) rho partial_theta e_theta = -(rho^2/r) e_r`, so `U.N(U) = 0` and
`w(U) = U` ✓. Support `5/4 < r < 7/4`, `|z| < 1/2`, so
`|x|^2 <= (7/4)^2+(1/2)^2 = 3.3125 < 9` and `zeta == 1` on a neighbourhood of
`supp U` ✓. There `curl a = (x,y,-2z) = grad phi`, so `h = g`,
`grad h = diag(1,1,-2)`, `U.h = 0` ✓, and `e = h-g` vanishes on `{|x|<3}`, so
`supp e` and `supp U` are disjoint ✓. Every item matches the audited HF20
record and the HF23 §6 reconstruction.

`Q(v_eps) <= F(U + eps e) = F(U) + C_e|eps|^3` because `U + eps e = v_eps -
eps g` with `g in G`, and `|U+eps e|^3 = |U|^3 + |eps e|^3` pointwise by
disjoint supports ✓. `<j(U), d_eps> = 0` because `d_eps = q(v_eps) + eps h`,
`<j(U),q(v_eps)> = 0` by stationarity at `U in M`, and `<j(U),h> = 0` by
`U.h = 0` on `supp U` ✓. Hence `Q(v_eps) - Q(U) = int B(U,d_eps) >= 0` and,
with `eq:bregman`,

    int rho|d_eps|^2 <= 4 C_e |eps|^3,     ||d_eps||_3^3 <= 6 C_e |eps|^3.  ✓

Recomputed; identical to the audited HF20 constants.

`<A_0,N_1> = c_0 = ||U||_3^3`: `<j(U),(h.grad)U> = int (h.grad)(|U|^3/3) = 0`
by `div h = 0`; `(U.grad)h = grad h . U = (U_1,U_2,-2U_3) = U` because
`U_3 = 0` for an azimuthal swirl, so `<j(U),(U.grad)h> = int|U|^3` ✓. The
error constant

    C_* = 4 sqrt(C_e)||U||_5^{5/2} + 4C_e||U||_inf + M^2||N_2||_3
          + L(||N_1||_3 + ||N_2||_3),   L = (2M+d_0)d_0, d_0 = (6C_e)^{1/3},

was rebuilt term by term: `|N_0| <= rho^2` (since `r >= 5/4 > 1`),
`|A_eps-A_0| <= (2rho+|d_eps|)|d_eps|` from `eq:jlip`, Cauchy--Schwarz on
`rho^{1/2}|d_eps|` against `rho^{5/2}`, `rho^2 <= ||U||_inf rho`,
`||A_eps||_{3/2} <= M^2 + L|eps|`, and `eps^2 <= |eps|^{3/2}` for `|eps|<=1`.
Every coefficient reproduces ✓. Hence `|K(U+eps h) + c_0 eps| <=
C_*|eps|^{3/2}` and `K(U - eps h) >= c_0 eps/2` for
`eps < min{1,(c_0/(2 max{1,C_*}))^2}` ✓ — the audited **two-sided** HF20
display, correctly used.

### 5.2 The Lipschitz-scale observation, and the direction

`eq:directionallip`: `q(v_eps) = w_eps - v_eps = d_eps - eps h`, so
`||q(v_eps)||_3 <= (6C_e)^{1/3}|eps| + ||h||_3 |eps| = B_q|eps|` ✓. This is a
one-line consequence of the audited HF20 gain, and HF25 says so ("The
stronger competitor estimate already present in HF20 closes this interval").

**The direction is correct, and HF25 does not conflate it.** The audited
HF21-B repair (Lemma R2) states: an `alpha > 1` bound *forces* the projection
to be non-Lipschitz; Lipschitz behaviour at `M` *refutes* `alpha > 1`. HF25
uses it in exactly that direction: it supplies the Lipschitz-scale bound and
derives the contradiction. Its remark is explicit that `eq:directionallip` is
"an anchored bound along one explicit direction at one member of `M`" and
"neither asserts a two-point Lipschitz estimate in a neighborhood nor settles
Lipschitz regularity of the nonlinear projection at every member of `M`".
That is precisely right, and it is exactly the hypothesis HF21-B Lemma R2(2)
needs — R2(2) as displayed assumes the stronger two-point bound
`||q(U+z)||_3 <= C(U)||z||_3`, but its proof consumes only the one direction
`z = -eps h`. So `thm:alpha` is HF21-B R2(2) instantiated with a hypothesis
that is *available* rather than assumed.

The contradiction, recomputed: apply `eq:superlinear` at `v_{-eps}`;
LHS `>= c_0 eps/2`; `Q(v_eps) >= Q(U) > 0` (from `eq:epsgain`, needed because
`(1-alpha)/3 < 0`); `D_Q(v_eps) <= ||v_eps||_3^2||Lap v_eps||_3 <= D_max`
uniformly for `|eps| <= 1` by `eq:heatsign` and `U,h in C_c^infty`; RHS
`<= C B_q^alpha Q(U)^{(1-alpha)/3} D_max eps^alpha`. Divide by `eps`:
`c_0/2 <= const . eps^{alpha-1} -> 0` ✓. Valid for every `alpha > 1`. The
`|K|` version follows since `|K| >= K` ✓. `v_eps = U + eps h` is real,
solenoidal, `C_c^infty`, hence Schwartz ✓. **Refutation attempts 7 and 8
fail.**

Scaling sanity: `eq:superlinear` has `b = (1-alpha)/3`, `c = 1`, so
`alpha + 3b = 1` — exactly the admissible segment of the audited HF21-B
Proposition 3.2 scaling lattice ✓. The family is therefore not
scaling-degenerate.

### 5.3 `thm:alpha` is new, and stronger than HF25 realises

HF25 says it closes `(1,2]`, quoting HF21-B. The audited **HF22-B** already
cut that to `(1,3/2]`, by exactly the `2/3`-Hölder bound that HF25
independently rederives as `eq:twothirds` (recomputed here: from
`int B(w_0,d) <= int B(w_0,h)`, `B(a,h) <= |a||h|^2 + |h|^3/3` and
`B(a,d) >= |d|^3/6`, one gets `||d||_3^3 <= 6||w_0||_3||h||_3^2 +
2||h||_3^3` ✓, i.e. `beta = 2/3`, exactly HF22-B's rate). HF22-B's table
reads: `alpha=1` audited true; `(1,3/2]` **open**; `(3/2,2]` refuted;
`alpha>2` refuted.

`thm:alpha` closes the last open interval `(1,3/2]`. **After this note, every
`alpha > 1` in the class `L(alpha): |K| <= C d_1^alpha Q^{(1-alpha)/3} D_3(w)`
is refuted and `alpha = 1` is sharp there, unconditionally.** That is a
strictly stronger and cleaner statement than HF25 itself claims, and it is
the most valuable result in Scope A.

---

## 6. Check (6): the energy-only failure on actual trajectories

### 6.1 Reconstructed in full; correct

**Common interval.** `Z = ||v^mu||_{H^6}`; the pressure terms and the
undifferentiated transport term vanish and the viscous term has a good sign,
so it is *discarded*, not divided by, and nothing degenerates as `mu -> 0`.
The commutator split was rechecked at the boundary: for `|gamma| <= 4`,
`partial^gamma v in L^infty` needs `H^{|gamma|+2} subset H^6` ✓ and the
partner `partial^{alpha-gamma} grad v` has order `<= |alpha|-|gamma|+1 <= 6`
in `L^2` ✓; for `|gamma| >= 5` the partner has order `<= 2` and needs
`H^2 -> L^infty`, available in `H^4 subset H^6` (and `H^2(R^3) -> L^infty` is
true, `2 > 3/2`) ✓. Hence `Z' <= C Z^2` uniformly in `mu <= 1`, giving
`T_0, B` depending only on `W`, and the fixed-`mu` `H^1` blow-up alternative
upgrades the a priori bound to existence past `T_0` ✓. This is HF04's
mechanism transcribed, as HF23 Scope B already recorded; HF25 reproves it.

**Uniform positivity.** `||partial_s v^mu||_{H^4} <= ||P N(v^mu)||_{H^4} +
mu||Lap v^mu||_{H^4} <= C(B^2+B)` using `mu <= 1` ✓, so
`||v^mu(s)-W||_{H^4} <= C_B s` uniformly in `mu`. `N` is Lipschitz from
bounded `H^4` sets into `L^3` and `A` is continuous (in fact Lipschitz, by
`eq:dual-lip`) from `L^3` into `L^{3/2}`, so `K(v^mu(s)) -> K(W)` uniformly
in `mu` and one `s_0 in (0,T_0)`, independent of `mu`, gives
`K(v^mu(s)) >= k/2` ✓.

**The `G` lower bound.** `|K| <= C_# d_1 D` gives `d_1 D >= k/(2C_#)` on
`[0,s_0]`, hence `eq:Gbase` ✓.

**Scaling back.** Rederived from scratch: with `u(t,x) = c v(alpha t,
lambda x)` the three inertial terms carry `c alpha`, `c^2 lambda`,
`c^2 lambda`, and the viscous term `nu c lambda^2`; matching forces
`alpha = c lambda` and `mu = nu lambda/c`. With `c = b lambda` this is
`alpha = b lambda^2`, `mu = nu/b` ✓, exactly HF25's substitution.
`||b T_lambda W||_2^2 = b^2 lambda^{-1} E_W = E` fixes
`lambda = b^2 E_W/E` ✓, and `tau_b = s_0/(b lambda^2) = s_0 (E/E_W)^2 b^{-5}`
✓. By `eq:scaling`, `||q||_3` carries `b`, `D_Q` carries `b^3 lambda^2`, and
`dt` carries `(b lambda^2)^{-1}`, so `G_b(tau_b) = b^3 int_0^{s_0}
||q(v^{nu/b})||_3 D_Q(v^{nu/b}) ds >= (k s_0/(2 C_#)) b^3 -> infinity` ✓.
`tau_b -> 0`, so `tau_b < H` for large `b`, and `tau_b < T_0/(b lambda^2) <=
T_*(u_b)` strictly, so the endpoint quantifier of `eq:G` is respected ✓
(the same point on which the HF04 audit had returned REPAIR; HF25, like
HF23, chooses `s_0` strictly inside).

**Refutation attempts 10 and 11 fail.** No `b`-dependence hides in
`k s_0/(2C_#)`: `k = K(W)` and `C_#` are fixed and `s_0` is uniform in
`mu <= 1`. And the family cannot be turned into a contradiction with `(G)`
under whole-datum dependence, because `||u_b(0)||_3 = b||W||_3 -> infinity`
and `Q(u_b(0)) = b^3 Q(W) -> infinity`; each `b` is a different datum with
its own vanishing witnessing interval. HF25 states both facts.

### 6.2 What is genuinely new here

Very little of the mechanism, but the statement is new.

- **Not new:** the sign certificate and its two-sided form (audited HF20,
  manuscript `rem:no-monotone`); the fixed-energy *instantaneous* supremum
  (audited HF20); the vary-viscosity-then-rescale method (audited HF04); the
  uniform-in-`mu` `H^6` interval, the `H^4` time-derivative bound, the
  uniform positivity of `K`, and the `b^3` / `b^{-5}` exponent count (audited
  HF23 Scope B `thm:spacetime`, confirmed by its review §2.1--§2.3); the
  bound `|K| <= C_# d_1 D` (audited HF21-B Prop. 3.1 — finding S3).
- **New:** the composition. `thm:Genergy` is HF23 `thm:spacetime`'s machinery
  plus HF21-B (3.1), yielding the exclusion for the *specific* functional
  `G(tau) = int ||q||_3 D_Q dt` rather than for `int K - beta nu int D_Q`.
  Two lines of new inference on top of two audited results. HF25 says exactly
  this ("a consequence of the HF20 sign field and the actual-trajectory
  scaling argument in the attachment, now stated for the current quantity
  `G`"), so there is no overclaim here.
- **Not attempted, and not needed:** HF25 does not handle the fixed
  high-strain cutoff `K_L`. HF23 Scope B's second upgrade (`K -> K_L` for
  every fixed `L`) is therefore *not* reproduced, and `thm:Genergy` says
  nothing about `hyp:highstrain`. HF25 does not claim otherwise.

Consistency with the audited HF21-B crossing bound: on this family
`int_0^{tau_b} d_1^4 dt = O(b^{-1}) -> 0` while the input-only budget
`24 C_S^2 C_#^4 E^2 nu^{-5}` is a fixed constant, so the bound is not binding
— the same check the HF23 Scope B review ran on its own family, with the same
conclusion ✓.

---

## 7. Replacement text for the three attribution defects

These are the exact substitutions. Nothing mathematical changes.

**R-S1.** In the ledger of `sec:literature`, replace the row

> Dissipation comparison & New candidate counterexample: mark the universal
> `D_Q <= D_3(u)` proposal false after audit.

by

> Dissipation comparison & **Not new as a qualitative fact.** The audited
> `hf19-difference-functional.md` (Proposition 3.4, Corollary 3.5), present
> at the pinned research revision, already exhibits an explicit compactly
> supported smooth solenoidal member of `M` that leaves `M` under linear heat
> flow and already refutes **both** directions of the comparison with
> constant `1`. What is new here is the quantitative early-time rate
> `F(v(t)) - Q(v(t)) >= c_* t^2` and the evaluation
> `H(pi/4,0,0) = 36(2/5)^{9/2}` on a fully specified curve.

and in `sec:literature`'s bounded-search paragraph, replace "did not
establish an exact prior match for the two counterexample conclusions" by
"did not establish an exact prior match in the external literature; within
the repository, the qualitative dissipation-comparison conclusion is prior
art (audited HF19-D Corollary 3.5) and only the quantitative rate is new".

**R-S2.** In `thm:counter`'s scope remark, add:

> The witnessing time `s` is obtained from a positive average and is not
> exhibited; `c_* = c^2/(4B)` is determined by `delta`, the patch `O` and the
> test function `psi`, none of which is fixed numerically, and the smallness
> threshold on `t` is not quantified. No lower bound for the ratio
> `D_Q(v_*)/D_3(v_*)` is obtained. The explicit-witness-with-computed-
> quantities question raised in `hf22-dissipation-comparison.md` is therefore
> narrowed, not closed.

**R-S3.** In `cor:Kbounds`, add after the display:

> The second estimate, with the constant `C_# = (3/2) C_9 S`, is the audited
> `hf21-crossing-sign-structure.md` Proposition 3.1 (3.1); it is reproduced
> here for self-containedness and no novelty is claimed for it. It is itself
> recorded there as a strengthening of the line preceding the audited HF18-A
> Theorem 4 substitution, not as a new theorem.

**Optional, and recommended.** In the remark after `thm:alpha`, replace "the
interval `(1,2]` not excluded by the repaired HF21 Hölder-only argument" by

> the interval `(1,3/2]` left open by the audited record: the repaired HF21-B
> Hölder-only argument excludes `alpha > 2`, and `hf22-projection-regularity.md`
> sharpens that to `alpha > 3/2` using the same `2/3`-Hölder bound rederived
> here as `eq:twothirds`. The present theorem closes `(1,3/2]`, so every
> `alpha > 1` in this monomial class is now refuted and `alpha = 1` is sharp.

---

## 8. Output block

**VERDICT:** PASS WITH SCOPE. No invalid or unsupported mathematical bridge
in Scope A; three attribution repairs (R-S1, R-S2, R-S3) required before any
integration.

**REVIEWED SCOPE:** `sec:variational` (`lem:minimum`, `lem:cubic`,
`lem:derivative`, `eq:twothirds`, `eq:dual-lip`, `eq:heatsign`,
`eq:evolution`, `eq:scaling`); `sec:heatcounter` (`thm:counter`, the ellipse
construction, `eq:heatH`--`eq:heatgap`); `sec:sharp`
(`eq:swirl`--`eq:Kpositive`, `thm:alpha`, its remark); `sec:actual`
(`thm:Genergy`); `cor:Kbounds`, consumed by both `sec:sharp` and
`sec:actual`. Not certified here: `thm:divcurl`, `thm:weighted`, `thm:mixed`
(as proved in this file), `thm:sigmacriterion`, `cor:Gproducer`,
`prop:generalcriterion`, `sec:budgets`, `thm:completion`.

**FIRST BAD BRIDGE:** none in the mathematics. The first *unsupported*
implication of any kind is the ledger inference "the two counterexample
conclusions have no exact prior match" `=>` "New candidate counterexample"
for the dissipation comparison, which is contradicted by the audited HF19-D
Proposition 3.4 / Corollary 3.5 present at the revision HF25 pins. It is a
novelty claim, not a step in any proof, and nothing downstream consumes it.

**EVIDENCE:** every constant recomputed independently
(`kappa = 2/m^3`, `kappa_s = -18 sin cos/m^6`,
`|grad U|^2 = kappa^2/(1+d kappa)^2`, `H = -2 kappa kappa_s`,
`H(pi/4) = 36(2/5)^{9/2} = 0.5828710183`, `c_* = c^2/(4B)`,
`||d_eps||_3^3 <= 6C_e|eps|^3`, `int rho|d_eps|^2 <= 4C_e|eps|^3`,
`c_0 = ||U||_3^3`, `C_*` term by term, `B_q = (6C_e)^{1/3} + ||h||_3`,
`C_# = (3/2)C_9 S` with Hölder exponents `(3,9,18,2)` and
`||grad V||_2^2 <= (9/8)D_Q`, `mu = nu/b`, `lambda = b^2 E_W/E`,
`tau_b = s_0(E/E_W)^2 b^{-5}`, `G_b = b^3 int_0^{s_0}`); direct numerical
evaluation of `div U`, `|U|`, `|grad U|^2`, `div(|U|U)` and
`div(Dj(U) Lap U)` from the exact signed distance (Appendix A), agreeing with the analytic values to `1e-7` and converging at
fourth order; cross-derivation of `H` from the audited HF19-D identity
`R = -4 kappa kappa_s phi^3/J^4` via the audited HF22-A Lemma 2.3
`R = 2|v| N(v)`.

Twelve refutation attempts, all failed: (1) class membership of the ellipse
field, attacked numerically at 46 tube points; (2) the value and sign of `H`,
attacked by direct finite-difference evaluation; (3) the Frenet/orientation
convention, cross-checked against HF19-D; (4) inflation of the `t^2` order,
bracketed above and below; (5) contradiction with HF19-D Theorem 3.2's
vanishing total, which instead confirms; (6) the second-order Taylor
remainder at the cubic's singular third derivative; (7) `eq:directionallip`
read as a disguised two-point Lipschitz claim; (8) uniformity of the
`thm:alpha` contradiction as `alpha -> 1^+`; (9) the Hölder exponents and
constants of `C_#` and `C_*`; (10) a hidden `b`-dependence in `thm:Genergy`'s
lower bound, and the commutator split at `|gamma| = 4/5`; (11) turning
`thm:Genergy` into a contradiction with whole-datum `(G)`; (12) a heat path
used as a Navier--Stokes trajectory.

**REPLACEMENT ARGUMENT:** none required for the mathematics. Three
attribution replacements are displayed in §7.

**CONDITIONAL SUFFIX THAT SURVIVES:** everything in Scope A survives
unconditionally, except that `cor:Kbounds`' second estimate (and hence
`thm:Genergy`, though not `thm:counter` or `thm:alpha`) consumes
`D_Q = D_3(w) >= (8/9)||grad V||_2^2` and therefore the div--curl layer,
audited as HF23 Scope A and now in the manuscript as `prop:quotient-divcurl`.
`thm:counter` and `thm:alpha` consume no unaudited input at all.

**UNNECESSARY DEPENDENCIES:**
1. Every `\cite{Attachment}` in `sec:sharp` and `sec:actual` is removable:
   both sections restate and reprove their inputs in full. The attachment
   hash question is therefore not load-bearing for Scope A.
2. `thm:alpha` does not need `eq:twothirds`; it needs only the anchored
   `eq:directionallip`, which comes from the audited HF20 gain.
3. `thm:alpha` does not need the two-point Lipschitz hypothesis of the
   audited HF21-B Lemma R2(2); one direction suffices, and the lemma's proof
   already uses only that.
4. `thm:counter` does not need the ellipse specifically. Any smooth closed
   strictly convex non-circular plane curve works, as audited HF19-D
   Proposition 3.4 states; the ellipse buys only the numeric `H` value.
5. `thm:counter` does not need the two-sided tube; a one-sided plateau works.
6. `sec:heatcounter` never uses `sec:divcurl`, `sec:weighted` or
   `cor:Kbounds`.

**NON-CLAIMS:** this review certifies no other section of HF25. It does not
certify `thm:divcurl`, `thm:weighted`, `thm:mixed` as proved *in this file*,
`thm:sigmacriterion`, `cor:Gproducer`, `prop:generalcriterion`,
`thm:completion`, or any statement in `sec:budgets`. Nothing here proves or
disproves `(G)`, `hyp:highstrain`, `hyp:highpressure`, CRITICAL or NS-R3; the
first gap is unchanged. `thm:counter` refutes the comparison with constant
`1` only; comparisons with `C > 1` or with an extra term remain open (HF22-A
questions (C1)/(C2)). `thm:alpha` refutes the monomial class
`L(alpha)` only, not signed or spacetime estimates. `thm:Genergy` excludes an
**energy-only** remainder for `G`, not a whole-datum remainder, and says
nothing about `K_L` or `hyp:highstrain`. No manuscript edit is applied, no
graph node is promoted or demoted, no commit or push is made, and no novelty
or priority claim against the external literature is endorsed. This audit's
numerics are bounded evidence at finite resolution, never proof. The two
artifacts (HF25's cited PDF and our HF23 `.tex`) are **not** asserted to be
identical; only that no Scope A attribution to the former exceeds what the
latter proves.

**REOPENING CONDITION:** the blacklisted implication is only the novelty
inference of R-S1. It reopens if an artifact predating
`hf19-difference-functional.md` in this repository is shown not to contain
Proposition 3.4 / Corollary 3.5, or if the HF19-D audit is withdrawn. The
mathematics of Scope A reopens only on (i) a demonstrated error in the
normal-coordinate identity `|grad U|^2 = kappa^2/(1+d kappa)^2` or in
`Dj(z) = |z|(I + zhat (x) zhat)`, (ii) a demonstrated failure of the
competitor `v(t) + a t grad psi` to lie in `v(t) + G`, (iii) a proof that
`Q(v_eps) < Q(U)` somewhere on the HF20 family, which would break
`thm:alpha`'s use of `Q^{(1-alpha)/3}`, or (iv) withdrawal of the audited
HF21-B Proposition 3.1, which would break `thm:Genergy` (but not
`thm:counter` or `thm:alpha`).

---

## 9. Exact edits the controller should make if this verdict stands

**Manuscript** (`navier-paper/main.tex`), two edits, both narrowing:

1. In `rem:qe-heatsign-scope` (l.7245), after "No quantitative comparison
   with the original cubic dissipation is claimed", add one sentence:

   > No comparison with constant `1` holds in either direction: on the class
   > of solenoidal Schwartz fields there are `v` with
   > `D_{\mathcal Q}(v) > D_3(v)` and `v` with `D_{\mathcal Q}(v) < D_3(v)`,
   > both realised along a single linear-heat trajectory started at a
   > compactly supported member of `\mathcal M`. Whether a comparison with a
   > larger constant holds in either direction is not addressed here.

   This is the sentence HF22-A's audit already licensed, unchanged; HF25
   adds no wording to it, because HF25 proves only one of the two directions.
   It must **not** say the comparison is "refuted".

2. In `rem:no-monotone` (l.7969), after the two-sided display, add:

   > The same estimate excludes every superlinear defect exponent. The
   > competitor bound `\norm{d_\varepsilon}_3^3\le6C_e|\varepsilon|^3` gives
   > `\norm{q(U+\varepsilon h)}_3\le B_q|\varepsilon|` along this family,
   > while `\mathcal Q\ge\mathcal Q(U)>0` and
   > `D_{\mathcal Q}\le\norm{v_\varepsilon}_3^2\norm{\Delta v_\varepsilon}_3`
   > stay bounded; so for no `\alpha>1` is
   > `K(v)\le C\norm{q(v)}_3^\alpha\mathcal Q(v)^{(1-\alpha)/3}
   > D_{\mathcal Q}(v)` available with a finite universal `C`. The exponent
   > `\alpha=1` of Lemma~\ref{lem:quotient-transport}'s companion estimate is
   > therefore sharp in this homogeneous monomial class, though not in every
   > signed or spacetime estimate.

   This requires the manuscript to carry the `|K| <= C_# d_1 D_Q` bound; if
   it does not yet (it is audited HF21-B Prop. 3.1 and is not currently a
   labelled manuscript statement), add that estimate first, or defer this
   edit to the wave that integrates HF21-B.

   Do **not** add `thm:Genergy` to the manuscript in this wave: it is
   subsumed in mechanism by the held-back HF23 Scope B `thm:spacetime`, whose
   four repairs are still outstanding, and adding both separately would
   duplicate.

**Graph.** Under HIGH-STRAIN, record two further excluded mechanism classes:
(i) the universal fixed-time dissipation comparison with constant `1` in the
`<=` direction, now with a quantitative early-time rate; (ii) every
superlinear exponent `alpha > 1` in the monomial class
`|K| <= C d_1^alpha Q^{(1-alpha)/3} D_3(w)`. Neither promotes or demotes any
node.

**PLAN.md**, four edits:

1. In the HF25 section, replace "an explicit compactly supported witness
   leaving the nonlinear-Hodge class under linear heat flow, so the
   dissipation comparison is false with a constructed field rather than an
   existence argument, which is exactly the witness the audited HF22-A said
   it had not delivered" by "a **quantitative** early-time rate
   `F - Q >= c_* t^2` for the audited HF19-D elliptic-swirl witness, which
   narrows but does not close the explicit-witness question HF22-A recorded:
   the witnessing time is still existential and `c_*` is not exhibited".
2. In the same section, replace "exclusion of every superlinear defect
   exponent, closing the interval HF21 and HF22-B left open" by "exclusion of
   every superlinear defect exponent, closing the interval `(1,3/2]` that
   HF22-B left open after cutting HF21-B's `(1,2]`; `alpha = 1` is now
   unconditionally sharp in that monomial class". This is the one Scope A
   result that is unambiguously new.
3. In the same section, add to the note-for-the-audit paragraph: "resolved:
   the attachment is a 23-page **PDF** and our HF23 artifact is its `.tex`
   source, so the hash discrepancy is expected. Every Scope A attribution to
   the attachment (Theorems 3.1, 4.2, 7.1 and Section 6, and every field and
   constant of the HF20 reconstruction) matches our audited HF23 exactly.
   Nothing in Scope A depends on the identification."
4. In "Ordered next actions" item 4, the plan's proposed correction (that the
   target inequality is a stronger *mechanism* than the manuscript's signed
   hypothesis, not an algebraic restatement) is **outside Scope A** and is
   not confirmed here; leave it for the Scope B reviewer, who owns
   `sec:budgets` and `thm:completion`.

**HF25 index note** (`hf25-beyond-hf21-continuation.md`): apply R-S1 and
R-S2 verbatim to claim 1 and to the "Why this matters" paragraph. The
sentence "supplies the counterexample HF22-A could not construct" is false
and must go.

**No repository state is changed by this review.** This file is its only
output.

---

## Appendix A. The verification script, verbatim

Numerics are bounded evidence at finite resolution and are never proof. This
is recorded here rather than left in session scratch, so the check is
reproducible. `python3`, numpy only.

```python
import numpy as np
from math import *

def gam(th):  return np.array([2*np.cos(th), np.sin(th)])
def gamp(th): return np.array([-2*np.sin(th), np.cos(th)])
def gampp(th):return np.array([-2*np.cos(th), -np.sin(th)])
def mm(th):   return np.hypot(2*np.sin(th), np.cos(th))
def nvec(th): return np.array([np.cos(th), 2*np.sin(th)])/mm(th)

def theta_star(p):                      # nearest point: (p-gamma).gamma' = 0
    ths = np.linspace(0, 2*pi, 721)
    th  = ths[int(np.argmin([(p[0]-2*cos(t))**2+(p[1]-sin(t))**2 for t in ths]))]
    for _ in range(80):
        g, gp, gpp = gam(th), gamp(th), gampp(th)
        th -= np.dot(p-g, gp)/(-np.dot(gp, gp) + np.dot(p-g, gpp))
    return th

def dist_n(p):
    th = theta_star(p); n = nvec(th)
    return np.dot(p-gam(th), n), n          # signed distance and grad d = n

delta = 0.10
def eta(t):  return exp(-1.0/t) if t > 0 else 0.0
def chi(r):
    a, b = eta(1-r*r), eta(r*r-0.25)
    return a/(a+b) if (a+b) > 0 else 0.0

def U(x, y, z):                             # eq:ellipseU
    d, n = dist_n(np.array([x, y]))
    if abs(d) >= delta or abs(z) >= 1.0: return np.zeros(3)
    T = np.array([-n[1], n[0]])             # T = J grad d
    s = chi(d/delta)*chi(z)
    return np.array([s*T[0], s*T[1], 0.0])

def j(v): return np.linalg.norm(v)*v
def Uv(X): return U(X[0], X[1], X[2])
def jU(X): return j(Uv(X))

def grad_field(F, X, h):                    # 4th order, J[i,j] = d_j F_i
    J = np.zeros((3, 3))
    for k in range(3):
        e = np.zeros(3); e[k] = h
        J[:, k] = (-F(X+2*e)+8*F(X+e)-8*F(X-e)+F(X-2*e))/(12*h)
    return J

def lap_field(F, X, h):
    acc = np.zeros(3); f0 = F(X)
    for k in range(3):
        e = np.zeros(3); e[k] = h
        acc += (-F(X+2*e)+16*F(X+e)-30*f0+16*F(X-e)-F(X-2*e))/(12*h*h)
    return acc

th0 = pi/4; m0 = mm(th0)
k0  = 2/m0**3
ks0 = -18*sin(th0)*cos(th0)/m0**6
print("kappa", k0, "kappa_s", ks0,
      "H_pred", -2*k0*ks0, "closed form", 36*(2/5)**4.5)

p0 = gam(th0); X0 = np.array([p0[0], p0[1], 0.0]); h = 2e-3
Jm = grad_field(Uv, X0, h)
print("div U          ", np.trace(Jm))
print("|U|            ", np.linalg.norm(Uv(X0)))
print("|grad U|^2     ", np.sum(Jm*Jm), " kappa^2 =", k0**2)
print("div(|U|U)      ", np.trace(grad_field(jU, X0, h)))

def DjLap(X):                               # Dj(U) Lap U
    v = Uv(X); L = lap_field(Uv, X, h); nv = np.linalg.norm(v)
    if nv == 0: return np.zeros(3)
    return nv*(L + v*np.dot(v, L)/nv**2)
print("H = div(Dj(U) Lap U)", np.trace(grad_field(DjLap, X0, 3e-3)))

rng = np.random.default_rng(0)              # off-plateau convergence sweep
for _ in range(6):
    th = rng.uniform(0, 2*pi); dd = rng.uniform(-0.099, 0.099)
    zz = rng.uniform(-0.99, 0.99)
    P = gam(th) + dd*nvec(th); X = np.array([P[0], P[1], zz])
    print(" ".join("%.2e/%.2e" % (abs(np.trace(grad_field(Uv, X, hh))),
                                  abs(np.trace(grad_field(jU, X, hh))))
                   for hh in (1e-3, 3e-4, 1e-4)))
```

Output obtained at audit time:

```
kappa 0.5059644256269408 kappa_s -0.5760000000000003
H_pred 0.5828710183222361 closed form 0.5828710183222359
div U           9.908740494779522e-12
|U|             1.0
|grad U|^2      0.2559999999992519  kappa^2 = 0.25600000000000006
div(|U|U)       9.913375675907332e-12
H = div(Dj(U) Lap U) 0.5828710787345207
9.11e-15/1.60e-16  2.43e-14/2.48e-16  2.82e-14/9.03e-17
5.50e-05/4.74e-05  4.54e-07/3.89e-07  5.61e-09/4.81e-09
1.26e-12/1.41e-12  1.85e-13/1.85e-13  3.70e-13/4.63e-13
1.74e-18/1.14e-31  1.42e-20/9.31e-34  1.76e-22/1.15e-35
1.65e-03/5.92e-04  1.35e-05/4.99e-06  1.67e-07/6.18e-08
1.95e-05/4.13e-04  1.64e-07/3.38e-06  2.02e-09/4.17e-08
```

The last six rows are `|div U|` / `|div(|U|U)|` at six random tube points for
`h = 1e-3, 3e-4, 1e-4`: fourth-order convergence to zero, i.e. discretisation
error, not a residual.
