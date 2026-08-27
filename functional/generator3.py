import sys

squares_gen = (i * i for i in range(1, 200))

for square in squares_gen:
    print(square, end= " ")
print()

squares_list = [i * i for i in range(1, 200)]

for square in squares_list:
    print(square, end= " ")
print()

print("Size of gen:", sys.getsizeof(squares_gen))
print("Size of list:", sys.getsizeof(squares_list))
