# HF18 independent audit: Euler-Lagrange structure of the quotient minimizer,
# weighted dissipation identity, transport forms

Frozen input: `research/evidence/hf18-hodge-regularity.md`, SHA-256
`718ed43d1fed1c65dd1c36a11bedd93c22ef98f65e3a53e8ee7273f4c1dcf62b`,
base commit `fd1c20e4ec32d7932bb318836d02b10a073e3500`.
Inputs treated as previously audited: `hf17-quotient-functional.md`,
`hf17-quotient-evolution.md` and their two PASS reviews.
MODE: REVIEW, proof-audit discipline. This audit claims no theorem of its own
beyond the two elementary verifications displayed in R2 and R6.

## VERDICT: PASS

Every claimed result (N1)-(N4), Theorem 1, Corollary 1, Theorem 2,
Proposition 3, Proposition 3' (under its stated hypothesis (H1)), Theorem 4
and Corollary 4 survives the audit with the scope stated in the candidate.
No invalid bridge was found. Two sentences are overstated relative to what is
proved and must be corrected before integration (S1, S2 below); they are
commentary, not load-bearing steps. One citation gains an exact label (S3).

The candidate is the first HF-lane note in this programme that produces a
genuine new *estimate* on the quotient object rather than another identity:
`D_Q(u) = D_3(w)` upgrades HF17's generator sign to a coercive weighted
dissipation, and it is correct.

## 1. What was verified, step by step

### R1. The difference-quotient identity (1.10) and (0.2)

With the candidate's conventions `tau_h f(x) = f(x+h e_k)`,
`D_h f = (tau_h f - f)/h`, one has `D_{-h} g(x) = (g(x) - g(x-h e_k))/h`, and
the change of variables `y = x + h e_k` gives exactly
`int f . D_{-h} g = - int D_h f . g` for `f in L^{3/2}`, `g in L^3`
(absolutely convergent, no boundary term, no decay). (0.2) is correct.

`G_3` is the `L^3`-closure of `grad C_c^infty`; translation is an `L^3`
isometry mapping `grad C_c^infty` onto itself, so it preserves the closure,
hence `D_{-h} D_h q in G_3` for `q in G_3`. Testing (E2) with it and applying
(0.2) once gives

    int D_h A . D_h q = 0,  hence  int D_h A . D_h w = int D_h A . D_h u.   (1.10)

Verified. This is the structural heart of the note and it is right: the
Euler-Lagrange condition holds against the *whole closed* space, so the
Bojarski-Iwaniec test function needs no cutoff, and no derivative of `q` or
`w` is ever formed. The formal identity behind it, `int grad A : grad q = 0`
(from `div A = 0` and `q = grad phi`), is consistent but is not what is used.

### R2. Lemma V (1.6)-(1.8): reproved independently

Put `rho = |z| >= rho' = |z'|`, `s = z.z' in [-rho rho', rho rho']`,
`M = (A(z)-A(z')).(z-z')`, `N = |V(z)-V(z')|^2`, `P = (rho+rho')|z-z'|^2`.
Then `M = rho^3 + rho'^3 - (rho+rho')s`, `N = rho^3 + rho'^3 - 2 sqrt(rho rho') s`,
`P = (rho+rho')(rho^2+rho'^2-2s)`, all affine in `s`, so each linear inequality
among them is decided at the two endpoints. I recomputed both endpoints:

- `s = -rho rho'`: `M - N = rho rho' (sqrt(rho)-sqrt(rho'))^2 >= 0`;
  `M = (rho+rho')(rho^2+rho'^2) <= 4 rho^3 <= 4N`; `P = (rho+rho')^3 <= 8 rho^3 <= 8N`.
