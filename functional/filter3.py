def is_even(number):
    return number % 2 == 0

def square(number):
    return number ** 2 

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

evens = list(map(square, filter(is_even, numbers)))
print(evens)
