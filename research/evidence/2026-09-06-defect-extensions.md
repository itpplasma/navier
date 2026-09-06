# Near-2 defect regularity and quantitative no-separation

Status: author-checked; independent mathematical audit pending. No gap or
terminal node is promoted. The complete proof is manuscript source
`sections/defect_extensions.tex` at `itpplasma/navier-paper` commit
`878dcff0d72c9b94e9bb344a0c8a96bf8fc37a19`.

Research base: `4c49cdd1d90f9aa2a8bd5ada9d1c24a18ecfc9f0`.
Manuscript integration base: `0c922e8961717be450b7ea28b948755d384f7274`.
The latter's previous integration workflow failed on overfull boxes; its
working-tree diagnostic archive is not a committed integration revision.

## Result A: an actual spatial regularity extension

For a real solenoidal H1 field u on R3 let w=u+q be the cubic minimizing
representative, d=div(w)=-sigma. The audited HF23 theorem supplies grad(w),
grad(q),d in L2. Set n=w/|w| off its zero set and e1 on the zero set,
N=n tensor n-I/3, H=D2 Delta^-1, and T=H-I/3. All matrix norms are
Frobenius; H has symbol xi tensor xi/|xi|^2, with positive sign.

The variational identity gives d+n^T grad(w)n=0. This remains valid almost
everywhere on the zero set because every weak derivative of w vanishes
there. Fourier div-curl gives grad(q)=H d, with no harmonic ambiguity:
the difference is L2 with Fourier support at zero and therefore vanishes.
Consequently

    d = K_n d + F_n,
    K_n f = -(3/4) N:T f,      F_n = -(3/4) N:grad(u).

This is a linear equation for the already determined defect with the
measurable coefficient n frozen. No derivative of n is taken. Plancherel
and |N|_F=sqrt(2/3) give ||T||_2=sqrt(2/3) and ||K_n||_2<=1/2.

Let tau_r denote the complex Lr scalar-to-matrix norm of T, and set

    M=max(2,tau_(4/3)/tau_2,tau_4/tau_2),
    theta(r)=4|1/r-1/2|,
    I={r in (4/3,4): theta(r) log(M)<log(2)},
    k_r=(1/2) M^theta(r), A_r=sqrt(6)/(4(1-k_r)).

Classical unweighted Riesz-transform boundedness makes M finite, and
Riesz-Thorin makes I a uniform nonempty open interval around 2. For r in
I and grad(u) additionally in Lr, the full proof establishes

    ||sigma||_r <= A_r ||grad(u)||_r,
    ||grad(q)||_r <= (tau_r+1/sqrt(3)) A_r ||grad(u)||_r,
    ||grad(w)||_r <= [1+(tau_r+1/sqrt(3)) A_r] ||grad(u)||_r.

There is no circular absorption of an unknown Lr norm: the same Neumann
partial sums converge in L2 and Lr, and their distributional limits agree.
The pre-existing sharp L2 defect constant 1/2 is retained; A_2 is not sharp.
No numerical radius for I or full-exponent weighted CZ theorem is claimed.
For r<2 the extra whole-space gradient integrability is not inferred from
Hk smoothness. This is a spatial extension, not a new temporal budget.

## Result B: a quantitative reverse finiteness implication

Let E=||u||_2^2, Y=||grad(u)||_2^2, Z=||Delta(u)||_2^2, Q0=Q(u0),
and B_Q(t)=integral_0^t D_Q. The accepted weighted coercivity and Leray L9
bound (constant C9 in the manuscript's F5) give

    ||u||_9^3 <= C9^3 (9 S^2/8) D_Q.

The pressure-free enstrophy test with exponents (9,18/7,2), interpolation
and the exact Young maximum then give

    Y'+nu Z <= [4 S^3 C9^3/(3 nu^2)] D_Q Y.

The resulting integrating-factor estimate is

    Y(t)+nu integral_0^t Z <= Y0 exp[4 S^3 C9^3 B_Q(t)/(3 nu^2)].

Apply the accepted HF25 bound B_Q <= (2Q0/nu) exp(Lambda_sigma), where
Lambda_sigma=C_sigma nu^-3 integral ||sigma||_2^4. With
Astar=8 S^3 C9^3 Q0/(3 nu^3), this proves

    integral_0^t Y^2
      <= [E0 Y0/(2 nu)] exp[Astar exp(Lambda_sigma(t))].

Conversely integral ||sigma||_2^4 <= (1/16) integral Y^2. Thus finiteness
of these two integrals is equivalent on every actual selected-branch
interval, including its full lifespan. This excludes the separation that
`rem:qe-defect-scope` previously left undecided. It also supplies a direct
nonendpoint suffix for the defect criterion: no ESS theorem and no comparison
between D_Q and D3 is needed. It develops the lead already recorded in the
HF26 linearization audit; no claim of first discovery is made.

## Implication and graph wording repairs

An estimate saying the gradient condition implies the defect condition
makes the latter no stronger as a bare condition; it does not mean 'not
weaker'. That phrase was inconsistent with the displayed implication in the
manuscript, graph and historical plan. The new reverse implication is an
actual-trajectory theorem, not a consequence of comparing two integrands.
The earlier 'unsettled in both directions' record is superseded by Result B,
subject to its pending independent audit. The weighted-dissipation graph
statement also said 'ninth power of the L9 norm' where its established
manuscript inequality has the cube; this is a transcription correction only.

## Source and scope audit performed by the author

Akseli Haarala and Saara Sarsa, *Global second order Sobolev-regularity of
p-harmonic functions*, arXiv:2204.13550v2 (28 August 2022), pages 1 and 3,
were read and rendered from the primary preprint. They describe the
Cordes matrix mechanism for scalar p-harmonic functions on bounded domains.
This is methodological prior art, NOT an applicable theorem for a nonzero
prescribed curl on R3. The manuscript bibliography records this distinction.
The classical harmonic-analysis inputs are the existing Stein1970 source,
componentwise Riesz-transform boundedness, and Riesz-Thorin interpolation.
No third-party PDF is copied into either repository and no novelty claim
is made for the perturbation mechanism.

Author checks reconstructed the Hessian sign, trace coefficient 4/3,
contraction 1/2, complex interpolation, zero-set argument, simultaneous
L2/Lr limits, nonendpoint exponents, two exponential coefficients, and the
zero-datum and finite-endpoint cases. The executable regression checks exact
fractions, 1000 finite-dimensional trace identities, and interval constants;
it is not an independent mathematical review or a test of PDE trajectories.

## What still fails to close

Energy supplies integral ||sigma||_2^2 <= E0/(8 nu), not the fourth power.
Even on (0,1), the scalar (1-t)^(-1/3) separates those two integrabilities;
it is not an NS counterexample. The near-2 estimate controls sigma only by
an additionally supplied gradient norm. Interpolating that norm above L2
requires higher derivatives for which energy supplies no budget. The
reverse-enstrophy bound still has the unknown fourth-power integral on its
right side. None of these arguments establishes a signed pressure deficit,
a first-crossing barrier, or the arbitrary-data defect producer. NS-R3,
HIGH-PRESSURE, HIGH-STRAIN, CRITICAL and DEFECT-L4 remain gaps.

## Independent review obligations

Reconstruct Result A without assuming d in Lr, including consistency of the
complex multiplier extensions and the zero-set identity. Reconstruct Result B
using only the published local theory and already audited manuscript inputs,
checking horizon equality, monotone limiting integrals and all constants.
Check that the scope repairs distinguish norm comparison, actual-branch
finiteness equivalence and universal existential continuation. The review
must be separate from these author checks before any node promotion.
