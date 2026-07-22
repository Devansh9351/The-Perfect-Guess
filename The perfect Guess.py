import random 
x = random.randint(1,100) 
a = -1
guesses = 1

while(a!=x):
    
    a = int(input("Guess the number: "))

    if(a>x):

        print("Think less: ")
        guesses +=1

    elif(a<x):

        print("Think more: ")
        guesses +=1

print(f"Congrats you found the number: {x} at {guesses} attempts")


