# Audit of HF24-B: the bad-set restriction of (G) under the new regularity

Proof-audit lane, **MODE: REVIEW**, 2026-09-06. Owned file:
`research/evidence/hf24-review-badset-restriction.md`. Nothing else in the
repository is edited, nothing is committed, nothing is promoted, the manuscript
is untouched. **NS-R3 remains open; nothing below closes (G) or any part of
it.**

## Freeze

| Object | Digest / revision |
|---|---|
| Target `research/evidence/hf24-badset-restriction.md` | `sha256 8a625c5f9a89ade386905334badc4ec3691b708cc5480b04fda24428007b3fa5` (790 lines) |
| Repository `/home/ert/proj/navier` HEAD | `a91fe79a10f810b81c9560186ef0f657a622f589` |
| Manuscript `/home/ert/proj/navier-paper` HEAD | `12f90758526a09e4a1bed55ae3eb79708394b32d` |

Directly inspected for this audit: `main.tex` `lem:quotient-coercive`
(L5455), `lem:quotient-scaling` (L5479), `prop:quotient-divcurl` (L5802),
`cor:quotient-defect` (L6283), `cor:quotient-vorticity-zero` (L6414),
`lem:quotient-mixed-pressure` (L6430) with \eqref{eq:qdc-mixedbound} and
\eqref{eq:qdc-KY}, `cor:quotient-budgets` (L6599) with its proof,
`rem:quotient-divcurl-scope` (L6670), `rem:quotient-scope` (L6691),
`def:qe-dissipation` (L7203), `lem:quotient-heatsign` (L7216),
`prop:quotient-evolution` (L7685), `lem:quotient-lowstrain` (L7773),
`hyp:highstrain` (L7830), `rem:highstrain-normalisation` (L7862),
`prop:quotient-conditional` (L7888), `rem:highstrain-scope` (L7940),
`lem:GN` (L2146), \eqref{eq:L4L3} (L2252), \eqref{eq:L4L3-constant} (L2306),
`prop:energy` (L2246 ff.), `thm:continuation` (L4664), `hyp:critical` (L4695),
`thm:conditional` (L4721); `hf21-crossing-sign-structure.md` §4.3–4.4
(Lemma 4.3, Theorem 4.5, Corollary 4.4); `hf22-good-set-dissipation.md`
§3 (Theorem B) and §4 ((T1)–(T9), Theorem C′);
`hf22-direct-attack.md` §2 (Prop. 2.1, Cor. 2.2, Prop. 2.3, Prop. 2.4);
`PLAN.md` L1270–1400.

---

## VERDICT

**REPAIR.**

Every load-bearing computation in the target is correct and every constant it
displays was recomputed here and reproduced. Theorem 2.1 (the first upper
bound for the quotient dissipation) is new, correct, and proved from audited
inputs. Theorem 3.1 (the *K*-form bad-set reduction), Theorem 3.2, the
deficit accounting of Proposition 4.1, its sharpness (Proposition 4.2), the
Ladyzhenskaya–Prodi–Serrin positions of Proposition 4.4, and the survival of
the HF22-C obstruction family under the enriched list (Theorem 5.2) all
survive independent reconstruction. The note uses nothing outside its audited
scope: no `w \in L^2`, no `\sigma \in L^{3/2}`, no derivative of `\|q\|_3`, no
residual defect hypothesis.

Two defects require repair, both displayed here with their replacements, and
neither destroys the note's mechanism:

- **D1 (arithmetic/bookkeeping, first in document order).** Theorem 3.3's
  displayed `A_{\rm input}` is the bound for `\int_0^\tau K`, but
  `hyp:highstrain` consumes `\int_0^\tau K_L`. The `K_{\rm low}` absorption
  permitted by `rem:highstrain-normalisation` is invoked in §3.1 and then
  omitted from the displayed constant. Exact replacement below (§R1).
- **D2 (overclaim, the substantive one).** Remark 3.4 and §7 assert that
  (H-BY) is **"strictly weaker than a Serrin bound"** and "a strictly weaker
  question". At the note's own quantifiers this is **false**: (H-BY) is
  equivalent to `T_* > H` for the datum, hence equivalent to `hyp:critical`,
  to `hyp:highstrain`, to a Serrin bound, and to (G)'s consequence. It is a
  member of the existential-equivalence class the programme already tracks.
  Exact replacement below (§R2), together with the lemma that proves the
  equivalence.

Three further imprecisions are recorded (§E7–E9) that the controller should
fix but that carry no mathematics.

---

## REVIEWED SCOPE

§§0–7 of the target in full, with these questions answered independently:

1. the unavailability claim for the route the lane was asked to try
   (Prop. 1.3 and the two classical routes);
2. the identity of the unconditional substitute with the audited measure
   bound, recomputed digit for digit (Prop. 1.1, Cor. 1.2);
3. **the main claim** — the deficit accounting of Prop. 4.1 with its displayed
   constants (Thms. 3.1, 3.2, 3.3);
4. the sharpness of the deficit, the plateau family, and the assertion that
   the bad-set restriction contributes nothing to the accounting
   (Prop. 4.2, Cor. 4.3);
5. the LPS bookkeeping, independently recomputed (Prop. 4.4, all three
   positions and the two comparisons);
6. the circularity status of the proposed next question (H-BY), against the
   critical hypothesis, and against the sibling lane HF24-A.

Not in scope: HF25 (under parallel audit, used nowhere here and not used by
the target); the correctness of the imported manuscript results themselves
(`hf23-review-regularity-core.md` PASS is taken as given, as instructed);
HF18-A, HF21-A/B and HF22-A/C beyond the specific statements the target cites.

---

## FIRST BAD BRIDGE

**Theorem 3.3, the sentence "so `hyp:highstrain` holds for that datum with
`\theta=0`" together with its displayed**
`A_{\rm input}=\frac{\delta}{3(1-\delta)}\|u_0\|_3^3+\frac{5C_S^3E_0N}{16\nu(1-\delta)}`.

The chain proved is `\int_0^\tau K\,dt \le A_{\rm input}` with `K=K_u` the
full strain work of \eqref{eq:quotient-evolution}. `hyp:highstrain`
\eqref{eq:quotient-gap} is stated for `K_L=K-K_{\rm low}` with a
datum-selected integer `L`. Since `K_{\rm low}` is not signed,
`\int K \le A` does **not** give `\int K_L \le A`; it gives
`\int K_L \le A + |\int K_{\rm low}|`. The note's §3.1 correctly cites
`rem:highstrain-normalisation` for the equivalence "up to an input-only change
of `A_{\rm input}`", so the gap is a display omission rather than a
misunderstanding — but as displayed, the constant in Theorem 3.3 is not the
constant that `prop:quotient-conditional` consumes, and Proposition 4.1
inherits it verbatim.

Everything downstream of the corrected constant is unaffected: the correction
is an additive input-only term with no `N` and no `\sup_{\mathcal B_\delta}Y`
in it, so the deficit statement — "input-only except for a single factor,
`\operatorname{ess\,sup}_{\mathcal B_\delta}Y`" — survives exactly.

**The substantive defect is D2 (Remark 3.4), not D1.** D1 is first in document
order and is arithmetic; D2 is the claim the controller would act on.

---

## EVIDENCE

### E1. Proposition 1.1 and Corollary 1.2: confirmed, and the coincidence is not accidental

