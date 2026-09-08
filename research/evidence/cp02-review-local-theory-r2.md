# CP02 audit: review of the local-theory lane (round 2)

MODE: REVIEW, proof-audit discipline. Date: 2026-09-05. Owner of this file
only; nothing else was edited, nothing was pushed. Nothing here asserts
HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION, or NS-R3.

## 0. Freeze record

| item | value |
|---|---|
| candidate | `../navier/research/evidence/cp02-local-theory.md` |
| sha256 | `cd6371c58eb542be8b21fa48eaedd19f679b9156384c91f64d68e84c240a4e56` |
| `git -C ../navier rev-parse HEAD` | `fc1ee2bcc7afbbef43bb41a9c5070009034e603f` |
| manuscript read in full | `../navier-paper/main.tex` (562 lines) |
| CP01 records read in full | `cp01-manuscript-obligations.md`, `cp01-literature-statements.md` |
| round-1 audit read in full | `cp02-review-local-theory.md` |
| cross-lane files inspected | `cp02-pressure.md` (label collision), `cp02-continuation.md` (C-0/C-3 interface) |

Primary sources opened in this audit (not trusted from CP01 or from round 1):
the **complete published PDF** of Tao, *Anal. PDE* **6** (2013) 25--107, read
at journal pp. 25--31, 35--39, 42, 47, 52--53, 56--57, 66--67, 82--84; and the
arXiv:1108.1165 LaTeX source (`ns.tex`) for the §11 corollary and for
transcription note (1).

**Pagination.** Journal page = PDF page **+ 23** (journal p. 25 is PDF p. 2).
The candidate's header states "+ 24". Every journal page number the candidate
actually cites is nevertheless correct (verified one by one, §"Source checks"
below), so this is a slip in the evidence log, not in the citations.

---

## VERDICT

**REPAIR** (minor; no invalid mathematical bridge; every mathematical claim
of the candidate survives).

Round 1's first bad bridge (R1, the `delta<0` half of the difference quotient
in `lem:mild-classical`) is **correctly and completely repaired**: I
reconstructed both one-sided derivative computations term by term, checked
that every argument of `h_psi` lies in the closed triangle
`Sigma = {0 <= t' <= t <= T}`, checked the mean value theorem is applied on
`[t+delta,t] subset [t',T]`, and checked the missing-slice estimate. R2 (the
`L^2`-tensor scope of `lem:pressure-convention`(a)), R3 (`a.e.` -> everywhere,
moved to the new Step 7 after continuity of `v` is available), and R4 (page
pinning) are also correctly applied, and every item of the round-1 audit's §5
is addressed.

Three places are still not valid *as literally written*, all of the same
species as round 1's R2 — a stated equivalence or pointwise conclusion whose
cited justification does not cover its stated scope:

1. `def:nu-mild`'s "Explicitly, by Lemma `lem:nu-scaling`: ... `p =
   R_iR_j(u_iu_j)`, and `eq:nu-duhamel` holds" is asserted as an unpacking of
   the definition, i.e. for **arbitrary** `H^1` mild competitors, but
   `lem:pressure-convention` is stated only for `u in L^2 cap L^inf` and
   `lem:nu-scaling`(e) only "whenever the integrals are Riemann integrals of
   continuous `L^2`-valued functions". Neither hypothesis is available for a
   competitor with merely `u(t) in H^1`.
2. `lem:mild-classical`'s final clause concludes `u(0,x) = u_0(x)`
   *pointwise* from smoothness of `u,p`; this needs `u_0` continuous, which
   is not among the lemma's hypotheses (it holds in the only application,
   where `u_0` is Schwartz).
3. §2.1 asserts "the Schwartz property of `u_0` is **not** preserved in
   time". Tao's source sentence, and `rem:tao-scope`(e), say "need not be
   preserved"; the universal negative is not proved anywhere and is a
   non-claim under (D5).

None of the three is load-bearing: item 1's clause is never used in either
direction (every proof uses the rescaling definition itself), item 2 is
satisfied in its single application, item 3 is a remark. All are text
changes; complete replacements are in §3. Because the paper text must be
correct as written, the verdict is REPAIR rather than PASS.

Two further items are cross-lane and blocking for the integrator (§5.1,
§5.2): the `lem:pressure-convention` label collision with `cp02-pressure.md`
(correctly flagged by the candidate) and a **newly found C-3 collision**:
`cp02-continuation.md` supplies a *complete replacement proof* of
`thm:conditional`, while this lane supplies two sentence-level insertions
into the *existing* `main.tex` proof. The two are mutually exclusive.

---

## REVIEWED SCOPE

Audited in full: the five fenced LaTeX blocks (the `\newtheorem` block, the
`premise:local` replacement, `sec:localtheory`, and the two `thm:conditional`
insertions), and §§1, 3, 4, 5, 6 of the candidate.

Reconstructed from the first nontrivial implication and found correct:

- `lem:sobolev-norms`: `(1+|xi|^2)^k = sum_{|beta|<=k} c_{k,beta} xi^{2beta}`
  with `c_{k,beta} = C(k,|beta|)|beta|!/beta! >= 1` (binomial + multinomial,
  recomputed); the identity holds in `[0,inf]` so both directions of the
  equivalence follow; `||d^alpha f||_{H^m} <= (2pi)^{|alpha|}
  ||f||_{H^{m+|alpha|}}` from `|(2pi i xi)^alpha|^2 <= (2pi)^{2|alpha|}
  (1+|xi|^2)^{|alpha|}`.
- `lem:embedding`: `int_{R^3}(1+|xi|^2)^{-2} dxi = 4pi(pi/4) = pi^2`
  (recomputed, `r = tan theta`), so the constant `pi` is right; (b)'s
  induction is correct at the edge cases `m = 2` (empty claim) and `m = 3`
  (one derivative), and uses `|xi|^2(1+|xi|^2)^2 <= (1+|xi|^2)^3` correctly;
  (c) is correct including `q = inf` (whose one-line proof is only implicit,
  §5.3).
- `lem:duality`: `phi_R` real-valued (real even multiplier + Hermitian
  symmetry), `<g,phi_R> = I_R = ||phi_R||_{H^{-k}}^2`, so `I_R <= C I_R^{1/2}`;
  monotone convergence. Correct.
- `lem:heat`: Gaussian normalisation `(4pi s)^{-3/2}e^{-|x|^2/4s} <->
  e^{-4pi^2 s|xi|^2}` under `hat f = int e^{-2pi i x.xi}f`, matching Tao's
  kernel on p. 39 and his `(14)` symbol on p. 38 (recomputed). (K3)'s
  domination rechecked for both signs of `h`: `h>0` gives bracket in `[0,a]`;
  `h<0` (so `|h| <= s`) gives `e^{-as}(a + a e^{a|h|}) <= 2a`. Correct.
- `lem:restriction`, and Steps 1--4 of `prop:localtheory`: the
  supremum-and-gluing construction uses only restriction plus Tao 5.4(i),(iii)
  and Corollary 5.8; no Duhamel concatenation. Step 3's case analysis
  (`T' > S_*` excluded by `(0,T') subset T`; `T' < S_*` contradictory;
  `T' = S_*`; `S_* not in T`) is exhaustive, and `S_* not in T` is derived
  from the blowup, not assumed. Correct.
