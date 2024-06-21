'''
    A variable is a container that is used to store values. 
    Variables behave as if they are the values themselves. E.g 2 + x = 5. the value of x = 3. Hence x is a 
    variable in this case.
'''

# To declare a variable, you simply need the name of the variable and the value it will contain.

age = 20
print(age) # This will print the variable age. OUTPUT: 20

# There are 4 ways I can print the age variable with other text using the print statement

# Method 1: Using String Concatenation:
print("I am " +str(age) + " years old")

# The above method considers the age to be a string which is just added to all the other strings.
# The str(age) In python is what is called Concatenation, which helps in transforming the age variable, which is
# initially and integer, into a string

# Method 2: Passing it as an argument in the print function
print("I am",age,"years old")

# So here they are separated into different arguments that are passed to the print function.

# Method 3: Using the formatted string method.
print(f"I am {age} years old")

# This method is becoming the most popular method for printing variables.
# It makes use of the aspect of formatted strings in Python which is just placed before the f""
# and then the variable to be displayed is placed within curly braces {age}

# Method 4: Using the format method.
print("I am {} years old".format(age))

# This method is very nice when using several variables.
# It is not very different from formatted strings. Infact they are similar,
# The difference is the use of the format method