import random
total=0
def dice(sides,throws):
    for i in range(throws):
        a=random.randint(1,sides)
        print("You got a",a)
        global total
        total+=a
    return "Total of the rolls:-",total
t=int(input("Enter the number of throws:-"))
s=int(input("Enter the number of sides:-"))
print(dice(s,t))