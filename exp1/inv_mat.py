import numpy as np

A=np.array([[1, 2],[3, 4]])
det_A=np.linalg.det(A)
# print(det_A)


from sympy import Matrix

A = Matrix([
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
])
A_inv=A.inv_mod(26)
# print(A_inv)

def mod_inverse(a,m):
    r1,r2=a,m
    t1,t2=0,1
    while r2!=0:
        q=r1//r2
        r=r1-q*r2 
        t=t1-q*t2

        r1,r2=r2,r
        t1,t2=t2,t 
    return t1%m
mod_inverse()

