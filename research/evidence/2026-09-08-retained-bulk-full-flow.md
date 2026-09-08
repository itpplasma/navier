# Retained bulk can be dynamically invisible but destroy full-energy normalization

Date: 2026-09-08. Frozen input:
`cf3658b381ee64556e17d68b97abb667952e68ab`.
Status: AUTHOR PROOF; independent mathematical audit PENDING. No canonical
promotion and no priority claim for the standard homogeneous stability method.

## 0. Consumer, falsification target, and exact scope

The preceding no-atom block theorem proves an actual positive-viscosity cost
and excludes long high-amplitude returns in a noncompact class. It still
requires bounded normalized FULL energy at the first and final endpoints.
This note tests the attempted inference

    efficient large critical packet + controlled complete normalized tube
       -> bounded normalized full energy, or a required critical bulk cost.

That inference is false even along an entire fixed-duration ORIGINAL NS
flow interval. A retained fixed physical bulk can dominate the full energy,
yet disappear in the critical velocity comparison and canonical pressure
comparison throughout that interval. This is a DYNAMICAL counterexample,
not just the earlier static small-power vorticity satellite.

It does NOT refute the no-atom block theorem, because no sequence of scale
and amplitude gains is constructed here. It does not prove that the mandatory
regenerative angular exterior is harmless. It only proves that large full
normalized energy can be caused by an independently harmless retained bulk.
Distinguishing that bulk from the dynamically essential exterior remains
necessary; deleting either from the actual evolution is not justified.

The terminal consumer remains

    input-only RF-q upper producer -> exact RF identity -> RF-q
      -> RF-LQ-SYNTHESIS -> RF-LOCAL-ID and Lorentz Fatou
      -> RF-LQ-CONTINUATION -> LOCAL and ENERGY -> NS-R3.

No edge missing from this chain is supplied here. The immediate consumer is
the no-atom extension audit: the false inference above cannot discharge its
endpoint-energy hypothesis. A finite reference-flow approximation below is
also available for testing a genuinely constructed finite Euler cell, but
is not a uniform infinite-cascade shadowing theorem.

## 1. Full-flow approximation with large L2 error and small critical error

Write

    X(z)^2=||grad z||2^2+||grad^3 z||2^2,
    Z(z)=||Lambda^(1/2)z||2.                              (1.1)

All third derivatives are counted as an ordered derivative tensor; its L2
norm equals ||Lambda^3 z||2. These are homogeneous norms of the actual
finite-energy fields, not quotient states with a deleted constant or bulk.

Fix real solenoidal Schwartz f, a nonzero real solenoidal compactly supported
smooth h, fixed nu>0, and 0<alpha<1/2. The support of h may be separated from
the origin, for example h=curl[eta(x-3e1)e3] with eta a nonzero unit-ball bump.
Let w be the smooth finite-energy Euler solution from f on any FIXED closed
interval [0,theta] contained in its smooth lifespan. Its pressure is canonical.
Such a positive interval exists by the inspected local theorem [T], and the
argument below also applies to any longer interval where w is actually known
to remain smooth. No global Euler regularity is assumed.

For K tending to infinity put A=K^alpha and set the ORIGINAL NS datum

    d_K(x)=A K f(Kx)+h(x).                               (1.2)

These are admissible real solenoidal Schwartz data for the same positive
physical viscosity nu. Let u_K be its maximal smooth NS solution, and define
its ENTIRE normalized velocity and pressure by

    U_K(tau,y)=u_K(tau/(A K^2),y/K)/(A K),
    P_K(tau,y)=p_K(tau/(A K^2),y/K)/(A^2 K^2),
    mu_K=nu/A.                                          (1.3)

The equation for U_K is exactly original NS with viscosity mu_K, and
P_K=R_i R_j(U_K,i U_K,j). The initial condition is

    U_K(0)=f+H_K,       H_K(y)=(A K)^(-1)h(y/K).           (1.4)

**Theorem 1 (retained-bulk finite-interval approximation).** For all large K,
u_K is smooth through theta/(A K^2). For every one fixed finite q>3,

    sup_(tau<=theta) [X(U_K-w)+Z(U_K-w)] <= C (1+nu)/A,
    sup_(tau<=theta) ||U_K-w||_(3,q) <= C_q (1+nu)/A,
    sup_(tau<=theta) ||P_K-p_w||H1 <= C (1+nu)/A.         (1.5)

