Controller-retained worker snapshot, 2026-09-07. Original worker file: large-q-production.md;
SHA256 `4aa5860b28239ee917996e4775e9e564691e0d6160453bee2b69bb2f9c365fc1`.
Author derivation with independent mathematical audit PENDING. This
record is evidence for further research, not an established graph theorem.
The original worker text follows unchanged. PLAN alone allocates work.

# Large-q concentration, actual record crossings, and the remaining cost

Date: 2026-09-07. Third bounded DISCOVER/PROVE period.
Frozen repository base: ec2ed88c8d1fdf3b66b0e989827d44d93f1f76df.
Owned file: this scratch record only; earlier scratch files unchanged.
Status: author derivations, no independent audit or claim promotion.

## Exact target

Original unforced NS on R3, solenoidal Schwartz datum f, fixed nu>0. Let
N_j=2^j N0 and u_j be the actual full spherical Fourier-Galerkin solution
with initial value P_{N_j}f. All nonlinear modes below each cutoff remain.
Set

  e_j=u_{j+1}-u_j,  a_j=N_j^(1/2)||e_j||2,
  W_q(t)=sum_{j<M} a_j(t)^q,

for one fixed finite q>3, with q=6 the designated test. The intended output
is sup_M sup_{t<=H} W_q(t)<=C(f,nu,H). A Lorentz consumer is being checked
separately by the controller; this note does not certify it or substitute
the q=infinity endpoint.

The exact weighted equation is

  (1/q) W_q' + nu sum_j N_j^(q/2)||e_j||2^(q-2)||grad e_j||2^2
    = sum_j N_j^(q/2)||e_j||2^(q-2)
                  [<F_j,e_j>-b(e_j,u_j,e_j)].           (0.1)

This period changes the object from a source/angle estimate to concentration
and record crossings. The claims below use actual projected NS trajectories,
not an assumed scalar shell model or arbitrary sequence of Hilbert vectors.

## 1. Actual high-component concentration estimate

Retain the distinction

  h_j=(P_{N_{j+1}}-P_{N_j})u_{j+1},
  r_j=P_{N_j}u_{j+1}-u_j,
  e_j=h_j+r_j,
  b_j=N_j^(1/2)||h_j||2.

Thus b_j<=a_j, but equality is not assumed. Let E=||f||2^2. The fine energy
law and the support |xi|>N_j give, for every H,

  integral_0^H b_j(t)^2 dt
    =N_j integral_0^H||h_j||2^2 dt
    <= N_j^(-1) integral_0^H||grad u_{j+1}||2^2 dt
    <= E/(2nu N_j).                                   (1.1)

Consequently, for any J>=0 and lambda>0,

  integral_0^H sum_{j>=J} b_j(t)^2 dt <= E/(nu N_J),     (1.2)
  integral_0^H #{j>=J:b_j(t)>=lambda} dt
                          <= E/(nu N_J lambda^2).       (1.3)

Tonelli justifies the infinite sums; all summands are nonnegative. This is
an input-only bound on the time spent with many high components above a
threshold, uniform in the number of actual refinement pairs.

In particular (b_j(t)) belongs to ell2, and hence to ellq for every q>=2,
for almost every t. More quantitatively,

  integral_0^H (sum_{j>=J} b_j(t)^q)^(2/q) dt
                                      <= E/(nu N_J).    (1.4)

This is a genuine concentration gain, but has two precise limitations:

1. It is an L2-in-time bound on the ellq norm, not an L-infinity-in-time
   bound. The exceptional times remain exactly where a terminal obstruction
   could concentrate. Increasing q does not improve the time exponent in
   this estimate.
2. It controls the high component h_j only. The full error contains r_j,
   which has no Poincare lower frequency N_j. Applying (1.1) to e_j would
   silently discard the resolved correction and would be invalid.

No claim that these estimates prevent actual simultaneous high-frequency
concentration is made. In particular, finite integral of the count does not
bound its supremum or the number of crossings without a time-duration bound.

## 2. A nonlinear modulus at a full refinement record

The exact equations supply a useful duration bound, with no unknown strain
norm. Suppose on a time segment I all full increments through index j obey

  a_k(t)<=A,  0<=k<=j, t in I.

