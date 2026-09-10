# Source-pulse prehistory and nonlinear regeneration with all quadratic outputs

Date: 2026-09-10. Input main:
`itpplasma/navier@9a02a356608cf2001f6f40bff1b24d6625d4695e`.

**Author derivations; independent mathematical audit and novelty undetermined.**
No unforced blow-up, arbitrary-data regularity, common Schwartz trace, or
completed regeneration cell is established. The positive result below is a
nonzero local nonlinear seeding channel, not a solution of the prehistory
problem. The original terminal target and canonical/formal statuses remain
unchanged.

## 0. Task, consumer, and scope distinctions

The preceding packet replaces a primary pulse's startup cutoff by an
exponentially small entry seed and restores its leading covariance locally.
It does not supply that seed from a common initial state. Extending the
uncut pulse by zero produces impulse forces. This continuation tests two
specific alternatives rather than constructing another generic inverse:

1. Continue the same frozen source ray backward without a cutoff.
2. Let already present source-type pulses generate a daughter internally.

The first has an exact large preparation cost in the stated principal
system. The second has a nonzero asymmetric channel, but necessarily also
produces a competing difference-frequency shear disturbance. That shear is
not removed by pressure, phase selection, or the previous two-weight covariance repair.
A two-parent cancellation escape uses a decaying polarization instead of
two growing ones. All generated quadratic modes are retained, and a full
nonlinear Fourier-jet check shows that the selected triad is not closed.

Four evidence levels must not be conflated:

* Section 1 is an exact theorem for an explicitly extrapolated frozen
  principal system, NOT the actual full physical prehistory of the source.
* Sections 2--5 are exact leading-symbol algebra in the source's reference
  frame. The finite-L source matrices only approach this reference frame.
* Section 6 realizes a nonzero seeding coefficient instantaneously for
  real Schwartz data in the original unforced NS equation on R3. It does
  NOT realize the concentrating source background or subsequent growth.
* The reported integrations are coefficient-level floating-point checks,
  not an NS simulation, interval certificate, or full dyadic history.

The required terminal consumer is still: one compatible unforced history,
with its mean/shear and every generated mode -> repeated amplification
with summable physical durations -> one Schwartz datum, finite energy,
canonical pressure and a preserved singular observation. The first missing
step is a complete coupled turnover, not merely one nonzero Fourier source.

## 1. The same frozen source ray cannot be preloaded cheaply for long

Use a regular source representative and the three-component matrix from
[OA, (7.5)--(7.6)], with its pressure constraint and cylindrical connection
terms. Write F for the representative angular velocity, g=(g_theta,g_z)
for its radial tangential shear, and mu=epsilon*k^2>0. Define

    K = [[0,-2F,0], [2F+g_theta,0,0], [g_z,0,0]],
    n(v)=n_0+v n_1,
    A(v)=-K+n(v)[n(v)^T K-n_1^T]/|n(v)|^2,
    a'=[A(v)-mu |n(v)|^2 I]a,       n(v).a(v)=0.          (1.1)

The source specifies this system on a short pulse rectangle. HERE we
explicitly define its constant-representative extension to [-W,0]. That
extension is a candidate initialization, not a previously proved property
of the physical field. The normal never vanishes because its tangential
part is nonzero.

### Proposition 1: pressure-retaining cubic preparation cost

For every transverse solution of (1.1),

    |a(0)| <= |a(-W)| exp[ |g|W/2 - mu I(W) ],
    I(W)=W|n_0|^2-W^2(n_0.n_1)+(W^3/3)|n_1|^2.          (1.2)

Thus any prescribed nonzero entry amplitude requires

    |a(-W)| >= |a(0)| exp[ mu I(W)-|g|W/2 ].              (1.3)

Proof. Differentiating n.a gives zero. The pressure-normal term has zero
pairing with a. The Hermitian part of K has eigenvalues 0,+|g|/2,-|g|/2,
so

    (1/2)(|a|^2)'=-Re(a* K a)-mu|n|^2|a|^2
                 <= (|g|/2-mu|n|^2)|a|^2.

