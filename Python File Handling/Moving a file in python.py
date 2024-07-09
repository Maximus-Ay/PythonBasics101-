'''
    MOVING A FILE IN PYTHOn
    => To move files in python you will need to import the os module, that is included in the python standard library
    => 

'''

import os

source = "C:\\Users\\Max The Developer\\Documents\\GitHub\\PythonBasics101-\\CopyofTest1.txt"
destination = "C:\\Users\\Max The Developer\\Desktop\\CopyOfTest1.txt"

try:
    # Let's do some file detection
    if os.path.exists(destination):
        print("There is already a file there!")
    else:
        print("File Was moved succesfully!")
except FileNotFoundError:
    print(source+" was not found!")
