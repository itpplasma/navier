# Review of HF19-B: second-order behaviour of the transport term on the nonlinear-Hodge class

Independent proof audit, 2026-09-06. Tier: full reconstruction from the first nontrivial
implication; lens: degenerate weighted elliptic theory and de Rham topology of the speed
support, plus an independent re-derivation of the first-order coefficient by a second
derivative-free form of `K` and a cross-check against the HF20 candidate.

**Frozen candidate.** `research/evidence/hf19-second-order-falsifier.md`,
sha256 `6114fd73322cfc6789c9c46a54810bf5ff39c1eedcdbdd39f53e97757f06c408`.
Research repository `1014e7e3c33af4a341a5f46156a22b808170257b`; manuscript
`../navier-paper/main.tex` at `39ccb664bf055fac94b3cfac97bf00a60191373d`. Comparison note
`research/evidence/hf20-harmonic-strain-test.md` at the same research revision. Nothing
outside this file was edited.

---

## VERDICT

**REPAIR.** Two load-bearing gaps, both in the identification of the weak limit of the
difference quotients (Step 3 and Step 4 of §1), plus five presentational slips. Both gaps
admit exact replacements, displayed in full below; the replacements are *stronger* than what
the note claims, so every downstream statement (Lemma 1(c), Lemma 1.4, Theorem 2, (2.4)–(2.6),
(3.3), §5.1–§5.4, and the frontier record) survives, and two of them are upgraded from
conditional to unconditional. No claim of the note is refuted, and the note's own scope
discipline (numerics as bounded evidence, first gap untouched) is accurate.

## REVIEWED SCOPE

Reconstructed and checked in full: §0 (characterisation of `M`, oddness, scalings); §1
Steps 1–4, Lemma 1(a)(b)(c), Remarks 1.2–1.3, Lemma 1.4, (1.8); §2 (2.1)–(2.6), Theorem 2
(i)(ii)(iii), Remarks 2.1–2.2; §3 (3.1)–(3.3); §4 mechanism paragraph and the thin-ring ODE
column (recomputed independently); §5.1–§5.4; §6.

Imported without re-proof, as directed: HF18-A/B and their reviews, and the manuscript labels
of `sec:quotient`. Two imports were nevertheless spot-verified because they are load-bearing:
`lem:cubic-pointwise` (manuscript line 4988: `|j(a)-j(b)| <= (|a|+|b|)|a-b|` and the exact
monotonicity identity) and the three inequalities of (0.2). A 4x10^5-sample search over
`R^3 x R^3` gives the sharp ratios `min = 0.888889` (constant `8/9`, sharp), `max = 2` for the
second (constant `8` valid, not sharp) and `max = 1` for the third (constant `2*sqrt(2)` valid,
not sharp). All three hold. Continuity of `t -> D_Q(u(t))` used in (1.8) is exactly
`lem:quotient-heatsign` (manuscript line 6229); the regularity used in Lemma 1.4 is exactly
package (R1) (manuscript line 3882), which gives `u in C^j([0,T];H^k)` for all `j,k` from
Schwartz data, so `u in C^2` is available.

## FIRST BAD BRIDGE

**§1 Step 3, the sentence "This holds if `Omega'` is simply connected, and it holds in the
axisymmetric class ... which is the gradient of a single-valued axisymmetric function (the
harmonic 1-form `d(theta)` has an `e_theta` component)."**

The verification of (H_Omega) in the axisymmetric class is incomplete, and it fails on members
of the very class the note computes in §4. The argument excludes only the generator `d(theta)`
of `H^1_dR`. If the speed vanishes at an interior point of the meridional cross-section — which
is the case for every "shell" profile of §4, `R = rho^c (1-rho^2)^2` with `c = 2,4,8`, and for
any `u_0 in M` whose speed has an interior zero curve — then `Omega'` is a solid torus with its
core circle removed, `H^1_dR(Omega') = R^2`, and the second generator is the *meridional*
harmonic form `d(vartheta) = e_vartheta / varrho`. That form is axisymmetric, meridional,
curl-free and not the gradient of any single-valued function, so the quoted reason does not
exclude it; and it is admissible, since for `R = varrho^2(1-varrho^2)^2` one has
`int rho |d(vartheta)|^2 dx ~ int varrho^4 (1-varrho^2)^4 varrho^{-1} d(varrho) < infinity`,
i.e. it lies in `L^2(rho)`. Hence the weak limit of `q_eps/eps` is not shown to be a gradient,
Lemma 1(b) does not follow along the full family, and the whole of Theorem 2 for those profiles
rests on an unverified hypothesis. The note's own NON-CLAIMS record the general case as open
("no treatment of non-simply-connected supports without symmetry (harmonic component)"), but
§4 then evaluates profiles that fall into exactly that case.

