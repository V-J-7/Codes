import matplotlib.pyplot as plt
import numpy as np
v=input("Enter the values with spaces:-")
values=v.split(" ")
print(values)
L=sorted(list(set(int(val) for val in values)))
print(L)
heights=[values.count(str(val)) for val in L]
x=input("Enter the value to be plotted on the x axis:-")
y=input("Enter the value to be plotted on the y axis:-")
colormap=plt.cm.get_cmap("inferno")
nrmheights=np.array(heights, dtype=float)/max(heights)
colors=colormap(nrmheights)
plt.bar(L,heights,width=1.0,color=colors)
plt.xlabel(x)
plt.ylabel(y)
plt.show()
