# Routed first gate in the actual unforced R3 equation

Date: 2026-09-11. Repository input before this packet:
`itpplasma/navier@a399af54b275542e81eed0c335f3ee337a18d64f`.

**Status: author proof; independent mathematical audit and novelty undetermined.**
This note proves a finite-time, one-generation realization in the original
unforced Navier--Stokes equation on R3. It does **not** prove a second gate,
a regenerative turnover, one-data infinite cascade, or finite-time blowup.
No PLAN/manuscript/proof-graph/formal status is promoted.

The input is the exact three-pulse Leray-symbol circuit in
`2026-09-11-dyadic-symbol-circuit.md`. Its co-located Fourier polynomial has
unwanted order-one pair outputs. The point here is to prove that the first
selected generation can nevertheless be implemented by ordinary Schwartz
initial data in two widely separated physical interaction sites, while
retaining the mandatory sibling and the complete original equation.

## 1. Exact carrier allocation

Use

    k1=(1,0,0),       a1=(0,1,1/2),
    k2=(1,1,0),       a2=(1,-1,-2/3),
    k3=(1,0,1),       a3=(1,0,-1).                       (1.1)

For the symmetric Leray pair

    C(p,a;q,b)=P_(p+q)[(a.q)b+(b.p)a],                   (1.2)

the two local gates are:

**site 13:** carriers `k1,k3`. Both nonzero outputs are useful:

    k1-k3=(0,0,-1),   C(k1,a1;-k3,a3)=(-1/2,1,0),
    k1+k3=(2,0,1),    C(k1,a1; k3,a3)=(1/10,1,-1/5).    (1.3)

**site 12:** carriers `k1,k2`. The negative-sum output is the first selected
circuit child,

   -k1-k2=(-2,-1,0),
    C(-k1,a1;-k2,a2)=(-1/5,2/5,1/6),                    (1.4)

but the difference sibling is unavoidable,

    k1-k2=(0,-1,0),
    C(k1,a1;-k2,a2)=(-1,0,7/6).                          (1.5)

Its squared coefficient norm relative to (1.4) is exactly

    (85/36)/(41/180)=425/41>10.                          (1.6)

Thus the sibling is explicitly retained and is not called a small error.
The purpose of routing is only to suppress the **unused k2--k3 collision**
at this gate. In a fully co-located field that collision is nonzero, for
example

    C(k2,a2;k3,a3)=(10/9,-10/9,-10/9).                   (1.7)

The companion checker freezes these coefficients and all twelve co-located
first-generation output centers. Their minimum mutual distance is one.

## 2. Exact solenoidal Schwartz carrier packets

Fix a nonzero real even `phi in C_c^infinity(B(0,1))`. For
`0<delta<1/20`, a carrier `(k,a)` with `a.k=0`, and a center `X in R3`,
define a real Schwartz field by its Fourier transform

    Fhat_(delta,k,a,X)(xi)
       = exp(-i X.xi) P_xi a
          [phi_delta(xi-k)+phi_delta(xi+k)],              (2.1)

where `phi_delta(xi)=delta^(-3/2)phi(xi/delta)` and the harmless Fourier
normalization is fixed once and for all. If a sine rather than cosine phase
is desired, replace the plus by `i` times the odd difference. All statements
below are unchanged in norm, and arbitrary fixed carrier phases may be
inserted. Because `P_(-xi)=P_xi` and phi is real even, (2.1) has the reality
symmetry. It is exactly solenoidal and Schwartz.

Let

    f_13^X = F_(delta,k1,a1,X)+F_(delta,k3,a3,X),
    f_12^Y = F_(delta,k1,a1,Y)+F_(delta,k2,a2,Y),
    f_(delta,D)=f_13^0+f_12^(D e1).                      (2.2)

Duplicating the k1 packet is intentional: the two copies belong to two
physical gate sites. The datum remains one real solenoidal Schwartz field.

## 3. Packetization of one local Leray gate

Write

    Q(v)=-P div(v tensor v).                              (3.1)

The following is the finite-carrier packet expansion used previously in
`2026-09-08-exact-circuit-obstructions.md`, now applied to (1.3)--(1.5).
For a nonzero output center `h=p+q`, put `xi=h+delta z`. Direct substitution
in the Fourier convolution gives

    Q(f_site)^hat(h+delta z)
       = kappa_F (-i) C_h (phi*phi)(z) + R_(h,delta)(z), (3.2)