This hypothesis is appropriate before the first crossing of a proposed
global barrier A. Define the input-plus-record quantity

  K=A+N0^(1/2)||f||2.

The telescoping identity u_{j+1}=u_0+sum_{k=0}^j e_k is exact. Since e_k
has upper Fourier support 2N_k, Bernstein and geometric summation give

  ||u_{j+1}||infinity <= C N_j K,
  ||grad u_{j+1}||2 <= C N_j^(1/2)K,
  ||A u_{j+1}||2 <= C N_j^(3/2)K.                      (2.1)

For example, ||e_k||infinity<=C N_k^(3/2)||e_k||2
<=C N_k A, whose dyadic sum is bounded by C N_j A.
The gradient and second derivative sums have ratios sqrt(2) and 2sqrt(2),
respectively. The coarse term u_0 uses its spectral radius N0 and its exact
input energy bound. The same estimates hold for u_j with these larger
right sides.

The full projected equation and the ordinary product estimate imply

  ||partial_t u_{j+1}||2
    <=nu||Au_{j+1}||2+||u_{j+1}||infinity||grad u_{j+1}||2
    <=C N_j^(3/2)(nu K+K^2).

Subtract the two actual equations. Since the norm is absolutely continuous,
this proves the full-error record modulus

  |a_j'(t)| <= C N_j^2(nu K+K^2)                       (2.2)

for almost every t in I. The same bound holds for |b_j'|, by projecting the
fine equation onto its high shell. This is a concrete nonlinear estimate
using the currently proposed record value and known coarse input, not a
future strain norm or a cutoff-dependent estimate hidden in an unspecified
constant. Its parabolic factor N_j^2 is explicit.

## 3. What an actual crossing costs

Suppose b_j has a crossing on [s,t] from lambda/2 to lambda, with
b_j>=lambda/2 throughout that interval, and the record hypothesis above
holds there with lambda<=A. For example choose the last lambda/2 crossing
before the first lambda crossing. Equation (2.2) gives

  t-s >= lambda/[2 C N_j^2(nu K+K^2)].                  (3.1)

The actual fine viscous energy spent on this high component is therefore

  nu integral_s^t||grad h_j||2^2
    >= nu N_j integral_s^t b_j^2
    >= c nu lambda^3/[N_j(nu K+K^2)].                   (3.2)

Equations (2.2)--(3.2) are the positive record-crossing result of this
period. They include the full vector coupling through the original
equations and a bound on all FULL increments, not a passive scalar surrogate.

The cost in (3.2) decays as N_j^(-1). Its dyadic sum is finite. Thus even
if a single common energy budget could be charged across all levels, this
lower bound would not force finitely many increasingly fine critical
crossings. In the actual paired sequence the energy budgets additionally
belong to different fine flows, so there is no automatic common account.

For a fixed j, disjoint crossings can be counted using (3.2) and the fine
energy law, but the resulting upper bound grows proportionally to N_j:

  number of such crossings
    <= C E N_j(nu K+K^2)/(nu lambda^3).                 (3.3)

Increasing q in W_q weights each amplitude crossing by lambda^q. It does
not change the N_j^(-1) spatial factor in its demonstrated energy cost.
Thus this actual record argument does not provide a uniform number of
active levels or a uniform finite-q sum. No assertion that NS actually
realizes infinitely many such crossings is inferred from this failure.

If the full a_j is large mainly because of r_j, even the high-shell cost
(3.2) need not apply to that full-error record. The modulus (2.2) remains
valid, but its conversion into a frequency-N_j dissipation cost is exactly
where the missing resolved-component control would be needed.

## 4. Concentrating the q-weight does not create a dissipative sign

There is a genuine common-data R3 test of the stronger proposed premise
that domination by one largest increment makes the weighted signed
production favorable once its critical amplitude is large. That premise
fails for every fixed finite q>3; a full-input-dependent barrier is not
refuted by this test.

Choose a real solenoidal Schwartz a supported strictly below N0 with

  F0=-(P_{2N0}-P_{N0})B(a,a)!=0,

and with B(a,a) supported below 2N0. Such data can be constructed with
narrow smooth Fourier packets around +/-p,+/-q, where p=(1,0,0), q=(0,1,0),
and solenoidal polarizations are the Leray projections of e2 and e3.
Choose 1<N0<sqrt(2) with packet-width margins. The nonzero output near p+q
is certified by

  P_Leray(p+q)[(e2.q)e3+(e3.p)e2]=e3.

