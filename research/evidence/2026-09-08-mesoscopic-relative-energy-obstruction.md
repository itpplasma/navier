# Mesoscopic clouds defeat automatic fixed-background energy normalization

Date: 2026-09-08. Frozen input main:
`641a58b6617a7907af9f559febafc5ab61d648a0`.
Status: AUTHOR PROOF; independent mathematical audit PENDING.
No canonical promotion. The homogeneous stability method is standard; no
exhaustive priority claim is made for these full-flow noncoercivity adapters.

## 0. Exact consumer and what is falsified

The preceding theorem excludes long controlled full-state returns when the
WHOLE normalized difference from one evolved smooth NS background has bounded
energy at both endpoints. It does not make those bounds automatic. This note
proves that neither a controlled efficient core nor any nonempty strict finite
flow condition open in the displayed homogeneous topology can do so by itself.

The counterexample has an intermediate-scale cloud that is SMALL even in the
PHYSICAL critical norm and is a globally regular small-data NS datum by itself.
It remains present in the full original evolution. Nevertheless, after any
fixed smooth physical background is subtracted, its normalized relative L2
energy diverges through an entire fixed normalized time interval. Thus the
obstruction is not removed merely by subtracting the fixed bulk from the
preceding retained-bulk example.

There are two separate theorems:

* a high-amplitude, fixed-physical-viscosity construction with a fixed smooth
  Euler reference and a fixed physical background (Theorem 2);
* an embedding of ANY fixed smooth ORIGINAL NS trajectory, preserving all
  strict finite critical flow conditions, at the SAME physical viscosity
  (Theorem 3). No Euler approximation is needed in this second theorem.

No actual positive regenerative reference cell is asserted to exist. The
second theorem preserves such a cell if it exists; it does not manufacture
one by preloading daughters or resetting the exterior. Neither theorem is a
one-datum infinite cascade or a counterexample to the preceding return theorem.

The terminal consumer remains the every-upper-time, M-uniform RF-q upper
producer -> exact RF identity -> RF-q -> finite L^{3,q} -> classical
identification -> Lorentz continuation -> NS-R3 with canonical pressure.
No new upper producer or blowup-event extraction is supplied. The concrete
consumer here is a sharp exclusion of automatic fixed-background endpoint
normalization based only on finite critical flow observations.

## 1. A full-flow stability fact with no L2-error factor

Set

    X(z)^2=||grad z||2^2+||Lambda^3 z||2^2,
    Z(z)=||Lambda^(1/2)z||2,  Y(z)=X(z)+Z(z).

Let w be a fixed smooth finite-energy solution of original NS with viscosity
mu0>=0 on a fixed closed interval [0,theta], with mu0=0 meaning ORIGINAL Euler.
Assume its H5 norm is bounded on that interval. Let U solve original NS with
mu>0 and initial datum w(0)+H, where H is real solenoidal and Schwartz. Write
z=U-w and assume mu<=mu0+1. There are c_w,C_w>0 such that

    Y(H)+|mu-mu0|<=c_w
      => sup_[0,theta] Y(U-w)<=C_w[Y(H)+|mu-mu0|],       (1.1)

and U is smooth through theta. The same bound, with changed reference
constants, controls every fixed finite L^{3,q}, q>3, velocity difference
and the H1 norm of the difference of CANONICAL pressures. There is NO
assumption that ||H||2 is bounded or small.

Here is the adapter, to avoid silently broadening the predecessor's statement.
Exact subtraction gives

    z_t-mu Delta z+P[((w+z).grad)z+(z.grad)w]
                                       =(mu-mu0)Delta w. (1.2)

The proof of (1.8)--(1.12) in the retained-bulk note uses the shape of H only
when inserting its initial norm. Its homogeneous estimates therefore give

    ||z||infinity+||grad z||infinity <=C X(z),
    X'(z)<=C_w X(z)+C X(z)^2+|mu-mu0| C_w,
    Z'(z)<=C_w Z(z)+C_w X(z)+|mu-mu0| C_w               (1.3)

