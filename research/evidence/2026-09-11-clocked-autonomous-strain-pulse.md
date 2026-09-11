# Clocked autonomous purifier pulse from three viscous pump layers

Date: 2026-09-11. Repository input:
`itpplasma/navier@6bb0056813aff78e34d56a3214d191a3994cfc17`.

**Status: exact second-Picard/Stokes-Duhamel mechanism plus a perturbative
original-NS lift; independent mathematical audit and novelty undetermined.**
This packet strengthens the preceding autonomous-strain-birth result in the
specific direction demanded by the current blocker. The low strain need not be
static after it is born. Three preloaded high-frequency pump layers can cancel
both its leading onset and its slow low-frequency heat tail, leaving a
one-signed strain pulse whose clock is set entirely by ordinary viscosity.

The exact algebra and a thirty-pump spectral-separation instance are frozen by
`research/check_clocked_strain_pulse.py`, which passes 365 exact symbolic and
rational assertions.

This is not yet a large-amplitude clean-gate integration theorem. The exact
pulse statement is for the second Picard iterate driven by Stokes-evolved pump
modes; the full nonlinear statement below is perturbative in the total pump
data. Recursive turnover remains open.

## 1. One prescribed low child and its Stokes-Duhamel response

Fix one transverse low mode `(kappa,d)`, with

    d.kappa=0.                                             (1.1)

Use the exact pump construction from the preceding packet. Let

    r=kappa cross d,
    p=N r,
    q=kappa-p,                                             (1.2)

and choose transverse polarizations `a,b` so that

    C(p,a;q,b)=d.                                         (1.3)

Because `r.kappa=0`, the heat-decay gap between the parent product and the low
child is exactly

    D = |p|^2+|q|^2-|kappa|^2
      = 2 N^2 |r|^2 >0.                                  (1.4)

Let `a0=|kappa|^2`. If the product of the two parent scalar coefficients is
`c`, then the `+kappa` coefficient of the quadratic Stokes-Duhamel term has the
common vector factor `-i d` and scalar factor

    F_(c,D)(t)
      = c [exp(-nu a0 t)-exp(-nu(a0+D)t)]/(nu D).         (1.5)

This is just the exact time integral

    integral_0^t exp[-nu a0(t-s)] exp[-nu(a0+D)s] ds.     (1.6)

The reality-conjugate coefficient at `-kappa` gives the corresponding real
sine carrier.

## 2. Three layers cancel onset and the slow low-frequency tail

Take three versions of the same exact pump geometry with parent radii in the
ratio

    1 : 2 : 3.                                             (2.1)

Their decay gaps are therefore

    D,       4D,       9D.                                (2.2)

Choose source-product weights

    c_1=5 c0,
    c_2=-32 c0,
    c_3=27 c0.                                             (2.3)

They satisfy two independent exact cancellations:

    c_1+c_2+c_3=0,                                        (2.4)

and

    c_1/D + c_2/(4D) + c_3/(9D)=0.                        (2.5)

Equation (2.4) cancels the instantaneous quadratic low source at `t=0`.
Equation (2.5) cancels the complete coefficient of the slow
`exp(-nu a0 t)` low-frequency heat tail in (1.5).

Summing the three responses gives exactly

    F_pulse(t)
      = -c0/(nu D) exp(-nu a0 t)
          [5 exp(-x)-8 exp(-4x)+3 exp(-9x)],               (2.6)

where

    x=nu D t.                                               (2.7)

Put `z=exp(-x)`, so `0<z<1` for `t>0`. The bracket factors exactly as

    5z-8z^4+3z^9
      = z(1-z)^2
          (3z^6+6z^5+9z^4+12z^3+15z^2+10z+5).            (2.8)

Hence it is strictly positive for every `t>0`. Choosing `c0<0` produces a
strictly positive low-child pulse with no sign reversal.

The double factor `(1-z)^2` also gives the exact initial expansion

    5e^(-x)-8e^(-4x)+3e^(-9x)
      = 60 x^2 - 280 x^3 + O(x^4).                        (2.9)

Thus the strain begins quadratically rather than linearly. At the opposite end
of time, (2.6) decays at least as

    exp[-nu(a0+D)t],                                      (2.10)

rather than leaving the slow `exp(-nu a0 t)` tail of a single low child.

This is the desired autonomous switch mechanism at second Picard order:
preloaded data, delayed onset, one-signed action, and high-frequency-clock
switch-off, with no external forcing and no reset.

## 3. Thirty pumps retain a clean low band

Apply the three-layer construction to each of the ten `(kappa_j,d_j)` modes
whose sine sum has gradient `H` at the origin. For the `j`th mode choose a
slightly different large base parent radius

    R_j=1000000+1000 j,       j=0,...,9,                   (3.1)

and use radii `R_j,2R_j,3R_j` for its three temporal layers. Since every
`kappa_j cross d_j` in the explicit decomposition is an axial rational vector,
this is realized exactly by a rational choice of `N` in (1.2).

The checker enumerates all 120 signed parent centers of these thirty pump
pairs. Among every pairwise quadratic center with `|xi|<=4`, the only ones are

* same-carrier conjugate sums at zero; and
* the intended matched same-layer sums `+/-kappa_j`.

Every other nonzero quadratic center satisfies the exact bound

    |xi|^2 >= 1000000,       hence |xi|>=1000.             (3.2)

Thus adding the extra temporal layers does not reintroduce a low-frequency
cross-family contamination at quadratic order.

For each `j`, its three gaps are exactly

    D_j, 4D_j, 9D_j,       D_j=2 R_j^2.                    (3.3)

