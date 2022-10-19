import random as rd,sys
print("This is a game of guessing number from 1 to 20 ")
secretNumber=rd.randint(1,20)
guesses=0
while(True):
    yourNumber=int(input("Enter your Number:"))
    if yourNumber==secretNumber:
        print("You are correct ")
        print("Your total guess is " + str(guesses))
        sys.exit()
    elif yourNumber<secretNumber:
        guesses+=1
        print("Your guess is lower than secret Number ")
    else:
        guesses+=1
        print("Your guess is higher than secret Number")
