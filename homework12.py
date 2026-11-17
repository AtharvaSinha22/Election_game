import matplotlib.pyplot as plt
import numpy as np
Expenses= np.array([25,10,25,15,10,15])
Use= np.array(["rent","entertainment","food","transportation","healthcare","others"])
mycolors= ["Yellow", "Blue", "red", "pink", "orange", "Green"]

plt.pie(Expenses, colors=mycolors)
plt.legend(title= "Expenses graph", labels= Use, loc=1)
plt.show()
