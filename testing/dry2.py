def apply_discount(total, quantity):
    if quantity >= 10:
        return total * 0.9
    return total

def calculate_book_price(price, quantity):
    total = price * quantity
    return apply_discount(total, quantity)

def calculate_pen_price(price, quantity):
    total = price * quantity
    return apply_discount(total, quantity)
