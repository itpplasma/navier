# Whole-space angular preparation: logarithmic damping, exterior occupation, and nonlinear supply

Date: 2026-09-08. Frozen input: `fedb45a640ea8537aa90578f2cafda9adca01756`.
Status: AUTHOR PROOFS; independent mathematical audit PENDING.
Integration preserves concurrent `694be9648450dbb1528232e08d20ec07ace302d0`.
Its causal pulse-inverse obstruction overlaps the audit here; that overlapping
statement is not counted as a second new result or independent review.
Original positive-viscosity Leray operator on R3. No Galerkin truncation,
angular-mode deletion, pressure reset, or artificial cylinder boundary.

## 0. Exact consumer and scope

UE1 proposes replacing the external starts of a countable pulse family by
one smooth initial perturbation. The theorem here excludes homogeneous
preloading of high-angular-frequency pulses that remain substantially in
a shrinking column during their preparation. More strongly, without that
localization assumption, it forces such homogeneous seeds to spend almost
all of their logarithmic preparation time outside the column. For the FULL
original nonlinear solution it gives the alternative: a large, explicitly
quantified cumulative nonlinear supply to those modes. Every other mode and
the entire radial exterior remain in that supply and occupation identity.

The proof is an angular energy argument with the actual vector Laplacian.
Its ingredients are standard; the quantitative preparation and exterior
occupation consequences are new relative to the frozen repository. No
exhaustive literature novelty search or independent review is claimed.

This is NOT an input-summable critical event cost. Its nonlinear work is
normalized by the current mode energy and can be large when absolute work
is small. It does not feed RF-q by itself. It is consumed as a precise
obstruction to a class of UE1 initializations, not as a regularity criterion.
A successful free-trace construction still needs UE2 -> UE3 -> UE4.

## 1. Rotational modes of the exact vector equation

Let R_theta be rotation about the z axis and define the unitary action

    (T_theta v)(x) = R_(-theta) v(R_theta x),
    Pi_n v = (1/(2 pi)) integral_0^(2 pi) exp(-i n theta) T_theta v dtheta.
                                                                    (1.1)

Complex fields are notation only; a real field retains the conjugate modes.
In cylindrical components, Pi_n selects dependence exp(i n theta). These
are vector rotation modes, NOT independent projections of fixed Cartesian
components. Rotations preserve divergence and the Laplacian and commute
with the whole-space Leray projector. Thus Pi_n is an orthogonal L2
projection preserving the solenoidal space. If B is axisymmetric, both
P[(B.grad)v] and P[(v.grad)B] preserve each of these modes.

For v=exp(i n theta)(v_r e_r+v_theta e_theta+v_z e_z), the angular derivative
of its Cartesian vector is

    partial_theta v = exp(i n theta)
        [(i n v_r-v_theta)e_r+(i n v_theta+v_r)e_theta+i n v_z e_z].  (1.2)

The transverse Hermitian quadratic form has eigenvalues (n-1)^2 and (n+1)^2;
the axial eigenvalue is n^2. Therefore for |n|>=2,

    ||grad v||_2^2 >= (|n|-1)^2 integral_R3 |v(x)|^2/r^2 dx.         (1.3)

The inequality extends from smooth fields away from the axis by approximation,
or directly by cylindrical integration for H1 fields. It introduces no
boundary condition at a cylinder or at the axis. The shift by ONE is essential:
using n^2 for a vector field would be false.

## 2. Exact preparation inequality with all radial exterior retained

Fix t0<T, tau=T-t, tau0=T-t0, h>0, nu>0, R>0, and C_B>=0. Let B be a real,
axisymmetric, divergence-free field, smooth with B and its spatial derivatives
bounded on every compact preterminal time interval. Write S(B)=(grad B+grad B^T)/2, and assume

    ||S(B(t))||_(L-infinity,operator) <= C_B tau^(-1-h).             (2.1)

B need not itself be an unforced solution. This allows both a trial background
and the exact angular mean of an original solution below. Let v_n be a smooth
solenoidal finite-energy solution, in rotation mode n, of

    partial_t v_n - nu Delta v_n
      + P[(B.grad)v_n+(v_n.grad)B] = G_n.                          (2.2)

