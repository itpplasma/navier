# Autonomous short-time birth of the common purifier strain

Date: 2026-09-11. Repository input for the exact checker:
`itpplasma/navier@2b209e9e71eecb522828207f3124e64451eadabc`.

**Status: author proof; independent mathematical audit and novelty undetermined.**
This packet removes one narrow but load-bearing objection to the clean-gate
programme: the common strain need not be inserted by hand at a later time. A
finite collection of ordinary Navier--Stokes Fourier packets can generate the
required low-frequency strain autonomously from one initial Schwartz datum.
The result is a single short-time birth theorem. It does **not** yet prove that
the strain is born at the correct recursive clock, that the pump population is
subsequently removed, that the clean carrier geometry survives the complete
pump history, or that a turnover/blowup occurs.

The exact finite-symbol part is frozen by
`research/check_autonomous_strain_birth.py`, which passes 185 exact rational
assertions.

## 1. General exact high--high to prescribed-low synthesis

For nonzero `kappa in R3` and nonzero `d` satisfying

    d.kappa=0,                                             (1.1)

put

    r=kappa cross d.                                      (1.2)

For any nonzero scalar `N`, define

    p=N r,
    q=kappa-p,
    a=d,
    b=kappa/|kappa|^2 + r/(N |r|^2).                      (1.3)

Then, exactly,

    a.p=0,        a.q=0,
    b.q=0,        b.p=1,                                  (1.4)

and therefore the original Leray pair symbol

    C(p,a;q,b)
      =P_kappa[(a.q)b+(b.p)a]                             (1.5)

satisfies

    C(p,a;q,b)=d.                                         (1.6)

Thus every prescribed transverse low child is the exact quadratic output of
one pair of arbitrarily high transverse parent carriers. This is an identity
for the original Navier--Stokes quadratic symbol, not an averaged
nonlinearity.

For a real field the negative parent coefficients are conjugates. With real
polarizations (1.3), the matched negative pair has symbol `-d`; after restoring
the common Fourier factor `-i`, the two low coefficients are `-i d` at
`+kappa` and `+i d` at `-kappa`. Their physical low field is therefore a sine
carrier proportional to

    2 d sin(kappa.x).                                     (1.7)

## 2. Exact decomposition of the common purifier matrix

Use the stronger common strain from the preceding inheritance-filter packet,

    H = [[ 71/100,    -1,       147/200],
         [ -1,       -143/200,   7/25  ],
         [147/200,     7/25,     1/200 ]].                (2.1)

It is symmetric and trace free. Let `e1,e2,e3` be the coordinate vectors.
The following ten transverse pairs `(kappa_j,d_j)` satisfy exactly

    2 sum_j d_j tensor kappa_j = H.                       (2.2)

Off-diagonal pairs:

    (e2, -e1/2),                 (e1, -e2/2),
    (e3, (147/400)e1),           (e1, (147/400)e3),
    (e3, (7/50)e2),              (e2, (7/50)e3).          (2.3)

For the diagonal part put

    A=143/400,        B=-1/400.                            (2.4)

Then use

    (e1+e2, (A/2)(e1-e2)),
    (e1-e2, (A/2)(e1+e2)),
    (e1+e3, (B/2)(e1-e3)),
    (e1-e3, (B/2)(e1+e3)).                                (2.5)

Every `d_j.kappa_j` is zero. Consequently the real low field

    W_low(x)=sum_j 2 d_j sin(kappa_j.x)                   (2.6)

has the exact local strain

    grad W_low(0)=H.                                      (2.7)

No approximation is used in (2.2)--(2.7).

## 3. A finite pump family with an exact spectral moat

Apply (1.3) to the ten pairs above with

    N_j=100 * 3^j,       j=0,...,9.                        (3.1)

The companion checker enumerates all signed parent centers

    +/-p_j,       +/-q_j.                                 (3.2)

Among every pairwise sum of these forty signed centers, the complete set with
`|xi|<=4` consists of exactly:

* the same-carrier conjugate sums at `xi=0`; and
* the intended matched sums `+/-kappa_j`.

Every other nonzero quadratic center satisfies the exact stronger bound

    |xi|^2 >= 10000,       hence |xi|>=100.                (3.3)

Thus the desired low strain channels are separated from all cross-family and
wrong-sign quadratic channels by a large open Fourier annulus. The zero output
from a carrier and its conjugate is killed at exact center by the divergence
factor in `Q(u)=-P div(u tensor u)`.

This spectral moat is useful because packetization does not require deleting
unwanted modes: they remain in the solution but are born far outside the low
strain band.

## 4. Schwartz packet lift

