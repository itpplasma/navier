# Prepared-family Fisher obstruction and sharp causal stress-output obstruction

Date: 2026-09-06. Inspected main: `64eaac42ccac6a00309a9af412d6e4f7ff21538a`.
Status: complete author derivations; independent mathematical audit pending.
No novelty claim, canonical graph promotion, manuscript change or formal proof.
NS-R3: NOT PROVED. Terminal obstruction: UNCHANGED.

The new exclusions concern two live kinetic mechanisms, not the kinetic
programme as a whole. Section 3 applies to actual, faithfully prepared
renormalized Boltzmann families, rather than arbitrary kinetic snapshots.
Section 4 concerns a forced linear response operator, NOT an unforced NS
solution or the actual nonlinear Boltzmann remainder. These premise classes
must not be combined or silently enlarged.

## 1. Terminal gate and architecture decisions

For solenoidal Schwartz u0 on R3 and fixed nu>0, LOCAL, ENERGY and
CONTINUATION close NS-R3 once an input-only finite-horizon L-infinity_t L3_x
bound for the classical branch is available. KPC and KCH give the alternative
suffix through one correctly prepared GSR Leray limit and K_res. The exact
nonlinear estimate remains missing; neither representation is a reduction
of the difficulty of that estimate.

Three structurally different mechanisms were attacked.

**Retarded kinetic stress / nonlinear dual observability (K1/K2).** If the
actual signed remainder output satisfies K_res, the already specified GSR,
weak--strong identification and continuation suffix proves NS-R3. The first
attempt was to close its output pairing using only a collision-dissipation
L2 stress budget and the causal propagator. Section 4 proves that the
limiting Stokes output map is unbounded in exactly those norms, even with
symmetric trace-free stress, zero initial response, fixed viscosity and
sources supported away from the initial time. Its dual formulation is the
same failed norm estimate, not a different architecture. This rules out an
L2-only black-box response argument, not a signed estimate restricted to
the genuine nonlinear source in KPC Section 3. Taking the hydrodynamic limit
of that source retains the convection term; no arbitrary-data bound on it
was obtained.

**Transport-coupled information (KF).** Section 2 gives a direct consumer:
a uniform bound for two transported relative Fisher quantities would give
H1 control of the truncated momentum, hence K_res and NS-R3. There is no
additional unknown moment or density lower bound in this consumer. The
attempt was to combine exact transport commutation with collision
monotonicity. Section 3 refutes both the single-clock multiplicative estimate
and the two-clock monotonicity needed by this proposed producer, on the
actual prepared kinetic class and already within a smooth fluid lifespan.
This is stronger than the old free-transport warning and instantaneous
Maxwellian concentration test. It does not rule out a nonmonotone information
estimate with genuinely controlled production.

**Stochastic deformation / geometric rigidity.** The next different attack
was an averaged deformation estimate, rather than kinetic dissipation.
Bounding the pullback by its absolute matrix norm returns an exponential
of accumulated strain; retaining its sign leaves an uncontrolled matrix
potential. No input-only estimate for that potential was proved. The older
intrinsic-record route likewise still needs a restriction excluding its
known viscous-mixing Euler-shear limits. Neither a new name for the matrix
norm nor another tangent selection supplies that restriction. No new theorem
or broader exclusion is claimed for these mechanisms; the existing scoped
falsifiers remain in force. They were not developed into another functional
or documentation-only candidate.

The durable change is the precise exclusion of the kinetic inference steps
proved below. It is not a smaller terminal obstruction.

## 2. The information mechanism would really close the terminal edge

Fix the whole-space hard-sphere scaling and preparation in KPC/KCH:

    epsilon^2 partial_t F_epsilon + epsilon v.grad_x F_epsilon
        = Q_nu(F_epsilon,F_epsilon),
    F_epsilon(0,x,v) = M(v-epsilon u0(x)),
    M(v) = (2 pi)^(-3/2) exp(-|v|^2/2).

