'''
    - This program is for a simple calculator that performs the basic arithmetic calculations,
    - That is, Addition, Subtraction, Muliplication and Division. 
    - It makes use of various concepts such as conditional statements for choice of operation
    - Loops that help you to repeat the process as often as you want
    - Functions for modularity
'''
# Addition function
def Addition(firstNumber, secondNumber):
    return firstNumber + secondNumber

# Subtraction function
def Subtraction(firstNumber, secondNumber):
    return firstNumber - secondNumber

# Multiplication function
def Multiplication(firstNumber, secondNumber):
    return firstNumber * secondNumber

# Division function
def Division(firstNumber, secondNumber):
    if secondNumber == 0:
        return f"{RED} Error: Invalid (Division by 0){RESET}"
    else:
        return firstNumber/secondNumber
    
# Goodbye Message
def GoodByeMessage():
    print(f"{GREEN}Thanks for using my Calculator. Good Bye!{RESET}")

# Choice Method
def Choice(choice):
    if choice == 1:
        print("{} {} + {} = {} {}".format(GREEN, firstNumber, secondNumber, Addition(firstNumber, secondNumber), RESET))
    elif choice == 2:
        print("{} {} - {} = {} {}".format(GREEN, firstNumber, secondNumber, Subtraction(firstNumber, secondNumber), RESET))
    elif choice == 3:
        print("{} {} x {} = {} {}".format(GREEN, firstNumber, secondNumber, Multiplication(firstNumber, secondNumber), RESET))
    elif choice == 4:
        print("{} {} / {} = {} {}".format(GREEN, firstNumber, secondNumber, Division(firstNumber, secondNumber), RESET))
    else:
        print(f"{GREEN}Thanks for Using my calulator{RESET}")



# MAIN PROGRAM
GREEN = "\033[32m" #ANSI COLOR CODE FOR TERMINAL
RED = "\033[31m"
RESET = "\033[0m" # RESET TO DEFAULT COLOR
CYAN = "\033[36m"
MAGENTA = "\033[35m" 
YELLOW = "\033[33m"

exitCalculator = True
while (exitCalculator):
    print(f"{MAGENTA}*** SIMPLE CALCULATOR PROGRAM ***")
    print(f"{CYAN}\t1. Addition ")
    print("\t2. Subtraction")
    print("\t3. Multiplication")
    print("\t4. Division")
    print(f"\t5. Exit{RESET}")

    choice = int(input(f"{YELLOW}Make a choice: "))

    if choice == 5:
        GoodByeMessage()
        exitCalculator = False
    elif choice == 1 or choice == 2 or choice == 3 or choice == 4:
        firstNumber = int(input("Enter the first number: "))
        secondNumber = int(input("Enter the second number: "))
        Choice(choice)
    else:
        print(f"{RED}Invalid response. If you want to quit choose option 5!{RESET}")