on X<=1. Transport cancellations, the Gagliardo seminorm calculation,
ordinary viscosity and the entire pressure pairing are unchanged. Integrate
on this FIXED reference interval, close X<1, then extend the smooth solution
using the resulting full ||grad U||infinity bound. Initial higher Sobolev
norms need only be finite separately for each datum. This proves (1.1).
The pressure proof is the full stress difference w tensor z+z tensor w+
z tensor z, controlled in L2 and dotH1 exactly as in that note. QED.

The proof compares entire solutions. It does not solve a projected equation
or compare only selected trees, Fourier carriers or instantaneous jets.

## 2. A critically vanishing cloud is globally harmless in isolation

Fix a nonzero real solenoidal Schwartz field h. Put

    L=K^(1/4),  C=K^(-1/16),  m_K(x)=C L h(Lx).         (2.1)

Then

    ||m_K||dotHhalf=C||h||dotHhalf ->0,
    ||m_K||_(3,q)=C||h||_(3,q) ->0,
    ||m_K||2^2=C^2/L ||h||2^2=K^(-3/8)||h||2^2.       (2.2)

For every fixed physical nu>0, m_K by itself has a global smooth original NS
solution for all large K. This last assertion follows from the following
standard energy/enstrophy argument, included to specify the smallness used.
For a smooth NS solution v put E=||v||2^2, J=||grad v||2^2, Q=||Delta v||2^2.
Energy decreases. Testing the equation against -Delta v and using Sobolev
and interpolation gives

    (1/2)J'+nu Q
       <=||v||3 ||grad v||6 ||Delta v||2
       <=C_* E^(1/4) J^(1/4) Q.                       (2.3)

If C_*[E(0)J(0)]^(1/4)<nu/2, a continuity bootstrap makes J nonincreasing
and bounds dotHhalf by interpolation for every finite time. Its L^{3,q}
bound feeds the existing classical Lorentz continuation theorem. The initial
product for m_K is

    E(0)J(0)=C^4 ||h||2^2 ||grad h||2^2 ->0,           (2.4)

independently of L. Smoothness at time zero follows from the Schwartz datum.
This proves the assertion with ordinary positive viscosity and no forcing.
It is NOT a claim that the sum of this cloud and an arbitrary large core is
globally regular. Their coupled finite-time evolution is handled below.

## 3. High-amplitude cores: fixed smooth subtraction still fails

Fix real solenoidal Schwartz f with ||Q_1 f||2=1 and gamma_1(f)>0, as supplied
by the explicit transverse pair in the retained-bulk note. Fix a real
solenoidal compact smooth h0, which may be zero, and fixed nu>0. Let w be the
smooth ORIGINAL Euler solution from f. Choose a fixed theta>0 in its smooth
lifespan such that

    3/4<=||Q_1 w(tau)||2<=5/4,
    gamma_1(w(tau))>=3 gamma_1(f)/4   (0<=tau<=theta).  (3.1)

Only continuity on a fixed reference interval is used here, not a Taylor
truncation. Put

    A=K^(1/4), L=K^(1/4), C=K^(-1/16),
    d_K(x)=A K f(Kx)+C L h(Lx)+h0(x).                  (3.2)

All these data are admissible real solenoidal Schwartz data for the SAME
physical viscosity nu. Let u_K be the actual original NS solution, and set

    t=tau/(A K^2),
    U_K(tau,y)=u_K(t,y/K)/(A K),
    P_K(tau,y)=p_K(t,y/K)/(A^2 K^2).                   (3.3)

**Theorem 2.** For all sufficiently large K the full u_K exists through
T_K=theta K^(-9/4), and, uniformly for tau in [0,theta],

    Y(U_K-w)+||P_K-p_w||H1 <= C_0(1+nu)K^(-1/4),
    a_K(u_K(t)) comparable to K^(1/4),
    gamma_K(u_K(t))>=gamma_1(f)/2>0,
    ||grad U_K||2+||grad U_K||infinity<=C_0,           (3.4)
    2nu integral_0^T_K ||grad u_K||2^2<=C_0 nu K^(-3/4).