**Second bad bridge (§1 Step 4).** In the uniqueness proof the estimate
`int_{delta^2 < d < delta} d^{-1} dx <= C log(1/delta)` is asserted "by coarea over the
Lipschitz level sets of `d` on a bounded region". Coarea alone does not give it. With
`m(t) = |{x in Omega' : d(x) < t}|`, integration by parts gives
`int_{delta^2<d<delta} d^{-1} dx = [t^{-1}m(t)]_{delta^2}^{delta} + int_{delta^2}^{delta} t^{-2} m(t) dt`,
which is only `O(delta^{-2})` from `m <= |Omega'|`; the stated `O(log(1/delta))` needs the
unstated upper Minkowski bound `m(t) <= C t`. For `u_0 in M cap H^m` the set `{u_0 = 0}` may have
positive measure and `partial(Omega')` need not have finite content, so the hypothesis of
Lemma 1 ("every `u_0 in M cap H^m`, `m >= 4`") is strictly wider than the proof. The
parenthetical for unbounded `Omega'` is also wrong as written: the quoted quantity
`N^2 R^{-2} int_{R<|x|<2R} rho` is `O(N^2)` and does not tend to zero, because
`int_{R<|x|<2R} rho <= ||rho||_3 |ann|^{2/3} = C R^2`.

Both are gaps in stated proofs, not false conclusions: the replacements below establish more
than the note asserts, with no hypothesis on the geometry of the support.

## EVIDENCE

Positively verified, by independent recomputation:

1. **`M = {u : u . grad|u| = 0}` (0.4), `K = P_3 = 0` on `M`, oddness (0.5).** Recomputed.
   `K(-u) = -K(u)` follows from `q(-u) = -q(u)` and the sign of the two `u` factors in
   `K = - int A . ((u.grad)u)`. The homogeneity used in §5.1, `Q ~ a^3`, `D_Q ~ a^3`, `K ~ a^4`,
   is correct.
2. **Step 1 (weighted a-priori bound).** The Euler–Lagrange cancellation
   `<A_eps - A_0, w_eps - u_0> = eps <A_eps - A_0, h>` is exact, and — this matters for Lemma 1.4
   — it holds at *any* base point, not only on `M`, since `A(v)` and `A(v+z)` both annihilate
   `G_3` and `q(v+z) - q(v) in G_3`. The constant `C_1 = (9/4) sqrt(2) (2||u_0||_3 + eps||h||_3)^{1/2} ||h||_3`
   is exactly `(9/8) * 2 sqrt(2) * (...)`, and `||w_eps||_3 <= ||u_0||_3 + eps||h||_3` because `w`
   minimises the `L^3` norm. (1.3) and its three consequences are correct.
3. **Step 2.** `D(Atilde)(z) = |z| I + zhat (x) z = rho (I + uhat (x) uhat)` with eigenvalues
   `rho, rho, 2rho`, so (1.1) is right; `D(Atilde)` is positively 1-homogeneous and smooth off the
   origin, hence globally Lipschitz, hence the quadratic Taylor remainder; the test identity uses
   only `grad(eta) in G_3` and the two Euler–Lagrange conditions.
4. **Lemma 1(c).** Every remainder is `o(eps)`: the two `<w_eps - u_0, G_eps - g>` pieces are
   `O(eps^2)` (the second by
   `int |delta| rho^2 <= ||delta||_{L^2(rho)} ||rho||_3^{3/2}`), and `eps <h, G_eps - g>` is
   `O(eps^2)` (`||A_eps - A_0||_{3/2} = O(eps)` follows from (1.3) by Hölder with exponents `4/3, 4`,
   which is better than the `O(eps^{1/2})` the stability lemma alone gives). The single limit
   taken is `<omega_eps, (u_0.grad)u_0>_rho -> <omega, (u_0.grad)u_0>_rho` against the *fixed*
   element `(u_0.grad)u_0 in L^2(rho)` (`int rho |(u_0.grad)u_0|^2 <= ||rho||_3 ||(u_0.grad)u_0||_3^2`).
   Weak convergence of the difference quotients is therefore exactly enough, and no
   differentiability of `u -> q(u)` is used or needed. The note's Remark 1.2 is accurate.
5. **Independent re-derivation of (1.6).** Expanding the *other* derivative-free form
   `K = - <A, (u.grad)u>` for solenoidal `h` gives
   `DK[h] = -<A_0, N_1> - lim eps^{-1} <A_eps - A_0, N_0>` with `N_1 = (h.grad)u_0 + (u_0.grad)h`.
   Here `<A_0, (h.grad)u_0> = int h . grad(rho^3/3) = 0` (needs `div h = 0`);
   `<A_0, (u_0.grad)h> = - <h, g>` (needs `u_0 . grad rho = 0`, i.e. `u_0 in M`, and `div u_0 = 0`);
   and `eps^{-1}<A_eps - A_0, N_0> -> <(I + uhat (x) uhat)(h + grad(phi_1)), N_0>_rho = <h + grad(phi_1), g>`,
   because `uhat . N_0 = rho^{-1} u_0 . grad(rho^2/2) = 0` on `M` kills the rank-one part. The two
   `<h,g>` cancel and `DK[h] = -<grad(phi_1), g>`, which is (1.6). This is a genuinely independent
   route to the same coefficient. Note that it needs `div h = 0`, which Lemma 1 does not assume;
   for non-solenoidal `h` the three forms of (0.1) differ (their first-order parts differ by
   `int (rho^3/3) div h`), so (1.6) is an expansion of the form `K = -<q,(A.grad)u>` and coincides
   with the transport term only on solenoidal directions. Every application uses solenoidal `h`.