`lem:quotient-coercive` gives `\mathcal Q(u)=\frac13\|w\|_3^3\le\frac13\|u\|_3^3`,
hence `\|w\|_3\le\|u\|_3` and `\|q\|_3\le\|w\|_3+\|u\|_3\le2\|u\|_3` — the
note's (A3), correct and, importantly, **not** routed through the
`(1+C_{\mathbb P})` form of \eqref{eq:cp-coercive}, so no `C_{\mathbb P}` leaks
into `\beta`. On `\mathcal B_\delta`, `C_\sharp\|q\|_3>\delta\nu` gives
`\|u\|_3>\delta\nu/(2C_\sharp)`. With \eqref{eq:L4L3-constant}
`\|u\|_3^4\le3C_S^2\|u\|_2^2Y` and `prop:energy` `\|u\|_2^2\le E_0`,
\[
 Y>\frac{(\delta\nu/2C_\sharp)^4}{3C_S^2E_0}
  =\frac{\delta^4\nu^4}{48\,C_S^2C_\sharp^4E_0}=y_\delta .
\]
Chebyshev against `\int_0^\tau Y\le E_0/(2\nu)`:
`|\mathcal B_\delta|\le E_0/(2\nu y_\delta)=24C_S^2C_\sharp^4E_0^2\delta^{-4}\nu^{-5}`.
**Recomputed digit for digit; identical to HF21-B Lemma 4.3 item 4 /
Theorem 4.5 (4.5), which at `\delta=1` reads `24C_S^2C_\sharp^4E_0^2\nu^{-5}`,
and identical to HF22-C's `|\mathcal B_{1/2}|\le384C_S^2C_\sharp^4E_0^2\nu^{-5}`
(`24\cdot2^4=384`).** ✓

The agreement is *forced*, not a coincidence, and the note does not say so.
HF21-B reaches it by `\int d_1^4\le16\int\|u\|_3^4\le16\cdot\frac32C_S^2E_0^2/\nu`
and Chebyshev on `d_1`; HF24-B reaches it by Chebyshev on `Y` first and then
`\int Y\le E_0/2\nu`. Both chains are `\|u\|_3^4\le3C_S^2E_0Y` composed with
`\int Y\le E_0/2\nu`, applied in the two possible orders, and Chebyshev at
exponent 4 commutes with the pointwise substitution. So the claim "the
unconditional substitute *is* the audited measure bound" is stronger than the
note states: it is the same proof, reordered. ✓

### E2. Proposition 1.3 and the unavailability of (1.2): confirmed, with one scope correction

The scaling enumeration is correct within its declared ingredient list. Under
`u\mapsto\lambda u(\lambda\cdot)` and `u\mapsto au`:
`\|q\|_3\sim(a,\lambda^0)`, `\|\nabla q\|_2\sim(a,\lambda^{1/2})`,
`\|u\|_2\sim(a,\lambda^{-1/2})`, `\nu\sim(a,\lambda^0)`. Dilation forces
`\alpha=\beta`; amplitude forces `\alpha+\beta+\gamma=1`; hence
`\alpha=\beta=(1-\gamma)/2`. ✓ Adding `\|w\|_6\sim(a,\lambda^{1/2})` or
`\|\nabla w\|_2` or `Y^{1/2}` changes nothing (same grading), so the
enumeration is stable under the obvious enlargements of the list. ✓

**Scope correction.** The step `\gamma=0` is justified by "a bound valid for
the functional `\mathcal Q` alone, which knows nothing of the viscosity". That
is a normative reading of `rem:quotient-scope`, not a derivation: a bound with
`\gamma\ne0` is not scaling-inadmissible, it is merely not a statement about
the functional. Proposition 1.3 should therefore be labelled an enumeration
*under a declared ingredient list and a declared viscosity-free requirement*,
not "the exponent pair is forced". This is inert: no downstream statement uses
Prop. 1.3 except as motivation for the two non-derivability routes, which stand
on their own.

Both non-derivability routes check out:
(i) Gagliardo–Nirenberg needs `q\in L^2`, i.e. `w\in L^2`, which
`prop:quotient-divcurl` closes with the sentence "These statements do not
assert `w\in L^2(\R^3)`" and `rem:quotient-divcurl-scope` repeats. The note's
extra observation that GN would produce `\|q\|_2` and not `\|u\|_2` is
**correct and sharper than it looks**: `\mathbb P` is an orthogonal projection
on `L^2` and `u=\mathbb Pw`, `q=(I-\mathbb P)w`, so if `w\in L^2` then
`\|w\|_2^2=\|u\|_2^2+\|q\|_2^2` and `\|q\|_2` is *unconstrained* by `\|u\|_2`.
So no inequality `\|q\|_2\le C\|u\|_2` can hold even granting `w\in L^2`. ✓
(ii) HLS on \eqref{eq:qdc-potential} needs `\sigma\in L^{3/2}`, which
`rem:quotient-divcurl-scope` names as unproved and explicitly warns does not
follow from `\sigma\in L^2` on infinite measure. ✓

Non-derivability, not falsity, as the note says. ✓

### E3. Proposition 1.4: confirmed, with the numeric direction stated

Granting (1.2) with constant `C`: on `\mathcal B_\delta`,
`\|q\|_3>\delta\nu/C_\sharp`, so
`\|\sigma\|_2>(\delta\nu/(CC_\sharp))^2E_0^{-1/2}` and Chebyshev against
`\int\|\sigma\|_2^2\le E_0/(8\nu)` gives
`|\mathcal B_\delta|\le C^4C_\sharp^4E_0^2/(8\delta^4\nu^5)`. ✓ Recomputed.

Unconditionally: `\|\nabla w\|_2\ge\|\nabla u\|_2-\|\nabla q\|_2\ge\frac12Y^{1/2}`
by \eqref{eq:qdc-q}, so `\|\nabla w\|_2^2>y_\delta/4` on `\mathcal B_\delta`, and
`\int\|\nabla w\|_2^2\le5E_0/(8\nu)` gives
`|\mathcal B_\delta|\le\frac{5E_0}{8\nu}\cdot\frac4{y_\delta}=5\beta`. ✓

**One correction of emphasis.** "Granting it changes nothing" understates the
comparison in the wrong direction. The two bounds agree in functional form but
not in size: the conditional one beats `\beta` iff `C^4<192C_S^2`, and the
natural constant from route (i) — `C=(\sqrt3C_S)^{1/2}` in
`\|q\|_3\le(\sqrt3C_S)^{1/2}\|q\|_2^{1/2}\|\nabla q\|_2^{1/2}` — gives
`C^4=3C_S^2`, i.e. a bound **64 times better** than `\beta`. The note's
conclusion nevertheless survives untouched, and for the right reason, which is
Corollary 4.3, not Prop. 1.4: the deficit is `\sup_{\mathcal B_\delta}Y`, and by
Cor. 4.3 that factor is *completely insensitive to the value of* `\beta`. So
(1.2) is inert **because the measure bound is inert**, not because it would
reproduce `\beta`. The note should say this; as written, the argument invites
the objection that a 64-fold constant is not "nothing".

The stated *reason* — both new budgets are pointwise multiples of `Y` before
integration, `\|\nabla w\|_2^2\le\frac54Y` and `\|\sigma\|_2^2\le\frac14Y`
(\eqref{eq:qdc-pointwisebudget} in the proof of `cor:quotient-budgets`) — is
exactly right and is the sharpest form of the claim. ✓

### E4. Theorem 2.1: confirmed, new, correct

`D_{\mathcal Q}(u)=-\langle A,\Delta u\rangle` (`def:qe-dissipation`).
Integration by parts: `A\in W^{1,3/2}` (`cor:quotient-defect`),
`C_c^\infty` dense in `W^{1,3/2}(\R^3)`, `\Delta u\in L^3` and `\nabla u\in L^3`
for `u\in H^m`, `m\ge4` (`H^2\subset L^2\cap L^\infty\subset L^3`;
`\nabla u\in H^3`), both limits converge by Hölder `(3/2,3)`. ✓

