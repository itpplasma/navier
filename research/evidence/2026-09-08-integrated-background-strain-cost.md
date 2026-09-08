# Integrated background-strain cost for full-state return blocks

Date: 2026-09-08.
Status: AUTHOR PROOF; independent mathematical audit PENDING. No canonical graph promotion.
Original unforced R3 Navier-Stokes, ordinary positive viscosity, canonical pressure, and the entire inherited state throughout. No NS-R3 resolution is claimed.

## 0. Exact consumer and scope

The terminal producer remains, for one fixed finite q>3,

    integral_0^t Pi_q,M <= nu integral_0^t D_q,M + C(d,nu,H,N0,q)

for every upper time t<=H uniformly in M. This note does NOT supply that producer or extract the required events from arbitrary hypothetical blowup.

The result here strengthens the preceding relative-background block obstruction by replacing the physical-energy-weighted cost with a dimensionless integrated background-strain cost. The complete solution is compared to one continuously evolved original-NS background at the same viscosity; no background reset is permitted.

Let u and b solve original NS at the same viscosity nu and put v=u-b. Write the canonical pressure difference as pi=p[u]-p[b]. Then

    -Delta pi = d_i d_j(v_i v_j + v_i b_j + b_i v_j),

and the mixed pressure obeys the exact identity

    -Delta pi_cross = 2 div((v.grad)b),

hence

    ||grad pi_cross||_2 <= 2 ||grad b||_infinity ||v||_2.

The complete local relative-energy identity is

    partial_t |v|^2
      + div[((|v|^2+2 pi)v) + b |v|^2]
      = nu Delta |v|^2 - 2 nu |grad v|^2
        - 2 v_i v_j partial_j b_i.

All generated exterior, reverse channels and canonical pressure are retained.

## 1. Background-following endpoint lemma with integrated strain

Fix finite Ebar,A,m and sigma_* >=0. There exist r_*>0 and eps_*>0 depending only on these parameters such that the following is impossible for smooth original NS pairs (u,b) on [-1,0], with the same viscosity eta>0, v=u-b, if

    sup_s ||v(s)||_2^2 <= Ebar,
    sup_s (-s)||grad v(s)||_infinity <= A,
    eta <= eps_*,
    2 eta integral_-1^0 ||grad v||_2^2 <= eps_*,
    integral_-1^0 ||grad b||_infinity ds <= eps_*,
    integral_{B(x,r_*)} |v(0)|^2 >= m.

Proof. If false, take a sequence with viscosity, relative dissipation and integrated background strain tending to zero, and terminal balls shrinking to a point while carrying mass m. Follow a background characteristic X_j satisfying X_j'=b_j(s,X_j). In translated variables around X_j(s), the transport by b_j disappears from the local-energy flux. The relative-energy identity becomes the usual local Euler energy balance plus the strain defect -2 v_i v_j partial_j b_i and viscosity. The total contribution of the strain defect is bounded by

    2 Ebar integral ||grad b_j||_infinity ds ->0.

The same finite-energy/Lipschitz interpolation as in the preceding no-atom lemma gives

    ||v_j(s)||_infinity <= C Ebar^(1/5) A^(3/5)(-s)^(-3/5),

which is time integrable. Local compactness on compact subintervals below zero follows from the local H1 bound and the equation in H^-2. The mixed pressure is controlled by the exact identity above and the self-pressure by the ordinary Riesz estimate; the background speed itself never enters. Passing to the limit gives a finite-energy Euler solution v with the same Type-I gradient bound and canonical pressure.

The translated local-energy identity passes the final energy trace because the full accumulated background-strain defect tends to zero. Consequently the terminal energy measures converge to the Euler energy trace. The shrinking terminal balls force an atom of mass at least m. Chae-Wolf's no-energy-atom corollary excludes such an atom. Contradiction.

No pointwise smallness of ||grad b||_infinity is needed, only small integrated strain.

## 2. Exact full-state return map relative to one background

Use the existing annular multiplier Q_K. At a return endpoint define

    a=K^(1/2)||Q_K u||_2,
    V(y)=u(t,x+y/K)/(a K),
    B(y)=b(t,x+y/K)/(a K),
    Z=V-B,
    mu=nu/a.

The next return is the complete original flow, followed by translation, rotation, rescaling and amplitude renormalization exactly as in the existing full-state map. No mode deletion, phase reset, polarization reset, pressure reset or background reset is allowed.

Fix constants M0,L,M1,rho,theta0,Theta,r0>1,gamma_*>0. Consider N consecutive returns satisfying

    theta0 <= theta_n <= Theta,
    g_n lambda_n^2 >= r0,
    ||Z_0||_2, ||Z_N||_2 <= M0,
    ||Z_n||_2 >= rho at every endpoint,
    sup_{n,tau} ||grad Y_n(tau)||_infinity <= L,
    sup_{n,tau} ||grad Y_n(tau)||_2 <= M1,
    gamma_1(V_N) >= gamma_*,

