'''
    The email slicer program simply asks the user to enter his email
    and from the email that he has entered I will be able to know his username and the domain
'''

email = input("Enter your email: ")

index = email.index("@")

username = email[:index]

domain = email[index+1:]

print(f"In the email: {email}:\n" +
 f"=>your username is {username} and \n" +
 f"=>the domain is {domain}")

