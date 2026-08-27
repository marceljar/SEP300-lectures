import time

def square(x):
    return x * x

def add(a, b):
    return a + b

def timed_function(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    print(f"{func.__name__} took {end - start:.6f} seconds")
    return result

print("Result:", timed_function(square, 10))
print("Result:", timed_function(add, 3, 4))
