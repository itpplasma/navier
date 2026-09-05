# HF01 numerical snapshot

This is a small mechanical falsifier for the signed cubic pressure quantity

\[
 P_3(u)=\int_{\mathbb T^3}p\,u\cdot\nabla|u|\,dx,
 \qquad -\Delta p=\partial_i\partial_j(u_i u_j),
\]

on \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\). It is a single static Fourier calculation. It is not a Navier–Stokes evolution, a singularity construction, or a proof about the Clay problem.

## Reproducible field

The script [`hf01-snapshot.py`](hf01-snapshot.py) uses NumPy's `default_rng` seed 0 and the SciPy FFT implementation. For each wavevector \(k\) in

```text
(1,0,1), (0,1,1), (1,1,0), (1,1,1), (2,1,1)
```

it samples vectors \(a_k,b_k\) from the standard normal generator and sets

\[
A(x)=\sum_k[a_k\cos(k\cdot x)+b_k\sin(k\cdot x)],\qquad u=-\nabla\times A.
\]

The resulting field is real and exactly divergence-free in analytic arithmetic. The seed-0 coefficients are:

| \(k\) | \(a_k\) | \(b_k\) |
|---|---|---|
| (1,0,1) | (0.12573022, −0.13210486, 0.64042265) | (0.10490012, −0.53566937, 0.36159505) |
| (0,1,1) | (1.30400005, 0.94708096, −0.70373524) | (−1.26542147, −0.62327446, 0.04132598) |
| (1,1,0) | (−2.32503077, −0.21879166, −1.24591095) | (−0.73226735, −0.54425898, −0.31630016) |
| (1,1,1) | (0.41163054, 1.04251337, −0.12853466) | (1.36646347, −0.66519467, 0.35151007) |
| (2,1,1) | (0.90347018, 0.09401230, −0.74349925) | (−0.92172538, −0.45772583, 0.22019512) |

The field is divided by its componentwise RMS, \(\sqrt{\operatorname{mean}_{i,x}|u_i|^2}\), computed on the initial grid (seed 0, \(N=32\)); this fixes scale while preserving the sign. Pressure is computed spectrally as

\[
\widehat p(k)=-\frac{k_i k_j}{|k|^2}\widehat{u_i u_j}(k),\quad k\ne0,
\qquad\widehat p(0)=0.
\]

## Run and result

Run:

```text
python hf01-snapshot.py --seed 0 --grid 32 64 128
```

Output from the reference run:

```text
seed=0 modes=((1, 0, 1), (0, 1, 1), (1, 1, 0), (1, 1, 1), (2, 1, 1)) normalization=divide by componentwise RMS 2.448855617268777
N=32  P3=5.783992666666046 independent=5.786715122797876 div_hat_rel=1.614e-15 L2=27.27912462538333
N=64  P3=5.786261948604166 independent=5.786191765308815 div_hat_rel=2.168e-15 L2=27.27912462538334
N=128 P3=5.786206891979936 independent=5.786186378309699 div_hat_rel=7.841e-15 L2=27.27912462538334
sign-flip check N=128: P3(u)=5.786206891979936 P3(-u)=-5.786206891979936
```

The positive value is robust across these grids and is nonzero by roughly six orders of magnitude above the observed pressure-work discrepancy (\(2.051367\times10^{-5}\) at \(N=128\)). The relative Fourier divergence residual is at double-precision roundoff scale. A small deterministic seed scan (seeds 0–19, \(N=64\), same modes and normalization) found both signs; for example, seed 0 is positive and seed 3 is negative. This is expected because \(p[-u]=p[u]\) while \(u\cdot\nabla|u|\) changes sign.

## Numerical caveat

The identity

\[
\int p\,u\cdot\nabla|u|=-\int |u|u\cdot\nabla p
\]

uses \(\nabla\cdot u=0\) and periodic integration by parts. The second value is evaluated independently from the spectral pressure gradient and differs by \(2.051367\times10^{-5}\) in the reported \(N=128\) run. Since \(|u|\) is nonanalytic at zeros of \(u\), the code evaluates \(\partial_j|u|=\sum_i u_i\partial_j u_i/|u|\) with a pointwise denominator guard `max(|u|,1e-14)`. The guard is not a proof of differentiability; convergence here only supports this numerical snapshot. No interval arithmetic, truncation-error bound, or claim of validated arithmetic is made.

The field is periodic and finite Fourier. It says nothing by itself about the forced or unforced Navier–Stokes initial-value problem on \(\mathbb R^3\), and it is not a counterexample to any global regularity statement.
