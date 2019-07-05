import random

def dice():
    diceRoll = random.randrange(1, 7, 1)
    return(diceRoll)

def diceRoll():
    userChoice = int(input())
    rollResult = []
    for value in range(userChoice):
        rollResult.append(dice())
    print(rollResult)
