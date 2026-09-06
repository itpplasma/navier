# HF28 audit — Section 5, Section 8 (thm:capped), Sections 9–11

Independent adversarial audit. Frozen candidate:
`research/evidence/hf28-weighted-spectral-continuation.tex`,
SHA-256 `80c6b1339704261d5540ce9620e5799f0e9c9ea7c78cd1af412d075ea8699055`
(recomputed here; matches the controller freeze).
Controller index note: `research/evidence/hf28-weighted-spectral-continuation.md`.
Nothing outside this file was edited, committed or pushed.

## 1. Scope

- **Section 5** `sec:spectral` (tex 469–521): `prop:spectral`, `eq:specenergy`,
  `eq:FN`, `lem:weightedY` (`eq:specY`, `eq:weightedY`).
- **Section 8** `sec:attempt` (tex 762–972): `eq:crudea`; `thm:capped` clauses
  (i)–(v) and its eight-step proof; the scope remark.
- **Section 9** `sec:boundary` (tex 973–1015): `hyp:producer` / `eq:missing`,
  the positive-implication chain, the status table.
- **Section 10** `app:cutoffs` (tex 1016–1023).
- **Section 11** `app:checks` (tex 1024–1040).

Sections 6–7 were re-derived only where 8–9 depend on them (`eq:Fpoint`,
`thm:weightedF`, `eq:UN`/`eq:VN`, `eq:logtest`, `thm:complete`, `H_E`).

Method: every algebraic step re-derived by hand, then confirmed with
sympy and with numerics (scripts in the session scratchpad; `eta/chi/L/B`
construction, exact-energy defect, `eq:cappedYexact` by finite differences,
the log rate against an analytic split for `4 <= N <= 10^12`, and an
independent extremal-trajectory ODE). Twelve refutation attempts, §7.

## 2. Verdict

**REPAIR.**

I found **no invalid mathematical step anywhere in scope**. Every clause of
`thm:capped` verifies, including the two that are easiest to get wrong
(global smoothness across the joint, and the exact energy identity). Section 5
is unconditionally correct with the stated constants. `eq:crudea` is correct
and — a finding the document does not claim — *rate-sharp* for the ingredients
it uses, in the large-data regime where its own countermodel lives (R5, R11).
Three things block PASS:

1. **The prior-art defect recurs, for the third time, in its strongest form.**
   The pre-cap branch of `eq:lambdaN` *is* the backward self-similar (Leray)
   ansatz; `eq:RW` *is* character-for-character the Leray-projected Leray
   profile equation — literally HF27's `eq:profileR`; and `eq:cappedT`
   *is* that equation's energy identity, equivalently `<R_W, W> = 0`
   (verified symbolically, §4). The document contains **zero** occurrences of
   "self-similar", "Nečas", "Růžička", "Šverák", "Tsai", "Scheffer" or
   "profile equation"; its single "Leray" is "Leray projection".
   `hf26-review-countermodel-crossings.md` R7 and
   `hf27-review-energy-concentration.md` R1–R3 already made this citation
   **mandatory in this repository for this exact ansatz**. (R1)
2. **One genuine logical gap in Step 6.** It defeats `V_N`, but
   `thm:onebudget` also licenses the *weaker* test `U_N < r_*^2`, and
   `U_N <= V_N` strictly. As written, the countermodel does not show
   `U_N >= r_*^2`. One constant repairs it. (R2)
3. **Section 9 is honest but materially incomplete.** `thm:complete`'s
   `eq:equivalence` makes `hyp:producer` *logically equivalent* to
   NS-R3 / Clay alternative A over all nonzero Schwartz data. Section 9 never
   cross-references it, and its status table lists the producer and the Clay
   alternative as two rows, which reads as a hierarchy where an equivalence
   exists. (R6, R7)

Plus disclosure/scope items R3–R5 and R8–R11, one of which (R11) records that
Section 8.1 **understates its own tools**: energy + `eq:specY` do give an
`N`-free bound on `a_N` below an explicit smallness threshold.
**The countermodel itself stands.**

---

## 3. THE DECISIVE QUESTION: does `thm:capped` stand?

**Yes. All five clauses verify independently. I could not break it.**

Setup as constructed: seed `hat W_0(xi) = (I - xi⊗xi/|xi|^2) e_1 phi(xi)`,
`phi` real even radial in `C_c^inf({1/2<|xi|<3/5})`; `W = A W_0`;
`c = Ybar/Ebar = ||grad W||^2/||W||^2` (amplitude-free, `c ∈ [1/4, 9/25]`);
`T = 1/(4 nu c)`; `kappa = N/2`, `t_N = T(1-kappa^-2)`;
`z_N = b_N lam_N W(lam_N x)`.

### (a) Are the curves genuinely globally smooth?

**Verified — and this is the construction's real content.**

- The seed is real, even, solenoidal, Schwartz, nonzero. The annulus avoids
  `xi = 0`, so the Leray symbol is smooth on the support; `(I-xi⊗xi/|xi|^2)e_1`
  vanishes only on the `xi_1`-axis, so a radial `phi` gives `W_0 != 0`.
- **The joint at `t_N` is exact, not `C^inf`-matched.** Substituting
  `t = t_N + T tau/kappa^2` into the first branch gives
  `1 - t/T = kappa^{-2}(1-tau)`, hence `(1-t/T)^{-1/2} = kappa (1-tau)^{-1/2}`;
  and on `tau ∈ [0,1/4]` one has `eta = 1`, `chi(tau) = tau`, so
  `L(tau) = (1-tau)^{-1/2}` and the second branch equals `kappa(1-tau)^{-1/2}`.
  The two formulas agree **identically** on a right-neighbourhood of `t_N`, and
  branch 1 is real-analytic there, so the glued function is analytic on a
  two-sided neighbourhood. The document's "agree on a neighborhood … not just
  to finitely many derivatives" is exactly right.
- **`lam_N` never blows up.** `eta ∈ [0,1]`, `eta = 0` for `s >= 3/4`, and the
  symmetry `eta(1-s) = 1-eta(s)` gives `int_0^1 eta = 1/2`; hence `chi <= 1/2`
  everywhere and `L ∈ [1, sqrt2]`, so `lam_N <= sqrt2 kappa = N/sqrt2`.
  Numerically: `eta` range `[0,1]`, `max|eta(1-s)-(1-eta(s))| = 4.4e-16`,
  `int_0^1 eta = 0.5`, `max chi = 0.5000`, `L ∈ [1, 1.41421356]`. All confirmed.
- After `tau >= 3/4`, `lam_N` is constant and `B ~ e^{-tau/2}`, so
  `z_N(t) -> 0` exponentially. **Defined and smooth on `[0, inf)`.**

