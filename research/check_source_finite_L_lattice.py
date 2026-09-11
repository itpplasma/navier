#!/usr/bin/env python3
"""Exact finite-L deformation of the four-parent source cage.

This freezes only the source phase/lattice kinematics used by the analytic
finite-horizon persistence theorem.  It is not a whole-space NS proof.
"""
import sympy as s

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

tau,eta=s.symbols('tau eta', real=True)
c=s.Rational(1,20)
uA=s.Rational(9,20)
uB=s.Rational(3,20)
a=1+tau

def parent(u,sgn):
    # Source unrounded phase law at a common fast time, divided by B_s.
    # tau=v/L and eta=(L|g|)^(-1).
    return s.Matrix([c+sgn*u*a,-sgn*u*eta,1])

p1=parent(uA,1)
p2=parent(uA,-1)
p3=parent(uB,1)
p4=parent(uB,-1)

check(s.simplify(p1+p2-p3-p4)==s.zeros(3,1),
      'two source pairs have exactly the same finite-L daughter')
check(s.simplify(p1+p2-s.Matrix([s.Rational(1,10),0,2]))==s.zeros(3,1),
      'common daughter is independent of fast time and transverse phase tilt')
check(s.simplify(p3-(s.Rational(2,3)*p1+s.Rational(1,3)*p2))==s.zeros(3,1),
      'third parent stays in the first-pair span')
check(s.simplify(p4-(s.Rational(1,3)*p1+s.Rational(2,3)*p2))==s.zeros(3,1),
      'fourth parent stays in the first-pair span')

# Frozen cage labels k_(m,z)=((3m-z)/10,0,z).  Put d=x-cz.  The complete
# finite-L unrounded phase lattice is the linear image below.
m,z=s.symbols('m z', integer=True)
k=s.Matrix([(3*m-z)/10,0,z])
d=s.simplify(k[0]-c*z)
Tk=s.Matrix([c*z+a*d,-eta*d,z])
check(s.factor(d-s.Rational(3,20)*(2*m-z))==0,'exact transverse label d')
for mm,p in ((2,p1),(-1,p2),(1,p3),(0,p4)):
    check(s.simplify(Tk.subs({m:mm,z:1})-p)==s.zeros(3,1),
          f'parent m={mm} is image of frozen cage label')

m1,m2,z1,z2=s.symbols('m1 m2 z1 z2', integer=True)
def Tlabel(mm,zz):
    kk=s.Matrix([(3*mm-zz)/10,0,zz])
    dd=s.simplify(kk[0]-c*zz)
    return s.Matrix([c*zz+a*dd,-eta*dd,zz])
check(s.simplify(Tlabel(m1,z1)+Tlabel(m2,z2)-Tlabel(m1+m2,z1+z2))==s.zeros(3,1),
      'finite-L phase lattice is exactly closed under convolution')

# Uniform deformation identities.  On a physical fixed fast-time window,
# tau=O(L^-1) and eta=O(L^-1).
diff=s.simplify(Tk-k)
check(s.simplify(diff-s.Matrix([tau*d,-eta*d,0]))==s.zeros(3,1),
      'finite-L lattice is a homogeneous shear of the reference lattice')
check(s.factor(diff.dot(diff)-d**2*(tau**2+eta**2))==0,
      'exact deformation norm identity')
# |d|=|x-cz| <= sqrt(1+c^2)|k| gives the analytic all-label bound.
check(1+c*c==s.Rational(401,400),'all-label deformation constant squared')

# The two spanning parents remain independent whenever 1+tau != 0.
cross=s.simplify(p1.cross(p2))
cross2=s.factor(cross.dot(cross))
check(s.simplify(cross2-s.Rational(81,40000)*(401*eta**2+400*tau**2+800*tau+400))==0,
      'exact spanning-area formula')
check(s.simplify(cross2.subs(eta,0)-s.Rational(81,100)*(1+tau)**2)==0,
      'reference-plane rank remains two away from tau=-1')

print(f'PASS: {len(CHECKS)} exact assertions.')
print('The four physical unrounded source normals remain on one exact rank-two convolution lattice.')
print('The lattice is a homogeneous O(|tau|+|eta|) shear of the frozen spectral cage.')
print('Scope: phase/lattice kinematics only; the finite-horizon nonlinear persistence proof is analytic.')
