def power(base=2, exponent=3):
    result = base ** exponent
    return result

print("No arguments:", power()) 
print("Only one argument:", power(3))
print("Both arguments:", power(2, 4))

# using keyword arguments
print("One keyword argument:", power(base = 3))
print("Another keyword argument:", power(exponent = 2))
print("Both keyword arguments:", power(base = 5, exponent = 2))
print("Arguments swapped:", power(exponent = 2, base = 5))