def is_palindrome_permutation(s: str) -> bool:
    # Count character frequencies ignoring spaces.
    # A string can form a palindrome if at most one 
    # char has an odd count.
    counts = {}
    for c in s.replace(" ", "").lower():
        counts[c] = counts.get(c, 0) + 1
    odd_counts = sum(1 for v in counts.values() if v % 2 != 0)
    return odd_counts <= 1
