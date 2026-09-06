# Audit of HF22-A: `hf22-dissipation-comparison.md`

Proof audit, 2026-09-06. Owned output file:
`research/evidence/hf22-review-dissipation-comparison.md`. Nothing else in the
repository was edited; nothing was committed or pushed; the manuscript was not
touched and no graph node was promoted.

## Freeze

* Target: `research/evidence/hf22-dissipation-comparison.md`,
  `sha256 = 1ef6b3bf872dd8d5c8879ce7a03c9ac68fba83382eaab3d89b919b66d8870497`,
  700 lines.
* Repository HEAD: `e36fec455e970a004519e5c91b856a3e1bba28bc` (`main`, clean).
* Manuscript: `../navier-paper/main.tex`, HEAD `4084330f`,
  `sha256 = 7a59b9cb3b3178c44da978f403f6397c7c44cd6a863429549b13280dddfe8671`.
* Premises admitted without re-proof, per the audit charter: HF17 functional and
  evolution; HF18-A (Theorem 2, (1.11), `A=|w|w\in W^{1,3/2}`, `V=|w|^{1/2}w\in
  H^1`, `D_Q(u)=D_3(w)`); HF18-B **only** its Prop. 1.4 for *smooth* fields;
  HF19-D as repaired; HF20 as repaired; HF21-A and HF21-B as repaired.
* Explicitly **not** admitted: HF23; and the open (H1)-type regularity
  `w\in W^{1,2}_loc`.

---

## VERDICT

**REPAIR.**

The mathematical core of the note is correct. Every new result of
§§1--4 was reconstructed from its first nontrivial implication and survives:
Lemma 1.1, Props. 1.2--1.3, Lemma 2.3, Prop. 2.4, Cors. 2.5--2.7, Lemmas
3.1--3.2 (within its declared conditional scope), Lemma 3.3, Prop. 3.4,
Cor. 3.5, Lemma 3.6. The negative answer to sub-question (a) stands, the
claimed third derivation of the elliptic-swirl identity is real and reproduces
the audited HF19-D (3.3) *exactly*, the inversion is a bijection onto the
nonlinear-Hodge class as claimed, and the constant `2` in the new
unconditional bound is correct and is the exact extension of the manuscript's
own `\eqref{eq:D3P3-bounds}`.

The first bad bridge is in §5, consequence 2 (= MODE/RESULT item 6, second
half): the claim that the affirmative branch **would not have closed (G)**
because it "would only have moved (G) onto the pressure route". That chain has
two independent defects and, as stated, is a non-sequitur. It is repaired
below at reduced strength; the repair changes no other result, because nothing
in §§1--4 depends on it.

Two further narrowings are required (item 6 first half; Prop. 2.1's
first-order assertion) and four cosmetic fixes are listed.

## REVIEWED SCOPE

Full note, §0 through §6, all statements. Reconstructed independently rather
than read: Lemma 1.1 (four forms of `D_3`); Prop. 1.3 (the equality set);
Lemma 2.3 (`\partial_s h = 2|v|N(v)`) including the general non-`M` form;
Prop. 2.4 (1)--(3) by a route different from the note's (`\Lap m=-\curl\curl m`
in the parallel-curve chart, then the frame divergence); Cor. 2.5 against
HF19-D (3.3) verbatim; Cor. 2.6; Lemma 3.1; Lemma 3.2 (master formula, both
integrations by parts, the nonlinear-Hodge cancellation, and the `L^2`
analogy); Lemma 3.3; Prop. 3.4 (1)--(4) including measurability and
integrability; Cor. 3.5; Lemma 3.6 (pointwise `|\grad A|^2`, the
Cauchy--Schwarz split, the exponent arithmetic `a+(7/9)b\le 2(a-(1/9)b)`, and
the two Hölder steps); §4 (C1)/(C2); §5 all three consequences; §6.
Manuscript objects re-read at the working tree: `def:D3P3`
\eqref{eq:D3-def}/\eqref{eq:D3P3-bounds}, `prop:pressure`
\eqref{eq:pressure-balance}, `hyp:absorption`, `def:quotient`,
`lem:quotient-minimizer`, `lem:gradient-closure`, `lem:leray`,
`lem:quotient-coercive`, `lem:quotient-heat`, `def:qe-dissipation`,
`lem:quotient-heatsign`, `rem:qe-heatsign-scope`, `rem:distance-balance`,
`rem:highstrain-normalisation`, `rem:highstrain-scope`, `rem:no-monotone`.
HF19-D Lemma 3.1, Thm 3.2, Props. 3.3--3.4, Cor. 3.5 re-read at statement
level and their hypotheses checked against the uses made here.

## FIRST BAD BRIDGE

§5, "In (G)", consequence 2, and its headline copy in MODE/RESULT item 6:

> Granting `D_3(w) <= D_3(u)`, (G) reduces to `int ||q||_3 D_3(u) dt <=
> A_input`; but by \eqref{eq:pressure-balance}, `nu int_0^tau D_3(u) dt =
> (1/3)X(0) - (1/3)X(tau) + int_0^tau P_3`, so an input-only bound for
> `int D_3(u)` uniform in `tau` is **exactly** `hyp:absorption` ... The
> affirmative answer would only have moved (G) onto the pressure route.

## EVIDENCE

### (E1) What is right, checked line by line

**Lemma 1.1.** All three pointwise lines recomputed.
`((\grad g)^T g)_k = g_i\partial_k g_i = |g|\partial_k|g|` gives line 1;
squaring `\partial_k(V_g)_i=|g|^{1/2}\partial_kg_i+\tfrac12|g|^{-1/2}(\partial_k|g|)g_i`
gives cross term `|g||\grad|g||^2` and tail `\tfrac14|g||\grad|g||^2`, i.e.
line 2 with the coefficient `5/4`; `|V_g|=|g|^{3/2}` gives
`\tfrac19|\grad|V_g||^2=\tfrac14|g||\grad|g||^2`, line 3. Difference
`=|g|(|\grad g|^2+|\grad|g||^2)` = the `def:D3P3` integrand. Correct, and it
is the pointwise algebra `def:D3P3` actually uses.

