# Remote pressure-Hessian control with every local velocity jet fixed

Date: 2026-09-08. Input main: `72b7fb1ab24428b522fb9637dc21582c0adcaaf2`.
Status: complete author derivation; independent mathematical audit PENDING.
Original unforced R3 NS, fixed nu>0, real compact smooth solenoidal data.
No regularity theorem, singular solution, or novelty claim is made.

## 0. Terminal relevance and the precise branch being tested

A pressure-based terminal producer would have to control the actual signed
critical production on every upper time, with a full-input bound, without
introducing an uncontrolled future pressure or strain norm. The reviewed
RF-q/Lorentz/continuation suffix would then imply NS-R3. No such producer
is established here.

We test the narrower prerequisite sometimes suggested by local geometric
reasoning: that pressure must instantaneously restore or oppose a locally
maximally stretching vorticity/strain configuration. The theorem below
shows that all five trace-free pressure-Hessian components are freely
prescribable by changing only remote parts of an admissible NS datum.
The energy cost is explicitly retained. Thus no deterministic restoring
sign follows solely from the entire local velocity germ, even with the
original Riesz pressure and fixed positive viscosity. This does NOT
exclude a nonlocal or time-integrated pressure-response theorem.

## 1. Exact theorem and pressure normalization

Write G(x)=1/(4pi|x|), so -Delta G=delta_0. For a real solenoidal compact
smooth velocity v define its canonical pressure by

    p[v]=sum_(i,j) partial_i partial_j G * (v_i v_j).       (1)

This solves -Delta p=partial_i v_j partial_j v_i and agrees with the
canonical double-Riesz pressure. Derivatives in (1) are distributional;
away from the support of v the usual smooth kernel integral is valid.
No freely chosen harmonic pressure is added.

**Theorem 1 (exact remote prescription).** Let u0 be any real compact
smooth solenoidal datum, R0>0, and H any real symmetric trace-free 3 by 3
matrix. There is a real compact smooth solenoidal field v, supported
outside B_(R0) and disjoint from supp u0, for which

    Hess p[u0+v](0)=Hess p[u0](0)+H.                       (2)

The perturbation can be chosen as the sum of at most two disjoint rotated
swirl fields. In particular u0+v and u0 agree on a neighborhood of zero,
with every velocity derivative there exactly identical. All these data
are Schwartz. The pressure perturbation is harmonic near zero, so the
trace-free restriction in the theorem is necessary, not a technical loss.

For any sufficiently large chosen distance L, the perturbation can be
supported in the annulus L-1<|x|<L+1. With one fixed unit-size swirl
profile there is a constant C independent of H,L,u0 such that

    ||v||2^2 <= C L^5 lambda_max(H),                       (3)

provided L is large enough for that profile and for the support separation.
For H=0 take v=0. The construction does NOT keep total input energy fixed.

## 2. One compact swirl supplies a signed trace-free projector

Choose a nonzero smooth compact axisymmetric profile so that

    w(x)=f(x_1^2+x_2^2,x_3)(-x_2,x_1,0)

is supported in B1. Then div w=0. It is equivariant under rotations about
e3. Put E=||w||2^2>0. Angular integration gives exactly

    integral w_i w_j = (E/2) diag(1,1,0).                 (4)

Translate this field to L e3: w_L(x)=w(x-L e3), L>2. Its pressure is
axisymmetric about the same axis. Since it is harmonic near zero, symmetry
and zero trace imply the EXACT form

    Hess p[w_L](0)=c_L (3 e3 tensor e3-I).                (5)

The sign of c_L is obtained without an assumption about local strain.
Differentiating (1) twice and expanding the kernel about -L e3 gives

    Hess p[w_L](0)
      =sum_(i,j) D_(a,b,i,j)G(-L e3) integral w_i w_j
                        + O(E L^(-6)).                  (6)

The error bound uses the bounded support radius and homogeneity degree -6
of the fifth derivatives; it is a matrix norm bound. At a nonzero axial
point, direct differentiation gives

    D_(a,b,3,3)G(L e3)
       =12/(4pi L^5) (3 e3 tensor e3-I)_(a,b).           (7)

Fourth derivatives are even under x -> -x. Harmonicity gives the transverse
sum D_(a,b,1,1)G+D_(a,b,2,2)G=-D_(a,b,3,3)G there. Using (4) in (6),

    c_L=-6E/(4pi L^5)+O(E L^(-6)).                       (8)

