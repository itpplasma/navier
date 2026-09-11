# Common-line Raman export has an exact Schur limit and a full-carrier purification gap

Date: 2026-09-11. Repository input:
`itpplasma/navier@667e62eae8ea61267f1ad40f803960ecef9215bb`.

**Status: author theorem for the reality-complete leading Raman slow operator.**
A two-axis common-Beltrami Raman background can be arranged so that all slow
translations lie on one common line. In a large translation-spacing limit the
bidirectional slow lattice has an explicit Schur-complement reduction: all
nonzero translated sectors are viscosity-dominated, the center sees a finite
positive semidefinite damping operator, and the remainder is `O(J^-1)` in
operator norm. With one fixed gain, the three desired second-target selected
polarizations are strictly less damped than every tracked rejected/inherited
carrier, including the complete inherited ladder.

The exact finite-dimensional algebra and uniform constants are frozen by

* `research/check_raman_common_line_schur_geometry.py`,
* `research/check_raman_common_line_rate_separation.py`, and
* `research/check_raman_common_line_schur_bounds.py`.

This is a genuine mechanism change from the excluded common-strain purifier.
It uses conservative Raman transport plus ordinary viscosity rather than a
trace-free affine strain with prescribed instantaneous signs. It is still an
effective slow-operator theorem, not yet a finite-energy full Navier--Stokes
stage or a recursive turnover.

## 1. Two axes and one translated slow line

Use the rational fast directions

    Q_A=(-1,-5,-6),       |Q_A|^2=62,
    Q_B=(10,-3,-1),       |Q_B|^2=110.                    (1.1)

Their common perpendicular is

    ell=Q_A cross Q_B=(-13,-61,53),
    |ell|^2=6699.                                         (1.2)

Let `q_i=Q_i/|Q_i|`. For an integer scale `J>=1`, take reality-paired Raman
modules with slow shifts

    +/- J ell       for axis A,
    +/- 2J ell      for axis B.                            (1.3)

The effective module strengths are chosen as

    alpha_A=64 J sqrt(30),
    alpha_B=128 J sqrt(10).                                (1.4)

Thus, with `m_A=1,m_B=2` and `w_A=30,w_B=10`,

    alpha_i=64 m_i J sqrt(w_i).                            (1.5)

Because both axes are perpendicular to `ell`, every translated frequency

    k_n=k+nJ ell                                           (1.6)

satisfies

    q_i.k_n=q_i.k.                                         (1.7)

This identity is the decisive simplification. The Raman edge coefficient grows
only like `J`, while viscosity on every nonzero translated sector grows like
`J^2 n^2`.

## 2. Reality-complete lattice operator

For one axis `q`, one shift `mJ ell`, and one complex module strength `alpha`,
the Beltrami-constrained leading Raman symbol from the preceding common-sphere
packet is

    R_+(k_n,a)
      =-2 alpha (a.q)(q.k_n) P_(k_(n+m)) q.                (2.1)

Fourier reality supplies the reverse edge

    R_-(k_(n+m),b)
      =+2 conjugate(alpha) (b.q)(q.k_(n+m)) P_(k_n) q.     (2.2)

By (1.7), these coefficients have the exact adjoint relation proved in
`2026-09-11-real-raman-skew.md`. Hence the complete Raman operator `S_J` on

    H_k=direct sum_(n in Z) {a in C^3: k_n.a=0}            (2.3)

is skew-adjoint in physical `L2`:

    S_J^*=-S_J.                                            (2.4)

Let

    (D_J a)_n=|k_n|^2 a_n.                                (2.5)

The reality-complete slow evolution is

    u_t=(-D_J+S_J)u.                                       (2.6)

Therefore, independently of the size of the Raman coefficients,

    d/dt ||u||_2^2=-2 <u,D_J u>.                           (2.7)

The Raman lattice redistributes energy but cannot create it.

## 3. Uniform complement gap on every finite load-bearing carrier

For the three desired target frequencies and the finite old/rejected carrier
frequencies used by the repository, exact interval bounds give

    |k|<3,
    |k.ell|<131.                                           (3.1)

For `n!=0` and integer `J>=1`,

    |k_n|^2
      =|k|^2+(nJ)^2 |ell|^2+2 nJ k.ell
      >6437 J^2 n^2.                                      (3.2)

The two strengths in (1.4) are both less than `405 J`, and
`|q_i.k|<=|k|<3`. Thus each unbalanced Raman edge has norm less than

    2430 J.                                                (3.3)

