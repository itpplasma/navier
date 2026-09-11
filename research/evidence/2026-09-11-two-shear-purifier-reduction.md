# Two-shear reduction of the common purifier

Date: 2026-09-11. Repository input:
`itpplasma/navier@e3bc0e2697f6de0c539c5f73b53c86a90f6a3fdb`.

**Status: exact author linear-algebra theorem; independent audit and novelty
undetermined.** The common purifier does not require the ten low Fourier modes
used in the first autonomous-strain construction. If one retains the same
symmetric energy form and allows a harmless antisymmetric local rotation, two
transverse sine modes are enough, and two are minimal for the present full-rank
matrix. This reduces the autonomous-pump coexistence problem from ten low
families to two.

The explicit algebra is frozen by
`research/check_two_shear_reduction.py`, which passes 16 exact algebraic
assertions over the quadratic extension

    T^2=708331/5680000.                                    (0.1)

No recursive turnover or nonlinear two-pump integration is proved here.

## 1. General rank-two reduction

Let `H` be a real symmetric trace-free `3 x 3` matrix. The instantaneous
relative-energy action of a local velocity gradient `G` depends only on its
symmetric part:

    w^T G w = w^T sym(G) w.                               (1.1)

Thus a purifier with symmetric strain `H` may be replaced, for the energy-sign
mechanism, by any

    G=H+A,       A^T=-A.                                  (1.2)

Write an antisymmetric matrix as the cross-product matrix `[omega]_x`. In
three dimensions one has the exact determinant identity

    det(H+[omega]_x)=det H + omega^T H omega.              (1.3)

For nonzero symmetric trace-free `H`, the eigenvalues have both signs. The
sign of `-det H` is represented by the quadratic form `omega^T H omega`.
Therefore `omega` can be chosen so that

    det(H+[omega]_x)=0.                                   (1.4)

A generic such choice gives a rank-two matrix `G` with

    tr G=0,       sym(G)=H.                               (1.5)

Now let `G` be any real rank-two trace-zero matrix. Choose a rank
factorization

    G=U V^T,       U,V in R^(3 x 2).                      (1.6)

Put

    C=V^T U.                                               (1.7)

Then

    tr C=tr G=0.                                          (1.8)

Every real `2 x 2` trace-zero matrix is similar to a matrix with zero diagonal.
A constructive choice, whenever `e1,C e1` are independent, is the basis

    M=[e1, C e1].                                         (1.9)

Cayley--Hamilton gives

    C^2=-det(C) I,                                        (1.10)

so in this basis

    M^(-1) C M = [[0,-det C],[1,0]].                      (1.11)

Transform the rank factorization by

    U'=U M,       V'^T=M^(-1)V^T.                         (1.12)

If `u_i,v_i` are the corresponding columns, (1.11) says exactly

    u_i.v_i=0,       i=1,2.                               (1.13)

Consequently

    G=u_1 tensor v_1 + u_2 tensor v_2                    (1.14)

is a sum of two transverse rank-one gradients. Setting

    d_i=u_i/2,       kappa_i=v_i                          (1.15)

gives

    2 sum_(i=1)^2 d_i tensor kappa_i = G,
    d_i.kappa_i=0.                                        (1.16)

Therefore the real divergence-free field

    W(x)=2 d_1 sin(kappa_1.x)+2 d_2 sin(kappa_2.x)         (1.17)

has

    grad W(0)=G,
    sym grad W(0)=H.                                      (1.18)

This is exactly the local tensor required by the common energy discriminator.

## 2. Explicit reduction for the repository purifier

The current common inheritance filter is

    H = [[ 71/100,    -1,       147/200],
         [ -1,       -143/200,   7/25  ],
         [147/200,     7/25,     1/200 ]].                (2.1)

Its determinant is exactly

    det H = -708331/8000000 != 0.                         (2.2)

Choose

    omega=(T,0,0),
    T=sqrt(708331/5680000).                               (2.3)