Constants can depend on the fixed fields, reference interval and nu, not K.
Let B be the fixed smooth original NS solution from h0 on a fixed positive
physical interval. Then the WHOLE relative energy satisfies

    sup_(tau<=theta) |K^(3/8)||u_K(t)-B(t)||2^2-||h||2^2|
                                                      ->0. (3.5)

Consequently

    inf_(tau<=theta) (K/A^2)||u_K(t)-B(t)||2^2 ->infinity,
    (K/A^2)||u_K(t)-B(t)||2^2 comparable to K^(1/8).     (3.6)

The divergence persists with A replaced by the exact current annular amplitude
in (3.4). More generally (3.6)'s divergence holds after subtraction of ANY
fixed F in C^1([0,t0];L2(R3)), including any fixed smooth NS reference with
such a lifespan. F is fixed independently of K; a K-dependent background is
not excluded.

**Proof.** The cloud in the actual normalized initial state is

    H_m,K(y)=(C/A)(L/K)h((L/K)y),
    H_0,K(y)=(A K)^(-1)h0(y/K),
    U_K(0)=f+H_m,K+H_0,K,   mu_K=nu/A.                (3.7)

Exact norm scalings are

    ||H_m,K||2^2=K^(1/8)||h||2^2,
    Z(H_m,K)=K^(-5/16)Z(h),
    ||grad H_m,K||2=K^(-11/16)||grad h||2,
    ||Lambda^3 H_m,K||2=K^(-35/16)||Lambda^3 h||2,
    ||H_m,K||infinity=K^(-17/16)||h||infinity,
    Z(H_0,K)=K^(-1/4)Z(h0),
    ||grad^r H_0,K||2=K^(-1/4+1/2-r)||grad^r h0||2.   (3.8)

Use (1.1) with mu0=0 and mu=nu K^(-1/4). This proves the full velocity and
canonical-pressure approximation in (3.4), despite the diverging L2 cloud.
It also gives the full derivative bounds. The annular multiplier and its
quadratic source are continuous on X on a nonzero annulus; (3.1) gives the
amplitude and efficiency bounds. Exact physical scaling gives

    2nu integral_0^T_K||grad u_K||2^2
      =2nu(A/K) integral_0^theta||grad U_K||2^2,         (3.9)

which is the final estimate in (3.4).

To prove (3.5), it is essential to control the WHOLE TIME INTERVAL, not just
its initial state. Write R=u_K-B in physical coordinates. At time zero,

    ||A K f(K.)||2=K^(-1/4)||f||2,
    ||C L h(L.)||2=K^(-3/16)||h||2.

The second term dominates; Cauchy--Schwarz bounds the cross term, giving

    ||R(0)||2^2=K^(-3/8)[||h||2^2+O(K^(-1/16))].       (3.10)

On a fixed short physical interval let the L2 and Linfinity gradient norms
of B be bounded by C_B. Its local smooth lifespan contains [0,T_K] for large
K. The exact relative energy identity from the preceding note gives

    E_R(t)+D_R(t)=E_R(0)-2 integral_0^t integral R.(R.grad B),
    E_R(t)<=exp(2C_B t)E_R(0),
    D_R(t)<=2D_u(t)+4nu C_B^2 t.                       (3.11)

Here the last inequality follows from ||grad(u-B)||2^2<=2||grad u||2^2+
2||grad B||2^2. The actual full dissipation in (3.9) is O(K^(-3/4)), whereas
E_R(0) is of order K^(-3/8). The absolute strain work in (3.11) is at most
2C_B t exp(2C_B t)E_R(0). Combining both sides of the exact identity therefore
proves (3.5) uniformly in t<=T_K. No cloud or background was evolved
independently inside the equation for u_K; (3.11) only compares exact flows.

