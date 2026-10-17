def capitalize(word):
    return word[0].upper() + word[1:]

words = ["hello", "world", "python", "rocks"]

capitalized_words = list(map(capitalize, words))

print(capitalized_words)
