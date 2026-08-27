def generate_squares():
    num = 1
    while True:
        yield num ** 2
        num += 1

square = generate_squares()

print(next(square))
print(next(square)) 
print(next(square)) 
print(next(square))

# print(list(generate_squares())) #infinity loop!