**Prop. 1.2, Prop. 1.3.** Correct. HF19-D Lemma 3.1 supplies exactly what
Prop. 1.3 consumes: `s\mapsto\Delta(v_s)\in C^1([0,\infty))` with
`\tfrac{d}{ds}\Delta(v_s)=D_3(w(v_s))-D_3(v_s)` and `\Delta(v_s)\to0`. The
interior-maximum argument is sound in detail: with `\varepsilon=\tfrac12\sup\Delta`
pick `S` with `\Delta<\varepsilon` beyond `S`; the max over `[0,S]` is the
global sup, is `>0`, so it is not at `0`, and continuity at `S` forbids `s^*=S`;
hence `s^*\in(0,S)` and `\tfrac{d}{ds}\Delta(v_{s^*})=0`. The elliptic swirl is
in `C_c^\infty\cap\mathcal M` (HF19-D Prop. 3.4) and leaves `\mathcal M` for
all small `s>0`, so `\Delta(v_0)=0` and `\Delta>0` nearby. The claim
"the equality set strictly contains `\mathcal M`" is therefore **correct**, and
so is the reading that equality is not a defect-detector.

**Lemma 2.3 — verified, including the general form the note does not display.**
`Dj(z)=|z|I+z\otimes z/|z|` is `\grad_z(|z|z)`; `\partial_s j(v_s)|_0
=Dj(v)\Lap v`; `\div` and `\partial_s` commute for Schwartz data. For
solenoidal `v`, `h=v_s\cdot\grad|v_s|^2=2|v_s|\div j(v_s)`, and `v\in\mathcal M`
kills the term where `\partial_s` hits the prefactor. I also expanded `N`
without assuming `v\in\mathcal M`:
```
 N(v) = \grad|v|\cdot\Lap v + (v/|v|)\cdot\grad(v\cdot\Lap v)
        + (v\cdot\Lap v)\,\div(v/|v|),      \div(v/|v|) = -\,v\cdot\grad|v|/|v|^2 ,
```
using `\div\Lap v=\Lap\div v=0`. Hence in general
`2|v|N(v)=\Lap v\cdot\grad|v|^2+2v\cdot\grad(v\cdot\Lap v)+2|v|(v\cdot\Lap v)\div(v/|v|)`,
and the last term vanishes precisely on `\mathcal M`. The first two terms are
**verbatim** HF19-D's `R(u_0)=\Lap u_0\cdot\grad|u_0|^2+2u_0\cdot\grad(u_0\cdot\Lap u_0)`
of (3.3). So Lemma 2.3 is correct and its object is literally HF19-D's.
Numerical corroboration of the general identity (evidence, not proof): random
solenoidal `v=\curl\psi` with Gaussian-modulated polynomial `\psi`, `161^3`
grid on `[-3.5,3.5]^3`, second-order differences, interior slab: relative
residual `8\times10^{-3}` at `h=0.044`, consistent with the fourth-derivative
truncation error.

**Prop. 2.4 — verified by an independent route.** Frame relations
`\partial_n n=0`, `\partial_n\tau=0`, `\partial_\tau n=\kappa\tau`,
`\partial_\tau\tau=-\kappa n`, `\div\tau=0` all correct for the exterior
parallel coordinates of a strictly convex curve. Rather than repeat the note's
direct second differentiation I computed `\Lap m=-\curl\curl m` (legitimate,
`\div m=0`) in the orthogonal chart `(t,d,z)` with `h_t=J=1+\kappa_0d`,
`h_d=h_z=1`, physical components `(A,B,C)` along `(\tau,n,e_3)`:
```
 (\curl F)_\tau=\partial_dC-\partial_zB,\quad
 (\curl F)_n=\partial_zA-J^{-1}\partial_tC,\quad
 (\curl F)_z=J^{-1}(\partial_tB-\partial_d(JA)) .
```
With `F=m=(b,0,0)`: `\curl m=(0,\;b_z,\;-(b_d+\kappa b))`, and then
`\curl\curl m=(\kappa^2b-\Lap b,\;b\kappa_s,\;0)`, i.e.
```
 \Lap m=(\Lap b-b\kappa^2)\,\tau-b\kappa_s\,n ,
```
which is the note's (2) exactly, with `\Lap b=b_{dd}+\kappa b_d+b_{zz}` and
`\kappa_s=J^{-1}\partial_t\kappa`. Then, with `\div(g\tau)=\partial_\tau g` and
`\div(hn)=\partial_nh+\kappa h`, `\partial_n\kappa=-\kappa^2`,
`\partial_d\kappa_s=-3\kappa\kappa_s` (from `\kappa=\kappa_0/J`,
`\kappa_s=\kappa_{0,t}/J^3`, both of which I rederived):
```
 N(m)= (2bb_d\kappa_s-4b^2\kappa\kappa_s) - (2bb_d\kappa_s-3b^2\kappa\kappa_s)
       - b^2\kappa\kappa_s = -2b^2\kappa\kappa_s .
```
Correct. The commutator justification the note gives
(`\partial_n\partial_\tau=\partial_\tau\partial_n-\kappa\partial_\tau`, hence
`\partial_n\kappa_s=\partial_\tau(-\kappa^2)-\kappa\kappa_s=-3\kappa\kappa_s`)
is also correct and follows from `[\partial_d,J^{-1}\partial_t]=-\kappa\partial_\tau`.

**Cor. 2.5 — the constant is reproduced exactly.** `R=2|m|N(m)=-4b^3\kappa\kappa_s`
(see (E3) for the sign bookkeeping), and with `b=\varphi(d)` on the slab,
`\kappa=\kappa_0/J`, `\kappa_s=\kappa_{0,t}/J^3`,
```
 R=-\,4\,\kappa_0\,\kappa_{0,t}\,\varphi(d)^3/J^4 ,
```
which is HF19-D (3.3),
`-4\kappa(t)\kappa_s(t)\varphi(d)^3/(1+\kappa(t)d)^4`, **including the
constant 4 and the power `J^{-4}`**, `\kappa(t),\kappa_s(t)` there being the
base-curve curvature and its arc-length derivative. The claim of a third
independent derivation is upheld, with one qualification recorded in (E4):
it is an independent *computation* of the same quantity by a different route
and frame (divergence of the linearised cubic flux vs. the Fermi-chart
expansion), not an independent proof of a different statement.

