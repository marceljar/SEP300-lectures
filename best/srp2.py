groceries = {
    "soap":   (3.49, 2),
    "cheese": (7.99, 1),
    "bread":  (2.99, 3),
    "milk":   (4.29, 2),
    "eggs":   (3.79, 20),
    "apples": (1.29, 10), 
}

def apply_coupon(total, coupon):
    return total * (1 - coupon/100)
        
def apply_discount(price, qty):
    if qty > 10:
        price *= 0.90
    return price

def calculate_subtotal(cart):
    total = 0.0
    for name, (unit_price, qty) in cart.items():
        price = unit_price * qty
        discounted_price = apply_discount(price,qty)
        total += discounted_price
    return total
        
def checkout(cart, coupon):  
    subtotal = calculate_subtotal(cart)
    total = apply_coupon(subtotal, coupon)
    return total

print(checkout(groceries, 30))