Write G_epsilon=F_epsilon/M and let gamma be the fixed density truncation
from GSR (2.40). Put b(z)=(z-1)gamma(z). The moment used in the contract is

    m_tilde_epsilon = epsilon^(-1) P integral v b(G_epsilon) M dv.

Here P is the spatial Leray projection. Since 2 sqrt(z) b'(z) is bounded,
Gaussian Cauchy--Schwarz, followed by the L2 boundedness of P, gives

    ||grad m_tilde_epsilon||_2
       <= C epsilon^(-1) I_x(F_epsilon)^(1/2),
    I_x(F) := 4 integral M |grad_x sqrt(G)|^2 dx dv.

Indeed grad b(G)=2 sqrt(G)b'(G) grad sqrt(G); the remaining Gaussian moment
is integral |v|^2 M dv=3. The entropy argument already in KPC gives

    ||m_tilde_epsilon||_2 <= C (H(F_epsilon|M)/epsilon^2)^(1/2).

Consequently Sobolev and interpolation yield the global-in-space estimate

    ||m_tilde_epsilon||_3
      <= C (H(F_epsilon|M)/epsilon^2)^(1/4)
             (I_x(F_epsilon)/epsilon^2)^(1/4).             (2.1)

These inequalities extend by approximation when their right sides are
finite. There is no division by the local particle density and no estimate
for an untruncated raw moment is being assumed.

For a fixed time offset c, define

    D_c(t) = grad_v + ((t+c)/epsilon) grad_x,
    J_c,epsilon(t) = integral F_epsilon |D_c(t) log G_epsilon|^2 dx dv
                  = 4 integral M |D_c(t) sqrt(G_epsilon)|^2 dx dv. (2.2)

The square-root expression is the definition in the weak class, with value
infinity if the indicated distributional derivative is not in L2(M dx dv).
The offsets have time units; fix any c>0, independent of epsilon. Then

    I_x(F_epsilon)/epsilon^2
       <= (2/c^2)(J_0,epsilon + J_c,epsilon).              (2.3)

Thus an input-only, epsilon-uniform bound for this sum on each (delta,H),
combined with the entropy inequality, gives an unsmoothed L-infinity L3
bound for m_tilde, stronger than K_res. The GSR Leray identification,
weak--strong uniqueness, LOCAL and CONTINUATION then prove NS-R3. This is
the full consumer chain, not a claim that such a bound has been proved.

For the prescribed shifted Maxwellian, direct Gaussian integration gives

    J_c,epsilon(0) = epsilon^2 ||u0||_2^2 + c^2 ||grad u0||_2^2,
    J_0,epsilon(0) + J_c,epsilon(0)
        = 2 epsilon^2 ||u0||_2^2 + c^2 ||grad u0||_2^2.    (2.4)

The cross term vanishes because v-epsilon u0 has zero mean. Also
[partial_t+epsilon^(-1)v.grad_x,D_c(t)]=0. For free transport G(t,x,v)
=G(0,x-tv/epsilon,v), change of variables therefore preserves each J_c
exactly. It was plausible to seek collision monotonicity as the missing
producer. The next section shows precisely why that inference is false.

## 3. A prepared-family lower bound that falsifies the Fisher producers

### 3.1 Lower semicontinuity on an actual hydrodynamic sequence

Use one GSR-convergent subsequence for the preparation above, on a compact
classical fluid interval. Set

    w_epsilon = (sqrt(G_epsilon)-1)/epsilon,
    g_epsilon = (G_epsilon-1)/epsilon
              = 2 w_epsilon + epsilon w_epsilon^2.

The scaled entropy inequality bounds w_epsilon in L-infinity_t L2(M dx dv).
In particular epsilon w_epsilon^2 -> 0 in L1 on each finite time interval,
including the whole spatial and velocity domains. The weak L2 limit of
w_epsilon is therefore g/2, where GSR identifies

    g(t,x,v) = u(t,x).v + theta(t,x)(|v|^2-5)/2.

