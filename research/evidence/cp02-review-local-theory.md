# CP02 audit: review of the local-theory lane (round 1)

MODE: REVIEW, proof-audit discipline. Date: 2026-09-05. Owner of this file
only; nothing else was edited. Nothing here asserts HIGH-PRESSURE,
HIGH-STRAIN, CRITICAL, ABSORPTION, or NS-R3.

## 0. Freeze record

| item | value |
|---|---|
| candidate | `/home/ert/proj/navier/research/evidence/cp02-local-theory.md` |
| sha256 | `8bddb4031170d5c2949ae1c865b1092255716ebc2b7b61a7f1a95e8dc2c82d0b` |
| `git -C /home/ert/proj/navier rev-parse HEAD` | `715ce84ec78d64c510e150360a354b5d55648b9c` |
| manuscript read in full | `/home/ert/proj/navier-paper/main.tex` (562 lines) |
| CP01 records read in full | `cp01-manuscript-obligations.md`, `cp01-literature-statements.md` |

Primary source opened in this audit (not merely trusted from CP01): the
**complete published PDF** of Tao, *Anal. PDE* **6** (2013) 25--107 (86-page
file; journal page = PDF page + 23). This matters: the candidate's open
obligation 1 asserts that only a 6-page publisher sample was reachable. It
was not, and the missing page number is now pinned (see §5.1).

---

## VERDICT

**REPAIR** (minor; no invalid mathematical bridge; every claim of the
candidate survives).

The deliverable is mathematically sound. I reconstructed every proof from
its first nontrivial implication, recomputed every constant and exponent,
and verified the four imported Tao statements verbatim against the published
text. No step is false; no step is circular; the regularity package R of
(D2) really is *derived* rather than assumed. Three places, however, are
not valid *as literally written* (one of them ill-defined for half of a case
split), and one bibliographic non-claim is refuted by the source itself.
These require text changes before integration, so the verdict is REPAIR
rather than PASS. Complete replacements are supplied in §3.

---

## REVIEWED SCOPE

Audited in full: the four fenced LaTeX blocks (`\newtheorem` block,
`premise:local` replacement, `sec:localtheory`, the `thm:conditional`
sentence replacement) and the surrounding claims in §1, §3, §4, §5 of the
candidate.

Checked item by item:

- `lem:sobolev-norms`: multinomial identity
  `(1+|xi|^2)^k = sum_{|beta|<=k} c_{k,beta} xi^{2beta}` with
  `c_{k,beta} = C(k,|beta|)|beta|!/beta! >= 1` — recomputed, correct;
  both directions of the equivalence and
  `||d^alpha f||_{H^m} <= (2pi)^{|alpha|} ||f||_{H^{m+|alpha|}}` — correct.
- `lem:embedding`: `int (1+|xi|^2)^{-2} dxi = 4pi * (pi/4) = pi^2` —
  recomputed by the substitution `r = tan(theta)`, correct, so the embedding
  constant `pi` is right; the `H^m -> C^{m-2}_b` induction and the bound
  `pi (2pi)^{|alpha|} ||f||_{H^m}` — correct; part (c)
  `||f||_q <= ||f||_2^{2/q} ||f||_inf^{1-2/q}` — correct including `q = inf`.
- `lem:duality`: the test field `phi_R` is in `L^2`, is real-valued (real
  even multiplier plus Hermitian symmetry of `hat g`), and gives
  `<g,phi_R> = I_R = ||phi_R||_{H^{-k}}^2`, so `I_R <= C I_R^{1/2}` — the
  converse is correct, with monotone convergence.
- `lem:heat`: Gaussian normalisation `(4pi s)^{-3/2} e^{-|x|^2/4s}` has
  transform `e^{-4pi^2 s |xi|^2}` under `hat f = int e^{-2pi i x.xi} f` —
  recomputed, correct, and consistent with Tao's `(14)` symbol
  `-1/(4pi^2|xi|^2)` for `Delta^{-1}`; (K3)'s domination was rechecked for
  both signs of `h` (`h>0`: bracket in `[0,a]`; `h<0`, `|h|<=s`: bound `2a`
  via `e^{-as}(a + a e^{a|h|}) <= 2a`) — correct.
