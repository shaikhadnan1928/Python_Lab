#Write a Python script to concatenate the following dictionaries to create a new one. 
#Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def concatenate_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate dictionaries
result = concatenate_dicts(dic1, dic2, dic3)
print("Expected Result:", result)


"""
============ RESTART: C:/Users/admin/Desktop/github/assignment34.py ============
Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
