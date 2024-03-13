def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
L=[]
a=int(input("Enter the number till which the sequence will be printed:-"))
for i in range(1,a):
    L.append(fib(i))
print(L)