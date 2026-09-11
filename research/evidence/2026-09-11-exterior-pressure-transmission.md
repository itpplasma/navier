# An exact angular barrier for exterior pressure transmission

Date: 2026-09-11. Input: `itpplasma/navier@1a039958a7c2909933a59646df29269b7012b15f`.

**Status:** author proof; independent mathematical audit, external novelty
assessment and formal verification pending. A later checkpoint,
`2026-09-11-exterior-pressure-energy.md`, removes the extra exterior-budget
hypothesis below for finite-energy quadratic stresses. This is a spatial transmission
estimate for the original whole-space Leray projection, not a complete
physical adjoint estimate or a proof of UE1 / NS-R3.

## 1. Prediction, consumer and first uncontrolled term

Prediction recorded before running the new checker: a regular harmonic
pressure of angular grade `n != 0` loses at least `(r/R)^abs(n)` in gradient
L2 norm when crossing a cylindrical gap from radius R to r. Axial dependence
and both real-field angular partners must be retained. Exterior Newtonian
pressure is not an unsuppressed shortcut around the already known angular
heat-import obstruction.

The consumer is the delivery of source parent harmonics
`abs(n_j) >= c 2^(h j/2)` into a radius `r_j` comparable to `sqrt(Q_j)`,
`Q_j=2^(-j)`. Their local entry amplitude is of order `exp(-C j^2)`, up to
fixed powers of Q_j. A fixed-ratio exterior gap gives a smaller-than-entry
pressure input unless its exterior budget is correspondingly large.

The first uncontrolled term is stress already inside an asymptotically thin
collar of the receiver, or transport/nonlinear generation that brings it
there. No bound for that term is assumed. Nor is a norm bound for the full
source propagator inferred from a fixed-window principal pulse bound.

Applicable frozen controls: angular preparation, local entry seed, harmonic
protection, localized-adjoint defect, common-control criterion, and the
terminal-open control. Existing passive heat and base-characteristic walls
are retained; this calculation addresses a distinct elliptic channel.

## 2. Harmonic cylinder theorem

Let `C_R = {(x,y,z): x^2+y^2<R^2, z in R}`. Suppose a complex scalar p is
harmonic in C_R, regular at its axis in the weak H1 sense, and has just angular
grade n, where `N=abs(n)>=1`. Assume `grad p in L2(C_R)`. Then for `0<r<R`,

    ||grad p||_(L2(C_r)) <= (r/R)^N ||grad p||_(L2(C_R)).       (2.1)

The constant is exactly one and is independent of axial frequency, N and R.
For a real field the same assertion applies to the orthogonal pair of grades
`+N,-N`. No periodic replacement of the axial direction is made.

**Proof.** Angular Poincare gives `||p||_2 <= R ||grad p||_2/N`, so the axial
Fourier transform is legitimate. For almost every axial frequency k the
regular radial solution f satisfies

    f'' + f'/s - (N^2/s^2+k^2) f = 0.                         (2.2)

