# Terminal tests: instantaneous vorticity closure, nonlocal pressure, and helicity selection

Date: 2026-09-06.
Frozen research input: `3ef911def6d0aab6ece6300e430d0b18e6b38993`.
Status: complete author derivations; independent mathematical audit pending.
Terminal theorem: not proved. Terminal obstruction: unchanged.
No novelty or priority claim. No graph-node promotion.

## 1. Terminal gate and the mechanisms actually tested

The target is NS-R3, for the original unforced equation on R3, every fixed
positive viscosity nu, and every solenoidal Schwartz datum. LOCAL supplies
the maximal classical branch and its finite-time H1 blow-up alternative.
ENERGY and CONTINUATION supply the already-established terminal suffix
once an input-derived uniform L3 bound is proved on every finite horizon.

This note tests mechanisms different from the retired pressure-work and
quotient programme. It does not promote a new conditional criterion.

**Maximum-vorticity comparison.** Write Omega(t)=||curl u(t)||_infinity.
A scalar-input Osgood upper bound, for example

    D^+ Omega <= C(nu,E0,Y0) Omega log(e+Omega),

would bound Omega on every finite interval. More generally the same holds
for a positive comparison function g with integral_1^infinity 1/g = infinity.
The closing implication does not require an additional unknown norm:
with E=||u||_2^2, Y=||grad u||_2^2, Z=||Delta u||_2^2,

$$
 Y'+2\nu Z=2\int\omega\cdot((\omega\cdot\nabla)u)
       \le2\Omega\|\omega\|_2\|\nabla u\|_2=2\Omega Y.       \tag{1}
$$

Thus Y(t)<=Y0 exp(2 integral_0^t Omega), contradicting LOCAL at a finite
maximal time; LOCAL and ENERGY finish NS-R3. Theorem A rules out this
scalar-input instantaneous producer, even after exact energy and enstrophy
are supplied. It does NOT rule out a comparison bound depending on the
full initial datum or on additional controlled spatial information.

**Local pressure self-damping.** A second attempt was to bound positive
stretching alpha=xi dot S xi, where xi=omega/|omega| and S=sym grad u,
by a local Riccati damping rule. An input-controlled bound for its positive
spatial supremum would give, at vorticity maxima, D^+ Omega<=sup(alpha)_+
Omega, and then (1). Section 4 tests the hardest proposed local inference:
can the pressure contribution have a forced damping sign, or be bounded
by the local velocity jet? It cannot. This excludes a pointwise local law,
not a law restricted to specially selected global stretching maxima or a
nonlocal spacetime argument.

**High-frequency helicity coercivity.** Uniform dominance of one helical
sign above an input-chosen finite cutoff would turn the exact helicity
balance into a critical H1/2 bound; Section 5 gives the complete implication
to L3 and NS-R3. An invariant symmetry of actual NS, however, prevents that
dominance at every frequency on an entire class of admissible trajectories.
This is not merely a zero-total-helicity snapshot.

The mathematical change is the exclusion of those precisely specified
producers. No input-only terminal bound or strictly weaker remaining
terminal theorem is obtained.

## 2. Theorem A: identical scalar inputs, unbounded initial vorticity growth

**Theorem A.** Fix nu>0. There exist constants E_*,Y_*,gamma>0, one compact
set K, and smooth compactly supported solenoidal odd data u_(0,N), N>=1,
such that

$$
 \|u_{0,N}\|_2^2=E_*,\qquad
 \|\nabla u_{0,N}\|_2^2=Y_*,\qquad
 \|\omega_{0,N}\|_\infty=1.                                 \tag{2}
$$

Every datum is supported in K and the velocities have a uniform L-infinity
bound. In a neighbourhood of the origin, omega_(0,N)=e3 exactly. On the
ACTUAL local classical NS solution of viscosity nu from each datum,

$$
 \liminf_{t\downarrow0}\frac{\|\omega_N(t)\|_\infty-1}{t}
                            \ge\gamma N.                    \tag{3}
$$

All spatial vorticity derivatives, including its Laplacian, vanish at
this maximum at time zero. The direction is perfectly coherent there.
The neighbourhood radius is not uniform in N. The data vary with N;
this is not a singular solution from one fixed datum.

