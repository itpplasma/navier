# Supercritical localized turnover: exact target, energy window, and the fixed-volume wall

Date: 2026-09-11. Repository input before this packet:
`itpplasma/navier@a4189880461d3e23d1842931ea9f2adbf872bd50`.

**Status: author proof / exact scaling reduction. Independent mathematical audit
and novelty are undetermined. No unforced singular solution is constructed.**
This note does not promote NS-R3, the canonical proof graph, the manuscript,
or formal status. Its purpose is to replace the vague phrase "regenerative
turnover" by a quantitative terminal contract and to identify a scope in
which the current periodic/source-reference calculations cannot possibly
close that contract.

The previous source-specific packets established actual local ingredients:
cheap pulse entry seeds, a source-derived nonlinear daughter, generated shear,
doubled-parent wavevectors, and a full linear shear response that can populate
those directions with radial velocity. The latest packet also established the
remaining failure under the old background: an isolated doubled copy has four
times the viscous damping and negative net rate. The question here is therefore
not whether another Fourier carrier can be born. It is what one complete
physical turnover must accomplish to imply a classical unforced singularity.

## 1. Definition of the terminal turnover chain

Fix viscosity `nu>0`. Let `u` be one exact classical unforced solution on
R3 issued from one nonzero solenoidal Schwartz datum. A **localized turnover
chain** with scale contraction `s>1` and amplitude gain `g>1` consists of
numbers

    ell_n = ell_0 s^(-n),       A_n = A_0 g^n,

observation times `t_n`, centers `x_n`, and fixed positive constants
`c_2,c_3,C_t` independent of n such that

    ||u(t_n)||_{L3(B(x_n,C ell_n))} >= c_3 A_n ell_n,       (1.1)
    ||u(t_n)||_{L2(B(x_n,C ell_n))}^2 >= c_2 A_n^2 ell_n^3, (1.2)
    0 < t_(n+1)-t_n <= C_t ell_n/A_n.                       (1.3)

Here `C` is another fixed profile-class constant. Condition (1.2) is a
nondegeneracy assumption on the regenerated cell; it prevents the symbol
`A_n` from being an arbitrarily large point value carried by vanishingly
small mass. A concrete turnover lemma may replace balls by scale-adapted
weights or packets, but it must imply fixed-constant analogues of (1.1)--(1.3).

The word "chain" also includes the construction obligation suppressed by
these inequalities: the complete output state at stage n must lie in the
admissible input class for stage n+1. No old parent, generated sideband,
pressure tail, exterior field, or viscous contribution may be reset or
deleted between stages. That closure condition is not proved in this note.

### Theorem 1: a supercritical chain is already a terminal negative consumer

If

    g > s,                                                     (1.4)

and one exact classical solution from one Schwartz datum satisfies
(1.1)--(1.3) for every n, then the observation times accumulate at a finite
`T<infinity`, the global `L3` norm diverges along `t_n -> T`, and the
classical solution cannot extend smoothly through T. Hence such a chain,
with the ordinary canonical pressure inherited from the exact equation,
would be an unforced finite-time breakdown construction.

Proof. Equation (1.3) gives

    t_n-t_0 <= (C_t ell_0/A_0)
                 sum_(j=0)^(n-1) (s g)^(-j),

so the times have a finite upper limit because `sg>1`. Equation (1.1) gives

    ||u(t_n)||_3 >= c_3 A_0 ell_0 (g/s)^n -> infinity

by (1.4). If the classical solution extended through the limiting time,
its smooth finite-energy branch would have finite continuous `L3` norm on
a compact interval containing T, a contradiction. QED.

This implication is deliberately elementary. It is useful because it fixes
the exact quantity the turnover must amplify. The repository's reviewed
continuation suffix uses the same critical `L3` boundary. No new literature
criterion is imported here.

## 2. Energy forces a narrow but nonempty gain window

The ordinary energy identity supplies a necessary condition on every
nondegenerate scale-repeating chain. From (1.2),

    ||u(t_n)||_2^2 >= c_2 A_0^2 ell_0^3
                       (g^2/s^3)^n.                        (2.1)

The total kinetic energy is bounded by its initial value. Therefore a chain
with fixed `c_2>0` requires

    g^2 <= s^3,       equivalently g <= s^(3/2).            (2.2)

Combining the terminal condition (1.4) and the energy condition gives

    boxed:        s < g <= s^(3/2).                         (2.3)

The interval is nonempty for every `s>1`. A strict upper inequality makes
the core kinetic energy tend to zero while its critical norm grows. Thus
finite energy does not by itself obstruct the required concentration.

