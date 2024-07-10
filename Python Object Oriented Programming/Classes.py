class Person:
    def __init__(self, name, height, skin_color, age, isStudent):
        self.name = name
        self.height = height
        self.skin_color = skin_color
        self.age = age
        self.isStudent = isStudent

    def walking(self):
        print(f"{self.name} is currently walkin!")
    
    def eating(self):
        print(f"{self.name} is currently eating!")

    def sleeping(self):
        print(f"{self.name} is currently sleeping!")
        