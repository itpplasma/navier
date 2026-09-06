# Dissipation-clock continuation: component derivations and producer boundary

Date: 2026-09-06. Status: complete written component derivations, author
checks only, independent mathematical audit pending. This evidence is not a
new task ledger; `PLAN.md` owns live status. No terminal or gap is promoted.

## Frozen inputs and source

The initial research main inspected was `fed387e50bf43016c1c6f7993376ad7ca4552c9d`.
The initial paper main was `dbd44acbf703539bb4bc9a05bc2ecd792d506c24`.
The component source is `itpplasma/navier-paper`,
`sections/dissipation_clock.tex`, introduced at
`7748a9816d0fd9003205684761c219a0b57d9c14`; its Git blob is
`5b0bdebc76af571d4df2b7181538a9da25d1083b`.
The standalone driver is `dissipation_clock.tex`; it includes the same section
as the main manuscript, so the proof is not duplicated. The source is explicit
about imported local theory, energy and cubic-balance inputs.

This task explicitly authorizes edits and unsigned commits in both private
repositories. It supersedes the earlier read-only/signed-only direction for
this task without pausing ongoing formalization or weakening mathematical
review requirements. No work in `navier-formal` is committed by this task.

## 1. The better exponent pair closes the dissipation-to-continuation suffix

Write `Y=||grad u||_2^2`, `Z=||Delta u||_2^2`, `X=||u||_3^3`,
`B(t)=integral_0^t D3`, and let `S` be the homogeneous H1-to-L6 constant.
The full source proves

```text
||u||_9^3 <= (9 S^2/8) D3,
Y' + nu Z <= (32 S/(27 nu^2)) ||u||_9^3 Y
          <= (4 S^3/(3 nu^2)) D3 Y,
Y(t) + nu integral_0^t Z <= Y0 exp(4 S^3 B(t)/(3 nu^2)).
```

The exact spatial Holder triple is `(9,18/7,2)`. The gradient interpolation
weights are `2/3,1/3`; the sharp scalar Young remainder is
`32 a^3/(27 nu^2)` for `2 a z^(2/3) - nu z`. The constant product is
`(32/27)(9/8)=4/3`. The weak chain rule across `u=0`, the tensor Sobolev
bound and Fourier Hessian identity are all stated explicitly. The proof
uses only the local package and energy at the continuation step. It covers
`Tstar=H` and the zero datum without dividing by enstrophy.

This uses the nonendpoint Serrin pair `(time,space)=(3,9)` directly. The
previous dissipation-budget supplement used `(4,6)`, and therefore carried
an unnecessary factor from a critical-norm bound. Under the SAME strict
pressure hypothesis, with `R=X0+3A`, the new exponent is

```text
4 S^3 R / (9 (1-theta) nu^3).
```

The old displayed exponent was
`81 S^4 R^(4/3)/(128 (1-theta) nu^4)`. These constants are not asserted to
be optimally ordered for every numerical value of the data; the structural
improvement is a dissipation-only suffix and a linear dependence on `R`
instead of a `R^(4/3)` dependence. There is no new critical smallness.

After an independent audit, the strict-pressure route can use this direct
suffix instead of ESS, Leray-Hopf endpoint membership and backward
uniqueness. The standalone theorem that a bare uniform L3 bound forces
continuation still retains its endpoint input. Do not remove ESS from that
separate statement. The main graph is not yet promoted on the strength of
these author checks.

## 2. A single finite barrier, rather than a fixed absorption fraction

The source proves the following first-crossing certificate. Fix the horizon
and cutoff, and let `L_J(H)` bound the absolute accumulated low pressure.
Choose finite `b>0` and `epsilon>0` BEFORE the running time. If the first
crossing `B(tau_b)=b`, whenever it occurs below `min(H,Tstar)`, obeys

```text
integral_0^tau_b Q_J <= nu b - X0/3 - L_J(H) - epsilon,
```

then the cubic balance would give `X(tau_b)/3 <= -epsilon`. Therefore the
crossing cannot occur, `B<b`, and the direct enstrophy bound continues the
branch past the horizon. No estimate at an unconstructed endpoint is used.

