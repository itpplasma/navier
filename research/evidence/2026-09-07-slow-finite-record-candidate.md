Controller-retained worker snapshot, 2026-09-07. Original worker file: slow-records.md;
SHA256 `a592f3d0c9c63cae5c72ca47e101fd7d9e3d20d0bc020d988e5dc8eece74bce0`.
Author derivation with independent mathematical audit PENDING. This
record is evidence for further research, not an established graph theorem.
The original worker text follows unchanged. PLAN alone allocates work.

# Actual-NS slow finite records can converge to a constant tangent

Date: 2026-09-07. Frozen clean base:
`ec2ed88c8d1fdf3b66b0e989827d44d93f1f76df`.
Worker evidence only. MODE: DISCOVER/PROVE, followed by FALSIFY of the
finite-segment extraction premise below. Complete author derivation;
independent mathematical audit and novelty assessment are pending.

## Frontier and result

TERMINAL CLAIM: NS-R3, original unforced incompressible NS on R3, every
solenoidal Schwartz datum and every fixed nu>0, globally smooth velocity and
normalized pressure with the energy bound. This note does not prove it.

ESTABLISHED INPUT: the frozen record notes supply bounded unit-viscosity
ancient compactness, but preserve the earlier smaller-amplitude mark only
when its normalized distance from the terminal mark stays bounded. The slow
alternative permits that mark to escape to minus infinity. Global physical
energy scales as nu^3/M times normalized energy.

PROSPECTIVE FINITE-SEGMENT REPAIR TESTED: an actual fixed-viscosity R3 solution
from Schwartz data, with two genuine first-hitting records separated by a
fixed positive relative amplitude gain, arbitrarily long normalized record
duration, exact energy/enstrophy identities and uniformly small physical
energy/dissipation, must have a nonconstant normalized ancient limit.

RESULT: that premise is false. A family of actual NS finite segments has all
of these properties and converges to a constant unit vector. The amplitude
ratio q>1 in the construction is fixed but close to one; a ratio of two is
NOT established. The construction uses different Schwartz data in different
members and does NOT give infinitely many records of one fixed parent.
These two boundaries are essential. This is an exact obstruction to the
stated energy-based finite-segment repair, not a singularity counterexample
or a refutation of a theorem retaining the full fixed-datum ancestry.

The positive dynamical ingredient is canonical pressure acceleration from a
distant compact solenoidal packet. Thus the growing record is produced by
the original NS equation, not an artificial comparison curve or a harmonic
pressure acceleration.

## 1. A compact unit core whose speed initially increases under NS

Choose a smooth nonincreasing function eta on R which is one on (-infinity,0],
zero on [4,infinity), and satisfies -1/2 <= eta' <= 0. Set f(r)=eta(log r),
with f=1 at and near r=0, and define

    A(x) = curl(0,0,x2 f(|x|)).

Then A is smooth, compactly supported, divergence free, equals e1 on B1,
and is even under x -> -x. It also has global supremum norm exactly one.
Indeed put g=rf'(r), aj=xj/r. Its nonzero components are

    A1=f+g a2^2,       A2=-g a1 a2.

Consequently

    |A|^2 = f^2+2fg a2^2+g^2 a2^2(a1^2+a2^2)
          <= max(f^2,(f+g)^2) <= 1,

since 0<=f<=1 and -1/2<=g<=0. This avoids the unjustified assumption that
an arbitrary solenoidal localization preserves the unit maximum.

We add a distant disjoint packet with predominantly transverse kinetic
stress. Choose nonzero smooth compact bump functions F,G,H, and put

    psi(x)=F(x1)G(x2/L)H(x3),
    B0=(partial2 psi,-partial1 psi,0).

Writing Qij=integral (B0)i(B0)j, the diagonal entries satisfy

    Q11 = L^(-1)||F||2^2 ||G'||2^2 ||H||2^2,
    Q22 = L ||F'||2^2 ||G||2^2 ||H||2^2,
    Q33 = 0.

