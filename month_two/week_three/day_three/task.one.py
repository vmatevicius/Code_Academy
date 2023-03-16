# Task Nr.1:

# Define a Shape class with the following attributes and methods:

# A name attribute, which is a string that represents the name of the shape.
# A sides attribute, which is an integer that represents the number of sides of the shape.
# An area method, which returns the area of the shape.

# Then, define a Rectangle class that inherits from the Shape class and has the following attributes and methods:

# A width attribute, which is a float that represents the width of the rectangle.
# A height attribute, which is a float that represents the height of the rectangle.
# An init method that initializes the name, sides, width, and height attributes.
# An area method that overrides the area method of the Shape class and returns the area of the rectangle.


# Finally, define a Square class that inherits from the Rectangle class and has the following attributes and methods:

# A side_length attribute, which is a float that represents the length of the sides of the square.
# An init method that initializes the side_length attribute and calls the init method of the Rectangle class to initialize the name,  width, and sides,height attributes.


class Shape:
    def __init__(self, shape_name: str, number_of_sides: int) -> None:
        self.shape_name: str = shape_name
        self.number_of_sides: str = number_of_sides

    def get_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        super().__init__("Rectangle", 4)
        self.width: float = width
        self.height: float = height

    def get_area(self) -> float:
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side_lenght: float) -> None:
        super().__init__(side_lenght, side_lenght)
        self.side_lenght: float = side_lenght