- `lem:upgrade`: the `L^inf` primitive claim (`int a chi' = -int b chi` for
  all `chi` implies `a = c + int_0^t b` a.e., proved via `B(t) = int_0^t b`,
  Fubini using `chi(T) = 0`, and the `chi_0` normalisation), measurability of
  `a_j^phi` by Tonelli, the single null set from a countable dense
  `D subset C_c^inf`, `eq:lip-offN`, the uniform-continuity extension into
  `L^2`, `eq:pair-fte-all`, `H^k`-differentiability with error `M_{j+2,k}|h|`,
  and Step 5's induction on `j+|alpha|` (`d_{x_i}U_{j,alpha} =
  U_{j,alpha+e_i}` by `lem:embedding`(b) with `m = |alpha|+3`;
  `d_t U_{j,alpha} = U_{j+1,alpha}` by transporting the `H^{|alpha|+2}`
  convergence through `lem:sobolev-norms` and `lem:embedding`) — all correct,
  with Clairaut making the order of differentiation immaterial. The hypothesis
  is exactly the second half of Tao 5.4(iv), so the closed-slab reading of
  Tao's word "smooth" is genuinely not load-bearing.
- `lem:mild-classical`: `F, G in C_t L^2` (the product-rule split
  `u_j(t)d_j u(t) - u_j(s)d_j u(s) = (u_j(t)-u_j(s))d_j u(t) +
  u_j(s)(d_j u(t) - d_j u(s))` is correct), `eq:mild-paired` and its extension
  to all `t` by continuity, `a'(t') = <G(t'), e^{(t-t')Delta}phi>` by the
  product rule for the continuous bilinear pairing plus (K1) with
  `u(t') in H^2`, `eq:difference`, `u(0) = u_0` in `L^2`, and the
  `m_psi' = <H,psi> + m_{Delta psi}` bootstrap with `psi in H^4` — correct,
  and the repaired `delta<0` case is correct (see VERDICT). `H(T) = 0` is now
  genuinely available, which is what round 1 required.
- `lem:pressure-convention`: the Cauchy--Schwarz-in-indices bound
  `|hat P[w]| <= |hat w|` (using `sum_{i,j} xi_i^2 xi_j^2 = |xi|^4`), the
  symbol chain `-Delta^{-1}d_i d_j -> -xi_i xi_j/|xi|^2 =
  (-i xi_i/|xi|)(-i xi_j/|xi|)`, local integrability for Tao's `(14)`,
  `-Delta p = d_i d_j(u_i u_j)` in `S'`, `||u (x) u||_2 = |||u|^2||_2 <=
  ||u||_inf ||u||_2`, and the Leibniz `H^k` bound — all correct, and exactly
  the (D1) convention. The R2 repair is properly executed; the residual
  problem is only that the *hypotheses* are still too strong for the use in
  `def:nu-mild` (§3, R1).
- `lem:nu-scaling`: every formula recomputed. `d_s v = nu^{-2}(d_t u)`,
  `(v.grad)v = nu^{-2}((u.grad)u)`, `grad q = nu^{-2} grad p`,
  `Delta v = nu^{-1}Delta u = nu^{-2}(nu Delta u)`, so the residual scales by
  the single factor `nu^{-2}`; `||v||_{L^2_s H^2([0,nu T'])}^2 =
  nu^{-1}||u||_{L^2_t H^2([0,T'])}^2`; `d_s^j v(s) = nu^{-1-j}(d_t^j u)(s/nu)`;
  the Duhamel substitution `s = nu t`, `s' = nu t'` giving `eq:nu-duhamel`
  (the stray `nu dt'` and the final multiplication by `nu` both check out).
  Agrees with the manuscript's existing `eq:nu-normalization` and CP01 §7.2.
- Steps 5--9 of `prop:localtheory`: `v_0` Schwartz `=> v_0 in H^k` for all `k`
  (`(1+|x|)^{-4}` integrable on `R^3`, recomputed); the consistency of the
  smooth representatives `V^T` across `T`; `nabla . v = 0` upgraded from a.e.
  to pointwise through continuity; Step 6's continuity of
  `s -> P[v (x) v(s)]` using the tensor identity
  `a (x) a - b (x) b = (a-b)(x)a + b(x)(a-b)` and `|x (x) y| = |x||y|`;
  Step 7's `everywhere` conclusion (`tilde v` continuous by
  `def:tao-mild`(b) with `k=0`, `v` continuous by Step 5); Step 8's uniqueness
  of the pair and of `T_*`; Step 9's pull-back of (i),(ii),(iii),(iv),(v),(vi)
  through `eq:nu-map`. Correct.
- `cor:Lq`: `||g(t)-g(s)||_{L^q} <= ||.||_{L^2}^{2/q}(pi||.||_{H^2})^{1-2/q}
  <= pi^{1-2/q}||.||_{H^2}` — recomputed, correct for all `2 <= q <= inf`.
- `lem:sup-esssup`, `lem:global-smooth`, `rem:continuation-shape`: correct.
  `ess sup = sup` for a continuous function holds in the strong sense (the
  complement of a null set is dense). `lem:global-smooth`'s locality-in-`t`
  argument is correct and is exactly what C-3 asks for.
- **Self-containedness (checked mechanically).** The five blocks define 38
  labels and reference exactly four labels from outside (`eq:NS`,
  `def:target`, `prop:energy`, `thm:continuation`), all present in
  `main.tex`; they cite only `Tao2013`, `Fefferman2000`, `SteinWeiss1971`,
  `Rudin1987`. **No evidence file is referenced as proof anywhere in the
  LaTeX** (zero occurrences of any `cp0*` string inside the blocks).
- **Compilation.** I extracted the four content blocks and compiled them
  against the `main.tex` preamble plus the three new `\newtheorem` lines,
  with stubs carrying `eq:NS`, `def:target`, `prop:energy`,
  `thm:continuation`, `thm:conditional` and a four-entry bibliography: 15
  pages, no undefined references, no undefined citations, no multiply-defined
  labels, **one** overfull `\hbox` of `0.49 pt` (in the second
  `thm:conditional` insertion). The candidate's "zero overfull boxes" claim
  is accurate to within that half-point; §5.6 of round 1 is discharged.
- **(D1)--(D5) conformance.** Fourier and Riesz conventions, the pressure
  identity, the arbitrary-`nu` unforced equation on `R^3`, the retained-label
  list (`premise:local` is kept on the replaced paragraph; no retained label
  is redefined), the non-claims, and the "no preserved Schwartz decay"
  restriction are honoured, with the single overstatement noted above.
  `prop:localtheory`(iii)+(iv)+`cor:Lq` deliver exactly the (D2) package R;
  `rem:continuation-shape` matches the (D3) route, correctly leaves the
  Leray--Hopf verification and the Serrin-type enstrophy bound to the
  continuation lane, and correctly warns that the `Q_{T_*}`-uniform
  memberships come from `prop:energy`, not from (iii). Nothing here touches
  (D4)'s `prop:pressure`.

### Refutation attempts (all failed to break a claim)