Integrate and evaluate the integral of |n_0+v n_1|^2. This argument also
applies to complex amplitudes, since the normal and K are real. QED.

For the unrounded source reference normal, in the orthonormal frame
(radial,N,K_tan),

    n(v)=B_s ( sigma(u/2+uv/L), -sigma u/(L|g|), 1 ),
    mu B_s^2 = lambda_0/(1+u^2)^(3/2)=:d_0.              (1.4)

Here N=g/|g|, K_tan=N-perpendicular, and u>0. This follows directly from
the source's chosen tangential wavevector and radial shear. Consequently

    mu I(W)=d_0[ W(1+u^2/4+u^2/(L^2|g|^2))
                   -u^2 W^2/(2L)+u^2 W^3/(3L^2) ].     (1.5)

The preceding packet gives the local entry size exp(-gamma_- L), up to
bounded frame factors, with gamma_->0. Set W=L^2. Equations (1.3)--(1.5)
give

    log |a(-L^2)| >= (d_0 u^2/3)L^4-(d_0 u^2/2)L^3
                         +O(L^2)-gamma_- L+O(1).         (1.6)

In particular the preparation cost diverges, rather than staying flat.
The O(L^2) term has a fixed finite coefficient; the positive L^4 term
controls the conclusion. Carrier rounding preserves a positive leading
L^4 preparation exponent (not necessarily the exact coefficients in (1.6))
whenever |n_1| has a uniform positive multiple of 1/L as a lower bound;
this holds in the source's asymptotic rounding regime k/L -> infinity.

This identifies why a cheap entry seed is not a cheap seed at an arbitrarily
earlier time: continuing the sheared phase raises its radial wavenumber,
and the integrated viscous penalty is cubic in the preparation duration.
This is the usual shear-enhanced dissipation mechanism with the source's
particular normal and connection matrix; no novelty is claimed for the
mechanism itself. See [BMV] for related shear-flow prior art, not an imported
unforced-blowup theorem.

**Limitation.** For L comparable to ell^2, the proposed interval has physical
length Q^(1+h)L^2. Its slow-time displacement epsilon L^2 is small. That
fact alone does NOT identify the full NS propagator with (1.1) over that
interval. Different rays, spatial transport, exterior participation,
nonlinear transfer, and the original source's slow/localization terms can
change the problem. Equation (1.6) excludes the literal frozen-ray attempt;
it is not a lower bound for every physical initial replacement.

## 2. Nonlinear regeneration: use the source's reference polarizations

At a fixed regular point, take the orthonormal basis (e_r,N,K_tan) from
[OA, (7.1)--(7.10)]. Let c_0<0 be the source polarization constant and
lambda_0>0 its undamped radial/tangential growth parameter. Set

    q(s)=sqrt(1+s^2),
    a_+(s)=(1,c_0 q(s),-s),
    a_-(s)=(1,-c_0 q(s),-s).                             (2.1)

The phase normal is proportional to (s,0,1), so both vectors are transverse.
In the frozen reference system their undamped eigenvalues are respectively
+lambda_0/q(s) and -lambda_0/q(s). These can be checked directly using

    K_ref=[[0,-lambda_0/c_0,-omega],
           [-lambda_0*c_0,0,0], [omega,0,0]],
    A_ref=-K_ref+n n^T K_ref/|n|^2,    n=(s,0,1).        (2.2)

The real number omega records the remaining rotational connection.
Viscosity subtracts the squared-wavenumber damping from both rates.

The source's finite-L normal contains a small N component, and its actual
moving-frame amplitudes contain matrix corrections. Thus an exact
cancellation for (2.1) is NOT asserted as an exact cancellation for every
finite-L physical pulse. Section 7 tests those differences explicitly.

Take two positive-branch reference parents with effective wavenumbers

    xi_1=b(s_1,0,1), xi_2=b(s_2,0,1),  b>0,
    a_1=a_+(s_1),     a_2=a_+(s_2),
    c=(s_1+s_2)/2,   Delta=s_1-s_2,   q_j=q(s_j).        (2.3)

