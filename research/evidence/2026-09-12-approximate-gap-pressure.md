# Approximate angular gaps: an all-mode pressure estimate and its exponential leakage cost

Date: 2026-09-12. Author analytic proof; independent mathematical audit pending.
Input: `itpplasma/navier@c7feb2cabf2329fcd5cff69165cb110d7c289903`.

## Working packet

TERMINAL CLAIM: original unforced incompressible NS on R3, fixed nu>0,
divergence-free Schwartz datum and its maximal classical branch. No forced or
periodic replacement is a terminal solution.

ESTABLISHED: `2026-09-12-weighted-pump-action.md` bounds a phase-coherent
primary pump by an extra exponent O(L^(3/4)), conditional on an exact angular
gap and an explicit even-feedback budget B_Z. Exact increasing rotational
symmetry cannot be installed at regular handoffs.

FIRST GAP: retain the old low angular sectors rather than setting them to zero.

PREDICTION (before computation): the weighted pressure estimate survives with
an explicit low-sector defect. Its worst elliptic coefficient is exponential
in the weight oscillation, not in L. Consequently exp(-c L) approximate
spectral purity suffices for the O(L^(3/4)) pump bound, but qualitative or
polynomial purity does not by itself supply that bound.

FALSIFIER: a derivative loss, an omitted angular cross term, or a uniform
weighted low-mode pressure estimate invalidating the proposed exponential
cost. CHECK: whole-space integration by parts, rotational orthogonality and an
exact Newtonian dipole counterexample. The latter is an elliptic control, not
an assertion that every such force is an NS linearization force.

## 1. Rotational projections, with no invariant-gap assumption

Use the unitary rotation action on vector fields, including rotation of their
components. Let P_<N and P_>=N be the orthogonal projections onto rotational
indices |m|<N and |m|>=N, respectively. For scalar fields use the corresponding
ordinary angular projections. They intertwine gradient and divergence.
An axisymmetric scalar multiplier commutes with all these projections.
Thus the splitting remains orthogonal in every axisymmetrically weighted L2
space. No angular mode of the velocity, coefficients or pressure is deleted.

At a fixed time let phi be smooth, real, bounded and axisymmetric, constant
outside a compact set, with bounded derivatives. Write

    W=exp(-phi),   A=ess sup phi-ess inf phi,
    delta=||r grad phi||_infinity/N < 1/2,
    c_delta=(1+2delta)/(1-2delta).

All norms below are whole-space norms. The canonical pressure solves

    -Delta p=div F.

It is enough initially to use smooth decaying fields, then approximate in the
homogeneous pressure energy class. The bounded weight permits this limiting
step for each fixed phi; uniform constants are obtained from the estimates,
not from an unstated uniform equivalence of weighted and unweighted norms.

Set F_l=P_<N F, F_h=P_>=N F and similarly p_l,p_h. The high component obeys

    ||W grad p_h||_2 <= c_delta ||W F_h||_2.              (1)

For completeness, angular Poincare gives ||W p_h/r||_2<=||W grad p_h||_2/N.
Test the Poisson equation with W^2 p_h. Both derivative-of-weight terms cost
at most 2delta, giving (1). This repeats the preceding lemma at its actual
scope; it makes no assertion that p_l=0.

The ordinary unweighted gradient-Poisson operator has L2 norm at most one.
The two norm conversions give

    ||W grad p_l||_2 <= exp(A) ||W F_l||_2.               (2)

Since the weighted high and low outputs are orthogonal, an all-mode form is

    ||W grad p||_2^2
      <= c_delta^2 ||W F_h||_2^2
                         +exp(2A)||W F_l||_2^2.          (3)

In particular, (3) requires no invariance of the chosen cutoff along a flow.
The cutoff N may be selected separately on each band, without resetting data.

## 2. Exact pressure-work defect in the velocity estimate

Let smooth solenoidal U,w solve on a compact classical interval

    w_t+(U.grad)w+(w.grad)U-nu Delta w+grad p=0.

The exact canonical pressure source is F=2(w.grad)U. Choose the matrix norm
in K(t)=||grad U||_infinity so that |F|<=2K|w|. Put v=Ww and v_l=W P_<N w.
Set

    theta=||v_l||_2/||v||_2,
    eta=||W F_l||_2/(2K||v||_2),                         (4)

with either ratio set to zero when its denominator is zero. Both ratios lie
in [0,1]. Eta measures the *actual* low pressure-source term, including all
cross-label products of U and w; it is not inferred from theta.

Rotational orthogonality and solenoidality give

    |<Ww,W grad p>|
       <= 2delta c_delta ||W P_>=N w||_2 ||W F_h||_2
                                 +||v_l||_2||W grad p_l||_2
       <= [4delta c_delta K+2K exp(A) theta eta]||v||_2^2. (5)

The high estimate integrates the gradient onto W^2 w_h and uses
|grad phi|<=delta N/r. The low estimate uses (2) directly. No derivative
of w occurs on the right, and the canonical pressure is not localized.

