def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}")
        print(f"Provided arguments {args[0]} and {args[1]}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(x, y):
    return x + y

add(10, 8)