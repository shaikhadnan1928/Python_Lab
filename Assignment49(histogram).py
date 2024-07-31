import matplotlib.pyplot as plt

days = list(range(1, 32))
temperature = [1,2,3,4,5,6,7,8,9,10,19,18,17,16,15,14,13,12,11,20,21,22,23,24,25,26,27,28,29,30,31]
plt.figure(figsize=(10, 6))
plt.plot(days, temperature)
plt.title("Daily Temperature Variations")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")

plt.grid(True)
plt.show()

# Conclusion 
# The temperature appears to be increasing over the first half of the month, then decreasing in the second half. 
# It's important to note that this is just a small sample dataset, and weather patterns can be much more complex.
print("Conclusion: The temperature appears to be increasing over the first half of the month, then decreasing in the second half. This is just a small sample dataset, and weather patterns can be much more complex.")
