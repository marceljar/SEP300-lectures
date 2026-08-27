import time

def timed(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} secs")
        return result
    return wrapper

def logger(func):
    def wrapper(*args):
        print(f"Calling function {func.__name__}")
        print(f"Provided arguments {args[0]} and {args[1]}")
        result = func(*args)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@timed
@logger
def add(x, y):
    return x + y

add(10, 8)