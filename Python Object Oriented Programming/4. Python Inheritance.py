'''
    INHERITANCE IN PYTHON
    => Python inheritance is in concept in OOP in python that allows a class to inherit the methods 
       and attributes from another class. e.g a child inherits attributes from his parent.
    => In python it will be represented as class Child(Parent):
    => This means that everything that the parent can do, the child can do as well
    => It helps in code reusability and extensibility

    => The child class is the class that inherits, where as the Parent class is the class from which 
       attributes and methods are inherited.
    => The child class can also be referred to as the sub class and the Parent class, the super class


'''

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating!")
    
    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def make_sound(self):
        print("WOO WOO!")

class Cat(Animal):
    def make_sound(self):
        print("MEOW MEOW!")

class Mouse(Animal):
    def make_sounds(self):
        print("SQUICK SQUICK!")


dog = Dog("Max")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

dog.eat()
print(dog.is_alive)
dog.sleep()
dog.make_sound()



