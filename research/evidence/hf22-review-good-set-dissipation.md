# Audit of HF22-C: the dissipation on the good set of times

Proof audit of `research/evidence/hf22-good-set-dissipation.md`, 2026-09-06.
Owned file: `research/evidence/hf22-review-good-set-dissipation.md`. Nothing
else in the repository is edited; nothing is committed or pushed; the
manuscript is untouched.

**Target frozen.** `research/evidence/hf22-good-set-dissipation.md`,
`sha256 = 0221d30c8bbe5620f86b6226 …` (full:
`827d1c5116a0c4070adca5013ae4333852cb61580221d30c8bbe5620f86b6226`), 646 lines.
Repository HEAD at audit time: `e36fec455e970a004519e5c91b856a3e1bba28bc`
(`/home/ert/proj/navier`, branch `main`, clean). Manuscript frozen at
`/home/ert/proj/navier-paper` HEAD `4084330f6b8130241c7afbde3878861229c4cceb`.

**Sources directly inspected [DI].** The target in full; `PLAN.md` lines
1006–1050 and 1124–1211; `../navier-paper/main.tex` §`sec:quotient` and the
labels `prop:scaling`/\eqref{eq:L4L3} (2227–2258), `thm:continuation` (4664),
`lem:quotient-coercive`/\eqref{eq:cp-coercive} (5454), `rem:distance-balance`
(6768), `lem:quotient-lowstrain` (6790 ff.), `prop:quotient-evolution` (6698),
`hyp:highstrain` (6843), `rem:highstrain-normalisation` (6875),
`prop:quotient-conditional` (6901), `rem:highstrain-scope` (6952),
`rem:no-monotone` (6983); `research/evidence/hf21-crossing-sign-structure.md`
(audited REPAIR, repairs applied) §0 facts (Q3), (Q5), (Q6), (P1), (3.1),
Lemma 4.3, Theorem 4.5, Lemma R3, O1, O2, O3;
`research/evidence/hf20-harmonic-strain-test.md` (Theorem 1.1′, closing block).
HF23 was **not** used as a premise anywhere, and is not needed for anything
below. No (H1)-type regularity is assumed anywhere in this audit.

---

## VERDICT

**REPAIR.** The mathematics of Theorems A, B and D is correct as written and
survives verbatim. Theorem C — the load-bearing negative result, the one on
which the lane's entire meta-claim rests — rests on a **false auxiliary claim
about the constraint set**, and the family as displayed **violates a genuine
constraint that the audited record does impose**. The failure is confined to
the tail and smoothing intervals on which the note sets `D ≡ 0`; a replacement
family is displayed in §R1 below with its proof and a numerical confirmation,
and with it the negative conclusion survives in a weakened, honest form:
non-derivability from an **explicitly listed** set of consequences of the
audited record, not from "the audited record" as such.

Three further defects are scope/attribution defects rather than invalid
mathematics, and all three matter because this lane advertises a decision:

