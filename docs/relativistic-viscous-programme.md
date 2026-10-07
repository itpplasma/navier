# Relativistic viscous breakdown programme

Updated 2026-10-07. This is a companion research contract. It does not alter the original unforced whole-space incompressible Navier--Stokes target in `PLAN.md`.

## Scientific question

Classical Navier--Stokes now has a released **smooth-forcing** finite-time
breakdown construction; the corresponding **unforced** classical problem is
still unresolved. No forced BDNK finite-time singularity theorem is currently
established here, and the unforced BDNK singularity problem is also open.
Relativistic Vlasov--Maxwell has a released claim of the opposite kind:
arbitrary admissible collisionless data remain globally classical, with the
proof organized around a causal signed-impulse estimate.

The exact comparison is therefore two-dimensional: forcing status and model.
The immediate apples-to-apples question is “does the released forced
Navier--Stokes singularity mechanism survive a causal relativistic viscous
completion?” The broader question is:

> For a specified causal relativistic viscous closure, does a genuine finite-time breakdown mechanism survive? If it does not, which exact relativistic identity excludes it? Is that obstruction model-independent, or does changing the closure change the answer?

The first model is **BDNK** (Bemfica--Disconzi--Noronha--Kovtun), because it is a first-order relativistic viscous theory with causal/strongly-hyperbolic formulations and a controlled nonrelativistic relation to Navier--Stokes. Israel--Stewart/DNMR and newer extended causal closures are comparison models. There is no unique equation called “relativistic Navier--Stokes”.

## Three meanings of “healed”

Do not conflate:

1. **PDE healing:** the relativistic closure itself has a global smooth solution.
2. **Hydrodynamic healing:** the solution stays smooth *and* inside the closure's regime of validity (for example small Knudsen/inverse-Reynolds corrections where required).
3. **Microscopic healing:** a fluid closure loses regularity or validity, but an underlying kinetic theory remains regular and simply leaves the hydrodynamic manifold.

A fluid gradient blow-up outside its controlled constitutive regime may be a mathematically real PDE singularity but evidence of closure failure rather than a microscopic plasma singularity.

## Present source-level status

The primary-source ledger is `literature/relativistic-viscous-status-2026-10-07.md`. Its current implications are:

- BDNK supplies local causal well-posedness and small-perturbation global decay in established parameter regimes.
- Numerical BDNK work reports smooth-data evolution toward extremely steep gradients/apparent singular behavior in some configurations. This is not a theorem.
- Other BDNK computations show viscous regularization of Euler shocks for selected data in a frame-robust hydrodynamic regime. This does not imply arbitrary-data regularity.
- Müller--Israel--Stewart/DNMR-type systems already have rigorous finite-time breakdown results for classes of smooth data, and 1+1-dimensional pure bulk/shear/diffusion regimes have rigorous gradient blow-up/shock formation.
- No source in the current screen settles arbitrary smooth large (3+1)-dimensional BDNK data in either direction.

Thus “relativity + viscosity always heals blow-up” is already untenable as a model-independent thesis. The open issue is which mechanisms survive in which closures and whether a more microscopic theory removes the singularity.

## Input from the two OpenAI PDE results

### Forced Navier--Stokes: construction side and the first relativistic failure

The released Navier--Stokes result provides a concrete shrinking/spiralling
vortex architecture whose residual is supplied by smooth forcing. In this
repository that theorem remains a **forced** control; it does not settle
`NS-R3`, whose unforced status remains open.

The first BDNK transfer has now been executed. Two independent pieces of the
classical construction fail to transport unchanged:

1. **Nonlinear energy-balance failure.** For a normalized proper-velocity lift
   with `gamma,w ~ tau^(-a)`, spatial scales `tau^beta_i` with
   `0<beta_i<1`, and temperature `Theta ~ tau^(-b)`, the full BDNK
   time-derivative constitutive stress dominates the spatial transport in the
   tested regime. Energy conservation forces a dilation equation whose only
   bounded nonnegative profile is trivial whenever
   `b > -a/kappa` (frame A: `kappa=25/12`). In particular a constant-scale
   or heating thermal completion cannot support the direct lifted vortex.
   A bounded smooth source is lower order and cannot repair this leading
   mismatch; maintaining the same profile would require leaving the hypotheses
   (for example sufficiently strong cooling/finer scales) or a source singular
   at the target scale.
