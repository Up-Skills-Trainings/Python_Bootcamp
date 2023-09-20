
class Person:

    def __init__(self, name):
        self.__name = None
        self.__age = None
        self.person_name = name

    @property
    def person_name(self):
        if self.__name is None or self.__name == '' or type(self.__name) != str:
            raise RuntimeError(f'Invalid name has been set: {self.__name}')

        return self.__name

    @person_name.setter
    def person_name(self, name):

        if type(name) != str:
            raise RuntimeError(f'Person name must be string')

        if name == '':
            raise RuntimeError(f'Person name can not be empty')

        self.__name = name