**Cor. 2.6.** Correct. For `m=g(r,z)e_\theta`, `\Lap m=(\Lap g-g/r^2)e_\theta`,
`Dj(m)\Lap m=2|g|(\Lap g-g/r^2)e_\theta`, and `\div(Ge_\theta)=r^{-1}\partial_\theta G=0`;
for straight shears `m=b(x_2,x_3)e_1` the flux is `2b(\Lap b)e_1`, again
divergence-free; `\kappa_s=0` kills the class of Prop. 2.4. The identification
of the `rem:no-monotone` swirl as azimuthal, hence degenerate, is right, and
the inference "that is why the refutation needs the *elliptic* swirl" is
legitimate.

**Cor. 2.7.** Correct quotation of HF19-D Cor. 3.5, and the transfer to
"the admissible class" is legitimate: each `G_su_0` is itself Schwartz
solenoidal, hence an admissible datum, so both signs occur at `t=0` of two
genuine classical branches. No instantaneous fact is promoted to a
time-integrated one anywhere in §2; §2.2's explicit refusal to read Thm 2.2 at
a fixed time is correct and is the right discipline.

**Lemma 3.1.** Correct. `\Lap u=-\curl\curl u` for solenoidal `u`; the two
integrations by parts are justified by `j(u)\in W^{1,3/2}` (smooth decaying
`u`) and `A\in W^{1,3/2}` (HF18-A), paired against `\omega\in L^3`.

**Lemma 3.2 (master formula) — verified twice.** By hand:
`|\grad g|^2=\partial_kg_i\partial_ig_k+|\curl g|^2`; the double integration by
parts gives
`\int|g|\partial_kg_i\partial_ig_k=-\int\grad|g|\cdot((g\cdot\grad)g)+\int|g|(\div
g)^2+\int(\div g)(g\cdot\grad|g|)`, the last two from
`-\int|g|g_k\partial_k\div g=\int\div(|g|g)\,\div g`; adding
`\int|g||\grad|g||^2` and using `g\times\curl g=|g|\grad|g|-(g\cdot\grad)g`
gives the display. The nonlinear-Hodge cancellation is
`(\div g)(g\cdot\grad|g|)=-|g|(\div g)^2`. Independent numerical check on a
non-solenoidal Gaussian-modulated field, `181^3` on `[-4,4]^3`:
`def:D3P3` form `26.48343`, master form `26.48216`, `-\langle j(g),\Lap g\rangle`
`26.47991` — agreement to the discretisation error. The `L^2` analogy
`\int|\grad w|^2=\int|\curl u|^2+\int|\div w|^2\ge\int|\grad u|^2` is correct
for decaying fields with `\curl w=\curl u` (Q6).

*Scope respected.* The note's own restriction is honoured throughout: the
difference display of §3.2 is used in **no** claim of the note; it appears only
in §3.2 itself and in SURVIVING CONDITIONAL SUFFIX (i), both explicitly
conditional on `w\in W^{1,2}_{loc}` with `|w|^{1/2}|\grad w|\in L^2`, and §4's
two constants and §5's three consequences use Lemma 3.6 and Prop. 3.4 only. I
found no use of the master formula at the minimizer outside its declared
conditional scope. Under that hypothesis the cancellation is legitimate:
`\div(|w|w)=0` in `\mathcal D'` plus `w\in W^{1,2}_{loc}` yields the product
rule `|w|\div w+w\cdot\grad|w|=0` a.e., so no approximate-gradient statement is
silently upgraded. One unstated step remains inside that conditional: the
identification of `D_3(w):=D_{\mathcal Q}(u)` with the `def:D3P3` integral of
`w` needs the a.e. chain rule `\grad V=|w|^{1/2}\grad w+\tfrac12|w|^{-1/2}(\grad|w|)w`
under the same hypothesis. Routine, but it should be said; see the integration
actions.

**Lemma 3.3.** Correct. For `f\in C_c^\infty`, `\div f\in C_c^\infty` with
vanishing mean, so `\psi=N*\div f` obeys `\psi=O(|x|^{-2})`,
`\grad\psi=O(|x|^{-3})`; the multiplier of `\grad\Delta^{-1}\div` is
`\xi\otimes\xi/|\xi|^2=I-\Pi(\xi)`, so `\grad\psi=(I-\mathbb P)f`. Density plus
boundedness of `\mathbb P` on `L^3` plus closedness of `\mathcal G_3` finishes.
The cutoff estimate is correct (`\|\psi\grad\chi_R\|_3=O(R^{-2})`), and
redundant — see UNNECESSARY DEPENDENCIES.

**Prop. 3.4 (inversion) — correct, including the three points singled out.**
* *Lands exactly on the nonlinear-Hodge class.* `|\Lambda(B)|=|B|^{1/2}` and
  `|\Lambda(B)|\Lambda(B)=B` pointwise, so `\div(|\Lambda(B)|\Lambda(B))=\div
  B=0` in `\mathcal D'`: the image lies in `H`. Conversely for `w\in H`,
  `B:=|w|w\in L^{3/2}` with `\div B=0`, so `H` is exactly the image.
* *The inverse is where claimed.* `\Lambda(|w|w)=\bigl||w|w\bigr|^{-1/2}|w|w
  =|w|^{-1}|w|w=w` off `\{w=0\}` and `0=0` on it; and
  `|\Lambda(B)|\Lambda(B)=B`. Two-sided, so a bijection `S_{3/2}\to H`.
* *Measurability and integrability.* `\Lambda` is continuous on `\R^3`
  (`|\Lambda(z)|=|z|^{1/2}\to0`), hence `\Lambda\circ B` is measurable; and
  `\int|\Lambda(B)|^3=\int|B|^{3/2}`, so `\Lambda` maps `L^{3/2}` into `L^3`
  with `\|\Lambda(B)\|_3^3=\|B\|_{3/2}^{3/2}`, and `w\mapsto|w|w` maps `L^3`
  into `L^{3/2}` likewise. Both are exact, not estimates.
