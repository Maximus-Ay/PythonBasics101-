'''
    This has to do with passing objects as arguments
    In python you can pass an object as an argument.
    
'''

class Car:
    color = None

class Motorcycle:
    color = None

def change_color(vehicle, color):
    vehicle.color = color # This simply means that the object color which is a class variable will change 
                      # to the color that is passed in as the argument/parameter to the function

# Let's create car objects
car_1 = Car()
car_2 = Car()
bike_1 = Motorcycle()
# Before
print(car_1.color)
print(bike_1.color)

change_color(car_1, "red")
change_color(bike_1, "Yellow")
# After
print(car_1.color)
print(bike_1.color)