Estimate: `|\nabla A|_F\le2|w||\nabla w|_F` a.e. (`cor:quotient-defect`);
Hölder `(6,2,3)`, `\frac16+\frac12+\frac13=1`. ✓
`\|w\|_6\le C_S\|\nabla w\|_2` and `\|\nabla w\|_2^2\le\frac54Y` give
`2C_S(\frac54Y)^{1/2}(\frac54Y)^{1/2}=\frac52C_SY`. ✓
`lem:GN` `\|\nabla u\|_3\le(3C_S)^{1/2}Y^{1/4}\|\Delta u\|_2^{1/2}` gives
`\frac52\cdot3^{1/2}C_S^{3/2}Y^{5/4}\|\Delta u\|_2^{1/2}=\frac{5\sqrt3}2C_S^{3/2}Y^{5/4}\|\Delta u\|_2^{1/2}`. ✓

Scaling: `D\sim(a^3,\lambda^2)`; `Y\|\nabla u\|_3\sim(a^2,\lambda)(a,\lambda)`
✓; `Y^{5/4}\|\Delta u\|_2^{1/2}\sim(a^{5/2},\lambda^{5/4})(a^{1/2},\lambda^{3/4})`
✓. The `m\ge4` restriction is used exactly where
`lem:quotient-mixed-pressure` uses it. ✓ The status claim is correct: the
audited record previously contained only `D\ge0` and the lower bound (A12).

**No refutation found.** The inequality is a chain of Hölder and Sobolev steps
with no cancellation, so no family can refute it; the only question is
sharpness, and the note's `q=0` consistency check is right (the direct route
`\int|u||\nabla u|^2\le\|u\|_6\|\nabla u\|_{12/5}^2` with
`\|\nabla u\|_{12/5}\le\|\nabla u\|_2^{1/2}\|\nabla u\|_3^{1/2}` gives the same
product). ✓

### E5. Theorem 3.1: confirmed exactly

`\int_0^\tau(\nu D-K)=\mathcal Q(u_0)-\mathcal Q(\tau)\le\mathcal Q(u_0)`.
On `\mathcal G_\delta`, `c\le\delta\nu` and `|K|\le cD` give
`\nu D-K\ge(1-\delta)\nu D\ge0`, so
`I_GK\le\delta\nu I_GD\le\frac\delta{1-\delta}I_G(\nu D-K)
\le\frac\delta{1-\delta}[\mathcal Q(u_0)+I_B(K-\nu D)]`; the last step is
legitimate because `I_G(\nu D-K)\ge0` and the multiplier is positive. Adding
`I_BK` and using `D\ge0` pointwise on `\mathcal B_\delta` collapses
`\frac\delta{1-\delta}(K-\nu D)+K\le\frac K{1-\delta}`. ✓
`\mathcal B_\delta` is open (continuity of `t\mapsto\|q(t)\|_3` via
`lem:quotient-stability`), all integrands continuous
(`prop:quotient-evolution`, `lem:quotient-heatsign`), so the splitting is
legitimate. ✓

The relation to HF22-C Theorem B is stated correctly in the body: 3.1 is
weaker on the left and weaker on the right. The RESULT summary's "strictly
sharper" is loose — it is sharper *as a bound on* `\int K` and says nothing
about `\int cD`. Recorded as E8.

### E6. THE MAIN CLAIM — Proposition 4.1 with its constants: confirmed

Theorem 3.2 = Theorem 3.1 plus \eqref{eq:qdc-KY} `|K_u|\le\frac58C_S^3Y^2`.
\eqref{eq:qdc-KY} recomputed from \eqref{eq:qdc-mixedbound}:
`|K_u|\le\frac12\|\nabla u\|_2\|u\|_6\|w\|_6^2
\le\frac12Y^{1/2}\cdot C_SY^{1/2}\cdot C_S^2\cdot\frac54Y=\frac58C_S^3Y^2`. ✓
It holds at every `t<T_*` with no defect hypothesis. ✓

Proposition 4.1, unconditionally, for every `\delta\in(0,1)`, `\tau<T_*`:
\[
 \int_0^\tau K\,dt\le\frac{\delta}{3(1-\delta)}\|u_0\|_3^3
 +\frac{5C_S^3E_0}{16\nu(1-\delta)}\operatorname*{ess\,sup}_{\mathcal B_\delta}Y ,
\]
because `\int_{\mathcal B_\delta}Y^2\le(\operatorname{ess\,sup}_{\mathcal B_\delta}Y)\int_{\mathcal B_\delta}Y
\le(\operatorname{ess\,sup}_{\mathcal B_\delta}Y)E_0/(2\nu)` and
`\frac{5C_S^3}{8(1-\delta)}\cdot\frac{E_0}{2\nu}=\frac{5C_S^3E_0}{16\nu(1-\delta)}`.
**Every constant recomputed and reproduced. The claim that the accounting is
input-only except for the single factor `\operatorname{ess\,sup}_{\mathcal B_\delta}Y`
is CONFIRMED**, subject only to D1 (the missing additive `K_{\rm low}` term,
which is input-only and carries no `Y`).

**Independent confirmation by a second route.** Remark 3.5's `L^2\times L^2`
pairing, reduced with the same supremum, produces the *identical* constant:
\[
 \Bigl(\frac{E_0}{8\nu}\Bigr)^{1/2}\Bigl(\int_{\mathcal B_\delta}\|\Pi_u\|_2^2\Bigr)^{1/2}
 \le\Bigl(\frac{E_0}{8\nu}\Bigr)^{1/2}\cdot\frac54C_S^3
   \bigl(\sup_{\mathcal B_\delta}Y\bigr)\Bigl(\frac{E_0}{2\nu}\Bigr)^{1/2}
 =\frac{5C_S^3E_0}{16\nu}\sup_{\mathcal B_\delta}Y ,
\]
using `\|\Pi_u\|_2\le\|u\|_6\|w\|_6^2\le\frac54C_S^3Y^{3/2}` and
`\int_{\mathcal B_\delta}Y^3\le(\sup Y)^2\int Y`. The two routes are not
merely of the same order; they agree in the constant `\frac5{16}C_S^3E_0/\nu`
exactly. This is strong evidence that the deficit factor is route-independent,
and the note did not notice it.

**A route the note did not enumerate, checked and closed here.** The enstrophy
inequality `\frac12Y'+\frac\nu2\|\Delta u\|_2^2\le C_E\nu^{-3}Y^3` supplies no
upper bound for `\sup_{\mathcal B_\delta}Y`. Integrating it backwards from a
peak `Y(t_0)=M` gives `Y(t)^2\ge(M^{-2}+4C_E\nu^{-3}(t_0-t))^{-1}`, hence
`Y\ge M/2` on an interval of length `3\nu^3/(4C_EM^2)`, hence
`E_0/(2\nu)\ge\int Y\ge3\nu^3/(8C_EM)`, i.e. `M\ge3\nu^4/(4C_EE_0)` — a lower
bound only. Likewise `Y\le\|u\|_2\|\Delta u\|_2` gives
`\int Y^2\le E_0\int\|\Delta u\|_2^2`, and `\int\|\Delta u\|_2^2` is not
input-bounded. Both routes are inert. The deficit accounting therefore
survives this audit's own search for a bypass.

### E7. Sharpness (Prop. 4.2, Cor. 4.3): confirmed, with three refinements

The plateau family verifies: `M>\max\{y_\delta,E_0/(4\nu\beta)\}`,
`|\mathcal B_\delta|=E_0/(4\nu M)\le\beta`, `Y\equiv M>y_\delta`,
`\int_{\mathcal B_\delta}Y=E_0/(4\nu)\le E_0/(2\nu)`,
`\int_{\mathcal B_\delta}Y^2=ME_0/(4\nu)\to\infty`. ✓ Extremality of the
elementary bound `\int Y^2\le(\sup Y)\int Y` on this family: equality. ✓ So
the factor cannot be improved by rearranging the same two budgets. ✓

