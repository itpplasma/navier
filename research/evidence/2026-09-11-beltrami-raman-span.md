# Common-sphere Beltrami repair of the Raman high-cross wall

Date: 2026-09-11. Repository input:
`itpplasma/navier@3a285df917b34d810d20a2f2383bd8f46b86be0a`.

**Status: exact author theorem for the leading state-triggered Raman symbol.**
The cross-module obstruction in
`2026-09-11-raman-high-cross-wall.md` is not intrinsic to state-triggered
purification. Five high-pair modules can be placed in one equal-radius,
same-helicity Beltrami eigenspace. Their complete high-high Navier--Stokes
self-interaction is then pure pressure at arbitrary amplitude, while their
first target-triggered Raman outputs still span all of `Sym_0(3)` at the
actual clean return root.

The exact algebra is frozen by `research/check_beltrami_raman_span.py`.
This does not yet give a finite-energy whole-space realization or control the
full high--slow normal form.

## 1. One common Beltrami sphere

Let `Q,l` be perpendicular unit coordinate vectors and put

    q=N Q+l/2,
    r=-N Q+l/2,
    L=sqrt(N^2+1/4).                                      (1.1)

Then

    |q|=|r|=L.                                             (1.2)

With

    m=Q cross l                                           (1.3)

and positive-helicity polarizations

    beta_N=m+i (q cross m)/L,
    epsilon_N=m+i (r cross m)/L,                          (1.4)

one has exactly

    q.beta_N=r.epsilon_N=0,
    i q cross beta_N=L beta_N,
    i r cross epsilon_N=L epsilon_N.                      (1.5)

Therefore every Fourier mode selected from any collection of such pairs lies
in the same curl eigenspace. If `U_H` is their real superposition, then

    curl U_H=L U_H.                                       (1.6)

Using

    (U.grad)U=grad(|U|^2/2)-U cross curl U,                (1.7)

it follows identically that

    P[(U_H.grad)U_H]=0.                                   (1.8)

Thus cross-module high-high sidebands are removed exactly, not estimated as a
small perturbation. Viscosity acts on the unlocalized Fourier field by the
common scalar `exp(-nu L^2 t)`.

## 2. Target-triggered response under the helicity constraint

Let the actual ancestry-contaminated middle clean target be `(h,A)` with

    h=(z-2,-1,-1),                                        (2.1)

and `A` the denominator-cleared coefficient already frozen in
`check_state_triggered_raman_span.py`. Let

    kappa=h+l.                                             (2.2)

For the Leray interaction `C`, define

    c_N=C(h,A;q,beta_N).                                   (2.3)

Since `c_N` is transverse to `h+q`, while `epsilon_N` is transverse to `r`,
and `(h+q)+r=kappa`, the second interaction can be written exactly as

    C(h+q,c_N;r,epsilon_N)
      =P_kappa[(c_N.kappa)epsilon_N
               +(epsilon_N.kappa)c_N].                    (2.4)

As `N->infinity`,

    beta_N -> m-i l,
    epsilon_N -> m+i l,
    N^-1 c_N -> (A.Q)(m-i l).                             (2.5)

Hence

    N^-1 C(h+q,c_N;r,epsilon_N)
      -> 2(A.Q) P_kappa[(m.kappa)m+(l.kappa)l]
       =-2(A.Q)(Q.kappa) P_kappa Q.                       (2.6)

This is the Beltrami-constrained Raman symbol. The helical phase has collapsed
the formerly free high polarizations to a rigid geometric response, but it has
not collapsed the strain span.

## 3. Five explicit modules retain rank five

Use

    (l_1,Q_1)=((-1, 0, 0),(0,0,1)),
    (l_2,Q_2)=(( 0,-1, 0),(0,0,1)),
    (l_3,Q_3)=((-1, 0, 0),(0,1,0)),
    (l_4,Q_4)=(( 0, 0,-1),(0,1,0)),
    (l_5,Q_5)=(( 0,-1, 0),(1,0,0)).                       (3.1)

Every module has `|l_j|=|Q_j|=1` and `l_j.Q_j=0`, so all ten high parents
belong to the single sphere (1.2).

For each module let `d_j` denote (2.6), with the harmless common factor `-2`
removed, and form the trace-free symmetric strain

    T_j=sym(d_j tensor kappa_j).                           (3.2)

Encode `T_j` by

    (T_11,T_22,T_12,T_13,T_23).                           (3.3)

After multiplying each `P_kappa Q` by `|kappa|^2` and using the common cleared
trigger denominator, the exact `5 x 5` determinant is a degree-61 polynomial
in `z`. The checker proves

    gcd(det M(z), Q_clean(z))=1,                           (3.4)

where `Q_clean` is the exact degree-10 clean-return polynomial. Therefore the
five columns are linearly independent at every root of `Q_clean`, in particular
at the isolated positive root

    1.2847<z_*<1.2848.                                    (3.5)

Consequently

    span{T_1,...,T_5}=Sym_0(3)                             (3.6)

at the actual clean return. The previously fixed inheritance filter `H` is in
this span.

## 4. What this repairs

The independent-pump lift failed because two generic high modules created a
cross sideband of size `O(rho)` relative to a parent while useful Raman action
requires `rho->infinity`. The present construction removes that source exactly:
all high modes are parts of one nonlinear Beltrami solution, so there is no
high-high cascade to expand around.

This is a genuine mechanism change, not a smaller constant in the failed
perturbative estimate.

## 5. Recomputed frontier

The exact common-sphere field is not yet an admissible whole-space finite-energy
packet. A nonzero constant-eigenvalue Beltrami field in `L^2(R^3)` cannot exist:
its Fourier transform is supported on the sphere `|xi|=L`, a measure-zero set.
Thus the next step cannot simply declare the plane-wave background physical.

The next discriminators are, in order:

1. localize the common-sphere Beltrami field and compute the exact size of the
   curl/nonlinear defect at the useful scaling `rho^2/R=O(1)`;
2. determine whether that defect is perturbative on the clean/filter time
   window while keeping one Schwartz initial trace;
3. derive a high--slow normal form about the large Beltrami background and test
   whether the nominally large intermediate high sidebands are removable
   transport/phase terms or produce a nonvanishing higher-order feedback; and
4. only if these pass, re-run the all-orders low Raman lattice with the new
   three shifts `-e_1,-e_2,-e_3` and the exact Beltrami coefficients.

No PLAN/canonical proof-graph promotion, regenerative turnover, singular
solution, or `NS-R3` claim is made here.