Choose L so Q22>2Q11, then multiply B0 by a fixed positive constant so that
||B0||infinity <= 1/4. This preserves the strict stress inequality.
Translate B0 to distance D in the e1 direction:

    B_D(x)=B0(x-D e1),        a=A+B_D.

Take D large enough that the two supports are disjoint. Then a is solenoidal
and compactly supported, a=e1 on B1, and ||a||infinity=1.

For the canonical NS pressure use

    p_a = partial_i partial_j (-Delta)^(-1)(a_i a_j).

The pressure of A is even, so its gradient vanishes at the origin. Disjoint
support gives a_i a_j=A_i A_j+(B_D)i(B_D)j exactly. Away from the packet the
pressure kernel is

    Kij(z)=(3zi zj-delta_ij |z|^2)/(4 pi |z|^5).

Taylor expansion about -D e1 gives

    partial1 p_(B_D)(0)
       = 3(2Q11-Q22-Q33)/(4 pi D^4) + O(D^(-5)) < 0       (1.1)

for sufficiently large fixed D. The remainder constant depends only on the
fixed compact packet, and is bounded by a constant times
integral |z| |B0(z)|^2. To check the sign directly, on the negative first
axis partial1 K11=6/(4pi D^4), whereas partial1 K22 and partial1 K33 both
equal -3/(4pi D^4); derivatives of the off-diagonal entries vanish there.

At the origin a is constant in a neighborhood. Therefore for the actual
NS solution with datum a and ANY viscosity epsilon>0,

    partial_tau v1(0,0)
       = -(a.grad)a1(0)+epsilon Delta a1(0)-partial1 p_a(0)
       = alpha > 0,                                      (1.2)

where alpha is fixed independently of epsilon. No external force or free
harmonic part of the pressure was used.

## 2. Uniform short-time solutions and two genuine records

For 0<epsilon<=1 let v^epsilon be the classical mild solution of

    partial_tau v+P(v.grad v)=epsilon Delta v,   v(0)=a.

There are a common time tau0>0 and constants C,C1, depending on the fixed
profile a but not epsilon, such that these solutions exist smoothly on
[0,tau0] and

    ||v||H8 <= C,
    ||partial_tau v||H6 + ||partial_tau^2 v||H4 <= C.        (2.1)

Here is the uniformity argument rather than an import of an inviscid limit.
The H8 energy commutator estimate gives

    (1/2)d||v||H8^2/dtau + epsilon ||grad v||H8^2
        <= C8 ||grad v||infinity ||v||H8^2
        <= C8' ||v||H8^3.

Starting with the local smooth solution for each epsilon>0, its norm remains
bounded by twice the fixed initial H8 norm on a common positive interval.
Bounded mild continuation prevents its maximal endpoint occurring within
that interval. Applying the equation once gives the H6 bound for v_tau;
differentiating it gives

    v_tautau = -P(v_tau.grad v+v.grad v_tau)+epsilon Delta v_tau,

and hence the H4 bound. The Sobolev product estimates and embeddings used
here have constants independent of epsilon. Smoothness at tau=0 follows
from the compact smooth datum. No Euler theorem is needed.

After reducing tau0, (1.2), (2.1), and Taylor's theorem imply, for all
0<=tau<=tau0 and all 0<epsilon<=1,

    v1^epsilon(0,tau) >= 1+(alpha/2)tau,
    ||v^epsilon(tau)-a||infinity <= C1 tau,
    |h_epsilon(tau)-h_epsilon(s)| <= C1 |tau-s|,            (2.2)

where h_epsilon(tau)=||v^epsilon(tau)||infinity. Choose

    d=alpha tau0/8 > 0,      q0=1+d,      q1=1+2d.

At tau0 the norm is at least 1+4d. Its initial value is one. Thus the first
hitting times theta0(epsilon), theta1(epsilon) of q0 and q1 both exist,
and (2.2) gives

    theta0 >= d/C1,
    theta1-theta0 >= d/C1,
    theta1 <= tau0.                                      (2.3)

