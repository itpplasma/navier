# Phase-locked NS, helicity-blind critical work, and the full ring's side ladder

Date: 2026-09-08. Mathematical input:
`7cd3444f10fa9f9780f4ef8ac1e73a0ebea689f9`.
Status: author proofs and exact finite arithmetic; independent mathematical
review PENDING. No novelty claim, terminal promotion, or full-turnover
certificate. The R3 assertions below use the original unforced equation,
fixed positive viscosity, its own Leray projection and canonical pressure.
The separate discrete-carrier assertions are explicitly periodic.

## 0. Terminal gate and why these negative tests matter

The terminal implication would be:

    input-only, every-upper-time, M-uniform
    integral Pi_q,M <= nu integral D_q,M + C
    -> W_q,M(t) <= W_q,M(0)+qC
    -> RF-q (Schwartz initial shells have bounded W_q,M(0))
    -> RF-LQ-SYNTHESIS: uniformly bounded L-infinity_t L^{3,q}_x
    -> RF-LOCAL-ID and Lorentz Fatou on each compact classical interval
    -> RF-LQ-CONTINUATION: no finite classical endpoint
    -> LOCAL's normalized smooth pressure/initial trace and ENERGY
    -> NS-R3.

Here q is one fixed finite number bigger than three. The names and exact
hypotheses are in `docs/refinement-proof-graph.yaml` and the reviewed
2026-09-07 Lorentz/whole-space evidence. No new link in that positive chain
is established here. These are falsification tests of proposed prerequisites,
not lemmas falsely advertised as sufficient producers.

The new paired-flow obstruction is quantitative at the ACTUAL Pi interface:
positive accumulated production minus diffusion can be arbitrarily large
while every Fourier-diagonal signed-helicity history vanishes and the
Cartesian Fourier coefficients stay on a fixed imaginary real-vector line.
The inputs vary. A nonzero full-input remainder C is NOT refuted.

The all-order side-ladder theorem and the finite exact jets then identify
what the full symmetric ring does instead of leaving that phase line:
its vector polarizations change, and further carriers are created. Scalar
phase locking modulo pi is not helical phase locking or fixed polarization.

## 1. An exact invariant sector, not a finite-mode truncation

Use angular Fourier frequency in Sections 1, 3 and 4, with exp(i k.x).
For real data odd about zero, u(-x)=-u(x), write

    uhat(k)=i b(k),   b(k) real,   b(-k)=-b(k),   k.b(k)=0. (1)

On R3 these statements hold almost everywhere in frequency. On the torus
they hold at every Fourier coefficient. The full equation becomes

    b_t(k)=-nu |k|^2 b(k)
        + P_k integral_(p+q=k) (q.b(p)) b(q),              (2)

with the integral replaced by the entire ordered sum on the torus, and the
Fourier convolution normalization included on R3. No daughter or return
channel is removed. Equation (2) has real coefficients, including viscosity.

**Theorem 1 (phase line and pointwise spectral helicity).** The local strong
solution of original NS from real odd solenoidal data remains odd throughout
its strong lifespan. The same is true for each exact Fourier-ball projected
flow and for every neighboring difference in the reviewed RF family.
For each such velocity or difference,

    h(k):=conjugate(uhat(k)).[i k cross uhat(k)] = 0,
    |P_+(k)uhat(k)|^2=|P_-(k)uhat(k)|^2=|uhat(k)|^2/2.   (3)

In particular every integrable diagonal weighted signed-helicity quantity
integral m(k)h(k), including angularly resolved weights, vanishes identically
in time. This is stronger than vanishing of radial shell helicity alone.

Proof. The orthogonal transformation u(x)->-u(-x), p(x)->p(-x)
commutes with the original equation, the canonical pressure construction,
and radial Fourier-ball projection. Uniqueness preserves its fixed space.
Equivalently, the right side of (2) preserves reality and oddness of b.
Since i k cross (i b)=-k cross b, the first expression in (3) is
`i b.(k cross b)=0`. The second follows from
P_+/-=(P +/- i k cross/|k|)/2 and |k cross b|=|k||b|.
The single zero frequency is harmless; on the periodic zero-mean sector
it is exactly zero. Differences remain in the same real linear fixed
space. Translation gives the corresponding result about any fixed center,
with the common factor exp(-i k.x0). QED.