The explicit `eta` from `vartheta(r) = e^{-1/r}/(e^{-1/r}+e^{-1/(1-r)})`,
`eta(s) = 1 - vartheta(2s-1/2)`, does satisfy all three requirements
(`=1` for `s<=1/4`, `=0` for `s>=3/4`, `eta(1-s)=1-eta(s)` from
`vartheta(r)+vartheta(1-r)=1`). Verified.

### (b) Is band-limitation preserved for all time?

**Verified.** `hat z_N(xi) ∝ hat W(xi/lam_N)` is supported in
`|xi| <= (3/5) lam_N <= (3/5) N/sqrt2 ≈ 0.4243 N`, inside `[-N,N]^3` for every
`t`. `z_N(0) = W` (since `lam_N(0)=1`, `b_N(0)=1`) and `J_N W = W` for every
`N >= 1` (support radius `3/5 < 1`). So `z_N(0) = W = J_N W` and
`J_N z_N = z_N` — clause (i) holds, and holds for the *common* datum `W`,
which is stronger than what the real comparisons have (`v_N(0) = J_N u_0`
varies with `N`).

### (c) Exact energy identity and the enstrophy inequality, with constants

**Both verified, and both are structurally forced.**

Scaling: `E_z = b^2 lam^{-1} E_W`, `Y_z = b^2 lam Y_W`,
`P_z = b^2 lam^3 P_W`, `||z||_6^4 = b^4 lam^2 ||W||_6^4`. Re-derived.

- **Energy.** `E_z' = -2 nu Y_z` requires exactly
  `d/dt log(b^2/lam) = -2 nu c lam^2`, i.e. `b = lam^{1/2} exp(-nu c ∫lam^2)`.
  So `eq:bN` is *not a choice* — it is the unique amplitude law compatible with
  clause (ii). Then `E_z = E_W exp(-2 nu c ∫ lam^2)` and
  `E_z + 2 nu ∫ Y_z = E_W` identically. Numerical defect
  `<= 4.2e-10` (N=16) / `1.7e-6` (N=256), pure quadrature error.
- **`b_N ≡ 1` on `[0,t_N]`** — this needs `nu c T = 1/4`, i.e. `T = 1/(4 nu c)`:
  `lam^{1/2} = (1-t/T)^{-1/4}` and `exp(-nu c ∫lam^2) = (1-t/T)^{nu c T}`.
  Confirmed numerically (`max|b-1| = 2.0e-12` at N=4).
- **Enstrophy.** With `lam'/lam^3 = eta/(2T) = 2 nu c eta`, differentiation
  gives exactly `eq:cappedYexact`,
  `Y_z' + nu P_z = nu b^2 lam^3[(4 eta - 2) c Y_W + P_W]`
  (finite-difference check: max relative error `1.0e-5` at N=32, `3.1e-4` at
  N=4, both grid-limited). The required inequality
  `Y_z' + nu P_z <= k nu^{-3} ||z||_6^4 Y_z` reduces exactly to
  `(4 eta - 2) c + Pbar/Ybar <= (k A^4 Lbar/nu^4) b^4`, and with `eta <= 1`
  and `b^4 >= e^{-3/2}` on the transition (`B >= e^{-3/8}`; numerically
  `min B = 0.885 > 0.687`), that is exactly `eq:Athreshold`.
  **`eq:Athreshold` is tight**: substituting it back gives
  `eta_max = 1` *identically* (sympy: the expression simplifies to `1`).
  The same `S` and `k = 27 S^2/16` as `eq:specY`; I re-derived `eq:specY`
  independently (Hölder `(6,3,2)`, `||grad v||_3 <= Y^{1/4}(S P^{1/2})^{1/2}`,
  Young at `eps = nu/2`) and got `27 S^2/16` exactly.
- `eq:seedratio`: `Pbar Ebar/Ybar^2 <= (9/25)/(1/4) = 36/25 < 2` — correct,
  and it is exactly what makes the bracket negative when `eta = 0`
  (so `N = 1,2,3` and the post-transition regime are free).

### (d) The logarithmic concentration rate, recomputed

**Verified exactly.** On `[0,t_N]`, `b_N ≡ 1` so
`||z_N||_6^4 = (1-t/T)^{-1}||W||_6^4` and
`∫_0^{t_N} = T ||W||_6^4 log kappa^2` — `eq:logpart` reproduces.
After `t_N`, `∫ = T||W||_6^4 ∫_0^{tau(H)} B^4 L^2 dtau` with
`B^4 L^2 = L^4 e^{-∫_0^tau L^2} <= 4 e^{-tau}` (numerically the ratio to
`4e^{-tau}` peaks at `0.7497 <= 1`), so the tail is uniformly bounded:
`∫_0^1 = 1.3099` (that is `H = T`, where `tau(H) = 1` exactly, as claimed) and
`∫_0^inf = 1.6823`.

Hence, exactly,
`a_N(H) = nu^{-3} T ||W||_6^4 [2 log N - 2 log 2 + I(tau_H)]`
`= alpha_W log N + O_W(1)`, `alpha_W = 2 T nu^{-3} ||W||_6^4`,
with `O_W(1)` uniform in `N` **and** in `H >= T`. Against the analytic split
(`nu=1, c=0.30`, `alpha_W = 1.66667`, offset `0.24665`) the direct quadrature
agrees to 6 significant figures for `4 <= N <= 512` and the analytic value is
exact out to `N = 10^12`. `alpha_W ∝ A^4` with `T` amplitude-free, so it is
arbitrarily large — confirmed.

Step 6 then gives, for `N >= 4` and `beta alpha_W >= 2`,
`V_N >= Kinf kappa_W N/4 >= r_*^2`; for `N <= 3` the exponential is `>= 1` and
`Kinf kappa_W/3 >= r_*^2` closes it. All three amplitude conditions
(`H_E(W) >= T`, `beta alpha_W >= 2`, `Kinf kappa_W/3 >= r_*^2`) grow in `A`
(as `A^4, A^4, A^2`) while `T` does not. Correct — **except** for the `U_N`
gap, R2.

### (e) What this actually excludes, and what it does not

**Excluded mechanism class (closed premise list).** Any derivation of
`hyp:producer` — equivalently, of an upper bound
`a_N(H_E) <= beta^{-1}[log(N nu^2/Y_0) + log(r_*^2/Kinf)]` for at least one
`N` — whose premises are contained in:

- (C1) real solenoidal Schwartz-valued curves, globally smooth on `[0,inf)`;
- (C2) a **common band-limited datum**, `z_N(0) = W = J_N W` for every `N`;
- (C3) band-limitation for all time, `J_N z_N = z_N`, and everything it
  implies: I checked that the curves also satisfy `Y <= 3N^2 E`,
  `P <= 3N^2 Y` and `Y_z(0) = Y_W` for every `N`;