The inequalities do not assume monotonicity of h. They use its first-hitting
property and Lipschitz bound. Each slice is continuous and tends to zero at
spatial infinity (it is smooth and H8), so a spatial maximum is attained.
Choose z_epsilon with |v^epsilon(z_epsilon,theta1)|=q1.

The ratio q=q1/q0>1 is fixed independently of epsilon. It may be extremely
close to one because the constants depend on the fixed remote packet.
Nothing here proves a factor-two increase.

## 3. Fixed parent viscosity, vanishing physical budgets, slow records

Fix any nu>0. Let R tend to infinity, and define

    epsilon_R=1/R,     M_R=R^4,     rho_R=nu R/M_R,
    u_R(x,t)=M_R v^(epsilon_R)(x/rho_R, M_R t/rho_R).

This solves ORIGINAL unforced NS with viscosity nu, because the transformed
viscosity is nu/(M_R rho_R)=1/R. The auxiliary epsilon is a proof coordinate;
every physical parent u_R has the SAME prescribed nu. The initial datum is
compact smooth and solenoidal, hence Schwartz. Pressure is transformed by
p_R=M_R^2 p_v and retains its canonical normalization.

The two first hitting times for the physical levels q0 M_R and q1 M_R are

    t_(j,R)=(rho_R/M_R) theta_j(1/R),   j=0,1.

They are genuine records above the initial supremum M_R. Normalize at the
second record and a maximizing point x_R=rho_R z_(1/R):

    W_R(y,s)=(q1 M_R)^(-1)
        u_R(x_R+nu y/(q1 M_R), t_(1,R)+nu s/(q1^2 M_R^2))
      = q1^(-1) v^(1/R)(z_(1/R)+y/(q1 R),
                       theta1(1/R)+s/(q1^2 R)).          (3.1)

These are unit-viscosity, coefficient-one NS mild solutions on
[-L_R,0], where

    L_R=q1^2 R theta1(1/R) -> infinity.

They satisfy EXACTLY

    ||W_R||_(L-infinity(R3 x [-L_R,0])) <= 1,
    |W_R(0,0)|=1,
    ||W_R(s)||infinity <= q0/q1 for -L_R<=s<=-ell_R,

with normalized record-transition length

    ell_R=q1^2 R[theta1(1/R)-theta0(1/R)]
          in [q1^2 R d/C1, q1^2 R tau0].                 (3.2)

Thus ell_R tends to infinity and the earlier fixed-fraction mark really
escapes to minus infinity; it has not merely been omitted from the input.

By (2.1) and (3.1), on the entire available history,

    ||grad_y W_R||infinity <= C/R,
    ||partial_s W_R||infinity <= C/R.                    (3.3)

Select a subsequence of the unit vectors W_R(0,0) converging to e. For every
fixed compact spacetime set in R3 x (-infinity,0], (3.3) gives

    W_R(y,s) -> e,             |e|=1.                   (3.4)

The limit is exactly a nonzero constant ancient mild solution. All spatial
curl witnesses on fixed normalized cylinders vanish. The initial amplitudes
and the two marks were real properties of the NS trajectories throughout.

Nevertheless their physical initial energies and total viscous losses go
to zero. Exact changes of variables give

    ||u_R(0)||2^2 = M_R^2 rho_R^3 ||a||2^2
                  = nu^3 R^(-1)||a||2^2,                (3.5)

    nu integral_0^t_(1,R) ||grad_x u_R||2^2 dt
       = nu M_R rho_R^2
            integral_0^theta1(1/R) ||grad v^(1/R)||2^2 d tau
       <= C nu^3 R^(-2).                               (3.6)

Every member also satisfies the exact global energy equality and exact
enstrophy identity, because it is a smooth actual NS solution. Its terminal
time t_(1,R)=nu R^(-7)theta1 tends to zero, its record amplitude q1 R^4
diverges, and its complete normalized past length is comparable to R.
The normalized plateau is broad enough that its local gradients disappear,
while its physical support scale rho_R=nu R^(-3) still shrinks.