The helicity quadratic form is identically zero on this entire real linear
space. Its polarized real bilinear form is consequently zero there too.
Thus energy and helicity do NOT provide two nondegenerate independent
quadratic metrics on this sector. This does not assert that the nonlinear
energy-preserving flow map is a linear orthogonal matrix.

### 1.1 Precisely what phase mechanism this excludes

For a general translation center the phase line is

    phi(k)=pi/2-k.x0 modulo pi.

The convolution factor satisfies
`-i exp(i phi(p)) exp(i phi(q))/exp(i phi(p+q))` real.
It is compatible with every convolution cycle, not just selected triads.
Viscosity multiplies by a real heat factor, not by a dispersive phase.
Therefore compulsory escape from this Cartesian phase line cannot be a
universal NS mechanism, even after all generated modes are retained.

There are important limits. Write b=b1 e1+b2 e2 in a real oriented basis
of k-perp, and use h_+/-=(e1 +/- i e2)/sqrt(2). The two scalar helical
coefficients are

    alpha_+=i(b1-i b2)/sqrt(2),
    alpha_-=i(b1+i b2)/sqrt(2).                            (4)

Their phases CAN rotate when the real vector b rotates. A Cartesian
component can also cross zero and change sign, giving a pi phase jump.
Neither helical-angle torques, sign frustration, nor polarization dynamics
is ruled out by Theorem 1. A Wigner or spatially localized cross-frequency
helicity observable is not a diagonal multiplier m(k)h(k), and is not
covered by (3). The invariant odd symmetry is established prior art;
see the primary-source ledger. No priority is claimed for that symmetry.

## 2. The obstruction reaches the actual RF production, on R3

Let sigma=(1,1,1), let K+ be the six permutations of (2,1,0), and put
v_k=P_k sigma. Choose one nonnegative, nonzero, even smooth compactly
supported Fourier bump phi_delta of sufficiently small radius delta.
Define the R3 datum by

    fhat_delta(xi)=sum_(k in K+) [
       -i P_xi v_k phi_delta(xi-k)
       +i P_xi v_k phi_delta(xi+k)].                       (5)

The supports avoid zero. This is exactly solenoidal, real, odd, and
Schwartz. A positive scalar normalization of the bump does not affect
any conclusion below. Choose delta small enough that the input support
is in the angular ball 5/2 and that its whole quadratic output is in the
angular ball 5. The daughter packets at permutations of (3,3,0), (4,1,1),
and (3,2,1) are outside the angular ball 5/2.

The full source projected onto one such daughter packet is nonzero.
For completeness, at the carrier limit its coefficient is the original
P_(p+q)[(q.a_p)a_q+(p.a_q)a_p] numerator, not an assigned coefficient.
Summing all ordered pairs gives positive-frequency squared source norms
216/25 and 5832/175 for the intended and side rings respectively, in the
normalization of Section 4. For bumps, rescaling the output about its center
and using continuity of P_xi gives this nonzero vector times phi*phi,
plus an error tending to zero relative to it in L2. This is the finite-packet
argument already proved in `2026-09-08-exact-circuit-obstructions.md`,
Sections 2 and 5; it uses no periodic trajectory as an R3 solution.

To match the repository's cycles-frequency convention exactly, set
N0=(5/2)/(2pi), so its projections P_N0 and P_(2N0) are precisely the two
angular balls above. Let U_A and v_A be the actual fine and coarse
whole-space projected solutions from the SAME datum d_A=A f_delta,
with fixed viscosity nu>0. Both are global bandlimited Hilbert-space
flows from RF-R3-FLOW, and neither is a finite-dimensional torus ODE.
Put e_A=U_A-v_A and

    F=(I-P_N0) Q_NS(f_delta,f_delta) !=0.                  (6)

The fine projection in (6) is redundant only for this initial source,
because its whole support is inside the fine ball. Both flows have the
same initial datum, hence e_A(0)=0, and e_A,t(0)=A^2 F.
All resolved corrections are included in e_A.

