## 2. Work backward from the terminal theorem

### 2.1 The exact missing implication

For viscosity `nu > 0` and a finite horizon `H > 0`, put

\[
v(y,s)=\sqrt{H/\nu}\,u(\sqrt{\nu H}\,y,Hs),\qquad
q(y,s)=(H/\nu)p(\sqrt{\nu H}\,y,Hs).
\]

Then

\[
v_s+v\cdot\nabla v+\nabla q=\Delta v,\qquad \nabla\cdot v=0,
\qquad \|v(s)\|_3=\nu^{-1}\|u(Hs)\|_3.
\]

In the current dependency graph the missing implication is therefore, in unit-viscosity, unit-horizon form,

\[
\boxed{\quad
v_0\in\mathcal S(\mathbb R^3)^3,\ \nabla\cdot v_0=0
\quad\Longrightarrow\quad
\sup_{0\le s<\min(1,S_*)}\|v(s)\|_3\le F(v_0)<\infty .
\quad} \tag{2.1}
\]

Here `v` is the selected maximal classical/mild branch, not an arbitrary weak solution. The finite bound must be established from the datum; naming the unknown supremum `F` is not a proof. The datum may be used in full: the project does not restrict `F` to kinetic energy alone.

The existing continuation suffix then rules out a finite maximal time. At these quantifiers (2.1) is itself equivalent to the terminal continuation assertion. The graph's `EXISTENTIAL` node already establishes the analogous fact for the high-pressure condition. There is no smaller proved producer hidden in that reformulation.

### 2.2 Common obstruction, with the scale retained

For a fixed nonzero test profile on a unit parabolic cylinder, form

\[
w_r(x,t)=r^{-1}W(x/r,t/r^2).
\]

Changes of variables give

\[
\|w_r(t)\|_2^2\sim r,\qquad
\iint |\nabla w_r|^2\sim r,
\qquad
\|w_r(t)\|_3\sim 1,
\qquad
\int\|\nabla w_r(t)\|_2^4\,dt\sim 1. \tag{2.2}
\]

Thus energy-scale costs of successive shrinking packets can be summable while critical costs are not. This calculation is a scaling test, not construction of an NS cascade. It shows exactly why another estimate using only these budgets cannot provide the required conclusion without genuinely new dynamical information.

The history repeatedly meets this obstruction. HF26's temporal uniformity was audited as equivalent to continuation. HF27's successful comparison certificate was likewise equivalent at its existential quantifiers. HF28 fixed the comparison canonically, removing the unknown solution from its definition, but a successful truncation index was again equivalent to continuation. The subsequent defect/form/shell/material laws keep replacing the uncontrolled critical integral by another quantity whose only proved upper bound returns to that integral. Local differentiability, a cancellation, and fixed-regularization control do not establish endpoint-uniform bounds. These diagnoses are recorded in `PLAN.md`, rather than inferred merely from the number of manuscript pages.

The stop rule is therefore mathematical: do not revive this producer family through a local refinement unless an independent input-only estimate is supplied at the start. Retain `LOCAL`, `ENERGY`, `SCALE`, and the continuation suffix as tools, not as evidence that a producer has been found.
