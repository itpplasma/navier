# Navier--Stokes terminal frontier: physical prehistory or full adjoint

This is the sole live task/status record. `NS-R3` remains **NOT PROVED** and no
unforced counterexample has been constructed. This PLAN supersedes the
2026-09-09 viscous-Fredholm live plan, preserved verbatim at
`research/history/PLAN-before-frontier-integration-2026-09-11.md`.
Historical plans are evidence/history only, not parallel task queues.

```yaml
terminal_claim: NS-R3
terminal_status: not-proved
unforced_counterexample: not-constructed
complete_terminal_route: none-established
checkpoint: CP1
phase: source-specific-physical-prehistory-or-full-adjoint-2026-09-11
active_task: UE1-source-prehistory-matching-or-complete-physical-adjoint
primary_direction: full-PDE-exactification-with-positive-route-fallback
dominant_research_nut: one-Schwartz-trace-supplying-all-required-source-entry-traces-through-the-full-viscous-history
raman_route: retired-after-two-distinct-leading-time-order-cancellations
positive_RFq_consumer: reviewed-and-closed-conditional-on-input-only-producer
arbitrary_data_RFq_producer: not-produced
weighted_moment_angular_resonance_budget: proved-author-2026-09-11
comparable_heat_normal_form: blocked-by-large-amplitude-coercivity-wall
finite_viscous_mixed_trace_inverse: proved-author-audit-pending
all_penalty_normal_selector: proved-author-audit-pending
operator_lipschitz_horizon_selector: proved-author-audit-pending
source_primary_local_entry_seed: exponentially-cheap-author-proof
source_primary_covariance_repair: exponentially-small-retuning-author-proof
source_zero_extension_gluing: refuted-by-solenoidal-time-impulse
source_localized_adjoint_shortcut: refuted-by-exact-half-unit-defect
angular_trapped_homogeneous_preparation: superalgebraically-damped-author-proof
angular_preparation_alternative: radial-exterior-occupation-or-large-nonlinear-supply
common_physical_initial_trace: not-produced
full_physical_adjoint: not-computed
nonlinear_deforcing_contraction: not-produced
source_singularity_preservation_under_correction: not-proved
regenerative_turnovers_certified: 0
formal_status: unchanged-see-navier-formal-and-archived-plan
new_results_audit: author-proofs-independent-mathematical-audit-pending
public_release: true
```

## 1. Rigid target and terminal consumers

For fixed `nu>0`, the target is original unforced incompressible Navier--Stokes
on `R^3`

    u_t - nu Delta u + P div(u tensor u) = 0,
    div u = 0,
    u(0)=d in S_sigma(R3;R3).

A positive solution must cover **every** such datum. A negative solution needs
**one** Schwartz finite-energy datum whose classical branch has a genuine finite
endpoint. Forced, periodic, averaged, inviscid or modified-dissipation systems
do not settle this target.

The reviewed positive consumer remains, for one fixed finite `q>3`,

    integral_0^t Pi_q,M
      <= nu integral_0^t D_q,M + C(d,nu,H,N0,q)
      uniformly for t<=H and M
    -> RF-q -> RF-LQ-SYNTHESIS -> finite L^{3,q}
    -> RF-LOCAL-ID / Lorentz Fatou -> RF-LQ-CONTINUATION
    -> LOCAL / ENERGY / canonical pressure -> NS-R3.

No arbitrary-data input-only producer for the displayed estimate is known.

The negative/full-PDE consumer is

    prescribed forced singular history U,F
      -> solve L_U w + P div(w tensor w) = -P F
      -> ONE Schwartz initial trace for U+w
      -> preserve a singular observation
      -> identify U+w with its classical unforced branch.

Finite-interval inversion alone is not this consumer.

## 2. Retired Raman purifier architecture

The September 11 Raman programme generated several exact scoped positive
Fourier-symbol theorems, but the physical time-evolution audit found a missing
ordering term. The load-bearing negative controls are now:

1. a real field necessarily carries reflected modules, invalidating a one-sided
   pointed slow semigroup;
2. one common affine filter is incompatible with the reality-complete clutter
   by an exact Farkas certificate;
