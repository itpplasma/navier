# Averaging obstruction to RF-q and the averaging gate

Date: 2026-09-08. Author proof by the owner's Claude session, recorded at
the owner's request after the controller stopped. Base
`141122011ef9383a12b622335f8b1af01f666a60`. Not independently audited.
Not a terminal result. No canonical proof-graph node is changed.

## Statement

Let B be the whole-space Navier--Stokes bilinear operator with Leray
projection, and let Bt be an averaged Euler bilinear operator in the sense
of Tao, Theorem 1.5: an average of B over rotations and order-zero Fourier
multipliers that preserves divergence-free fields and the cancellation
<Bt(u,u),u>=0. Fix N0>0, N_j=2^j N0, orthogonal Fourier ball projections
P_N, and define for the averaged equation

    u_N,t = nu Delta u_N + P_N Bt(u_N,u_N),   u_N(0)=P_N d,

the increments e_j=u_(N_(j+1))-u_(N_j) and a_j(t)=N_j^(1/2)||e_j(t)||2,
exactly as in PLAN for the original equation.

LEMMA (averaging obstruction). There exist a real solenoidal Schwartz datum
d, a viscosity nu>0 and a finite horizon H such that, for every finite q>3,

    sup_(0<=t<=H) sup_M sum_(j<M) a_j(t)^q = infinity.

That is, RF-q, and a fortiori RF-CUBE and RF-SUM, are false for the
averaged equation with its own projected family.

COROLLARY (averaging gate). Any proof of RF-q for the original equation
must contain at least one step that is false when B is replaced by Bt.
No estimate whose proof uses only the following ingredients can be that
step: the energy identity, orthogonality of ball projections, the
Fourier-support trichotomy, Bernstein and sharp shell estimates, the
Hilbert-space ODE construction, layer-cake synthesis, H3 residual and
energy comparison on compact classical lifespans, Fatou, and every signed
or unsigned shell budget of the form int Pi_M <= nu int D_M + C(inputs).

## Proof of the lemma

Tao's Theorem 1.5 supplies Bt and a Schwartz divergence-free datum u0 whose
mild H10 solution of the averaged equation has no global continuation; the
solution is smooth on [0,T*) and blows up at a finite T*. Tao's footnote
11 states the blowup type verbatim:

> This would not be in contradiction to Theorem 1.5, as the blowup solution
> constructed in the proof of that theorem is of "Type II" in the sense that
> critical norms of the solution u(t) diverge in the limit t -> T*. In
> contrast, the results in [16] rules out "Type I" blowup, in which a certain
> critical norm stays bounded.

Here [16] is Escauriaza, Seregin and Sverak. Take d=u0, the viscosity
implicit in (1.9), and any H>T*. Suppose RF-q held for the averaged
projected family on [0,H] with some finite constant K. Run the reviewed
consumer chain of this repository on the averaged equation:

1. Construction. `2026-09-07-whole-space-cubic-refinement.md` proves global
   existence of each u_N in the bandlimited solenoidal L2 space by a
   Hilbert-space ODE contraction plus exact energy. Both use only the
   bilinear L2 bound on the projected operator and the cancellation
   <Bt(u,u),u>=0, which Tao's (1.16) provides.
2. Synthesis. `2026-09-07-lorentz-synthesis.md` bounds the L3 norm of the
   overlapping ball-supported increment sum by the finite-q sum of the
   a_j through sharp L2 shell estimates and layer-cake. This is a statement
   about the fields e_j, not about the operator, and transfers unchanged.
3. Identification. On every compact subinterval of [0,T*), the H3 residual
   and energy comparison identify u_N with the classical branch in C_t L2.
   The residual bound uses the bilinear estimate for the projected operator
   and the Fourier-support bookkeeping of (I-P_N)Bt(v,v); rotations and
   order-zero multipliers preserve |xi|, so the support bookkeeping is the
   same as for B.
4. Fatou. Strong L2 convergence on compact subintervals and lower
   semicontinuity of the L3 norm give sup_(t<T*) ||u(t)||3 <= K.

Step 4 contradicts Type II divergence of the critical L3 norm at T*.
Hence RF-q fails for the averaged family. QED.