Complex Fourier coefficients are A_1 a_1 and A_2 a_2, with the conjugate
negative frequencies retained for a real field. The real coefficient before
-i A_1 A_2 at the sum frequency is

    C_sum=P_(xi_1+xi_2)[(a_1.xi_2)a_2+(a_2.xi_1)a_1].   (2.4)

This is the original incompressible quadratic symbol, not the unprojected
convective term. Here P_xi=I-xi xi^T/|xi|^2.

### Proposition 2: exact sum coefficient and growing projection

One has

    C_sum=( b Delta^2 c/(1+c^2),
            b c_0 Delta(q_1-q_2),
           -b Delta^2 c^2/(1+c^2) ).                   (2.5)

Its coordinate along the daughter's positive eigenvector a_+(c) is

    beta_+ = (b Delta^2 c/2)
       [ 1/(1+c^2)+2/(q(c)(q_1+q_2)) ].                (2.6)

Therefore beta_+ has precisely the sign of c when Delta!=0. The entire
projected sum coefficient vanishes for the mirror pair s_2=-s_1. It also
vanishes for equal tilts s_1=s_2. Otherwise it is nonzero.

Proof. Transversality gives a_1.xi_2=-b Delta and a_2.xi_1=b Delta.
The unprojected coefficient is b Delta(a_1-a_2). Projection onto the
plane perpendicular to (c,0,1) gives (2.5). A vector f in this plane has
positive eigenvector coordinate (f_r+f_N/(c_0 q(c)))/2. Substitute (2.5)
and use

    q_1-q_2=2c Delta/(q_1+q_2).

This proves (2.6), its sign, and the stated zero cases. QED.

Thus simply overlapping an exactly mirrored pair does not create the
naively expected daughter at leading order: that proposed source is a
pressure gradient. A controlled tilt asymmetry does create a daughter.
Changing a scalar phase only changes its sine/cosine phase; it does not
invalidate the nonzero growing projection.

### A daughter can have positive instantaneous reference growth

Write s_1=u+c and s_2=-u+c. Under the source normalization

    epsilon b^2=lambda_0/(1+u^2)^(3/2),

the sum wavevector is 2b(c,0,1), and its positive-branch net rate is

    gamma_d/lambda_0=1/q(c)-4(1+c^2)/(1+u^2)^(3/2).      (2.7)

It is positive exactly when

    1+u^2 > 4^(2/3)(1+c^2).                             (2.8)

For example u=2,c=1/4 satisfies (2.8). These are allowable reference
parameters, not a claim to have located the source's globally chosen
representative point. Positive instantaneous growth does not prove a
long-time daughter pulse, a stable phase history, or a regeneration cell.

### Robustness for the actual finite-L principal matrices

The positive seeding result is not limited to setting the source matrix
error to zero. Assume the source's regular-patch bounds in the actual
moving frame:

    z'=[diag(lambda,-lambda)+E-d I]z,
    lambda>=lambda_min>0, |E_ij|<=C/L, z(0)=(P(0),0).    (2.9)

The ratio r=z_-/z_+ satisfies

    r'=-2lambda r+E_21+(E_22-E_11)r-E_12 r^2.           (2.10)

For sufficiently large L, the interval |r|<=2C/(lambda_min L) is forward
invariant: at its positive endpoint the right-hand side is negative, and
at its negative endpoint it is positive. Start at r=0 and reconstruct z_+
from its scalar exponential equation. This proves z_+!=0 and r=O(1/L),
without dividing by a potentially unknown zero.

The two columns of the actual frame both have radial component one.
Normalizing the physical amplitude by its radial component therefore gives

    h/h_r = a_+(s)+O(1/L).                              (2.11)

The source's normal/frame comparisons in Lemma 7.1 give the remaining
O(1/L) errors. The common damping d cancels from (2.10). Thus for two
clock-shifted principal pulses at a common regular representative,

    beta_actual=beta_reference+O(B_s/L),
    C_diff_actual=C_diff_reference+O(B_s/L),             (2.12)