- `s = rho rho'`: `M = P = (rho+rho')(rho-rho')^2`, `N = (rho^{3/2}-rho'^{3/2})^2`;
  with `a = sqrt(rho'/rho) in [0,1]`,
  `N/M = (1+a+a^2)^2 / ((1+a^2)(1+a)^2)`. The claim `N <= (9/8)M` reduces to
  `1 + 2a - 6a^2 + 2a^3 + a^4 >= 0`, i.e. `(y+4)(y-2) >= 0` with `y = a + 1/a >= 2`.
  Correct, with equality at `a = 1`. And `M <= N` reduces to `a^2 >= 0`.

So (1.6) `(8/9)N <= M <= 4N` and (1.7) `P <= 8N` hold, and `8/9` is sharp
(attained in the collinear equal-length limit). Independent Monte Carlo
(2x10^6 pairs per family: generic, collinear, near-coincident, one-zero;
`scratchpad/lemmaV.py`) gives `min M/N = 0.888889`, `max M/N = 1.0516`,
`max P/N = 2.0000`, `max |A(z)-A(z')|^2 / ((|z|+|z'|)N) = 1.0000`. The
displayed constants are all valid; `8/9` is sharp, `4` and `8` are not, and
(1.8) holds with the sharp constant `1` in place of `2 sqrt 2` (the note's
`2 sqrt 2` is safe and is what the constants (1.9), (4.2) are built on).

Note that (1.6) with constant `8/9` is *stronger* than the source inequality
the note cross-checks against (Lindqvist (V) gives only `4/9` at `p = 3`); the
improvement is the note's own and is proved correctly. Nothing downstream
depends on the improvement beyond a factor 2 in (1.9).

### R3. Theorem 1 (V in H^1) - verified

From (1.10), (1.6) lower and (1.8):

    (8/9)||D_h V||_2^2 <= int D_h A . D_h w = int D_h A . D_h u
        <= 2 sqrt2 ||D_h V||_2 ( int (|tau_h w| + |w|) |D_h u|^2 )^{1/2}
        <= 2 sqrt2 ||D_h V||_2 (2 ||w||_3 ||D_h u||_3^2)^{1/2}
        <= 4 ||w||_3^{1/2} ||d_k u||_3 ||D_h V||_2,

using Hoelder with exponents 3 and 3/2 and `||D_h u||_3 <= ||d_k u||_3` for
`u in W^{1,3}`. Hence `||D_h V||_2 <= (9/2) ||w||_3^{1/2} ||d_k u||_3`
uniformly in `h`; with `V in L^2` (`||V||_2^2 = ||w||_3^3`) weak `L^2`
compactness gives `d_k V in L^2` with the same bound. (1.9) is correct as
displayed, constant included. No decay of `u` or `w` is used, only (0.1).

### R4. Corollary 1 - verified

(a) `||V||_6^6 = int |w|^9`, so `||V||_6 = ||w||_9^{3/2}`; Sobolev on `R^3`
gives `w in L^9`; `u = P w` on `L^3 cap L^9` by (E3), so `u in L^9`.
(b) `Psi(V) = |V|^{-1/3}V` is positively homogeneous of degree `2/3` and
Lipschitz on the sphere; by homogeneity it suffices to check the Hoelder
bound on the unit ball, where it holds; hence
`|tau_h w - w|^3 <= C|tau_h V - V|^2` and `w in B^{2/3}_{3,infty}`.
(c) `DPhi(V) = |V|^{1/3}(I + (1/3) Vhat ⊗ Vhat)`, `|DPhi| <= (4/3)|V|^{1/3}`;
the mollification argument is correct (`|V|^{1/3} in L^{18}` because
`V in L^6`, product `L^18 . L^2 -> L^{9/5}`).
(d) `|grad A| <= (4/3)|w|^{1/2}|grad V|` and `|| |w|^{1/2} ||_6 = ||w||_3^{1/2}`
give `||grad A||_{3/2} <= (4/3)||w||_3^{1/2}||grad V||_2`. Correct.
(e) The `W^{1,1}_loc` non-claim is correctly isolated.
(f) I reproved the pointwise algebra symbolically:
`DPsi(V) = |V|^{-1/3}(I - (1/3)P)`, `(I + P/3)(I - P/3) = I - P/9` for the rank
one projection `P = Vhat ⊗ Vhat`, so
`d_k A . d_k w = |d_k V|^2 - (1/9)(d_k|V|)^2`, and
`w . d_k A = (4/3) V . d_k V = (2/3) d_k |V|^2`.
Also `|d_k V|^2 = |w||d_k w|^2 + (5/4)|w|(d_k|w|)^2` and
`(1/9)(d_k|V|)^2 = (1/4)|w|(d_k|w|)^2`, whose difference is exactly
`|w||d_k w|^2 + |w|(d_k|w|)^2`. (1.12) and the `D_3` integrand identity are
correct.