1. *A `u` satisfying `lem:upgrade`'s hypothesis that is nowhere continuous in
   `t`.* Impossible: Step 2 forces every `u^{(j)}` to agree a.e. with a
   Lipschitz `L^2`-valued curve, and Lipschitz constants `M_{j+1,k}` are
   finite for every `k`. The lemma is sharp for the use made of it.
2. *`m_psi'(T)` unavailable, as in round 1.* Now available: the `delta<0`
   decomposition `m_psi(t) = int_0^{t+delta}h(t',t) + int_{t+delta}^t h(t',t)`
   keeps every argument inside `Sigma`, and both one-sided derivatives equal
   `h_psi(t,t) + int_0^t d_t h_psi(t',t)dt'`. Checked at `t = 0` and `t = T`
   separately.
3. *A mild competitor for which `q = -Delta^{-1}d_i d_j(v_i v_j)` fails to be
   `R_iR_j(v_iv_j)` because `v(t)` is not bounded.* The identity survives
   (`v(t) in H^1 subset L^2` gives `v (x) v(t) in L^1`, so Tao's `(14)`
   applies and the symbols agree), but **not by the lemma as stated** — this
   is repair R1, not a refutation of the mathematics.
4. *A mild competitor whose Duhamel integral does not rescale.* Also survives
   (for `u in X^1` one has `-(u.grad)u - grad p in L^4_t L^2_x subset
   L^1_t L^2_x` by Tao's `(24)`--`(25)`, so the integral is a Bochner integral
   in `L^2` and the affine substitution is valid), but again not by
   `lem:nu-scaling`(e) as stated. The recommended repair avoids importing
   `(24)`--`(25)` by making the explicit list one-directional (R1).
5. *`prop:localtheory`(ii)'s `T < T_*` strict inequality failing at
   `T = T_*`.* Impossible: Step 3 proves `T = (0,S_*)` exactly, with
   `S_* not in T`.
6. *A smooth pair satisfying (i) with a different `T_*`.* Impossible: (i)
   determines `T_*` as `sup T`, a function of `(nu,u_0)` alone.
7. *Circularity through the manuscript's hypotheses.* None: the section cites
   only `eq:NS` and (in remarks) `thm:continuation`, `prop:energy`,
   `def:target`; no hypothesis of the manuscript is used.

### Source checks (all against the complete published PDF unless noted)

| statement as used by the candidate | location verified | verdict |
|---|---|---|
| Theorem 5.4 (i)--(iv), verbatim | **pp. 52--53** | faithful. All six transcription notes confirmed: the `X^k` bound really is printed `.<=_{k,||u_0||_{H^k},||f||_{L^1_tH^k},1}` with an **empty right-hand side** (in the published text *and* in `ns.tex`); the spurious sixth tuple slot `,1` really appears in (i) and (iv); `H^1` data uses `L^inf_t H^1_x` while (ii) uses `L^1_t H^1_x`; `(13)` really prints `X^s := L^inf_t H^s_x cap L^2_x H^{s+1}_x`; the two `H^k` norms and the "conflicts slightly ... equivalent up to constants" sentence are on p. 36; the `C^k_t X_x` norm on p. 37 really is printed with `nabla^j` where `d_t^j` is meant |
| Corollary 5.8 + the "incomplete mild `H^1` solution" definition (with the `v`-for-`p` typo) | **p. 56**, Remark 5.9 on p. 57 | faithful, including `0 < T_* < T` in the second alternative |
| Corollary 4.3, verbatim | **p. 47** (last result of §4, immediately above the §5 heading) | faithful: "Let `(u,p,u_0,f,T)` be an almost smooth `H^1` solution. Then `(u,tilde p,u_0,f,T)` is a mild `H^1` solution, where `tilde p := -Delta^{-1}d_i d_j(u_i u_j) + Delta^{-1} nabla . f`. Furthermore, for almost every `t in [0,T]`, `p(t)` and `tilde p(t)` differ by a constant (and thus `nabla p = nabla tilde p`)" |
| Definition 1.1; `(1)`, `(3)`, `(4)` | pp. 26--27 | faithful |
| `(5)`, `(6)`, `(7)`, footnote 3 (`nu=1`) | **p. 27** | faithful; the footnote-3 quotation is exact, word for word, and no rescaling formula is given there (so `lem:nu-scaling` is genuinely owned by this paper) |
| `(8)`, `(9)` normalised pressure, footnote 4 | p. 28 | faithful |
| `(10)` Duhamel integral form; `(11)`, `(12)` | **p. 29** | faithful. The candidate's correction of CP01 §1.1 stands: the identity with `-(u.grad)u - grad p + f` is **(10)**; **(11)** is the Leray-projected form with `P B(u,u) + P f` |
| `R^3` `H^1` mild solution ("obeying `(4)`, `(1)`, and `(10)` (and thus `(11)`)"); the almost-smooth definition | **p. 31** | faithful in content; but Tao's concept is "almost smooth **finite energy** solution" and his `R^3` "`H^1` data" is defined only by the words "Similarly, define the concept of `H^1` data `(u_0,f,T)`" (§5.4, §5.5 below) |
| Theorem 1.12; "the incompressible nature of the fluid implies that the Schwartz property need not be preserved over time" | **p. 30** | faithful |
| §2 notation: Fourier convention p. 35; `H^s` norms p. 36; `L^p_t X_x`, `C^k_t X_x`, `(13)` p. 37; `(14)` and its domain p. 38; heat kernel p. 39 | **pp. 35--39** | faithful |
| footnote 12 (`int omega_1(t,x)(x_2^2-x_3^2)dx` not conserved but zero for Schwartz `u(t)`); "time translation can instantly convert Schwartz data to non-Schwartz data" | **§3, p. 42**, attached to the time-translation paragraph preceding the scaling symmetry `(31)` | faithful; the round-1 misattribution is repaired |
| Corollary "Unconditional uniqueness" and the following remark conjecturing uniqueness for finite-energy data | **Corollary 11.4, p. 84**; **Remark 11.5, p. 84** (§11 "Consequences of enstrophy localisation" begins on p. 83) | **now pinned** (closes the candidate's open obligation 3). Content check: Cor. 11.4 reads "Let `(u_0,f,T)` be smooth `H^1` data. Then there is at most one almost smooth finite energy solution `(u,p,u_0,f,T)` with this data and with normalised pressure." Remark 11.5 conjectures uniqueness when the data is "merely **smooth and** finite energy, rather than smooth and `H^1`" — so the candidate's phrase "merely finite-energy data" needs the word *smooth* (§5.4) |
| Fefferman `(6)`, data class (A) | not reopened | [DI] in CP01 §5 |
| Plancherel / Fourier inversion / derivative multiplier / Gaussian transform / `L^1 * L^2` / density and separability of `L^2` / fundamental lemma | **not** re-verified in Stein--Weiss or Rudin | remain **[MO]** at chapter level, exactly as the candidate records |

---

## FIRST BAD BRIDGE

`def:nu-mild`, the sentence beginning "**Explicitly, by
Lemma~\ref{lem:nu-scaling}:**".

The definition proper — "`(u,p)` is an `H^1` mild solution of `eq:NS` with
viscosity `nu` and datum `u_0` on `[0,T]` if `(v,q,v_0,0,nu T)` is an `H^1`
mild solution in the sense of `def:tao-mild`(d)" — is unimpeachable. The
following sentence, however, asserts an *equivalent* explicit description of
that class, for arbitrary members of it, and two of its four clauses are not
supported by the lemmas cited:

- `p = R_iR_j(u_iu_j)`. Via `lem:nu-scaling`(c) this reduces to
  `-Delta^{-1}d_i d_j(u_iu_j) = R_iR_j(u_iu_j)`, which is
  `lem:pressure-convention`(b). But (b) is stated only "for
  `u in L^2 cap L^inf(R^3;R^3)`, so that `u_i u_j in L^1 cap L^2`", and a
  member of this class has only `u(t) in H^1` for a.e. `t`. `H^1(R^3)` does
  **not** embed in `L^inf`.
- `eq:nu-duhamel` holds. `lem:nu-scaling`(e) proves the equivalence of the
  `nu`-form with Tao's `eq:tao-duhamel` only "whenever the integrals are
  Riemann integrals of continuous `L^2`-valued functions" (its proof
  substitutes in a Riemann integral after pairing with an element of `L^2`).
  For a competitor with merely `u in L^inf_t H^1_x cap L^2_t H^2_x` no such
  continuity is available, and Tao himself leaves the interpretation of
  `(10)` unspecified.

