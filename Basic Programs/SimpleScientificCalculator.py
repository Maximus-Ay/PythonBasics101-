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
    while True:
        print("Welcome to simultaneous equations with two unknowns, (say x and y)")
        print("Getting input from equation 1.....")
        a = int(input("Please enter the coefficient of x in equation 1: "))
        b = int(input("Please enter the coefficient of y in equation 1: "))
        e = int(input("Enter the constant term in equation 1 (on the RHS): "))

        print("Getting input for the equation 2....")
        c = int(input("Please enter the coefficient of x in equation 2: "))
        d = int(input("Please enter the coefficient of y in equation 2: "))
        f = int(input("Enter the constant term in equation 2 (on the RHS): "))

        print("{}x + {}y = {}----------(1)".format(a,b,c))
        print("{}x + {}y = {}----------(2)".format(d,e,f))

        # To solve this equations we will use Cramers Rule

        determinant = (a*d)-(b*c)
        xdeterminant = (e*d)-(f*b)
        ydeterminant = (a*f) - (c*e)

        x = xdeterminant/determinant
        y = ydeterminant/determinant

        print("Solution to the simultaneous equation is x = {} and y = {}".format(x,y))

        userinput = input("Do you wish to continue (y or n): ")

        if userinput == "y":
            clearScreen()
        else:
            break


def SimulWithThreeUnknowns():
    while True:
        print("Welcome to simultaneous equations with three unknowns, (say x, y and z)")
        print("Getting input from equation 1.....")
        a = int(input("Please enter the coefficient of x in equation 1: "))
        b = int(input("Please enter the coefficient of y in equation 1: "))
        c = int(input("Please Enter the coefficient of z in equation 1: "))
        j = int(input("Enter the constant term in equation 1 (on the RHS): "))

        print("Getting input for the equation 2....")
        d = int(input("Please enter the coefficient of x in equation 2: "))
        e = int(input("Please enter the coefficient of y in equation 2: "))
        f = int(input("Please enter the coefficient of z in equation 2: "))
        k = int(input("Enter the constant term in equation 2 (on the RHS): "))

        print("Getting input for the equation 3....")
        g = int(input("Please enter the coefficient of x in equation 3: "))
        h = int(input("Please enter the coefficient of y in equation 3: "))
        i = int(input("Please enter the coefficient of z in equation 3: "))
        l = int(input("Enter the constant term in equation 3 (on the RHS): "))

        print("{}x + {}y + {}z = {}----------(1)".format(a,b,c,j))
        print("{}x + {}y + {}z = {}----------(2)".format(d,e,f,k))
        print("{}x + {}y + {}z = {}----------(3)".format(g,h,i,l))


        # To solve this equations we will use Cramers Rule

        determinant = a*((e*i)  - (h*f)) - b*((d*i) - (g*f)) + c*((d*h) - (e*g))
        xdeterminant = j*((e*i) - (h*f)) - b*((k*i) - (l*f)) + c*((k*h) - (e*l))
        ydeterminant = a*((k*i) - (l*f)) - j*((d*i) - (g*f)) + c*((d*l) - (k*g))
        zdeterminant = a*((e*l) - (k*h)) - b*((d*l) - (g*k)) + j*((d*h) - (e*g))

        x = xdeterminant/determinant
        y = ydeterminant/determinant
        z = zdeterminant/determinant

        print("Solution to the simultaneous equation is x = {}, y = {} and z = {}".format(x,y,z))

        userinput = input("Do you wish to continue (y or n): ")

        if userinput == "y":
            clearScreen()
        else:
            break

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


