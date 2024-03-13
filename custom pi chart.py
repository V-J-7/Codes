import matplotlib.pyplot as plt
labels=[]
values=[]
L=[]
while True:
    a=input("Enter the label and the percentage corresponding to it:-")
    L.append(a)
    labels.append(L[0][:-2])
    for i in L:
        while type(i)!=str:
            values.append(i)
    L.clear()
    q=input("Continue(y/n)?")
    if q=="y":
        continue
    elif q=="n":
        break
    else:
        print("Press only y or n")
print(labels)
print(values)
plt.pie(values,labels=labels)
plt.legend(labels=labels,loc="upper left")
plt.axis("equal")
plt.show()
        
    
    
    
