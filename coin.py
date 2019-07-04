import random

def coin():
  a = random.randrange(1, 3, 1)
  return(a)

def coin_flip():
    coin_number = input()
    coin_store = []
    while int(coin_number) > len(coin_store):
        coin_store.append(coin())
        if int(coin_number) <= len(coin_store):
            break
    print(coin_store)