### 2.1 A compact strain with annular vorticity

Let H=diag(-1/2,-1/2,1), and set

$$
 A(x)=(-x_2x_3/2,x_1x_3/2,0),\qquad \nabla\times A=Hx.
$$

Choose a smooth radial chi equal to one on B1 and zero outside B2. Put
W=curl(chi A). It is odd, compactly supported and solenoidal, and equals
Hx on B1. Consequently curl W is supported in the annulus 1<=|x|<=2.
Let C=||curl W||_infinity>0 and gamma=1/(4C). For r>0 put

$$
 W_r(x)=rW(x/r).
$$

Its gradient is H on Br, while its vorticity is confined to r<=|x|<=2r
and has supremum C. These assertions concern exact compactly supported
fields, not affine infinite-energy solutions.

### 2.2 A rotation core whose global vorticity maximum is known

Choose a nonnegative smooth g compactly supported in (0,4), with integral
one and g<=1. Define f(r)=1 for r<=1 and

$$
 f(r)=1-\int_0^{\log r}g(s)\,ds\quad(r>1),\qquad R=e^4.
$$

Then f=0 for r>=R, 0<=f<=1, and -1<=rf'(r)<=0. All joins are smooth.
Define

$$
 V(x)=\tfrac12 f(|x|)(-x_2,x_1,0).
$$

This is odd, solenoidal and compactly supported in BR. It has vorticity
e3 on B1. Writing c=x3/|x|, direct differentiation gives

