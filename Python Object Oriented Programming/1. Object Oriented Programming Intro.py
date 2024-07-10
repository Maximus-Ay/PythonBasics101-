'''
    PYTHON OBJECT ORIENTED PROGRAMMING
    => An object in python is a bundle that contains variables(attributes) and functions (methods)
       They are basically real world entities e.g. Phone, Cup, Laptop etc
    => A class in python is a blueprint for creating objects. Hence what does this mean, That when I create a 
       class, all what I want any object to have that is attributes and methods, are placed inside the class.
       So any object created at any given point in time has those parameters.

'''

# So to create a class in python, we use the class keyword
class Car:
    # Now we need to create a constructor (a method that is runned immediately anytime an object of a class
    # is created,) 
    # The constructor is created using the dunder which is double underscore.
    # the __init__(self, attribute1, attribute2, ...) helps us create a constructor in python
    # The self indicates the current instance and all the attributes of the object are placed 
    # within the constructor.
    def __init__(self,model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale


# Now let's create objects of the car class
car1 = Car("BMW", 2020, "Grey", False)
car2 = Car("Mercedes Benz", 2024, "Black", True)

print(car1) # This will give you the memory address of the car1 object
# When using the print statement with classes, you can print the individual attributes or you can
# use one print statement, with formatted strings

print(f"Car1 :\nModel: {car1.model}\nYear: {car1.year}\nColor: {car1.color}\nFor Sale: {car1.for_sale}")
print(f"\nCar2 :\nModel: {car2.model}\nYear: {car2.year}\nColor: {car2.color}\nFor Sale: {car2.for_sale}")


# for organisation, you can write your classes in a different python file, and just import them
# I will create the class person in a python file called Classes and import that particular class here, 
# and print its attributes and use their different methods

from Classes import Person

person1 = Person("Maximus", "185cm", "Fair", 20, True)
print(person1.age)
print(person1.height)
person1.eating()
person1.sleeping()
