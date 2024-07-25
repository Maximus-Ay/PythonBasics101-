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


'''

from abc import ABC, abstractmethod