Fix a real even `phi in C_c^infinity(B(0,1))`. Around each parent center in
(3.2), place a sufficiently narrow compact Fourier packet and apply the exact
Leray projector `P_xi` to the corresponding polarization. Add the conjugate
packet at the negative center. Choose one common scalar normalization so that
the physical convolution envelope of a matched pair equals one at the origin.
Call the resulting real solenoidal Schwartz field `F_delta`.

Let `Pi_low` be a smooth Fourier cutoff supported in `|xi|<4` and equal to one
on a neighborhood of all `+/-kappa_j`. By (3.3), for sufficiently small packet
width `delta`, no cross-family or wrong-sign nonzero quadratic packet meets
`Pi_low` at all. Taylor expansion of the smooth Leray symbol inside each
matched packet gives, in every fixed Sobolev norm,

    Pi_low Q(F_delta)
      = common_envelope(x)
          sum_j 2 d_j sin(kappa_j.x) + R_delta,            (4.1)

with

    ||R_delta||_(H^m) <= C_m delta.                        (4.2)

The near-zero self-conjugate windows also gain the small output-frequency
factor from `div`; they are included in `R_delta`. Since every sine in (4.1)
vanishes at the origin, differentiation of the common envelope contributes no
leading term there. Hence, after the stated normalization,

    grad Pi_low Q(F_delta)(0)=H+O(delta).                  (4.3)

This is a standard compact-packet consequence of the exact finite symbol
certificate; no numerical PDE approximation is used.

## 5. Actual unforced R3 short-time birth

Fix `nu>0` and take a Sobolev index high enough for `C^1` point evaluation.
For every amplitude `A>=1`, let `u_A` be the classical original unforced
Navier--Stokes solution from

    u_A(0)=A F_delta.                                     (5.1)

Put

    v_A(s,x)=A^(-1) u_A(s/A,x),       mu=nu/A.             (5.2)

Then

    partial_s v_A=mu Delta v_A+Q(v_A),
    v_A(0)=F_delta,       0<mu<=nu.                        (5.3)

The ordinary high-Sobolev local estimate gives one input-determined interval
`0<=s<=s0` and uniform bounds for all `A>=1`. The same Banach-space Taylor
argument used in the clean-first-gate packet yields

    u_A(s/A)
      =A exp(nu(s/A)Delta)F_delta
       +A s Q(F_delta)+E_A(s),                             (5.4)

    ||E_A(s)||_(H^m) <= C A s^2.                          (5.5)

The initial pump spectrum is disjoint from the low band, so

    Pi_low exp(nu(s/A)Delta)F_delta=0.                     (5.6)

Applying `grad Pi_low` at the origin to (5.4), and using (4.3), gives

    grad Pi_low u_A(s/A,0)
       =A s [H+O(delta)+O(s)].                             (5.7)

Therefore, for fixed sufficiently small `delta,s>0`, one genuine finite-energy
Schwartz solution of the original unforced equation autonomously creates a
nonzero low-frequency strain with the required common-purifier orientation.
All viscosity, pressure, pump cross-products and high-frequency sidebands are
part of the same exact solution; only the low observation is isolated by
`Pi_low`.

This is the precise sense in which the strain can now be **born rather than
inserted**.

## 6. What this changes, and the new blocker

The previous inheritance-filter packet ended at the forbidden instruction
"turn on `H` after the second targets are born." The present construction
shows that there is no algebraic or finite-energy obstruction to generating
that `H` from the same initial Cauchy datum. The unresolved issue is now
quantitative timing and state integration.

In particular, (5.7) alone does not prove that:

1. the pump-generated strain reaches the advective strength required by the
   clean-gate discriminator while its earlier integrated effect on the clean
   parents is negligible;
2. pump--clean cross interactions stay harmless in the target windows;
3. the high-frequency pump population disappears after the filtering stage;
4. the filtered target triple has the phases/envelopes required for the next
   rescaled clean birth; or
5. the construction repeats from one common Schwartz datum.

The next calculation should therefore be a **clocked autonomous strain pulse**,
not another static carrier identity. A particularly relevant possibility is to
use two or more pump layers with different viscous decay rates but the same low
child. Their low Duhamel tails can be arranged to cancel, producing a strain
that is small initially, rises on a chosen viscous clock, and then disappears
without an external switch. This directly targets the remaining timing/reset
objection.

## 7. Audit boundary

The exact statements in Sections 1--3 are mechanically checked with rational
arithmetic by `research/check_autonomous_strain_birth.py` (185 assertions).
Sections 4--5 use the same narrow-packet expansion and uniform short-time
classical theory already used by the repository's clean-first-gate theorem.
An independent proof audit and literature novelty check remain required.

No regenerative turnover, common infinite cascade, unforced singular solution,
or arbitrary-data regularity estimate is supplied. `NS-R3` remains unresolved.
