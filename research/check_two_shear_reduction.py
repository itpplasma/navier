#!/usr/bin/env python3
"""Exact two-transverse-mode reduction of the common purifier energy form.

By adding a controlled antisymmetric rotation to the symmetric trace-free H,
we make the full local gradient rank two. Every rank-two trace-zero matrix is
a sum of two rank-one tensors d_j tensor k_j with d_j.k_j=0. Thus two
transverse sine modes suffice to reproduce the exact symmetric purifier form.
"""
import sympy as sp

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

T=sp.symbols('T', real=True)
rel=sp.Poly(5680000*T**2-708331,T)

def zero_mod(expr):
    num,den=map(sp.factor,sp.together(expr).as_numer_denom())
    rem=sp.rem(sp.Poly(num,T),rel).as_expr()
    return sp.factor(rem)==0

def matrix_zero_mod(M):
    return all(zero_mod(M[i,j]) for i in range(M.rows) for j in range(M.cols))

H=sp.Matrix([
 [sp.Rational(71,100),-1,sp.Rational(147,200)],
 [-1,sp.Rational(-143,200),sp.Rational(7,25)],
 [sp.Rational(147,200),sp.Rational(7,25),sp.Rational(1,200)],
])
check(H==H.T,'H symmetric')
check(sp.trace(H)==0,'H trace free')
check(sp.factor(H.det())==sp.Rational(-708331,8000000),'exact det H')

# A(T) is the cross-product matrix for omega=(T,0,0).
A=sp.Matrix([[0,0,0],[0,0,-T],[0,T,0]])
G=H+A
check((G+G.T)/2==H,'symmetric part of G is exactly H')
check(zero_mod(G.det()),'det G=0 on T^2=708331/5680000')
check(sp.factor(G[:2,:2].det())==sp.Rational(-30153,20000),
      'fixed 2x2 minor nonzero, so rank G=2')

# Rank factorization from the first two columns.
U=G[:,0:2]
ab=sp.simplify(U[0:2,:].inv()*G[0:2,2])
Vt=sp.Matrix([[1,0,ab[0]],[0,1,ab[1]]])
check(matrix_zero_mod(G-U*Vt),'rank-two factorization G=U V^T')

# C=V^T U has trace zero because tr G=0. For any trace-zero 2x2 matrix,
# the basis [e1,C e1] gives zero diagonal by Cayley-Hamilton.
C=sp.simplify(Vt*U)
check(zero_mod(sp.trace(C)),'trace of factor matrix C is zero')
c10=sp.factor(C[1,0])
num_c10=sp.Poly(sp.together(c10).as_numer_denom()[0],T)
check(sp.gcd(num_c10,rel).degree()==0,'chosen basis [e1,C e1] is nondegenerate')

M=sp.Matrix([[1,C[0,0]],[0,C[1,0]]])
U2=sp.simplify(U*M)
Vt2=sp.simplify(M.inv()*Vt)
C2=sp.simplify(Vt2*U2)
check(zero_mod(C2[0,0]),'first transverse dot product zero')
check(zero_mod(C2[1,1]),'second transverse dot product zero')
check(matrix_zero_mod(G-U2*Vt2),'two transverse rank-one terms reconstruct G')

# d_i=u_i/2, k_i=row_i(Vt2). The physical field
# W=sum 2 d_i sin(k_i.x) has grad W(0)=G and sym grad W(0)=H.
for i in range(2):
    d=U2[:,i]/2
    k=Vt2[i,:].T
    check(zero_mod((d.T*k)[0]),f'mode {i+1} transverse')
R=sp.zeros(3)
for i in range(2):
    d=U2[:,i]/2
    k=Vt2[i,:].T
    R += 2*d*k.T
check(matrix_zero_mod(R-G),'two sine gradients reconstruct full G')
check(matrix_zero_mod((R+R.T)/2-H),'two sine gradients have symmetric part H')

print(f'PASS: {len(CHECKS)} exact algebraic assertions.')
print('With T=sqrt(708331/5680000), G=H+[omega]_x has rank two and sym(G)=H.')
print('G is exactly the sum of two transverse sine-mode gradients; two is minimal since det(H)!=0.')
print('Scope: local gradient/energy-form reduction only; nonlinear two-pump coexistence remains open.')