Multiplication by K/A^2=K^(1/2) proves (3.6). For general fixed F there are
two cases. If F(0)=h0, then ||F(t)-B(t)||2=O(t), which is negligible compared
with K^(-3/16) throughout t<=T_K. Thus (3.5) holds for F as well. If
F(0) differs from h0 in L2, the triangle inequality and (3.11) give uniformly

    ||u_K(t)-F(t)||2 -> ||h0-F(0)||2>0.

Multiplication by K/A^2 again proves divergence. These two cases establish
the stated quantifiers. QED.

In particular the initial total physical energy tends to ||h0||2^2; it tends
to zero when h0=0. The cloud tends to zero in the physical critical norms
in (2.2), is globally regular in isolation, and is invisible in the entire
normalized critical/pressure comparison. Its unbounded relative energy is
therefore NOT a required critical loss. Neither next-scale amplitude gains
nor a regenerative turnover have been constructed by this example.

The construction is not confined to an isolated choice of powers. More
generally put A=K^alpha, L=K^beta, C=K^chi for any

    alpha>0, beta>0, chi<0,  2alpha+beta-2chi<1.       (3.12)

Then the cloud critical norm tends to zero, its physical energy is of order
K^(2chi-beta), and the normalized relative energy grows like
K^(1-2alpha-beta+2chi). The core energy K^(2alpha-1) and the actual full
viscous bound O(K^(alpha-1)) are both smaller than the cloud energy. Its
normalized derivative and critical norms are o(K^(-alpha)), so (1.1) still
gives O(K^(-alpha)) full-flow convergence for fixed nu. The same relative
energy proof applies. Thus an open set of exponent choices has this failure.

## 4. Arbitrary strict finite ORIGINAL-NS flow tests do not repair this

The preceding construction used an Euler reference to make a_K tend to
infinity at fixed physical viscosity. The following version uses a fixed
ORIGINAL NS reference instead, and preserves its actual finite flow events.

**Theorem 3 (full-flow mesoscopic embedding at fixed viscosity).** Let w be
ANY real smooth finite-energy ORIGINAL NS solution of viscosity nu>0 on a
fixed closed interval [0,theta], with solenoidal Schwartz datum f and a
bounded H5 reference norm. With h,L,C as in (2.1), take

    d_K(x)=K f(Kx)+C L h(Lx),
    U_K(tau,y)=u_K(tau/K^2,y/K)/K.                      (4.1)

For all large K the complete original u_K exists through theta/K^2 and

    sup_[0,theta] [Y(U_K-w)+||P_K-p_w||H1] ->0,         (4.2)
    sup_(tau<=theta)|K^(3/8)||u_K(tau/K^2)||2^2-||h||2^2|
                                                       ->0. (4.3)

Thus ||U_K(tau)||2^2 is comparable to K^(5/8), uniformly over the whole
interval. The same normalized relative-energy divergence holds against
every fixed F in C^1([0,t0];L2) after physical subtraction, with the
normalization K||u_K-F||2^2. No F may depend on K in this assertion.

Proof. In (1.1) use mu=mu0=nu and

    H_K(y)=C(L/K)h((L/K)y),
    Z(H_K)=K^(-1/16)Z(h),
    ||grad H_K||2=K^(-7/16)||grad h||2,
    ||Lambda^3 H_K||2=K^(-31/16)||Lambda^3 h||2.         (4.4)

All forcing differences are zero. This proves (4.2) with rate O(K^(-1/16))
and a uniform full normalized enstrophy bound. At time zero the cloud norm
K^(-3/16)||h||2 dominates the core norm K^(-1/2)||f||2. The FULL energy
identity and

    D_u(theta/K^2)=2nu K^(-1) integral_0^theta||grad U_K||2^2
                                                              =O(K^(-1))

prove (4.3), since K^(-1)=o(K^(-3/8)). For F(0)=0 the O(t) comparison is
negligible; for F(0) nonzero use the same triangle argument as above. QED.

