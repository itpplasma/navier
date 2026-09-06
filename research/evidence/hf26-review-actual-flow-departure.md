# Review of HF26, Scope C: exact defect creation under the actual Navier–Stokes flow

Independent adversarial proof audit, 2026-09-06. Lens: rebuild every
implication of Section 4 from the first nontrivial one, recompute every
constant, exponent and geometric quantity from scratch (symbolically and
numerically), and try to refute each load-bearing claim. Scope C only.
Nothing is promoted, no graph node changes, and no file other than this one
was written.

## Freeze

| object | identity |
|---|---|
| candidate (never edited) | `research/evidence/hf26-temporal-continuation.tex`, sha256 `24b538280c8639b81a1f6f86d4c72370362625ca8a52d1d81a99b29236a540ab` (1432 lines) |
| controller index note | `research/evidence/hf26-temporal-continuation.md` (re-read after the controller's temporal-audit corrections landed) |
| research HEAD at audit | `54d9e2a26c02a3c4d39c56bc2647a5c4255526bf` |
| candidate's pinned `navier` | `a3e85f2d75fb01f1421e95f51ec6f8eedab0ec50` — resolves |
| candidate's pinned `navier-paper` | `34cdffd2fe2bd8a35068e96f907302e00c10850f` — resolves; `prop:localtheory`(iii) verified **at that revision**, not only at the working tree |
| candidate's pinned `navier-formal` | `54f8e89119e90399044bae8dcd404dc405a381f9` — resolves |
| audited comparanda read in full | `hf19-difference-functional.md` (Prop. 3.4, Cor. 3.5, NEXT ACTION (1)), `hf19-second-order-falsifier.md` (Lemma 1.4, (2.2)), `hf25-beyond-hf21-continuation.tex` §`sec:heatcounter`, `hf25-review-counterexamples.md`, `cp02-review-local-theory-r2.md` |
| own computations | `scratchpad/ellipse2.py`, `scratchpad/symmetry.py`, `scratchpad/extra.py`, `scratchpad/gapquad.py` (session scratch; the essential outputs are transcribed below) |

**Scope actually audited.** `prop:gapquadratic` (§4.1), the inherited ellipse
field and `eq:gH` (§4.2), `thm:NSdeparture`, `eq:NSgaplower` and the corollary
"A source-free gap equation cannot hold universally" (§4.3), together with the
§2 objects those consume (`eq:defs`, `eq:objects`, `eq:stationarity`,
`eq:matrixM`, `eq:Hspace`, `eq:weightedE`, `lem:jTaylor`).

**Scope note / controller error.** The commission also pointed at the appendix
"The inherited compact positive-work field used in the comparison curve"
(`app:positive`, line 1286) "insofar as the ellipse field is used". That
appendix does **not** contain the ellipse field: it reconstructs the
axisymmetric swirl seed `U_s = ρ(r,z) e_θ` and `W_0 = U_s − ε h`, which feed
`thm:curve` in §7 and are logically disjoint from §4. The ellipse field lives
only in §4.2 of this document (and in `hf25` §`sec:heatcounter`, and in audited
HF19-D Prop. 3.4). Nothing in §4 depends on `app:positive`, and I audited none
of it.

---

## VERDICT

**PASS WITH SCOPE.** No invalid or unsupported mathematical bridge was found in
Scope C: the ellipse field, the exact value `H(π/4,0,0) = 36(2/5)^{9/2}`, the
nonvanishing of `g_H`, the initial tangent, the weight-scaling identities, the
quadratic gap coefficient and the Gronwall corollary all reproduce
independently. The scope conditions are that the *equality* in `eq:NSgap`
imports the unaudited §3 while only the "≥" half is used (R1 supplies a §3-free
proof of that half), that the constants of `eq:NSgaplower` are determined but
never exhibited and its amplitude restriction is a smallness condition tying
`a` to `ν` (R4, R5), and that the corollary's `L^1_loc` hypothesis is sharp and
load-bearing (R6). One statement is *weaker than what its own construction
supports*: "except possibly one amplitude" can be deleted outright for this
field (R2).

---

## Q1. The initial tangent and the `C^2(L^3)` regularity

**Verdict: correct, with one missing line of justification (R3).**

*Tangent.* The note's `Π_ij = δ_ij + R_iR_j` with `R_j = ∂_j(−Δ)^{−1/2}` has
symbol `δ_ij − ξ_iξ_j/|ξ|²`, i.e. it is the Leray projector, and it is
consistent with the manuscript's normalisation `p = R_iR_j(u_iu_j)`: from
`−Δp = ∂_i∂_j(u_iu_j)` one gets `p̂ = −ξ_iξ_j û_iu_j/|ξ|²`, and
`N − ΠN = −∇p` identically, so the classical equation
`∂_t u = νΔu − N(u) − ∇p` is exactly `∂_t u = νΔu − Π N(u)`. Since
`u(0) = aU` is solenoidal and smooth, `Δ(aU) = aΔU` (already solenoidal, so
`ΠΔU = ΔU`) and `N(aU) = a²N(U)`, giving

    h_a = ∂_t u^(a)(0) = ν a ΔU − a² Π N(U).

This is exactly the tangent the repository's own audited HF19-B uses along the
actual flow, its (2.2): `u_1 = νΔu_0 + m`, `m = Π f`, `f = −N(u_0)`. Two
independent formulations agree. `ΔU ∈ C_c^∞ ⊂ L^3`; `N(U) ∈ C_c^∞` and `Π` is
bounded on `L^3` (Calderón–Zygmund), so `ΠN(U) ∈ L^3` although it is *not*
compactly supported — the note's one-sentence justification is right.

*Regularity.* `prop:gapquadratic` needs the trajectory to be `C^2` as a curve
in `L^3` on `[0,t_0]`, one-sided at `t = 0`. The imported package
(`navier-paper` `main.tex` at the pinned `34cdffd`, `prop:localtheory`(iii),
derived from Tao Thm 5.4 + Cor 4.3 + Cor 5.8) gives, for `u_0 ∈ S(R^3)`
divergence-free and every `T < T_*`,

    u ∈ C^j([0,T]; H^k(R^3))  for all j,k ≥ 0,  time derivatives classical,

*smooth up to and including `t = 0`*. `aU` is compactly supported and smooth,
hence Schwartz, so the package applies, and `T_*(ν,aU) > 0`. The step the note
omits is the embedding: `C^2([0,T];H^1) ⊂ C^2([0,T];L^3)` because
`H^1(R^3) ↪ L^3(R^3)` (`‖f‖_3 ≤ C‖f‖_2^{1/2}‖∇f‖_2^{1/2}`), and a continuous
linear embedding transports the `C^2` property. So the regularity **is**
supplied. The repository's own audit of that package
(`cp02-review-local-theory-r2.md`) returns REPAIR with *no invalid
mathematical bridge*, and explicitly certifies that clause (iii) is a theorem
of the section rather than an assumption; its recorded caveat (uniformity only
on compact `[0,T]`, `T < T_*`) is harmless here, since §4 works on an
arbitrarily short interval at `t = 0`.

I checked that the note does not misquote the package: its §1 sentence "on
every `[0,T] ⊂ [0,T_*)`, `u,p ∈ C^j([0,T];H^k)` for all `j,k ≥ 0`, the pressure
is normalized by `p = Σ R_iR_j(u_iu_j)`, and finite `T_*` forces loss of the
`H^1` bound" reproduces clauses (iii), (iv), (v) verbatim in content.

## Q2. "Positive for every `a > 0` except possibly one"

**Verdict: the argument as given is valid; the conclusion is *not tight for
this field* and should be strengthened (R2). It hides no case.**

*The given argument is valid.* The coefficient vanishes iff `ν g_H = a g_E` in
`H_U`. If `a_1 ≠ a_2` both annul it, subtracting gives `(a_1−a_2) g_E = 0`,
hence `g_E = 0`, hence `ν g_H = 0`, hence `g_H = 0` since `ν > 0` —
contradicting `eq:gH`. Correct. It is also not vacuous in general: in a
finite-dimensional model of the same variational structure I constructed a
configuration with `g_H ∥ g_E` and confirmed that exactly one positive
amplitude annuls the vector (`gapquad.py`, TEST E). So "at most one" is the
right *general* statement.

*Two things the note does not say, both of which matter.*

(i) The exceptional amplitude, if it existed, would be `a* = ν c/|b|` with
`b = ⟨g_E,∇ψ⟩_U < 0`, and it therefore depends on `ν`. As phrased, a reader can
read "except possibly one" as one universal amplitude; the excluded value moves
with `ν` (`ν g_H = a g_E` with `g_H = λ g_E` gives `a* = νλ`). Note the
consistency check with `eq:NSgaplower`: exceptionality forces `a*|b| = νc`, so
every `a` satisfying the note's own restriction `a|b| ≤ νc/2` is automatically
non-exceptional.

(ii) **The exception can be removed entirely for this field, by a parity
obstruction.** Because `∇ψ ∈ E_U` and `P_U` is an orthogonal projection,
`⟨P_U X, ∇ψ⟩_U = ⟨X, ∇ψ⟩_U` for every `ψ ∈ C_c^∞(R^3)`. Hence `ν g_H = a g_E`
implies, testing against all such `ψ`,

    ν div(M_U ΔU) = a div(M_U Π N(U))   in D'(R^3),

and pointwise on the open plateau, where every field is smooth. Let
`S = diag(1,−1,1)`. The ellipse, the signed distance `d`, the cutoffs and the
plateau are `S`-invariant, and `J S_2 = −S_2 J` gives `T(Sx) = −S T(x)`, hence

    U(Sx) = −S U(x).

Then `|U|∘S = |U|`, `M_U(Sx) = S M_U(x) S`, `(ΔU)(Sx) = −S ΔU(x)`, so
`M_U ΔU` is odd-equivariant and `H := div(M_U ΔU)` is an **odd** scalar. On the
other hand `N(U)` is quadratic in `U`, so `N(U)(Sx) = +S N(U)(x)`; the Leray
projector commutes with the pushforward by any orthogonal map (its symbol
`δ_ij − ξ_iξ_j/|ξ|²` is `O(3)`-equivariant), so `ΠN(U)` is even-equivariant and
`N := div(M_U Π N(U))` is an **even** scalar. The displayed identity at `x` and
at `Sx` then gives `νH(x) = −νH(x)`, i.e. `H ≡ 0` on the plateau — contradicting
`eq:Hpositive`. **Therefore no `a > 0` is exceptional and the coefficient in
`eq:NSgap` is positive for every `a > 0` and every `ν > 0`.**

I verified the parity bookkeeping symbolically (`symmetry.py`): `U` odd, `N(U)`
even, `H` odd (also off `d = 0`), `div(M_U N(U))` even — all to 30 digits at
four independent points. (Incidentally the *local* part vanishes identically:
`U·N(U) = 0` and `div N(U) = tr((∇U)²) = 0` on the plateau because `∇U` has
rank one there, so `N = div(M_U ∇p_U)` is purely pressure-driven. This is not
needed for the parity argument.)

A cheaper fallback that needs no symmetry, if the parity argument is not
wanted: `ν g_H = ±a g_E` cannot hold for both signs unless `g_H = 0`, so for
**every** `a > 0` at least one of the two data `± aU` (both in `M`, both
compactly supported smooth solenoidal) has a strictly positive coefficient.

## Q3. `M_{aU} = a M_U` and `P_{aU} = P_U`

**Verdict: correct.**

For `a > 0` and `ρ = |U| > 0`, `M_{aU} = a|U| I + a²(U⊗U)/(a|U|) = a M_U`, and
both sides are `0` where `U = 0`, so the identity is global. `H_{aU}` and `H_U`
have the same underlying space (the null sets of `aρ dx` and `ρ dx` coincide
for `a > 0`) and proportional inner products, `⟨·,·⟩_{aU} = a⟨·,·⟩_U`. Equivalent
norms have the same closed subspaces, so `E_{aU} = E_U`; and the orthogonal
projection onto a fixed closed subspace is unchanged when the inner product is
multiplied by a positive constant, so `P_{aU} = P_U`. Consequently

    ‖P_{aU} h_a‖²_{aU} = a‖P_U(νaΔU − a²ΠN(U))‖²_U = a·a²‖ν g_H − a g_E‖²_U
                       = a³‖ν g_H − a g_E‖²_U,

exactly as claimed. One hypothesis is used silently and does hold: `aU ∈ M`
(since `div(|aU|aU) = a² div(|U|U) = 0`), so the base point of the expansion is
`w(aU) = aU` and the relevant weight really is `aU`.

Numerically confirmed to machine precision in the finite-dimensional model
(`gapquad.py`, TEST C: `‖M_{aU} − aM_U‖_F ≤ 4e−15`, `‖P_{aU} − P_U‖_F ≤ 4e−15`
for `a = 0.3, 1, 2.5`) and TEST D (`½‖P_{aU}h_a‖²_{aU}` equals the
`a³`-formula to 12 digits, and both match a direct numerical evaluation of
`d(v(t))/t²`).

## Q4. `eq:NSgaplower` and the amplitude restriction

**Verdict: the inequality chain is correct; the presentation overstates how
explicit the constants are, and understates that the restriction is a
smallness condition (R4, R5).**

With `b = ⟨g_E,∇ψ⟩_U` and `⟨g_H,∇ψ⟩_U = −c`,

    |⟨ν g_H − a g_E, ∇ψ⟩_U| = |νc + ab| ≥ νc − a|b|,

and Cauchy–Schwarz against `‖∇ψ‖_U = √B` gives
`‖ν g_H − a g_E‖²_U ≥ (νc − a|b|)²/B`, valid because `a|b| ≤ νc/2` makes the
bracket nonnegative; then `(νc − a|b|)² ≥ ν²c²/4`. Halving the leading term to
absorb the `o(t²)` gives `d(u^(a)(t)) ≥ a³ν²c² t²/(16B)`. Every step
reproduces.

Three qualifications:

1. The bound is **not sharp**: the exact coefficient is
   `½a³‖νg_H − ag_E‖²_U ≥ ½a³(νc − a|b|)²/B`, so the two halvings cost a
   factor 4 — with `b = 0` the same chain already gives `a³ν²c²t²/(4B)` before
   absorbing the `o(t²)`, and `a³ν²c²t²/(2B)` as the exact coefficient. For the
   pure heat comparison (`ν = a = 1`, tangent `ΔU`, no `g_E` term) this reads
   `½‖g_H‖²_U ≥ c²/(2B)`, which is **exactly** HF25's audited
   `thm:counter` constant before it absorbs the `o(t²)` — see Q8.
2. `a|b| ≤ νc/2` is a restriction `a ≤ νc/(2|b|)` (vacuous only if `b = 0`).
   So `eq:NSgaplower` is a *small amplitude relative to viscosity* statement,
   and at fixed `a` its guaranteed constant `∝ a³ν²` degenerates as `ν → 0`
   (worse: with `b ≠ 0` the admissible `a` is itself `O(ν)`, so the bound is
   `O(ν⁵)`). The unrestricted "every viscosity, all but one amplitude" claim is
   the *qualitative* statement of the theorem, not this bound.
3. "The constants use only fixed spatial fields and tests, not unknown endpoint
   norms" is **true but not shown**: as written, `b` and `c` are defined through
   the unknown projection `P_U`. Self-adjointness of `P_U` plus `P_U∇ψ = ∇ψ`
   removes it: `c = −⟨ΔU,∇ψ⟩_U = ∫Hψ` and `b = ⟨ΠN(U),∇ψ⟩_U = ∫ΠN(U)·M_U∇ψ`.
   Add this line (R4). Separately, and in the same sense the HF25 audit recorded
   as its S2, `δ_0`, the patch `O` and `ψ` are only asserted to exist, so
   `c, B, b` are *determined but not exhibited*, and the threshold
   `t_0(a,ν,ψ)` below which `eq:NSgaplower` holds is not quantified. The only
   number actually computed in this construction is `H(π/4,0,0)`.

## Q5. `prop:gapquadratic`

**Verdict: correct as stated; but its proof consumes §3 (unaudited here), and
the half that §4 actually needs has a two-line §3-free proof (R1).**

*Independent reconstruction.* `j : L^3 → L^{3/2}` is Fréchet differentiable
with `Dj(v) = M_v` (from `lem:jTaylor`'s pointwise `|j(a+d) − j(a) − Dj(a)d| ≤
2|d|²`, so `‖·‖_{3/2} ≤ 2‖d‖_3²`), and `v ↦ M_v` is Lipschitz in operator norm
(`‖Dj(a) − Dj(b)‖_op ≤ 4|a−b|`). Hence `F(v) = ⅓‖v‖_3³` is `C²` on `L^3` with
`D²F(v)[h,k] = ∫h·M_v k`, and along a `C²` curve `φ(t) = F(v(t))` is `C²` with

    F(v(t)) = F(U) + t⟨j(U),h⟩ + ½t²(‖h‖²_U + ⟨j(U),k⟩) + o(t²).

For `Q`: `ψ(t) = Q(v(t))` is differentiable with `ψ'(t) = ⟨A(v(t)),v_t(t)⟩`
(`eq:Qprime`, no derivative of `w`), and `eq:Qtt` gives `ψ''(0)`; Taylor–Peano
needs only differentiability near `0` plus existence of `ψ''(0)`, which is
exactly what `cor:second` provides, one-sided at an endpoint included. `U ∈ M`
gives `Q(U) = F(U)`, `A(U) = j(U)`, so the constant, linear and acceleration
terms cancel and `‖h‖²_U − ‖L_U h‖²_U = ‖P_U h‖²_U` by orthogonality. Correct.
(The hypothesis "solenoidal" is not used: `w(U) = U` follows from
`U ∈ M` alone, by stationarity plus convexity.)

*Numerical falsification attempt.* In a finite-dimensional model with the same
structure (`F(v) = ⅓Σ|v_i|³`, `j(z) = |z|z`, a fixed subspace `G` in the role
of `G_3`, `U` chosen with `j(U) ⊥ G` so that `w(U) = U`), the ratio
`d(U + th + ½t²k)/t²` converges to `½‖P_U h‖²_U` with relative error falling
linearly in `t` (consistent with an `O(t³)` remainder):

    non-degenerate U:  predicted 1.913953061180;  t=1e-2 → 1.890949, 1e-3 → 1.911591, 1e-4 → 1.913717
    degenerate U (3 zero-weight nodes):
                       predicted 6.682173568127;  t=1e-2 → 6.641694, 1e-3 → 6.677972, 1e-4 → 6.681752

The degenerate test matters: the ellipse field is compactly supported, so
`{U = 0}` has infinite measure and `H_U` genuinely records nothing there. The
quotient-space projection is the right object, and the coupling through `G`
(gradients cannot be chosen freely on `{U = 0}`) is correctly absorbed by
taking the closure `E_U = cl_{H_U}(G_3)` before projecting.

*The §3 dependency, and how to remove it.* `prop:gapquadratic` as proved needs
`cor:second`, hence `thm:Aderivative`, hence `thm:weightedresponse` — all
outside my scope and unaudited at the time of writing. But `thm:NSdeparture`'s
conclusion, `eq:NSgaplower` and the corollary use only the lower bound. That
half is elementary:

> **Lemma (R1).** Let `U ∈ M`, and let `v(t) = U + th + ½t²k + o(t²)` in `L^3`.
> Then `liminf_{t↓0} d(v(t))/t² ≥ ½‖P_U h‖²_U`.
>
> *Proof.* Fix `g_m ∈ G_3` with `g_m → P_U h` in `H_U` (possible by definition
> of `E_U`). Since `−t g_m ∈ G_3`, `Q(v(t)) ≤ F(v(t) − t g_m)`. Expand both
> `F(v(t))` and `F(v(t) − t g_m)` by the `C²` Taylor formula above; the
> `⟨j(U),·⟩` linear terms differ by `t⟨j(U),g_m⟩ = 0` (stationarity at `U`),
> the acceleration terms are identical, and the cubic remainders are
> `O_m(t³)`. Hence
> `d(v(t)) ≥ ½t²(‖h‖²_U − ‖h − g_m‖²_U) + o_m(t²)`, and
> `‖h − g_m‖_U → ‖L_U h‖_U`. Let `m → ∞`. ∎

No weighted linearization, no Hadamard derivative, no strong convergence of
difference quotients. With this in place §4 stands on §2 alone.

## Q6. The ellipse field and `eq:gH` (the linchpin)

**Verdict: correct. `g_H ≠ 0`, verified independently and exactly.**

*Class membership.* `|T| = |J∇d| = |∇d| = 1`, so `|U| = χ(d/δ_0)χ(z) ≥ 0` is a
**smooth** function (no kink from the absolute value), whence `|U|U` is smooth
and the distributional divergences are classical. `div U = χ(z)[χ'(d/δ_0)δ_0^{-1}
n·T + χ div(J∇d)] = 0` since `n·T = 0` and `div(J∇d) = −∂_x∂_y d + ∂_y∂_x d = 0`;
`div(|U|U) = div(χ²χ²T)` vanishes for the same two reasons, the third component
being identically zero. So `U ∈ M`, `w(U) = U`, `q(U) = 0`. Smoothness of the
zero extension follows from the flatness of `χ` at `|r| = 1`; `χ` is checked to
be `1` on `|r| ≤ ½` and `0` on `|r| ≥ 1` with a denominator that never vanishes.
The tube/injectivity argument is the standard compactness one (`κ ≤ 2`, so any
`δ_0 < ¼` gives `1 + dκ > 0` on `|d| < 2δ_0`).

*Geometry, recomputed from scratch.* `γ' = (−2sinθ, cosθ)`, `|γ'| = m`,
`T = γ'/m`, `n = (cosθ, 2sinθ)/m` is the outward normal (`n(0) = (1,0)`),
`Jn = T`, `T_s = −κn`, `n_s = κT`, `κ = 2/m³`, `κ_s = −18 sinθcosθ/m⁶` — all
confirmed symbolically (the last one simplifies to `0` when differenced).

*The heat-normal scalar, recomputed without using the note's formulas.* I built
exact Cartesian derivative operators from the chart
(`∇θ = T/(m(1+dκ))`, `∇d = n`, both verified curl-free) and computed, on the
plateau, `div U`, `∇U`, `ΔU`, `M_U ΔU = ΔU + (U·ΔU)U` and its divergence
symbolically, then evaluated at 40 digits (`ellipse2.py`):

    div U = 0                                         (exactly, at every tested point)
    |∇U|² − κ²/(1+dκ)² = 0                            (exactly)
    U·ΔU + |∇U|² = 0                                  (exactly)
    H(θ,0) = −2κκ_s = 72 sinθ cosθ/m⁹                 (agreement to all 40 digits, 6 values of θ)
    H(π/4,0) = 0.5828710183222356784740360581098386801352
    36(2/5)^{9/2} = 0.5828710183222356784740360581098386801352   difference exactly 0

This is an independent confirmation of the note's `eq:heatnormal`,
`eq:Hpositive` and of the normal-coordinate expression for `|∇U|²`, which I did
not assume. It also agrees with HF25's audited value and, through
`H = R/(2φ)`, with audited HF19-D's `R = −4κκ_sφ³/J⁴`.

*Nonvanishing of `g_H`.* `ψ ∈ C_c^∞(O)` gives `∇ψ ∈ G_3`, hence its class lies
in `E_U`, hence `P_U∇ψ = ∇ψ`; `P_U` is self-adjoint on `H_U`, so

    ⟨g_H,∇ψ⟩_U = ⟨ΔU, ∇ψ⟩_U = ∫ (M_U ΔU)·∇ψ = −∫ div(M_U ΔU) ψ = −∫Hψ = −c.

The integration by parts is legitimate because `supp ψ ⊂ O` sits inside the
open plateau, where `U` is smooth and `|U| = 1`, so `M_U ΔU ∈ C^∞` there; the
global integral reduces to `∫_O` because `∇ψ` is supported in `O`. `c > 0`
because `H` is continuous and positive at `(π/4,0,0)` and `ψ ≥ 0`, `ψ ≢ 0`.
`B = ‖∇ψ‖²_U > 0` because `M_U = I + U⊗U ≥ I` on `O`. Cauchy–Schwarz gives
`‖g_H‖_U ≥ c/√B`. All correct; `g_H ≠ 0` follows from the pairing alone, so the
theorem is **not** vacuous.

## Q7. The corollary refuting a homogeneous defect-feedback law

**Verdict: the Gronwall argument is valid; the scope statement is right in
substance but must be made precise on two points (R6).**

*Validity.* For `u_0 = aU` with `a` admissible, `d(u(0)) = 0`, `d ≥ 0`, and
`t ↦ d(u(t)) = F(u(t)) − Q(u(t))` is `C^1` on `[0,t_0]` (both terms are `C^1`
functionals along a `C^1` `L^3`-curve). If `y' ≤ b(t)y` with `y(0) = 0`,
`y ≥ 0`, `b ∈ L^1(0,ε)`, then `(y e^{−∫_0^t b})' ≤ 0` gives `y ≡ 0` — which
contradicts `eq:NSgaplower`. Correct. The quantifier structure is also right:
what is refuted is the existence, for *this one* classical solution, of any
locally integrable feedback coefficient; a fortiori no universal law exists.

*Scope, stated correctly.* The note's disclaimer ("It does not prove growth of
`Q`, a singularity, or failure of any input-dependent spacetime estimate. The
initial full velocity can be chosen small") is accurate and should be kept
verbatim: the datum is `aU` with `a` as small as one likes, so nothing here is
a large-data or blowup mechanism, and `d` is not `Q`, not `‖q‖_3`, and not any
critical norm. Two things need sharpening:

- The hypothesis `b ∈ L^1_loc` "extending through `t = 0`" is **sharp and
  load-bearing**, not a technical convenience. The constructed solution has
  `d(u(t)) ≍ t²`, which satisfies `d' = (2/t)d` exactly; so a feedback law with
  a non-integrable coefficient at the origin (`b(t) = 2/t`) is entirely
  consistent with the counterexample and is *not* refuted. Likewise a law with
  a nonnegative source, `d' ≤ b d + S(t)`, is not refuted. The note should say
  `b ∈ L^1(0,ε)` and add both remarks.
- `d'(u(t))` is written as if `d'` were the Fréchet derivative of the
  functional evaluated at `u(t)`; the intended object is `(d/dt) d(u(t))`.
  Cosmetic, but in a statement whose whole content is a differential
  inequality it should be unambiguous, and the `C^1`-in-time fact should be
  recorded.

Finally, the corollary's proof invokes `eq:NSgaplower`, which carries the
amplitude restriction `a|b| ≤ νc/2`; that is harmless (choose `a` small, or
`b = 0`), but the phrase "for the data above" should name which datum.

## Q8. Consistency with audited HF19-D and HF25 `thm:counter`: what is new

**Verdict: genuinely stronger on the departure statement, not a restatement —
but it does not subsume HF25 `thm:counter`'s headline, and the index note
should not say it does.**

What was already in the repository, audited:

- **HF19-D Prop. 3.4 + Cor. 3.5** (audited; REPAIR applied): the same
  construction (`u_0 = f(x_3)φ(d)T` on a smooth strictly convex curve, i.e. the
  ellipse field with a general profile) leaves `M` under the **linear heat
  semigroup**, via `∂_s(v_s·∇|v_s|²)|_0 = −4κκ_sφ³/J⁴`. Its explicit NON-CLAIM
  is "no invariance or non-invariance of `M` under the Navier–Stokes flow (only
  under the heat semigroup)", and its **NEXT DISTINCT ACTION (1)** is precisely
  to compute the Euler contribution on this family and conclude non-invariance
  "if it is nonzero and not proportional to (3.3)".
- **HF25 `thm:counter`** (audited PASS WITH SCOPE, three attribution repairs):
  the same field, the same `H = −2κκ_s`, the same `36(2/5)^{9/2}`, with a
  **quantitative early-time rate** `F(v(t)) − Q(v(t)) ≥ c_* t²`,
  `c_* = c²/(4B)`, still along the **heat path**, plus the dissipation
  reversal `D_Q(v_*) > D_3(v_*)` obtained by integrating
  `dF/dt = −D_3`, `dQ/dt = −D_Q` — an identity available only because the path
  is the heat flow.

What HF26 §4 adds, precisely:

1. **The flow is the actual one.** `prop:gapquadratic` is applied directly to
   `t ↦ u^(a)(t)`, the classical Navier–Stokes branch from `aU`, using only
   that it is `C²` into `L^3` with tangent `h_a`. No data-space substitution
   and no heat proxy (contrast HF19-B, which needed its Lemma 1.4 to transfer a
   data-space Gateaux derivative to the flow at cost `O(t^{3/2})`). This is
   HF19-D's own requested next action, discharged.
2. **The nonlinear term is handled without computing it.** HF19-D asked for
   "nonzero and not proportional to (3.3)"; HF26 replaces that computation by
   the two-amplitude argument, at the price of one possibly exceptional
   amplitude — which R2 above removes by parity, so the proportionality
   question is in fact settled, not merely bypassed.
3. **An exact coefficient replaces a lower bound.** `½‖P_U h‖²_U` is an
   equality (modulo §3), where HF19-D/HF25 had a single-competitor lower bound.
   Specialising to `ν = a = 1`, `h = ΔU` reproduces HF25's constant exactly:
   the single-competitor choice `g_m = −(c/B)∇ψ` gives
   `½(‖h‖² − ‖h−g_m‖²) = c²/(2B)`, which is HF25's coefficient before it
   absorbs the `o(t²)` into `c_* = c²/(4B)`, and the exact coefficient
   `½‖P_U ΔU‖²_U ≥ c²/(2B)` dominates it. **No contradiction anywhere, and
   HF26 is sharper on the shared heat instance.**
4. **`ν`- and `a`-dependence** (`a³ν²c²/16B`) and the Gronwall corollary, both
   new.

What HF26 does **not** do, and what the index note overstates: `thm:NSdeparture`
does not reprove `thm:counter`'s headline conclusion (`D_Q > D_3` at a single
field). That conclusion used `dF/dt = −D_3` and `dQ/dt = −D_Q`, identities of
the heat flow; along Navier–Stokes the corresponding balance is
`Q' + νD = K` with a transport term. So HF26 strengthens the *departure from
`M`* half of HF25 `thm:counter` and of HF19-D, and leaves the *dissipation
comparison* half untouched. The index note's "This is a genuine strengthening
of HF19-D and of HF25's `thm:counter`" is true only with that qualification.