Since `H_11=71/100`, (1.3) gives

    det(H+[omega]_x)
      = -708331/8000000 + (71/100)T^2
      =0.                                                  (2.4)

Put

    G=H+[omega]_x
     = [[ 71/100, -1,       147/200],
        [-1,      -143/200,  7/25-T],
        [147/200,  7/25+T,   1/200 ]].                    (2.5)

The upper-left `2 x 2` minor is

    -30153/20000 != 0,                                    (2.6)

so `rank G=2` exactly. The checker performs the constructive factorization
(1.6)--(1.16) over the quadratic field (2.3) and verifies both transverse dot
products and the full reconstruction.

For orientation, at the positive value

    T approximately 0.3531375964,                          (2.7)

the two resulting transverse pairs can be chosen approximately as

    d_1=( 0.355000, -0.500000,  0.367500),
    k_1=( 1.000000,  0.751576,  0.056566),                (2.8)

    d_2=( 1.022163, -0.024378, -0.053806),
    k_2=( 0.000000, -0.750184,  0.339886).                (2.9)

Their dot products vanish exactly in the quadratic field, and

    2 d_1 tensor k_1 + 2 d_2 tensor k_2 = G.              (2.10)

Hence their symmetric gradient is exactly the original `H`, not an
approximation.

## 3. Minimality

One transverse sine mode has local gradient

    2 d tensor kappa,                                     (3.1)

which has rank at most one. Its symmetric part has a zero eigenvalue and hence
zero determinant. The present `H` has nonzero determinant by (2.2), so one mode
cannot reproduce its symmetric quadratic form. Two modes are therefore
minimal once an antisymmetric part of the full gradient is allowed.

## 4. Consequence for the autonomous pump programme

The preceding autonomous-strain packet decomposed `H` into ten rational low
children solely to keep the full gradient symmetric and rational. That was
useful for an initial existence proof but expensive dynamically: ten pump
families create many cross-family sidebands.

The present result shows that the energy discrimination itself only needs two
low children. Each transverse child `(kappa_i,d_i)` can be generated by one
near-opposite high-frequency pump pair using the exact identity

    C(p_i,a_i;q_i,b_i)=d_i.                               (4.1)

Moreover each **individual** pump pair has a special invariant geometry. Its
high frequencies lie in the plane

    E_i=span{p_i,kappa_i},                                 (4.2)

while `d_i` is perpendicular to that plane. The second parent polarization can
be chosen inside `E_i`. Thus an isolated real pump pair belongs to a 2D3C
class: the in-plane single-wave velocity evolves by heat and the perpendicular
component is governed by a linear advection-diffusion equation. It does not
create an uncontrolled generic 3-D self-cascade by itself.

This observation makes the next problem substantially smaller. Instead of
controlling thirty temporal pump pairs built on ten unrelated low children, it
is enough to understand two low purifier channels (six pairs if the three-layer
clocked pulse is retained), plus their **mutual** cross-family interactions.

## 5. What remains

The antisymmetric part `[omega]_x` in (2.5) is a local rigid rotation. It does
not alter the instantaneous energy inequalities proved with `H`, but over a
finite pulse it rotates wavevectors and polarizations. Therefore the next
combined-stage theorem must retain it rather than silently replace `G` by
`H`.

The immediate targets are now:

1. build the two exact high-frequency pump families corresponding to
   (2.8)--(2.9), preferably with the three-layer tail-canceling clock;
2. exploit the exact 2D3C structure of each family to solve its self-dynamics
   rather than treating it perturbatively;
3. enumerate and estimate only the cross interactions between the two
   families and the clean target triple; and
4. test whether one complete pulse gives the same desired/rejected separation
   after including the rotation and all cross-sidebands.

If the two-family cross terms cannot be made lower order by frequency or
spatial separation, that is the next precise obstruction. If they can, the
current abstract router/switch problem reduces to a finite-stage map that is
much closer to direct analysis.

No terminal result is promoted. `NS-R3` remains unresolved.
