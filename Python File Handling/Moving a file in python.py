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

#You could as well copy folders
# In the source rather than just using the name of the file, you will need to be able to use the name of the 
# folder and as well for the destination, that's the only major change.
