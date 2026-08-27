from functools import reduce

grades = {
    "Alice": 85,
    "Bob": 42,
    "Charlie": 90,
    "Diana": 58,
    "Ethan": 34
}

def best_student(student1, student2):
    return student1 if student1[1] > student2[1] else student2

print(reduce(best_student, grades.items()))