Constants depend on f,h,theta and the smooth reference bounds, but not K.
The estimates apply to the entire actual U_K, including every generated
mode, reverse interaction, pressure contribution and inherited bulk.
There is no independent evolution or reset of h after the initial time.
Nevertheless,

    ||H_K||2=K^(1/2-alpha)||h||2 -> infinity.              (1.6)

In particular (1.5) is not obtained from a uniform inhomogeneous-Hs bound
for U_K or from a small global L2 difference.

### Proof: close the derivative estimates without the large L2 norm

The exact initial scalings are

    ||grad^r H_K||2=A^(-1)K^(1/2-r)||grad^r h||2,
    Z(H_K)=A^(-1)Z(h),
    ||H_K||_(3,q)=A^(-1)||h||_(3,q).                     (1.7)

For every smooth finite-energy z, Fourier Cauchy--Schwarz below and above
|xi|=1, followed by Sobolev embedding for grad z, gives

    ||z||infinity+||grad z||infinity+||grad^2 z||2
         +||grad^2 z||3+||grad^2 z||6 <= C X(z).          (1.8)

For clarity, the low-frequency integral for ||z||infinity uses
integral_(|xi|<1)|xi|^(-2) dxi<infinity; the high-frequency integral uses
integral_(|xi|>1)|xi|^(-6) dxi<infinity. For the gradient, interpolate the
second derivative between the first and third; grad z then belongs to H2.
The L6 estimate for grad^2 z is the homogeneous H1 Sobolev inequality, and
its L3 estimate follows by interpolation. No ||z||2 appears in (1.8).

Write z=U_K-w and mu=mu_K. Subtract the equations EXACTLY:

    z_tau-mu Delta z
      +P[((w+z).grad)z+(z.grad)w]=mu Delta w.             (1.9)

For a derivative order m=1 or 3, test (1.9) against that derivative of z.
The Leray projector is orthogonal and commutes with derivatives. The full
transport term (w+z).grad(grad^m z) cancels because div(w+z)=0. Ordinary
viscosity contributes -mu||grad^(m+1)z||2^2 and is retained as dissipation.
For m=3 the remaining transport products have derivative counts

    (1,3), (2,2), (3,1)

on (w+z,z). Bound these respectively in (Linfinity,L2), (L3,L6), and
(L2,Linfinity), using (1.8). For (z.grad)w the counts are

    (0,4), (1,3), (2,2), (3,1)

on (z,w). Use the fixed H5 bound for w, z in Linfinity, and derivatives of
z in L2 or Linfinity from (1.8). The m=1 terms are the corresponding simpler
products. Thus, after the usual regularization at X=0,

    d_tau X(z) <= C_w X(z)+C X(z)^2+mu C_w,              (1.10)

where C_w is controlled by 1+sup_[0,theta]||w||H5. This is a reference-flow
constant, not an unknown norm of the target NS solution. On the bootstrap
X<=1, ordinary integration on the FIXED interval yields

    sup X(z) <= C_(w,theta)[X(H_K)+mu]
               <= C [A^(-1)K^(-1/2)+nu/A].              (1.11)

For large K this is strictly smaller than the bootstrap threshold. Estimate
(1.8) then bounds the entire U_K and grad U_K in Linfinity throughout the
interval. The standard high-Sobolev energy estimate

    d_tau ||U_K||Hs^2 <= C_s ||grad U_K||infinity ||U_K||Hs^2

with its nonpositive viscous term extends each smooth solution through theta;
its initial Hs norm need only be finite for that K, not uniform in K. This
prevents a shorter NS lifespan from invalidating the bootstrap. The smooth
local theory and continuation input are within the inspected scope of [T].

### Retain the critical norm, rather than infer it from X

Small X alone does NOT imply small Z, so this step cannot be omitted.
For 0<s<1 the homogeneous Gagliardo seminorm is, up to its fixed constant,

    integral integral |z(x)-z(y)|^2/|x-y|^(3+2s) dx dy.

For divergence-free Lipschitz transport b its differentiated transport
contribution is bounded in absolute value by
(3+2s)||grad b||infinity times the seminorm. This follows directly by
integration by parts in x and y: the kernel derivative is multiplied by
b(x)-b(y), whose size is at most ||grad b||infinity |x-y|. At s=1/2 the
factor is 4. The pressure pairing still vanishes, since z is solenoidal.
Ordinary viscosity is nonpositive in this seminorm as well.

