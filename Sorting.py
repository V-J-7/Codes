import random
import time
def sort(L):
    L1=[]
    while len(L)>0:
        mn=L[0]
        for i in L:
            if i<mn:
                mn=i
        L.remove(mn)
        L1.append(mn)
    return L1
L=[]
for i in range(200000):
    L.append(random.randint(0,2000))
start=time.time()
print(sort(L))
end=time.time()
print(end-start)