The only Navier--Stokes-specific input in the reviewed consumer chain is
the final continuation step in `2026-09-07-lorentz-continuation.md`, which
applies Phuc's Lorentz-space theorem, that is, the Escauriaza--Seregin--
Sverak mechanism. It is not used above. Frozen consumer inputs inspected:

- `2026-09-07-whole-space-cubic-refinement.md`, SHA256
  `5e985a4587264d20650a6038132e0dd415ef223c3f2409f027f7b1a02481b31b`.
- `2026-09-07-lorentz-synthesis.md`, SHA256
  `ba075437818bbe5b1ae59e5bbc87bf52889e6455dab5a78b469d01bec809eb38`.
- `2026-09-07-lorentz-continuation.md`, SHA256
  `33be1a9aa36405fb9572b22d552cbb2e7bb1ded95427843cb58948d1fd90df36`.

Source: T. Tao, *Finite time blowup for an averaged three-dimensional
Navier--Stokes equation*, J. Amer. Math. Soc. 29 (2016), 601--674,
[arXiv:1402.0290](https://arxiv.org/abs/1402.0290). Inspected: abstract,
Theorem 1.5, cancellation (1.16), footnote 11. The averaging in the arXiv
abstract is over rotations and order-zero multipliers; the exact averaging
class does not affect the proof, which uses only cancellation, the mapping
properties of Bt, Fourier-support preservation, and Type II blowup.

## Proof of the corollary

Each listed ingredient holds verbatim for Bt: the energy identity by (1.16),
the projection and support facts because rotations and order-zero
multipliers commute with the radial support bookkeeping, and the rest are
statements about fields. A proof of RF-q for B using only these ingredients
would prove RF-q for Bt, contradicting the lemma. QED.

## Consequences for the live allocation

- The positive transfer estimate recorded in PLAN,
  int_0^H ||P_K G||2 <= C K^(5/2) N^(-2) ||d||2^2/nu, is Bernstein plus
  energy and holds for Bt. It cannot be the decisive step.
- The paired-history, single-flow cubic, smooth-block, three-level,
  signed-phase and large-q lanes of 2026-09-07 and 2026-09-08 all work
  inside the averaging-invariant class. Their audited lemmas are correct;
  their target is false in the class where their proofs live. This is the
  exact reason every lane returned to the squared-enstrophy clock.
- Structures not preserved by averaging, hence not excluded: the local
  energy inequality and epsilon-regularity, Lagrangian transport and Cauchy
  invariants, the exact Riesz-transform pressure and its Hessian, backward
  uniqueness and Carleman inequalities, vorticity-direction geometry.
  The 2026-09-08 record-pressure lemma lives in the third item.

## Recorded failed positive attempt

A Galilean-quotiented concentration-scale extraction for Type II blowup was
attempted. Define rho(t) as the largest radius at which the local L3
oscillation ||u(t)-mean||_(L3(B(x,r))) stays below a fixed epsilon on every
ball, select times at which the running minimum of rho is attained, and
rescale by rho. Epsilon-regularity in the moving frame gives locally uniform
smoothness, and the limit is an ancient solution with uniformly small local
L3 oscillation on (-infinity,0] and oscillation exactly epsilon at time
zero. Spatially constant trivial solutions are removed by the quotient.

First invalid bridge: rigidity. Affine flows U=Sx with traceless S and
pressure -(1/2) x.S^2 x are exact eternal solutions with unit-ball
oscillation of size epsilon, and shear flows built from ancient heat
polynomials give a polynomial hierarchy of the same kind. Every
derivative-based normalization admits the next polynomial degree as a
limit, and the finite energy of the original flow does not survive the
rescaling. The extraction is sound; the class it lands in has no Liouville
theorem. Do not repeat this attempt without a new rigidity input.

## Non-claims

- No statement about the original equation's regularity or about RF-q for
  B is made. The lemma is about Bt.
- No claim that critical control of the original equation is impossible;
  only that its proof must use a Bt-breaking step.
- The exact averaging class of Tao's final Bt was not re-derived here.
- Independent audit is pending. Audit scopes: (i) that steps 1--3 of the
  consumer chain indeed use no Bt-breaking property, by reading the three
  frozen files; (ii) the reading of Tao's footnote 11 and Theorem 1.5.
