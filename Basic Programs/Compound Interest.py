'''
    THIS IS A SIMPLE COMPOUND INTEREST CODE
    => Compound Interest is calculated as:
    A = P((1 + r/100) ^t)
    Where 
    A = is what we are calculating
    P = principal amount
    r = interest rate
    t = time

    => You will prompt the user to enter an amount until he does


'''

principal= 0
rate = 0
time = 0 # in years

while principal <=0:
    principal = float(input("Enter an initial amount: "))
    if principal <=0:
        print("Principal amount cannot be less than or equal to 0")

while rate <=0:
    rate = float(input("Enter the interest rate: "))
    if rate <=0:
        print("The interest rate cannot be less than or equal to 0")

while time <=0:
    time = float(input("Enter the time in years: "))
    if time <=0:
        print("The time cannot be less than or equal to 0")


Amount = principal * pow(1 + rate/100, time)

print(f" Your compound interest for the principal of ${principal} with rate {rate} over a period of {time} years is: ${Amount}")




