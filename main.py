from coin import coinFlip
from dice import diceRoll


def mainMenu():
    print('hello, what would you like to do?')
    print('options: coin, dice, exit')
    userChoice = str(input())
    if userChoice.lower() == 'coin':
        coin()
    elif userChoice.lower() == 'dice':
        dice()
    elif userChoice.lower() == 'exit':
        print('good bye')
        exit()
    else:
        print('INVALID INPUT')
        return(mainMenu())


def coin():
    print('how many coins would you like to flip?\n(enter a numerical value)')
    coinFlip()
    tryAgain('flip')

def dice():
    print('how many dice would you like to roll?\n(enter a numerical value)')
    diceRoll()
    tryAgain('roll')


def tryAgain(varWord):
    print('would you like to ' + varWord + ' some more? y or n')
    userChoice = str(input())
    if userChoice.lower() == ('y'):
        pass
    elif userChoice.lower() == ('n'):
        mainMenu()
    else:
        print('INVALID INPUT!!!')
        return(tryAgain())

mainMenu()
