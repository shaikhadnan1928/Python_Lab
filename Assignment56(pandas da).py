import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame
student_data = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'VI', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
})

# Group the data by 'class' and count the number of students
student_count = student_data.groupby('class').size()

# Create the bar chart
student_count.plot(kind='bar')
plt.title('Number of Students per Class')
plt.xlabel('Class')
plt.ylabel('Number of Students')
plt.show()

# Conclusion
print("Conclusion:")
print("The bar chart shows the distribution of students across different classes.")
print("Class VI has the highest number of students, followed by Class V.")

"""
Conclusion:
The bar chart shows the distribution of students across different classes.
Class VI has the highest number of students, followed by Class V.
"""