### R5. Theorem 2 (D_Q = D_3) - verified, and independently confirmed twice

Step 1: `D_{-h}D_h u -> d_k^2 u` in `L^3` for `u in W^{2,3}`; `A in L^{3/2}`;
(0.2) and (1.10) then give
`- int A . d_k^2 u = lim_h int D_h A . D_h u = lim_h int D_h A . D_h w`,
every equality exact on `R^3`. Step 2: `f_h = D_h A . D_h w >= 0`,
`f_h <= 4|D_h V|^2` by (1.6) upper, and `|D_h V|^2 -> |d_k V|^2` in `L^1`;
a.e. convergence on `{V != 0}` by `C^1`-ness of `Phi, Psi` off the origin, and
on `{V = 0}` by `grad V = 0` a.e. there; generalized dominated convergence
(Vitali) identifies the limit. Since the full limit exists by Step 1 it equals
it. Step 3 (`- int A . Lap u = int grad A : grad u`) is justified by the
displayed cutoff with the annulus term `<= R^{-1}||grad eta||_inf ||A||_{3/2}
||grad u||_{L^3(R<=|x|<=2R)} -> 0`. Step 4 gives (2.3) with the arithmetic
`(4/3)^2 (9/8) = 2`. All correct.

Two independent confirmations of the identity, neither taken from the note:

*(i) An exact family with a computable minimizer.* Let
`u = g(r,z) e_theta` be an axisymmetric pure-swirl field, `g` smooth and
compactly supported away from the axis. Then `|u|u = |g| g e_theta` and the
divergence of any azimuthal, `theta`-independent field vanishes identically,
so `div(|u|u) = 0`; by convexity the Euler-Lagrange condition is sufficient,
hence `q = 0`, `w = u`, `Q(u) = ||u||_3^3/3` exactly. For this family
`- int A . Lap u = - int |g|g (Lap g - g/r^2) dV = 2 int |g| (g_r^2 + g_z^2) dV
+ int |g|^3/r^2 dV`, while `|grad u|^2 = g_r^2 + g_z^2 + g^2/r^2` and
`|grad|u||^2 = g_r^2 + g_z^2` give
`D_3(w) = int |g|(2 g_r^2 + 2 g_z^2 + g^2/r^2) dV`. The two agree exactly, for
signed `g` as well. This also shows the upper bound in HF17 (8) is attained on
a nontrivial class, and (see R9) that `K` vanishes identically there.

*(ii) A direct numerical minimization with q != 0.* On a `48^3` periodic box I
minimized `int |u + grad phi|^3/3` by L-BFGS in the full `48^3`-dimensional
`phi` space for two smooth solenoidal `u` (spectral derivatives; the periodic
problem is used only as a proxy for the *variational* problem, never for the
evolution). Converged Euler-Lagrange residual `max|div A|/max|A| ~ 3x10^{-6}`,
`||q||_3/||w||_3 = 0.167`, `Q = 7.3452 < ||u||_3^3/3 = 7.6947`. Then

    -int A . Lap u = 86.3587,  int grad A : grad u = 86.3587,
    int grad A : grad w = 86.3587,
    int(|w||grad w|^2 + |w||grad|w||^2) = 86.3629,
    int(|grad V|^2 - (1/9)|grad|V||^2) = 86.3580,   ||grad V||_2^2 = 91.6447,

