# Independent integration audit: whole-space cubic refinement

VERDICT: PASS

REVIEWED SCOPE:

Sections 1–6 of `research/evidence/2026-09-07-whole-space-cubic-refinement.md`,
including the whole-space projected ODE construction, the sharp-shell cubic
embedding and its use for overlapping increments, the time quantifiers, the
direct comparison with the canonical classical branch, the nonlinear error
identities, and the separated-scale stress estimate. This is a fresh
mathematical integration review. Component review verdicts were not used as
a correctness oracle.

Frozen base: `ec2ed88c8d1fdf3b66b0e989827d44d93f1f76df`.

Frozen proof SHA256:
`2f0a91378b48f15ca28120b62b8a5fef5f3038b36b6ca77147cd2f14a30ca347`.

Frozen new-file patch: `.git/navier-wave-20260907/integration-proof.patch`.
Patch SHA256:
`c71c04638be94796b48170c54e50df74a5be5b4cb67918b90ddfb168c3bd3061`.

The base and both digests matched when review began and at the final
post-review check; the reviewed proof and patch remained unchanged. The proof's exact
Fourier convention is exp(-2 pi i x dot xi), with physical derivatives
represented by 2 pi i xi. The canonical LOCAL, CONTINUATION and ENERGY
statements were read in `docs/proof-graph.yaml`; they are accepted scoped
premises here, not independently recertified literature results. PLAN,
the proof dossier, verifier and relevant refinement/kinetic contracts and
source ledgers were inspected for scope.

FIRST BAD BRIDGE: none in the reviewed claims.

EVIDENCE:

1. The projected family is a genuine whole-space family.

The radius-N Fourier ball has measure (4 pi/3) N^3, so Plancherel and
inversion give ||f||infinity <= B N^(3/2) ||f||2 with B=sqrt(4 pi/3).
The inequality ||f||3^3 <= ||f||infinity ||f||2^2 gives the stated second
Bernstein bound. These computations use neither an L3 sharp-ball multiplier
bound nor an angular-frequency normalization.

For a tensor S, the L2 operator norm of P_N P div is at most 2 pi N.
Applying this to b tensor a and using ||b tensor a||2 <= ||a||infinity
||b||2 gives precisely the bound 2 pi B N^(5/2) in (3). The Laplacian
constant 4 pi^2 N^2 is consistent with the same convention. Thus the
quadratic vector field is locally Lipschitz on the closed real Hilbert
space X_N. Its dimension need not be finite for the contraction proof.

All derivatives of a band-supported L2 field belong to L2 and Linfinity.
This justifies the energy pairing and its spatial-cutoff limit; the
convection boundary error is bounded by the displayed R^(-1) expression.
The L2 energy bound provides a fixed ball on which a common positive
restart time exists for each N. This proves global projected existence,
uniqueness and smoothness. It invokes no spectral gap, expanding-domain
limit, or future regularity of an unprojected solution.

Subtracting the two nested projected equations yields exactly (6),
including the negative sign of F and the nonzero initial shell. The
unresolved source does not imply the total error is unresolved.

2. The cubic synthesis inequality and its constants are valid.

For finite shell support, the low part has norm at most A_J in Linfinity
and the high part has squared L2 norm T_J by orthogonality. Chebyshev at
alpha >= 2 A_J yields 4 alpha^(-2) T_J. Integrating 3 alpha^2 times this
bound over [2 A_J,2 A_(J+1)) gives 24 (A_(J+1)-A_J) T_J. These intervals
cover the relevant positive levels; zero-width intervals and the initial
A_J=0 case cause no loss. Reindexing gives

    24 B sum_k b_k^2 sum_(l<=k) 2^(l-k) b_l.

Holder and the one-sided geometric kernel of ell1 norm 2 give (7), with
constant 48 B. L2 convergence of truncations over both shell extremes,
an almost-everywhere subsequence, and Fatou extend the result to L2
fields. No low-frequency point mass occurs in L2, and the argument works
for the Euclidean norm of vector fields.

For overlapping ball-supported increments, the bound at shell k is a
convolution with coefficients 2^((k-j)/2), j >= k-1. Its ell1 norm is
sqrt(2)/(1-2^(-1/2)). Young's inequality on ell3 therefore yields exactly
the C_syn in (8). It includes resolved corrections without pretending
they are annular or mutually orthogonal. Applying it to finite telescopic
sums and applying the coarse Bernstein/energy bound proves (1).