After balancing by the viscous diagonal, every complement-to-complement edge
satisfies

    ||D_c^(-1/2) S_edge D_c^(-1/2)||
      < 2/[5J |n n'|].                                    (3.4)

There are at most four such neighbors per lattice site. Schur's row/column
test therefore yields

    ||T_J||
      :=||D_c^(-1/2) S_cc D_c^(-1/2)||
      <=8/(5J).                                            (3.5)

For `J>=4`, `||T_J||<=2/5`. Since

    -D_c+S_cc
      =-D_c^(1/2)(I-T_J)D_c^(1/2),                        (3.6)

it follows that the complement is invertible and

    ||(-D_c+S_cc)^(-1)+D_c^(-1)||
      <= 8/(19311 J^3).                                   (3.7)

This estimate is an infinite-lattice operator bound, not a finite-depth
Galerkin observation.

The center couples only to the four sectors `n=+/-1,+/-2`. The exact crude
bound

    ||B_J||^2 < 25,000,000 J^2                            (3.8)

then gives an `O(J^-1)` bound for every contribution to the center Schur
complement that uses at least one complement-complement Raman edge. The checker
freezes the explicit estimate

    ||Schur_tail|| < 9000/J.                               (3.9)

The large constant is deliberately crude; only its uniform `J^-1` decay is
load-bearing.

The same proof is stable for spectral parameters in any fixed bounded set:
adding `lambda D_c^-1` changes the balanced complement by `O(J^-2)`.

## 4. Explicit center operator

Ignore the `O(J^-1)` complement-complement correction for a moment. The direct
center--first-star--center Schur term is positive semidefinite. For a transverse
center vector `a`, its quadratic form is

    <a,K_J^(star)a>
      =sum_(i=A,B) 4 alpha_i^2 (q_i.k)^2 |a.q_i|^2
        * [ |P_(k+m_iJell)q_i|^2/|k+m_iJell|^2
           +|P_(k-m_iJell)q_i|^2/|k-m_iJell|^2 ].         (4.1)

Because `q_i.ell=0`, every term has an elementary `J->infinity` limit. Using
(1.5),

    K_J^(star) -> K_0(k)                                  (4.2)

in operator norm, with error `O(J^-1)`, where

    K_0(k)
      =(32768/6699)
        sum_(i=A,B) w_i (k.q_i)^2
          (P_k q_i) tensor (P_k q_i).                     (4.3)

Combining (3.7)--(3.9) and (4.2), the complete center Schur complement is

    -|k|^2 I - K_0(k) + O(J^-1).                          (4.4)

Equivalently, for every fixed bounded spectral parameter `lambda`, the exact
center resolvent Schur complement converges in operator norm to

    -|k|^2 I-K_0(k)-lambda.                               (4.5)

This is the promised all-orders slow-lattice reduction. Reality reflections
and arbitrary repeated `+/-1,+/-2` translations are already included in
`S_cc`; they are not discarded as clutter.

## 5. Dynamic meaning: fast viscous sidebands adiabatically eliminate

The resolvent proof has a direct time-domain version. Split `u=(x,y)` into the
center and complement. Then

    x'=-|k|^2 x+B_J y,
    y'=-B_J^* x+E_J y,
    E_J=-D_c+S_cc.                                        (5.1)

By skewness of `S_cc` and (3.2),

    ||exp(t E_J)|| <= exp(-6437 J^2 t).                    (5.2)

Starting with `y(0)=0`, variation of constants gives `||y||=O(J^-1)||x||`.
Integration by parts in the memory integral gives

    x'
      =-[|k|^2 I+K_J]x
        + initial-layer + O(J^-1),                         (5.3)

where

    K_J=-B_J E_J^(-1) B_J^*=K_0+O(J^-1).                 (5.4)

The initial layer has width `O(J^-2)` and total effect `o(1)` on every fixed
finite time interval. Thus center solutions with center-supported initial data
converge uniformly on compact time intervals to

    x_t=-[|k|^2 I+K_0(k)]x.                               (5.5)

The complement energy is `O(J^-2)` after the initial layer. No positive-norm
Gronwall factor is used; the proof relies on the exact skew/dissipative
splitting.

## 6. Exact full-carrier selected-rate separation

For a nonzero transverse selected polarization `a`, define

    C(k,a)
      =sum_(i=A,B)
         w_i (a.Q_i)^2 (k.Q_i)^2
           /[|a|^2 |Q_i|^4].                              (6.1)

Since `q_i=Q_i/|Q_i|`, (4.3) gives

    <a,K_0(k)a>/|a|^2
      =(32768/6699) C(k,a).                               (6.2)

The exact checker proves on the complete clean-root isolating interval:

    C(k_j,v_j)<1/4                                        (6.3)

for all three desired selected second targets, while

    C(k,a)>1                                               (6.4)

for

* all three rejected second-target directions;
* all three original parents `p1,p2,p3`;
* all three first selected carriers `g1,g2,g3`; and
* every inherited-ladder carrier

      r_n=(-n,-1,0),  a=e3,  n>=1.                       (6.5)

For the ladder the exact formula is

    C(r_n,e3)
      =(422800 n^2+3209340 n+8176149)/1162810 >1.         (6.6)

Moreover every desired target has `|k|^2<4`, while every finite unwanted
carrier has `|k|^2>=1`. Hence the selected Rayleigh decay rates for the limit
operator satisfy

    desired:   |k|^2+<a,K_0a>/|a|^2 <21/4,               (6.7)

    unwanted:  |k|^2+<a,K_0a>/|a|^2 >47/8.               (6.8)

The uniform gap is therefore

    47/8-21/4=5/8.                                        (6.9)

The constants are intentionally rational and conservative. The actual margins
are substantially larger for most unwanted carriers.

## 7. The infinite inherited ladder is uniform without taking `J` after `n`

The finite-carrier Schur theorem fixes a carrier and lets `J->infinity`. That
order is not uniform in the ladder index `n`, because `r_n.ell` grows with
`n`. The ladder nevertheless has a stronger geometric estimate.

Translation along the common Raman line preserves the cross product with
`ell`. Thus every translated frequency on the lattice through `r_n` obeys

    |r_n+s ell|^2
      >= |r_n cross ell|^2/|ell|^2                       (7.1)

for every real `s`. Here

    |r_n cross ell|^2
      =2(3265 n^2-793 n+1489).                            (7.2)

The checker proves

    |r_n cross ell|^2/6699 > n^2/2                       (7.3)

for every `n>=1`. Since the Raman part is exactly skew, the full lattice energy
therefore satisfies

    ||u_n(t)||_2^2 <= exp(-n^2 t)||u_n(0)||_2^2           (7.4)

regardless of `J` and of the Raman amplitude.

Consequently large ladder indices are uniformly more strongly damped than the
desired target components. Only finitely many ladder indices need the Schur
limit, and one common sufficiently large `J` handles that finite remainder.

## 8. Effective relative purifier theorem

The new consumer is **relative attenuation**, not instantaneous affine growth.
For the limit equation (5.5), the derivative at `t=0` of the log energy of a
selected carrier is twice the negative rate in (6.7)--(6.8). Therefore for any
unwanted selected carrier `u` and any desired selected target `d`,

    d/dt log(E_u/E_d)|_(t=0) < -5/4.                      (8.1)

The finite unwanted set has strict margins, so continuity gives one
`tau_0>0` on which every such ratio decreases. Section 7 gives the same result
uniformly for the complete inherited ladder after enlarging a finite checked
prefix.

By the dynamic convergence in Section 5, the same strict relative
purification holds for the complete reality-paired Raman lattice for all
sufficiently large `J`. The desired targets themselves are only weakly damped
on that short interval and hence retain a fixed positive fraction of their
incoming amplitude.

This bypasses the exact Farkas wall because no trace-free strain is required to
make desired modes grow while unwanted ones decay. The Raman operator is
conservative; viscosity removes energy after the Raman mixer exports unwanted
components preferentially to high wave number.

## 9. What is still missing

This theorem closes the **reality-complete slow-lattice consumer** for a new
mechanism. It does not yet prove the full Navier--Stokes stage. The remaining
load-bearing steps are now different and explicit:

1. **high-background realization.** Realize the two modules (1.3)--(1.4) as
   same-helicity high pairs on one common Beltrami sphere. Because the shift
   lengths differ by a factor two, the radial high components must differ so
   that all parent wavevectors have one common magnitude;
2. **scale matching.** Choose the common high radius much larger than `J|ell|`
   and map the effective strengths `alpha_A,alpha_B` to physical high-parent
   amplitudes at fixed viscosity;
3. **finite energy.** Insert the thin-shell Schwartz localization while proving
   that its shell defect remains small after the present `J`-dependent Schur
   amplification;
4. **clean-stage timing.** Show that the preloaded mixer does not destroy the
   clean nonlinear birth before the desired second-target triple exists, or
   stage the export interaction autonomously without resetting the Cauchy
   problem; and
5. **recursive consumer.** Quantify how much relative attenuation is required
   by the next clean gate and close the stage-to-stage amplitude/energy ledger.

These are full-PDE/scaling questions. The previous simultaneous-sign
obstruction is no longer the active hard core.

No PLAN/canonical proof-graph promotion, recursive turnover, finite-time
singularity, or `NS-R3` conclusion is claimed here.
