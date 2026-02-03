"""
Mini App Task — “Shopping Cart Summary” (single file)

Requirements
Create a build_item(name, price, qty=1, **extra) function with validation:
name non-empty
price is int|float and > 0
qty is int and > 0
raise InvalidItemError

In __main__, define two lists: item_names, item_qtys, and a dict price_by_name.

Build a list of cart items using zip (no manual indexes).

Print each item with an index using enumerate(start=1) in format:
1. Milk x2 @ 3.5 = 7.0

Print the totals dict:
Totals: {"count": <total_qty>, "subtotal": <sum>}
"""

class InvalidItemError(Exception):
    pass

def build_item(name, price, qty=1, **extra):
    if not name.strip():
        raise InvalidItemError("Item name cannot be empty.")
    if price is None:
        raise InvalidItemError("Price must be provided.")
    if not (isinstance(price, (int, float)) and price > 0):
        raise InvalidItemError("Price must be a positive number.")
    if not (isinstance(qty, int) and qty > 0):
        raise InvalidItemError("Quantity must be a positive integer.")
    
    item = {
        "name": name,
        "price": price,
        "qty": qty,
        **extra
    }
    return item

def print_cart_items(cart):
    for index, item in enumerate(cart, start=1):
        total_price = item["price"] * item["qty"]
        print(f"{index}. {item['name']} x{item['qty']} @ {item['price']} = {total_price}")

def print_cart_summary(cart):
    total_qty = sum(item["qty"] for item in cart)
    subtotal = sum(item["price"] * item["qty"] for item in cart)
    totals = {"count": total_qty, "subtotal": subtotal}
    print("Totals:", totals)

if __name__ == "__main__":
    items_names = ["Milk", "Bread", "Eggs", "Chocolate", "Juice"]
    items_qtys = [2, 1, 12, -3, 3]
    price_by_name = {"Milk": 3.5, "Bread": 2.0, "Eggs": 0.2, "Chocolate": 5.0, "Juice": -1.5}
    cart_items = []

    for name, qty in zip(items_names, items_qtys):
        try:
            price = price_by_name.get(name)
            item = build_item(name, price, qty)
            cart_items.append(item)
        except InvalidItemError as e:
            print(f"Error adding item '{name}': {e}")
    
    print_cart_items(cart_items)
    print_cart_summary(cart_items)
