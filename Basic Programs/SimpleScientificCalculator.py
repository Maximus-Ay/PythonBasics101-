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
def Basic():
    pass

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


print("*** WELCOME TO MY BASIC CALCULATOR***")
print("***********      MENU     ***********")

print("1. Basic Mathematical Operations")
print("2. Matrix Operations")
print("3. Vector operations")
print("4. Simultaneous equations with 2 unknowns")
print("5. Simultaneous equations with 3 unknowns")
print("6. Calculation game")
print("7. Quit")

choice = int(input("Enter your choice: "))

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
else:
    option = input("Invalid input do you wish to quit or continue (answer y or n): ")
    if option == "y":
        Quit()
    else:
        choice = int(input("Enter a choice from the menu still: "))


