# Full-duration mixing cascades are not concentrating cascade cells

Date: 2026-09-08. Frozen research input:
`c2c34f870ed0fad5f14030629c5bbf5363006f98`.
Status: AUTHOR PROOF; independent mathematical audit PENDING.
Scope: a finite-duration, arbitrarily-many-but-finite generation test in
original R3 NS. Not an indefinite cascade, a proof of NS-R3, a hexagon
turnover certificate, or a claim of priority for shear mixing / slow variation.

## 0. Terminal contract, and the direction of the new implication

The positive terminal output remains, for one fixed finite q>3,

    integral_0^t Pi_q,M <= nu integral_0^t D_q,M + C(d,nu,H,N0,q),

for EVERY upper time t<=H, uniformly in M. Together with the exact RF identity
and the Schwartz initial bound this gives RF-q; RF-LQ-SYNTHESIS gives uniform
L^{3,q}; RF-LOCAL-ID and Lorentz Fatou identify the classical branch;
RF-LQ-CONTINUATION, LOCAL and ENERGY then prove NS-R3 with canonical pressure.
No estimate of an unknown future strain or critical norm may be inserted.

This note is a NEGATIVE mechanism test. It does not supply that upper bound.
It proves a LOWER bound for the actual accumulated RF work over a finite
forward spectral cascade, while the L^{3,q} norm changes arbitrarily little.
Thus the positive chain does not start with the present theorem. In particular,
large squared-Hhalf gain, even repeated, is not proof of concentrating
regeneration. This distinction is not a new obstruction to arbitrary-data
regularity or to an input-dependent RF-q bound.

The new features relative to the frozen repository are an order-one transferred
energy fraction over a complete fixed normalized interval, arbitrarily many
successive transfers on ONE chosen R3 trajectory, a full-equation error
adapter retaining every 3D mode, and an actual-refinement-work lower bound.
The auxiliary passive-sector mechanism and slow-variation method are prior art.
The data vary with the requested number of generations and error tolerance.

Throughout, |D|=(-Delta)^(1/2) uses ANGULAR frequency. Set

    E(u)=||u||2^2,             C(u)=|| |D|^(1/2)u||2^2.

C is the SQUARED critical Sobolev norm, without the optional factor 1/2.
For the RF comparison in Section 6 the repository's cycles-frequency cutoff
is written explicitly, so factors 2*pi are not silently lost.

## 1. A precise original-R3 theorem

**Theorem 1 (finite repeated spectral transfer without concentration).**
Fix nu,H>0, a finite q>3, an integer J>=1, and 0<eta<1/100. There are real,
central-odd, compactly supported smooth solenoidal data d and d_P on R3,
a number A>0 and a classical ORIGINAL unforced NS solution u from d, and
one u_P from d_P, with the same viscosity nu, with these properties.
Both solutions are smooth through t_J<=H, where

    s_*=2/A,        t_j=3*8^j/A,        K_j=8^j,  0<=j<=J.

Their pressure is the canonical double-Riesz pressure, not a prescribed
forcing or a freely chosen harmonic Hessian. Write E0=E(d)>0.

(a) There is negligible high-frequency preload:

    ||(-Delta-1)d||2 <= eta ||d||2.                         (1.1)

(b) A complete order-one normalized interaction already gives

    ||1_{|D|>11/10}u(s_*)||2^2 >= E0/4,
    C(u(s_*)) >= (6/5) C(d).                               (1.2)

The time 2/A does NOT tend to zero relative to the initial shear clock 1/A.
The transferred fraction is not sent to zero as eta tends to zero.

(c) At the later observation times,

    ||1_{K_j<|D|<=6K_j}u(t_j)||2^2 >= E0/3,                (1.3)
    ||1_{|D|>K_(j+1)}u(t_j)||2^2 <= E0/100,               (1.4)
    C(u(t_(j+1))) >= 5 C(u(t_j)),       0<=j<J.             (1.5)

The frequency bands in (1.3) are disjoint. Between successive observation
times the energy above K_(j+1) consequently increases by at least
97 E0/300. This is actual nonlinear forward transfer, not high-frequency
energy silently supplied in the initial datum or by external forcing.

(d) On the WHOLE interval [0,t_J],

    2nu integral_0^t_J ||grad u||2^2 <= eta E0,              (1.6)
    sup_t ||(u-u_P)^h||2 <= eta ||d||2,                    (1.7)
    sup_t | ||u(t)||_{3,q}/||d||_{3,q} - 1 | <= eta.        (1.8)

Here h means the first two velocity components. The pump-only datum d_P
is specified in the proof. Its horizontal part differs from d^h by a small
solenoidal correction; it is NOT claimed to be exactly identical. Estimate
(1.7) is small loading of the DRIVING planar pump. It is not a claim that
all return interactions, resolved response, or depletion of the advected
parent carrier are small. Those return interactions are retained.

