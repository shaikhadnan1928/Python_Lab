import pandas as pd

# Given data
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
expenses = [500, 200, 1200, 300, 150]

# Create a Pandas Series
expense_series = pd.Series(expenses, index=categories)

print(expense_series)

"""
Groceries          500
Utilities          200
Rent              1200
Transportation     300
Entertainment      150
dtype: int64

"""

print(expense_series['Rent'])

# Output: 1200