- (C4) the exact scalar energy identity, hence `E` nonincreasing and
  `∫_0^inf Y = E_W/(2 nu)` **with equality**;
- (C5) the scalar enstrophy differential inequality `eq:specY` with the
  document's own `S, k` — hence also `eq:weightedY` and `Y <= Y_0 e^{k a}`,
  which the curves satisfy because those are derived from (C5) alone;
- (C6) uniform boundedness of the projected residual and of `∂_t z_N` in
  `L^{4/3}(0,inf; Hdot^{-1})` (clause (v), re-derived: `||R||_{Hdot^{-1}} =
  lam^{1/2}||R_W||_{Hdot^{-1}}` and `∫_0^{t_N} lam^{2/3} <= 3T/2`, plus
  `T kappa^{-4/3} ∫ ||R(tau)||^{4/3}` after `t_N`).

**Not excluded** — I verified each of these separates the curves from the
comparisons, so none of them is refuted:

- (N1) **the exact enstrophy identity** `½Y_N' + nu P_N = ∫(v·∇)v·Δv`. The
  curves are *visible* to it: Step 8's own pairing gives
  `<R_W, -ΔW> = Y_W/(4T) + nu P_W > 0`. (This is exactly the third scalar test
  HF26's audit R4 asked for, and HF28 supplies it — credit due.)
- (N2) anything using the residual's frequency structure `F_N =
  (I-J_N)(v_N⊗v_N)`, `eq:Fpoint`, or its `1/N` decay. Their residuals are
  bounded, not decaying, and — I computed this — their *certificate* stress
  diverges: with `Q_0 = 0` (common datum), `Z_H^2 = (4/3^{2/3}nu) e^{beta a_N}
  ∫_0^H e^{-beta a_N(t)}||F||_3^2 dt ≳ kappa^{beta alpha_W} -> inf`, and
  `||F_{z_N}||^2_{L^2_t L^3_x} ~ ||F_W||_3^2 T log kappa^2`. They are not
  accidentally admissible comparisons.
- (N3) anything using cross-`N` coherence (`v_N -> u`). The `z_N` do not
  converge; on `[0,T)` they converge to the *uncapped Leray self-similar
  curve*, which is the mechanism identification (§4).
- (N4) **small data.** The countermodel needs `A` above three explicit
  thresholds; it says nothing where the certificate is easy.
- (N5) the pressure, vorticity, local energy inequality, helicity, or higher
  projections `<∂_h A(v), ·>`.
- (N6) the **energy** projection of the residual: `<R_W, W> = 0` identically
  by the tuning of `T` (sympy: `<R_W,W> = -E_W/(4T) + nu Y_W`, zero iff
  `T = E_W/(4 nu Y_W)`). The curves are energy-blind and enstrophy-visible.
  Undisclosed in the document (R1, R4).

One-line statement of the class: **`thm:capped` excludes exactly the
"scalar-budget closures" — arguments that bound `a_N` using only scalar
functionals `E, Y, P, ||·||_6` of the comparison subject to the energy
identity, the enstrophy inequality, and band-limitation. It excludes nothing
that touches the vector equation, the residual's `N`-decay, or cross-`N`
coherence.** The document's own scope remark says essentially this and is
accurate.

### A sharpness fact the document misses (favourable)

The countermodel is the **minimal**, not the maximal, obstruction. Defeating
`eq:logtest` at every `N` requires only `a_N ≳ beta^{-1} log N`, so
`thm:capped` already kills every bound of the form `a_N <= C log N` with
`C > 1/beta`. That is the sharp reading, and it is stronger than the
document's own narrative ("`eq:crudea` permits quadratic growth", which
suggests a *rate* gap). See R5.

---

## 4. Comparison against the two earlier audited countermodels

| | HF26 (`hf26-review-countermodel-crossings.md`, PASS WITH SCOPE) | HF27 (`hf27-review-energy-concentration.md`, REPAIR) | HF28 `thm:capped` |
|---|---|---|---|
| curve | `v = b S_lam W`, `lam = (1-t/T_c)^{-1/2}` | `lam(t) W(lam(t)x)`, `lam = (1-t/T)^{-1/2}` | `b_N lam_N W(lam_N x)`, `lam_N` = the same, **capped at `kappa L(tau)`** |
| `T` | `T_c = E_W/(4 nu Y_W)` | `T = E_W/(4 nu Y_W)` | `T = 1/(4 nu c) = E_W/(4 nu Y_W)` — **identical** |
| interval | `[0, T_c)`, blows up | `[0, T)`, blows up | **`[0, inf)`, globally smooth** |
| family | one curve | one curve | **`N`-indexed family, one common datum** |
| band-limited | no | no | **yes, `J_N z_N = z_N` for all `t`** |
| energy identity | exact | exact | exact |
| enstrophy | exact cubic identity | not the target | **the same inequality `eq:specY`, same `S,k`** |
| residual | `R != 0` via ESS/GKP | `R != 0` via ESS endpoint | `R != 0` via elementary parity + `<·,-ΔW>` |
| self-similar prior art cited | **no** (R7 required it) | **no** (R1–R3 required it) | **no** — third occurrence |

**Is HF28 genuinely stronger? Yes, on three axes, and the claim is fair —
with one caveat about how it is phrased.**

1. **Global definedness — real and decisive.** HF26/HF27's curves cease to
   exist at `T_c`. HF28's are smooth on `[0,inf)`, obey the energy identity
   there with `E -> 0`, and are tested at `H_E >= T`, i.e. *past* the
   concentration time. The document's phrase "a comparison curve undefined
   after its concentration time" is an accurate description of both
   predecessors, and HF28 does improve on it.
2. **Common `N`-indexed datum — new and necessary.** The producer it attacks
   is an `∃N` statement; a single curve cannot refute it. Choosing a
   band-limited `W` also sets `Q_0 = 0`, i.e. the countermodel *helps* the
   certificate and still defeats it. Neither predecessor had this.
3. **Band-limitation — new.** `J_N z_N = z_N` matches the exact structural
   property of the objects under attack.

**Caveat.** The other half of the comparative sentence — "stronger … than an
abstract blowing-up scalar ODE" — does **not** describe HF26 or HF27. HF26's
audit is explicit ("This is a genuine countermodel, not a formal analogy";
"it obeys them with the same constants a real trajectory does"). Read as a
comparison to the in-repo predecessors, that half is a strawman. It should
either name what it compares to, or be dropped.

**Does the prior-art defect recur? Yes — identically, and this is the third
time.** Confirmed by direct symbolic match, not by analogy:

- `eq:lambdaN` pre-cap branch = `lam(t) = (1-t/T)^{-1/2}` = NRS/Tsai (1.2)
  with `a = 1/(2T)` — verbatim HF27's `eq:conccurve`.
- `eq:RW`: `R_W = (1/2T)Λ W + P div(W⊗W) - nu ΔW`, `ΛW = W + (x·∇)W`
  — **character-for-character HF27's `eq:profileR`**, i.e. the
  Leray-projected Leray profile equation (1.3).
- `eq:cappedT`: `T = 1/(4 nu c) = E_W/(4 nu Y_W)` — sympy confirms this is
  exactly `<R_W, W> = 0`, i.e. the Leray profile energy identity
  `nu||∇U||^2 = (a/2)||U||^2`. HF28 *derives* it (from requiring the energy
  identity) without ever naming it.
- `∫_0^{t_N} lam^{2/3} dt <= 3T/2` (Step 7) — verbatim HF27's computation.
- `<ΛW, -ΔW> = Y_W/2` — the standard dilation law for enstrophy.
- The `N -> inf` limit of the family, on `[0,T)`, **is** the NRS/Tsai object:
  `t_N ↑ T` and `b_N ≡ 1` there, so `z_N -> (1-t/T)^{-1/2} W((1-t/T)^{-1/2}x)`
  locally uniformly. The construction is precisely *the Leray self-similar
  blow-up curve regularized at the spectral cutoff scale*.

Grep over the whole 1078 lines: `self-similar` 0, `Nečas`/`Necas` 0,
`Růžička`/`Ruzicka` 0, `Šverák`/`Sverak` 0, `Tsai` 0, `Scheffer` 0,
`profile equation` 0; `Leray` appears once, as "Leray projection".

**One point in HF28's favour.** Unlike HF27, HF28 does **not** need
NRS/Tsai mathematically: Step 8 proves `R_W != 0` by an elementary
parity argument plus `<R_W,-ΔW> = Y_W/(4T)+nu P_W > 0` for its explicit `W`
(and `nu(P_W - Y_W^2/E_W) > 0` by strict Cauchy–Schwarz for `N<=3`; strict
because a smooth profile on an annulus is not carried by one sphere). That
route is self-contained and arguably cleaner than HF27's endpoint import.
The obligation is therefore attribution of the *ansatz and the profile
equation*, not replacement of the proof (R1).

---

## 5. Per-question findings

### Q2 — Section 5: do the global comparisons exist for every datum, with the claimed unconditional identities?

**PASS.** Re-derived in full.

- Well-posedness: on the closed real solenoidal `L^2` subspace with support in
  `[-N,N]^3`, `Δ` is bounded (`<= 3N^2`), Fourier inversion gives
  `||v||_inf <= (2N)^{3/2}(2π)^{-3/2}||v||_2`, and
  `||J_N P div(v⊗v)||_2 <= 2√3 N ||v⊗v||_2 <= C N^{5/2}||v||_2^2`
  (the `2√3 N` because `v⊗v` lives in `[-2N,2N]^3` before truncation — the
  document's `CN` is right). Polarization gives local Lipschitz; Picard–
  Lindelöf gives a local solution; the subspace is invariant; reality and
  solenoidality are preserved because both symbols are real and even.
- Energy: testing with `v_N` removes both projections (`J_N P v_N = v_N`,
  self-adjointness) and the convection integral vanishes by
  `∫ v_i v_j ∂_j v_i = ½∫ v·∇|v|^2 = 0`. `eq:specenergy` holds with
  `||J_N u_0||_2^2 <= E_0`. The a priori `L^2` bound plus local Lipschitz on
  balls gives **global** existence for **every** datum. Spatial regularity is
  Bernstein; time regularity is the polynomial field. **Unconditional.**
- `eq:FN`: `R_{v_N} = (I-J_N)P div(v⊗v) = P div F_N` with
  `F_N = (I-J_N)(v_N⊗v_N)`, since `(I-J_N)` commutes with `P` and `div`. ✓
- `eq:specY`: re-derived from scratch — the `-Δv_N` test is in the range of
  both projections, so they disappear *exactly*; then Hölder `(6,3,2)`,
  `||∇v||_3 <= ||∇v||_2^{1/2}||∇v||_6^{1/2}`, `||∇v||_6 <= S||Δv||_2`
  (Plancherel `||∇^2v||_2 = ||Δv||_2`) and Young `a x^{3/4} <= εx +
  27a^4/(256ε^3)` at `ε = nu/2` give **exactly** `k = 27S^2/16`. ✓
- `eq:weightedY`: `d/dt(e^{-k a_N}Y_N) <= -nu e^{-k a_N}P_N`, integrate,
  `Y_N(0) <= Y_0`. ✓ Both are genuinely unconditional — no property of the
  unknown exact solution enters.

Only presentational point: Section 5's opening proves the uniform `L^p`
bound and strong `L^p` convergence of `J_N`, which Appendix A then declares
unused. I traced every use and confirm they are unused (R9).

### Q3 — `eq:crudea`: correct, and is it conceding too much or too little?

**Correct, and conceding exactly the right amount. It is rate-sharp.**

The chain `||v||_6^4 <= S^4 Y^2`, `Y_N <= 3N^2 E_0` (cube, `|xi|^2 <= 3N^2`),
`∫_0^H Y_N <= E_0/(2nu)` gives `3S^4 N^2 E_0^2/(2 nu^4)` — sympy confirms the
product is identical to the display.

I tried three alternative routes:

1. **Fourier Cauchy–Schwarz.** `Y^2 <= E P`, then `P <= 3N^2 Y` and
   `∫Y <= E_0/2nu`: gives `3 S^4 N^2 E_0^2/(2 nu^4)` — the *same constant*.
2. **Bernstein split.** `||v||_6^4 = ||v||_6^2·||v||_6^2 <= S^2 Y · C_B^2N^2E`:
   gives `C_B^2 S^2 N^2 E_0^2/(2 nu^4)` — same rate, possibly better constant,
   no gain in `N`.
3. **Weighted budget.** `nu ∫ e^{-k a_N} P_N <= Y_0` only yields
   `a <= (S^4 E_0 Y_0/2nu^4) e^{k a}`, which is self-referential and gives no
   unconditional `N`-improvement.

**And no better rate is available from those ingredients at all.** Inside
the *same* ansatz `z = b lam W(lam x)` with `b` forced by the exact energy
identity, common datum `lam(0)=1`, band limit `lam <= Λ_N`, and the *same*
enstrophy inequality, the maximal-growth trajectory is governed by
`dm/ds <= 2 C_1 m^2 e^{-4 nu c s}` (`m = lam^2`, `s = ∫lam^2 dt`,
`C_1 = k nu^{-3}||W||_6^4/2`), which permits `m` to reach the cap in bounded
`s` whenever `k A^4 Lbar/(4 nu^4 c) > 1` — and `eq:Athreshold` already forces
that ratio above `e^{3/2}/2 ≈ 2.24`. Integrating numerically at
`Gamma = 1.02 ×` the document's own threshold:

```
 cap Λ        a (units nu^-3||W||_6^4)       a/Λ^2      s_cap
    16                    156.139          0.609918    0.2671
    64                   2475.790          0.604441    0.2683
   256                  39580.082          0.603944    0.2683
  1024                 633235.652          0.603901    0.2684
  4096               10131686.582          0.603896    0.2684
```

i.e. `a_N = Θ(N^2)`, converged to six digits, with the cap reached at bounded
`s` (hence bounded `t < T <= H_E`). **So `eq:crudea`'s `N^2` is rate-sharp
for the information (i)–(iii)**, the document is not conceding too much, and
its own `log`-rate curve is the *minimal* obstruction, not the maximal one.
(Cross-check: the quadratic construction respects `eq:crudea` with a factor
`c/9 <= 0.04` of slack, as it must.) See R5.

**But there is an exact dichotomy, and it settles a disagreement in the
controller note.** The note (revised while this audit ran) states that
energy-and-Sobolev-give-only-quadratic "excludes the document's own spectral
enstrophy inequality, which does better". Both statements are true, in
disjoint regimes, and the split is explicit. Keep the weight inside:

```
a_N' = nu^-3 ||v||_6^4 <= nu^-3 S^4 Y^2 <= nu^-3 S^4 E P        (Y^2 <= E P, Fourier C-S)
=>  int_0^H e^{-k a_N} a_N' dt  <=  nu^-3 S^4 E_0 int e^{-k a_N} P  <=  S^4 E_0 Y_0/nu^4  =: mu
                                                                 (eq:weightedY)
LHS = (1 - e^{-k a_N(H)})/k   exactly.      =>   e^{-k a_N(H)} >= 1 - k mu.
```

- If `k mu < 1`, i.e. **`E_0 Y_0 < nu^4/(k S^4) = 16 nu^4/(27 S^6)`**, then
  `a_N(H) <= -(1/k) log(1 - k S^4 E_0 Y_0/nu^4)` **for every `N` and every
  `H`** — an `N`-free bound, incomparably better than quadratic, and it makes
  `eq:logtest` fire for all large `N`. (That region is about `9.5x` larger than
  `lem:smallEY`'s `nu^4/(16 S^6)`.) So the note's correction is right, with
  this explicit constant.
- If `k mu >= 1` the same inequality is **vacuous**: `(1-e^{-ka})/k <= 1/k <= mu`
  identically. And this is exactly where the countermodel lives: there
  `Gamma = k A^4 Lbar/nu^4 >= 4.123` and `Lbar <= S^4 Ybar^2`, `c <= 9/25`, so
  `k S^4 E_0 Y_0/nu^4 >= Gamma/c >= 11.4 > 1`. Above the threshold, my
  `Theta(N^2)` family shows nothing better than `eq:crudea` follows from
  (i)–(iii).

**Dichotomy.** `E_0 Y_0 < nu^4/(kS^4)`: energy + `eq:specY` give an `N`-free
bound. `E_0 Y_0 >= nu^4/(kS^4)`: they give nothing beyond `eq:crudea`, which is
then rate-sharp. No contradiction between the two lanes; the countermodel is
provably confined to the second regime, which is also the only regime the Clay
statement is about. Section 8.1's "It does not supply a bound on `a_N` by
reversing Gronwall" is therefore **too pessimistic as written** (R11).

### Q4 — Section 9: is the "first unresolved implication" honest and complete? Is the handoff precise?

**Honest; the handoff is precise; but incomplete on three counts.**

Correct as written: `eq:missing` is exactly `eq:logtest` at `H = H_E`, i.e.
`V_N(H_E) < r_*^2`; all its terms are defined without assuming continuation of
the exact solution (`a_N` involves only `v_N`; `E_0, Y_0` are data); and the
positive chain `eq:missing ⟹ Z_{H_E} < r_* nu ⟹ u-v_N ∈ L^4_tL^6_x ⟹ T_*>H_E
⟹ T_*=∞` is valid step by step (I re-derived `U_N`, `V_N` and the `H_E`
margin; all reproduce). The zero datum is handled. The statement "Any
successful continuation … must use additional information from the actual
truncated vector equation" is a fair and precise handoff.

Incomplete:

1. **The equivalence is not cross-referenced.** `thm:complete`'s
   `eq:equivalence` says `T_* = ∞ ⟺ ∃N: V_N(H_E) < r_*^2` for each nonzero
   datum. Quantifying over all `nu` and all nonzero Schwartz `u_0`,
   `hyp:producer` is therefore **logically equivalent to NS-R3 / Clay
   alternative A**. Section 9 says only "Conditional completeness cannot
   supply it", which acknowledges the dependency without stating the
   equivalence. The status table then lists the producer and the Clay
   alternative as separate "not proved" / "not established" rows, which reads
   as a hierarchy. The document is not concealing this — Section 7's remark
   says `eq:equivalence` "states the exact logical strength of the producer" —
   but a reader of Section 9 alone is misled. (R6)
2. **The producer is stated in the non-minimal form.** `thm:onebudget`
   licenses the weaker `U_N < r_*^2`, and `U_N <= V_N` strictly
   (`Kinf/(3^{-2/3}S) = 1 + 16S/sqrt(2δ) > 1`). So `eq:missing` is sufficient
   but not the weakest remaining statement. Asymptotically harmless
   (`Φ(a) -> (2δ)^{-1/2}`, so `U_N/V_N -> 1` as `a_N -> ∞`), but it should be
   recorded. (R7)
3. Given (1), the countermodel's message ("scalar budgets do not decide")
   is, at the level of logic, unsurprising — the producer is equivalent to a
   Clay problem. Its real value is the *specific* premise list it closes off,
   which Section 9 states only in prose. (R4)

### Q5 — Section 10: are the spectral assumptions actually used the ones listed?

**Yes for `J_N`. Nothing is smuggled in. Two omissions.**

I traced every place `J_N` could carry an `L^p` bound:

- `prop:spectral` uses only `||J_N||_{L^2→L^2} <= 1`;
- `eq:dN` and `eq:Fpoint` come from `eq:highpass`, which is pure
  `L^2` interpolation (`||h||_3^2 <= ||h||_2||h||_6`) plus Sobolev plus
  `|xi| >= N` off the cube — no multiplier theory;
- `thm:certificate`'s `F ∈ L^2_t L^3_x` hypothesis is met for fixed `N,H` by
  smoothness of `v_N`;
- `thm:complete` uses only Plancherel tails `eq:tailHm` and `H^m` bounds;
  `h_N(0) = 0` needs no convergence statement.

So `J_N ∈ L(L^p)` and `J_N f -> f` in `L^p` are genuinely unused, and the
generalized family `B_N ⊆ K_N ⊆ B_{cN}`, symmetric, works: it is an `L^2`
orthogonal projection, preserves reality (real even symbol) and solenoidality,
commutes with derivatives, has bounded support (ODE + Bernstein), and its
complement lies in `{|xi| >= N}` (this is exactly what `eq:highpass` needs).
The certificate constants `beta, Kinf, r_*, k, S` are geometry-free, so
"the same analytic constants in its displayed test" is correct, and the sharp
ball is legitimately admitted.

Two omissions, neither an error:

- The **Leray projection's** `L^p` bounds `C_3, C_9, C_{9/2}` remain
  load-bearing in *every* constant (`Csharp`, `c_q`, `b`, `c_b`, `beta`,
  `r_*`). An appendix titled "which spectral assumptions are actually used"
  that discusses only `J_N` invites the reading that no multiplier `L^p`
  theory is used. (R8)
- `eq:crudea`'s `Y_N <= 3N^2E_0` *is* cube-specific; for the general family it
  becomes `c^2 N^2 E_0`. Harmless (it is not part of the test) but it should
  be said, since Section 8 uses it. (R8)

Also: Section 5's remark ("A sharp ball projection cannot replace the cube
without checking the required `L^p` bounds") is stated flatly and is then
contradicted by Appendix A. (R9)

### Q6 — Section 11 checklist: do the items reproduce?

Spot-checked **seven**; six reproduce exactly, one needs a hypothesis, and the
companion file is missing.

| item | result |
|---|---|
| `(I+⅓e⊗e)(I-⅓e⊗e) = I-⅑e⊗e` | reproduces **only for `|e| = 1`**; sympy gives the residual `(1-|e|^2)e⊗e/9`. In context `e = z/|z|`, so the document's `eq:matrixnatural` is right; the *checklist* omits the hypothesis. (R10) |
| `27b^4/(256(nu/4)^3) = c_b nu^{-3}` | **reproduces exactly** (sympy difference `0`), with `b^4 = 12a_0(1+2C_{9/2})^4`, `c_b = 81a_0(1+2C_{9/2})^4` |
| `k = 27S^2/16` | **reproduces**, re-derived from the `L^4_tL^6_x` estimate independently |
| `beta/k = 36(1+2C_{9/2})^4` | **reproduces exactly** (sympy, with `a_0 = 9S^2/8`, `beta = 2c_b/3`) |
| time-weight primitive `eq:exacttimeintegral` | **reproduces**: `∫ f^4 e^{-2δa}dt = nu^3(1-e^{-2δ a(H)})/(2δ)`, and the document's remark that it survives flat pieces of `a_N` is correct (no inverse substitution is used) |
| factor-of-two margin at `H_E` | **reproduces**: `E_0·E_0/(2 nu H_E) = nu^4/(32S^6)`, exactly half the `nu^4/(16S^6)` threshold |
| cap's energy/enstrophy differentiation | **reproduces** (§3c above) |
| powers in `thm:weightedF` (not listed but implied) | **reproduce**: I re-derived `eq:weightedF` and `U_N` end to end and got the displayed constants `4S^2 nu Y_0 Φ/N` and `3^{-2/3}(κ_0/N)e^{βa}[S+16S^2Φ]` exactly |
| `check_weighted_spectral.py` | **DOES NOT EXIST.** Not in the repository (`find` over the whole tree), and not beside the original drop in `~/Nextcloud/navier/` (which holds only `.tex`/`.pdf`). The randomized two-point natural-distance sample is therefore **unreproducible as delivered**. (R10) |

---

## 6. Repairs

**R1 (prior art, mandatory — third occurrence in this programme).**
In `thm:capped` Step 1–2, state that the branch `lam_N = (1-t/T)^{-1/2}` is
the backward self-similar (Leray) ansatz, that `eq:RW` is the Leray-projected
Leray profile equation, and that `eq:cappedT` (`T = 1/(4 nu c) =
E_W/(4 nu Y_W)`) is that equation's energy identity, equivalently
`<R_W, W> = 0`. Add that the `N -> ∞` limit of the family on `[0,T)` is
exactly that self-similar curve, so the construction is a smooth spectral-scale
regularization of a known object. Cite:
- J. Leray, *Sur le mouvement d'un liquide visqueux emplissant l'espace*,
  Acta Math. **63** (1934), 193–248 (the ansatz and the profile equation);
- J. Nečas, M. Růžička, V. Šverák, *On Leray's self-similar solutions of the
  Navier–Stokes equations*, Acta Math. **176** (1996), 283–294,
  DOI `10.1007/BF02551584`;
- T.-P. Tsai, *On Leray's self-similar solutions … satisfying local energy
  estimates*, Arch. Ration. Mech. Anal. **143** (1998), 29–51,
  DOI `10.1007/s002050050099`; erratum ibid. **147** (1999), 363.
Record that Tsai's Remark 5.5 (Scheffer's question, `U·g <= 0`) is the nearest
prior notion of a Leray profile carrying a residual, and that the tuning puts
`<R_W, W> = 0` exactly on that boundary. **Do not replace Step 8's proof** —
the elementary parity + `<·,-ΔW>` argument is self-contained and needs no
import; label it as such. This repair discharges the standing obligation from
HF26 R7 and HF27 R1–R3.

**R2 (logical gap, mandatory).** Step 6 shows `V_N >= r_*^2`, but
`thm:onebudget` also licenses the weaker test `U_N < r_*^2`. Replace the
amplitude condition `Kinf κ_W/3 >= r_*^2` by `3^{-2/3} S κ_W/3 >= r_*^2`
(which is stronger since `Kinf > 3^{-2/3}S`) and state the conclusion as
`U_N(H_E(W)) >= r_*^2` for every `N >= 1`; `V_N >= U_N` then follows. Without
this, the countermodel does not defeat the sharper form of the certificate.

**R3 (scope, mandatory).** Disclose that `thm:capped` is a **large-amplitude**
statement: it requires `A` above three explicit thresholds (`eq:Athreshold`,
`beta alpha_W >= 2`, and the `κ_W` condition of R2), i.e. large `κ_0 = Y_0/nu^2`
and large `H_E`. The exclusion is at large data, not uniform in the datum;
the certificate is not shown to be undecided in any small- or moderate-data
regime. (Amplitude scaling `W ↦ AW` is *not* the Navier–Stokes symmetry, so
this is a genuine Reynolds-number condition, not a scaling artefact — which is
also why the countermodel is legitimate for the Clay statement.)

**R4 (scope).** State the exclusion as a closed premise list (C1)–(C6) with
the non-exclusions (N1)–(N6) of §3(e), in the style HF26's audit required.
In particular record that (a) `<R_W, W> = 0` identically, so the curves are
invisible to the energy projection *by construction of `T`*, while
`<R_W, -ΔW> > 0`, so they are visible to the enstrophy identity; and (b) the
certificate stress `||F_{z_N}||^2_{L^2_t L^3_x}` diverges like `log N`, so the
curves are not accidentally admissible comparisons.

**R5 (sharpness, Section 8.1).** Two additions.
(i) State the sharp reading: `thm:capped` defeats every bound of the form
`a_N <= C log N` with `C > 1/beta`, so the gap is not merely "quadratic where
logarithmic is needed" — it is a *constant* gap at the logarithmic rate.
(ii) State that `eq:crudea` is **rate-sharp** for its ingredients: inside the
same ansatz, subject to (i)–(iii), there exist curves with `a_N = Θ(N^2)`
(verified numerically to six digits at the document's own amplitude
threshold). Then the document's own log curve is the minimal, not the maximal,
obstruction, and no route using only (i)–(iii) can improve the `N^2` rate —
*in the regime `E_0 Y_0 >= nu^4/(k S^4)` where `thm:capped` lives*. Below that
threshold see R11.

**R6 (Section 9, mandatory).** Cross-reference `eq:equivalence` in Section 9
and state plainly that `hyp:producer` is **equivalent** to NS-R3 / Clay
alternative A over all nonzero Schwartz data and all `nu > 0`. Merge or
annotate the last two rows of the status table accordingly; as printed they
imply a strict hierarchy that `thm:complete` denies.

**R7 (Section 9).** Record that `eq:missing` is stated in the `V_N` form and
is therefore *sufficient but not minimal*; the weakest remaining statement is
`∃N: U_N(H_E) < r_*^2`, and `U_N/V_N -> 1` as `a_N -> ∞`.

**R8 (Section 10).** Add that the Leray projection's `L^p` bounds
`C_3, C_9, C_{9/2}` remain load-bearing in every constant of the test — the
appendix's claim is about `J_N` only. Add that `Y_N <= 3N^2E_0` in
`eq:crudea` is cube-specific and reads `c^2N^2E_0` for the general family.

**R9 (Section 5).** The remark "A sharp ball projection cannot replace the
cube without checking the required `L^p` bounds" is contradicted by
Appendix A. Cross-reference, or scope it explicitly to the attachment's proof.

**R10 (Section 11).** `check_weighted_spectral.py` is not present in the
repository nor beside the delivered `.tex`. Ship it or delete the sentence;
as written the checklist is unreproducible. Add `|e| = 1` to the first
identity. (Everything else I spot-checked reproduces exactly.)

**R11 (Section 8.1, mandatory).** "The enstrophy inequality `eq:specY` …
does not supply a bound on `a_N` by reversing Gronwall" is too pessimistic.
Combined with the energy identity and `Y^2 <= E P`, `eq:weightedY` gives the
exact inequality `(1 - e^{-k a_N(H)})/k <= S^4 E_0 Y_0/nu^4`, hence the
`N`-free, `H`-free bound `a_N <= -(1/k) log(1 - k S^4 E_0 Y_0/nu^4)` whenever
`E_0 Y_0 < nu^4/(k S^4) = 16 nu^4/(27 S^6)`. State this, state that it is
vacuous above that threshold, and state that `thm:capped` is confined to the
vacuous side (`k S^4 E_0 Y_0/nu^4 >= 11.4` there). This makes the true shape of
the obstruction visible: the certificate is proved to fire in an explicit
smallness region, and the countermodel shows the scalar budgets decide nothing
outside it.

**Minor, not numbered.** `alpha_W = 2T nu^{-3}||W||_6^4` reads as `nu^{-3}`
but `T = 1/(4 nu c)`, so `alpha_W = ||W||_6^4/(2 nu^4 c)`; printing the
`nu^{-4}` form makes the scaling check visible.

---

## 7. Refutation attempts (12; one partial success)

1. **Break global smoothness at the joint `t_N`.** FAILED. The two branches
   agree *identically*, not asymptotically, on `tau ∈ [0,1/4]`; branch 1 is
   analytic at `t_N`, so the glued curve is analytic on a two-sided
   neighbourhood.
2. **Break band-limitation at peak concentration.** FAILED. `max lam_N =
   √2κ = N/√2`, support radius `<= 0.4243 N`, comfortably inside the cube.
3. **Break the exact energy identity.** FAILED, and instructively: `eq:bN` is
   *forced* by it (`b = lam^{1/2}e^{-nu c∫lam^2}` is the unique solution of
   `d/dt log(b^2/lam) = -2 nu c lam^2`), and `T = 1/(4nu c)` is forced by
   `b ≡ 1` on the self-similar branch. Numerical defect `<= 4e-10`.
4. **Break the enstrophy inequality at the transition.** FAILED.
   `eq:Athreshold` is exactly tight: substituting it gives `eta_max = 1`
   identically (sympy). The `b >= e^{-3/8}` bound on `[0,3/4]` is true with
   room (numerical min `0.885` vs `0.687`).
5. **Show the log rate is really `O(1)` or `O(N^ε)`.** FAILED. The rate is
   exactly `alpha_W log N + O_W(1)`, `alpha_W = 2T nu^{-3}||W||_6^4`, matching
   an analytic split to 6 significant figures for `4 <= N <= 512` and exactly
   out to `N = 10^12`; the tail is uniformly bounded (`∫_0^∞ B^4L^2 = 1.6823`).
6. **Show the curves are secretly admissible comparisons** (which would make
   the certificate apply and contradict the failure). FAILED. With `Q_0 = 0`,
   `Z_H^2 ≳ κ^{beta alpha_W} -> ∞` and `||F_{z_N}||^2_{L^2L^3} ~ log κ^2`.
   They are excluded exactly as claimed.
7. **Find a band-limitation-derived scalar constraint they violate.** FAILED.
   `Y <= 3N^2E`, `P <= 3N^2Y`, `∫_0^∞ Y = E_0/(2nu)`, `eq:crudea` and
   `eq:weightedY` all hold, with slack (`Y_z/E_z <= 0.18N^2` vs `3N^2`).
8. **Show the enstrophy inequality can only be met by violating Sobolev**
   (`||z||_6 <= S||∇z||_2`), making the countermodel vacuous. FAILED. The
   Sobolev-consistent form `nu[2cY_W+P_W] <= k nu^{-3}S^4 b^4 Y_W^3` scales
   as `A^2` vs `A^6` and holds for large `A`. `||W||_6 <= S Y_W^{1/2}` is
   automatic and does not conflict with `eq:Athreshold`.
9. **Add the Hölder form of the exact enstrophy identity**
   (`½Y'+nuP <= ||z||_∞||∇z||_2||Δz||_2`) as an extra premise. FAILED: the
   requirement reduces to `b >= 2 nu c Y_W^{1/2}/(||W||_∞ P_W^{1/2}) ∝ A^{-1}`,
   satisfied at large amplitude. Only the enstrophy *identity itself* — with
   the vector nonlinearity — separates the curves, and that is outside the
   premise list, as the document says.
10. **Attack Step 6 through the `U_N`/`V_N` distinction.** **PARTIAL
    SUCCESS** — the one genuine gap in scope. Step 6's amplitude condition
    defeats `V_N` but not the weaker `U_N` test that `thm:onebudget` also
    licenses. Repaired by one constant (R2); the countermodel survives.
11. **Show a better-than-quadratic bound follows from (i)–(iii) after all**,
    which would make `eq:crudea` a lossy concession. FAILED and instructive:
    the same ansatz admits curves with `a_N = Θ(N^2)` (`a/Λ^2 -> 0.6039`,
    converged to six digits at `1.02 ×` the document's own amplitude
    threshold, cap reached at bounded `s_cap = 0.268 < T`). `eq:crudea` is
    rate-sharp *above the smallness threshold* `E_0Y_0 >= nu^4/(kS^4)`; below
    it the enstrophy inequality gives an `N`-free bound (§5 Q3). The
    countermodel is provably confined to the sharp side. (→ R5, R11)
12. **Break the seed** (non-Schwartz, non-solenoidal, zero, or support
    touching the origin). FAILED. `hat W_0 = (I - ξ⊗ξ/|ξ|^2)e_1 φ` with radial
    `φ` on `{1/2<|ξ|<3/5}` is real, even, solenoidal, Schwartz and nonzero;
    the annulus avoids the projector's singularity, and `eq:seedratio`
    (`36/25 < 2`) holds with the stated slack.

---

## 8. Controller-note observations

The index note was revised by a parallel lane while this audit ran; the
version I read at the end already self-corrects its "arithmetic rather than
conceptual" framing and records the equivalence. Provenance is accurate (I
recomputed the SHA-256 and re-verified the research pin). Three points remain.

