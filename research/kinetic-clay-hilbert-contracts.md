# Contracts for kinetic Clay regularity and a scoped Newtonian fluid limit

Specification date: 2026-09-06. Base: `3291278efce2510fbc43ba8ad66c571dc5359c2d`.
Status: unproved research contracts, not a new theorem or independent audit.
PLAN.md alone assigns work. KPC means the preserved evidence file
`research/evidence/2026-09-06-kinetic-plan-contracts.md`. Sources H1--H6 are
recorded in `literature/kinetic-hilbert-scope.md`.

## 1. The three endpoints are different

### NS-R3 (unchanged Clay alternative A)

For each real nu>0 and real solenoidal u0 in Schwartz(R3), construct smooth
u,p on R3 x [0,infinity), satisfying the original unforced incompressible NS
system and initial datum u0, with ||u(t)||_2^2<=||u0||_2^2 for every t>=0.
Use the existing local-classical branch, uniqueness class and pressure
normalization. No force, stochastic forcing, altered viscosity, moment
closure or regularization is part of the terminal equation. Source H1.

### KIN-R3 (a kinetic realization of that theorem)

For each same (u0,nu), select a positive, input-prepared family of solutions
of the correctly scaled hard-sphere Boltzmann initial-value problem whose
projected macroscopic momentum converges, on each finite horizon, to a
velocity satisfying NS-R3. The admissible kinetic class may be renormalized;
its regularity and moment observables must be specified. One such family
suffices. Claiming that ALL kinetic families converge in a strong topology
would be an additional theorem, not part of this minimum target.

KPC supplies a less demanding resolved-momentum sufficient certificate K_res.
Its proof-to-NS interface is conditional until the endpoint producer and
application audit are complete. KIN-R3 is not a physically restricted datum
class: arbitrary solenoidal Schwartz u0 has the proposed Maxwellian preparation.

### MIC-R3 (stronger scoped Hilbert-VI/gas-dynamics endpoint)

For each same (u0,nu), specify elastic Newtonian hard-sphere initial probability
laws and microscopic/hydrodynamic/domain parameters, independent of an unknown
future fluid solution. Prove that their normalized momentum observables converge
on every finite macroscopic interval to the same global smooth NS velocity.
Start with convergence of ensemble observables in spacetime distributions;
state a stronger topology only when proved. Spell out the law, dynamics,
normalization, admissible sequence and limiting equation.

This is a dilute-gas Newtonian-to-fluid theorem, not all of Hilbert VI and
not a theorem about dense liquids. A kinetic-only result does not prove it.
Neither NS-R3 nor a regular velocity moment automatically makes a finite-
epsilon Boltzmann solution regular enough for an existing particle theorem.

## 2. Least-demanding analytic route retained from KPC

Set M(v)=(2pi)^(-3/2) exp(-|v|^2/2). Use Q_nu=c_nu Q_HS with a fixed positive
constant c_nu calibrated to the prescribed viscosity. KPC records the inverse
linearized-collision scaling; audit the kernel convention, including any
angular factor, before composing with H3. Work with

    epsilon^2 partial_t F + epsilon v.grad_x F = Q_nu(F,F),
    F^in=M(v-epsilon u0(x)),
    epsilon^(-2)H(F^in|M)=||u0||_2^2/2.

For a density cutoff gamma fixed as in H2 and any additional justified
velocity cutoff, the observable is

    g_epsilon=(F_epsilon/M-1)/epsilon,
    m_tilde_epsilon=P integral v g_epsilon gamma(F_epsilon/M) M dv.

Do not take the raw moment's global L3 integrability from finite entropy.
H2's truncated construction and the removal of defects are part of the
application audit. No division by a possibly small local density is needed:
the incompressible limit uses rescaled momentum, not an assumed bounded
finite-epsilon fluid velocity m/rho.

Let delta=tau_loc(u0,nu)/2 and H>delta. For S_J defined in KPC, establish

    sup_J liminf_k ||S_J m_tilde_epsilon_k||_{L-infinity(delta,H;L3(R3))}
        <= C(u0,nu,H,delta),                              (C1)

