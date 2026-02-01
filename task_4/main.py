"""
Defines a user dict with nested data:
user = {
    "name": "Alice",
    "roles": ["admin", "editor"]
}

Creates:
a reference copy
a shallow copy
a deep copy

Mutates roles in each copy

Prints all users to show the differences
"""

import copy

user = {
    "name": "Alice",
    "roles": ["admin", "editor"]
}

# Creating a reference copy
ref_copy = user

# Creating a shallow copy
shallow_copy = user.copy()

# Creating a deep copy
deep_copy = copy.deepcopy(user)

# Mutating roles in the reference copy
ref_copy["roles"].append("viewer")
ref_copy["name"] = "Bob"

# Mutating roles in the shallow copy
shallow_copy["roles"].append("contributor")
shallow_copy["name"] = "Charlie"

# Mutating roles in the deep copy
deep_copy["roles"].append("subscriber")
deep_copy["name"] = "Diana"

print("Original user:", user)
print("Reference copy:", ref_copy)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)