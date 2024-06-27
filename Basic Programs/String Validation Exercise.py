'''
    Below is an exercise in Python, which will deepen my understanding of Strings
    It is a string validation program, just like for login in and signing up when
    creating accounts for your different websites.
    These are the rules:
    => The username cannot contain more than 12 characters
    => The username must not contain spaces
    => The username must not contain digits
'''

username = input("Enter your username: ")

if len(username) >= 12:
    print(f"Error! {username} is more than 12 characters.")