**Theorem 2 (helicity-blind accumulated refinement work).** Fix nu,H>0,
a finite q>3, and the single sufficiently small delta in (5). For every
L>0 there are a finite A>=1 and 0<t<=H such that

    integral_0^t [Pi_(q,1)-nu D_(q,1)] > L,               (7)

although every diagonal signed-helicity quantity of both projected flows
and their difference is identically zero at every time. They retain the
Cartesian phase line (1) throughout. In particular, an upper bound for
this accumulated work by a budget that vanishes whenever all those signed
helicity histories vanish is false.

Proof. Rescale amplitude and time, not the PDE being claimed:
s=A t, U_A(t)=A U_mu(s), v_A(t)=A v_mu(s), mu=nu/A.
At the two FIXED band cutoffs the polynomial Hilbert-space vector fields
are uniformly locally Lipschitz on fixed L2 balls for 0<=mu<=nu. Their
energy estimates bound those balls. Differentiating the integral equation
once more consequently gives, for one input-selected s0>0 and C<infinity,

    ||U_mu(s)-v_mu(s)-sF||2 <= C s^2,
                      0<=s<=s0, 0<=mu<=nu.              (8)

All constants here concern fixed bands and f_delta; no future critical
norm enters. Choose one positive s<=s0 with Cs<=||F||2/2. Then

    ||e_A(s/A)||2 >= A s ||F||2/2.                        (9)

The reviewed exact production identity, with M=1 and W_(q,1)(0)=0, is

    integral_0^t [Pi_(q,1)-nu D_(q,1)]
                   = N0^(q/2)||e_A(t)||2^q/q.            (10)

Taking A large enough that s/A<=H and the right side of (9), inserted
in (10), exceeds L proves (7). Theorem 1 applies to the two full projected
flows and their entire difference, proving the other assertions. QED.

This is NOT an M-uniform counterexample for one fixed input. The datum
changes with A, exactly as an arbitrary full-input C is permitted to do.
The chosen normalized s is a rigorously controlled short interval, not
an asserted quarter-energy-transfer time or a complete turnover.
No budget counting helical phase rotation or pi sign jumps is asserted to
vanish. These qualifications are necessary, not optional caveats.

### 2.1 Positive critical work for the original unprojected R3 equation

The same obstruction to diagonal signed-helicity budgets is not an artifact
of projecting the dynamics. A direct compact-data construction is available.
Take the preceding helical-production note's

    psi=cos x+cos(2y)+cos(x+2y),  V=(partial_y psi,-partial_x psi,0),
    f_L=curl[theta(x/L) psi e3],                           (11)

but now choose theta nonnegative, nonzero, radial, smooth and compact.
The vector potential is even, so f_L is odd. The full computation and
cutoff limit in that note give

    L^-3 {-<|D| f_L,P[(f_L.grad)f_L]>}
       -> (integral theta^3)(7-3 sqrt(5))/2 >0.           (12)

Here the cutoff-curl error is O(L^-1) pointwise, and the Fourier-multiplier
approximation to |D| on each nonzero carrier is o(L^(3/2)) in L2; hence it
does not change the leading cubic pairing. Fix a sufficiently large finite
L. For datum A f_L the nonlinear production is cubic in A and the viscous
critical dissipation quadratic. At any fixed nu>0, a sufficiently large
finite A gives a genuine interval with

    d_t (|| |D|^(1/2)u||2^2/2)>0.

Theorem 1 makes every diagonal signed-helicity history zero throughout the
actual local strong lifespan, including this growth interval. Both chiral
critical energies grow equally. This strengthens the earlier radial-budget
example to all diagonal angular weights, but supplies no sustained cascade.

## 3. A nonzero side ladder at every input degree, with viscosity retained

This section concerns the full equation on the 2pi-periodic three-torus,
with normalized spatial measure. It is not an R3 solution. Its initial
Fourier coefficients are uhat_A(k,0)=i A b0(k), where

    b0(k)=-P_k sigma on K+,   b0(-k)=-b0(k).               (13)

For fixed nu>0 and finite T, sufficiently small complex |A| gives a strong
solution on [0,T] analytic in A. One elementary justification is the Hm
mild contraction for m>=3: the product maps Hm x Hm to H^(m-1), and the
heat gain has integrable norm C[1+(nu(t-s))^(-1/2)]. Taking |A| small
makes the quadratic integral map contractive. Holomorphic Picard iteration
then gives its homogeneous input expansion. This does not assert an
all-amplitude convergent expansion or real global regularity.

