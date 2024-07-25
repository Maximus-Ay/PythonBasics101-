'''
    ABSTRACT CLASSES
    => Abstract classes are classes that cannot be instantiated on their own
    => They contain abstract methods
    => They are meant to be subclassed, means they are supposed to be parents to children classes
    => Abstract methods are only declared but have no implementation
    => abstract classes is important because it prevents the instantiation of classes by themselves, that 
       is you cannot create an object from an abstract class and requires children to use their 
       inherited abstract methods.
    => To start dealing with abstract classes in python we need to use the abc module which is 
       short form for abc = Abstract base class, we could equally import abstract method too
    => When a class inherits from the abstract class, that contains abstract methods, it must provide an 
       implementation for all those methods.


'''

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("The area of the circle is null")


class Triangle(Shape):
    def area(self):
        print("This is the area of the triangle")

triangle = Triangle()
circle = Circle()

circle.area()
triangle.area()

