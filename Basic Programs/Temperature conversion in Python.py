'''
    This is a temperature conversion program 
    It converts the temperature from Fahrenheit to Celcius and vice versa
    depending on the unit the user enters.
'''

def ToCelcius(tempInFahrenheit):
    return round((tempInFahrenheit-32) * 5 / 9, 2)
 
def ToFahrenheit(tempInCelcius):
    return round((9*tempInCelcius)/5 + 32, 2)

print("This program converts the wwight from pounds to kilograms and from kilograms to pounds")

unit = input("Is the temperature in Fahrenheit or celcius (F or C):  ")

temperature = float(input("Enter your temperature in: "))


if unit == "F":
    print(f"{temperature}F = {(ToCelcius(temperature))}C")
elif unit == "C":
    print(f"{temperature}F = {(ToFahrenheit(temperature))}F")
else: 
    print(f"{unit} is an invalid unit of measurement")