For a factor-two spatial scale contraction,

    boxed:        2 < g <= 2 sqrt(2).                       (2.4)

A convenient rational interior target is

    s=2,       g=5/2.                                      (2.5)

For this target the generation ratios are exactly

    critical L3:                g/s       = 5/4,
    core kinetic energy:         g^2/s^3   = 25/32,
    turnover duration:           1/(sg)    = 1/5,
    fixed-shape dissipation cost: g/s^2     = 5/8,
    local Reynolds number:       g/s       = 5/4,
    relative viscous action:     s/g       = 4/5.           (2.6)

The last three entries are scaling diagnostics. If a uniform profile-class
estimate gives

    integral_(t_n)^(t_(n+1)) ||grad u||_2^2 dt
       <= C_D A_n ell_n^2,                                  (2.7)

then its contributions form a geometric series with ratio `g/s^2`; (2.3)
with `s>1` implies `g<s^2`, so this cost is summable. The dimensionless
viscous action over a turnover is

    nu (t_(n+1)-t_n)/ell_n^2
       <= C_t nu/(A_n ell_n),                               (2.8)

whose stage ratio is `s/g<1`. Equivalently the local Reynolds number
`A_n ell_n/nu` grows by `g/s>1`. Once an exact supercritical turnover exists,
ordinary viscosity becomes relatively weaker down the chain rather than
stronger. This statement does **not** construct the first turnover or prove
(2.7).

At the canonical point (2.5), the normalized total turnover time is `5/4`
and the normalized sum of the scale-model dissipation contributions is
`8/3`. The companion checker verifies these identities through many finite
prefixes using exact rational arithmetic.

## 3. Why the critical copy g=s is insufficient

A geometrically exact scale copy with amplitude proportional to inverse
length has `g=s`. Its core critical norm is then scale invariant:

    A_(n+1) ell_(n+1) / (A_n ell_n) = 1.                   (3.1)

Such a cell may transfer energy to arbitrarily high frequency, but (1.1)
does not force the global critical norm to diverge. The already proved
`2026-09-08-full-duration-mixing-cascade.md` is an exact warning of this
kind: original unforced R3 solutions can undergo arbitrarily many prescribed
finite spectral transfers and large critical-Sobolev growth while their
finite Lorentz critical norm changes arbitrarily little. Spectral transfer
is therefore not the missing terminal property.

The turnover sought here must be **slightly supercritical**: `g>s`. This is
why a scale-neutral or exactly self-similar Fourier relay is not enough for
our negative route even before considering known restrictions on special
self-similar profiles.

## 4. Fixed-volume periodic copies cannot close the turnover

The current source-reference system and the older ring experiments are
periodic/fixed-volume mechanism locators. This section records the exact
reason they cannot by themselves certify (2.3).

Suppose one normalized cell/profile `U` at fixed physical volume has kinetic
energy `E(U)>0`. Reproducing the same fixed-volume profile with amplitude
gain `g` gives energy

    E(g U)=g^2 E(U).                                        (4.1)

For an unforced NS solution the total kinetic energy cannot increase. Thus
an exact same-volume copy, with no reduction of active volume and no change
of normalization, requires

    g <= 1.                                                 (4.2)

The same statement holds for a finite Fourier shell with M equal normalized
components: reproducing M corresponding children each at common gain g
multiplies that shell energy by `g^2`. One child can in principle collect
energy from several parents, but that is not a regenerated M-component cell.

Therefore the quartic births and shear transmission proved in
`2026-09-10-source-shear-feedback.md` are useful topology/polarization facts,
not a turnover certificate. The load-bearing missing operation is physical
concentration/intermittency.

For `g=5/2`, energy alone requires the active-volume fraction of a same-shape
output to be at most

    1/g^2 = 4/25 = 0.16.                                   (4.3)

An isotropic half-scale profile has volume fraction `1/8=0.125`, which is
small enough: its energy ratio is exactly

    (5/2)^2 / 8 = 25/32.                                   (4.4)

This is the quantitative margin the next localized turnover construction
should exploit.

## 5. The source quartic term has the right formal localization order

There is one positive clue from the preceding exact source-reference
calculation. For equal parent amplitudes A, the doubled-parent coefficient
has leading term

    v_(2p)(t)=(16 i/3)c_0 Q (b u)^3 A^4 t^3 N+O(t^4).      (5.1)

The growing/decaying source polarizations obey

    N = [a_+(u)-a_-(u)]/(2 c_0 Q).

