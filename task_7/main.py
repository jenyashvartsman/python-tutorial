"""
Add file: books.json
- JSON array of 5 books
- each book: {"id": int, "title": str, "author": str, "year": int}

Add file: main.py
- uses pathlib.Path to load books.json
- parses JSON into Python list
- prints:
  - total count
  - titles sorted by year asc (one per line: "YEAR - TITLE")
- handles errors:
  - missing file
  - invalid JSON
  - empty list
"""

from pathlib import Path
import json


def load_books(file_path):
    try:
        data = file_path.read_text(encoding='utf-8')
        books = json.loads(data)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' contains invalid JSON.")
        return None

    if not books:
        print("No books found in the file.")
        return None

    return books

def print_books_info(books):
    print(f"Total number of books: {len(books)}")
    sorted_books = sorted(books, key=lambda x: x['year'])
    for book in sorted_books:
        print(f"{book['year']} - {book['title']}")

if __name__ == "__main__":
    base_dir = Path(__file__).parent
    file_path = base_dir / 'books.json'
    books = load_books(file_path)
    if books:
        print_books_info(books)