---

## Required repairs

**R1 (structural; removes an inherited audit risk).** Add to §4.1 the §3-free
lower bound proved above (Q5), and phrase `thm:NSdeparture`, `eq:NSgaplower`
and the corollary as consequences of the "≥" half only, keeping the equality of
`eq:gapquadratic`/`eq:NSgap` as a separate sentence flagged as consuming
`cor:second`. As written, the whole of §4 fails if §3 is repaired or withdrawn;
after R1 it does not.

**R2 (strengthening; deletes the theorem's only escape clause).** Replace "The
coefficient is positive for every `a > 0` except possibly one" by "The
coefficient is positive for every `a > 0`", with the parity proof of Q2(ii):
exceptionality would force `ν div(M_U ΔU) = a div(M_U ΠN(U))` pointwise on the
plateau; under `S = diag(1,−1,1)` the left side is odd and the right side even,
so `H ≡ 0` there, contradicting `eq:Hpositive`. If the parity argument is
declined, keep "except possibly one" but add (a) that the exceptional amplitude
depends on `ν` and equals `νc/|b|` with `b < 0`, and (b) the `±U` remark, so
that no amplitude is left uncovered.

**R3 (missing justification, one line).** In the proof of `thm:NSdeparture`,
justify "`C²(L^3)` time regularity": `prop:localtheory`(iii) gives
`u ∈ C^j([0,T];H^k)` for all `j,k` and all `T < T_*`, one-sided at `t = 0`, and
`H^1(R^3) ↪ L^3(R^3)`; `aU` is Schwartz because it is compactly supported and
smooth.

**R4 (explicitness of the constants).** Add `c = −⟨ΔU,∇ψ⟩_U = ∫Hψ` and
`b = ⟨ΠN(U),∇ψ⟩_U`, both by `P_U∇ψ = ∇ψ` and self-adjointness, so that neither
constant refers to the unknown projection; and state plainly that `δ_0`, `O`,
`ψ` are not exhibited, hence `c`, `B`, `b` are determined but not numbers, and
the threshold `t_0(a,ν,ψ)` is unquantified. (Same species as the HF25 audit's
S2; it keeps the note from being read as supplying an explicit witness.)

**R5 (scope of `eq:NSgaplower`).** Say that `a|b| ≤ νc/2` is a smallness
condition `a ≤ νc/(2|b|)` coupling amplitude to viscosity, that at fixed `a` the
guaranteed constant degrades like `ν²` (like `ν⁵` if `b ≠ 0`), and that the
"every viscosity, all but one amplitude" claim rests on the theorem, not on
this bound. Optionally record that with `b = 0` the same chain gives
`a³ν²c²/(4B)` and the exact coefficient is `≥ a³ν²c²/(2B)`.

**R6 (corollary scope, sharp).** Write the hypothesis as `b ∈ L^1(0,ε)`; add
that `b(t) = 2/t` is consistent with the counterexample (whose gap is `≍ t²`),
so exactly the integrable-at-zero feedback laws are refuted; add that laws with
a nonnegative source term are not refuted; replace `d'(u(t))` by
`(d/dt) d(u(t))` and record that this is `C^1` in `t`; name the datum used.

**R7 (attribution completeness).** §4.2 credits the ellipse construction to
`[Attachment, §5]` only. The same field and the same mechanism are in this
repository's audited **HF19-D Prop. 3.4/Cor. 3.5**, and the HF25 audit already
recorded (its S1) that HF25's novelty claim for it was wrong. HF26 claims no
novelty for it — the ledger explicitly disclaims authorship — so this is
completeness, not a novelty defect: cite HF19-D alongside, and note that
`thm:NSdeparture` discharges HF19-D's own NEXT DISTINCT ACTION (1).

**R8 (presentational).** Notation collisions inside one document: `B(a,d)`
(Bregman, §2) vs `B = ‖∇ψ‖²_U` (§4) vs `B_6` (§5) vs `B_v` (§3 operator) vs
`B_δ` (§8 bad set); the dummy `a` in `η(a) = e^{−1/a}` against the amplitude
`a`; the constant `b` against the corollary's `b(t)`; `γ` parametrised both by
`θ` and by arclength `s`. Also "Local invertibility follows from the displayed
derivative" has no displayed derivative in §4 (it means `eq:ellipsecurv`, via
`X_s = (1+dκ)T`, `X_d = n`). Finally, `prop:gapquadratic`'s hypothesis
"solenoidal" is unnecessary — `U ∈ M` alone gives `w(U) = U`.

