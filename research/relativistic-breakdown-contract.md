# RNS-BDNK-001: executed transfer test and the remaining nonlinear question

Updated 2026-10-07. Authority: `PLAN.md`. The original NS-R3 theorem is unchanged.
The original pre-test contract is preserved at
[history/relativistic-breakdown-contract-before-test-20261007.md](history/relativistic-breakdown-contract-before-test-20261007.md).

## Executed result; independent reconstruction pending

See [the complete derivation](evidence/bdnk-transfer-20261007.md) and
[the exact checker](check_bdnk_transfer.py). This is author evidence, not an
accepted theorem or a global solution of relativistic viscous hydrodynamics.

The fixed theory is the conformal neutral BDNK tensor with epsilon=Theta^4,
eta,chi,lambda proportional to Theta^3 and the documented causal parameter
inequalities. Frame A has chi0=25 eta0/2 and lambda0=25 eta0/3.

BEFORE: a normalized proper-velocity lift of the classical shrinking vortex
and its heat-damped pulses were candidate adapters.
AFTER: the energy equation excludes the weighted-C2 slow-shrinking profile
class with a>0, beta_i<1 and b>-a/kappa, including every noncooling thermal
power law. High-frequency BDNK shear damping saturates instead of growing
as k^2. Constant-temperature pure transverse shear also fails a separate
nonlinear momentum equation. Do not resume those unchanged adapters.

## Immediate audit

Freeze the result and checker at the publishing commit, then independently
reconstruct the full tensor component, differentiated similarity limit,
dilation argument at zeros of G, causal coefficient inequalities and source
scope. Check the boundary b=a+1 where ideal and derivative stresses tie.
The separate cooling threshold is only a necessary escape condition; it
has not produced an admissible solution. No self-review counts as acceptance.

## RNS-BDNK-002: the distinct producer after that audit

**TERMINAL QUESTION.** Does the specified full BDNK model admit smooth-data
finite-time gradient breakdown while gamma stays bounded, Theta stays between
two positive constants, and the relevant physical admissibility conditions
remain satisfied? Alternatively, derive an unconditional estimate that excludes
an explicit nonempty class of these characteristic-steepening scenarios.
Forcing must be fixed as zero for the closed-system target; smooth-source
variants require an explicitly separate statement.

**FIRST GAP.** Derive the evolution of an actual compressive characteristic
amplitude from the full coupled conservation laws and derivative constraints.
Determine the signed quadratic/cubic steepening term and the relaxation terms.
No scalar Burgers or independent shear equation is supplied by analogy.

**CHEAPEST TEST.** Insert a plane-wave/shear packet including its induced
longitudinal flow and temperature perturbation. Retain the complete nonlinear
residual and initial derivative data. Test whether the proposed compressive
amplitude closes, is linearly degenerate, or feeds an uncontrolled coupled mode.
Equation (10) of the result already falsifies the pure transverse,
constant-temperature shortcut for generic time-dependent shear.

**FALSIFIER.** A violated conservation/derivative constraint, a missing mode
at the same order, a coefficient of the opposite sign, or an admissibility
exit before the claimed singularity. Linear high-frequency damping alone
proves neither shock formation nor nonlinear regularity.

**TRANSFER LIMITS.** The matched MIS and BDNK shear spectra agree only at the
linearized level. A nonlinear model-separation result needs the actual MIS
stress evolution. A kinetic comparison needs a positive distribution realizing
the relevant moments, a specified collision operator and a controlled closure
error. Collisionless Vlasov--Maxwell is not automatically the kinetic parent
of this neutral conformal viscous fluid. The Galilean limit also needs an
appropriate massive equation of state, not just substitution c -> infinity.

**STOP/PIVOT.** If the full amplitude equation does not close, retain the first
failed coupling and change the compression mechanism or model with a named
new premise. Do not infer global healing from the excluded similarity class.
No compute campaign, new solver architecture or parallel lane is authorized
by this handoff.