Write uhat_A(k,t)=i sum_(m>=1) A^m B_m(k,t). Set

    p=(0,1,2), q=(0,2,1), k_n=n p+q=(0,n+2,2n+1),
    c=3/5, K_n^2=|k_n|^2=5n^2+8n+5.

**Theorem 3 (exact minimal-degree side ladder).** For every n>=1,

    B_(n+1)(k_n,t)=c_n(t)e1,                              (14)
    c_1'+18nu c_1=2c exp(-10nu t),
    c_n'+nu K_n^2 c_n=-c exp(-5nu t)c_(n-1), n>=2,
    c_n(0)=0.

For every t>0 its sign is (-1)^(n+1), and

    2 c^n t^n exp(-nu K_n^2 t)/n!
       <= |c_n(t)|
       <= 2 c^n t^n exp(-5nu(n+1)t)/n!.                  (15)

The bounds include all original Fourier interactions at this input degree;
no cutoff or hand-deleted reverse channel is used to obtain them.

Proof. A degree-m coefficient has m initial leaves. Since sigma.k_n=3(n+1)
and every initial leaf has axial sum +/-3, a contribution of degree n+1
must use only positive leaves. Every such leaf has nonnegative coordinates.
The zero first coordinate of k_n then forces every leaf to be p or q.
Solving the other two coordinates forces exactly n copies of p and one q.
Heat propagation does not change any of these support statements.

It remains to sum ALL the admissible trees, rather than select one.
For these two input waves the first velocity component is passive, because
all spatial dependence is in x2,x3. The two tangential velocities have
common Laplacian eigenvalue 5. Their two-dimensional streamfunction and
vorticity are proportional, so their full projected tangential convection
vanishes, also for complex coefficients. They therefore evolve exactly by
the common heat factor exp(-5nu t). The normal component obeys the full
linear advection-diffusion equation with that time-dependent tangential
velocity. This is an exact calculation in the exposed positive support face,
not an assertion that the real six-carrier flow is passive.

The initial coefficient vectors are

    b0(p)=(-1,-2/5,1/5),  b0(q)=(-1,1/5,-2/5),
    q.b0(p)=p.b0(q)=-3/5.

At p+q the two ordered source terms each give c e1. To reach n p+q
for n>=2, the only nonzero remaining step adds p to (n-1)p+q:
its coefficient is -c exp(-5nu t)c_(n-1)e1. A normal velocity at a
first-coordinate-zero wavevector cannot advect either tangential parent.
Pure multiples of p have no nonlinear birth. These facts sum the entire
passive evolution coefficient and prove (14).

The integrating-factor formula for (14) is a positive ordered-simplex
integral times 2(-1)^(n+1)c^n. On an interval of the ordered integral with
j completed interactions, its heat rate is

    nu [K_j^2+5(n-j)],  with K_0^2=5.

These rates lie between 5nu(n+1) and nu K_n^2. The simplex volume is
t^n/n!. This proves (15), including strict nonvanishing and the sign. QED.

At zero viscosity the finite-degree identity reads

    c_n(t)=2(-1)^(n+1)(3/5)^n t^n/n!.                    (16)

Equivalently, at any fixed viscosity the coefficient of the first possible
temporal power t^n A^(n+1) in this mode is the same number.
The real solution has further, higher-input-degree contributions at k_n,
including all return interactions; their signs are NOT supplied by (15).
Nothing here says the actual finite-amplitude coefficient has the sign of
its first homogeneous term over a full turnover.

This theorem supplies an explicit infinite side ladder which any faithful
ring representation must account for. It does not prohibit every finite-width
scale-repeating packet ensemble: the ladder can be part of its controlled
tail. Its wavevector length grows linearly with n and its leading coefficients
have a factorial denominator, so it is NOT an amplifying geometric cascade.
The finite-support classification of Kishimoto--Yoneda is separate prior art;
(14) is a concrete coefficient theorem, not a new version of that classification.

## 4. Complete generated jets: polarization changes before scalar phase does

