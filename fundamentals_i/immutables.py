x = 10     # x is an int object with a value of 10
print("After x = 10")
print("id(x):", id(x))

y = x      # y points to the same object as x 
print("After y = x")
print("id(x):", id(x))
print("id(y):", id(y))

y = 20     # y gets assigned a new int object 
print("After y = 20")
print("id(x):", id(x))
print("id(y):", id(y))

print("The value of x is: ", x)
print("The value of y is: ", y)