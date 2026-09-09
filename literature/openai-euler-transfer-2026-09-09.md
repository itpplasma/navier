# OpenAI Euler construction: source inspection and viscous transfer

Inspection date: 2026-09-09. Research input: navier commit
`5244cc979129cb8283a4cf99283670582c5aca85`. This is an original source-inspection
and transfer note, not an independent audit of the Euler proof. PLAN owns
allocations. No claim in the canonical graph is promoted.

## Provenance and scope

The source is OpenAI, *Finite Time Blowup for the Euler Equation*, 57 pages,
linked from the [September 8 release](https://openai.com/index/navier-stokes-solution/).
The [PDF](https://cdn.openai.com/pdf/315b36cd-ec98-4023-8342-93345194ece1/euler.pdf)
was retrieved September 9; its SHA-256 is
`a0c234518e6c489e16996805023eb2e75c00b7c03455f7a3a5be2c124954bfdd`.
Page references below use printed page numbers. The PDF is external scratch
material; only metadata and original notes are retained here. The release
attributes the Euler work to an internal agent system; this is author-reported
provenance, not mathematical evidence or independently verified training history.

The associated [Lean source](https://github.com/openai/NavierStokesAndEuler/tree/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538)
is pinned at `8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538`. The existing local
package checkout at that commit was clean when inspected, read-only. It uses
Lean `v4.34.0-rc2`, Mathlib `85e3a25e006c35636f0e53b0e9296caca2685bc0`,
and Apache-2.0 licensing. These identifiers freeze the source input; they do
not certify the paper-to-Lean correspondence.

Theorem 1.1 concerns unforced incompressible Euler on R3, viscosity zero:
one nonzero smooth compactly supported divergence-free datum, finite maximal
smooth lifespan, unbounded velocity gradient at the endpoint, and infinite
time integral of the maximum vorticity. Compact smooth data are Schwartz.
It is an existence assertion for one datum, not arbitrary-data blowup, and
it need not assert unbounded speed. No collision model is present. It is
separate from OpenAI's forced positive-viscosity theorem and the Caltech
Euler profile/stability framework; their fingerprints and scopes remain in
the [September ledger](recent-progress-2026-09.md).

Inspection covered the packet hypotheses and estimates in Proposition 3.1,
the mean/transverse inverses, expansion and correction (§§3.3--3.7), initial
bounds, the statement and activation argument of Proposition 4.1, scale
selection and induction (§5), and limiting datum/continuation (§6). The
moving-frame calculation was inspected selectively; its full perturbation
bounds and every all-order estimate have not been independently reproduced.
The bibliography is a dependency-discovery list, not a set of newly audited
literature premises. Source author proof: present. Source inspection: detailed
but selective. Independent mathematical audit: not performed. Euler kernel
replication and complete statement-faithfulness audit: not performed here.
The previous forced-NS kernel result does not establish those Euler statuses.

## Construction and consumer chain

The source constructs distinct exact smooth odd Euler solutions U_j, with
activation/target times t_j increasing to a finite T_infty. Their initial
increments are summable in each fixed H^m and supported in one fixed ball.
Their central gradients at t_j diverge. The final datum is the limit of
U_j(0), rather than a concatenation of independently initialized solutions.

The dependency order is:

    one-sided pressure and initial-strain bounds
      -> coercive displacement histories and localized initial mean
      -> primary wave amplification and full transverse propagator
      -> mean-first coefficient recursion with exact incompressibility
      -> exponentially small residual and exact lifted correction
      -> next shear, pressure sign and geometric frame
      -> scale induction and summability of one initial datum
      -> hypothetical smooth-continuation comparison -> Euler breakdown.

The NS consumer would need the same chain at ONE fixed nu>0, uniformly over
all stages and terminal cutoffs, including canonical pressure and the full
exterior. A successful stage alone does not provide UE1--UE4. Constants may
depend on nu and fixed construction choices, but not on an uncontrolled
future norm of the sought singular solution.

## Connected preparation and the mean inverse

Write X_t=u(t,X), F=grad_a X, M=(grad u)(t,X), H=(Hess p)(t,X).
Euler gives F_t=MF and F_tt=-HF. With m=F^{-T}m0, a transverse velocity obeys

    m_t=-M^T m,
    v_t=-Mv+2m(m.Mv)/|m|^2,       m.v=0.

For activation time t0>0, the history displacement is eta=F R_perp xi,
xi(0)=0, xi(t0)=xi_T. Its stationary action integrates
|eta_t|^2-H eta.eta. The velocity is v=F R_perp xi_t and is generally
NONZERO initially. Forward continuation uses the terminal history velocity;
there is no reset at activation. Proposition 4.1 chooses xi_T using a
symmetric positive endpoint map Lambda, with 0<=Lambda<=C h_* I, to obtain
the activation signs v_q=1 and -C<=v_p<=0. This is a concrete response to
our common-trace problem in the inviscid setting.

The angle-independent mean is also essential (§3.3, pp. 13--17). Its
history variable z is divergence-free and satisfies z(S)=0. The boundary
operator is A=curl chi (-Delta)^{-1} chi curl, with the outer localization
chosen in physical initial labels. Its positive quadratic form controls a
localized part of z(0); the remainder is harmonic in an interior ball.
The volume factor r^3 makes a large negative initial strain in a tiny core
compatible with coercivity. In the source notation the sufficient bounds are

    H <= K_+ I,
    sym M(0) >= -B_e I outside the core, >= -B_c I inside,
    K_+ S^2/2 + B_e S + C_2 B_c r^3 S <= 1/2,
    L >= C_1 B_c.

The variational form adds the initial M(0) term and L<A z(0),z(0)>.
Its coercivity is at least half the displacement-velocity energy, with
conversion to label norms costing a fixed power of the coefficient bound P.
The boundary equation gives z_t(0)=L A z(0), hence compact initial mean.
The positive-time mean may be noncompact: the pressure is global throughout.
This avoids imposing compact support on an evolving velocity.

The source proves Gevrey-order-two estimates, allowing compact cutoffs.
P bounds the parent coefficients, inverse metrics, scales and actual
transverse propagator. Powers of P have fixed exponents independent of
frequency and expansion length; constants for initial H^m bounds may depend
on the fixed m. A finite-parent bound is not automatically uniform in j:
§5 supplies the separate scale induction needed to use it repeatedly.

## Pressure sign and exact correction

For physical phase k m0.a/ell, the leading increment is
(ell alpha/k) chi_1 v f_delta. Its gradient is
alpha chi_1 v tensor m f_delta', with lower-order errors. The asymmetric
periodic profile has f_delta'(0)=delta^{-1} and f_delta'>=-C. The leading
pressure Hessian increment is

    -2 alpha chi_1 (m.Mv) (m tensor m)/|m|^2 f_delta'.

Proposition 4.1 proves m.Mv>0 after the initial activation transient.
The large positive derivative spike therefore produces a negative
semidefinite Hessian increment. Only the bounded negative derivative and
small errors consume the UPPER pressure-Hessian budget. Large absolute
Hessian norms are allowed. Earlier history/transient costs are controlled
by their exponentially smaller relative amplitude. In §5.7, the summed
positive costs involve delta_j h_j h_{j-1}, history costs, and k_j^{-1/4}.
Replacing this signed estimate by a summable absolute Hessian bound would
lose the mechanism. The formula includes global remainders; it is not a
local-pressure assumption.

At order p in k^{-1}, solve the mean B_p before the transverse A_p. The
current-order coupling -(B_p.m) partial_theta A_1 has zero angle mean;
it is then known in the transverse solve. Curl potentials supply exact
lifted divergence-freeness at every order. This is a useful triangular
structure to seek in a viscous redesign, not an established viscous inverse.

Section 3.6 solves an actual correction on R3_y times T_theta. With
kappa=k^{-1} and D_i=kappa partial_yi+(m0)_i partial_theta, incompressibility
is constant-coefficient div_D z=0. The pressure projection has symbol
(q tensor q)/|q|^2, q=kappa xi+n m0; its norm is bounded despite the
measure-zero zero set. Coercivity of the metric handles the variable
coefficient inverse. The correction starts at zero; its graph restriction
has a genuine scalar pressure and solves the exact Euler equation.

The expansion length is floor(k^vartheta), vartheta=10^{-6}. The source
requires P^Q<=k^{vartheta/100}, for a fixed sufficiently large Q. Its
normalized residual is at most exp(-0.7 k^vartheta log k), whereas the
correction is bounded by a power of P times exp(-k^{vartheta/2}). This
margin pays the exp(P^c S) Gronwall factor and graph differentiation costs.
Thus the paper does not identify a merely flat residual with zero force.
The heat term introduced in (3.51) regularizes ONLY this correction in
(y,theta); its coefficient tends to zero before graph restriction. Retaining
it neither diffuses the approximate velocity correctly nor yields physical
fixed-viscosity NS.

## Scales and passage to a single datum

For normal stages, (5.3) chooses

    x_j=j^2 x_{j-1},
    log h_j=x_{j-1}/j^5,       log k_j=x_{j-1}/j^2,
    log delta_j^{-1}=x_{j-1}/j^3,
    log ell_j^{-1}=x_{j-1}/j^(7/2).

The seed has fixed large parameters chosen in order D0, Dk, J, x0 (D0=1000).
Normal-stage amplitudes satisfy alpha_j<=P_j^c exp(-b x_{j-1}) for an
absolute b>0, with log P_j=o(log k_j). The estimates for the logarithms
of the initial H^m increments are

    high: -b x_{j-1}+m x_{j-1}/j^2+m x_{j-1}/j^(7/2)+C_m log P_j,
    mean: -2 x_{j-1}/j^2+m x_{j-1}/j^(7/2)+C_m log P_j.

Both are summably negative eventually for EACH FIXED m. The mean has no
oscillatory k_j^m differentiation cost. This separation is indispensable
for obtaining a smooth datum with compact support.

Section 6 compares U_j with the limiting solution only under the assumption
that the latter persists smoothly beyond T_infty. For y=||U_j-u||_{H^3},
y'<=C_u y+C y^2, with C_u controlled by the hypothetical solution's H^4
norm and independent of j. Initial convergence closes the small-difference
bootstrap, contradicting the central gradient growth. This is legitimate
conditional continuation reasoning; it is distinct from assuming an unknown
future norm to construct the stages. The conclusion is T_*<=T_infty, not
an identification T_*=T_infty. The same type of final argument is a useful
NS closure template if exact viscous approximants can first be constructed.

## First failures of an unchanged NS transfer

The following are direct equation calculations and transfer diagnostics by
this note's author, not new independently audited impossibility theorems.
For a smooth unforced NS parent at fixed nu>0,

    F_tt = [nu (grad Delta u)(t,X)-H] F.

Consequently the Euler cancellation in the displacement action leaves
nu grad Delta u. Bounding it requires a new estimate or a different inverse;
the source's one-sided pressure bound does not bound this third velocity
derivative. The pressure Poisson equation itself still has the usual
quadratic source, but that alone does not preserve its dynamical sign bounds.

In the physical lifted increment equation, diffusion contributes

    nu ell^{-2} sum_i tilde_d_i tilde_d_i W,
    tilde_d_i=d_i+k m_i partial_theta.

This differentiates envelopes and coefficients as well as the phase, couples
labels in the history solve, and generates noncompact analytic leakage.
The pointwise-in-label transverse history inverse is therefore not the same
problem. An Euler exact solution used unchanged also leaves projected NS
residual -nu Delta u; pressure cannot absorb a general solenoidal residual.

For a single leading Fourier harmonic n and a prescribed smooth parent,
the geometric-optics amplitude acquires scalar damping

    exp(-D_{j,n}(t)),
    D_{j,n}(t)=nu n^2 (k_j/ell_j)^2 integral_0^t |m_j(s)|^2 ds.

This follows by taking the leading phase part of the Laplacian. It is a
leading-symbol diagnostic, not a complete localized packet estimate. Lower
order diffusion, mean coupling and nonlinear transfer still need analysis.
For n=1 the frequency multiplier in D is
exp(2 x_{j-1}/j^2+2 x_{j-1}/j^(7/2)). Any common early interval with a
uniform positive lower bound for the ray integral would make this loss
outgrow the Euler logarithmic amplification budget b x_{j-1}. Such an
interval is natural for a family with convergent smooth initial data, but
must be proved for the proposed viscous construction. Small fixed viscosity
does not remove this asymptotic issue.

The sharp angular spike contains multiple harmonics with n^2-dependent
damping. Even a fundamental-mode estimate does not preserve its shape or
pressure sign. A revised construction could transport initially low
frequencies into late high frequencies, use a different geometry or obtain
additional amplification, but must estimate its full prehistory and
harmonic distortion. This inspection excludes no such redesigned mechanism.

## Lean declaration trail and verification boundary

At the pinned commit, `ComparatorChallenges/Euler.json` names
`Euler.euler_breakdown_R3` and `Euler.exists_compact_smooth_euler_singularity`,
with solution module `Euler.Solution` and permitted axioms `propext`,
`Quot.sound`, `Classical.choice`. The reference challenge contains intentional
`sorry` placeholders; `Euler/Solution.lean` imports separate definitions and
supplies proof bodies, ending with axiom-print commands. Seeing those
commands is not observing their output or running Comparator/nanoda.

The first challenge excludes a global jointly smooth finite-energy Euler
solution for a rapidly decaying datum. The quantitative challenge also
provides nonzero compact initial data, 0<T_*<=1, a maximal all-order Sobolev
solution, locally finite C1/vorticity bounds, and divergent endpoint bounds.
Its finite-interval pressure class differs from the global smooth class.
The source explicitly bridges those classes; that bridge needs a separate
faithfulness audit before importing the result.

Useful code navigation, all relative to the pinned repository:

| Source obligation | Lean trail to inspect |
| --- | --- |
| Actual initial high/mean bounds | `Euler/PacketInitializedInitial.lean`, especially `initializedInitialHigh_Hm`, `initializedInitialMean_Hm` |
| Fixed-order summability | `Euler/PacketInitialSummability.lean`: `actual_high_summable`, `actual_mean_summable` |
| Mean localization and curl identities | `Euler/MeanCurlIntegration.lean`, `Euler/MeanTranslatedGevrey.lean` |
| Exact correction and pressure on the graph | `Euler/AllOrderLiftedCorrection.lean`, `Euler/ExactLiftedGraphPressure.lean` |
| Joining histories and scale budgets | `Euler/PacketJoinedStepBudget.lean`, `Euler/PacketJoinedUniformProfiles.lean` |
| Finite lifespan and ordinary-function bridge | `Euler/EulerSingularity.lean`, `Euler/ComparatorMaximalSolution.lean`, `Euler/Solution.lean` |

Declaration headers and the challenge/solution surfaces were inspected;
this table also contains navigation leads whose complete dependencies were
not read. No new Lean build, axiom report or formal coverage is claimed.

## Literature clues and next discriminating estimate

The bibliography points to several older mechanisms worth preserving with
their limitations. Craik--Criminale (1986),
[DOI 10.1098/rspa.1986.0061](https://doi.org/10.1098/rspa.1986.0061), is the
viscous wave-construction lead. Fabijonas--Holm (2004),
[DOI 10.1017/S0022112004008511](https://doi.org/10.1017/S0022112004008511),
must be read together with Le Dizes--Leblanc (2006),
[DOI 10.1017/S0022112005007949](https://doi.org/10.1017/S0022112005007949).
These are source-bibliography leads, not newly verified Schwartz-class NS
theorems. The correction's publisher abstract says the proposed general construction
solves NS along a single base-flow trajectory and generally cannot be
iterated after its first step. That is a direct warning against confusing
ray evolution with a whole-space solution. Full original
statements and their spatial/energy classes remain to be checked before use.
Do not infer that multiple exact wave additions remain exact after
localization or interaction.

Other precise trails are Brenier (2008),
[10.1016/j.physd.2008.02.026](https://doi.org/10.1016/j.physd.2008.02.026)
for the pressure/action connection; Cheverry (2006),
[10.24033/bsmf.2501](https://doi.org/10.24033/bsmf.2501) for phase cascades;
and Lifschitz--Hameiri (1991),
[10.1063/1.858153](https://doi.org/10.1063/1.858153) for ray/polarization
instability. Their original theorem hypotheses were not audited in this
inspection. BKM and local classical theory are the endpoint tools; neither
supplies the packet producer.

The next UE1 calculation is the fixed-viscosity history map for one complete
packet, including the mean, harmonics, envelope derivatives and exterior.
Measure initial H^m preparation cost against target shear using the integrated
physical wavevector, then test the countable scale sequence. A successful
estimate must preserve the upper pressure-Hessian budget and give initial
costs summable for each fixed m. If it returns exponential preparation loss
that defeats those costs, change the frequency history or geometry before
attempting the all-order correction. PLAN, rather than this source note,
allocates that work. No terminal NS theorem follows from the inspection.