Both conclusions happen to be **true** (the pressure identity survives
because `u(t) in H^1 subset L^2` already gives `u (x) u(t) in L^1`, which is
all Tao's `(14)` needs; the Duhamel equivalence survives because for
`u in X^1` the forcing lies in `L^4_t L^2_x subset L^1_t L^2_x` by Tao's
`(24)`--`(25)`, making the integral a Bochner integral in `L^2`, for which
the affine substitution is again valid). So this is a **scope defect, not a
false step**, of exactly the species round 1 flagged as R2 — and it is not
load-bearing: `def:nu-mild` is used only through the rescaling definition
(in `prop:localtheory`(i),(ii) and Step 9), and the explicit list is used
nowhere in either direction. A mechanical check confirms `def:nu-mild` is
referenced by no other CP02 lane.

Severity: **editorial-grade**, but it must be fixed, because as written the
paper claims an equivalence it has not proved. There is no bad bridge
anywhere earlier: `lem:sobolev-norms`, `lem:embedding`, `lem:duality`,
`lem:heat`, `lem:restriction`, `lem:upgrade`, `lem:mild-classical` (including
the repaired `delta<0` case) and `lem:pressure-convention` are all valid as
written within their stated hypotheses.

---

## REPLACEMENT ARGUMENT (complete)

Three replacements, R1--R3, plus two exactness fixes R4--R5. R1 widens
`lem:pressure-convention` so that no new external fact is needed (in
particular **no** `H^1 -> L^6` Sobolev embedding and **no** import of Tao's
bilinear estimates `(24)`--`(25)`), and makes the explicit list in
`def:nu-mild` one-directional. Nothing downstream changes: `prop:localtheory`
Steps 6 and 7 apply the widened lemma under strictly stronger hypotheses than
before, and `cor:Lq`, `lem:sup-esssup`, `lem:global-smooth`,
`rem:continuation-shape` are untouched.

### R1. `lem:pressure-convention` widened to `L^1` tensors, and
### `def:nu-mild`'s explicit list made one-directional

Replace the whole of `lem:pressure-convention` (statement and proof) by:

```latex
\begin{lemma}[Normalised pressure]\label{lem:pressure-convention}
Define the Riesz transforms $R_j$ ($j=1,2,3$) as the Fourier multipliers
with symbols $-i\xi_j/|\xi|$, and for
$w\in L^1(\R^3;\R^{3\times3})\cup L^2(\R^3;\R^{3\times3})$ let $P[w]$ be the
tempered distribution
\[
 P[w]:=\sum_{i,j=1}^3R_iR_jw_{ij},\qquad\text{that is}\qquad
 \widehat{P[w]}(\xi)=-\sum_{i,j=1}^3\frac{\xi_i\xi_j}{|\xi|^2}\,
 \widehat{w_{ij}}(\xi)\qquad(\xi\neq0);
\]
the right-hand side is a locally integrable function in either case, by (a)
and (b) below, so $P[w]$ is well defined.  Then:
\begin{itemize}
\item[(a)] For every $w\in L^2$ one has $|\widehat{P[w]}(\xi)|\leq
|\widehat w(\xi)|$ for almost every $\xi$; hence $P[w]\in L^2$ with
$\norm{P[w]}_{L^2}\leq\norm w_{L^2}$, and $\norm{P[w]}_{H^k}\leq
\norm w_{H^k}$ whenever $w\in H^k$, $k\geq0$.
\item[(b)] For every $w\in L^1$ the right-hand side above is bounded by
$\sum_{i,j}\norm{w_{ij}}_{L^1}$.  In either case ($w\in L^1$ or $w\in L^2$),
Tao's definition \cite[(14), p.~38]{Tao2013} applies to
$\partial_i\partial_jw_{ij}$ and
\[
 P[w]=-\Delta^{-1}\partial_i\partial_jw_{ij}
\]
as tempered distributions.  For $w\in L^1\cap L^2$ the two descriptions of
$P[w]$ agree, and $P[w]\in L^2$.
\item[(c)] $-\Delta P[w]=\partial_i\partial_jw_{ij}$ in the sense of
tempered distributions.
\item[(d)] If $u\in L^2(\R^3;\R^3)$ then $u\otimes u\in L^1$ with
$\norm{u\otimes u}_{L^1}=\norm u_{L^2}^2$, so
$p:=P[u\otimes u]=R_iR_j(u_iu_j)$ is defined and is exactly Tao's normalised
pressure \eqref{eq:tao-pressure} with $f=0$.  If moreover $u\in L^\infty$
then $u\otimes u\in L^1\cap L^2$ and $p\in L^2$ with
$\norm p_{L^2}\leq\norm{u\otimes u}_{L^2}\leq
\norm u_{L^\infty}\norm u_{L^2}$.  If $u\in H^k$ for every $k$, then
$u\otimes u\in H^k$ and $p\in H^k$ with $\norm p_{H^k}\leq
\norm{u\otimes u}_{H^k}$ for every $k$.
\end{itemize}
\end{lemma}

\begin{proof}
(a) Cauchy--Schwarz in the indices gives, for $\xi\neq0$,
\[
 \Bigl|\sum_{i,j}\frac{\xi_i\xi_j}{|\xi|^2}\widehat{w_{ij}}(\xi)\Bigr|
 \leq\Bigl(\sum_{i,j}\frac{\xi_i^2\xi_j^2}{|\xi|^4}\Bigr)^{1/2}
 \Bigl(\sum_{i,j}|\widehat{w_{ij}}(\xi)|^2\Bigr)^{1/2}=|\widehat w(\xi)|,
\]
since $\sum_{i,j}\xi_i^2\xi_j^2=\bigl(\sum_i\xi_i^2\bigr)
\bigl(\sum_j\xi_j^2\bigr)=|\xi|^4$.  Multiplying the square of this
pointwise bound by $(1+|\xi|^2)^k$ and integrating gives
$\norm{P[w]}_{H^k}\leq\norm w_{H^k}$ for every $k\geq0$, the case $k=0$
being the $L^2$ bound (Plancherel).
(b) For $w_{ij}\in L^1$ one has $\norm{\widehat{w_{ij}}}_{L^\infty}\leq
\norm{w_{ij}}_{L^1}$ and $|\xi_i\xi_j|\leq|\xi|^2$, whence the stated bound;
a bounded measurable function is locally integrable, and so is the
$L^2$ function dominating the same expression when $w\in L^2$, by (a).  With
$\widehat{\partial_i\partial_jF}=(2\pi i\xi_i)(2\pi i\xi_j)\widehat F
=-4\pi^2\xi_i\xi_j\widehat F$ and Tao's
$\widehat{\Delta^{-1}F}=-(4\pi^2|\xi|^2)^{-1}\widehat F$, the right-hand
side of \cite[(14)]{Tao2013} for $F=\partial_i\partial_jw_{ij}$ is the
locally integrable function just bounded, so $\Delta^{-1}$ is defined on it
in Tao's sense, and
\[
 \widehat{-\Delta^{-1}\partial_i\partial_jw_{ij}}(\xi)
 =-\Bigl(\frac{-1}{4\pi^2|\xi|^2}\Bigr)(-4\pi^2\xi_i\xi_j)\,
 \widehat{w_{ij}}(\xi)
 =-\frac{\xi_i\xi_j}{|\xi|^2}\,\widehat{w_{ij}}(\xi)
 =\Bigl(\frac{-i\xi_i}{|\xi|}\Bigr)\Bigl(\frac{-i\xi_j}{|\xi|}\Bigr)
 \widehat{w_{ij}}(\xi),
\]
which is the symbol of $R_iR_j$ applied to $w_{ij}$; summing over $i,j$
proves the identity, and two tempered distributions with the same Fourier
transform coincide.
(c) $\widehat{-\Delta P[w]}(\xi)=4\pi^2|\xi|^2\widehat{P[w]}(\xi)
=-4\pi^2\xi_i\xi_j\widehat{w_{ij}}(\xi)
=\widehat{\partial_i\partial_jw_{ij}}(\xi)$; the middle expression is a
locally integrable function of at most polynomial growth, hence a tempered
distribution, so the identity holds in $\mathcal S'$.
(d) $|u\otimes u|=(\sum_{i,j}u_i^2u_j^2)^{1/2}=|u|^2$, which gives both
$\norm{u\otimes u}_{L^1}=\norm{|u|^2}_{L^1}=\norm u_{L^2}^2$ and, when
$u\in L^\infty$, $\norm{u\otimes u}_{L^2}=\norm{|u|^2}_{L^2}\leq
\norm u_{L^\infty}\norm u_{L^2}$; the identification with
\eqref{eq:tao-pressure} is (b).  If $u\in H^k$ for every $k$ then, by
Lemma~\ref{lem:embedding}, $u$ and all its derivatives are bounded, so by
the Leibniz rule $\norm{\partial^\alpha(u_iu_j)}_{L^2}\leq
\sum_{\beta\leq\alpha}\binom\alpha\beta
\norm{\partial^\beta u_i}_{L^\infty}
\norm{\partial^{\alpha-\beta}u_j}_{L^2}<\infty$; thus $u_iu_j\in H^k$ for
every $k$ by Lemma~\ref{lem:sobolev-norms}, and (a) applies with
$w=u\otimes u$.
\end{proof}
```

