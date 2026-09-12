# Full pump chains have certified extra growth, including a decaying-pump gain

Date: 2026-09-12. Input: `itpplasma/navier@fe808d8f73b38a6b54e839157f2c9534e201e60c`.

**Author proof with an exact-rational a-posteriori infinite-tail certificate;
independent audit pending.** The negative products of two projected growing
coefficients do not imply stability of the full pump linearization. Keeping
both polarizations and every axial sideband, the charge-9 instantaneous
operator at pump amplitude 30 has an eigenvalue with real part greater than 5.
The actual freely decaying reference pump also gives an `L2` amplification
strictly greater than `51/50` at time `1/200` for a suitable real perturbation.
No frozen pump is maintained by an unmentioned force in this latter statement.

This is a reference-model linear gain, not a nonlinear regenerative turnover,
a physical whole-space realization, or an `NS-R3` result. A separate all-time
energy bound shows that a fixed decaying pump has only finite extra strain
action; unbounded small-seed compensation still needs a new quantitative input.

## Working packet

TERMINAL CLAIM: original unforced NS on `R3`, positive fixed viscosity and
Schwartz divergence-free data; the same original regularity/blowup alternatives.

ESTABLISHED: the one-seed Fourier charge is exact; fixed short-time ladder birth
does not provide independent rank-four bridge controls. The two-mode pump
coefficient signs concern a projection, not an invariant spectral block.

FIRST GAP: can the full pump-coupled chains give additional finite-time gain,
rather than merely exchange pre-existing growing coordinates?

PREDICTION BEFORE PROBE: both polarizations and non-half-grade sidebands may
create an instability absent from the projected two-mode signs. The ordinary
finite-section eigenvalue probe suggested a charge-9 root near `5.05+6.71i`.
The subsequent, frozen validation target was an eigenvalue with `Re>5` in the
complete infinite operator, followed by gain for the genuinely decaying pump.

FALSIFIER: loss under the omitted-tail bound, a failed exact contraction bound,
or an uncontrolled step from frozen spectrum to nonautonomous amplification.

FORBIDDEN INFERENCES: finite-section eigenvalue = PDE eigenvalue; frozen
spectrum = a sustained nonautonomous instability; linear gain = nonlinear
turnover; reference system = original whole-space target.

CHECK: exact Leray reduction; rational residual/Jacobian/tail validation;
Duhamel comparison with the actual time-dependent pump; total strain budget.

## 1. Exact infinite charge chain

Use the same frozen reference equation and initial pump as in the one-seed
packet. Set

    h=(1/10,0,1/2),  d=(1/20,0,1),
    b=(1,beta,-1/20),  beta=sqrt(401)/20,
    mu=3/5,  K_0=[[0,1,0],[1,0,0],[0,0,0]].

The real pump at amplitude `B` is `B b exp(i d.x)+B b exp(-i d.x)`.
On a fixed nonzero charge `n`, let

    k_p=n h+p d=(x_p,0,z_p),   r_p=|k_p|^2,
    a_n=b.k_p=3n/40,          r_d=401/400,
    v_(k_p)=i^p (z_p phi_p, theta_p, -x_p phi_p),  p in Z.

Both independent transverse polarizations are represented. The gauge `i^p`
makes the infinite matrix real when `B` is real. The complete linearization is

    phi_p' = -mu r_p phi_p - (z_p/r_p) theta_p
       + a_n B [(r_(p+1)-r_d)phi_(p+1)
                       -(r_(p-1)-r_d)phi_(p-1)]/r_p,

    theta_p' = -mu r_p theta_p - z_p phi_p
       + a_n B [theta_(p+1)-theta_(p-1)
                       +beta(phi_(p+1)+phi_(p-1))].       (1)

To verify (1) directly, put `q=k_(p-s)` and `s=+/-1` in the unordered Leray
symbol with pump wavevector `s d`. For a perturbation
`v_q=(q_z phi,theta,-q_x phi)`, one has

    b.q=a_n,   v_q.(s d)=-s a_n phi.

