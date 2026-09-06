# Kinetic research contracts: terminal sufficiency and falsification tests

Date: 2026-09-06. Research input: `1383040bbb775826c6d78674852f8ba89f25b353`.
Status: planning calculations and primary-source scope checks, not a new
critical estimate, independent audit, or promoted graph node. PLAN.md alone
allocates live work. This note defines its interfaces and test cases.

NS-R3 remains NOT PROVED; the terminal obstruction is UNCHANGED.

## 1. A faithful kinetic entry, not an assumed smooth fluid solution

Use R3_x x R3_v, a uniform Gaussian M(v)=(2pi)^(-3/2) exp(-|v|^2/2),
and a fixed hard-cutoff Boltzmann collision operator. Start with the
Golse--Saint-Raymond (GSR) whole-space renormalized-solution framework [R1],
not a perturbative global classical kinetic theorem. In scaled coordinates,

    epsilon^2 partial_t F + epsilon v.grad_x F = Q_nu(F,F),
    F_epsilon^in(x,v) = M(v-epsilon u0(x)).

This uses only the prescribed solenoidal Schwartz u0. It does not insert an
unknown future fluid velocity into a kinetic force. Fix one base hard-sphere
kernel with limiting viscosity nu_b>0; multiplying that kernel by nu_b/nu
multiplies the linearized collision operator by the same factor and its
inverse by nu/nu_b. The viscosity formula [R1, (2.27)/(2.53)] therefore gives
the prescribed nu. Verify this normalization once with the chosen conventions.

Direct Gaussian integration gives

    epsilon^(-1) integral v F_epsilon^in dv = u0,
    epsilon^(-2) H(F_epsilon^in|M) = (1/2)||u0||_2^2.

Here H(F|M)=integral(F log(F/M)-F+M) dx dv. Total background mass is infinite;
relative entropy, not unrenormalized total entropy or mass, is finite.
The initial thermal fluctuation in GSR's convention is
(epsilon/5)|u0|^2 -> 0. The preparation saturates the kinetic-energy entropy
bound. GSR Theorem 2.4 and the paragraph after (2.27) specifically distinguish
the general NSF limit from the resulting Leray NS solution with this
preparation. Import the exact energy/initial-trace conclusion, not merely
the phrase "hydrodynamic limit". The momentum equation has no thermal forcing.

Collision moments are exact for sufficiently regular integrable solutions;
for renormalized solutions, truncated identities and their conservation
defects must be retained until the hypotheses allowing their removal hold.
Do not take an unproved classical moment equation for F as an input.

A practical projected moment for estimates is

    g_epsilon = (F_epsilon/M-1)/epsilon,
    gamma_epsilon = gamma(F_epsilon/M),
    m_tilde_epsilon = P integral v g_epsilon gamma_epsilon M dv,

where gamma is the fixed smooth density truncation in [R1, (2.40)] and P is
the spatial Leray projection, NOT the collision-nullspace projection below.
On the support of gamma, |g_epsilon gamma_epsilon| is bounded by a constant
times |sqrt(F_epsilon/M)-1|/epsilon. The entropy estimate and Gaussian
Cauchy--Schwarz therefore give an L-infinity_t L2_x bound for this moment.
GSR's velocity cutoffs can be included when deriving its evolution.
Its identification with the fluid velocity in the limit, including removal
of density/velocity truncations, must be checked from that framework. The
raw moment and m_tilde need not have the same finite-epsilon L3 regularity.
An alternative surrogate is allowed only with a proved distributional limit
and the same initial-data identification. No truncation defect is discarded
on the strength of its name.

## 2. A limit-first certificate is enough

Choose an input-determined local existence time tau_loc(u0,nu)>0 from LOCAL,
put delta=tau_loc/2, and consider H>delta. The local branch already handles
the initial interval. A kinetic estimate need not resolve its initial layer
uniformly all the way to t=0.

Let S_J be convolution by rho_J(x)=2^(3J)rho(2^J x), where rho is a fixed
nonnegative C_c^infinity approximate-identity kernel with integral one.
These are spatial smoothing operators, not collision or Hermite projections.
They commute with P on its legitimate domain and converge to the identity.
Suppose a single hydrodynamically convergent sequence epsilon_k -> 0 has
m_tilde_epsilon_k -> u in distributions on (delta,H) x R3, with the
preparation and Leray-solution conclusions of Section 1. The proposed
sufficient certificate is

    sup_{J>=0} liminf_{k->infinity}
      ||S_J m_tilde_epsilon_k||_{L-infinity(delta,H;L3(R3))}
        <= C(u0,nu,H,delta) < infinity.                    (K_res)

