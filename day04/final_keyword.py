from typing import final

pi: final = 3.14

pi = 3.5


@final
class Animal:
    pass


class Dog(Animal):
    pass


class Employee:

    @final
    def work(self):
        print('Working')


class Driver(Employee):

    def work(self):
        print('Driving')


class Person:

    def __init__(self, age: int):
        self.__age = age

    @property
    def person_age(self):
        return self.__age

    @person_age.setter
    def person_age(self, value):
        raise RuntimeError(f' age is constant, can not be changed')


person1 = Person(10)

print(person1.person_age)

# person1.person_age = 100

print(person1.person_age)

print(person1.__age)
