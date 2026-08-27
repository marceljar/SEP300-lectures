grades = {
    "Alice": 85,
    "Bob": 42,
    "Charlie": 90,
    "Diana": 58,
    "Ethan": 34
}

def is_passing(item):
    name, grade = item
    return grade >= 50

passed = dict(filter(is_passing, grades.items()))
print(passed)
