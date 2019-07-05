import random

def coin():
    coinFlip = random.randrange(1, 3, 1)
    return(coinFlip)

def coinFlip():
    userChoice = int(input())
    flipResult = [coin() for value in range(userChoice)]
    print(flipResult)
