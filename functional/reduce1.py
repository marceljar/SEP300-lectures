from functools import reduce

numbers = [1, 2, 3, 4, 5, 6 , 7, 8]

def sum(a, b): 
    return a + b

total = reduce(sum, numbers)
print(total)