* Part (2) is correct: `\langle j(w),g\rangle=\langle B,g\rangle=0` for
  `g\in\mathcal G_3` (test on `\grad\phi`, extend by `B\in L^{3/2}=(L^3)'` and
  closedness), convexity of `F` gives minimality over `w+\mathcal G_3`,
  `w-u=(I-\mathbb P)w\in\mathcal G_3` gives `w+\mathcal G_3=u+\mathcal G_3`,
  and `lem:quotient-minimizer`(b) gives uniqueness. There is **no circularity**:
  sufficiency of the Euler--Lagrange condition is proved from convexity here,
  it is not quoted from `lem:quotient-minimizer`(c), which is only the
  necessity direction.
* Parts (3), (4) correct. A by-product worth stating explicitly, which the note
  leaves implicit: (2)+(3) prove `H=\{w(u):u\in L^3\ \text{solenoidal}\}` —
  the nonlinear-Hodge class *is* the set of minimizers, not merely contained in
  it.

**Lemma 3.6 — correct, constant `2` confirmed, and it is the stated extension.**
`A=\Lambda_1(V)`, `\Lambda_1(z)=|z|^{1/3}z`, and
`|\grad A|^2=|V|^{2/3}(|\grad V|^2+\tfrac79|\grad|V||^2)=|w|(|\grad V|^2+\tfrac79|\grad|V||^2)`
recomputed: cross term `\tfrac23|V|^{2/3}|\grad|V||^2`, tail
`\tfrac19|V|^{2/3}|\grad|V||^2`, sum `\tfrac79`. Cauchy--Schwarz with the split
`|\grad A|=(|\grad A|/|w|^{1/2})\cdot|w|^{1/2}` is legitimate because
`\grad V=0` a.e. on `\{V=0\}` (Q6, HF21-A Prop. 4.1), so the `0/0` set
contributes nothing. With `a=\int|\grad V|^2`, `b=\int|\grad|V||^2\le a`
pointwise, `a+\tfrac79b\le2(a-\tfrac19b)\iff b\le a` — correct, and the
resulting `D_3(w)^2\le2D_3(w)\int|w||\grad u|^2` gives the bound (trivial when
`D_3(w)=0`). Hölder steps correct; `\|w\|_3\le\|u\|_3` is `q=0` admissibility.
The manuscript's own bound at \eqref{eq:D3P3-bounds} is
`0\le D_3(t)\le2\int|u||\grad u|^2\le2\|u\|_\infty\|\grad u\|_2^2`, so the
claim "the exact extension to the minimizer with the same constant `2`",
coinciding at `w=u`, is **accurate**. The non-producer label is also accurate:
`\|\grad u\|_3` is supercritical for the input data.

**§4.** Correct. (C1) follows from `\int|w||\grad u|^2\le(C/2)D_3(u)` by
Lemma 3.6; `\mathcal M` gives `C\ge1` and nothing more; the note's honesty
about the weakness of the `C=1` refutation (a mean-value existence argument
with no ratio bound) matches HF19-D Cor. 3.5 exactly.

**§5 consequence 1 and 3.** The distance-balance reading is correct and is a
confirmation, not a correction, of `rem:distance-balance` and
`rem:qe-heatsign-scope`, both of which I re-read: neither asserts any
comparison, so nothing in `sec:quotient` is falsified. Consequence 3's list of
what survives is accurate.

### (E2) The bad bridge, in detail

Two independent defects.

**(D1) The dropped factor `\|q\|_3`.** The affirmative branch majorises the
(G)-integrand by `\|q\|_3D_3(u)`, not by `D_3(u)`. The note then argues about
`\int_0^\tau D_3(u)\,dt`. No implication runs either way:

* `\|q(t)\|_3` is **not** input-bounded pointwise in `t`. The audited input
  bound is time-integrated —`\int_0^\tau\|u\|_3^4dt\le3C_S^2\|u_0\|_2^4/(2\nu)`
  by \eqref{eq:L4L3}, hence `\int_0^\tau\mathcal Q\,dt\le` input by
  `rem:highstrain-normalisation` — and gives no bound on `\sup_t\|q(t)\|_3`.
  So a bound on `\int\|q\|_3D_3(u)` does not follow from one on `\int D_3(u)`.
* `\|q(t)\|_3` is not bounded below either (it vanishes on `\mathcal M`), so a
  bound on `\int\|q\|_3D_3(u)` does not imply one on `\int D_3(u)`.
* The note's own §0 scaling table refutes the identification directly:
  `\|q\|_3\sim(a,\lambda^0)`, `D_3\sim(a^3,\lambda^2)`, `dt\sim(a^0,\lambda^{-2})`,
  so `\int\|q\|_3D_3\,dt\sim(a^4,\lambda^0)` while `\int D_3\,dt\sim(a^3,\lambda^0)`.
  The two quantities do not even carry the same amplitude weight; no
  dimensionless comparison between them is admissible. This is the note's own
  falsifier discipline applied to its own §5.

**(D2) "exactly `hyp:absorption`" is not an equivalence of estimates.** One
direction is right: from \eqref{eq:pressure-balance} with `s=0,t=\tau` and
\eqref{eq:absorption},
`(1-\theta)\nu\int_0^\tau D_3\le\tfrac13\|u_0\|_3^3+A(\nu,u_0,H)`, so
`hyp:absorption` (with its `\theta<1`) **does** give an input-only bound for
`\int_0^\tau D_3`. The converse fails as stated: the same identity gives
`\int_0^\tau P_3=\nu\int_0^\tau D_3+\tfrac13X(\tau)-\tfrac13X(0)`, and
recovering \eqref{eq:absorption} needs an input bound on `X(\tau)=\|u(\tau)\|_3^3`,
which the identity does not supply. So "exactly" over-reads a one-way
implication as a biconditional.

