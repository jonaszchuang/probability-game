from random import random, randint
print("In this game, the computer will pick a random number from 1-100 and you can guess the number in some ammount of tries.")
again = True
win = False
turns = 0
number = randint(1, 100)
while win == False:
    print("Turn(s):")
    print(turns)
    turns += 1
    i = int(input("Pick a number from 1-100: "))
    if i < number:
        print("The number is higher, guess again.")
    elif i > number:
        print("The number is lower, guess again.")
    else:
        print("You guessed the number!")