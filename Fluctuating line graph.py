import matplotlib.pyplot as plt
import numpy as np
import math
L1=[]
L2=[]
L3=[]
for i in range(1,100):
    L1.append(((-1)**(i+1))*i+1)
for j in range(1,100):
    L2.append((-1)**j*j)
def line(n):
    L=[]
    for i in range(1,100):
        L.append(i/n)
    return L
plt.plot(L1,"black",mec="red",mfc="blue")
plt.plot(L2,"red",mec="blue",mfc="red")
for k in range(1,100):
    plt.plot(line((-1)**k),"white")
plt.show()
