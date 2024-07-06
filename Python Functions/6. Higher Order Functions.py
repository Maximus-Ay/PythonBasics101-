'''
    HIGHER ORDER FUNCTIONS IN PYTHON
    A higher order function is a function that does either of the following
    1. Take a function as an argument.
       Or
    2. Return a function.
    In python function are treated as objects.


'''

# Take a function as an argument
def SmallLetters(text):
    return text.lower()

def CapitalLetters(text):
    return text.upper()

# The higher order function
def Letters(func):
    text = func("Hey Dude")
    print(text)

Letters(SmallLetters)
Letters(CapitalLetters)


# Returning a function
# Let's do some function that returns another function
# Consider the divisor function below

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(5) # Hence here it skips the dividend method and returns dividend

print(divide(10)) # Here it returns whatever the dividend method returns, hence it returns 10/2 = 5
