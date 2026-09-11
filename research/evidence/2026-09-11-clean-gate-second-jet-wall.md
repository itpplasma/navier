# Second-jet wall for the contamination-free dyadic gate

Date: 2026-09-11. This packet continues the clean family in
`2026-09-11-clean-dyadic-gate.md` and the actual first-gate realization in
`2026-09-11-routed-first-gate.md`.

**Status: exact author Fourier-jet calculation; independent audit and novelty
undetermined.** No localized turnover or singular solution is claimed.

## 1. Setup

Use the contamination-free family

    k1=(1,0,0),   a1=(0,1,z),
    k2=(0,1,0),   a2=(1,0,z),
    k3=(-z,0,1),  a3=(1,0,z),

and let the positive Fourier coefficients be `c1,c2,c3`, with independent
negative-mode coefficients `d1,d2,d3` during the algebraic calculation.  The
reality condition may be imposed afterwards by `d_j=conjugate(c_j)`.

For the original projected Navier--Stokes equation in Fourier variables,

    d_t u_k = -nu |k|^2 u_k
              - i P_k sum_(p+q=k) (u_p.q) u_q.             (1.1)

The previous packet proves that the nonlinear first derivative has only the
three selected children and their conjugates.  In lattice coordinates relative
to `(k1,k2,k3)`, their support is

    +/-(-1,-1,0),  +/-(1,0,-1),  +/-(1,0,1).              (1.2)

## 2. An unavoidable new mode in the second derivative

Consider the lattice frequency

    r=(-2,-1,0) = (-1,0,0)+(-1,-1,0).                     (2.1)

It is absent from both the initial support and the first nonlinear derivative.
Its only parent--child support decomposition is exactly the one displayed in
(2.1): the old `-k1` parent collides with the newly born `-k1-k2` child.
There is no second decomposition with which a phase choice could cancel it.

Exact differentiation of (1.1) at `t=0` gives

    u_r''(0) = (0,0,-2 d1^2 d2 z).                        (2.2)

The coefficient is independent of viscosity.  Indeed the linear viscous term
cannot create a frequency absent from the initial and first-derivative support;
viscous differentiation of the parents only feeds the same first-generation
frequencies.  Equation (2.2) is therefore a genuine original-NS parent--child
term.

The conjugate frequency `(2,1,0)` has the corresponding reality-conjugate
coefficient.

## 3. Consequence for the exact projective circuit

Projective return of the clean three-gate circuit requires

    Q(z)=z^10-z^9+4z^8+2z^6-2z^5
         -8z^3-32z^2+40z-16 = 0.                          (3.1)

The checker verifies `gcd(Q,z)=1`; in particular every projective-return root
has `z!=0`.  Hence if the first two parent amplitudes are nonzero, (2.2) cannot
vanish at any clean projective-return root.

This gives a sharp no-go statement:

> The clean three-parent circuit can eliminate every unwanted quadratic mode
> at the first derivative, but it cannot be an exact three-mode replacement
> history.  Before a second selected generation is completed, persistence of
> the old parents creates genuinely new Fourier support at second time order.

The obstruction is stronger than a generic "higher modes appear" warning:
the displayed pollutant has a unique support ancestry, so no choice of the
three initial phases can cancel it.

## 4. Implication for the live route

The new clean family remains useful because it removes the order-one first-gate
siblings.  But an autonomous turnover must now do at least one of the
following:

1. **enlarge the return class** so modes such as `-2k1-k2` are retained and
   participate in a finite/infinite self-similar state;
2. **physically separate parent and child after birth** quickly enough that
   their next interaction is perturbative, while keeping one exact forward
   history;
3. **damp/filter the inherited parents or pollutants** by a load-bearing
   background mechanism, such as the new strain-router direction, and then
   localize that mechanism to finite energy;
4. find a different circuit in which the entire parent--child closure, not
   just the first quadratic source, is invariant.

Option 1 is the most algebraically testable next step.  The natural finite-jet
experiment is to generate the complete support through several derivatives,
quotient by the dyadic return map, and search for a finite projective closure or
a monotone explosion of distinct ancestry classes.  A finite closure would be
a genuine candidate state space for the turnover; a proof of unavoidable
support growth would rule out this circuit family as an exact Fourier cascade
and force localization/transport to carry the burden.

## 5. Reproducibility

`research/check_clean_gate_second_jet.py` computes the original Fourier
quadratic vector field with independent positive/negative parent amplitudes.
It checks the clean first support, the unique decomposition (2.1), the exact
coefficient (2.2), and nonvanishing on every projective-return root.

No PDE numerics, continuum localization estimate, manuscript update, Lean
change, or canonical claim promotion is part of this additive packet.
