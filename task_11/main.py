"""
Data (in main.py)
products = [
  {"name": "Laptop", "price": 1200, "rating": 4.6},
  {"name": "Mouse", "price": 25, "rating": 4.2},
  {"name": "Keyboard", "price": 75, "rating": 4.8},
  {"name": "Monitor", "price": 300, "rating": 4.4},
  {"name": "USB Cable", "price": 10, "rating": 3.9},
]

Requirements
Create main.py
- print products sorted by:
  - price asc
  - price desc
  - rating desc
- print top 2 products by rating
- demonstrate:
  - sorted()
  - key=
  - lambda
- do NOT mutate original list
- no external libs
"""

products = [
  {"name": "Laptop", "price": 1200, "rating": 4.6},
  {"name": "Mouse", "price": 25, "rating": 4.2},
  {"name": "Keyboard", "price": 75, "rating": 4.8},
  {"name": "Monitor", "price": 300, "rating": 4.4},
  {"name": "USB Cable", "price": 10, "rating": 3.9},
]

def print_sorted_products(products, key, reverse=False):
    sorted_products = sorted(products, key=lambda x: x[key], reverse=reverse)
    print(f"Products sorted by {key} {'descending' if reverse else 'ascending'}:")
    for product in sorted_products:
        print(product)

def print_top_rated_products(products, top_n=2):
    top_rated_products = sorted(products, key=lambda x: x['rating'], reverse=True)[:top_n]
    print(f"Top {top_n} products by rating:")
    for product in top_rated_products:
        print(product)

if __name__ == "__main__":
    print_sorted_products(products, key='price', reverse=False)  # Price ascending
    print('---')
    print_sorted_products(products, key='price', reverse=True)   # Price descending
    print('---')
    print_sorted_products(products, key='rating', reverse=True)  # Rating descending
    print('---')
    print_top_rated_products(products, top_n=2)  # Top 2 products by rating