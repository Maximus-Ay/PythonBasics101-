'''
    The @property is a decorator that permits us to consider methods as properties.(They act as attributes)
    They permit us to be able to add additional logic to methods when writing, reading or deleting
    Hence they provide the logic for getter, setters and deleters.
'''

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    # Let's create getter methods so that we can access our rectangle width and height, 
    # without using the private version of it
    @property
    def width(self):
        return f"{self._width:.1f} cm"

    @property
    def height(self):
        return f"{self._height:.1f} cm"
    
    # Now let's create setter methods, that will permit us to be able to set 
    # the width and height to what I desire

    @width.setter
    def width(self, new_width):
        self._width = new_width
        print("The new width has been set")

    @height.setter
    def height(self, new_height):
        self._height = new_height
        print("The new height has been set") 

rectangle = Rectangle(4,5)

rectangle.width = 10

print(rectangle.width)
print(rectangle.height)