import matplotlib.pyplot as plt
import numpy as np
L=[]
a=int(input("Enter the seed:-"))
while a>1:
    if a%2!=0:
        a=3*a+1
        print(a)
    elif a%2==0:
        a=a//2
        print(a)
        L.append(a)
y=np.array(L)
plt.plot(y, marker="o")
plt.show()
