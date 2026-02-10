"""
Data (in main.py)
events = [
  {"type": "click", "page": "home"},
  {"type": "click", "page": "pricing"},
  {"type": "view", "page": "home"},
  {"type": "click", "page": "home"},
  {"type": "signup", "page": "pricing"},
  {"type": "view", "page": "docs"},
  {"type": "click", "page": "docs"},
  {"type": "view", "page": "home"},
  {"type": "signup", "page": "home"},
]

Requirements
Create main.py
- build:
  - counts_by_type using Counter
  - counts_by_page using Counter
  - counts_by_type_per_page using defaultdict(Counter)
- print:
  - counts_by_type (dict)
  - counts_by_page (dict)
  - for each page: "<page>: <type_counts_dict>"
- no manual .get() counting
- no external libs
- keep 2 blank lines between top-level defs (if any)
"""

from collections import Counter, defaultdict

events = [
  {"type": "click", "page": "home"},
  {"type": "click", "page": "pricing"},
  {"type": "view", "page": "home"},
  {"type": "click", "page": "home"},
  {"type": "signup", "page": "pricing"},
  {"type": "view", "page": "docs"},
  {"type": "click", "page": "docs"},
  {"type": "view", "page": "home"},
  {"type": "signup", "page": "home"},
]


counts_by_type = Counter(event["type"] for event in events)
counts_by_page = Counter(event["page"] for event in events)


counts_by_type_per_page = defaultdict(Counter)
for event in events:
    counts_by_type_per_page[event["page"]][event["type"]] += 1


if __name__ == "__main__":
    print("Counts by type:")
    print(dict(counts_by_type))
    print("\nCounts by page:")
    print(dict(counts_by_page))
    print("\nCounts by type per page:")
    for page, type_counts in counts_by_type_per_page.items():
        print(f"{page}: {dict(type_counts)}")