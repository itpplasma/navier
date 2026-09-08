# Review of HF23, Scope B: the HF20 reconstruction, the new spacetime obstruction, the stated boundary

Independent proof audit, 2026-09-06. Lens: reconstruct every implication from
the first nontrivial one, recompute every exponent and constant, and try to
refute each new fact. Scope B only: the sections named below. Sections
`sec:regularity` and `sec:mixed` (Theorem `thm:main`, Corollary `cor:sigma`,
Theorem `thm:mixed`) belong to a different lens and are **not** certified here;
where a Scope B statement consumes one of them, this review says so explicitly
and marks the conclusion conditional.

## Freeze

| object | identity |
|---|---|
| research HEAD when the audit began | `928713dcc012adbbea279d681d5298d5a887fcfb` |
| research HEAD when this note was written | `e36fec455e970a004519e5c91b856a3e1bba28bc` (the controller committed the HF22 wave during this audit; it touches nothing in Scope B and the target file's hash is unchanged) |
| target | `research/evidence/hf23-divcurl-continuation.tex`, sha256 `abe74421ef6a8a7bacc108c0c08834e32f2a6116530fceb00368c8e67b129075` (1129 lines, read in full) |
| index note | `research/evidence/hf23-divcurl-continuation.md` |
| manuscript | `../navier-paper/main.tex` at `4084330f6b8130241c7afbde3878861229c4cceb` |
| manuscript revision the candidate pins | `39ccb664bf055fac94b3cfac97bf00a60191373d` |
| research revision the candidate pins | `1014e7e3c33af4a341a5f46156a22b808170257b` |
| audited HF20 record | `research/evidence/hf20-harmonic-strain-test.md` (post-repair) and `hf20-review-harmonic-strain-test.md` |
| audited HF04 record | `research/evidence/hf04-energy-only-spacetime.md`, `hf04-review-spacetime.md` |
| audited HF21-B record | `research/evidence/hf21-crossing-sign-structure.md` (post-repair), Theorem 4.5 |
| audited prior art | `research/evidence/cp01-prior-art-quotient.md`, `cp02-prior-art-related-work.md` |

Pin drift, checked rather than assumed. `git diff 39ccb66..4084330 -- main.tex`
is **additions only** (`rem:highstrain-normalisation`, one sentence in
`rem:highstrain-scope`, `rem:distance-balance`, `rem:no-monotone`). Every
manuscript object the candidate quotes -- `hyp:highstrain`,
`prop:quotient-conditional`, `lem:quotient-lowstrain`, `eq:qe-bernstein`,
`thm:continuation` -- is textually unchanged between the pinned revision and
the current head, so the candidate's quotations are still exact. One added
remark bears on it and is used in §7.3 below.

At `1014e7e`, the research revision the candidate says it read, the repository's
HF20 record still carried the **one-sided** display of Theorem 1.1 and the HF20
audit had not yet been committed (`ba8a033` is later). The candidate therefore
reconstructed HF20 from the frozen PDF without access to the audit. This matters
for finding F1.

## Reviewed scope

`sec:hf20` (Reconstruction and scope review of the attached HF20 proof),
`sec:spacetime` (A further obstruction on actual fixed-viscosity trajectories,
Theorem `thm:spacetime`), `sec:frontier` (The exact remaining estimate and the
full conditional continuation, `eq:bernstein`--`eq:ML`, `eq:quantifiers`,
`eq:remaining-sigma`, Proposition `prop:consumer`, the existential-remainder
subsection), `sec:literature` (all four subsections and the readiness table),
and the Final proof ledger. Preliminaries `lem:min`, `lem:convex`,
`lem:derivative`, `lem:evolution` were reconstructed because Scope B consumes
them. `sec:budget`'s `eq:KY`, `eq:Pi-conditional` and `eq:firstgap` were
recomputed because item (4) is about them; their inputs `thm:main` and
`thm:mixed` were **not** audited here.

## Verdict summary

**No invalid or unsupported bridge was found in Scope B.** Every constant,
exponent, scaling law and quantifier in `sec:hf20`, `sec:spacetime`,
`sec:frontier` and the ledger was recomputed independently and confirmed;
the divergence exponent `b^3`, the interval exponent `b^{-5}`, the low-strain
remainder `O(b^{-2})` and the Bernstein constant `C_B` all reproduce exactly.
Theorem `thm:spacetime` is correct and is **genuinely new relative to the
audited HF20 record**: it supplies precisely the two upgrades the HF20 audit
listed as unsupported by HF20's own argument. The ledger's closing admission is
**exactly right**, and §8.2 below shows it is in fact understated.

Four defects, none of them invalid mathematics, all statement- or
citation-level, are recorded with displayed replacements in §7:

- **R1** the regularity chain behind `lem:evolution` repeats the compressed
  sketch the HF20 audit already ruled a non-proof at this tier, and does not
  carry the audit's citation repair;
- **R2** `sec:literature` rests on three unverifiable external conversation
  reports while the repository's own audited prior-art notes, present in the
  very revision the candidate pins, are never cited, and two located prior-art
  items bearing directly on the div--curl theorem are missing;
- **R3** the HF20 scope paragraph omits the `K` versus `K_L` limitation and the
  qualitative smallness of the certificate, both of which the HF20 audit
  required to be stated wherever the result is recorded;
- **R4** `eq:strainK` is presented as newly unlocked by `thm:main`, but the
  manuscript already owns it unconditionally as `lem:quotient-transport`.

Verdict: **PASS WITH SCOPE (four repairs required before integration).**

---

## 1. Item (1): the HF20 reconstruction against the audited HF20 record

### 1.1 Same construction, same constants

Compared object by object against `hf20-harmonic-strain-test.md` §3--§5 and
against `hf20-review-harmonic-strain-test.md` §2(a)--(k). Identical in every
particular:

| object | HF20 record | HF23 `sec:hf20` |
|---|---|---|
| bump, swirl | `b(t)=e^{-1/(1-t^2)}`, `s(r,z)=b(4r-6)b(2z)`, `U=s e_theta` | identical |
| support | `5/4<=r<=7/4`, `|z|<=1/2` | identical |
| cutoff | `chi=eta(16-|x|^2)/(eta(16-|x|^2)+eta(|x|^2-9))` | identical |
| fields | `a=(yz,-xz,0)`, `phi=(x^2+y^2)/2-z^2`, `h=curl(chi a)`, `g=grad(chi phi)`, `e=h-g` | identical |
| local identities | `h=g=(x,y,-2z)`, `grad h=diag(1,1,-2)`, `U.h=0` | identical (`eq:hlocal`) |
| gain | `C_e=||e||_3^3/3`; `int rho|d|^2<=4C_e|eps|^3`; `||d||_3^3<=6C_e|eps|^3` | identical (`eq:gain`) |
| error | `4 sqrt(C_e)||U||_5^{5/2}|eps|^{3/2}+4C_e||U||_inf|eps|^3` | identical (`eq:N0error`), with the intermediate split displayed |
| coefficient | `c_0=||U||_3^3`, `<A_0,N_0>=0` | identical (`eq:c0`) |
| constant | `C_*=4sqrt(C_e)||U||_5^{5/2}+4C_e||U||_inf+M^2||N_2||_3+L(||N_1||_3+||N_2||_3)` | identical (`eq:Cstar`) |
| threshold | `eps_0=min{1,(c_0/(2max{1,C_*}))^2}` | identical (`eq:epschoice`) |
| amplitude | `b=1+2 nu ||V||_3^2 ||Delta V||_3/(eps c_0)` | identical |
| scaling | `Q->b^3`, `||.||_2^2->b^2 lam^{-1}`, `K->b^4 lam^2`, `D_Q->b^3 lam^2` | identical (`eq:scaling-table`) |
| increase | `lam^2 b^3(bk-nu d)>0` | identical (`eq:increase`) |
| supremum | `(E_V/E)^2 b^7(bk-beta nu d)` | identical (`eq:instant-sup`) |

All four exponents of `eq:scaling-table` and both consequences were recomputed
from `T_lambda v(x)=lambda v(lambda x)` and agree with the HF20 audit §2(h) and
with the manuscript's `lem:quotient-scaling`.

### 1.2 F1: the one-sided-display defect is NOT repeated, and not copied

The HF20 audit's single real defect was that Theorem 1.1 was displayed as
`K(U+eps h)+eps||U||_3^3 <= C_*|eps|^{3/2}`, an upper bound only, which does not
entail `K(U-eps h) >= eps c_0/2` and therefore does not entail Theorem 1.2.

The candidate's `eq:hf20sign` is displayed as

    | K(U + eps h) + eps c_0 |  <=  C_* |eps|^{3/2}      (|eps| <= 1),

i.e. exactly the audit's repaired Theorem 1.1', with the same `C_*`. Its
`eq:twosigns` then states both halves,
`K(U-eps h) >= eps c_0/2 > 0` and `K(U+eps h) <= -eps c_0/2 < 0`. Both follow
from the boxed two-sided display by substituting `eps -> -eps` and using
`C_* eps^{1/2} <= c_0/2` on `eq:epschoice`; recomputed and confirmed.

This is not a copy of the repair. At the research revision the candidate pins
(`1014e7e`) the repository's HF20 note still displayed the one-sided form and
`hf20-review-harmonic-strain-test.md` was not in the tree; the frozen PDF's own
display (2) is one-sided. The candidate reached the two-sided form from the
proof, independently. **This is a blind corroboration of the HF20 audit's
repair R1 and should be recorded as such.**

### 1.3 What the reconstruction adds, and what it drops

Adds: nothing mathematically. It is a faithful reconstruction at the audited
scope, plus the intermediate split in `eq:N0error` that the repository's
condensation had elided (the frozen PDF's (16) has it), plus the two-sided
display. Its own sentence is accurate: "This is a component-by-component
self-review, not a second independent review tier."

Drops three things the HF20 audit produced, all recorded here as repair R3
(§7.3) rather than as errors:

- the audit's **integration action** replacing the §5 regularity sketch by a
  citation of `prop:localtheory`(iii),(iv) and `lem:upgrade`. The candidate
  instead re-asserts the sketch inside `lem:evolution` ("On a compact classical
  interval, `u in C^1_t L^3` ... Moreover `p in W^{1,3}`: this follows from the
  normalized Riesz formula and the high Sobolev bounds") and, in `sec:hf20`,
  writes only "The actual local classical branch exists by Tao's local theory."
  This is the same one-sentence compression of a multi-step manuscript lemma
  that the audit ruled "not a proof at the tier the rest of the note is written
  at". See R1.
- the audit's **Lemma A** (`K(-v)=-K(v)`, `D_Q(-v)=D_Q(v)`), which makes the
  two-sided estimate unnecessary and which demotes "both signs occur" to a
  consequence of `K` not vanishing identically. Not a defect; recorded in
  Unnecessary Dependencies.
- the audit's **non-defect on quantitative usability** (`eps_0 ~ 6e-21` for the
  fields as written). The candidate writes "All norms here involve explicitly
  specified compact smooth fields. No numerical minimization is needed", which
  is true but reads as a usability claim. The manuscript's `rem:no-monotone`
  already says "The certificate is qualitative". See R3.

### 1.4 The HF20 scope paragraph

`sec:hf20`'s closing subsection reproduces the audited non-claims: the
perturbation is a direction in data space, not the time derivative; the family
has `Q(u_0)=b^3 Q(V) -> infinity`; it exhibits no blowup and does not
contradict a whole-datum remainder. All correct.

It **omits** the third of the HF20 audit's three independent reasons why HF20
does not touch `hyp:highstrain`: that the hypothesis concerns `K_L`, not the
full `K`, and that the family `b T_lambda V` does not transfer because the fixed
low-pass is not equivariant under `T_lambda`. The audit asked explicitly that
"this limitation should be stated explicitly wherever the result is recorded".
The candidate closes the gap for its own new theorem in `sec:spacetime`, which
is the honest way to do it, but the HF20 scope paragraph should still carry the
sentence. See R3.

---

## 2. Item (2): Theorem `thm:spacetime`

Reconstructed in full. **Correct.**

### 2.1 The auxiliary family and the common short interval

`v^mu` solves NS at viscosity `mu in (0,1]` from the same fixed datum `V`.
The uniform bound `sup_{0<mu<=1} sup_{0<=s<=T_0} ||v^mu(s)||_{H^6} <= B`
is proved by the standard commutator energy estimate, and the viscous term is
**discarded** rather than divided by, so nothing degenerates as `mu -> 0`. The
commutator bookkeeping was rechecked term by term: in
`[d^alpha, v.grad]v = sum_{0<gamma<=alpha} c (d^gamma v . grad) d^{alpha-gamma}v`
with `|alpha|<=6`, the split at `|gamma|<=4` puts `d^gamma v in L^inf` (needs
`v in H^{|gamma|+2} subset H^6`) against `d^{alpha-gamma} grad v in L^2` of
order `<= |alpha|-|gamma|+1 <= 6`; the split at `|gamma|>=5` puts `d^gamma v in L^2`
against a factor of order `<= |alpha|-|gamma|+1 <= 2` in `L^inf` (needs `H^4`).
Both are available inside `H^6`. Hence `Z' <= C Z^2`, `Z <= 2Z(0)` on `[0,T_0]`
once `C Z(0) T_0 <= 1/4`, and the fixed-`mu` `H^1` blowup alternative upgrades
the a priori bound to existence past `T_0`. Correct.

`||d_s v^mu||_{H^4} <= ||P N(v^mu)||_{H^4} + mu||Delta v^mu||_{H^4} <= C(B^2+B)`
uses `H^6` for the Laplacian, `H^5` for the product, boundedness of the Leray
projection on `H^4`, and `mu <= 1`. Hence `||v^mu(s)-V||_{H^4} <= C(B^2+B)s`,
uniformly in `mu`. Correct.

This is HF04's mechanism, transcribed to the quotient route. The candidate says
so and disclaims priority for the scaling method. Confirmed against
`hf04-energy-only-spacetime.md` §1: same uniform-in-`mu` `H^m` estimate, same
`||v_mu(s)-phi||` linear-in-`s` bound, same three-stage structure.

**The HF04 audit's own repair is not repeated.** `hf04-review-spacetime.md`
returned REPAIR because HF04 integrated to the endpoint of the full guaranteed
interval, while the theorem's supremum requires `tau < T_*`. HF23 chooses
`s_0 in (0,T_0)` strictly, and the solutions exist **past** `T_0`, so
`tau_b = s_0/(b lambda^2) < T_0/(b lambda^2) <= T_*(u_b)` strictly. The
candidate states this ("It lies inside the classical interval"). Correct.

### 2.2 Uniform positivity of the work

`||N(v)-N(V)||_3 <= ||v-V||_inf ||grad v||_3 + ||V||_inf ||grad(v-V)||_3`
is the exact expansion `((v-V).grad)v + (V.grad)(v-V)`; both factors are
controlled on bounded `H^4` sets. Then, from `lem:derivative`,

    |K(v)-K(V)| <= ||A(v)-A(V)||_{3/2} ||N(v)||_3 + ||A(V)||_{3/2} ||N(v)-N(V)||_3,

with `||A(v)-A(V)||_{3/2} <= (2||w(V)||_3+||d||_3)||d||_3` and
`||d||_3^2 <= 2(||w(v)||_3+||w(V)||_3)||v-V||_3` from `eq:holderw`. This gives
exactly the displayed
`|K(v)-K(V)| <= C_B(||v-V||_{H^4}^{1/2} + ||v-V||_{H^4})`, hence one `s_0`,
independent of `mu`, with `K(v^mu(s)) >= k/2` on `[0,s_0]`. Correct. The
`1/2`-Hölder rate is the honest one: it comes from the value function, not from
any derivative of the minimizer, exactly as the candidate claims.

`0 <= D_Q(v^mu(s)) <= ||v^mu||_3^2 ||Delta v^mu||_3 <= D_max` follows from
`eq:heatbound` and the uniform `H^6` bound. Correct.

### 2.3 Scaling back to the prescribed viscosity and energy

The substitution was verified from scratch. With `u(t,x)=c v(alpha t, lambda x)`
the three inertial terms carry `c*alpha`, `c^2*lambda`, `c^2*lambda` and the
viscous term carries `nu c lambda^2`; matching forces `alpha = c lambda` and
`mu = nu lambda / c`. With `c = b lambda` this is `alpha = b lambda^2` and
`mu = nu/b`, exactly `eq:aux-scale`. The candidate's sentence "the time
derivative, transport term, and pressure gradient each carry `b^2 lambda^3`" is
correct. Datum `u_{b,0} = b T_lambda V` with
`||b T_lambda V||_2^2 = b^2 lambda^{-1} E_V = E` for `lambda = b^2 E_V/E`.
Correct.

Symbolic recomputation of every scaling factor (sympy, `scratchpad/sc.py`):

    tau_b            = s_0 (E/E_V)^2 b^{-5}                       matches eq:taub
    int_0^{tau_b} K  = b^3 * int_0^{s_0} K ds
    beta nu int D_Q  = b^2 beta nu * int_0^{s_0} D_Q ds
                     = b^3 * beta (nu/b) * int_0^{s_0} D_Q ds     matches eq:spacetime-scale
    int_0^{tau_b} Q  = (E/E_V)^2 b^{-2} * int_0^{s_0} Q ds        matches eq:small-low

so `eq:spacetime-scale` is an identity, not an estimate, and the `b^{-1}` inside
`beta(nu/b)` is exactly what lets the choice `beta(nu/b) D_max <= k/4` be made
after `b` has already been sent large. With `K >= k/2` and that choice the
integrand is `>= k/4`, giving `>= (k s_0/4) b^3 -> +infinity`. Correct.

### 2.4 The fixed high-strain cutoff

`eq:bernstein` was rederived. With the manuscript's `2 pi` convention,
`|grad S_L f| <= 2 pi int |xi| |varphi(xi/2^L)| |hat f|`, and
`|| |xi| varphi(xi/2^L) ||_2^2 = 2^{5L} || |xi| varphi ||_2^2` by
`xi = 2^L eta`, `dxi = 2^{3L} d eta`. Hence
`||grad S_L f||_inf <= C_B 2^{5L/2} ||f||_2` with `C_B = 2 pi || |xi| varphi ||_2`.
This is **identical** to the manuscript's `eq:qe-bernstein`, constant included.
`eq:ML`'s `M_L = 3(1+C_P) C_B 2^{5L/2} ||u_0||_2` is **identical** to the
manuscript's `eq:qe-lowstrain`. The Hölder chain
`|K_low,L| <= ||grad S_L u||_inf ||q||_3 ||A||_{3/2}` with `||A||_{3/2}=||w||_3^2`,
`||q||_3 <= (1+C_P)||w||_3`, `||w||_3^3 = 3 Q` reproduces the manuscript's proof
line for line. Correct.

For `thm:spacetime`, `L` is fixed and `M_L` depends on `||u_{b,0}||_2 = sqrt(E)`,
hence not on `b`. The cutoff is applied at the **original** scale to the actual
solution `u_b`; the dilation acts only on `Q`, whose spacetime integral is
`O(b^{-2})`. Nothing is commuted with `T_lambda` and no cutoff is moved.
`int K_L >= (k s_0/4) b^3 - M_L O(b^{-2}) -> +infinity`. **The claim that every
fixed high-strain cutoff is handled without rescaling it is correct.**

### 2.5 What is new here rather than restated

Against the audited HF20 record, precisely two upgrades, and they are exactly
the two the HF20 audit named as unsupported by HF20's own argument:

1. **Instantaneous to integrated.** HF20 Theorem 1.2 gives
   `sup{K - beta nu D_Q : ||v||_2^2 = E} = +infinity` at a fixed time, and a
   strict increase at `t = 0+`. The HF20 audit's refutation attempt 6 records
   that HF20 does *not* promote this to a time integral. The obstruction the
   candidate itself names -- "the interval of positivity might shrink too fast"
   -- is real and is settled by the exponent count: the interval is `O(b^{-5})`
   while the integrand is `O(b^8)`, product `b^3`.
2. **`K` to `K_L` for every fixed `L`.** HF20 audit non-claim 3 and reopening
   condition 2 state flatly that Corollary 5.1 "says nothing about `K_L`, and
   the family `b T_lambda V` does not transfer, because the fixed low-pass `S_L`
   is not equivariant under `T_lambda`". `thm:spacetime` closes this by never
   transferring the cutoff at all.

Not new: the sign certificate, the two-sign conclusion, the fixed-energy
instantaneous supremum, and the general varying-viscosity-then-rescale method,
which is the audited HF04 theorem on the pressure route. The candidate states
both disclaimers.

### 2.6 Consistency with the audited HF21-B crossing theorem

No contradiction, and the two agree quantitatively.

HF21-B Theorem 4.5(1) (post-repair) bounds the measure of the set where the
quotient can increase, `B_tau = {t < tau : C_# ||q(t)||_3 > nu}`, by
`(C_#/nu)^4 int_0^tau d_1^4 dt <= 24 C_S^2 C_#^4 E_0^2 nu^{-5}`, uniformly in
`tau`. On the HF23 family, `q(b T_lambda f) = b T_lambda q(f)` gives
`d_1(u_b(t)) = b d_1(v^mu(s))`, and the same change of variables as §2.3 gives

    int_0^{tau_b} d_1^4 dt = (E/E_V)^2 b^{-1} int_0^{s_0} d_1(v^mu)^4 ds = O(b^{-1}) -> 0,

verified symbolically. So the sharp form of the crossing bound gives
`|B_{tau_b}| = O(b^{-1})`, while `tau_b = O(b^{-5})`: the whole witnessing
interval is far inside the permitted measure budget, and the increase lives on a
set of times that shrinks *faster* than the bound requires. The input-only form
`24 C_S^2 C_#^4 E^2 nu^{-5}` is a fixed constant while `tau_b -> 0`, so it is not
even binding. Consistent.

Theorem 4.5(3), `Q(tau) <= Q(0) + C_# int_{B_tau} d_1 D_3(w) dt`, is also
consistent and order-sharp on this family: the left side minus `Q(0)` is
`>= (k s_0/4) b^3` at `beta = 1`, and
`int_0^{tau_b} d_1 D_Q dt = b^3 int_0^{s_0} d_1(v^mu) D_Q(v^mu) ds`, the same
order `b^3`. The two audited statements meet at the same exponent.

Consistency with the audited HF18-A bound `|K| <= C_* Q^{1/3} D_3(w)` is
inherited from the HF20 audit's §5.7: the ratio is exactly scale-invariant, and
`Q(u_{b,0})^{1/3} = b Q(V)^{1/3} -> infinity` puts the increase in the
supercritical regime HF18-A requires.

---

## 3. Item (3): the consumer proposition and the remaining estimate

### 3.1 `eq:quantifiers` versus `hyp:highstrain`

Compared symbol by symbol against `main.tex` lines 6843--6874. **Exact match**,
including quantifier order and the dependence pattern:

    exists theta in [0,1] ; forall nu > 0, u_0 Schwartz solenoidal, H > 0 ;
    exists L = L(nu,u_0,H) in Z, A_input = A_input(nu,u_0,H,L) in [0,infinity) ;
    forall 0 < tau < min{H,T_*} :   int_0^tau K_L <= theta nu int_0^tau D_Q + A_input

`theta = 1` is permitted in both, and the candidate's `rem` on the strict margin
reproduces the manuscript's own sentence ("Because `theta=1` is permitted, the
value of `theta` plays no role below"). The candidate's `K_L` is the
manuscript's `K_L`, not a substituted cutoff, and the candidate says so
explicitly. The sentence "The same `L` and the same finite `A_input` must work
for the whole indicated interval" is the manuscript's own. Correct.

### 3.2 `prop:consumer` versus `prop:quotient-conditional`

Reconstructed. The integrated balance `eq:consumer-integral` is the manuscript's
display; dropping `(1-theta) nu int D_Q >= 0` uses `theta <= 1` and
`D_Q >= 0` in both. The explicit Gronwall (`z = y(0)+A_input+M_L int y`,
`y <= z`, `z' <= M_L z`) is the manuscript's `lem:qe-gronwall` written out, and
is correct including the degenerate case `M_L = 0`. Coercivity gives
`3y(0) <= ||u_0||_3^3` and `||u||_3^3 <= 3 C_P^3 y`, so

    sup ||u(t)||_3^3 <= C_P^3 (||u_0||_3^3 + 3 A_input) e^{M_L H},

which is exactly the cube of the manuscript's `eq:qe-M`
`M = C_P(||u_0||_3^3+3A_input)^{1/3} exp(M_L H/3)`. **Exact match.**

The closing step is the manuscript's `thm:conditional`: choose `H > T_*`, so
`min{H,T_*} = T_*`, contradict `thm:continuation`, get `T_* = infinity`, then
Schwartz persistence for smoothness and `eq:energy` for the bounded-energy
condition. Correct.

### 3.3 The endpoint theorem is correctly identified and not reproved

The candidate's dependency sentence is accurate against the current manuscript:
"the pinned manuscript derives its endpoint theorem from the Leray--Hopf
membership of its classical branch, the Escauriaza--Seregin--Sverak theorem, a
Serrin-type estimate, and Tao's local theory. That is the manuscript's actual
dependency chain. Gallagher--Koch--Planchon's Theorem 4 is a directly inspected
corroborating strong-solution endpoint statement; it is not silently added as a
new formal dependency."

Checked: `thm:continuation` = `lem:l3-to-l5` (Leray--Hopf membership +
ESS Thm 1.3) + `lem:serrin-enstrophy` (manuscript-owned) + (R4). And
`rem:gkp` says verbatim "We do not use it", listing the three further statements
GKP Theorem 4 would require. **The candidate's description is correct and is
more accurate than `PLAN.md`'s own "Paper preparation" paragraph**, which still
says "The source premises are Tao Theorem 5.4 and GKP Theorem 4"; see the
controller list.

The explicit Serrin display the candidate writes "for clarity" was recomputed:
`|int (u.grad)u . Delta u| <= ||u||_5 ||grad u||_{10/3} ||Delta u||_2` with
`1/5+3/10+1/2 = 1`; `||grad u||_{10/3} <= ||grad u||_2^{2/5}||grad u||_6^{3/5}
<= C Y^{1/5} Z^{3/5}` (interpolation exponent `theta = 2/5` recomputed); Young
at `(5/4, 5)` gives `(nu/2)Z^2 + C nu^{-4}||u||_5^5 Y`. This is the manuscript's
`lem:serrin-enstrophy` in its `s = l = 5` form, correctly reproduced and
correctly labelled as the manuscript's, and backward uniqueness is explicitly
left external. Nothing is reproved that should have been imported.

### 3.4 `eq:remaining-sigma` is a restatement, and says so

`K_L = int sigma Pi_{u - S_L u}` requires `thm:mixed` at `b = u - S_L u`, which
is solenoidal (`S_L` is a Fourier multiplier) and lies in every `H^m` on the
classical branch, so the hypotheses of `thm:mixed` are available where used --
**conditional on Scope A certifying `thm:mixed` and `cor:sigma`.** Given that,
`eq:remaining-sigma` is `eq:quantifiers` rewritten, and the candidate labels it
"a restatement of the *same* missing high-strain inequality, not its proof",
declines to identify `Pi_{u-S_Lu}` with `p_{>J}`, and states that no new cutoff
is substituted. All correct.

The existential-remainder subsection reproduces the manuscript's own
`rem:highstrain-scope` converse (`L = 0`, `theta = 0`,
`A_input = int_0^H |K_0| < infinity` when `T_* = infinity`) and draws the right
conclusion: equivalence at these quantifiers, no producer. Correct.

---

## 4. Item (4): the ledger's closing admission

The admission reads: "An absolute estimate leaves `int Y^2` (or a still stronger
time norm of the mixed pressure), not the energy integral `int Y`."

**This is exactly right.** Recomputed:

- `eq:KY`: `|K| <= (1/2)||grad u||_2 ||u||_6 ||w||_6^2 <= (1/2) Y^{1/2} (S Y^{1/2})
  (S^2 (5/4) Y) = (5/8) S^3 Y^2`. Arithmetic confirmed.
- `eq:firstgap`: integrating gives `int_0^tau K <= (5/8) S^3 int_0^tau Y^2`.
  Energy controls `int Y <= E_0/(2 nu)`; it does not control `int Y^2`.
- The mixed route: `||Pi_u||_2 <= ||u||_6 ||w||_6^2 <= (5/4) S^3 Y^{3/2}`, so
  `eq:Pi-conditional` reduces the need to `int ||Pi_u||_2^2`, for which the only
  available bound is `(25/16) S^6 int Y^3`. Since
  `int Y^2 = int Y^{1/2} Y^{3/2} <= (int Y)^{1/2}(int Y^3)^{1/2}` by
  Cauchy--Schwarz, the split route is **weaker** than the direct one. The
  parenthetical "or a still stronger time norm of the mixed pressure" is
  therefore accurate, not hedging.
- `Y = ||grad u||_2^2` is four times the enstrophy, so `int Y^2` is exactly the
  time integral of the square of the enstrophy, and `int Y` is exactly the
  energy-controlled dissipation integral. The phrasing is literal.

**Do the budgets get closer?** No, and the candidate does not claim they do.
`cor:budgets` gives `int ||grad w||_2^2 <= 5E_0/(8 nu)` and
`int ||sigma||_2^2 <= E_0/(8 nu)`; both are `int Y`-level statements obtained by
integrating a pointwise-in-time inequality against the energy identity, so
neither supplies any time integrability beyond `int Y`. What they *do* supply is
a change of shape, which the candidate records honestly at `eq:Pi-conditional`:
one of the two factors in `int int sigma Pi_u` is now input-only bounded, so the
missing object is an **absolute** spacetime bound on `Pi_{u-S_L u}` rather than
a signed correlation. That is a real reduction in the kind of statement needed
and a nil reduction in its strength. The ledger says exactly this
("a real but insufficient consequence"; "It does not supply that missing time
bound"). Nothing is overstated.

The scalar illustration `y=(T-t)^{-1/2}`, `y'=y^3/2`, `int y < infinity`,
`int y^2 = infinity` is correct and correctly flagged as not a Navier--Stokes
solution. §8.2 replaces it with an actual solution family, and §8.1 shows the
admission is understated.

---

## 5. Item (5): literature and novelty

### 5.1 Every attribution checked

**Sarsa.** `arXiv:2009.10102v1` fetched. Title "Note on an elementary inequality
and its application to the regularity of `p`-harmonic functions", author Saara
Sarsa, submitted 21 September 2020 -- **all three exact as cited**. Abstract:
`|Du|^{(p-2+s)/2} Du in W^{1,2}_loc` for `s > -1-(p-1)/(n-1)`. Introduction
fetched: it states verbatim that Manfredi and Weitsman proved `W^{2,2}_loc` for
`1 < p < 3+2/(n-2)` and that "This restriction for the range of `p` arises from
so-called Cordes condition", and that at `s = 2-p` the paper reproves
`W^{2,2}_loc`. **So the candidate's sentence -- symmetric-matrix inequalities,
Sobolev regularity of nonlinear fields attached to scalar `p`-harmonic
functions, and a Cordes-condition discussion in the introduction -- is accurate
on every clause.**

The attribution is if anything **too weak**, and this matters for the repository.
Sarsa's Lemma 2.1 reads, for symmetric `A` and vector `e`,

    |e|^4 |A|^2  >=  2|e|^2 |Ae|^2 + (|e|^2 tr A - <e,Ae>)^2/(n-1) - <e,Ae>^2 .

Take `n = 3`, `|e| = 1`, write `d = tr A`, `beta = <e,Ae>`, and drop
`2|Ae|^2 >= 2 beta^2` (Cauchy--Schwarz). Under the candidate's Euler--Lagrange
constraint `d = -t beta`, i.e. `beta = -d/t`:

    |A|^2  >=  beta^2 + (d-beta)^2/2  =  d^2/t^2 + d^2(1+1/t)^2/2
           =  d^2 (t^2+2t+3)/(2 t^2),

which is **literally** the candidate's `lem:matrix`. Verified numerically
(200000 random symmetric matrices for Sarsa's lemma, minimum slack `3.4e-8`;
400000 constrained triples for `lem:matrix`, minimum slack `3.2e-3`; the
reduction reproduces the claimed right side to machine precision at
`t = 0.05, 0.3, 0.7, 1`). So `lem:matrix` is not merely methodological kin to
published work: it is a corollary of a published lemma. The candidate's own
caution ("It would be inappropriate to claim that regularization plus a trace
inequality is a new general regularity mechanism") is therefore correct and
should be stated in this sharper form. Bounded numerical evidence, not proof;
the algebraic reduction above is the proof.

**Yu.** `arXiv:2606.25322` abstract page fetched: title "Coarse-Grained
Resolution and Pressure-Flux Work Depletion for Navier-Stokes CKN Badness",
author Runlong Yu, submitted 24 June 2026 -- exact as cited. The body was not
re-fetched; it does not need to be, because the repository's own audited record
`cp02-prior-art-related-work.md` §1.1 read it `[DI]` in this repository and
records the same objects
(`G^l = Pi^l + div(P^l U^l)`, `Pi^l = -R^l : grad U^l`), the same Theorem 4.1
(finite-chain weighted telescoping, forward work and resolved dissipation paid
by initial localized energy, leakage and negative work), and the same
Remark 4.2 withholdings. **The candidate's description matches the audited
record clause for clause.** Its conclusion -- relevant structure and a
comparison target, not the missing estimate -- is the audited record's
conclusion transposed from the pressure-route object `Q_J` to the
quotient-route object `sigma Pi_{u-S_L u}`. That transposition is new (no
repository record compares Yu to the quotient route), but it is a *negative*
comparison, the safe direction, and it is supported by Remark 4.2 as recorded.

**GKP.** "Theorem 4 ... checked on printed page 18 of arXiv v3." The repository's
own `cp01-literature-statements.md` records Theorem 4 `[DI]` from the arXiv
LaTeX source `GKPrevised_16_07_2012.tex`, not by printed page, so the page
number is not corroborated here. It is not load-bearing: the theorem's content
and its status as corroboration-only are both confirmed against `rem:gkp`.

**Clay, Tao, ESS, Stein.** Consistent with the repository's records; nothing
load-bearing for a novelty claim rests on them.

### 5.2 Novelty claims: none unsupported

Every novelty-adjacent sentence in `sec:literature` was extracted and checked.
The candidate:

- asserts only "additional derivation in this note", explicitly distinguishing
  it from "previously unpublished theorem";
- refuses a novelty certificate for the div--curl estimate, deferring to "a
  dedicated theorem-level comparison before publication";
- disclaims priority for the general scaling method of `thm:spacetime`, crediting
  HF04;
- declines the three broad claims of the recovered surveys (first AI-assisted
  programme, first pressure method, first reduction to a single obstruction);
- states correctly that the surveys' negative search result "is not a
  certification of worldwide priority".

**No claim of novelty in this document is unsupported by the repository's own
searches, because the document makes no claim of novelty.** Its only positive
prior-art claims (Sarsa, Yu) are both verified above. Item (5) has no adverse
finding of the kind it was looking for.

### 5.3 The real defect: the wrong sources are used

`sec:literature` is built on `\cite{Survey1,Survey2,Survey3}`, three "prior
conversation research reports recovered from the user's file library". These are
not in the repository, cannot be verified at any revision, and are of unknown
audit status. Meanwhile the repository's own **audited** prior-art notes were
present in the very revision the candidate pins (`git cat-file -e
1014e7e:research/evidence/cp01-prior-art-quotient.md` and `...cp02-...` both
succeed) and are never cited; `\cite{Navier}`'s path list names `PLAN.md`,
`docs/proof.md`, `hf18-divergence-speed-link.md`, the HF19 notes and the HF20
record, but not `cp01`/`cp02`.

Two consequences, both concrete:

- `cp01` §1.8 records **Manfredi--Weitsman, Comm. PDE 13 (1988) 651--668**,
  `W^{2,2}_loc` for `p`-harmonic functions with `1 < p < 3+2/(n-2)`, which at
  `p = 3, n = 3` is exactly the unshifted scalar analogue of `thm:main`'s
  conclusion, and which Sarsa's own introduction names as the Cordes-condition
  result. It is the nearest located prior art for the *conclusion*, not just the
  method, and the candidate does not cite it.
- `cp01` §1.1 records **Sibner--Sibner, Acta Math. 125 (1970) 57--73** `[DI]` as
  the located source for the variational mechanism the candidate calls
  "nonlinear Hodge minimization ... not new"; `cp01` §1.7 records
  **Bojarski--Iwaniec 1983 via Lindqvist Thm 4.1** `[DI]` as the located source
  for the difference-quotient mechanism the candidate's regularization step
  reuses. Neither is cited.

`cp01`'s verdict table is also the right home for the candidate's own result:
its rows "(Q)(W) with **prescribed nonzero curl** at `p=3`: unlocated (not a
novelty claim)" and "(R) ... shifted + global version unlocated" are precisely
where `thm:main` sits, and they already carry the correct epistemic label. See
repair R2.

---

## 6. Refutation attempts, all failed

1. **Break `thm:spacetime` by shrinking the interval faster.** The exponents are
   forced: `tau_b = s_0/(b lambda^2)` and `lambda = b^2 E_V/E` are both
   determined by the two constraints (viscosity `= nu`, energy `= E`). No free
   parameter remains to trade. `b^8 * b^{-5} = b^3` is not adjustable.
2. **Break it by making the auxiliary lifespan collapse as `mu -> 0`.** The
   `H^6` estimate discards viscosity; `Z' <= C Z^2` has no `mu` in it. Checked
   the commutator split at both ends (`|gamma| <= 4` and `|gamma| >= 5`); both
   close inside `H^6`. No collapse.
3. **Break the `K_L` extension by making `M_L` grow with `b`.**
   `M_L = 3(1+C_P) C_B 2^{5L/2} ||u_{b,0}||_2` and `||u_{b,0}||_2 = sqrt(E)` is
   pinned by construction. `L` is quantified before `b`. No growth.
4. **Force a contradiction with the audited HF21-B crossing theorem.**
   Attempted quantitatively in §2.6: `int_0^{tau_b} d_1^4 dt = O(b^{-1})` and
   `tau_b = O(b^{-5})`, both consistent with a fixed input-only measure budget.
   The crossing bound is not even active on this family.
5. **Force a contradiction with the audited HF18-A bound.** Ratio is exactly
   scale-invariant (HF20 audit §5.7), and `Q^{1/3} ~ b -> infinity` places the
   increase in the supercritical region HF18-A requires. No tension.
6. **Find a hidden circularity in `thm:spacetime`.** None. `k = K(V) > 0` is
   fixed before any limit; `D_max`, `B`, `T_0`, `s_0` depend only on `V`; `b`
   enters only after all of them. No quantity is bounded by the quantity it is
   used to bound.
7. **Find an identity mistaken for an estimate.** `eq:spacetime-scale` and
   `eq:small-low` are identities (verified symbolically) and are used as such;
   the estimates are `eq:uniform-positive`, `eq:Dmax` and `eq:lowstrain`, all
   genuine.
8. **Find an instantaneous fact promoted to a time-integrated one.** This is the
   exact failure mode the section exists to avoid, and it does not occur: the
   time integration is performed on the *auxiliary* family over the fixed
   interval `[0,s_0]`, where positivity was proved uniformly in `mu`, and then
   transported by an exact change of variables. `eq:instant-sup` is never
   integrated.
9. **Find a claim whose proof supports only something weaker.** The one candidate
   was `eq:hf20sign`; it is displayed two-sidedly and the proof gives the
   two-sided form, so the HF20 defect is absent. Checked every other boxed
   display in Scope B (`eq:quantifiers`, `eq:remaining-sigma`,
   `eq:spacetimesup`); each is used only at the strength it is displayed.
10. **Break `prop:consumer` on quantifiers.** `H > T_*` is admissible because `H`
    is universally quantified; `L, A_input` are then the ones supplied for that
    `H`; `tau_1 < min{H,T_*}` arbitrary gives the estimate on the whole maximal
    interval. No slippage.
11. **Numerics.** Sarsa Lemma 2.1 and the constrained inequality checked over
    600000 random configurations; all scaling factors of §2.3, §2.6 recomputed
    symbolically. Scripts in session scratch; all results reproduced in-line
    above so the note does not depend on them. Bounded evidence, never proof.

---

## 7. Repairs, with their replacements

### R1. Cite the manuscript's local-theory package instead of re-sketching it

**Defect.** `lem:evolution`'s proof asserts "On a compact classical interval,
`u in C^1_t L^3` and `Delta u, N(u), grad p in C_t L^3`. Moreover `p in W^{1,3}`:
this follows from the normalized Riesz formula and the high Sobolev bounds on
`u`", and `sec:hf20` says only "The actual local classical branch exists by
Tao's local theory". This is the same compression the HF20 audit ruled a
non-proof at this tier, and whose replacement the controller already applied to
the HF20 record. Everything in Scope B that uses `eq:evolution` --
`eq:increase`, `eq:split-final`, `prop:consumer` -- rests on it.

**Replacement.** Delete the sketch and insert, in the proof of `lem:evolution`:

> The regularity package is imported, not re-derived. On every compact
> `[0,T] subset [0,T_*)`, `prop:localtheory`(iii) of the pinned manuscript gives
> `u in C^j([0,T];H^k)` for all `j,k`, whence `u in C^1([0,T];L^3)` and
> `Delta u, N(u) in C([0,T];L^3)` by Sobolev embedding on the closed interval,
> including `t = 0`; `prop:localtheory`(iv) gives the pointwise equation with the
> normalised pressure `p = R_i R_j(u_i u_j)` and `p in C([0,T];H^k)`, hence
> `p(t), grad p(t) in L^2 cap L^6 subset L^3`, i.e. `p(t) in W^{1,3}`. The upgrade
> from Tao 5.4(iv)'s `L^inf_t H^k` to `C^0_t H^k` is `lem:upgrade`; it is not
> re-proved here. Tao 5.4(ii)'s smallness hypothesis is available because only a
> short interval for one fixed datum is required.

*Justification.* This is verbatim the repair the HF20 audit prescribed
(§2(i), "Integration action") and the controller applied. No new hypothesis and
no change to any constant; the four facts listed are exactly `lem:evolution`'s
own hypotheses.

### R2. Replace the survey-based literature basis by the repository's audited prior art

**Defect.** §5.3.

**Replacement.** In `sec:literature`, (a) add `cp01-prior-art-quotient.md` and
`cp02-prior-art-related-work.md` to the `\cite{Navier}` path list; (b) replace
the opening of "What the earlier surveys establish" by:

> The repository contains two audited prior-art records for exactly these
> objects: `cp01-prior-art-quotient.md` for the quotient functional and its
> minimizer, and `cp02-prior-art-related-work.md` for the pressure-route
> comparison. They are used here in preference to the recovered conversation
> reports, which are retained only for the historical research state. `cp01`
> locates the variational mechanism in Sibner and Sibner (Acta Math. 125 (1970)
> 57--73) for closed data and bounded density, locates the difference-quotient
> mechanism behind the weighted statement in Bojarski--Iwaniec via Lindqvist
> Theorem 4.1, and records the coset problem with prescribed nonzero curl at
> `p = 3`, and the shifted global form of the weighted regularity, as
> *unlocated* -- an absence of located prior art, not a claim of priority. The
> theorem proved here sits on those two rows.

and (c) append to "The div--curl calculation belongs beside Cordes-type prior
art":

> The relation is closer than methodological. With `n = 3`, `|e| = 1`,
> `d = tr A`, `beta = <e,Ae>`, Sarsa's Lemma 2.1 gives
> `|A|^2 >= 2|Ae|^2 + (d-beta)^2/2 - beta^2 >= beta^2 + (d-beta)^2/2` by
> Cauchy--Schwarz, and substituting the Euler--Lagrange constraint
> `beta = -d/t` yields `|A|^2 >= d^2 (t^2+2t+3)/(2 t^2)`, which is
> Lemma `lem:matrix` exactly. The lemma is therefore a corollary of published
> work, and no novelty attaches to it. For the *conclusion* rather than the
> method, the nearest located prior art is Manfredi and Weitsman, Comm. PDE 13
> (1988) 651--668, `W^{2,2}_loc` for `p`-harmonic functions when
> `1 < p < 3 + 2/(n-2)` -- the unshifted, curl-free, scalar case of the present
> statement at `p = 3`, `n = 3`, and the result whose range restriction Sarsa's
> introduction attributes to the Cordes condition. What is not covered by either
> is the shifted field with prescribed nonzero `curl w = curl u`.

*Justification.* (c)'s algebra is displayed above and verified in §5.1; (b)
quotes `cp01`'s own verdict rows verbatim.

### R3. Restore the two HF20 scope sentences

**Defect.** §1.3, §1.4.

**Replacement.** Append to "What the HF20 calculation does not say":

> Two further restrictions, from the audited record of that candidate. First,
> the excluded instantaneous estimate concerns the full `K`; it says nothing
> about `K_L`, and the family `b T_lambda V` does not transfer to `K_L`, because
> the fixed low-pass `S_L` is not equivariant under `T_lambda`. That gap is
> closed separately, and by a different argument, in Section `sec:spacetime`.
> Second, the certificate is qualitative: for the fields as written the
> admissible `eps` is far below any scale of numerical use, and the size is
> driven by the far shell `3 <= |x| <= 4` where `h` and `g` disagree.

*Justification.* Sentence one is the HF20 audit's non-claim 3 and reopening
condition 2; sentence two is its §2(g) non-defect and the manuscript's
`rem:no-monotone` closing sentence. Both are statements about the *attached*
candidate, so they belong in the section that reconstructs it.

### R4. Attribute the transport identity to the manuscript

**Defect.** `sec:mixed` introduces `eq:strainK` with "The weak-derivative results
above permit direct integrations by parts that were previously gated by HF18's
hypothesis (H1)", suggesting the identity `K(u) = -int q.((A.grad)u)` is newly
unlocked. It is not: the manuscript proves it unconditionally as
`lem:quotient-transport` by a flow-map/pullback argument that never
differentiates `w`, and `eq:split-final` in `sec:frontier` consumes the
manuscript's version anyway.

**Replacement.** Insert before `eq:strainK`:

> The identity itself is not new and is not gated by (H1): it is
> `lem:quotient-transport` of the pinned manuscript, proved there by pulling the
> minimizer back along the flow of `u`, with no derivative of `w`. What follows
> is an alternative derivation available once `grad w in L^2`, recorded because
> the same integrations by parts are reused in Theorem `thm:mixed`.

*Justification.* `main.tex` line 6545, `lem:quotient-transport`, with the
absolute-convergence bounds displayed there; its proof uses only `lem:flow` and
`lem:qe-pullback`.

---

## 8. Offered strengthenings (not repairs; the candidate is not wrong without them)

### 8.1 The absolute estimate is not merely insufficient; its right side is a regularity criterion

The ledger says an absolute estimate leaves `int_0^tau Y^2 dt`. That quantity is
*exactly* a Ladyzhenskaya--Prodi--Serrin norm of the solution, so an input-only
bound on it would already prove the target by the manuscript's own machinery,
without the quotient. Proof, at the manuscript's own tier:

> Since `||u||_6 <= S ||grad u||_2`, `int_0^tau Y^2 dt < infinity` is
> `u in L^4((0,tau); L^6)`, and `(s,l) = (6,4)` satisfies `3/s + 2/l = 1`.
> Concretely, testing the equation with `-Delta u` as in `lem:serrin-enstrophy`
> and using `|int (u.grad)u . Delta u| <= ||u||_6 ||grad u||_3 ||Delta u||_2`
> with `||grad u||_3 <= C ||grad u||_2^{1/2} ||grad u||_6^{1/2} <= C Y^{1/4} Z^{1/2}`
> gives `(1/2) Y' + nu Z^2 <= C ||u||_6 Y^{1/4} Z^{3/2}`, and Young at
> `(4/3, 4)` gives `(1/2) Y' + (nu/2) Z^2 <= C nu^{-3} ||u||_6^4 Y <= C S^4 nu^{-3} Y^3`.
> Gronwall yields `Y(t) <= Y(0) exp(C S^4 nu^{-3} int_0^tau Y^2)`, so a finite
> input-only bound on `int_0^tau Y^2` gives `sup_{t<T_*} ||u(t)||_{H^1} < infinity`,
> contradicting (R4) and forcing `T_* = infinity` outright; it also gives
> `hyp:critical` by interpolating `L^3` between `L^2` and `L^6`.

Consequently `eq:firstgap` cannot be a producer under any circumstances: proving
its right side finite from input data *is* the target, reached by a route that
does not pass through the quotient at all. This is the frontier packet's
"a bound that depends on the very norm it must control", instantiated exactly,
and it converts the ledger's admission from a report of insufficiency into a
proof of unusability. Recommended as a replacement for the scalar
`y = (T-t)^{-1/2}` illustration, which makes a weaker point.

### 8.2 `thm:spacetime`'s own family proves the admission, on actual solutions

The candidate notes that its scalar illustration "is not a Navier--Stokes
solution". Its own family removes that caveat. With `u_b` as in `eq:aux-scale`,
`||grad u_b(t)||_2^2 = b^2 lambda ||grad v^mu(s)||_2^2`, so by the same change of
variables as §2.3 (verified symbolically):

    int_0^{tau_b} Y dt   = (E/E_V) b^{-1} int_0^{s_0} ||grad v^mu||_2^2 ds  =  O(b^{-1}) -> 0,
    int_0^{tau_b} Y^2 dt = b^3 int_0^{s_0} ||grad v^mu||_2^4 ds             >=  (s_0/16) ||grad V||_2^4 b^3 -> infinity,

the lower bound because `eq:uniform-close` gives
`||grad v^mu(s)||_2 >= ||grad V||_2/2` on `[0,s_0]` after a harmless further
reduction of `s_0`, uniformly in `mu`. So there is a sequence of **genuine
classical Navier--Stokes solutions at the prescribed `nu` and `E`** along which
the energy integral tends to zero while the square of the enstrophy in time
diverges, at the same rate `b^3` as `int K`. The gap between `int Y` and
`int Y^2` is therefore not an artefact of Hölder; `eq:firstgap` is order-sharp on
this family. Recommended as a two-line addition to the ledger.

---

## 9. Conditional suffix that survives

All of Scope B survives, with R1--R4 applied and with the Scope A conditionality
stated where it exists.

- `sec:hf20` in full, as a reconstruction at the audited HF20 scope, with the
  two-sided display. **Unconditional** (it consumes only `lem:min`,
  `lem:convex`, `lem:derivative`, `lem:evolution`, none of which uses
  `thm:main`), modulo R1's citation.
- **Theorem `thm:spacetime`**, both halves (`K`, and `K_L` for every fixed
  integer `L`), for the original unforced equation, at the prescribed `nu` and
  `E`, over compactly supported smooth solenoidal data, using only local
  existence and the fixed-`mu` blowup alternative. **Unconditional**, modulo
  R1's citation. Its quantifier remark is correct as written.
- `sec:frontier`'s low-strain calculation `eq:bernstein`--`eq:ML`.
  **Unconditional**; it reproduces `lem:quotient-lowstrain` with identical
  constants.
- **Proposition `prop:consumer`** and the endpoint identification.
  **Unconditional**; it reproduces `prop:quotient-conditional` and
  `thm:conditional` with identical constants and quantifiers, and imports the
  endpoint theorem correctly without reproving it.
- The existential-remainder subsection. **Unconditional**; it reproduces
  `rem:highstrain-scope`.
- `eq:remaining-sigma`, and the `eq:KY`/`eq:firstgap`/`eq:Pi-conditional`
  arithmetic feeding the ledger. **Conditional on Scope A** certifying
  `thm:main`, `cor:sigma` and `thm:mixed`. The arithmetic itself is correct as
  checked in §4.
- The ledger's boundary statement, including "an absolute estimate leaves
  `int Y^2` ... not the energy integral", and the claim that the negative result
  excludes an energy-only repair over all data on genuine trajectories.
  **The first is exactly right and understated (§8.1); the second is exactly
  `thm:spacetime` and is proved.**

Unchanged: the first gap. `hyp:highstrain` is neither proved nor refuted, and
`thm:spacetime` explicitly cannot refute it because the family uses a different
datum for each `b` and `hyp:highstrain` selects its cutoff and remainder from
the whole datum. NS-R3 remains open.

## 10. Unnecessary dependencies

- **The `K_L` half of `thm:spacetime` no longer needs `eq:small-low`.** At the
  current manuscript head, `rem:highstrain-normalisation` (added at `4478bde`,
  after the candidate's pin) proves
  `int_0^tau Q(u(t)) dt <= (1/3) H^{1/4} (3 C_S^2 ||u_0||_2^4/(2 nu))^{3/4}`,
  input-only. With `||u_{b,0}||_2^2 = E` fixed, this bounds
  `|int_0^{tau_b} K_low,L(u_b) dt| <= M_L c(E,nu,H)` by a constant independent
  of `b`, so `int K_L >= (k s_0/4) b^3 - const -> infinity` follows from the `K`
  half alone. The candidate's `O(b^{-2})` route is sharper and is correct;
  it is simply no longer required. Worth recording because it shows the
  frequency split is cosmetic for the obstruction as well as for the hypothesis.
- **The two-sided display of `eq:hf20sign` is not needed** if the HF20 audit's
  Lemma A (`K(-v) = -K(v)`, `D_Q(-v) = D_Q(v)`, from `lem:quotient-scaling` at
  `alpha = -1`) is available; the one-sided form plus oddness gives everything.
  The candidate proves the two-sided form anyway, which is fine and is the
  repaired repository form.
- **`w(U) = U` is not needed for the certificate**, only for the bookkeeping
  `Q(U) = F(U)` and `<j(U), d_eps> = 0`; it makes the competitor argument exact
  and should be kept (HF20 audit §7).
- **Harmonicity of `phi` is not needed**; the HF20 audit's generalization (any
  traceless symmetric `S` with `int |U| U.SU != 0`) covers it. The candidate
  keeps the harmonic gradient, which is harmless.
- **Surveys 1--3 are not needed anywhere.** Every statement `sec:literature`
  draws from them is either in `cp01`/`cp02` or is a disclaimer. Removing the
  three citations costs nothing (R2).
- **The Riesz sign convention differs** from the manuscript's (`R_j` has symbol
  `i xi_j/|xi|` here, `-i xi_j/|xi|` there), but every object actually used --
  `R_i R_j`, `P`, `Pi_b` -- is invariant under that sign flip, so nothing
  depends on it. Recorded because HF18 once carried a genuine Riesz-sign defect.

## 11. Non-claims

- This review certifies nothing in `sec:regularity` or `sec:mixed`. `thm:main`,
  `cor:sigma` and `thm:mixed` are **not** audited here; the controller check
  recorded in the index note is not an audit and this review does not upgrade
  it. Every Scope B statement that consumes them is marked conditional in §9.
- No graph node is promoted or demoted by this review. `HIGH-STRAIN`,
  `HIGH-PRESSURE`, `CRITICAL` and `NS-R3` are untouched.
- `thm:spacetime` is not a refutation of `hyp:highstrain`, not a singular
  solution, not an unbounded critical norm on a fixed trajectory, and not a
  statement about any single flow: the initial critical norms diverge
  (`||u_{b,0}||_3 = b ||V||_3`), a different datum is used for each `b`, and the
  witnessing times tend to zero.
- No novelty or priority is claimed for anything in the candidate or in this
  review. §5.1's placement of `lem:matrix` beneath Sarsa Lemma 2.1 is a
  *reduction* of a claim, not an assertion about anyone's priority.
- The numerics in §5.1 and the symbolic scaling checks in §2.3 are bounded
  evidence at finite resolution. The proofs are the algebraic derivations
  displayed alongside them.

## 12. Reopening condition

Reopen this audit if any of the following occurs.

1. Scope A returns anything other than a clean pass on `thm:main`, `cor:sigma`
   or `thm:mixed`. Everything in §9 marked conditional falls with it, including
   `eq:remaining-sigma` and the whole `int Y^2` discussion of §4, though
   `sec:hf20`, `thm:spacetime`, `prop:consumer` and the low-strain lemma do not.
2. `thm:spacetime` is ever stated with the cutoff `L`, the parameter `beta`, or
   the remainder allowed to depend on the initial *field* rather than on
   `(E, nu, H, L, beta)`. That is a strictly stronger claim, it would refute
   `hyp:highstrain`, and this argument does not support it.
3. `thm:spacetime` is ever stated for a *fixed* datum, or the family is
   described as a single trajectory. The construction uses a different datum for
   each `b` and the intervals shrink like `b^{-5}`.
4. `prop:localtheory`(iii),(iv), `lem:upgrade`, `lem:quotient-lowstrain`,
   `eq:qe-bernstein`, `hyp:highstrain` or `prop:quotient-conditional` is altered
   in the manuscript. §2.4 and §3 verify the candidate against their present
   text, and R1 makes the dependence explicit.
5. The manuscript's `lem:quotient-scaling` amplitude law is narrowed from
   `alpha in R` to `alpha > 0`, which removes the Lemma A alternative recorded
   in §10.
6. A primary reading of Sarsa arXiv:2009.10102 Lemma 2.1 disagrees with the
   statement quoted in §5.1, or the reduction displayed there fails at some `t`.
7. `PLAN.md`'s "Paper preparation" paragraph continues to describe GKP Theorem 4
   as a source premise after `rem:gkp` demoted it to corroboration; the candidate
   is right and the plan is stale, and a reader comparing them will conclude the
   candidate misdescribed the dependency chain.

---

## Exact edits the controller should make if this verdict stands

**Candidate note (`hf23-divcurl-continuation.md`, the index note only; the
`.tex` is frozen and must not be edited).** Record: Scope B audited, PASS WITH
SCOPE, four repairs R1--R4 required before any manuscript integration; the HF20
reconstruction reproduces the audited construction with identical constants and
independently states the repaired two-sided form; `thm:spacetime` is new
relative to HF20 in exactly two respects and is the quotient-route analogue of
the audited HF04; the ledger's boundary admission is exact and understated.

**Manuscript (`navier-paper/main.tex`).** One licensed edit, and one only.
Extend `rem:no-monotone` in `sec:quotient` with a second paragraph recording the
*spacetime* exclusion, kept strictly separate from the instantaneous one already
there:

> The exclusion also holds after time integration, and for the high-frequency
> piece. For every `nu, E, H > 0`, every `beta >= 0` and every fixed integer `L`,
> the supremum of `int_0^tau (K_L(u(t)) - beta nu D_Q(u(t))) dt` over classical
> branches from divergence-free `u_0 in C_c^inf(R^3)^3` with `||u_0||_2^2 = E`
> and `0 < tau < min{H, T_*}` is `+infinity`. Hence no finite remainder
> depending only on `(E, nu, H, L, beta)` can serve in
> Hypothesis~`hyp:highstrain`, and neither can a cutoff rule depending only on
> those scalars. This does not bear on Hypothesis~`hyp:highstrain` itself, whose
> cutoff and remainder are selected from the entire datum: the witnessing family
> uses a different datum for each amplitude, its initial critical norms diverge,
> and its witnessing times tend to zero.

Do **not** state this for `K` alone (it holds for both, but the `K_L` form is the
one that matters), do **not** weaken "depending only on" to "depending on", and
do **not** attach it to `prop:quotient-conditional`, which is untouched.

**Graph (`docs/proof-graph.yaml`, HIGH-STRAIN review text).** Add one excluded
mechanism class: *a fixed-cutoff, energy-only spacetime remainder -- i.e. any
`A_input` depending only on `(E, nu, H, L, theta)` -- is excluded on genuine
fixed-viscosity trajectories, for every fixed `L`.* Note that the previously
recorded HF20 class covered only the instantaneous statement for the full `K`.
No node is promoted or demoted; `HIGH-STRAIN` stays open.

**`PLAN.md`.**
1. In the HF23 section, replace "Nothing is promoted and the manuscript is
   untouched pending audit" by the Scope B outcome above, naming the two new
   facts (integrated exclusion; `K_L` for every fixed `L`) and the four repairs.
2. In "Ordered next actions", record that the HF20 audit's reopening condition 2
   has now been *satisfied by a different argument* rather than violated, so it
   is discharged rather than triggered.
3. Correct the stale sentence in "Paper preparation": "The source premises are
   Tao Theorem 5.4 and GKP Theorem 4" no longer matches `rem:gkp`, which states
   GKP Theorem 4 is corroboration only and is not used. Replace "GKP Theorem 4"
   by "ESS Theorem 1.3, with GKP Theorem 4 as corroboration only". Reported, not
   applied: outside this review's one-file scope.

**Do not** integrate `thm:main`, `cor:sigma`, `thm:mixed`, `eq:remaining-sigma`
or the `sec:budget` budgets on the strength of this review. They are Scope A.

---

**VERDICT:** PASS WITH SCOPE. No invalid or unsupported bridge in Scope B; four
statement- and citation-level repairs (R1--R4) required before integration.

**REVIEWED SCOPE:** `research/evidence/hf23-divcurl-continuation.tex` sections
`sec:hf20`, `sec:spacetime`, `sec:frontier`, `sec:literature` and the Final
proof ledger, plus the preliminaries `lem:min`, `lem:convex`, `lem:derivative`,
`lem:evolution` they consume, and the arithmetic of `eq:KY`,
`eq:Pi-conditional`, `eq:firstgap`. Cross-checked against
`hf20-harmonic-strain-test.md` (post-repair) and `hf20-review-harmonic-strain-test.md`
in full, `hf04-energy-only-spacetime.md` and `hf04-review-spacetime.md`,
`hf21-crossing-sign-structure.md` Theorem 4.5 and Lemma R3,
`cp01-prior-art-quotient.md`, `cp02-prior-art-related-work.md`,
`cp01-literature-statements.md`, and `main.tex@4084330`
`lem:quotient-transport`, `lem:quotient-lowstrain`, `eq:qe-bernstein`,
`hyp:highstrain`, `rem:highstrain-normalisation`, `rem:highstrain-scope`,
`rem:no-monotone`, `prop:quotient-conditional`, `hyp:critical`,
`thm:conditional`, `thm:continuation`, `lem:l3-to-l5`, `lem:serrin-enstrophy`,
`rem:gkp`. Primary sources fetched: arXiv:2009.10102v1 (abstract, introduction,
Lemma 2.1) and arXiv:2606.25322 (abstract page). **Not reviewed:**
`sec:regularity`, `sec:mixed`, `sec:budget`'s Corollary `cor:budgets`.

**FIRST BAD BRIDGE:** None in Scope B. The nearest thing to one is the
regularity chain asserted in `lem:evolution`'s proof and reused in `sec:hf20`:
it is the same one-sentence compression of `prop:localtheory`(iii),(iv) and
`lem:upgrade` that the HF20 audit ruled a non-proof at this tier and that the
controller already repaired once. The mathematics is right; the tier is not.
Repair R1.

**EVIDENCE:** `eq:hf20sign` is displayed two-sidedly, so the HF20 defect is
absent, and at the pinned research revision `1014e7e` the repository's own HF20
record was still one-sided and the audit uncommitted, so the two-sided form was
reached independently. `thm:spacetime`'s exponents were recomputed symbolically:
`tau_b = s_0 (E/E_V)^2 b^{-5}`, `int K = b^3 int K ds`,
`beta nu int D_Q = b^3 beta (nu/b) int D_Q ds` (so `eq:spacetime-scale` is an
identity), `int Q = (E/E_V)^2 b^{-2} int Q ds`, `int d_1^4 = O(b^{-1})`,
`int Y = O(b^{-1})`, `int Y^2 = b^3 int ||grad v||_2^4 ds`. `C_B` and `M_L`
reproduce `eq:qe-bernstein` and `eq:qe-lowstrain` exactly; `eq:quantifiers` and
`eq:critical-bound` reproduce `hyp:highstrain` and `eq:qe-M` exactly. Sarsa
Lemma 2.1 verified over 200000 random symmetric matrices (min slack `3.4e-8`)
and shown to imply `lem:matrix` by `2|Ae|^2 >= 2<e,Ae>^2` under
`tr A = -t <e,Ae>`, matching to machine precision at `t = 0.05, 0.3, 0.7, 1`.
Eleven refutation attempts, all failed (§6).

**REPLACEMENT ARGUMENT:** R1 (cite `prop:localtheory`(iii),(iv) and
`lem:upgrade`, text displayed in §7.1), R2 (cite `cp01`/`cp02`, add
Manfredi--Weitsman and Sibner--Sibner, and state that `lem:matrix` is a corollary
of Sarsa Lemma 2.1 with the reduction displayed in §7.2), R3 (restore the
`K`/`K_L` limitation and the qualitative-smallness sentence, §7.3), R4 (attribute
`eq:strainK` to `lem:quotient-transport`, §7.4). Two offered strengthenings with
proofs: §8.1, that `int Y^2` finite is itself an LPS regularity criterion, so the
absolute route is not merely insufficient but unusable; §8.2, that
`thm:spacetime`'s own family gives actual Navier--Stokes solutions with
`int Y -> 0` and `int Y^2 -> infinity` at the same rate `b^3` as `int K`, which
replaces the ledger's scalar illustration by a genuine one and shows
`eq:firstgap` is order-sharp.

**CONDITIONAL SUFFIX THAT SURVIVES:** §9. Unconditionally: the HF20
reconstruction at the audited scope; Theorem `thm:spacetime` in both halves; the
low-strain lemma; Proposition `prop:consumer` with its endpoint import; the
existential-remainder equivalence. Conditional on Scope A: `eq:remaining-sigma`
and the `int Y^2` boundary arithmetic. The first gap is unchanged; NS-R3 remains
open.

**UNNECESSARY DEPENDENCIES:** §10. Chiefly, the `K_L` half of `thm:spacetime`
follows from the `K` half plus the manuscript's `rem:highstrain-normalisation`,
which post-dates the candidate's pin; and the two-sided display is avoidable via
the HF20 audit's Lemma A. Surveys 1--3 are used nowhere that `cp01`/`cp02` do not
cover better.

**NON-CLAIMS:** §11. No Scope A statement is certified; no graph node moves; no
refutation of `hyp:highstrain` or `hyp:highpressure`; no singular solution; no
unbounded critical norm on a fixed trajectory; no novelty or priority claim; the
numerics are bounded evidence, never proof.

**REOPENING CONDITION:** §12, seven items; the two decisive ones are a Scope A
failure on `thm:main`/`cor:sigma`/`thm:mixed`, which removes `eq:remaining-sigma`
and §4 but leaves `sec:hf20`, `thm:spacetime`, `prop:consumer` and the low-strain
lemma standing; and any restatement of `thm:spacetime` with a cutoff or remainder
permitted to depend on the initial field, which would be a strictly stronger
claim that this argument does not support.
