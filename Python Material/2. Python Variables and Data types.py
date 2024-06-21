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


'''
##########################################
######  DATA TYPES IN PYTHON##############
##########################################
'''

# In python, we basically have 4 data types.
#1. INTEGERS: These are whole numbers e.g age, jersey number, quantity etc 
age = 20
jerseyNumber = 12

print(f"My age is {age} and my Jersey number is {jerseyNumber}")

# 2. FLOAT: These are numbers that contain decimal values. 
price = 2.99
gpa = 3.7

print(f"My Gpa is {gpa} and the price of my spotofy account is ${price}")

#3. STRINGS: These are simply a series of characters that are enclosed in quotation marks.

name = "Maximus"
course = "Software Engineering"

print(f"My name is {name} and I am a Student of {course} at the Birla Institute of Technology in India")

#4. BOOLEAN: These are data types that can have only two values. True or False. They are mostly used in
# conditional statements
isOnline = True
isAvailable = False
print(f"is Maximus Online? {isOnline}")

# Note that for booleans their values always start with Capital, and you don't need to put them in quotes
# as python interpreter alreasy knows it is dealing with a Boolean. 