def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n -1) + fibonacci(n - 2)    

for i in range(0, 15):
    print(i , ': ', fibonacci(i))        