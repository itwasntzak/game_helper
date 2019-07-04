from coin import coin_flip
from dice import dice_roll

def main_menu():
    
    user_choice = ''
    
    while user_choice == '':
        print('hello, what would you like to do?')
        print('options: coin, dice, exit')

        user_choice = str(input())

        if user_choice.lower() == 'coin':
            coin()
            
        elif user_choice.lower() == 'dice':
            dice()
            
        elif user_choice.lower() == 'exit':
            print('good bye')
            break
        else:
            print('INVALID INPUT')
            main_menu()


def coin():
    print('how many coins would you like to flip?')
    coin_flip()
    user_2nd_choice = ''

    while user_2nd_choice == '':
        print('would you like to flip some more? y or n')
        user_2nd_choice = str(input())
            
        if user_2nd_choice.lower() == ('y'):
            coin()
                
        elif user_2nd_choice.lower() == ('n'):
            main_menu()
                
        else:
            print('INVALID INPUT')
            main_menu()

def dice():
    print('how many dice would you like to roll?')
    dice_roll()
    user_2nd_choice = ''

    while user_2nd_choice == '':
        print('would you like to roll some more? y or n')
        user_2nd_choice = str(input())
            
        if user_2nd_choice.lower() == ('y'):
            dice()
                
        elif user_2nd_choice.lower() == ('n'):
            main_menu()
                
        else:
            print('INVALID INPUT')
            main_menu()

main_menu()