**(D3) Non-derivability read as non-production.** Even with (D1) and (D2)
repaired, "the affirmative branch would not have been a producer" does not
follow. What the argument can show is that *one* route from the affirmative
answer — majorise, then bound the velocity-side spacetime dissipation
unconditionally — terminates at a quantity the record does not control. That
is non-derivability by that route, not a proof that no argument starting from
the affirmative answer closes (G). Indeed the affirmative answer combined with
smallness of `\|q\|_3` off a small set is precisely the shape lane (c)
explores, and it is not excluded by anything here. This is the falsifier
"distinguishing non-derivability from falsity", and the note trips it in the
one place where its own §6 discipline paragraph does not look.

**Check against the audited ordering.** The note's appeal to
`rem:highstrain-scope` is *quoted correctly*: that remark does state that
subtracting \eqref{eq:pressure-balance} from the integrated
\eqref{eq:quotient-evolution} shows `hyp:absorption` implies
\eqref{eq:quotient-gap} with `\theta=1` and
`A_{\rm input}=A(\nu,u_0,H)+\tfrac13\|u_0\|_3^3` plus the input quantity of
`rem:highstrain-normalisation`, "so the high-strain hypothesis is not harder
than the high-pressure one". The ordering is therefore as the note says. What
does not follow from that ordering is the *counterfactual*: the ordering says
`hyp:absorption\Rightarrow`(quotient gap); it says nothing about what an
affirmative answer to (a) would or would not reduce (G) to.

### (E3) Refutation attempts that failed (the note survives them)

* **Scaling family against Lemma 3.6.** `D_3(w)` and `\int|w||\grad u|^2` both
  scale `(a^3,\lambda^2)`; the inequality is dimensionless and cannot be broken
  by amplitude or dilation. No absorption is performed, so there is no
  scaling-inconsistent absorption to exploit.
* **Attempt to break Prop. 3.4 at the zero set.** `\Lambda` is continuous but
  not Lipschitz at `0`; I tried to produce `B\in S_{3/2}` with `\Lambda(B)`
  outside `L^3` or with `|\Lambda(B)|\Lambda(B)\ne B` on a positive-measure set.
  Impossible: the two identities are pointwise algebra, valid at every point
  including `B=0` under the stated convention, and the `L^3`/`L^{3/2}`
  correspondence is an exact equality of integrals, not an estimate.
* **Attempt to break injectivity of `B\mapsto\mathbb P\Lambda(B)`.** Would need
  two distinct minimizers of one coset; excluded by
  `lem:quotient-minimizer`(b).
* **Attempt to find a hidden circularity in Prop. 3.4(2).** The suspicious step
  is proving minimality from `\div B=0`. It is proved from convexity of `F`
  directly, and `lem:quotient-minimizer`(c) is used only where it is a
  necessity statement (part (3)). No circularity.
