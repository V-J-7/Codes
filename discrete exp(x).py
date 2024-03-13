import matplotlib.pyplot as plt
import numpy as np
import math
L=[ ]
for i in range(1,1000):
    a=math.exp(i/100)
    L.append(a)
    y=np.array(L)
plt.plot(y, marker="o")
plt.show()

