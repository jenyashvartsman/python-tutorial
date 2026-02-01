"""
Task

Defines a custom exception InvalidUserError

Updates build_user to:
raise if name is empty
raise if age is not a positive int

Creates users inside try / except
Prints either the user or the error message
Continues execution after failures
"""

class InvalidUserError(Exception):
    pass

def build_user(name, age):
    if not name.strip():
        raise InvalidUserError("Name cannot be empty.")
    if  not isinstance(age, int) or age <= 0:
        raise InvalidUserError("Age must be a positive integer.")
    
    return {"name": name, "age": age}

if __name__ == "__main__":
    user_data = [
        ("Alice", 30),
        ("", 25),
        ("Bob", -5),
        ("Charlie", "twenty"),
        ("Diana", 22)
    ]

    for name, age in user_data:
        try:
            user = build_user(name, age)
            print(f"User created: {user}")
        except InvalidUserError as e:
            print(f"Error creating user with name '{name}' and age '{age}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        else:
            print(f"Successfully created user: {user}")