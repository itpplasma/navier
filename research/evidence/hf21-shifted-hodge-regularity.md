# HF21-A: regularity of the shifted 3-Laplace minimizer — the admissibility constraint, the scalar reduction, and the sharp integrability criterion

Lane HF21-A of the Track B frontier packet, **MODE: DISCOVER with a falsifier arm**, 2026-09-06.
This is the lane commissioned in wave HF19 whose absence was certified by
`hf19-review-shifted-hodge-regularity.md` (VERDICT INVALID, target absent at `5aefa82`).
It is delivered here against research HEAD `30d715d` and manuscript `sec:quotient`.

Inputs (all audited PASS, cited and **not** re-proved): `hf17-quotient-functional.md`,
`hf17-quotient-evolution.md`, `hf18-hodge-regularity.md` (+ `hf18-review-hodge-regularity.md`),
`hf18-divergence-speed-link.md` (+ its two reviews, final PASS), the manuscript
`/home/ert/proj/navier-paper/main.tex` §`sec:quotient`, and `PLAN.md`
("Frontier packet", "Beyond the checkpoint", "HF16–HF17", "HF18", "HF19", "HF20",
"Ordered next actions"). The three HF19 notes and `hf20-harmonic-strain-test.md` are
UNAUDITED and are **not used**, not even as motivation, anywhere below.
Source tags: **[DI]** directly inspected this session or in a named prior wave,
**[MO]** metadata only, never load-bearing.

Pre-registered checks C1–C7 of `hf19-review-shifted-hodge-regularity.md` §3 are answered
in §8 below, in order.

---

## Summary

**(H1) is not decided here, and no claim is made that it is.** What is proved is a
complete change of the shape of the question, in five theorems, each with every
hypothesis displayed.

1. **Admissibility (Theorem 1, Theorem 2).** For the datum `u` to be a classical
   `H^m` field, `m >= 4`, the *whole* skew part of the distributional gradient of the
   minimizer is already known and smooth: `curl w = curl u in H^{m-1} ⊂ C^{1,1/2}`.
   Hence (H1) is a statement about the *symmetric* part alone. Theorem 2 is a rigidity
   statement: if a solenoidal `A ∈ C^1` has a zero `x_0` with `DA(x_0) ≠ 0`, then
   `curl(|A|^{-1/2}A)` blows up like `dist^{-1/2}`, so the datum it produces is not
   in `H^s_loc` for any `s > 5/2`. **Every field in the HF18-B witness family, bulk and
   oscillation alike, is inadmissible in exactly this way** (computed, §2.3). The
   natural constructive route to a counterexample is therefore closed, not by taste but
   by an identity.
2. **Scalar reduction (Theorem 3).** For admissible `u` and every `1 < p < ∞`,
   `w ∈ W^{1,p}_loc ⟺ div w ∈ L^p_loc` (the *distributional* `div w`, no circularity).
   In particular (H1) follows from `div w ∈ L^p_loc` for a single `p > 1`. Corollary 3.3:
   the two HF18-B hypotheses (H1) and (H2) collapse to the single distributional
   statement `div w ∈ L^{3/2}(R^3)`.
3. **The standard obstacle is not the true one (Theorem 4, Proposition 4.4).** The
   condition `|w|^{-1} ∈ L^1_loc` — named as "the exact analytic obstacle" in
   `hf19-review-shifted-hodge-regularity.md` §3 — is sufficient but **strictly not
   necessary**. An explicit element of the minimizer class is exhibited on which
   `∫_B |w|^{-1} = ∞` while `w ∈ C^∞(B)` and `u ∈ C^∞(B)`, `curl u = e_3 ≠ 0`.
   The sharp criterion is the layered one of Theorem 4, which that example satisfies.
4. **Vorticity non-degeneracy (Theorem 5).** An unconditional lower bound obtained from
   Stokes' theorem alone: `⨍_{B_r(x_0)}|w| ≥ (r/32)·max_n inf_{B_r} (ω·n)`, `ω = curl u`.
   So `|w|` cannot vanish faster than first order at any point where the vorticity is
   nonzero. With Theorem 2 this is a **pincer**: at a nondegenerate model zero the order
   of vanishing of `|w|` is forced to be exactly `1`, and there (H1) is automatic.
5. **The positive route runs and then stops at a named place (Theorem 6, §6.2).** The
   localized difference-quotient argument does produce a genuine local Caccioppoli
   inequality for `V`. Gehring cannot be started from it: the right-hand side carries
   `|w|^{1/2}|q - c|`, and converting it to `∇V` needs a Sobolev–Poincaré inequality
   for `q`, i.e. needs (H1). That circularity is exhibited, not asserted.
6. **Literature placement, corrected and sharpened (§1).** Our `w` is exactly Stern's
   canonical `p`-coclosed primitive `β_∞` of Lemma 2.2 [DI], for which **no regularity is
   stated anywhere in that paper**; the regularity credited to Uhlenbeck (Prop. 3.1 [DI])
   is for the `p`-harmonic forms of Theorem 2.9, which are additionally **closed**.
   Uhlenbeck's own structure — `div(a(|∇U|)∇U) = f`, coefficient depending on the modulus
   of the gradient of the unknown, with no `x`-dependence — is not the structure of our
   operator, whose coefficient depends on `|u(x) + ∇φ|`.

Non-claims are in §9. The first gap is untouched (check C7).

---

## 0. Setting, audited inputs, conventions

Fix a time on a compact classical interval; the whole note is a statement about one
fixed time. Throughout,
```
u ∈ H^m(R^3; R^3),   m >= 4,   div u = 0.                                    (0.1)
```
`H^m ⊂ C^{m-2,1/2}` for `m >= 2` in `R^3`, so `u ∈ W^{2,∞}`, `∇u ∈ L^∞ ∩ L^2 ∩ L^3`.
`G_3`, `Q`, `w = u + q`, `A = |w|w`, `P` (Leray) are as in `def:quotient`,
`lem:quotient-minimizer`, `lem:leray` of `sec:quotient`. `V := |w|^{1/2}w`,
`Φ(V) = |V|^{1/3}V`, `Ψ(V) = |V|^{-1/3}V` (`Ψ(0) = 0`), so `A = Φ(V)`, `w = Ψ(V)`.
`D_3(w) := ∫(|∇V|^2 − (1/9)|∇|V||^2)`. `d(x,S)` is Euclidean distance;
`⨍_E f = |E|^{-1}∫_E f`. `sk(N) = (N − N^T)/2`.

**Audited and used without re-proof.**

- **(P1)** [`lem:quotient-minimizer`, DI] For `u ∈ L^3` the minimizer `q = q(u) ∈ G_3`
  exists, is unique, `A = |w|w ∈ L^{3/2}` with `‖A‖_{3/2} = ‖w‖_3^2`, and the
  Euler–Lagrange condition `∫ A·g = 0` holds for **every** `g ∈ G_3`; in particular
  `div A = 0` in `D'(R^3)`.
- **(P2)** [`lem:gradient-closure`, DI] If `ψ ∈ L^3(R^3)` has distributional gradient
  `∇ψ ∈ L^3(R^3)`, then `∇ψ ∈ G_3`.
- **(P3)** [`lem:leray`, DI] `P` is bounded on `L^p(R^3;R^3)` for `1 < p < ∞`,
  `P∇φ = 0` for `φ ∈ C_c^∞`, `Pu = u` for solenoidal `u ∈ L^3`; every `q ∈ G_3` is
  curl-free in `D'` (limits in `L^3` of `∇ψ`, `curl` continuous on `D'`).
- **(A1)–(A4)** [HF18-A, PASS] `V ∈ H^1(R^3)`, `‖V‖_2^2 = 3Q`,
  `‖∂_k V‖_2 ≤ (9/2)‖w‖_3^{1/2}‖∂_k u‖_3`; `A ∈ W^{1,3/2}(R^3)` with
  `∇A = DΦ(V)∇V` a.e. and `div A = 0` a.e.; `w ∈ L^3 ∩ L^9 ∩ B^{2/3}_{3,∞}`;
  `D_Q(u) = D_3(w) >= (8/9)‖∇V‖_2^2 >= c‖u‖_9^3`.
- **(A5)** [HF18-A Lemma V, (1.6)–(1.8), PASS] For all `z, z' ∈ R^3`, with
  `Ã(z) = |z|z`, `V(z) = |z|^{1/2}z`:
  `(8/9)|V(z) − V(z')|^2 ≤ (Ã(z) − Ã(z'))·(z − z') ≤ 4|V(z) − V(z')|^2` and
  `|Ã(z) − Ã(z')| ≤ 2√2 (|z| + |z'|)^{1/2}|V(z) − V(z')|`.
- **(A6)** [HF18-A Cor. 1(e), PASS] On `{V ≠ 0}`, `w = Ψ(V)` has the *approximate*
  gradient `∇w = DΨ(V)∇V`, `DΨ(V) = |V|^{-1/3}(I − (1/3)V̂⊗V̂)`, hence
  `|∇w| ≤ |w|^{-1/2}|∇V|` there. Equivalently
  `|∇V|^2 = |w||∇w|^2 + (5/4)|w||∇|w||^2` a.e. on `{V ≠ 0}`.
- **(B1)** [HF18-B Prop. 1.4, PASS] With `M := {w ∈ L^3 : div(|w|w) = 0 in D'}`,
  `M = { |A|^{-1/2}A : A ∈ L^{3/2}(R^3;R^3), div A = 0 in D' }`, and **every** `w ∈ M`
  is the minimizing representative of the solenoidal field `u = Pw`, with
  `q = (I − P)w ∈ G_3` and `Q(Pw) = (1/3)‖A‖_{3/2}^{3/2}`. Conversely `w(u) ∈ M` for
  every solenoidal `u ∈ L^3`.
- **(B2)** [HF18-B Lemma A, PASS] *Under* (H1), the weak gradient of `w` equals
  `DΨ(V)∇V` a.e. on `{w ≠ 0}` and `0` a.e. on `{w = 0}`, and then
  `div w = −σ` in `D'(R^3)` with `σ = ŵ·∇|w| ∈ L^1_loc`.

**Hypothesis under test.** `(H1)`: `w ∈ W^{1,1}_loc(R^3)`, equivalently `q ∈ W^{1,1}_loc`,
equivalently `φ ∈ W^{2,1}_loc`, where `q = ∇φ` with `φ ∈ W^{1,3}_loc` (de Rham; `φ ∈ BMO`,
determined up to an additive constant — HF18-A §1.1).

