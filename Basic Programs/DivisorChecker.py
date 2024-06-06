'''
    This program checks to see if a number is a divisor of another.
'''

def isDivisor(number, check):
    if number % check == 0:
        return True
    else:
        return False

number = int(input("Enter the number: "))

check = int(input("Enter the number to check: "))

print(isDivisor(number, check))
