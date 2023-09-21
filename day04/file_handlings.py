import os

path = 'files/Test.txt'

text_file = open(path, 'r')

print( text_file.read() )


text_file.close()

"""
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
"""

print('----------------------------------')

path = 'files/Test2.txt'

text_file2= open(path, 'w')

text_file2.write('This is a new text file\nPython created this file')

text_file2.close()

print('----------------------------------')

os.remove(path)