**Standing warning against circularity (check C1).** `σ` is defined through the
*approximate* gradient. Every statement below that involves a divergence of `w` before
(H1) is available is written for the **distribution** `div w = div q = Δφ ∈ W^{-1,3}(R^3)`,
never for `σ`. `σ` appears only in Corollary 3.3, and there only downstream of (H1).

**(B1) is upstream and is not re-sold.** It is used as a certificate: whenever a field is
produced below by choosing a solenoidal `A ∈ L^{3/2}` and setting `w = |A|^{-1/2}A`, the
Euler–Lagrange condition against **all** of `G_3` and the minimality for the datum `u = Pw`
are supplied by (B1), not asserted by inspection. This discharges the lane statement's
requirement that a field which "merely looks like a minimizer" be checked; by (B1) the
check is automatic and the class of candidates is exactly parametrized.

---

## 1. What the literature gives, and exactly what it does not

### 1.1 Our object is Stern's canonical `p`-coclosed primitive

**[DI]** M. A. Stern, *L_p-cohomology and the geometry of p-harmonic forms*,
arXiv:2403.19481v2 (submitted 28 Mar 2024, revised 2 Sep 2024), HTML full text fetched
this session. Definitions read off directly:
`C_p^k(M) = {f : f ∈ L_p^k(M), df ∈ L_p^{k+1}(M)}`, `B_p^k(M) = d C_p^{k-1}(M)`,
`Z_p^k(M) = {z ∈ C_p^k(M) : dz = 0}`; the manifolds are complete Riemannian `n`-manifolds
(`R^n` qualifies, and receives no special treatment).

> **Lemma 2.2** (verbatim). "For each `ζ ∈ B_p^k(M)`, `∃! β_∞ ∈ C_p^{k-1}(M)` such that
> `dβ_∞ = ζ`, and `d*(|β_∞|^{p-2}β_∞) = 0`."

