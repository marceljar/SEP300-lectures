squares = (x ** 2 for x in range(10))
for num in range(10):
    print(next(squares), end=" ")
print()

squares = tuple(x ** 2 for x in range(10))
print(squares)