Then replace, in `def:nu-mild`, the sentence

> Explicitly, by Lemma~\ref{lem:nu-scaling}: $u\in L^\infty_tH^1_x\cap
> L^2_tH^2_x([0,T]\times\R^3)$, $\nabla\cdot u=0$, $p=R_iR_j(u_iu_j)$, and
> \eqref{eq:nu-duhamel} holds (with the integral interpreted as in Tao).

by

```latex
The rescaling is the definition; the following three consequences are the
only features of the class used in this paper, and no converse to them is
claimed or needed.
\begin{itemize}
\item[($\nu$1)] One has
\[
 u\in L^\infty_tH^1_x\cap L^2_tH^2_x([0,T]\times\R^3),
\]
and $\nabla\cdot u(t)=0$ in $L^2$ for almost every $t\in[0,T]$
(Lemma~\ref{lem:nu-scaling}(a),(b)).
\item[($\nu$2)] For almost every $t\in[0,T]$,
\[
 p(t)=R_iR_j(u_iu_j)(t)=-\Delta^{-1}\partial_i\partial_j(u_iu_j)(t).
\]
Indeed, $q(s)=-\Delta^{-1}\partial_i\partial_j(v_iv_j)(s)$ for almost every
$s\in[0,\nu T]$ by Definition~\ref{def:tao-mild}(d); both sides of that
identity are multiplied by $\nu^{-2}$ under \eqref{eq:nu-map}
(Lemma~\ref{lem:nu-scaling}(c) and the linearity of the multipliers), so
$p(t)=-\Delta^{-1}\partial_i\partial_j(u_iu_j)(t)$ for almost every
$t\in[0,T]$; and $u(t)\in H^1(\R^3)\subset L^2(\R^3)$ for almost every $t$,
so $u\otimes u(t)\in L^1$ and
Lemma~\ref{lem:pressure-convention}(b),(d) identifies that distribution with
$R_iR_j(u_iu_j)(t)$.
\item[($\nu$3)] If in addition $u\in C^1([0,T];L^2)\cap C([0,T];H^2)$ and
$p\in C([0,T];H^1)$, then \eqref{eq:nu-duhamel} holds for every
$t\in[0,T]$, the integral being the Riemann integral of a continuous
$L^2$-valued function (Lemma~\ref{lem:nu-scaling}(e) together with the
continuity of the integrand established in the proof of
Lemma~\ref{lem:mild-classical}).
\end{itemize}
```

(Nothing else in `def:nu-mild` changes; its almost-smooth clause is already
stated as an explicit unpacking of a pointwise condition, for which
`lem:nu-scaling`(a),(b) suffice.)

### R2. `lem:mild-classical`: the missing continuity hypothesis on $u_0$

In the statement, replace

> If moreover $u,p$ are smooth on $[0,T]\times\R^3$, the equation and
> $u(0,x)=u_0(x)$ hold pointwise on $[0,T]\times\R^3$.

by

```latex
If moreover $u,p$ are smooth on $[0,T]\times\R^3$, the equation holds
pointwise on $[0,T]\times\R^3$; and if in addition $u_0$ is continuous, then
$u(0,x)=u_0(x)$ for every $x\in\R^3$.
```

and, in the last sentence of the proof, replace "likewise $u(0,\cdot)=u_0$
pointwise, $u_0$ being continuous" by

```latex
likewise $u(0,\cdot)=u_0$ in $L^2$ with both sides continuous, hence
pointwise.
```

In Step 6 of `prop:localtheory`, the hypothesis is met: $v_0\in\mathcal
S(\R^3)^3$ is continuous. Add the four words "($v_0$ is continuous)" after
"Lemma~\ref{lem:mild-classical} gives $v(0,x)=v_0(x)$".

### R3. §2.1: remove the universal negative

In the `premise:local` replacement, replace

> the Schwartz property of $u_0$ is not preserved in time

by

```latex
the Schwartz property of $u_0$ need not be preserved in time
```