- **S1.** MODE/RESULT item 1 asserts falsity ("There is no input-only bound
  for ∫_{G_δ}D_3(w)dt"), which the note's own NON-CLAIMS block and its own
  Theorem D contradict. Must be restated as non-derivability.
- **S2.** Theorem D is **not new**: it is the manuscript's own
  `rem:highstrain-scope` equivalence, with the same two-line proof, transported
  from `hyp:highstrain` to (G). This is exactly the HF21-B defect B3 pattern
  ("correct but not new"), and the same remedy applies.
- **S3.** The O1(c) sharpening says the Hölder route needs a hypothesis
  "stronger than the conclusion"; the HF21-B audit explicitly downgraded that
  wording to "at least as strong". The downgrade must not be reverted.

The first gap is unchanged and is not closed by this lane. (G) is neither
proved nor refuted here, and nothing in this audit bears on `hyp:highstrain`,
`hyp:highpressure`, `hyp:absorption`, `hyp:critical` or NS-R3.

---

## REVIEWED SCOPE

Everything in the target was reconstructed from its first nontrivial
implication:

| Item | Status |
|---|---|
| §0 (A1)–(A7), (0.1), (0.2), target (G) | **verified**, constants recomputed |
| §1 Theorem 1.1, (1.1), (1.2), scaling check | **verified**, faithful transcription of HF21-B Thm 4.5 + Lemma 4.3 |
| §2 Theorem A, (2.1), (2.2), remarks 2.1–2.3 | **verified**, including the claimed sharpening of Lemma R3 |
| §3 Theorem B, (3.1), items 1–3, (3.2), δ=½ constants | **verified**, all constants recomputed |
| §4 constraint list (T1)–(T7) | **DEFECTIVE**: (T7) is not vacuous; the list is not exhaustive and the exhaustiveness claim is not needed |
| §4 Theorem C items 1–6 and the arithmetic verification | **items 1–6 verified as arithmetic**, but the family violates the corrected constraint (T8) on `(2nℓ,2)` and on the smoothing ramps; **repaired in §R1** |
| §4 the two refuted Hölder routes | **verified**, including the exponent count `2/4+3/9 = 5/6 < 1`; one wording regression (S3) |
| §5 Theorem D, Corollary D.1, the meta-claim | **theorem verified; novelty claim refuted** (S2); the meta-claim survives with the quantifier repair in §R3 |
| §6 open question and two leads | **verified as posed**; correctly identifies the single structure the family exploits |
| closing block | **verified** except the two overclaims inherited from S1 and S2; the two different normalisations of `A_B` in §3.1 and in SURVIVING CONDITIONAL SUFFIX are both internally correct |

Recomputed constants that check out exactly: `C_♯ = (3/2)C_9 S` (HF21-B (3.1));
`κ = 3^{1/3}(1+C_ℙ)C_♯ = C_*` of HF18-A (Q6) — the note's (0.1) is the audited
size bound, not a new one; `∫_0^τ‖q‖_3^4 ≤ 16∫‖u‖_3^4 ≤ 24C_S^2E_0^2/ν`
(\eqref{eq:L4L3} gives `3C_S^2‖u_0‖_2^4/(2ν)` and `16·3/2 = 24`);
`A_4 = 24C_S^2C_♯^4E_0^2/ν`; `|B_δ| ≤ 24C_S^2C_♯^4E_0^2δ^{-4}ν^{-5}` and its
value `384 C_S^2C_♯^4E_0^2ν^{-5}` at `δ = ½`;
`A_Q = ⅓H^{1/4}(3C_S^2E_0^2/(2ν))^{3/4}` verbatim from
`rem:highstrain-normalisation`; `δ/(1-δ) + 1 = 1/(1-δ)`.

Quantifier, space and class checks that pass: every statement is about the
classical branch of `prop:localtheory` from a divergence-free Schwartz datum
on `ℝ^3`, unforced, full viscosity; `Q ∈ C^1` and `D_Q`, `K` continuous on
compact subintervals of `[0,T_*)` are used only there; `D_3(w)` (HF18-A) is
never confused with `D_3(u)` (`def:D3P3`), and `rem:distance-balance` is
respected — no inequality between them is used. HF18-B is not a premise, and
no approximate-gradient statement is upgraded: the note's only HF18-B-adjacent
uses are absent. The Hölder-½ modulus of `‖q‖_3` is used **only** for
continuity (openness of `B`, finiteness on compacts), never with an input-only
constant, and the note flags this correctly at (A7) and in §6.

---

## FIRST BAD BRIDGE

**§4, the constraint list, item (T7):**

> "(T7) `D ≥ (8/(9S^2C_9^3))‖u‖_9^3 ≥ 0` — HF18-A (Q6); **as a constraint on
> the triple this is vacuous, since it only bounds `D` from below by a quantity
> not otherwise constrained.**"

and the sentence it supports, immediately above:

> "Along the classical branch the audited record imposes, on the triple
> `(Q,c,D)` … **exactly the following, and nothing else that couples the
> three**."

Both clauses are false. `‖u‖_9` **is** otherwise constrained by the audited
record: it is bounded **below** by `Q` through log-convexity of `L^p` norms,
the energy bound (P1) and the coercivity (Q3). The audited record therefore
imposes a genuine `D`–`Q` coupling that the list omits, and the family of
Theorem C **violates it** on the interval `(2nℓ,2)`, where the note sets
`c = D = K = 0` while `Q ≡ Q_0 > 0`, and again on every smoothing ramp, where
the note's regularisation paragraph sets `D ≡ 0` "so `Q' = 0` there".

### The omitted constraint, with proof

**(T8)** For the classical branch, at every `t < T_*`,
\[
 D_3(w(t))\ \ge\ \gamma\,\mathcal Q(u(t))^{7/3},
 \qquad
 \gamma:=\frac{8\cdot3^{1/3}}{S^2C_9^3E_0^2}\ >\ 0 .
\]

*Proof.* All four ingredients are audited. (i) (Q6) of HF21-B §0 (HF18-A,
audited PASS): `‖w‖_9^{3/2} = ‖V‖_6 ≤ S‖∇V‖_2`, `‖u‖_9 ≤ C_9‖w‖_9`, and
`D_3(w) ≥ (8/9)‖∇V‖_2^2`; combining,
`D_3(w) ≥ (8/(9S^2C_9^3))‖u‖_9^3`, which is the note's own (T7). (ii)
Log-convexity of `L^p` norms with `1/3 = (4/7)/2 + (3/7)/9`:
`‖u‖_3 ≤ ‖u‖_2^{4/7}‖u‖_9^{3/7}`, hence `‖u‖_9^3 ≥ ‖u‖_3^7/‖u‖_2^4`.
(iii) `prop:energy` (P1): `‖u(t)‖_2^2 ≤ E_0`, hence `‖u‖_2^4 ≤ E_0^2`.
(iv) `lem:quotient-coercive` \eqref{eq:cp-coercive}: `Q ≤ ⅓‖u‖_3^3`, hence
`‖u‖_3^7 = (‖u‖_3^3)^{7/3} ≥ (3Q)^{7/3}`. Chaining,
`D_3(w) ≥ (8/(9S^2C_9^3))·3^{7/3}Q^{7/3}/E_0^2` and
`3^{7/3}/9 = 3^{1/3}`. □

*Scaling check.* With the HF21-B §0 conventions `u ↦ λu(λ·)`: `Q` is
invariant, `D_3(w) ∼ λ^2`, `E_0 ∼ λ^{-1}` so `γ ∼ λ^2`. Both sides of (T8)
carry `λ^2` and `a^3·a^{... }` consistently — `D ∼ (a^3,λ^2)`,
`γQ^{7/3} ∼ (a^{-4}·a^{7},λ^{2}) = (a^3,λ^2)` ✓.

A second omitted constraint, harmless but worth listing so that the repaired
statement is honest:

**(T9)** `∫_0^τ Q^{4/3}dt ≤ 3^{-1/3}C_S^2E_0^2/(2ν)`, `τ`-uniform — from
`Q ≤ ⅓‖u‖_3^3` and \eqref{eq:L4L3} directly; it is strictly stronger than the
note's (T4), which is the same bound after one time-Hölder step
(`rem:highstrain-normalisation`).

### Why this is a bad bridge and not a typo

The lane's headline is a **derivability** claim, and a derivability claim is a
statement about a constraint *set*. Declaring a listed constraint vacuous, and
declaring the list exhaustive, are the two steps that convert "the family
beats these seven inequalities" into "no proof from the audited record can
exist". The first is false and the second is unproved (and, by (T8) and (T9),
false as stated). Without repair, Theorem C's family is not a counterexample
to derivability from the audited record: it is not even a member of the
constraint set the audited record defines.

---

## EVIDENCE

**1. The violation is real and is not a boundary artefact.** In the displayed
family with `ν = 1`, on `(2nℓ,2)` one has `D ≡ 0` and `Q ≡ Q_0 ≥ 1`, so (T8)
demands `0 ≥ γQ_0^{7/3} > 0`. The interval has length `2 - 2/n`, i.e. **most
of the time axis** for large `n`, which is the regime the whole argument uses.
The same violation recurs on each of the `2n` smoothing ramps of the
"Regularity of the data" paragraph, which are introduced precisely to make
`Q ∈ C^1` — so the violation survives the note's own regularisation.

**2. Everything else in Theorem C is arithmetically correct.** Recomputed
independently: on `I_k^-`, `Q' = -Q_0/ℓ + 2Q_0/ℓ = +Q_0/ℓ`, increment `+Q_0`;
on `I_k^+`, `Q' = -Q_0/ℓ`, increment `-Q_0`; `|K| ≤ cD` with equality on
`I_k^-` and `0 = 0` on `I_k^+`; `∫_0^2c^4 = 16nℓ = 16/n`; `∫_0^2c^3 = 8/n`;
`∫_0^2 Q ≤ 4Q_0`; `|B_δ| = nℓ = 1/n` for every `δ ∈ (0,1]` since `c ∈ {0,2}`;
`∫_{G_δ}D ≥ nQ_0`. The pointwise coupling holds: with
`Q_0 = max{1,(2/κ)^3}` one has `κQ_0^{1/3} ≥ 2 = c` and `Q ≥ Q_0`.
Theorem A on the family: LHS `= nQ_0`, RHS `= Q_0 + nQ_0`, ratio `→ 1` — the
sharpness claim of §2 is correct.

**3. Refutation attempts that failed** (i.e. the note survives them):

- *Does (T8) or (T9) kill the repaired family?* No. Both are lower bounds on
  `D` or bounds on `∫Q^{4/3}`, and the family's `D` on the spikes is `Q_0n^2`,
  far above `γ(3Q_0)^{7/3}`, while `Q` stays in a fixed compact interval. Only
  the `D ≡ 0` intervals were in conflict, and they are inessential.
- *Does HF20's sign structure forbid `K = +cD` on the bad phase?*  No — it
  supports it. `rem:no-monotone` / HF20 Theorem 1.1′ give the two-sided
  certificate: `K` takes both signs, and
  `sup{K - βνD_Q : ‖v‖_2^2 = E} = +∞` for every `β ≥ 0`. There is no audited
  sign constraint on `K` beyond `|K| ≤ cD`, so the bad phase is not excluded.
- *Is the family a single trajectory in disguise, so that the Hölder-½ modulus
  of `‖q‖_3` applies with one constant?* No, and the note is right to say so:
  the members are indexed by `n`, and (A7) supplies no input-only constant.
  This is the honest crux, and §6 identifies it correctly as the unique
  structure the family exploits.
- *Can all members share one input tuple?* Yes — this is required for the
  refutation to bite and the note leaves it implicit. Fix `ν = 1`, choose a
  divergence-free Schwartz `u_0` with `⅓‖u_0‖_3^3 ≥ 3Q_0` and
  `E_0 = ‖u_0‖_2^2` large, and `H > 2`; then `A_4 ≥ 16`, `A_Q ≥ 12Q_0` and
  `γ(3Q_0)^{7/3} ≤ Q_0/4` all hold simultaneously, for all `n` at once, because
  `A_4` and `A_Q` increase and `γ` decreases in `E_0`.
- *Does the Hölder route survive the family?* No. Recomputed:
  `(∫c^4)^{1/4}(∫_{B}D^{4/3})^{3/4} = (16/n)^{1/4}(n^{5/3}Q_0^{4/3})^{3/4}
   = 2nQ_0 = ∫_B cD`, exactly — Hölder is saturated and diverges. The note's
  claim is correct and in fact exact, not merely asymptotic.
- *Is the subcriticality claim right?* Yes. `D ∈ L^{4/3}_t` with (T7) gives
  `∫‖u‖_9^4 < ∞`, i.e. `u ∈ L^4_tL^9_x`, and `2/4 + 3/9 = 5/6 < 1`: strictly
  inside the Ladyzhenskaya–Prodi–Serrin region, so classical Serrin (not the
  ESS endpoint) already yields regularity. The route is therefore closed by a
  hypothesis that implies the conclusion. Only the wording is wrong (S3).

**4. Numerics (evidence, never proof).** The repaired family of §R1 was
integrated segment-by-segment with `ν = 1`, `κ = 1` (so `Q_0 = 8`), `S = C_9 = 1`,
`E_0 = 10^3` (so `γ = 1.154·10^{-5}`), `n ∈ {1,4,16,64,256,1024}`. Every
constraint (T1)–(T9) held on every segment (zero (T8) violations), with
`Q(0) = 8.038` fixed, `Q ∈ [8.000, 16.039]`, `∫c^4 = 16/n → 0`,
`∫Q ≤ 24.1`, `∫Q^{4/3} ≤ 56.5`, `|B_δ| = 1/n → 0`, and
`∫_{G_δ}D = 8n → ∞` (8192 at `n = 1024`), with the Theorem A ratio
`0.499, 0.800, 0.941, 0.985, 0.996, 0.999 → 1`. Script kept in session
scratch only; it is reproducible from the displayed family in three lines and
nothing below depends on it.

---

## REPLACEMENT ARGUMENT

### R1. Repaired Theorem C

**Theorem C′ (explicit family; the good-set dissipation is not controlled by
(T1)–(T9)).** Fix `ν = 1` and any `κ > 0`; put `Q_0 := max{1,(2/κ)^3}` and
`τ = 2`. Fix any input tuple `(ν,u_0,H)` with `H > 2`,
`⅓‖u_0‖_3^3 ≥ 3Q_0` and `E_0 = ‖u_0‖_2^2` large enough that
\[
 D_\flat\ :=\ \gamma\,(3Q_0)^{7/3}\ \le\ \tfrac14 Q_0 ,
 \qquad \gamma=\frac{8\cdot3^{1/3}}{S^2C_9^3E_0^2},
\]
which is possible because `γ ↓ 0` as `E_0 ↑ ∞` while `A_4`, `A_Q` of (T3),
(T4) increase in `E_0`. For each integer `n ≥ 1` put `ℓ := n^{-2}` and define
on `(0,2)`:
\[
 \begin{aligned}
 &\text{bad phase } I_k^-=((2k-2)\ell,(2k-1)\ell): && c\equiv2,\quad D\equiv Q_0/\ell,\quad K=cD,\\
 &\text{good phase } I_k^+=((2k-1)\ell,2k\ell): && c\equiv0,\quad D\equiv Q_0/\ell,\quad K=0,\\
 &\text{tail } (2n\ell,2): && c\equiv0,\quad D\equiv D_\flat,\quad K=0,
 \end{aligned}
\]
for `k = 1,…,n`, and let `Q` solve `Q' = -νD + K` with
`Q(0) := Q_0 + 2D_\flat`. Then, for every `δ ∈ (0,1]`:

1. `Q` rises by `Q_0` on each `I_k^-`, falls by `Q_0` on each `I_k^+`, and
   falls by `D_\flat` per unit length on the tail, so
   `Q_0 ≤ Q ≤ 2Q_0 + 2D_\flat ≤ 2.5Q_0 < 3Q_0` throughout and `Q > 0`;
   `Q(0) = Q_0 + 2D_\flat ≤ 1.5Q_0 ≤ ⅓‖u_0‖_3^3`. **(T1), (T2), (T6) hold**,
   with `Q(0)` independent of `n`.
2. `c ≤ 2 ≤ κQ_0^{1/3} ≤ κQ^{1/3}`: **(T5) holds**.
3. `∫_0^2c^4 = 16/n → 0`: **(T3) holds** for all `n ≥ 16/A_4`.
4. `∫_0^2Q ≤ 5Q_0` and `∫_0^2Q^{4/3} ≤ 2(2.5Q_0)^{4/3}`, both independent of
   `n`: **(T4), (T9) hold** for the fixed tuple above.
5. `D ≥ D_\flat = γ(3Q_0)^{7/3} ≥ γQ^{7/3}` **everywhere**, since on the
   spikes `D = Q_0n^2 ≥ Q_0 > D_\flat` and on the tail `D = D_\flat` while
   `Q < 3Q_0`: **(T7), (T8) hold**.
6. `B_δ = ⋃_k I_k^-`, so `|B_δ| = 1/n → 0`, `∫_{B_δ}c^4 → 0`, and `c ≡ 2` is
   bounded on `B_δ`; the good set contains `⋃_k I_k^+` and the tail.
7. `∫_{G_δ}D dt ≥ Σ_k ℓ·(Q_0/ℓ) = nQ_0 → ∞`, while
   `∫_{B_δ}(c-ν)D dt = nQ_0 → ∞` carries the entire excess.

Hence **no bound** `∫_{G_δ}D dt ≤ Φ(ν,A_4,A_Q,A_{4/3},Q(0),κ,γ,δ,H)` follows
from (T1)–(T9). □

*Proof.* Items 1–4, 6, 7 are the note's own arithmetic, verified above, with
the two additive `D_\flat` corrections: the tail contributes at most
`2D_\flat ≤ Q_0/2` of downward drift, which the shifted initial value absorbs,
and at most `2D_\flat` to `∫_{G_δ}D`, which only helps item 7. Item 5 is the
choice of `D_\flat` together with `Q < 3Q_0` from item 1. For `Q ∈ C^1` and
`c` Lipschitz, replace each jump by a linear ramp of relative length `ε` on
which `D ≡ D_\flat` (**not** `D ≡ 0`); this multiplies `∫c^4` by at most
`1+2ε` (the note's "`1+ε`" is off by the factor 2, harmlessly), changes item 7
by `1-O(ε)`, and preserves items 1–6. □

**Scope of Theorem C′, stated correctly.** No input-only bound on
`∫_{G_δ}D_3(w)dt` is derivable **from (T1)–(T9)**. Whether some other
consequence of the audited record suffices is *not* decided: the exhaustiveness
claim is withdrawn, it was false as stated, and — this is the point — it is
**not needed**. A non-derivability result relative to an explicitly displayed
list is exactly what rules out the proof strategies the lane was testing (the
two Hölder routes, the small-measure route, the threshold-tuning route), and
it is all that O3's upgrade requires.

### R2. What survives of the O3 upgrade

With C′ in place, the lane's strengthening of HF21-B's O3 stands, in this
form: O3 asserted unavailability by a saturation heuristic and left open
"whether any input-only bound for `∫_{G^δ_τ}D_3(w)dt` exists for some fixed
`δ ∈ (0,1]`". Theorem C′ closes the *derivability* half of that open question
against the nine listed constraints, including the four — (T2), (T4), (T5),
(T6) — that O2 never tested, and the two — (T8), (T9) — that this audit adds.
That is a genuine advance over O3 and over O2's two-fact family. It is not a
decision of the lane question itself.

### R3. Theorem D: correct, not new, and the quantifier that makes the gloss true

Theorem D is verified line by line. `¬2 ⇒ ¬1` is continuity of `‖q‖_3` (A7)
and of `D_Q` (A1) on the compact `[0,H] ⊂ [0,T_*)`. `¬1 ⇒ ¬2` integrates (A1),
uses `|K| ≤ cD` (A2) and `‖u‖_3^3 ≤ 3C_ℙ^3Q` (A3) to bound
`sup_{τ<min{H,T_*}}‖u(τ)‖_3`, and contradicts `thm:continuation` (A6). Both
directions are correct.

**It is the manuscript's own statement.** `rem:highstrain-scope` reads: "At the
quantifiers of Hypothesis~\ref{hyp:highstrain}, the hypothesis is equivalent to
global continuation of the selected classical branch… Conversely, if
`T_* = ∞` … `K_0` is continuous on the compact classical interval `[0,H]`, so
`A_input = ∫_0^H|K_0|dt` is finite… This converse assumes global continuation
and supplies no method for proving it." Theorem D is that sentence with `K_L`
replaced by `‖q‖_3D_3(w)` — legitimate by (A2) and
`rem:highstrain-normalisation`, and a two-line transcription. The correct
attribution sentence:

> Theorem D is `rem:highstrain-scope` of the manuscript, transported from
> `hyp:highstrain` to (G) by (A2) and `rem:highstrain-normalisation`. No
> novelty is claimed; what is new here is only the *use* made of it in
> Corollary D.1(ii).

**One quantifier must be added.** For a single fixed `H`, `T_* ≤ H` is
strictly stronger than "finite-time singularity", so MODE/RESULT item 4's
gloss "i.e. if and only if that trajectory develops a finite-time singularity"
is false as written. It becomes true at the quantifiers (G) actually carries
from `hyp:highstrain` ("for every `ν,u_0,H`"): failure of (G) for **some**
`H < ∞` is equivalent to `T_* < ∞`. Insert "for some horizon `H < ∞`".

**What Theorem D does establish, and it is worth stating plainly.** Because
`A_input` may be *any* finite function of `(ν,u_0,H)`, (G) restricted to one
datum is equivalent to `T_* > H` for that datum. So (G) is not a lemma of
intermediate strength on the way to regularity; it is regularity restated in
quotient variables. The note says this ("exactly as strong as the open
question") and is right; the controller should keep that sentence, because it
is the sharpest thing in the lane.

### R4. The three wording repairs

- **S1.** Replace, in MODE/RESULT item 1, "**No.** There is no input-only
  bound for `∫_{G_δ}D_3(w)dt`" by "**Not derivable.** No input-only bound for
  `∫_{G_δ}D_3(w)dt` follows from the listed consequences (T1)–(T9) of the
  audited record; by Theorem B(3) such a bound *is* implied by (G), so it
  cannot be false unless (G) is."
- **S2.** Add the attribution sentence of §R3 immediately after Theorem D.
- **S3.** In the O1(c) sharpening, replace "a Ladyzhenskaya–Prodi–Serrin
  hypothesis **stronger than** the conclusion" by "**at least as strong as**
  the conclusion", per the HF21-B audit's explicit downgrade of that wording.

---

## CONDITIONAL SUFFIX THAT SURVIVES

Unconditionally, for the classical branch from a divergence-free Schwartz
datum, every `τ < T_*`, `c = C_♯‖q‖_3`, `D = D_3(w) = D_Q(u)`:

1. **Theorem A** (verified, unchanged):
   `∫_0^τ(ν-c)_+D dt ≤ ⅓‖u_0‖_3^3 + ∫_B(c-ν)D dt`, and for `δ ∈ (0,1]`,
   `(1-δ)ν∫_{G_δ}D dt ≤ Q(u_0) + ∫_B(c-ν)D dt`. It sharpens Lemma R3(3) of
   HF21-B in both advertised respects (smaller support, smaller weight), and
   it is sharp: Theorem C′ attains it with ratio `→ 1`.
2. **Theorem B** (verified, unchanged): for `δ ∈ (0,1)` and every `τ < T_*`,
   `∫_0^τ cD dt ≤ (δ/(1-δ))Q(u_0) + (1/(1-δ))∫_{B_δ}cD dt`, with
   `Q(u_0) ≤ ⅓‖u_0‖_3^3` and `|B_δ| ≤ 24C_S^2C_♯^4E_0^2δ^{-4}ν^{-5}`
   uniformly in `τ`. Hence **(G) holds iff its bad-set restriction holds**, for
   one and hence every `δ ∈ (0,1)`: if `∫_{B_δ}‖q‖_3D_3(w)dt ≤ A_B` for all
   `τ < min{H,T_*}`, then (G) holds with
   `A_input = δ‖u_0‖_3^3/(3(1-δ)C_♯) + A_B/(1-δ)`, hence `hyp:highstrain` with
   `θ = 0` and no cutoff (`rem:highstrain-normalisation`), hence `hyp:critical`
   by `prop:quotient-conditional`, hence the Clay target by `thm:conditional`.
   This is the lane's one genuinely usable output and it is **untouched** by
   the defect above.
3. **Theorem B(3)** (verified): (G) `⇒ ∫_{G_δ}D dt ≤ (⅓‖u_0‖_3^3 + C_♯A_input)/((1-δ)ν)`.
   The good-set bound is a *necessary* condition for regularity, never a
   sufficient one.
4. **Theorem D** (verified, attribution corrected): for a fixed datum and
   `H < ∞`, `sup_{τ<min{H,T_*}}∫_0^τ‖q‖_3D_3(w)dt = ∞ ⟺ T_* ≤ H`; over all
   `H < ∞`, failure of (G) `⟺ T_* < ∞`.
5. **Theorem C′** (repaired): (T1)–(T9) do not imply any input-only bound on
   `∫_{G_δ}D dt`, and in the witnessing family `|B_δ| → 0`, `∫_{B_δ}c^4 → 0`
   and `c` is bounded on `B_δ`, so smallness of the bad set in measure and in
   the audited distance norm does not help.
6. **The meta-statement, repaired**: no route of the form "the profile cannot
   occur on a trajectory, therefore (G)" is available, because by Theorem D
   its hypothesis *is* (G). Any proof of (G) must use structure absent from
   (T1)–(T9) — the equation itself, the minimiser, or a quantitative modulus
   the audited record does not supply.

**Not surviving:** the claim that the negative decision holds "at the level of
the audited record" as such (exhaustiveness is unproved and the displayed list
was incomplete); the claim that no input-only good-set bound exists; the
implicit novelty of Theorem D.

---

## UNNECESSARY DEPENDENCIES

- **HF23** is correctly absent. Nothing in the target, and nothing in this
  audit, uses `w ∈ W^{1,2}_loc` or any (H1)-type regularity. No load-bearing
  step needs flagging on that account.
- **HF18-B** is correctly excluded from the premise list, and the weighted
  Calderón–Zygmund and `L^2`-projection items (both OPEN) are never used.
- **(T7) as stated is redundant** once (T8) is listed: (T8) is (T7) plus three
  audited facts, and it is (T8), not (T7), that constrains the triple. Keep
  (T7) as the intermediate step of (T8)'s proof, not as a list entry.
- **(T4) is redundant** given (T9), which is the same bound before the
  time-Hölder step and needs no horizon `H`. Both may be kept; only (T9) does
  work.
- **(A5)/`rem:highstrain-normalisation`** is used only for (T4) and for the
  `hyp:highstrain` transfer; the surviving Theorems A, B do not need it, and
  they are `τ`-uniform without any horizon. Worth recording: **Theorems A and
  B hold for all `τ < T_*`, with no `H` anywhere.**
- **(0.1)/(T5)** is the audited HF18-A size bound `|K| ≤ C_*Q^{1/3}D_3(w)` with
  `κ = C_*` exactly; it is not an additional input and should not be presented
  as one.
- The `δ = ½` specialisation, the scaling check of (1.2), and Remark 2.3 are
  presentational; nothing depends on them.

---

## NON-CLAIMS

This audit proves no new statement about Navier–Stokes. It does not prove or
refute (G), `hyp:highstrain`, `hyp:highpressure`, `hyp:absorption`,
`hyp:critical`, NS-R3, or the Clay target. (T8) and (T9) are elementary
consequences of already-audited facts and are asserted only as constraints on
the triple; no bound on `sup_t Q`, `sup_t‖u‖_3`, `∫D dt` or `∫D^{4/3}dt` is
claimed or used. The repaired family of §R1 is a family of real functions on
`(0,2)`, **not** a Navier–Stokes trajectory, and is never claimed to be one;
its members are indexed by `n` and need not share a Hölder constant for
`‖q‖_3`. No comparison between `D_3(u)` and `D_3(w)` is used
(`rem:distance-balance`). No forced, periodic, hyperdissipative or Euler
substitute appears; no smallness hypothesis is used. The numerics of §EVIDENCE
item 4 are evidence and never proof, and no conclusion rests on them. Nothing
is promoted; the manuscript, `PLAN.md`, the proof graph and the target note are
untouched by this audit, and nothing is committed or pushed.

---

## REOPENING CONDITION

Reopen this audit if any of the following occurs.

1. **An input-only modulus of continuity for `t ↦ ‖q(u(t))‖_3`** is produced on
   `[0,min{H,T_*})` — the note's §6 open question. Any such modulus bounds the
   number of crossings of the level `δν/C_♯` inside a set of measure `m` by
   `⌈m/ω^{-1}(δν/C_♯)⌉`; combined with (1.2) this is a crossing-*count*
   constraint, it is a tenth constraint (T10) on the triple, and the family of
   Theorem C′ — which needs `n` crossings inside a set of measure `1/n` —
   violates it outright. Theorem C′ would then be void and the lane question
   would reopen in the affirmative direction. This is the correct next action
   and the target names it correctly.
2. **Any further constraint on `(Q,c,D)` derivable from the audited record** is
   exhibited that the repaired family violates. The audit of the family is only
   as strong as the list (T1)–(T9); this audit found two omissions in a list of
   seven, so a third is not unlikely. Candidates not settled here: an upper
   bound on `D` in terms of `Q` and input (none is known and none follows from
   HF18-A); any constraint arising from `lem:quotient-lowstrain` without the
   cutoff hypothesis; any two-sided refinement of `|K| ≤ cD` beyond the
   monomial lattice of HF21-B Prop. 3.2.
3. **HF23 is audited and stands.** It would supply `w ∈ W^{1,2}_loc`
   unconditionally, which may add constraints coupling `D` to `Q` from above or
   supply the time-regularity of item 1. Nothing in the present verdict assumes
   HF23 either way.
4. **The bad-set lead of §6 is pursued**: transferring `hyp:absorption` on
   `B_δ` alone, a set of input-bounded measure. Theorem B is what makes this
   well posed, and it is unaffected by the defect; if that transfer produces
   `A_B`, then (G) follows by Theorem B(1) and the lane's negative result
   becomes irrelevant rather than wrong.

---

## EXACT EDITS THE CONTROLLER SHOULD MAKE IF THIS VERDICT STANDS

All edits are to files this audit does **not** own; the auditor made none.

**E1 — `research/evidence/hf22-good-set-dissipation.md`, §4 constraint list.**
Delete the clause "as a constraint on the triple this is vacuous, since it only
bounds `D` from below by a quantity not otherwise constrained" from (T7).
Delete the words "and nothing else that couples the three" from the sentence
introducing the list, and replace by "the following consequences, which are the
ones used below; the list is not claimed to be exhaustive". Append (T8) and
(T9) with the proofs displayed in §R1 and §"FIRST BAD BRIDGE" of this audit,
including the constant `γ = 8·3^{1/3}/(S^2C_9^3E_0^2)` and its scaling check.

**E2 — same file, Theorem C.** Replace Theorem C and its "Regularity of the
data" paragraph by Theorem C′ of §R1 verbatim, including the input-tuple
selection sentence, the tail value `D_\flat = γ(3Q_0)^{7/3} ≤ Q_0/4`, the
shifted initial value `Q(0) = Q_0 + 2D_\flat`, item 5, and the ramp correction
`1+2ε`. Replace every occurrence of "(T1)–(T7)" by "(T1)–(T9)" in the theorem,
in its "What Theorem C settles" bullets, and in the closing block.

**E3 — same file, MODE/RESULT item 1.** Apply repair S1 of §R4 verbatim.
Replace "satisfies **every** constraint the audited record imposes on the
triple" by "satisfies every constraint in the displayed list (T1)–(T9)". In the
same item, replace "and the negative is not a gap of technique at the level of
the audited record" by "and the negative is not a gap of technique relative to
those constraints".

**E4 — same file, §5.** Insert the attribution sentence of §R3 immediately
after the proof of Theorem D. In MODE/RESULT item 4 and in the third bullet of
"The decision the lane asked for", insert the horizon quantifier: "for some
horizon `H < ∞`" before the gloss "finite-time singularity".

**E5 — same file, §4 last bullet.** Apply repair S3: "at least as strong as
the conclusion", not "stronger than".

**E6 — same file, closing block.** In MODE / RESULT, replace "No input-only
bound … is derivable from the audited record" by "… is derivable from the
displayed constraints (T1)–(T9)". In CLAIM AND SCOPE item (C), same
replacement. In NON-CLAIMS, add: "The constraint list is not claimed
exhaustive; (T8) and (T9) were added by audit." Add to EVIDENCE:
`prop:energy` and `rem:highstrain-scope` (the latter as the source of
Theorem D).

**E7 — `PLAN.md`, "HF22" section, sub-question (c) bullet (lines ~1183–1194).**
Replace "an explicit family satisfies every constraint the audited record
imposes" by "an explicit family satisfies every constraint in an explicitly
displayed list of nine consequences of the audited record (two of which the
audit added)". Replace "Sub-question (c) is decided NO" by "Sub-question (c) is
decided NO **for derivability**". Replace "The lane also proves that realising
the obstruction profile on an actual trajectory is logically equivalent to
finite-time loss of the classical branch" by "The lane also records — as an
application of the manuscript's `rem:highstrain-scope`, not as a new result —
that realising the obstruction profile on an actual trajectory is logically
equivalent to loss of the classical branch before the horizon, hence, over all
horizons, to finite-time blow-up." Keep the positive by-product sentence about
Theorem B unchanged: it is verified.

**E8 — `PLAN.md`, add an audit-status line** for HF22-C alongside the existing
HF19/HF20/HF21 pattern: "`hf22-good-set-dissipation.md`: audited 2026-09-06,
**REPAIR** (`hf22-review-good-set-dissipation.md`); Theorems A, B, D stand,
Theorem C repaired to C′ after the constraint list was found incomplete;
Theorem D attributed to `rem:highstrain-scope`."

**E9 — no manuscript edit.** Nothing in this lane is ready for `main.tex`.
Theorem B is the only candidate and it is a two-line consequence of Lemma R3
of the HF21-B audit; if the controller wants it in the paper it belongs as a
remark after `rem:highstrain-normalisation` reading "(G) is equivalent to its
restriction to `{C_♯‖q‖_3 > δν}`, a set of times of input-bounded measure",
and only after HF21-B itself is integrated. Do not integrate Theorem C or
Theorem D: the first is an obstruction to a proof strategy, the second is
already in the manuscript.

**E10 — proof graph.** No node changes. If the controller records the lane at
all, record it as an obstruction edge into the (G) node labelled
"non-derivable from (T1)–(T9)", never as a negative result about (G).
