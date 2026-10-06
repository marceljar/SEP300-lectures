def apply_discount(price, percent):
    return price * (1 - percent / 100.0)


def add_tax(amount, rate):
    return amount * (1 + rate / 100.0)


def final_price(price, percent_discount, tax_rate):
    return add_tax(apply_discount(price, \
                   percent_discount), tax_rate)
