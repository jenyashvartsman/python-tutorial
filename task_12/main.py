"""
Data (in main.py)
numbers = range(1, 1_000_001)

Requirements
Create main.py
- build:
  - squares_list: list of squares of even numbers using list comprehension
  - squares_gen: generator of squares of even numbers using generator expression
- print:
  - first 5 values from squares_list
  - first 5 values from squares_gen
- demonstrate:
  - memory-friendly iteration with generators
  - same filtering logic, different constructs
- use:
  - list comprehension
  - generator expression
  - no external libs
  - no manual indexing
"""

numbers = range(1, 1_000_001)

def squares_list():
    return [x**2 for x in numbers if x % 2 == 0]

def squares_gen():
    for x in numbers:
        if x % 2 == 0:
            yield x**2


if __name__ == "__main__":
    # Build squares_list and squares_gen
    squares_list_result = squares_list()
    squares_gen_result = squares_gen()
    squares_gen_expr = (x**2 for x in numbers if x % 2 == 0)

    # Print first 5 values from squares_list
    print("First 5 values from squares_list:")
    print(squares_list_result[:5])

    # Print first 5 values from squares_gen
    print("\nFirst 5 values from squares_gen:")
    for _ in range(5):
        print(next(squares_gen_result))

    # Print first 5 values from squares_gen_expr
    print("\nFirst 5 values from squares_gen_expr:")
    for _ in range(5):
        print(next(squares_gen_expr))