'''
    PYTHON STRINGS INTRODUCTIOn
    => Strings in python are just a series of characters.
    => They can be used to represent people's names and things like that as well as they
       can contain a mixture of text and numbers
    => You can declare a string by using " " quotation marks
'''
print("PYTHON STRINGS INTRODUCTION\n")
# Example declaring an empty string
name = " "
print(name)

# This is a string

hobby = "Basketball"
print(hobby)

# It can also contain a mixture of letters and characters.
password = "TheTrue@234%290!"

print(f"Your password is {password}")

'''
    PYTHON STRING METHODS
    => They are a whole lot of python string methods. 
    => Some of them can be gotten by just pressing a dot, after the name of your string variable.
    => But we will just do a few.
    => To actually know all the string methods, you can use the help(str) method and it will give 
       you all the methods and their functions.
'''

print("\nPYTHON STRING METHODS\n")

name = "johnathan David"
# To get the length of a string, you use the length method.
print(f"The length of the string {name} is {len(name)}") # It returns an integer.

# To get the number of occurence of a certain character in the string, you use the count() method.
print(f"The number of occurence of the letter a in {name} is: {name.count("a")}") # Returns and integer

# To find the index of the first occurence of a certain character, you make use of the find() method.
print(f"The first occurence of the letter h in {name} is {name.find("h")}") # note that indexing in strings starts at 0

# You can replace a string in python with another one, using the replace() method.
print(f"In {name} if I replace all the h with o I get: {name.replace("h", "o")}")

# If you want to capitalize all the letters in the name you use the capitalize method.
print(f"Before: {name} => After: {name.upper()}")

# If you want to lower case all the letters in the name you use the capitalize method.
print(f"Before: {name} => After: {name.lower()}")

# To capitalize only the first character, you use the capitalise method.
print(f"before: {name} => After: {name.capitalize()}")

# To check if the string contains only alpha characters, you use the isalpha() method
print(f"Does the string {name} contain only Alphabetical characters: {name.isalpha()}")
# It will give false because there is an empty string because we are separating the two names.

# To check if all the characters within the string are digits we use the isdigit() method. It return True or False
number = "123456789"
print(f"Is {name} a digit string? {name.isdigit()}") # False
print(f"is {number} a digit string? {number.isdigit()}") # True
print(f"Is name Alpha numberic: {password.isalnum()}") # For alpha Numeric characters

# The above methods is just but a few. There are a whole lot of them. 
# To get all the string methods that exists in python, you need to use the help method
# and the name of the data type, which is string.

print(help(str))


