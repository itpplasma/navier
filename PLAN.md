# Navier–Stokes programme

```yaml
terminal_claim: NS-R3
phase: paper-integration-review
phase_i_status: not-started-awaiting-user
phase_ii_status: not-started
paper_status: conditional-manuscript-with-explicit-high-frequency-gap
active_task: frozen-integration-audit
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

The manuscript at `navier-paper` commit `3545e17` contains complete written
arguments for the classical estimates, the cubic pressure balance, the
low-frequency pressure lemma, and the conditional continuation chain.
The source premises are Tao Theorem 5.4 and GKP Theorem 4, directly inspected
in the scope recorded in `literature/`. No new universal high-frequency
estimate or solution of the Millennium problem is claimed.

The evidence reviews use exact immutable revisions and distinguish valid
conditional conclusions from the unresolved terminal theorem. Final
integration checks are in progress; no Lean files have been created.
