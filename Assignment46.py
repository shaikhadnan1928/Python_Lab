import numpy as np

# Input data
revenue = np.array([10000, 12000, 11000, 10500])
expenses = np.array([4000, 5000, 4500, 4800])

# Calculate profit for each period
profit = revenue - expenses

print("Profit:", profit)

"""
Output

Profit: [6000 7000 6500 5700]

"""