The number J is any prescribed FINITE integer. No single datum is asserted
to satisfy these conclusions for all J. The parameters, energy and initial
critical norm may depend on J and eta. The times grow by a factor eight;
they do not accumulate. No daughter regenerates a comparably rescaled pump.

There is an optional stronger lifespan conclusion using the already published
Chemin--Gallagher theorem: by making the final slow length still larger,
these data can be chosen in its global smooth class. Section 8 checks its
hypotheses. That global result is imported prior art, not a new NS theorem.
The finite-time conclusions (1.1)--(1.8) have the direct proof below.

## 2. An exact full infinite ladder, including both return directions

The elementary auxiliary Euler solution, periodic in x,y and independent
of z, is

    v(tau,x,y,z)=(sin y, 0, 2 sin(x-tau sin y)),   p=0.     (2.1)

This is not claimed to be a finite-energy R3 solution. Its use as an
auxiliary profile is removed by the adapter in Section 4.
Solenoidality and substitution give the entire equation: the horizontal
shear has zero self-convection, the vertical component is passively advected,
and its self-convection and its forcing of the shear are identically zero.
No projection of selected daughters has been made.

For positive auxiliary viscosity mu, replace the shear by exp(-mu tau)sin y
and let w solve

    w_tau + exp(-mu tau) sin y w_x = mu(w_xx+w_yy),
    w(0)=2 sin x.                                         (2.2)

This is likewise an exact 2D3C reduction of the FULL NS equation. In the
positive x-frequency part write w_hat(1,n)=-i f_n. Then the entire ladder is

    f_n'=-mu(1+n^2)f_n
         -(exp(-mu tau)/2)(f_(n-1)-f_(n+1)),  n in Z,       (2.3)
    f_n(0)=1_{n=0}.

Negative partners are fixed by reality. Both off-diagonals in (2.3) are
present. Their coefficient product is -exp(-2mu tau)/4, and their L2 work
cancels by a shift of index. At mu=0 the full transfer operator is
multiplication by exp(-i tau sin y), hence is exactly unitary on L2.
Its infinite Fourier series is obtained directly by expanding this
exponential; no finite closure is imposed. This unitary transfer map can
nevertheless amplify C by arbitrarily large factors on finite intervals.
An energy-unitary map is not a critical-Sobolev contraction.

The transport (x,y,z)->(x-tau sin y,y,z) preserves volume and the value of
the horizontal speed. Consequently the ENTIRE magnitude of (2.1) is an
equimeasurable rearrangement of its initial magnitude. This preserves every
Lp and Lorentz norm on the auxiliary periodic domain, not just its energy.

### 2.1 Why the earlier isolated clean two-carrier pump is not a relay

A useful exact calibration uses the two-carrier classification already proved
in `2026-09-08-exact-circuit-obstructions.md`: nonzero sum production and
vanishing difference production force equal parent lengths R. Resolve the
velocity into its component in the plane of the two carriers and its normal
component. The planar streamfunction is a single Laplacian eigenfunction,
Delta_h psi=-R^2 psi. Hence planar vorticity is proportional to psi and its
transport by the planar velocity is zero. The FULL planar driver is therefore

    v(t)=exp(-nu R^2 t)v(0),

and the normal velocity solves the full passive advection-diffusion equation.
All normal daughters and their returns are retained; none can force the
planar driver because the field is independent of the normal coordinate.
In particular its strain integral is explicitly input-controlled:

    integral_0^infinity ||grad v(t)||infinity dt
         =||grad v(0)||infinity/(nu R^2).

Differentiating the linear passive equation gives global bounds at every
fixed Sobolev order, using this known driver and its higher derivatives.
This rules out an isolated clean two-carrier seed regenerating a new planar
driver. It does not rule out its spectral mixing, adding noncoplanar carriers,
or a genuinely three-dimensional packet departure from the exact sector.
This is a structural consequence of the known 2D3C reduction, not an additional
claim of novelty or a theorem for arbitrary R3 inputs.

## 3. Exact moments imply order-one transfer and repeated critical growth

For a solenoidal field let

    M0=||u||2^2,   M1=||grad u||2^2,   M2=||Delta u||2^2.

For (2.1), with normalized torus volume, divide these moments by the shear's
initial energy 1/2. Direct integration gives

    m0(tau)=5,
    m1(tau)=5+2tau^2,
    m2(tau)=5+6tau^2+(3/2)tau^4.                           (3.1)

For example, with phi=x-tau sin y,

    Delta w=-2(1+tau^2 cos^2 y)sin phi+2tau sin y cos phi.

