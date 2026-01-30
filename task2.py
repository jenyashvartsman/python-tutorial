"""
Task

Defines a function build_user.
Required params: name, age
Optional param: active (default True)
Accepts extra attributes via **kwargs
Returns a user dictionary

Creates 3 users with different arguments

Prints the users list
"""

def build_user(name, age, active=True, **kwargs):
    user = {
        "name": name,
        "age": age,
        "active": active,
        **kwargs
    }
    return user

if __name__ == "__main__":
    users = [
        build_user("Alice", 28),
        build_user("Bob", 35, active=False, email="bob@example.com"),
        build_user("Charlie", 32, phone="123-456-7890", address="123 Main St")
    ]

    for user in users:
        print(user)