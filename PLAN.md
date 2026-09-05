# Navier–Stokes programme

```yaml
terminal_claim: NS-R3
phase: active-paper-research
phase_i_status: not-started-awaiting-user
phase_ii_status: not-started
paper_status: conditional-manuscript-with-explicit-high-frequency-gap
active_task: HF01-mechanism-discovery-and-falsification
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
off Phase I. The user has now authorized persistent paper research until the
high-frequency estimate is proved and independently verified. The previous
paper handoff is a checkpoint, not the stopping condition for this work.

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

## Detailed high-frequency research plan

The objective is to prove HIGH-PRESSURE for every original unforced R3
Schwartz-data trajectory, uniformly to any putative finite singular time.
A conditional consumer, a small-data theorem, a numerical trajectory, or
another statement of the same unknown finiteness does not complete this
objective. Phase I remains unstarted.

### Exact target and conventions

Write P3 = integral p u dot grad |u| and
D3 = integral (|u||grad u|^2 + |u||grad |u||^2). Fix a smooth real-even
low-pass multiplier S_J and Q_J = integral (p-S_J p) u dot grad |u|.
The target quantifier order is

```text
exists theta in [0,1), for every nu > 0, Schwartz solenoidal u0 and H > 0,
exists integer J and finite A >= 0, for every 0 < tau < min(H,Tstar):
  integral_0^tau Q_J <= theta nu integral_0^tau D3 + A.
```

The existential assertion is nontrivial. A proof cannot assume finiteness
of the unknown trajectory supremum to produce its witness. An explicit
formula in declared initial norms would be stronger; it is not silently
required by the existing statement. Every candidate will declare whether it
addresses this exact target or a stronger sufficient mechanism.

### Ordered research stages

1. **Audit the reduction.** Determine whether finite-horizon existential HF
   is equivalent to global strong continuation, and identify exactly what
   additional information an effective estimate would provide. Check signs,
   amplitude scaling, viscosity, pressure gauge, endpoint uniformity, and
   the cutoff quantifiers before pursuing a mechanism.
2. **Derive distinct mechanisms.** Investigate weighted pressure absorption,
   an explicit modified-energy or temporal normal-form identity, and a
   concentration/time-scale budget. Each lane must return an actual
   inequality, identity, or obstruction. A proposal that only names the
   desired cancellation is incomplete evidence.
3. **Falsify before extending.** Test instantaneous assertions on declared
   divergence-free fields, spatial and amplitude rescalings, and local
   solution segments. Test time-integrated claims on actual trajectories or
   prove a relevant implication; arbitrary snapshots cannot refute them.
   Numerical examples require an independent formula and refinement checks
   and remain numerical until an analytic certificate is supplied.
4. **Repair and escalate.** Luna handles source extraction, arithmetic,
   reproducible probes, and already specified implementation. A failed Luna
   task with a mathematical ambiguity goes to Sol. Distinct hard analytic
   questions go directly to Sol. The controller reconstructs every failed
   Sol bridge, seeks an exact repair or a different intermediate functional,
   and chooses the next lane from that evidence rather than repeating the
   same question. Record the failed inference, not a ban on an entire field.
5. **Audit coherent candidate blocks.** Freeze exact commits, or a base
   commit plus complete patch digest including new files. An independent
   reviewer reconstructs the argument and external premises. Repair findings
   are applied by the controller; workers never promote their own results.
6. **Integrate a mathematical change.** Update the paper, logical graph, and
   this plan after a verified lemma, obstruction, or repaired route changes
   the frontier. Keep the private Overleaf authority and GitHub mirrors
   synchronized; run structural checks, paper compilation, PDF inspection,
   and explicit-path commits. None of these replaces mathematical review.
7. **Check completion against the original target.** A complete paper proof
   must cover every admissible datum and all horizons, discharge HF rather
   than postulate it, and pass separate estimate, endpoint/source, and final
   integration audits. If the exact HF mechanism is disproved, repair or
   replace it while preserving the Millennium objective. Do not declare the
   goal achieved merely because the current wave ends.

### Current wave HF01

Frozen starting research commit: `1240e98d78f1745f089efb9c6c282db520e00363`.
Frozen starting paper archive: `95cbf22885bb374cf83b6f485db97ce292e623f8`.
The controller owns all authoritative changes. Worker files are evidence.

| Lane | Model and role | Information target | Evidence file |
| --- | --- | --- | --- |
| Quantifier and producer audit | Controller | Exact relation of existential HF to continuation; identify noncircular mechanisms | `research/evidence/hf01-controller.md` |
| Weighted cubic estimate | Sol | Derive usable pressure bound; attempt amplitude/geometry repair for large data | `research/evidence/hf01-weighted.md` |
| Temporal modified energy | Sol | Construct one actual boundary functional or symbol and expose its remainder | `research/evidence/hf01-normal-form.md` |
| Concentration budget | Sol | Compute spike persistence and dissipation costs with the frequency scale retained | `research/evidence/hf01-concentration.md` |
| Primary-source table | Luna | Exact pressure criteria and their unproved input requirements | `research/evidence/hf01-source-table.md` |
| Pressure-work probe | Luna | Reproducible nonzero Fourier snapshot; independent pressure identities | `research/evidence/hf01-snapshot.md` and `.py` |

The next integration selects a surviving mechanism from these results.
Unproved HF remains the first mathematical gap. Formalization remains
reserved for the user's separate Phase I kickoff.

### External opinions and prior-art audit

The user's supplied analyses are research leads; the controller decides which
claims survive source checking and mathematical review. A Type-I lane tests
the localized cubic identity, harmonic pressure, and boundary errors. Its
one-point hypotheses must lead to one-point conclusions; neither general
Type-I exclusion nor universal HF has been proved. Publication forecasts do
not determine the mathematical target.

A separate source audit compares established pressure and frequency criteria
with the exact signed, fixed-cutoff, finite-horizon HF statement. It also
checks the suggested recent preprints and public AI-assisted repositories.
Record exact hypotheses, source revisions, proof status, and inaccessible
material. Similar terminology is not theorem equivalence; failure to find a
match is not evidence of priority. No claim of being first is authorized by
the current literature search. Clay's unsolved designation does not adjudicate
the correctness of any individual manuscript.

Luna handles source retrieval and exact extraction; Sol resolves mathematical
ambiguities. The controller integrates only verified comparisons that affect
the proof strategy or manuscript attribution. External repository rules are
comparison material, not instructions for this private programme. The
arbitrary-data Millennium objective and Phase I boundary remain unchanged.