### R4. `rem:tao-scope`(d): pin the §11 corollary and correct its content

Replace item (d) by:

```latex
\item[(d)] Nothing is said about $L^3$ or any critical norm; the uniqueness
in (iii) is uniqueness \emph{within the class of $H^1$ mild solutions}
(Definition~\ref{def:tao-mild}(d)).  The class matters: Tao's Theorem~1.12
\cite[p.~30]{Tao2013} exhibits smooth $u_0\in H^1$ for which no smooth
finite energy solution exists for any $T>0$.  Tao's Corollary~11.4
(``Unconditional uniqueness'') \cite[p.~84]{Tao2013} extends (iii) to
almost smooth finite energy solutions with normalised pressure from smooth
$H^1$ data, and the Remark~11.5 following it \cite[p.~84]{Tao2013}
conjectures, but does not prove, uniqueness when the data is merely smooth
and of finite energy rather than smooth and $H^1$.  Neither is used below:
the almost-smooth uniqueness of Proposition~\ref{prop:localtheory}(ii) is
obtained from Theorem~\ref{thm:tao43} instead, and allows an arbitrary
pressure.
```

### R5. `def:tao-mild`(b) and `def:tao-data`: two transcription exactnesses

Replace `def:tao-mild`(b) by:

```latex
\item[(b)] Tao's concept is that of an \emph{almost smooth finite energy
solution}: it is the same as a smooth finite energy solution except that
$u,p$ are required to be smooth only on $(0,T]\times\R^3$, while for each
$k\geq0$ the functions $\nabla_x^ku$, $\partial_t\nabla_x^ku$,
$\nabla_x^kp$ exist and are continuous on $[0,T]\times\R^3$
\cite[p.~31]{Tao2013}; the equation \eqref{eq:tao-ns} is then still
interpreted in the classical sense.  We call such a quintuplet an
\emph{almost smooth $H^1$ solution} when its data is $H^1$ and it obeys the
$H^1$ condition (7) of (a); this is the reading of the term used in
Theorem~\ref{thm:tao43}, and it entails Tao's finite energy conditions,
since $u_0\in H^1_x(\R^3)$ and $f=0$ give
$E(u_0,0,T)=\frac12\norm{u_0}_{L^2}^2<\infty$, and (7) implies (6).
```

and append to `def:tao-data`, after the parenthesis on $H^1$ data:

```latex
(Tao's text at \cite[p.~31]{Tao2013} reads only ``Similarly, define the
concept of $H^1$ data $(u_0,f,T)$''; the display above is that definition
read off from the regularity hypotheses of his $\R^3$ mild solution on the
same page together with the divergence condition (1) imposed on the data in
the periodic case on p.~29.)
```

---

## CONDITIONAL SUFFIX THAT SURVIVES

Everything the candidate claims. Explicitly, with R1--R5 applied and with
Tao's Theorem 5.4(i),(iii),(iv) (pp. 52--53), Corollary 5.8 (p. 56) and
Corollary 4.3 (p. 47) as the only imported theorems, and with the textbook
facts of the candidate's §3 items 11--14 at [MO] chapter level:

For every `nu > 0` and every divergence-free `u_0 in S(R^3)^3` there are a
unique `T_*(nu,u_0) in (0,inf]` and a smooth pair `(u,p)` on `[0,T_*) x R^3`,
unique among smooth pairs satisfying (i), such that

1. `{T > 0 : an H^1 mild solution with viscosity nu and datum u_0 exists on
   [0,T]} = (0,T_*)` **exactly**, and `(u,p)` restricts to it on every
   `[0,T]`, `T < T_*`;
2. uniqueness holds in the exactly stated `H^1` mild class
   (`def:nu-mild`, a.e. equality) and, through Corollary 4.3, among almost
   smooth `H^1` classical solutions with an **arbitrary** pressure
   (everywhere equality of velocities; pressures equal up to a function of
   time for a.e. `t`);
3. `u, p in C^j([0,T];H^k)` for all `j,k >= 0` and all `T < T_*`, with every
   space-time derivative bounded on `[0,T] x R^3` and
   `d_t^j u, d_t^j p in L^inf_t H^k([0,T] x R^3)`, i.e. the (D2) package R is
   a **theorem** of this section, not an assumption;
4. the equation, `div u = 0` and `u(0) = u_0` hold pointwise on
   `[0,T_*) x R^3`, and `p(t) = R_iR_j(u_iu_j)(t) =
   -Delta^{-1} d_i d_j (u_iu_j)(t)` = Tao's normalised pressure for **every**
   `t`, with `-Delta p = d_i d_j (u_iu_j)` in `S'`;
5. `||u(t)||_{H^1} -> inf` as `t -> T_*` whenever `T_* < inf`;
6. `t -> ||u(t)||_3` is continuous on `[0,T_*)`, so `sup = ess sup =
   limsup`-boundedness there (`lem:sup-esssup`), which is the C-0 statement
   shape, and `cor:Lq` gives `u, grad u, Delta u, d_t u, p, grad p in
   C([0,T];L^q)` for every `2 <= q <= inf`;
7. `T_* = inf ==> u,p in C^inf(R^3 x [0,inf))` in Fefferman's sense, with the
   equation, `div u = 0` and `u(x,0) = u_0(x)` pointwise and
   `p = R_iR_j(u_iu_j)` (`lem:global-smooth`), which is C-3.

Obligations **L-1**, **P-1**, **C-3** and the **C-0 statement shape** are
discharged at the (D5) standard. Nothing in this lane bears on
`hyp:highpressure`, `hyp:absorption`, `hyp:critical`, `eq:quotient-gap`, or
NS-R3, and nothing in it is used to prove any of them.

Not discharged by this lane, and correctly flagged by it: the identification
of the branch with a Leray--Hopf weak solution in the ESS sense, and the
manuscript-owned Serrin-type enstrophy bound (both continuation lane, (D3)).
The caution it now carries is right and should be preserved:
`prop:localtheory`(iii) is uniform only on compact `[0,T]`, `T < T_*`; the
`L^inf(0,T_*;L^2)` and `L^2((0,T_*) x R^3)` memberships that ESS (1.3) needs
on `Q_{T_*}` come from `prop:energy`, not from (iii).

---

## UNNECESSARY DEPENDENCIES

- **Theorem 5.4(ii)** is not needed anywhere. Step 1 of `prop:localtheory`
  obtains `T != empty` from Corollary 5.8 alone and cites (ii) only
  parenthetically ("Theorem 5.4(ii) gives the same conclusion"). Keeping the
  transcription is informative; the parenthesis may go, and no proof depends
  on the small-data condition `(||u_0||_{H^1} + ||f||_{L^1_tH^1})^4 T <= c`.
  This is worth recording, because it means the lane needs **no quantitative
  local-existence time** at all.
- `lem:heat`(K1)'s clause "real-valued functions go to real-valued
  functions" is used only implicitly (all pairings are real by construction);
  it may stay as a sanity clause.
- `lem:sobolev-norms`'s explicit constants `c_{k,beta}` are not used
  quantitatively, only the equivalence — but they are precisely what
  reconciles Tao's two competing `H^k` norms (transcription note (6)), so
  they should stay.
