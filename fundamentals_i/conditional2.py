score = int(input("Enter your score (0 - 100): "))

if score >= 90:
    print("Grade: A+")
elif score >= 80:
    print("Grade: A")
elif score >= 75:
    print("Grade: B+")
elif score >= 50:
    pass
else:
    print("Grade: F")