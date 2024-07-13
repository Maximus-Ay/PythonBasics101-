'''
    METHOD OVERRIDING
    Method overriding is the ability for a class use provide its own implementation of a method 
    that it originally inherited from its parent class.
    Hence we cannot have method overriding without first having inheritance.
    Hence a class will use its, own implementation of a method that should normally be inherited and 
    when it does so, it is called method overriding
'''

class Animal:
    def eat(self):
        print("This animal is eating!")

class Rabbit(Animal):
    def eat(self):
        print("This animal is eating carrot!")

rabbit = Rabbit()
rabbit.eat() # In case there is no method in the Rabbit class like eat, it will print (This animal is eating!)