- `lem:heat`(K0) (Gaussian kernel = multiplier) **is** necessary: Tao's
  `e^{tDelta}` in `(10)` is defined by the kernel formula (p. 39), so the
  identification is load-bearing.
- No Calderon--Zygmund theory, no `L^p` Riesz-transform bound, no
  Littlewood--Paley theory, no `L^p` Leray projection, and (after R1) still
  no `H^1 -> L^6` Sobolev embedding is used anywhere in this lane. That
  economy is real and should be preserved; note that the *manuscript* uses
  `||u||_6 <= C||grad u||_2` in `prop:scaling` and `prop:enstrophy`, so the
  economy is local to this section.
- Theorem 5.4(v), Remark 5.9, Theorem 1.12, Corollary 11.4 and Remark 11.5
  are genuinely unused; they appear only to delimit scope.

---

## NON-CLAIMS

This review asserts no regularity result, no critical bound, no absorption
estimate, and no Millennium result. It does not certify the pressure,
energy/enstrophy, low-pressure, quotient, or continuation lanes; it certifies
only `cp02-local-theory.md` at the freeze recorded in §0, subject to R1--R5.
ESS Theorem 1.3, GKP Theorem 4, Kato, and Fefferman were **not** reopened
here (CP01 records them [DI]). The textbook facts (Plancherel, Fourier
inversion on `L^1 cap L^2`, the derivative multiplier, the Gaussian
transform, `L^1 * L^2` convolution, density and separability of `L^2`, the
fundamental lemma) were **not** re-verified in Stein--Weiss or Rudin and
remain [MO] at chapter level. No statement is made about `u(t)` decay beyond
`H^k` membership for `t > 0`.

---

## REOPENING CONDITION

Reopen this audit if any of the following changes: (i) the (D2) package or
the (D3) continuation route is restated; (ii) `def:nu-mild` or
`prop:localtheory`(i) is weakened — the exact identity `T = (0,T_*)` is what
makes (ii)'s `T < T_*` strict and is used by the continuation lane; (iii) a
lane starts needing `p in L^q` for `q < 2`, or `u(t)` decay beyond `H^k`
membership, or a *converse* to `def:nu-mild`'s explicit list ($\nu$1)--($\nu$3),
none of which this section supplies; (iv) the integrator resolves the label
collision of §5.1 in favour of `cp02-pressure.md`'s copies, in which case
both lemmas must be re-checked for agreement; (v) the C-3 collision of §5.2
is resolved in favour of the continuation lane's Step 2, in which case that
lane's "(R2)" clause must be re-audited as a substitute for
`lem:global-smooth`.

---

## 5. Items for the integrator

### 5.1 Label collision `lem:pressure-convention` (blocking) — confirmed

`cp02-pressure.md` line 220 still defines
`\begin{lemma}[The normalised pressure]\label{lem:pressure-convention}`.
Splicing both lanes verbatim gives a multiply-defined label and two lemmas
with overlapping content. I read both copies: they agree mathematically
(same symbol computation `-xi_i xi_j/|xi|^2`, same use of Tao's `(14)`, same
`-Delta p = d_i d_j(u_iu_j)`), so only deduplication is needed. Since
`sec:localtheory` precedes the pressure section, this lane should own the
label; the pressure lane's copy must be deleted and its `(R2)--(R3)` list
replaced by citations of `prop:localtheory`(iii),(iv) and `cor:Lq` — which
its own parenthesis already anticipates. Note that the pressure lane's copy
derives `u_iu_j in L^2` from `u in L^4`, which the widened R1 version also
covers.

### 5.2 C-3 collision with the continuation lane (blocking) — new

`cp02-continuation.md` supplies a **complete replacement proof** of
`thm:conditional` (its Steps 1--5, including a Step 2 that reproves
smoothness on `R^3 x [0,inf)` from its own clause "(R2)"), whereas this lane
supplies **two sentence-level insertions** into the existing `main.tex` proof
of `thm:conditional`. If the continuation lane's replacement is spliced, the
sentences this lane quotes as insertion points no longer exist, and §2.3 is
inapplicable; if this lane's insertions are spliced, the continuation lane's
Steps 2--5 are duplicated. The integrator must choose one. Recommendation:
take the continuation lane's proof skeleton (it also discharges Fefferman's
(1)--(7) item by item) but have its Step 2, Step 3 and Step 5 cite
`Lemma~\ref{lem:global-smooth}` and `Lemma~\ref{lem:pressure-convention}` of
this section instead of its own "(R2)"/"convention paragraph", and drop §2.3
of this lane. `lem:global-smooth` is the better-supported vehicle: it proves
the locality-in-`t` step explicitly, which the continuation lane's Step 2
asserts.

### 5.3 Smaller items

1. Header pagination: "journal page = PDF page + 24" should read "+ 23"
   (journal p. 25 is PDF p. 2), and the header's "read as page images for
   ... 51--52 (Theorem 5.4)" conflicts with the §3 table's correct
   "pp. 52--53". Make the header quote journal pages throughout.
2. §3 table item 4 still hedges: "footnote 3 and (7) on p. 27 per CP01 and
   the round-1 publisher sample". Both are now directly verified on the
   published p. 27; drop the hedge and mark the row [DI] without
   qualification.
3. §4 item 3 (published page of the §11 corollary) is **closed**: it is
   Corollary 11.4, p. 84, with Remark 11.5 on the same page. Delete the open
   obligation and update `rem:tao-scope`(d) per R4.
4. `lem:embedding`(c)'s proof covers only `q < inf`; add "(the case
   $q=\infty$ is trivial)".
5. The label `subsec:conventions` is defined but never referenced; either
   reference it or drop it.
6. `def:tao-mild`(d)'s closing remark says the integral form is "Tao's (10),
   displayed on p. 29 for the periodic setting and invoked verbatim for
   $\R^3$ on p. 31" — correct, and worth adding that Tao's own cross
   references on p. 29 point at "(19)" and "(20)" where "(10)" is meant, so
   that a reader checking the source is not confused.
7. `rem:continuation-shape` writes `\sup_{0\leq t<T_*}` while
   `cp02-continuation.md`'s `thm:continuation` writes `\sup_{0<t<T_*}`;
   `lem:sup-esssup` proves them equal, but the two lanes should print the
   same form (recommend `0<t<T_*`, matching `eq:endpoint` in `main.tex`).
8. Step 1 of `prop:localtheory`: the parenthesis "(Theorem
   \ref{thm:tao54}(ii) gives the same conclusion.)" may be deleted (see
   UNNECESSARY DEPENDENCIES); if kept, note that it needs the smallness
   condition (46) whereas Corollary 5.8 needs nothing.