* **Attempt to make the claimed third derivation a rederivation of itself.**
  Checked: the note's route computes `\div(Dj(v)\Lap v)` in the
  Frenet/eikonal frame; HF19-D expands
  `\Lap u_0\cdot\grad|u_0|^2+2u_0\cdot\grad(u_0\cdot\Lap u_0)` in the Fermi
  chart. I verified the algebraic bridge between the two objects myself
  (Lemma 2.3's general form above), so the two computations are genuinely
  different manipulations that meet at the same closed form. It is not a
  circular quotation of (3.3).
* **Attempt to refute Prop. 1.3 by making the interior maximum degenerate.**
  Would require `\Delta(v_s)\equiv0` or `\Delta` not `C^1`; both excluded by
  HF19-D Lemma 3.1 and Prop. 3.4.
* **Attempt to refute the equality-set claim by arguing `v_{s^*}\in\mathcal M`.**
  `\Delta(v_{s^*})>0` and (Q5)'s equality case give `v_{s^*}\notin\mathcal M`
  directly.
* **Numerical falsification attempts.** Master formula (three forms agreeing to
  `5\times10^{-5}` relative) and the general Lemma 2.3 identity (`8\times10^{-3}`
  relative at `h=0.044`, consistent with truncation) both corroborate rather
  than refute. Numerics nominate; they are recorded here as evidence only.

### (E4) Defects requiring narrowing, short of the bad bridge

**(N1) MODE/RESULT item 6, first sentence.** "The negative answer closes the
class of attacks on (G) that replace `D_3(w)` by `D_3(u)` pointwise in time."
True only for the constant-free replacement. §4 of the same note leaves (C1)
(`D_3(w)\le CD_3(u)`, `C<\infty`) explicitly open, and a replacement up to a
constant would serve any of those attacks equally well. The sentence must say
"the `C=1` replacement".

**(N2) Prop. 2.1, the minimality paragraph.** "Minimality supplies
`\mathcal Q(u)-\mathcal Q(G_su)\ge F(w)-F(G_sw)` ... whose two sides agree to
first order in `s`, both equal to `sD_3(w)`." The left side is fine
(`\lim_{s\downarrow0}s^{-1}(\mathcal Q(u)-\mathcal Q(G_su))=-\langle A,\Lap
u\rangle=D_3(w)` by `prop:quotient-derivative` and `lem:heat-generator`). The
right side is **not** justified: it needs the generator limit
`(G_sw-w)/s\to\Lap w` in `L^3`, i.e. `\Lap w\in L^3`, which is the open
regularity. This is a first-order differentiation at the merely-`L^3`
minimizer, exactly the operation the note's §6 says it never performs. It
supports nothing (the paragraph's conclusion — that minimality is neutral —
follows from the left side alone) and must be deleted or replaced by the
one-sided form `\limsup_{s\downarrow0}s^{-1}(F(w)-F(G_sw))\le D_3(w)`.

**(N3) Cor. 3.5, "is equivalent to".** The reformulated question quantifies
over all `B\in S_{3/2}`, whose image `\{\mathbb P\Lambda(B)\}` is *all*
solenoidal `L^3` fields, strictly larger than the smooth solenoidal class of
sub-question (a). The direction the note uses (a smooth counterexample is a
counterexample in the larger class) is valid, so nothing downstream breaks; but
"equivalent" should read "restricts to". The note's own "Scope and cost"
paragraph already says this in different words; the headline should match it.

**(N4) Prop. 2.4(2)--(3) implicitly assume `b>0`.** The displays use `|m|=b`;
with `|m|=|b|` and `\sigma=\operatorname{sign}(b)` one gets
`Dj(m)\Lap m=\sigma[2b(\Lap b-b\kappa^2)\tau-b^2\kappa_sn]` and
`N(m)=-2\sigma b^2\kappa\kappa_s`. Cor. 2.5 is **unaffected**, since
`R=2|m|N(m)=2\sigma b\cdot(-2\sigma b^2\kappa\kappa_s)=-4b^3\kappa\kappa_s`
either way — I checked this because HF19-D's `\varphi\in C_c^\infty((0,\infty))`
is not assumed nonnegative and the orientation `\tau=\pm T` is a free choice.
Add "assume `b\ge0`" or carry `\sigma`.

**(N5) Notation clash in MODE/RESULT item 2.** There (3.3) is quoted as
`R=-4\kappa\kappa_s\varphi^3/J^4`, in HF19-D's base-curve variables, while §2
of the same note uses `\kappa,\kappa_s` for the *level-curve* quantities
`\kappa_0/J` and `\kappa_{0,t}/J^3`. Read with §2's meanings the headline
display is off by `J^{-4}`. Cor. 2.5's display is correct; the headline must
use `\kappa_0,\kappa_{0,t}`.

## REPLACEMENT ARGUMENT

The following replaces §5 consequence 2 and the second half of MODE/RESULT
item 6. It is weaker than what the note claims, and it is proved.

**Lemma R1 (Serrin coercivity of the velocity dissipation; unconditional).**
For every smooth solenoidal `u` in the package (R) at a fixed time,
```
 D_3(u) \ge c\,\|u\|_9^3 ,        c = \tfrac89 S^{-1} ,
```
`S` the Sobolev constant of `\dot H^1(\R^3)\hookrightarrow L^6`.

*Proof.* By Lemma 1.1 with `g=u` and `V_u=|u|^{1/2}u`,
`D_3(u)=\int(|\grad V_u|^2-\tfrac19|\grad|V_u||^2)`. Pointwise
`|\grad|V_u||\le|\grad V_u|`, so `D_3(u)\ge\tfrac89\int|\grad V_u|^2\ge
\tfrac89S^{-1}\|V_u\|_6^2`. Since `|V_u|=|u|^{3/2}`,
`\|V_u\|_6^2=(\int|u|^9)^{1/3}=\|u\|_9^3`. `[]`

(This is the `u`-side analogue of the audited HF18-A bound
`D_{\mathcal Q}(u)=D_3(w)\ge c\|u\|_9^3`; it is proved here directly and is not
quoted from HF18-A, whose statement is about `w`.)

**Proposition R2 (what an input-only bound on `\int D_3(u)` is worth).** Fix
`\nu>0`, a divergence-free Schwartz datum `u_0`, and `0<H<\infty`, and let `u`
be the classical branch of `prop:localtheory`. The following are equivalent.

1. There is a finite `B(\nu,u_0,H)` with
   `\int_0^\tau D_3(u(t))\,dt\le B` for every `0<\tau<\min\{H,T_*\}`.
2. `T_*>H` (the branch survives the horizon).

*Proof.* (1)`\Rightarrow`(2). By Lemma R1, `\int_0^\tau\|u(t)\|_9^3dt\le B/c`
for all `\tau<\min\{H,T_*\}`, i.e. `u\in L^3_tL^9_x` on that interval with
`2/3+3/9=1`: the Ladyzhenskaya--Prodi--Serrin criterion at a subcritical-in-time
exponent pair. With the blow-up characterisation of `prop:localtheory` this
excludes `T_*\le H`. (2)`\Rightarrow`(1). `t\mapsto D_3(t)` is continuous and
bounded on the compact classical interval `[0,H]` by `prop:pressure`(i), so
`B=\int_0^HD_3` is finite. `[]`

**Corollary R3 (the corrected counterfactual).** Suppose, contrary to
Cor. 2.7, that `D_3(w)\le D_3(u)` held at every fixed time on the admissible
class. Then the majorant it supplies for (G) is
`\int_0^\tau\|q(t)\|_3D_3(u(t))\,dt`, and by `lem:quotient-coercive`
`\|q\|_3\le(1+C_{\mathbb P})\|w\|_3\le(1+C_{\mathbb P})\|u\|_3`, so the target
becomes the velocity-side spacetime quantity
`\int_0^\tau\|u\|_3D_3(u)\,dt`. Three things are then true and no more:

1. This is **not** the pressure-route quantity `\int_0^\tau D_3(u)\,dt`. The
   two differ by the factor `\|u(t)\|_3`, which the audited record controls
   only in the time-integrated form \eqref{eq:L4L3}, never pointwise; and they
   carry different amplitude weights, `(a^4,\lambda^0)` against
   `(a^3,\lambda^0)`. Neither bound implies the other.
2. The pressure route does control the second quantity, in one direction only:
   `hyp:absorption` with its `\theta<1` gives
   `(1-\theta)\nu\int_0^\tau D_3\le\tfrac13\|u_0\|_3^3+A(\nu,u_0,H)` through
   \eqref{eq:pressure-balance}. The converse implication does not follow from
   that identity, which also carries `\tfrac13X(\tau)`.
3. By Proposition R2, an input-only bound on `\int_0^\tau D_3(u)` is, *at the
   quantifiers of (G) and of `hyp:absorption`*, equivalent to global
   continuation on the horizon — exactly the status `rem:highstrain-scope`
   records for `hyp:absorption` itself. So the pressure-route quantity is not a
   softer target than (G); it is the same difficulty in different variables.

Consequently the licensed statement is: *the affirmative answer to (a) would
have replaced (G) by a velocity-side spacetime quantity of the same difficulty
class as the pressure route's, and would therefore not by itself have been a
shortcut.* It is **not** licensed to say that the affirmative branch "would not
have been a producer": that would require excluding every argument from the
affirmative answer, and the obvious surviving one — combining it with smallness
of `\|q\|_3` off a small set, i.e. the shape of lane (c) — is not excluded by
anything in this note or in the audited record.

## CONDITIONAL SUFFIX THAT SURVIVES

Everything in §§0--4 survives unconditionally within its stated classes, plus
§5 consequences 1 and 3, plus §5 consequence 2 in the repaired form R1--R3.
Explicitly:

* **The answer to (a) is NO**, in both directions, on smooth solenoidal fields
  and hence on admissible data. `D_3(w)-D_3(u)` has no sign; the last term of
  `rem:distance-balance` may not be dropped or one-sided. Confirms the
  manuscript; licenses no manuscript correction.
* **Third derivation of HF19-D (3.3)** via `N(v)=\div(Dj(v)\Lap v)`, with
  `N(m)=-2b^2\kappa\kappa_s` on the elliptic-swirl class and
  `R=-4\kappa_0\kappa_{0,t}\varphi^3/J^4`, matching the audited identity
  including the constant. Independently reproduced in this audit by a fourth
  route (`\Lap m=-\curl\curl m` in the parallel-curve chart).
* **Prop. 1.3**: the equality set of the two dissipations strictly contains
  `\mathcal M`; equality is not a defect-detector.
* **Prop. 3.4 / Cor. 3.5**: `\Lambda(B)=|B|^{-1/2}B` is a bijection
  `S_{3/2}\to H=\{w\in L^3:\div(|w|w)=0\}` with inverse `w\mapsto|w|w`, and
  `\mathbb P\Lambda` a bijection onto the solenoidal `L^3` fields; hence
  `H` is exactly the set of cubic minimizers, and every admissible pair
  `(u,w,q,A)` is an explicit algebraic-plus-Leray function of a free solenoidal
  `B\in L^{3/2}`. Cor. 3.5's reformulation *restricts to* sub-question (a)
  (N3), and the parametrisation does not preserve regularity — as the note
  already says.
* **Lemma 3.6**: `D_3(w)\le2\int|w||\grad u|^2\le2\|w\|_3\|\grad u\|_3^2\le
  2\|u\|_3\|\grad u\|_3^2`, unconditional (no (H1)), scaling-consistent, the
  exact extension of \eqref{eq:D3P3-bounds} to the minimizer with the same
  constant, and a non-producer. With it, (C1) is *equivalent* to the weighted
  substitution inequality `\int|w||\grad u|^2\le C'D_3(u)` up to the factor 2.
* **Conditional, and unused:** the master formula applied to `w`. If
  `w\in W^{1,2}_{loc}` with `|w|^{1/2}|\grad w|\in L^2`, then the two
  divergence terms cancel exactly and
  `D_3(u)-D_3(w)=\int(|u|-|w|)|\omega|^2+\int[\grad|u|\cdot(u\times\omega)-\grad|w|\cdot(w\times\omega)]`
  with the common `\omega=\curl u=\curl w`. HF23, if it stands, would discharge
  this hypothesis; HF23 is not admitted here.

## UNNECESSARY DEPENDENCIES

* **Lemma 3.3 does not need its cutoff argument.** `lem:gradient-closure` in
  the manuscript (`main.tex` l.5222) already states: `\psi\in L^3` with
  `\grad\psi\in L^3` implies `\grad\psi\in\mathcal G_3`. The multipole decay
  `\psi=O(|x|^{-2})` gives `\psi\in L^3` and `\grad\psi=O(|x|^{-3})\in L^3`, so
  the cited lemma finishes at once. Half a proof can be deleted.
* **Lemma 3.6 does not need the exact pointwise `|\grad A|^2`.** The audited
  HF18-A (1.11) `|\grad A|\le\tfrac43|w|^{1/2}|\grad V|` plus
  `\int|\grad V|^2\le\tfrac98D_3(w)` (from `D_3(w)=a-\tfrac19b\ge\tfrac89a`)
  gives, by the same Cauchy--Schwarz split,
  `D_3(w)\le\tfrac{16}9\cdot\tfrac98\int|w||\grad u|^2=2\int|w||\grad u|^2` —
  **the same constant 2**, with no new chain rule. The `[MO]` Lipschitz-
  truncation remark is also unnecessary: HF18-A already proves
  `A=\Phi(V)\in W^{1,1}_{loc}` with `\grad A=D\Phi(V)\grad V` a.e., and
  `D_{\mathcal Q}(u)=\int\grad A:\grad u` is HF18-A Theorem 2 (2.2), so the
  integration by parts need not be redone either.
* **Prop. 2.1** is a restatement of HF19-D Lemma 3.1 and carries no new content;
  its second sentence is (N2) and should go.
* HF18-B is cited five times but is load-bearing only through its Prop. 1.4 for
  *smooth* fields, where `\div(|v|v)=|v|\div v+v\cdot\grad|v|` is elementary
  calculus. None of HF18-B's open items (weighted Calderón--Zygmund, the `L^2`
  projection bound, the a.e. approximate-gradient divergence relation) is used
  as a premise. This is correct practice and worth recording.