This calculation includes every Fourier daughter and all return interactions.
It is not an extrapolation of a small-time Taylor polynomial.

Two elementary moment inequalities avoid truncating the infinite ladder.
With spectral variable X=|xi|^2 and positive measure |u_hat(xi)|^2 dxi,
Holder gives

    M1 <= C(u)^(2/3) M2^(1/3),
    M1^(3/2)/sqrt(M2) <= C(u) <= sqrt(M0 M1).              (3.2)

For c>0, if a=M1-cM0>0, Cauchy--Schwarz gives

    ||1_{|D|>sqrt(c)}u||2^2
       >= a^2/(M2-2cM1+c^2M0).                           (3.3)

Indeed a<=integral_(X>c)(X-c)dE and its square is bounded by the high-pass
mass times integral_(X>c)(X-c)^2 dE. Replacing the latter integral by the
full positive integral gives (3.3). Upper tails obey

    ||1_{|D|>B}u||2^2 <= M2/B^4.                          (3.4)

Here is a robust version that the R3 adapter will achieve. For one common
positive normalization B0, suppose at every required time each M_i/B0 differs
from m_i in (3.1) by at most h=1/100. At tau=2, (3.2)--(3.3), c=121/100,
give the exact rational lower bounds

    high-pass mass / initial mass >= 533286649/1609286649 > 1/4,
    [C(tau)/C(0)]^2 >= 81182737/49279863 > 36/25.           (3.5)

This proves (1.2) under those moment bounds.

For the repeated events put X=tau^2>=9 and

    a=5-h + [2-(5+h)/9]X,
    b=5+h + [6-2(5-h)/9]X + [3/2-4/9+(5+h)/81]X^2.

Equations (3.3)--(3.4) show that the energy in
[tau/3,2tau], divided by B0, is at least

    a^2/b - (5+6X+(3/2)X^2+h)/(16X^2).                   (3.6)

This exceeds (5+h)/3 for ALL X>=9. Also

    (5+6X+(3/2)X^2+h)/[(4096/81)X^2] < (5-h)/100,         (3.7)

and

    (5-h+128X)^3
      > 25(5+h)(5+h+2X)(5+h+384X+6144X^2).              (3.8)

The first two prove (1.3)--(1.4) at tau=3*8^j; (3.2),(3.8) prove (1.5).
These are rational polynomial inequalities, not fits to a finite list of
values. After clearing the displayed positive denominators and substituting
X=9+Y, every coefficient is strictly positive. The exact checker records
all coefficients. For example the polynomial for (3.8) has coefficients,
in descending degree in Y,

    558080, 284046528/25, 343337029167/5000,
    52266601122287/500000.

Small absolute moment errors thus leave a strict margin uniformly for the
whole algebraic half-line. The PDE realization below is still only on each
prescribed finite interval; this polynomial uniformity does not construct
one infinite-duration or infinite-generation R3 solution with these bounds.

## 4. The finite-energy R3 adapter, with the full residual retained

### 4.1 Compact planar circular shears with an explicit passive component

Fix a smooth even cutoff chi, equal to one on [-1,1], supported in
[-1-delta,1+delta], 0<=chi<=1. Choose L large and a=m a much larger ODD
integer, a>(2+delta)L. In planar polar coordinates (r,theta) define

    V0(r)=chi((r-a)/L) sin(r-a),
    v0=V0(r)e_theta,
    zeta0=-2 chi((r-a)/L) sin(m theta),
    w0=Delta_h zeta0.                                    (4.1)

These are smooth and compactly supported away from the origin. The vector
v0 is solenoidal and admits a compact smooth streamfunction: choose a radial
antiderivative of V0 that is zero beyond the outer radius and constant
inside the inner radius. All of v0,w0,zeta0 are central-odd in the required
vector/scalar sense because m is odd.

For a parameter b in [0,1] and viscosity 0<=mu<=1, put

    v^b(tau)=b exp(mu tau Delta_h)v0,
    w^b_tau+v^b.grad_h w^b=mu Delta_h w^b,   w^b(0)=b w0.   (4.2)

The heat-evolved planar velocity remains circular. If its azimuthal speed
is V^b, its exact pressure is

    p^b(r)=-integral_r^infinity (V^b(s))^2/s ds.            (4.3)

Thus (4.2),(4.3) solve the full 2D3C equations at each parameter b. At mu=0
there is the explicit formula

    w^b(tau,r,theta)
       =b w0(r,theta-b tau V0(r)/r).                       (4.4)

The variables r,b and the horizontal speed are fixed by this transport.
It preserves r dr dtheta, so the full vector magnitude is equimeasurable
with its initial value, including outside the plateau of chi.

