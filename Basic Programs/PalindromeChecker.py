'''
    This program checks if an entered String is a Palindrome
    It makes use of functions and the conditional Statements
'''

def isPalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
    
def outputMessage(output):
    if output:
        print("The string is a palindrome")
    else:
        print("The String is not a palindrome")
    

input = input("Enter a String: ")

outputMessage(isPalindrome(input))

