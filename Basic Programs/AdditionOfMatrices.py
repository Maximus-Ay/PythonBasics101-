'''
    This is a simple python program that adds two matrices together.
    Normally a matrix is a two dimwnsional array but in python we don't
    have the array data structure, hence we will use the list data type or structure.
    Note that to add two matrices, they must have the same number of rows and columns

'''

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
matrix1 = []
matrix2 = []
resultMatrix = []

print("Enter the values of matrix 1 by row: \n")
for i in range(rows):
    for j in range (columns):
        matrix1[i][j] = int(input("Enter the values of row "+str(i+1)+": "))

print("Enter the values of matrix 2 by row: ")
for i in range(0,rows+1):
    for j in range (0, columns+1):
        matrix2[i][j] = int(input("Enter the values of row "+i+": "))
    
for i in range(rows):
    for j in range(columns):
        resultMatrix[i][j] = matrix1[i][j] + matrix2[i][j]

print("Matrix 1 is: ")
for i in range(rows):
    for j in range(columns):
        print(matrix1[i][j], end="\t")

print("Matrix 2 is: ")
for i in range(rows):
    for j in range(columns):
        print(matrix2[i][j], end="\t")

print("The Addition of Both Matrices is: ")
for i in range(rows):
    for j in range(columns):
        print(resultMatrix[i][j], end="\t")