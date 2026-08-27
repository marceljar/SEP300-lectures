words = ["hello", "world", "python", "rocks"]

capitalized_words = list(map(\
    lambda word: word[0].upper() + word[1:], words))

print(capitalized_words)