6. **Lemma 1.4 (this *is* the actual Navier–Stokes flow).** The transfer
   `K(u(t)) = K(u_0 + t u_1) + O(t^{3/2})` is correct: first term `O(||r||_3) = O(t^2)` by
   Cauchy–Schwarz against `int |w_u|^3` and Step 1 at base point `ubar`; third term
   `||q(ubar)||_3 ||G_u - G_ubar||_{3/2} = O(t^{1/2}) O(t)`. So `dK/dt(0)` is the honest one-sided
   derivative of `t -> K(u(t))` along the classical trajectory, in the single direction
   `u_1 = u_t(0)`. This answers the question put to this audit: **Lemma 1 is a Gateaux derivative
   in data space, and Lemma 1.4 converts it to the actual flow at the cost of `O(t^{3/2})`; the
   note does not confuse the two.**
7. **Theorem 2(i) (the viscous direction drops out).** For `h = nu Delta u_0` (azimuthal),
   `M h = 2 rho h_theta e_theta` and `int M h . grad(eta) = int 2 rho h_theta r^{-1} partial_theta(eta) = 0`
   for every `eta`, since the coefficient is `theta`-independent. So `grad(phi_1) = 0` by
   uniqueness and `DK[nu Delta u_0] = 0`. The `nu`-independence of `dK/dt(0)` is real.
8. **Theorem 2(ii),(iii) and (2.6).** With `a = Pi_rho f`, `b = Pi f = grad(p_0)`, `q_1 = b - a`,
   the weighted stationarity `<f - a, grad(eta)>_rho = 0` gives `dK/dt(0) = <b-a,a>_rho`,
   `P_3'(0) = -<m, grad(p_0)>_rho = <b, b-a>_rho`, difference exactly `-||q_1||_rho^2`, and the lower
   bound `>= -<m,f>_rho` from `||a||_rho <= ||f||_rho`. All correct as Hilbert-space algebra.
9. **Far field.** `p_0 = O(|x|^{-3})`, `m = O(|x|^{-4})` is right: the monopole
   `int div f = 0` and the dipole moments `int y_i div f = - int f_i` vanish, the last by
   `int e_r d(theta) = 0`. So `m in L^3` and the cut-off family `h_R -> m` in `L^3` of §5.1 is
   legitimate (`|A| ~ |x|^{-3}`, `||grad(chi_R) x A||_3^3 = O(R^{-9})`).
10. **The depolarisation factor `1/2` and the constant-speed closed form (3.3).** Verified twice,
    independently of the note.
    (a) `P(varrho) = varrho^{-1} int_0^varrho t R^2 dt` does solve `P'' + P'/varrho - P/varrho^2 = (R^2)'`
    (substitute `J' = varrho R^2`), and the weak form
    `int [ R^3 (varrho H)' + R (varrho Psi' H' + Psi H / varrho) ] d(varrho) = 0` reproduces (3.1)
    together with the natural condition `R(1)^3 + R(1) Psi'(1) = 0`. For `R = 1` this gives
    `P = varrho/2` (interior field `= f/2`, the 2D transverse depolarisation factor `1/2` — the
    circular-cylinder value, not the spherical `1/3`) and `Psi = -varrho`, hence `q_1 = -f/2` and
    `I[1] = pi int_0^1 (varrho G)' d(varrho) = -pi/2`, i.e. `dK/dt(0) = -pi^2 a^2 S_0^5 / r_0`.
    (b) The same three numbers follow from the note's own exterior identity: for `rho = rho_0`
    constant on its support, `int_{R^3} m . grad(p_0) = 0` and `m = -grad(p_0)` outside give
    `<m,grad(p_0)>_rho = rho_0 int_{ext} |grad(p_0)|^2`. For the unit disk cross-section
    `p_0^{ext} = cos(vartheta)/(2 varrho)` and `int_{ext}|grad(p_0)|^2 dA = pi/4`, so
    `P_3'(0) = -2 pi (pi/4) = -pi^2/2`, and `||q_1||_rho^2 = pi^2/2`, `dK/dt(0) = -pi^2`, exactly
    (3.3) and exactly the lower bound of (2.6). The two routes agree; the constant-speed identity
    and the factor `1/2` are correct.