1. **Independently confirmed, not an error.** The note's revised
   "FIRST GAP: Clay alternative A" matches what I found from Section 9's own
   scope: `thm:complete`'s `eq:equivalence` makes `hyp:producer` equivalent to
   NS-R3 over all nonzero Schwartz data. My R6/R7 concern only that **Section 9
   of the document never cross-references `eq:equivalence`** and states the
   producer in the non-minimal `V_N` form — the note is now ahead of the
   document on this point, not behind it.
2. **Partly right, needs the threshold — the note as written overstates it.**
   "This note also repeated as fact the document's statement that energy and
   Sobolev supply only quadratic growth; the audit found that excludes the
   document's own spectral enstrophy inequality, which does better." The
   enstrophy inequality does better **only when `E_0 Y_0 < nu^4/(kS^4) =
   16nu^4/(27S^6)`**; above that threshold the derived inequality is
   identically vacuous, and I constructed curves inside the document's own
   premise class with `a_N = Theta(N^2)`, so no better-than-quadratic bound is
   available there. The note should carry the threshold, otherwise it reads as
   a general refutation of `eq:crudea`, which is false — and `thm:capped`
   itself provably lives on the vacuous side (`k S^4 E_0Y_0/nu^4 >= 11.4`).
3. **The standing prior-art obligation is still not carried forward.** The
   note correctly says the countermodel must be checked "against our audited
   HF26 countermodel and HF27 concentration test, both of which used the
   backward self-similar family", but does not record that HF26 R7 and HF27
   R1–R3 already made citation of Leray / NRS / Tsai **mandatory in this
   repository for this exact ansatz**. This should be a standing checklist item
   for any future document reusing `lam = (1-t/T)^{-1/2}`,
   `T = E_W/(4 nu Y_W)` or `Lambda W = W + (x·∇)W`. Relatedly, "The prior-art
   claims, which are better than its predecessors'" is only half true: the
   improvement is real for CCRT / Pham / Diening–Kreuzer and nil for the
   countermodel's own ansatz, where the defect is identical to HF27's.

