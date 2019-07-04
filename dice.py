import random

def dice():
    a = random.randrange(1, 7, 1)
    return(a)

def dice_roll():
    dice_number = input()
    dice_store = []
    while int(dice_number) > len(dice_store):
        dice_store.append(dice())
        if int(dice_number) <= len(dice_store):
            break
    print(dice_store)
