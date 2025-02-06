import numpy as np
from numpy import linalg as LA

c = 0.3
A = np.array([[1.03, 0, -c], [0.1, 0.5, c], [0, 0.5, 0.1]])
x_0 = np.array([3340000, 2100, 1500])

eigvals, eigvecs = LA.eig(A)

P = eigvecs
D = np.diag(eigvals)

A_52 = (P @ D**52 @ LA.inv(P)).round(2)
x_52 = A_52 @ x_0

print(f"A^{52} =\n{A_52}.\n\nA^{52}(x_0) = {x_52}\n\nPopulation = {x_52.sum()}")