agreeing to 5x10^{-5} relative (discretization), with
`(8/9)||grad V||_2^2 = 81.5 <= D_3 <= 91.6` as (2.1) requires, and
`D_3 = 86.36 <= 2||w||_3||grad u||_3^2 = 161.6` as (2.3) requires. (1.9) holds
in this example with ratio ~0.23 on each `k`. The identity survives a serious
attempt to break it.

### R6. Proposition 3 (transport forms) - verified

(F2): `(u.grad)u = grad(|u|^2/2) + omega x u`; `|u|^2/2 in W^{1,3}(R^3)` under
(0.1), so its gradient lies in `G_3` by (E5) and is annihilated by (E2); the
triple-product rearrangement `A.(u x omega) = u.(omega x A)` is the cyclic
identity. (F5): `A_j u_i d_i u_j = A_j d_i(u_i u_j)` by `div u = 0`, and
`A_j F_{ij} in W^{1,1}(R^3)` with `F = u ⊗ u in W^{1,3}`, `A in W^{1,3/2}`, so
the integration by parts has no boundary term. (F6): the substitution
`u = w - q` plus (1.12) turns the `w` part into `(2/3) int u . grad |V|^2`,
and `|V|^2 = |w|^3 in W^{1,1}(R^3)` (`grad|V|^2 = 2 (grad V)^T V in L^1`), so
(0.3) kills it; (0.3) itself is correct (density of `C_c^infty` in `W^{1,1}`,
`u in L^inf`, `div u = 0`). (F7): the average of (F1) and (F6), with
`u_i d_i A_j + A_i d_i u_j = d_i(u_i A_j + A_i u_j)` a.e. from `div u = 0` and
`div A = 0` a.e.; the projection form uses that a divergence-free `L^{3/2}`
field annihilates `G_3`. The consistency remark (F1) - (F6)
`= int q . curl(A x u) = 0` is correct for the same reason, with
`A x u in W^{1,3/2}`.

Numerically, on the converged `48^3` minimizer above, the seven forms give

    T = -0.04216589,  F1 = -0.04216580,  F2 = -0.04216588,  F5 = -0.04216589,
    F6 = -0.04216560,  F3 = -0.04216567,  F4 = -0.04216596,

agreeing to 6-7 digits. Proposition 3 and (numerically, where `w` happens to
be regular enough) Proposition 3' are confirmed.

### R7. Proposition 3' - correctly quarantined

The hypothesis (H1) `w in W^{1,1}_loc` is stated, used, and not proved; its
consequences are not used in Section 4. Step A's cutoff estimate is correct
(`|q|^2 in L^{3/2}`, `|w|^2 in L^3` on the annulus, factor `R^{-1}`), Step C's
symmetry of `grad q` is legitimate under (H1). The scope sentence "true under
(H1) and false to assert without it" is the right disposition.

### R8. Theorem 4 and Corollary 4 - verified

