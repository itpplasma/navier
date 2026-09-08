# Navier--Stokes: original-nonlinearity critical control after the Tao audit

```yaml
terminal_claim: NS-R3
checkpoint: CP1
phase: tao-audit-and-structural-research-2026-09-08
phase_i_status: reopened-2026-09-06-in-progress
phase_ii_status: reopened-2026-09-06-target
paper_status: conditional-manuscript-held-after-strategic-pivot
paper_repo: writable-authorized-2026-09-06
external_deps: permitted-if-no-axioms-beyond-mathlib
active_task: original-nonlinearity-critical-producer-unresolved
active_architecture: no-complete-positive-producer-selected
complete_terminal_route: none-established
terminal_status: not-proved
terminal_obstruction: input-only-critical-bound-not-produced
refinement_wave: reviewed-conditional-consumer-preserved
run_status: completed-with-terminal-gaps-open
averaging_gate: exact-proof-assumptions-not-lane-names
averaging_audit: preceding-proof-repair-required
averaging_repair: author-proof-independent-audit-pending
incumbent_producer_class: averaging-invariant-budgets-remain-excluded
secondary_goal: MIC-R3
secondary_goal_status: kinetic-and-microscopic-interfaces-remain-separately-gated
formal_work_this_run: deferred
public_release: false
```

## Authority, target, and preserved state

This is the sole live task/status record. The current owner request resumes
research, asks for solutions to the blockers, and authorizes commit/push in
private `itpplasma/navier`. It does not authorize publication, outside
contact, authorship changes, force pushes, or writes to the manuscript and
formal repositories. No worker or background computation is running.

NS-R3 remains: every real solenoidal Schwartz datum on R3, every fixed
nu>0, original unforced incompressible NS, globally smooth velocity AND
normalized pressure, the prescribed initial trace, and energy at most its
initial value. A rigorous counterexample must meet that same equation and
data contract. Modified, forced, periodic, kinetic and microscopic claims
are different claims. NS-R3 and CRITICAL remain gaps in the UNCHANGED
canonical `docs/proof-graph.yaml`.

This run read main at `0b087fe886d829ecca8a5591232030fcd6df45b0`.
The entire preceding PLAN is preserved by its original Git blob
`51f9fa38bdf3140ff75fb6e9917ce3704193af22` at
`research/history/PLAN-before-tao-audit-2026-09-08.md`. Its completed-worker,
resource, validation, and stopped-run descriptions are history, not claims
about workers or checks performed in this run. All preceding reviewed
components, exact counterexample scopes, and pending audit qualifications
remain in force except for the corrections below.

Read `AGENTS.md`, `docs/proof.md`, the canonical graph and
`research/verify.py`; the refinement contract/maps and kinetic contracts
retain their separate mathematical specifications. This PLAN supersedes
stale allocation words such as "active" or "incumbent" in those maps.

## Completed this run: repair of the averaging argument

The full derivation and source ledger are
`research/evidence/2026-09-08-tao-packet-audit-and-repair.md`.
The preceding averaging proof is preserved byte-for-byte at
`research/history/averaging-obstruction-before-audit-2026-09-08.md`, blob
`501e99d2a7b070252ff791f0651563a42be8e326`. Its old path now points to the
corrigendum. The old proof is NOT accepted as written.

The fresh-context audit found the following substantive defects: finite-q
synthesis produces L^{3,q}, not L3; the final published averaging includes
dilations; exact original triad identities do not all transfer; and an
inequality's syntax does not identify its invariant proof assumptions.
Using Tao's actual checkpoints also requires a maximal-lifespan adapter,
not a silent use of a proposition stated under global-existence hypotheses.

The replacement author proof establishes the stronger averaged-only claim

    sup_(0<=t<=H) sup_j
      N_j^(1/2)||v_(N_(j+1))(t)-v_(N_j)(t)||2 = infinity,
    N_j=2^j N0,

for one fixed Tao cascade operator and Schwartz datum at unit viscosity,
on a finite H, for every N0>0. Thus even the uniform ell-infinity increment
bound fails there, and all finite-q RF bounds fail as well.

Its chain is explicit: Sobolev mapping estimates including dilations give
projected global flows and compact-classical L2 identification; the
published finite-step cascade is localised by excluding a lifespan exit
using its high-mode H4 bound; a telescoping annular-packet test contradicts
the resulting growing critical packet amplitudes. No original-NS endpoint
theorem is applied to the averaged equation. The new derivation, especially
its lifespan adapter, still needs an independent mathematical audit.

Additional exact results in the same file: weak-L3 divergence of that
particular cascade; a smooth solenoidal field sequence disproving the
false L2-plus-L^{3,q}-to-L3 inference; failure of common-translation
covariance for the fixed cascade; and the one-carrier Fourier-support
obstruction to an exact same-annulus original-NS pump.

These results repair and sharpen the obstruction. They are NOT a positive
critical estimate for original NS, and are not terminal regularity progress.

## The corrected averaging gate

A proposed positive producer must identify a necessary step whose hypotheses
or conclusion fail for the specific averaged counterexample. Energy and
operator-uniform norm estimates alone remain insufficient. Keep the valid
reviewed component estimates; do not promote an unproved budget.

Do NOT retire every method called "smooth-block", "signed-phase", or
"shell-budget" merely by its name. Original NS has the exact identity

    B(T_a f,T_a g)=T_a B(f,g),

