'''
    - This program is for a simple calculator that performs the basic arithmetic calculations,
    - That is, Addition, Subtraction, Muliplication and Division. 
    - It makes use of various concepts such as conditional statements for choice of operation
    - Loops that help you to repeat the process as often as you want
    - Functions for modularity
'''

def Addition(firstNumber, secondNumber):
    return firstNumber + secondNumber

def Subtraction(firstNumber, secondNumber):
    return firstNumber - secondNumber

def Multiplication(firstNumber, secondNumber):
    return firstNumber * secondNumber

def Division(firstNumber, secondNumber):
    if secondNumber == 0:
        return "Error: Invalid (Division by 0)"
    else:
        return firstNumber/secondNumber
    
def GoodByeMessage():
    print("Thanks for using my Calculator. Good Bye!")

def Choice(choice):
    if choice == 1:
        print("{} + {} = {}".format(firstNumber, secondNumber, Addition(firstNumber, secondNumber)))
    elif choice == 2:
        print("{} - {} = {}".format(firstNumber, secondNumber, Subtraction(firstNumber, secondNumber)))
    elif choice == 3:
        print("{} x {} = {}".format(firstNumber, secondNumber, Multiplication(firstNumber, secondNumber)))
    elif choice == 4:
        print("{} / {} = {}".format(firstNumber, secondNumber, Division(firstNumber, secondNumber)))
    else:
        print("Thanks for Using my calulator")



# MAIN PROGRAM

print("*** SIMPLE CALCULATOR PROGRAM ***")
print("1. Addition ")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Quit")

choice = int(input("Make a choice: "))

if choice == 5:
    GoodByeMessage()
else:
    firstNumber = int(input("Enter the first number: "))
    secondNumber = int(input("Enter the second number: "))

    Choice(choice)