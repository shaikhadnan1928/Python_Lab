import numpy as np

# Input list
my_list = [1, 2, 3, 4, 5]

# Convert list to NumPy array
my_array = np.array(my_list)

# Display the array
print("Original array:")
print(my_array)

# Display first and last index
print("First index:", my_array[0])
print("Last index:", my_array[-1])

# Multiply each element by 2
my_array *= 2

# Display the multiplied array
print("\nArray after multiplying by 2:")
print(my_array)

"""
Original array:
[1 2 3 4 5]
First index: 1
Last index: 5

Array after multiplying by 2:
[ 2  4  6  8 10]

"""
