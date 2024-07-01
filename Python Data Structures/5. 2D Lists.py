'''
    PYTHON 2D LIST
    => A 2D list is a list that contains other lists.
    => It is pretty good when you want to create an excel sheet or a matrix
    => You can place lists within lists.
    => To access the individual elements, you will have to note that all the list within the main list
       contribute the rows and the individual list items are the columns.
       Hence to access the individual elements themselves, you will need two squared brackests
       list[rows][columns]

'''

individualSports = ["Tennis", "Boxing", "Wrestling", "Golf"]
collectiveSports = ["Basketball", "Football", "Handball"]

Sports = [individualSports, collectiveSports]

print(f"My list of Sports is {Sports}")

# Rather than separating them you could as well just declare sports and put the individual list themselves

Sports2 = [["Tennis", "Boxing", "Wrestling", "Golf"],
           ["Basketball", "Football", "Handball"]]

print(f"The first element of Sports is {Sports2[0][0]}")
print(f"I can have two different list here: which are {Sports[0]} and {Sports2[1]}")


# To iterate through the list, you can use two for loops
# if you use one for loop you will iterate through the rows, which are the individual lists
print("\nAll the lists within our 2D lists are: \n")
for collection in Sports2:
    print(collection)


# Iterating each element will require that we use two for loops
print("\nPrinting each individual element in the list we have\n")
for collection in Sports2:
    for element in collection:
        print(element, end=" ")
    print()


# You could make a lists of tuples, a lists of sets, a lists of dictionaries basically all other collection, you can make a list of .
