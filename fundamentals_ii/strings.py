string = "  hello, SEP300 students!  "

# remove whitespace 
print("strip():", string.strip())

# change cases
print("lower():", string.lower())
print("upper():", string.upper())

# finding and counting substrings
print("find('SEP300'):", string.find("SEP300"))
print("count('e'):", string.count("e"))

# replacing substrings
print("replace:", string.replace("SEP300", "SD and D"))

# splitting and joining
words = string.split()
print("split():", words)
print("join():", "-".join(words))

#iterating over a string
for char in string:
    print(char, end=' ')
print()    