where `C_h` is the exact coefficient (1.2), `kappa_F` is the fixed Fourier
normalization, and on each fixed output window

    ||R_(h,delta)||_L2 = O(delta^(5/2)),
    ||leading packet||_L2 = c_phi |C_h| delta^(3/2).      (3.3)

Hence the relative error is `O(delta)`. The same assertion holds in every
fixed Sobolev norm after inserting the corresponding fixed carrier weights.

Proof. The support variables are `eta=p+delta y` and
`xi-eta=q+delta(z-y)`. The two factors `delta^(-3/2)` cancel the integration
Jacobian `delta^3`, leaving `(phi*phi)(z)`. On the fixed compact z support,
`P_xi` and the convection symbol are smooth because `h != 0`; Taylor
expansion about `(p,q,h)` gives an `O(delta)` pointwise symbol error.
The output occupies volume `O(delta^3)`, proving (3.3). Zero-frequency
packets, self-pairs and any leading algebraic cancellation gain an additional
factor delta from the divergence symbol or Taylor remainder; they are kept
in the error, not deleted. QED.

Because distinct nonzero co-located output centers are at distance at least
one, `delta<1/20` allows fixed disjoint observation balls around every center.
Thus the three selected packets and the sibling in (1.3)--(1.5) can be
measured independently.

## 4. Physical separation suppresses only the unused cross-site collision

For fixed delta, both fields in (2.2) are Schwartz. Let

    X_D=f_13^0,
    Y_D=f_12^(D e1).

The cross-site source is

    R_D=-P div(X_D tensor Y_D+Y_D tensor X_D).             (4.1)

For every integer m>=0,

    ||R_D||_(H^m) -> 0       as D -> infinity.             (4.2)

Proof. Leray projection is bounded on H^m and div costs one derivative.
Every derivative of `X_D` is a fixed Schwartz function and every derivative
of `Y_D` is a translate of one. By Leibniz, each H^(m+1) norm of their
products is a finite sum of L2 norms of products of such translates. Split
space into the half closer to one center and the half closer to the other.
On each half one factor is evaluated in a Schwartz tail of radius at least
D/2. Every product norm therefore tends to zero faster than any fixed power
of D. This proves (4.2). QED.

Consequently

    Q(f_(delta,D))=Q(f_13^0)+Q(f_12^(D e1))+R_D.          (4.3)

Given any eta>0, first choose delta small enough for the packet errors in
(3.3), then D large enough that (4.2) is at most eta times the smallest
selected source-packet norm. In particular the k2--k3 interaction, which
requires one factor from each site, is arbitrarily small at the first source
step. Nothing makes the within-site sibling (1.5) small.

Notice that (4.2) does not assert disjoint support at positive time and does
not contradict spatial analyticity. The packets have Schwartz tails already
at t=0, and the theorem below evolves the complete equation.

## 5. Actual short-time original-NS realization

### Theorem 1 (routed first-generation seed gate)

Fix `nu>0`, an integer `m>=0`, and eta>0. There are
`0<delta<1/20`, `D<infinity`, and a real nonzero solenoidal Schwartz datum
`f=f_(delta,D)` as above with this property.

There is `s0=s0(f,nu,m)>0` such that for every amplitude `A>=1`, the original
unforced Navier--Stokes solution from

    d_A=A f                                                (5.1)

exists classically at least to `t=s0/A`. For every `0<s<=s0`, writing
`t=s/A`,

    u_A(t)-A exp(nu t Delta) f
       = A s Q(f)+E_(A,s),
    ||E_(A,s)||_(H^m) <= C_f A s^2,                       (5.2)

where `C_f` and s0 are independent of `A>=1`.

After decreasing s0, the projections of the nonlinear increment in (5.2)
onto the three selected output windows have relative error at most eta from
the routed leading packets (1.3)--(1.4), while the contribution caused by
cross-site k2--k3 interaction has H^m norm at most eta times the smallest
selected packet. The mandatory k1--k2 sibling (1.5) is retained at its
order-one size.