The amplitude-only sharpness example is valid by choosing the fixed
nonzero Schwartz field with Fourier support, for example, in
{1/2 < |xi| < 1}. Scaling gives constant c_j and constant L3 norms.
For any finite number of terms, approximation in L3 by compactly
supported functions and sufficiently separated translations make the
cubed norm approach the sum of cubed norms. This excludes p>3 for the
universal synthesis inequality. It asserts nothing about actual NS
increment geometry.

3. The time statements use the correct quantifiers.

For actual projected paths each finite W_M is continuous on [0,H]. A
common essential bound on the countably many W_M therefore gives the
same bound at every time, including the endpoints. Supremum in time of
the sum is the hypothesis; the proof does not interchange it with a sum
of levelwise time suprema.

For the generic variant, the explicitly assumed strong L2 measurability
and stated band supports give strong L3 measurability by the continuous
fixed-band map. The stated supports include the coarse radius-N0
support used in its Bernstein estimate. Taking one common null set for
the countably many support and finite-sum conditions is legitimate.
The cubic tail tends to zero almost everywhere and is bounded by K.
Finite H supplies the integrable majorant for every finite time exponent
q. Thus the sequence is Cauchy in Lq_t L3_x, as claimed, without a
uniform-in-time L3 tail conclusion.

The independent L2 tail estimate follows from Holder with exponents
3 and 3/2:

    sum_(j>=L) N_j^(-1/2) a_j
      <= K [sum_(j>=L) N_j^(-3/4)]^(2/3)
      = K N0^(-1/2) 2^(-L/2)
          (1-2^(-3/4))^(-2/3).

Actual path continuity upgrades this to C([0,H];L2) convergence. A
continuous L2 path on a compact time interval has compact image and
uniform spatial L2 tails. Uniform convergence transfers that property
to the tail of the sequence; the finitely many remaining continuous
paths each have the same compact-image property. This verifies the
global-tail statement, though it is not needed for Section 4's consumer.

4. The direct identification closes the conditional consumer faithfully.

On each T<Tstar, canonical LOCAL supplies the finite C_t H3 bound used
in (11). Projection commutes with derivatives, and Cauchy–Schwarz in
Fourier variables bounds both v_N and its gradient in Linfinity
uniformly in N. Expanding the residual as

    (r_N dot grad)u + (v_N dot grad)r_N

gives ||R_N||2 <= C ||u||H3 ||r_N||H2. On |xi|>N the H2/H3 weight ratio
is at most C/N, proving the residual rate for N>=1. This rate is a
compact-classical comparison estimate, not an endpoint estimate or an
input-only strain bound.

Projection of the original classical equation shows that the z_N
equation has forcing +R_N. Testing cancels the v_N transport and the
self-transport of z_N, leaving exactly the strain term in (10).
Regularized norm Gronwall yields O_T(N^(-1)) in C_t L2_x, and the
spectral L2 tail of the classical u tends to zero. Consequently the
dyadic projected sequence converges to the original classical branch
on every compact classical interval independently of RF-CUBE.

Under RF-CUBE, (1) bounds all finite approximations by the same M_H.
At a fixed eligible time, their L2 convergence provides a spatial
almost-everywhere subsequence; Fatou gives the classical L3 bound.
Alternatively this can first be done almost everywhere in time, as in
the proof, and C_t H1 continuity extends the bound to all classical
times. An increasing countable sequence of compact classical intervals
retains the same M_H; no comparison constant C_T enters M_H.

Choosing H>Tstar at a hypothetical finite endpoint contradicts exactly
the canonical CONTINUATION statement. The now-global canonical LOCAL
branch supplies the original unforced equation, the initial datum,
and normalized smooth velocity and pressure on every closed finite
time interval. Canonical ENERGY supplies the required energy identity
and initial-energy bound. No pressure limit of the approximations,
new weak-solution uniqueness result, or unproved endpoint smoothness
is hidden in this composition.

5. The nonlinear bookkeeping keeps the missing terms visible.

For each finite M, multiplying the error energy identity by
N_j^(3/2)||e_j||2 gives (12), since the derivative of ||e_j||2^3 is
3||e_j||2 times its Hilbert inner product with e_j'. This remains
valid at zero. The initial shell is supported above N_j, so its L2
norm is at most (2 pi N_j)^(-1)||grad d||2; the initial cubic sum is
therefore uniformly finite for any fixed positive N0.

