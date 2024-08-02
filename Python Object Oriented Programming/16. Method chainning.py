'''
    Method chaining is the act of calling multiple methods for the same class sequentially
    All it does is that it executes the method and returns self 
    
'''

class Car:
    def turn_on(self):
        print("You start the engine!")
        # When yoyu call a method in python and nothing is returned, it returns None, 
        # so at the end we need to return self
        return self
    def drive(self):
        print("You are driving!")
        return self

    def brake(self):
        print("You have applied the brakes")
        return self

    def turn_off(self):
        print("You turned off the car!")
        return self
    
car = Car()

#Method chaining looks more like
car.brake().turn_off()

# To call all the methods, you will have to
car.turn_on()\
    .drive()\
    .brake().\
    turn_off()

# The \ is a line continuation character