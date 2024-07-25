'''
    POLYMORPHISM IN PYTHON
    => Polymorphism is word that originates from two greek words called: 
                   Poly = Many
                   Morphe = Forms
    => Hence Polymorphism means to have many forms or faces.
    => Polymorphism can be achieved in python using two concepts:
       1) Inheritance
       2) Duck typing
    => Here we will focus more on inheritance
'''

# HOW POLYMORPHISM IS ACHIEVED USING INHERITANCE
# Let;s say we have a parent class Shape and child classes: Square, Cicrle, Triangle
# when you create a cicle object it acts as both a circle and a shape since it inherits from 
# the Shape class, hence it has two forms and so polymorphism is achieved.


# To demonstrate polymorphism, we need to import the abc module to be able to use abstract methods
from abc import ABC, abstractmethod
from math import pi
class Shape:
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * pow(self.radius, 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return pow(self.side, 2)

class Triangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def area(self):
        return 0.5 * self.height * self.width
    

# Creating a list of shapes

Shapes = [Circle(4), Triangle(3,2), Square(7)]

for shape in Shapes:
    print(f"{shape.area():.2f}cm^2")


