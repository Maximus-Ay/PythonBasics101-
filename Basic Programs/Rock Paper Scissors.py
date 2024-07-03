'''
    ROCK PAPER SCISSORS GAME 
    => This will help you improve your knowledge on using Random module in python
    Rules:
    The computer picks a choice,
   ,The user picks his choice,
    if you have a rock and the computer has a scissors, you win!
    if you have a scissors and the computer has a paper, you win!
    if you have a paper and the computer has a rock, you win!
    otherwise you loose
    We want the user to play as many times as possible until he says that he is tired of playing

'''
import random
options = ("Rock", "Paper", "Scissors")
running = True
while running:

    userInput = None
    computer = random.choice(options)

    while userInput not in  options:
        userInput = input("Enter a choice: (Rock, Paper, Scissors): ")

    print(f"You: {userInput}")
    print(f"Computer: {computer}")

    if userInput == computer:
        print("Its a tie!")
    elif userInput == "Rock" and computer =="Scissors":
        print("You Win!")
    elif userInput == "Scissors" and computer =="Paper":
        print("You Win!")
    elif userInput == "Paper" and computer =="Rock":
        print("You Win!")
    else:
        print("You Loose!")

    quit = input("Play again? (y/n): ").lower()
    if not quit == "y":
        running == False

print("Thanks for playing the game!")


