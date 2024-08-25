'''
    This is a simple python program that adds two matrices together.
    Normally a matrix is a two dimwnsional array but in python we don't
    have the array data structure, hence we will use the list data type or structure.
    Note that to add two matrices, they must have the same number of rows and columns, if not it won't be possible to perform such an operation.

'''
 
rows = int(input('Enter number of rows: '))
cols  = int(input('Enter number of column: '))

print() 
print('Enter values for matrix A')

matrix_A = [[int(input(f"Enter element {i+1} for Column {j+1}:")) for j in range(cols)] for i in range(rows) ]  

print()
print('Enter values for matrix B ')

matrix_B = [[int(input(f"Enter element {i+1} for Column {j+1}:")) for j in range(cols)] for i in range(rows) ]  

print() #for new line

print('Matrix-A :')
for i in matrix_A:
    print(i)

print() #for new line

print('Matrix-B :')
for i in matrix_B:
    print(i)

# resultant matrix (matrix that store answer and intially it is Zero)
result = [[0 for j in range(cols)] for i in range(rows)]

# addition
for i in range(rows):
    for j in range(cols):
        result[i][j] = matrix_A[i][j] + matrix_B[i][j]

print() #for new line

print('Addition of Matrix-A and Matrix-B is :')

for i in result:
    print(i)