Three refinements, all confirming rather than weakening the claim.

1. **`\mathcal B_\delta` is not merely inert; a small bad set is adverse.**
   Cauchy–Schwarz gives `\int_{\mathcal B_\delta}Y^2\ge(\int_{\mathcal B_\delta}Y)^2/|\mathcal B_\delta|`,
   with equality exactly on the plateau family. So making the bad set smaller
   (larger `\delta`) *raises* the floor of the quantity the route must bound,
   at fixed occupancy of the energy budget. The measure bound is therefore not
   just uninformative for the upper bound; it certifies that no gain can come
   from shrinking `\mathcal B_\delta`.
2. **The displayed `A_{\rm input}` is monotone in `\delta` the wrong way.**
   At fixed `N`, `\frac{\delta}{3(1-\delta)}\|u_0\|_3^3+\frac{5C_S^3E_0N}{16\nu(1-\delta)}`
   is strictly increasing in `\delta` on `(0,1)`, with limit
   `\frac{5C_S^3E_0N}{16\nu}` as `\delta\downarrow0`. So the entire value of
   the bad-set restriction is carried by the `\delta`-dependence of
   `N=N(\nu,u_0,H,\delta)` and by nothing in the constants. The note writes
   `N(\nu,u_0,H,\delta)` correctly but never draws this conclusion, which is
   the sharpest available statement of Corollary 4.3 and should replace the
   looser "buys nothing".
3. **Cor. 4.3 and Rem. 3.4 need reconciling.** Cor. 4.3 says the restriction
   "buys nothing"; Rem. 3.4 says its "only advantage is that it needs the
   bound on a set of input-bounded measure only". Both are true, of different
   things: nothing in the *quantitative accounting* (constants, exponent,
   deficit), something in the *shape of the residual hypothesis* — and by D2
   below, nothing in its *logical strength* either.

**Numerical discrepancy (cosmetic).** RESULT bullet 4 states the plateau family
with measure `E_0/(2\nu M)` and `\int_{\mathcal B_\delta}Y^2=ME_0/(2\nu)`;
§4.2 states `E_0/(4\nu M)` and `ME_0/(4\nu)`; Cor. 4.3 quotes
`M\ge E_0/(2\nu\beta)` against §4.2's `E_0/(4\nu\beta)`. Both variants are
internally consistent (the summary saturates `\int Y\le E_0/2\nu`, the body
takes a factor-2 margin); the note must pick one.

### E8. LPS bookkeeping (Prop. 4.4): all three positions independently recomputed

With `\lambda(r,q)=\frac2r+\frac3q`:

| Object | Space | `\lambda` | Status |
|---|---|---|---|
| `u`, energy sup | `L^\infty_tL^2_x` | `0+\frac32=\frac32` | audited hull endpoint ✓ |
| `u`, energy dissipation + Sobolev | `L^2_tL^6_x` | `1+\frac12=\frac32` | audited hull endpoint ✓ |
| `u`, \eqref{eq:L4L3} | `L^4_tL^3_x` | `\frac12+1=\frac32` | `\theta=\frac12` midpoint ✓ |
| `w`, `cor:quotient-budgets` + `\|w\|_6\le C_S\|\nabla w\|_2` | `L^2_tL^6_x` | `\frac32` | **same point** ✓ |
| `cD` route, `s=4` | `u\in L^4_tL^9_x` | `\frac12+\frac13=\frac56` | overshoot `\frac16` ✓ |
| `K` route | `Y\in L^2_t\Leftrightarrow\nabla u\in L^4_tL^2_x\Rightarrow u\in L^4_tL^6_x` | `\frac12+\frac12=1` | overshoot `0` ✓ |

Cross-checked against the scaling grading: `\|\nabla u\|_{L^4_tL^2_x}` is
invariant under `u\mapsto u_\lambda` (`\lambda^{1/2}` from the space norm,
`\lambda^{-1/2}` from `dt`), confirming criticality independently of the
`\lambda(r,q)` arithmetic; `\|u\|_{L^4_tL^9_x}` carries `\lambda^{1/6}`,
confirming the `\frac16` overshoot. ✓ `1-\frac2{3s}` at `s=4` is `\frac56`,
matching `hf22-direct-attack` (2.1). ✓ Deficit `\frac32-1=\frac12` matches
Cor. 2.2. ✓

**Claim CONFIRMED: the two new budgets sit on the hull point `(2,6)` already
occupied by the energy identity and add no new time-integrability.** The
sharpest reason is the note's own: `\|\nabla w\|_2^2\le\frac54Y` and
`\|\sigma\|_2^2\le\frac14Y` hold *pointwise in `t`*, so the budgets are
corollaries of `\int Y`, not new spacetime information. ✓

**Claim CONFIRMED with a scope qualification: "the new route demands the
Serrin line exactly, the older one overshot by `\frac16`".** The two
`\lambda`-values are computed in the same direction — each is what the route's
demand *forces* via an audited lower bound (`D\ge\frac8{9C_S^2C_9^3}\|u\|_9^3`
for the `cD` route, Sobolev for the `K` route) — so the comparison is
apples-to-apples. ✓ **Qualification:** the `\frac16` is the best value over
the `s`-family *for which the audited record supplies a budget*, i.e. `s\le4`
(`\int c^4\le A_4` plus finite measure covers `s<4`; `s>4` needs a bound on
`\sup_tc` that the record does not have). `hf22-direct-attack` Prop. 2.4
already records that the same family reaches `\lambda=1` at `s=\infty`, where
the block moves to the factor `\int D\,dt`. So "the older one overshot" is
true of the audited-attainable members, not of the whole family, and the
target should say so. Prop. 4.4's own proof only ranges over `s\in(1,4)`.

**Claim CONFIRMED: the bad-set restriction contributes nothing to either
number.** Independently checked: using `|\mathcal B_\delta|\le\beta` in the
`K` route via Hölder, `\int_{\mathcal B}Y^2\le\beta^{1/2}(\int_{\mathcal B}Y^4)^{1/2}`,
demands `Y\in L^4_t`, i.e. `\nabla u\in L^8_tL^2_x`, i.e. `u\in L^8_tL^6_x`,
`\lambda=\frac14+\frac12=\frac34<1` — strictly subcritical, strictly worse. ✓
Matches the note's Prop. 4.4 proof pattern for the `cD` route. The measure
bound can only be traded downward in `\lambda`. ✓

**Correction, inert but displayed.** Corollary 1.5's heading "the defect's
spacetime hull is a single point" and Prop. 4.4(1)'s "the defect contributes a
single point and no segment" are false as stated about `w` and `q`: (A3) plus
\eqref{eq:L4L3} give `\|w\|_3\le\|u\|_3` and `\|q\|_3\le2\|u\|_3`, hence
`w,q\in L^4_tL^3_x`, so the defect *does* have a hull segment, spanned by
`(4,3)` and `(2,6)`. The segment lies entirely at `\lambda=\frac32`, so every
conclusion drawn from it is correct; the sentence to fix is the reason, not
the result. Cor. 1.5's own final clause ("comes from `\|q\|_3\le2\|u\|_3` and
`u`'s own hull, not from the import") already contains the correction.

### E9. §5, Theorem 5.2: verified, including the numerics

