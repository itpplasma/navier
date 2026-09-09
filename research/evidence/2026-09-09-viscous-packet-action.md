# The full viscous displacement action: exact identity and a finite-energy no-go

Date: 2026-09-09. Frozen input: `69cc6a45cf27f14d7ef0961a03df5245c23cdbfb`.
AUTHOR PROOFS; independent mathematical audit PENDING; novelty undetermined.
The complete proofs are in `paper/sections/viscous_history.tex`, labels
`va:identity`, `va:negative`, `va:classification`, and `va:hardy`. This supplements, and does not
replace, the preceding pressure-curvature barrier. Canonical graphs unchanged.

## 1. Exact consumer and the next failed implication

The preceding full-NS theorem excludes a singular fixed-viscosity realization
that retains the Euler construction's global upper pressure-Hessian budget.
This note follows the route to the NEXT inverse rather than stopping there.
It proves that even on one globally small original-NS background, the natural
full deterministic displacement form is unbounded below on its unit material-
derivative sphere although the Euler-shaped pressure form is coercive.

This refutes an unrestricted transfer of Euler's displacement coercivity,
not existence of all parabolic inverses. A different inverse with one common
Schwartz trace, including actual viscous spatial derivatives and signed strain,
would still have to feed UE2's nonlinear zero-residual equation, then UE3's
whole-space realization and UE4's singular endpoint. No such inverse or
terminal positive producer is proved in this note.

## 2. Full NS identity, with pressure and spatial corrections retained

Let u,p be an actual smooth unforced R3 solution at fixed nu>0. Put

    G_ij=partial_j u_i, H_p=Hess p, D_t=partial_t+u.grad,
    L_u w=P[D_t w+G w-nu Delta w].

For a real solenoidal eta compactly supported in (0,T) x R3, set
w=D_t eta-G eta. Then div w=0. The exact identity is

    L_u w=P[D_t^2 eta+H_p eta-nu Delta D_t eta
             +nu G Delta eta+2nu sum_j(partial_j G)partial_j eta]. (1)

The proof uses D_t G+G^2=nu Delta G-H_p. The two terms involving
(Delta G)eta cancel. The remaining viscous spatial terms DO NOT cancel.
No source field, prescribed local pressure, or truncated dynamics is used.

Define integrals over (0,T) x R3 by

    q_nu(eta)=-integral eta.L_u(D_t eta-G eta),
    q_E(eta)=integral[|D_t eta|^2-eta.H_p eta].

The complete tested formula is

    q_nu=q_E+nu integral[
        sum_j partial_j eta.G partial_j eta
       -sum_jk G_kj partial_j eta.partial_k eta
       -sum_j eta.(partial_j G)partial_j eta].            (2)

The Leray projection disappears only in the solenoidal pairing. All temporal
and spatial boundary terms vanish because eta is compactly supported.
The first two viscous terms at a rank-one derivative a tensor xi have symbol

    |xi|^2 a.G a-|a|^2 xi.G xi.                          (3)

Even when a is perpendicular to xi, (3) can have either sign. Its two
strain contributions are a polarization-direction difference, not ordinary
nonnegative viscous dissipation. The pressure-only Euler form is not (2).

## 3. One genuine finite-energy background defeats the coercivity shortcut

For every fixed nu>0 and delta>0 there is a nonzero real compact smooth
solenoidal d with ||d||H3<delta, whose actual original NS flow is global,
and one T>0, such that the actual canonical pressure has

    H_p<=K I on [0,T], K T^2/pi^2<=1/2,

but there are solenoidal compact spacetime eta_N satisfying

    ||D_t eta_N||_(L2_tx)=1,
    q_E(eta_N)>=1/2,             q_nu(eta_N)->-infinity.  (4)

Complete construction: take G0=diag(-1,1,0), theta=1 on B2, theta smooth
compact, and

    d_epsilon=epsilon curl[-theta(x)(x cross G0 x)/3].

It equals epsilon G0 x on B2 but is globally compact and solenoidal.
Choose epsilon small enough for both the requested H3 bound and the ordinary
energy/enstrophy small-data bootstrap. Explicitly,

    |<(u.grad)u,Delta u>|<=C||u||3||Delta u||2^2,
    ||u||3<=C||u||2^(1/2)||grad u||2^(1/2).

