"""
Task

Defines a list of users (name, age).
Filters users older than 30.
Returns their names upper-cased.
Prints the result.
"""

users = [
    {"name": "Alice", "age": 28},
    {"name": "Bob", "age": 35},
    {"name": "Charlie", "age": 32},
    {"name": "David", "age": 25},
    {"name": "Eve", "age": 40}
]

def get_uppercase_names_of_users_older_than_30(users):
    return [user["name"].upper() for user in users if user["age"] > 30]

if __name__ == "__main__":
    result = get_uppercase_names_of_users_older_than_30(users)
    print(result)