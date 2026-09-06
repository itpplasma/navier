# Navier--Stokes: terminal-first closure search

```yaml
terminal_claim: NS-R3
checkpoint: CP1
phase: arbitrary-data-terminal-architecture-search-2026-09-06
phase_i_status: reopened-2026-09-06-in-progress
phase_ii_status: reopened-2026-09-06-target
paper_status: conditional-manuscript-held-after-strategic-pivot
paper_repo: writable-authorized-2026-09-06
external_deps: permitted-if-no-axioms-beyond-mathlib
active_task: terminal-closure-search-after-quadratic-and-local-energy-exclusions
active_architecture: none-passes-complete-terminal-gate
complete_terminal_route: none-established
retired_primary_route: pressure-quotient-defect-shell-material-response
intrinsic_bridge_status: author-checked-independent-audit-pending
single-profile-rigidity_status: falsified-for-the-normalized-package
two_balance_falsification_status: author-checked-independent-audit-pending
quadratic_lyapunov_status: author-checked-independent-audit-pending
local_energy_only_status: source-statement-checked-consequence-author-checked
terminal_status: not-proved
terminal_obstruction: unchanged
formal_work_this_run: deferred
public_release: false
```

## 1. Target and exact terminal edge

For every fixed positive viscosity nu and every solenoidal Schwartz datum
u0 on R3, prove global smooth existence for the ORIGINAL unforced
Navier--Stokes equation, with kinetic energy bounded by its initial value.
Neither a forced/averaged model nor a comparison curve proves this target.

The retained LOCAL, ENERGY and CONTINUATION nodes in
`docs/proof-graph.yaml` give the following complete suffix: an input-derived
finite bound

$$
 \sup_{0\le t<\min(H,T_*)}\|u(t)\|_3\le F(u_0,\nu,H)<\infty
$$

for every finite H rules out any finite maximal time; LOCAL then gives
smoothness on every compact time interval and ENERGY supplies the energy
bound. Defining F using an unknown terminal norm is not an argument.
A direct contradiction to finite Tstar may bypass this L3 route.

**The terminal theorem is not proved and its obstruction has not been
strictly reduced.** The current research delta is a rigorous exclusion of
specific closure mechanisms, with author proofs awaiting independent audit.
No conditional criterion is promoted to a producer.

## 2. New mathematical exclusion and resulting allocation

Read the complete derivations in
`research/evidence/2026-09-06-two-balance-falsification.md` before reopening
any of the following routes.

**Critical two-scalar Lyapunov closure is falsified.** There is no C1
scale-invariant F(E,Y), coercive in EY, which is nonincreasing on every
actual classical NS trajectory. Here E=||u||_2^2 and Y=||grad u||_2^2.
Scale invariance forces F(E,Y)=Phi(EY). A compactly supported positive-
stretching datum, varied in amplitude, makes (EY)' positive at every
sufficiently large value of EY. Monotonicity would force Phi to be
nonincreasing on a tail, contradicting coercivity. Had the candidate been
true, ||u||_3^4 <= C EY and CONTINUATION would have closed the theorem.
This is a falsification on actual local NS solutions, not on a model.

**The exact global enstrophy identity does not repair scalar-budget
closure.** The new two-component countermodel has one fixed smooth
whole-space datum, one fixed positive viscosity, and a finite endpoint.
It satisfies BOTH exact global identities

$$
 E'=-2\nu Y,\qquad Y'=2S-2\nu Z,
 \quad S=\int\omega\cdot((\omega\cdot\nabla)b),\quad Z=\|\Delta b\|_2^2,
$$

with S the actual stretching of its own velocity. Nevertheless L3 diverges.
The residual is orthogonal to both b and -Delta b but has an explicitly
nonzero curl. Thus it is NOT an unforced NS solution. This closes an
explicit loophole left open by the earlier energy-exact countermodels,
which did not satisfy the exact NS enstrophy identity.

**Qualitative strong L2 compactness does not repair that inference either.**
The same curve has uniformly compact support, zero helicity, a strong L2
limit equal to a smooth nonzero field, and the energy equality at its
endpoint. A shrinking ball contains energy of order r^(1/2), which tends
to zero, while that energy divided by r diverges. Absence of an energy atom
or strong L2 continuity therefore supplies no critical spatial rate.

Retire these precisely stated closures. Do not retire local energy
transport, the full momentum/vorticity equations, spatially resolved
geometry, nonmonotone estimates, or all Lyapunov methods: those are outside
the exclusions. The new countermodel is not band-limited, not a Galerkin
solution and not known to satisfy a local NS energy inequality.

### Additional exclusions: quadratic forms and local energy alone

Read `research/evidence/2026-09-06-quadratic-local-energy-exclusions.md`.
Its Theorem Q rules out every fixed, datum-independent continuous quadratic
form on a finite-order Sobolev space that both controls L3 and is
nonincreasing along every actual local classical NS solution. Translation,
rotation and NS-scale invariance are NOT hypotheses on the original form.
Viscosity is fixed and positive. The proof first forces cubic cancellation
by varying the initial amplitude, then averages bounded bilinear forms over
translations and O(3). A whole-space localized passive-scalar triad forces
the resulting measurable radial multiplier to be constant. Its energy form
cannot control L3. This is an author proof pending independent audit.

