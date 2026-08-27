def fibonacci(n: int) -> int:
    # This implementation has exponential time complexity
    # Works fine for small n (<35)
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
