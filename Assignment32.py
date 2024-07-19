#Write a Python program to get the largest and smallest number from a list without builtin functions.

def get_largest_and_smallest(lst):
    if not lst:  # Check if the list is empty
        return None, None

    largest = lst[0]
    smallest = lst[0]

    for num in lst:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest

# Example usage
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
largest, smallest = get_largest_and_smallest(numbers)
print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)

"""
============ RESTART: C:/Users/admin/Desktop/github/Assignment32.py ============
The largest number in the list is: 9
The smallest number in the list is: 1

"""
