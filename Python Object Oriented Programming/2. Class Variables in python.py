'''
    CLASS VARIABLES IN PYTHON
    => A class variable in python is a variable created within the class, but outside the constructor.
    => They can be accessed by the class directly and are shared among instances or objects
    => For example: when you create an object of the student class, it has its specific attributes 
       but they can have common attributes like graduating_year, rather than accessing it by individual 
       objects, they can be accessed directly

'''

class Students:
    graduating_year = 2024
    num_of_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Students.num_of_students +=1

    
student1 = Students("Maximus", 18)
student2 = Students("John", 16)
student3 = Students("Ronald",18)

# Accessing the class variables
# rather than using the individual objects created, we use the name of the class
print(Students.graduating_year)

print(f"My graduating year of {Students.graduating_year} had {Students.num_of_students} students: ")
print(student1.name)
print(student2.name)
print(student3.name)