---

## Refutation attempts and outcomes

1. **Class membership of the ellipse field.** Tried to break `div U = 0`,
   `div(|U|U) = 0`, smoothness of the zero extension, and the two-sided tube.
   *Failed*: all verified symbolically and structurally; `|U| = χχ` is smooth,
   so no Lipschitz-kink issue arises and the divergences are classical.
2. **The heat-normal scalar.** Tried to break `H = div(M_U ΔU) = −U·∇|∇U|²`,
   `|∇U|² = κ²/(1+dκ)²`, and the value `36(2/5)^{9/2}`, by recomputing all of
   them from exact Cartesian derivatives built from the chart, never using the
   note's own reductions. *Failed*: exact agreement to 40 digits at every tested
   point; the value at `θ = π/4` differs from `36(2/5)^{9/2}` by exactly `0`.
3. **`g_H = 0` (would make the theorem vacuous).** Tried to attack the chain
   `∇ψ ∈ E_U` → `P_U∇ψ = ∇ψ` → self-adjointness → integration by parts,
   including the worry that `H_U` only records values on `{U ≠ 0}` and that
   `M_U ΔU` is not `C^1` across `∂{U ≠ 0}`. *Failed*: `supp ψ` sits strictly
   inside the plateau, where everything is smooth and `ρ = 1`.