3. the reality-complete leading slow translation is conservative/skew rather
   than a one-way dissipative filter;
4. simultaneously preloaded near-opposite Raman parents have two ordered
   target-assisted paths whose leading coefficients cancel exactly;
5. heat-rate, phase/amplitude and leading-polarization tweaks cannot select one
   ordering; and
6. a genuinely different autonomous 2D3C parent-birth mechanism still has a
   complete cubic `O(N)` cancellation when all trees are retained.

The last item is frozen in
`research/evidence/2026-09-11-raman-parent-birth-wall.md`.
After two genuine mechanism changes returned to the same ordering obstruction,
Raman is **not an active route**. Do not resume parameter searches or use the
earlier one-ordered effective theorems as physical NS modules without first
supplying a genuinely new time-ordering mechanism and redoing the complete
Taylor/propagator calculation.

## 3. Positive route: one new trajectory budget, then an exact wall

The audited smooth-block sixth-power functional remains valid and removes the
old low-transport boundary loss. Its open term is signed comparable-frequency /
high-pair transfer at arbitrary critical amplitude. Absolute estimates return
to `A D` or `integral ||grad u||_2^4` and are not terminal producers.

A new whole-space estimate was proved on September 11: the first spatial moment
has an input-only finite-horizon bound, and the corresponding weighted
viscous dissipation controls Fourier angular derivatives. A one-dimensional
slab inequality then gives an input-only `O(eta)` spacetime budget for block
mass concentrated in a relative-width heat-resonance slab. This is genuine
trajectory information, not a criterion reformulation.

The first natural consumer is nevertheless blocked exactly. Away from the
resonance slab the heat mismatch is `Omega=-2 nu p.q`; one normal-form
integration produces a boundary primitive of natural size

    M^7/(nu eta)

against critical entropy `M^6`. Its ratio is `M/(nu eta)`, unbounded at
arbitrary amplitude. Shrinking the resonance width helps the slab term but
worsens this boundary term. The detailed obstruction is
`research/evidence/2026-09-11-comparable-normal-form-coercivity-wall.md`.

Therefore the active run must not iterate another perturbative heat normal form
or another absolute smooth-block estimate. A future positive attack must use a
genuinely nonlinear spacetime/trajectory mechanism that controls accumulated
comparable transfer without `sup a_k` or squared-enstrophy input.

## 4. Full-PDE inverse: what is already proved

For every prescribed smooth finite history the repository has a full viscous
mixed-trace inverse. The later positive-normal initialization removes the
exceptional-penalty issue. With

    C=(-Delta)^(-1/2) chi curl,
    H_T = integral_0^T T(0,s)E(s,0) ds,
    S_T = H_T C*,

one has, for every `lambda>=0`,

    eta(0)=-(I+lambda S_T S_T*)^(-1)b_T,
    a_T=-lambda S_T*(I+lambda S_T S_T*)^(-1)b_T,
    v(0)=C* a_T.

The selector is operator-Lipschitz in `S_T`. Hence convergence of the actual
history operators and data gives a precise sufficient common-trace criterion.
This does **not** by itself bound the source's concentrating propagator or
preserve the singular core.

More invariantly, required pulse observations define nested affine constraints
on the single initial control. If `a_N` is the minimum-norm control satisfying
the first `N` observations, a common finite-norm control exists iff

    sup_N ||a_N|| < infinity,

with the exact Pythagorean increment identity for nested constraints. Thus
"carry the correction globally" does not remove trace coherence; it is exactly
a bounded common-control problem.

## 5. Source-specific progress: local seeds are cheap, gluing is not

The source-pulse adjoint calculation is favorable locally. For the actual
principal primary pulse, whose envelope satisfies

    P(0)=exp(-gamma_- L),

its normalized peak adjoint has initial norm comparable to `1/P(0)`. Therefore
the minimum local entry seed producing the desired peak has norm comparable to
`P(0)`, exponentially small. Removing the startup cutoff and using this entry
seed preserves the local peak. The two leading covariance weights can also be
retuned by an exponentially small relative amount while keeping positivity.

Those are entry-face data, not one physical initial datum. Extending the uncut
pulse by zero produces the exact solenoidal time impulses

    J_a delta_(t=t_a) - J_b delta_(t=t_b),