whereas the fixed packet cascade fails it on real Schwartz inputs. Exact
common transport, common-translation Fourier phases, pressure structure,
and physical-space locality must be examined in an actual proof rather
than declared averaging-invariant. Passing this test only avoids this
counterexample; it is not evidence that the remaining estimate is true.
The existing absolute comparable-scale bound still returns to the
uncontrolled squared-enstrophy integral. No new bound for it was proved.

For a negative terminal attempt, a cascade must be realized by the ORIGINAL
Leray-projected quadratic operator, with all unwanted interactions and
viscous errors controlled. A scalar assigned pump is not such a realization.
The new one-carrier support test eliminates that particular exact embedding,
not multi-carrier circuits or all possible blowup constructions.

## Exact remaining positive edge

The reviewed original-NS LOCAL/ENERGY/CONTINUATION suffix remains available.
A full-input-dependent bound in L-infinity_t L3_x on every finite horizon
would close NS-R3. A fixed finite L^{3,q}, q>3, also closes it through the
separately inspected Phuc adapter. No q=infinity continuation is assumed.

The exact Fourier-ball family and the reviewed conditional RF-q consumer
are preserved, not required as the only architecture. With
 e_j=u_(N_(j+1))-u_(N_j), a_j=N_j^(1/2)||e_j||2, the sufficient target is

    sup_(0<=t<=H) sup_M sum_(j<M) a_j(t)^q
         <= K(d,nu,H,N0,q)^q < infinity

for ONE fixed finite q>3, uniformly in all cutoffs and every upper time.
Arbitrary amplitude, full-datum dependence, fixed positive viscosity and
non-polynomial costs are allowed. The paired identity retains BOTH source
work and resolved response:

    (1/q) Wq_M' + nu Dq_M = Piq_M,
    Piq_M=sum N_j^(q/2)||e_j||2^(q-2)
                     [<F_j,e_j>-b(e_j,u_j,e_j)],
    F_j=-(I-P_j)B(u_j,u_j).

Bounding integral_0^t Piq_M by nu integral_0^t Dq_M+C(inputs), for EVERY
upper time and uniformly M, would suffice. No such bound was obtained.
The first uncontrolled term is signed comparable-frequency production
correlated with the actual resolved response. Bounding source and strain
separately, or returning to integral ||grad u||2^4, does not close it.

A direct original-pressure alternative retains the canonical cubic balance

    (1/3)(||u(t)||3^3-||d||3^3)
       = integral_0^t [P3(u)-nu D3(u)].

A uniform input-only upper bound on its right side would also suffice.
This is the same missing positive estimate in another formulation, not a
new solution. A proposed geometric, Lagrangian, pressure-Hessian, kinetic,
or phase-sensitive mechanism must supply its actual quantitative gain
without assuming a future critical norm, recurrence, Type I behaviour, or
uniform conditioning. Merely adding a discriminator or a new functional
is not a producer. No complete positive producer is selected by this run.

## Other blockers: retained scopes, not silently marked solved

The causal/restart and slow-manifold branches retain their finite-cutoff
results and nonuniform reconstruction/conditioning gaps. Static C2 slaving,
polynomial metric costs, and entire zero-centred series retain their exact
scoped exclusions. They are optional mechanisms, not prerequisites of the
reviewed direct whole-space conditional consumer.

The singularity/rigidity branch still requires both an admissible extraction
and a Liouville theorem for the ACTUAL limit class. Affine, shear and
inviscid limits cannot be excluded by importing a theorem for a smaller
bounded positive-viscosity class. The interrupted record and signed-transfer
notes retain pending-review status; this run supplied no new rigidity.

The kinetic route still lacks its uniform resolved-momentum critical bound
and complete application audit in the stated whole-space hard-sphere class.
The microscopic extension additionally needs a compatible particle-to-kinetic
solution class and a whole-space/domain limit. Regular-fluid-target and
regular-Boltzmann results cannot be used to assume the missing regularity.
These are not all discharged by a fluid estimate. See
`research/kinetic-clay-hilbert-contracts.md` and
`literature/kinetic-hilbert-scope.md`. No kinetic or microscopic gap was closed.

Formal Phase I/II meanings and statuses are unchanged. No Lean coverage,
manuscript theorem, new imported canonical claim, or independent audit of
the replacement proof is asserted.

## Validation and next handoff

The new exact regression has 204 passing assertions; its output is
`research/evidence/2026-09-08-tao-packet-checks.json`. The existing
`research/check_closed_feedback.py` was also rerun: 652 assertions passed,
after verifying the local script against frozen Git blob
`ba8c7d8df16d943bb8738bb12c526acbc282b20e`. These are finite algebra,
scaling, support and phase checks, not PDE certification. Local PLAN
YAML/status and changed-file whitespace checks passed separately. The
execution environment did not provide a full research checkout, so
`research/verify.py --research-only`, the rest of the regression suite,
manuscript checks and Lean builds were NOT run. Do not relabel this
narrower validation as a full checkout PASS. The canonical graph is
preserved rather than promoted.

The next review input is the frozen replacement proof, with special scrutiny
of the lifespan-exit argument in Section 4 and the quantifiers in Section 2.
Further positive work must attack the remaining original-operator estimate,
not re-prove the conditional consumer or repeat an invariant shell budget.
Refresh main before every write; preserve concurrent edits and use ordinary
non-force updates. No task is running after this handoff.
