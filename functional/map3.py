def to_kg(lbs):
    return round(lbs * 0.453592, 1)

def classify(kg):
    if kg < 65:
        return "Lightweight"
    elif kg < 80:
        return "Middleweight"
    else:
        return "Heavyweight"

weights_lbs = [115, 140, 155, 170, 200, 210]

result = list(map(classify, map(to_kg, weights_lbs)))

print(result)