(4.2): `|K| <= (4/3) int |q||u||w|^{1/2}|grad V|`, Hoelder with `3, 6, 2`
(`1/3+1/6+1/2 = 1`), `|| |u||w|^{1/2} ||_6^6 = int |u|^6|w|^3 <= ||u||_9^6
||w||_9^3` (Hoelder `3/2, 3`), so
`|| |u||w|^{1/2} ||_6 <= ||u||_9 ||w||_9^{1/2} <= C_9 ||w||_9^{3/2} = C_9||V||_6
<= C_9 S ||grad V||_2`; with `||q||_3 <= (1+C_3)||w||_3` and
`||grad V||_2^2 <= (9/8)D_3` this is exactly the boxed constant
`C_* = (3/2) 3^{1/3} (1+C_3) C_9 S`. Verified including every constant.
Scaling: under `S_lambda`, `Q -> Q`, `D_3 -> lambda^2 D_3`, `K -> lambda^2 K`;
under `u -> a u`, `Q -> a^3 Q`, `D_3 -> a^3 D_3`, `K -> a^4 K`. Both checked on
the integral representations; `alpha = 1/3`, `beta = 1` is indeed the only
admissible monomial in `Q` and `D_3`, and (4.2) is scale invariant, so no
scaling-inconsistent absorption occurs. Corollary 4's continuity/first-crossing
argument is valid, and `Q^{1/3} < nu/C_*` is implied by
`||u||_3 < 3^{1/3} nu/C_*` since `Q <= ||u||_3^3/3`. The statement that this
reproduces a classical small-`L^3` result and claims no new regularity is
accurate; the ESS dependence is declared.

### R9. Reviewer observation (not a defect)

On the swirl family of R5(i), and more generally on the set
`{u : div(|u|u) = 0}`, the minimizer is `q = 0` and *every* form of the
transport term vanishes identically: `K = -int q.((u.grad)A) = 0`, so
`Q' = -nu D_3(w)` exactly. `K` is therefore a strictly "off-nonlinear-Hodge"
quantity, vanishing to first order in the distance from `u` to the set of
divergence-free fields with divergence-free `|u|u`. This is the natural place
to look for the cancellation the note's NEXT DISTINCT ACTION asks for, and it
is a sharper starting point than a generic numerical family: in my `48^3`
experiment with `||q||_3/||w||_3 = 0.167` the ratio
`|K|/(Q^{1/3} D_3) = 2.5x10^{-4}` was five orders below `C_*`. That single
observation is not evidence of a mechanism (the ratio is small mainly because
`q` is small), but it does say the saturation test must be run on a family
that drives `||q||_3/||w||_3` towards 1, not on generic smooth fields.

## 2. Scope corrections required before integration

**S1 (statement hygiene, (N2)).** The headline form
`D_3(w) = int(|w||grad w|^2 + |w||grad|w||^2)` presupposes a gradient of `w`
that is only *approximate*; the theorem-grade object is
`int(|grad V|^2 - (1/9)|grad|V||^2)`, and (H1) is explicitly not proved.
Section 2 states the caveat; the summary list (N2) and the author's abstract
drop it, where it reads as `w in W^{1,1}_loc`. Restate (N2) in the `V` form
with the approximate-gradient identity as a parenthetical.

**S2 (overstated sentence, Section 4 item 1).** "any absorption
`|K| <= theta nu D_3 + A` with `theta < 1` requires `C_* ||w||_3 <= theta nu`"
is false as written: with `A > 0` the inequality does not force a pointwise
critical smallness, and the sought estimate is a *spacetime* one with an
input-only remainder, which the instantaneous monomial argument cannot
exclude. What is proved is: (4.2) alone yields such an absorption only when
`C_* ||w||_3 <= theta nu`, and no *size* bound in `Q` and `D_3` can do better
by scaling. Replace "requires" with "is not obtainable from (4.2) alone unless".
The FIRST GAP entry and Section 4 item 3 already state the correct version, so
this is a wording repair, not a change of result. Similarly, "the gap is
equivalent to continuation" is proved only in the direction
gap ==> `L^3_t L^9_x` ==> ESS; the converse is asserted by the packet, not here.