Hence the formal growing-coordinate amplitude in (5.1), divided by one
parent amplitude, is

    G_formal(beta) = (8/3) beta^3,
    beta = b u A t.                                        (5.2)

This is an exact consequence of the already proved t^3 coefficient; it is
**not** a remainder estimate at beta of order one. Formal gain two occurs
at `beta^3=3/4`; the canonical gain `5/2` occurs at

    beta^3=15/16.                                          (5.3)

Thus the favorable coefficient reaches the required turnover only near one
full carrier-scale nonlinear time. A small-time Taylor proof cannot certify
it; all higher modes, depletion, pressure, and viscosity are then load-bearing.
This agrees with the previous numerical pilot, which was reliable only for
early born doubled energy and was not converged at the attempted later
turnover time.

There is nevertheless a useful localization locator. If a parent amplitude
has a Gaussian envelope

    G_ell(x)=exp(-|x|^2/(2 ell^2)),                         (5.4)

then the four-parent product appearing in the quartic principal interaction
has

    G_ell^4 = exp(-2|x|^2/ell^2) = G_(ell/2).              (5.5)

Its squared-amplitude volume is therefore smaller by exactly `1/8` in three
dimensions. Algebraically, the quartic order that first produces the doubled
parent is also the first product order whose Gaussian envelope has exactly
the factor-two width required by (2.5).

This is only a **principal-symbol locator**. For modulated waves, derivatives
of the envelope and the nonlocal Leray projection contribute additional
terms; no exact localized identity analogous to (5.1) has been proved.
Moreover if `K=b ell >>1` is used to make carrier-symbol errors small, then
at beta of order one the physical displacement over the carrier turnover is

    A t / ell = beta/(u K),                                (5.6)

which is small. The envelope has not undergone an order-one material
reorganization on that time scale. If instead `K=O(1)`, there is no WKB
small parameter controlling the passage from (5.1) to a localized packet.
There is therefore no simultaneous asymptotic regime in which the plane-wave
quartic coefficient plus (5.5), by themselves, prove the required physical
turnover. This is a proof-strategy wall, not a no-go theorem for full NS.

## 6. Exact acceptance contract for the next attack

A result counts as the missing turnover only if it establishes, for one
scale-normalized localized input class and fixed viscosity:

1. **Exact original NS evolution.** No body force, no resetting between
   stages, complete Leray pressure, diffusion, all generated modes and
   exterior retained.
2. **Physical concentration.** An output cell at scale at most `ell/2`
   satisfying fixed-profile lower bounds analogous to (1.1)--(1.2).
3. **Supercritical gain.** A uniform amplitude gain, for example `g=5/2`,
   or any fixed `g` in `(2,2sqrt(2))` for half-scale turnover.
4. **Closure.** The entire output state, including sidebands/background,
   lies in the next admissible input class without deleting inherited fields.
5. **Turnover time.** `Delta t <= C ell/A` with C independent of generation.
6. **One-data iteration.** The countable chain is an actual forward history
   from one nonzero Schwartz datum, not a sequence of separately prepared
   finite-horizon data.

If items 1--6 are proved, Theorem 1 supplies the terminal blow-up implication;
there is no additional mysterious "cascade principle" left to establish.
Whole-space localization and one-data closure are part of the turnover
lemma rather than deferred decorations.

Conversely, a future impossibility theorem for every admissible localized
cell would have to use more than the fixed-volume energy wall. The window
(2.3) is energetically and dissipatively consistent, so energy scaling alone
cannot prove global regularity.

## 7. Validation and scope

`research/check_supercritical_turnover.py` was executed before upload and
passed **498 exact rational assertions**. It checks the canonical recurrence,
finite-prefix geometric sums through 40 generations, fixed-volume energy
wall calibrations, rational samples of the general window, half-scale volume
margin, and the formal quartic beta-cube thresholds. The checker verifies
only scaling algebra; it is not a PDE solver or a computer-assisted turnover
proof.

The source-reference t^3 coefficient used in Section 5 is taken from the
previous author proof and exact checker in
`research/evidence/2026-09-10-source-shear-feedback.md`; its independent
audit remains pending. The full-duration transfer negative control is the
previous project theorem in
`research/evidence/2026-09-08-full-duration-mixing-cascade.md`, with its own
recorded audit status.

A full repository checkout was not used for this additive packet. Therefore
the repository-wide verifier, all historical checkers, manuscript build and
Lean were not rerun. No existing PLAN/manuscript/proof-graph status is
silently changed by this note.