This proves the counterfamily asserted at the start. It is stronger in
equation fidelity than terminal-reset/05's comparison curve, which has an
explicit nonzero NS curl residual. It is weaker in ancestry: that curve has
one fixed initial field and a full slow record sequence, whereas this proof
has a family of actual finite NS segments with two record levels each.
Neither construction supplies an NS singularity.

## 4. Exact remaining implication and next distinct action

The theorem defeats a local extraction claim based only on long normalized
history, a fixed relative first-record gain, and physical energy/enstrophy
budgets. It does not defeat the banked marked ancient theorem: here ell_R
diverges, and the smaller-amplitude mark vanishes from every fixed ancient
window. The limiting constant has the canonical mild pressure, so the
non-mild accelerating-constant exclusion is also untouched.

It does not yet falsify the same proposed claim restricted to a gain of
exactly two. More importantly, it does not replace the actual fixed-datum
singularity ancestry: the initial amplitudes and high Sobolev norms vary
with R, and the physical segment lengths shrink to zero. A continuation
theorem retaining those data may still exclude the sequence. The L3 norms
of these data grow as nu R ||a||3; no bounded critical input is claimed.

The first uncontrolled term for a fixed singular parent remains the
pressure-driven gain connecting the escaped earlier mark to the endpoint.
The explicit family shows that it can be supplied locally by a remote stress
while all retained normalized derivatives vanish. Thus a successful repair
must control that stress across actual successive records, or must retain
an additional spatial/temporal scale or the fixed-datum ancestry. Reusing
the endpoint energy budget or its exact identities alone cannot distinguish
this family.

NEXT DISTINCT ACTION: test a statement that keeps the whole dyadic ancestor
chain and its physical locations, rather than adding another scalar budget
to a single record segment. In particular, quantify whether pressure work
delivered by spatially separated stress packets can be reused through all
ancestor records with one fixed Schwartz datum. This note supplies a finite
segment adversarial input that any proposed transfer inequality must pass;
it supplies no bound on that reuse and no terminal claim promotion.

## Sources and check record

Project inputs read: PLAN, canonical proof/graph and verifier, the current
refinement contract, the one-slice and axial record notes, and
terminal-reset/04--05. The present task changes none of them.

The sole analytic literature input used is bounded-data local mild
existence, uniqueness and continuation, with smooth-data persistence. The
actual primary text inspected was Koch--Nadirashvili--Seregin--Sverak,
*Liouville theorems for the Navier-Stokes equations and applications*,
Section 4, formulae (4.6)--(4.9) and Proposition 4.1:
https://arxiv.org/html/0709.3599v1 . Its domain is whole space, its equation
is unforced NS, and bounded divergence-free data are permitted. It supplies
no slow-record rigidity. The epsilon-uniform H8 bound, pressure packet and
all scalings above are author derivations, not attributed to that source.

No computation or repository verifier is called mathematical certification.
An in-memory symbolic differentiation of partial_i partial_j(1/(4pi|x|))
and evaluation at -D e1 returned diagonal coefficients
(6,-3,-3)/(4pi D^4), independently checking the sign in (1.1); this is an
algebra check only. `git diff --check` passed with the tracked tree unchanged.
Adversarial audit should first check the pressure-kernel sign and disjoint
tensor decomposition, then the epsilon-uniform differentiated H8 estimates,
the first-hitting inequalities, and the three scale changes. The claimed
scope must retain the fixed q>1 versus factor-two distinction and the
varying-data versus single-parent distinction.

AUTHOR PROOF: complete as written, audit pending.
SOURCE INSPECTION: Section 4 primary text inspected during this worker run.
INDEPENDENT AUDIT: not performed.
FORMAL VERIFICATION: not performed.
NS-R3 / CRITICAL: open and unchanged.
