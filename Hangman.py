import random
def indices(L,ele):
    indices=[]
    for i in range(len(L)):
        if L[i]==ele:
            indices.append(i)
    return indices
word_list=["ORANGE","BANANA","APPLE","MANGO","GRAPES","KIWI","PAPAYA","MELON","WATERMELON","PINEAPPLE","BROCOLLI","CAPSICUM",]
word=random.choice(word_list)
revealed_word=[]
list_word=[]
guesses=[]
for i in word:
    list_word.append(i)
    if i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        revealed_word.append(i)
    else:
        revealed_word.append("_")
print(" ".join(revealed_word))
errors=0
while revealed_word!=list_word:
    guess=input("Enter your guess:")
    guesses.append(guess)
    if guess.lower() in list_word or guess.upper() in list_word:
        index=list(set(indices(list_word,guess.upper())))
        for k in range(len(index)):
            revealed_word.insert(index[k],guess.upper())
            revealed_word.pop(index[k]+1)
        print(" ".join(revealed_word))
    elif guess.upper() in revealed_word or guesses.count(guess)>1:
        print("Already guessed")
        print(" ".join(revealed_word))
    elif len(guess)>1 or type(guess)!=str:
        print("Invalid character")
    elif guess.lower() not in list_word or guess.upper() not in list_word:
        errors+=1
        print(errors,"steps closer to death")
        if errors==6:
            print("You dead")
            break
if revealed_word==list_word:
    print("Congrats! You guessed correctly")
else:
    print("Answer was:",word)
    