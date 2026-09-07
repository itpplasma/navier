# RF frontier packet: compatible refinement, slow manifolds and causal memory

Date: 2026-09-07. Frozen starting main: f0add720620a4e381c98bb6ed762bc2906f77e11.
Status: research specification, not an NS proof or a theorem from the literature.
Workflow: krystophny/prompts at 2929639d8ed611917bd1086df002296a611a475b,
skills/math-frontier/SKILL.md. PLAN alone is the live allocation.

## 1. Compact frontier packet

TERMINAL CLAIM: NS-R3, original unforced R3, every solenoidal Schwartz datum,
every nu>0, smooth velocity AND pressure for all nonnegative times, initial
trace and energy bounded by its initial value.

ESTABLISHED: the repository's LOCAL/ENERGY/CONTINUATION conditional suffix;
exact energy cancellation for correctly projected/conforming approximations;
the elementary inverse scaling ||v_h||3 <= C h^(-1/2)||v_h||2 when the
reconstruction spaces meet a uniform inverse-estimate hypothesis; existing
scoped no-go and singularity consumers, none a general producer.

FIRST GAP: build a reduction that retains resonant dynamics, and bound TOTAL
changes between refinements in a critical topology without future smoothness,
unknown strain or a cutoff-dependent normal-stability constant.

FALSIFIER: an exact allowed NS interaction at a zero homological denominator;
a normal mode with uncontrolled feedback; or a correctly normalized family
whose proposed uniform estimate fails. A frozen linear, forced, periodic or
finite-dimensional counterexample defeats only an assertion covering that
class. A numerical example is not proof until its sign/limit is certified.

FORBIDDEN INFERENCES: fixed-mesh global existence -> uniform regularity;
energy conservation -> critical compactness; AP -> spatial-limit regularity;
normal attraction -> tangential boundedness; finite algebraic rank -> bounded
inverse; asymptotic series to each order -> convergence; graph-lift obstruction
-> impossibility of all geometric reductions; torus -> R3 without an adapter.

CHECK: exact projected NS interaction and invariance equation; then a causal
reconstruction with rigorous remainder. Keep only one main mathematical
mechanism under the original allocation; the owner's current parallel-run
override and allocation are in PLAN. The final proposed consumer is Section 2, not a new criterion
advertised as the desired producer.

## 2. Explicit sufficient terminal interface (conditional)

Fix u0,nu and H. Let h_j=2^(-j)h0 and u_j be conforming whole-space numerical
reconstructions or reconstructions on expanding domains with a separately
proved R3 adapter. They must come from one coherent sequence, preserve the
specified datum in the limit, and have uniform energy/trace control.

Require for e_j=u_(j+1)-u_j a common-space inverse bound

    ||e_j(t)||3 <= C_inv h_j^(-1/2)||e_j(t)||2,

with C_inv independent of j and of the box limit. Nested conforming spaces,
uniform shape assumptions and correct reconstruction may supply this; do not
apply it to an arbitrary difference of unrelated meshes. Require a bounded
coarse L-infinity L3 term and the input-only estimate

    sum_j h_j^(-1/2)||e_j||_(L-infinity(0,H;L2)) <= C(u0,nu,H). (S)

Then telescoping makes u_j Cauchy in L-infinity(0,H;L3), with an input-only
bound. It is enough to use essential suprema; smoothness of the later
identified classical branch fixes pointwise interpretations. Consistency
must include the nonlinear term, pressure/solenoidal testing, derivative
residuals, datum and energy inequality. Strong local L3 convergence handles
the local quadratic flux; energy and discrete-derivative bounds still need
their own passages. The limit is a legitimate unforced R3 weak solution.
Weak--strong uniqueness identifies it below Tstar; the established endpoint
continuation excludes Tstar<H. Since H is arbitrary, NS-R3 follows.

(S) is stronger than necessary and is not asserted equivalent to NS-R3.
It need hold for only one faithfully constructed family. A direct uniformly
resolved momentum certificate or another precisely consumed critical norm
may replace it. No existence, consistency or tail hypothesis is supplied
merely by writing (S).

## 2a. Reviewed direct whole-space alternative

