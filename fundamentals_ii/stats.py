def stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    mean = sum(numbers) / len(numbers)
    return minimum, maximum, mean

min_value, max_value, mean_value = stats([1, 4, 2, 2, 1])

print("Min:", min_value)
print("Max:", max_value)
print("Mean:", mean_value) 