G_n is the ENTIRE solenoidal source in that mode. There is no finite harmonic
closure premise. Define A_n=||v_n||_2, E_n=A_n^2, and, when E_n>0,

    eta_n(t) = integral_(r<=R sqrt(tau)) |v_n|^2 / E_n,
    J_n(t) = integral_t0^t eta_n(s)/(T-s) ds,
    W_n(t) = integral_t0^t Re <G_n,v_n>/E_n ds.                    (2.3)

Set eta_n=0 at zero-energy times. The positive-work version W_n^+ replaces
the numerator by its positive part and is an extended nonnegative integral.
All L2 norms and pairings in this note are over the WHOLE R3.

### Theorem 1: angular occupation/work inequality

On intervals where A_n is nonzero,

    log(A_n(t)/A_n(t0)) + [nu (|n|-1)^2/R^2] J_n(t)
       <= (C_B/h)(tau^(-h)-tau0^(-h)) + W_n(t).                    (2.4)

If A_n(t0)<=M with M>0, the same inequality with log(A_n(t)/M) and W_n^+
holds for any final time with A_n(t)>0, including zero intermediate modes.

Proof. The full Leray energy pairing in (2.2) gives

    (1/2) E_n' + nu ||grad v_n||_2^2
        = -Re integral conjugate(v_n,i) v_n,j partial_j B_i
          + Re <G_n,v_n>.                                        (2.5)

Transport by B integrates to zero. Only S(B) contributes to the real
stretching term, so its absolute value is bounded by (2.1) times E_n.
In (1.3), retain just r<=R sqrt(tau), obtaining

    ||grad v_n||_2^2/E_n >= (|n|-1)^2 eta_n/(R^2 tau).              (2.6)

Divide (2.5) by E_n and integrate. The strain integral is exactly
(C_B/h)(tau^(-h)-tau0^(-h)), proving (2.4). The pressure has been removed
only by the exact solenoidal whole-space pairing, not by omitting its dynamics.

For zeros, divide instead by E_n+epsilon^2, use the positive part of source
work, and bound the initial norm by sqrt(M^2+epsilon^2). At the endpoint the
logarithm converges, the occupation term converges by dominated convergence
on each compact time interval, and the positive-work term increases to W_n^+
by monotone convergence. This proves the second statement. QED.

### Corollary 2: homogeneous trapped preparation is superalgebraically damped

If G_n=0 and eta_n(s)>=eta_*>0 for almost every preparation time, then

    A_n(t) <= A_n(t0) exp[(C_B/h)(tau^(-h)-tau0^(-h))]
                     (tau/tau0)^[nu eta_* (|n|-1)^2/R^2].          (2.7)

In particular, consider n_j and t_j increasing in frequency and approaching T,
write q_j=T-t_j, and suppose

    c_- q_j^(-h) <= (|n_j|-1)^2 <= c_+ q_j^(-h),
    A_(n_j)(t0) <= M,                                             (2.8)

where M,c_-,c_+ are fixed positive constants. For all sufficiently large j,

    A_(n_j)(t_j) <= M exp[-c_* q_j^(-h) log(tau0/q_j)],
    c_* = nu eta_* c_-/(2 R^2).                                   (2.9)

Proof. In (2.7), the damping exponent is at least
(nu eta_* c_-/R^2)q_j^(-h) log(tau0/q_j), while the positive strain exponent
is at most (C_B/h)q_j^(-h). The logarithm eventually dominates its fixed
coefficient. A nonzero homogeneous endpoint ensures nonzero earlier norms
by forward uniqueness, so the logarithmic derivation is legitimate. QED.

This conclusion is incompatible not only with algebraic terminal amplitudes,
but also with amplitudes bounded below by

    exp[-C_* (1+log(tau0/q_j))^p]                                 (2.10)

for ANY fixed finite p>0 and C_*. Indeed q^(-h) log(1/q) dominates every fixed
power of log(1/q). The required initial norm for such trapped preparation
would diverge at least as the reciprocal of (2.9), times (2.10). A single
finite-energy datum has ||Pi_n d||_2<=||d||_2 for every n and cannot provide it.
No Schwartz or analyticity restriction on the datum is needed for this
exclusion; finite energy already suffices.

