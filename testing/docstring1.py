def factorial(n: int) -> int:
    """
    Compute the factorial of a non-negative integer.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n (n!).

    Raises:
        ValueError: If n is negative.

    Example:
        >>> factorial(5)
        120
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

help(factorial)
print(factorial(5))