where Y_n is the complete normalized relative flow on turnover n. No upper bound on g_n or lambda_n is imposed, and g_n itself need not exceed one.

Assume also that the normalized background contribution to the final selected annulus is at most a fixed small fraction of the full final annulus, so the final efficient annulus yields a definite localized relative-energy mass by the same convolution argument as in the predecessor theorem.

Let chi_b denote the dimensionless accumulated background strain over the physical block:

    chi_b = integral_{t_0}^{t_N} ||grad b(t)||_infinity dt.

This quantity is invariant under the turnover normalization.

## 3. Dimensionless strain-cost theorem

There exist N_* and positive mu_*,delta_* depending only on the displayed comparison-class constants and Q_1 such that any block with N>=N_* and 0<mu_0<=mu_* satisfies

    2 mu_0 integral_0^T ||grad(u-b)||_2^2 dt + chi_b > delta_*.

Proof. The clock condition D_{n+1}/D_n=g_n lambda_n^2>=r0 gives a finite normalized endpoint horizon and an Euler-Type-I gradient bound for the complete relative flow exactly as before. The bounded first/final relative energy and final efficient annulus give a terminal physical ball with fixed positive relative energy after endpoint normalization. If both relative viscous dissipation and chi_b were arbitrarily small along increasingly long blocks at mu_0->0, normalize the whole block to [-1,0] and apply the integrated-strain endpoint lemma. The final spatial radius shrinks geometrically with the number of returns. This yields the contradiction.

The theorem is a complete-interval original-NS statement with all exterior and mixed pressure retained. It does not assert existence of such returns.

## 4. Strain-only corollary under relative enstrophy control

Under the additional endpoint lower bound ||Z_n||_2>=rho and uniform normalized relative enstrophy bound ||grad Y_n||_2<=M1, the actual relative viscous expenditure is O(mu_0). Indeed the exact change of variables gives on block n

    2 mu_0 integral ||grad(u-b)||_2^2
      = 2 mu_0 (a_n/K_n) integral_0^{theta_n} ||grad Y_n||_2^2,

and relative endpoint normalization plus ||Z_n||_2>=rho bounds a_n^2/K_n by the physical relative energy divided by rho^2. Geometric growth of the nonlinear clocks makes the sum finite. Therefore for sufficiently small mu_0,

    chi_b > delta_*/2.

Hence any family of disjoint admissible sufficiently long blocks using the SAME smooth background b satisfies

    number of blocks < (2/delta_*) integral_0^H ||grad b(t)||_infinity dt.

This is a dimensionless block-counting obstruction. It avoids the previous a^2/K prefactor.

## 5. Retained-bulk family is compatible with the comparison

For the existing retained-bulk construction

    d_K(x)=A K f(Kx)+h(x),
    A=K^alpha, 0<alpha<1/2,

let b be the actual NS evolution from h at the same physical viscosity. In normalized coordinates U_K for the full flow and B_K for this evolved background, the full difference obeys the exact equation

    z_t - (nu/A) Delta z + (U_K.grad)z + (z.grad)w + grad q
      = ((nu/A) Delta w) + lower mixed terms,

with canonical pressure difference obtained from the complete stress tensor. Standard H^m energy estimates around a fixed smooth Euler reference w yield, for fixed m>=4 and fixed normalized interval,

    sup_tau ||U_K-B_K-w||_{H^m}
      <= C_m (nu/A + 1/(A K)),

and the corresponding pressure estimate

    sup_tau ||p[U_K]-p[B_K]-p[w]||_{H^m}
      <= C_m (nu/A + 1/(A K)).

Thus the harmless fixed retained bulk can be absorbed into one continuously evolved same-viscosity background while retaining full relative L2 control; the comparison does not merely rename the predecessor counterexample.

This does NOT construct a regenerative turnover or infinite shadowing orbit.

## 6. Exact remaining gap

The new theorem does not imply NS-R3. The missing implication is

    hypothetical arbitrary-data blowup
      -> infinitely many admissible relative return blocks
      -> one legitimate background with input-controlled total strain.

Choosing b=u makes the relative endpoint trivial and is inadmissible. Choosing b=0 reintroduces full normalized-energy coercivity. Replacing b from block to block incurs an exact comparison-change defect with no sign:

    ||u-b_new||_2^2 - ||u-b_old||_2^2
      = -2 <u-b_old, b_new-b_old> + ||b_new-b_old||_2^2.

No input-summable critical estimate for such adaptive background changes is proved here.

Therefore the current surviving nut is: construct and shadow dynamically essential inherited exterior that escapes every controlled smooth-background comparison, or prove a critical input-summable cost plus blowup-event extraction that covers that escaping class.

Certified positive regenerative turnovers remain zero. NS-R3 remains unresolved.