11. **Independent recomputation of the thin-ring ODE column.** A linear finite-element solve of
    the weak form above (4000 elements, 8-point Gauss, natural condition at `varrho = 1`,
    `Psi(0) = 0`), with `P` by cumulative quadrature and
    `I = pi int R^3 (varrho(P+Psi))'`, `J = pi int R (G'^2 + G^2/varrho^2) varrho`, reproduces the
    note to four digits where the profile is normalised to unit maximum:
    `R = 1: -1.5708` (note `-1.5705`, exact `-pi/2`); `(1-varrho^2)^4: -0.052613` (note `-0.05259`);
    `(1-varrho^2)^2: -0.104769` (note `-0.1047`); `1-varrho^2: -0.205480` (note `-0.2054`);
    `sqrt(1-varrho^2): -0.383519` (note `-0.3835`); `(1-varrho^2)^8: -0.026329` (note `-0.0263`);
    `(1-varrho^2)^20: -0.010534` (note `-0.0105`). The discrete weighted identity
    `<grad(psi),f>_rho = -||grad(psi)||_rho^2` holds to roundoff. `P_3'(0) = I + J` is negative in
    every case, with `P_3'/I` in `0.50–0.55` (the note's "0.4–0.8" is consistent).
12. **Refutation attempt inside the reduction (failed).** `I[R]` is homogeneous of degree 5 in
    `R`, so its sign is normalisation-free. Maximising `I[R]` over `R = z^2 >= 0` on a 401-node
    grid (L-BFGS-B, six starts: smooth, single Gaussian ring, double ring, three random) never
    produced a positive value; the optimiser drives `I` to `0^-` by degenerating the profile
    (best `-2.3 x 10^-6`). No counterexample to the nominated `P_3'(0) <= 0` was found in the
    thin-ring class. This is bounded evidence, not proof, exactly as the note says.

Defects found, in reading order:

- **(D1) Step 3, (H_Omega) in the axisymmetric class** — the first bad bridge above.
- **(D2) Step 4, the logarithmic cutoff** — the second bad bridge above, plus the incorrect
  unbounded-`Omega'` parenthetical.
- **(D3) §0, scalings.** `nu D_3 (nu D_3 / Q) ~ (a^4 nu^2, lambda^4)` should be `(a^3 nu^2, lambda^4)`:
  `nu^2 D_3^2 / Q = nu^2 a^6 lambda^4 / a^3`. The conclusion drawn from it,
  `(dK/dt)/(nu^2 D_3^2/Q) ~ a^2/nu^2 = Q^{2/3}/nu^2 ~ Re^2`, is correct with the corrected exponent.
- **(D4) Lemma 1.4, "Lemma 1(c) with `h = u_1 in H^m`".** `u_1 = nu Delta u_0 + m in H^{m-2}`, and
  Lemma 1 needs `grad(h) in L^infinity`, i.e. `m >= 5` (or `u_0` Schwartz). The lemma's own
  hypothesis is `u_0 in M cap S`, so the application is fine; the citation is not.
- **(D5) Theorem 2(iii), the derivation of `P_3'(0)`.** `P_3'(0) = int p_0 [u_1 . grad(rho) + u_0 . grad(uhat_0 . u_1)]`
  differentiates `|u|` pointwise, and `{u_0 = 0}` has non-empty interior here, where
  `partial_t |u| = uhat . u_t` is meaningless. The stated value is nonetheless right; see the
  replacement in R3 below.
- **(D6) §4, the shell entries of the thin-ring list.** The note reports
  `varrho^{2,4,8}(1-varrho^2)^2: -0.0273, -0.0045, -0.0042`. My solver gives raw
  `-2.66e-5, -3.22e-7, -1.30e-9`; unit-maximum normalisation gives `-0.373, -0.337, -0.256`;
  fixed-`Q` normalisation gives `-1.99, -2.03, -2.29`. No convention I could infer reproduces the
  three numbers, although every other entry in the same list reproduces to four digits under
  unit-maximum normalisation. Signs agree, so no conclusion moves; the numbers are not
  reproducible as published and should carry their normalisation.
- **(D7) §5.1, "rigorous family".** The positivity of `K(u_0 - eps h_R)` rests on
  `DK(u_0)[m] != 0`, which in the note is established only numerically (the one closed-form case,
  the constant-speed tube, is explicitly outside Lemma 1's hypotheses). As written, §5.1 provides
  no unconditional field with `K != 0`, so the "rigorous" tag over-reaches. R4 below repairs this
  unconditionally, from the note's own Lemma 1.
- **(D8) Headline vs §5.1/§6.** The header ("the intended refutation did NOT occur") and PLAN.md's
  one-line record ("FALSIFY, target survived") understate the note: by (0.5) plus any datum with
  `K != 0`, the stated target — a monotone/Lyapunov mechanism for `Q` — *is* refuted, as §6 itself
  says. What survived is only the sharper sub-question, whether the second-order dynamics
  *through* `M` produce the failure.

## REPLACEMENT ARGUMENT

### R1 (replaces (H_Omega); it is not a hypothesis, it is a theorem)

**Lemma R1.** Let `Omega' subset R^3` be open, `eps_j -> 0`, `q_j in G_3`, and suppose
`q_j / eps_j -> v` weakly in `L^2_loc(Omega')`. Then `v = grad(phi)` for some
`phi in W^{1,2}_loc(Omega')`. No connectivity, symmetry or regularity hypothesis on `Omega'` is
used.

*Proof.* (i) Each `q_j` is an `L^3` limit of gradients of `C_c^infinity` functions, hence
`curl q_j = 0` in `D'(R^3)`, hence `curl v = 0` in `D'(Omega')`.
(ii) Let `J in C_c^infinity(Omega';R^3)` with `div J = 0`. For `phi in C_c^infinity(R^3)`,
`int grad(phi) . J = - int phi div J = 0`; since `J in L^{3/2}` this passes to the `L^3` limit, so
`int q_j . J = 0` for every `j`. As `supp J` is a compact subset of `Omega'`, `J in L^2(supp J)`
and weak `L^2_loc` convergence gives
```
   int_{Omega'} v . J = lim_j eps_j^{-1} int q_j . J = 0
   for every solenoidal J in C_c^infinity(Omega';R^3).                                (R1.1)
```
(iii) Fix a connected open `omega` with compact closure in `Omega'`, and let
`v_delta = v * eta_delta` for `delta < dist(omega, partial(Omega'))`. Then `v_delta` is smooth and
curl-free on `omega`, and for solenoidal `J in C_c^infinity(omega)` the field
`J * eta_delta^{reflected}` is again solenoidal, smooth and compactly supported in `Omega'`, so
`int v_delta . J = 0` by (R1.1). In the language of forms, `v_delta` is a smooth closed 1-form on
`omega` annihilating every compactly supported closed 2-form; by the de Rham isomorphism
`H^1_dR(omega) = (H^2_c(omega))^*` (compactly supported solenoidal vector fields are exactly the
compactly supported closed 2-forms), `[v_delta] = 0`, i.e. `v_delta = grad(phi_delta)` on `omega`.
Normalising `phi_delta` to have zero mean on a fixed ball and using `v_delta -> v` in `L^2(omega)`
together with the Poincaré inequality, `phi_delta -> phi` in `L^2(omega)` with `grad(phi) = v`.
Exhausting `Omega'` by such `omega` and matching on overlaps (the potentials differ by constants
on connected overlaps) gives `phi in W^{1,2}_loc(Omega')`. `[]`

**Consequence.** (H_Omega) is deleted from Lemma 1, Theorem 2 and the frontier record. Lemma 1
holds for every `u_0 in M cap H^m` and every open `Omega'` — including the shell profiles of §4,
whose harmonic mode `d(vartheta)` R1 excludes by the vanishing of its periods rather than by
symmetry. The note's NON-CLAIM "no treatment of non-simply-connected supports without symmetry
(harmonic component)" is void: that case is now covered. This is a strengthening, not a
weakening: the first bad bridge is repaired by removing the hypothesis it tried to verify.

### R2 (replaces Step 4)

**Lemma R2.** Let `u_0 in M cap H^m`, `m >= 4`, `rho = |u_0|`, `Omega' = {rho > 0}`,
`M = rho (I + uhat_0 (x) uhat_0)`. Assume
```
   (W)   for every R > 0 :  int_{{delta^2 < rho < delta} cap B_R} |grad(rho)|^2 / rho  dx
                            = o( log^2(1/delta) )   as delta -> 0.                    (R2.1)
```
Let `phi in L^2_loc(Omega')` with `grad(phi) in L^2(rho)` and
`int_{Omega'} M grad(phi) . grad(eta) = 0` for all `eta in C_c^infinity(Omega')`. Then
`grad(phi) = 0`.

*Proof.* Put
`zeta_delta = min{ 1, (log(rho/delta^2))_+ / log(1/delta) }` — built from `rho`, not from the
distance to `partial(Omega')`. Then `zeta_delta = 0` on `{rho <= delta^2}`, `= 1` on
`{rho >= delta}`, it is Lipschitz on `Omega'`, and on the shell
`|grad(zeta_delta)| = |grad(rho)| / (rho log(1/delta))`, so
```
   int rho |grad(zeta_delta)|^2 = log(1/delta)^{-2} int_{shell} |grad(rho)|^2 / rho .   (R2.2)
```
Let `chi_R = 1` on `B_R`, `0` off `B_{2R}`, `|grad(chi_R)| <= 2/R`, and `phi_N = max(-N,min(phi,N))`.
The function `eta = zeta_delta chi_R phi_N` is Lipschitz with support in the compact set
`{rho >= delta^2} cap closure(B_{2R}) subset Omega'`, hence admissible by mollification. Expanding
`grad(eta)`,
```
   int chi_R zeta_delta M grad(phi_N) . grad(phi_N)
     = - int phi_N chi_R M grad(phi) . grad(zeta_delta)
       - int phi_N zeta_delta M grad(phi) . grad(chi_R) .
```
The left side is nonnegative and increases to `int chi_R M grad(phi_N).grad(phi_N)` as
`delta -> 0` (dominated convergence, dominant `2 rho |grad(phi)|^2 in L^1`). By `M <= 2 rho`,
`|phi_N| <= N`, Cauchy–Schwarz and (R2.2), the first right-hand term is at most
`2 N ( int_{{rho<delta}} rho|grad(phi)|^2 )^{1/2} ( o(log^2(1/delta)) )^{1/2} / log(1/delta) -> 0`
as `delta -> 0` at fixed `R`, the first factor tending to `0` by dominated convergence. The second
right-hand term is at most
```
   (4N/R) ( int_{|x|>R} rho|grad(phi)|^2 )^{1/2} ( int_{B_{2R}} rho )^{1/2}
   <= (4N/R) o_R(1) ( ||rho||_3 (C R^3)^{2/3} )^{1/2} = C N o_R(1) ,
```
uniformly in `delta` — this is the corrected form of the note's parenthetical: the factor that
vanishes is the tail `int_{|x|>R} rho |grad(phi)|^2`, not `R^{-2} int rho`, which is merely
bounded. Letting `delta -> 0` at fixed `R` and then `R -> infinity` gives
`int M grad(phi_N).grad(phi_N) = 0`, so `grad(phi_N) = 0` for every `N`, so `grad(phi) = 0`. `[]`

**Verification of (W) where the note uses it.** (W) is implied by the note's implicit content
bound `|{0 < rho < t} cap B_R| <= C_R t` (then the shell integral is `O(log(1/delta))`), and it
holds directly whenever `rho` vanishes to finite order `k >= 1` on a rectifiable set
(`|grad(rho)|^2/rho ~ d^{k-2}`, locally integrable for `k >= 1`) and whenever it vanishes to
infinite order (`rho ~ exp(-c/d)` gives `|grad(rho)|^2/rho ~ rho/d^4 -> 0`, bounded). Every profile
of §§2–4 — `B(x) = (1-x^2)^4_+`, the exponential bumps, the shells, and the
`b(t) = exp(-1/(1-t^2))` swirl of the HF20 comparison — satisfies (W). The correct scope line for
Lemma 1 is therefore "`u_0 in M cap H^m` satisfying (W)", not "`u_0 in M cap H^m`".

### R3 (replaces the derivation of (2.5))

Do not differentiate `|u|`. Since `div(|u|u) = u . grad|u|` for solenoidal `u in W^{1,infinity}`,
```
   P_3(t) = int p (u . grad|u|) = int p div(j(u)) = - int j(u) . grad(p) ,   j(z) = |z|z .
```
`t -> u(t)` is `C^1` into `L^3` and `t -> grad(p)(t)` is `C^1` into `L^3` by (R1); `j` is `C^1` from
`L^3` to `L^{3/2}` with `Dj(u_0) = M`. Hence `P_3` is `C^1` near `0` and
```
   P_3'(0) = - int M u_1 . grad(p_0) - int j(u_0) . grad(pdot_0) = - <(I + uhat_0 (x) uhat_0) u_1, grad(p_0)>_rho ,
```
the second term vanishing because `u_0 in M` means `j(u_0)` annihilates `G_3` and
`grad(pdot_0) in G_3`. For the swirl, `uhat_0 = +-e_theta` is orthogonal to the meridional
`grad(p_0)`, so the rank-one part drops and the azimuthal `nu Delta u_0` drops with it; with
`u_1 = nu Delta u_0 + m`,
```
   P_3'(0) = - <m, grad(p_0)>_rho = int p_0 m . grad(rho) ,
```
which is (2.5), `nu`-independent, with no pointwise differentiation of `|u|` anywhere.

### R4 (upgrades §5.1 from numerics-dependent to unconditional, using the note's own Lemma 1)

**Proposition R4.** There exist `U, h in C_c^infinity(R^3;R^3)` with `div U = div h = 0`,
`U in M`, `U != 0`, such that
```
   K(U + eps h) = - eps ||U||_3^3 + o(eps) ,       eps -> 0 .                          (R4.1)
```
In particular `K(U - eps h) > 0` for all small `eps > 0`, so smooth compactly supported solenoidal
fields with `K != 0` exist, and §5.1 holds with no numerical input.

*Proof.* Take the pair of the HF20 candidate (§3 there), which is explicit: with
`b(t) = exp(-1/(1-t^2))`, `s(r,z) = b(4r-6) b(2z)`, `U = s e_theta` (support in
`5/4 <= r <= 7/4`, `|z| <= 1/2`, so `U` is smooth and compactly supported away from the axis and
`U in M` by (0.4)); with `chi = 1` on `B_3`, `chi = 0` off `B_4`, `a = (yz, -xz, 0)`,
`Phi = (x^2+y^2)/2 - z^2`, put `h = curl(chi a)`. Then `h` is smooth, compactly supported and
solenoidal, and on a neighbourhood of `supp U` one has `h = grad(Phi) = (x,y,-2z)`.
`U` satisfies (W) (infinite-order vanishing), so Lemma 1 applies with R1 and R2 in place of
Step 3–Step 4. Since `h = grad(Phi)` on `Omega' = {U != 0}` with `Phi` smooth and bounded there,
`grad(phi_1) := -h|_{Omega'}` lies in `L^2(rho)`, has a potential in `L^2_loc(Omega')`, and solves
`div(M(h + grad(phi_1))) = div(0) = 0`; by R2 it is *the* solution. Hence, by (1.6),
```
   DK(U)[h] = - <grad(phi_1), g> = <h, g> = int rho h . ((U.grad)U)
            = int rho (x,y,-2z) . ( - rho^2 r^{-1} e_r ) = - int rho^3 r^{-1} r = - ||U||_3^3 ,
```
using `(x,y,-2z) . e_r = (x^2+y^2)/r = r` on `supp U`. Lemma 1(c) then gives (R4.1). `[]`

R4 has three uses. It removes (D7). It is an independent confirmation, by a completely different
mechanism, of the first-order coefficient the HF20 candidate obtains from a competitor-gradient
argument that never linearises: HF20's `<A_0, N_1> = ||U||_3^3` and HF19-B's
`DK(U)[h] = -||U||_3^3` are the same number, computed from the two different derivative-free forms
of `K`, with the minimiser handled in two different ways. And it shows the two notes are
consistent, not competing.

## HF19-B versus HF20: the data-space / flow distinction

The distinction the HF20 candidate draws in its §6 ("the field `h` is a direction in the space of
data, not the Navier–Stokes time derivative at `U`, so (1.1) is not a computation of
`dK(u(t))/dt` along the trajectory from `U`") is correct, and the two notes are **consistent**:

- HF19-B Lemma 1 is a data-space Gateaux derivative `DK(u_0)[.]`, a bounded linear functional on
  `L^3` directions. HF19-B Lemma 1.4 evaluates it at the one distinguished direction
  `u_1 = u_t(0)` and pays `O(t^{3/2})` for the transfer, so `dK/dt(0)` there *is* along the actual
  flow. HF20 never evaluates the flow direction; it evaluates `DK(U)[.]` at a harmonic-gradient
  direction and then amplifies and rescales the *perturbed* datum before invoking the flow.
- Evaluating HF19-B's functional at HF20's direction reproduces HF20's coefficient exactly (R4).
  Evaluating it at the flow direction gives Theorem 2's `<(Pi - Pi_rho)f, f>_rho`, which is
  negative on every profile tested. There is no contradiction: `DK(u_0)[.]` is a linear functional
  that is negative on `m` and on `h`, and positive on `-m` and `-h`.
- Consequently HF19-B §5.1 and HF20 Theorem 1.2 are the same obstruction at two strengths.
  HF19-B has the mechanism (oddness plus any `K != 0`) but supplies the required `K != 0` only
  numerically; HF20 supplies an analytic certificate and additionally fixes the `L^2` norm by the
  scaling `b T_lambda`. R4 shows the certificate is also derivable from HF19-B's own Lemma 1,
  which is a useful independent check on the HF20 audit now in progress: an HF20 audit that
  refutes the *coefficient* `||U||_3^3` would also refute R4, and hence Lemma 1.

## CONDITIONAL SUFFIX THAT SURVIVES

With R1 and R2 substituted for Steps 3–4, and R3 for the derivation of (2.5), the following are
unconditional:

- Lemma 1(a)(b)(c) for every `u_0 in M cap H^m`, `m >= 4`, satisfying (W), every open `Omega'`
  (no simple connectivity, no symmetry), and every `h in H^m`; the transport functional being the
  form `K = -<q,(A.grad)u>`, which coincides with the transport term for solenoidal `h`.
- Lemma 1.4 and (1.8) for classical trajectories from Schwartz data in `M` (with `m >= 5` or
  Schwartz in Lemma 1's citation, per D4).
- Theorem 2 (i)(ii)(iii), (2.4), (2.5), (2.6) and Remark 2.1 for smooth compactly supported or
  Schwartz swirl fields; in particular the exact link `dK/dt(0) = P_3'(0) - ||q_1||_rho^2` and the
  two-sided bound, and the `nu`-independence of both `dK/dt(0)` and `P_3'(0)`.
- (0.4), (0.5), (3.3) as the closed-form solution of the limiting weighted problem for the
  constant-speed tube (still outside Lemma 1's hypotheses, correctly flagged by the note), the
  exterior identity `<m,grad(p_0)>_rho = rho_0 int_{ext}|grad(p_0)|^2 > 0` for constant speed, and
  §5.1 including the explicit family — now unconditional by R4.
- §5.4: the first gap is untouched. Confirmed. Nothing in the note bounds `int_0^tau K dt`, and
  the note's own statement of why (an instantaneous local sign is not a time-integrated bound, and
  `K > 0` on one side by (5.1)) is exactly right.

Conditional on numerics only, and correctly labelled as such by the note: the *sign*
`dK/dt(0) < 0` for the tested profiles, the nominated `P_3'(0) <= 0` on the swirl class, and every
number in §4. My independent solver reproduces the sign on the whole thin-ring column and finds no
positive `I[R]` under direct maximisation, which strengthens the nomination without proving it.

## UNNECESSARY DEPENDENCIES

- **(H_Omega) in full.** Deleted by R1; with it go the simple-connectivity restriction, the
  axisymmetry-based verification, and the "harmonic component" NON-CLAIM.
- **The distance function `d` and `rho <= Lip(u_0) d`.** R2 uses the weight itself; the
  Lipschitz-distance bound and the coarea argument over level sets of `d` are not needed, and
  the geometry of `partial(Omega')` never enters.
- **The numerics, for the qualitative conclusions of §5.1 and §6.** R4 makes the existence of
  Clay data with `K > 0` unconditional. Numerics remain necessary only for the *sign of
  `dK/dt(0)` on the flow direction*, i.e. for the lane's actual FALSIFY outcome, and for `P_3'(0) <= 0`.
- **Kato's uniform-in-`nu` local theory [MO]**, already flagged by the note as entering only the
  non-load-bearing remark in §5.2. Confirmed non-load-bearing.
- **`m >= 4`** is not enough for Lemma 1.4's citation of Lemma 1 (D4); `m >= 5`, or the Schwartz
  hypothesis actually assumed, is.

## NON-CLAIMS OF THIS REVIEW

This review does not audit HF20 (that audit is a separate action; R4 uses only HF20's explicitly
displayed fields `U` and `h`, verifying their stated properties directly, and none of its
estimates). It does not prove `P_3'(0) <= 0` on the swirl class and does not refute it; the
maximisation in item 12 is bounded evidence at finite resolution in the thin-ring reduction only.
It does not verify the 2D, 3D or box-convergence numerics of §4 beyond the ODE column and the
closed form. It supplies no bound, sign, or absorption for `K` away from `M`, no statement about
`Q''(0)`, no differentiability of `u -> q(u)`, no HIGH-STRAIN or HIGH-PRESSURE input, and no
progress on the first gap. NS-R3 remains OPEN. It makes no novelty claim for R1 (the vanishing of
periods under weak limits of exact forms is standard de Rham duality) or for R2 (a standard
degenerate-weight `H = W` argument with an explicit sufficient condition).

## INTEGRATION ACTIONS (for the controller, if this verdict stands)

1. Record HF19-B as **REPAIR**, not as an unaudited lead, once R1–R4 are applied to the note by
   its owner; the note itself must not be edited by this audit.
2. Apply R1 (delete (H_Omega) throughout, including from Lemma 1, Theorem 2(i), CLAIM AND SCOPE,
   EVIDENCE and NON-CLAIMS), R2 (replace Step 4 and add hypothesis (W) to Lemma 1's scope line),
   R3 (replace the derivation of (2.5)), R4 (replace §5.1's conditional family), and fix D3–D6, D8.
3. Correct the PLAN.md HF19 bullet: HF19-B does **not** leave the Lyapunov target standing. It
   refutes it (oddness plus any `K != 0`, now unconditional by R4) and reports the sharper
   sub-question — whether the second-order dynamics through `M` produce the failure — answered
   negatively on the tested swirl class. Record the excluded class accordingly.
4. Record in the HF20 audit dossier that HF19-B's Lemma 1, once repaired, independently reproduces
   HF20's first-order coefficient `-||U||_3^3` by a different route, and that the two notes are
   consistent on the data-space / flow distinction. This is a cross-check available to that audit,
   not a substitute for it.
5. Leave the graph unchanged: no node is promoted, `hyp:highstrain` and `hyp:highpressure` are
   untouched, and the first gap is unchanged.
6. Carry the open sub-question forward as stated by the note: prove or refute
   `int rho |grad(p_0)|^2 <= int rho^3 partial_r(p_0)/r` with `Laplacian(p_0) = r^{-1} partial_r(rho^2)`.
   Note additionally that with `a = Pi_rho f`, `b = Pi f` this is `<b,b-a>_rho <= 0`, and that
   `dK/dt(0) = -<m,f>_rho + min_{grad} ||f - grad||_rho^2`, which makes the lower bound of (2.6)
   the statement `min >= 0` and the upper bound the choice `grad = grad(p_0)`.

## REOPENING CONDITION

This verdict is reopened if any of the following is exhibited:

1. A `u_0 in M cap H^m` with `Omega' = {u_0 != 0}` for which (W) of R2 fails and for which the
   homogeneous weighted problem `div(M grad(phi)) = 0`, `grad(phi) in L^2(rho)`, has a nonzero
   solution — a Lavrentiev gap for this weight. That would restrict Lemma 1 further than R2 does,
   though it would not affect any profile used in the note.
2. A solenoidal `h in H^m` and `u_0 in M` for which the two derivative-free forms of `K` in (0.1)
   are shown to have different first-order parts, which would break the cross-check in EVIDENCE 5
   and hence (1.6).
3. A thin-ring profile `R >= 0` with `I[R] > 0`, or a smooth swirl `u_0 in M` with
   `P_3'(0) = int p_0 m . grad|u_0| > 0`. This would not invalidate Lemma 1, Lemma 1.4 or
   Theorem 2 — the identity (2.6) is sign-free — but it would retire the note's nominated Goal B
   and change its NEXT DISTINCT ACTION.
4. An audit of HF20 that refutes its coefficient `<j(U), (U.grad)h> = ||U||_3^3` for the displayed
   `U, h`. Since R4 derives the same coefficient from HF19-B's Lemma 1, such a refutation would
   force a re-examination of Lemma 1 itself.
5. Any later use of `dK/dt(0) < 0` as an input to a bound on `int_0^tau K dt`. That step is not
   available at any scope and is the note's own §5.4.