The original sufficient interface (S) remains valid in its stated scope.
For the selected exact Fourier-ball family on R3, the 2026-09-07 wave
constructs every projected flow and replaces (S) by the weaker conditional
RF-CUBE output: sup_t sum_j [N_j^(1/2)||u_(j+1)-u_j||2]^3 is finite on
every finite horizon, with constants depending on full datum and nu.
The [complete reviewed proof](evidence/2026-09-07-whole-space-cubic-refinement.md)
supplies overlapping-increment synthesis and direct compact-classical L2
identification. This selected consumer uses the canonical branch's pressure,
trace and energy, so it needs no approximate-pressure limit or new
weak--strong uniqueness interface. A separately claimed global weak-limit
construction retains all its own pressure/tail/energy obligations.

The later [finite-Lorentz synthesis](evidence/2026-09-07-lorentz-synthesis.md)
and [continuation adapter](evidence/2026-09-07-lorentz-continuation.md) allow
one fixed finite q>3 in place of the cubic exponent. Their full conditional
composition has passed independent review. The required RF-q producer and
RF-CUBE remain unproved; weak q=infinity is not an accepted endpoint. The construction
is on an infinite-dimensional bandlimited Hilbert space, not a finite-mode
whole-space discretization. Causal/slaving representations are optional
methods for RF3, not prerequisites of this selected family. Audit scopes
and the repaired generic time-measurability assumption are recorded with
the evidence. PLAN allocates further weakening and producer experiments.

## 3. Exact slow-manifold bookkeeping

For dot x=f(x,y), dot y=g(x,y), let y=Phi(x) be a proposed closure. Its
invariance defect is R_Phi=g(x,Phi)-D Phi f(x,Phi), NOT just g(x,Phi).
For z=y-Phi(x), the exact normal equation is

    dot z=A_Phi(x,z)z+R_Phi(x),
    A_Phi(x,z)=integral_0^1 [D_y g(x,Phi+theta z)
                             -D Phi D_y f(x,Phi+theta z)] dtheta.

An actually proved bound <z,A_Phi z><=-gamma||z||^2 gives

    ||z(t)|| <= exp(-gamma t)||z(0)||
                 + integral_0^t exp[-gamma(t-s)]||R_Phi(x(s))|| ds.

This estimate is conditional on the trajectory staying in the checked
neighborhood; a trapping/bootstrap proof is required. For moving metrics
include the metric time derivative. Negative frozen eigenvalues do not
bound an arbitrary nonautonomous propagator. The quantities Phi(x), x(t),
z(t), and changes of Phi across meshes are separate obligations.

A genuine small parameter must be named. In a kinetic fluid scaling the
transport-to-collision ratio at spatial frequency k is epsilon |k|. For
fluid modes, nonlinear coupling a|k| versus diffusion nu|k|^2 has ratio
a/(nu|k|). Critical concentration can keep this ratio order one. h->0 is
numerical resolution, not an automatic dynamical perturbation parameter.

## 4. Resonance test and admissible repairs

For heat eigenvalues nu|p|^2, the quadratic slaving equation has denominator

    Delta = nu(|p|^2+|q|^2-|p+q|^2) = -2nu p.q.

Orthogonal parents can have a nonzero ORIGINAL Leray-projected interaction;
see the repository's single-channel test. The actual interaction coefficient
must be computed, not inferred from the wavevector condition alone.

Before assuming a C2 static graph over a spectral cutoff, inspect the
homological equation on every retained resonant pair. If it fails, the
narrow graph assertion is retired; retain the resonant variable, allow an
appropriately justified nonsmooth graph, or use a history-dependent map.
An exact causal kernel has no small-denominator singularity:

    integral_0^t exp[-gamma(t-s)] exp[-(alpha+beta)s] ds
      = exp(-gamma t)(1-exp[-Delta t])/Delta,
    Delta=alpha+beta-gamma,

and equals t exp(-gamma t) when Delta=0. This is only a scalar kernel
calibration until nonlinear feedback and operator costs have been controlled.

For dot y+(D+K)y=F, D=D*>=0 and K*=-K, initial y=0 gives

    integral <F,y> = ||y(H)||^2/2 + integral <Dy,y> >=0.

The matching negative feedback in the resolved ENERGY equation therefore
has a cumulative sign. At a critical weighted level the pairing may no
longer match. Prove the required weighted/corrected estimate rather than
asserting it from positivity of D.

## 5. Exact full-fluid error: the term a model must not discard

