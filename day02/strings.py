name = 'Python'

print(len(name))
print(name[0])
print(name[len(name) - 1])

print(name[-1])
print(name[-2])

s = 'Java Programming Language'
s2 = s[5:16]

print(s2)

s3 = s[:4]

print(s3)

s4 = s[::-1]  # reverses the string after slicing

print(s4)

s = 'Python Programming'

s5 = str(reversed(s))

print(type(s5))
reversed(s5)

print(s5)

s5 = s[::-1]

print(s5)

s5 = 'python Programming'

s6 = s5[7:]  # by default it slices the string from index 7 to the last character

print(s6)


s7 = 'CYDEO SCHOOL'
# str(reversed(s7))

print('----------------------')

# print( help(str))


print('----------------------')

s = 'python programming language'

# s = s.capitalize()
s = s.title()
print(s)

s = "            Python           "
s = s.strip()  # trim method of java

print(s)


s = 'JAVA'

print( s.index('A'))
print(s.rindex('A'))

s = 'Java Java'

s = s.replace('Java', 'Python', 1)

print(s)

s = 'C# C# Python'

s = s.replace(' C#', ' Java')
print(s)


s = 'Java jAVA java JAVA Python Python'

count_java = s.lower().count('java')
count_python = s.count('Python')

print(count_java)
print(count_python)


s1 = 'java'
s2 = 'JAVA'

print( s1.lower() == s2.lower())  # ignore case


s = 'Java'

print(s[0].islower())
print(s[0].isupper() )


s = 'a'

print(s.isalpha())

s = '1'

print(s.isdigit())


s = 'Cydeo School'

print(s.istitle())

