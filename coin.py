import random

def coin():
    coinFlip = random.randrange(1, 3, 1)
    return(coinFlip)

def coinFlip():
    userChoice = int(input())
    flipResult = []
    for value in range(userChoice):
        flipResult.append(coin())
    print(flipResult)
