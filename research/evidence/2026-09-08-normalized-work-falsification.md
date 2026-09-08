# Infinite normalized angular work in globally small unforced Navier--Stokes

Date: 2026-09-08. Input: ececd70fc6115318f78a2aca121254952d59529c;
concurrent formal-core record 373bd3e0504df775434ad579607ded9481af624f preserved.
Status: AUTHOR PROOFS, independent mathematical audit pending. No literature
priority claim. All solutions here are ORIGINAL unforced whole-space NS at
fixed nu>0, with real Schwartz data and canonical pressure. No modified flow,
Galerkin equation, or merely formal time series is used.

## 0. Exact assertion being falsified

The predecessor angular-preparation theorem defines

    B=Pi_0 u, z=u-B, v_n=Pi_n u,
    G_n=-Pi_n P[(z.grad)z],
    W_n^+(t)=integral_0^t [Re<G_n,v_n>]_+/||v_n||2^2 ds.     (0.1)

It correctly treats W_n^+ as an extended nonnegative integral and explicitly
does NOT bound it by the input. The possible promotion of this quantity into
an input-summable critical cost is now falsified more sharply: it can be
INFINITE during an ordinary mode birth in a globally regular solution whose
L3 norm remains arbitrarily small. With a nonzero initial seed it is unbounded
on a Schwartz-compact family of uniformly globally small solutions.

This does not retract the predecessor's occupation/work inequality. It kills
using its normalized work alone, or a cost dominating it, as a finite
arbitrary-data budget. It is not a proof against every possible work
functional restricted to genuine large-amplitude concentrating events.

## 1. An explicit Schwartz parent with an actual angular daughter

Write (x,y,z) for Cartesian coordinates, r^2=x^2+y^2, and set

    F=exp[-(x^2+y^2+z^2)], psi=x F,
    d=(partial_y psi,-partial_x psi,0)
      =(-2xy,2x^2-1,0)F.                                  (1.1)

The field is real, solenoidal and Schwartz. Its cylindrical coefficients are

    d_r=-sin(theta)F,
    d_theta=(2r^2-1)cos(theta)F, d_z=0.                     (1.2)

Thus under the vector rotation projectors from the predecessor it has only
modes +1 and -1, and Pi_0 d=Pi_2 d=0. Direct exact differentiation gives

    c=(d.grad)d=(-4x^3+2x,-4x^2 y-2y,0)F^2,
    [curl c]_z=8xy F^2=4r^2 sin(2theta)F^2.                (1.3)

Let

    b=-Pi_2 P c.                                          (1.4)

This is nonzero: its curl has a nonzero mode-2 axial component by (1.3),
since curl annihilates the complementary gradient part of c. Leray and the
vector rotation action commute with curl in the corresponding scalar/vector
representation. In particular the coefficient of exp(2i theta) in (1.3)
is -2i r^2 F^2, so that of [curl b]_z is +2i r^2 F^2.
The field b is in every H^m. It need not be Schwartz; no such assertion is
needed for the pressure-projected acceleration.

## 2. The single-datum full-PDE theorem

### Theorem 1

For every nu>0 and epsilon_target>0 there is a nonzero real solenoidal
Schwartz datum u0 for which the unique classical unforced NS solution is
global, sup_(t>=0)||u(t)||3<=epsilon_target, and

    W_2^+(t)=+infinity                                     (2.1)

for every sufficiently small t>0. The solution has finite energy and the
canonical pressure p=sum R_i R_j(u_i u_j). The same example has uniformly
small finite L^{3,q}, q>3, by the inclusion L3 into L^{3,q}.

Proof. Take u0=epsilon d, epsilon>0 sufficiently small. We give the global
smallness argument to avoid making the mode expansion conditional on
unproved long-time existence. For a classical unforced solution let
E=||u||2^2, Y=||grad u||2^2, Z=||Delta u||2^2. Its energy and enstrophy
identities, Sobolev inequality and interpolation imply

    E'=-2nu Y,
    (1/2)Y'+nu Z <= C||u||3 Z <= C E^(1/4)Y^(1/4) Z.       (2.2)

Choose epsilon so C(E(0)Y(0))^(1/4)<nu/2. A first-crossing bootstrap then
gives E(t)<=E(0), Y(t)<=Y(0) and Y'+nu Z<=0 throughout the classical
lifespan. The H1 continuation alternative extends that solution globally.
Moreover ||u(t)||3<=C(E(0)Y(0))^(1/4)<=C_d epsilon. Choose epsilon smaller
again for the desired target. Local theory and smooth persistence give the
required classical solution and canonical pressure. Those standard inputs
are specified in the source note below; the a priori estimate is (2.2).

For this datum all Sobolev orders are finite. The original projected PDE,
not a truncation, gives a Taylor expansion in every fixed H^m for small t:

    Pi_2 u(t)=epsilon^2 t b+O_(epsilon,nu,m)(t^2),
    G_2(t)=epsilon^2 b+O_(epsilon,nu,m)(t).                  (2.3)

Indeed the viscous term preserves angular mode and Pi_2 d=0, so the
projected time derivative at zero is exactly epsilon^2 b. The smooth
solution makes the second derivative bounded on a sufficiently short
interval. Also B(0)=0 and z(0)=epsilon d, proving the second identity.
No later term of the actual trajectory is omitted in the error estimate.
It follows that

    Re<G_2(t),v_2(t)> = epsilon^4 t ||b||2^2+O(t^2),
    ||v_2(t)||2^2 = epsilon^4 t^2 ||b||2^2+O(t^3),
    [Re<G_2,v_2>]_+/||v_2||2^2 = 1/t+O(1).                (2.4)

