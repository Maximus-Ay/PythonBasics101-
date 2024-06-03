'''
    This program is an interactive program that permits me to couple my knowledge of conditional statements
    and loops to represent the different logic gates.
    Here I will be dealing mostly with the AND, OR and NOT and their variants like the NAND and NOR.
    Also dealing with the XOR gate as well 
    However it deals only with 1 input

'''
def Choice(choice):
    if choice == 1:
        print("{} AND {} = {}".format(firstInput, secondInput, And(firstInput, secondInput)))
    elif choice == 2:
        print("{} OR {} = {}".format(firstInput, secondInput, Or(firstInput, secondInput)))
    elif choice == 4:
        print("{} NAND {} = {}".format(firstInput, secondInput, Nand(firstInput, secondInput)))
    elif choice == 5:
        print("{} NOR {} = {}".format(firstInput, secondInput, Nor(firstInput, secondInput)))
    else:
        print("{} XOR {} = {}".format(firstInput, secondInput, Xor(firstInput, secondInput)))


def And(firstInput, secondInput):
    if firstInput == 1 and secondInput == 1:
        return 1
    else:
        return 0
def Or(firstInput, secondInput):
    if firstInput == 0 and secondInput == 0:
        return 0
    else:
        return 1

def Not(firstInput):
    if firstInput == 0:
        return 1
    else:
        return 0

def Nand(firstInput, secondInput):
    if firstInput == 1 and secondInput == 1:
        return 0
    else:
        return 1

def Nor(firstInput, secondInput):
    if firstInput == 0 and secondInput == 0:
        return 1
    else:
        return 0

def Xor(firstInput, secondInput):
    if (firstInput == 0 and secondInput == 1) or (firstInput == 1 and secondInput == 0):
        return 1
    else:
        return 0

def GoodByMessage():
    print("Thanks for using my application. GoodBye!")




#MAIN 
keepGoing = True

while(keepGoing):
    print("** WELCOME TO THE LOGIC GATE ANALOGY PROGRAM **")
    print("1. AND GATE")
    print("2. OR GATE")
    print("3. NOT GATE")
    print("4. NAND GATE")
    print("5. NOR GATE")
    print("6. XOR GATE")
    print("7. Quit")

    choice = int(input("Make a choice: "))

    if choice == 7:
        GoodByMessage()
    elif choice == 3:
        input = int(input("Enter the input (either 1 or 0): "))
        Not(input)
    elif choice == 1 or choice == 2 or choice == 4 or choice == 5 or choice == 6:
        firstInput = int(input("Enter the first input(either 1 or 0): "))
        secondInput = int(input("Enter the second input(either 1 or 0): "))
        Choice(choice)
    else:
        print("Invalid response! If you want to quit, click on 7.")







