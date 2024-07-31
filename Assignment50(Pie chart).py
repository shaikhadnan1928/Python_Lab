import matplotlib.pyplot as plt

# Income sources and their corresponding monthly income
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

# Create a pie chart
plt.pie(monthly_income, labels=income_sources, autopct="%1.1f%%")
plt.title("Distribution of Monthly Income by Source")
plt.show()

# Analyze the pie chart
salary_percentage = (monthly_income[0] / sum(monthly_income)) * 100
freelance_percentage = (monthly_income[1] / sum(monthly_income)) * 100
investment_percentage = (monthly_income[2] / sum(monthly_income)) * 100
rental_percentage = (monthly_income[3] / sum(monthly_income)) * 100
other_percentage = (monthly_income[4] / sum(monthly_income)) * 100

print("Analysis of Monthly Income Distribution:")
print(f"Salary contributes {salary_percentage:.1f}% to the total income.")
print(f"Freelance work contributes {freelance_percentage:.1f}% to the total income.")
print(f"Investments contribute {investment_percentage:.1f}% to the total income.")
print(f"Rental income contributes {rental_percentage:.1f}% to the total income.")
print(f"Other sources contribute {other_percentage:.1f}% to the total income.")

# You can add further analysis here based on your income distribution.
# For example, if your income heavily relies on salary, you might consider strategies to diversify your income streams.

"""Analysis of Monthly Income Distribution:
Salary contributes 58.8% to the total income.
Freelance work contributes 17.6% to the total income.
Investments contribute 11.8% to the total income.
Rental income contributes 7.1% to the total income.
Other sources contribute 4.7% to the total income."""