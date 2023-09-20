groceries_list = ['Eggs', 'Milk', 'Rice']

groceries_list.append('Chicken')
groceries_list.extend(('Beef', 'Oranges', 'Onion'))

print(len(groceries_list))
print(groceries_list)

groceries_list[-2] = 'Cherry'

print(groceries_list)

print('------------------------------------')

numbers_list = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers_list)

numbers_list[2:-2] = [300, 4000, 5, 60000]

print(numbers_list)

print('------------------------------------')

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

list1 = characters[2: -3]
print(list1)

list2 = characters[:4]
print(list2)

list3 = characters[2:]
print(list3)

characters[2:5] = ['C', "D", 'E', 'C', 'D', 'E', 'X', 'Y', 'Z']

print(characters)

print('------------------------------------')

names = ['Conor', 'Steve', 'Hazel', 'Breanna']

for x in names:
    print(x)

print('------------------------------------')

nums = [10, 20, 30, 40, 50, 60]

for i in range(len(nums)):
    nums[i] = int(nums[i] / 5)

print(nums)

print('------------------------------------')

nums = [10, 20, 30, 40, 50, 60]

for i in reversed(range(len(nums))):
    print(nums[i])

print('------------------------------------')

for x in nums[::-1]:
    print(x)

print('------------------------------------')

for x in reversed(nums):
    print(x)

print('------------------------------------')

i = 0

while i < len(nums):
    print(nums[i])
    i += 1

print('------------------------------------')

for i in range(1, 6):
    i += 2
    print(i)


print('------------------------------------')


nums = [60, 500, 10, 20, 15, 5, 0]

# nums.sort()  # ascending order

nums.sort(reverse=True)

print(nums)


