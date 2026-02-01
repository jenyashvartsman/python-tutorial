"""
Create a file utils.py with:
- function slugify(text: str) -> str
  - lowercases
  - trims
  - replaces spaces with "-"

Create a file app.py that:
- imports slugify from utils
- has a list of titles
- builds a list of slugs
- prints them

Use:
- import from another file
- __name__ == "__main__"
- no external libs
"""

from utils.string_utils import slugify

if __name__ == "__main__":

    titles = [
        "  Hello World  ",
        "Python Programming 101",
        "  Learn to Code in Python ",
        "Data Science & AI ",
    ]

    slugs = [slugify(title) for title in titles]

    for slug in slugs:
        print(slug)