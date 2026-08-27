# this function does not change the original argument
def add_one(num):
    num += 1
    return num

number = 3
print("Function returns:", add_one(number))
print("Number is now:", number)

# this function changes the original argument
def append_one(list_arg):
    list_arg.append(1)
    return list_arg

list_val = [4, 3, 2]
print("Function returns:", append_one(list_val))
print("The list is now:", list_val)
