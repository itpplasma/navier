# Follow-through: the locally born daughter is not yet a repeatable phase configuration

Date: 2026-09-10. Author derivation, independent audit pending.
This supplements `2026-09-10-source-prehistory-regeneration.md` at
`itpplasma/navier@a6e287434bb10dbe638fb7f48e3871ab8ddb8d2f`.
It preserves that note's positive local seeding result and adds a missing
kinematic test before interpreting it as a recursive cascade.
No original-NS prehistory, endpoint estimate, or blow-up is constructed.

## 1. Follow the phases after birth, not only their instantaneous sum

Use the same unrounded source normals in the orthonormal (radial,N,K_tan)
frame, with N=g/|g| and K_tan perpendicular to g. At the proposed birth
instant take the two source clocks

    a=L/2+cL/u,     b=L/2-cL/u.

Advance both clocks by a common fast-time v while retaining the same
frozen representative and phase laws. Then

    n_+(v)=B_s(u/2+u(v+a)/L, -u/(L|g|), 1),
    n_-(v)=B_s(-u/2-u(v+b)/L, u/(L|g|), 1).

Consequently their sum and difference are EXACTLY

    n_d(v)=n_+(v)+n_-(v)=2B_s(c,0,1),
    n_s(v)=n_+(v)-n_-(v)=2B_s(u(1+v/L),-u/(L|g|),0).   (1)

The daughter phase has no radial winding in this prescribed background:
its tangential component is perpendicular to the shear g. Its tilt stays
c. The difference sideband does wind. These statements concern the source
phase laws under their specified frozen continuation, not the eikonal of
an as-yet unconstructed full nonlinear solution.

**Midpoint clarification.** Formula (3.2a) of the preceding note is the
value at its birth/midpoint configuration. For a general common unshifted
source clock w its radial difference is B_s(u+2uw/L), not the constant
2B_s u. Equation (1) supplies the time-dependent version explicitly.
The finite-L sideband/non-mean distinction in that note is unchanged.

If only the angular carrier is rounded, the tangential sum differs from
2B_s K_tan by O(1/k). Its radial slope is therefore O(1/k). On every fixed
polynomial-in-L time interval its tilt change is o(1) when k grows faster
than every such polynomial, as on the source's small-epsilon scales.
Rounding alone does not turn a small-tilt daughter into an order-one-tilt
parent under the same frozen phase law.

Thus the child is NOT automatically a fresh copy of either parent pulse.
A repeatable mechanism needs changed shear, additional interacting modes,
or another geometric arrangement. The generated shear may participate in
that change, so this is not a no-go for a coupled mechanism. Treating it as
an ignorable error would discard a possible part of the required mechanism.

## 2. Tangential frequency doubling is not total-frequency doubling

With b_eff=k B_s, the birth configuration has

    |xi_d|^2=4 b_eff^2(1+c^2),
    |xi_+|^2=b_eff^2[1+(u+c)^2],
    |xi_-|^2=b_eff^2[1+(u-c)^2].                        (2)

Both parents have larger total wavenumber than the daughter exactly when

    u^2-3-3c^2-2u|c|>0.                                (3)

For the robust near-peak choice c=L^(-3/4), fixed u>=2, this holds for all
sufficiently large L. The sum doubles the K_tan component but cancels most
of the parents' radial frequency. This helps explain why the newborn can
have a positive frozen linear growth rate despite viscosity. It is not yet
a forward cascade in total wavenumber or a proof of a growing physical
scale parameter. The strongly generated difference sideband instead has
large predominantly radial wavenumber and cannot be deleted from the flow.

The reference values u=2,c=1/4 used in some coefficient calibrations need
not satisfy (3): that numerical example proves a nonzero growing-coordinate
source, not that BOTH parents have larger wavenumber. The phase conclusion
(1) applies regardless. At u=2,c=1/8, the smaller squared-norm gap in (2)
is exactly 29/64 times b_eff^2, providing a rational calibration of (3).

## 3. Where the weak-overlap possibility now stands

The preceding note's weak-overlap size calculation survives: an exponentially
small overlap can produce a tiny daughter seed and a tiny sideband. But
it does not supply an indefinitely repeatable geometry. Following the
newborn requires the whole linear response about the existing wave-bearing
background, because its interactions with those waves are first order in
the newborn's small amplitude. As it grows, nonlinear feedback and changes
to the phase gradients have to be retained as well.

No contraction, sign-definite regeneration, finite-time amplification chain,
or common Schwartz initialization is inferred. The next genuine positive
result would have to produce a complete coupled phase/amplitude turnover,
not just another favorable coefficient at the birth instant.

## 4. Reproducible validation

The following Python/SymPy calculation was executed and passed six exact
assertions. They check prescribed phase identities and wavenumber algebra,
not the full NS evolution. The initial check implementation needed algebraic
simplification of a structurally different but equal expression; the final
checks below use exact simplification.

```python
#!/usr/bin/env python3
"""Six exact frozen-phase checks; not an unforced NS construction."""
import sympy as s

v, L, B, u, c, g = s.symbols('v L B u c g', positive=True)
a = L / 2 + c * L / u
b = L / 2 - c * L / u
plus = B * s.Matrix([u / 2 + u * (v + a) / L, -u / (L * g), 1])
minus = B * s.Matrix([-u / 2 - u * (v + b) / L, u / (L * g), 1])
D = (plus + minus).applyfunc(s.simplify)
S = (plus - minus).applyfunc(s.simplify)
assert (D - B * s.Matrix([2 * c, 0, 2])).applyfunc(s.simplify) == s.zeros(3, 1)
assert D.diff(v) == s.zeros(3, 1)
assert (S - B * s.Matrix([2 * u * (1 + v / L), -2 * u / (L * g), 0])).applyfunc(s.simplify) == s.zeros(3, 1)
xd = s.Matrix([2 * c, 0, 2])
p = s.Matrix([u + c, 0, 1])
q = s.Matrix([-u + c, 0, 1])
assert s.expand(p.dot(p) - xd.dot(xd)) == u * u + 2 * u * c - 3 * c * c - 3
assert s.expand(q.dot(q) - xd.dot(xd)) == u * u - 2 * u * c - 3 * c * c - 3
assert (u * u - 2 * u * c - 3 * c * c - 3).subs({u: 2, c: s.Rational(1, 8)}) == s.Rational(29, 64)
print('PASS: six exact phase-closure / wavenumber assertions.')
print('Sum normal:', D.T)
print('Difference normal:', S.T)
print('Scope: prescribed frozen source phases, not a nonlinear NS history.')
```

The source phase formula was inspected in OpenAI, *Finite Time Blowup for
Navier--Stokes*, (7.2)--(7.5), in the same source inspection as the parent
packet. All equations in this supplement are derived from that local phase
formula and the explicitly specified clock shift; none asserts that the
original disjoint source pulses already overlap physically.
https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf

Repository-wide checks, manuscript compilation, independent audit, and Lean
were not run. This additive supplement changes no canonical/formal status.
