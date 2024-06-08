'''
    This program checks if an entered String is a Palindrome
    It makes use of functions and the conditional Statements
'''

def isPalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
    

input = int(input("Enter a String: "))