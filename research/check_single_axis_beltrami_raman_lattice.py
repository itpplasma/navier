#!/usr/bin/env python3
"""Exact single-axis Beltrami purifier and all-orders slow-lattice certificate.

Five equal-radius, same-helicity Raman modules all use the same fast direction
Q=e1.  Their shifts are pointed, their actual contaminated h0 responses span
Sym_0(3), and the already-certified inheritance strain H damps every active
translated slow state after the intended first h0 outputs.  The old p1/g1 and
full inherited ladder are exactly inactive because their polarizations have
zero e1 component.

Scope: leading effective Raman slow operator plus exact common-Beltrami high
background.  Finite-energy shell localization and the full high-sideband
normal form are separate checkpoints.
"""
from __future__ import annotations
import sympy as sp

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

z,N=sp.symbols('z N',real=True,positive=True)
lo=sp.Rational(12847,10000); hi=sp.Rational(803,625)
Qclean=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)
check(Qclean.eval(lo)<0 and Qclean.eval(hi)>0 and Qclean.count_roots(lo,hi)==1,
      'unique positive clean root isolated')

H=sp.Matrix([
 [sp.Rational(71,100),-1,sp.Rational(147,200)],
 [-1,sp.Rational(-143,200),sp.Rational(7,25)],
 [sp.Rational(147,200),sp.Rational(7,25),sp.Rational(1,200)],
])
H200=((142,-200,147),(-200,-143,56),(147,56,1))
check(H==H.T and sp.trace(H)==0,'inheritance filter symmetric trace free')
fro2=sp.factor(sum(H[i,j]**2 for i in range(3) for j in range(3)))
check(fro2==sp.Rational(21263,5000) and fro2<sp.Rational(33,16)**2,
      'operator norm bounded by 33/16 through Frobenius norm')

# Actual ancestry-contaminated h0 target coefficient, common Fourier phase removed.
pure=sp.Matrix([
 2*z*(z**3+2*z-4)/(3*(z**2-4*z+6)),
 2*z*(z**4-8*z**3+14*z**2-16*z+8)/(3*(z**2-4*z+6)*(z**2-2*z+2)),
 2*z*(z**6-4*z**5+7*z**4-8*z**3+14*z**2-16*z+8)/(3*(z**2-4*z+6)*(z**2-2*z+2)),
])
other=sp.Matrix([
 (5*z**10-32*z**9+89*z**8-120*z**7+67*z**6-12*z**5+159*z**4-396*z**3+412*z**2-176*z+20)/(6*(z**2-4*z+5)*(z**2-4*z+6)*(z**2-2*z+2)*(z**2-2*z+3)),
 (4*z**7-31*z**6+85*z**5-132*z**4+89*z**3-3*z**2-42*z+10)/(3*(z**2-4*z+6)*(z**2-2*z+2)*(z**2-2*z+3)),
 (5*z**11-42*z**10+145*z**9-204*z**8-151*z**7+1108*z**6-1901*z**5+1324*z**4+374*z**3-1326*z**2+872*z-140)/(6*(z**2-4*z+5)*(z**2-4*z+6)*(z**2-2*z+2)*(z**2-2*z+3)),
])
a=sp.Matrix([sp.cancel(x) for x in pure+other])
h=sp.Matrix([z-2,-1,-1])
check(sp.simplify(h.dot(a))==0,'actual contaminated trigger transverse')
num_ax,den_ax=sp.together(a[0]).as_numer_denom()
check(sp.gcd(sp.Poly(num_ax,z),Qclean).degree()==0,
      'actual trigger has nonzero e1 component at every clean root')
check(den_ax.subs(z,(lo+hi)/2)>0,'trigger denominator positive calibration')

# All modules use the same fast axis and the same shift length.
Q=sp.Matrix([1,0,0])
SHIFTS=[(0,-7,-1),(0,-7,1),(0,-5,-5),(0,-1,-7),(0,1,-7)]
check(all(sum(x*x for x in l)==50 for l in SHIFTS),'all shift norms squared equal 50')
check(all(l[0]==0 for l in SHIFTS),'all shifts perpendicular to Q')
check(all(l[1]+l[2]<=-6 for l in SHIFTS),'slow translation semigroup strictly pointed by y+z')