Thus for every sufficiently large finite L, c_L<0 and
|c_L|>=3E/(4pi L^5). The shape (5) is exact; only its nonzero sign and
size were determined asymptotically. We never replace the actual c_L
with its leading approximation when solving the prescription problem.

Rotating by any O in SO(3) with O e3=n supplies an equally sized compact
field w_(L,n), supported in the unit ball about L n, with

    Hess p[w_(L,n)](0)=c_L(3 n tensor n-I).               (9)

This follows directly from (1) and rotation covariance of G. The same
coefficient c_L works for every n.

## 3. Exact spectral assembly, without cross stresses

Diagonalize H in an orthonormal eigenbasis n_i with eigenvalues h_i,
so sum h_i=0. Set h*=max h_i and

    b_i=(h*-h_i)/(3|c_L|) >=0,
    v=sum_i sqrt(b_i) w_(L,n_i).                         (10)

At least one b_i is zero. Choose L sufficiently large that the unit balls
around L n_i are mutually disjoint and outside supp u0 and B_(R0). This
is possible since distinct eigenbasis vectors are orthogonal and the
support of u0 is compact. Degenerate eigenvalues cause no difficulty.
Pointwise products of any two distinct supported fields vanish exactly.
Consequently the quadratic stress and its canonical pressure are additive:

    p[u0+v]=p[u0]+sum_i b_i p[w_(L,n_i)].                 (11)

Equations (9)--(10) give

    sum_i b_i c_L(3 n_i tensor n_i-I)
      =sum_i (h_i-h*)/3 (3 n_i tensor n_i-I)=H.           (12)

The last equality uses sum h_i=0. This proves (2), with no limiting datum
and no approximation error in H. Disjointness also gives

    ||v||2^2=E sum_i b_i=E h*/|c_L| <= (4pi/3)L^5 h*,    (13)

which proves (3) after increasing the lower threshold for L as in (8).
At most two swirls are nonzero. This completes the proof.

The distance/energy cost is important. Conversely, for any field supported
outside B_d, the kernel representation and |D4G(y)|<=C|y|^(-5) imply

    |Hess p[v](0)| <= C d^(-5)||v||2^2.                 (14)

Thus a fixed amount of energy arbitrarily far away cannot create an
arbitrary Hessian. The construction respects, rather than contradicts,
this quantitative nonlocal decay. No full-input estimate is falsified
merely by letting the input cost (13) grow.

## 4. Actual material vorticity acceleration at fixed viscosity

Let A_ij=partial_j u_i, omega=curl u, and D_t=partial_t+u.grad on the
actual local classical NS solution. The exact equations are

    D_t A=-A^2-Hess p+nu Delta A,
    D_t omega=A omega+nu Delta omega.                   (15)

Applying the product rule once more gives

    D_t^2 omega=-(Hess p)omega+nu J[u]+nu^2 Delta^2 omega,
    J[u]=(Delta A)omega+A Delta omega+Delta(A omega)
             -(Delta u).grad omega
             -2 sum_(i,j) (partial_i u_j) partial_i partial_j omega. (16)

Indeed [D_t,Delta]omega=-(Delta u).grad omega
-2 sum (partial_i u_j)partial_i partial_j omega. Every term in J[u]
is determined by spatial velocity derivatives at the same point. Thus,
for the two actual local NS solutions from u0 and u0+v in Theorem 1,

    difference of D_t^2 omega at (0,0) = -H omega0(0).    (17)

Each material derivative refers to its own solution's material curve.
All viscous terms in their initial values agree exactly; no inviscid
limit or independently prescribed pressure history was used.

If omega0(0) is nonzero, symmetric trace-free matrices H can map it to
any specified vector. In coordinates with omega0(0)=Omega e3, choose
H13,H23,H33 to obtain the desired third column and adjust H11+H22=-H33.
Theorem 1 therefore prescribes the difference in the ENTIRE initial
material vorticity acceleration arbitrarily, with the same local
vorticity, strain, alignment and all spatial derivatives.

### 4.1 This also applies at maximal positive strain alignment

For s>0 and Omega>0 let

    A0=diag(-s/2,-s/2,s)
                  +[[0,-Omega/2,0],[Omega/2,0,0],[0,0,0]].