4. **The quadratic coefficient, in the presence of an infinite zero set.**
   Suspected that the compactly supported `U` makes the degenerate weighted
   projection the wrong object (gradients cannot be chosen freely off
   `supp U`). Built a finite-dimensional model with zero-weight nodes and
   measured `d(v(t))/t²`. *Failed*: converges to `½‖P_U h‖²_U` in both the
   degenerate and non-degenerate case; the closure `E_U` absorbs the coupling.
5. **The scaling identities.** Tried to break `M_{aU} = aM_U`, `P_{aU} = P_U`
   and the `a³` law numerically. *Failed*: machine-precision agreement, and the
   direct numerical gap matches the `a³` formula for `a = 0.4, 1, 2`.
6. **Make the exceptional amplitude real.** Constructed `g_H ∥ g_E` in the
   abstract model: exactly one `a` annuls the vector, so the caveat is not
   vacuous in general. *Then failed for the actual field*: the parity
   obstruction of Q2(ii) shows no exceptional amplitude exists here. Outcome:
   the theorem is true but under-claims (R2).
7. **Break the Gronwall corollary with an inverse-power coefficient.**
   `d' ≤ (2/t)d` is satisfied by the counterexample itself. *Outcome*: the
   corollary survives because it assumes `b ∈ L^1_loc` through `t = 0`, but the
   attempt shows the hypothesis is exactly sharp — recorded as R6, since a
   reader could otherwise take the corollary to exclude more than it does.