# Exact common Beltrami sphere/helicity.  m=Qxl has |m|=sqrt(50).
L=sp.sqrt(N**2+sp.Rational(25,2))
for j,lt in enumerate(SHIFTS):
    l=sp.Matrix(lt); m=Q.cross(l)
    q=N*Q+l/2; r=-N*Q+l/2
    beta=m+sp.I*q.cross(m)/L
    eps=m+sp.I*r.cross(m)/L
    check(sp.expand(q.dot(q)-L**2)==0 and sp.expand(r.dot(r)-L**2)==0,
          f'module {j}: common Beltrami sphere')
    check(sp.simplify(q.dot(beta))==0 and sp.simplify(r.dot(eps))==0,
          f'module {j}: helical parents transverse')
    check(all(sp.simplify(x)==0 for x in sp.I*q.cross(beta)-L*beta) and
          all(sp.simplify(x)==0 for x in sp.I*r.cross(eps)-L*eps),
          f'module {j}: common positive helicity')

# For fixed Q=e1 and l_x=0, kappa=(x,y,c), x=z-2 is common to all modules.
# The leading same-helicity Raman direction is, up to one common nonzero scalar,
# P_kappa Q.  Multiply by |kappa|^2 and form the strain.  The geometric span
# determinant factors completely.
def geom_col(lt):
    y=-1+lt[1]; c=-1+lt[2]; x=z-2
    k=sp.Matrix([x,y,c])
    d=sp.Matrix([y*y+c*c,-x*y,-x*c]) # |k|^2 P_k e1
    S=(d*k.T+k*d.T)/2
    return sp.Matrix([sp.expand(S[0,0]),sp.expand(S[1,1]),
                      sp.expand(S[0,1]),sp.expand(S[0,2]),sp.expand(S[1,2])])
Span=sp.Matrix.hstack(*[geom_col(l) for l in SHIFTS])
det=sp.factor(Span.det(method='berkowitz'))
check(det==-9216*(z-2)**3*(z**2-4*z-44)**2,
      'single-axis geometric strain determinant factorization')
check(sp.Poly(det,z).count_roots(lo,hi)==0,'strain determinant nonzero on clean interval')
# The omitted common scalar is -2 |l|^2 (a.e1)(e1.kappa), and the per-column
# |kappa|^-2 factors are positive, so the geometric rank is the physical rank.
check(hi<2,'common e1.kappa=z-2 is nonzero on clean interval')

# Old carrier classes that never enter this purifier: their e1 component is zero.
check(sp.Matrix([0,1,z]).dot(Q)==0,'p1 exactly inactive')
check(sp.Matrix([0,0,-2*z]).dot(Q)==0,'g1 exactly inactive')
check(sp.Matrix([0,0,1]).dot(Q)==0,'full inherited ladder polarization exactly inactive')

# Integer-polynomial arithmetic for the active translated slow states.  For an
# output frequency k=(x,y,c), the denominator-free polarization is
# d=|k|^2 e1-k k_x=(y^2+c^2,-xy,-xc).  R_2048<0 is equivalent to
# 25 |k|^2 |d|^2 + 256 d.H200.d > 0.
def padd(A,B):
    out=[0]*max(len(A),len(B))
    for i in range(len(out)):
        out[i]=(A[i] if i<len(A) else 0)+(B[i] if i<len(B) else 0)
    while len(out)>1 and out[-1]==0: out.pop()
    return out
def pscale(A,c):
    out=[c*x for x in A]
    while len(out)>1 and out[-1]==0: out.pop()
    return out
def pmul(A,B):
    out=[0]*(len(A)+len(B)-1)
    for i,x in enumerate(A):
      if x:
       for j,y in enumerate(B):
        if y: out[i+j]+=x*y
    while len(out)>1 and out[-1]==0: out.pop()
    return out
def psum(*args):
    out=[0]
    for A in args: out=padd(out,A)
    return out

def cert_poly(xc,xs,y,c):
    x=[xc,xs]; x2=pmul(x,x); yz2=y*y+c*c
    k2=padd(x2,[yz2])
    d0=[yz2]; d1=pscale(x,-y); d2=pscale(x,-c)
    dn=psum(pmul(d0,d0),pmul(d1,d1),pmul(d2,d2))
    dh=[0]
    for coeff,A,B in [(142,d0,d0),(-400,d0,d1),(294,d0,d2),
                      (-143,d1,d1),(112,d1,d2),(1,d2,d2)]:
        dh=padd(dh,pscale(pmul(A,B),coeff))
    return padd(pscale(pmul(k2,dn),25),pscale(dh,256)),dn