Let b(t)=sum t^n b_n denote the finite Taylor jets of the inviscid homogeneous
part of the full vector field at (13). Equivalently these are the highest
amplitude-degree terms of the fixed-positive-viscosity NS jets. They obey

    (n+1)b_(n+1)=sum_(j=0)^n B(b_j,b_(n-j)),
    B(a,b)_k=P_k sum_(p+q=k) (q.a_p)b_q.                  (17)

Every ordered pair is included. At order n the support is inside the sum
of n+1 initial carriers, hence in the finite box |k_i|<=2(n+1).
Enumerating that recursively generated set is exact finite arithmetic,
not a spatial Galerkin truncation or an approximation of a trajectory.

The attached standard-library checker gives these complete support counts:

    n             0    1    2    3    4    5     6     7     8
    # support    12   24  120  240  504  792  1296  1824  2640.

It proves divergence, odd reality, permutation and sigma-mirror covariance,
energy-coefficient cancellation, and (16) in every checked order. A separate
rotational formula P(u cross curl u) is compared with the advective formula
on an occupied network including parents and both first two jet layers.
This is a second arithmetic implementation, NOT an independent review.

### 4.1 Exact escape from the common meridional polarization

At k=(4,0,-1),

    b_2(k)=(141/425,6/5,564/425),
    (sigma cross k).b_2(k)=9/25 !=0.                     (18)

Thus the full field does not stay in the one-polarization space spanned
modewise by P_k sigma, although its Cartesian Fourier phase line stays
fixed by Theorem 1. The pure top-face example k=(0,4,5) is already given
by (16): b_2=(-9/25,0,0), also not parallel to P_k sigma.

At order three the first exactly transverse layer sigma.k=0 consists of
precisely the permutations and negatives of (3,-2,-1) and (4,-3,-1),
24 modes in total. Two coefficients are

    b_3(3,-2,-1)=(-98886/1145375,-395544/1145375,98886/229075),
    b_3(4,-3,-1)=(84/2125,42/425,-294/2125).              (19)

Every one is perpendicular to sigma. This is also forced by the exact
sigma-mirror symmetry for a wavevector lying in its fixed plane.
These modes are not present in the first or second jets.

For fixed A and nu the leading appearances in (18) and (19) are respectively
i A^3 t^2 b_2(k) and i A^4 t^3 b_3(k). Diffusion preserves support;
three initial leaves have odd axial grading, while two-leaf difference
channels vanish with the common parent heat rate. Therefore no lower-degree
viscous term supplies these missing modes at their displayed first orders.
The calculation retains the full parent back reaction and all differences.

### 4.2 Exact signs of the critical jets, with no trajectory extrapolation

With normalized periodic measure define

    S(b)=(1/2)sum_k |k||b_k|^2,
    S(b(t))=C0+C2 t^2+C4 t^4+C6 t^6+C8 t^8+o(t^8).

This is a finite-jet assertion at nu=0, or about the highest amplitude
homogeneous terms of positive-viscosity NS. Its evenness also follows
from the axial parity in (17). The exact first coefficients are

    C0=36 sqrt(5)/5,
    C2=648 sqrt(2)/25-7344 sqrt(5)/175+5832 sqrt(14)/175.

The checker evaluates all pairings sum_(j=0)^n <|D|b_j,b_(n-j)>/2,
not only the energy of the newly born modes. It certifies with rational
square-root intervals that

    67 < C2 < 68,       49 < C4 < 50,
    -2815 < C6 < -2814, 39739 < C8 < 39740.                (20)

Thus the first complete quartic correction, including the new polarization
and parent corrections, is still positive, but the sextic one is negative.
Neither observation proves restoration, continued growth, or saturation
over a complete turnover. A finite Taylor polynomial is not a remainder
bound at an order-one transfer time. The earlier closed-feedback obstruction
to all-amplitude homogeneous convergence is not bypassed.

The radical certificate uses integers only: for D=10^30, floor(sqrt(r D^2))/D
and the next rational enclose sqrt(r), and multiplication respects the
sign of each rational coefficient. The finite polynomial identities are
computer-assisted arithmetic statements with an explicit justified search
space. They are not proof of an infinite-dimensional evolution estimate.

## 5. Tao gate, sources, and what remains alive

