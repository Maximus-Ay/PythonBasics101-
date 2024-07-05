'''
    ARGS AND KWARGS IN PYTHOn
    *args are used when you want to pass in multiple arguments to a function, that are non key arguments
     What it does is that it all the arguments passed and makes a tuple of them.
    * Kwargs is rather used for multiple keyword arguments

'''

# Example: Imagine you want to add many numbers, and you have to create a function for this.

def Sum(*args):
    sum = 0
    for arg in args:
        sum +=arg
    return sum

print(Sum(1,2,3,4,5))

# You could actually use *nums rather than args, the name matters not, 
# its the number unpacking operator (*) that matters

# Let's do for an unlimited number of names
# 
def displayName(*names):
    for name in names:
        print(name, end=" ")

displayName("Engr.", "Ngoh", "Maximus", "Ayisih") 



# The difference between *args and **kwargs is that 
# 1) args need one unpacking operator (*args) where as kwargs need two (**kwargs) 
# 2) args treat the arguments as tuples, hence every operation that can be carried out on tuples can be 
# carried out in functions with *args, where as kwargs treat the arguments passed in as dictionaries, 
# hence every every operation carried out on dictionaries can be carried out on those arguments. 


# KWARGS
print("\n\nUsing Kwargs\n")
def Student(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

Student(Name = "Maximus",
        Level= 2,
        Semester=2,
        Course="Software Engineering",
        Program="Bachelors",
        )


# Anytime you want to use both kwargs and args in a method or function, make sure the args come before the kwargs
