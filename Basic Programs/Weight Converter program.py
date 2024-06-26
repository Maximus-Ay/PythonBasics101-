'''
    This is a weight converter program that still makes use of the if statement.
    The user can convert from kilograms to pounds and from pounds to kilograms, 
    depending on what the user is asking for
    Note that 1 pound = 0.454 kilogram.
'''
def ToPounds(weightInKg):
    return weightInKg/0.454

def ToKilograms(weightInPounds):
    return weightInPounds * 0.454

print("This program converts the wwight from pounds to kilograms and from kilograms to pounds")

weight = float(input("Enter your weight in: "))

unit = input("Enter the unit(lbs or kg):  ")

if unit == "lbs":
    print(f"{weight}lbs = {(ToKilograms(weight))}kg")
elif unit == "kg":
    print(f"{weight}kg = {(ToPounds(weight))}lbs")
else: 
    print(f"Error: Incorrect unit {unit}")

