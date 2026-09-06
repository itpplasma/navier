## 5. Marked ancient extraction and its exact scope

Work at unit viscosity. Let `u` be the selected smooth mild solution on `[0,T)`, with finite maximal time `T`. Local bounded mild theory implies that

\[
h(t)=\|u(t)\|_\infty
\]

is unbounded as `t` approaches `T`. It is continuous on each compact classical interval. Choose `M_0 > h(0)`, let `M_n=2^n M_0`, and let `t_n` be the first time `h(t_n)=M_n`. Then `t_n` increases to `T` and

\[
h(t)\le M_n\quad(0\le t\le t_n),\qquad
h(t)\le M_n/2\quad(0\le t\le t_{n-1}).
\]

Define the dimensionless record-transition length

\[
\ell_n=M_n^2(t_n-t_{n-1}). \tag{5.1}
\]

This parameter labels two blow-up regimes. No finite bound on it is claimed from arbitrary data, and it is not proposed as another continuation clock.

### Proposition 5.1: a universal lower transition length

The Oseen-kernel bound for the mild bilinear term gives, for a numerical constant `C_K`,

\[
\|u(t_n)\|_\infty
\le\|u(t_{n-1})\|_\infty
 +C_K\sqrt{t_n-t_{n-1}}\,
       \sup_{t_{n-1}\le t\le t_n}\|u(t)\|_\infty^2.
\]

The heat operator is an `L^infinity` contraction. Consequently

\[
M_n/2\le C_K M_n^2\sqrt{t_n-t_{n-1}},
\qquad \ell_n\ge c_0:=(2C_K)^{-2}>0. \tag{5.2}
\]

The local bounded mild theory and its kernel estimates are standard inputs from [KNSS, Section 4].

### Theorem 5.2: two-time marks exclude constant blow-up limits

Suppose `ell_n <= A < infinity` on an infinite subsequence. There is a bounded ancient mild NS solution `U`, smooth through time zero, such that

\[
|U(y,s)|\le1\quad(s\le0),\qquad
|U(0,0)|=1,\qquad
|U(y,s)|\le\tfrac12\quad(s\le-A). \tag{5.3}
\]

In particular it is not constant, and its vorticity is not identically zero on `R^3 x (-A,0)`.

**Proof.** Choose `x_n` with `|u(x_n,t_n)| >= (1-1/n)M_n` and set

\[
U_n(y,s)=M_n^{-1}u(x_n+M_n^{-1}y,t_n+M_n^{-2}s).
\]

For `-M_n^2 t_n < s <= 0`, this is a mild NS solution with `|U_n| <= 1`. Its left endpoint tends to minus infinity. If `s <= -A`, the corresponding physical time is no later than `t_{n-1}`, because `ell_n <= A`; whenever that physical time is nonnegative, `|U_n| <= 1/2` there.

To retain the mark at `s=0`, rather than merely convergence for `s<0`, restart the bounded mild solution with datum `U_n(0)`. The datum has norm at most `1`, so the bounded local theory provides an extension to a common positive time `delta`, uniformly bounded by `2`. This extension agrees with the prior branch on its overlap by mild uniqueness. Applying bounded mild compactness [KNSS, Lemma 6.1], after shifting the common right endpoint if necessary, gives a locally uniformly convergent subsequence on an open time neighborhood of `(-infinity,0]`.

The limit is mild, inherits the two global bounds pointwise at every fixed `(y,s)`, and has `|U(0,0)|=1`. If its vorticity vanished throughout the slab `(-A,0)`, divergence freedom and the vector identity `Delta U = grad div U - curl curl U` would make each component bounded and harmonic in all of `R^3`. It would therefore be spatially constant. The mild equation then makes that spatial constant independent of time: the heat flow preserves constants and the nonlinear divergence vanishes. Continuity at the two ends of the slab contradicts the half-to-one marks. This also excludes accelerating spatial constants, which solve a differently normalized pressure problem but are not bounded ancient mild solutions of this form. QED.

The new retained datum relative to the repository's old extraction is the earlier half-amplitude mark. The underlying compactness is the standard KNSS theorem. The assertion does **not** inherit finite global energy, a finite `L^3` norm, spatial decay, a zero final trace, or an a priori Type-I bound.

### Proposition 5.3: a uniformly localized rotational witness

For each fixed `A`, there are `R_A < infinity` and `eta_A > 0` such that every ancient mild solution satisfying (5.3) obeys

\[
\int_{-A}^0\int_{B_{R_A}}|\nabla\times U|^2\,dy\,ds\ge\eta_A. \tag{5.4}
\]

**Proof.** If the marked class is empty the assertion is vacuous. Otherwise suppose no such pair exists. Choose marked solutions `U_j` for which the integral on `B_j x (-A,0)` is less than `1/j`. Uniform bounded mild compactness, using the same extension through zero, gives a limit retaining all of (5.3). On every fixed ball the curls tend to zero in `L^2` on the slab; distributional convergence from local uniform velocity convergence then implies zero curl for the limit on the entire slab. The last paragraph of Theorem 5.2 gives a contradiction. QED.

This is a qualitative localization statement. Its constants depend on `A`, not on the original solution. No numerical values or novelty claim are asserted.

### Proposition 5.4: the exhaustive slow-record alternative

Either the sequence `ell_n` has a bounded subsequence, or `ell_n` tends to infinity. In the latter case the running maximum

\[
H(t)=\sup_{0\le s\le t}h(s)
\]

satisfies

\[
(T-t)H(t)^2\longrightarrow\infty. \tag{5.5}
\]

Indeed, if `t_n <= t < t_{n+1}`, then `H(t) >= M_n` and `T-t >= t_{n+2}-t_{n+1}`. Hence

\[
(T-t)H(t)^2\ge\ell_{n+2}/16.
\]

The assertion is about the **running maximum**, not automatically the instantaneous `h(t)`. Having a bounded subsequence of transition lengths does not imply a global Type-I bound; intermittent slow transitions can coexist with fast ones. The two cases are a dichotomy about `ell_n`, not a claimed disjoint classification of all named Type-I/Type-II solution classes.

### 5.5 Why the two attempted terminal closures fail

**Maximum-principle attempt.** The scalar speed equation contains signed pressure work, while the vorticity equation contains stretching. Neither supplies the proposed no-amplification theorem. That theorem has not been proved here. Calling it a Liouville principle is not a proof.

**Energy-summation attempt.** At the normalization used above,

\[
\iint |\nabla\times U_n|^2\,dy\,ds
 = M_n\iint |\omega|^2\,dx\,dt. \tag{5.6}
\]

Thus a fixed positive normalized rotational cost scales back to a physical cost of order `1/M_n`, not order one. Lower semicontinuity gives such a positive lower cost for the prelimit sequence once the limit has (5.4), but those dyadic costs are summable. Even disjointness would not give a contradiction. At viscosity `nu`, length is `nu/M_n`, time is `nu/M_n^2`, and the viscous-energy cost is of order `nu^3/M_n`; the same summability remains.

After these two failures, no more scalar-energy refinement of the marked-ancient family is authorized by this run. Section 6 separately falsifies the attempt to use the available energy/enstrophy budgets to eliminate (5.5).
