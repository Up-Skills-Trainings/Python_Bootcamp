
s = 'Python Programming'

for each in s:
    print(each)

print('-----------------------')

for i in range(0, len(s)):
    print(s[i])

print('-----------------------')

for i in range(-len(s), 0):
    print(s[i])

print('-----------------------')

for i in reversed( range(0, len(s)) ):
    print(s[i])

print('-----------------------')

result = ''

for x in s[::-1]:
   result += x

print(result)

print('-----------------------')

for x in range(1, 11):
    print('Hello World')

print('-----------------------')

num = int( input('Enter a positive number:\n'))

while num <= 0:
    num = int( input('Enter a positive number:\n'))

print(f'You have entered {num}')

print('-----------------------')

answer = input('Enter yes or no:\n')

while not ( answer.lower() == 'yes' or answer.lower() =='no'):
    answer = input('Enter yes or no:\n')

print(f'You have entered {answer}')
