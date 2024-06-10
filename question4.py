import numpy as np

# Reshape array without changing its data
array_3x2 = np.array([[1, 2], [3, 4], [5, 6]])
reshaped_array_2x3 = np.reshape(array_3x2, (2, 3))
print("\nReshaped array 2x3:")
print(reshaped_array_2x3)
reshaped_array_3x2 = np.reshape(array_3x2, (3, 2))
print("Reshaped array 3x2:")
print(reshaped_array_3x2)
