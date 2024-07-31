import matplotlib.pyplot as plt

categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

plt.figure(figsize=(10, 6))
plt.bar(categories, expenses, color=['blue', 'green', 'orange', 'purple', 'red'])
plt.title("Monthly Expenses by Category")
plt.xlabel("Spending Category")
plt.ylabel("Expenses (USD)")

plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

plt.tight_layout()
plt.show()

# Conclusion (based on sample data)
# Rent is the largest expense category, followed by groceries, transportation, utilities, and entertainment. 
# You can adjust this conclusion based on your actual spending data.
print("Conclusion: Rent is the biggest expense category, followed by groceries, transportation, utilities and entertainment.")
