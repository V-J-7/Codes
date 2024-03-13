c=int(input("Enter the number:-"))
p=float(input("Enter the guess:-"))
for x in range(12):
    a=1/2*(p+c/p)
    p=a
    print(p)
