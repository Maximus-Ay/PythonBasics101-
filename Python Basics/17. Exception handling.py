'''
    EXCEPTION HANDLING
    => An exception is an event that occurs during the execution of a program that troubles the 
       flow of a program
    => Like for example, dividing a number by 0
    => A simple exception is handled by using the try except block.
    => The try block will attempt to do run the code that you talked of and if an error occurs 
       it moves to the except section, but its is not good practice to use just one except for all exceptions
       cause, what might be halting the program may be a particular error and another error manifested that
       should not stop the program.



'''

# Using a simple try except block
try:
    number = float(input("Enter a number: "))
    number_to_divide_by = float(input("Enter the number to divide by: "))
    result = number/number_to_divide_by

#except Exception:
    #print("Something went wrong")
# So rather than using the conventional except Exception: you have to specify the type of error.
# Some error include: ZeroDivisionError: When a number is divided by 0
# Other include: ValueError: when you attempt to divide a number by a non number

except ZeroDivisionError:
    print("You cannot divide by zero! :(")
except ValueError as e:
    print(e)
    print("You cannot divide by a non value idiot!")
#except Exception: # For all exceptions that we know nothing about
#    print("Something went wrong!")

# an additional way is to use the except Exception as e: then print(e)
# You can use the else at the end of a program.
# The try will check if there is an exception, the except handles the exception, and the else does the code
# Let's say we print the result at the end
else:
    print(result)