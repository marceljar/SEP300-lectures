groceries = {
    "soap":   (3.49, 2),
    "cheese": (7.99, 1),
    "bread":  (2.99, 3),
    "milk":   (4.29, 2),
    "eggs":   (3.79, 20),
    "apples": (1.29, 10), 
}

def checkout(cart, coupon):
    
    total = 0.0
    for name, (unit_price, qty) in cart.items():
        line = unit_price * qty
        if qty > 10:
            line *= 0.90
        total += line

    if coupon:
        total *= 1 - coupon/100

    return total

print(checkout(groceries, 20))