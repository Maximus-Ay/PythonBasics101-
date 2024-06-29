'''
    PYTHON DICTIONARIES
    => dictionaries in python is one of the four collection types.
    => They are like sets but with key value pairs.
    => A simple dictionary will look like:
    => mydic = {key: value}, Example: think of Countries and Capitals, 
    => Basically anything that is in the form of a pair, you can use a dictionary to store it
    => Also, 
        1. dictionaries are ordered, they can be accessed using their key, using the indexing operator.
        2. They do not accept duplicates.
        3. They are changeable, since the 

'''

theWorld = {"Cameroon":"Yaounde", 
            "USA":"Washington DC", 
            "Nigeria": "Lagos", 
            "Egypt": "Cairo"}
print(theWorld)
# Let me print the capital of Cameroon
print(f"The capital of Cameroon from the dictionary is: {theWorld['Cameroon']}")

# Its always better to display the dictionary on one line.

# dictionaries have a couple of method, by using the dot notation, you can get to it.

print(theWorld.get("Japan")) # It returns the value of the key if the key is found, but returns none if the key doesn't exist

key = "Japan"
if theWorld.get(key):
    print(f"The value of {key} is {theWorld.get(key)}")
else:
    print(f"The key {key} doesn't exist")

# Using the update method, we can add a new key-value pair or update an existing key-value pair into the dictionary

theWorld.update({"Germany":"Berlin"})
print(f"Germany and its capital have been added to the dictionary")
print(theWorld)

# To get the list of keys within a dictionary, you use the keys method.

keys = theWorld.keys()

# You can use the key to display the values of all keys in the dictionary.
for key in keys:
    print(key)

print(f"All the keys within our dictionary include: {keys}")

# We also have the values method.

values = theWorld.values()
for value in values:
    print(value)
print(f"All the keys within our dictionary include: {values}")

# We have the items method that returns a 2D tuple of key values pairs within our program

items = theWorld.items()
print(items)

for key, value in items:
    print(f"{key} : {value}")



