# HF23: an unweighted div–curl estimate for the cubic minimizer

Status: **UNAUDITED candidate**, imported 2026-09-06. Nothing is promoted, the
manuscript is untouched, and no graph node changes until an independent audit
returns.

Provenance. Arrived as a LaTeX source on the work capture surface, 1129 lines,
dropped 2026-09-06 09:14. The source is committed verbatim beside this note as
`hf23-divcurl-continuation.tex`, so no transcription step stands between the
repository and the artifact; the original is filed at
`~/Nextcloud/navier/navier-divcurl-proof-continuation-2026-09-06.tex`. Both are
frozen by SHA-256
`abe74421ef6a8a7bacc108c0c08834e32f2a6116530fceb00368c8e67b129075`.
It states the revisions it was written against: research `1014e7e`, paper
`39ccb66`, formal `54f8e89`, plus the frozen HF20 candidate, whose hash it
quotes correctly. It describes itself as self-checked, not independently
audited, promotes no repository status, and makes no priority claim.

## What it claims

**Main result.** For every solenoidal `u` in `H^1(R^3)^3`, the cubic minimizing
representative `w` has genuine unweighted weak derivatives, with

```text
    ||grad w||_2^2 <= (5/4) ||grad u||_2^2 ,
    ||grad q||_2^2  = ||div w||_2^2 <= (1/4) ||grad u||_2^2 ,
```

and `w, q` in `L^6 ∩ W^{1,2}_loc`, `grad w, grad q` in `L^2`, with no critical
smallness. It does not assert `w` in `L^2`.

**Consequences claimed.** The divergence defect `sigma = -div w` lies in `L^2`
with `||sigma||_2^2 <= (1/4)||grad u||_2^2`, equals the pointwise radial speed
derivative a.e. including across the zero set, and `q` is the gradient of the
Newtonian potential of `sigma`. The mixed-pressure pairing becomes
unconditional in `L^2 x L^2`, `K_b = int q·grad Pi_b = int sigma Pi_b`, without
the separate `L^{3/2}` hypothesis on the defect; consequently
`|K| <= (5/8) S^3 Y^2` with `Y` the enstrophy. Integrating the energy identity
gives the spacetime budgets `int ||grad w||_2^2 <= 5E_0/(8 nu)` and
`int ||sigma||_2^2 <= E_0/(8 nu)`.

**Explicitly not claimed.** Hypothesis (H2), `sigma in L^{3/2}(R^3)`, does not
follow from `sigma in L^2` on a space of infinite measure; it is bypassed, not
proved. No `L^2` bound for `w` itself and no resolution of the weighted
Calderón–Zygmund question. The document also reconstructs the HF20
construction with explicit constants and adds a fixed-energy, fixed-viscosity
spacetime obstruction covering every fixed high-strain cutoff, and it states
plainly that none of this establishes the arbitrary-data signed spacetime
bound.

## Why this matters to the programme

If it survives audit it discharges hypothesis (H1), which HF18-B introduced and
which HF21-A reduced but left open, and it does so in the stronger form
`W^{1,2}_loc` with explicit constants. HF18-B's conditional items, gated on
`w in W^{1,1}_loc`, would become unconditional, and HF21-A's Calderón–Zygmund
equivalence would be satisfied at `p = 2`. The mixed-pressure form of the
transport term, which HF18-B could only state under (H2), would become
unconditional.

## Controller check of the core (not an audit)

The mechanism is a Cordes-type argument with two pillars.

1. *The constrained matrix inequality.* The regularized Euler–Lagrange
   equation forces `d = -t e^T S e` with `S = sym grad w`, `d = tr S`, `e` the
   direction of the field and `t` in `[0,1]`. Under that constraint the note
   proves `d^2 <= (1/3)|S|_F^2`. This is *not* the false unconstrained
   inequality: for `S = I` one has `d = 3` and `|S|_F^2 = 3`, but the
   constraint fails there, so the case is excluded. Rotating `e` to the first
   axis gives `S_11 = -d/t` and `S_22 + S_33 = d + d/t`, whence
   `|S|_F^2 >= d^2/t^2 + (1/2)(d + d/t)^2 = d^2 (t^2 + 2t + 3)/(2t^2)`, and
   `(t^2+2t+3)/(2t^2) >= 3` is `3 + 2t - 5t^2 = -(5t+3)(t-1) >= 0`, valid on
   `[0,1]` with equality exactly at `t = 1`. Verified.
2. *The div–curl identities.* By Plancherel, for `z` in `H^1`,
   `||grad z||_2^2 = ||curl z||_2^2 + ||div z||_2^2` and
   `||sym grad z||_2^2 = (1/2)||curl z||_2^2 + ||div z||_2^2`. Verified.

Since `q` is curl free, `curl w = curl u`, which is exactly the audited HF21-A
Theorem 1, so an audited repository result is one pillar of this candidate.
Writing `C = ||curl u||_2^2 = ||grad u||_2^2` for solenoidal `u` and
`D = ||div w||_2^2`, the integrated inequality gives `D <= (1/3)(D + C/2)`,
hence `D <= C/4` and `||grad w||_2^2 = C + D <= 5C/4`. Verified.

The core algebra is therefore sound. What the controller did **not** check, and
what an audit must, is listed below.

## Points an audit must examine first

- The regularized problem: existence and uniqueness of the minimizer in
  `L^2 ∩ L^3`, and whether the fixed-regularizer weak derivatives are genuinely
  proved before use, as the note's own subsection heading asserts.
- The passage to the limit as the regularizer vanishes, and whether the
  regularized minimizers converge to the actual `L^3` minimizer rather than to
  some other object; the constants are uniform in the regularizer, which is
  the crux.
- The extension from `H^m` data to every solenoidal `H^1` input.
- The a.e. identity for the defect across the zero set, which uses that a
  Sobolev function has vanishing weak gradient a.e. on a level set.
- Consistency with the audited HF21-A: its Theorem 1 corollary says (H1) fails
  if the zero set meets the region of nonzero vorticity in positive measure,
  and its rigidity theorem excludes zeros of nonvanishing derivative. Together
  with this candidate those become statements about the zero set that must be
  mutually consistent, and the audit should confirm they are rather than
  assume it.
- Whether `|K| <= (5/8) S^3 Y^2` and the budgets are correctly derived, and in
  particular the note's own closing admission that an absolute estimate leaves
  the square of the enstrophy in time, not the energy integral.
- The reconstruction of HF20 and the added spacetime obstruction, against the
  already audited HF20 record.

## Frontier record

**MODE / RESULT:** DISCOVER, unaudited. Claimed: unconditional unweighted
Sobolev regularity of the cubic minimizer with explicit constants, an
unconditional mixed-pressure pairing, and spacetime budgets, together with a
reconstruction of HF20 and a further trajectory obstruction.

**FIRST GAP:** unchanged. The document states its own boundary: none of this
establishes the arbitrary-data signed spacetime bound, and the natural
absolute estimate leaves a quantity the energy identity does not control.

**SURVIVING CONDITIONAL SUFFIX:** if audited, hypothesis (H1) is discharged in
the strong form and every HF18-B item gated on it becomes unconditional; the
mixed-pressure identity holds without (H2).

**NON-CLAIMS:** no proof of (H2); no `L^2` bound for the representative; no
resolution of the weighted Calderón–Zygmund question; no regularity or blowup
result; no promotion of any graph node; no novelty or priority claim. NS-R3
remains open.

**NEXT DISTINCT ACTION:** independent audit at a different lens, freezing the
hash above and checking the points listed in the previous section.
