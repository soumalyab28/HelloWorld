
# import only system from os -- this is only for executing the Clear screen funtionality
import random
from os import system, name
from time import sleep
#From Random module import shuffle
# define our clear function
def clear():
    if name == 'nt':
        _ = system('cls')
#Call the randint method from the random package and randomly select a number between 1 and 50 
#And assign it to num variable
num = random.randint(1,50)

flag = 101
guess_cnt = 1
print(num)

print("\n")
print("----------------------------------------------------")
print("----------------- WELCOME TO GUESSING NAME----------")
print("----------------------------------------------------")
print("\n")
print("--------- RULES----------")
print("You have to guess a number between 1 and 50")
print("If your guess is more than 5 away from my number, I'll tell you you're COLD")
print("If your guess is within 5 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
print("\n")


while flag == 101:
    guess = int(input("Please guess a number between 1 and 50 :   "))
    guess_prev = guess
    if guess < 0 or guess > 50:
        print("Out of Bounds.. Please enter a number between 1 and 50 ")
        flag = 101

    elif guess == num:
        if guess_cnt == 1:
            print("WOW Congratulations! It's a MATCH. You have guessed it in FIRST attempt itself.")
        else:
            print("Congratulations! It's a MATCH. You have guessed it in "+str(guess_cnt)+" attempts")
        flag = 102
    
    if num > guess:
        if ((num - guess) <= 5):
            if guess_cnt == 1:
                print("WARMER")
                guess_cnt+= 1
            elif guess_cnt > 1:
                if guess < guess_prev:
                    print("COLDER")
                    guess_cnt+= 1
                elif guess > guess_prev:
                    print("WARMER")
                    guess_cnt+= 1
        elif ((num - guess) > 5):
            if guess_cnt == 1:
                print("COLDER")
                guess_cnt+= 1
            elif guess_cnt > 1:
                if guess > guess_prev:
                    print("WARMER")
                    guess_cnt+=1
                elif guess < guess_prev:
                    print("COLDER")
                    guess_cnt+= 1

    


    