## NON-CLAIMS

This audit does not prove or disprove (G), `hyp:highstrain`,
`hyp:highpressure`, `hyp:absorption`, or NS-R3, and asserts no regularity of
the minimizer. It does not decide (C1) or (C2). It does not audit HF23 and does
not use it. It licenses no manuscript edit; in particular the one-sentence
addition to `rem:qe-heatsign-scope` that the note offers should, if the
controller wants it at all, say only that no comparison with constant `1` holds
in either direction, since (C1)/(C2) with `C>1` are open. Proposition R2's
(1)`\Rightarrow`(2) direction uses the Ladyzhenskaya--Prodi--Serrin criterion
as an external classical input; it is standard, but it is external and is
flagged as such. The numerics in this audit are corroboration, never proof. No
novelty or priority is claimed for anything above.

## REOPENING CONDITION

The blacklisted implication is exactly: *"an input-only bound for
`\int_0^\tau D_3(u)\,dt` is what an affirmative sub-question (a) reduces (G) to,
and it is exactly `hyp:absorption`, hence the affirmative branch is not a
producer."* Reopen it only on one of:

1. an input-only pointwise-in-time bound for `\|q(t)\|_3`, or a proof that
   `\int_0^\tau\|q\|_3D_3(u)\,dt` and `\int_0^\tau D_3(u)\,dt` are comparable
   with input-only constants (which would repair (D1) and restore the intended
   reduction); or