Then tr A0=0, omega0=Omega e3 and
A0 omega0=s omega0. Vorticity is aligned with the most positive strain
eigenvector and its initial stretching is strictly positive.
To obtain admissible whole-space data agreeing with A0 x near zero, choose
a compact smooth cutoff chi equal to one near zero and set

    u0=curl[-chi(x) (x cross A0 x)/3].                   (18)

The identity curl(x cross A0 x)=-3 A0 x follows from tr A0=0 and
homogeneity. Hence (18) is real compact smooth solenoidal and equals
A0 x on that neighborhood. It is NOT an infinite-energy affine solution.
There omega is spatially constant and all terms J[u], Delta^2 omega
vanish at the initial point. Thus (16) reduces there to

    D_t^2 omega=-(Hess p)omega                           (19)

for every fixed nu>0. Applying Theorem 1 now makes omega.Hess(p).omega
arbitrarily positive or negative, or makes the full vector in (19)
arbitrary, without altering that maximal initial stretching alignment.

These examples are instantaneous statements about genuine local NS
solutions. Continuity gives some short interval on which any chosen
strict sign persists, but its length is NOT uniform in the remote input
or Hessian magnitude. We claim neither a full-turnover interval nor a
singular material deformation history.

## 5. What is ruled out, what survives, and the Tao gate

Ruled out: an instantaneous universal sign or deterministic local closure
for the trace-free pressure Hessian based only on local velocity, strain,
vorticity alignment, or even the whole local spatial germ. Such a closure
cannot become exact simply by adding more local derivatives. In particular,
local maximal stretching does not by itself enforce an initial restoring
pressure response.

Not ruled out: full-input or energy-aware bounds; integrated responses
over dynamically selected intervals; spatially nonlocal geometric
constraints; dissipation-based compensation; a restriction automatically
satisfied by a hypothetical singularity; or a joint signed bound for the
actual comparable-frequency refinement production. No such hypothesis is
proved automatically by the present construction.

The calculation uses the EXACT original-NS pressure relation (1), its
fourth-derivative kernel in (6)--(9), and the cancellation of A^2 omega
in (16). Tao's assigned cascade operator is not governed by (15)--(16)
with the canonical Riesz Hessian generated by its own velocity. More
concretely, the nonzero same-carrier pump coefficient in his Table 1
violates the original convolution support relation proved and tested in
Section 8 of `2026-09-08-exact-circuit-obstructions.md`. That already gives
an explicit discriminator for the same original operator used here.
No claim that this negative local test bounds Tao's or NS's critical norm
is made. Passing the discriminator is not a positive producer.

A material change of coordinates does not resolve this test: (17) is
already a material identity. A useful surviving mechanism must retain
nonlocal pressure information AND control its evolution over a long enough
interval, with no unknown critical clock. The new theorem narrows the
permitted pressure mechanism to that genuinely dynamical problem, but
supplies no general reduction of NS-R3 to the special carrier circuits.

## 6. Source and audit ledger

The elementary compact-swirl pressure-tail construction is already used in
this repository's `research/evidence/hf13-entropy-far-field.md`, in a
different entropy calculation. Here it is differentiated twice, combined
with exact axisymmetry, and assembled spectrally to prescribe every
trace-free Hessian component. The original pressure/stretching identities
and leading viscous correction were also checked against
`2026-09-07-pressure-stretching-graph-lift-test.md`; no invalid positive
value-space diffusion or harmonic-pressure freedom is introduced.

Primary-source background: E. Cozzi and J. P. Kelliher, *Incompressible
Euler Equations and the Effect of Changes at a Distance*,
arXiv:1507.05566v2, https://arxiv.org/html/1507.05566v2 . Introduction and
Theorem 1 inspected. Its distance stability bounds retain global velocity
and vorticity bounds. It is neither the prescription theorem above nor
an arbitrary-data NS regularity theorem. Remote pressure influence itself
is established background; no claim of discovery or publication priority.

`research/check_remote_pressure.py` checks the exact axial fourth
Newton-kernel derivative, harmonic trace, swirl divergence, spectral
assembly and energy weights in exact rotated examples, affine solenoidal
extension, maximal alignment, and the material/Laplacian commutator.
These are finite algebra checks, not certification of the analytic proof
or an independent mathematical review. Canonical proof-graph claims and
all terminal gaps remain unchanged.
