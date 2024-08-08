import pandas as pd
import matplotlib.pyplot as plt

student_data = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
})

grouped_single = student_data.groupby('school_code').agg({'age': ['mean', 'min', 'max']})

print("Mean, min, and max value of age for each school:")
print(grouped_single)

# Generate a horizontal bar chart
plt.figure(figsize=(10,6))
grouped_single.plot(kind='barh', figsize=(10,6))
plt.title('Mean, min, and max value of age for each school')
plt.xlabel('Age')
plt.ylabel('School Code')
plt.show()


"""
Mean, min, and max value of age for each school:
              age        
             mean min max
school_code              
s001         12.5  12  13
s002         13.0  12  14
s003         13.0  13  13
s004         12.0  12  12
<Figure size 1000x600 with 0 Axes>
"""
