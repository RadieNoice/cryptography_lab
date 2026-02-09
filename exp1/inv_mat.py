import numpy as np

A=np.array([[1, 2],[3, 4]])
det_A=np.linalg.det(A)
print(det_A)


from sympy import Matrix

A = Matrix([
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
])
A_inv=A.inv_mod(26)
print(A_inv)