Only the velocity component is needed. The prepared energy/trace conclusion
of GSR makes u a Leray velocity, and weak--strong uniqueness identifies it
with the classical branch on this interval. No regularity of that branch
beyond its input-derived local lifespan is assumed.

By (2.2),

    J_c,epsilon = 4 ||epsilon grad_v w_epsilon
                         +(t+c) grad_x w_epsilon||^2_{L2(M dx dv)}.

In distributions, epsilon grad_v w_epsilon -> 0, and the expression inside
the norm tends to (t+c)grad_x g/2. For the first assertion integrate by
parts against a compact velocity test; differentiating M introduces only
-v M, so the entropy L2 bound supplies the factor epsilon. The second
assertion follows directly from weak convergence of w_epsilon.

Let eta>=0 be a smooth compactly supported time test in the classical
interval. Weak lower semicontinuity gives

    liminf_epsilon integral eta(t) J_c,epsilon(t) dt
      >= integral eta(t)(t+c)^2
                      integral M |grad_x g|^2 dx dv dt
      >= integral eta(t)(t+c)^2 ||grad u(t)||_2^2 dt.      (3.1)

If the left side is infinite the assertion is immediate; otherwise a
bounded-derivative subsequence and distributional identification prove it.
One can first restrict to compact x,v sets and then exhaust them. The last
inequality uses integral v_i v_j M=delta_ij and the odd/even orthogonality
of the velocity and thermal modes. It does not require setting theta=0.
For sums of J's the same argument applies in the direct-sum Hilbert space.

This proof differentiates neither a renormalized moment equation nor the
Boltzmann solution in time. It needs only the established entropy bound and
the stated hydrodynamic convergence. It does not exchange epsilon with a
spatial-resolution limit or assert pointwise-in-time kinetic convergence.

### 3.2 No uniform multiplicative propagation of the zero-offset clock

Take any nonzero datum and a sufficiently short positive interval I within
its classical lifespan, so Y(t)=||grad u(t)||_2^2 stays positive there.
For c=0, (3.1) implies

    liminf_epsilon integral_I J_0,epsilon(t) dt
                 >= integral_I t^2 Y(t) dt > 0,          (3.2)

where the interval version follows by increasing compact time tests.
But J_0,epsilon(0)=epsilon^2 ||u0||_2^2 -> 0. Hence no estimate

    sup_{t in I} J_0,epsilon(t)
                  <= C(u0,nu,I) J_0,epsilon(0)           (3.3)

with C independent of epsilon can hold on this prepared class. The same
contradiction holds for an integrated version of (3.3). In particular both
monotonicity and a Knudsen-uniform multiplicative Gronwall estimate are
false. This is an order-one versus order-epsilon-squared discrepancy on an
already smooth fluid interval, not a hypothetical singularity.

The interval can be placed after a smaller input-derived local initial
layer. Omitting t=0 from the desired OUTPUT interval does not repair a
multiplicative estimate whose right side is still J_0,epsilon(0).
An additive production term of order one is not ruled out.

### 3.3 The two-clock monotonicity that would close the theorem is also false

Suppose the sum in (2.3) were nonincreasing for every prepared family.
Equations (2.4) and (3.1), tested with arbitrary eta, would imply

    W_c(t) Y(t) <= c^2 Y(0),
    W_c(t) := t^2+(t+c)^2,                               (3.4)

almost everywhere in each local classical interval. Smoothness makes the
left side continuous, so the inequality would hold at every such time.
We construct admissible data for which its derivative at zero is positive.

Choose a nonzero solenoidal Schwartz phi. Set u0(x)=a phi(kappa x), with
kappa>0 sufficiently small that

    nu ||Delta u0||_2^2 <= Y(0)/(4c),

