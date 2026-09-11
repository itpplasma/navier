#!/usr/bin/env python3
"""Exact symbolic checks for nested 2D3C localization identities."""
import sympy as sp

x, y, z, t, nu = sp.symbols("x y z t nu", nonzero=True)
a = sp.Function("a")(x)
b = sp.Function("b")(y)
c = sp.Function("c")(z)
d = sp.Function("d")(x)
e = sp.Function("e")(y)
f = sp.Function("f")(z)
psi = sp.Function("psi")(y, t)
q = sp.Function("q")(x, y, t)

Phi = a * b * c * psi
Theta = d * e * f * q

V = sp.Matrix([sp.diff(Phi, y), -sp.diff(Phi, x), 0])
W = sp.Matrix([-sp.diff(Theta, z), 0, sp.diff(Theta, x)])


def div(F):
    return sp.diff(F[0], x) + sp.diff(F[1], y) + sp.diff(F[2], z)


def lap(s):
    return sp.diff(s, x, 2) + sp.diff(s, y, 2) + sp.diff(s, z, 2)


def adv(U, F):
    return sp.Matrix([
        U[0] * sp.diff(F[i], x)
        + U[1] * sp.diff(F[i], y)
        + U[2] * sp.diff(F[i], z)
        for i in range(3)
    ])


assert sp.simplify(div(V)) == 0
assert sp.simplify(div(W)) == 0

v = sp.diff(psi, y)
V0 = sp.Matrix([v, 0, 0])
assert all(sp.simplify(s) == 0 for s in adv(W, V0))
assert all(sp.simplify(s) == 0 for s in (adv(V0, W) - v * W.diff(x)))


def Lv_scalar(s):
    return sp.diff(s, t) - nu * lap(s) + v * sp.diff(s, x)


def Lv_vec(F):
    return sp.Matrix([Lv_scalar(F[i]) for i in range(3)])


Etheta = sp.expand(Lv_scalar(Theta))
curl_Etheta = sp.Matrix([-sp.diff(Etheta, z), 0, sp.diff(Etheta, x)])
assert all(sp.simplify(s) == 0 for s in (Lv_vec(W) - curl_Etheta))

qt = nu * (sp.diff(q, x, 2) + sp.diff(q, y, 2)) - v * sp.diff(q, x)
Etheta_pde = sp.expand(Etheta.subs(sp.diff(q, t), qt))
Ei_expected = (
    -nu
    * (
        2
        * (
            sp.diff(d, x) * e * f * sp.diff(q, x)
            + d * sp.diff(e, y) * f * sp.diff(q, y)
        )
        + q
        * (
            sp.diff(d, x, 2) * e * f
            + d * sp.diff(e, y, 2) * f
            + d * e * sp.diff(f, z, 2)
        )
    )
    + v * sp.diff(d, x) * e * f * q
)
assert sp.simplify(Etheta_pde - Ei_expected) == 0


def Lheat(s):
    return sp.diff(s, t) - nu * lap(s)


psit = nu * sp.diff(psi, y, 2)
Ephi = sp.expand(Lheat(Phi).subs(sp.diff(psi, t), psit))
Eo_expected = -nu * (
    2 * a * sp.diff(b, y) * c * v
    + psi
    * (
        sp.diff(a, x, 2) * b * c
        + a * sp.diff(b, y, 2) * c
        + a * b * sp.diff(c, z, 2)
    )
)
assert sp.simplify(Ephi - Eo_expected) == 0

curl_Ephi = sp.Matrix([sp.diff(Ephi, y), -sp.diff(Ephi, x), 0])
Lheat_V = sp.Matrix([Lheat(V[i]) for i in range(3)])
assert all(
    sp.simplify(s.subs(sp.diff(psi, t), psit)) == 0
    for s in (Lheat_V - curl_Ephi)
)

chi, Q = sp.symbols("chi Q")
common_cutoff_mismatch = sp.expand(chi**2 * Q - chi * Q)
assert sp.factor(common_cutoff_mismatch) == chi * (chi - 1) * Q

print("nested 2D3C localization: 8 exact symbolic identity groups passed")
