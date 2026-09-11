#!/usr/bin/env python3
"""Exact autonomous synthesis of the common purifier strain by high-high -> low NS pairs.

This is a finite Fourier-symbol certificate. Ten mutually separated pump
pairs produce exactly the ten transverse low modes whose real sine field has
gradient H at the origin. Every other nonzero quadratic center is separated
from the low ball by an exact spectral moat.

No PDE trajectory, recursive turnover, or singular solution is certified here.
"""
from fractions import Fraction as F

CHECKS = []
def check(ok, label):
    if not ok:
        raise AssertionError(label)
    CHECKS.append(label)

def add(x, y): return tuple(a+b for a,b in zip(x,y))
def sub(x, y): return tuple(a-b for a,b in zip(x,y))
def scale(c, x): return tuple(c*a for a in x)
def dot(x, y): return sum(a*b for a,b in zip(x,y))
def norm2(x): return dot(x,x)
def cross(x, y):
    return (x[1]*y[2]-x[2]*y[1],
            x[2]*y[0]-x[0]*y[2],
            x[0]*y[1]-x[1]*y[0])

def proj(k, v):
    kk = norm2(k)
    check(kk != 0, "projection frequency nonzero")
    return sub(v, scale(dot(k,v)/kk, k))

def leray_pair(p, a, q, b):
    """Symmetric principal symbol with the common Fourier factor -i suppressed."""
    k = add(p,q)
    return proj(k, add(scale(dot(a,q), b), scale(dot(b,p), a)))

e1=(F(1),F(0),F(0))
e2=(F(0),F(1),F(0))
e3=(F(0),F(0),F(1))

H = (
    (F(71,100), F(-1),      F(147,200)),
    (F(-1),     F(-143,200),F(7,25)),
    (F(147,200),F(7,25),    F(1,200)),
)
check(all(H[i][j] == H[j][i] for i in range(3) for j in range(3)),
      "H symmetric")
check(sum(H[i][i] for i in range(3)) == 0, "H trace free")

A=F(143,400)
B=F(-1,400)
modes = [
    (e2, scale(F(-1,2), e1)),
    (e1, scale(F(-1,2), e2)),
    (e3, scale(F(147,400), e1)),
    (e1, scale(F(147,400), e3)),
    (e3, scale(F(7,50), e2)),
    (e2, scale(F(7,50), e3)),
    (add(e1,e2), scale(A/2, sub(e1,e2))),
    (sub(e1,e2), scale(A/2, add(e1,e2))),
    (add(e1,e3), scale(B/2, sub(e1,e3))),
    (sub(e1,e3), scale(B/2, add(e1,e3))),
]
check(len(modes) == 10, "ten low strain modes")

# Their real low field is sum_j 2 d_j sin(kappa_j.x), so
# grad u_low(0)=2 sum_j d_j tensor kappa_j = H.
M = [[F(0) for _ in range(3)] for _ in range(3)]
for j,(kappa,d) in enumerate(modes):
    check(dot(kappa,d)==0, f"low mode {j} transverse")
    for r in range(3):
        for c in range(3):
            M[r][c] += d[r]*kappa[c]
for r in range(3):
    for c in range(3):
        check(2*M[r][c] == H[r][c], f"strain entry {r}{c}")
check(all(M[r][c] == M[c][r] for r in range(3) for c in range(3)),
      "low gradient half-strain symmetric")

# Exact pump synthesis.
#
# For kappa.d=0 set r=kappa x d, p=N r, q=kappa-p,
# a=d, b=kappa/|kappa|^2 + r/(N |r|^2).
# Then a.p=a.q=b.q=0, b.p=1, and
# P_kappa[(a.q)b+(b.p)a]=d.
pumps=[]
for j,(kappa,d) in enumerate(modes):
    r = cross(kappa,d)
    check(norm2(r) != 0, f"pump {j} cross direction nonzero")
    N = F(100*(3**j))
    p = scale(N,r)
    q = sub(kappa,p)
    a = d
    b = add(scale(F(1,1)/norm2(kappa), kappa),
            scale(F(1,1)/(N*norm2(r)), r))
    check(add(p,q)==kappa, f"pump {j} frequency closure")
    check(dot(a,p)==0, f"pump {j} a transverse p")
    check(dot(a,q)==0, f"pump {j} a transverse q")
    check(dot(b,q)==0, f"pump {j} b transverse q")
    check(dot(b,p)==1, f"pump {j} normalization b.p=1")
    child = leray_pair(p,a,q,b)
    check(child==d, f"pump {j} exact desired Leray child")
    pumps.append((kappa,d,p,a,q,b))

# Include reality conjugates. A matched positive pair produces +kappa;
# its matched negative pair produces -kappa. Self-conjugate sums are zero
# and therefore killed by the divergence factor in Q=-P div(u tensor u).
centers=[]
for j,(_,_,p,a,q,b) in enumerate(pumps):
    for tag,k,pol in (("p",p,a),("q",q,b)):
        centers.append((j,tag,+1,k,pol))
        centers.append((j,tag,-1,scale(F(-1),k),pol))

low_pairs=[]
high_norms=[]
for i in range(len(centers)):
    for j in range(i,len(centers)):
        ci,cj=centers[i],centers[j]
        s=add(ci[3],cj[3])
        ns=norm2(s)
        if ns <= 16:
            low_pairs.append((ci,cj,s))
            if ns == 0:
                # Only a carrier and its reality conjugate may reach zero.
                check(ci[0]==cj[0] and ci[1]==cj[1] and ci[2]==-cj[2],
                      "every zero center is a same-carrier conjugate")
            else:
                # Every nonzero low center must be a matched p/q pair from
                # one pump family with the same sign.
                check(ci[0]==cj[0] and ci[1]!=cj[1] and ci[2]==cj[2],
                      "every nonzero low center is an intended matched pump")
                kappa=modes[ci[0]][0]
                check(s==scale(F(ci[2]),kappa),
                      "matched low center equals signed target kappa")
        else:
            high_norms.append(ns)

check(len(low_pairs)==40, "exactly forty low pair centers incl. conjugate zeros")
check(min(high_norms) == F(10000), "exact spectral moat: every other center has |xi|>=100")

# Recheck the signed negative child directly away from zero.
for j,(kappa,d,p,a,q,b) in enumerate(pumps):
    neg = leray_pair(scale(F(-1),p),a,scale(F(-1),q),b)
    check(neg==scale(F(-1),d), f"pump {j} negative child is -d")

print(f"PASS: {len(CHECKS)} exact assertions.")
print("Exact result: ten separated pump pairs synthesize the common trace-free strain H")
print("in the low quadratic Leray output; all other nonzero centers satisfy |xi|>=100.")
print("Scope: Fourier-symbol/frequency-separation certificate only; no NS trajectory or turnover.")
