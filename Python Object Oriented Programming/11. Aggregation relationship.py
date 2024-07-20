'''
    An agregation relationship in python is one of the type "has-a" between one or more objects, that can
    exist independently of each other.
    Example: A library contains books, but a book can exist without a library and library can exist without
    books.
'''

class Library:
    def __init__(self, name):
        self.name = name
        self.new_book = []

    def add_books(self, book):
        self.new_book.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.new_book]



class Books:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    
my_library = Library("ICT U Library!")

book1 = Books("God's Big Idea", "Dr. Myles Munroe")
book2 = Books("The Power of Positive thinking", "Norman Vincent Peale")
book3 = Books("Atomic Habits", "James Clear")

print(book1.title, book1.author)
my_library.add_books(book1)
my_library.add_books(book2)
print(my_library.list_books())
print("Let's add some Atomic Habits to it")
my_library.add_books(book3)
print(my_library.list_books())

