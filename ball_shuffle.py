
# import only system from os -- this is only for executing the Clear screen funtionality
from os import system, name
from time import sleep
#From Random module import shuffle
from random import shuffle
# define our clear function
def clear():
    if name == 'nt':
        _ = system('cls')

#All Function declarations
# 1. to shuffle a list
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

# 2. to get user's choice   
def player_guess():
    #guess = ''
    #while guess not in ['1','2','3','4']:
    guess = input('Pick a number between 1,2,3 or 4 : ')
    return (int(guess) - 1)

# 3. To check if 'O' is found at the position identified by guess
def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print('Correct!')
        print('\n\n')
    else:
        print('Incorrect!')
        print(mylist)
        print('\n\n')

# Initialize list
game_list = [' ','O',' ',' ']
#Shuffle list
mixedup_list = shuffle_list(game_list)
#Get user's guess
user_guess = player_guess() 
#Real game - where the user's guess is matched against the list
clear()
check_guess(mixedup_list,user_guess)