**S3 (citation precision).** The inequality used for (1.8) is Lindqvist
*Notes on the p-Laplace equation*, Section 10, inequality **(VI)** (directly
inspected):
`| |b|^{p-2}b - |a|^{p-2}a | <= (p-1)(|b|^{(p-2)/2} + |a|^{(p-2)/2})
| |b|^{(p-2)/2}b - |a|^{(p-2)/2}a |`, `p >= 2`.
The note quotes the statement correctly but does not give it a label. The two
cross-checks are (I) `<.,.> >= 2^{-1}(|b|^{p-2}+|a|^{p-2})|b-a|^2 >= 2^{2-p}|b-a|^p`
(so `M >= P/2` at `p = 3`; confirmed numerically, `min M/P = 0.5000`) and
(V) `| |b|^{(p-2)/2}b - |a|^{(p-2)/2}a |^2 <= (p^2/4) <.,.>` (so `N <= (9/4)M`
at `p = 3`). Both labels as used in the note are correct. Theorem 4.1
(Bojarski-Iwaniec) reads verbatim: "Let `p >= 2`. If `u` is `p`-harmonic in
`Omega`, then `F in W^{1,2}_loc(Omega)`", `F = |grad u|^{(p-2)/2} grad u`,
with `||DF||_{L^2(G)} <= C(n,p) dist(G, dOmega)^{-1} ||F||_{L^2(Omega)}`; the
`C^{1,alpha}` attribution to Uraltseva 1968 with references [Ur], [Db], [E],
[Uh], [Le2], [To] is on printed page 28 as the note states. The note's use of
Theorem 4.1 as a *mechanism to re-execute*, not as an imported theorem, is the
correct handling: its hypothesis ("u is p-harmonic") is not satisfied by (1.1).

## 3. Refutation attempts and their outcome

1. *Explicit computable minimizer.* Axisymmetric swirl `u = g(r,z) e_theta`:
   `div(|u|u) = 0` identically, so `q = 0` and everything is closed-form.
   Theorem 2 holds as an exact identity on this family (analytic check, R5(i)).
   Not refuted.
2. *Numerical minimizer with `q != 0`.* `48^3` L-BFGS minimization, two fields,
   converged EL residual `3x10^{-6}`: `D_Q`, `int grad A : grad u`,
   `int grad A : grad w`, `D_3(w)`, `D_3(V)` agree to `5x10^{-5}`; the seven
   transport forms agree to 6-7 digits; (1.9), (2.1), (2.3) all hold with
   margin. Not refuted.
3. *Constant-speed / collinear degeneracies in Lemma V.* Dedicated collinear,
   near-coincident and one-zero Monte Carlo families, 2x10^6 samples each:
   `8/9` is attained (sharp), never violated; `4`, `8`, `2 sqrt 2` never
   approached. Not refuted.
4. *Rescaled families.* Both scalings (`S_lambda` and amplitude) applied to
   (1.9), (2.1), (2.3), (4.2) and to `D_Q >= c||u||_9^3`: every displayed
   inequality is scale consistent, and (4.2) is scale invariant, so no hidden
   absorption of a scale factor. Not refuted.
5. *Circularity sweep.* `||grad u||_3` appears only in (1.9) and (2.3), both
   labelled non-input; `||w||_3` in (4.2) is the controlled quantity and is
   labelled as the obstruction; `||u||_inf` and `||u||_9` appear only in the
   explicitly non-closing alternatives of Section 4 item 2. `sup_t ||u||_3`
   appears only inside Corollary 4's hypothesis. No claimed conclusion uses
   the norm it must control. Clean.
6. *Identity mistaken for estimate.* (2.2), (F1)-(F7), (4.1) are identities and
   are labelled as such; the only estimates claimed are (1.9), (1.11), (2.1),
   (2.3), (4.2), and each is proved. (F7) is explicitly flagged as an
   equivalent identity that does not discharge the gap, as PLAN requires.
