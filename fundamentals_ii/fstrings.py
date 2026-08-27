name = "Alice"
age = 30

# mixing strings and variables or expressions
print(f"My name is {name} and I am {age} years old.")
print(f"In five years, I will be {age + 5} years old.")

# number formatting
pi = 3.141592653589793
print(f"Pi rounded to 2 decimals: {pi:.2f}")
print(f"Pi in scientific notation: {pi:.3e}")

# applying methods
print(f"My name in uppercase: {name.upper()}")
print(f"My name in lowercase: {name.lower()}")

# using dictionaries
person = {"name": "Bob", "age": 25}
print(f"{person['name']} is {person['age']} years old.")
