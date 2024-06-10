import numpy as np

# Compute the sum of the diagonal element of a given array
array_diagonal = np.array([[0, 1, 2], [3, 4, 5]])
sum_diagonal = np.trace(array_diagonal)
print("\nSum of the diagonal elements:")
print(sum_diagonal)
