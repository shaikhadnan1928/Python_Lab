#2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

import numpy as np

# Generate an array from 2 to 10 (excluding 10)
arr = np.arange(2, 11)

# Reshape the array into a 3x3 matrix
matrix = arr.reshape(3, 3)

# Print the matrix
print(matrix)

#output
"""
[[ 2  3  4]
 [ 5  6  7]
 [ 8  9 10]]
"""
