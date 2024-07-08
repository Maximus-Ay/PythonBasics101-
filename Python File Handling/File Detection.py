'''
    FILE DETECTION IN PYTHON
    => To do some file detection, you need to import the os module.
    => File detection is just checking if a file exists
    => 

'''

import os

file_location = "C:\\Users\\Max The Developer\\Documents\\Hello.txt"

if os.path.exists(file_location):
    print("File location exists!")
    if os.path.isfile(file_location): # To check if a file exists or not
        print("This file exist!")
    # if its is a folder
    #if os.path.isdir(file_location):
else:
    print("File location exists!")


