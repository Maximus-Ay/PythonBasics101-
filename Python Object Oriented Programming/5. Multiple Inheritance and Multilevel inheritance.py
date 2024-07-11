'''
    MULTIPLE INHERITANCE  
    => This is a situation where a class inherits from more than onr parent class
    => C(A, B) This means that C inherits both from A and B parent classes

    MULTILEVEL INHERITANCE
    => This is a situation where the class that acts as a parent class to another class inherits from
       another class which becomes it's parent class.
    => A -> B(A) -> C(B) 
'''

# Let's take the example of Prey and Predator.
# Preys include: Rabbit, Antelope
# Predators include: Lions, Tigers
# Both preys and predators include: Fish, cause a fish can run from bigegr fish like Sharks and 
# hunt smaller fish

class Animal:
    def eat(self):
        print("This animal is eating!")
    
    def sleep(self):
        print("This animal is sleeping!")
class Prey(Animal):
    def Flee(self):
        print("I am a miserable prey, So I am fleeing!")

class Predator(Animal):
    def Hunt(self):
        print("I am a predator, so I am hunting!")

class Lion(Predator):
    pass

class Antelope(Prey):
    pass

class Fish(Predator, Prey):
    pass

lion = Lion()
antelope = Antelope()
fish = Fish()

lion.eat() # This is possible because the lion class inherits from the predator class which
# in turns inherits from the animal class. This is called Multilevel inheritance

fish.Hunt()
fish.Flee()
lion.Hunt()
lion.Flee() # Error, cause Lion has no method flee