7. *Missed applicable theorem for the shifted system (1.5).* The note says no
   theorem directly applicable was found. The relevant literature family is
   nonlinear Hodge theory (L. M. and R. J. Sibner; and T. Otway, *An elliptic
   inequality for nonlinear Hodge fields*, arXiv math-ph/9806007, abstract and
   HTML full text fetched), which studies exactly `delta(rho(Q) omega) = 0`
   with a *weakened* irrotationality condition `d omega = u ^ omega`, under
   the structure condition `K^{-1}(Q+k)^q <= rho + 2Q rho' <= K(Q+k)^q`, the
   operator being "uniformly elliptic for `k > 0`". Here `rho(Q) = Q^{1/2}`
   gives `rho + 2Q rho' = 2Q^{1/2}`, i.e. `q = 1/2` and `k = 0`: precisely the
   degenerate boundary case the theory excludes; and our curl condition
   `curl w = curl u` is a prescribed 2-form, not of the multiplicative form
   `u ^ omega` near `{w = 0}`. So the note's conclusion stands, but its
   literature search was incomplete and this family, not the scalar
   `p`-Laplacian papers, is where (H1) should be attacked. Recorded in the
   reopening condition.

## Audit record

**VERDICT:** PASS.

**REVIEWED SCOPE:** `research/evidence/hf18-hodge-regularity.md` in full:
Section 0 imports and (0.2)-(0.3); Section 1 (equation (1.1), structure
conditions, the ellipticity obstruction, Lemma V, Theorem 1, Corollary 1);
Section 2 (Theorem 2, (2.1)-(2.3)); Section 3 (Proposition 3, Proposition 3'
under (H1)); Section 4 (Theorem 4, Corollary 4, the scaling discussion);
Section 5 self-check; Section 7 sources. HF17's minimizer, derivative,
pressure cancellation, heat monotonicity and inner-variation identity are
taken as previously audited input and were not re-audited.

**FIRST BAD BRIDGE:** none in any claimed result. The first sentence that
outruns its proof is Section 4 item 1's "requires `C_* ||w||_3 <= theta nu`"
(correction S2); it is commentary and nothing depends on it.

**EVIDENCE:** (0.2) recomputed; translation invariance of `G_3` and hence
(1.10) re-derived; Lemma V reproved from the endpoint structure of the affine
functions `M, N, P` with the sharp constant `8/9`, and cross-checked against
2x10^6-sample Monte Carlo per degenerate family; Theorem 1's chain
recomputed with all constants; the chain rule, Hoelder exponents, Sobolev
exponents and the mollification convergence classes of Corollary 1
recomputed; Theorem 2's Steps 1-4 recomputed, including the `W^{1,1}(R^3)`
membership of `A_j u_i u_j` and `|V|^2` that removes every boundary term;
the pointwise algebra of (1.12) re-derived from `(I + P/3)(I - P/3) = I - P/9`;
Theorem 2 confirmed exactly in closed form on the axisymmetric swirl family
(where `q = 0` provably) and numerically to `5x10^{-5}` on two converged
`48^3` minimizers with `q != 0`; all seven transport forms confirmed
numerically to 6-7 digits; (4.2)'s Hoelder chain and constant recomputed;
both scalings recomputed on the integral representations. Primary source
directly inspected: P. Lindqvist, *Notes on the p-Laplace equation*
(NTNU PDF, 81 pages), Theorem 4.1 (Bojarski-Iwaniec) verbatim on printed
p. 28-29, the `C^{1,alpha}` attribution on printed p. 28, and Section 10
inequalities (I), (IV), (V), (VI), (VII) verbatim on printed pp. 71-74.
Directly inspected: T. Otway, arXiv math-ph/9806007 (HTML), equations (1)-(3)
and Theorem 1. Metadata-only, not load-bearing anywhere in this audit:
Tolksdorf, DiBenedetto, Lieberman, Ural'tseva, Uhlenbeck, Manfredi-Weitsman,
Kato, Sibner-Sibner, Bojarski-Iwaniec [BI1].

**REPLACEMENT ARGUMENT:** none needed. Two wording repairs (S1, S2) and one
citation label (S3) are recorded above; no lemma is replaced.