On a common spectral fine space, let v solve the coarse projected NS and U
solve the fine projected NS. Embed v without changing its coefficients and
put w=U-v, A=-Delta, B(a,b)=P_f P_Leray[(a.grad)b]. With nested commuting
spectral projections, the EXACT error equation is

    dot w+nu A w+B(v,w)+B(w,v)+B(w,w)=F,
    F=-(I-P_c)B(v,v).

Here w generally has resolved as well as unresolved components. It is not
silently replaced by Q_c U. The energy identity is

    (1/2) d||w||2^2/dt+nu||grad w||2^2
       = <F,w> - integral (w.grad)v . w.

The second term is not skew. Absolute values return ||grad v||infinity,
which is finite at one mesh but not known uniformly at the terminal limit.
A FEEC transfer has additional projection/commutation/reconstruction terms
unless their cancellation is actually proved. Keeping the full pressure
projection here does not authorize ignoring pressure consistency on R3.

RF3 must control this signed interaction and the associated retained dynamics
across scales. The matched passive-memory identity alone does not do so.
An invariant shear/passive-scalar sector is a useful EXACT test, but lacks
this feedback and cannot be advertised as arbitrary-data progress.

## 6. Parameter and structural contracts

Keep distinct: viscosity nu (fixed); horizon H (arbitrary finite); spatial
mesh h_j; time step dt; kinetic epsilon; velocity cutoff R_v and Hermite/order
index M_v; box size L_box; reduction order m; spectral separation threshold;
normal propagator and reconstruction constants. State permitted dependence
before each estimate. A justified diagonal is allowed, not an interchange of
limits with no uniform estimates.

Start spatially semidiscrete. Positive mass matrices and skew projected
convection give global finite-ODE solutions through an energy identity, not
an inverse norm uniform in dimension. Use no pseudospectral aliasing in the
algebraic test. FEEC/mimetic support requires exact complexes and adjoints
plus uniform analytic inequalities, not just incidence matrices. A discrete
Poisson Jacobi identity, an energy identity and thermodynamic entropy are
separate claims. Landau versus hard-sphere Boltzmann is a model change.

The whole-space adapter must not use a fixed-box Poincare gap as though it
survived L_box->infinity. Retain global/tail control, pressure normalization,
initial solenoidal preparation and the energy inequality. Keep MIC-R3's
particle and large-volume obligations separate from these fluid limits.

## 7. Source ledger for this research specification

Only the first three sources' indicated primary text portions were inspected
for this wave; the last two are leads with explicitly limited review. No
source is claimed to provide RF3 or arbitrary-data regularity.

[S1] Burby--Klotz, Slow manifold reduction for plasma science,
https://arxiv.org/html/2006.06636v1
Sections VI.1 (normal deviations and the moving-graph derivative), VI.2--3
(normal stability distinctions), VIII (inheritance of Hamiltonian structure).
Scope: geometric reduction and conditional stability; not uniform NS closure.

[S2] Foias--Hoang--Saut, Navier and Stokes meet Poincare and Dulac,
https://arxiv.org/html/1711.07184
Introduction and normal-form/resonance discussion. Prior art for NS normal
forms and long-time asymptotics, not a proof of the present terminal bound.

[S3] Carlier--Campos Pinto--Fambri, Mass, momentum and energy preserving FEEC
and broken-FEEC schemes for the incompressible Navier-Stokes equations,
https://arxiv.org/html/2306.13778
Section 3 commuting sequence, adjoint operators, skew discretization and
conservation statements. Requires its specified spaces/boundaries. Its
existence does not prove a universal three-dimensional approximation theorem.

[S4] Engel--Hummel--Kuehn, Connecting a direct and a Galerkin approach to slow
manifolds in infinite dimensions, https://arxiv.org/abs/2102.13533
Abstract inspected this wave; the previously discussed theorem is NOT used
without rechecking its spectral/semigroup/smallness and cutoff hypotheses.

[S5] Possanner, Gyrokinetics from variational averaging: existence and error
bounds, https://arxiv.org/abs/1711.09620
Prior-conversation methodological lead only in this wave. No gyrokinetic
stability or all-orders convergence theorem is imported into NS.

The original frontier-method file was read through the connected GitHub
repository, not reconstructed from memory. Use the matching proof-audit
workflow for a genuinely independent review when such a reviewer is actually
available. Author rechecking and symbolic tests are not independent review.
