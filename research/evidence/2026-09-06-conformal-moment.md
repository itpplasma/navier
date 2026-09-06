# Conformal inversion, finite-energy representatives and moment budgets

## Frozen component and review boundary

Base research revision: `75304802949f070d12c13fe0ee00513b7e4fc2b0`.
Base manuscript revision: `173667199559e4dec2b9e7698dc6dae3bda4d040`.
Canonical complete proof: `itpplasma/navier-paper`, commit
`464a13d1c99318431cba1ed5d954528d1a31c95b`,
`sections/conformal_moment.tex`, SHA-256
`54a6cdfb7d4173550141027d3dd5d3205115a43d37bab484d818d7275a0dca5c`.

Status: author-checked, independent mathematical audit pending. The source
contains complete component derivations, not a proof of NS-R3. Neither the
accepted graph nor any gap node is promoted. Algebra/source regression,
compilation and rendered-page inspection are separate from mathematical audit.

## Exact inputs and resolved spatial questions

The accepted cubic minimizer w(f) is defined on every L3 affine gradient
coset, not only on solenoidal inputs. The accepted unweighted div-curl theorem
for solenoidal H1 data gives w in L6, grad w in L2 with squared norm at most
5/4 times squared grad u, and sigma=-div w in L2 with squared norm at most
1/4 times squared grad u. It did not supply w in L2 or sigma in L^(3/2).

The new snapshot theorem assumes, additionally, |x| grad u in L2. Put
A=|| |x| grad u ||2, U=||u||2, F=(sqrt(5)/2)(A+2sqrt(3)U),
c1=1+4sqrt(3), C*=2^(2/3)(4pi/3)^(1/6). It proves

    ||w||2 <= 2F,                   ||q||2 <= 2F+U,
    || |x| grad w ||2 <= c1 F,     || |x| sigma ||2 <= c1 F/sqrt(3),
    ||sigma||_(3/2) <= C* (||sigma||2 || |x|sigma ||2)^(1/2).

Thus w,q are in H1 and sigma is in L^(3/2). These statements apply to every
such weighted H1 snapshot; they are not claimed for every bare H1 datum.
In particular the theorem does not assert ||w||2 <= C||u||2.

## Mechanism and delicate bridges

Inversion I(x)=x/|x|^2 pulls back one-forms by

    Kf(x)=|x|^-2 (Id-2 n_x tensor n_x) f(I(x)).

Its Jacobian exactly matches the cubic power in dimension three. K is an
L3 isometric involution preserving the closed gradient subspace. For a
compactly supported scalar phi, subtract phi(0) from phi composed with I
before cutting off at infinity. The resulting gradient error is O(1/R) in
L3; near zero the composition is identically zero. This proves preservation
of the actual closed gradient space, not merely formal curl cancellation.
Uniqueness of the minimizer gives w(Kf)=K w(f).

The differentiated pullback is r^-4 R(grad f)(Ix)R+r^-3 B(n,f(Ix)), where

    B(n,v)=-2 v tensor n-2(n.v)Id-2 n tensor v+8(n.v)n tensor n,
    |B(n,v)|F^2=8|v|^2+4(n.v)^2 <= 12|v|^2.

Hardy and change of variables prove Kf in H1, with
||grad Kf||2 <= A+2sqrt(3)U. The puncture is removable in the weak derivative:
the extra cutoff pairing is bounded by C epsilon^(1/2) times the local L2
norm of Kf. No point-supported distribution is omitted.

Crucially, K does NOT preserve ordinary solenoidality. Apply the accepted
div-curl theorem to v=P K u, whose gradient norm contracts and whose cubic
coset is that of K u. It gives K w in L6 with grad K w in L2. Hardy then
proves ||w||2^2=integral |Kw|^2/r^2 <=4F^2, so w in L2 is a conclusion,
not a hypothesis. Rearranging the differentiated formula on annuli proves
the weighted gradient estimate. The accepted trace constraint supplies
sigma^2 <= |sym grad w|^2/3 pointwise, with zero-set derivatives handled
by the Sobolev level-set property. An explicit ball/complement split
then proves the L^(3/2) interpolation, including its constant.

## The weight is available on the original selected branch

For each viscosity nu>0, solenoidal Schwartz datum u0 and finite H>0, let
E0=||u0||2^2, M0=|| |x|u0 ||2^2, M(t)=|| |x|u(t) ||2^2 and
W(t)=|| |x|grad u(t) ||2^2. Define

    K_H = M0+6 nu E0 H,
    I_H = 6 S^(3/2) E0^(1/4) H^(1/4) (E0/(2nu))^(3/4),
    L_H = (I_H+sqrt(I_H^2+4K_H))/2.