All J use the same family and limiting u. Constants must be independent of J.
This is a weaker kinetic demand than sup_epsilon ||m_epsilon||_{L-infinity L3};
it is NOT a proved estimate or a strictly reduced NS terminal obstruction.
Different H may use different kinetic subsequences, since identification with
the unique classical branch on its lifespan is sufficient.

Why K_res suffices: fix J and a smooth compact test phi in time and space.
Distributional convergence and Holder imply

    |<S_J u,phi>| <= C ||phi||_{L1_t L^(3/2)_x}.

To justify the use of liminf, choose a subsequence attaining it for this J;
its distributional limit is still S_J u. Convolution with rho_J preserves
local distributional convergence. Letting J tend to infinity gives the same
inequality for u. Density and the duality of L1_t L^(3/2)_x give
u in L-infinity(delta,H;L3_x), with norm at most C. This argument is global
in x: estimates only on compact spatial sets with growing constants are not
enough. An L2-based estimate growing like 2^(J/2) fails K_res.

Weak--strong uniqueness identifies the Leray limit with the local classical
branch on every compact interval before Tstar. The usual difference-energy
estimate uses integral ||grad u_classical||_infinity dt, finite there by LOCAL;
it is used ONLY for identification, not as an endpoint bound. Combine LOCAL
on [0,delta] with K_res on (delta,H). If Tstar<H were finite, CONTINUATION
would contradict the resulting uniform L3 bound on the classical branch.
Thus LOCAL, ENERGY, the correctly instantiated hydrodynamic theorem, this
identification argument and K_res imply NS-R3. The interface work is routine
compatibility work; the unproved content is K_res's arbitrary-data producer.

Do not exchange the limits. Taking epsilon -> 0 at each fixed resolution
before removing smoothing does not justify a simultaneous estimate at
J=J(epsilon), and does not require one. Estimates for finitely many fixed
resolutions with constants C_J are also insufficient. A bound for each
individual dyadic block does not automatically control L3 of their sum.

## 3. What transport actually couples to collisions

For smooth weighted fluctuations define T=v.grad_x, the nonnegative
linearized collision operator L, and Gamma(g,g)=M^(-1)Q_nu(Mg,Mg), with the
bilinear convention consistent with L. The scaled fluctuation equation is

    partial_t g + epsilon^(-1)Tg + epsilon^(-2)Lg
        = epsilon^(-1)Gamma(g,g).                          (F)

Let Pi be orthogonal projection in L2(Mdv) onto
span{1,v1,v2,v3,|v|^2}; let Qmic=I-Pi, a=Pi g, h=Qmic g. Collisions conserve
these five modes, so Pi Gamma(g,g)=0. Formally, on a smooth justified class,

    partial_t a + epsilon^(-1)Pi T a + epsilon^(-1)Pi T h = 0,
    partial_t h + A_epsilon h
       = -epsilon^(-1)Qmic T a
         +epsilon^(-1)Qmic Gamma(g,g),
    A_epsilon = epsilon^(-2)L + epsilon^(-1)Qmic T Qmic.

Duhamel elimination of h produces a retarded macroscopic stress with kernel
-Pi T exp(-(t-s)A_epsilon) Qmic T, plus the initial microscopic layer and the
NONLINEAR Gamma source. These formulas specify a candidate analysis, not a
proved semigroup construction on all renormalized solutions. Domains,
truncation errors and their limit must be supplied in an actual estimate.
Eliminating h does not eliminate its nonlinear source.

For a solenoidal smooth U(x), Gaussian projection gives the exact linear
identity

    Qmic T(U.v) = (v tensor v - |v|^2 I/3) : D U,
    D U = (grad U + grad U^T)/2,
    integral M |Qmic T(U.v)|^2 dv = 2|D U|^2.              (S)

The antisymmetric part cancels in v_i v_j partial_i U_j; trace(D U)=0 and
Gaussian second/fourth moments prove (S). At a transverse Fourier mode it
has squared norm |xi|^2 |U_hat|^2. This is a concrete macroscopic coupling,
not damping of every collision-invariant mode by collisions alone. On R3
there is no uniform spatial gap as xi -> 0. The low-frequency loss must be
handled by the energy class rather than a torus/confinement Poincare bound.
The identity recovers strain-level information, not automatically critical
L-infinity_t L3 control.

A further exact identity in [R1, (2.36)] is

    Gamma(a,a) = (1/2)L(a^2) for a in ker L.              (M)

It comes from differentiating the local-Maxwellian manifold twice. Put
r=h-(epsilon/2)Qmic(a^2). With the symmetric bilinear convention for Gamma,
the formal remainder equation is

    partial_t r + A_epsilon r = -Qmic T a/epsilon
      + Qmic[2 Gamma(a,h)+Gamma(h,h)]/epsilon
      - (epsilon/2)Qmic partial_t(a^2) - (1/2)Qmic T Qmic(a^2).

