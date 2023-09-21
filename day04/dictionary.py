employee1 = {}

employee1['name'] = 'James'
employee1['name'] = 'Daniel'
employee1['age'] = 45
employee1['salary'] = 60_000

print(employee1)

employee2 = {
    'name': 'James',
    'age': 29,
    'salary': 80_000,
    'full_time': False
}

print(employee2)
print(employee2['name'])

employee2['salary'] += 10000
print(employee2)

employee2.update({'age': 40})

print(employee2)

employee2['full_time'] = True

# employee2.update( {'full_time': True} )

print(employee2)

employee2.pop('full_time')

print(employee2)

# print( help(dict.popitem) )

employee2.popitem()

print(employee2)

l = employee2.copy()

print(l)

print(employee2 is l)

print('--------- Iterating Dictionary -----------------')

employee3 = {
    'name': 'Shay',
    'age': 29,
    'salary': 110_000,
    'full_time': False,
    'job_title': 'Developer',
    'company': 'Apple Inc'
}

print(list(employee3.keys()))

for key in employee3.keys():
    print(f'{key} : {employee3[key]}')

print('---------------------------------------')

values = list(employee3.values())

print(values)

for value in employee3.values():
    print(value)

print('---------------------------------------')

for x in employee3.items():  # items(): returns a collection of tuples, in each tuple there will be two elements
    # print(x)
    print(f'{x[0]} : {x[1]}')

print('---------------------------------------')

students = {
    'A01': {
        'name': 'James',
        'gender': 'Male',
        'gpa': 3.5,
        'subjects': ['Math', 'Physics']
    },

    'A02': {
        'name': 'Hazel',
        'gender': 'Female',
        'gpa': 3.8,
        'subjects': ['Biology', 'Programming']
    },

    'A03': {
        'name': 'Yulia',
        'gender': 'Female',
        'gpa': 4,
        'subjects': ['Chemistry', 'Programming']
    }
}

print(students)

students['A01']['gpa'] = 2.5

print(students)

# students['A02'].update( {'name': 'Daniel' , 'gender': 'Male'} )
students['A02']['name'] = 'Daniel'
students['A02']['gender'] = 'Male'

print(students)

students['A03']['subjects'][1] = 'Biology'

print(students['A03'])

print('---------------------------------------------')


for x in students.items():
    print(x[1])
    for y in x[1]:
        print(y)

print('---------------------------------------------')

for value in students.values():
    print(value)
    for item in value.items():
        print(item[1])





