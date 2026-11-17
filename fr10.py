import matplotlib.pyplot as plt
import numpy as np

x=np.array([28,31,43])
y=np.array([13,19,44])

plt.xlabel("x axis",{"color":"Blue", "size":50, "family":"serif"})
plt.ylabel("y axis",{"color":"Red", "size":50, "family":"serif"})
plt.title("Cars and thier sales per year")


plt.plot(x,"b*--")
plt.plot(y, color="Red", linestyle = ":", linewidth=7, marker= "+")

plt.show()
    