$$
 |\nabla\times V|^2
 =f^2c^2+(f+rf'/2)^2(1-c^2)\le1.                             \tag{4}
$$

Indeed |f|<=1 and -1/2<=f+rf'/2<=1. Thus the vorticity supremum is
EXACTLY one, including in the cutoff region. Let V_epsilon(x)=epsilon
V(x/epsilon); its vorticity has the same supremum and equals e3 on
B_epsilon.

### 2.3 Nested strains and the central maximum

Take r0>0, to be fixed small below, and set

$$
 r_k=r_0 4^{-(k-1)},\qquad \epsilon_N=r_N/(4R),\qquad
 C_N=\gamma\sum_{k=1}^N W_{r_k}+V_{\epsilon_N}.                \tag{5}
$$

The strain-vorticity annuli are mutually disjoint, and the rotation core
is supported inside B_(r_N/4), disjoint from all those annuli. Thus
||curl C_N||_infinity=1; outside the rotation core each nonzero vorticity
contribution has size at most 1/4. The velocity supports of the nested
strains DO overlap; they are not being incorrectly treated as disjoint.

Near zero C_N is the affine field

$$
 C_N(x)=(\gamma NH+K_0)x,\qquad
 K_0=\begin{pmatrix}0&-1/2&0\\1/2&0&0\\0&0&0\end{pmatrix}.   \tag{6}
$$

In particular C_N(0)=0, omega=e3, grad omega=Delta omega=0, and
(omega dot grad)C_N=gamma N e3 there.

The energy is bounded uniformly by a small quantity. Scaling and the
triangle inequality give

$$
 \|C_N\|_2\le
 \frac{\gamma\|W\|_2r_0^{5/2}}{1-4^{-5/2}}
       +\|V\|_2(r_0/(4R))^{5/2}.                             \tag{7}
$$

The solenoidal div-curl identity and disjoint VORTICITY supports give

$$
 Y(C_N)=\gamma^2Y(W)\sum_{k=1}^N r_k^3+\epsilon_N^3Y(V).
                                                                    \tag{8}
$$

Hence E(C_N)<=C_E r0^5 and Y(C_N)<=C_Y r0^3, with constants independent
of N and r0. Also ||C_N||_infinity is bounded by the analogous convergent
sum of r_k. All central fields are supported in B_(2r0).

### 2.4 Exactly matching energy AND enstrophy

Uniform bounds alone would not exclude a pathological scalar function
with different finite values on different inputs. We therefore match the
inputs exactly.

Put delta=1/8, L1=1, L2=2. Choose fixed centres plus/minus a1 and plus/minus
a2 so the four balls of radii R Lj are mutually disjoint and avoid B2.
Let

$$
 R_j(x)=\delta L_j\{V((x-a_j)/L_j)+V((x+a_j)/L_j)\}.
$$

Each R_j is odd and solenoidal, with vorticity supremum at most delta.
Disjointness within each pair yields

$$
 E_j=E(R_j)=2\delta^2L_j^5E(V),\qquad
 Y_j=Y(R_j)=2\delta^2L_j^3Y(V).
$$

The matrix M with columns (E1,Y1) and (E2,Y2) is invertible, because
Yj/Ej=L_j^(-2)Y(V)/E(V) takes two different values. Set
E_*=E1+E2 and Y_*=Y1+Y2, and define positive coefficients by

$$
 \binom{a_N^2}{b_N^2}
   =\binom{1}{1}-M^{-1}\binom{E(C_N)}{Y(C_N)}.                    \tag{9}
$$

Choose r0<1 sufficiently small using (7)--(8). Uniformly in N, both
entries of (9) then lie in [3/4,5/4]. Finally put

$$
 u_{0,N}=C_N+a_NR_1+b_NR_2.                                  \tag{10}
$$

The three terms now have disjoint VELOCITY supports, so (9) proves the
two exact identities in (2). Reservoir vorticity has magnitude at most
sqrt(5/4)/8<1, so the vorticity maximum is still exactly one. The reservoirs
vanish near zero and change none of (6). The union of their fixed supports
and B2 is a common compact K, and the coefficients are uniformly bounded.
This proves every asserted property of the data, including oddness and
the uniform velocity bound.

### 2.5 Testing the actual NS generator

LOCAL gives a classical solution from each (10), with the prescribed,
unchanged positive viscosity. Curling the actual equation yields

$$
 \partial_t\omega+u\cdot\nabla\omega
               =(\omega\cdot\nabla)u+\nu\Delta\omega.
$$

At (x,t)=(0,0), (6) therefore gives

$$
 \partial_t\omega_N(0,0)=\gamma N e_3.                       \tag{11}
$$

LOCAL justifies the time derivative, so
|omega_N(0,t)|=1+gamma Nt+o(t). Since the global supremum is at least this
value and its initial value is one, (3) follows. No differentiability of
the spatial maximum, or persistence of its location, has been assumed.
This completes the proof of Theorem A.

## 3. Exact scope of the instantaneous exclusion

There is no function F, finite at (nu,E_*,Y_*,1), for which the pointwise
upper-right-Dini estimate

$$
 D^+\Omega(t)\le F(\nu,E(t),Y(t),\Omega(t))                   \tag{12}
$$

holds at every classical state of every admissible NS branch. Evaluate it
at t=0 in Theorem A and let N increase. Including the initial scalar
values E0,Y0 as additional arguments does not help; they too are identical.

There is also no LOCALLY BOUNDED F of those scalar variables for which
(12) is asserted only almost everywhere on the initial classical
interval. E,Y and Omega are continuous there and Omega is locally
Lipschitz: LOCAL bounds the time derivative of vorticity in L-infinity
on each compact classical interval. Fix a neighbourhood of the common
initial scalar tuple and a finite bound B for F on it. For each N the
trajectory remains in that neighbourhood for some positive, possibly
N-dependent interval. Integration would give Omega(t)<=1+Bt there,
contradicting (3) when gamma N>B. The exclusion is not an artifact of
requiring a derivative inequality exactly at the initial time.

This eliminates, in particular, scalar-input Osgood producers in Section 1
and bounds on the stretching at a vorticity maximum from only E,Y,Omega
and the local spatial vorticity jet. At the exhibited maximum the latter
jet is identical for all N, but xi dot S xi=gamma N. Even all derivatives
of the vorticity vanish. Local directional coherence without its spatial
scale and nonlocal contribution is insufficient.

It also disproves a proposed strictly positive local Laplacian depletion
at such a maximum based only on those inputs: Delta omega=0 there. The
ordinary Laplacian must not be substituted into a strictly fractional
nonlocal maximum principle without checking the order restriction.

These are NOT exclusions of full-datum estimates, high-derivative initial
constants, bounds tracking a controlled coherence radius, or nonlocal
time-integrated depletion. The coherent ball shrinks with N. Large
initial growth need not persist for an N-independent time. No finite-time
NS blow-up, failure of a full-input bound, or uniform existence-time
statement is inferred from (3).

## 4. A separate pressure test: the full local velocity jet does not close

Theorem A leaves the local strain itself free. A proposed repair might
track that strain and assert that pressure must damp it. The following
construction holds the entire LOCAL VELOCITY FIELD fixed instead. Its
global energy and enstrophy are not asserted to be fixed; do not combine
its premises with (2).

Fix a>0 and M0=aH+K0. On B1 prescribe U(x)=M0x. A compact solenoidal
extension is

$$
 U=\nabla\times\{\chi(x)[-\tfrac13x\times(M_0x)]\}.           \tag{13}
$$

Here curl[-x cross(M0x)/3]=M0x because tr M0=0. Near zero, omega=e3,
S=aH, xi=e3 and alpha=xi dot S xi=a; all spatial derivatives of omega and
S vanish. Thus even alpha is constant on a neighbourhood.

Let G(x)=1/(4pi|x|), the fundamental solution of -Delta. For a compact
solenoidal B supported away from U, the canonical NS pressures add:

$$
 p_{U+LB}=p_U+L^2p_B,\qquad
 p_B=\partial_i\partial_jG*(B_iB_j).                         \tag{14}
$$

This follows because the velocity supports are disjoint, so the quadratic
stress has no cross terms. It is not the addition of an arbitrary
harmonic pressure gauge.

Use the radial swirl V of Section 2.2. Symmetry gives

$$
 \int V_iV_j=\operatorname{diag}(m,m,0),\qquad m>0.
$$

For b outside the support of U set B_(eta,b)(x)=V((x-b)/eta). For small
eta its support is disjoint from U. Differentiating the smooth exterior
kernel and changing variables gives

$$
 \eta^{-3}\partial_{33}p_{B_{\eta,b}}(0)
       \longrightarrow-m\partial_{3333}G(b).                \tag{15}
$$

Indeed the limiting contraction is
m(partial_3311+partial_3322)G(b)=-m partial_3333G(b), because G is
harmonic away from zero. All derivatives in this limit are evaluated a
positive distance from the compact integration support.

Writing c=b3/|b|, direct differentiation gives

$$
 \partial_{3333}G(b)
     =\frac{105c^4-90c^2+9}{4\pi|b|^5}.                     \tag{16}
$$

Choose a fixed d>2. At b=d e3 this is 6/(pi d^5)>0; at
b=d(e1+e3)/sqrt(2) it is -39/(16pi d^5)<0. For sufficiently small fixed
eta the actual, not just limiting, pressure contributions in (15) have
opposite nonzero signs. Varying the amplitude L and choosing one of the
two locations therefore makes the total partial_33 p(0) in (14) any
prescribed real number. Every spatial velocity jet on B1 stays unchanged.

To see the dynamical consequence on the ACTUAL local NS solution, use
A=grad u, K=skew A and the material derivative D_t. Differentiating the
momentum equation gives

$$
 D_tA=-A^2-\nabla^2p+\nu\Delta A,\qquad
 D_tS=-S^2-K^2-\nabla^2p+\nu\Delta S.                       \tag{17}
$$

At the initial origin, the vorticity equation gives D_t omega=a e3,
hence D_t xi=0. Also K0e3=0 and Delta S=0. Consequently

$$
                  D_t\alpha(0,0)=-a^2-\partial_{33}p(0,0).   \tag{18}
$$

Its value is arbitrarily positive or negative with exactly the same local
velocity field, local vorticity direction, viscosity, and positive alpha.
The exterior pressure is harmonic on B1 but its Hessian is not determined
by the local Poisson source; knowing that source fixes only its trace.

Thus no universal finite upper bound for this initial material derivative
can depend ONLY on the local spatial velocity jet. In particular the
pressure does not supply an automatic pointwise Riccati self-damping law
from those local data. This statement is restricted to that pointwise
inference. The origin is not asserted to be a GLOBAL maximum of alpha,
and the theorem does not exclude rules using global-maximum selection,
remote geometry, global initial norms or time-integrated pressure control.

## 5. Helical coercivity: a complete closing implication and an invariant obstruction

Use the unitary Fourier transform and the transverse Leray symbol P(xi).
For xi nonzero define the helical projections

$$
 P_\pm(\xi)=\tfrac12\left(P(\xi)\pm\frac{i\xi\times}{|\xi|}\right),
 \qquad a_\pm(\xi,t)=|P_\pm(\xi)\widehat u(\xi,t)|^2.
$$

They are orthogonal Hermitian projections on the transverse plane, so
a_++a_-=|u-hat|^2. Define

$$
 Q=\int|\xi|(a_++a_-)=\|u\|_{\dot H^{1/2}}^2,\qquad
 h=\int u\cdot\omega=\int|\xi|(a_+-a_-).
$$

### 5.1 What would have closed the theorem

The precise selection claim tested was this: for each input and finite
horizon H, choose finite K>=0, kappa>0 and a fixed sign sigma in {+1,-1}
from those inputs, such that throughout the classical branch up to H,

$$
 \sigma(a_+-a_-)\ge\kappa(a_++a_-)
             \quad\hbox{for almost every }|\xi|>K.           \tag{19}
$$

This allows arbitrary unpolarized low modes and requires only strict
dominance, not a pure one-handed field, at high frequencies.

For actual smooth NS the exact helicity identity is

$$
 h'=-2\nu\int|\xi|^3(a_+-a_-).                              \tag{20}
$$

To derive it, differentiate integral u dot curl u, integrate curl by
parts, and use the Lamb identity: the nonlinear contribution is a gradient
paired with omega plus a multiple of (u cross omega) dot omega, both zero.
The viscous term gives (20) by Fourier transformation. LOCAL justifies
these operations on compact classical intervals.

If (19) held, its high-frequency contribution to sigma h' would be
nonpositive. The low-frequency part has absolute value at most
2nu K^3 E0. Hence

$$
 \sigma h(t)\le |h(0)|+2\nu K^3E_0H.
$$

On the other hand sigma h(t)>=kappa Q_(>K)(t)-K E0, and
Q_(<=K)(t)<=K E0. Therefore

$$
 Q(t)\le KE_0+\kappa^{-1}
       \{ |h(0)|+KE_0+2\nu K^3E_0H\}.                       \tag{21}
$$

The homogeneous Sobolev inequality ||u||_3^2<=C Q, followed by
CONTINUATION, LOCAL and ENERGY, gives NS-R3. This is the explicit terminal
implication for the mechanism, not a new approved conditional theorem.

### 5.2 Why the selection claim is false for the original equation

Suppose u0 is real and odd: u0(-x)=-u0(x). Orthogonal invariance of NS and
LOCAL uniqueness imply

$$
                         u(-x,t)=-u(x,t)                    \tag{22}
$$

throughout its classical lifespan. The symmetry used is u(x,t) mapped
to -u(-x,t), NOT velocity sign reversal without spatial reflection.

Reality and oddness imply u-hat=i b for a real transverse vector b at
almost every frequency. Explicitly,

$$
 P_\pm\widehat u=\tfrac12(ib\mp\widehat\xi\times b),
 \qquad
                a_+=a_-=\tfrac12|\widehat u|^2.              \tag{23}
$$

Thus the two helical energies agree pointwise in frequency at EVERY
classical time, including after every high-frequency truncation. In
physical space, zero total helicity also follows because u is odd and
omega even, but that weaker observation is not the assertion in (23).

The data constructed in Theorem A are nonzero, odd, compactly supported
and admissible. A nonzero compactly supported smooth field cannot be
band-limited: its Fourier transform extends to an entire function, and
vanishing on an open exterior region would make it identically zero.
Consequently Q_(>K)(0)>0 for every finite K. Equation (23) contradicts
(19) for any kappa>0 and either sign, regardless of how K depends on the
full datum. By continuity in H1, the nonzero high-frequency tail persists
on a short positive interval for each fixed K; the failure is not
confined to the initial slice.

More generally (23) prevents any spontaneous strict helical dominance
on an odd branch wherever a nonzero high-frequency tail is present.
No theorem about absence of exact band-limitation at all later times is
needed or asserted. Nor is a theorem about polarization of local blow-up
tangents inferred from this global parity argument.

Retire automatic global high-frequency handedness as an arbitrary-data
producer. Do not transfer the positive-helicity coercivity of a projected,
helical-decimated equation to the original equation. Estimates that retain
both helical signs and control their actual cross-transfer, or that use
additional spatially localized hypotheses, are outside this exclusion.

## 6. Research disposition, attribution, and author checks

The scalar maximum-vorticity comparison route fails even on actual local
whole-space NS solutions at fixed viscosity, with EXACTLY matched E,Y and
maximum vorticity. Adding qualitative local direction coherence does not
repair it. Adding the full local velocity jet still does not determine a
pointwise self-damping pressure law. A structurally different spectral
route, automatic high-frequency sign-definite helicity, is excluded by an
exact invariant symmetry, not by a surrogate model or an assumed singular
limit.

Preserve all previous evidence and its stated qualifications. None of
these results removes a node from the terminal proof obligation. Full
momentum/vorticity evolution, controlled nonlocal spatial geometry,
full-datum estimates and nonmonotone spacetime mechanisms remain available.
They are not automatically promising merely because they are not excluded.
No new complete primary architecture has passed the terminal gate.

The remaining terminal obligation is unchanged: prove an input-derived
uniform L3 bound before every finite horizon for the actual fixed-input
branch, or directly contradict a finite maximal time. Do not replace that
obligation by proving another continuation criterion or by asserting a
rigidity/selection theorem not established here.

### Literature scope checked

The constructions and proofs above are supplied in this note; no external
regularity theorem is used to assert them. The closing suffix is the
repository's retained LOCAL, ENERGY and CONTINUATION package. Relevant
primary-source checks explain why nearby known mechanisms do not supply
an unconditional producer:

* P. Constantin and V. Vicol, *Nonlinear maximum principles for dissipative
  linear nonlocal operators and applications*, arXiv:1110.0179v1 (2011),
  published in Geometric and Functional Analysis 22 (2012), 1289--1321.
  Theorem 2.1 treats fractional orders strictly between zero and two; it
  does not assert the positive local-Laplacian depletion contradicted here.
  https://arxiv.org/abs/1110.0179 ; https://arxiv.org/html/1110.0179v1 .
* L. Biferale and E. S. Titi, *On the global regularity of a helical-decimated
  version of the 3D Navier--Stokes equations*, arXiv:1303.1215 (2013).
  The abstract explicitly describes a projected, sign-definite-helicity
  equation with periodic boundary conditions, not arbitrary solutions of
  the original whole-space equation. No theorem for that altered equation
  is imported here. https://arxiv.org/abs/1303.1215 .
* T. Y. Hou and Z. Shi, *Dynamic growth estimates of maximum vorticity for
  3D incompressible Euler equations and the SQG model*, Discrete and
  Continuous Dynamical Systems 32 (2012), 1449--1463. The source specifies
  additional geometric assumptions; its abstract is not an unconditional
  Navier--Stokes Osgood estimate.
  https://www.aimsciences.org/article/doi/10.3934/dcds.2012.32.1449 .

Author checks addressed: smooth solenoidal localization; the exact global
vorticity maximum including cutoff regions; disjoint vorticity versus
velocity supports; invertibility and positivity in the two-reservoir
matching; the fixed positive viscosity and actual NS generator; Dini and
almost-everywhere formulations; shrinking coherence scale and uncontrolled
higher initial derivatives; canonical rather than freely chosen pressure;
the two signs of its fourth-derivative kernel; no global-alpha-maximum
claim; the distinction between local spatial and temporal jets; the exact
reflection symmetry and helical projection algebra; the finite-cutoff
loophole; and all signs and low-frequency terms in (20)--(21).

Symbolic differentiation checked the strain potential, (16), and the
33-component of the symmetric square in (17); the proofs are the displayed
identities, not those checks. Independent mathematical audit remains
pending, especially for the scope of each excluded inference. No NS
blow-up, complete terminal proof, formal proof or novelty is claimed.