when computed using the source normals before their common carrier k.
The projection is smooth because both output normals stay bounded away
from zero. Coefficients after restoring k acquire that same factor k.
This is a statement about the actual finite-L PRINCIPAL matrices, not the
full physical PDE or a claim that the original separated supports overlap.

A useful admissible choice is c=L^(-3/4), u fixed and at least 2. Its
positive seeding coefficient is comparable to B_s L^(-3/4), larger than
the O(B_s/L) error. The clocks are v_+=L/2+cL/u and v_-=L/2-cL/u.
Both lie in the peak plateau for large L. The envelope exponent changes
by only O(c^2 L)=O(L^(-1/2)), so neither parent is in a flat tail there.
The positive rate (2.7) also survives an O(1/L) reference perturbation on
a fixed local fast-time interval. This identifies a robust proposed local
birth channel; it does not prove its later nonlinear amplification.

## 3. The competing difference-frequency shear is unavoidable for this pair

The real field also has the interaction between xi_1 and -xi_2. Its
coefficient before -i A_1 conjugate(A_2) is

    C_diff=P_(xi_1-xi_2)[-(a_1.xi_2)a_2+(a_2.xi_1)a_1]
          = b Delta(0,c_0(q_1+q_2),-2c).                (3.1)

This follows by the same dot products: the unprojected vector is
b Delta(a_1+a_2), and the difference normal is radial. In particular

    |C_diff| >= b |Delta c_0|(q_1+q_2)>0                (3.2)

whenever the parents are nonparallel. The pressure projection retains this
tangential shear. In this REFERENCE calculation, if K_tan has a nonzero
angular component, the equal tangential wavenumbers give nonzero parent
angular frequencies but a zero-angular-frequency difference output. It is
spatially oscillating, not a spatial constant.

This distinction changes when the source's finite-L phase correction is
retained. Before rounding, for mirrored source normals at equal pulse time,

    n_+-n_-=B_s(2u,-2u/(L|g|),0)                       (3.2a)

in the (radial,N,K_tan) frame. Its small tangential component generally has
NONZERO angular frequency after multiplication by k. The actual difference
output is therefore a nearly radial sideband, not necessarily an angular
mean. We do not promote the reference angular-mean statement to the full
source. The nonzero leading size in (3.2) persists by (2.12).

For c near zero with u and c_0 in fixed nondegenerate ranges,

    beta_+=O(b c),          |C_diff| >= constant*b.       (3.3)

Thus a small asymmetry suppresses the desired sum compared to the competing
shear. The magnitudes of A_1 A_2 and A_1 conjugate(A_2) are equal. Neither
relative phase nor scalar retuning of the two pulse weights can eliminate
only the difference output while preserving the sum.

### Consequence for retaining the old source hierarchy

The source's primary normalized waves have size sqrt(epsilon) times
coefficient factors polynomial in L, and b is comparable to k with
k sqrt(epsilon) comparable to one [OA, (7.2), (7.24)]. For an overlap in
which both parent coefficients are not small, the cross source (3.1) is
therefore of order

    epsilon b A_1^{coef} A_2^{coef}
        = order(sqrt(epsilon)) times the coefficient product.  (3.4)

Here A_j^{coef} denotes the coefficient after the sqrt(epsilon) factor
has been removed; it is distinct from the Fourier coefficient A_j above.
On compact reference patches and nontrivial overlaps, (3.2) provides a
lower bound of this order, with polynomial L factors made explicit through
the chosen parent weights. Negative powers of L are not a gain of any
fixed positive power of epsilon along the source's scales.

In the fixed reference system the transverse difference mode has no
undamped linear stretching: A_ref at radial normal kills tangential inputs.
It has the O(1) viscous decay rate d_diff=epsilon b^2 Delta^2. A fixed
nonzero source vector f maintained in the co-transported reference frame
and zero initial sideband give exactly

    a_diff(v)=(1-exp(-d_diff v)) f/d_diff.               (3.5)

