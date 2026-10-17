def add_numbers(*args):
    total = sum(args)
    return total

print(add_numbers(2, 3))
print(add_numbers(1, 2, 3, 4, 5))

def introduce(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

introduce(name="Alice", age=30, city="Toronto")