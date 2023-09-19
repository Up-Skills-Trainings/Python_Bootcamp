import numbers


class Employee:

    def __init__(self, name: str = 'Unknown', job_title: str = 'Janitor', salary: numbers = 0):
        self.name = name
        self.job_title = job_title
        self.salary = salary



employee1 = Employee()

print(employee1.name)
print(employee1.job_title)
print(employee1.salary)

employee2 = Employee('Daniel')

print(employee2.name)
print(employee2.job_title)
print(employee2.salary)

employee3 = Employee('Breanna', 'SDET')

print(employee3.name)
print(employee3.job_title)
print(employee3.salary)

employee4 = Employee('Yulia', 'Python Developer', 150_000)
print(employee4.name)
print(employee4.job_title)
print(employee4.salary)