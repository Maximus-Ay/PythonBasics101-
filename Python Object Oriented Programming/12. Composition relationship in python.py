'''
    A composition relationship is one in which we have a two objects or classes, where one owns the others
    Hence when trying to mimic this, we create the attributes of the other classes inside the constructor
    of the class that owns it.

    Difference between Aggregation and Composition
    Aggregation = "has-a", hence if the object who has is deleted, then the other objects will still exist,
                   hence objects are independent.

    Composition = "owns-a", hence if the objects who owns is deleted, then the other objects will stop existing,
                   hence they are dependent.

'''

# Like a House has several rooms, and if the house is deleted, the rooms will seize to exist
class House:
    def __init__(self, name, type_of_room, room_size, num_of_rooms):
        self.name = name
        self.num_of_rooms = num_of_rooms
        self.room = Room(type_of_room, room_size)
    
    def display_House_Details(self):
        return f"{self.name},{self.num_of_rooms}, {self.room.size}, {self.room.type}"

class Room:
    def __init__(self, type, size):
        self.type = type
        self.size = size

my_house = House(name="Residence Kolly", type_of_room= "studio",room_size=200, num_of_rooms=5)
print(my_house.display_House_Details())




