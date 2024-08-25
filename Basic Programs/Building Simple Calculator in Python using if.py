'''
    Here we are going to make use of the concepts of python conditional statements to be able to make a simple calculator, that is using the if statement to be more specific 
    where the user enters the operators and the calculation is performed.
'''

operator = input("Enter the operator: + - * /:  ")

firstNumber = float(input("Enter the first number: "))
secondNumber = float(input("Enter the second number: "))

if operator == "+":
    result = firstNumber + secondNumber
    print(f"{firstNumber} + {secondNumber} = {round(result, 2)}")
elif operator == "-":
    result = firstNumber - secondNumber
    print(f"{firstNumber} - {secondNumber} = {round(result, 2)}")
elif operator == "*":
    result = firstNumber * secondNumber
    print(f"{firstNumber} * {secondNumber} = {round(result, 2)}")
elif operator == "/":
    result = firstNumber / secondNumber
    print(f"{firstNumber} / {secondNumber} = {round(result, 2)}")
else:
    print(f"Error! Invalid operator: {operator}")