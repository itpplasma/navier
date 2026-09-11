# Energy-controlled exterior pressure and the optimized angular barrier

Date: 2026-09-11. Input:
`itpplasma/navier@3fbc190029dc8ffaefc225fe97fcff0f614f47f3`.

**Status:** analytic author proof; independent mathematical audit and formal
verification pending. This strengthens the preceding pressure checkpoint by
removing its extra exterior-budget assumption for finite-energy quadratic
stresses. It does not bound the complete physical propagator or settle UE1.

## 1. Prediction and terminal consumer

Prediction before the exact test: an L1 exterior stress supplies a derivative-
free L2 bound for its pressure gradient in a separated inner cylinder. Combining
that bound with the preceding angular harmonic theorem makes the direct far-
pressure input an input-only quantity for every unforced finite-energy branch.

The estimate is on R3, at fixed physical viscosity nu>0, for the total unforced
velocity v with datum d in S_sigma. It is uniform on compact pre-endpoint
intervals and uses only E0=||d||_2^2, not a velocity-derivative norm. The intended
consumer is delivery of angular parent traces at N_j >= c 2^(h j/2), radius
r_j comparable to 2^(-j/2), and entry scale exp(-C j^2).

The remaining uncontrolled terms are pressure produced in the near collar,
local transport and stretching/nonlinear generation, and amplification by the
complete source-history operator. No local-window gain is substituted for that
operator. Applicable frozen controls are the earlier pressure theorem, angular
preparation, common-control criterion, local adjoint defect and terminal-open.

## 2. A separated L1-stress estimate with an explicit constant

Let S be an L1(R3) tensor, with Frobenius tensor norm in the L1 definition,
vanishing in the cylinder C_R={r<R, z in R}. In the interior define the canonical
exterior pressure gradient by the absolutely convergent kernel formula

    g(x) = integral D^3 N(x-y) : S(y) dy,
    N(x) = 1/(4 pi |x|).

This agrees there with P div S for smooth S; it requires no derivatives of S.
For every 0<s<R,

    ||g||_(L2(C_s)) <= C0 (R-s)^(-5/2) ||S||_1,
    C0 = 3/sqrt(2 pi).                                      (2.1)

**Proof.** Direct differentiation gives

    partial_i partial_j partial_k N(x)
      = [3(delta_ij x_k+delta_ik x_j+delta_jk x_i)/|x|^5
         -15 x_i x_j x_k/|x|^7]/(4 pi).

The squared Frobenius norm of this third-order tensor is
`90/(16 pi^2 |x|^8)`. Rotational invariance reduces its calculation to x=(r,0,0):
one component has magnitude 6/(4 pi r^4), and six components have magnitude
3/(4 pi r^4). If y lies outside C_R and x lies in C_s, then |x-y|>=R-s. Thus

    integral_(C_s) |D^3 N(x-y)|_F^2 dx
      <= 90/(16 pi^2) integral_(|z|>=R-s) |z|^(-8) dz
      = 9/[2 pi (R-s)^5].                                  (2.2)

Tensor contraction followed by Minkowski proves (2.1). The same separated
kernel argument with D^2 N gives p in L2(C_s); differentiation under the kernel
is valid on every smaller cylinder. Hence p is harmonic and H1-regular at the
axis there. Approximation in L1 justifies the stated class without compact
support or any derivative assumption.

## 3. Angular transmission and exact radius optimization

Let Pi_n be the natural vector rotation projection, N=abs(n)>=1. It is an
orthogonal contraction in L2(C_s). The scalar pressure has the corresponding
scalar grade, so the preceding harmonic cylinder theorem applies and gives,
for every 0<r<s<R,

    ||Pi_n g||_(L2(C_r))
      <= C0 (r/s)^N (R-s)^(-5/2) ||S||_1.                   (3.1)

No sum over all angular grades is estimated by the norm of a single grade.
The real +/-n pair can instead be treated as its orthogonal real projection,
with the same bound. Cartesian component shifts of vector grades do not
change the harmonic energy exponent N.

The logarithm of the radius-dependent factor has derivative

    -N/s + (5/2)/(R-s).

It is strictly convex and attains its unique minimum at

    s_* = 2 N R/(2N+5).                                    (3.2)

