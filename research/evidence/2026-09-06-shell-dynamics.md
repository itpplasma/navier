# Natural-variable time regularity and regularized shell dynamics

Date: 2026-09-06. Status: author-checked; independent mathematical audit
pending. This is a complete fixed-regularization component derivation, not
a proof of the missing arbitrary-data critical bound or NS-R3.

## Frozen inputs and output

Research inspected at `a891263a1733c37a964751b75721c463d90d6fa3`; paper
inspected at `f01941b2e964be64a357f925f835afba1384f1c5`. The source was
committed through the GitHub connector to private `itpplasma/navier-paper`
at `a9993cccee0f9544c49f9c98524c6c4af4c0e080`, path `sections/shell_dynamics.tex`, SHA-256
`66f3ff185f220e8be874ea2090bc982abe42b4208ee093dc6799b5ee015e5677`.

The accepted cubic minimizer and weighted dissipation are the project
inputs. The signed pairing and speed-shell cancellation retain the
independent-audit-pending status of their source supplements. No predecessor
is independently audited or promoted by this evidence. The construction
uses the existing Riesz multiplier bounds, no new imported PDE estimate.
The natural-distance geometry is standard nonlinear variational geometry;
no novelty or priority claim is made.

## 1. Natural-distance estimate, including gradient freedom

Put A(z)=|z|z, J(z)=|z|^(1/2)z. With r=|z| and e=z/r away from zero,
DA=r(I+e tensor e) and DJ=sqrt(r)(I+(e tensor e)/2). Both derivatives
are zero at zero. The squared radial/transverse ratios of DJ against DA
are 9/8 and 1. Segment integration and Cauchy--Schwarz therefore give

    |J(b)-J(a)|^2 <= (9/8)(A(b)-A(a)) dot (b-a).

For the minimizing representatives wi=w(fi), let d=w1-w0 and
H=integral_0^1 DA(w0+s d) ds. Then 0<=H<=(|w0|+|w1|)I. Both A(wi)
annihilate the closed gradient space G3. Thus for every g in G3,
e=f1-f0+g satisfies

    E=integral d^T H d=integral d^T H e
     <= sqrt(E) sqrt(integral e^T H e).

All terms are finite by Holder in L3; H need not be invertible. Dividing
only when E>0 and integrating the pointwise estimate proves

    ||V1-V0||2^2 <= (9/8) integral (|w0|+|w1|)|f1-f0+g|^2.

In particular V=J(w(f)) is locally Lipschitz from L3 to L2. This does
not assert that w itself is locally Lipschitz in L3.

## 2. Time derivative without pressure or division at the zero set

On any compact classical interval u is C1 into L3. Hilbert-valued
Lipschitz differentiation gives V in W^(1,infinity)(time;L2). In the
increment estimate choose g=integral_t^(t+h) grad p(s) ds. This belongs
to G3; the equation replaces the velocity increment plus g by the
integral of F=nu Delta u-(u dot grad)u. At almost every time, division by
h^2 and passage to the strong L3 limits gives

    ||V_t||2^2 <= (9/4) integral |w| |F|^2.

The weighted identity supplies V locally bounded in H1 and
M^2:=||V||6^2<=a0 D, a0=9 C_S^2/8. Write W=||V_t||2. These are
local classical estimates, not endpoint-uniform a priori bounds.

## 3. Differentiable finite ridge residual

Write chi=T Pi(V tensor V), where T is the double Riesz contraction and
Pi is the symmetric trace-free projection. For fixed smooth speed
features gj compactly supported inside (0,infinity), put phij=gj(|w|),
Gij=<phii,phij>, bi=<chi,phii>, eta>0, and

    a=(G+eta I)^(-1)b,
    R=||chi||2^2-b^T(G+eta I)^(-1)b,
    r=chi-sum aj phij.

Completing the square and shell cancellation give

    N_rho^2 <= R=||r||2^2+eta |a|^2 <= ||chi||2^2,
    K=<sigma,r>,  |K|<=||sigma||2 sqrt(R).

The temporal argument deliberately uses different dual spaces:

    chi_t=T Pi(V_t tensor V+V tensor V_t) is in L^(3/2),
    ||chi_t||_(3/2)<=2 C_(3/2) M W,
    ||chi||3<=C3 sqrt(2/3) M^2.

Also hj(z)=gj(|z|^(2/3)) is smooth and globally Lipschitz, because gj
vanishes near zero. Hence phij,t=Dhj(V)V_t lies in L2 and
||phij,t||2<=ellj W. Time mollification in L3 and L^(3/2), and the
continuous L2 representative of chi, justify the scalar product rules.
No L2 derivative of chi or time derivative of w at zero is assumed.

For fixed finite n and positive eta the exact envelope identity is

    R'=2<chi,chi_t>-2 a dot b'+a^T G' a
      =2<r,chi_t>-2<r,sum aj phij,t>.

The first last-line pairing is L3--L^(3/2); the second is L2--L2.
With A3=(sum ||phij||3^2)^(1/2), ell=(sum ellj^2)^(1/2), the full
quantitative consequence is

    |R'| <= 4 C_(3/2) M W [C3 sqrt(2/3) M^2+A3 sqrt(R/eta)]
            +2 ell eta^(-1/2) W R.

A single countable smooth family gives nested feature spans dense in the
speed-function subspace for every snapshot. Decreasing eta to zero while
increasing the spans gives R decreasing to N_rho^2 at each fixed time.
This is not convergence of derivatives, uniform convergence near Tstar,
or permission to differentiate the full moving sharp projection.

## 4. What is unblocked, and the first unsupported implication

The previous speed-shell checkpoint required a new temporal regularity
argument before using its projection dynamically. The result supplies
such an argument for finite smooth features and positive regularization,
including a pressure-free derivative estimate and an exact residual
identity. It is not just another conditional continuation criterion.

A proposed closure would now need endpoint control of M and W in the
last bound. The available estimate contains
integral |w| |nu Delta u-(u dot grad)u|^2, not an energy-controlled
quantity. Moreover eta^(-1/2), the feature Lipschitz norms, and A3 are not
uniform in refinement. Pointwise monotone convergence does not control
these losses. There is no input-only bound for the combined clock L_c,
for integral ||sigma||2^4, or for these evolution drivers in this work.
The central arbitrary-data bound remains unproved.

A useful non-PDE caution: on two equal-mass atoms, the smooth speed path
(1+t,1-t) determines every function when t is nonzero but only constants
at t=0. The associated orthogonal projections can therefore jump at a
speed collision. This is only a two-atom projection diagnostic, not a
Navier--Stokes example or a proof of failure of any trajectory estimate.
The fixed positive ridge penalty avoids that inversion singularity.

## 5. Author checks and audit boundary

The proof checks degenerate PSD matrices without taking their inverse,
zeros of w without division, the factor 9/4 in the time limit, the sign
of the pressure-gradient increment, both dual spaces in the residual
derivative, and the coefficient-derivative cancellation in the envelope.
`tools/check_shell_dynamics.py` in the paper repository checks frozen
source/labels, exact rational constants, exact rational ridge identities,
and 2003 deterministic natural-distance probes including zeros and
opposites. These checks passed locally. Finite probes are not a proof of
the analytic assertions and are not an independent mathematical audit.

The main manuscript source compiled locally with no undefined references,
undefined citations or overfull boxes after adding the section. That is a
document check only. Remote integration, complete-map build and final
source replay are to be recorded separately after execution.

No formal repository edits, axiom claims, public release, contact,
submission, added authorship or gap-node promotion are made.