Projection onto the planar transverse direction at `q+s d` gives
`a_n (|q|^2-r_d)phi/|q+s d|^2`; the scalar output is
`a_n(theta-s beta phi)`. The Fourier factor and gauge give `-s a_n B`.
The source multiplier supplies the two displayed cross-polarization terms.
Thus (1) is a full charge chain, not a pair truncation.

## 2. Exact a-posteriori certificate for the infinite operator

Fix `n=9`, `B=30`. The checker uses the finite section `-20<=p<=12`, with
66 scalar coordinates, only to propose an eigenvector and an approximate
inverse. Fix the eigenvalue center

    lambda_bar = 5049883304450/10^12
                   +i 6708966735593/10^12.                (2)

Normalize `theta_-6=1`. The unknown vector replaces that one field coordinate
by `lambda`. Its equation is `F=(A-lambda)v=0`. A numerical eigensolver and
matrix inverse propose the remaining coordinates and a finite preconditioner
`R`; each real and imaginary part is then rounded to a rational with
denominator `10^12`. Their errors are not assumed small: they are tested below
in exact rational arithmetic.

The only irrational operator coefficient is enclosed by

    floor(sqrt(401)*10^20)/(20*10^20) <= beta
      < [floor(sqrt(401)*10^20)+1]/(20*10^20).

The integer floor is computed by `isqrt(401*10^40)`. Its square inequalities
are checked. The midpoint operator is rational and the uncertainty has row-sum
norm at most `2 a_n B` times the enclosure half-width.

Work on the complex sequence sup norm, using `|Re z|+|Im z|` on each scalar;
include the eigenvalue in the same maximum norm. Outside the finite section,
precondition by `(-mu r_p)^(-1)`. Call the combined preconditioner `M`.
The boundary maps in **both directions** between the finite section and the
entire tails are retained in the derivative estimate.

For `p<=-21` or `p>=13`, convexity gives

    r_p >= r_min=108909/400.

All neighboring tail radii exceed `r_d`, and the exact identity

    (r_(p-1)-r_d)+(r_(p+1)-r_d)=2r_p

bounds the two planar hopping coefficients together. With `l=|lambda_bar|_1`
and the upper endpoint `beta_hi`, the entire tail derivative is bounded by

a planar row bound

    (l+2a_n B)/(mu r_min)+1/(mu r_min^(3/2)),

and a scalar row bound

    [l+2a_n B(1+beta_hi)]/(mu r_min)
                                    +1/(mu sqrt(r_min)).  (3)

Here `|z_p|<=sqrt(r_p)`. Reciprocal square roots are bounded by checked rational
lower square-root bounds. There is no cutoff assertion on the omitted tail.
The finite rows of `I-M DF` are evaluated exactly, including `R` times all
boundary columns. The finite residual and both boundary tail residuals are
also evaluated exactly, with the `beta` uncertainty included.

The certified coarse constants are

    ||M F(v_bar,lambda_bar)|| < Y = 1/25000000,
    ||I-M DF(v_bar,lambda_bar)|| < Z = 67/100,
    ||M|| < 47.                                         (4)

The only nonlinear part of this eigenproblem is `-lambda v`. Hence on the
ball of radius `r=10^-6` the Newton-like map `X -> X-M F(X)` satisfies

    Y+Zr+47r^2 < r,
    Z+94r < 1.                                          (5)

These are exact rational comparisons. The contraction theorem supplies an
infinite-sequence eigenpair with

    |lambda-lambda_bar|_1 <= 10^-6,   Re(lambda)>5.        (6)

The tail preconditioned equation is defined on bounded sequences, even before
asserting that the unbounded diffusion operator maps a trial sequence into
that space. At a fixed point it gives the original eigen-equations pointwise.
The finite preconditioner is injective because its checked identity defect is
less than one. Equation (1) and `r_p` quadratic first give
`phi_p=O(p^-2)`, then `theta_p=O(p^-2)`. Iterating those estimates gives decay
of every polynomial order. Thus the reconstructed velocity is a smooth
`L2` eigenfunction of the complete parabolic charge operator, not a spurious
bounded-sequence solution. The conjugate charge gives the real perturbation.

