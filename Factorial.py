def ab():
    a=int(input("Enter the number:-"))
    for x in range(a-1,1,-1):
        if a!=0:
            a=a*x
    print("Factorial:-",a)
while True:
    ab()
