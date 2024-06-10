import numpy as np

# Compute the eigenvalues and right eigenvectors of a given square array
square_array = np.array([[3, -2], [1, 0]])
eigenvalues, eigenvectors = np.linalg.eig(square_array)
print("\nEigenvalues:")
print(eigenvalues)
print("Right eigenvectors:")
print(eigenvectors)
