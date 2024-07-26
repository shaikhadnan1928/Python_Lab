import numpy as np

# Input data
category1_revenue = np.array([500, 600, 700, 550])
category2_revenue = np.array([450, 700, 800, 600])

# Calculate total revenue for each period
total_revenue = category1_revenue + category2_revenue

print("Total Revenue:", total_revenue)

"""
output

Total Revenue: [ 950 1300 1500 1150]
"""