The code uses floating point only for proposals. A successful exit requires
(3)--(5) with exact rational arithmetic. It is rigorous a-posteriori numerical
evidence under the analytic operator reduction/proof above, not an ordinary
spectral plot or an independently audited theorem.

At `B=0`, the source multiplier has norm at most one and viscosity decreases
the real parts. Thus `Re>5` is genuinely additional pump-coupled growth.

## 3. Transfer to the actually decaying reference pump

A single pump is an exact reference solution with

    B(t)=30 exp(-kappa t),
    kappa=20/sqrt(401)+1203/2000.

Its nonlinearity vanishes. Let `A(t)` be its full linearization and `v_*` the
smooth eigenfunction certified in (6). Denote

    c_0=|b||d|=401/(200 sqrt(2)) < 71/50,
    kappa <161/100.

Because `b.d=0`, the exact supremum norm of the pump's symmetric strain is
`c_0 |B(t)|`. The transport term has zero real energy pairing and the source
matrix contributes at most one. Consequently both the frozen and actual
propagators have the coarse `L2` upper bound `exp(44(t-s))` at this amplitude.

On charge nine, `b.k_p=27/40` for all `p`. The pump's advection and stretching
operator per unit amplitude is bounded on physical velocity `L2` by

    2(27/40+c_0)<21/5.

Thus

    ||A(t)-A(0)|| <= (21/5) 30 kappa t.

Variation of constants against `exp(lambda t)v_*` gives, without truncating
any sideband,

    ||v(t)-exp(lambda t)v_*||_2
       <= 102 t^2 exp(44t) ||v_*||_2.                    (7)

We used `Re(lambda)<44`, also immediate from (6), and the energy propagator
bound. At `T=1/200`, a rational Taylor/geometric remainder enclosure proves
`exp(44T)<5/4`, so

    ||v(T)||_2/||v_*||_2
      >= 1+5T-102 T^2(5/4) >51/50.                      (8)

For comparison `exp(T)<101/100`. Taking both conjugate charge sectors
produces real initial data and preserves this norm ratio. This establishes
finite-duration gain for the **freely decaying** reference pump, not just the
spectrum of a fictitiously maintained pump.

## 4. Pump action is still finite: what this does not supply

The same exact energy calculation, now integrated with the actual decay,
gives for every charge and every time

    ||v(T)||_2/||v(0)||_2
      <= exp[T+c_0 |B(0)|(1-exp(-kappa T))/kappa].         (9)

A fixed pump can therefore provide at most a finite extra factor
`exp(c_0 |B(0)|/kappa)` beyond the coarse free-reference energy growth. A
linear mechanism asking the pump alone for an extra factor `exp(eta L)` must
at least have `|B(0)|>=eta kappa L/c_0`. This necessary bound does not control
ratios whose denominator cancels, or replace a nonlinear trajectory estimate.

The certified charge-nine gain cannot produce that class from a seed solely
in charge one: the linear charge separation remains exact. Nonlinear supply
first creates charge-nine data at ninth seed order. Its eventual amplification
and feedback cannot be treated as four independently prescribed bridge inputs.
A new construction needs a quantitative growing pump-action regime, controlled
nonlinear saturation and inherited phases, followed by physical localization
and one common trace. None is obtained by (8).

The full-chain attack has therefore resolved a real ambiguity: projected pair
signs did hide a genuine infinite-chain growth mechanism, but a fixed decaying
pump has a finite action budget. The next first-gap test is source-specific
availability and cost of the required pump action, or the distinct localized
full-history adjoint. More finite-section spectral sweeps would not settle it.

Companion: `research/check_full_pump_chain.py`. No canonical proof-graph or
formal status is promoted; no external theorem is newly imported and no
novelty or independent-audit claim is made.