For `k!=0`, it is a scalar multiple of `I_N(abs(k)s)`. The other independent
solution is excluded by finite H1 energy at the axis. For `k=0` the regular
solution is a multiple of `s^N`. Multiplication of (2.2) by `s conjugate(f)`
and integration by parts gives

    E_k(r) := integral_0^r (|f'|^2+(N^2/s^2+k^2)|f|^2)s ds
            = r Re(f'(r) conjugate(f(r))).                   (2.3)

The axis boundary term is zero. For `k!=0` write

    I_N(abs(k)s) = sum_(l>=0) a_l s^(N+2l),
    a_l = (abs(k)/2)^(N+2l)/(l! (N+l)!) >= 0.

Thus, apart from the nonnegative squared scalar multiplier,

    E_k(r) = sum_(m>=0) (N+m)
               [sum_(l=0)^m a_l a_(m-l)] r^(2N+2m).          (2.4)

Every coefficient is nonnegative. Consequently
`E_k(r) <= (r/R)^(2N) E_k(R)`. For `k=0`, this is equality. Plancherel in z,
angular integration and a square root prove (2.1). One can first integrate
on radii below R and pass to R by monotone convergence if the outer trace is
not regular. The argument also proves the stated weak-H1 formulation.

The exponent cannot be uniformly increased: regular solutions with axial
Fourier support concentrating near k=0 have energy ratios approaching
`(r/R)^(2N)`. These are actual finite-energy axial wave packets; the exactly
z-independent monomial is only a per-unit-length equality example, not an
L2(R3) example.

## 3. Why this controls an actual Leray tail

Let S be a smooth compactly supported tensor on R3, vanishing in C_R, and put

    p = (-Delta)^(-1) partial_i partial_j S_ij,
    g = P div S = div S + grad p.

Take the angular grade n using the natural scalar, vector and tensor rotation
actions. Rotation commutes with div, grad, Delta and the whole-space Leray
projection. It also preserves cylindrical support. Inside C_R, `g_n=grad p_n`
and `Delta p_n=0`. Therefore

    ||g_n||_(L2(C_r)) <= (r/R)^N ||g_n||_(L2(C_R)).           (3.1)

In particular the right side is at most `(r/R)^N ||g_n||_(L2(R3))`.
The statement extends to H1 tensors by approximation when the displayed
norms exist. Local exterior stresses can be treated this way; a decomposition
of a general stress by radial cutoffs leaves its collar stress as a separate
term and does NOT bound that term.

A locally harmonic gradient in (3.1) must not be discarded by applying P a
second time just to that local expression. The globally solenoidal field g
has exterior source `div S`; it is not a global pure gradient.

The gradient has vector rotation grade n, not grade n-1. Its Cartesian
components involve scalar grades n-1,n,n+1, as in the earlier angular
viscosity estimate. That component shift does not weaken (2.1): harmonicity
and the integrated Dirichlet energy supply the exponent N exactly.

## 4. Source-scale consequence and the necessary collar

Let I_j be any time interval on which the exterior stress vanishes in a
cylinder of radius R_j (a fixed radius for this statement). Define its direct
pressure-input budgets

    B_j = integral_(I_j) ||g_(n_j)(t)||_(L2(C_(R_j))) dt,
    J_j = integral_(I_j) ||g_(n_j)(t)||_(L2(C_(r_j))) dt.

Then, with no time-propagator approximation,

    J_j <= (r_j/R_j)^N_j B_j,    N_j=abs(n_j).               (4.1)

If `R_j/r_j >= 1+delta` for a fixed positive delta and
`B_j <= exp(C_1 j^2)`, then

    J_j <= exp(C_1 j^2 - c log(1+delta) 2^(h j/2)).          (4.2)

For fixed `h>0`, this is eventually smaller than `exp(-C_2 j^2)` for every
fixed C_2. Fixed powers of Q_j and polynomial normalization factors do not
alter the comparison.

A conditional local receiver estimate with gain at most `exp(C_3 j^2)` gives
the same conclusion for that receiver's response. Such a gain must be proved
for the actual receiver and its input norm before this conditional sentence
can be used. It is NOT asserted for the complete physical history operator.

Conversely, if a mechanism actually requires `J_j >= exp(-C_2 j^2)` and has
the stated B_j bound, then (4.1) necessarily implies

    N_j log(R_j/r_j) <= (C_1+C_2) j^2.                     (4.3)

Hence `R_j/r_j-1 = O(j^2/N_j)` whenever `N_j/j^2 -> infinity`.
At the source angular scale, the allowable relative collar is
`O(j^2 Q_j^(h/2))`. This is a necessary geometric condition for this specific
bounded-budget pressure-input mechanism, not a universal localization
requirement for every possible unforced solution.

## 5. Scope, failure cases and frontier recomputation

The theorem excludes unattenuated *direct pressure transmission across a
fixed radial gap*. It does not exclude a pressure budget of size
`exp(c N_j)`, a source in the thin collar, advected entry, an interaction
already inside the cylinder, or amplification by an uncontrolled full-history
propagator. For generic exterior stress these bounds were not supplied at this
checkpoint. The sequel proves that finite energy does bound the direct
far-pressure input of quadratic velocity stress; it does not bound the collar
or full-history gain. There is no cut-off adjoint and no omitted adjoint defect here.

UE1 therefore remains nonlinear/global. The next discriminating question is
whether the thin-collar or in-core stress can be generated from one Schwartz
trace with the full angular hierarchy retained, or whether the complete
physical adjoint forces an unbounded prefix-control cost. UE2--UE4 and the
positive RF-q producer are unchanged.

## 6. Verification and provenance

`research/check_exterior_pressure_transmission.py` checks the radial energy
identity, positive coefficient formula and exact rational-radius inequalities,
including hostile wrong-exponent and singular-axis cases. The infinite-series
argument and the arbitrary-N theorem are the analytic proof above, not an
inference from finitely many tests.

Inputs inspected: the repository's angular-preparation, angular-heat-import,
source-exterior-characteristic, source-pulse-adjoint and physical-harmonic
packets at the input commit, and PLAN sections 1, 5--9. The mathematical proof
is self-contained. Modified Bessel functions are used only through the series
and ODE explicitly stated here. No new literature theorem is assumed.

Verification checkpoint: 374 exact pressure controls passed. The existing
source-characteristic checker passed after correcting the coordinate definition.
The first hostile-model selftest exposed a pre-existing regression: the two
controls required by `refuted_peak_strain` had been removed in earlier frontier
refreshes. Their exact original records were recovered from
`4945332b9f867c4a4ccb49a7eb6fc92db1d34a2e:research/game/controls.json` and
restored without changing observations. This is validation maintenance, not a
mathematical result. No current control observation was changed.

The existing angular-heat checker also initially failed its strict decay claim
at k=2: both k/2^k and its square are equal at k=1 and k=2. The checker now
freezes that equality and requires strict decrease from k=3. No continuum
heat estimate or asymptotic conclusion is changed. All the applicable exact
checkers, fast gate, hostile selftest, research-only and paper-only structural
checks were rerun; full formal verification was not run.
