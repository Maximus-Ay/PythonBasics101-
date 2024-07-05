'''
    DEFAULT ARGUMENT IN FUNCTIONS FOR PYTHON
    => The dafault parameter is used when a certain argument is obmitted when calling the function.
    => They make your functions more flexible and reduces the number of arguments.
    => E.g if the default age is 12 and you obmit your age when the function is called, then 

'''

# We use default arguments were consistent and not everywhere.
# Imagine you want to start counting, from any number but if the user obmits the start number,
# you start counting from -1
# make sure you place default arguments towards the end of parameters of the function declaration

def count(end, start =-1):
    for number in range(start,end):
        print(number)

print("Start at default value")
count(10) # I have not put the start, hence it will start at -1
print("Start at 4")
count(20, 4) # it is now set to start at 4
