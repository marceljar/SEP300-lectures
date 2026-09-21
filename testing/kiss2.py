def is_even(n):
    result = None
    if isinstance(n, int):
        remainder = n % 2
        if remainder == 0:
            result = True
        else:
            result = False
    else:
        raise ValueError("Input must be an integer")
    
    if result == True:
        return True
    elif result == False:
        return False
    else:
        return None

print(is_even(4))
print(is_even(7))
