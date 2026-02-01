"""
Create task8/books.json
- JSON array of 5 books
- each: {"id": int, "title": str, "author": str, "year": int}

Create task8/models.py
- @dataclass Book:
  - id: int
  - title: str
  - author: str
  - year: int

Create task8/main.py
- load books.json with pathlib + json
- convert dicts -> Book instances (Book(**d))
- validate during conversion:
  - year between 1450 and current year
  - title non-empty
  - raise InvalidBookError
- print:
  - total count
  - newest book title
  - list of authors (unique, sorted)
"""

import json
from pathlib import Path
from models import Book, InvalidBookError

def load_books(file_path: Path) -> list[Book]:
    base_dir = Path(__file__).parent
    path = base_dir / file_path
    
    try:
      book_dicts = json.loads(path.read_text())
    except json.JSONDecodeError as e:
      print(f"Error reading JSON file: {e}")
      return []
        

    books = []
    for book_dict in book_dicts:
        try:
            book = Book(**book_dict)
            books.append(book)
        except InvalidBookError as e:
            print(f"Error loading book: {e}")
    
    return books

def print_total_count(books: list[Book]) -> None:
    print(f"Total books loaded: {len(books)}")


def print_newest_book(books: list[Book]) -> None:
    if not books:
        print("No valid books available.")
        return
    newest_book = max(books, key=lambda b: b.year)
    print(f"Newest book: {newest_book.title} ({newest_book.year})")


def print_unique_sorted_authors(books: list[Book]) -> None:
    authors = sorted({book.author for book in books})
    print("Unique authors:")
    for author in authors:
        print(f"- {author}")


if __name__ == "__main__":
    books = load_books(Path("books.json"))
    print_total_count(books)
    print_newest_book(books)
    print_unique_sorted_authors(books)
   