### Corollary 3: the exterior must carry almost all logarithmic preparation time

Retain homogeneous evolution, (2.8), and the terminal lower bound (2.10),
but do NOT impose any lower bound on eta_n. Put L_j=log(tau0/q_j). Then

    J_(n_j)(t_j)
       <= [R^2/(nu c_-)] [C_B/h
                     +q_j^h {C_*(1+L_j)^p+log^+ M}],              (2.11)

up to enlarging the fixed constant if the lower-bound prefactor is not one.
Consequently

    (1/L_j) integral_t0^t_j eta_(n_j)(s)/(T-s) ds -> 0.             (2.12)

For every eta_*>0, the fraction of logarithmic time on which eta_n>=eta_*
is at most J_n/(eta_* L_j), and tends to zero.

Proof. Rearrange (2.4), use G_n=0 and the endpoint bounds, and divide by
the lower bound nu c_- q_j^(-h)/R^2. QED.

This is a WHOLE-PREPARATION result, not a static exterior example. It permits
arbitrarily large radial/axial tails, and says that homogeneous preloading
must use them. It does not assert that this exterior is large in a critical
norm, has a summable physical cost, or can actually supply a future pulse.

## 3. The exact full nonlinear alternative

Now let u be an ORIGINAL UNFORCED classical R3 solution, with finite energy,
and set

    B=Pi_0 u,  z=u-B,  v_n=Pi_n u  (n!=0).

B is the actual angular mean, not an independently reset background. Exact
rotation equivariance gives (2.2) with

    G_n = -Pi_n P[(z.grad)z].                                    (3.1)

This expression retains ALL angular harmonics, their mixed products,
polarizations, radial exterior, and reverse interactions. B need not solve
unforced NS separately; its mean Reynolds forcing disappears under Pi_n,
which is why (3.1) is exact. The full original pressure is still determined
by the entire u tensor u, not by a cylinder-local relation.

### Theorem 4: required nonlinear supply if the modes do not escape radially

Suppose the mean satisfies (2.1), the selected modes satisfy (2.8), their
terminal sizes satisfy (2.10), and eta_(n_j)>=eta_*>0 during preparation.
Their actual positive normalized nonlinear work must obey

    W_(n_j)^+(t_j)
       >= [nu eta_* c_-/R^2] q_j^(-h) L_j
          -(C_B/h) q_j^(-h)-C_*(1+L_j)^p-log^+ M.                 (3.2)

In particular it is at least c_* q_j^(-h) L_j for sufficiently large j.
When there are no zeros and the signed work is integrable, (3.2) holds for
W_n itself. Proof: apply Theorem 1 with (3.1) and rearrange. QED.

Thus the proposed autonomous conversion must provide one of the following,
not silently use externally planted seeds: substantial radial escape during
preparation, or cumulative nonlinear generation quantified by (3.2), or a
failure of the stated mean-strain/frequency/size class.

This is NOT an RF-q producer. The division by E_n is crucial: exponentially
small physical interactions can have large relative work. Total kinetic
energy does not bound W_n^+, and summing (3.2) as though it were an absolute
energy cost would be invalid. No arbitrary-blowup extraction is obtained.

## 4. Frequency ceiling and the attempted logarithmic repair

### Corollary 5: necessary frequency shift for trapped homogeneous preparation

Without assuming (2.8), any homogeneous mode with eta_n>=eta_*, initial norm
at most M and final norm at least a_*>0 satisfies

    (|n|-1)^2 <= R^2/[nu eta_* log(tau0/tau)]
        * [(C_B/h)(tau^(-h)-tau0^(-h)) + log(M/a_*)].              (4.1)

For the quasi-polynomial lower sizes (2.10), this requires

    |n|-1 = O(tau^(-h/2)/sqrt(log(tau0/tau))).                     (4.2)

The instantaneous balance n^2 comparable to tau^(-h) omits the logarithm of
the preceding preparation interval. This is the distinction between planting
a new pulse late and preparing it autonomously from a fixed earlier time.

For [OA]'s carrier k comparable to Q^(-h/2), an actual azimuthal wave number
is n=k p. Only where the pitch |p| is bounded below (and q comparable to tau)
does the source fall into the frequency class (2.8). The source asserts only
n!=0 in general. This note DOES NOT assume all its labels have nondegenerate
pitch, and DOES NOT claim its externally forced pulses have a prehistory
satisfying eta_n>=eta_*.

