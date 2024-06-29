'''
    SETS IN PYTHON
    => they are also a collection, just as list and tuples.
    => To create a set just set a variable to a set of curly braces.
    => Example:
        Objects = {} # An empty set of objects.
    => They have characteristics that distinguish them from other collections.
        1. They do not accept duplicates.
        2. They are immutable, that is you cannot change the value of a set element when you create a set.
        3. They are unordered, this means that you cannot access them using an index.
    => Sets became ordered as from a certain version of python. But at first it wasn't ordered. The 
       ordered nature of sets is that when printing it multiple times, you get the same values in the same order.
    => It is unordered in the sense that you cannot access them using indexing.
    => You can displat all the attributes and methods of the set you use the dir(name_of_set) method.
    => You can display an in dept information about sets, using the help(name_of_set) method.


'''


setOfFruits = {"banana", "Apple", "Banana"}
print(setOfFruits)
setOfFruits.add("Cocunut") # To add a value.
print(setOfFruits)

# Sets are useful when you are dealing with constants.

# By using the set name and pressing on the dot you get all the list of sets 



