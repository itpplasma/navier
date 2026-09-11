# Instantaneous strain separation for the clean dyadic gate

Date: 2026-09-11. This packet combines the clean dyadic circuit with the
affine-strain routing idea already present in the repository.

**Status: exact author carrier theorem on an affine infinite-energy unforced
Navier--Stokes background; independent audit and novelty undetermined.** It is
an instantaneous spectral filter, not a finite-time localized turnover.  No
terminal status is promoted.

## 1. Positive projective-return root

Keep the clean family and return polynomial

    Q(z)=z^10-z^9+4z^8+2z^6-2z^5
         -8z^3-32z^2+40z-16.                              (1.1)

Exact Sturm/root counting gives one and only one root in

    I=(12847/10000,803/625)=(1.2847,1.2848).              (1.2)

Call it `z_*`.

The parent carriers are

    p1: k=(1,0,0),       a=(0,1,z),
    p2: k=(0,1,0),       a=(1,0,z),
    p3: k=(-z,0,1),      a=(1,0,z).                       (1.3)

The three selected first-generation children are

    s1: k=(-1,-1,0),     a=(0,0,-2z),                     (1.4)

    s2: k=(1+z,0,-1),
        a=(-z^3/D_+,1,-z^3(z+1)/D_+),                     (1.5)

    s3: k=(1-z,0,1),
        a=( z^3/D_-,1, z^3(z-1)/D_-),                     (1.6)

where

    D_+=z^2+2z+2,       D_-=z^2-2z+2.                    (1.7)

## 2. A rational trace-free strain

Set

    H = [[ 11/2, -33/4,   -1  ],
         [-33/4,   -3,     33/4],
         [  -1,    33/4,   -5/2]].                       (2.1)

It is symmetric and trace free.  For any carrier scale `b>0`, the affine field

    U_b(x)=nu b^2 H x                                     (2.2)

is an exact steady unforced Navier--Stokes solution on `R3`: `Delta U_b=0`,
`div U_b=0`, and `(U_b.grad)U_b` is the gradient of the quadratic potential
`(nu b^2)^2 x.H^2.x/2`.  Its scope is deliberately only algebraic because
`U_b` has infinite kinetic energy.

For a transverse Kelvin carrier with physical wavevector `b k` and
polarization `a`, the instantaneous logarithmic amplitude-energy rate divided
by `nu b^2` is

    R_H(k,a)=-(a.H.a)/|a|^2-|k|^2.                        (2.3)

## 3. All selected children grow, all parents decay

For the vertical selected child,

    R_H(s1)=1/2.                                          (3.1)

The other two rates are rational functions of `z`.  Exact numerator root
counting on the isolating interval (1.2), together with manifestly positive
denominators, gives

    R_H(s2)>0,       R_H(s3)>0                             (3.2)

throughout `I`.  Numerically at `z_*` they are approximately

    R_H(s2)=0.5333...,   R_H(s3)=0.4619....                (3.3)

In contrast the three parent rates are exactly

    R_H(p1)=(3z^2-33z+4)/(2(z^2+1)),                      (3.4)

    R_H(p2)=(3z^2+4z-13)/(2(z^2+1)),                      (3.5)

    R_H(p3)=-(2z^4-z^2-4z+13)/(2(z^2+1)),                 (3.6)

and each is strictly negative on `I`.  At the root they are approximately

    (-6.3090,-0.5489,-2.1994).                            (3.7)

Thus one exact affine strain separates the desired newborn modes from **all
three inherited parents at the level of instantaneous viscous Kelvin rates**.

## 4. The same strain damps the entire inherited-parent ladder

The all-orders wall packet proved that

    r_n=-n k1-k2=(-n,-1,0),       n>=1,                   (4.1)

has polarization `e3`.  Because

    e3.H.e3=-5/2,                                         (4.2)

its normalized rate is exactly

    R_H(r_n,e3)=5/2-(n^2+1)=3/2-n^2.                     (4.3)

Hence

    R_H(r_1)=1/2                                           (4.4)

for the selected first child, while every pollutant on the continuation of
the ray satisfies

    R_H(r_n)<=-5/2,       n>=2.                            (4.5)

This is the useful spectral gap suggested by the ladder analysis: the same
polarization can be amplified at the first selected wavenumber yet damped at
all higher inherited-parent harmonics because viscosity contributes the
strictly increasing `|r_n|^2` cost.

## 5. What this does and does not solve

The result supplies a new compatible pair of mechanisms:

    algebraically clean first birth
      + instantaneous parent/ladder spectral filtering.                  (5.1)

It eliminates a potential immediate contradiction between the clean circuit
and the strain-router idea.  In particular, no strain-polarization sign wall
forces the desired child and its inherited-parent ladder to behave alike once
viscosity is retained.

However (5.1) is **not yet a turnover**.  Under a finite affine-strain pulse the
wavevectors themselves obey a Kelvin transport equation and their directions
change; an instantaneous sign need not persist for one order-one filtering
time.  Moreover the affine background (2.2) has infinite energy and its
magnitude scales like `b^2`, so it cannot simply be inserted into the desired
one-Schwartz-datum chain.

The next tests are therefore sharply defined:

1. integrate the full Kelvin system over a finite strain interval and determine
   whether a quantitative child/parent separation survives after wavevector
   deformation;
2. search for a time-dependent trace-free symmetric **strain loop** whose net
   spatial deformation returns the three selected carrier directions while
   viscosity provides irreversible parent/ladder attenuation;
3. if such a finite-time filter exists, replace the affine field by a
   finite-energy localized strain packet and quantify the pressure/tail error
   on the turnover time scale.

Failure of item 1 for this particular `H` should not be hidden: the theorem in
this packet is intentionally instantaneous.  A finite-time filter must be
proved separately.

## 6. Reproducibility

`research/check_clean_gate_strain_filter.py` freezes the rational matrix (2.1),
the exact root interval, all selected/parent rate signs, and the all-`n` ladder
formula (4.3).  It uses exact SymPy rational arithmetic and polynomial root
counting; floating values in (3.3),(3.7) are explanatory only.

No finite-time PDE trajectory, finite-energy localization, manuscript/formal
change, or NS-R3 claim is made here.
