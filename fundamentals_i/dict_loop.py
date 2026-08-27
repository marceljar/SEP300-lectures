phone_book = {
    "Alice": "416-555-1234",
    "Bob": "647-555-5678",
    "Charlie": "905-555-2468",
    "Diana": "289-555-1357",
    "Ethan": "613-555-9876"
}

print("Printing keys")
for key in phone_book:
    print(key)

print("Printing Values")
for value in phone_book.values():
    print(value)

print("Printing Pairs")
for key, value in phone_book.items():
    print(key, ": ", value)