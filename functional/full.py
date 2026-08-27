from functools import reduce

def square(n):
    return n * n

def is_even(n):
    return n % 2 == 0

def add(a, b):
    return a + b

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
            
result = reduce(add, \
         map(square, \
         filter(is_even, numbers)))

print("The sum of even squares is:", result)