The pure macroscopic collision source has canceled, but differentiating the
correction has introduced exactly the terms displayed. The macro equation
also retains (1/2)Pi T Qmic(a^2), which contains the convective flux. This is
already known structure in the fluid-limit literature, not a new cancellation
claim. The FIRST hard test is whether those actual remainder terms admit
K_res's uniform output estimate for arbitrary data. Merely recovering the
Newtonian stress, or an uncontrolled cubic flux, fails that test.

## 4. Kinetic and algebraic rejection tests

### Entropy and instantaneous collision production

For F_epsilon,U=M(v-epsilon U(x)), Gaussian integration gives
H/epsilon^2=||U||_2^2/2 and the rescaled momentum equals U. The collision
operator and its entropy production vanish pointwise in x, because each
slice is Maxwellian. For U_lambda=lambda^(3/2)phi(lambda x), with fixed
nonzero compact solenoidal phi, L2 is fixed and
||U_lambda||_3=lambda^(1/2)||phi||_3 -> infinity.
Thus those two instantaneous scalar inputs alone cannot give critical
spatial control. These are snapshots, not transport-collision trajectories.
For each lambda one may also choose epsilon small enough that epsilon U_lambda
is small in supremum norm; that does not make the limiting U_lambda small.

### Algebraic rank versus quantitative cost

[partial_v_i,v.grad_x]=partial_x_i and the Gaussian ladder operators satisfy
[a_i,a_j^*]=delta_ij. These are genuine differential-operator relations.
For T_b=b v partial_x in one dimension, b>0, bracket generation holds for
EVERY b, yet the controllability Gramian for (dot x=b v, dot v=input) is

    G_t = [[b^2 t^3/3, b t^2/2], [b t^2/2, t]],
    det G_t = b^2 t^4/12.

Its smallest eigenvalue degenerates as b -> 0, despite unchanged rank.
This elementary calculation tests any purported uniform certificate-to-
estimate step; it is not the scaling of the full Boltzmann problem.
For the actual problem track epsilon, spatial frequency, collision-kernel
constants, velocity weights and every approximation order explicitly.

The Stafford identity 1=dR+FdS is an algebraic identity in the written
operator order, not a positive coercivity estimate or a bounded inverse.
A useful transfer must specify operator domains, adjoints, analytic norms,
coefficient costs and derivative loss. Boltzmann's collision integral is not
a finite polynomial differential operator. Hermite or quadratic-model
approximations require uniform control of their discarded terms; a fixed
finite truncation proves nothing about their infinite-dimensional parent.
Kinetic Ornstein--Uhlenbeck models generally do not retain Boltzmann's five
collision invariants. They are calibration problems, not interchangeable
NS-producing collision operators.

### Physical and microlocal geometry

In the canonical bracket on physical (x,v), c_i=v_i-U_i(x) obeys
{x_i,c_j}=delta_ij and {c_i,c_j}=partial_i U_j-partial_j U_i.
For the low-Mach shift c=v-epsilon U the latter bracket has the additional
factor epsilon. All other scaling factors must remain in the generator.
The identity displays vorticity; (S) displays symmetric strain. A moving
Hermite frame must retain both and its time derivatives. It cannot make
unknown strain harmless by changing coordinates.

Physical phase space is T*R3, dimension 6. Microlocal analysis of an operator
on f(x,v) uses T*R6, dimension 12. An A6-type polynomial differential algebra
acts on six independent variables; physical v is not the fluid Fourier xi.
An arbitrary concentration measure is not a finitely generated D-module and
has no automatic involutivity or coisotropic support theorem. Also
(x,v)->(lambda x,lambda^(-1)v) is symplectic but squeezes space, so symplectic
non-squeezing is not a spatial concentration bound.

Ordinary quadratic defect measures can miss the critical phenomenon:
U_r(x)=r^(-5/4)phi(x/r) has ||U_r||_2^2=r^(1/2)||phi||_2^2 -> 0 but
||U_r||_3=r^(-1/4)||phi||_3 -> infinity. Its unnormalized L2 defect is zero.
Any proposed defect selection must retain the critical normalization, not
infer critical tightness from strong L2 convergence. This is a field test,
not an actual NS or kinetic blowup trajectory.

## 5. Sources and verified scope

These are planning references, not new imported nodes of the proof graph.
Public primary records were checked on 2026-09-06. R1's Theorem 2.4,
preparation paragraph, collision nullspace and equations (2.36)/(2.38), and
R2's small-data hypotheses in Theorems 2.1--2.2 were read in full HTML.
For R3--R9 the primary abstracts/records were checked; their full proofs
were not audited here. A literature lead is not an applicable theorem until
its exact hypotheses are instantiated. No exhaustive novelty search is claimed.

