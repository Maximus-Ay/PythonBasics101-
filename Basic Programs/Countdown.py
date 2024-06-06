'''
    This is a basic python program that deals mostly with counting down based on user input.
    It makes use of the loops to be able to do that.
'''



number = int(input("Enter the number the count down should start from: "))

print("Using the while loop: ")

while(number>=0):
    print(number, end = " ")

    number-=1


# another way to achieve this is to use the for loop
print("\nUsing the for loop: ")
for number in range(10, -1, -1):
    print(number, end=" ")

# remember that the range function is exclusive on one side
