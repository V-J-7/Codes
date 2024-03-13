def AB():
    a=int(input("Enter the number to be verified:-"))
    b=int(input("Enter the divisibility check number:-"))
    c=a%b
    if c==0:
        print("Divisible")
    if c!=0:
        print("Not divisible")
    while c==0 or 1:
        AB()
AB()
