'''
    In this section, we will treat the if statement
    The if statement is for decision making.
    based on "if" a statement is true it does something, if it isn't you can do something else
    the basic if statement is simply a and if with a condition.
    Also we have the if else which does what is in the body of the if, if the condition in the if is correct
    and does what is in the body of the else if that in the if is false.
    We can also check multiple conditions and to do so we use an elif which is shortened as elif in python.
    When using multiple conditions, the order in which the conditions appear matter a lot

'''

print("****Simple if statement***")
print("Let's ask the user to enter their age and let's see if he/she is eligible to go to high school")

age = int(input("Enter your age: "))

if age >= 17:
    print("Congratulations! You can move to High school")


# For the above statement if you are not 17 or above, it does nothing. Hence that is why we have the if else construct

print("\nThe if else statement\n")
age = int(input('Enter your age: '))
if age >= 17:
    print("Congratulations! You can move to High School!")
else:
    print("Sorry you are not of age to move to High School")

print("\nThe if elif else construct to check multiple decisions or choices")

print("\nNow let's check if the person has an A grade assuming that A is from 70, B is from 60 and C is from 50 and anything below that is a fail ")

grade = int(input("Enter the grade mark: "))

if grade >=70:
    print('Congrats! You have an A grade!')
elif grade >=60:
    print('Congrats! You have an B grade!')
elif grade >= 50:
    print('Congrats! You have an C grade!')
else:
    print("Sorry you didn't make it")

# Note here that the order matters a lot, just changing the positions
#  of the different if statements can cause a lot of troube and make the program wrong


# The if statement evaluates the truthfulness of a statement, so when dealing with booleans, you don't need 
# To write something like if variable = True.
# Example:


online = True

if online:
    print("Welcome to another session Man")
else:
    print("Oops you are offline!")

    

