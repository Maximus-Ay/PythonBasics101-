'''
    DUCK TYPING IN PYTHON
    => Duck typing is another way to achieve polymorphism besides inheritance
    => The simple analogy here is that: if it looks like a duck, and it quacks like a duck, then it must be a duck
    => Objects must have the minimum necessary attributes/methods

'''

class Animal:
    is_alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

# Let's create a class Car that has nothing to do with animals and provide it with the speak 
# method. you will realise that when iterating through the list of cars, it will work, because
# it has the minimum requirement, necessary attribute/method

class Car:
    is_alive = False
    def speak(self):
        print("HONK")


animals = [Cat(), Dog(), Car()]


# Let's try the is_alive class attribute and see if works for Car.
# Originally it will show an error since the Car class has no attribute is_alive
# But if we add the attribute is_alive in the Car class, then it will behave exactly as those animals.
# Hence this is where duck typing comes from, if it looks like a duck, it quacks like a duck, then it is a duck
for animal in animals:
    animal.speak()
    print(animal.is_alive)