Together with the exact diffusion and transport identities, (5) yields

    (1/2)d_t||v||_2^2+nu||grad v||_2^2
       <= [M_phi+4delta c_delta K+2K exp(A)theta eta]
                                                        ||v||_2^2, (6)

    M_phi=ess sup_x[-lambda_min(S(U))-phi_t-U.grad phi
                                             +nu|grad phi|^2].

The earlier exact-gap estimate is the special case theta=0. One may replace
eta by 1, but keeping the product can be appreciably stronger. The new
accumulated defect is

    J_gap(T)=2 int_0^T K(s)exp(A(s))theta(s)eta(s) ds.     (7)

This is a proved all-mode estimate, NOT a production of a bound on (7).

## 3. Consequence for the physical pump band

Under exactly the primary-envelope, clock and regular-patch hypotheses of
`2026-09-12-weighted-pump-action.md`, but no exact angular gap, choose a high
cutoff with delta small as in that note. Its calculation now gives

    ||w(T)||_2 <= exp[int M_base+C L^(3/4)+o(1)
                                      +B_Z(T)+J_gap(T)]||w(0)||_2. (8)

All angular sectors and physical copies are retained. The constants in C
depend on the fixed profiles and patch, not on L; B_Z remains the actual
solution-dependent even-feedback action from the preceding note.

For example, if A<=C_A L^(3/4), K<=C_K L^b, T<=C_T L, and

    sup_[0,T] theta eta <= exp(-c L),  c>0,              (9)

then J_gap<=2C_K C_T L^(b+1)exp(C_A L^(3/4)-c L)=o(1).
More generally, it suffices that the logarithmic purity exceeds the weight
oscillation and the logarithm of the integrated K budget. None of (9), the
polynomial bound on the *total* K, or B_Z=o(L) is asserted for the unknown
inherited source history. In particular, its nonlinear Z may violate the
polynomial K hypothesis.

This identifies a quantitative alternative to an impossible exact reset:
retain a nonzero but sufficiently small low sector. It does not yet construct
that approximate depletion or its repeated causal supply.

## 4. Exact low-mode obstruction to removing exp(A) from the elliptic estimate

Let chi>=0 be smooth radial on R3, supported in |x|<1, with mass M>0, and let
F_0=chi e_3. This is a rotational index-zero vector force. Its canonical
pressure p_0=(-Delta)^(-1)div F_0 has, for |x|>1, the exact dipole form

    p_0(x)=M partial_3(1/(4pi|x|)).

For any R>1, direct angular and radial integration gives

    ||grad p_0||_(L2(|x|>R))^2=M^2/(6pi R^3).            (10)

Indeed |grad partial_3(1/(4pi rho))|^2 equals
(1+3cos(theta)^2)/(16pi^2 rho^6). The angular integral is 8pi and the radial
integral is 1/(3R^3).

Choose a smooth radial psi equal to one on the support of chi and zero on
|x|>=R, with 0<=psi<=1, and put phi_A=A psi. Its oscillation is exactly A.
Then

    ||exp(-phi_A)F_0||_2=exp(-A)||F_0||_2,
    ||exp(-phi_A)grad p_0||_2>=M/sqrt(6pi R^3).          (11)

Therefore the weighted gradient-Poisson norm on the index-zero sector is at
least c exp(A), with c>0 independent of A. Even if N is chosen so large that
||r grad phi_A||_infinity/N tends to zero, (11) is unchanged. A high cutoff
does not improve the low sector.

One can add any weighted-unit, smooth solenoidal high-grade force F_h,
supported where phi_A=0. It creates no pressure. Add a multiple of F_0 with
weighted norm theta_A. The resulting input is approximately high-grade,
with low weighted fraction theta_A/sqrt(1+theta_A^2), while its weighted
pressure norm is at least c exp(A)theta_A. For theta_A=A^(-p), p>0, this
diverges. For theta_A=exp(-beta A), beta<1, it also diverges.

Thus qualitative/polynomial approximate purity cannot replace the exponential
leakage coefficient in a uniform *elliptic* estimate. This counterexample
does not prove necessity of (9) for NS energy growth: solenoidal pressure-work
cancellations or dynamical restrictions on F may improve a particular history.

## 5. Recomputed frontier and verification scope

The missing exact-gap hypothesis has been replaced by the explicit all-mode
functional J_gap, with a worst-case-sharp elliptic exponential dependence.
No mode reset, new source background or independent entry state was used.
The first unresolved estimate is now the simultaneous bound on J_gap and B_Z
for one actual inherited physical history, not another scalar pressure lemma.

The next distinct test is whether the available energy/small critical norm can
control the even-feedback action at all; it must use actual unforced solutions,
not an independently forced even field. The terminal consumer still also needs
one Schwartz trace, full de-forcing and preservation of a singular observation.
The positive arbitrary-data critical producer remains independently open.

`research/check_approximate_gap_pressure.py` verifies the exact dipole tail
constant, the pressure-work coefficients and limiting exponent comparisons.
The all-mode analytic estimates and their scope are proved above, not by that
finite checker. No canonical graph node or formal status is promoted.
