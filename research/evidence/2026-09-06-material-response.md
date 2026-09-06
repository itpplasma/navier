# Strong natural response and corotational material dynamics

Date: 2026-09-06. Status: author-checked; independent mathematical audit
pending. Complete component derivations, not an arbitrary-data critical
bound or a proof of NS-R3.

## Frozen inputs and source

Inspected research main: `0a15896cb7d0e0e5f50065905438831b5bffa634`.
Inspected paper main: `a7dbeb54fcf4e966ae9b59196529c30988f7a36c`.
New paper source committed through the GitHub connector at
`2959003806907fa4742518bff741f24c592921e6`, path
`sections/material_response.tex`, SHA-256
`54eb89147a08ee4403d8278fbe844bf396fb2978962cf156a6c5e547f4b90034`.
Finite regression source was committed at
`c3212286ed96d42421fb13dd0f19a4b2701a2282`.

The proof uses the accepted cubic gradient minimizer and weighted
natural-variable dissipation. The fixed-weight response mechanism was
already proved and scoped in `hf26-temporal-continuation.tex` and
`hf26-review-weighted-linearization.md`. The new proof is supplied in full
rather than importing a project lemma as literature. It adds a moving
metric and a cubic little-o limit strong enough to differentiate J(w) in
unweighted L2 even on the zero set. The finite ridge-residual construction
and its signed-work interpretation retain their predecessor supplements'
independent-audit-pending status. This document promotes none of them.

## 1. The zero-set term that the coarse estimate cannot discard

Put A(z)=|z|z, J(z)=|z|^(1/2)z, w=w(f), rho=|w|, n=w/rho off zero and
n=0 on zero. The fixed metric is M=DA(w)=rho(I+n tensor n). Its Hilbert
space identifies values on {rho=0}. Let E be the closure of G3 in that
space, P its orthogonal projection and L=I-P. These are not the ordinary
Leray projection. The natural derivative N=DJ(w) has squared metric
ratios 1 and 9/8. No inverse elliptic regularity or distributional gradient
representative for every element of E is assumed.

For B_e=I+e G+o(e) in L-infinity and h_e -> h in L3, minimize
integral |B_e^(-T)a|^3/3 over f+e h_e+G3. Define

    c=(I-n tensor n/2)G w,
    b=G^T w+c,
    z=Lh+Pb.

The theorem proves simultaneously, for positive and negative e,

    (a_e-w)/e -> z strongly in the fixed weighted Hilbert space,
    ||a_e-w||3^3/e^2 -> 0,
    (J(a_e)-J(w))/e -> N z strongly in L2,
    (J(B_e^(-T)a_e)-J(w))/e -> N(z-G^T w) strongly in L2.

The second limit matters: the earlier O(e^2) cubic error only gives a
bounded, not vanishing, squared natural Taylor error after division by
e^2. Its proof uses monotonicity against fixed L3 approximants to the
weighted response, takes e->0 first, and only then refines the approximant.
The same positive monotonicity term controls both the weighted difference
and |e| times its L3 cube. Matrix remainders are estimated in the weighted
dual space before any pairing with the possibly divergent L3 difference
quotient. This avoids the hidden assumption that the weighted limit is L3.

With B_e=I this gives the Hadamard derivative D[J o w](f)[h]=N Lh.
There is still no assertion that w itself is differentiable into L3.

## 2. Actual-flow pullback gives an exact diffusion-strain action

On each compact classical interval of the original unforced R3 equation,
write G_ij=partial_j u_i, S=(G+G^T)/2 and Omega=(G-G^T)/2. Pull back the
one-form w by the actual volume-preserving velocity flow Phi. Gradients
are preserved by pullback in the original L3 closure. The input evolves,
modulo a gradient, by the pullback of nu Delta u; the gradient is exactly
the pullback of grad(|u|^2/2-p). The changing metric is D Phi, not the
Euclidean metric held fixed.

For V=J(w) define U=(partial_t+u dot grad)V-Omega V. The resulting exact
strong-L2 identity is

    U = N [L(nu Delta u-Sw)+P cS],
    cS=(I-n tensor n/2)Sw.

Skew rotation cancels because n dot Omega w=0 and L+P=I. Thus a raw
transport norm or separate vorticity-amplitude norm is not present in
this driver. Strain is not dropped or assumed small. The two response
terms are orthogonal BEFORE application of N. With

    action = ||L(nu Delta u-Sw)||M^2 + ||P cS||M^2,