Nonnegative narrow packets preserve the sign of this component by
continuity; other packet outputs are disjoint there. Opposite real-even
packets make a real Schwartz velocity. The input support lies below N0,
and its quadratic product support lies below 2N0. These are full R3
Galerkin trajectories, not a claim that the packet family is invariant.

Consider the three actual cutoffs N0, 2N0, 4N0 with the SAME input R a,
R>=1. Let y_l(tau)=R^(-1)u_l(tau/R), l=0,1,2. They solve their full
projected equations with viscosity nu/R and common input a. Taylor
differentiation at zero gives, uniformly for nu/R in [0,nu],

  y_1-y_0=tau F0+O(tau^2),
  y_2-y_1=O(tau^2).                                   (4.1)

The first difference has derivative F0. The second has derivative zero
because both larger cutoffs retain the complete initial quadratic product.
Uniform Taylor remainders follow from the bounded bilinear vector fields
at these fixed cutoffs, their energy bounds, and the compact viscosity
parameter interval. Their differentiated remainders have the corresponding
orders. No external analytic-solution theorem or numerical experiment is
being imported.

For each fixed q>3 and sufficiently small fixed tau>0, the normalized
two-increment quantity therefore satisfies

  W_q^norm(tau)
    =N0^(q/2)||F0||2^q tau^q+O(tau^(q+1)),
  (W_q^norm)'(tau)
    =q N0^(q/2)||F0||2^q tau^(q-1)+O(tau^q)>0.          (4.2)

Also the second critical increment is at most C tau times the first.
The first increment is strictly increasing on this short interval and
is the largest increment throughout it. For q=6 its dominance in W_6
is even stronger than its dominance in the maximum.

In physical variables at time tau/R,

  a_0 >= c R sqrt(N0) tau||F0||2,
  a_1/a_0 <= C tau,
  W_q' = R^(q+1)(W_q^norm)' >0.                        (4.3)

Thus the largest active critical increment can be arbitrarily larger than
nu, can dominate the entire finite-q sum, and can still be an increasing
record along genuine common-data solutions. All initial refinement errors
are zero. By (0.1), the weighted signed source production exceeds its
viscous dissipation at these times. Raising q does not change that sign;
it concentrates more weight on the growing pair.

This refutes only a concentration-based, viscosity-scale dissipative
maximum principle claimed uniformly over amplitude, or a claim that large
q alone makes the signed right side nonpositive in the dominated state.
It does NOT refute an input-selected threshold, a signed time-integrated
budget depending arbitrarily on R a, or the desired finite-q estimate for
one fixed datum. It uses a finite band M=2, which is enough to test a
universal differential maximum principle asserted for every M. No claim
about domination of an infinite sequence is made.

## First shared unknown and handoff

NEW POSITIVE GAIN: high-component threshold occupation has the uniform
bound (1.3), and actual full-NS record crossings have the modulus (2.2)
and energy cost (3.2). These are quantitative concentration statements,
not restatements of the relative-strain Gronwall estimate.

FIRST FAILED BRIDGE: using that energy cost to bound the number of
high-scale active records uniformly fails because the cost decays as
N_j^(-1). For resolved-error records there is an additional missing
frequency-to-dissipation comparison. The input-only occupation bound is
L2 in time and cannot exclude exceptional-time concentration.

The isolated-active-pair test shows that weighting by a larger finite q
does not by itself supply the missing favorable sign. The still-open
producer must use an additional actual cross-level correlation or a
stronger cost per critical record, with constants allowed to depend on
the full datum. No arbitrary model sequence has been presented as NS.

NEXT DISTINCT ACTION: identify a conserved or dissipated quantity that
charges an actual transfer record by more than its L2 energy, or prove
that the actual source/feedback imposes a non-summable delay between
successive critical records. Repeating the existing L2 energy charge
with a different finite q cannot remove its explicit spatial scaling.

Evidence: all calculations above are direct Fourier support, Bernstein,
energy, and fixed-cutoff ODE derivations using the project's inspected
paired-refinement contract. No external source theorem, new computation,
source download, build, formalization, or independent audit was used.
No tracked repository file was edited by this worker.
