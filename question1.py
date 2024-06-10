import numpy as np

# Create random vector
random_vector = np.random.randint(1, 21, size=15)
print("Random vector:")
print(random_vector)

# 1. Reshape the array to 3 by 5
reshaped_array = random_vector.reshape(3, 5)
print("\nReshaped array:")

# 2. Print array shape
print(reshaped_array)

# 3. Replace the max in each row by 0
max_indices = np.argmax(reshaped_array, axis=1)
for i, idx in enumerate(max_indices):
    reshaped_array[i, idx] = 0
print("\nArray after replacing max in each row by 0:")
print(reshaped_array)

# Create a 2-dimensional array of size 4 x 3
array_4x3 = np.random.randint(0, 100, size=(4, 3), dtype=np.int32)
print("\nArray of size 4x3:")
print(array_4x3)
print("Shape:", array_4x3.shape)
print("Type:", type(array_4x3))
print("Data type:", array_4x3.dtype)
