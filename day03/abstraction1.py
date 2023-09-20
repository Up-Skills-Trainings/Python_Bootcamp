import numbers
# from day02.utility import className


class Shape:

    def __init__(self):
        self.name = type(self).__name__

    def area(self) -> numbers:
        pass

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Square(Shape):

    def __init__(self, side):
        super().__init__()
        self.side = side


square = Square(5)

print(square)
print( square.area())
