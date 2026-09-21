def calculate_book_price(price, quantity):
    total = price * quantity
    if quantity >= 10:
        total *= 0.9   # 10% discount
    return total

def calculate_pen_price(price, quantity):
    total = price * quantity
    if quantity >= 10:
        total *= 0.9   # same discount logic repeated
    return total