For every fixed finite T, all required Sobolev, weighted Sobolev, bounded
spatial derivative, time derivative and b-derivative norms of (4.2) are
bounded in terms of (v0,w0,T) only, uniformly in b in [0,1], 0<=mu<=1.
Here is an input-only way to see the bounds used below. Heat contraction
bounds every bounded derivative of v^b by a derivative of v0. Differentiating
the linear scalar equation, cancelling its transport term, and using the
product rule gives an H^s bound by exp(C_s T)||w0||H^s. Differentiating in b
produces only lower b-derivatives and derivatives of the explicitly known
v^b; induction gives the same type of finite bound. Polynomial spatial
weights give analogous estimates, since the commutators of Delta and
transport with each fixed weight have lower weight and derivative order.
No norm of a future, unknown 3D solution enters these bounds.
Subtracting the mu=0 equations gives, at any fixed Sobolev order with enough
input derivatives, an O(mu) difference on [0,T]. The forcing is
mu Delta_h w^0 -(v^b_mu-v^b_0).grad_h w^0; the heat difference is O(mu T).
This also proves the uniform inviscid limit used later.

The scalar retains only angular harmonics +/-m. Define zeta^b by

    Delta_h zeta^b=w^b,                                   (4.5)

with the decaying, L2 solution. There is no inverse-Laplacian infrared gap:
for a radial coefficient W(r)e^{im theta} its potential is

    Z(r)=-(1/(2m)) [r^(-m) integral_0^r s^(m+1)W(s)ds
                    +r^m integral_r^infinity s^(1-m)W(s)ds]. (4.6)

The weighted bounds above imply rapid decay of W; the potential decays
like r^(-m), and m>=3 ensures the L2 bounds needed here. It is smooth at
zero by the angular harmonic condition. Every fixed spatial, time and
parameter derivative needed below has finite H^s and bounded-derivative
norm on [0,T]. At tau=0 uniqueness gives zeta^b=b zeta0 EXACTLY.

### 4.2 A genuinely three-dimensional, exactly solenoidal comparison field

Choose a smooth even profile b=b(Z) with 0<=b<=1, equal to one on [-1,1]
and zero outside [-1-delta_z,1+delta_z]. For R>=1 set Z=z/R and define

    U_R^h=v^{b(Z)} - R^(-1) b'(Z) grad_h partial_b zeta^{b(Z)},
    U_R^3=w^{b(Z)},             P_R=p^{b(Z)}.              (4.7)

