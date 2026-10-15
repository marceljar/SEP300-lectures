def calculate_discounted_price(price, quantity):
    if quantity > 10:
        discount = 0.10
    else:
        discount = 0.05
    
    tax_rate = 0.13
    shipping_fee = 15
    
    total = (price * quantity) * (1 - discount)
    total += total * tax_rate
    total += shipping_fee
    return total

print(calculate_discounted_price(20, 12))
