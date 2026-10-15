def is_even(n):
    if isinstance(n, int):
        remainder = n % 2
        if remainder == 0:
            return True
        else:
            return False
    else:
        raise ValueError("Input must be an integer")

print(is_even(4))
print(is_even(7))