The carrier theorems use the full unaveraged relation k=p+q and its actual
Leray numerator. An explicit failure for Tao's operator is the already
checked same-carrier test:

    <Q_NS(psi_(1,n)),psi_(2,n)>=0,
    <C_Tao(psi_(1,n),psi_(1,n)),psi_(2,n)>
                       =epsilon(1+epsilon0)^(5n/2) !=0.

The first identity is support geometry; the second is Tao's actual Table 1
coefficient (1,1,2,0,0,0). The table was inspected in the primary PDF,
printed page 49. The invariant Cartesian phase line alone is NOT a Tao
separator: an abstract cascade can also use real modal amplitudes.
No quantitative NS-versus-Tao turnover-gain gap has been obtained here.

[T] T. Tao, *Finite time blowup for an averaged three-dimensional
Navier-Stokes equation*, arXiv:1402.0290, Section 6 Table 1 and the local
cascade setting. https://arxiv.org/pdf/1402.0290 .

[M] E. Miller, *Finite-time blowup for the Fourier-restricted Euler and
hypodissipative Navier-Stokes model equations*, arXiv:2307.03434v5,
Section 1 and the carrier/polarization construction.
https://arxiv.org/html/2307.03434v5 . The additional projection is a model
change, and the symmetric odd ansatz is prior art, not a result of this run.

[MS] E. Miller, *Permutation symmetric solutions of the incompressible Euler
equation*, arXiv:2404.01505v3, symmetry discussion in the introduction.
https://arxiv.org/html/2404.01505v3 . No Euler blowup result is imported as
an original positive-viscosity NS statement.

[KY] N. Kishimoto and T. Yoneda, *Characterization of three-dimensional
Euler flows supported on finitely many Fourier modes*, arXiv:2110.08039,
Theorems 1.4 and 5.1, rendered primary PDF pages 6 and 22.
https://arxiv.org/pdf/2110.08039 . Exact finite support over a time interval
is much stronger than finitely supported initial data. Their theorem is
not a quantitative small-tail theorem for a cascade cell.

Rigorous exclusions in this note: compulsory escape from a Cartesian
phase line; control of actual accumulated RF work solely by vanishing
diagonal signed-helicity histories; nondegenerate two-metric reasoning
using only energy and helicity on the odd sector; common-meridional
closure of the ring; and deletion of its explicit higher side ladder.
Helical phase torques, unsigned angular geometry, nonlinear sign changes,
full nonlocal pressure histories, packet broadening and turnover-dependent
return remain possible. No one of these surviving mechanisms is proved.

## 6. Handoff and audit boundary

The next mathematical test must evolve the full real-vector equation (2),
not enforce one meridional polarization and not wait for a forbidden
Cartesian phase escape. A concrete first finite-cell hurdle is to certify
or refute an order-one parent-to-high transfer and its signed critical
work for (13), retaining the entire tail, at normalized times comparable
to 1/4 and effective viscosities near 1/100. The exploratory computation
in the companion discovery note is only a locator for that test.

Even a certified single turnover is NOT RF-q. One must then prove a
scale-uniform return/broadening loss with a telescoping, input-controlled
consumer, or a repeatable cell with inherited tails under control. A loss
merely relative to an ideal Tao pump is not enough: transferring energy
fraction eta to frequency lambda K multiplies squared critical amplitude
by lambda eta. Avoiding gain by this mechanism alone requires eta<=1/lambda,
not merely eta<1. Side energy at comparable high frequencies must be counted.

No original-NS scale-repeating cell, no whole-turnover contraction, no
input-only bound for integral Pi-nu integral D, and no terminal theorem
has been proved. The first terminal gap is unchanged. These results narrow
specific mechanisms; they do not supply a universality theorem reducing
all hypothetical singularities to this symmetric ring.

Checks actually run before the initial commit: `check_phase_locked_ring.py
--order 8`, 81 exact assertions. Author adversarial rechecking covered
Fourier signs, reality, Cartesian versus helical phases, the varying-input
quantifier, the time normalization, full pair support, exposed-face leaf
counting, viscous simplex bounds, and the absence of a full-turnover remainder.
No independent reviewer or spawned agent was available. No Lean build or
full-checkout `research/verify.py --research-only` run is claimed here.
