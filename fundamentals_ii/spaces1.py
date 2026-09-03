# Good: spaces around operators and after commas
x = 5
y = 10
result = (x + y) * (x - y)

# Good: spaces after commas in lists, dicts, and sets
numbers = [1, 2, 3, 4, 5]
point = (3, 4)
person = {"name": "Alice", "age": 30}

# Good: default parameter values — no spaces around '='
def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")

# Good: blank lines separate functions and classes
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


def square(num):
    return num ** 2

# Good: no trailing whitespace at line ends
if x > 0:
    print("Positive number")
