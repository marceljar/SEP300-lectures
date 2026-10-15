import time

def timed(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} secs")
        return result
    return wrapper

@timed
def square(x):
    return x * x

# @timed is equivalent to:
# square = timed(square)

@timed
def add(a, b):
    return a + b

# @timed is equivalent to:
# add = timed(add)

print("Result:", square(10))
print("Result:", add(3, 4))
