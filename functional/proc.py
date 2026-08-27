numbers = [1, 2, 3, 4, 5, 6]
squares = []

for n in numbers:
    if n % 2 == 0:
        squares.append(n * n)

print(squares)
