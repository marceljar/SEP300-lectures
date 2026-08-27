grades = {
    "Alice": 85,
    "Bob": 62,
    "Charlie": 90,
    "Diana": 58,
    "Ethan": 74
}

passed = [name for name, grade in grades.items() \
                                   if grade >= 70]
print(passed) # list of names

passed = {name: grade for name, grade in grades.items() \
                                   if grade >= 70}
print(passed) # filtered dictionary