ZLO=12847; ZHI=12848; ZDEN=10000
def poly_lower_num(coeffs):
    # z>0, so each monomial z^i is increasing.  This is a rigorous lower
    # bound term by term on [ZLO/ZDEN,ZHI/ZDEN].
    deg=len(coeffs)-1; total=0
    for i,c in enumerate(coeffs):
        if not c: continue
        zz=ZLO if c>0 else ZHI
        total += c*(zz**i)*(ZDEN**(deg-i))
    return total

# Distinct semigroup shifts through depth 15.  Path is irrelevant after one
# output because all modules have the same Q, hence the same polarization at a
# fixed final frequency.
seen={(0,0,0):0}; front={(0,0,0)}
for dep in range(1,16):
    new=set()
    for s in front:
      for l in SHIFTS:
        t=(s[0],s[1]+l[1],s[2]+l[2])
        if t not in seen:
            seen[t]=dep; new.add(t)
    front=new
check(len(seen)==3932,'3932 distinct semigroup shifts through depth 15')

# Only these seed classes have nonzero e1 polarization initially.
ACTIVE={
 'p2':(0,0,1,0),
 'p3':(0,-1,0,1),
 'g2':(1,1,0,-1),
 'g3':(1,-1,0,1),
 'h+':(0,-1,1,1),
 'h-':(0,-1,-1,1),
 'h0':(-2,1,-1,-1),
}
finite_cases=0
for sh,dep in seen.items():
    if dep==0: continue
    for name,(xc,xs,y0,c0) in ACTIVE.items():
        if name=='h0' and dep==1:
            continue # these five intended first outputs synthesize H
        C,dn=cert_poly(xc,xs,y0+sh[1],c0+sh[2])
        if len(dn)==1 and dn[0]==0:
            continue
        finite_cases+=1
        check(poly_lower_num(C)>0,f'{name} depth={dep} shift={sh}: damped')
check(finite_cases==27512,'27512 exact clean-interval damping certificates')

# Universal tail.  Every active seed has initial y+z<=2 and every shift lowers
# y+z by at least 6.  At depth n>=16, y+z<=-94, hence
# |k|^2 >= (y+z)^2/2 >= 4418 > 4224.  Since ||H||op<33/16,
# R_2048 <= 2048*(33/16)-|k|^2 = 4224-|k|^2 <0.
check(sp.Rational(94**2,2)>4224,'all translated states at depth >=16 coercively damped')

# Required-window collision test.  Depth >=3 has y+z<=2-18=-16, whereas every
# clean or intended-purifier window has y+z>=-12, so only depths 1 and 2 need
# exact comparison.  The h0 depth-one hits are precisely the intended outputs.
REQ=[]
for j,l in enumerate(SHIFTS):
    REQ.append((f'pur{j}',(-2,1),-1+l[1],-1+l[2]))
REQ += [('h+',(0,-1),1,1),('h0',(-2,1),-1,-1),('h-',(0,-1),-1,1)]
collision_checks=0
for sh,dep in seen.items():
    if dep not in (1,2): continue
    for name,(xc,xs,y0,c0) in ACTIVE.items():
        yy=y0+sh[1]; cc=c0+sh[2]
        for rname,(rc,rs),ry,rr in REQ:
            if name=='h0' and dep==1 and rname.startswith('pur') and yy==ry and cc==rr:
                continue
            collision_checks+=1
            if yy!=ry or cc!=rr: continue
            aa=xs-rs; bb=xc-rc
            if aa==0:
                check(bb!=0,f'no exact collision {name}->{rname}')
            else:
                check(Qclean.eval(-sp.Rational(bb,aa))!=0,
                      f'no clean-root collision {name}->{rname}')
check(collision_checks==1115,'1115 exact finite required-window collision checks')
check(sp.Rational(-16)<-12,'depth >=3 separated from every required y+z window')

print(f'PASS: {len(CHECKS)} exact assertions.')
print('Five Q=e1, |l|^2=50 modules lie in one Beltrami eigenspace and span Sym_0(3) at the clean root.')
print('The semigroup is pointed; p1, g1 and the full inherited ladder are exactly inactive.')
print(f'All other repeated slow states: {finite_cases} exact finite damping certificates, then a universal coercive tail.')
print(f'Required-window collisions: {collision_checks} exact finite comparisons, then pointed separation.')
print('Scope: leading effective slow Raman lattice; full finite-energy high-sideband NS realization remains open.')