9. `prop:localtheory`(ii) says "$\tilde p=p$ almost everywhere on
   $[0,T]\times\R^3$"; Step 4 proves equality at almost every time in $L^2$,
   which gives a.e. equality on the slab by Tonelli. One clause ("hence
   almost everywhere on the slab, by Tonelli") makes this explicit.
10. Transcription note (1) says the empty right-hand side appears "in both
    the published and the preprint text" — I confirmed this directly in
    `ns.tex` as well as on p. 52; the note can cite both.

---

## 6. External facts used *by this review*

| # | fact | source | status |
|---|---|---|---|
| 1 | Tao, Theorem 5.4(i)--(v), including the empty-RHS `X^k` bound, the spurious `,1` tuple slot, the `L^1_t` vs `L^inf_t` mismatch | *Anal. PDE* 6 (2013), **pp. 52--53** | [DI] published PDF, read this round |
| 2 | Tao, Corollary 5.8 and the "incomplete mild `H^1` solution" definition (with the `v`-for-`p` typo); Remark 5.9 | **pp. 56--57** | [DI] |
| 3 | Tao, Corollary 4.3, verbatim | **p. 47** | [DI] |
| 4 | Tao, Definition 1.1, `(1)`--`(7)`, footnote 3 (`nu=1`, exact quotation), footnote 4, `(8)`--`(9)` | **pp. 26--28** | [DI] |
| 5 | Tao, `(10)`--`(12)` and the periodic mild-solution definition | **p. 29** | [DI] |
| 6 | Tao, Theorem 1.12 and "the Schwartz property need not be preserved over time" | **p. 30** | [DI] |
| 7 | Tao, the `R^3` almost smooth **finite energy** definition and the `R^3` `H^1` mild solution definition ("obeying (4), (1), and (10) (and thus (11))"); "Similarly, define the concept of `H^1` data" | **p. 31** | [DI] |
| 8 | Tao, §2 notation: Fourier convention (p. 35), the two `H^k` norms and "conflicts slightly ... equivalent up to constants" (p. 36), `C^k_t X_x` with the `nabla^j` slip and `(13)` with the `L^2_x` slip (p. 37), `(14)` and its domain (p. 38), heat kernel and `(19)` (p. 39) | **pp. 35--39** | [DI] |
| 9 | Tao, footnote 12 and "time translation can instantly convert Schwartz data to non-Schwartz data" | **§3, p. 42** | [DI] |
| 10 | Tao, Corollary 11.4 "Unconditional uniqueness" and Remark 11.5 (conjecture for smooth finite energy data); §11 heading and Corollary 11.1 | **pp. 83--84** | [DI] published PDF **and** arXiv:1108.1165 source (labels `unconditional`, `uniq`) |
| 11 | Tao, arXiv:1108.1165 LaTeX source, Theorem `lwp-h1-r3` (= 5.4) with the empty-RHS bound | arXiv source `ns.tex` | [DI] |
| 12 | `L^1 cap L^3 subset L^2` with `||f||_2 <= ||f||_1^{1/4}||f||_3^{3/4}` (used only in refutation attempt 3, not in the repairs) | Hölder interpolation, recomputed | [MO] |
| 13 | Plancherel, Fourier inversion, derivative multiplier, Gaussian transform, `L^1 * L^2`, density/separability of `L^2`, fundamental lemma, Tonelli/Fubini, dominated/monotone convergence, MVT, Riemann integrals of continuous Banach-valued functions | Stein--Weiss Ch. I; Rudin Ch. 3, 7; standard | [MO], chapter level, **not** re-verified |
| 14 | Fefferman's `(6)` and data class (A) | Clay problem description | [MO] here; [DI] in CP01 §5, not reopened |

---

## 7. Frontier record

**MODE / RESULT.** REVIEW (round 2), proof-audit discipline. Verdict
**REPAIR**: no invalid mathematical bridge; round 1's R1--R4 are correctly
repaired; three residual scope/exactness defects (R1--R3 above) and two
exactness fixes (R4--R5) must be applied before integration, and two
cross-lane collisions (§5.1, §5.2) are blocking for the integrator.

**CLAIM AND SCOPE.** The audit certifies that, with R1--R5 applied,
`cp02-local-theory.md` discharges L-1, P-1, C-3 and the C-0 statement shape
at the (D5) standard, and that the (D2) regularity package R is a *theorem*
of the section rather than an assumption; the surviving statement is items
1--7 of CONDITIONAL SUFFIX above. The certificate is conditional on Tao's
Theorem 5.4(i),(iii),(iv), Corollary 5.8 and Corollary 4.3 as stated on
pp. 47, 52--53, 56 of the published paper (all verified verbatim this round)
and on the [MO] textbook facts of item 13.

**EVIDENCE.** Complete published PDF of Tao 2013 read at journal
pp. 25--31, 35--39, 42, 47, 52--53, 56--57, 66--67, 82--84, plus the arXiv
source; every quoted statement, equation number, typo and page number
checked one by one (§"Source checks"); the pagination offset independently
determined as +23; every constant and exponent recomputed
(`int(1+|xi|^2)^{-2} = pi^2`, embedding constant `pi`,
`(2pi)^{|alpha|}`, `sum_{i,j}xi_i^2 xi_j^2 = |xi|^4`, `L^2_s H^2` scaling
`nu^{-1}`, `c_{k,beta} = C(k,|beta|)|beta|!/beta!`, `int_0^inf
r^2(1+r^2)^{-2}dr = pi/4`, `int(1+|x|)^{-4}dx < inf`); Step 3's case split
checked exhaustive; (K3)'s domination checked for both signs of `h`; the
`delta<0` decomposition in `lem:mild-classical` checked term by term with the
triangle membership of every argument of `h_psi`; seven refutation attempts
run and reported; the four content blocks recompiled (15 pages, no undefined
or multiply-defined labels, one 0.49 pt overfull box); label graph and
citation list extracted mechanically to confirm self-containedness; the
cross-lane copies in `cp02-pressure.md` and `cp02-continuation.md` read.

**FIRST GAP.** Mathematically none inside this lane. The first defect is the
non-load-bearing but unproved equivalence asserted by `def:nu-mild`'s
"Explicitly" clause (FIRST BAD BRIDGE), repaired in R1 without any new
external fact. The first *structural* gap is cross-lane: C-3 is discharged
twice, incompatibly (§5.2).

**SURVIVING CONDITIONAL SUFFIX.** With `prop:localtheory` in place the
paper's chain reads `hyp:highpressure => hyp:absorption => hyp:critical =>`
(`thm:continuation`, via `lem:nu-scaling` + the Leray--Hopf verification +
ESS Theorem 1.3 + the manuscript-owned Serrin-type enstrophy bound +
`prop:localtheory`(v)) `T_* = inf =>` (`lem:global-smooth` + `prop:energy`)
Clay alternative (A). The two links this lane does not own — the Leray--Hopf
verification, with the `Q_{T_*}`-uniform memberships taken from
`prop:energy`, and the Serrin-type bound — remain with the continuation lane
and are not certified here.

**NON-CLAIMS.** As in §NON-CLAIMS above: no regularity theorem, no critical
bound, no HIGH-PRESSURE / HIGH-STRAIN / CRITICAL / ABSORPTION / NS-R3
statement, no `L^3` uniqueness import, no certification of any other lane.

**NEXT DISTINCT ACTION.** Author of this lane: apply R1--R5 and the ten items
of §5.3 (a text-only round; no proof is affected). Integrator: resolve the
two blocking collisions of §5.1 and §5.2 before the splice. Literature lane:
correct CP01 §1.1's "(11)" to "(10)", record the pagination offset +23, add
Corollary 11.4 / Remark 11.5 (p. 84) to `cp01-literature-statements`, and pin
theorem numbers for the [MO] textbook items 13.
