'''
    RANDOM NUMBERS IN PYTHON
    => To generate random numbers in python we will use the random module.
    => we need to import it right at the beginning of our program.
    import random
    => The random module gives us access to a lot of functions that we can use.
'''

import random
# Generate random integers we use randint
number = random.randint(1,10) # Both sides are inclusive
print(number)

# generate a random float from 0 to 1 we use the random method itseld
number = random.random()
print(number)

# Let's say we have a sequence(list, tuple) of choices like rock paper scissors
game = ("rock", "paper", "scissors")

output = random.choice(game)
print(output)

# We can aswell shuffle our list using the shuffle method.
deck_of_cards = ["A", "2", "3", "4", "5", "6", "7", "8", "10", "J", "Q", "K"]
random.shuffle(deck_of_cards)
print(deck_of_cards)
