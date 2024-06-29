'''
    NESTED LOOPS IN PYTHON
    => This is a loop inside another loop
    => format: 
            outer loop:
                inner loop:
                    # Inner loop code

    => Anytime you go out of the inner loop the condition of the outer loop is checked and if still satisfied, 
    => continues the execution of the inner loop.
    => For example if you want to print numbers from 1 to 5, 5 times you will not copy and paste 5 for loops for it.
    => You can just nest it within another loop, where 
    => The outer loop is for the 5 times and the inner loop is to print the numbers from 1 to 5
'''
 # This will print from one to 5 six times
for i in range(1,7): # Outer loop
    for j in range(1,6): # Inner Loop
        print(j, end=" ")
    print() # This print statement is to skip a lign at the end of every iteration of the outer loop


# Let's print a rectangle based on user's input

print("\n LET DRAW A RECTANGLE USING THE NESTED FOR LOOPS!")

rows = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol for printing the rectangle: ")

for x in range(rows):
    for y in range(column):
        print(symbol, end="")
    print()



