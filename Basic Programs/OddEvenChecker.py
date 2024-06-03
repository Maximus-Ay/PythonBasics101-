'''
    This program asks the user for an input and determines whether the number is even or odd.
    It makes use of the analogy of conditional statements
'''
def OddEvenChecker(number):
    if number % 2 == 0:
        return True
    else:
        return False

def CheckIfEven(checkValue):
    if checkValue == True:
        print(f"{number} is Even")
    else:
        print(f"{number} is odd")


number = int(input("Enter a number: "))
CheckIfEven(OddEvenChecker(number))





