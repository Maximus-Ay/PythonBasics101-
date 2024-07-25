'''
    DECORATORS IN PYTHON
    => a decorator in python is a function that extends the behaviour of another function without 
       modifying the base function
    => pass the base function as an argument to the decorator.
    => 
       @add_sprinkles
       get_ice_cream("Vanilla")

'''
#let's say we want to get an icecream

# The definition of the basic decaorator function, is a nested function that takes in the base function
# as argument.
# If the function is not nested, anytime the decorator is called using the @name_of_decorator function, 
# the implementation of the decorator will be called, where as the decorator aims at extending the behaviour
# of the get_ice_cream() method by adding sprinkles anytime we need ice cream and not when we call the decorator.

def add_sprinkles(base_function):
    def wrapper():
        print("You just added a sprinkles to your ice cream")
        base_function()
    return wrapper

# A I was saying earlier, if you remove the wrapper method, anytime you call the @add_sprinkles decorator
# It will run, whether the get_ice_cream is there or not, hence it completely spoils the essense of using 
# decorator in the first places
#  

@add_sprinkles
def get_ice_cream():
    print("This is your ice cream")

get_ice_cream()


# In the case where I want to add parameters, to the function, I need to include the *args and **kwargs 
# keyword using in the wrapper
'''
ALTERNATIVE CODE
def add_sprinkles(base_function):
    def wrapper(*args, **kwargs):
        print("You just added a sprinkles to your ice cream")
        base_function(*args, **kwargs)
    return wrapper


@add_sprinkles
def get_ice_cream():
    print("This is your ice cream")

get_ice_cream()

'''