'''
    PYTHON TUPLES
    => They are one of the collections besides list and sets.
    => They are declared by using parenthesis:
    => Example: 
        name_of_tuple = () # This is an empty tuple
    => Onike other collections,
        1. Tuples are ordered, That is you can access them using indexing.
        2. They are immutable, that is unchangeable, its values cannot be changes after being created.
        3. They can contain duplicates as well.
        4. They are faster than list
    => They do not have many methods as the other collections.

'''

fruits = ("banana", "apple", "banana", "cherry", "grapes")
print(fruits)
print(f"The length of the fruits is: {len(fruits)}")
# They have only 2 methods, which are

# Count: which counts the number of occurence of an element.

print(f"The number of occurences of banana in fruits is {fruits.count("banana")}")

# We also have index, which gives us the index of the first occurence of an element within a tuple

print(f"The first occurence of the element banana in the tuple of fruits is {fruits.index("banana")}")
print("\n\n")
print(type(fruits))
print("\n\n")
print(dir(fruits))
print("\n\n")
print(help(fruits))





