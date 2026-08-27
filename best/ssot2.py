import config

def calculate_discounted_price(price, quantity):
    if quantity > config.DISCOUNT_THRESHOLD:
        discount = config.HIGH_DISCOUNT
    else:
        discount = config.LOW_DISCOUNT
    
    total = (price * quantity) * (1 - discount)
    total += total * config.TAX_RATE
    total += config.SHIPPING_FEE
    return total

print(calculate_discounted_price(20, 12))
