'''
    MODULES IN PYTHON
    => A module in python is just a separate file that contains some reusable code that you want to 
       include in your program.
    => You can use the import keyword to import a module.
    => There are also built in modules in python.



'''

# print(help("modules")) This will help you to get all the modules in python and their uses

# There are 3 ways you can import a module.
# 1. import <<name of module>>
import time

time.sleep(2)

# 2. import <<name of module>> as <<your alias>> 
# This is used to shorten name of module when using it 

import math as m

print(m.pi)
print(m.pow(2,3))

# 3. from <<name of module>> import <<specific attribute or function>> 
# useful when you only need specific attributes to use within your program

from string import ascii_letters, ascii_uppercase

print(ascii_letters, ascii_uppercase)


# You can also create your module.
# Let's create a module called MyModule.
# To do this, create a different python file called MyModule
# Then within this program import MyModule

import MyModule as mm

print(mm.pi)
print(mm.e)
print(mm.cube(3))
print(mm.Area(2))
print(mm.circumference(2))
print(mm.square(4))
