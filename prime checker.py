a=int(input("Enter the number:-"))
count=0
def prime(t):
    global count
    for i in range(1,t//2):
        if t%i==0:
            count+=1
            print(i)
    print(t)
    if count>=1:
        return "composite"
    else:
        return "prime"
print(prime(a))