one obtains

    action = ||U||2^2-||n dot U||2^2/9,
    action <= ||U||2^2 <= 9 action/8,
    ||U||2^2 <= (9/2)nu^2 integral rho|Delta u|^2
                 +(81/16) integral rho^3 ||S||op^2.

The radial action identity gives measurability without claiming continuity
of the moving weighted projections. Testing the response with V recovers
exactly Q'+nu D_Q=-integral V^T S V. A positive action is not substituted
for the signed work in this balance.

## 3. Nonlocal residual transport is retained, not cancelled by fiat

Let Psi=Pi(V tensor V), chi=T Psi with the scalar double-Riesz contraction,
and r=chi-sum a_j h_j(V) for the finite ridge problem. The full new term is

    C_u[V] = [u dot grad,T]Psi
             +T Pi(Omega V tensor V+V tensor Omega V).

The finite residual obeys

    R' = 2<r,T Pi(U tensor V+V tensor U)+C_u[V]>
           -2<r,sum a_j Dh_j(V)U>.

The source provides the quantitative derivative inequality. Its first
pairing is L3--L^(3/2), its second L2--L2. The transport contribution to
the scalar norm is zero by a whole-space W^(1,1) cutoff argument, whereas
the displayed Riesz commutator survives. The radial feature derivative
annihilates Omega V. Constant rigid motions cancel the combined
commutator by Fourier covariance; this is a compact-test-field diagnostic,
not a finite-energy NS datum or a new regularity case.

## 4. Attempted closure and precise stopping point

The material formulation removes an artificial convection driver and
separates rigid rotation, but its absolute action bound still contains
weighted second derivatives and squared strain. The accepted energy and
moment budgets do not bound those terms at the endpoint. The complete
residual law also needs commutator control, and finite-feature Lipschitz
norms and inverse-square-root ridge factors are not uniform under
refinement. No input-only endpoint bound on L_c or on the fourth-power
defect integral follows from these local identities.

Differentiating dissipation was investigated as a way to pay for the
action. No signed estimate for the resulting higher-derivative terms was
established, so no heat-convexity assertion or differentiated weighted
projection is inserted into the manuscript. Positive-scalar heat entropy
arguments alone do not address this vector-valued quotient. This is an
unclosed mechanism test, not a no-go theorem about future refinements.
The next positive target is the exact combined action or a signed temporal
estimate that controls the complete residual; estimating every component
by its absolute size may unnecessarily destroy cancellation.

## 5. Source attribution and author verification

Constantin and Iyer, *A stochastic Lagrangian representation of the
three-dimensional incompressible Navier-Stokes equations*, CPAM 61(3)
(2008), 330--345, DOI 10.1002/cpa.20192, arXiv math/0511067v4: journal
metadata verified on the primary arXiv record; the author's PDF page 7
was directly inspected for Lemmas 3.2--3.3 and the one-form commutator.
The article supplies background attribution only; no stochastic PDE
result is imported. Natural-distance geometry and the earlier fixed-weight
project response are not claimed as new. No general novelty claim is made.

`tools/check_material_response.py` in the paper repository checks the
frozen source, labels, exact rational constants, a weighted projection and
orthogonal action, a rational rigid-rotation Riesz symbol identity, and
six nonlinear moving-metric minimization probes on three atoms, including
a zero atom and both signs of the perturbation. All passed locally.
These finite probes are not an analytic proof or an independent audit.
The main manuscript built locally with no undefined references, undefined
citations or overfull boxes. The local BibTeX binary was selected explicitly
as bibtex.original because the environment's bibtex symlink was broken.
The new section's six rendered pages and the three bibliography pages were
visually inspected. Remote integration, source replay and final maps are
to be recorded separately after execution, not presumed successful here.

Independent audit must check the moving stress expansion, the order of
limits yielding the cubic little-o, the zero-set natural derivative,
proper-flow gradient closure, matrix transposes and pressure sign,
orthogonality before N, the constants 9/2 and 81/16, and every dual space
and transport cutoff in the complete residual identity. No formal theorem,
Lean build, new axiom, public release, contact, submission, added authorship,
or gap-node promotion is claimed.