[R1] F. Golse and L. Saint-Raymond, The incompressible Navier--Stokes limit
of the Boltzmann equation for hard cutoff potentials, J. Math. Pures Appl.
91 (2009), 508--552. https://arxiv.org/html/0808.0039v2
Large-data weak limit; no arbitrary-data critical regularity estimate.

[R2] C. Cao and K. Carrapatoso, Hydrodynamic limit for the non-cutoff
Boltzmann equation, Ann. Inst. H. Poincare C 43 (2026), 417--482,
doi:10.4171/AIHPC/139. https://arxiv.org/html/2304.06362v3
Uniform strong-limit estimates in a perturbative framework; their smallness
is on the scaled fluctuation. Changing to non-cutoff kernels requires a
compatible large-data limit theorem, not an unannounced reuse of R1.

[R3] J. Gibbons, D. D. Holm and C. Tronci, Geometry of Vlasov kinetic moments:
a bosonic Fock space for the symmetric Schouten bracket (2008).
https://arxiv.org/abs/0803.2667
Moment-map and Lie--Poisson geometry, not finite closure or NS regularity.

[R4] M. Grmela et al., Hamiltonian and Godunov structures of the Grad hierarchy,
Phys. Rev. E 95 (2017), 033121. https://arxiv.org/abs/1609.05070
Structured moment hierarchies; arbitrary finite truncation remains unjustified.

[R5] P. J. Morrison and M. H. Updike, Inclusive curvaturelike framework for
describing dissipation: metriplectic 4-bracket dynamics, Phys. Rev. E 109
(2024), 045202. https://arxiv.org/abs/2306.06787
A. Zaidni and P. J. Morrison, Metriplectic four-bracket algorithm for
constructing thermodynamically consistent dynamical systems, Phys. Rev. E
112 (2025), 025101. https://arxiv.org/abs/2501.00159
Geometric thermodynamic structure is prior art, not an endpoint producer.
Conserved thermodynamic energy includes internal energy; the target NS
kinetic energy decreases. Added stresses/dissipation must not change the target.

[R6] C. Villani, Hypocoercivity, Mem. Amer. Math. Soc. 202 (2009).
https://arxiv.org/abs/math/0609050
Transport--dissipation methods; positivity alone does not supply nonlinear,
whole-space, singular-limit critical constants.

[R7] M. Hitrik and K. Pravda-Starov, Spectra and semigroup smoothing for
non-elliptic quadratic operators, Math. Ann. 344 (2009), 801--846.
https://arxiv.org/abs/0712.0819
K. Pravda-Starov, Subelliptic estimates for quadratic differential operators,
Amer. J. Math. 133 (2011), 39--89. https://arxiv.org/abs/0809.0186
Quantitative analytic precedent for the algebraic lane. Quadratic differential
operators and singular spaces are not the nonlinear collision integral.

[R8] M. Tessarotto and M. Ellero, Unique representation of an inverse kinetic
theory for incompressible fluids (2006). https://arxiv.org/abs/physics/0602140
An exact representation still needs independent existence and estimates;
no smooth-input assumption may be used to establish that same smoothness.

[R9] Stafford context inspected through the connected repositories:
`itpplasma/stafford38/README.md`, blob
`5fce0341f10afc0a3f50c576943dceeaee57fe1f`, and
`itpplasma/stafford38-formal/README.md`, blob
`cb080e4c5ef6bb0bada3ce6a63f9f2fcd47aa6c4`.
The stated certificate, ordered operator identity and geometric proof
architecture motivate a possible quantitative adapter. Its reported Lean
verification was not rerun here and supplies no analytic NS estimate.

## 6. Integrity-check scope for this plan update

The unchanged research-only verifier and its graph inputs were checked using
an overlay of the retained GitHub Actions source artifact (run 34047280192,
artifact 9993481723, source commit 5ee2b9880a7dfe27f990a9e3706bb3817f5ac8b3).
The archive SHA-256 is
58242a5844358e8e2805debe7dea563e1f6fe9ac9ead21f3db1dd56519f1b4a3.
The connector comparison to the frozen research input shows the graph,
verifier and graph-referenced inputs unchanged; the local graph and verifier
blob hashes were checked against that input. The new PLAN and this note were
overlaid, `python3 research/verify.py --research-only` and `git diff --check`
passed. This was not a fresh full checkout; manuscript/formal-repository
checks were skipped. These are file/status integrity checks, not verification
of the proposed nonlinear estimates or a mathematical audit.