Initial smallness, energy, and a continuity argument keep the nonlinear
coefficient below nu/2 and the enstrophy nonincreasing. LOCAL gives global
smoothness. No numerical existence assertion or uninspected small-data import
is necessary.

Let X be THIS actual flow map, F=D_a X. For a in B1 put
v=F e1, xi=F^(-T)e2. The coefficient (3) along the flow is -2epsilon
initially, so it is <=-epsilon on a sufficiently short fixed interval,
independent of N. Local classical bounds also let T satisfy the pressure
condition above. The exterior is the actual evolving exterior; it is never
replaced by an affine field or prescribed to vanish after time zero.

Choose nonzero real phi in C_c^infinity(B1), chi in C_c^infinity((0,T)), and

    z_N=curl_a[e3 phi(a) sin(N a2)/N],
    eta_tilde_N(t,X(t,a))=chi(t)F(t,a)z_N(a).

This pushforward is exactly divergence free and compactly supported. The
full curl seed includes its envelope derivative terms. Its L2 and material-
derivative L2 norms are bounded, and

    grad eta_tilde_N=-N chi phi sin(N a2) v tensor xi+O(1).

Thus q_E=O(1), the last viscous term in (2) is O(N), and

    lim_N N^-2 q_nu(eta_tilde_N)
      =(nu/2)integral chi^2 phi^2[|xi|^2 v.G v-|v|^2 xi.G xi]<0. (5)

All background coefficients in (5) are evaluated at (t,X(t,a)). Volume
preservation and sin^2=(1-cos(2N a2))/2 prove the limit by integration by
parts against fixed compact coefficients. Material Poincare gives
||eta||2<=(T/pi)||D_t eta||2, hence q_E>=||D_t eta||2^2/2. The test norms
have a positive lower bound from the cos^2 average; normalization proves (4).

The eta_N are TEST DISPLACEMENTS, not a sequence of independent nonlinear NS
solutions, and the polynomial/affine calibrations in the checker are only
algebraic tests. The counterexample BACKGROUND is the one actual finite-energy
R3 solution constructed above. No floating-point limit is promoted to proof.

## 3a. The obstruction classifies EVERY nonzero finite-energy background

The manuscript's Theorem `va:classification` proves a stronger conclusion:
for any actual smooth finite-energy unforced NS background on an open
classical interval I, the form q_nu has a lower bound

    q_nu(eta) >= -C_I (||eta||2^2+||D_t eta||2^2)

for all compact solenoidal tests if and only if u is identically zero there.
The constant C_I may depend on the ENTIRE fixed background.

Proof: for a nonzero H1 solenoidal u, the identity
integral |sym grad u|^2=(1/2)integral |grad u|^2 shows that its strain is
nonzero somewhere. Trace zero gives distinct minimum/maximum eigenvalues.
Taking the polarization in the minimum direction and the covector in the
maximum direction makes (3) strictly negative. Continuity supplies a fixed
transported patch and a short interval. Rotate the complete curl/pushforward
construction of Section 3 to those two directions. Equation (5) and material
Poincare give unit-material-derivative tests with q_E>=1/2 and q_nu tending
to minus infinity. No special affine germ is needed for this general theorem.
Conversely u=0 implies canonical p=0 and q_nu=||partial_t eta||2^2.

Thus widening the class of backgrounds or changing pulse geometry cannot
repair this particular time-only displacement coercivity. This is a
classification of a quadratic-form method, NOT a theorem excluding all
regenerative NS trajectories or all inverses. The principal-symbol test is
standard high-frequency methodology; priority for the combined NS statement
has not been established.

## 4. Repairs actively tested and their exact limits

Boundary penalties do not repair (4): all eta_N vanish near both temporal
endpoints. A universal lower bound by q_E, or by any fixed negative constant
times ||eta||2^2+||D_t eta||2^2, fails on this one background. A norm including
spatial derivatives, a non-selfadjoint parabolic inverse, or a rigorously
restricted admissible displacement space is NOT excluded.