which is possible since the ratio ||Delta phi(kappa .)||_2^2 /
||grad phi(kappa .)||_2^2 is kappa^2 times the original ratio. Next choose
a>0 sufficiently small that ||grad u0||_infinity<=1/(4c). The exact
classical enstrophy identity and its elementary stretching bound give

    Y'(0) = -2 nu ||Delta u0||_2^2 + 2 integral omega0.S0 omega0
           >= -Y(0)/c,

because |integral omega0.S0 omega0|<=||grad u0||_infinity Y(0).
Since W_c(0)=c^2 and W_c'(0)=2c,

    (W_c Y)'(0) >= c Y(0) > 0.                           (3.5)

This contradicts (3.4) on a nonempty positive time interval. All data here
are legitimate fixed whole-space data for fixed nu and c. No periodic
parent, variable viscosity, external force or singular NS solution is used.

The result excludes the proposed nonincreasing sum, not every bound on the
sum with a larger input-only right side. Such a nonmonotone bound could
still close the theorem by Section 2, but it needs a new production estimate.
The homogeneous velocity-Fisher theorem supplies neither (3.3) nor (3.4).

## 4. The causal stress map cannot upgrade an L2 collision budget to K_res

This section has a different premise class. Fix nu>0 and 0<delta<H. For a
smooth symmetric trace-free tensor Sigma, define the zero-initial response

    V_Sigma(t) = integral_0^t exp(nu(t-s)Delta) P div Sigma(s) ds. (4.1)

There is no constant depending only on nu,delta,H such that

    ||V_Sigma||_{L-infinity(delta,H;L3)}
                    <= C ||Sigma||_{L2((0,H) x R3)}.     (4.2)

The failure persists for stresses supported strictly inside (delta,H), and
with uniform energy-class bounds for the response.

Choose a real Schwartz phi whose Fourier transform is supported away from
zero and nonzero near xi=(1,1,0), together with its reflected support.
Let S=diag(1,-1,0), and choose a nonnegative, nonzero smooth chi supported
in (-1,-1/2). Define Sigma(s,x)=chi(s)S phi(x). Its causal response V is
zero before time -1. At time 0 its Fourier transform is

    V_hat(0,xi) = i P(xi)S xi phi_hat(xi)
                         integral chi(s) exp(nu s |xi|^2) ds.

It is not zero: at xi=(1,1,0), S xi is nonzero and perpendicular to xi.
The Fourier supports avoid zero, so all the spatial profiles in this
construction are Schwartz, with finite required norms.

Fix t_c in (delta,H). For lambda sufficiently large put

    Sigma_lambda(t,x)
        = lambda^(5/2) Sigma(lambda^2(t-t_c),lambda x),
    V_lambda(t,x)
        = lambda^(3/2) V(lambda^2(t-t_c),lambda x).

Differentiation verifies (4.1) exactly, with zero initial response. Changing
variables gives

    ||Sigma_lambda||_{L2((0,H) x R3)} = ||Sigma||_2,
    ||V_lambda(t_c)||_3 = lambda^(1/2) ||V(0)||_3 -> infinity. (4.3)

Also ||V_lambda||_{L-infinity L2} and ||grad V_lambda||_{L2_t,x} are bounded
independently of lambda. For example the Stokes energy estimate gives

    sup_t ||V_lambda(t)||_2^2
          + nu integral ||grad V_lambda||_2^2
                  <= 2 nu^(-1) ||Sigma_lambda||_2^2.

These are forced-response estimates; the unforced zero-data energy identity
would of course force V=0 and is NOT a premise of this counterexample.

The precise resolution test also fails. For lambda=2^j and the compact
mollifiers S_J of KPC, fix L sufficiently large that S_L V(0) is nonzero.
Then

    ||S_(j+L) V_lambda(t_c)||_3
          = lambda^(1/2) ||S_L V(0)||_3.                 (4.4)

Thus permitting fixed-resolution smoothing does not produce a uniform-J
operator bound. This is not an exchange of epsilon and J limits: it is a
counterexample to the proposed limiting response estimate itself.

