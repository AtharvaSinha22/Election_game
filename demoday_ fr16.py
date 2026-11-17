import numpy as np 
import matplotlib.pyplot as plt 

quarters = ['Q1', 'Q2', 'Q3', 'Q4'] 
sales_data = np.array([90, 120, 80, 140])  


plt.bar(quarters, sales_data) #ploting bar
plt.xlabel('Quarter')
plt.ylabel('Sales Performance')
plt.title('Sales Performance by each Quarter')
plt.show()

x = 90


y =  100 #np.polyfit fits the data within a polynomial function
slope, intercept = y

new_quarter = 5 #the new quater would be quarter 5
predicted_sales = (slope* new_quarter) + intercept
print('Predicted sales for Quarter:', predicted_sales)


 
