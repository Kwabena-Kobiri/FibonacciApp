def fibonacci():
    try:
        starting = int(input('Enter the starting number (1): '))
        num = int(input('Enter the number of elements to be generated from the sequence: '))

        num1 = 1
        num2 = 1
        sum = 0
        sequence = [num1, num2]

        if starting != 1:
            print('Starting number should be the integer one (1)')
        elif 0 > num  or num > 24:
            print('Number of elements to be generated should be between the integers zero(0) and twenty four(24)')
        else:
            for i in range(2, num):
                sum = num1 + num2
                num1 = num2
                num2 = sum
                sequence.append(sum)
            print(sequence)    
    except ValueError as err:
        print("Value Not an Integer: ", err)

fibonacci() 
