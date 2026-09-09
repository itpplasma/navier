# Structural obstructions for the original three-dimensional Navier--Stokes equation

This is a standalone paper, separate from the retained conditional manuscript
at `../main.tex`. Its complete LaTeX source, including the bibliography, is
`main.tex`. No research-note inclusion or sibling repository is needed to build it.

```sh
cd structural-obstructions
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

## Mathematical scope

Theorem 1.1 proves that no fixed continuous symmetric quadratic form on a
finite-order whole-space Sobolev space can be both L3-coercive and monotone
along every local classical unforced Navier--Stokes solution. No spatial
symmetry is imposed on the original form. The proof includes the averaging,
measurable multiplier representation, and whole-space localization steps.

Theorem 1.2 constructs globally smooth actual unforced Navier--Stokes
solutions whose initial data have exactly the same energy, enstrophy and
maximum vorticity, but arbitrarily large initial maximum-vorticity growth.
Only the initial supports are compact. The scalar comparison exclusions
include both pointwise and almost-everywhere formulations, with their
respective finiteness and local-boundedness hypotheses.

## Status and attribution

The manuscript contains complete author-level proofs of these two statements.
A same-session adversarial proof audit and primary-source comparison are
recorded in `itpplasma/navier` at
`research/evidence/2026-09-06-structural-obstructions-paper-audit.md`.
This is not an independent expert audit, a Lean certification, or a
priority certificate. No unresolved arbitrary-data estimate is used in
these proofs. Arbitrary-data global regularity is neither proved nor disproved.

The qualitative quadratic-energy obstruction is established background,
explicitly discussed in Goulart--Chernyshenko (2012) and
Darrow--Carlson--Goluskin (2026), with older quadratic-invariant literature.
Do not advertise that principle as newly discovered. The exact whole-space
formulation and the matched-scalar globally smooth family are the scoped
results; priority for those formulations is not certified.

The prior conditional manuscript, its proof map, all research evidence and
formalization are preserved. This paper does not promote NS-R3 or CRITICAL.
Authorship is left blank. Public hosting in `navier/paper/` was authorized
on 2026-09-09. Submission and outside contact remain unauthorized.
