def is_prime(n):
    c=0
    for i in range(2,n//2+1):
        if n%i==0:
            c=1
    if c!=1:
        return n
    else:
        pass 
def factors(n):
    L=[]
    for i in range(1,n+1):
        if n%i==0:
            L.append(i)
    return L
print(factors(90))
print(list(map(is_prime,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])))
            
            