Thus all three first-generation selected circuit seeds are simultaneously
created by **one actual unforced R3 solution from one Schwartz datum**, on a
time of order `1/A`, without modifying the equation or projecting unwanted
modes out of the dynamics.

Proof. Put

    v_A(s,x)=A^(-1)u_A(s/A,x),      mu=nu/A.               (5.3)

Then v solves the original projected equation with initial datum f and
viscosity `0<mu<=nu`:

    partial_s v = mu Delta v + Q(v),       v(0)=f.         (5.4)

Choose an integer M>m+5. The standard H^M energy/product estimate gives

    d/ds ||v||_(H^M) <= C_M ||v||_(H^M)^2                 (5.5)

on a classical interval after discarding the favorable dissipative term.
Hence all `0<mu<=nu` share one input-determined interval `[0,s_*]` and a
uniform H^M bound. Differentiating (5.4), or using its mild formula and the
same product estimates, gives a uniform H^m bound on the second s derivative
of

    w_A(s)=v_A(s)-exp(mu s Delta)f                         (5.6)

on a smaller common interval. Since

    w_A(0)=0,       w_A'(0)=Q(f),                          (5.7)

Taylor's theorem in H^m gives

    ||w_A(s)-s Q(f)||_(H^m)<=C_f s^2,                     (5.8)

uniformly in A>=1. Rescaling gives (5.2).

Now freeze delta and D chosen in Sections 3--4. Every selected leading
packet has positive H^m norm by (1.3)--(1.4). Choose s0 once more so that
the Taylor remainder in (5.8) is at most eta times s times the smallest
of those norms. The fixed disjoint Fourier observations are bounded on H^m,
so (3.2)--(4.3) and (5.8) give all stated observations. No estimate assumes
that unobserved modes vanish. QED.

### Corollary 2 (arbitrarily short and arbitrarily large first birth)

With delta,D,s fixed as above, the observation time `t=s/A` tends to zero as
A tends to infinity, while each selected nonlinear increment in physical
velocity has norm comparable to `A s` times its fixed packet norm. Therefore
for every prescribed L>0 one can choose A so the three selected child
observations all exceed L while retaining the same relative source geometry.

This scaling statement does not say the children contain an order-one
fraction of parent energy, nor that their output state is admissible for a
second gate. The datum changes with A.

## 6. What this closes and what it does not

This packet closes one gap between the exact circuit algebra and the actual
PDE:

    exact Leray child coefficients
       -> real solenoidal Schwartz packets
       -> spatial routing of the unused parent pair
       -> actual finite-time unforced R3 child birth.              (6.1)

It is stronger than a selected Fourier-source computation because the final
statement concerns the genuine unprojected NS branch and keeps pressure,
viscosity, all siblings, packet errors and cross-site leakage.

It does **not** close the regenerative turnover. The immediate obstruction is
now precise. The two useful outputs of site 13 are born in the same physical
interaction region, whereas the next circuit generation requires a different
pairing graph: its first child must interact separately with each of the
other two children. The strong sibling (1.5), whose source energy exceeds
the selected site-12 child by the exact factor 425/41, must also be retained.
There is no dispersion in the heat operator that automatically routes these
packets to the next sites.

Therefore the next theorem cannot merely repeat Theorem 1 independently at
another time. It must supply an **inter-generation transport/filter step**
inside one autonomous solution, or replace the circuit by a geometry whose
full output graph is self-routing. Resetting daughter locations would return
to externally prepared pulses.

For the OpenAI de-forcing objective, Theorem 1 is nevertheless directly
relevant: source pulses need exponentially small entry seeds, not an order-one
energy transfer. A sufficiently weak actual gate can generate a seed while
its feedback is perturbative. Matching the source's near-coplanar pulse
eigengeometry and its prescribed spacetime rectangles is still unproved.

## 7. Reproducible finite algebra and validation boundary

`research/check_routed_first_gate.py` records the exact carrier allocation,
all six displayed pair coefficients, the twelve nonzero co-located output
centers, their minimum separation, and the mandatory sibling. Its finite
algebra was independently recalculated with exact SymPy arithmetic before
upload. The continuum assertions are proved above; the checker is not a PDE
solver.

No full repository checkout was available for this additive packet. The
repository-wide verifier, manuscript build, Lean build, historical checkers,
and independent mathematical audit were not run. No terminal claim is made.
