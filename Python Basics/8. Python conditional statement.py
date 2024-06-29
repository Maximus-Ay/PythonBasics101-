'''
    => A conditional statement in python is a one line statement for the if else construct. In other programming 
    languages it is known as the ternary operator.
    => Here the outcome of each statements can only be to print or to assign a value, they cannot contain
       more than one line of code.
    => The format is:
                            X if condition else Y
    => X is what will ne done if the condition is true and Y is what will be done if the condition is false.    
'''

# Let's check if a number is even or odd, using the conditional statement in python.

number = 11

print("Number is even") if number % 2 == 0 else print("Number is odd")

# You can englove everything in a print, statement, that will be shorter.

# Let's check if the number is positive

print("Positive" if number > 0 else "Negative")


# You can also assign the answer to a variable.
# Let's say, we want to find the max number of two numbers

firstNumber = 10
secondNumber = 20

maxNumber = firstNumber if firstNumber > secondNumber else secondNumber

print(maxNumber)

# The same logic applies for the minimum number


