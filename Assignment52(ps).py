import pandas as pd

# Given data
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]

# Create a Pandas Series
exam_results = pd.Series(exam_scores, index=students)

print(exam_results)

"""
Alice      92
Bob        88
Charlie    76
David      94
Eve        82
Frank      90
Grace      85
Hannah     89
Ivy        78
Jack       91
dtype: int64

"""

print(exam_results['Alice'])

# Output: 92
