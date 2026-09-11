# Reality-complete single-axis Raman transport is exactly `L2`-skew

Date: 2026-09-11. Repository input:
`itpplasma/navier@c5e51135beb2882ebf3663778bf7a8dabdcc869b`.

**Status: exact leading-effective-operator theorem.** The Fourier-reality wall
forces every single-axis Raman shift `+l` to occur with its reflected shift
`-l`. This destroys the preceding pointed-semigroup argument, but the resulting
bidirectional translation operator has a compensating exact structure: on its
active slow subspace it is skew-adjoint in the physical `L2` inner product.
Thus reality-generated cycles are conservative at leading Raman order; in
particular the unavoidable same-module depth-two return is negative
semidefinite rather than an autonomous amplification mechanism.

The algebra is frozen by `research/check_real_raman_skew.py`.

This result does not repair the common affine filter: the independent exact
Farkas certificate in `2026-09-11-real-raman-filter-farkas.md` proves that no
single trace-free strain can meet all required growth/damping signs once one
reality-generated sideband is included.

## 1. Active one-axis scalarization

Fix

    Q=e1,
    k=(x,y,c),
    l=(0,m,n),                                             (1.1)

so `Q.l=0`. Let

    e_k=P_k Q.                                             (1.2)

Then

    c_k:=Q.e_k=|e_k|^2
       =(y^2+c^2)/|k|^2 >=0.                              (1.3)

Any transverse polarization `v` decomposes into an active component parallel
to `e_k` and an inactive component satisfying `v.Q=0`. The Beltrami Raman
symbol depends only on `v.Q`, so the latter component is exactly uncoupled at
this order.

Write an active mode as

    v_k=s_k e_k.                                           (1.4)

Its physical energy is

    |v_k|^2=c_k |s_k|^2.                                  (1.5)

## 2. Reality-paired edge coefficients

For a `+l` module of complex strength `alpha`, the common-sphere Beltrami
symbol is

    R_(l,Q)(k,v)
      =-2 alpha (v.Q)(Q.(k+l)) P_(k+l)Q.                  (2.1)

Because `Q.l=0`, `Q.(k+l)=x`. Hence in the scalar coordinates (1.4),

    A_(k+l,k)=-2 alpha x c_k.                              (2.2)

Reality supplies the reflected module `(-l,-Q)` with strength
`conjugate(alpha)`. Its reverse edge is

    A_(k,k+l)=+2 conjugate(alpha) x c_(k+l).              (2.3)

Therefore

    c_(k+l) A_(k+l,k)
      +c_k conjugate(A_(k,k+l))=0.                        (2.4)

Equation (2.4) is exactly the off-diagonal condition

    W A+A^* W=0,
    W=diag(c_k),                                           (2.5)

for the physical `L2` metric on the active lattice.

Summing modules preserves (2.5), including arbitrary complex phases and
amplitudes. The full reality-complete leading Raman translation operator is
therefore `L2`-skew on every finite truncation and, formally, on the natural
weighted lattice domain.

## 3. Same-module return is negative semidefinite

Composing a `+l` edge with its reality partner gives

    A_(k,k+l) A_(k+l,k)
      =-4 |alpha|^2 x^2 c_k c_(k+l).                      (3.1)

Equivalently, for arbitrary transverse `v`,

    <v,R_(-l,-Q) R_(l,Q)v>
      =-4 |alpha|^2 x^2 c_(k+l) |v.Q|^2 <=0.             (3.2)

Thus the depth-two return isolated in the reflection-wall packet is a genuine
return to the same spectral window, but not a positive self-energy. Its sign is
fixed by the skew structure.

This resolves one ambiguity in the preceding checkpoint: the reality wall does
not by itself create an instability of the slow Raman operator.

## 4. What remains after combining the two exact results

Two facts now coexist:

1. **Raman clutter alone is conservative:** the reality-complete leading slow
   translation operator is `L2`-skew.
2. **The old simultaneous purifier is impossible:** no single trace-free affine
   strain can both retain the required target sign and damp even a six-carrier
   subset containing one reality-generated sideband.

Therefore the next mechanism must exploit time ordering or a changed consumer,
not more static filter optimization.

The cheapest exact escape is a **sequential filter**. Split the original common
inheritance objective into two or more time windows, allowing different
trace-free strains `S_1,S_2,...`. The Raman part remains conservative in every
window, while the product of noncommuting dissipative/growth propagators may
preserve the target triple without requiring each `S_j` to satisfy the
simultaneous Farkas-infeasible signs.

The first discriminator should use only the six Farkas carriers plus the other
two desired second targets. Search for a two-stage schedule with rational
trace-free `S_1,S_2` and positive durations whose exact finite-dimensional
Kelvin propagator has:

* net gain on all three intended selected targets;
* net loss on `p1,g2,g3,r1` and the depth-two real Raman sideband;
* no reset or externally prescribed state between stages.

A diagonal-rate toy schedule is only a necessary discriminator: if even the
commuting frozen-carrier exponential product is infeasible, abandon sequential
static strains immediately. If it is feasible, the next checkpoint must include
wavevector transport and the skew Raman coupling exactly.

No PLAN/canonical proof-graph promotion, recursive turnover, finite-time
singularity, or `NS-R3` conclusion is claimed here.
