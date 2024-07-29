import numpy as np
from scipy.optimize import linprog

# Example problem: minimize c^T x subject to Ax <= b
c = np.array([1, 2, 3])
A = np.array([[1, 1, 0], [0, 2, 1], [1, 0, 1]])
b = np.array([4, 5, 6])

# Solve the problem
result = linprog(c, A_ub=A, b_ub=b, method='highs')

# Output results
print('Optimal value:', result.fun)
print('Optimal solution:', result.x)
