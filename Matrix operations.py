def add(M1,M2):
    L=[[0]*len(M1[0]) for k in range(len(M1))]
    for i in range(len(L)):
        for j in range(len(L[0])):
            L[i][j]=M1[i][j]+M2[i][j]
    return L
def subtract(M1,M2):
    L=[[0]*len(M1[0]) for k in range(len(M1))]
    for i in range(len(L)):
        for j in range(len(L[0])):
            L[i][j]=M1[i][j]-M2[i][j]
    return L
def sumrow(M):
    L=[]
    for i in range(len(M)):
        sum=0
        for j in range(len(M[0])):
                sum+=M[i][j]
        print("Row "+str(i+1)+":",sum)
M1=[[1,5],[3,2],[1,3]]
M2=[[1,2],[6,2],[3,5]]
print(M1)
print(M2)
print(add(M1,M2))
print(subtract(M1,M2))
sumrow(M1)
sumrow(M2)


                   
