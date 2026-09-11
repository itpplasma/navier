# Co-located clean first gate in the actual unforced R3 equation

Date: 2026-09-11. This packet combines the contamination-free carrier family
with the short-time Schwartz-packet realization argument already established
for the older routed circuit.

**Status: author proof; independent mathematical audit and novelty
undetermined.** It proves one actual clean nonlinear generation in original
unforced Navier--Stokes on `R3`.  It does not prove the router/purifier stage, a
second clean gate, regenerative turnover, or blowup.

## 1. Clean carrier datum

Let `z=z_*` be the unique positive root of the clean return polynomial in
`(1.2847,1.2848)`, and use

    k1=(1,0,0),       a1=(0,1,z),
    k2=(0,1,0),       a2=(1,0,z),
    k3=(-z,0,1),      a3=(1,0,z).                         (1.1)

The exact Leray algebra gives three selected first-generation channels, up to
reality conjugates,

    g1=-k1-k2,
    g2= k1-k3,
    g3= k1+k3,                                           (1.2)

with nonzero transverse polarizations.  At the same time all three unwanted
cross-parent channels vanish exactly at principal symbol level:

    C(k1,a1;-k2,a2)=0,
    C(k2,a2; k3,a3)=0,
    C(k2,a2;-k3,a3)=0,                                   (1.3)

where

    C(p,a;q,b)=P_(p+q)[(a.q)b+(b.p)a].                    (1.4)

Self-interactions of each exact plane-wave carrier also vanish by
transversality.

## 2. Exact solenoidal Schwartz packetization

Fix a nonzero real even `phi in C_c^infinity(B(0,1))`.  For sufficiently small
`delta>0`, define a real packet for each carrier by

    Fhat_(delta,k,a)(xi)
      = P_xi a [phi_delta(xi-k)+phi_delta(xi+k)],          (2.1)

    phi_delta(xi)=delta^(-3/2) phi(xi/delta).              (2.2)

Fixed phases can be inserted by the standard even/odd combinations.  Put

    f_delta=sum_(j=1)^3 F_(delta,kj,aj).                  (2.3)

Then `f_delta` is real, nonzero, solenoidal and Schwartz.  All three parent
families are co-located; unlike the older routed construction there is no
duplicated `k1` packet and no second interaction site.

## 3. Quadratic source: selected windows are O(1), every nonselected window is O(delta)

Let

    Q(v)=-P div(v tensor v).                              (3.1)

Near a nonzero output center `h=p+q`, write `xi=h+delta zeta`.  The standard
compact Fourier-packet expansion gives

    Q(f_delta)^hat(h+delta zeta)
      = kappa_F (-i) C(p,a;q,b) (phi*phi)(zeta)
        + R_(h,delta)(zeta),                              (3.2)

with

    ||R_(h,delta)||_L2 = O(delta^(5/2)),
    ||leading packet||_L2 = c_phi |C| delta^(3/2).        (3.3)

Thus a nonzero principal coefficient has relative error `O(delta)`.

For the three selected centers (1.2), the principal coefficients are nonzero.
For every distinct cross-parent center not in (1.2), (1.3) makes the principal
coefficient exactly zero, so that complete output window is only
`O(delta^(5/2))`.  Self-pair centers have the same extra Taylor-symbol factor
because the exact carrier self-interaction is zero.  Near zero frequency the
divergence factor supplies the corresponding small factor while the Leray
projection remains `L2` bounded.

Because the finite set of distinct output centers is separated at fixed
`z_*`, choose disjoint observation windows around the selected centers.  It
follows that for every `eta>0`, `delta` can be chosen so that

* each selected nonlinear source window differs from its exact clean Leray
  packet by at most relative error `eta`;
* the sum of all nonselected quadratic output windows is at most `eta` times
  the smallest selected source norm, in any fixed Sobolev norm after adjusting
  constants.

No unwanted mode is projected out; its leading symbol is genuinely zero and
its packet remainder is retained.

## 4. Actual short-time original-NS realization

### Theorem 1 (co-located clean first gate)

Fix `nu>0`, a Sobolev index `m`, and `eta>0`.  There is a real nonzero
solenoidal Schwartz field `f=f_delta` and `s0>0` such that for every amplitude
`A>=1`, the original unforced Navier--Stokes solution from

    u_A(0)=A f                                             (4.1)

exists classically at least to `t=s0/A`.  For every `0<s<=s0`, at
`t=s/A`,

    u_A(t)-A exp(nu t Delta)f
       = A s Q(f)+E_(A,s),                                (4.2)

    ||E_(A,s)||_(H^m) <= C_f A s^2,                       (4.3)

with constants independent of `A>=1`.

After choosing `delta` as in Section 3 and then `s0` small enough, all three
selected observations in the nonlinear increment have relative error at most
a fixed multiple of `eta` from the exact clean packets, while the complete
nonselected first-generation contribution has norm at most the same small
fraction of the smallest selected packet.

Hence one genuine unforced `R3` solution from one co-located Schwartz datum
simultaneously realizes the three clean first-generation births without the
order-one sibling present in the earlier rational circuit.

### Proof

Set

    v_A(s,x)=A^(-1) u_A(s/A,x),       mu=nu/A.             (4.4)

Then

    partial_s v_A = mu Delta v_A + Q(v_A),
    v_A(0)=f,       0<mu<=nu.                             (4.5)

Choose `M>m+5`.  The standard `H^M` energy/product estimate, dropping the
favorable viscous term, gives a common input-determined existence interval and
uniform `H^M` bound for all `0<mu<=nu`.  Define

    w_A(s)=v_A(s)-exp(mu s Delta)f.                        (4.6)

Then

    w_A(0)=0,       w_A'(0)=Q(f),                         (4.7)

and the same product estimates bound `w_A''` uniformly in `H^m` on a smaller
common interval.  Banach-space Taylor expansion gives

    ||w_A(s)-s Q(f)||_(H^m) <= C_f s^2.                   (4.8)

Rescaling proves (4.2)--(4.3).  Finally choose `s0` so the Taylor error is
small relative to the fixed positive selected packet norms supplied by
Section 3.  All unobserved modes, viscosity, Leray pressure and packet tails
remain in the exact solution.  QED.

## 5. What improved and what remains

Compared with the older routed first-gate theorem, this construction removes
three complications at once:

1. no duplicated parent packet;
2. no two-site separation merely to suppress the unused `2--3` collision;
3. no order-one mandatory `1--2` sibling at first source order.

The first gate is therefore no longer the main obstacle.

The second-generation ancestry theorem shows why this does not immediately
iterate: inherited parents contaminate later Taylor trees and even alter a
nominal second-gate target polarization at leading quartic order.  The
purifiability theorem shows that the desired component survives inside all
three contaminated targets.  The live negative route is consequently

    actual clean birth
      -> autonomous spatial separation
      -> localized mode-specific purification
      -> recombination
      -> next rescaled birth.                             (5.1)

The missing theorem in (5.1) is the physical-space router/localized-purifier
step inside one finite-energy unforced history.

## 6. Validation boundary

The exact carrier identities and return root are frozen in
`research/check_clean_dyadic_gate.py`; the packet/local-theory proof above is
the same original-NS short-time mechanism already used in
`2026-09-11-routed-first-gate.md`, now with a strictly cleaner carrier source.
No numerical PDE trajectory or external forcing is used.

No full repository verifier, manuscript/Lean update, regenerative turnover, or
terminal NS-R3 claim is made by this additive packet.