which viscosity, convection and pressure cannot cancel. Cutting off the
backward adjoint to manufacture a zero initial trace is also invalid: the
adjoint defect has an exact order-one half-unit pairing and cancels the apparent
obstruction. These results are frozen in
`research/evidence/2026-09-10-source-pulse-adjoint.md`.

Therefore another local pulse inverse, another flatness argument, or another
artificially localized adjoint is not progress.

## 6. Whole-prehistory angular obstruction

The whole-space angular preparation theorem supplies the complementary global
constraint. For angular mode `n`, viscosity gives the exact vector estimate
with the essential `(abs(n)-1)^2/r^2` factor. If a high mode is prepared
homogeneously while retaining a fixed fraction of its energy inside the
shrinking core, its amplitude is superalgebraically damped over the logarithmic
preparation interval. Without a trapping assumption, a mode retaining the
required terminal size must instead spend asymptotically almost all logarithmic
preparation time in the radial exterior.

For the full original nonlinear solution, if it remains substantially trapped,
the missing alternative is a quantitatively large cumulative nonlinear supply
from the complete non-axisymmetric field. No finite harmonic closure is used.
See `research/evidence/2026-09-08-angular-preparation-obstruction.md`.

This result is not yet an absolute event cost: the nonlinear work is normalized
by the current mode energy. It therefore neither proves impossibility nor feeds
RF-q directly.

## 7. ONE active terminal nut

The next attack is source-specific **physical prehistory matching**. For the
actual forced singular history, determine whether one Schwartz initial
correction can supply all required nonzero pulse-entry traces through the full
viscous evolution, including mean, pressure, exterior, diffusion and nonlinear
transfer.

There are exactly two acceptable outcomes:

**Constructive closure.** Build a common initial control with bounded all-order
Schwartz costs, propagate it through the complete prehistory, cancel the entire
force by a convergent nonlinear correction, and prove the singular observation
survives.

**Quantitative exclusion of this profile/correction class.** Construct the
complete physical backward adjoint(s), not locally cut off substitutes, and
prove that the actual force/observation pairing violates the exact nonlinear
de-forcing budget for the stated bounded correction class. Such an exclusion
would retire this forced-profile exactification route; it would NOT prove global
regularity of arbitrary unforced NS.

The first discriminating subproblem is to combine the actual local entry-seed
sizes with the full physical prehistory transfer. The angular theorem says that
a homogeneous high-angular seed cannot simply stay in the shrinking core: the
proof must quantify radial exterior transport or nonlinear generation. Test the
minimum-norm prefix controls / complete adjoint against those two alternatives.

After two serious returns to an uncontrolled future critical quantity or to the
same trace/prehistory obstruction, change mechanism again. Do not replace this
source-specific calculation by another generic Fredholm inverse.

## 8. UE2--UE4 after UE1

Only after one common trace / prehistory is controlled:

- **UE2:** solve the full nonlinear correction with every cross-product,
  pressure term, exterior tail and ordinary diffusion retained;
- **UE3:** obtain one nonzero Schwartz datum on all of `R^3`, canonical
  pressure, finite energy and pre-endpoint smoothness;
- **UE4:** identify the exact field with that datum's classical branch and
  prove a finite endpoint via a preserved singular lower bound.

No numerical orbit is a certificate for these steps.

## 9. Verification, provenance, formal work

The route-invariant formal programme is unchanged. Current Lean status remains
owned by `itpplasma/navier-formal` and `navier-formal/docs/verification-status.md`;
no new formal coverage is claimed by this PLAN update. The complete prior formal
status text and earlier viscous history are preserved in the archived PLAN.

All September 11 theorem/obstruction packets are author proofs unless their own
files state otherwise; independent mathematical audit and novelty remain
pending. The accepted forced-source and Euler-source scopes remain unchanged.

A full checkout is required for `python3 research/game/run.py fast`,
`python3 research/verify.py --research-only`, paper checks and `git diff --check`.
When only the connected GitHub interface is available, verify authoritative blob
hashes and baseline controls there and state explicitly that this is not a local
repository-wide verifier run.
