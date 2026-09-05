# Navier–Stokes programme

```yaml
terminal_claim: NS-R3
phase: paper-preparation
phase_i_status: not-started-awaiting-user
phase_ii_status: not-started
paper_status: architecture-under-development
active_task: source-audit-and-paper-architecture
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

FIRST GAP: derive from arbitrary initial data an a priori critical-norm or
equivalent continuation bound valid up to any putative finite singular time.

FALSIFIER: an invalid norm interpolation, a hidden smallness hypothesis, a
bound that depends on the very norm it must control, or a change of equation.

FORBIDDEN INFERENCES: energy bounds imply critical control; an ODE upper bound
that can blow up proves PDE blowup; a conditional continuation theorem proves
its missing hypothesis; weak nonuniqueness refutes Clay smooth existence.

CHECK: direct proof and independent falsification of the proposed critical
bound, plus audit of every continuation-theorem hypothesis.
