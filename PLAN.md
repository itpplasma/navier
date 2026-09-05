# Navier–Stokes programme

```yaml
terminal_claim: NS-R3
phase: awaiting-user-phase-i-kickoff
phase_i_status: not-started-awaiting-user
phase_ii_status: not-started
paper_status: conditional-manuscript-with-explicit-high-frequency-gap
active_task: await-user-phase-i-kickoff
public_release: false
```

## Objective

Resolve Clay's unforced existence-and-smoothness alternative on R3: for every
smooth divergence-free rapidly decreasing initial velocity and every viscosity
nu > 0, construct a global smooth velocity and pressure satisfying the original
equation and a uniform finite kinetic-energy bound. The exact official data
class and alternatives are recorded in the literature dossier. The periodic
problem is a separate alternative, not an automatic corollary of the R3 proof.

## Authority

`docs/proof-graph.yaml` is the dependency map; `docs/proof.md` gives the
paper argument and exact open bridge. `literature/` holds source evidence.
`research/verify.py` checks structural consistency only. Independent review
of mathematical implications is required separately.

## Phase boundary

Paper preparation precedes the two formalization phases. Phase I proves all
project-owned manuscript steps in Lean down to precisely stated, directly
verified literature theorems. Phase II proves the remaining literature
theorems from Mathlib. No Lean implementation begins before the user kicks
off Phase I. The present request ends with a reviewed paper handoff, with any
unresolved mathematics stated explicitly.

## Frontier packet

TERMINAL CLAIM: NS-R3, the unforced full-viscosity equation on R3 for arbitrary
Clay data, with global smoothness and finite energy.

ESTABLISHED: local classical solvability, energy dissipation, and published
continuation criteria, subject to exact source-hypothesis verification.

FIRST GAP: HIGH-PRESSURE in the graph. Prove a signed high-output pressure
absorption estimate for every arbitrary-data classical trajectory, uniform
for tau < min(H,Tstar), with a finite input-only remainder. The low-output
pressure work is already bounded by energy. Alternative producers of a
critical continuation bound remain possible.

FALSIFIER: an invalid norm interpolation, a hidden smallness hypothesis, a
bound that depends on the very norm it must control, or a change of equation.

FORBIDDEN INFERENCES: energy bounds imply critical control; an ODE upper bound
that can blow up proves PDE blowup; a conditional continuation theorem proves
its missing hypothesis; weak nonuniqueness refutes Clay smooth existence.

CHECK: direct proof and independent falsification of the proposed critical
bound, plus audit of every continuation-theorem hypothesis.

## Paper preparation

Four Luna research lanes collected the official statement, foundational and
critical results, blowup barriers, and recent developments. Four Sol workers
developed the architecture, enstrophy and compactness evidence, a frequency
reduction, and the manuscript; distinct scopes received frozen independent
audits. The literature search is substantial but not exhaustive.

The manuscript at `navier-paper` source commit `d7563ef` contains complete written
arguments for the classical estimates, the cubic pressure balance, the
low-frequency pressure lemma, and the conditional continuation chain.
The source premises are Tao Theorem 5.4 and GKP Theorem 4, directly inspected
in the scope recorded in `literature/`. No new universal high-frequency
estimate or solution of the Millennium problem is claimed.

The evidence reviews use exact immutable revisions and distinguish valid
conditional conclusions from the unresolved terminal theorem. The final
integration review and its repair confirmation are in
`research/evidence/review-integration.md`: PASS for the conditional dossier,
FAIL WITH SCOPE for the terminal Clay claim. Its first unsupported bridge is
HIGH-PRESSURE. This is a prepared research handoff, not a completed proof of
the Millennium problem. No Lean files have been created.

## Private manuscript and verification

The private manuscript authority is
https://www.overleaf.com/project/6a9bb675ea9d4d0d368d8ee6.
The private `itpplasma/navier-paper` repository is its synchronized archive,
with the `overleaf` remote authoritative. The research repository is private
`itpplasma/navier`. No collaborators were added or contacted.

Verified at this handoff:

- Local manuscript and proof-map builds pass without undefined references or
  layout overflow; the manuscript is six pages and the map supplement four.
- The private Overleaf manuscript compiles successfully. Its fetched source
  matches the archive, and its rendered PDF was inspected.
- The manuscript has 49 resolved internal links, and the map has 43, including
  map-to-claim and claim-to-map directions. Color and grayscale map renderings
  were inspected.
- The structural verifier checks 13 acyclic claim records, source paths, and
  manuscript labels. It is a document-integrity check, not a mathematical test.
- Component and integration audits independently reconstruct the conditional
  mathematical implications at the frozen revisions recorded in their files.

## Next authorized boundary

Wait for the user to kick off Phase I. The open mathematical research task is
to prove HIGH-PRESSURE, repair its mechanism, or find a distinct a priori
continuation producer. Formalizing the current conditional implication alone
would not discharge that gap. Any future claim of a completed proof must
prove the missing producer and pass a new independent frozen audit.