Theorem C′ of HF22-C reproduced from source: `\nu=1`, `\tau=2`, `\ell=n^{-2}`,
`2n` phases on `(0,2/n)`, `D\equiv\mathcal Q_0/\ell=\mathcal Q_0n^2` on all
phases, `c\equiv2,K=cD` on bad phases, `c=K=0` on good phases, tail
`D\equiv D_\flat`, and `E_0` free to be arbitrarily large (C′ requires it, to
make `\gamma\downarrow0`). ✓ The note's restatement is faithful.

New assignments and constraints, all recomputed:

- `y_1^2=16\mathcal Q_0/(5C_S^3)`, so on bad phases
  `\frac58C_S^3Y^2=\frac58C_S^3y_1^2n^2=2\mathcal Q_0n^2=K`: **(T10) holds
  with equality.** ✓
- `\int_0^2Y=2n\cdot n^{-2}\cdot y_1n+O(1)=2y_1+O(1)`, independent of `n`;
  `E_0` free gives **(T11)**. ✓
- `\int_0^2Y^3=2n\cdot n^{-2}\cdot y_1^3n^3=2y_1^3n^2`;
  `Z=(D/(c_1Y^{5/4}))^4=\mathcal Q_0^4n^3/(c_1^4y_1^5)` and
  `\int Z=2\mathcal Q_0^4n^2/(c_1^4y_1^5)`. **(T13) equality, (T14) reduces to
  `\mathcal Q_0^4\le2C_Ec_1^4y_1^8`.** ✓
- The numerical slack, computed exactly:
  `c_1^4=(75/4)^2C_S^6=\frac{5625}{16}C_S^6`, `C_E=\frac{2187}{32}C_S^6`,
  `y_1^8=\frac{65536}{625}\mathcal Q_0^4C_S^{-12}`, so
  `2C_Ec_1^4y_1^8=2\cdot\frac{2187}{32}\cdot\frac{5625}{16}\cdot\frac{65536}{625}\mathcal Q_0^4
  =2187\cdot2304\,\mathcal Q_0^4=5\,038\,848\,\mathcal Q_0^4`.
  **All `C_S` powers cancel; the slack factor is exactly `5\,038\,848`,
  i.e. the note's `\approx5\times10^6` digit for digit.** ✓
- (T12), (T15): slack on the phases because `Y\to\infty`; the tail value
  `y_0` may be taken small as `E_0\uparrow\infty`. ✓

**Sharpness cross-check the note states but does not compute.** On this family
`\int_{\mathcal B_\delta}Y^2=n\cdot n^{-2}\cdot y_1^2n^2=y_1^2n`, so
`\frac58C_S^3\int_{\mathcal B_\delta}Y^2=2\mathcal Q_0n=\int_0^2K` exactly.
Theorem 3.2 is therefore **attained with equality (up to the `1/(1-\delta)`
and the `\mathcal Q_0` term) on the HF22-C obstruction family**. That is an
independent confirmation of Proposition 4.1's sharpness by a route that does
not pass through Proposition 4.2. ✓

**Residual weakness, recorded.** The ramp verification is sketched, not
carried out: the note checks the rate condition `\frac12y_1n^3\le(2C_Ey_1^3-\mathcal Q_0^4/(c_1^4y_1^5))n^3`
on the up-ramps and asserts that raising `y_1` fixes it if needed, but does not
display the ramp profile for `Y` and `Z` jointly, nor the down-ramps, nor the
tail's own contribution to the integrated (T14). All of these are `O(1)` against
`\Theta(n^2)` and the free parameters `y_0,y_1,E_0` are available, so the audit
finds the construction plausible but **not fully displayed**. Since Theorem 5.2
is a non-derivability statement — the weakest kind of claim in the note, and one
whose failure would only remove an obstruction — this is recorded, not repaired.

### E10. Circularity of (H-BY) — the question the brief asks

**Finding: (H-BY) is not circular as an inference, and is exactly equivalent to
the conclusion as a hypothesis. The note's "strictly weaker than a Serrin
bound" is false at its own quantifiers.**

Theorem 3.3 is a genuine implication: its proof consumes only (A4), (A8),
Theorem 3.1 and `prop:quotient-conditional`, and nowhere assumes a continuation
bound. There is no hidden circularity *inside the proof*. But the hypothesis
sits in the existential-equivalence class:

> **Lemma A (equivalence of (H-BY) with global continuation past the horizon).**
> Fix `\nu>0`, a divergence-free Schwartz datum `u_0`, `\delta\in(0,1)` and
> `0<H<\infty`; let `u` be the maximal classical branch on `[0,T_*)`. Then
> (H-BY) holds for that datum if and only if `T_*>H`.
>
> *Proof.* (⇒) Suppose (H-BY) with finite `N`. By Theorem 3.3 (repaired as
> §R1) `\int_0^\tau K_L\le A_{\rm input}` for all `\tau<\min\{H,T_*\}`, so
> `hyp:highstrain` holds for this datum with `\theta=0`, and
> `prop:quotient-conditional` gives
> `\sup_{0<t<\min\{H,T_*\}}\|u(t)\|_3\le M(\nu,u_0,H)<\infty`. If `T_*\le H`
> then `\min\{H,T_*\}=T_*` and `\sup_{0<t<T_*}\|u(t)\|_3<\infty`, so
> `thm:continuation` gives `T_*=\infty`, contradicting `T_*\le H<\infty`.
> Hence `T_*>H`.
> (⇐) Suppose `T_*>H`. By `prop:localtheory`, `u\in C([0,H];H^m)` for every
> `m`, so `Y=\|\nabla u\|_2^2` is continuous on the compact `[0,H]` and
> `N:=\sup_{[0,H]}Y<\infty`. The branch is determined by `(\nu,u_0)`, so `N`
> is a function of `(\nu,u_0,H)` alone, which is the dependence (H-BY)
> permits; and `\operatorname{ess\,sup}_{\mathcal B_\delta(\tau)}Y\le N` for
> every `\tau<\min\{H,T_*\}` and every `\delta`. `\square`

