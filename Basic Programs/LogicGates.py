'''
    This program is an interactive program that permits me to couple my knowledge of conditional statements
    and loops to represent the different logic gates.
    Here I will be dealing mostly with the AND, OR and NOT gate.

'''
def Choice(choice):
    pass

def And(firstInput, secondInput):
    pass
def Or(firstInput, secondInput):
    pass

def Not(firstInput):
    pass

def Nand(firstInput, secondInput):
    pass

def Nor(firstInput, secondInput):
    pass

def Xor(firstInput, secondInput):
    pass

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







