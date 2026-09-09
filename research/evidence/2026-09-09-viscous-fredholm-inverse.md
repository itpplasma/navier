# A full viscous localized mixed-trace inverse

Date: 2026-09-09. Input main: `75ca907cad70b7ced4469d8492e7e5dc27cc7444`.
AUTHOR PROOF; independent mathematical audit and novelty undetermined.
The full proof is integrated in `paper/sections/viscous_fredholm.tex`.
No canonical graph or formal status is promoted.

## Exact result and its consumer

On each prescribed smooth all-Sobolev solenoidal R3 history U and fixed
nu,T>0, let L_U be the complete linearized viscous NS operator. Let E(t,s)
be its forward evolution; let T(t,s) be pushforward by the actual flow of
U, solving D_U b=(grad U)b. For a fixed compact smooth cutoff chi put

    A=curl chi(-Delta)^(-1)chi curl.

This operator is bounded, nonnegative, self-adjoint, preserves every Hm,
and has compactly supported output. It is not a projection and does not
commute with heat. The integrated full-history operator

    K=integral_0^T T(0,s) E(s,0) A ds

is compact on L2_sigma(R3), and maps Hr into H^(r+sigma) for every sigma<2.
Compactness uses localized heat smoothing and the full Volterra evolution,
not a false compact Sobolev embedding on the whole space.

For every positive lambda outside a locally finite exceptional set,

    L_U v=f,
    D_U eta-(grad U)eta=v,
    v(0)=lambda A eta(0), eta(T)=0

has a unique smooth solution for smooth all-Sobolev solenoidal f. Its
initial velocity v(0) is compactly supported and smooth. The exact initial
compatibility is

    (I+lambda K)eta(0)=-b_f,
    b_f=integral_0^T T(0,s) integral_0^s E(s,r)f(r)dr ds.

A finite-rank analytic determinant proves the assertion without an
uninspected analytic-Fredholm theorem. There are arbitrarily large
admissible penalties. All pressure projections and exterior interactions
remain in E. No upper pressure-Hessian or positive displacement-action
hypothesis is used. At U=0, every positive lambda works by a noncommuting
positive-operator inverse formula.

The consumer is a prospective nonlinear zero-residual correction using
this inverse, followed by the ONE-trace and singularity-preservation
requirements UE1--UE4. This theorem does not yet supply quantitative losses
on concentrating histories, a small nonlinear defect, or one shared initial
trace. Countably many horizons can share a generic lambda, but their
initial velocities need not coincide or have summable differences.

## Relation to the concurrent obstruction and prior art

The concurrent `2026-09-09-viscous-packet-action.md` classifies failure of
Euler-shaped time-only displacement coercivity on every nonzero finite-energy
NS background. This new inverse neither uses nor repairs that form. It uses
forward parabolic smoothing followed by a compact initial-data equation.
Thus an indefinite displacement action is not proof that all mixed inverses
are unavailable. The full equations here differ from simply adding viscosity
to a pressure-only Euler Jacobi equation.

The localized curl/Newton-potential operator and initialized-mean motivation
come from the inspected Euler source recorded in
`literature/openai-euler-transfer-2026-09-09.md` and
`literature/viscous-history-source-audit-2026-09-09.md`. The source's inviscid
proof is not silently imported as a viscous one. Compact-operator reduction,
heat smoothing, Piola transport and Banach-space inversion are standard
methods. No claim of first presentation is made for their present combination.
The source repository was rechecked at
`openai/NavierStokesAndEuler@8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538`;
no new kernel build or independent source-proof audit occurred here.

## Validation boundary

`research/check_viscous_fredholm.py` passes 205 exact assertions: positive
noncommuting heat-matrix inverses (14 noncommuting cases), a nonnormal mixed
boundary calibration, finite-rank resolvent identities and smoothing powers.
It also checks that finite-horizon solvability does not imply an identical
initial trace at different horizons. Finite matrix examples are algebraic
calibrations, NOT affine finite-energy R3 solutions.

The universal analytic claims are proved in the manuscript and await
independent review. No numerical NS orbit, certified regenerative turnover,
input-only critical bound, unforced singular solution or NS-R3 proof is claimed.

All 24 research/check_*.py programs passed in the full checkout, with the
phase-ring checker run through order eight. Both research-only and paper-only
verifier modes passed (29 records, 8 pending supplements). The nested TeX
include resolver was corrected to use the manuscript build working directory,
matching latexmk rather than the including file's directory. Manuscript
`make documents check` passed with resolved references; the new section on
pages 143--146 of the 148-page main PDF was rendered and inspected.
The pre-existing history/action text is preserved byte-for-byte as
`paper/sections/viscous_history_core.tex`; its old path is now the input wrapper.
Whitespace passed. No PDF, cache, local bibtex shim or generated log is committed.
These successful checks are not an independent mathematical audit.
