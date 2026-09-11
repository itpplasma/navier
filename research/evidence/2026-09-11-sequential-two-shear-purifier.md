# Sequential two-shear purifier: simultaneous strong coexistence is unnecessary

Date: 2026-09-11. Repository input:
`itpplasma/navier@10506a8c5db4ea6c2a704f9ffbf9609615506d3d`.

**Status: exact author carrier/Kelvin reduction plus a uniform ladder
continuity argument; independent mathematical audit and novelty are
undetermined.** The result removes the requirement that the two strong
rank-one purifier channels coexist at the same instant. It does not yet prove
that the two pulses are autonomously scheduled inside one finite-energy Cauchy
history.

No recursive turnover, singular solution, or `NS-R3` result is claimed.

## 1. Exact rank-one splitting

Use the common inheritance-filter matrix

    H = [[ 71/100,    -1,       147/200],
         [ -1,       -143/200,   7/25  ],
         [147/200,     7/25,     1/200 ]].                (1.1)

The two-shear reduction supplies transverse pairs `(d_i,kappa_i)`, `i=1,2`,
with

    d_i.kappa_i=0,                                        (1.2)

and rank-one gradients

    G_i=2 d_i tensor kappa_i                              (1.3)

such that

    G_1+G_2=G,
    sym G=H.                                               (1.4)

Because of (1.2),

    tr G_i=0,
    G_i^2=0.                                               (1.5)

Thus each affine shear field

    U_i(x)=G_i x                                           (1.6)

is itself an exact steady unforced incompressible Navier--Stokes solution:
`div U_i=0`, `Delta U_i=0`, and

    (U_i.grad)U_i=G_i^2 x=0.                              (1.7)

The obstruction is therefore not the self-dynamics of either rank-one shear;
it is only how to create and schedule them autonomously with finite energy.

## 2. The common filter has strict margins

At dimensionless strain strength

    M=2048,                                                (2.1)

the common-inheritance packet proves strict normalized Kelvin-energy rates

    R_H(k,a)=-M (a.H.a)/|a|^2-|k|^2.                     (2.2)

They satisfy:

* `R_H>0` on all three intended contaminated second-target directions;
* `R_H<0` on all three rejected transverse directions;
* `R_H<0` on all original parents and all first selected carriers; and
* for the complete inherited ladder

      r_n=(-n,-1,0),  a=e3,  n>=1,

  one has exactly

      R_H(r_n,e3)=-256/25-n^2-1<0.                        (2.3)

All inequalities used below therefore have nonzero margin.

## 3. Two half-time pulses reproduce the full first variation

Normalize time by the viscous carrier scale so that the diffusion contribution
to one carrier is `-|k|^2`. Consider a small total filter parameter `tau>0`.
Instead of applying one affine gradient `M G` for time `tau`, apply sequentially

    2 M G_1    for time tau/2,                            (3.1)

then

    2 M G_2    for time tau/2.                            (3.2)

Let `E_seq(tau;k,a)` be the squared amplitude of the exact Kelvin solution
after these two affine intervals, divided by its initial squared amplitude.
The wavevector and polarization are allowed to deform during each interval;
no frozen-carrier approximation is imposed in the definition.

At `tau=0`, both intervals collapse and the carrier is `(k,a)`. The derivative
of log energy with respect to `tau` is the sum of the two half-interval
instantaneous derivatives. The strain part is

    -2 * (1/2) * [a.(2 M sym G_1).a]/|a|^2
    -2 * (1/2) * [a.(2 M sym G_2).a]/|a|^2

      =-2 M (a.H.a)/|a|^2,                                (3.3)

while the two half-interval viscous exposures add to

    -2 |k|^2.                                              (3.4)

Therefore the exact first variation is

    d/dtau log E_seq(tau;k,a)|_(tau=0)
      =2 R_H(k,a).                                         (3.5)

This is the key identity. Individual `G_i` need not have the correct sign on
every carrier. Their **sequential composition** has exactly the same first
energy variation as the full common filter.

## 4. Strict finite-set discrimination survives for nonzero time

The affine Kelvin ODE depends smoothly on `tau`, `k`, and `a`. Hence for every
fixed carrier with `R_H(k,a)!=0`, (3.5) implies the same net sign for all
sufficiently small positive `tau`:

    R_H(k,a)>0  => E_seq(tau;k,a)>1,                      (4.1)

    R_H(k,a)<0  => E_seq(tau;k,a)<1.                      (4.2)

