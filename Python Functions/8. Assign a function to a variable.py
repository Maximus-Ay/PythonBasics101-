'''
    This is a simple tutorial on how to assign a function to a variable

    when you want to assign a function to a variable, what you are assigning is the memory address of that function.
    of that function and not the function itself. And to do that we use write the function without parenthesis
    example: print(), say = print, 
    What happens now is that the say will behave exactly as the print. So everything that the print can do, 
    the say can do as well. 

'''

def Hello():
    print("Hello World!")

Hello() # This will also print Hello World
hi = Hello
hi() # This will print Hello World

print(Hello) # This will print the memory address in which the Hello function is found
print(hi) # This will print the same memory address in which the Hello function is found

say = print
say("Hello I am no longer the print, I am now the say function")

display = print

display("My name is John, I can't believe that this is real!")