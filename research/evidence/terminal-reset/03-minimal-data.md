## 4. A compact minimizing set is not a compact evolving orbit

### Proposition 4.1: the direction of the inequality

Assume finite-time-singularity-generating data in a critical mild-solution space exist, and let `rho` be the infimum of their initial norms. If a minimizing datum `u_0` produces a singular solution, every later regular slice `u(t)` also generates a finite-time singularity, by time translation and local uniqueness. Therefore

\[
\|u(t)\|_{\dot H^{1/2}}\ge\rho, \tag{4.1}
\]

not `<= rho`. In particular, compactness of the set of data with norm exactly `rho` does not apply to an arbitrary time slice of the minimizing trajectory.

This distinguishes the initial-data compactness theorem in [RS] from a forward-orbit compactness theorem. It does not contradict [RS].

### Proposition 4.2: exact smooth dynamical counterexample

On `R^2` consider the polynomial vector field

\[
\dot y=1+y^2-(z-1)^2y^3,\qquad \dot z=0. \tag{4.2}
\]

If `z != 1`, write `c=(z-1)^2>0`. For sufficiently large `R`, containing the initial `y`, the vector field points strictly inward at both ends of `[-R,R]`: it is negative at `R` and positive at `-R`. The solution stays in that interval and hence exists globally forward in time.

If `z=1`, then

\[
y(t)=\tan\bigl(t+\arctan y(0)\bigr),
\]

which blows up at a finite positive time. Thus the singularity-generating initial set is exactly the line `z=1`. Its minimum Euclidean norm is `1`, attained at the unique point `(0,1)`. Every datum of norm less than `1` is global, and the minimizing set is a compact singleton.

Nevertheless, the orbit of this minimizer is `(tan t,1)`, of norm `sec t`, unbounded as `t` tends to `pi/2`.

This refutes the *generic dynamical inference* from small-data regularity, an attained minimal singular norm, and compactness of minimizers to a bounded/precompact forward orbit. It is not an NS counterexample, nor does it rule out a new NS-specific theorem proving orbit compactness by some other mechanism.