8. **Hidden use of unweighted `L^3` differentiability of `w` or `q`** (the
   thing `rem:linear-scope` warns against). Walked every step of §4 looking for
   it. *Failed*: §4 never differentiates the minimizer; the only §3 input is
   `cor:second`, and R1 removes even that for the half that is used.
9. **Inconsistency with audited HF25.** Specialised HF26's coefficient to the
   heat instance and compared with `c_* = c²/(4B)`. *Failed*: HF26 gives
   `½‖P_U ΔU‖²_U ≥ c²/(2B)`, exactly HF25's pre-absorption constant and
   dominating it. The two audited records agree.
10. **Over-reading of the strengthening claim.** Checked whether
    `thm:NSdeparture` implies HF25 `thm:counter`'s dissipation ordering.
    *Succeeded as a criticism of the index note*: it does not (the ordering
    used heat-flow identities), so "genuine strengthening of HF25's
    `thm:counter`" holds only for the departure half.

## Controller errors noted (index note and commission)

- **Scope assignment.** The commission attached `app:positive` (line 1286) to
  this scope "insofar as the ellipse field is used by your scope". That
  appendix is the axisymmetric swirl seed `U_s`/`W_0` for the §7 comparison
  curve; it contains no ellipse field and is not used by §4 at all.
- **Index note, claim 2.** "a genuine strengthening of HF19-D and of HF25's
  `thm:counter`, both of which used linear heat flow" — true for the departure
  content, false if read as subsuming `thm:counter`, whose headline is a
  dissipation comparison proved through heat-flow identities that Navier–Stokes
  does not supply. Suggest: "strengthens the *departure* half of HF19-D and of
  HF25 `thm:counter` from the heat semigroup to the actual flow; the
  dissipation-comparison half is untouched."
