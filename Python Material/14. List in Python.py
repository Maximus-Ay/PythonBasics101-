'''
    LIST IN PYTHON
    => List are a what we call in python collections.
    => collections are a single "variable" that can store multiple values.
    => Other collections include: tuple, sets and dictionaries.
    => Here we will focus on lists in python
    => To declare a list, you simply 
        name_of_list = []
    => Your list items are placed within the squared brackets.
    => Some characteristics of list is that:
        1. They are ordered.
        2. They are changeable.
        3. They can contain duplicates.
    => Some of this characteristics, distinguishes it from other collections.
    => You can iterate over a list.
    => You can use the indexing operator to go through the elements of a list.
    => To get all the properties of a list, you use the dir() function. dir(name_of_list)
    => Also to get a more detailed properties of the list, you can use the help(name_of_list) function
    => We will treat all the aspects of the list below.


'''

# Let's create a list of cars

Cars = ["BMW", "Mercedes Benz", "Toyota Yaris", "KIA", "MacLauren", "Bugatti", "Lamborghini", "JEEP"]

# One function we could use is the len() to get the length of the list.
print(f"List of Cars: {Cars}")
print(f"The length of the list of cars is: {len(Cars)}")

# Now we can decide to index the elements in the list of cars.

print(f"The second element in the list of Cars is {Cars[1]}")

# Now we can get a range using sicing.

print(f"The 3rd to the 5th element of the list of Cars is {Cars[2:6]}")

# Note that the slicing rule follows all the rules of the indexing operator.

# You could as well iterate through the list:
# It is a convention that when you create a list, the name of the list is pluralised. Like a list of cars, 
# You name it Cars, a list of books, you name it Books. 
# Now when iterating, using a for loop, you name the counter as the singular of the list name. So 
# to iterate through the list of cars and print all its values, you simply say for car in Cars.

for car in Cars:
    print(car, end=" , ")

# This is read as for every car in the List of Cars, print that car.

# List are ordered and changeable and duplicates are okay.

# List are ordered, that is why you can get the value of an element of a list at a particular index.

Names = ["Maximus", "Rafael", "Neves", "Georgio"]

print(f"Because the lists are ordered, I can get the name of at index 3 which is {Names[2]}")

# When we say list are changeable, that means that you can change the element of a list at a particular index.

print(f"Before: {Names}")

Names[0] = "Ronaldinho"

print(f"After: {Names}")

