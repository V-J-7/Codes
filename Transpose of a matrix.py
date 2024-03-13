def transpose(matrix):
    a=len(matrix)
    L=[[0]*a for k in range(len(matrix[0]))]
    print(L)
    for i in range(len(L)):
        for j in range(len(L[0])):
            print(i,j)
            if i==j:
                L[i][j]=matrix[i][j]
            else:
                L[i][j]=matrix[j][i]
    return L
print(transpose([[1,2],[2,3],[2,4],[2,6]]))
a=list(input("Enter:"))
print(transpose(a))

