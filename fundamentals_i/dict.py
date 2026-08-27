phone_book = {
    "Alice": "416-555-1234",
    "Bob": "647-555-5678",
    "Charlie": "905-555-2468",
    "Diana": "289-555-1357",
    "Ethan": "613-555-9876"
}

print("Bob's number is:", phone_book["Bob"])

print("Names in the phone_book", phone_book.keys())
print("Numbers in the phone_book", phone_book.values())

phone_book["John"] = "416-416-1122" # adds another entry
phone_book.pop("Ethan")             # removes an entry
print("Names in the phone_book", phone_book.keys())
print("Numbers in the phone_book", phone_book.values())