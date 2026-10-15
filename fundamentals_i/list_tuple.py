fruits = ["apple", "banana", "cherry"]
print("List of fruits:", fruits)

print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

fruits.append("orange")
print("After append:", fruits)

fruits[1] = "blueberry"
print("After modification:", fruits)

const_fruits = tuple(fruits)
print("After tuple:", const_fruits)

# const_fruits.append("melon") error