### Microscopic realization of the stress norm, and the dual test

Let A(v)=v tensor v-|v|^2 I/3 and K_Sigma(x,v)=(1/2)Sigma(x):A(v).
Gaussian fourth moments give

    Pi K_Sigma = 0,     integral A K_Sigma M dv = Sigma.

For the fixed hard-sphere linearized collision operator L_nu,

    integral K_Sigma L_nu K_Sigma M dv <= C_nu |Sigma|^2.

This uses only the finite-dimensional space of quadratic stress polynomials;
the defining hard-sphere Gaussian integrals are finite. Hence the stress
packets remain bounded in the corresponding microscopic dissipation norm.
They are not asserted to solve the nonlinear kinetic remainder equation or
to be positive kinetic densities. This rules out a norm-only transfer step,
not a trajectory-specific estimate. The trace-free microscopic restriction
and a fixed Hermite stress space do not fix that norm-only step.

For a smooth compact spacetime vector test varphi, set

    z_varphi(s) = integral_s^H exp(nu(t-s)Delta) P varphi(t) dt.

Then <V_Sigma,varphi>=-<Sigma,sym grad z_varphi>; the trace term vanishes
since z_varphi is solenoidal. If

    ||sym grad z_varphi||_2 <= C ||varphi||_{L1_t L^(3/2)_x},

held, Cauchy--Schwarz and duality would prove (4.2), contradicting (4.3).
Thus writing the same budget as an adjoint observability estimate does not
repair it. No claim is made against specially weighted nonlinear adjoints
whose additional terms have independently controlled signs and constants.

## 5. Self-review, source scope and exact remaining obligations

The main counterexample in Section 3 uses actual hydrodynamic families and
an exact local NS enstrophy identity. Its proofs survive an initial-layer
allowance, weak (rather than pointwise) convergence, thermal modes, and the
whole-space background. The stress example instead has an external tensor
source. It is not evidence of NS blow-up, not a kinetic solution, and not
a falsification of all signed stress-memory mechanisms. Constants depending
on the actual nonlinear source beyond its L2 budget are not excluded.

GSR was checked directly at Theorem 2.4, equations (2.23)--(2.27) and the
following prepared-energy paragraph, and Proposition 7.2 (rendered PDF pages
8--9 and 41, with the paragraph continuing on page 10): F. Golse and
L. Saint-Raymond, *The incompressible Navier--Stokes limit of the Boltzmann
equation for hard cutoff potentials*, J. Math. Pures Appl. 91 (2009), 508--552,
https://arxiv.org/abs/0808.0039 . Its solution class is renormalized, its
spatial domain R3, and its limiting conclusion is Leray/NSF, not global
classical regularity. The canonical LOCAL/ENERGY/CONTINUATION interfaces
remain as recorded in docs/proof-graph.yaml. No new imported theorem is
needed for the scaling construction or the lower-semicontinuity argument.

The homogeneous Fisher scope was compared with C. Villani, *Fisher
information in kinetic theory*, arXiv:2501.00925v5, abstract and kinetic
setup, https://arxiv.org/html/2501.00925v5 . No inhomogeneous Fisher theorem
is imported, and no claim of novelty or exhaustive prior-art review is made.

Exactly one new arbitrary-data producer is still needed: K_res (or another
estimate with a complete critical continuation consumer) on the genuine
prepared trajectory. K1 must control its true signed nonlinear source,
not arbitrary stress via an L2 norm. KF must bound actual information
production nonmonotonically or use a different mechanism, not either of the
falsified propagation laws. After such a producer, finish the source
application/truncation audit and the already specified identification suffix.
MIC-R3's extra particle-class, whole-space and scaling/observable obligations
remain separate. No microscopic bridge is required merely to close NS-R3.

The kinetic programme, all valid earlier estimates, and all scoped previous
no-gos are preserved. No new terminal reduction or successful architecture
is claimed. Independent mathematical review remains outstanding.
