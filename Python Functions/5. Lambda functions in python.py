'''
    LAMBDA FUNCTIONS:
    => A lambda function is a function that has only one expression, that is performs only one action.
    => It's some kind of function short cut and reduces the line of code, cause it occupies just 
       one line of code.
    => It accepts any number of arguments but performs only one action.
    => it is useful if needed for a short period of time, then It can be trashed or thrown away.
    => Its format is:
      lambda parameters: expression

'''

# Imagine this double function
def double(x):
    return x * 2

print(double(4))

# Now to write it as a lambda function it goes as follows
double = lambda x: x*2
print(double(2))

# let's say we want to add three numbers together
addition = lambda x,y,z: x + y + z
print(addition(12,13,14))

# print full name
fullname = lambda firstname, lastname: firstname + " " + lastname
print(fullname("Ngoh", "Maximus"))
# Check age
AgeCheck = lambda age: True if age>18 else False
print(AgeCheck(20))


