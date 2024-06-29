'''
        PYTHON FOR LOOP
    => A for loop is the best loop to use when you know the number of times you want to execute a particular
       piece of code.
    => You can iterate over a range, over a string, sequence etc.
    => The simple for loop has a syntax of 
              for counter in range(start, end, step):
                    # Code to be executed.
    => The range function helps you to do the action the number of times required and it has 3 parameters.
    => The start is where it begins and it is inclusive, just like the indexing operator.
    => The end is where it ends and it is exclusive just like the indexing operator.
    => The step is the number of times you will skip for the next iteration.
    => To reverse the movement of the range, you can use the reversed method over the range.

'''

# Let's print numbers from one to 10 using a for loop

for x in range(1,11):
    print(x, end=" ")

# Here the end method is used to print all the 
# numbers on a single line, since the print skips a line for all of them.
# As we said to print from 1 to 10, te end needs to be 11, since the end is exclusive.


# So print in reverse all we do is
print("\nReverse the printing: ")
for x in reversed(range(1,11)):
    print(x, end=" ")


# You can also iterate through strings.

myName = "Maximus"
print("\nLet's print each letter in Maximus separately using a for loop: ")
for x in myName:
    print(x, end="")

print("\nMy name reversed is: ")
for x in reversed(myName):
    print(x, end="")


# Making use of the step, we have, 
print("\nLet's print from 1 to 20 in steps of 3: \n")
for x in range(1,21,3):
    print(x, end=" ")


# So while using for loops in python, there are two important keyword sthat could be used with them.
# => They are the continue and the break statement
# => The difference between the break and the continue statement is that,
# => The break completely stops the loop or breaks out of the loop, even if the number of iterations are not done
# => Whereas the continue just skips an iteration based on a certain condition.

# Example: Demonstrating the difference between the Break and continue with the same code
# 1. Continue:
print("\nContinue")
for x in range(1, 11):
    if x == 5:
        continue
    else:
        print(x, end=" ")


# 2. Break
print("\nBreak")
for x in range(1, 11):
    if x == 5:
        break
    else:
        print(x, end=" ")