All planar fields on the right are evaluated at (tau,x_h). Its divergence
is exactly zero: the horizontal correction contributes
-R^(-1)b' partial_b w^b, cancelling partial_z w^b. At time zero,

    d_R=(b(Z)v0 - R^(-1)b'(Z)grad_h zeta0, b(Z)w0),
    d_(P,R)=(b(Z)v0,0).                                   (4.8)

Both are real central-odd C_c^infinity solenoidal R3 data. There is no
periodic tail or unbounded affine velocity in either datum.

Calculate the FULL residual

    f_R=partial_tau U_R-mu Delta U_R
                       +(U_R.grad)U_R+grad P_R.           (4.9)

Its order-zero part vanishes by (4.2). Every remaining term contains at
least one slow derivative or one corrector factor R^(-1); examples include
the vertical pressure gradient R^(-1)b' partial_b p^b, vertical advection,
horizontal correction transports, and vertical diffusion. They are NOT
dropped. For each fixed integer s>=4 and fixed input parameters,

    sup_[0,T] ||U_R||W^(s+1,infinity) <= C_T,
    sup_[0,T] ||f_R||H^s(R3) <= C_T R^(-1/2).              (4.10)

Indeed dz=R dZ, all nonzero terms are supported in a fixed bounded Z set,
and each coefficient and its planar H^s and bounded derivatives are bounded
as just proved. Multiplication by R^(-1) and the L2 volume factor sqrt(R)
give the second bound. Higher slow derivatives only improve it. The checker
expands all three residual components, retaining every power through R^-3.

P_R is an approximate pressure, not asserted to equal the canonical 3D
pressure of U_R. This is harmless: applying the FULL Leray projector to
(4.9) gives its exact projected residual P f_R. In particular one has not
chosen a pressure to suppress any mode of the actual solution.

### 4.3 Stability to an actual NS solution on the complete finite interval

Let u_R be the original R3 solution from d_R with viscosity mu>0, and
write e=u_R-U_R on its initial classical interval. It obeys exactly

    e_tau-mu Delta e
      +P[(U_R.grad)e+(e.grad)U_R+(e.grad)e]=-P f_R,
    e(0)=0.                                              (4.11)

At integer s>=4, the differentiated transport cancellation and product rule
give, with r=||e||H^s,

    r' <= C_T r + C_s r^2 + C_T R^(-1/2).                 (4.12)

The linear coefficient uses W^(s+1,infinity) of U_R, NOT its global H^s
norm, which grows like sqrt(R). This distinction is essential. The self-term
uses ||grad e||infinity<=C_s||e||H^s. Dissipation is nonnegative and need
not be estimated adversely. Regularizing r at zero justifies division.
A bootstrap r<=1 and scalar Gronwall now give

    sup_[0,T] ||u_R-U_R||H^s <= C'_T R^(-1/2)              (4.13)

for sufficiently large R depending on the already fixed parameters. This
also proves existence through T: otherwise the bound, together with the
known finite H^s norm of U_R for that fixed R, contradicts LOCAL's endpoint
alternative. Thus (4.13) is not an assumption of a smooth target 3D solution.
Its reference family is explicitly controlled by heat and a linear equation.
The actual pressure is the canonical pressure from the resulting u_R.

Repeat the argument for the comparison field (v^{b(Z)},0) and datum d_(P,R).
The horizontal parts of the two comparison fields differ by O(R^-1/2) in
L2. Their exact solutions therefore satisfy

    sup_[0,T] ||(u_R-u_(P,R))^h||2 <= C_T R^(-1/2).         (4.14)

Every three-dimensional feedback term in the actual equations is retained
in (4.11); the estimate bounds it rather than deleting it. The constants
can be extremely large. No uniform-in-T, in-J, or in-input bound is asserted.

### 4.4 Moment convergence and the order of parameter choices

For i=0,1,2, (4.7),(4.13) and z=RZ imply, uniformly on [0,T],

    R^-1 M_i(u_R(tau))
      -> integral || |D_h|^i (v^{b(Z)},w^{b(Z)})(tau)||2^2 dZ. (4.15)

Only integer moments are taken in this limit. The fractional and sharp
spectral conclusions follow afterward from (3.2)--(3.4), so no nonlocal
fractional-cutoff convergence is being presumed.

On the annular plateau r=a+y, |y|<=L, put x=a theta, with m=a. Then
m/r->1, r/a->1, derivatives of the moving unit vectors are O(1/a), and
(4.1),(4.4) converge in these local coordinates, through every fixed spatial
derivative on the finite time interval, to (2.1) at b=1. Averaging in theta
is exact because m is an integer. Averaging in y over an interval containing
increasingly many periods gives the normalized y average. The transition
annuli have relative volume O(delta), with fixed-T bounded integrands after
L is chosen large. The b-transition has relative length O(delta_z), also
with bounded fixed-T integrands. The small-mu convergence was proved above.
Consequently, with normalization

    B0=4*pi*a*L*R,

all three M_i(u_R)/B0 can be made uniformly as close as desired to (3.1)
on [0,T]. The factor B0 is half the core volume, not the whole volume.

One safe successive choice is: fix T=3*8^J; fix small delta,delta_z; choose
L large and then an odd integer a/L large; choose mu>0 sufficiently small;
finally choose R sufficiently large. At each stage all constants from earlier
choices are fixed. The limits do not claim that the R3 error constants are
uniform in the earlier geometric parameters. This is an existence proof of
finite data, not a numerically practical value for them.

At tau=0 this gives (1.1), because

    ||(-Delta-1)d_R||2^2=M2(d_R)-2M1(d_R)+M0(d_R),

whose limiting normalized value is zero. Use a tolerance smaller than 1/100
as needed for eta; all the strict inequalities of Section 3 are preserved.
Uniform M1 control and the exact NS energy law give arbitrarily small
relative dissipation by reducing mu. Equations (4.13)--(4.14) give (1.7),
since ||d_R||2 is comparable to sqrt(R) for fixed planar parameters.

Finally choose mu still smaller if necessary so that A=nu/mu>=T/H and A>=1,
and set

    d=A d_R,    d_P=A d_(P,R),
    u(t,x)=A u_R(A t,x),    u_P(t,x)=A u_(P,R)(A t,x).      (4.16)

This is EXACTLY the original equation with viscosity nu, since A mu=nu.
All relative conclusions above survive; t_J=T/A<=H. The viscosity in the
user's target has not been changed. Only the datum has been chosen.

## 5. Why the Lorentz norm is nearly unchanged throughout

Use the inviscid (4.4) comparison at each b(Z). The map

    (r,theta,Z)->(r,theta-b(Z)tau V0(r)/r,Z)

preserves r dr dtheta dZ and leaves b(Z)^2 V0(r)^2 unchanged. It therefore
preserves the full vector magnitude distribution. Its L^{3,q} quasi-norm
is constant for every finite q, including the q fixed in Theorem 1.
This assertion holds on the whole comparison domain, not just on its core.

For fixed planar and b profiles, the small-mu error tends to zero in L3,
uniformly on [0,T], by the L2 and bounded-derivative estimates in Section 4.
After stretching z it has its expected R^(1/3) factor. The horizontal
corrector in (4.7) has L3 norm O(R^(-2/3)), and the exact-solution error
(4.13) has L3 norm O(R^(-1/2)). Both are negligible relative to the leading
norm, which is a positive fixed multiple of R^(1/3). The embedding
L3 into L^{3,q}, q>3, gives the same convergence there.

For completeness, this implies convergence of the actual rearrangement
quasi-norm, not only convergence in an unspecified equivalent norm. For
0<epsilon<1 the standard distribution inequality gives

    (f+g)^*(s) <= f^*((1-epsilon)s)+g^*(epsilon s),
    ||f+g||_(3,q) <= (1-epsilon)^(-1/3)||f||_(3,q)
                         +epsilon^(-1/3)||g||_(3,q).

Apply this in both directions, take the uniform error to zero for fixed
epsilon, and then take epsilon to zero. The equimeasurability of the
reference flow makes the conclusion uniform in tau. Selecting the preceding
parameters sufficiently accurately gives exactly (1.8). This completes the
proof of Theorem 1.

Real central oddness is preserved by the actual flow and its ball projections,
as already proved in the frozen phase-locked-ring note. Accordingly all its
diagonal signed-helicity histories vanish throughout these full-duration
examples. This uses the existing symmetry theorem; it does not assert that
all helical angles are fixed or that every real Fourier coefficient retains
its sign.

## 6. A lower bound for the ACTUAL accumulated RF work

This section concerns the true neighboring projected solutions, not just
Fourier pieces of the unprojected solution. Use the repository transform
exp(-2*pi*i*x.xi). Take

    N0=1/pi,   N_l=2^l N0,   angular cutoff k_l=2*pi*N_l=2^(l+1),
    e_l=u_(N_(l+1))-u_(N_l),
    W_q,M=sum_(l<M) [N_l^(1/2)||e_l||2]^q.

Classical identification on the smooth interval of Theorem 1 gives
u_N(t)->u(t) in L2 as N->infinity. For an angular dyadic K=8^j, j>=1,
choose l0=3j-1, so k_(l0)=K. Since u_(N_(l0)) has no frequencies above K,

    1_{|D|>K}u(t)=sum_(l>=l0) 1_{|D|>K} e_l(t)             (6.1)

in the limiting telescoping sense. If the supremum of the weighted errors
is finite, geometric summation gives

    sup_l N_l^(1/2)||e_l(t)||2
       >= (1-2^(-1/2)) sqrt(K/(2*pi))
                                  ||1_{|D|>K}u(t)||2.    (6.2)

If it is infinite, the resulting lower bound is automatic. No unknown
upper bound is used. By (1.3),

    sup_M W_q,M(t_j) >= c_q K_j^(q/2) E0^(q/2),
    c_q=[(1-2^(-1/2))/sqrt(6*pi)]^q.                      (6.3)

At the initial time e_l(0) is just the shell of d between k_l and 2k_l.
Equation (1.1), k_l>=2, and k_l^2-1>=(3/4)k_l^2 give

    W_q,infinity(0) <= B_q eta^q E0^(q/2),
    B_q=[4/(3sqrt(2*pi))]^q
                   *2^(-3q/2)/(1-2^(-3q/2)).             (6.4)

The exact full-error identity therefore proves

    sup_M integral_0^t_j [Pi_q,M - nu D_q,M]
      >= (E0^(q/2)/q)[c_q K_j^(q/2)-B_q eta^q].            (6.5)

This is the precise connection to the terminal integrand. It is a LOWER,
not an upper, estimate. It retains all resolved changes, all refinement
levels in the telescope, and the original pressure and nonlinearity.
A bound depending arbitrarily on the full input is NOT contradicted:
the datum and its initial norms depend on J, eta and the chosen slow lengths.
For these data (1.8) holds simultaneously. The RF sufficient condition is
stronger than merely tracking the size or change of the L^{3,q} norm.

There is also a direct exact signed-work identity for the unprojected C:

    integral_0^t <Q(u),|D|u> ds
      -nu integral_0^t || |D|^(3/2)u||2^2 ds
        = [C(u(t))-C(d)]/2.                               (6.6)

It is positive at s_* by (1.2) and grows through the finite sequence. It
is not substituted for Pi_q,M; (6.5) is the separate refinement adapter.

## 7. What is eliminated, and the genuinely unfilled part

These results exclude the following universal implementations, in the
stated varying-input class, even over complete finite transfer intervals:

* energy-unitary full transfer plus return coefficients implies nonincrease
  of the physical squared-Hhalf norm;
* every order-one forward spectral transfer forces a fixed positive
  fraction of driver loading, viscous energy expenditure, or Cartesian
  phase escape, independently of the full input;
* arbitrarily many such finite spectral transfers alone certify spatial
  concentration, regeneration, or approach to a singularity.

The second item concerns EACH named cost, or their sum: (1.6),(1.7) and
odd invariance can make them simultaneously small. It does NOT include all
side-mode work, all passive-parent response, a nontrivial helical-angle cost,
nonlocal pressure-history cost, or an arbitrary full-input remainder.
Likewise the construction does not exclude an input-controlled count of
these events or a scale-weighted dissipation cost that tends to zero.

The last item is a statement about the insufficiency of the proposed
diagnostic, not a theorem that concentrating cascades cannot occur. The
optional global smooth realization in Section 8 makes this especially clear.

There is NO new positive universal turnover contraction. In fact even a
strict loss relative to an ideal pump would not suffice by itself: a cell
retaining fraction theta at a scale lambda higher still has squared critical
gain lambda*theta, which may exceed one.

For this particular mixing construction, the missing regenerative feature
is explicit, not hidden in an error estimate. Frequencies are of size tau,
while the driving shear remains at frequency one. The observation times
satisfy t_(j+1)=8t_j; the waits INCREASE, rather than following K_j^-2.
The vertical field has no leading-order vertical self-transport. The
3D corrections can be made arbitrarily small for the chosen finite sequence,
so they do not supply a new higher-scale driver in this theorem. The L^{3,q}
norm stays almost constant. Sending J to infinity requires changing the
input and all auxiliary lengths/viscosity parameters; it is not a limiting
construction of one Schwartz-data singular solution.

The current hexagon test at nu=.01, tau<=.25 remains an unproved benchmark.
It may still be useful for genuinely 3D pump regeneration; Theorem 1 neither
certifies that trajectory nor proves that it has the passive architecture.
No arbitrary-blowup reduction to the hexagon has been obtained.

**One dominant remaining mathematical nut:** a concentration-producing,
critically timed packet-regeneration cell, with inherited tails included.
The next successful negative construction must show that the daughter
actually drives the NEXT transfer on its own critically scaled time, not
just that a fixed coarse shear can mix it to higher frequencies. The next
successful positive proof must bound the cumulative signed work of these
regenerating cells and prove a covering/summation into Section 0. A theorem
only about one symmetric ring cannot silently supply that covering.
The exact finite benchmark and a sharpened packet-level test are retained
in PLAN; neither is advertised as equivalent to NS-R3.

### 7.1 A diagnostic that the mixing example cannot fake

This is a specification for the next NEGATIVE construction, not a new positive
regularity criterion. Fix once and for all a smooth radial multiplier psi,
0<=psi<=1, supported in (2/3,5/3), equal to one on [3/4,3/2]. Let Q_K have
symbol psi(|xi|/K) in angular frequency, let v_K=Q_K u, and define

    a_K(u)=K^(1/2)||v_K||2,
    gamma_K(u)=||Q_(2K) P[(v_K.grad)v_K]||2
                         /(K^(5/2)||v_K||2^2),             (7.1)

with gamma=0 if v_K=0. The trajectory is NEVER projected to this annulus;
(7.1) only measures its daughter's ability to produce the next daughter.
The high-frequency field of the exact passive ladder has gamma=0: it cannot
regenerate its own driver, despite its growing a_K.

This diagnostic has a direct critical meaning. If G is the convolution kernel
of Q_1, the rearrangement Holder inequality gives

    ||Q_K u||infinity <= K ||G||_(3/2,q') ||u||_(3,q),

where 1/q+1/q'=1. Also ||grad v_K||2<2K||v_K||2. Consequently

    gamma_K(u) a_K(u) <= 2||G||_(3/2,q') ||u||_(3,q).       (7.2)

This is proved by the two displayed inequalities, not by a sharp-ball Lp
multiplier assertion. The kernel is Schwartz. In particular an actual
recursion with a_K increasing without bound and gamma_K bounded below would
force growth in the very Lorentz norm used by the terminal consumer. Large
a_K alone, as in Theorem 1, does not. No converse or singularity extraction
is claimed; a smooth growing-norm field can also have small gamma.

The concrete two-turnover packet challenge specified in PLAN uses (7.1),
the original hexagon packet initial family, and the ACTUAL inherited state
on its second leg. It is an unproved finite regenerative benchmark. Proving
it would still require a robust repeated-neighborhood / tail argument for
an indefinite cascade. Refuting it would only eliminate that stated family
and thresholds, not every original-NS cascade.

## 8. Primary-source checks and exact applicability

[CG] J.-Y. Chemin and I. Gallagher, *Large, global solutions to the
Navier--Stokes equations, slowly varying in one direction*, arXiv:0710.5408v2,
https://arxiv.org/html/0710.5408v2, Theorem 3 and its following remarks.
The statement concerns original R3 NS, unit viscosity, with initial data
(v0^h+epsilon w0^h,w0^3)(x_h,epsilon x3). The horizontal v0^h and all its
derivatives must be L2 and L2_(x3) Hdot^(-1)_(xh); w0 is smooth solenoidal.
For fixed profiles and sufficiently small epsilon it gives global solutions.
It is not a theorem for every large R3 datum.

Our optional global conclusion is an exact specialization. At auxiliary
viscosity mu>0, divide the initial velocity by mu and rescale time to unit
viscosity. Choose the source profiles

    v0^h(x_h,Z)=mu^-1 b(Z)v0(x_h),
    w0^h(x_h,Z)=-mu^-1 b'(Z)grad_h zeta0(x_h),
    w0^3(x_h,Z)=mu^-1 b(Z)Delta_h zeta0(x_h),
    epsilon=R^-1.

The full w0 is divergence-free. The horizontal v0 is a rotated gradient
of a compact smooth streamfunction; its planar Hdot^-1 norm and those of
all derivatives are finite, as is their Z integral. All source profiles
are compact smooth. Thus every hypothesis holds, and R may be chosen
larger than both the finite-time adapter threshold and the CG threshold.
This only imports lifespan; none of the quantitative transfer conclusions
(1.1)--(1.8) is attributed to CG. No novelty is claimed for this data class.

[T] T. Tao, *Finite time blowup for an averaged three-dimensional
Navier--Stokes equation*, arXiv:1402.0290v3,
https://arxiv.org/html/1402.0290v3, Sections 5.1 and 6, especially Table 1.
The auxiliary pump and assigned cascade coefficients belong to the averaged
operator, not original NS. The existing exact discriminator remains the
same-carrier convolution support identity, violated by Table 1's
(1,1,2,0,0,0) coefficient. The new proof additionally uses the genuine
transport reduction (2.2), exact incompressibility, and canonical pressure
in the slow adapter. Arbitrary assigned pump coefficients need not possess
this reduction. No positive RF bound is obtained from that discriminator.

[CDP] A. Cheskidov, M. Dai and S. Palasek, *Instantaneous Type I blow-up and
non-uniqueness of smooth solutions of the Navier--Stokes equations*,
arXiv:2511.09556v2, https://arxiv.org/html/2511.09556v2.
Inspected Theorem 1.1, Remark 1.4, Theorem 1.7, and Sections 2.6 and 4.2--4.3.
Their original-NS inverse cascade is a relevant exact-operator construction,
not a counterexample to this repository's target. The singular limit is
from the RIGHT of the chosen time, with energy entering from infinite
wavenumber; their solutions are not L-infinity_t L2_x or L2_t H1_x near it.
Their whole-space statement does not provide the decaying finite-energy
Schwartz-data forward blowup required here. Time reversal changes the sign
of viscosity and cannot convert it to the terminal counterexample.
No theorem from CDP is used in the proof above; no new exclusion of all
possible forward adaptations is asserted.

Repository inputs: the reviewed full-error identity, LOCAL/ENERGY,
RF-LOCAL-ID, Lorentz synthesis/continuation, and the central-odd invariance
result at the frozen input. Their scopes and statuses are unchanged.

## 9. Verification and author audit boundary

`research/check_turnover_mixing.py` checks 97 exact assertions: the complete
shear equation and Laplacian, exact integer moments, full-support ladder
Taylor rows and moments through degree eight, strict rational moment
inequalities on the ENTIRE half-line X>=9, the exact slow-coordinate
divergence correction, all residual components including vertical pressure,
and frequency/scaling factors. These checks do not prove the PDE adapter,
parameter limits, Lorentz continuity or imported global-existence theorem.
The written analytic argument carries those obligations.

An author adversarial pass checked in particular: finite energy rather than
periodic substitution; m odd and the inverse-Laplacian infrared issue;
W^(s+1,infinity) rather than growing global H^s as the stability coefficient;
the order of geometric, inviscid and slow limits; pressure normalization;
the difference between driver loading and all return channels; the distinction
between a Sobolev SQUARED-norm gain and an L^{3,q} gain; and the finite-J
quantifier and increasing rather than accumulating generation times.
This is self-review, NOT an independent mathematical audit.

No agent spawning or independent reviewer was available in this session.
No canonical graph status is promoted. The user-defined terminal/
critically-regenerating breakthrough has NOT been reached by this note.
