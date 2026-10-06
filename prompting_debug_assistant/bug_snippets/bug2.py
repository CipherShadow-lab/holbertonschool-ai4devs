# Code snippet runs, however produces the wrong result due to incorrect logic.

def calculate_discount(price, discount_percent):
    """Function calculates discounted price for products"""
    discount = price * discount_percent
    final_price = price - discount
    return final_price


products = [
    ("Laptop", 1200),
    ("Keyboard", 100),
    ("Mouse", 50),
]

for product_name, product_price in products:
    discounted_price = calculate_discount(product_price, 10)
    print(product_name, "costs $", discounted_price)