The full proof on the page gives, uniformly for t<min(H,Tstar),

    M(t)+2 nu integral_0^t W <= L_H^2.

Use bounded weights rho_R=r^2/(1+r^2/R^2), with
|grad rho_R|<=2sqrt(rho_R) and Delta rho_R<=6. The pressure tensor-to-scalar
Fourier symbol has Frobenius norm one, hence ||p||2<=||u||4^2. Weighted
transport and pressure are bounded by 6sqrt(M_R)||u||4^2. Sobolev and the
ordinary energy identity make the time coefficient Y^(3/4) integrable,
with the explicit input-only bound I_H. Solve a quadratic bound for the
supremum of sqrt(M_R), retain dissipation, and take the monotone R limit.
This does not assume persistence of the entire Schwartz class.

A separate differentiated weighted estimate proves W locally bounded on
every compact classical interval. This latter estimate uses local high
Sobolev norms and is NOT uniform at an unknown singular endpoint. It is
used only to justify the snapshot theorem at every time rather than a.e.
The integrated W budget above is endpoint-uniform and uses only inputs.

With T_H=L_H^2/(2nu)+12HE0 and B_H=(5/6)c1^2 T_H, the source proves

    integral ||w||2^2 <= 10 T_H,
    integral || |x|sigma ||2^2 <= B_H,
    integral ||sigma||_(3/2)^2 <= C*^2 sqrt(E0 B_H/(8nu)).

All integrals run to arbitrary t<min(H,Tstar). Measurability follows from
L3 continuity of the minimizer, countable distributional dual tests and
spatial exhaustion. Zero datum is covered without dividing by its energy.

## Attempt at the critical closure and exact failure

The new defect pair (time,space)=(2,3/2) satisfies 2/s+3/a=3, whereas the
critical defect line is 2/s+3/a=2. It is supercritical in the standard
Navier-Stokes terminology, not a subcritical regularity criterion. Neither
spatial membership nor the displayed time-square bounds implies DEFECT-L4.

The source constructs a concrete solenoidal Schwartz U with nonzero
minimizing defect, then the curve v(t,x)=lambda(t)U(lambda(t)x), with
lambda=[4nu Y_U(T-t)/E_U]^(-1/2). It obeys the exact ordinary energy identity;
all the new time-square and moment finiteness assertions hold; nevertheless
integral ||sigma_v||2^4 diverges. Its constant L3 velocity norm prevents it
from being a singular selected Navier-Stokes branch. This is a non-solution
test curve, not a PDE counterexample. It concerns finiteness, not every
numerical bound in the moment theorem. It is of the backward self-similar
type already examined in the HF26-HF28 evidence, not a novelty claim.

The missing implication is still from actual vector dynamics to a critical
signed pressure/strain or defect budget. No closed arbitrary-data temporal
producer has been obtained. The spatial questions are no longer to be
listed as unproved for the Schwartz-data branch, subject to review.

## Attribution and independent-review questions

Conformal invariance at exponent equal to dimension is classical, not new.
Liimatainen and Salo, Mathematical Research Letters 21(2) (2014), 341-361,
`n-harmonic coordinates and the regularity of conformal mappings`,
arXiv:1209.1285v2 (3 June 2016), introduction on printed page 2, was directly
inspected in the primary-source PDF, including a rendered page. Their scalar
n-harmonic regularity is not applied to our generally nonzero-curl w.
The bibliography also retains Iwaniec-Scott-Stroffolini (1999) for nonlinear
Hodge context. Every new conformal and moment calculation is given in full;
no priority claim is made.

An independent reviewer should reconstruct: preservation of G3 by inversion;
the Leray projection before applying div-curl; puncture removal and both
Hardy uses without circular L2 assumptions; weighted weak-gradient recovery;
trace/zero-set handling; pressure's constant-one L2 estimate; uniform cutoff
and time quantifiers in the quadratic moment bound; pointwise versus
endpoint-uniform W control; exact supercritical scaling; and the non-solution
scope of the self-similar diagnostic. The existing div-curl proof remains an
explicit accepted dependency and should be checked at integration.

The companion regression checks 300 matrix/involution/differentiation probes,
1000 quadratic identities, exact exponent arithmetic, the nonzero defect
seed and source integration. These checks are NOT an independent audit,
a proof assistant verification or a Navier-Stokes simulation.
