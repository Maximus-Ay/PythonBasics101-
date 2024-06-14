'''
    This program is a simple scientific calculator and will enable me to be able to be able
    to compress all basics of python needed to solve mathematical problems.
    The calculator will begin with a menu and will allows users choose and based on the menu, they
    will perform the different operation based on what the user wants.
    This calculator will perform 
    -> basic mathematical operations, 
    -> operations on Matrices,
    -> Vectors operations,
    -> solving simultaneous equations with two unknowns
    -> Solving simultaneous equations with three unknowns
    -> A small calculation game at the end of it all.
'''

import os
def Basic():
    print("WELCOME TO BASIC MATHEMATICAL OPERATIONS")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Quit")

    choice = int(input("Enter your choice: "))
    if choice == 6:
        print("Thanks for using my calculator")
    elif choice ==1 or choice ==2 or choice ==3 or choice ==4 or choice ==5:
        firstNumber = int(input("Enter the first number: "))
        secondNumber = int(input("Enter the first number: "))
        if choice == 1:
            print("{} + {} = {}".format(firstNumber, secondNumber, firstNumber + secondNumber))
        elif choice == 2:
            print("{} - {} = {}".format(firstNumber, secondNumber, firstNumber - secondNumber))
        elif choice == 3:
            print("{} x {} = {}".format(firstNumber, secondNumber, firstNumber * secondNumber))
        elif choice == 4:
            print("{} / {} = {}".format(firstNumber, secondNumber, firstNumber / secondNumber))
        elif choice == 5:
            print("{} mod {} = {}".format(firstNumber, secondNumber, firstNumber % secondNumber))
    else:
        print("Invalid choice") 
        

def Matrix():
    pass

def Vector():
    pass

def SimulWithTwoUnknowns():
    pass

def SimulWithThreeUnknowns():
    pass

def calculationGame():
    pass

def Quit():
    print("Thanks for using my calculator!")

def mainMenu():
    print("*** WELCOME TO MY BASIC CALCULATOR***")
    print("***********      MENU     ***********")

    print("1. Basic Mathematical Operations")
    print("2. Matrix Operations")
    print("3. Vector operations")
    print("4. Simultaneous equations with 2 unknowns")
    print("5. Simultaneous equations with 3 unknowns")
    print("6. Calculation game")
    print("7. Quit")

def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


while True:
    # Screen is cleared if the menu is loaded again.
    clearScreen()
    mainMenu()

    choice = int(input("Enter your choice: "))
    # after selecting the choice, the screen is cleared as well
    clearScreen()

    

    if choice == 1:
        Basic()
    elif choice == 2:
        Matrix()
    elif choice == 3:
        Vector()
    elif choice == 4:
        SimulWithTwoUnknowns()
    elif choice == 5:
        SimulWithThreeUnknowns()
    elif choice == 6:
        calculationGame()
    elif choice == 7:
        Quit()
        break
    else:
        option = input("Invalid input do you wish to quit or continue (answer y or n): ")
        if option == "y":
            Quit()
            break


