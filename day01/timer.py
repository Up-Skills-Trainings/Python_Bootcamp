import time as t

minutes = int(input('please enter the number of minutes\n'))

while minutes > 0:
    seconds = 59

    while seconds >=0:
        print(f'\r{minutes-1} minutes and {seconds} seconds left', end='')
        t.sleep(1)
        seconds -= 1

    minutes -= 1


print('\n\033[31m')
print("\t\t\t* * * * * * * * * * * * * * * * * * * * * * * * * *")
print("\t\t\t*                                                 *")
print("\t\t\t*       Times is Up, Please take your seats!      *")
print("\t\t\t*                                                 *")
print("\t\t\t* * * * * * * * * * * * * * * * * * * * * * * * * *")