'''
    super(): The super function is a method within the child class that is used to call all the methods
             from the parent class (super class)
             Allows you to extend the functionalities of inherited methods.

    => Let's say that you want to create different shapes, like a circle, square and Triangle.
    => Now all of them should have attributes color and is_filled. 
    => A circle will normally have its radius. a square will have its side, and triangle will have a base and 
       height.
    => If you want to modify the color attribute or is_filled, you will have to modify it all through different
       shapes which might lead you to errors. So this is where inheritance comes in.
    => The square, circle and triangles will all inherit from the Shape, the attributes color and is_filled.
    => Now the parent class will have a constructor for the color and is_filled attributes, 
    => Hence to be able to use that we will need the super method in the child class.
    => Also if the parent class has a method say describe() that describes the shape, we can use method overriding
       to provide our own version for the child for that particular child or extend that functionality
       that is, we will use the parent version of the describe() class and still provide our own version for
       the class.
    => Hence you have to note that, there will be no need of super, if there is no inheritance in the first
       place.
'''
import math
class Shape:
    # Creating the constructor of the parent class
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    # Let's create a method called descibe
    def describe(self):
        print(f"It is {self.color} and is {"Filled" if self.is_filled else "Not filled"}")

    
# Let's create child classes
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        # The super method for using the constructor of the parent class
        super().__init__(color, is_filled)
        self.radius = radius

    # Let's describe our own method for the describe method
    def describe(self):
        # Let's call the describe method for the parent class using the super, then extend it using our own 
        # own definition of the descibe
        super().describe()
        print(f"The circle has an area of {math.pi * pow(self.radius, 2):.2f}cm^2")

class Square(Shape):
    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)
        self.side = side

    def describe(self):
        super().describe()
        print(f"The square has an area of {pow(self.side, 2)}cm^2")

class Triangle(Shape):
    def __init__(self, color, is_filled, base, height):
        super().__init__(color, is_filled)
        self.base = base
        self.height = height

    def describe(self):
        super().describe()
        print(f"The triangle has an area of {self.base * self.height / 2}cm^2")


print("For the circle")
circle = Circle("blue", True, 5)
print(circle.color, circle.radius, circle.is_filled)
circle.describe()
print()
print("For the Square")
square = Square("red", True, 5)
print(square.color, square.side, square.is_filled)
square.describe()
print()
print("For the triangle")
triangle = Triangle("yellow",False, 10, 5)
print(triangle.color, triangle.base, triangle.is_filled, triangle.height)
triangle.describe()
