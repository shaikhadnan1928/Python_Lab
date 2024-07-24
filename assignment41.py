import numpy as np

# Define the temperature array, including hypothetical cold days for demonstration
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, 4.0, -4.0, -12.0])

# Find the indices of the days with hot and cold temperature conditions
hot_days_indices = np.where(temperatures > 35)[0]
cold_days_indices = np.where(temperatures < 5)[0]

# Print the results in the specified format
print("Hot Days:")
print("Day\tTemperature (°C)")
for i in hot_days_indices:
    print(f"{i+1}\t{temperatures[i]}")

print("\nCold Days:")
print("Day\tTemperature (°C)")
for i in cold_days_indices:
    print(f"{i+1}\t{temperatures[i]}")
    
    """
    Outputs 
    
   Hot Days:
Day	Temperature (°C)
3	36.8
6	38.7
10	37.2

Cold Days:
Day	 Temperature (°C)
11  	4.0
12 	   -4.0
13	   -12.0




    """