**CONDITIONAL SUFFIX THAT SURVIVES:** the full candidate survives. At every
fixed time of a classical `H^m` solution, `m >= 4`, divergence-free on `R^3`,
with no smallness and no decay beyond (0.1): `V = |w|^{1/2} w in H^1(R^3)`
with (1.9); `A = |w|w in W^{1,3/2}(R^3)` with (1.11); `w in L^3 cap L^9 cap
B^{2/3}_{3,infty}`; `D_Q(u) = int grad A : grad u = int(|grad V|^2 -
(1/9)|grad|V||^2)`, with `(8/9)||grad V||_2^2 <= D_Q <= ||grad V||_2^2`,
`D_Q >= (8/(9 S^2 C_9^3))||u||_9^3` and `D_Q <= 2(3Q)^{1/3}||grad u||_3^2`;
the transport forms (F2), (F5), (F6), (F7) and, under (H1) only, (F3)-(F4);
and on every compact classical interval `Q' + nu D_3(w) = K` with
`|K| <= C_* Q^{1/3} D_3(w)`, `C_* = (3/2) 3^{1/3}(1+C_3) C_9 S`. Hence, if the
first gap is ever closed with `theta <= 1` and input-only `A_input`, then
`Q(tau) + (1-theta) nu int_0^tau D_3 <= Q(0) + A_input`, giving
`sup_t ||u||_3` and `u in L^3_t L^9_x` up to `min(H, T*)`, hence continuation
by the imported ESS node. Unchanged from HF17 except that the dissipation is
now explicit and coercive.

**UNNECESSARY DEPENDENCIES:** rapid decay of `u` (only (0.1) is used); any
`C^{1,alpha}`, continuity, local boundedness or `W^{2,2}_loc` theory for the
`p`-Laplacian (correctly not applied); any cutoff in Section 1 or Section 2
(removed by (1.10)); HF17's inner-variation identity (9) for the results of
Section 4, since (F5) and (F6) follow from HF17 (6) alone via
`T = -int A.((u.grad)u)`; the `L^{9/5}` bound for `grad A` (used only in a
non-closing alternative); and Lemma V's improvement from `4/9` to `8/9`, which
only halves the constant in (1.9).

**NON-CLAIMS:** this audit establishes no regularity of `w`, `q` or `phi`
beyond what the candidate proves; no `W^{1,1}_loc`; no validity of (F3)-(F4)
without (H1); no time-integrated absorption of `K`; no input-only bound for
`K`; no HIGH-STRAIN or HIGH-PRESSURE theorem; no continuation theorem for
arbitrary data; no Millennium claim. Corollary 4 is a classical small-data
statement obtained with a stronger tool and depends on the imported ESS node.
The numerical work is bounded evidence on a periodic proxy for the variational
problem only, never for the evolution, at finite resolution; it supports but
does not prove Theorem 2, and it proves nothing about the frontier gap.

**REOPENING CONDITION:** (1) Apply the corrections S1-S3. (2) The gap is
unchanged: an input-only spacetime bound `int_0^tau K <= theta nu int_0^tau
D_3 + A_input`, uniform for `tau < min(H, T*)`. Section 4 shows no size bound
in `Q` and `D_3` can supply it, so a cancellation inside
`K = -int q . ((u.grad)A) = -int q . grad Pi_{u,A}` is required. (3) The two
sharpest next probes suggested by this audit: (a) `K` vanishes identically on
`{u : div(|u|u) = 0}` (R9), so the saturation test of the candidate's NEXT
DISTINCT ACTION must be run on a family driving `||q||_3/||w||_3` towards 1,
not on generic smooth fields; (b) hypothesis (H1) should be attacked through
the nonlinear Hodge literature (Sibner-Sibner; Otway math-ph/9806007) for
`delta(rho(Q) omega) = 0` with prescribed non-zero `d omega`, whose structure
condition degenerates here exactly at `k = 0` - closing that degenerate case,
or showing it cannot be closed, would decide (H1) and promote Proposition 3'.