In the resolved/unresolved decomposition, F_j is orthogonal to r_j,
but the four displayed strain pairings need not vanish. Orthogonality
only makes the outside error norm equal to
sqrt(||q_j||2^2+||r_j||2^2). Thus (14) neither drops resolved strain
nor replaces total error by the high shell.

Integrating (12) and assuming (13) at EVERY upper time gives

    W_M(t)/3 + (1-theta) nu integral_0^t D_M
      <= W_M(0)/3 + C.

This supplies the desired uniform W_M(t) bound. Control only at H
would not supply control at intervening times. The estimate itself
is explicitly unproved; the review certifies its sufficiency only.

Expanding the two individual energy identities, using orthogonality
of the initial shells, gives exactly (15). Applying
||U-v||2^2 <= 2||U||2^2+2||v||2^2 both to the velocities and integrated
gradients gives the upper estimate 4||d||2^2 sum_(j<M) N_j. This
does not produce cubic summability and is correctly not called a
lower bound or an obstruction to sharper correlated estimates.

6. The separated-scale estimate is uniform in the claimed parameters.

If q has frequencies |eta|>N, a parent of frequency at most N-K
cannot combine with it to produce output at most K. Hence the two
cross terms at that output can use p_hi in place of p, with no
discarded low-high interaction. The sharp boundaries have zero
Fourier measure and the strict q support also gives the required
inequality at K=N/2.

For an L1 tensor, its Fourier transform is bounded pointwise by its
L1 Frobenius norm. The Leray symbol is an orthogonal contraction,
and the divergence multiplier is 2 pi i xi. Direct integration over
the output ball therefore gives

    ||P_K P div S||2
      <= 2 pi sqrt(4 pi/5) K^(5/2) ||S||1.

Pointwise in time, the high supports imply

    ||p_hi||2 <= (pi N)^(-1) ||grad U||2,
    ||q||2 <= (2 pi N)^(-1) ||grad U||2.

Thus

    integral_0^H (2||p_hi||2||q||2+||q||2^2)
      <= [5/(4 pi^2 N^2)] integral_0^H ||grad U||2^2
      <= [5/(8 pi^2)] ||d||2^2/(nu N^2).

For example C=(5/(4 pi)) sqrt(4 pi/5) is an admissible absolute
constant in (16). There is no fine-cutoff or horizon dependence.
These are estimates on the actual fine flow and its projected stress.
They bound forcing into the separated output band, not the nonlinear
response or the weighted neighboring-level errors. At K=N/2 the
displayed N^(1/2) cost is correct and proves no no-go statement.

REPLACEMENT ARGUMENT: none required.

CONDITIONAL SUFFIX THAT SURVIVES:

For the explicitly constructed whole-space projected family, RF-CUBE
for arbitrary solenoidal Schwartz data, every positive viscosity and
every finite horizon supplies CRITICAL and then the canonical
LOCAL/CONTINUATION/ENERGY conclusion for the original NS-R3 target.
RF-CUBE and its signed-production estimate remain missing inputs.

UNNECESSARY DEPENDENCIES:

- The generic Lq convergence result, global approximation-limit
  identification and tail control are not needed for the shorter
  conditional NS consumer. Uniform finite-approximation L3 control
  plus compact-classical L2 comparison suffices.
- For RF-CUBE alone, (13) can allow theta=1: the integrated identity
  still bounds W_M. Strict theta<1 additionally controls accumulated
  D_M. This is an optional weakening, not a defect in the sufficient
  hypothesis currently stated.
- Energy saturation, sharpness examples, the separated-scale forcing
  estimate and prior-art comparison are not premises of the conditional
  continuation argument. They have their separately stated scopes.

NON-CLAIMS:

This PASS is not a proof of RF-CUBE, (13), arbitrary-data regularity,
a new singularity restriction, a nonlinear-response estimate, or
novelty of the spatial embedding. It does not recertify the imported
PDE interfaces, audit Section 7's source metadata or reviewer provenance,
or constitute formal verification. No canonical state was edited or
promoted. Optional wording precision would specify the sharpness
annulus and repeat the coarse support in the generic-family paragraph;
the required choices/supports are already available in its context.

REOPENING CONDITION:

Reaudit any change to the Fourier convention, frozen synthesis
inequalities, measurability/support assumptions, the quantifiers in
RF-CUBE or (13), the original-equation comparison, or the imported
consumer interfaces. Promotion of terminal claims requires an actual
arbitrary-data critical producer and its independent audit.