Specialise `n = 3`, `p = 3`, `k = 2`, identify the 1-form `w^♭` with `w` and the 2-form
with `curl`: `dβ = ζ` reads `curl w = curl u`, and `d*(|β|^{p-2}β) = 0` reads
`div(|w|w) = 0`. **Our minimizer is exactly Stern's `β_∞`.** The proof mechanism is the
same convexity argument as `lem:quotient-minimizer` (Stern: "convex analysis on the `L_p`
norm"); no novelty is claimed by us for this, consistent with `rem:quotient-related` and
with HF18-B's scope note.

> **Theorem 2.9** (verbatim). "For each `φ ∈ H^k_{p,red}(M)`, `∃! h ∈ Z_p^k(M)` such that
> `[h]_red = φ`, and `d*(|h|^{p-2}h) = 0`."

> **Proposition 3.1 context** (verbatim, [DI]): "By elliptic regularity, a `p`-harmonic
> form `h` is smooth in a neighborhood of any point where it is nonzero", with `h` only
> Hölder continuous where it vanishes; the credit is to Uhlenbeck.

**The decisive reading.** The regularity statement in that paper attaches to
`h ∈ Z_p^k`, i.e. to forms that are **closed and nonlinearly coclosed**. Our `w` is
nonlinearly coclosed and has `dw = curl u ≠ 0`. Asked directly, the source states **no**
regularity whatsoever for `β_∞` of Lemma 2.2. This is a stronger and more precise
statement of the situation than HF18-B's scope note ("our `w` is not closed, so no
regularity transfers"): the object *is* named in the literature, and the literature is
silent about its regularity. Nothing here is an impossibility statement.

Note also that the closed case is vacuous for us: if `curl u = 0` then, `u` being
solenoidal and in `L^3`, `u = P w` with `w` curl-free, so `w ∈ G_3` and the
Euler–Lagrange condition with `g = w` gives `∫|w|^3 = 0`, i.e. `w = 0`, `Q = 0`.
So on the quotient route the closed case carries no information.

### 1.2 Uhlenbeck's structure is not our structure

**[MO]** K. Uhlenbeck, *Regularity for a class of non-linear elliptic systems*,
Acta Math. **138** (1977) 219–240 (Project Euclid landing page located; full text not
inspectable through the available channel). The structure, as reported consistently by
the secondary literature located this session [DI of the secondary statements]:
systems `−div(a(|∇U|)∇U) = f(x)` for vector-valued `U`, the nonlinearity entering only
through the **modulus of the gradient of the unknown**, with no `x`-dependence in `a`;
for `a(t) = t^{p-2}` this yields `∇U ∈ L^∞_loc ∩ C^{α}_loc`. The phrase "Uhlenbeck
structure" is standard for exactly this class.

Our operator is `div a(x,∇φ) = 0` with `a(x,ξ) = |u(x) + ξ|(u(x) + ξ)`. Three
independent failures, each verifiable from the display:

- (i) the nonlinearity depends on `|u(x) + ξ|`, **not** on `|ξ|`, so the coefficient is
  not a function of the modulus of the gradient of the unknown;
- (ii) it depends on `x` explicitly and irremovably (removing the shift by `ξ ↦ ξ + u(x)`
  destroys the gradient structure, because `u` is divergence-free rather than curl-free —
  HF18-A §1.3, audited);
- (iii) the ellipticity lower bound
  `D_ξ a(x,ξ)η·η >= γ(κ + |ξ|)^{p-2}|η|^2` fails for every `γ > 0`, `κ >= 0`, at any `x`
  with `u(x) ≠ 0` and `ξ = −u(x)` (HF18-A (1.3)–(1.4), audited).

So "run Uhlenbeck's trick" cannot mean "apply Uhlenbeck's theorem". §6 runs the
*mechanism* — difference quotients in the `V` variable — from scratch, which is legitimate
and which is what Theorem 6 delivers. Re-importing any member of the `C^{1,α}` family
would be the packet's "p-Laplace theorem outside its structure hypotheses" falsifier
(check C2).

### 1.3 Sibner–Sibner, Iwaniec–Scott–Stroffolini, Otway

**[MO]** L. M. Sibner and R. J. Sibner, *A non-linear Hodge–de Rham theorem*,
Acta Math. **125** (1970) 57–73 (Project Euclid landing page located; full text not
inspected). The manuscript's own directly-inspected characterization
(`rem:quotient-related`, [DI]) is that the theorem is proved for a **closed** datum and for
densities **bounded above and below**. Our density is `ρ(Q) = Q^{1/2}`, which is not
bounded below at `Q = 0`, and our datum is not closed. Both hypotheses fail, at the same
place: `{w = 0}`.

**[MO]** T. Iwaniec, C. Scott, B. Stroffolini, *Nonlinear Hodge theory on manifolds with
boundary*, Ann. Mat. Pura Appl. (4) **177** (1999) 37–115 (bibliographic record confirmed
this session; the technical structure conditions were not inspectable). Credited by Stern
[DI] together with Scott 1995 as the source of the `L^p`-form machinery, not of a
regularity theorem for `β_∞`. Not load-bearing anywhere below.

**[DI, prior wave]** T. H. Otway, arXiv:math-ph/9806007: structure condition
`K^{-1}(Q+k)^q ≤ ρ + 2Qρ' ≤ K(Q+k)^q` with uniform ellipticity asserted only for `k > 0`;
`ρ(Q) = Q^{1/2}` gives `q = 1/2`, `k = 0` — the excluded degenerate boundary case. This was
recomputed and verified in `hf19-review-shifted-hodge-regularity.md` §4 and is inherited
here unchanged (check C4). §2 below closes that degenerate case *for the admissible
class* in one direction only: Theorem 2 shows the linear-zero model is incompatible with
smooth data, which is a structural statement about `{w = 0}` and not the regularity
theorem the case would need.

**[MO]** M. Giaquinta, *Multiple Integrals in the Calculus of Variations and Nonlinear
Elliptic Systems*, Ann. of Math. Studies 105, Princeton 1983, Ch. V (Gehring's lemma in
the Giaquinta–Modica form: a reverse Hölder inequality
`⨍_{B_r} g^s ≤ C(⨍_{B_{2r}} g)^s + ⨍_{B_{2r}} f^s` self-improves the exponent).
Cited only to name the route attempted in §6 and to say exactly why its hypothesis is
unavailable; nothing below depends on the statement.

**[DI, prior wave]** P. Lindqvist, *Notes on the p-Laplace equation*, §4 Thm. 4.1
(Bojarski–Iwaniec difference quotients) and §10 inequalities (I), (V), (VI). Used only
through the audited (A5); not re-cited as load-bearing.

---

## 2. The admissibility constraint

### 2.1 The skew part is already known and smooth

**Theorem 1 (curl reduction).** Let `u` satisfy (0.1) and let `w = u + q` be the
minimizer, `q = ∇φ`. Then, in `D'(R^3)`,
```
curl w = curl u =: ω ∈ H^{m-1}(R^3) ⊂ C^{1,1/2}(R^3) ∩ L^∞,                   (2.1)
```
equivalently `sk(∇w) = sk(∇u)` as distributions. Consequently:

(a) (H1) holds **iff** the symmetric part `sym(∇w) = ∇u_sym + Hess φ` is in `L^1_loc`;
    the antisymmetric part contributes nothing to the question.

(b) If `w ∈ W^{1,1}_loc` then `curl w = ω` a.e.; in particular `ω = 0` a.e. on `{w = 0}`
    (a Sobolev field has vanishing weak gradient a.e. on any level set). Hence:
    **if `|{w = 0} ∩ {ω ≠ 0}| > 0` then (H1) is false.**

(c) On any open set where `ess inf |w| > 0`, (H1) holds, with
    `∫_E |∇w| ≤ (ess inf_E |w|)^{-1/2} |E|^{1/2} ‖∇V‖_2`. So (H1) is entirely a question
    about neighbourhoods of `{w = 0}`.

*Proof.* `q ∈ G_3` is curl-free in `D'` by (P3), so `curl w = curl u` in `D'`;
`u ∈ H^m` gives `curl u ∈ H^{m-1}`, and `m − 1 >= 3 > 3/2` gives the embedding.
(a) is the decomposition `∇w = sym(∇w) + sk(∇w)` together with (2.1).
(b) is the standard fact that the weak gradient of a `W^{1,1}_loc` function vanishes a.e.
on `{w = c}`, applied componentwise on `{w = 0}`, combined with `curl w = ω`.
(c) is (A6) and Cauchy–Schwarz: `|∇w| ≤ |w|^{-1/2}|∇V|` a.e. on `{V ≠ 0} ⊇ E`, and the
approximate gradient of a field that is bounded below in modulus and has
`|w|^{1/2}|∇w| ∈ L^2` is the weak gradient there — see Proposition 4.1 for the
identification step. ∎

Theorem 1(b) is a *falsification criterion*, recorded for later use: any construction
producing a genuine minimizer that vanishes on a set of positive measure inside
`{ω ≠ 0}` refutes (H1) outright. No such construction is produced here.

### 2.2 Rigidity: a nondegenerate zero of `A` is incompatible with smooth data

This is the falsifier arm's main theorem. It says that the one mechanism by which every
natural construction produces a zero of `w` — a solenoidal `A` vanishing linearly, giving
`|w| ~ d^{1/2}` — is *never* admissible.

**Theorem 2 (rigidity of linear zeros).** Let `A` be `C^1` on a neighbourhood of `x_0`,
`div A = 0`, `A(x_0) = 0`, and `L := DA(x_0) ≠ 0` (so `tr L = 0`). Put
`w = |A|^{-1/2}A`. Then there are an open cone `Γ` of directions at `x_0` and constants
`c_0, r_0 > 0` with
```
|sk(∇w)(x)| >= c_0 |x − x_0|^{-1/2}   for all x ∈ Γ, 0 < |x − x_0| < r_0.       (2.2)
```
In particular `curl w ∉ L^∞_loc(x_0)`. If moreover `A ∈ L^{3/2}(R^3)` globally and
`div A = 0` on `R^3`, so that `w ∈ M` and `u = Pw` is its datum by (B1), then
`curl u = curl w ∉ L^∞_loc`, hence `u ∉ W^{1,∞}_loc` and `u ∉ H^s_loc` for any `s > 5/2`.
**Such a `w` is not the minimizer of any datum satisfying (0.1).**

*Proof.* Write `x = x_0 + rθ`, `|θ| = 1`. Since `L ≠ 0`, choose a unit `θ_0` with
`Lθ_0 ≠ 0` and let `Γ_1` be a small open cone around `θ_0` on which `|Lθ| >= κ > 0`.
Then `A(x) = rLθ + O(r^2)` and `|A| >= κ r/2` for `r` small, so `A ≠ 0` and `w` is `C^1`
there, with (differentiating `f(z) = |z|^{-1/2}z`, `Df(z) = |z|^{-1/2}(I − (1/2)ẑ⊗ẑ)`)
```
∂_i w_j = |A|^{-1/2}( ∂_i A_j − (1/2) Â_j Â_k ∂_i A_k ),
```
whence, with `n := Â` and `(∇A)_{ij} = ∂_i A_j`,
```
2 sk(∇w) = |A|^{-1/2} · [ −2 sk(L) + (1/2)( n⊗L^T n − L^T n⊗n ) ] + O(1)
        =: |A|^{-1/2} M(n) + O(1),                                            (2.3)
```
the `O(1)` collecting the `O(r)` corrections to `∇A` and to `n` multiplied by
`|A|^{-1/2} = O(r^{-1/2})`, hence itself `O(r^{1/2})`; and `n → Lθ/|Lθ|` as `r ↓ 0`,
uniformly on `Γ_1`.

Suppose `M(n) = 0` for all `n` in some open subset `U` of the unit sphere. Applying the
matrix identity to the vector `n` itself, and using
`(n⊗v − v⊗n)n = n(v·n) − v` with `v = L^T n`:
```
sk(L) n = (1/4)[ n (n·Ln) − L^T n ],     i.e.   2Ln − L^T n = (n·Ln) n .        (2.4)
```
Both sides of (2.4) are real-analytic in `n` after homogenization
(`2Lx − L^T x = (x·Lx)x/|x|^2` on `R^3 \ {0}`), so validity on the open set `U` forces
validity for all `x ≠ 0`. Thus `Bx ∥ x` for all `x`, with `B := 2L − L^T`, which forces
`B = μI`. Transposing, `2L^T − L = μI`; adding and subtracting gives `L = L^T` and then
`L = μI`; `tr L = 0` gives `μ = 0`, i.e. `L = 0`, contradicting the hypothesis.

Hence `M` does not vanish identically on any open set of directions, so by continuity
there are an open cone `Γ ⊆ Γ_1` and `c_1 > 0` with `|M(n(θ))| >= c_1` on `Γ`. Insert
`|A| ≤ C r` into (2.3):
`|sk(∇w)| >= (1/2)(Cr)^{-1/2} c_1 − O(r^{1/2}) >= c_0 r^{-1/2}` for `r < r_0`, which is
(2.2). The last statement: `curl u = curl w` by Theorem 1; `u ∈ H^s_loc` with `s > 5/2`
would give `∇u ∈ H^{s-1}_loc ⊂ L^∞_loc` since `s − 1 > 3/2`, contradicting (2.2). ∎

*Numerical cross-check (bounded, not part of the proof).* 200 random traceless
normalized `L`, 2000 random directions each with `|Lθ| > 0.3`: the minimum over `L` of
`max_θ |M|` was `0.532`, i.e. `M` was never close to identically zero
(scratchpad `chk.py`, §10).

**Reading of Theorem 2.** `|A| = |w|^2`, so a linear zero of `A` is `|w| ≍ d^{1/2}`.
Theorem 2 says: *a minimizer of a smooth datum never vanishes to order `1/2`.*
Together with Theorem 5 below (which excludes order `> 1`), the order at a nondegenerate
model zero is pinned to `1`, where `∇w` is bounded and (H1) is trivial.

### 2.3 Consequence: the HF18-B witness family is inadmissible (computed)

The family of `hf18-divergence-speed-link.md` §2.3 is `w_δ = |A_δ|^{-1/2}A_δ` with
`A_δ = A_0 + A_1` on disjoint supports,
`A_0 = curl(φ_0 e_3)`, `φ_0 = (1−|x|^2)_+^4`, and
`A_1 = curl(ψ e_3)`, `ψ = δ^2(2 + cos k x_1)(sin k x_2)/k · χ((x−x_0)/R)`.
Both pieces vanish linearly on their zero sets. Explicitly:

*Oscillation.* Away from the cutoff annulus,
`A_1 = δ^2 F(kx)`, `F(y) = ((2 + cos y_1)cos y_2, sin y_1 sin y_2, 0)`.
Zeros: `cos y_2 = 0` (since `2 + cos y_1 >= 1`), then `sin y_2 = ±1`, so `sin y_1 = 0`:
the lines `y = (nπ, π/2 + mπ)`, as the note states. Near `y_0 = (0, π/2)`, writing
`y = (a, π/2 + b)`, `F ≈ (−3b, a, 0)` — a linear zero with `L ≠ 0`. With
`ρ = (a^2 + 9b^2)^{1/2}` and `G = ρ^{-1/2}(−3b, a, 0)`, a direct computation gives
```
(curl G)_3 = ∂_a G_2 − ∂_b G_1 = 4ρ^{-1/2} − (1/2)ρ^{-5/2}(a^2 + 27 b^2),
```
so on the ray `b = 0`, `(curl G)_3 = (7/2)|a|^{-1/2} → ∞`. Since
`curl_x w_1 = δk (curl_y G)(kx)`, `curl w_δ` is unbounded near every zero line.
(Numerical check, scratchpad `chk.py`: at `a = 10^{-2}, 10^{-3}, 10^{-4}` the centred
difference of `curl G` gives `35.0000, 110.6795, 349.9332` against
`3.5·a^{-1/2} = 35.0000, 110.6797, 350.0000`.)

*Bulk.* `w_0 = √8 (1−|x|^2)_+^{3/2} ρ^{-1/2}(−x_2, x_1, 0)` is azimuthal with speed
`f = √8(1−|x|^2)^{3/2}ρ^{1/2}`; for an azimuthal field
`curl w = −(∂_z f)e_ρ + ρ^{-1}∂_ρ(ρ f)e_z`, and `ρ^{-1}∂_ρ(ρ^{3/2}) = (3/2)ρ^{-1/2} → ∞`
on the axis.

**Corollary 2.1.** For every `δ`, `curl u_δ = curl w_δ ∉ L^∞_loc`; hence
`u_δ = P w_δ ∉ H^s_loc` for `s > 5/2`, and no member of the HF18-B witness family — bulk,
oscillation, or their sum — is the minimizer of a datum satisfying (0.1).

**Scope, stated precisely so this is not read as a re-audit.** HF18-B Prop. 2.2 is a
statement about the class `M` (all minimizers, `L^3` data), and on that class it stands
exactly as audited: this note re-derives nothing of it and contradicts nothing in it. The
observation here is only that *the family cannot be reused as a candidate for the (H1)
question*, whose standing hypothesis is (0.1). Whether the HF18-B classification of
weighted inequalities changes when restricted to the admissible class is a **separate,
unexamined question**, flagged in §9 as a non-claim and in §10 as a next action.

**Corollary 2.2 (the natural negative route is closed).** Producing a counterexample to
(H1) by choosing a solenoidal `A ∈ C^1 ∩ L^{3/2}` and reading off `w = |A|^{-1/2}A`
requires **every** zero of `A` to be degenerate (`DA = 0` there). Linear vanishing —
which is what generic solenoidal fields do on their zero sets, and what every construction
in the programme so far has produced — is vetoed by Theorem 2.

---

## 3. The scalar reduction: (H1) is a statement about `div w` alone

**Theorem 3 (Calderón–Zygmund equivalence).** Let `u` satisfy (0.1), `w = u + q` the
minimizer, `q = ∇φ`, and let `T := div w = div q = Δφ ∈ W^{-1,3}(R^3)` be the
**distributional** divergence. Let `1 < p < ∞`. Then, for concentric balls
`B_{r/2} ⊂ B_r ⊂ B_{2r}`:

(a) If `T ∈ L^p(B_{2r})` then `w ∈ W^{1,p}(B_{r/2})`, with
```
‖∇w‖_{L^p(B_{r/2})} ≤ C_p ‖T‖_{L^p(B_{2r})} + C(p,r)‖q‖_{L^3(B_{2r})} + ‖∇u‖_{L^p(B_{r/2})}.
```
(b) Conversely, if `w ∈ W^{1,p}(B_r)` then `T = tr(∇w) ∈ L^p(B_r)`.

Hence `w ∈ W^{1,p}_loc(R^3) ⟺ div w ∈ L^p_loc(R^3)`, and

(c) **(H1) holds as soon as `div w ∈ L^p_loc` for a single `p > 1`.**

(d) If `T ∈ L\log L(B_{2r})` then `∇w ∈ L^1(B_{r/2})`, i.e. (H1) holds locally
    [Stein's endpoint theorem for Calderón–Zygmund operators, MO, non-load-bearing].
    If `T` is only a locally finite measure, one gets `∇w ∈ L^{1,∞}_loc` (weak `L^1`,
    the CZ weak-type estimate, MO) — which does **not** give (H1).

Globally: if `T ∈ L^{3/2}(R^3)` then `Hess φ ∈ L^{3/2}(R^3)` with
`‖Hess φ‖_{3/2} ≤ C_{3/2}‖T‖_{3/2}`, and `w ∈ W^{1,3/2}_loc`.

*Proof.* `div u = 0` gives `T = Δφ`. Let `η ∈ C_c^∞(B_{2r})`, `η = 1` on `B_r`,
`0 ≤ η ≤ 1`. Assume `T ∈ L^p(B_{2r})`; then `f := ηT ∈ L^p(R^3)` has compact support.
Let `N(x) = −1/(4π|x|)` and `ψ := N * f`. By the Calderón–Zygmund theorem
`D^2ψ ∈ L^p(R^3)` with `‖D^2ψ‖_p ≤ C_p‖f‖_p ≤ C_p‖T‖_{L^p(B_{2r})}` [classical; used at
`1 < p < ∞` only]. Now `Δ(φ − ψ) = T − f = 0` in `D'(B_r)`, and `φ − ψ ∈ L^1_loc`, so by
Weyl's lemma `φ − ψ` is harmonic, hence smooth, in `B_r`; interior estimates for harmonic
functions give
`‖D^2(φ − ψ)‖_{L^∞(B_{r/2})} ≤ C r^{-2}‖∇(φ − ψ)‖_{L^1(B_r)} ≤ C(r)(‖q‖_{L^3(B_{2r})} + ‖∇ψ‖_{L^3(B_r)})`,
and `‖∇ψ‖_{L^3(B_r)} ≤ C(p,r)‖f‖_p` by the Sobolev embedding applied to `ψ ∈ W^{2,p}`
(or, for small `p`, by the Riesz-potential bound for `N * f`, `f` compactly supported).
Therefore `Hess φ ∈ L^p(B_{r/2})`, and `∇w = ∇u + Hess φ` with `∇u ∈ L^∞`. This is (a).
(b) is immediate: the distributional divergence of a `W^{1,p}` field is the a.e. trace of
its weak gradient. (c) is (a) with `L^p_loc ⊂ L^1_loc`. (d) replaces the CZ bound by the
corresponding endpoint statements; both are quoted, not used elsewhere.
For the global claim, `q = ∇φ ∈ L^3(R^3)` and, as tempered distributions,
`∂_i q_j = −R_i R_j (div q)` (Fourier: `(∂_i q_j)^ = −4π^2 ξ_i ξ_j φ̂ = (ξ_iξ_j/|ξ|^2)(div q)^`),
so `T ∈ L^{3/2}(R^3)` gives `Hess φ ∈ L^{3/2}(R^3)` by the `L^{3/2}` boundedness of the
Riesz transforms. ∎

**Remark 3.1 (this is not circular).** Theorem 3 is a statement about the distribution
`Δφ`, available before any regularity of `w`. It uses nothing about the nonlinear equation
`div(|w|w) = 0` — only `curl q = 0` and `q ∈ L^3`. The nonlinear content of the problem
must therefore enter through a statement *about the divergence*, and only that.

**Remark 3.2 (what Theorem 3 does and does not buy).** It buys a genuine reduction:
a `3`-component question about `∇w` becomes a `1`-component question about a scalar
distribution, and the vector/curl half of `∇w` is discharged by Theorem 1. It does not buy
(H1), because the equation `div(|w|w) = 0` controls `div w` only through the weighted
bound `∫|w|σ^2 ≤ D_3/2` (HF18-B (1.3'), audited, and stated for the approximate gradient),
which degenerates exactly on `{w = 0}`.

**Corollary 3.3 (the HF18-B hypotheses collapse).** With `T = div w` distributionally:
```
(H1) and (H2)   ⟺   T ∈ L^{3/2}(R^3),
```
and then `σ = −T`. *Proof.* (⟸) `T ∈ L^{3/2}` gives `w ∈ W^{1,3/2}_loc ⊂ W^{1,1}_loc`
(Theorem 3), i.e. (H1); then (B2) gives `σ = −T ∈ L^{3/2}`, i.e. (H2). (⟹) Under (H1),
(B2) gives `T = −σ` in `D'`, and (H2) says `σ ∈ L^{3/2}`. ∎
This is a statement about the *logical structure* of the two hypotheses of HF18-B, not a
proof of either, and not a re-audit of that note.

---

## 4. The sharp integrability criterion, and the failure of the standard obstacle

### 4.1 The exact statement of what is needed

**Proposition 4.1 (localization to the zero set).** Let `E ⊂ R^3` be open and bounded.
If
```
∫_E |w|^{-1/2}|∇V| dx < ∞                                                      (4.1)
```
then `w ∈ W^{1,1}(E)` and its weak gradient is `DΨ(V)∇V` on `{V ≠ 0}`, `0` on `{V = 0}`.
On `{V = 0}`, `∇V = 0` a.e. (Sobolev functions have vanishing weak gradient a.e. on level
sets), so the integrand of (4.1) is `0` there and the zero set contributes nothing.

*Proof.* Set `G := DΨ(V)∇V · 1_{{V≠0}}`, so `|G| ≤ |w|^{-1/2}|∇V|` and `G ∈ L^1(E)` by
(4.1). Let `w_ε^{(τ)} := Ψ_τ(V)` with `Ψ_τ(V) := (|V|^2 + τ^2)^{-1/6}V`, a `C^1` map with
`Ψ_τ → Ψ` locally uniformly and `|DΨ_τ| ≤ (|V|^2+τ^2)^{-1/6}`. The chain rule for
`C^1 ∘ H^1` gives `Ψ_τ(V) ∈ W^{1,1}(E)` with `∇Ψ_τ(V) = DΨ_τ(V)∇V`; as `τ ↓ 0`,
`Ψ_τ(V) → w` in `L^3(E)` (dominated convergence, `|Ψ_τ(V)| ≤ |w|`), and
`DΨ_τ(V)∇V → G` a.e. and dominated by `2|w|^{-1/2}|∇V| ∈ L^1(E)` on `{V ≠ 0}` while on
`{V = 0}` both sides vanish a.e. Closedness of the weak gradient gives `w ∈ W^{1,1}(E)`
with `∇w = G`. ∎

**Theorem 4 (layered criterion; sharp).** Let `E` be open and bounded and put
`E_j := E ∩ {2^{-j-1} ≤ |w| < 2^{-j}}`, `j ∈ Z`. If
```
S(E) := Σ_j 2^{(j+1)/2} |E_j|^{1/2} ‖∇V‖_{L^2(E_j)} < ∞ ,                       (4.2)
```
then `∫_E |w|^{-1/2}|∇V| ≤ S(E)` and hence, by Proposition 4.1, `w ∈ W^{1,1}(E)`.
Moreover:

(a) `S(E) ≤ (2∫_E |w|^{-1})^{1/2}‖∇V‖_{L^2(E)}`, so `|w|^{-1} ∈ L^1(E)` is sufficient;

(b) *(sharpness)* for a fixed sequence `(|E_j|)` with `Σ_j 2^j|E_j| = ∞`, there is a
    square-summable allocation `a_j = ‖∇V‖_{L^2(E_j)}` of the finite Dirichlet budget
    for which `S(E) = ∞`. Equivalently: `∫_E |w|^{-1} < ∞` is exactly the condition on
    the level-set measures alone that makes (4.2) hold **for every** distribution of
    `|∇V|`; but for a *given* `V` it is strictly stronger than needed.

(c) More generally, if `∇V ∈ L^p(E)` for some `p ∈ [2,∞]` and `∫_E |w|^{-p'/2} < ∞`
    with `p' = p/(p−1) ∈ [1,2]`, then (4.1) holds. At `p = 2` this is `|w|^{-1} ∈ L^1`;
    at `p = ∞` it is only `|w|^{-1/2} ∈ L^1`.

*Proof.* (4.2): `∫_{E_j}|w|^{-1/2}|∇V| ≤ 2^{(j+1)/2}∫_{E_j}|∇V| ≤ 2^{(j+1)/2}|E_j|^{1/2}‖∇V‖_{L^2(E_j)}`
by Cauchy–Schwarz, then sum. (a): Cauchy–Schwarz in `j`, with
`Σ_j 2^{j+1}|E_j| ≤ 2Σ_j ∫_{E_j}|w|^{-1} = 2∫_E|w|^{-1}`
(on `E_j`, `|w| < 2^{-j}`, so `2^j |E_j| ≤ ∫_{E_j}|w|^{-1}`) and `Σ_j‖∇V‖^2_{L^2(E_j)} ≤ ‖∇V‖^2_{L^2(E)}`.
(b): put `c_j := 2^{(j+1)/2}|E_j|^{1/2}`, so `Σ_j c_j^2 = ∞`; for any sequence with
`Σ c_j^2 = ∞` there is `a ∈ ℓ^2` with `Σ c_j a_j = ∞` (else `c ∈ (ℓ^2)^* = ℓ^2`).
(c): Hölder with exponents `p, p'`. ∎

**Answer to the lane's question about the singular inverse map.** `Ψ(V) = |V|^{-1/3}V`
is singular at `V = 0` with `|DΨ| = |V|^{-1/3} = |w|^{-1/2}`. The exact integrability of
`∇V` required to convert `V ∈ H^1` into `w ∈ W^{1,1}_loc` is (4.1); the borderline
statements are Theorem 4(c). Nothing weaker than a **negative moment of `|w|`** will do
in this route, at any integrability of `∇V`: even `∇V ∈ L^∞_loc` still needs
`|w|^{-1/2} ∈ L^1_loc`.

**Coarea and capacity, explicitly (lane question).** The zero set itself is harmless:
`∇V = 0` a.e. on `{V = 0}` (Proposition 4.1), so it contributes nothing to (4.1) — the
difficulty is entirely in the strip `{0 < |w| < λ}` as `λ ↓ 0`. The coarea formula for
`|V| ∈ H^1 ∩ W^{1,1}_loc`, `∫_E |∇|V|| = ∫_0^∞ H^2({|V| = t} ∩ E) dt`, is available and
**does not close the strip estimate**: it controls the perimeters of superlevel sets, and
yields no upper bound on `|{0 < |V| < τ} ∩ E|`, which is the quantity (4.2) needs. A
capacity argument is likewise unavailable, for two independent reasons: `{w = 0}` can carry
positive Lebesgue measure (nothing above excludes it, and Theorem 1(b) shows only that it
would then refute (H1) where `ω ≠ 0`), and the removability theory relevant to `W^{1,1}`
is measure-theoretic (`H^2`/perimeter), not capacitary, so a set of zero `p`-capacity
carries no `W^{1,1}` conclusion. This is the honest disposition of both suggestions in the
lane statement.

### 4.2 The standard obstacle is sufficient but not necessary

`hf18-hodge-regularity.md` §1.6(e) records, correctly, that `|w|^{-1}` *need not* be
locally integrable, and `hf19-review-shifted-hodge-regularity.md` §3 elevates this to
"the exact analytic obstacle", demanding that a candidate "either bound `∫_E|∇w|` without
passing through `∫_E |w|^{-1}`, or control `|{|w| < ε} ∩ E|` quantitatively". The first
alternative is realised here, and the demand is shown to be strictly stronger than (H1).

**Proposition 4.4 (an explicit minimizer with `|w|^{-1} ∉ L^1_loc` and `w` smooth).**
Let `ψ(x) = −|x_1| x_1^2/3` (so `ψ ∈ C^2(R^3)`, `−∂_1ψ = |x_1| x_1`, `∂_2ψ = 0`), let
`χ ∈ C_c^∞(R^3)` with `χ = 1` on `B := B_1(0)`, and set
```
A := curl( χ ψ e_3 ) ∈ C^1_c(R^3;R^3),      w := |A|^{-1/2}A .                  (4.3)
```
Then:

(i) `div A = 0` and `A ∈ L^{3/2}`, so by **(B1)** `w ∈ M` **is** the minimizing
    representative of `u := Pw ∈ L^3`, with `q = (I − P)w ∈ G_3`; the Euler–Lagrange
    condition holds against **all** of `G_3`.
(ii) On `B`: `A = (0, |x_1|x_1, 0)` and `w = (0, x_1, 0)`, so `w ∈ C^∞(B)`,
     `∇w = e_2⊗e_1` is constant, `div w = 0` on `B`, `curl w = e_3`.
(iii) `Δφ = div q = div w = 0` in `D'(B)`, so `φ` is harmonic hence real-analytic on `B`;
      therefore `q ∈ C^∞(B)` and `u = w − q ∈ C^∞(B)`, with `div u = 0` and
      `curl u = e_3 ≠ 0` on `B`.
(iv) `{w = 0} ∩ B = {x_1 = 0} ∩ B` is a codimension-one set, `|w| = |x_1| = d(x, {w=0})`
     exactly, and
```
     ∫_B |w|^{-1} dx = ∫_B |x_1|^{-1} dx = ∞ ,     while     w ∈ W^{1,∞}(B).
```
(v) The layered criterion (4.2) holds on `B`: `|E_j| ≍ 2^{-j}`, `|V| = |x_1|^{3/2}` gives
    `|∇V| ≍ |x_1|^{1/2}`, so `‖∇V‖_{L^2(E_j)} ≍ 2^{-j}` and
    `S(B) ≍ Σ_j 2^{j/2}·2^{-j/2}·2^{-j} < ∞`.

*Proof.* (i) `A` is a curl, hence solenoidal, and is `C^1` with compact support, hence in
`L^{3/2}`; apply (B1). (ii) On `B`, `χ ≡ 1` so
`A = (∂_2(χψ), −∂_1(χψ), 0) = (0, |x_1|x_1, 0)`; then `|A| = x_1^2`, `|A|^{-1/2} = |x_1|^{-1}`,
and `|A|^{-1/2}A = (0, x_1, 0)` (with the value `0` at `x_1 = 0`, consistent with `A = 0`
there). The rest is direct. (iii) `div u = 0` always, so `Δφ = div q = div w`, which on
`B` is `∂_2 x_1 = 0`; Weyl's lemma applies to `φ ∈ W^{1,3}_loc`. (iv), (v) direct
computation. ∎

**Consequence.** `∫_E |w|^{-1} < ∞` is **not** a necessary condition for (H1), and the
route that must be found is not "avoid `∫|w|^{-1}`" as an exotic manoeuvre but simply
"use the layered criterion (4.2)". Proposition 4.4 also shows that a codimension-one zero
set of `w` is compatible with everything: `w` smooth, `u` smooth, `curl u` nonzero, `w` a
genuine minimizer against all of `G_3`.

**Scope of Proposition 4.4, stated exactly.** `u` is `C^∞` on `B` and `w` is the genuine
global minimizer of `u = Pw`; but `u` is **not** claimed to be in `H^m(R^3)` globally
(outside `B` the cutoff region of `A` generically has linear zeros, which by Theorem 2
make `curl u` unbounded there). Since (H1) is a local statement and all hypotheses of the
admissible setting hold on `B`, this is enough for the conclusion drawn — and it is
*not* enough to claim an admissible global example. Constructing one, or showing none
exists, is a next action (§10).

---

## 5. Vorticity non-degeneracy: a quantitative lower bound on `|w|`

The HF19 review's second alternative was "control `|{|w| < ε} ∩ E|` quantitatively".
This section supplies the only quantitative control that the structure actually yields —
an averaged lower bound — and states precisely how far it falls short.

**Theorem 5 (circulation bound).** Let `w ∈ L^3(R^3;R^3)` with `curl w = ω` in `D'` for a
continuous `ω`. Then for every ball `B_r(x_0)` and every unit vector `n`,
```
⨍_{B_r(x_0)} |w| dx  >=  (r/32) · inf_{B_r(x_0)} (ω·n) .                        (5.1)
```
Consequently `⨍_{B_r(x_0)}|w| >= (r/32)·max_{|n|=1} inf_{B_r(x_0)}(ω·n)` and, `ω` being
continuous,
```
limsup_{r ↓ 0}  r^{-1} ⨍_{B_r(x_0)} |w|  >=  |ω(x_0)| / 32 .                    (5.2)
```

*Proof.* Fix `n`; use cylindrical coordinates `(s, θ, z)` about the axis `x_0 + Rn`.
Let `C := {|x' − x_0'| ≤ r/2, |z| ≤ r/2}`, a cylinder contained in `B_r(x_0)` (its
farthest points are at distance `r/√2 < r`). Let `w_ε := ρ_ε * w`, so `w_ε ∈ C^∞`,
`curl w_ε = ρ_ε * ω`, `w_ε → w` in `L^1(C)`, and `ρ_ε*ω → ω` uniformly on compacts. For
each `s ∈ (0, r/2]` and `|z| ≤ r/2`, Stokes' theorem on the disc `D_{s,z} ⊂ C` gives
```
∮_{∂D_{s,z}} |w_ε| dl  >=  | ∮_{∂D_{s,z}} w_ε·dl |  =  | ∫_{D_{s,z}} (ρ_ε*ω)·n dS |  >=  π s^2 c_ε ,
```
`c_ε := inf_C (ρ_ε*ω)·n`. Integrating in `s` and `z` (cylindrical coordinates),
```
∫_C |w_ε| dx = ∫_{-r/2}^{r/2}∫_0^{r/2} ( ∮_{∂D_{s,z}}|w_ε| dl ) ds dz >= r · π c_ε (r/2)^3/3 = π c_ε r^4/24 .
```
Let `ε ↓ 0`: the left side tends to `∫_C |w|`, and `c_ε → c := inf_C ω·n >= inf_{B_r} ω·n`
by uniform continuity. Since `∫_{B_r}|w| >= ∫_C|w|` and `|B_r| = 4πr^3/3`,
`⨍_{B_r}|w| >= (π c r^4/24)/(4π r^3/3) = c r/32`. (5.2) follows by continuity of `ω`
with `n = ω̂(x_0)`. ∎

By Theorem 1, `ω = curl u` here, so (5.1) is a bound in terms of the **input datum**.

**Corollary 5.1 (no vanishing faster than first order).** If `|w(x)| = O(|x − x_0|^α)`
as `x → x_0` for some `α > 1`, then `ω(x_0) = 0`. In particular at every point of
`{ω ≠ 0}`, `|w|` vanishes at most to first order in the mean.

**Corollary 5.2 (no flat spots inside `{ω ≠ 0}`).** If `w = 0` a.e. on an open set `U`,
then `ω = 0` on `U`. (Immediate from (5.1), or from `curl w = ω` in `D'(U)`.)

**Theorem 6 (the pincer at a nondegenerate model zero).** Let `x_0 ∈ {w = 0}` with
`ω(x_0) ≠ 0`, and suppose `|w| ≍ d(x, Z)^β` near `x_0` for a closed set `Z ∋ x_0` and some
`β > 0`. Then:
- `β ≤ 1` by Corollary 5.1;
- `β = 1/2` — i.e. `A = |w|w` vanishing linearly — is excluded by Theorem 2 whenever `A`
  is `C^1` near `x_0` with `DA(x_0) ≠ 0`;
- for `0 < β ≤ 1` and `Z` a `C^1` submanifold of codimension `1` or `2`,
  `|∇w| ≲ d^{β-1}` is locally integrable (codimension `1`: `∫_0 t^{β-1}dt < ∞`;
  codimension `2`: `∫_0 t^{β-1} t\,dt < ∞`), so **(H1) holds locally**.

So the entire model class of power-law vanishing on rectifiable zero sets is settled
affirmatively, and the admissible exponent is pinned near `β = 1` — which is exactly the
`C^1` picture of Proposition 4.4.

**Exactly how far Theorem 5 falls short (no overclaim).** (5.1) is an *averaged* lower
bound and does not control a negative moment. Quantitatively: from (5.1) with
`λ < c r/64` one gets, by splitting and Hölder,
`|{|w| >= λ} ∩ B_r| >= ( (c r/64)|B_r| / ‖w‖_{L^3(B_r)} )^{3/2}`; choosing `r = 64λ/c`
this reads `|{|w| >= λ} ∩ B_r| >= C λ^6`, a *fraction* `≍ λ^3` of `|B_r|`. Summing over a
covering of a unit ball gives only `|{|w| >= λ} ∩ B_1| >= C λ^3`, whereas Theorem 4
would need `|{|w| < λ} ∩ B_1| = O(λ^{1+η})`. The gap is not small and is not closed here.

---

## 6. The positive route (i): Uhlenbeck's mechanism in the `V` variable

### 6.1 A local Caccioppoli inequality for `V`

The global identity of HF18-A is cutoff-free and gives `‖∇V‖_2`. For a Gehring iteration
one needs a *local* inequality. It exists, and here it is.

**Theorem 6' (local Caccioppoli for `V`).** Let `u` satisfy (0.1), `w = u + q` the
minimizer, `q = ∇φ`. Then for every `ζ ∈ C_c^∞(R^3)` with `0 ≤ ζ ≤ 1` and every constant
vector `c ∈ R^3`,
```
∫ ζ^2 |∇V|^2 dx  ≤  (81/2) ∫ ζ^2 |w| |∇u|^2 dx  +  162 ‖∇ζ‖_∞^2 ∫ ζ^2 |w| |q − c|^2 dx .   (6.1)
```

*Proof.* Fix `k` and `h ≠ 0`; `τ_h f = f(· + h e_k)`, `D_h f = (τ_h f − f)/h`.
`G_3` is translation invariant, so the Euler–Lagrange condition (P1) applied to `w` and to
`τ_h w` (the minimizer of `τ_h u`, by translation invariance of the whole problem) gives
`∫ D_h A · g = 0` for every `g ∈ G_3`.

Take `ψ := ζ^2 (D_h φ − c_k)`. Then `ψ` has compact support, `ψ ∈ L^3(R^3)` and
`∇ψ = ζ^2 D_h q + 2ζ (D_hφ − c_k)∇ζ ∈ L^3(R^3)`, so `∇ψ ∈ G_3` by **(P2)**. Hence
```
0 = ∫ D_h A·∇ψ = ∫ ζ^2 D_h A · D_h q + 2∫ ζ (D_hφ − c_k) D_h A·∇ζ ,
```
all integrals absolutely convergent (`D_hA ∈ L^{3/2}`, `∇ψ ∈ L^3`). With `q = w − u`,
```
∫ ζ^2 D_h A·D_h w  =  ∫ ζ^2 D_h A·D_h u  −  2∫ ζ (D_hφ − c_k) D_h A·∇ζ .
```
By (A5), pointwise `D_hA·D_hw = h^{-2}(Ã(τ_hw) − Ã(w))·(τ_hw − w) >= (8/9)|D_hV|^2` and
`|D_hA| ≤ 2√2 (|τ_hw| + |w|)^{1/2}|D_hV|`. Writing `X := (∫ζ^2|D_hV|^2)^{1/2}`,
`Y_1 := (∫ζ^2(|τ_hw|+|w|)|D_hu|^2)^{1/2}`, `Y_2 := (∫ζ^2(|τ_hw|+|w|)|D_hφ − c_k|^2)^{1/2}`,
Cauchy–Schwarz gives
```
(8/9) X^2 ≤ 2√2 X Y_1 + 4√2 ‖∇ζ‖_∞ X Y_2 ,   hence   X ≤ (9/8)(2√2 Y_1 + 4√2 ‖∇ζ‖_∞ Y_2)
```
(if `X = 0` the conclusion is trivial; otherwise divide by `X`).
Now let `h → 0`: `D_hV → ∂_k V` in `L^2(R^3)` (HF18-A Theorem 1), `τ_h w → w` in `L^3`,
`D_h u → ∂_k u` uniformly on compacts (`u ∈ C^2`), and `D_hφ → ∂_kφ = q_k` in `L^3_loc`
(`φ ∈ W^{1,3}_loc`); hence `X → (∫ζ^2|∂_kV|^2)^{1/2}`,
`Y_1 → (2∫ζ^2|w||∂_ku|^2)^{1/2}`, `Y_2 → (2∫ζ^2|w||q_k − c_k|^2)^{1/2}`. Squaring,
using `(a+b)^2 ≤ 2a^2+2b^2`, and summing over `k = 1,2,3` gives (6.1). ∎

*Consistency check.* Taking `ζ ↑ 1`, `c = 0` and Hölder gives
`‖∇V‖_2^2 ≤ (81/2)‖w‖_3‖∇u‖_3^2`, of the same form and within a factor `2` of the audited
global bound (A1) — the factor being the extra Young step. No boundary term at infinity
appears (check C6): (6.1) is proved with a compactly supported `ζ`, and the global
statement is only quoted for the check.

### 6.2 Exactly why Gehring cannot be started (the obstruction)

A Gehring/Giaquinta–Modica iteration needs a **reverse Hölder inequality**: the same
quantity on both sides, with a lower exponent on the right,
`⨍_{B_r} |∇V|^2 ≤ C (⨍_{B_{2r}} |∇V|^{2σ})^{1/σ} + (data)` for some `σ < 1`. Inequality
(6.1) is not of this form and cannot be brought to it:

- **(O1) The test class is only `G_3`.** In the scalar `p`-Laplace situation one tests with
  `ζ^2(φ − c)`, a *scalar* multiple of a cutoff, and the Caccioppoli produced has
  `|∇φ − c|` on the right — one derivative below the left-hand side. Here the same is true
  in the `V` variable, and worse: `V` is not the unknown of a variational problem whose
  admissible variations include `ζ^2(V − V_B)`. Every admissible variation is `∇ψ ∈ G_3`,
  and `ζ^2(V − V_B)` is not a gradient. **No Caccioppoli inequality with `V − V_B` on the
  right is derivable from the Euler–Lagrange condition of this problem.**
- **(O2) The right-hand side of (6.1) is not convertible.** Its dangerous term is
  `r^{-2}∫_{B_{2r}}|w||q − c|^2` (choosing `‖∇ζ‖_∞ ≍ r^{-1}`). To dominate it by a lower
  power of `∫|∇V|^2` one needs a Sobolev–Poincaré inequality for `q` on `B_{2r}` — i.e.
  one needs `q ∈ W^{1,s}_loc` for some `s`. That is (H1). **The iteration is circular at
  its first step**, and the circularity is exhibited, not conjectured.
- **(O3) Even a successful Gehring would not suffice.** Suppose, counterfactually, that
  `∇V ∈ L^p_loc` were proved for every `p < ∞`, or even that `V ∈ C^{0,1}_loc`. By
  Theorem 4(c) the conclusion `w ∈ W^{1,1}_loc` would still require
  `∫_E |w|^{-p'/2} < ∞` with `p' > 1`, and at the extreme `p = ∞` still
  `|w|^{-1/2} ∈ L^1_loc`. **Higher integrability of `∇V` never removes the negative
  moment**; only a lower bound on `|w|` does, and the only lower bound available is the
  averaged Theorem 5, whose shortfall is quantified in §5.
- **(O4) Local boundedness of `V` is the wrong direction.** `w ∈ L^∞_loc` is equivalent to
  `q ∈ L^∞_loc` (since `u ∈ L^∞`) and would be a genuine gain for other purposes, but by
  (O3) it bears on (H1) not at all: (H1) is a statement about *lower* bounds on `|w|`.

This is the exact obstruction requested by the lane statement for arm (i). It is an
obstruction to the *route*, not an impossibility statement about (H1).

---

## 7. The falsifier arm: what a counterexample must now look like

Collecting Theorems 1, 2, 4, 5, a counterexample to (H1) must satisfy **all** of:

1. `w = |A|^{-1/2}A` for a solenoidal `A ∈ L^{3/2}` (by (B1) this is not a restriction —
   it is the exact parametrization, and it is what makes the Euler–Lagrange check against
   all of `G_3` automatic);
2. `curl w = curl u ∈ H^{m-1} ⊂ C^{1,1/2}` — a *smoothness* constraint on the skew part of
   `∇w` which the gradient part `q` cannot help satisfy, since `curl q = 0`;
3. therefore **every zero of `A` is degenerate**: `DA = 0` there (Theorem 2, Corollary 2.2);
4. `|w|` vanishes at most to first order in the mean at every point of `{ω ≠ 0}`
   (Theorem 5), so the vanishing cannot be "fast";
5. and yet `Σ_j 2^{j/2}|E_j|^{1/2}‖∇V‖_{L^2(E_j)} = ∞` on some bounded set (Theorem 4),
   which by Theorem 4(b) requires at minimum `∫_E |w|^{-1} = ∞`, i.e. the level-set
   measures must satisfy `Σ_j 2^j |E_j| = ∞` — *and* the finite Dirichlet budget
   `Σ_j ‖∇V‖^2_{L^2(E_j)} ≤ ‖∇V‖_2^2` must be adversarially allocated across those
   levels.

**The scale budget, and why it is only Cauchy–Schwarz.** On a region of measure `m` where
`|w| ≍ δ` and `|∇w| ≍ δ k`, the audited dissipation costs `δ^3 k^2 m` and the target
integral is `δ k m`; eliminating `k` gives exactly
`∫|∇w| ≤ (∫|w||∇w|^2)^{1/2}(∫|w|^{-1})^{1/2}`, i.e. Cauchy–Schwarz again. A single field
can be built with `Σ_j δ_j^3 k_j^2 m_j < ∞` and `Σ_j δ_j k_j m_j = ∞` (e.g.
`m_j = 2^{-j}`, `δ_j = 2^{-2j}`, `k_j = 2^{3j}`, with `Σ δ_j^3 m_j < ∞` so `w ∈ L^3`):
**the dissipation budget alone does not exclude a counterexample.** What excludes this
family is constraint 2: its oscillating piece has `|curl w| ≍ δ_j k_j = 2^j → ∞`. The same
veto is what Corollary 2.1 applies to the HF18-B family, where the blow-up is
`d^{-1/2}` at the zero lines rather than `2^j` across scales.

**Status of the falsifier arm.** No counterexample is produced, and none is claimed to be
impossible. What is produced is the veto on the entire linear-zero mechanism, which is the
mechanism every construction in the programme so far has used, together with the exact
list 1–5 that a future construction must satisfy simultaneously. The constraints 3 and 5
pull in opposite directions: 3 forces `|w|` to vanish *slowly* (order `>= 1`, since
`|A| = |w|^2` must vanish to order `> 2` in the `C^1` model), while 5 forces the level-set
measures `|E_j|` to be *large* at small `|w|`; whether they are jointly satisfiable is the
open question this lane leaves.

---

## 8. Answers to the pre-registered checks C1–C7

- **C1 (circularity in the divergence identity).** Every divergence statement before (H1)
  is written for the distribution `Δφ` (Theorem 3, Remark 3.1). `σ` appears only in
  Corollary 3.3, downstream of (H1) via the audited (B2). Theorem 5 uses `curl w = curl u`
  in `D'`, proved via (P3), and Stokes' theorem for the mollification, never a pointwise
  gradient of `w`.
- **C2 (structure hypotheses, checked at `{w = 0}` not at `{∇φ = 0}`).** No member of the
  `C^{1,α}` family is imported; §1.2 records the three independent failures of Uhlenbeck's
  structure and refers the ellipticity failure to the audited HF18-A §1.3. The
  difference-quotient mechanism is re-executed from scratch in Theorem 6', localized.
- **C3 (Manfredi–Weitsman).** Not invoked anywhere. `W^{2,2}_loc` for the *shifted*
  equation is neither used nor claimed.
- **C4 (nonlinear Hodge, degenerate case `k = 0`, `q = 1/2`).** Inherited from the parent
  review unchanged (§1.3). Not cited past; §2 gives a structural result about `{w = 0}`
  (Theorem 2), which is not the regularity theorem the degenerate case would need. §1.1
  adds a sharper placement: the object is Stern's `β_∞`, for which the source states no
  regularity.
- **C5 (scaling).** Under `S_λ : u ↦ λu(λ·)`: `Q ↦ Q`, `‖∇V‖_2 ↦ λ‖∇V‖_2`,
  `D_3 ↦ λ^2 D_3`, `ω ↦ λ^2 ω(λ·)`, `w ↦ λ w(λ·)`, `|w|^{-1} ↦ λ^{-1}|w|^{-1}(λ·)`.
  Theorem 5: both sides of (5.1) scale as `(a, λ^{-1}·λ^2·λ^{-1}) = (a, λ^0)` after the
  ball radius is carried through as `r ↦ r/λ` — the radius appears explicitly on the right
  of (5.1), so no radius-free constant is claimed. Theorem 4: `S(E)` and
  `∫_E|∇w|` both carry `(a^{1/2}·a^{1/2}, λ^{-1})` on `E ↦ λ^{-1}E`, consistent with
  `‖∇w‖_{L^1(B_R)} ↦ λ^{-1}‖∇w‖_{L^1(B_{λR})}`. Theorem 6' carries `‖∇ζ‖_∞ ≍ r^{-1}`
  explicitly. Theorem 2 is scale-covariant by construction (`d^{-1/2}` on both sides).
- **C6 (boundary terms at infinity).** Theorem 3 and Theorem 6' are local with explicit
  cutoffs and no limit `R → ∞` is taken. Theorem 5 is proved on a fixed cylinder. Theorem 1
  is distributional. Nowhere is an unjustified global integration by parts performed.
- **C7 (scope ceiling).** Acknowledged and respected: granted in full, (H1) promotes
  exactly HF18-A Proposition 3' and gives `∇w` as a genuine object. **It supplies no
  time-integrated absorption and does not touch the first gap.** Nothing in this note
  claims otherwise; §9 restates this as a non-claim, and §10 restates the first gap
  unchanged.

---

## 9. Self-check against the packet falsifiers

- *A bound that uses the norm it must control*: none. Theorems 1–6' involve only
  `‖∇u‖_∞`, `‖w‖_3`, `‖∇V‖_2`, `‖q‖_3` and geometric quantities, and none of them is
  offered as a bound on the transport term or on any critical norm.
- *Scaling-inconsistent absorption*: no absorption is performed anywhere. C5 records the
  exponents of every displayed inequality.
- *Hidden smallness*: none. No smallness hypothesis appears in any statement.
- *Differentiating the merely-`L^3` minimizer*: never. Derivatives are taken of `V ∈ H^1`
  (audited), of `A = Φ(V) ∈ W^{1,3/2}` (audited), of `φ` only as a distribution
  (Theorem 3), and of `w` only where it is `C^1` because `A` is `C^1` and nonzero
  (Theorem 2, Proposition 4.4) or under (H1) by hypothesis. Theorem 6' differentiates
  nothing: it uses difference quotients and passes to the limit in `L^2`/`L^3_loc`.
- *An instantaneous fact promoted to a time-integrated one*: the whole note is at one
  fixed time and says so in §0; no time integral appears.
- *A `p`-Laplace or nonlinear-Hodge theorem applied outside its structure hypotheses*:
  none applied. §1 records the exact hypotheses of Uhlenbeck, Sibner–Sibner,
  Iwaniec–Scott–Stroffolini, Stern and Otway and why each fails or is silent.
- *A forced, periodic, hyperdissipative or Euler substitute*: none; unforced `R^3`
  throughout, and no evolution equation is used at all.
- *Forbidden inferences*: no size bound in `Q` and `D_3` is proposed; energy is never
  claimed to control anything critical; no equivalent identity is claimed to discharge
  the gap.
- *Unaudited material*: the three HF19 notes and `hf20-harmonic-strain-test.md` are not
  used, not cited as motivation, and no statement here depends on them.

---

## 10. Frontier record

**MODE / RESULT.** DISCOVER with a falsifier arm. **(H1) is not decided.** Positive arm:
Uhlenbeck's *theorem* is inapplicable for three displayed reasons and Uhlenbeck's
*mechanism*, localized, yields a genuine Caccioppoli inequality (Theorem 6') from which
Gehring provably cannot be started (O1–O2) and which, even if it could, would not suffice
(O3). Negative arm: no counterexample; instead a rigidity theorem (Theorem 2) that vetoes
the linear-zero mechanism used by every construction in the programme, verified on the
HF18-B family by explicit computation (Corollary 2.1). Net: the question is reshaped —
Theorem 1 discharges the skew half of `∇w`, Theorem 3 reduces (H1) to a scalar
distributional statement, Theorem 4 replaces the standard obstacle by a sharp criterion,
Proposition 4.4 shows the standard obstacle was not necessary, and Theorem 5 supplies the
first quantitative lower bound on `|w|` in the programme.

**CLAIM AND SCOPE.** All claims are at one fixed time of a classical solution with
`u ∈ H^m(R^3;R^3)`, `m >= 4`, `div u = 0`, unless narrower.
1. (Theorem 1) `curl w = curl u ∈ H^{m-1} ⊂ C^{1,1/2}` in `D'`; (H1) is a statement about
   `sym(∇w)` only; if `|{w = 0} ∩ {ω ≠ 0}| > 0` then (H1) is false; (H1) holds on every
   open set where `ess inf|w| > 0`.
2. (Theorem 2) If a solenoidal `A ∈ C^1` has a zero with `DA ≠ 0`, then
   `|sk(∇(|A|^{-1/2}A))| >= c_0 d^{-1/2}` on an open cone, so the associated datum is not
   in `H^s_loc` for `s > 5/2`. Scope: `A` of class `C^1` near the zero; no global
   hypothesis. (Corollary 2.1) Every field of the HF18-B witness family, bulk and
   oscillation, is inadmissible in this sense — a statement about reusability of that
   family for the (H1) question, **not** about HF18-B's own conclusions on the class `M`.
3. (Theorem 3) For `1 < p < ∞`, `w ∈ W^{1,p}_loc ⟺ div w ∈ L^p_loc` (distributional
   `div w`); (H1) follows from `div w ∈ L^p_loc` for a single `p > 1`.
   (Corollary 3.3) (H1) ∧ (H2) ⟺ `div w ∈ L^{3/2}(R^3)`.
4. (Theorem 4) `w ∈ W^{1,1}(E)` whenever `Σ_j 2^{(j+1)/2}|E_j|^{1/2}‖∇V‖_{L^2(E_j)} < ∞`;
   this is implied by `|w|^{-1} ∈ L^1(E)` and is sharp in the sense of 4(b);
   `∇V ∈ L^p` plus `|w|^{-p'/2} ∈ L^1` suffices for every `p ∈ [2,∞]`.
   (Proposition 4.4) There is a genuine element of `M`, certified minimal against all of
   `G_3` by the audited (B1), with `∫_B|w|^{-1} = ∞`, `w ∈ C^∞(B)`, `u ∈ C^∞(B)`,
   `curl u = e_3 ≠ 0` — so `|w|^{-1} ∈ L^1_loc` is **not necessary** for (H1).
   Scope: `u` smooth on `B`, not claimed globally `H^m`.
5. (Theorem 5) `⨍_{B_r(x_0)}|w| >= (r/32)·max_n inf_{B_r}(ω·n)` for every `w ∈ L^3` with
   continuous `curl w = ω`; hence `|w|` vanishes at most to first order at points of
   `{ω ≠ 0}`. (Theorem 6) At a power-law zero on a `C^1` set of codimension `1` or `2`
   inside `{ω ≠ 0}`, the exponent satisfies `β ≤ 1`, `β = 1/2` is excluded in the `C^1`
   model, and (H1) holds locally.
6. (Theorem 6') Local Caccioppoli (6.1) with explicit constants `81/2` and `162`.
7. (§1.1) Our `w` is exactly the canonical `p`-coclosed primitive `β_∞` of Stern
   Lemma 2.2 [DI]; that paper states no regularity for `β_∞`, and the Uhlenbeck-credited
   smoothness of Prop. 3.1 [DI] is for the closed-and-coclosed forms of Theorem 2.9.

**EVIDENCE.** For 1: (P3) plus Sobolev embedding, and the level-set property of Sobolev
functions. For 2: the exact derivative `Df(z) = |z|^{-1/2}(I − (1/2)ẑ⊗ẑ)`, the
homogenized identity `2Lx − L^Tx = (x·Lx)x/|x|^2` and its real-analytic continuation from
an open cone, and `tr L = 0`; cross-checked numerically over 200 random traceless `L`
(min over `L` of `max_θ|M| = 0.532`). For Corollary 2.1: the closed-form
`(curl G)_3 = 4ρ^{-1/2} − (1/2)ρ^{-5/2}(a^2 + 27b^2)`, equal to `(7/2)|a|^{-1/2}` on
`b = 0`, confirmed by centred differences at `a = 10^{-2}, 10^{-3}, 10^{-4}` to four
figures; and `ρ^{-1}∂_ρ(ρ^{3/2}) = (3/2)ρ^{-1/2}` for the azimuthal bulk. For 3:
Newtonian-potential localization, the Calderón–Zygmund theorem on `1 < p < ∞`, Weyl's
lemma, and interior estimates for harmonic functions. For 4: Cauchy–Schwarz layer by
layer, `(ℓ^2)^* = ℓ^2` for sharpness, the `τ`-regularized chain rule for `Ψ_τ(V)`, and
direct computation on (4.3) certified minimal by the audited (B1). For 5: Stokes' theorem
on discs for the mollification `ρ_ε * w`, cylindrical coordinates, and uniform convergence
of `ρ_ε * ω`. For 6': the audited (A5) inequalities, translation invariance of `G_3`,
(P2) for admissibility of `ψ = ζ^2(D_hφ − c)`, and `L^2`/`L^3_loc` convergence of the
difference quotients.

**FIRST GAP.** Unchanged, and untouched by this lane. An input-only spacetime bound
`∫_0^τ K dt ≤ θ ν ∫_0^τ D_3(w) dt + M ∫_0^τ Q dt + A_input`, uniformly for
`τ < min(H, T_*)`, `θ ≤ 1`, with `A_input` depending only on `u_0, ν, H` — or the
pressure-route analogue. By check C7, (H1) is not this gap and would not close it: it
promotes exactly HF18-A Proposition 3'.

**SURVIVING CONDITIONAL SUFFIX.** The HF18 suffix, unchanged and neither extended nor
reduced: at every fixed time of a classical `H^m` solution, `m >= 4`, divergence-free on
`R^3`, with no smallness — `V = |w|^{1/2}w ∈ H^1`, `A = |w|w ∈ W^{1,3/2}` with `div A = 0`,
`w ∈ L^3 ∩ L^9 ∩ B^{2/3}_{3,∞}`,
`D_Q(u) = D_3(w) = ∫(|∇V|^2 − (1/9)|∇|V||^2) >= c‖u‖_9^3`, the transport forms
(F2), (F5), (F6), (F7), and on every compact classical interval `Q' + ν D_3(w) = K` with
`|K| ≤ C_* Q^{1/3} D_3(w)`; (F3)–(F4) under (H1) only. Hence, if the first gap is ever
closed with `θ ≤ 1` and input-only `A_input`, then
`Q(τ) + (1−θ)ν∫_0^τ D_3 dt ≤ Q(0) + A_input`, giving `sup_t‖u‖_3` and `u ∈ L^3_t L^9_x`
up to `min(H, T_*)`, hence continuation by the imported ESS node. **New conditional
suffixes added by this note, both strictly inside the (H1) question:** if
`div w ∈ L^p_loc` for one `p > 1` then (H1) and hence HF18-A Proposition 3' hold; and if
the level-set sum (4.2) is finite on every bounded set then (H1) holds.

**NON-CLAIMS.** No proof of (H1); no disproof of (H1); no proof that (H1) is unprovable.
No `C^{1,α}`, `C^0`, `L^∞_loc`, `W^{2,2}_loc` or `W^{1,p}_loc` regularity of `w`, `q` or
`φ` is established. No higher integrability of `∇V` is established — Theorem 6' is a
Caccioppoli inequality only, and §6.2 states why it does not iterate. No counterexample to
(H1) is constructed, and the existence of an admissible global example with a nonempty
zero set is left open. Theorem 5 does not control `|{|w| < λ}|` at a rate, and the
shortfall is quantified. Corollary 2.1 is a statement about the reusability of the HF18-B
family for the (H1) question and is **not** a re-audit of, nor a correction to, HF18-B
Prop. 2.2, whose conclusions on the class `M` are untouched; whether that classification
changes on the admissible subclass is not examined here. Proposition 4.4 does not exhibit
a globally `H^m` datum. No bound on the transport term `K`, no time-integrated absorption,
no HIGH-STRAIN and no HIGH-PRESSURE result, no continuation theorem for arbitrary data,
no Millennium claim. No novelty claim for anything: the variational mechanism is
nonlinear Hodge theory (Sibner–Sibner, Scott, Iwaniec–Scott–Stroffolini, Stern), the
difference-quotient mechanism is Bojarski–Iwaniec, and the Calderón–Zygmund and Stokes
inputs of §§3, 5 are classical. Uhlenbeck, Sibner–Sibner, Iwaniec–Scott–Stroffolini,
Manfredi–Weitsman, Stein's `L\log L` endpoint and the CZ weak-type estimate are cited
metadata-only and none is load-bearing. The three HF19 notes and HF20 are unused.

**NEXT DISTINCT ACTION.** Decide the joint satisfiability of constraints 3 and 5 of §7 by
attacking the scalar question directly: **is `div w` (the distribution `Δφ`) locally a
function of class `L^p` for some `p > 1`, for admissible data?** By Theorem 3 that settles
(H1) affirmatively; by Theorem 4(b) a counterexample needs `Σ_j 2^j|E_j| = ∞` together
with an adversarial allocation of the Dirichlet budget. Two concrete sub-actions, in
order: (i) construct, or prove impossible, a **globally admissible** minimizer with a
nonempty zero set — Proposition 4.4 gives the local model (`|w| ≍ d` on a hyperplane,
`A` vanishing to second order) and Theorem 2 says every zero of `A` in the construction
must be degenerate, so the question is whether a compactly supported solenoidal
`A ∈ L^{3/2}` can have *only* degenerate zeros; (ii) test whether the weighted bound
`∫|w|σ^2 ≤ D_3/2`, restricted to the admissible class, upgrades to `div w ∈ L^p_loc`,
`p > 1`, using Theorem 5 as the lower bound on the weight — this is the one place where
the two new tools of this note meet, and it is not attempted here.

---

## 11. Sources

**Directly inspected [DI] this session:**
- M. A. Stern, *L_p-cohomology and the geometry of p-harmonic forms*, arXiv:2403.19481v2
  (28 Mar 2024, rev. 2 Sep 2024), HTML full text: space definitions `C_p^k`, `B_p^k`,
  `Z_p^k`; Lemma 2.2 (canonical `p`-coclosed primitive, quoted verbatim in §1.1);
  Theorem 2.9 (Nonlinear Hodge Theorem, quoted verbatim); Proposition 3.1 context
  (Uhlenbeck's Bochner formula; smoothness where the `p`-harmonic form is nonzero,
  Hölder only at its zeros); complete Riemannian manifolds, `R^n` included; **explicitly
  confirmed: no regularity statement for `β_∞`**.
- Repository files at HEAD `30d715d`: `PLAN.md` (sections named in the header);
  `research/evidence/hf17-quotient-functional.md`, `hf17-quotient-evolution.md`;
  `hf18-hodge-regularity.md` (§0 imports, §1.1–1.6 including (1.1)–(1.12), §2 Theorem 2,
  §3 Propositions 3 and 3', §4, §5, §7); `hf18-review-hodge-regularity.md`;
  `hf18-divergence-speed-link.md` (§0, §1.1–1.5 including Prop. 1.1, Remark 1.2,
  Prop. 1.4, Lemma A; §2.1–2.4 including Prop. 2.2 and Lemma B);
  `hf19-review-shifted-hodge-regularity.md` (§§1–5 and the full audit record).
- `/home/ert/proj/navier-paper/main.tex`, `sec:quotient`: `rem:quotient-related`,
  `subsec:quotient-conventions` (F1)–(F5), `def:quotient`, `lem:cubic-pointwise`,
  `lem:cubic-frechet`, `lem:density`, `lem:quotient-minimizer`, `lem:gradient-closure`,
  `lem:leray`, `lem:quotient-coercive`, `def:qe-dissipation`, `prop:quotient-evolution`,
  `hyp:highstrain`.

**Directly inspected in a named prior wave [DI, prior], inherited, not re-fetched:**
- P. Lindqvist, *Notes on the p-Laplace equation*, §4 Thm. 4.1, p. 28, §10 (I), (V), (VI)
  — inherited through the audited (A5) of HF18-A.
- T. H. Otway, arXiv:math-ph/9806007 — inherited through
  `hf19-review-shifted-hodge-regularity.md` §4 (structure condition, uniform ellipticity
  only for `k > 0`, specialisation `q = 1/2`, `k = 0`).

**Metadata only [MO], none load-bearing:**
- K. Uhlenbeck, *Regularity for a class of non-linear elliptic systems*, Acta Math. **138**
  (1977) 219–240 (Project Euclid record; the "Uhlenbeck structure"
  `−div(a(|∇U|)∇U) = f` and the `C^{1,α}` conclusion for `a(t) = t^{p-2}` are reported
  from secondary literature located this session, not from the paper).
- L. M. Sibner, R. J. Sibner, *A non-linear Hodge–de Rham theorem*, Acta Math. **125**
  (1970) 57–73 (Project Euclid record; the hypotheses used in §1.3 are the manuscript's
  own directly-inspected characterization at `rem:quotient-related`).
- T. Iwaniec, C. Scott, B. Stroffolini, *Nonlinear Hodge theory on manifolds with
  boundary*, Ann. Mat. Pura Appl. (4) **177** (1999) 37–115 (bibliographic record).
- M. Giaquinta, *Multiple Integrals in the Calculus of Variations and Nonlinear Elliptic
  Systems*, Ann. of Math. Studies 105, Princeton 1983, Ch. V (Gehring's lemma).
- E. M. Stein, endpoint `L\log L → L^1_loc` bound for Calderón–Zygmund operators, and the
  weak-type `(1,1)` estimate (both quoted in Theorem 3(d) as asides).
- J. Manfredi, A. Weitsman, Comm. PDE **13** (1988) 651–668 — named only to record that
  it is **not** invoked (check C3).

**Bounded numerical cross-checks (not part of any proof):** scratchpad `chk.py` —
(i) 200 random traceless normalized `L`, 2000 directions each with `|Lθ| > 0.3`: minimum
over `L` of `max_θ|M(θ)|` equal to `0.532`, no `L` with `M ≡ 0`; (ii) centred differences
of `(curl G)_3` for `G = ρ^{-1/2}(−3b, a, 0)` at `b = 0`, `a = 10^{-2}, 10^{-3}, 10^{-4}`:
`35.0000, 110.6795, 349.9332` against the closed form `3.5 a^{-1/2} =
35.0000, 110.6797, 350.0000`. Declared range: finite sampling and finite differences;
these support but do not prove Theorem 2 and Corollary 2.1, both of which are proved
symbolically above.
