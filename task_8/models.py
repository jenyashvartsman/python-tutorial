from dataclasses import dataclass
from datetime import date

class InvalidBookError(Exception):
    pass

@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int

    def __post_init__(self):
        current_year = date.today().year
        if not self.title:
            raise InvalidBookError("Title cannot be empty")
        if not (1450 <= self.year <= current_year):
            raise InvalidBookError(f"Invalid year {self.year} for book '{self.title}'")
    