- **Index note, claim 2, continued.** "every amplitude except possibly one" can
  be recorded as *the note's* claim; per R2 the construction supports every
  amplitude without exception, so the exception should not be carried forward
  into the plan as a limitation of the result.
- **Index note, audit checklist.** For `thm:NSdeparture` it lists "the
  inherited ellipse field" last; the prior and more consequential question is
  the §3 dependency of `prop:gapquadratic` (R1), which the checklist does not
  mention. The ellipse field itself was already verified twice in this
  repository (HF19-D and the HF25 audit) and a third time here.
- Not an error, for the record: the three pinned revisions do resolve in the
  three repositories, as the note and the index claim; I re-checked all three,
  and I additionally verified `prop:localtheory`(iii) **at the pinned
  `34cdffd`**, not only at the current working tree.

## What I did NOT check

- §3 (`thm:weightedresponse`, `thm:Aderivative`, `cor:second`) — another
  scope. My verdict is conditional on §3 **only** for the equality in
  `eq:gapquadratic`/`eq:NSgap`; after R1 the departure conclusion,
  `eq:NSgaplower` and the corollary are independent of §3.
- §§5–8 (temporal producer, integrated increments, crossings, comparison
  curve), `sec:boundary`, `sec:ledger`, and the appendices `app:spatial`,
  `app:weighted`, `app:positive`, `app:checks`. In particular I did not check
  `thm:curve`, `cor:curveenstrophy`, or the `W_0` seed.
