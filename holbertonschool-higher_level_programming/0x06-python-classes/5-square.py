#!/usr/bin/python3
class Square:
    """A class that defines the size of a square with a private attribute
    making sure that size is of an integer value and greater than zero and
    returns the area size of the square. Retrieves value to set size of square.
    Class also has method of printing the square represented by a hashtag. """
    def __init__(self, __size=0):
        self.__size = __size
        try:
            if type(__size) is not int:
                raise TypeError
            if __size < 0:
                raise ValueError
        except TypeError:
            print('size must be an integer', end="")
            raise
        except ValueError:
            print('size must be >= 0', end="")
            raise

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            if type(value) is not int:
                raise TypeError
            if value < 0:
                raise ValueError
            else:
                self.__size = value
        except TypeError:
            print('size must be an integer', end="")
            raise
        except ValueError:
            print('size must be >= 0', end="")
            raise

    def area(self):
        return int(self.__size) ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end="")
                print()