The same double-integral formula and the identity

    a(x)z(x)-a(y)z(y)
       =a(x)[z(x)-z(y)]+z(y)[a(x)-a(y)]

give the elementary fractional product inequality

    ||a z||dotHhalf <= C[||a||infinity Z(z)
                                      +||z||infinity ||a||dotHhalf].

Apply it componentwise to (z.grad)w, use (1.8), and retain mu Delta w in
(1.9). On the already closed X bootstrap this gives

    d_tau Z(z) <= C_w Z(z)+C_w X(z)+mu C_w.              (1.12)

The finite reference constants include ||grad w||dotHhalf and
||Delta w||dotHhalf, both bounded by its H5 norm. Integrating (1.12), with
Z(H_K)=A^(-1)Z(h), proves the first line of (1.5). The homogeneous Sobolev
embedding dotHhalf into L3, followed by L3 into L^{3,q} for q>3, proves its
second line. No false homogeneous embedding X into the critical norm is used.

Finally Z(z) controls ||z||3 and X(z) controls ||z||infinity, hence
||z||4 <= ||z||3^(3/4)||z||infinity^(1/4) tends to zero at the stated rate.
For the ACTUAL canonical pressures, the L2 Riesz bound and product rule give

    ||P_K-p_w||2 <= C[2||w||4||z||4+||z||4^2],
    ||grad(P_K-p_w)||2
       <= C[||z||infinity||grad w||2
                  +(||w||infinity+||z||infinity)||grad z||2].

This proves the final line of (1.5). There is no hidden harmonic pressure or
unmeasured remote forcing. This completes the proof of Theorem 1. QED.

## 2. An efficient critical core while full normalized energy diverges

Choose f as above with ||Q_1 f||2=1 and gamma_1(f)>0. Such real Schwartz f
exists without an unproved cascade construction. For example take smooth
even nonnegative sufficiently narrow Fourier bumps about

    k=(6/5,0,0), q=(0,6/5,0)

and their negatives, polarizations a=e2,b=e3, pure imaginary odd phases,
and the exact pointwise Leray projector. Both parents lie strictly inside
the Q_1 plateau, while k+q lies strictly inside the Q_2 plateau. The exact
symmetrized Leray numerator at their sum is

    P_(k+q)[(a.q)b+(b.k)a]=(6/5)e3 !=0.

At sufficiently small fixed width its third component keeps one sign in
this sum channel; the other carrier pairs do not reach that neighborhood.
Thus the projected Schwartz convolution is nonzero. Normalize its L2 norm.
This is only an existence witness for nonzero gamma, NOT a next-driver or
a regenerative cell; the known passive-sector warnings remain in force.

By continuity choose a fixed theta>0 inside the Euler lifespan so that on
[0,theta] the reference annular norm is in [3/4,5/4] and

    gamma_1(w(tau)) >= (3/4)gamma_1(f)>0.

There is no truncated Taylor series here. Theorem 1 approximates the whole
Euler trajectory on that interval by the whole original NS trajectory.
Annular continuity follows directly from (1.11): Q_1 and its derivatives
map dotH1 to the needed L2 and Linfinity norms, and the denominator stays
away from zero. Therefore, for large K, uniformly throughout the interval,

    b_K(tau):=||Q_1 U_K(tau)||2 in [1/2,2],
    gamma_K(u_K(tau/(A K^2)))=gamma_1(U_K(tau))
                                   >= gamma_1(f)/2,
    a_K(u_K(tau/(A K^2)))=A b_K(tau) -> infinity.          (2.1)

The complete normalized tubes have uniformly bounded grad U_K in BOTH L2
and Linfinity. Their duration theta/(A K^2) is comparable, with fixed
constants, to the instantaneous nonlinear clock 1/(a_K K^2). This does
not assert a transfer to 2K or a multiplicative daughter gain.

**Corollary 2 (dynamical failure of full-energy normalization).** The above
actual solutions satisfy, uniformly over this entire interval,

    ||d_K||2^2 -> ||h||2^2 >0,
    2nu integral_0^(theta/(A K^2)) ||grad u_K||2^2
                                      <= C nu A/K ->0,
    ||u_K(t)||2^2 -> ||h||2^2,
    ||U_K(tau)||2^2=(K/A^2)||u_K(tau/(A K^2))||2^2
                                      ->infinity.        (2.2)

