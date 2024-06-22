'''
    To receive input from the user from the console, in python, we use the input() function.
    By default the value obtained from the input function is string.
    So if you want to do some calculations, you will definitely need to type cast it for 
    mathematical calculations.


'''

name = input("Enter your name: ")
age = int(input("Enter your age: ")) # It has been type casted to integer by reason of the fact that the age of someone is always an integer.
hobby = input("Enter your hobby: ")

print(f"Your name is {name} and you are {age} years old and you like {hobby}")





