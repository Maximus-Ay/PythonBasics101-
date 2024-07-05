'''
    PYTHON FUNCTIONS
    => A function is a block of reusable code
    => To Create one, you use the def keyword, followed by the name of your function, then 
       indent it and write the code that it has to perform.
    => Example:
        def HelloWorld():
            // piece of code it executes

'''
# Declaring and defining a function

def HelloWorld():
    print('Hello World!')

# Calling the function
HelloWorld()
HelloWorld()

# Now when calling the function, you can pass it variables known as arguments.
# But when you are defining it to write the code it will execute, they are known as parameters

def Greetings(name): # name is a parameter
    print(f"Hello {name}")

Greetings("Bro") # Bro here is an argument

# You can pass a function many arguments and let the parameters match the number of arguments passed.

def GreetingsPro(name, age):
    print(f"Hello {name}, you are {age} years old")

GreetingsPro("Maximus", 18)


# Now you can return a value using the return keyword when using functions.
# Most at times you will need to store the return value in a variable. 

# let's write a function that returns the addition of two numbers
def Addition(num1, num2):
    return num1 + num2

sum = Addition(10,12)
print(sum)
