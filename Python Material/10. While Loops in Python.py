'''
    PYTHON WHILE LOOPS
    
    A while loop is a way of doing something repeatedly until a certain condition is no longer satisfied.
    Hence the while loop is a condition controlled loop.
    As in the definition, a while loop can run infinitely, that is why we have what we call an exit strategy.
    The exit strategy is simply what will permit you to be able to go out of the while loop.
    It usually is the opposite of the condition that made you enter the while loop in the first place.


'''

# Example: Let's asks the user to enter his name
# if he doesn't enter anything we stick him into the loop until he does


name = input("Enter your name: ")

while name == "":
    print("You didn't enter your name!")
    name = input("Enter your name: ")

print(f"Hello {name}")


# Example 2: let's ask the user for his age, 
# if he doesn't enter his age, or give a negative answer he will be stuck in the loop.

age = int(input("Enter your age: "))

while age < 0:
    print("You didn't enter your age dude!")
    age = int(input("Enter your age: "))

print(f"You are {age} years old hahahahah!")




