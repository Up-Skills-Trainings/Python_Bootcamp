import numbers

from abc import ABC, abstractmethod

# import abc

"""
abc: module name (built in module)
ABC: Abstract class in abc module
abstractmethod: annotations that can be given to abstract methods
"""


class Volume(ABC):

    @abstractmethod
    def volume(self):
        pass


class Shape(ABC):

    def __init__(self):
        self.name = type(self).__name__

    @abstractmethod
    def area(self) -> numbers:
        pass

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Square(Shape):

    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self) -> numbers:
        return self.side * self.side


class Circle(Shape):

    def area(self) -> numbers:
        pass


class Rectangle(Shape):

    def area(self) -> numbers:
        pass


class Cube(Shape, Volume):

    def area(self) -> numbers:
        pass

    def volume(self):
        pass


class Cylinder(Shape, Volume):

    def area(self) -> numbers:
        pass

    def volume(self):
        pass


square1 = Square(5)

print(square1)
print(square1.area())