Thus a coherent O(sqrt(epsilon)) source over an O(1) fast-time interval
has an O(sqrt(epsilon)) response in this reference calculation. A norm
bound on an arbitrarily oscillating source alone would not prove that
lower bound; coherence or an actual Duhamel calculation is necessary.

The reference mean is outside the retained small mean-correction class
M^0.9 in [OA, (9.9)]. For the actual finite-L phases, the response is instead
a new sideband, potentially of the SAME epsilon order as the leading
waves, not a higher-order W^0.68 correction to the prescribed leading
wave. It requires a new leading component. Its gradient can be order one
because its predominantly radial wavenumber is order k. These are tests
of keeping the old hierarchy, not a proof of the full sideband's physical
history or a universal lower bound on all possible corrections.

This is a restriction on preserving the OLD perturbative hierarchy, not a
proof that nonlinear overlap is impossible. A new leading-order coupled
mean/wave system could include the shear. An exponentially weak overlap or
extra carriers can also change (3.4), but then their ability to prepare and
amplify the daughter must be proved, not inferred.

## 4. Test an escape instead of mistaking (3.1) for a universal no-go

Allow general transverse parent polarizations

    a_1=(1,d_1,-s_1), a_2=(1,d_2,-s_2).

For nonparallel parents the same algebra gives

    C_diff=b Delta(0,d_1+d_2,-2c).                       (4.1)

Thus it vanishes precisely when c=0 and d_2=-d_1. At those values,

    C_sum=(0,4b u d_1,0),      s_1=u, s_2=-u,            (4.2)

which is nonzero if d_1!=0. So a two-parent route with a canceled difference
output exists algebraically. It must not be erased by an overbroad claim.

For the source eigenpolarizations at equal |s|, however, this replacement
pairs one growing eigenbranch with one decaying eigenbranch. The second
parent has net rate

    -lambda_0/q(u)-epsilon b^2 q(u)^2 < 0.               (4.3)

Preparing that parent is an additional task; it is not another cheap
growing source pulse. Its scalar phase cannot change its eigenbranch.
The mixed-branch algebra does not close the nonlinear dynamics after the
daughter appears, as the next section illustrates for a positive-branch
asymmetric pair.

### Weak overlap is a separate escape, not excluded by the sideband size

Making the overlap exponentially weak changes the conclusion about the old
hierarchy. To calibrate this without claiming a nonlinear solution, freeze
the source-derived rates gamma_d>0 and d_diff>0 over a fixed interval and
prescribe a parent product delta. The two zero-initial-value responses are

    D(v)=delta beta_+ (exp(gamma_d v)-1)/gamma_d,
    S(v)=delta C_diff (1-exp(-d_diff v))/d_diff.           (4.4)

For c=L^(-3/4) on a fixed interval, D is of order delta L^(-3/4) and S of
order delta. Their ratio is unfavorable by a polynomial factor, but with
delta=exp(-a L), BOTH are flat at every fixed epsilon order along the
source scales. Thus (3.3) by itself cannot exclude a sufficiently weak
overlap from supplying a tiny entry seed. A long subsequent unstable
amplification would have to be proved, not inferred from (4.4).

This calculation deliberately does not model the complete nonlinear
feedback. A newly generated amplitude proportional to delta interacts with
an existing strong parent at order delta, not delta squared. Every carrier
created by those interactions belongs to the leading linear response of
the full pump background. Small delta alone therefore does NOT justify
keeping only the two responses in (4.4). The strong-overlap route needs a
changed leading system; the weak-overlap route needs the full linearized
pump evolution and nonlinear error control, including its common trace.
Neither route is excluded merely by the sideband computation.

## 5. All-output test: the newborn is not a closed three-mode system

In orthonormal coordinates (r,N,K_tan), use the exact rational pair

    xi_1=(96,0,40),  a_1=(1,-13/5,-12/5),
    xi_2=(-75,0,40), a_2=(1,-17/8,15/8),                (5.1)

and conjugates, with Fourier coefficients one. These are (2.3) with
b=40, c_0=-1, s_1=12/5, s_2=-15/8; both q values are rational.

