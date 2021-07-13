"""
THIS IS A PURE PYTHON FUNCTIONAL IMPLEMENTATION OF THE FIBONACCI SEQUENCE.
IT TAKES A STARTING NUMBER INPUT FROM THE USER AS WELL AS THE
NUMBER OF ELEMENTS TO BE GENERATED.
THE CODE GENERATES A FIBONACCI SEQUENCE BASED ON THE NUMBER OF 
ELEMENTS THE USER SPECIFIED.
"""

def fibonacci():
    try:
        # Taking input from the User
        starting = int(input('Enter the starting number (1): '))
        num = int(input('Enter the number of elements to be generated from the sequence: '))

        # Initializing first two values of the sequence and the sequence list
        num1 = 1
        num2 = 1
        sum = 0
        sequence = [num1, num2]

        # Checking if starting number is equal to 1
        if starting != 1:
            print('Starting number should be the integer one (1)')
        # Checking if value falls between 0 and 24     
        elif 0 > num  or num > 24:
            print('Number of elements to be generated should be between the integers zero(0) and twenty four(24)')
        # Handling an event where user does not want to generate any item in the sequence    
        elif num == 0:
            sequence = sequence.clear()
            print(sequence)
        # Handling a situation where user wants to generate only the first item in the sequence    
        elif num == 1:
            sequence = sequence.pop()
            print(sequence)    
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