2. **Parabolic pulse-damping failure.** The classical pulse design raises
   wavenumber until viscous `k^2` damping overtakes amplification. Linearized
   causal BDNK shear satisfies a telegraph equation
   `lambda v_tt+h0 v_t-eta v_xx=0`; above its crossover wavenumber the decay
   rate has constant real part `-h0/(2 lambda)`, not `-D k^2`. Therefore
   the high-frequency heat-semigroup bookkeeping used by the classical
   construction is unavailable.

These facts justify calling the released forcing **finely tuned to the
classical parabolic Navier--Stokes dynamics**. “Artificial” is a reasonable
informal description of this lack of robustness, but the mathematical claim is
the scoped one above: the direct forcing/profile architecture is not invariant
under this causal relativistic completion. They do **not** prove that every
smooth relativistic forcing fails or that BDNK is globally regular.

The next forced task is therefore constructive: redesign the relativistic
profile/source around the full causal stress rather than transplant the
classical pulse machinery. See
[`openai-forcing-relativistic-failure.md`](openai-forcing-relativistic-failure.md).

### Relativistic Vlasov--Maxwell: obstruction side

The `itpplasma/vlasov-maxwell` source audit records the opposite proof shape. There an absolute-force estimate loses a factor `sqrt(w)`; the argument keeps vector signs, derives an exact retarded cancellation, and produces a `w^(-1/2)` coefficient exactly where selection forces the expensive geometry to be used. The conditional suffix is then closed separately.

The transferable lesson is not the Vlasov formula itself. For a causal relativistic fluid:

- identify the precise continuation/breakdown quantity;
- locate the exact scale or characteristic family where absolute energy estimates fail;
- keep the stress-energy flux signed/coupled long enough to search for a causal-cone or entropy-flux cancellation;
- demand that any new structure pay the named deficit quantitatively;
- close the bootstrap/rigidity separately.

If no such cancellation exists and a collapse construction survives, that is equally valuable information.

## Model hierarchy and falsifiable targets

### RNS-BDNK-F — forced transfer screen

**Question:** Can the released forced NS collapse be embedded, after relativistic rescaling, in a specified (3+1) BDNK model with smooth covariant source?

This is the cheapest mechanism test, not the main physical theorem. A negative result must identify the first unavoidable relativistic term/sign/causality condition that kills the scaling.

### RNS-BDNK-U — closed large-data BDNK

**Main fluid target:** for a fixed physically admissible (3+1) BDNK constitutive law, prove either

- one smooth admissible unforced/closed initial state develops a finite-time singularity; or
- every smooth admissible datum in a precisely stated large-data class continues globally.

A conditional criterion is a consumer until its arbitrary-data producer is proved.

### RNS-IS — robustness across relaxation theories

Extend or sharpen known Israel--Stewart/DNMR breakdown beyond reduced one-dimensional/pure-channel regimes. Determine whether the same geometric mechanism can be realized in full coupled (3+1) dynamics.

### MODEL-SEPARATION — does the answer depend on the closure?

Use a common thermodynamic state and matched low-gradient transport data across BDNK, Israel--Stewart, and an extended causal large-gradient closure. Seek a theorem where the models provably diverge in continuation/breakdown behavior. This would show that “relativistic viscosity” is not one mathematical prediction.

### KINETIC-ESCAPE — closure singularity versus physical singularity

Couple the programme to `itpplasma/vlasov-maxwell` and its proposed relativistic Maxwell--Landau extension. A high-value theorem would show that a fluid gradient singularity corresponds to loss of hydrodynamic validity while the underlying kinetic solution remains regular over the same interval.

### CLASSICAL-BACKTRANSFER — better physics that survives (c\to\infty)

If a relativistic/kinetic correction prevents collapse, test whether it has a nontrivial classical limit producing a better continuum model. If the correction vanishes exactly to ordinary Navier--Stokes, any uniform regularity estimate must degenerate in that limit if the forced NS breakdown theorem applies. Treat that degeneration as a required quantitative check, not a philosophical objection.

## First research contract

Start with `research/relativistic-breakdown-contract.md`. Do not launch all targets. The first calculation is the BDNK scaling adapter: determine what the classical shrinking-vortex balance becomes when velocity is timelike, Lorentz factors are retained, and the full first-order stress tensor is differentiated.

A win is not “BDNK looks safer”. It is one of:

- an exact admissible relativistic singular construction;
- an unconditional exclusion of a nonempty collapse-profile class;
- a model-separation theorem;
- a precise source-derived continuation estimate that genuinely removes a surviving breakdown class;
- or a decisive falsifier of the proposed transfer.