- `lem:restriction`, Steps 1--4 of `prop:localtheory`: the supremum/gluing
  construction uses only restriction plus Tao 5.4(i),(iii) and Corollary 5.8;
  no Duhamel concatenation is needed, and the case analysis of Step 3
  (`T' > S_*` excluded, `T' < S_*` contradictory, `T' = S_*`,
  `S_* not in T`) is exhaustive. Correct.
- `lem:upgrade`: the whole chain (scalar pairings and their measurability
  by Tonelli; the `L^inf` primitive claim `int a chi' = -int b chi ⟹ a = c +
  int_0^t b`; the countable-dense-`D` construction of the single null set;
  `eq:lip-offN`; uniform-continuity extension into `L^2`; `eq:pair-fte-all`;
  `H^k`-differentiability with error `M_{j+2,k}|h|`; joint smoothness by
  induction on `j+|alpha|` with `d_{x_i} U_{j,alpha} = U_{j,alpha+e_i}`,
  `d_t U_{j,alpha} = U_{j+1,alpha}`) — reconstructed and correct.
  Counterexample search: any `u` satisfying the hypothesis has all `u^{(j)}`
  a.e.-equal to Lipschitz `L^2`-valued curves, so no "nowhere continuous in
  `t`" example can satisfy it. The lemma is sharp for the use made of it.
- `lem:mild-classical`: the `L^2` pairing of `eq:tao-duhamel`, the
  `a(t') = <u(t'), e^{(t-t')Delta} phi>` differentiation, `eq:difference`,
  `u(0) = u_0`, and the `m_psi' = <H,psi> + m_{Delta psi}` bootstrap with
  `psi in H^4` — correct in substance; the `delta < 0` half of the
  difference-quotient computation is ill-defined as written (§2).
- `lem:pressure-convention`: the Cauchy--Schwarz-in-indices bound
  `|hat p| <= |hat w|` (using `sum_{i,j} xi_i^2 xi_j^2 = |xi|^4`), the
  symbol chain `-Delta^{-1} d_i d_j -> -xi_i xi_j/|xi|^2 = (-i xi_i/|xi|)
  (-i xi_j/|xi|)`, local integrability for Tao's `(14)`, `-Delta p =
  d_i d_j (u_i u_j)` in `S'`, and the Leibniz `H^k` bound — all correct, and
  exactly the (D1) convention. `||u (x) u||_2 = || |u|^2 ||_2 <=
  ||u||_inf ||u||_2` — correct.
- `lem:nu-scaling`: every formula recomputed. `d_s v = nu^{-2}(d_t u)`,
  `(v.grad)v = nu^{-2}((u.grad)u)`, `grad q = nu^{-2} grad p`,
  `Delta v = nu^{-1} Delta u = nu^{-2}(nu Delta u)`; hence the residual
  scales by the single factor `nu^{-2}`. `||v||_{L^2_s H^2([0,nu T'])}^2 =
  nu^{-1} ||u||_{L^2_t H^2([0,T'])}^2` — correct (this is the one norm whose
  power of `nu` is easy to get wrong). The Duhamel substitution giving
  `eq:nu-duhamel` is correct. The map agrees with the manuscript's existing
  `eq:nu-normalization` and with CP01 §7.2.
- `cor:Lq`, `lem:sup-esssup`, `lem:global-smooth`, `rem:continuation-shape`:
  correct. In particular `ess sup = sup` for a continuous function is right
  in the strong sense (the infimum over null sets of the restricted suprema
  equals the full supremum, because the complement of a null set is dense).
- Self-containedness: the LaTeX cites only `Tao2013`, `Fefferman2000`,
  `SteinWeiss1971`, `Rudin1987`, and refers to exactly two labels outside its
  own block (`eq:NS`, `thm:continuation`), both in `main.tex`. **No evidence
  file is referenced as proof anywhere in the LaTeX.** Verified mechanically.