A useful sufficient template is

```text
integral_0^t Q_J <= nu B(t) - Phi(B(t)) + A_high.
```

One only needs a SINGLE finite `b` with
`Phi(b)>X0/3+A_high+L_J(H)`. Monotonicity, continuity and coercivity of Phi
are not necessary for that first-crossing argument. An increasing logarithm
is a particularly transparent special case:

```text
Phi(B)=eta nu b0 log(1+B/b0),
B <= b0 [exp((X0/3+A_high+L_J(H))/(eta nu b0))-1].
```

Here `Phi(B)/B -> 0`: a constant positive fractional dissipation margin is
not necessary in this sufficient-condition framework. No arbitrary-data
pressure estimate with this deficit is proved. Introducing Phi is not an
estimate of the term that contains it.

The scalar example in the source shows precisely why a bounded deficit below
the available budget cannot bound B through the cubic balance alone. It is
not a velocity field, a PDE trajectory, or a counterexample to regularity.
At existential quantifiers the new barrier is again equivalent to
continuation; choosing `b>B(H)` after assuming a regular branch proves only
the converse. This is explicitly not advertised as a logically weaker
arbitrary-data problem.

## 3. Producer attempt: where absolute pressure estimates stop

The next natural attempt was reconstructed rather than silently assumed.
Let `A_rad=integral |u| |grad|u||^2 <= D3/2`, and let `C_R` bound the
pressure map from `u tensor u in L3` to `p in L3`. Holder, interpolation and
the weighted Sobolev bound give

```text
|P3| <= ||p||_3 || |u| grad|u| ||_(3/2)
     <= C_R ||u||_6^2 ||u||_3^(1/2) A_rad^(1/2)
     <= C_p ||u||_3 D3,     C_p = 3 S C_R/4.
```

Consequently the cubic balance gives, by a zero-safe regularization,

```text
X(t)^(2/3) <= X0^(2/3) + 2 C_p B(t).
```

Integrating the absolute pressure bound in the B clock then yields only

```text
integral_0^t P3 <= [(X0^(2/3)+2 C_p B(t))^(3/2)-X0]/3.
```

The available upper bound grows like `B^(3/2)`, not like
`nu B - Phi(B)` with a useful deficit. It therefore does not establish the
barrier for arbitrary data. This is a diagnosis of this absolute-norm
attempt, NOT a proof that signed trajectory cancellations are impossible.
The missing producer must use more information from the vector equation
than this chain of absolute estimates retains.

## 4. Audit questions and verification boundaries

An independent reviewer should reconstruct the tensor Sobolev step, all
Young constants, integrating-factor direction, endpoint `Tstar=H`, zero-set
chain rule, retained strict dissipation, first-crossing quantifiers,
logarithmic inversion and scalar counterexample. In particular, check that
no supremum of an unknown solution has been used to choose a sufficient
witness. The deliberately stated converse must not be mistaken for a
producer.

Local checks performed on the frozen section: `latexmk -pdf` for the
standalone driver, four rendered pages inspected, no LaTeX warnings or
overfull boxes, and `tools/check_dissipation_clock.py` (paper repository).
The latter checks exact rational exponent identities, 200 deterministic
Young samples including equality, logarithmic inversions, the scalar
boundary and 18 unique/resolved component labels. These are arithmetic and
source checks, not PDE verification, an independent audit, or a Lean build.

Narrow private GitHub workflows apply anchor-checked, idempotent edits to
main documents after refreshing main; run builds/structural checks; and
push only explicit source paths without force. The research-only verifier
mode explicitly excludes external manuscript/formal checks; its output
must not be described as a full cross-repository verification. Full default
verification still requires the manuscript and formal manifest.

The continuation mechanism is elementary nonendpoint enstrophy testing,
not a newly imported endpoint theorem. Tao's primary record arXiv:1108.1165
was checked on 2026-09-06; the LOCAL package remains a project-owned proof
using his published local theory. No novelty or priority claim is made.