The checker computes the full original NS quadratic convolution, without
projecting back onto selected carriers. At first nonlinear order the only
nonzero plane-wave outputs are

    +/-(21,0,80),       +/-(171,0,0).                    (5.2)

Both outputs are retained. Differentiating the original quadratic operator
once more produces nonzero feedback on BOTH parents and the additional
carriers

    +/-(267,0,40), +/-(246,0,-40),
    +/-(117,0,120), +/-(54,0,-120).                     (5.3)

This calculation is the coefficient cubic in initial amplitude in the
second time derivative of NS. Ordinary viscosity produces additional
linear/quadratic-amplitude terms, but cannot delete these cubic coefficients.
At the new frequencies (5.3) the lower-amplitude terms have no support.
The computation keeps the whole vector at each frequency, not just its
positive-eigenvector coordinate.

These are exact plane-wave Taylor coefficients, not a finite-energy R3
trajectory or a numerical blow-up. In particular the test fields have a
planar Fourier support; no conclusion about a 3D concentrating evolution
is taken from these few coefficients. Their role is to disprove the
unjustified closure of the newborn with its two parents.

## 6. A Schwartz-data, full-NS instantaneous seeding statement

The asymmetric coefficient is not an artifact of an averaged nonlinear
operator. Here is a precise realization, with the scope limited to initial
generation and not later pulse growth.

### Proposition 3: initially absent daughter, nonzero unforced derivative

Fix an asymmetric pair in (2.3), with Delta*c!=0. For every nu>0 there
exists a real solenoidal Schwartz datum d on R3 whose Fourier transform
vanishes in a neighborhood of xi_d=xi_1+xi_2, but whose local classical
unforced NS evolution has an initial Fourier derivative, represented by a
smooth function near xi_d, satisfying

    l_d( partial_t uhat(xi_d,0) ) != 0,                 (6.1)

where l_d(f)=(f_r+f_N/(c_0 q(c)))/2 is the reference daughter's growing
coordinate. This statement asserts only a nonzero derivative, not actual
subsequent growth in the source background.

Proof. Choose a nonnegative nonzero even real eta in C_c^infinity(B(0,1)).
For a sufficiently small rho>0, set

    dhat_rho(xi)=rho^(-3/2) sum_(j=1,2)
      [eta((xi-xi_j)/rho)+eta((xi+xi_j)/rho)] P_xi a_j.    (6.2)

The supports avoid zero, are disjoint, and avoid a fixed neighborhood of
xi_d. The inverse Fourier transform is real, solenoidal and Schwartz, and
has bounded L2 norm as rho decreases. Local classical NS exists for these
data in the repository's local-theory class.

At xi_d the initial viscous term vanishes exactly. Only the neighborhoods
of (xi_1,xi_2) and (xi_2,xi_1) contribute to the nonlinear convolution.
Substitute xi=xi_1+rho z into the first contribution, and similarly into
the second. The two factors rho^(-3/2) cancel the Jacobian rho^3. Since
P_xi is smooth near all these nonzero frequencies, dominated convergence
gives, with a fixed positive Fourier normalization constant c_F,

    partial_t uhat_rho(xi_d,0)
        -> -i c_F (integral eta(z)^2 dz) C_sum.          (6.3)

Equation (2.6) makes its l_d coordinate nonzero, so it remains nonzero for
all sufficiently small rho. A Fourier observation supported in a small
daughter neighborhood can equally be used in place of point evaluation.
The full PDE is used throughout: every other generated frequency and the
canonical pressure projection remain present. QED.

The datum can also be multiplied by any nonzero arbitrarily small real
constant; the derivative remains nonzero and scales quadratically. This
initial frequency birth is therefore not a diagnostic of singular behavior.

This is the standard localized-wavepacket realization of a nonzero NS
symbol. Its value here is the link to the specified source polarization;
no claim of novelty is made for instantaneous Fourier transfer. It cannot
be counted as one completed regenerative turnover.

## 7. Finite-L source-form check and actual validation

