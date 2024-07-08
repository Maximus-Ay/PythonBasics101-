'''
    READING A FILE IN PYTHON
    basically to read a file in python, you need only two lines of code
    # Case 1: When the file is in the same directory
    with open('name_of_file.txt') as file:
        print(file.read())
    # Case 2: When the file is in a different directory
    with open('path of file') as file:
        print(file.read())
'''

# Let's read the Test1.txt I created
# I tried using open('Test1.txt) and it didn't work

with open("C:\\Users\\Max The Developer\\Documents\\GitHub\\PythonBasics101-\\Python File Handling\\Test1.txt") as file:
    print(file.read())

# print(file.closed) To check if the file is closed.
# with the with open() you close the file automatically after openning it

# But here, we don't handle errors. Cause in case the file is not found, this will stop the flow of the program
# SO when dealing with files, it is very important to use the try except for exception handling
print("\nThis is with the try except block:\n")
try:
    with open("Test1.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("Something went wrong, File doesn't exist")
except Exception as e:
    print(e)
finally:
    print("I just used the try except!")

