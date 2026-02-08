"""
Data
Create a file: files.txt
- each line: "<path> <size_kb>"
- example:
  /src/main.py 12
  /src/utils.py 8
  /README.md 4
  /src/main.py 12   # duplicate
  INVALID LINE
  /assets/logo.png -5

Requirements
Create models.py
- @dataclass FileEntry:
  - path: str
  - size_kb: int
  - validate in __post_init__:
    - path non-empty
    - size_kb > 0
- InvalidFileEntryError

Create main.py
- read files.txt with pathlib
- parse each line into FileEntry
- on error: print `SKIP: <line> (<reason>)`
- print:
  - total valid entries
  - total size (sum of size_kb)
  - counts by directory (e.g. "/src": 2)
  - largest file: "<path> <size_kb>kb"
- use:
  - dataclass
  - typing
  - try/except
  - enumerate at least once
  - split(maxsplit=1)
  - no external libs
"""

from pathlib import Path
from models import FileEntry, InvalidFileEntryError

data_file = "files.txt"

def read_file_entries(file_path: str) -> list[FileEntry]:
    current_dir = Path(__file__).resolve().parent
    entries = []
    with open(current_dir / file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = FileEntry.from_text_line(line)

                # Check for duplicates
                if any(e.path == entry.path and e.size_kb == entry.size_kb for e in entries):
                    print(f"SKIP: {line} (duplicate entry)")
                    continue

                entries.append(entry)
            except InvalidFileEntryError as e:
                print(f"SKIP: {line} ({e})")
    return entries


def print_total_entries(entries: list[FileEntry]) -> None:
    print(f"Total valid entries: {len(entries)}")


def print_total_size(entries: list[FileEntry]) -> None:
    total_size = sum(entry.size_kb for entry in entries)
    print(f"Total size: {total_size}kb")


def print_counts_by_directory(entries: list[FileEntry]) -> None:
    directory_counts = {}
    for entry in entries:
        directory = Path(entry.path).parent.as_posix()
        directory_counts[directory] = directory_counts.get(directory, 0) + 1
    print("Counts by directory:")
    for directory, count in directory_counts.items():
        print(f"{directory}: {count}")


def print_largest_file(entries: list[FileEntry]) -> None:
    if not entries:
        print("No valid entries to determine largest file.")
        return
    largest_entry = max(entries, key=lambda e: e.size_kb)
    print(f"Largest file: {largest_entry.path} {largest_entry.size_kb}kb")


if __name__ == "__main__":
    entries = read_file_entries(data_file)
    print_total_entries(entries)
    print_total_size(entries)
    print_counts_by_directory(entries)
    print_largest_file(entries)