- Tao's Theorem 5.4, Corollaries 4.3 and 5.8 themselves, and the manuscript's
  derivation of `prop:localtheory` from them. I relied on the statement at the
  pinned revision plus this repository's own audit
  (`cp02-review-local-theory-r2.md`, REPAIR, no invalid bridge).
- Whether `g_E ≠ 0`, or any numerical evaluation of `ΠN(U)`, `c`, `B`, `b`, or
  of a specific `ψ`. None is needed for the theorem; all are needed if the note
  ever wants an explicit numerical witness.
- Any quantitative statement about `‖q(u(t))‖_3` (the Bregman bounds give
  `‖q‖_3 ≳ √d ≍ t` and `‖q‖_3 ≤ (6d)^{1/3}`, but the note claims neither).
- Anything about `Q`, blowup, the endpoint theory, `hyp:temporal`, or NS-R3.
  Nothing in this scope bears on them, and this review promotes nothing.
- No Lean build, no kernel replay, no manuscript edit, no commit, no push.

## Output block

**MODE / RESULT.** REVIEW (Scope C), proof-audit discipline. **PASS WITH
SCOPE**: no invalid mathematical bridge; eight repairs R1–R8, of which R1
(re-base §4 on a §3-free lower bound) and R2 (delete "except possibly one" by
parity) are substantive and the rest are scope, attribution and presentation.

**CLAIM AND SCOPE CERTIFIED.** For the explicit compactly supported smooth
solenoidal ellipse field `U ∈ M`, every `ν > 0` and every `a > 0` (every `a`
except at most one, on the note's own argument; every `a` without exception
after R2), the classical Navier–Stokes branch from `aU` satisfies
`d(u^(a)(t)) > 0` for all sufficiently small `t > 0`, with
`d(u^(a)(t)) = ½a³t²‖νg_H − a g_E‖²_U + o(t²)` (equality conditional on §3;
"≥" unconditional after R1), hence `q(u^(a)(t)) ≠ 0`. Consequently no
homogeneous defect-feedback law with a coefficient integrable at `t = 0` holds
on all classical solutions.

**NON-CLAIMS.** No growth statement for `Q`, no singularity, no failure of any
input-dependent spacetime estimate, no dissipation-comparison conclusion, no
statement about `‖q‖_3` along the trajectory beyond positivity, no promotion of
any graph node, and no novelty claim for the ellipse construction, which is
this repository's own audited HF19-D material.