The numerator is positive and the mode is nonzero for sufficiently small
positive t. Integrating (2.4) from zero proves (2.1). This is an actual
improper integral on a global smooth flow, not a blowup in the velocity.
QED.

More generally any smooth actual mode birth v_n(t)=t^k b+O(t^(k+1)), b!=0,
with bounded linear coefficients has normalized signed source work
k/t+O(1). Thus the issue is intrinsic to division by newborn energy, not
a special feature of the numerical constants in (1.1).

## 3. Removing the zero-denominator loophole

### Theorem 2

There is a family u0_delta, 0<=delta<=delta0, continuous in the Schwartz
topology and all inside the same global smallness class, such that v_2 is
nonzero on a common interval [0,t_*] for delta>0 and

    W_(2,delta)^+(t_*) >= log(1/delta)-C,                   (3.1)

with t_*>0,C<infinity independent of delta. Hence the failure is not repaired
by requiring a nonzero selected mode at every observation time.

Proof. Define a complex Schwartz mode-2 field

    e=-Pi_2 curl curl c = -Delta b.                         (3.2)

The second equality uses curl curl b=-Delta b and (1.4); it is an equality
of tempered distributions, all of which belong to the indicated Sobolev
spaces. The first formula is a finite derivative of a Gaussian polynomial,
followed by angular averaging, so e is Schwartz and divergence-free. Also

    Re<e,b>=||grad b||2^2>0.                                (3.3)

Take u0_delta=epsilon d+delta epsilon^2(e+conjugate(e)). Reality and
solenoidality are exact, and Pi_2(e+conjugate(e))=e. For a fixed small epsilon
and fixed small delta0 these data satisfy (2.2) uniformly and form a compact
set in the Schwartz topology, as the continuous image of [0,delta0].
The resulting unforced solutions are globally regular and uniformly small
in L3. Uniform local smoothness and continuous dependence, or the usual
Hs difference-energy estimate on a common short interval, give

    v_delta(0)=delta epsilon^2 e,
    v_delta'(t)=epsilon^2 b+O_(epsilon,nu)(delta+t)          (3.4)

in L2, uniformly for 0<=t<=t_* after t_*,delta0 are chosen small. Choose
these constants so the error's pairing with b has modulus at most
(epsilon^2/2)||b||2^2. Using (3.3) gives

    Re<v_delta(t),b>
       >=delta epsilon^2||grad b||2^2
          +(epsilon^2 t/2)||b||2^2.                        (3.5)

In particular v_delta never vanishes on [0,t_*] for delta>0 and its final
L2 norm is bounded below uniformly in delta. Let B_delta=Pi_0 u_delta.
Uniform local smoothness bounds integral_0^t_* ||S(B_delta)||infinity
independently of delta. The EXACT mode energy identity gives

    d log||v_delta||2/dt
       =-nu||grad v_delta||2^2/||v_delta||2^2
        -Re integral conjugate(v_delta,i) v_delta,j
                    partial_j B_delta,i /||v_delta||2^2
        +Re<G_delta,v_delta>/||v_delta||2^2.               (3.6)

Drop the favorable dissipation, bound the strain, and integrate. Replacing
the last integrand by its positive part yields

    W_delta^+(t_*) >= log(||v_delta(t_*)||2/
                              (delta epsilon^2||e||2))
                      -integral_0^t_*||S(B_delta)||infinity.

Equations (3.5) and this common strain bound prove (3.1). For each fixed
positive delta the work is finite on this compact interval, by (3.5) and
smoothness. Thus it is a genuine unbounded family, in addition to the
single-datum infinite-work example. QED.

This also excludes a work bound by any input functional that is finite and
locally bounded on Schwartz data: such a functional is bounded on this
compact family. Without that continuity qualification, Theorem 1 already
excludes ANY finite-valued universal bound for W_2^+ including zero seeds.

## 4. What this does and does not remove from the main problem

The exact angular occupation inequality stays valid, with its stated
extended-integral interpretation. Its homogeneous confined-preload and
exterior-occupation consequences also remain unchanged. The invalid NEXT
inference would have been that large normalized nonlinear work requires
large physical energy, critical-norm growth, or a finite initial resource.
Theorems 1 and 2 disprove that inference in the original unforced equation.
No use of the forced OpenAI theorem is needed for this counterexample.

One cannot repair an arbitrary-data producer merely by adding a tiny initial
seed: (3.1) rules that out uniformly. Starting a proposed event only after
its mode reaches a specified nonzero critical size could remove this
particular singular denominator, but event extraction and a finite
initial-data-controlled budget would have to be proved anew. No such claim
is made here. These examples are not regenerative concentrating turnovers.

The current negative route still requires common-data realization and a
full-PDE shadow of a singular architecture. The positive route still needs
an input-only RF-q/L3/Serrin producer. Neither follows from this falsification.

## Sources and validation

[T] Terence Tao, Localisation and compactness properties of the Navier-Stokes
global regularity problem, arXiv:1108.1165v4 (31 May 2012), Theorem 5.4
(local H1 existence, uniqueness, Schwartz-data regularity), Corollary 5.8
(H1 continuation alternative); Sections 4-5 specify pressure and energy.
https://arxiv.org/pdf/1108.1165
The statements and relevant proof passages were inspected directly this run.
Viscosity nu is retained in (2.2); the standard local theory at viscosity one
transfers by u(t,x)=nu v(nu t,x), p(t,x)=nu^2 q(nu t,x) from viscosity one.
Small-data global regularity and
the energy method are prior art; no novelty is claimed for them.

The finite exact checker verifies (1.1)-(1.3), divergence/curl algebra,
rotation bookkeeping, factorization identities and rational inequalities.
It is not a numerical PDE simulation, an independent proof audit, or a
formal verification of the analytic existence theorem or the limits.
