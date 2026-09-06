# Kinetic / Hilbert-VI source and applicability ledger

Checked on 2026-09-06 for the programme update at base
`3291278efce2510fbc43ba8ad66c571dc5359c2d`. These are scoped source records,
not newly imported canonical proof nodes. Original notes only; no third-party
PDFs are stored. Source statement inspection is not an independent proof audit.
Earlier geometric/hypocoercive references remain in KPC Section 5.

## H1 -- official Clay target

Charles L. Fefferman, *Existence and Smoothness of the Navier--Stokes Equation*.
https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf

Inspected official statement, including rendered PDF page 2. Alternative A
is the unforced R3 smooth rapidly decreasing-data problem; alternative B is
periodic. The repository's NS-R3 contract keeps A. A periodic result would be
a separate accepted alternative, not a proved whole-space transfer. Check
smooth velocity AND pressure, the initial trace and the energy clause.

## H2 -- whole-space large-data weak hydrodynamic limit

F. Golse and L. Saint-Raymond, *The incompressible Navier--Stokes limit of the
Boltzmann equation for hard cutoff potentials*, J. Math. Pures Appl. 91 (2009),
508--552. https://arxiv.org/html/0808.0039v2

Read the introduction, scaling (2.3), solution definition, and the source
interfaces already inspected in KPC: Theorem 2.4, energy preparation following
(2.27), microscopic identity (2.36), and moment convergence in Proposition 7.2.
Hard spheres belong to the stated collision class. The source uses R3 and a
uniform Maxwellian with finite relative entropy, not finite total background
mass. Well-prepared data lead to a Leray velocity; the theorem does not provide
arbitrary-data endpoint regularity. Truncated observations, conservation
defects, temperature and the exact energy conclusion must be instantiated.
This supplies the entry route without assuming a smooth NS target. It does
not provide the regular kinetic solution required by every particle theorem.

## H3 -- long-time particles and the fluid companion have distinct scopes

Y. Deng, Z. Hani and X. Ma, *Long time derivation of the Boltzmann equation
from hard sphere dynamics*, arXiv:2408.07818.
https://arxiv.org/abs/2408.07818
Official Annals listing inspected on the check date:
https://annals.math.princeton.edu/articles/22284
The listing says forthcoming and states validity over the lifespan of a
regular Boltzmann solution. It is not an arbitrary-data kinetic regularity
result. No publication/acceptance date beyond that checked listing is asserted.

Companion: *Hilbert's sixth problem: derivation of fluid equations via
Boltzmann's kinetic theory*, arXiv:2503.01800v1 (3 March 2025).
https://arxiv.org/html/2503.01800v1

Inspected Theorem 1, Proposition 1.6, Theorem 2 and the empirical-observable
argument. The particle setting is T^d, d=2,3. Theorem 2 fixes a smooth NSF
target on the selected time interval; it therefore cannot produce arbitrary-
data global regularity by assuming that interval already exists. Its particle
and hydro parameters are different, and probability claims use two-particle
information. The authors claim the Newtonian/kinetic/fluid portion of Hilbert
VI. The programme adopts only a precisely scoped dilute-gas claim. Applying
this torus theorem to whole-space infinite-background renormalized H2 solutions
requires additional class and domain arguments; neither is supplied by its title.

## H4 -- strong hydrodynamic reconstruction is downstream, not a Clay producer

I. Gallagher and I. Tristani, *On the convergence of smooth solutions from
Boltzmann to Navier--Stokes*, Ann. Henri Lebesgue 3 (2020), 561--614,
doi:10.5802/ahl.40.
https://arxiv.org/abs/1903.02214
https://www.numdam.org/articles/10.5802/ahl.40/

Primary abstract and publication record inspected. The kinetic lifespan is
controlled from below using information about the fluid lifespan; the result
covers whole-space data and well-prepared periodic data in dimensions 2,3.
H3's Proposition 1.6 supplies an inspected periodic instantiation. Full function-
space hypotheses for a new whole-space particle adapter remain to be checked.
After NS-R3 is independently proved, a compatible use is noncircular. Before
then, it cannot establish the missing arbitrary-data regularity. One may
construct sufficiently small-epsilon families separately on finite horizons;
no theorem for every fixed epsilon at all times should be inferred.

Additional primary lead: P. Gervais, *On the convergence from Boltzmann to
Navier--Stokes--Fourier for general initial data*, arXiv:2201.02825.
https://arxiv.org/abs/2201.02825
Abstract inspected only; it likewise relates the kinetic lifespan to the
fluid lifespan, with polynomial velocity decay. Not an imported substitute.

## H5 -- transport-dependent Fisher control is still a research task

M. H. Duong and Z. He, *Multi-species kinetic models: GENERIC formulation and
Fisher information*, arXiv:2602.09875 (10 February 2026).
https://arxiv.org/abs/2602.09875

Primary abstract inspected. The GENERIC formulation is spatially inhomogeneous;
the stated Fisher monotonicity result is spatially homogeneous and assumes
appropriate collision kernels. Those are different scopes. No inhomogeneous,
hydrodynamically uniform macroscopic endpoint estimate is inferred. The
free-transport test in PLAN must be passed before this is used as a producer.
Changing hard-sphere collisions to Landau or another kernel needs replacement
fluid AND microscopic applicability records. Homogeneous Fisher breakthroughs
are motivation, not evidence that their critical transfer has been established.

## H6 -- geometry and Stafford remain quantitative-adapter leads

Use the primary records already checked in KPC [R3--R9] for moment geometry,
metriplectic/GENERIC structure, Villani hypocoercivity, quadratic kinetic
operators and the inverse-kinetic warning. This update does not upgrade their
proof-audit status. The Stafford38 repository's algebraic certificate and
characteristic-support architecture are not themselves bounds in kinetic
Banach spaces. Require domains, positivity, coefficient cost, derivative loss,
collision nullspace and a valid representation of the integral operator.

## Corrections binding on programme claims

Do not say the two famous problems share their ONLY missing estimate. The
critical estimate could close NS-R3, but microscopic class/domain compatibility
is an additional obligation. Do not say existing strong limits all assume
small data: some assume a smooth target on its lifespan instead. Do not infer
a regular inhomogeneous Boltzmann solution from regular momentum alone. Do
not equate finite-Knudsen physical validity, singular-limit regularity and
all of Hilbert VI. The extended programme defines its own precise endpoints;
no canonical named kinetic Millennium conjecture or novelty priority is claimed.
