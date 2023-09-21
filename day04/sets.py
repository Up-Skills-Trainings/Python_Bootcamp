
unique_element = set()

unique_element.add(10)
unique_element.add(10)
unique_element.add(10)
unique_element.add(20)
unique_element.add(20)

print( type(unique_element))
print(unique_element)

#print(unique_element[1])

#print( unique_element[1:] )

unique_element.remove(10)

print(unique_element)

unique_element.update( (1, 2, 3, 4, 5,1 ,2 ,3 , 4, 5) )

# print( help(set.update) )

print(unique_element)

n = unique_element.pop()

print(unique_element)

print(n)

# print( help( str.istitle ) )




print('-------------difference-----------------------')

# difference(): compares two sets and returns a new set which contains the items that only exist in first set
s1 = {'Java', 'Python', 'C#'}
s2 = {'Ruby', 'Java', 'C++', 'Swift'}

s3 = s1.difference(s2)

print(s3)


print('----------------------intersection-------------------')

# intersection(): compares two sets and returns a new set which contains the common elements of two sets
set1 = {'Java', 'Python', 'C#', 'Cydeo'}
set2 = {'C++', 'Ruby', 'Swift', 'Java', 'Python'}

set3 = set1.intersection(set2)

print(set3)


print('------------------different_update-------------------')

# different_update(): removes the elements of the first Set that exist in the second Set
a1 = {'Book', 'Pen', 'Apple', 'Cherry', 'Coffee'}
a2 = {'Book', 'Apple', 'Banana', 'Grape', 'TV'}

a1.difference_update(a2)
print(a1)


print('---------------intersection_update----------------------')

# intersection_update(): removes the uncommon elements of first & second sets
b1 = {'Cydeo', 'Python', 'Java', 'C#', 'Wooden Spoon', 'Ruby', 'Swift'}
b2 = {'Wooden Spoon', 'Python', 'Cydeo'}

b1.intersection_update(b2)

print(b1)




print('------------------symmetric_update-------------------')

# symmetric_difference(): Compares two sets and returns a new set which contains all elements except the common once
e1 = {'Apple', 'Banana', 'Cherry'}
e2 = {'Grape', 'Strawberry', 'Banana', 'Mango', 'Lemon', 'Apple'}

e3 = e1.symmetric_difference(e2)

print(e3)










