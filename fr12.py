import matplotlib.pyplot as plt
import numpy as np
'''a= np.array([169,175,148,159,167,180])
b= np.array([49,58,44,51,62,64])
plt.xlabel("Hieght is cms")
plt.ylabel("Weight in kgs")
plt.title("Relationship between wieght and height")
plt.scatter(a,b)
plt.show()'''

population= np.array([35,27,25,13,])
country= np.array(["India","Italy","Sweden","Germany"])
mycolors=["Yellow", "Green", "Red", "Blue"]
myexplode=[0.1,0,0,0]
plt.pie(population, labels= country, colors=mycolors, explode=myexplode)
plt.legend(title="Population Graph", labels= country, loc=2)
plt.show()
