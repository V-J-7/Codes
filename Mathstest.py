import random
count=0
for x in range(10):
    a=print("Add these numbers:-")
    b=random.randint(0,1000)
    c=random.randint(0,1000)
    print(b,"\n",c)
    e=int(input("Enter the answer:-"))
    if e==b+c:
        print("Correct")
        count+=1
    if e!=b+c:
        print("Incorrect")
print("Congratulations! You got",count,"out of 10 marks")

        
