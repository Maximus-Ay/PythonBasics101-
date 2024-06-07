'''
    This program aims at asking the user for the number.
    And it prints all the divisors of that number
'''

number = int(input("Enter a number: "))

print("The divisors of {} include: ".format(number))
for i in range(1,number + 1):
    if number % i == 0:
        print(i ,end=" ")


