# Finite Lorentz refinement synthesis

Frozen base ec2ed88c8d1fdf3b66b0e989827d44d93f1f76df. Controller derivation;
independent synthesis review passed, independent integration review passed.
No NS producer or novelty claim.

Fix q in [3,infinity), finite, e.g. q=6. For measurable vector f define
L_q(f)^q = integral_0^infinity [s^(1/3) f*(s)]^q ds/s,
where f* is the decreasing rearrangement of |f|. This is the usual
L^{3,q} rearrangement quasinorm, with no normalization prefactor.
Take Fourier convention exp(-2pi i x.xi), B=sqrt(4pi/3),
lambda_k=2^k N0, sharp L2 shells Delta_k on (lambda_k/2,lambda_k],
and b_k=lambda_k^(1/2)||Delta_k f||2. Then

    L_q(f) <= C_q ||b||ellq,
    C_q=2(log 8)^(1/q)(2B+1).                              (L1)

Proof first for finitely many shells. The low sum has L-infinity bound
A_J=B sum_(k<=J)lambda_k b_k and the high sum has squared L2 norm
T_J=sum_(k>J)lambda_k^(-1)b_k^2. Chebyshev implies
f*(s)<=A_J+s^(-1/2)T_J^(1/2). With s_J=lambda_J^(-3),

    s_J^(1/3)f*(s_J) <= d_J,
    d_J=B sum_(k<=J)2^(k-J)b_k
          +[sum_(k>J)2^(J-k)b_k^2]^(1/2).

For s in [s_(J+1),s_J], monotonicity of f* gives
s^(1/3)f*(s)<=2d_(J+1). Integrating each interval yields
L_q(f)<=2(log8)^(1/q)||d||ellq. Young's inequality bounds the
first term's ellq norm by 2B||b||ellq. For the second term apply
Young on ell^(q/2) to b^2 with kernel sum_(n>=1)2^(-n)=1.
Its ellq norm is at most ||b||ellq. This proves (L1).
For general L2 f, finite shell truncations converge in L2 and along
a subsequence almost everywhere. Lorentz Fatou follows from

    L_q(f)^q=3 integral_0^infinity alpha^(q-1)
                         measure{|f|>alpha}^(q/3) d alpha.

Fatou for the level-set measures and then for this integral proves
(L1) for general f. No multiplier estimate on Lorentz space is used.

For finite ball-supported f_j, supp fhat_j subset {|xi|<=N_(j+1)},
c_j=N_j^(1/2)||f_j||2, sharp shell contraction gives

    b_k(sum f_j)<=sum_(j>=k-1)2^((k-j)/2)c_j.

The convolution kernel has ell1 norm L=sqrt2/(1-2^(-1/2)), hence

    L_q(sum f_j)<= C_q L (sum c_j^q)^(1/q).                 (L2)

This permits arbitrary overlapping low corrections. Include the coarse
term u_0 as index j=-1, since it is supported at N0=N_(-1+1), with
c_(-1)=(N0/2)^(1/2)||u_0||2. Thus for the exact projected family
in research/evidence/2026-09-07-whole-space-cubic-refinement.md,

    sup_(0<=t<=H) sup_(M>=1) sum_(0<=j<M) [N_j^(1/2)||u_(j+1)-u_j||2]^q
                   <= K_q(d,nu,H,N0)^q                    (RF-q)

implies uniform finite-approximant L-infinity_t L^{3,q}_x bound
C_q L [(N0/2)^(q/2)||d||2^q+K_q^q]^(1/q).
Actual paths are smooth at each cutoff; all-time versus essential-time
uniformity follows from continuity of finite sums. No uniform Lorentz
convergence in time is required. Compact-classical L2 identification
has already been independently audited; Lorentz Fatou transfers the
same bound to the original classical branch at every classical time.
The finite-q Lorentz continuation consumer and its inspected source
hypotheses are proved in 2026-09-07-lorentz-continuation.md. Its
independent component and full integration reviews passed. The combined
implication remains conditional on RF-q. q=infinity is NOT being used as a continuation
criterion. Constants may depend on fixed finite q as well as full
initial datum, viscosity, fixed N0 and finite horizon.

For any q>1, RF-q additionally gives the uniform L2 tail

    ||u_M-u_L||2 <= N0^(-1/2) 2^(-L/2)
          (1-2^(-q' /2))^(-1/q') K_q, q'=q/(q-1).

The exact finite-M producer identity for q>=3 is

    Wq_M=sum_(0<=j<M) a_j^q,
    (1/q) Wq_M' + nu Dq_M = Piq_M,
    Dq_M=sum N_j^(q/2)||e_j||2^(q-2)||grad e_j||2^2,
    Piq_M=sum N_j^(q/2)||e_j||2^(q-2)
                    [<F_j,e_j>-b(e_j,u_j,e_j)].

An integrated bound integral_0^t Piq_M <= nu integral_0^t Dq_M+C
at EVERY upper time t<=H, uniformly M, suffices; strict absorption
is unnecessary for the supremum certificate alone. Schwartz initial
shells give a finite initial Wq_M uniformly M. This bound is UNPROVED.
RF-q with q>3 is a weaker target than RF-CUBE. Neither a known
continuation criterion nor the synthesis proof produces it. Its
possible value is allowing a new large-q concentration/record attack
on actual signed pair production; that is the first remaining gap.
