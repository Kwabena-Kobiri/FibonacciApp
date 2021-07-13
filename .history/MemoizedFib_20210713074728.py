from functools import lru_cache   # Import the Least Recently Used Cache to provide a means of adding memoization to your function.

@lru_cache(maxsize = 1000)   # Parameter shows the number of values to cache. Default is the first 128 values.
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n -1) + fibonacci(n - 2) 

for i in range(1, 1000):
    print(i , ': ', fibonacci(i))         
