import matplotlib.pyplot as plt
import numpy as np

x=np.array(["January","February","March","April","May","June","July","August","September","October","November","December"])
y=np.array([1.43,1.53,1.54,1.69,1.84,2.60,2.03,1.73,1.65,1.50,1.45,1.39])
plt.title("Ice cream sales around india every month")
plt.ylabel("Ice cream sales in millions",{"color":"Red","size":15})
plt.xlabel("Months",{"color":"Blue", "size":15})
plt.plot(x,y, marker = ".")
plt.show()