This is verbatim the structure `rem:highstrain-scope` uses for
`hyp:highstrain` (converse: "if `T_*=\infty`, take `L=0` and `\theta=0`;
`A_{\rm input}=\int_0^H|K_0|` is finite"), and the note itself applies it to
(G) in §0. Consequences:

1. **(H-BY) ⟺ `hyp:highstrain` for the datum ⟺ `hyp:critical` for the datum
   ⟺ a Serrin/enstrophy bound for the datum ⟺ `T_*>H`.** All five are the
   same statement at these quantifiers. Quantified over all data, all five are
   NS-R3.
2. **The unrestricted enstrophy bound is therefore no stronger than (H-BY).**
   Lemma A's (⇐) produces a bound on *all* of `[0,H]`, not only on
   `\mathcal B_\delta`. So restricting to the bad set does not lower the
   existential strength by any amount.
3. **Remark 3.4 and §7's "strictly weaker" are false as claims about logical
   strength.** What is true, and should be said instead: (H-BY) is strictly
   weaker *pointwise, for a fixed trajectory and a fixed `\tau`* — it
   constrains `Y` on a set of measure at most `\beta` and leaves
   `\mathcal G_\delta` free — while being *equivalent, as an input-uniform
   existential hypothesis*, to the conclusion it produces. The narrowing is a
   narrowing of the search surface, not of the assumption.
4. §4.2 rider (i) — "a route that demands exactly `\lambda=1` is exactly as
   strong as an LPS criterion, so Theorem 3.3 cannot be easier than a Serrin
   bound in general" — is the note's own correct statement and *contradicts*
   Remark 3.4's "strictly weaker". The note is internally inconsistent on
   precisely this point; rider (i) is the sentence that survives.

**Comparison with the sibling lane (answering the brief's final question).**
`PLAN.md` records that `hf24-modulus-of-continuity.md` (HF24-A) needs an
input-only enstrophy bound on a corridor of times where the distance sits near
the critical level, and that the lane calls the *unrestricted* form "the
critical hypothesis verbatim, hence circular", concluding that "the corridor
restriction is the whole distance between its hypothesis and its conclusion".
The audit's answer to the brief:

- **Both lanes' hypotheses are in the same class, and neither is more circular
  than the other.** Lemma A applies verbatim to the corridor form (any
  measurable subset of `[0,H]` on which the criterion closes): (⇒) is the
  lane's own criterion, (⇐) is continuity of `Y` on a compact interval. So
  HF24-A's corridor hypothesis and HF24-B's (H-BY) are both equivalent to
  `T_*>H`, hence to each other, hence to the critical hypothesis.
- **HF24-A's conclusion is therefore half right and half wrong in the same way
  HF24-B's is.** It is right that the unrestricted form is the critical
  hypothesis. It is wrong that the restriction creates logical distance:
  restricting the set of times does not weaken an input-uniform existential
  hypothesis, because the converse direction reconstructs the bound on the
  whole interval from `T_*>H` regardless of which subset was assumed.
- **So: both are "circular" in the precise sense the programme already uses
  for `hyp:highstrain`, `hyp:highpressure`, `hyp:absorption`, `hyp:critical`
  and (G) — equivalent to the conclusion at the problem's quantifiers — and
  neither is circular in the fatal sense of a proof that assumes what it
  proves.** They do not differ in this respect. What differs between the two
  lanes is only the *shape* of the set to be controlled (a level-crossing
  corridor versus the whole bad set) and the currency of the modulus, which
  are heuristic distinctions.

This is not a reason to discard either lane. It is a reason to stop describing
either hypothesis as weaker than a Serrin bound, and to record both under the
existential-equivalence caution `PLAN.md` already applies to the HF25 defect
hypothesis ("it belongs to the existential-equivalence class, so at the
problem's quantifiers it is equivalent to global continuation, like every
other formulation the programme has produced").

### E11. Scope compliance

Checked exhaustively, all clean:

- **`w\in L^2` is never used.** Every use of `w` is through `\|w\|_6`,
  `\|\nabla w\|_2`, `\|w\|_3` or `A=|w|w\in L^{3/2}`. ✓
- **`\sigma\in L^{3/2}` is never used.** `\sigma` appears only through
  `\|\sigma\|_2` and the `L^2\times L^2` pairing of
  `lem:quotient-mixed-pressure`. ✓
- **No residual defect hypothesis, no `\int Y^2` bound, no `\sup_tY`,
  no `\int D`, no `\int\|\Delta u\|_2^2` is assumed anywhere.** The one place
  `\|\Delta u\|_2` enters (Theorem 2.1, (T13)) is as an upper-bounding factor,
  never as an input budget. ✓
- **The merely-`L^3` minimizer is never differentiated in `t`**; the only
  derivatives of `w` are the distributional spatial ones from
  `prop:quotient-divcurl`. ✓ The only time derivative taken is
  `\frac d{dt}\mathcal Q(u(t))`, which `prop:quotient-evolution` supplies. ✓
- **HF25 is not used.** ✓ Confirmed by inspection of the input list and every
  citation in §§1–7.
- Theorem 2.1's `m\ge4` matches `lem:quotient-mixed-pressure`'s own
  restriction. ✓
- All `\delta`-quantifiers are correct: `\delta\in(0,1)` in Theorems 3.1–3.3
  (needed for `1-\delta>0`), `\delta\in(0,1]` in Prop. 1.1 (no division). ✓

---

## REPLACEMENT ARGUMENT

### R1. Repair of D1 — Theorem 3.3's constant

Replace the displayed `A_{\rm input}` of Theorem 3.3 by the following, which is
what `hyp:highstrain` \eqref{eq:quotient-gap} consumes.

> **Theorem 3.3′ (repaired).** Fix `\delta\in(0,1)` and `0<H<\infty`, and
> suppose (H-BY) holds with finite `N=N(\nu,u_0,H,\delta)`. Then
> `hyp:highstrain` holds for that datum with `\theta=0`, `L=0`, and
> \[
>  A_{\rm input}
>  =\underbrace{\frac{\delta}{3(1-\delta)}\|u_0\|_3^3
>   +\frac{5C_S^3E_0}{16\,\nu\,(1-\delta)}\,N}_{\text{bound for }\int_0^\tau K}
>  \;+\;\underbrace{\frac{M_0}{3}\,H^{1/4}
>   \Bigl(\frac{3C_S^2E_0^2}{2\nu}\Bigr)^{3/4}}_{\text{absorption of }K_{\rm low}},
>  \qquad M_0=3(1+C_{\mathbb P})C_B\|u_0\|_2 .
> \]
>
> *Proof.* Theorem 3.2 with `\int_{\mathcal B_\delta}Y^2\le N\int_{\mathcal B_\delta}Y\le NE_0/(2\nu)`
> gives the first bracket as a bound for `\int_0^\tau K\,dt`, `K=K_u` the full
> strain work of \eqref{eq:quotient-evolution}. By `lem:quotient-lowstrain`
> with `L=0`, `K=K_0+K_{\rm low}` and `|K_{\rm low}(t)|\le M_0\mathcal Q(u(t))`
> with `M_0=3(1+C_{\mathbb P})C_B2^0\|u_0\|_2`. By
> `rem:highstrain-normalisation` (equivalently HF21-B Corollary 4.4),
> `\int_0^\tau\mathcal Q\,dt\le\frac13H^{1/4}(3C_S^2E_0^2/(2\nu))^{3/4}` for
> `\tau<\min\{H,T_*\}`, which is input-only. Hence
> `\int_0^\tau K_0=\int_0^\tau K-\int_0^\tau K_{\rm low}\le\int_0^\tau K+M_0\int_0^\tau\mathcal Q`,
> which is the display. `\theta=0` is admissible because `D_{\mathcal Q}\ge0`.
> `prop:quotient-conditional` then gives `hyp:critical` for the datum with
> `M=C_{\mathbb P}(\|u_0\|_3^3+3A_{\rm input})^{1/3}e^{M_0H/3}`, and
> `thm:continuation` gives `T_*>H`. `\square`

The repair changes nothing structurally: the added term is input-only, carries
no `N` and no `\sup_{\mathcal B_\delta}Y`, and introduces the horizon `H`,
which `hyp:highstrain` already permits. **Proposition 4.1's deficit statement
stands verbatim** once the same additive input term is carried there, and the
sharpness argument (Prop. 4.2) is untouched because it concerns only the
`\int_{\mathcal B_\delta}Y^2` factor.

### R2. Repair of D2 — Remark 3.4 and §7

Delete "The hypothesis is **strictly weaker than a Serrin bound**" (RESULT
bullet 3), "**(the hypothesis is strictly weaker than a Serrin bound)**"
(Remark 3.4 heading), and "This is a strictly weaker question than a Serrin
bound (Remark 3.4)" (§7 NEXT DISTINCT ACTION). Replace by:

> **Remark 3.4′ (the exact status of (H-BY)).** (H-BY) constrains `Y` only on
> `\mathcal B_\delta`, a set of measure at most `\beta`, and says nothing on
> `\mathcal G_\delta`; for a fixed trajectory and a fixed `\tau` it is
> therefore a strictly weaker *pointwise* requirement than an enstrophy or
> Serrin bound on `(0,\tau)`. As an input-uniform existential hypothesis it is
> **not** weaker: by Lemma A it is equivalent to `T_*>H` for the datum, hence
> equivalent to `hyp:highstrain`, to `hyp:critical`, and to a Serrin bound at
> the same quantifiers. It belongs to the existential-equivalence class of
> every formulation the programme has produced, and nothing here changes that.
> What the reduction does supply is a narrower *search surface* — the enstrophy
> on a set of input-bounded measure, with `\mathcal G_\delta` free — together
> with the observation of §4.2 that, at fixed `N`, the constant is monotone
> increasing in `\delta`, so the entire value of the restriction is carried by
> the `\delta`-dependence of `N`.

(Lemma A is displayed in §E10 above and should be transcribed into the target
as the justification.)

### R3. Minor repairs

- **Cor. 1.5 / Prop. 4.4(1).** Replace "the defect's spacetime hull is a
  single point" and "the defect contributes a single point and no segment" by
  "the *import* supplies a single point for `w` and `q`; the segment they do
  have, spanned by `L^4_tL^3_x` (from `\|w\|_3\le\|u\|_3`,
  `\|q\|_3\le2\|u\|_3` and \eqref{eq:L4L3}) and `L^2_tL^6_x`, is inherited
  from `u`'s own hull and lies entirely at `\lambda=\frac32`". The conclusion
  "deficit unchanged at `\frac12`" is unaffected.
- **Prop. 1.4 / RESULT bullet 1.** Replace "granting it changes nothing" by
  "granting it improves the numerical constant of `\beta` (by a factor `64`
  for the natural GN constant `C^4=3C_S^2`) and changes nothing structural,
  because by Corollary 4.3 the deficit factor `\sup_{\mathcal B_\delta}Y` is
  insensitive to the value of `\beta`".
- **Prop. 4.4(2).** Add: "over the exponents `s\le4` for which the audited
  record supplies a budget; `hf22-direct-attack` Prop. 2.4 records that the
  same family reaches `\lambda=1` at `s=\infty`, where the block moves from
  the exponent to the factor `\int D\,dt`."
- **Prop. 4.2 / RESULT bullet 4 / Cor. 4.3.** Unify the plateau constants
  (`E_0/(4\nu M)` and `ME_0/(4\nu)`, or the saturated `E_0/(2\nu M)` and
  `ME_0/(2\nu)`; pick one).
- **Theorem 3.1, RESULT bullet 3.** Replace "strictly sharper" by "sharper as
  a bound on `\int K`, and silent about `\int cD`", matching the body.
- **Cor. 4.3.** Add the two strengthenings of §E7: the Cauchy–Schwarz floor
  `\int_{\mathcal B_\delta}Y^2\ge(\int_{\mathcal B_\delta}Y)^2/|\mathcal B_\delta|`
  (a smaller bad set raises the floor) and the `\delta`-monotonicity of the
  constant.
- **§E6's second-route coincidence.** Add to Remark 3.5: reduced with the same
  supremum, the `L^2\times L^2` route yields the identical constant
  `\frac5{16}C_S^3E_0\sup_{\mathcal B_\delta}Y/\nu`, so the deficit factor is
  route-independent within the audited record.
- **§5.** Either display the ramp profiles for `(Y,Z)` on the up- and
  down-ramps and the tail's contribution to the integrated (T14), or label
  Theorem 5.2's ramp verification explicitly as a sketch.

---

## CONDITIONAL SUFFIX THAT SURVIVES

Unconditionally, from audited inputs only, for the maximal classical branch of
a divergence-free Schwartz datum, every `\delta\in(0,1)` and every
`\tau<T_*`:

1. **Theorem 2.1** (new, correct, unconditional, for every solenoidal
   `u\in H^m`, `m\ge4`):
   `D_{\mathcal Q}(u)\le2\|w\|_6\|\nabla w\|_2\|\nabla u\|_3
   \le\frac52C_SY\|\nabla u\|_3\le\frac{5\sqrt3}2C_S^{3/2}Y^{5/4}\|\Delta u\|_2^{1/2}`.
   This is the first upper bound for the quotient dissipation in the record and
   is the note's clearest new contribution, even though the note shows it
   cannot enter the closing route.
2. **Proposition 1.1 / Corollary 1.2**: `Y>y_\delta` on `\mathcal B_\delta` and
   `|\mathcal B_\delta|\le\beta=24C_S^2C_\sharp^4E_0^2\delta^{-4}\nu^{-5}`,
   `\tau`-uniform — the audited HF21-B bound, re-derived by the reordered
   proof.
3. **Theorem 3.1**:
   `\int_0^\tau K\le\frac{\delta}{1-\delta}\mathcal Q(u_0)+\frac1{1-\delta}\int_{\mathcal B_\delta}K`.
4. **Theorem 3.2**:
   `\int_0^\tau K\le\frac{\delta}{3(1-\delta)}\|u_0\|_3^3+\frac{5C_S^3}{8(1-\delta)}\int_{\mathcal B_\delta}Y^2`.
5. **Proposition 4.1** (the main claim, as repaired in §R1): the integrated
   strain work is bounded by input-only quantities plus the additive
   `K_{\rm low}` term, **except for the single factor**
   `\operatorname{ess\,sup}_{\mathcal B_\delta}Y`, with the displayed
   constant `\frac{5C_S^3E_0}{16\nu(1-\delta)}`; and that factor is sharp
   against the audited budgets (Prop. 4.2, and independently against the
   HF22-C family, §E9).
6. **Theorem 3.3′** (conditional): (H-BY) ⟹ `hyp:highstrain` with `\theta=0`
   ⟹ `hyp:critical` for the datum ⟹ `T_*>H`, with the repaired
   `A_{\rm input}`. By Lemma A the implication is an equivalence, so this is a
   reformulation of the conclusion, not a reduction of it.
7. **Proposition 4.4** (bookkeeping, as qualified): the import adds no point to
   the LPS hull; the `cD` route at the audited `s=4` sits at `\lambda=\frac56`;
   the `K` route sits at `\lambda=1`; the restriction to `\mathcal B_\delta`
   moves neither number.
8. **Theorem 5.2** (non-derivability, ramp sketch noted): the HF22-C family
   extends to a tuple satisfying (T1)–(T15) with
   `\int_{\mathcal B_\delta}cD\to\infty` and `|\mathcal B_\delta|\to0`, so the
   bad-set restriction of (G) is not derivable from that enriched list.

---

## UNNECESSARY DEPENDENCIES

- **Theorem 2.1 is not used by any other statement in the note.** §2.2 shows it
  yields only inert consequences and Cor. 2.3 shows it cannot enter the
  `\theta=0` route. It should be kept — it is the note's one genuinely new
  inequality and belongs in the record — but it should be relabelled as a
  standalone result rather than a step in the deficit argument, so that a
  future reader does not look for its load.
- **Proposition 1.3 is motivational only.** The unavailability of (1.2) is
  established by the two classical routes (`w\in L^2` and `\sigma\in L^{3/2}`),
  each citing `rem:quotient-divcurl-scope` directly; the scaling enumeration
  adds rhetorical completeness, not necessity, and it carries the one soft step
  (`\gamma=0`).
- **Corollary 1.5 is redundant** given Prop. 4.4(1), which reaches the same
  conclusion by the correct route ("the same point of the hull"), and it is the
  source of the false "single point" sentence. It can be deleted outright.
- **(T7), (T12), (T15) do no work in Theorem 5.2** — all three are slack on the
  family by construction (`Y\to\infty` on the phases, `y_0` free on the tail).
  (T13) and (T14) are the only additions that bind, and they bind only through
  the single `n`-independent numerical inequality
  `\mathcal Q_0^4\le2C_Ec_1^4y_1^8`. Theorem 5.2 would be sharper if it said so.
- **Remark 3.5 is recorded and unused**, correctly; §E6 shows it is not merely
  non-comparable but reduces to the *same* constant, which makes it a
  confirmation rather than an alternative.
- **`cor:quotient-vorticity-zero` and `lem:trace-control` appear in the input
  list and are used nowhere.** Harmless, but the list overstates the
  dependency footprint.

---

## NON-CLAIMS

This audit does **not** claim:

- that (G), its bad-set restriction, `hyp:highstrain`, `hyp:critical` or NS-R3
  is proved, disproved, or advanced toward a proof;
- that (H-BY) is **false**. By Lemma A it is equivalent to `T_*>H`, so
  refuting it for a datum would be a finite-time blowup proof; it is neither
  provable nor refutable by the means in the record;
- that the bad-set restriction of (G) is false. HF22-C Theorem B is an
  equivalence, so it cannot be false unless (G) is;
- that (1.2) `\|q\|_3\le C\|\nabla q\|_2^{1/2}\|u\|_2^{1/2}` is false, only
  that it is not derivable from the listed record and that its consequences for
  the measure bound are a constant factor;
- that Theorem 5.2's list (T1)–(T15) is exhaustive, or that its ramp
  construction is fully displayed;
- that the target's numerics were re-derived from a solution of Navier–Stokes;
  the HF22-C family is a tuple of real functions and is not claimed to be a
  trajectory (HF22-C Theorem D);
- any novelty or priority for Theorem 2.1 beyond "not previously in this
  programme's record";
- anything about HF25, which is under parallel audit, is not used by the
  target, and is not used here;
- that the sibling lane HF24-A is correct or incorrect in any respect other
  than the single logical point of §E10, which is assessed from `PLAN.md`'s
  description of that lane, not from an audit of its file.

Nothing is promoted; no manuscript, plan, or graph file is touched by this
audit.

---

## REOPENING CONDITION

The blacklisted implication is exactly one: **"(H-BY) is strictly weaker than a
Serrin bound"** (and its sibling in `PLAN.md`, "It is strictly weaker than a
Serrin bound, since it constrains the enstrophy only on a set of
input-bounded measure and leaves the good set free"). Reopen it only on one of
the following:

1. **A quantitative form of Lemma A's converse that fails.** If someone
   exhibits a class of data for which `T_*>H` does *not* yield an
   input-*computable* `N` while (H-BY) with a computable `N` is available, the
   distinction between the two hypotheses becomes effective rather than merely
   existential and the "strictly weaker" claim can be reinstated in an
   effective form. Lemma A's converse is non-constructive; nothing in this
   audit rules out an effective separation.
2. **A bound for `\operatorname{ess\,sup}_{\mathcal B_\delta}Y` that uses the
   defining property of `\mathcal B_\delta` and not merely its measure.**
   Corollary 4.3 and §E7 close every route through
   `\{Y>y_\delta,\ |\mathcal B_\delta|\le\beta,\ \int_{\mathcal B_\delta}Y\le E_0/2\nu\}`.
   A route that instead uses `\|q(t)\|_3>\delta\nu/C_\sharp` *as a structural
   constraint on the field* — for instance a lower bound on `\|\sigma\|_{3/2}`
   or on the geometry of `\{w=0\}` forced by a large defect, coupled back to
   the enstrophy — is not covered by the enumeration and would reopen the
   accounting.
3. **Any new spacetime integrability that is not a pointwise multiple of `Y`.**
   Proposition 1.4's "reason, stated once" is the exact hinge: the import's
   budgets are corollaries of `\int Y`. An estimate producing, for example,
   `\int_0^\tau\|\Pi_u\|_2^2\,dt` or `\int_0^\tau\|\sigma\|_{3/2}^s\,dt`
   input-boundedly, not through `Y`, would put a genuinely new point on the
   LPS hull and reopen Prop. 4.4(1) and Cor. 1.5.
4. **A weighted or localized form of Theorem 2.1 with `\|\nabla u\|_2` in place
   of `\|\nabla u\|_3`.** The note's own last open question. It would place `D`
   inside the energy budget and void Corollary 2.3, which is currently the
   statement that forces `\theta=0` and hence forces the whole `Y^2` accounting.

---

## EXACT EDITS FOR THE CONTROLLER, IF THIS VERDICT STANDS

**In `research/evidence/hf24-badset-restriction.md`** (owner lane, not this
audit):

1. Replace Theorem 3.3's `A_{\rm input}` and Prop. 4.1's display by the
   repaired constants of §R1, and transcribe Theorem 3.3′ with its proof.
2. Replace Remark 3.4, RESULT bullet 3's last sentence, and §7's "NEXT DISTINCT
   ACTION" first sentence by Remark 3.4′ of §R2, and transcribe Lemma A of
   §E10 with its proof as the justification.
3. Apply the six minor repairs of §R3 (Cor. 1.5 / Prop. 4.4(1) wording;
   Prop. 1.4's "changes nothing"; Prop. 4.4(2)'s `s`-range; the plateau
   constants; Theorem 3.1's "strictly sharper"; Cor. 4.3's two strengthenings),
   and add the route-coincidence observation to Remark 3.5.
4. Relabel Theorem 2.1 as a standalone result; delete Cor. 1.5 or restate it as
   in §R3; label Theorem 5.2's ramp verification a sketch or complete it.
5. Add to Open Questions: "needs review: whether the equivalence of Lemma A
   admits an effective form, i.e. whether an input-*computable* `N` on
   `\mathcal B_\delta` is strictly easier than an input-computable Serrin
   bound; this is the only sense in which the bad-set restriction can be
   weaker."

**In `PLAN.md`**, HF24 block:

6. Under "**Convergence again.**" (L1366–1372), strike "It is strictly weaker
   than a Serrin bound, since it constrains the enstrophy only on a set of
   input-bounded measure and leaves the good set free." Replace with: "The
   audit establishes that this question is equivalent, at the programme's
   quantifiers, to global continuation past the horizon for the datum, hence to
   the critical hypothesis and to a Serrin bound; it belongs to the
   existential-equivalence class, exactly like the HF25 defect hypothesis. It
   is strictly weaker only pointwise, for a fixed trajectory: it constrains the
   enstrophy on a set of input-bounded measure and leaves the good set free.
   The narrowing is of the search surface, not of the assumption. The same
   correction applies to the corridor form of `hf24-modulus-of-continuity.md`,
   whose claim that the corridor restriction is 'the whole distance between its
   hypothesis and its conclusion' does not survive: restricting the set of
   times does not lower existential strength."
7. In the HF24-B paragraph (L1352–1364), after "demands the Serrin line
   exactly", add: "audited and confirmed digit for digit, with the
   qualification that the one-sixth overshoot is the best value over the
   exponents the audited record supplies (`s\le4`); the same family reaches the
   Serrin line at `s=\infty`, where the block moves to the dissipation
   integral."
8. Record the audit verdict: "`hf24-badset-restriction.md` audited 2026-09-06:
   **REPAIR**. All constants recomputed and reproduced, including the measure
   bound `24C_S^2C_\sharp^4E_0^2\delta^{-4}\nu^{-5}`, the deficit constant
   `5C_S^3E_0/(16\nu(1-\delta))`, the three LPS positions `3/2, 5/6, 1`, and
   the `5\,038\,848` slack of the enriched obstruction family. Two repairs
   applied: the `K_{\rm low}` term missing from Theorem 3.3's `A_{\rm input}`,
   and the withdrawal of 'strictly weaker than a Serrin bound'. Theorem 2.1,
   the first upper bound for the quotient dissipation, is new and correct."
9. In "The sharpened first gap", extend the second caution to name both HF24
   hypotheses alongside the HF25 one as members of the existential-equivalence
   class.

**Nothing else.** No manuscript edit is warranted by this audit: the target
does not propose one, and every manuscript statement it uses was used inside
its stated scope.
