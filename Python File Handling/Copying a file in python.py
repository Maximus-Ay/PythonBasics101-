'''
    COPYING A FILE IN PYTHON
    => To copy a file in python, you need to import the Shutil module.
    => There are three types of methods that can handle the copying of a file:
       1) copyfiles() : This copies the content of a file.
       2) copy(): this does the same thing like copyfile() and also includes permission mode and destination directory
       3) copy2(): This copies everything about the file including meta data(its creation and modification date).
                   It does also everything the Copy() does
    => Hence among all of them, the Copy2() sounds to be the more appropriate one.


'''

import shutil

shutil.copyfile('Test1.txt', 'CopyofTest1.txt')

# all of those copy methods make use of 2 arguments, which are:
# the source of the file and its destination. 
# In case the file is in the same directory, you just need the name of the file
# If its not, you will need the file path