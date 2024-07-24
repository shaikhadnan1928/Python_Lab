import numpy as np

# Employee data for full-time employees
full_time_employees = np.array([
    [101, 'John Doe', 'Full-Time', 55000],
    [102, 'Jane Smith', 'Full-Time', 60000],
    [103, 'Mike Johnson', 'Full-Time', 52000]
], dtype=object)

# Employee data for part-time employees
part_time_employees = np.array([
    [201, 'Alice Brown', 'Part-Time', 25000],
    [202, 'Bob Wilson', 'Part-Time', 28000],
    [203, 'Emily Davis', 'Part-Time', 22000]
], dtype=object)

# Combine the data
combined_employees = np.concatenate((full_time_employees, part_time_employees), axis=0)

# Print the combined employee data
print("Combined Employee Data:")
for employee in combined_employees:
    print(f"Employee ID: {employee[0]}, Name: {employee[1]}, Type: {employee[2]}, Salary: {employee[3]}")


"""
OUTPUT
Combined Employee Data:
Employee ID: 101, Name: John Doe, Type: Full-Time, Salary: 55000
Employee ID: 102, Name: Jane Smith, Type: Full-Time, Salary: 60000
Employee ID: 103, Name: Mike Johnson, Type: Full-Time, Salary: 52000
Employee ID: 201, Name: Alice Brown, Type: Part-Time, Salary: 25000
Employee ID: 202, Name: Bob Wilson, Type: Part-Time, Salary: 28000
Employee ID: 203, Name: Emily Davis, Type: Part-Time, Salary: 22000

"""