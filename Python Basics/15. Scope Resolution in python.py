'''
    SCOPE RESOLUTION IN PYTHON
    -> We have variable scope, this is where a variable is visible and accessible within our code
    -> We have also scope resolution, which follows the order:
    LEGB : Local -> Enclosed -> Global -> Built in


'''
# 1) THE LOCAL SCOPE
# Let's create two functions
def Greeting1():
    a = "Hello 1"
    print(a)

def Greeting2():
    b = "Hello 2"
    print(b)

Greeting1()
Greeting2()
 
# Above, a and b are local variables because they are within the functions and cannot 
# be accessed outside of the functions.

# 2) ENCLOSED SCOPE
# This has to deal with a function within another function

def Print1():
    x = 2
    def Print2():
        x = 3
        print(x)
    Print2()

Print1()

# If you run this program like this it will give you 3 as output. But if you remove the x = 3 within print2 
# you will get 2 as output because it is enclosed.

# 3) GLOBAL SCOPE
# When they say that a variable is of global scope, it means that it is not within 
# any function or enclosed scope.
def SayHello():
    Hello = "Hello"
    print(Hello)

Hello = "Say Hello"
SayHello()

# Here it will rather print Hello, because Hello is of local scope, but if you remove the 
# hello that is in SayHEllo function, it will rather print SayHello 

# 4) Built-In
# This is the last in the line, this will only be acceptible if there is no Local, no Enclosed, and no global.

from math import e
e = 4
print(e)
# Rather than printing the e = 2.71.. in mathematics, it prints the e = 4, because it has found a global scope
# However if you remove the e = 4, then it will work