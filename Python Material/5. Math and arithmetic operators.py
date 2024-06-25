'''
    Here we are going to see some functions in Mathematical module of python
    we have the 4 basic:
    Addition : +
    Subtraction: -
    Multiplication: *
    Division: /

    Others include the:
    Modulus : % 
    Exponent: **


'''

print("**********PYTHON MATHEMATICAL OPERATORS******************")
number = 12

# number = number + 1 # Increment number by 1
number += 1 # Shortened form to increment number by 1. Augmented increment

print(number)  # At this level, Output = 13

# number = number - 1 # reduce number by 1
number -= 1 # Shortened form to reducing number by 1.

print(number) # At this level, Output = 12

# number = number * 2 # multiply number by 2
number *= 2 # Shortened form

print(number) # At this level, Output = 24

# number = number / 3 # divide number by 3
number /= 3 # Shortened form 

print(number) # At this level, Output = 8

# number = number % 4 # finds  number by 4
number %= 4 # Shortened form 

print(number) # At this level the answer is 0

number = number ** 2 # number raised to the power 2
number **= 2 # Shortened form 

print(number) # At this level the answer is still 0


'''
    In python, we have built in mathematical functions: Some of them include:
    round() => this function rounds any decimal or floating point number to the nearest integer whole number.
    max() => This method or function finds the maximum number of a list of numbers.
    min() => This method or function finds the minimum number of a list of numbers.
    abs() => it finds the absolute value of a given number. Which is the nearest whole number distance from 0 of that number.
    pow() => Finds the result of a number raised to a certain power. Hence it takes two arguments

'''

print("\n********BUILT IN PYTHON MATH FUNCTION**********\n")
x = 3.1415
y = -5
z = 8

print(round(x)) # Output is 3
print(max(x,y,z)) # Output: 8
print(min(x,y,z)) # Output: -5
print(abs(y)) # Output: 5
print(pow(2,4)) # Output: 16


print("\n **********USEFUL MATHEMATICAL FUNCTIONS ***********\n")

# To use mathematical functions, you can make use of the math module.

import math

# By just pressing math.something, you get all the mathematical functions that exist in python.
# Some include:

print(math.sqrt(64)) # Finding the squared root of a number
print(math.pi) # constant pi
print(math.e) # The exponential constant
print(math.ceil(4.6)) # Rounds a number up no matter the decimal point
print(math.floor(4.6)) # Rounds a number down no matter the decimal number









