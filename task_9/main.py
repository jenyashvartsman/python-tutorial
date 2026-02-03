"""
Create task9/logs.txt

- 10 lines
- format: "<level> <service> <message>"
- level is one of: DEBUG INFO WARN ERROR
- include 2 invalid lines (bad level or missing parts)

Create task9/models.py

- Enum Level: DEBUG/INFO/WARN/ERROR
- @dataclass LogEntry:
  - level: Level
  - service: str
  - message: str
- InvalidLogError exception

Create task9/main.py

- read logs.txt with pathlib
- parse each line:
  - use match on level string -> Level enum
  - validate: service non-empty, message non-empty
  - raise InvalidLogError on invalid line
- print:
  - SKIP: <line> (<reason>) for invalid lines
  - counts by level (dict[str,int] or dict[Level,int])
  - counts by service
"""

from pathlib import Path
from models import Level, LogEntry, InvalidLogError

def load_logs(file_path: Path) -> list[LogEntry]:
    log_entries = []
    with file_path.open("r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            try:
                log_entry = LogEntry.from_line(line)
                log_entries.append(log_entry)
            except InvalidLogError as e:
                print(f"SKIP: {line} ({e})")
    return log_entries


def count_by_level(log_entries: list[LogEntry]) -> dict[Level, int]:
    level_counts: dict[Level, int] = {}
    for entry in log_entries:
        level_counts[entry.level] = level_counts.get(entry.level, 0) + 1
    return level_counts


def count_by_service(log_entries: list[LogEntry]) -> dict[str, int]:
    service_counts: dict[str, int] = {}
    for entry in log_entries:
        service_counts[entry.service] = service_counts.get(entry.service, 0) + 1
    return service_counts


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    log_file = base_dir / "logs.txt"
    log_entries = load_logs(log_file)

    level_counts = count_by_level(log_entries)
    service_counts = count_by_service(log_entries)

    print("Counts by Level:")
    for level, count in level_counts.items():
        print(f"{level.value}: {count}")

    print("\nCounts by Service:")
    for service, count in service_counts.items():
        print(f"{service}: {count}")