import matplotlib.pyplot as plt
import numpy as np

'''courses= np.array(["A", "B", "C", "D"])
number_of_students= np.array([5,8,6,10])
colors= ["red", "blue", "green", "purple"]

plt.barh(courses,number_of_students, color= colors,)
plt.show()'''

x=np.random.normal(150,15,250)

plt.hist(x)
plt.show()