Indeed the physical core's initial energy is A^2/K times ||f||2^2, which
tends to zero; its cross term with h also tends to zero by Cauchy--Schwarz.
The entire normalized enstrophy is bounded by Theorem 1. Exact change of
variables then gives the dissipation bound in (2.2), with no separate pump
or bulk energy identity. The original full energy identity gives the rest.

Even the EXACT current annular normalization

    V_K(tau)=U_K(tau)/b_K(tau)

has ||Q_1 V_K||2=1, gamma_1(V_K)>=gamma_1(f)/2 and ||V_K||2 tending to
infinity throughout. The divergence is not a wrong normalization by A
instead of the measured critical amplitude.

Meanwhile Theorem 1 shows that the extra bulk is dynamically invisible in
all the stated critical comparisons; the canonical pressure comparison also
vanishes. These conclusions hold with the same physical h and nu, while
the localized critical core varies with K. No datum is being claimed to
traverse this K-indexed family in time.

## 3. Sharp meaning of this obstruction and the remaining theorem

This construction kills the general a priori inference in Section 0,
including its full-interval version. It is stronger than a static satellite
because the complete original equation, its pressure and the generated
feedback have all been followed on a fixed normalized interval.
It does NOT show that the endpoint-energy hypothesis can be removed from,
or is unnecessary in, a theorem about MANY genuinely regenerative gains.
Additional dynamical information from those gains may impose restrictions
that this example does not satisfy. No positive regenerative turnover, robust
two-cell orbit, invariant neighborhood, or infinite cascade is certified.

The proof's reference constants depend on the fixed smooth Euler tube. They
are not uniform over a hypothetical singular Euler trajectory or indefinitely
many returns. Therefore Theorem 1 is NOT the infinite shadowing theorem
required for an original-NS blowup construction. Initial critical norms also
grow with K; bounded physical energy here is not bounded full input data.

There is also a precise consequence of the preceding no-atom Corollary 3.
An infinite exact orbit with its uniform full-gradient bounds, clocks and
gains, and with gamma uniformly bounded below, must obey

    ||V_n||2 -> infinity,
    ||Q_(K_n)u(t_n)||2^2 / ||u(t_n)||2^2 = 1/||V_n||2^2 ->0.

Otherwise two sufficiently late energy-bounded efficient endpoints would
violate that corollary. Thus, IN THAT RETURN CLASS, any surviving orbit must
have a vanishing annular energy fraction. This is a necessary condition,
not existence or extraction of such an orbit. The present construction shows
why efficient finite-time packets alone cannot exclude that fraction regime.

The no-atom positive-viscosity block theorem is preserved. Its physical
cost weight a^2/K is exactly the vanishing weight displayed by (2.2).
One cannot repair the missing critical budget by charging this harmless
full-energy bulk, nor by deleting it and assuming the remainder is autonomous.

ONE dominant nut remains: determine the full-state critical return with
inherited dynamically essential exterior, allowing vanishing core-energy
fraction and distinguishing harmless bulk without deleting it. Either
construct a robust scale-repeating concentrating orbit and shadow it in
original NS with summable errors, or prove a REQUIRED critical cost,
extract the relevant events from hypothetical blowup, and feed the complete
RF-q/Lorentz consumer. Neither arbitrary blowup extraction nor single-annulus
amplitude growth as a necessary singularity mechanism is proved here.

## 4. Source and verification scope

[T] T. Tao, *254A, Notes 3: Local well-posedness for the Euler equations*,
9 October 2018,
https://terrytao.wordpress.com/2018/10/09/254a-notes-3-local-well-posedness-for-the-euler-equations/ .
Directly inspected whole-space canonical-pressure setup, Theorem 1's
viscosity-uniform high-Sobolev estimates, Corollary 3's local smooth Euler
existence, and the difference/continuation discussion. We use those local
facts, NOT a global Euler or Navier--Stokes assertion. The homogeneous
large-L2 comparison needed here is proved explicitly in (1.8)--(1.12).

The extra exact checker tests the scalings, complete difference equation,
Leibniz derivative counts, fractional product identity, carrier numerator,
and exponent signs. These are finite symbolic identities, not validation
of PDE estimates, an independent audit, interval numerics or a recurrent
original-NS state. No external publication or canonical proof promotion.
