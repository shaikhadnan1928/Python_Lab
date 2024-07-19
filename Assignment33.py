# Write a Python program and calculate the mean of the below dictionary.
#test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}
#Output: 6.2
def calculate_mean(d):
    total = 0
    count = 0

    for key in d:
        total += d[key]
        count += 1

    mean = total / count
    return mean

# Example usage
test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}
mean_value = calculate_mean(test_dict)
print("The mean of the values in the dictionary is:", mean_value)

"""============ RESTART: C:/Users/admin/Desktop/github/Assignment33.py ============
The mean of the values in the dictionary is: 6.2"""
