'''
    Type Casting is the art of converting a variable from one data type to another data type.
    We have 4 data types which are Integers, String, Boolean and Floats.
    Hence, with type casting you can move from one of these data types to another.
    We have two types of casting, that is Implicit casting and Explicit casting

    Explicit type casting occurs when you manually decide to cast it your self, where as implicit 
    type casting is done automatically.

    Below are some examples


'''


name = "Maximus"
age = 18
isStudent = True
gpa = 3.7

# This is Explicit type casting
age = str(age)
print(type(age))

# float to integer
gpa = int(gpa)
print(type(gpa))

# string to boolean
age = bool(age)
print(type(age))

# Now when we say Implicit type casting, that means that the casting is done automatically especially during calculations

age = age /2.5

print(type(age))
# Snce the age has been divided by a a float, the result is a float and hence it has been converted automatically to float