The other natural repair is scale-critical positive pressure curvature.
For H_p<=c/(T0-t)^2 I, zero-endpoint compact displacements on [0,T'], T'<T0,
have the classical Hardy bound q_E>=(1-4c)||D_t eta||2^2. Pull back by the
volume-preserving flow, extend by zero to T0, and apply the exact identity

    |zeta'|^2-|zeta|^2/[4(T0-t)^2]
        =(T0-t)|h'|^2-(|h|^2)'/2, zeta=sqrt(T0-t) h.

This proves a uniform interior estimate for c<1/4 even though its majorant's
sqrt-curvature clock diverges logarithmically. It is a classical scalar
inequality, not a constructed pressure, completed free-trace inverse, or NS
counterexample. The predecessor already excludes sufficiently small c for
NS by its type-I theorem. Most importantly, Hardy controls q_E and NOT (2);
the negative-action theorem defeats that automatic bridge even for bounded K.

Returning to the velocity linearization gives the valid energy identity

    (1/2)partial_t||w||2^2+nu||grad w||2^2
        =-integral w.G w+<L_u w,w>.

This is a possible parabolic repair, but its signed strain term has no
endpoint-uniform bound on a concentrating common history. Replacing it by
an uncontrolled future strain norm would not close UE1. No new regularity
producer follows merely by renaming that term.

## 5. Provenance, adversarial review boundary, and what changed

The source correspondence remains the directly inspected OpenAI Euler
history/pressure construction, with the primary URLs, version limitations
and inherited fingerprint disclosures in the companion
`2026-09-09-pressure-curvature-barrier.md` and
`literature/viscous-history-source-audit-2026-09-09.md`. Its inviscid equation
has D_t G+G^2=-H_p; the viscous counterpart is computed explicitly in (1).
No external Euler result is contradicted. The owner-checked FORCED NS theorem
and previous Lean records remain at their existing scopes; no new kernel
run or independent source audit is claimed.

Fresh primary inspections also retained the distinction between Palasek's
forced viscous model / inviscid unforced model (arXiv:2605.13827v1, Sections
1.3.2 and 3.3) and actual unforced NS. Chae--Constantin's arXiv:2103.10672v1,
Theorem 1.1 and Proposition 1.1, concerns signed directional Euler Hessian
criteria; it is not an imported NS action theorem. Seregin--Sverak's 2002
pressure-criterion record was inspected at abstract/metadata level only.
The Caltech author endpoints were attempted again and remained unavailable;
no new complete stability certificate or source fingerprint is claimed.
Targeted primary-source searches did not establish priority for the present
combination. The Lie-bracket displacement relation, integration by parts,
small-data bootstrap and Hardy inequality are standard ingredients.

`research/check_viscous_packet_action.py` checks the full three-component
operator on a nonconstant-gradient NS jet, an independently expanded local
integration-by-parts current, the all-entry rank-one matrix symbol, exact
cutoff curls, the strain sign, oscillatory averages and the Hardy identity.
It does NOT certify the continuum proof, Riemann-Lebesgue limit, small-data
lifespan, all admissible backgrounds, novelty, or independent correctness.
No independent reviewer or agent was obtained. Proof graphs are unchanged.

The first failed unrestricted implication is now explicit:

    upper-pressure control / Euler-shaped coercivity
        DOES NOT IMPLY coercivity of the full viscous displacement form.

The primary remaining theorem is one viscosity-specific, common-Cauchy-trace
inverse on a specified concentrating full history, compatible with the
necessary unbounded positive-pressure-curvature budget, and strong enough to
cancel its entire solenoidal residual while preserving a singular lower bound.
UE2--UE4 remain behind it. Neither NS-R3 nor an unforced regenerative cascade
has been resolved by these obstructions.

## 6. Completed validation in the integrated full checkout

All 23 `research/check_*.py` programs passed, with the phase-ring checker run
through order eight and the new action checker passing 27 exact assertions.
Both `research/verify.py --research-only` and `--paper-only` passed with 29
canonical records and 8 pending supplements. `git diff --check` passed.
The manuscript's `make documents check` and a forced complete main rebuild
passed with resolved references. The new action/classification section on
pages 139--143 of the 146-page main PDF was rendered and visually inspected.
The first build found an unsupported mathscr macro; it was changed to mathcal
and the entire build rerun successfully. No generated PDF, cache or local
bibtex shim is committed. No numerical NS orbit, independent audit, formal
kernel run, terminal theorem, or breakthrough-grade cascade is claimed.
