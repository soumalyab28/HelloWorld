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
num = random.randint(10,50)

flag = 101
guess_cnt = 0
guess_prev = 0
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
    guess_cnt+= 1
    if guess < 0 or guess > 50:
        print("Out of Bounds.. Please enter a number between 1 and 50 ")
        flag = 101

    elif guess == num:
        if guess_cnt == 1:
            print("WOW Congratulations! It's a MATCH. You have guessed it in FIRST attempt itself.")
        else:
            print("Congratulations! It's a MATCH. You have guessed it in "+str(guess_cnt)+" attempts")
        break

    if (abs(num - guess) <= 5):
            if guess_cnt == 1:
                print("WARM")              
            elif guess_cnt > 1:
                if guess < guess_prev:
                    print("COLDER")
                elif guess > guess_prev:
                    print("WARMER")
    elif (abs(num - guess) > 5):
            if guess_cnt == 1:
                print("COLD")
            elif guess_cnt > 1:
                if guess < guess_prev:
                    print("COLDER")
                elif guess > guess_prev:
                    print("WARMER")
    guess_prev = guess


# Alternate soluation using Lists
# Hint: zero is a good placeholder value. It's useful because it evaluates to "False".
# So we create a list with just 0 element in it
 guesses = [0]
 while True:

     # we can copy the code from above to take an input
     guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
   
     if guess < 1 or guess > 100:
         print('OUT OF BOUNDS! Please try again: ')
         continue
   
     # here we compare the player's guess to our number
     if guess == num:
         print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
         break
       
     # if guess is incorrect, add guess to the list
     guesses.append(guess)
   
     # when testing the first guess, guesses[-2]==0, which evaluates to False
     # and brings us down to the second section
   
     if guesses[-2]:  
         if abs(num-guess) < abs(num-guesses[-2]):
             print('WARMER!')
         else:
             print('COLDER!')
  
     else:
         if abs(num-guess) <= 10:
             print('WARM!')
         else:
             print('COLD!')