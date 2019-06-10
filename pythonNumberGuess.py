import random

num = random.randint(1,100)
g = 0 # Guesses
x = 0 # Loop Flag

while(x<1):

    try:
        guess = int(input("Guess a number. (1 - 100) \n"))

        if(guess>num):
            print("The number is smaller than " + str(guess) + "\n")
            g += 1
        elif(guess<num):
            print("The number is larger than " + str(guess) + "\n")
            g += 1
        else:
            print("\n " + str(guess) + " is correct! \n You used " + str(g) + " guesses.")
            x += 1

    except:
        print("NaN - Try Again")