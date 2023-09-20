import numbers

from abc import ABC, abstractmethod
# import abc

"""
abc: module name (built in module)
ABC: Abstract class in abc module
abstractmethod: annotations that can be given to abstract methods
"""

class Shape(ABC):

    def __init__(self):
        self.name = type(self).__name__

    @abstractmethod
    def area(self) -> numbers:
        pass

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'
