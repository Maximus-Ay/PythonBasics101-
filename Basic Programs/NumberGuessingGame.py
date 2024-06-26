'''
    This is a basic Number Guessing code in Python.
    The user will try to guess the number the machine is thinking of based on 3 attempts.
    If the number generated by the User is higher than that of the computer it simply displays high
    This will help the user to be able to guess the number.

'''
import random

print("Enter the range of guess you want: ")
max = int(input("Enter the max number: "))
min = int(input("Enter the minimum number: "))
attempts = int(input("Enter the number of attempts you want for the guessing: "))

computerValue = random.randint(min, max)
flag = True
while flag == True:
    
    if attempts > 0:
        userGuess = int(input("Enter your guess: "))

        if userGuess > computerValue:
            attempts = attempts - 1
            print("Too High. Try Again! you have {} attempt(s) left".format(attempts))
            
            

        elif userGuess < computerValue:
            attempts = attempts - 1
            print("Too Low. Try Again! you have {} attempt(s) left".format(attempts))
            
        else:
            print("Your guess is right!")
            flag = False
    else:
        print("You failed the game!")
        flag = False