The companion `research/check_source_regeneration.py` has 28 named exact
checks, including the pressure energy cancellation, cubic preparation
integral, both source eigenpolarizations, all sum/difference coefficients,
the mixed-branch escape, conjugacy and the complete first two nonlinear
jets. It does not replace the analytic proofs above.

With `--principal`, it imports the previous in-repository
`check_source_pulse_adjoint.py` and integrates its actual three-component
principal matrices, including pressure, viscous damping, connection terms
and rounded angular carrier. Both parents are evaluated at shifted local
clocks giving reference tilts u+c and -u+c, and normalized by their radial
amplitudes. This tests a PROPOSED overlap, not an overlap already present in
the disjoint-support source.

For u=2, c=1/4, the computed positive daughter coordinate approaches the
reference value approximately 1.102226 as L grows. At L=512 it is
approximately 1.101725, while the difference-source norm is approximately
7.806843. At exact reference symmetry c=0, the finite-L source-form
coefficient need not vanish: at L=512 it is approximately -0.002376.
Thus the reference null has NOT been misreported as an exact null of the
finite-L or full physical construction.

These floating-point calibrations use F_0=R_0=1 and g_0=(-3,2). As in the
previous checker, k and L are calibration parameters, not simultaneous
realizations of all dyadic source choices. The numerical checks are neither
interval-certified estimates nor proof of convergence rates.

Executed this run: the 28 exact checks, nine finite-L coefficient cases,
Python syntax compilation, local whitespace checks, and the previous
`check_adjoint_deforcing.py` (1049 exact assertions). The complete previous
`check_source_pulse_adjoint.py` was also rerun and passed 12 exact symbolic
assertions and 102 numerical assertions. These distinct scopes are not
combined into a purported PDE-certification count.

Shell networking could not resolve the source host. The source PDF was read
through the web tool, including rendered pages 74--75; repository state and
files were read through the GitHub connector. No full repository checkout,
main manuscript build, independent mathematical audit or Lean build was
performed. No canonical graph or formal status is promoted. The numerical
report is `research/evidence/2026-09-10-source-regeneration-checks.json`.

## 8. What remains after the follow-through

The local entry-seed result survives, but direct frozen-ray preloading does
not. Internal nonlinear birth is available and can point into an unstable
reference direction. It also generates an unavoidable shear sideband at the
same epsilon order, and subsequent interactions leave the chosen triad.
The two-parent cancellation escape consumes a decaying branch instead.
Exponentially weak overlap avoids a size-only sideband obstruction, but its
complete pump-response evolution remains uncomputed.

A usable continuation must therefore solve a LEADING coupled mean/wave
history, or arrange additional carriers/overlap scales with controlled
unwanted outputs, rather than append independent cheap entry seeds to the
old source proof. It must prove an entire turnover and the data/exterior
compatibility before being iterated. No sign, convergence, or infinite
cascade conclusion follows from the nonzero instantaneous channel alone.

### Inspected sources and internal antecedents

[OA] OpenAI, *Finite Time Blowup for Navier--Stokes*, released 2026-09-08.
Inspected source locations: (6.1), (6.6), (6.11)--(6.12), (7.1)--(7.11),
(7.24), (7.30), (9.2), (9.9), and the support/product discussion in Section 6.
https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf
No full source-proof audit or formal rebuild occurred here.

[BMV] J. Bedrossian, N. Masmoudi, V. Vicol, *Enhanced dissipation and inviscid
damping in the inviscid limit of the Navier-Stokes equations near the 2D
Couette flow*, arXiv:1408.4754. Abstract inspected for prior-art scope only;
no theorem from it is used to infer a 3D result.
https://arxiv.org/abs/1408.4754

Internal antecedents at the input revision: the September 10 adjoint and
source-pulse packets, September 8 angular-preparation obstruction and
all-output Fourier-ring/cone tests. They are project work, not independent
external literature. The general importance of pre-activation damping was
already recorded in the September 9 viscous-history source audit. This
packet makes no claim to have first discovered that issue.