Here is the precise finite-event consequence. Fix any finite set of reference
times tau_j and positive reference scales kappa_j at which the relevant
annuli are nonzero. Set t_j=tau_j/K^2 and K_j=K kappa_j. Exact scaling gives

    a_(K kappa)(u_K(tau/K^2))=a_kappa(U_K(tau)),
    gamma_(K kappa)(u_K(tau/K^2))=gamma_kappa(U_K(tau)),
    (t_(j+1)-t_j) a_Kj(u_K(t_j)) K_j^2
       =(tau_(j+1)-tau_j) a_kappa_j(U_K(tau_j)) kappa_j^2. (4.5)

The functionals on the right are continuous under (4.2), with denominators
bounded away from zero. Every fixed finite collection of strict gain,
efficiency and nonlinear-clock inequalities satisfied by the ACTUAL w is
therefore also satisfied by the ACTUAL u_K for all large K. The complete
finite return outputs converge in Y after the corresponding continuous
normalizations; no output is projected back onto a carrier ansatz. Strict
open output-neighborhood conditions in that topology persist as well.
They do not persist in full L2, which is precisely the obstruction.

Consequently a nonempty finite flow condition OPEN in this homogeneous full-flow
topology cannot, by itself, force a uniform fixed-background normalized L2
bound. This statement includes hypothetical robust finite regenerative cells
if such cells are constructed; it does not assert they already exist. The
physical amplitudes of a fixed reference are preserved in this version,
not made unbounded by K. The high-amplitude assertion belongs to Theorem 2.

## 5. Exact limits and remaining task

The preceding relative-background return theorem remains valid. Its endpoint
bound is not a topological consequence of an efficient core, small critical
cloud, bounded normalized derivatives, or finitely many strict flow tests.
The constructions here vary the datum with K and do not iterate one datum
through accumulating returns. In particular Theorem 3 does not prove that
ANY positive regenerative cell exists, nor that an existing one repeats.

A K-dependent or history-dependent background that absorbs the cloud is NOT
ruled out. Any such background must be evolved on the whole interval with
its actual defect, cross pressure and feedback accounted for; selecting it
again at the next return and dropping the discrepancy is still a reset.
The new no-go concerns automatic bounds relative to a FIXED smooth physical
background and bounds inferred solely from finite critical flow observations.

The one dominant nut remains the original full-state critical return with
inherited dynamically essential exterior: construct and shadow scale
repetition, or extract regenerative events from arbitrary blowup and prove
an input-summable CRITICAL cost. Whole/relative L2 divergence alone is not
that cost. The physical a^2/K weight from the preceding theorem still need
not count infinitely many events. No new uncontrolled strain norm has been
renamed as a continuation producer.

Certified positive regenerative turnovers remain ZERO. No recurrent set,
full infinite-cascade shadowing, arbitrary-data RF-q estimate, or NS-R3
resolution is claimed. The checkers are exact finite identities, not PDE
validation or independent review. The original viscosity, canonical pressure,
all generated modes and the entire inherited exterior are retained in every
claimed full-flow comparison.

## 6. Proof inputs and computational scope

The general stability argument explicitly adapts Sections 1--2 of
`research/evidence/2026-09-08-retained-bulk-full-flow.md`, using only its
proved homogeneous estimates and fixed smooth reference. The relative energy
identity is Section 1 of `2026-09-08-relative-background-return.md`; its
Chae--Wolf import is NOT needed for the counterexamples in this note.
The small-cloud global argument is derived in (2.3)--(2.4) and uses the
existing reviewed finite-Lorentz classical continuation consumer in
`docs/proof.md`, not the missing arbitrary-data RF-q producer.

The smooth reference local theory and canonical pressure convention are the
primary local facts already inspected in T. Tao, *254A, Notes 3: Local
well-posedness for the Euler equations*, 9 October 2018:
https://terrytao.wordpress.com/2018/10/09/254a-notes-3-local-well-posedness-for-the-euler-equations/ .
No claim about another equation or a finite-mode model is imported as a
result for original NS. The exact checker covers scale exponents, complete
pressure stresses and difference equations, dissipation/relative-energy
comparisons, and all finite-event scaling formulas. It does not compute or
certify any actual regenerative orbit.