## 4. Assemble the complete matrix H at a chosen pulse time

Let

    G(x)=5e^(-x)-8e^(-4x)+3e^(-9x)>0,       x>0.           (4.1)

Fix any target time `T>0`. For the `j`th low mode let

    a_j=|kappa_j|^2.                                       (4.2)

Because `G(nu D_j T)>0`, choose its common source scale `c0_j<0` by

    c0_j
      = -nu D_j exp(nu a_j T)/G(nu D_j T).                (4.3)

Then its scalar pulse coefficient (2.6) satisfies exactly

    F_j(T)=1.                                               (4.4)

Consequently, at the plane-wave second-Picard level, the real low field at
`T` is exactly

    W_low(T,x)=sum_j 2 d_j sin(kappa_j.x),                 (4.5)

and therefore

    grad W_low(T,0)=H.                                     (4.6)

The ten pulse shapes have slightly different `D_j`, but all are smooth and
strictly positive near `T`; by continuity, the resulting strain remains in an
arbitrarily small neighborhood of `H` on a sufficiently short nonzero time
window about `T`. The common-strain discriminator has strict inequalities, so
only such a neighborhood is required at mechanism level.

The signs and magnitudes in (4.3) are implemented by the scalar phases and
amplitudes of the parent Fourier coefficients. Reality is restored with the
usual conjugate modes.

## 5. Schwartz-packet and full original-NS perturbative lift

Replace every plane wave by a sufficiently narrow compact Fourier packet, use
the exact Leray projector on each packet, and add its reality conjugate. Call
the resulting real solenoidal Schwartz datum `F_delta`. The spectral moat
(3.2) permits one fixed low projector `Pi_low` to isolate only the intended
low children. For fixed `T` and finite pump set, the Stokes multipliers and
Leray symbol vary smoothly across the packets. Hence the second Picard term
`U_2` satisfies

    grad Pi_low U_2(T,0)=H+O(delta).                       (5.1)

Moreover its principal time profile has the quadratic onset and canceled slow
tail of Section 2, up to `O(delta)` packet errors.

Now solve the original unforced equation from the small datum

    u_epsilon(0)=epsilon F_delta.                          (5.2)

On any fixed finite interval inside the smooth small-data perturbative regime,
the classical mild solution depends analytically on `epsilon` in high Sobolev
spaces:

    u_epsilon(t)
      = epsilon exp(nu t Delta)F_delta
        +epsilon^2 U_2(t)+O(epsilon^3).                    (5.3)

The first term has no low-frequency support. Therefore

    grad Pi_low u_epsilon(T,0)
      = epsilon^2 [H+O(delta)+O(epsilon)].                 (5.4)

This is a genuine original unforced Navier--Stokes solution from one Schwartz
initial datum. At small amplitude it contains an autonomous, clocked,
approximately tail-free purifier pulse. No time-dependent forcing or manual
insertion is used.

Finally, ordinary Navier--Stokes scaling preserves fixed viscosity:

    u_(epsilon,lambda)(t,x)
       =lambda u_epsilon(lambda^2 t,lambda x).             (5.5)

At physical time `T/lambda^2`, its pulse strain is

    grad Pi_low u_(epsilon,lambda)
       =lambda^2 epsilon^2[H+O(delta)+O(epsilon)],          (5.6)

while its initial kinetic energy scales as

    ||u_(epsilon,lambda)(0)||_2^2
       =lambda^(-1) epsilon^2 ||F_delta||_2^2.             (5.7)

Thus finite energy does not impose a scale obstruction to making the local
clocked strain strong at small spatial scales. What remains difficult is its
simultaneous coupling to the large clean-gate state, not production of the
pulse in isolation.

## 6. What blocker remains

Compared with the previous state, two separate operations are now available
inside actual unforced NS histories:

1. a clean first nonlinear birth from one co-located Schwartz packet triple;
2. a finite-energy common discriminator whose required orientation `H` can be
   generated autonomously, and now can be made pulse-like rather than static.

The missing theorem is their **nonperturbative composition in one Cauchy
history**. It must prove that a scaled clocked pump can act strongly on the
actual contaminated target triple while:

* pump--clean cross interactions remain outside or small in the selected
  target windows;
* the quadratic pulse approximation survives at the required strength;
* inherited parents and rejected polarizations are suppressed by a definite
  factor;
* the residual pump and low-strain state after the pulse are small enough for
  the next clean gate; and
* the stage map has a supercritical gain `g/s>1` with summable total energy and
  time.

This is substantially more concrete than the earlier instruction to
"autonomously turn on a strain." The next decisive calculation is a
**single-stage combined gate--pulse map with scale-explicit error bounds**.
If that map cannot close, the exact term that breaks it should be recorded as
the next no-go theorem rather than introducing another carrier identity.

## 7. Audit boundary

`research/check_clocked_strain_pulse.py` verifies 365 exact assertions:

* the ten-mode decomposition of `H`;
* the two cancellation identities for `(5,-32,27)`;
* the positive factorization (2.8) and quadratic onset (2.9);
* all thirty exact Leray children and `1:4:9` decay gaps; and
* complete pairwise frequency enumeration with the moat (3.2).

The packet expansion and perturbative full-NS lift use standard smooth
Fourier-multiplier estimates and classical high-Sobolev mild theory. They have
not received an independent audit. The large-amplitude combined stage has not
been proved.

No regenerative turnover, common infinite cascade, finite-time singularity,
or arbitrary-data regularity theorem is claimed. `NS-R3` remains unresolved.
