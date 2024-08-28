'''
    POSTIONAL ARGUMENTS
    => Generally the arguments that are passed to a function are positional arguments.
    => That is the position of the argument matters. If you happen to interchange two of them, 
       the output will not be as expected 
'''
# Example
print("Positional arguments")
def Greetings(Name,Faculty, Program, Course):
    print(f"Hello {Name} you are in the {Faculty} faculty in the {Program} program, taking {Course}")

Greetings("Maximus","ICT","Bachelors","Software Engineering")

# Now Let's change the order of the 
Greetings("Maximus", "Bachelors", "Software Engineering", "ICT")


'''
    KEYWORD ARGUMENTS
    => Now with keyword arguments, the position or order is needless.
    => Also if you want to mix both keyword arguments and positional arguemnts, be sure to place the
       keyword arguments before

'''

# Using the same greetings function
print("\nKeyword Arguments")
# Order doesn't matter
Greetings(Program="Bachelors", Name="Maximus", Course="Software Engineering", Faculty="ICT")

# Some built in functions have what we call keyword arguments
print("1", "2", "3", "4", sep="-") # Sep here is a keyword argument

for x in range(1,11):
    print(x, end=" ") # End here is a keyword argument

