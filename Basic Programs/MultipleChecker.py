'''
    This program aims at checking if a certain number is a multiple of another.
'''
def isMultiple(number, multiple):
    if multiple % number == 0:
        return True
    else:
        return False


number = int(input("Enter the number: "))

multiple = int(int("Enter the number to check: "))

print(isMultiple(number, ))