Do not reopen this class by changing the fixed Fourier weight, adding
anisotropy or using a fixed spatially inhomogeneous quadratic kernel still
bounded on some Hm. The averaging is over uniformly bounded bilinear forms,
not an assumed compact NS orbit. Nonlinear or datum-adapted functionals,
nonmonotone estimates and unbounded spatial weights outside the continuity
hypothesis are not excluded.

A separate, source-statement-checked test excludes local-energy-ONLY
budget/packing closure. The branching Scheffer--Ozanski NS-inequality
construction yields `||b(t_j)||_3^3 = M^j ||f||_3^3 -> infinity` while
`||b(t_j)||_2^2 = (M tau)^j ||f||_2^2 -> 0`, with M>=2 and M tau<1.
The note checks this critical-norm consequence and the transfer to any
fixed positive viscosity. This is not an unforced NS solution: switching
times can have velocity jumps, and the exact energy/enstrophy identities
of the previous comparison curve are NOT asserted. Do not combine the two
counterexamples into one satisfying the union of their premises. Full
momentum/vorticity evolution and local-energy arguments using that extra
evolution remain outside this exclusion.

The same note rejects analyticity radius alone as a critical-bound
producer: entire Gaussian-based solenoidal snapshots can have fixed L2
and unbounded L3. A quantitative input-only analytic envelope, not merely
its finiteness or radius, would still have to be proved. No analytic side
machinery is an approved task.

These exclusions change the admissible research allocation, not the
terminal obstruction. NS-R3 and CRITICAL remain gaps; no new architecture
has an established complete terminal implication.

## 3. Intrinsic records are retained tools, not an approved terminal route

The author derivation in
`research/evidence/2026-09-06-intrinsic-record-tangents.md` is preserved.
At a hypothetical finite-time breakdown it constructs nonconstant centred
ancient NS/Euler limits from intrinsic Holder-record increments, with a
lower Reynolds bound and no assumed critical estimate. It neither proves
an upper Reynolds bound nor inherits global finite normalized energy.
Independent audit of the pressure gauge, weighted kernel argument and
compactness remains pending.

The actual viscous-ancestry counterexample in
`research/evidence/2026-09-06-viscous-mixing-falsifier.md` is also preserved.
It excludes blanket rigidity from the normalized package alone. Its
parents are periodic, have varying viscosities and unbounded physical
record times; it does not falsify fixed-input, fixed-viscosity finite-time
selection in the target class.

The former primary task, selecting an intrinsic tangent whose centred
projected nonlinear generator is nonzero, is **not an approved main task
by itself**. Even if proved, it leaves the nonlinear ancient profiles to
be excluded. No such complete rigidity suffix is established. This is a
failure of the terminal progress gate, not a counterexample to the
selection statement. Do not promote selection to a new terminal theorem.
A proposal using this tool must first supply a specific selection AND
rigidity mechanism reaching NS-R3 without another unknown critical bound.

## 4. Binding research gate

Before investing in X, state why X plus already-established results implies
the terminal theorem, or identify the exact plausible architecture that a
rigorous falsification of X would eliminate. An independently significant
bridge must make the remaining terminal obligation demonstrably weaker;
renaming the original obstruction is not such a bridge.

Attack the hardest implication first. Try substantially different
mechanisms. After repeated failure at the same uncontrolled quantity,
change the architecture rather than its terminology. New identities,
regularizations, clocks, local bounds, formalization and manuscript pages
are not terminal progress on their own.

The pressure/quotient/defect/speed-shell/material-response family remains
retired as the primary route. Its valid conditional results and reviews
remain intact. Reopening requires a genuinely input-only endpoint
argument, including all limiting uniformity, not another consumer.

The exact remaining obligation is still to exclude finite-time breakdown
for the actual fixed-input equation, for example by the bound in Section 1.
The exclusions in Section 2 change which approaches should be attempted;
they do not turn this obligation into a strictly weaker theorem.

## 5. Preserved history and authority

The pre-two-balance PLAN, including its ten-architecture
screen and all references, is preserved byte-for-byte at
`research/history/PLAN-before-two-balance-falsification-2026-09-06.md`,
using original blob `aa1376847ee438b5a27269d44c215ba8121ffedf` from input
commit `f95bd7c9edf18d45059c4b8b024444ac625bf96b`. It is history, not a
second live task list. The earlier pre-intrinsic PLAN remains preserved at
`research/history/PLAN-before-intrinsic-pivot-2026-09-06.md`.

The complementary marked-ancient and earlier failed-route record remains
at `research/evidence/2026-09-06-terminal-architecture-reset.md` and its
`terminal-reset/` continuations. No previous evidence file is deleted or
rewritten. No graph node is promoted; NS-R3 and CRITICAL remain gaps.

This PLAN is the sole live allocation. Manuscript work, formalization and
infrastructure are deferred for this terminal-first task. Phase I/II
coverage strings above preserve the existing status; they do not assert
new Lean proofs or authorize substituting formal work for terminal research.

Keep all repositories private. Preserve concurrent changes and use fresh
refs and non-force updates. The owner's authorization permits unsigned
commits. Do not publish, contact outsiders, invent authorship or recreate
Overleaf. Structural checks do not certify mathematical correctness.
