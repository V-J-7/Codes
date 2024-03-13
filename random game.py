import random
a=random.randint(10,50)
for x in range(5):
    b=int(input("Enter your Guess from a number between 10 to 50:-"))
    if b==a:
        print("You win")
        break
    elif b>a:
        print("Choose a smaller number")
    elif b<a:
        print("Choose a larger number")
    elif b>50:
        print("Invalid choice")
else:
    print("You lose")
print("The answer:-",a)
    