Whenever r<s_*, equation (3.1) yields

    ||Pi_n g||_(L2(C_r))
      <= C0 R^(-5/2) (r/R)^N
         (1+5/(2N))^N ((2N+5)/5)^(5/2) ||S||_1
      <= C0 exp(5/2) R^(-5/2) ((2N+5)/5)^(5/2)
         (r/R)^N ||S||_1.                                 (3.3)

This retains the full angular exponential while paying only a polynomial
factor N^(5/2). If r>=s_*, then the gap already satisfies
`R/r-1 <= 5/(2N)`; the thin-collar conclusion below is automatic. The simpler
choice s=(r+R)/2 is valid without this case split.

## 4. The actual unforced quadratic stress

On any compact interval of a classical unforced finite-energy solution v,
let chi_out(t,r) be a radial scalar cutoff between zero and one, vanishing
for r<R(t). Set

    S_out(t) = chi_out(t,r) v(t) tensor v(t).

The exact energy identity gives, pointwise in time,

    ||S_out(t)||_1 <= ||v(t)||_2^2 <= E0.                  (4.1)

Apply (3.1) or (3.3) at each time. No derivatives of chi_out occur in this
interior pressure estimate: all derivatives are on the separated Newton
kernel. The omitted stress (1-chi_out) v tensor v is a separate near-field
term and is not bounded by (3.3).

For fixed radii r_j<R_j, an interval I_j contained in [0,H], N_j=abs(n_j),
and r_j<2N_j R_j/(2N_j+5), the direct far-pressure input obeys

    J_j := integral_(I_j) ||Pi_(n_j) g_out(t)||_(L2(C_(r_j))) dt
      <= C0 exp(5/2) E0 |I_j| R_j^(-5/2)
         ((2N_j+5)/5)^(5/2) (r_j/R_j)^N_j.                 (4.2)

This is an input-only bound, with |I_j|<=H. Time-dependent radii comparable to
these scales give the analogous pointwise bound integrated over I_j.

For the source scales log N_j=O(j), log(1/R_j)=O(j), and
N_j>=c 2^(h j/2), a fixed positive ratio R_j/r_j-1 therefore gives

    log J_j <= -N_j log(R_j/r_j) + O(j)+log(C E0 H),       (4.3)

with constants independent of j and the solution's derivative norms. This is
eventually below -C_2 j^2 for every fixed C_2. In contrast to the preceding
checkpoint, a postulated exp(C j^2) exterior-budget hypothesis is unnecessary
for this quadratic stress.

If the mechanism requires J_j>=exp(-C_2 j^2), then either the already-thin case
r_j>=s_* holds or (4.2) forces

    N_j log(R_j/r_j) <= C_2 j^2 + O(j)+log(C E0 H).        (4.4)

Thus the necessary collar thickness is again O(j^2/N_j), now derived directly
from finite energy. This is a necessary condition on the stated direct input,
not on every possible velocity response to that input.

For a correction w=v-U, the same estimates can separately be applied to its
quadratic and cross stresses using
`||w||_2 <= sqrt(E0)+||U||_2` and Cauchy--Schwarz. This supplies a bound in terms
of the prescribed background norm; it does not assert any unproved uniform
bound for U, or identify a cancellation among distinct correction terms.

## 5. Frontier and scope correction

The earlier note's allowance for an arbitrarily large *direct far-pressure*
budget was too weak for finite-energy quadratic stress. Equations (4.1)--(4.3)
remove that escape on this channel. They do not give an input-only bound on
the full physical propagation of g_out through the concentrating source, or
on the near-field stress. Pressure is neither discarded nor replaced by a
finite harmonic closure.

The first dependency remains actual thin-collar entry / in-core generation
from one trace with the inherited angular hierarchy, or a complete physical
adjoint estimating those effects and the ensuing amplification. The full
nonlinear correction, Schwartz trace coherence, singularity preservation and
positive arbitrary-data RF-q producer remain unproved.

## 6. Exact checks and status

`research/check_exterior_pressure_energy.py` tests the Newton tensor constant,
its harmonic output identity, the radial tail integral, the optimization and
spatial homogeneity: 38 exact checks. The L1 approximation, angular theorem,
energy identity consumer and arbitrary-N conclusions are analytic arguments,
not conclusions drawn from those finitely many checks.

The preceding angular-pressure packet and the energy identity already used in
`2026-09-11-angular-quartic-event-budget.md` are the only theorem inputs; all
additional kernel calculations are displayed here. No new literature result
or independent review is claimed. NS-R3 and canonical proof-graph statuses
are unchanged.