on one sequence with a single Leray limit. At fixed J, choose a norm-liminf
subsequence; it still has the same distributional limit. Test against compact
phi and obtain |<S_J u,phi>|<=C||phi||_{L1 L^(3/2)}. Remove J by distributional
convergence and use L1(L^(3/2)) duality. This gives the global-in-space endpoint
norm, not just local bounds. The argument does not require exchanging limits.

H2's preparation must give a Leray solution with the right energy bound and
trace. On every compact classical interval, weak--strong uniqueness identifies
it with the existing branch. Identification uses only local smoothness; it
must not introduce an endpoint strain bound. LOCAL covers [0,delta]. Taking
H beyond a hypothetical finite Tstar and applying CONTINUATION gives a
contradiction. ENERGY completes the energy clause. Different H may use
different kinetic subsequences; uniqueness identifies their velocities on
the classical lifespan, and the resulting global branch is consistent.

A direct dual bound with the same test norm can replace (C1), without uniform
norm control on all finite-epsilon outputs. An input-only L5 spacetime bound
can instead use the existing SERRIN node, with lower semicontinuity and the
same identification. Neither alternative is a new proved producer.

Full-phase-space Sobolev control, uniform bounds at t=0, a quantitative rate,
all finite-epsilon solutions being classical, and a uniform-in-H constant are
NOT requirements for this route. Adding them without a consuming theorem
makes the research harder without bringing the terminal edge closer.

## 3. Noncircular microscopic completion after regularity

The primary microscopic completion strategy is deliberately downstream:

    K-CRIT + K-ENTRY -> NS-R3/KIN-R3
    NS-R3 + a matched strong hydrodynamic theorem -> regular kinetic families
    regular families + a matched particle theorem + domain adapter -> MIC-R3.

Once NS regularity has been proved independently, invoking a theorem that
assumes smooth NS is legitimate. Before that point, it is circular as a
regularity argument. H4 offers lifespan-dependent strong kinetic results;
H3's Theorem 2 assumes a smooth NSF target on T^d. Both still require exact
hypothesis checks. They are not automatic full-space particle adapters.

Alternative: prove a particle-to-kinetic convergence theorem for the actual
renormalized family used in C1. This could bypass regular kinetic reconstruction,
but is an additional research problem, not a free use of H3. Choose one
completion strategy explicitly; do not switch weak and strong kinetic classes
inside an implication without a uniqueness/stability theorem.

For each finite H it may suffice to construct regular kinetic solutions for
0<epsilon<epsilon_0(u0,nu,H). The same fixed epsilon need not work for every
H, and no general arbitrary-data global classical Boltzmann theorem is a
mandatory dependency. A regular fluid momentum does not control all other
kinetic modes without such reconstruction or a new estimate.

## 4. Particle/domain specification and the parameter ledger

Use distinct names throughout:

| Symbol | Meaning | Required control |
| --- | --- | --- |
| epsilon | hydro Knudsen/Mach parameter | tends to zero with nu fixed |
| a_part | hard-sphere diameter | Boltzmann--Grad scale, distinct from epsilon |
| N or E N | deterministic/expected particle number | match the chosen ensemble |
| alpha | collision-rate parameter | convert exactly to c_nu/epsilon |
| L_box | side length of periodic box | infinity if used to reach R3 |
| H and s_fin | macro and transport-time horizons | state conversion |
| J | macro spatial observation resolution | remove only in proved order |
| R_v and cutoffs | velocity/density observation truncations | moment tails controlled |
| K_Hermite | optional computational/analytic truncation | no fixed-tail assumption |

For example, with space unrescaled, n(s,x,v)=F(epsilon s,x,v) satisfies

    partial_s n+v.grad_x n=(c_nu/epsilon)Q_HS(n,n),
    0<=s<=H/epsilon.