We tested the simplest proposed repair: lower k by sqrt(log(1/Q)), while
keeping the phase normals and the unstable frame geometry uniformly bounded.
That change alone cannot preserve the source's grow-then-decay pulse.

**Lemma 6 (fixed-geometry damping failure).** On [0,L], consider the real
principal frame equation

    z' = [diag(lambda,-lambda)+E-d I]z,
    lambda>=lambda_min>0,  |E_ab|<=delta<=lambda_min/8,
    0<=d<=lambda_min/4,  z_+(0)>0, z_-(0)=0.

Then |z_-/z_+|<=2 delta/lambda_min and

    z_+' >= (lambda_min/2) z_+ .                                 (4.3)

Proof. With r=z_-/z_+, scalar damping cancels in

    r'=E_21+(-2 lambda+E_22-E_11)r-E_12 r^2.

For delta>0, at r=2 delta/lambda_min the right side is strictly negative,
and at the negative endpoint it is positive. For delta=0, r=0 is an exact
solution. Thus this interval is invariant. The equation
for z_+ and the stated constants give (4.3). Positivity follows by its scalar
integrating factor, closing the ratio argument. QED.

If d=epsilon k^2|n_Phi|^2 goes to zero with bounded |n_Phi| and the same
positive spectral gap, this lemma precludes a decaying second tail. This is
a principal-equation obstruction, not a full-PDE stability assertion.

One also cannot merely change k in [OA, (7.2)] and leave the damping restored
by its prescribed B_s: that formula gives the exact identity

    k^2 B_s^2 = lambda_0/[epsilon (1+u_*^2)^(3/2)],                (4.4)

independent of k. It restores the effective spatial wave number. A genuinely
modified geometry might evade this: the scalar balance d=lambda for a fixed
B_s would require

    (1+s^2)^(3/2)=lambda_0/(epsilon k^2 B_s^2),                    (4.5)

so reduced epsilon k^2 of order 1/log entails |s| of order log^(1/3) at the
turning point. Such an enlarged phase swing changes the polarization and
stress realization problem; it is NOT validated here. Small-pitch families,
nonlinear angular generation, and genuine exterior preparation also remain.

## 5. What has and has not collapsed

Together with `2026-09-08-unforced-support-and-pulse-audit.md`, the following
conversion branches are excluded in their exact scopes:

1. keep the localized source velocity and reinterpret its force as pressure
   on a terminal slab;
2. preserve exact open heat-exterior/axisymmetric-core patches;
3. remove seed tails with the same zero-trace principal inverse and retain
   the original pulse/covariance;
4. preload the high-angular, substantially column-trapped family from one
   finite-energy datum by homogeneous linearized evolution;
5. fix (4) solely by lowering the carrier in an otherwise fixed bounded
   phase geometry while preserving a two-sided Gaussian pulse.

Free-trace filling exactly repairs each principal pulse on its own interval
(Proposition 6 in the companion note). A coupled autonomous full-state
construction realizing ALL those traces is not excluded. Its first
missing theorem is now a FREE-TRACE realization supplying the complete
nonaxisymmetric pulse family from ONE datum, with global analytic leakage
and actual inherited exterior, through nonlinear angular supply or a proved
radial-import mechanism. It must then solve the full correction equation,
not just the principal amplitude equations, and prove convergence, canonical
pressure, Schwartz initialization and preserved blowup. None of these is
inferred from the present lower bounds.

No positive regenerative turnover or infinite cascade was constructed; no
hypothetical arbitrary singularity was extracted. No independent mathematical
audit was available. Exact algebra checks accompany the derivations but do
not certify the continuum arguments or the external manuscript.

The companion `2026-09-08-mixed-trace-principal-inverse.md` proves a positive
logarithmic-loss principal inverse after changing the trace constraints. Its
simultaneous realization by one whole-space Cauchy datum remains unproved.

The final integration also preserves the concurrent formal-core update
`dd074604f04ebd705583df8dba1d9d3e53df0793`; no formal file or status is promoted.
