import matplotlib.pyplot as plt

# Sample data
x = [0, 5, 9, 10, 15, 20, 25]
y = [0, 1, 2, 3, 4, 5, 6]

# Create the line plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Line Plot')

# Show the plot
plt.show()
