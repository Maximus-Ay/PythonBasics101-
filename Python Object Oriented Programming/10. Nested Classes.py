'''
    A Nested Class in python, is simply a class that is found within another class
    The format is
        class A:
            class B:
            
    Nested classes are important because they encapsulate data pretty much better and reduces
    possibility of naming conflicts, and also keep the namespaces clean.
    They encapsulate, private details that aren't necessary for the outer class.
    They help in grouping classes that are closely related.
'''
# since in python we deal with a lot of importing and exporting data or files,
# nested classes found their importance, because some classes may have the same names.

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position
        
        def get_details(self):
            return f"{self.name} {self.position}"
    
    def __init__(self, company_name):
        self.company_name = company_name
        self.employess = []

    def add_employees(self, name, position):
        new_employee = self.Employee(name, position)
        self.employess.append(new_employee)

    def list_employess(self):
        return [employee.get_details() for employee in self.employess]
    

company1 = Company("Kaldor Zane")
company2 = Company("Pearson Specter Litt")

company1.add_employees("Robert Zane", "Managing Partner")
company2.add_employees("Harvey Specter", "Managing partner")
company2.add_employees("Donna Pulsen", "COO")
company2.add_employees("Rachel Zane", "Paralegal")

print(company1.company_name)
print(company1.list_employess())
print(company2.list_employess())




