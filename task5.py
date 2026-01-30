"""
Has two lists:
names = ["Alice", "Bob", "Charlie"]
ages = [28, 35, 32]


Builds a list of user dicts using zip

Prints each user with its index using enumerate

Iterates over a dict and prints key -> value
Uses no indexes (range, len) manually
"""

names = ["Alice", "Bob", "Charlie"]
ages = [28, 35, 32]

# Building a list of user dicts using zip
users = [{"name": name, "age": age} for name, age in zip(names, ages)]

# Printing each user with its index using enumerate
for index, user in enumerate(users, start=1):
    print(f"User {index}: {user}")

# Iterating over a dict and printing key -> value
for user in users:
    user_str = 'User details: '
    for key, value in user.items():
        user_str += f"{key} -> {value}, "
    print(user_str.strip())