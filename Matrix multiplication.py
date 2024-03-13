def multi(M1,M2):
    L=[[0]*len(M1) for b in range(len(M2))]
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M2)):
                L[i][j]+=M1[i][k]*M2[k][j]
    return L
M1=[[1,2],[1,2]]
M2=[[1,2],[1,2]]
print(multi(M1,M2))
        
