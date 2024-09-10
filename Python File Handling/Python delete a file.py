'''
    DELETING A FILE IN PYTHON
    => to delete a file in python, you need the os.remove() method from the os module.
    => If a file doesn't exist you will encounter an exception, that's why it's important to use the try except block.
    => So, the best thing to do when deleting files is to use


'''

import os
path = "C:\\Users\\Max The Developer\\Documents\\GitHub\\PythonBasics101-\\Python File Handling\\Test1.txt"
try:
    os.remove(path)
except FileNotFoundError:
    print("File was not found!")


# You can aswell delete directories in python
# Let's create an empty directory

folderPath = "C:\\Users\\Max The Developer\\Documents\\GitHub\\PythonBasics101-\\Empty_folder"

try:
    os.rmdir(folderPath)
except FileNotFoundError:
    print("The folder you want to delete! doesn't exists!")
except PermissionError:
    print("Sorry, you don't have permission to delete this file!")
else:
    print("The folder has been deleted!")

# Note that the rmdir() removes or deletes an empty folder,
# To delete folders that contain files, you import the shutil method.
# But you have to be careful when doing that because, the you may not want to delete some files or folders.
# import shutil
# shutil.rmtree(path) That's the method that does delete a directory and all its contents.