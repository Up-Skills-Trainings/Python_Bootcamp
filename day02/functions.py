"""

Java Methods:
    public static void method(parameter){

    }


"""
import numbers


def display_message():
    print('Hello Cydeo')
    print('Hello World')


display_message()


def value():
    return 'Python Programming'


print(value())


def return_int() -> int:
    return 10.0


print(return_int())


def square(num: int):
    return num * num


print(square(10))


# print( square('Java'))

# print( divide('C#', 'Python'))

def add(num1: numbers, num2: numbers) -> numbers:
    return num1 + num2


print(add(10, 20))

print(add(10.5, 20.5))

print('------------------------------------------')


def calculate(num1: numbers, num2: numbers, operator: str) -> numbers:
    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('Invalid operator')
        return 0


print(calculate(10, 20, '+'))

print(calculate(100.5, 2.5, '/'))

print('---------------------------------------------------------')


# example of method overloading

def sum(n1: numbers, n2: numbers, n3: numbers = 0, n4: numbers = 0) -> numbers:
    return n1 + n2 + n3 + n4


print(sum(10, 20))

print(sum(10, 20, 30))

print(sum(10, 20, 30, 40))


class test:
    def method(self):
        pass


print('----------------------------------------')


def concat(a: str, b, c='', d='', e=''):
    print(f'{a} {b} {c} {d} {e}'.strip())


concat('Cydeo', 'School')
concat('Python', 3, 2.5)
concat('Python', 3, 2.5, True)
concat('Python', 3, 2.5, True, False)


"""
1. Declaring
2. parameters
3. restricting parameter' data type
4. setting default value to parameter
5. restricting return type

Dynamic Typing
"""