- Compilation: I built the three splice blocks against the `main.tex`
  preamble plus the three new `\newtheorem` lines. 13 pages, **no undefined
  references, no multiply-defined labels**. (Eight overfull `\hbox`
  warnings; see §5.6 — the author's "zero warnings" claim is inaccurate.)
- (D1)--(D5) conformance: conventions, Riesz/pressure identity, the
  arbitrary-`nu` unforced equation on `R^3`, the retained-label list, the
  non-claims, and the "no preserved Schwartz decay" restriction are all
  honoured. `prop:localtheory`(iii) delivers exactly the (D2) package;
  `rem:continuation-shape` matches the (D3) route and correctly leaves the
  Leray--Hopf verification and the Serrin-type enstrophy bound to the
  continuation lane; nothing here touches (D4)'s `prop:pressure`.

Source checks (all against the complete published PDF, journal pagination):

| statement | location verified | verdict |
|---|---|---|
| Theorem 5.4 (i)--(v) | **pp. 52--53** | transcription in `thm:tao54` is verbatim-faithful; the four transcription notes (empty RHS of the `X^k` bound; spurious sixth tuple slot `,1`; `L^1_t` vs `L^inf_t` for `f`; `L^2_x` typo in (13)) are all confirmed in the published text |
| Corollary 5.8 + "incomplete mild `H^1` solution" | **p. 56** (Remark 5.9 on p. 57) | verbatim-faithful, including the `v`-for-`p` typo in the definition |
| Corollary 4.3 | **p. 47** | verbatim-faithful (see §5.1) |
| Definition 1.1 (smooth / `H^1` / Schwartz data, smooth solution) | pp. 26--27 | faithful |
| `H^1` solution condition (7); footnote 3 (`nu=1`) | p. 27 | faithful, quotation exact |
| (8), (9) normalised pressure | p. 28 | faithful |
| (10) Duhamel integral form | **p. 29** | faithful — and the candidate is right that this is `(10)`, correcting CP01 §1.1, which called it `(11)`; `(11)` is the Leray-projected form |
| `R^3` `H^1` mild solution definition; "almost smooth" definition; "the Schwartz property need not be preserved over time" | **p. 31** (the last sentence on p. 30) | faithful |
| (13) `X^s`, (14) `Delta^{-1}`, heat kernel, `H^s` norms | pp. 36--39 | faithful |
| "Unconditional uniqueness" corollary and the following remark conjecturing uniqueness for finite-energy data (`rem:tao-scope`(d)) | Tao §11, labels `unconditional`, `uniq` | **confirmed to exist and to say what the candidate says** |
| Theorem 1.12 (`rem:tao-scope`(d)) | p. 30 | faithful |
| moment footnote `int omega_1 (x_2^2 - x_3^2) dx` (`rem:tao-scope`(e)) | Tao **§3**, footnote after the time-translation symmetry (30), **p. 42** — *not* attached to the §1 sentence the candidate quotes | content correct, location misattributed (§5.4) |

---

## FIRST BAD BRIDGE

`lem:mild-classical`, proof, paragraph *The equation*, the justification of
`m_psi in C^1([0,T])`. The displayed difference quotient

```
delta^{-1}(m_psi(t+delta) - m_psi(t))
  = delta^{-1} int_t^{t+delta} h_psi(t', t+delta) dt'
    + int_0^t delta^{-1}( h_psi(t', t+delta) - h_psi(t', t) ) dt'
```

is followed by "`delta < 0` is identical". It is not. For `delta < 0` the
second integrand `h_psi(t', t+delta) = <H(t'), e^{(t+delta-t')Delta} psi>`
is **undefined** for `t' in (t+delta, t]`, because the heat semigroup is
defined only for nonnegative times; the domain of `h_psi` is the closed
triangle `{0 <= t' <= t <= T}`. The case is not dispensable: at `t = T`
only `delta < 0` is available, and `m_psi'(T)` is needed, since the
conclusion `<H(t), psi> = 0` is asserted for **every** `t in [0,T]`
(and `H(T) = 0` is used, via `prop:localtheory`(iv) on `[0,T]`, for
`t = T`).

Severity: **editorial-grade**. The conclusion is true and the left
derivative has the same value; only the display and one line of argument
must be rewritten. There is no bad bridge anywhere earlier: `lem:sobolev-norms`,
`lem:embedding`, `lem:duality`, `lem:heat`, `lem:restriction` and
`lem:upgrade` are all valid as written.

---

## REPLACEMENT ARGUMENT (complete)

### R1. The `delta < 0` case in `lem:mild-classical`

Replace the clause "`; $\delta<0$ is identical.`" by the following (LaTeX,
to be appended after the `delta > 0` sentence):

```latex
For $-t\leq\delta<0$ the corresponding decomposition is
\[
 \frac{m_\psi(t+\delta)-m_\psi(t)}{\delta}
 =\int_0^{t+\delta}\frac{h_\psi(t',t+\delta)-h_\psi(t',t)}{\delta}\,dt'
  +\frac1{|\delta|}\int_{t+\delta}^{t}h_\psi(t',t)\,dt',
\]
in which every value of $h_\psi$ that occurs has $t'\leq t+\delta$ or
$t'\leq t$, so all terms are defined.  The second term tends to
$h_\psi(t,t)$ by continuity of $h_\psi$ at $(t,t)$.  In the first, the mean
value theorem gives, for each $t'\leq t+\delta$, a $\theta\in(0,1)$ with
$(h_\psi(t',t+\delta)-h_\psi(t',t))/\delta=\partial_th_\psi(t',t+\theta
\delta)$, which is legitimate because $t'\leq t+\delta\leq t+\theta\delta$;
this converges to $\partial_th_\psi(t',t)$ uniformly in $t'$ by uniform
continuity of $\partial_th_\psi=h_{\Delta\psi}$ on the compact triangle, and
the missing slice $\int_{t+\delta}^t\partial_th_\psi(t',t)\,dt'$ tends to
$0$ because $\partial_th_\psi$ is bounded there.  Hence the left derivative
of $m_\psi$ at $t$ exists and equals $h_\psi(t,t)+\int_0^t\partial_t
h_\psi(t',t)\,dt'$, the same value as the right derivative.
```

Nothing downstream changes.

### R2. `lem:pressure-convention`(a),(d) are applied outside their stated scope

In Step 6 of `prop:localtheory` the candidate bounds
`|| R_iR_j( v_iv_j(s) - v_iv_j(s') ) ||_2` "by Lemma
`lem:pressure-convention`(a)". Part (a) is stated only for the argument
`u (x) u`; the difference of two such tensors is not of that form. The
required inequality *is* established inside the lemma's own proof (the
Cauchy--Schwarz-in-indices step never uses `w = u (x) u`), so the repair is
to state it. Replace parts (a) and (d) by:

```latex
\item[(a)] For every $w\in L^2(\R^3;\R^{3\times3})$ the field
$P[w]:=\sum_{i,j}R_iR_jw_{ij}$ obeys $\norm{P[w]}_{L^2}\leq\norm w_{L^2}$,
and $\norm{P[w]}_{H^k}\leq\norm w_{H^k}$ whenever $w\in H^k$.  In
particular $p=P[u\otimes u]\in L^2$ with $\norm p_{L^2}\leq
\norm{u\otimes u}_{L^2}\leq\norm u_{L^\infty}\norm u_{L^2}$;
```

and delete the now-redundant first sentence of (d), keeping only the
Leibniz estimate `||d^alpha(u_iu_j)||_2 < inf` that puts `u (x) u in H^k`.
The proof text needs no change beyond splitting its first sentence: the
pointwise bound `|hat P[w](xi)| <= |hat w(xi)|` is exactly what is proved.
Step 6 then reads "by Lemma~\ref{lem:pressure-convention}(a) applied to
$w=v\otimes v(s)-v\otimes v(s')$".

### R3. The "everywhere" in `prop:localtheory`(ii), almost-smooth case

Statement (ii) concludes `tilde u = u` **everywhere** on `[0,T] x R^3` for
an almost smooth competitor; Step 4 proves only "a.e.". Append to Step 4:

```latex
Since $\tilde v$ is almost smooth, $\tilde v$ is continuous on
$[0,T]\times\R^3$ (Definition~\ref{def:tao-mild}(b): $\nabla_x^k\tilde v$
is continuous there for every $k$), and $v$ is continuous by Step~5; two
continuous functions that agree almost everywhere agree everywhere, so
$\tilde v=v$ on $[0,T]\times\R^3$.
```

(Note the ordering: this sentence belongs after Step 5, or Step 4 must
forward-reference it. The cleanest fix is to move the almost-smooth half of
Step 4 to the end of Step 6.)

---

## CONDITIONAL SUFFIX THAT SURVIVES

Everything the candidate claims. Explicitly, with R1--R3 applied and with
Tao's Theorem 5.4(i)--(iv) (pp. 52--53), Corollary 5.8 (p. 56) and
Corollary 4.3 (p. 47) as the only imported theorems:

For every `nu > 0` and every divergence-free `u_0 in S(R^3)^3` there are a
unique `T_*(nu,u_0) in (0,inf]` and a unique smooth pair `(u,p)` on
`[0,T_*) x R^3` such that

1. `{T : an H^1 mild solution with viscosity nu and datum u_0 exists on
   [0,T]} = (0,T_*)` exactly, and `(u,p)` restricts to it on each `[0,T]`,
   `T < T_*`;
2. uniqueness holds in the exactly stated `H^1` mild class
   (`def:nu-mild`) and, through Corollary 4.3, among almost smooth `H^1`
   classical solutions with an arbitrary pressure;
3. `u, p in C^j([0,T];H^k)` for all `j,k >= 0` and all `T < T_*`, with all
   space-time derivatives bounded on `[0,T] x R^3`, i.e. the (D2) package R
   is a **theorem** of this section, not an assumption;
4. the equation, `div u = 0` and `u(0) = u_0` hold pointwise, and
   `p(t) = R_iR_j(u_iu_j)(t) = -Delta^{-1} d_i d_j (u_iu_j)(t)` = Tao's
   normalised pressure for **every** `t`, with `-Delta p = d_i d_j(u_iu_j)`;
5. `||u(t)||_{H^1} -> inf` as `t -> T_*` when `T_* < inf`;
6. `t -> ||u(t)||_3` is continuous, so `sup = ess sup = limsup`-boundedness
   on `[0,T_*)` (`lem:sup-esssup`), which is the (C-0) statement shape;
7. `T_* = inf ⟹ u,p in C^inf(R^3 x [0,inf))` in Fefferman's sense with the
   equation and `u(0) = u_0` pointwise (`lem:global-smooth`), which is (C-3).

Obligations L-1, P-1, C-3 and the C-0 statement shape are discharged at the
(D5) standard. Nothing in this lane bears on `hyp:highpressure`,
`hyp:absorption`, `hyp:critical`, `eq:quotient-gap`, or NS-R3.

Not discharged by this lane, and correctly flagged by it: the Leray--Hopf
verification of ESS (1.3)--(1.7) and the manuscript-owned Serrin-type
enstrophy bound (both continuation lane, (D3)). One caution for that lane:
`prop:localtheory`(iii) is uniform only on compact `[0,T]`, `T < T_*`; the
`L^inf(0,T_*;L^2)` and `L^2(0,T_*;H^1)` memberships that ESS (1.3) needs on
`Q_{T_*}` come from `prop:energy`, not from (iii). `rem:continuation-shape`
should say so.

---

## UNNECESSARY DEPENDENCIES

- `lem:heat`(K1)'s semigroup identity `e^{s Delta} e^{r Delta} =
  e^{(s+r)Delta}` is never used. Harmless; may be dropped.
- The explicit constants `c_{k,beta}` in `lem:sobolev-norms` are not used
  quantitatively; only the equivalence is. Keep them anyway — they are what
  resolves Tao's two competing `H^k` norms (§5.5).
- `lem:heat`(K0) (Gaussian kernel = multiplier) *is* necessary: Tao's
  `e^{tDelta}` in (10) is defined by the kernel formula (p. 39), so the
  identification is load-bearing, not decorative.
- No Calderon--Zygmund theory, no `L^p` Riesz-transform bound, no
  Littlewood--Paley theory, and no Leray projection on `L^p` is used
  anywhere in this lane. That is a real economy and should be preserved.
- Theorem 5.4(v) is genuinely unused; omitting it is right.

---

## NON-CLAIMS

This review asserts no regularity result, no critical bound, and no
Millennium result. It does not certify the pressure, energy/enstrophy,
quotient, or continuation lanes. The textbook facts (Plancherel, Fourier
inversion on `L^1 cap L^2`, the derivative multiplier, the Gaussian
transform, `L^1 * L^2` convolution, density and separability of `L^2`, the
fundamental lemma) were **not** re-verified in Stein--Weiss or Rudin and
remain [MO] at chapter level, exactly as the candidate records. ESS
Theorem 1.3, GKP Theorem 4, Kato, and Fefferman were not reopened in this
audit (CP01 records them [DI]).

---

## REOPENING CONDITION

Reopen this audit if any of the following changes: (i) the (D2) package or
(D3) continuation route is restated; (ii) `def:nu-mild` or
`prop:localtheory`(i) is weakened (the exact identity `T = (0,T_*)` is what
makes `prop:localtheory`(ii)'s `T < T_*` strict and is used by the
continuation lane); (iii) a lane starts needing `p in L^q` for `q < 2`, or
`u(t)` decay beyond `H^k` membership, either of which is outside what this
section supplies; (iv) the integrator resolves the label collisions of §5.7
in favour of the pressure lane's copies, in which case the two lemmas must
be re-checked for agreement.

---

## 5. Repairs and editorial issues for the integrator

### 5.1 The candidate's open obligation 1 is refuted by the source (fix required)

Corollary 4.3 is on **published page 47** of *Anal. PDE* 6 (2013) no. 1
(section 4, immediately before the start of section 5 on the same page).
The complete published PDF is reachable and was read in this audit; the
claim that only a 6-page sample exists is wrong. Replace
`\cite[Corollary~4.3, \S4]{Tao2013}` by
`\cite[Corollary~4.3, p.~47]{Tao2013}` and delete open obligation 1 from
the candidate's §4 and from its frontier record's FIRST GAP.

Same fix for the two other unpinned locations: the `R^3` `H^1` mild-solution
definition and the "almost smooth" definition are both on **p. 31**; Tao's
Duhamel `(10)` is displayed on **p. 29**; "the Schwartz property need not be
preserved over time" is the last sentence of **p. 30**.

### 5.2 `Corollary 5.8` page span

The statement of Corollary 5.8 and the preceding "incomplete mild `H^1`
solution" definition are entirely on **p. 56**; p. 57 carries only
Remark 5.9. Change `pp.~56--57` to `p.~56` in `cor:tao58` (and in the §3
facts table).

### 5.3 CP01 correction worth recording

CP01 `cp01-literature-statements.md` §1.1 attributes the Duhamel identity
`u(t) = e^{tDelta}u_0 + int_0^t e^{(t-t')Delta}(-(u.grad)u - grad p + f)`
to Tao's `(11)`. It is `(10)`; `(11)` is the Leray-projected form with
`P B(u,u)`. The candidate has it right. Not a defect of this lane, but the
literature record should be corrected so later lanes do not inherit it.

### 5.4 `rem:tao-scope`(e): footnote misattributed

The quoted sentence is in §1 (p. 30); the footnote about
`int omega_1(t,x)(x_2^2 - x_3^2) dx` is in **§3**, attached to the sentence
"time translation can instantly convert Schwartz data to non-Schwartz data"
after the time-translation symmetry (30), **p. 42**. Split the citation.
The mathematical content of (e) is unaffected and correct.

### 5.5 Tao has two `H^k` norms; say so

Tao defines both a classical norm `||u||_{H^k} = (sum_{j<=k}
||grad^j u||_2^2)^{1/2}` (for smooth `u`) and the Bessel norm
`(int (1+|xi|^2)^s |hat u|^2)^{1/2}`, and notes they "conflict slightly ...
but the two norms are equivalent up to constants" (p. 36). The candidate
writes "this is Tao's `H^s_x(R^3)`" for the Bessel norm without recording the
ambiguity. Since Theorem 5.4(iv)'s `L^inf_t H^k` could be read with either,
add a transcription note pointing at `lem:sobolev-norms`, which is precisely
the reconciliation (and shows both norms have the same finiteness set, so
(iv) is unambiguous for the use made of it). Also worth a note: Tao's
displayed `C^k_t X_x` *norm* on p. 37 is written with `grad^j` where
`d_t^j` is meant; the candidate uses only the "`k` times continuously
differentiable" clause, so nothing is load-bearing.

### 5.6 "Zero warnings" is inaccurate

My rebuild of the three splice blocks against the `main.tex` preamble plus
the three new `\newtheorem` lines produced 13 pages with no undefined
references and no multiply-defined labels, but **eight overfull `\hbox`
warnings**. The worst are the long inline displays in the conventions
paragraph, `lem:upgrade` Step 5, `lem:nu-scaling`(a) (77 pt over), and
Step 6 of `prop:localtheory`. Break those lines.

### 5.7 Cross-lane label collisions (blocking for the integrator)

`cp02-pressure.md` independently defines `\label{lem:embedding}` and
`\label{lem:pressure-convention}` with near-identical content. Splicing both
lanes verbatim yields multiply-defined labels and two copies of the same two
lemmas. Since `sec:localtheory` precedes the pressure section, the
local-theory lane should own both; the pressure lane's copies must be
deleted and replaced by references (its `(R1)--(R3)` package should become a
citation of `prop:localtheory`(iii) and `cor:Lq`). The two versions agree
mathematically where they overlap (same embedding constant `pi`, same
`int(1+|xi|^2)^{-2} = pi^2`, same symbol computation), so no reconciliation
of content is needed — only deduplication.

### 5.8 Smaller items

1. `def:nu-mild`, almost-smooth clause: the "explicitly" list omits that
   `u_0` must be smooth (it follows from continuity of `grad_x^k u` on the
   closed slab, but Tao's definition requires a *smooth set of data*). Add
   half a sentence.
2. `prop:localtheory` preamble says "a unique pair `(u,p)` of smooth
   functions"; the uniqueness assertion is proved in Step 7 only within the
   class of smooth pairs satisfying (i). That is what is meant, but the
   statement should say "unique among smooth pairs satisfying (i)".
3. The Tao imports are typeset as `theorem` while labelled `cor:tao58`,
   `cor:tao43`. Harmless; either relabel or use the `corollary`
   environment the lane already introduces.
4. §2.3's splice instruction is ambiguous: in `main.tex` the
   `prop:energy` sentence sits *between* the two sentences being replaced,
   so the replacement must be spliced in two places, not one. State the two
   insertion points explicitly.
5. `rem:continuation-shape` should add the caution in the CONDITIONAL
   SUFFIX above: (iii) is uniform only on compact subintervals; the
   `Q_{T_*}`-uniform memberships ESS needs come from `prop:energy`.
6. The frontier record's phrase "proved from the distributional bounds
   alone (so the reading of Tao's word 'smooth' is not load-bearing)" is
   defensible but should be sharpened: `lem:upgrade` does assume the
   distributional time derivatives *exist as functions* with those bounds,
   which is exactly Tao's `d_t^j u in L^inf_t H^k` assertion. What is not
   load-bearing is the *closed-slab* reading of "smooth".
7. `lem:sobolev-norms` and `lem:embedding` are stated for `R^N`-valued `f`;
   `lem:embedding`(a)'s `|hat f|` is the Euclidean norm of the vector. Say
   so once, since the Cauchy--Schwarz step depends on it.
8. The word "arXiv" appears once inside the LaTeX (transcription note 1).
   Acceptable, but a published paper normally says "in both the published and
   the preprint text".