This fixes ONE time convention. H2 also uses a different simultaneous x,t
rescaling; provide an explicit dictionary rather than mix the two.
On a unit torus H3 uses E N * a_part^2 approximately alpha in dimension 3.
With number density normalized per volume, the corresponding large-box
quantity is (E N/L_box^3)*a_part^2; rederive all constants under the chosen
normalization. Vanishing volume fraction requires the associated
alpha*a_part -> 0 condition. No change in nu is hidden in these limits.

H3's microscopic theorem includes restrictions involving collision rate,
weighted kinetic norms and observation time. At fixed epsilon and H these
can potentially be met by taking a_part sufficiently small if those norms
are already finite. A joint explicit rate requires tracking their dependence;
qualitative iterated convergence does not require a universal joint rate.

Whole-space H2 has infinite background mass: M is uniform in x and only
relative entropy is finite. It is not an N-particle probability density in
R3. Supply either an infinite-volume equilibrium/perturbation theorem, or
finite-volume ensembles plus a proved exhaustion. In the latter case audit
solenoidal u0 preparation, pressure/flux boundaries, local compactness,
initial trace and the global energy inequality by controlled exhaustion.
Kinetic velocities are unbounded and pressure is nonlocal, so boxes cannot
be ignored by an unsupported finite-speed argument.

A periodic companion NS-T3/KIN-T3/MIC-T3 may be a useful separate result and
would meet Clay alternative B if arbitrary smooth periodic data are covered.
H3 handles zero-mean data; a Galilean reduction and every rescaling must be
written. Such a theorem neither changes nor automatically proves NS-R3.

## 5. Observables, error budgets and legitimate diagonals

Let mu_N be a normalized empirical phase-space measure (normalization chosen
consistently with number intensity), and let f_N^(1) denote its expected
one-particle observable density when it exists. For smooth compact spacetime
phi and a velocity cutoff chi_R, a basic momentum test has integrand
chi_R(v) v.phi(t,x)/epsilon, with the equilibrium mean subtracted as needed.
Empirical delta masses do not have an L3 norm. A coarse-grained norm requires
a specified mollifier and resolution; particle fluctuation estimates cannot
be silently inherited from smooth marginal estimates.

Write, in the actual chosen topology and normalization,

    error_total <= error_particle-to-kinetic
                   + error_kinetic-to-fluid
                   + error_domain + error_observable-cutoffs.       (E)

For a first-moment test the underlying distribution error must be o(epsilon),
not merely o(1), unless the iterated order first removes it at fixed epsilon.
Convergence in probability additionally needs covariance/two-particle control:
a fluctuation variance before division by epsilon must be o(epsilon^2).
The same issue occurs when the spatial resolution is refined. H3's treatment
of empirical observables explicitly uses one- and two-particle information;
do not replace it with mean convergence alone.

First prove each arrow at fixed outer parameters. Then enumerate compact
test functions, H=1,2,..., increasing spatial/velocity compact sets and any
needed resolutions. For the first n tests at horizon n, choose parameters
making every term in (E) <1/n, preserving the earlier admissibility constraints.
Pass to a single diagonal using a separating countable test class and the
uniform bounds needed to extend to all tests. Such selection is a proof
obligation, not a license to commute all limits. A single choice of preparations
across horizons is needed for a single global microscopic sequence; a separate
family per finite horizon is a weaker statement and must be labeled as such.

Rates, typical-trajectory convergence, propagation of chaos of every order,
and a uniform approximation for all t>=0 are optional stronger endpoints.
State exactly which qualitative endpoint is proved before claiming MIC-R3.

## 6. Acceptance records for each research result

Each candidate record must contain: its exact quantified statement and
solution class; all inputs and their constant dependence; the first genuinely
new estimate; a complete consumer chain to C1 or a specified alternative;
all limits and discarded errors; attempted falsifiers; and a proof/audit
status. No candidate is promoted by this file or the programme map.

Before claiming the joint endpoint, independently audit four noncircular
chains: kinetic source applicability; critical regularity/continuation;
regular or weak particle-class matching; and domain/scaling/observable
composition. The particle chain must derive the original equation, not an
averaged, forced, finite-moment or momentum-damped model. Distinguish mathematical
completion from publication, priority, journal review and Lean coverage.
