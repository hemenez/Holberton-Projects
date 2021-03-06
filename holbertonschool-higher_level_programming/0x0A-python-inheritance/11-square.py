#!/usr/bin/python3
class BaseGeometry:
    """Class Base Geometry
    """
    def area(self):
        """Method raises exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Method validates value
        """
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError(str(self.name) + " must be an integer")
        if value <= 0:
            raise ValueError(str(self.value) + " must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry parent class
    """
    def __init__(self, width, height):
        """Method handles instantiation
        """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def __str__(self):
        """Method returns string representation of when area is evaluated
        """
        return '[Rectangle] %s/%s' % (self.__width, self.__height)

    def area(self):
        """Method returns area of rectangle
        """
        return self.__width * self.__height


class Square(Rectangle):
    """Square class inherited from Rectangle parent class
    """
    def __init__(self, size):
        """Initializes values for every new instance
        """
        super(Square, self).__init__(size, size)
        self.__size = size
        BaseGeometry.integer_validator(self, "size", self.__size)

    def __str__(self):
        """Method returns string rep of when area is evaluated
        """
        return '[Square] %s/%s' % (self.__size, self.__size)
