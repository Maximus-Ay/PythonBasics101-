'''
    LOGICAL OPERATORS IN PYTHON

    We are going to do logical operators in python.
    => Logical operators are used in conditional statements. Most especially in if statements
    => In python we have 3 types:
        1) => The and: This logical operator checks if two or more statements are true. 
        2) => The or: This logical operator checks if at least one statement is true.
        3) => the not: It changes the truthfulness of a statement. That is turns True to False and False to true.

'''

# Simple code that gives the grade of a student based on his mark.
# To keep it simple we will just have 3 grades : A, B, C and D
# A is between 80 and 100, B is between 60 and 79, C is between 40 and 59, everything else is you didn't make it.


# Let's get user input

mark = int(input('Enter the mark: '))

if mark >=80 and mark <=100:
    print("Congrats You have an A!")
elif mark >= 60 and mark<=79:
    print("Congrats you have a B!")
elif mark >= 40 and mark<=59:
    print("Congrats you have a C grade!")
else:
    print("Try again next time, you didn't make it")

# This simply demonstrates the use of the and operator, both of expressions must be true for it to function.