Apply this to the finite collection consisting of the three desired second
targets, their three rejected transverse directions, the three original
parents and the three first-generation selected carriers. Since the collection
is finite and all margins are strict, one common

    tau_0>0                                                (4.3)

works for all of them simultaneously.

Thus two short sequential rank-one pulses already implement the same desired
finite carrier discrimination as the simultaneous matrix `H`.

## 5. The complete inherited ladder remains uniformly damped

The infinite ladder requires a uniform argument rather than pointwise
continuity in `n`.

During either affine pulse the wavevector solves

    k'=-A^T k,                                             (5.1)

with `A=2 M G_i`, while the transverse amplitude solves the standard finite-
dimensional Kelvin equation with coefficients bounded only by `M,G_i`. For
`0<=tau<=tau_1` small enough, uniformly in the initial wavevector,

    c |k(0)| <= |k(t)| <= C |k(0)|                        (5.2)

through both half-pulses, with fixed `c,C>0`. The total strain work on log
energy is bounded by

    C_M tau,                                               (5.3)

independently of `n`, whereas the viscous contribution for
`r_n=(-n,-1,0)` is at most

    -c_M tau (n^2+1).                                     (5.4)

Hence every sufficiently large `n` is uniformly damped for all
`0<tau<=tau_1`. The finitely many remaining `n` are covered by (3.5), (2.3),
and continuity after shrinking `tau_1` if necessary. Therefore there is one

    tau_ladder>0                                           (5.5)

such that the complete ladder is damped by the sequential filter for every
`0<tau<=tau_ladder`.

Combining Sections 4 and 5 yields one positive duration

    tau_* >0                                               (5.6)

on which the two-pulse sequence grows all intended targets and damps every
tracked rejected/inherited class including the infinite ladder.

## 6. Why this changes the autonomous construction problem

The previous finite-energy two-channel theorem proved simultaneous coexistence
only after weakening the physical channel velocities. That was useful, but a
full-strength recursive filter would eventually need a strain of order the
clean carrier's advective/viscous rate, and simultaneous high-frequency pump
families then become much harder to control.

The sequential theorem removes that requirement. It is enough to realize

    channel 1 pulse -> channel 2 pulse                    (6.1)

with little overlap. Each channel separately already has:

* exact full nonlinear 2D3C self-dynamics;
* a three-layer autonomous clock with quadratic onset and canceled slow tail;
* nested finite-energy localization; and
* one-channel Wiener shadowing by an actual unforced `R3` solution.

The strong two-family cross problem can therefore be replaced by a **temporal
scheduling problem**.

## 7. Natural scheduling by separated viscous clocks

The existing clocked channel has fast time `O(N^-2)`. Two channels with

    N_1 >> N_2                                             (7.1)

peak on well-separated times `N_1^-2 << N_2^-2`. The three-layer pulse has
quadratic onset, so the slow channel's low output is tiny on the first clock;
the fast channel's tail is exponentially small on the second clock.

However both channels' **preloaded high parents** are present from time zero.
Thus (7.1) alone is not yet a proof of autonomous scheduling. What must be
shown next is frequency-selective stability:

1. on the fast `N_1^-2` interval, cross interactions with the slow preloaded
   parents do not significantly alter the fast low output;
2. more importantly, the fast family does not change the specific slow parent
   coefficients needed for the later `N_2^-2` pulse, even though it may create
   transient sidebands near frequency `N_1`;
3. those transient high sidebands decay before the slow pulse;
4. after both low pulses, the clean target sees the sequential Kelvin map of
   Sections 3--5 up to controlled localization and packet errors.

The spectral moat mechanism used in the simultaneous weak-channel theorem is
well suited to item 2: a direct fast--slow interaction changes frequency and
cannot directly overwrite a slow parent center. A return to that center needs
at least one additional fast interaction.

This is now the first uncontrolled term. Another simultaneous-purifier
construction would not advance the route.

## 8. Scope

This packet is an exact carrier-level reduction. Piecewise affine switching is
not claimed to be an unforced physical solution; it is the consumer that the
autonomous clocked channels must approximate. The theorem says that **if** the
two individually available rank-one pulses are scheduled sequentially, their
net purifier action has the required signs. It does not assume either pulse is
individually a complete discriminator.

No PLAN, canonical proof graph, manuscript, or formal status is promoted.
Full repository verification and independent audit are pending. `NS-R3`
remains unresolved.