total = 0
for num in range(1, 11, 2):
    total += num

print(total)

print(sum([num for num in range(1, 11) if num % 2 != 0]))
