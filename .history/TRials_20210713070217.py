starting = int(input('Enter the starting number (1): '))
num = int(input('Enter the number of elements to be generated from the sequence: '))

if starting != 1:
    print('Starting number should be the integer one (1)')
if 0 > num  or num > 24:
    print('Number of elements to be generated should be between the integers zero(0) and twenty four(24)')
else:
    print('Its Okay')        