Also unrecorded: Section 11 references a companion script
`check_weighted_spectral.py` that was **not delivered** with the artifact and
does not exist anywhere in the repository or the capture surface (R10).

## 9. What I did NOT check

- Sections 2, 3, 4, 6 and 7 as such. I re-derived only what Sections 5 and
  8–9 consume (`eq:specY`, `eq:weightedY`, `eq:Fpoint`, `thm:weightedF`,
  `eq:UN`/`eq:VN`, `eq:logtest`, `thm:complete`'s statement, `H_E`). I did
  **not** audit `thm:natural` (the difference-quotient limit at `V = 0` or at
  infinity), `prop:relative`'s residual sign/tensor convention,
  `lem:transport`, or Steps 1–3 of `thm:certificate`.
- The numerical admissibility of `S, C_3, C_9, C_{9/2}` and hence the actual
  values of `beta, δ, Kinf, r_*`. Every check here is symbolic in them.
- `Lbar = ||W_0||_6^4` for a concrete `φ`. The proof uses only
  `0 < Lbar < ∞`, which is immediate; I did not compute it.
- I did not fetch or retain any third-party PDF. The Leray/NRS/Tsai
  identification rests on (a) the verbatim NRS/Tsai (1.2)/(1.3) forms already
  extracted and quoted in `hf27-review-energy-concentration.md`, and (b) my
  own symbolic match of those forms to `eq:RW` and `eq:cappedT`. Bibliographic
  data in R1 is copied from HF27's audit and should be re-verified against the
  primary sources before it is printed in the manuscript.
- The other two repository pins, the attachment SHA-256 values in Section 1.2,
  the PDF build, and reference integrity.
- The existential status of the certificate as a whole (another scope),
  beyond recording the `eq:equivalence` consequence that Section 9 needs.
- Whether `thm:capped`'s `L^{4/3}(0,∞;Hdot^{-1})` claim (v) is *sharp*; I
  verified only that it holds with the stated scaling.
