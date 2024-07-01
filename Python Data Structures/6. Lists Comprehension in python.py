'''
    LISTS COMPREHENSION
    => A list comprehension in python is a concise way of creating a list from another existing list or iterable.
    => They are more compact and easier than the traditional loops.
    => They have the formula:
    [expression for value in iterable if condition]
    if condition is if there is a particular condition

'''

# Let's create a list of doubles of a certain range of numbers, using traditional for loops
print("Using traditional for loops")
doubles = []

for x in range(1,5):
    doubles.append(x * 2)

print(doubles)

print("\n Using lists comprehension, let's say doubles from 1 to 10 we can reduce the number of lines of code:\n")

doubles2 = [x * 2 for x in range(1, 11)]

print(doubles2)


print("List of squares: ")

squares = [ x * x for x in range(1,6)]

print(squares)

print("Let's do something with a list of strings:")

fruits = ["Banana", "Apples", "Cherry", "Grapes"]

print(f"Using lists comprehension we can make the list of fruits{fruits}: and we will capitalize each fruit")

capitalisedFruits = [fruit.upper() for fruit in fruits]
print(capitalisedFruits)


# For the if condition, we can use it in the context where we get values only if a condition is satisfied.
# Lets have a list of numbers, that contain both positive and negative numbers, and create two lists
# A list of positive numbers and a list of negative numbers.

numbers = [1,2,3,4,-2,7,-23,-7,87,2,5,-8,1]

positive_numbers = [number for number in numbers if number > 0]

negative_numbers = [number for number in numbers if number < 0]

print(f"From numbers: {numbers}: We have: \n")

print(f"Positive numbers: {positive_numbers}")
print(f"Negative numbers: {negative_numbers}")