2. an estimate-level converse to R3.2, i.e. an input-only bound for
   `X(\tau)=\|u(\tau)\|_3^3` derived from an input-only bound on
   `\int_0^\tau D_3(u)`, which would upgrade R2's quantifier-level equivalence
   to the biconditional the note asserted; or
3. a proof that *no* argument from an affirmative (a) closes (G) — which, given
   that lane (c)'s good-set shape is the obvious surviving candidate, would
   itself be a substantial theorem, not a remark.

Separately, the conditional suffix (the master formula at `w`) reopens
unconditionally the moment HF23, or any other route, is audited to deliver
`w\in W^{1,2}_{loc}` with `|w|^{1/2}|\grad w|\in L^2`.

---

## EXACT EDITS THE CONTROLLER SHOULD MAKE

Target file `research/evidence/hf22-dissipation-comparison.md`, if this verdict
stands. All edits are narrowings or replacements; none removes a surviving
result.

1. **Header status line.** Add, immediately under the title, the line used for
   HF19-D: `**AUDITED: REPAIR** (`hf22-review-dissipation-comparison.md`,
   2026-09-06); repairs below applied.`
2. **§5, "In (G)", consequence 2 — replace entirely** by Lemma R1,
   Proposition R2 and Corollary R3 of this audit, verbatim, together with the
   sentence: *"It is not claimed that no argument from an affirmative (a)
   closes (G); the good-set shape of lane (c) is not excluded."*
3. **MODE/RESULT item 6 — replace** "It also shows the affirmative branch would
   **not** have been a producer: by \eqref{eq:pressure-balance} ... in the other
   order, in `rem:highstrain-scope`." by: *"It also shows the affirmative branch
   would not by itself have been a shortcut: the majorant it supplies is the
   velocity-side spacetime quantity `\int\|u\|_3D_3(u)dt`, which is not the
   pressure-route quantity `\int D_3(u)dt` (different amplitude weight, and
   `\|u\|_3` is input-bounded only in time-integrated form), while an
   input-only bound on `\int D_3(u)dt` is, at these quantifiers, equivalent to
   global continuation — the same status `rem:highstrain-scope` records for
   `hyp:absorption`. Whether some other use of an affirmative (a) would close
   (G) is not decided."*
4. **MODE/RESULT item 6, first sentence, and §5 consequence 1 — narrow**
   "replace `D_3(w)` by `D_3(u)` pointwise in time" to "replace `D_3(w)` by
   `D_3(u)` pointwise in time **with constant `1`**", and append: "the
   replacement up to a finite constant is question (C1) of §4 and remains
   open."
5. **§2.1 — delete** ", whose two sides agree to first order in `s`, both equal
   to `s D_3(w)`" and substitute ". The left side has derivative `D_3(w)` at
   `s=0` (`prop:quotient-derivative`, `lem:heat-generator`); the right side is
   not differentiated, since that would need `\Lap w\in L^3`. Minimality
   produces no comparison with `D_3(u)` at all."
6. **Prop. 2.4 — insert** "and `b\ge0`" into the hypotheses of the statement
   (or carry `\sigma=\operatorname{sign} b` through (2) and (3)); add after (3):
   "`R=2|m|N(m)=-4b^3\kappa\kappa_s` regardless of the sign of `b` and of the
   orientation `\tau=\pm T`."
7. **MODE/RESULT item 2 — fix the notation clash**: write the quoted (3.3) as
   `R=-4\kappa_0\kappa_{0,t}\varphi^3/J^4` and add "(`\kappa_0,\kappa_{0,t}`
   the base-curve quantities of HF19-D; §2 below uses `\kappa,\kappa_s` for the
   level-curve quantities `\kappa_0/J` and `\kappa_{0,t}/J^3`)".
8. **Cor. 3.5 — replace** "is equivalent to" by "restricts to the following
   question over the strictly larger class `S_{3/2}`", and cross-reference the
   existing "Scope and cost" paragraph.
9. **§3.2 Scope — add** one sentence: "Under the same hypothesis the
   identification of `D_3(w):=D_{\mathcal Q}(u)` with the `def:D3P3` integral of
   `w` follows from the a.e. chain rule
   `\grad V=|w|^{1/2}\grad w+\tfrac12|w|^{-1/2}(\grad|w|)w`; this step is part
   of the conditional and is not proved here."
10. **Optional simplifications** (Lemma 3.3 via `lem:gradient-closure`;
    Lemma 3.6 via HF18-A (1.11) and Theorem 2 (2.2), same constant `2`), as in
    UNNECESSARY DEPENDENCIES. If applied, keep the exact pointwise
    `|\grad A|^2=|w|(|\grad V|^2+\tfrac79|\grad|V||^2)` as a displayed remark —
    it is correct and may be wanted later.
11. **`PLAN.md`, "HF22" bullet for sub-question (a) — replace** "It also records
    that the affirmative branch would not have closed (G) anyway, since it would
    only have moved (G) onto the pressure route, which the audited ordering
    already covers." by: "It also records that the affirmative branch would not
    by itself have been a shortcut: it converts (G) into a velocity-side
    spacetime quantity whose input-only control is, at these quantifiers,
    equivalent to global continuation. It does not show that no argument from an
    affirmative (a) closes (G)." Mark the lane **AUDITED: REPAIR, repairs
    applied**.
12. **No manuscript edit.** `rem:distance-balance` and `rem:qe-heatsign-scope`
    are confirmed, not corrected. If the optional sentence in
    `rem:qe-heatsign-scope` is wanted, it must say "no comparison with constant
    `1` holds in either direction" and cite the audited HF19-D witness; it must
    not say the comparison is refuted, since (C1)/(C2) are open.
13. **Graph.** No node promotion. Record the lane's four new results
    (Prop. 1.3, Lemma 2.3 + Prop. 2.4 + Cor. 2.5, Prop. 3.4 + Cor. 3.5,
    Lemma 3.6) as audited-PASS evidence leaves, and record the repaired §5
    consequence 2 as an audited narrowing.
