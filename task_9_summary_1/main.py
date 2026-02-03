"""
Data
requests = [
  {"endpoint": "/login", "status": 200, "ms": 120},
  {"endpoint": "/login", "status": 401, "ms": 80},
  {"endpoint": "/books", "status": 200, "ms": 220},
  {"endpoint": "/books", "status": 500, "ms": 900},
  {"endpoint": "/books", "status": 200, "ms": 180},
  {"endpoint": "/profile", "status": 200, "ms": 140},
  {"endpoint": "/profile", "status": 404, "ms": 60},
]

Requirements
Create models.py
- @dataclass Request:
  - endpoint: str
  - status: int
  - ms: int
  - validate in __post_init__:
    - endpoint non-empty
    - status in {200,401,404,500}
    - ms > 0
- InvalidRequestError

Create main.py
- convert dicts -> Request instances (handle errors, print SKIP)
- print:
  - total requests
  - counts by status (dict)
  - counts by endpoint (dict)
  - slowest request: "<endpoint> <status> <ms>ms"
- use:
  - dataclass
  - typing
  - try/except
  - enumerate at least once
  - no external libs
"""

from models import Request, InvalidRequestError
from pathlib import Path
import json

DATA_FILE = "data.json"

def load_requests() -> list[Request]:
    current_dir = Path(__file__).resolve().parent

    try:
        data = (current_dir / DATA_FILE).read_text(encoding='utf-8')
        json_data = json.loads(data)
    except FileNotFoundError:
        print(f"Error: The file '{DATA_FILE}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file '{DATA_FILE}' contains invalid JSON.")
        return []

    reqs = []
    for i, item in enumerate(json_data):
        try:
            req = Request(**item)
            reqs.append(req)
        except InvalidRequestError as e:
            print(f"SKIP: Invalid request at index {i}: {e}")

    return reqs

def print_total_requests(reqs: list[Request]) -> None:
    print(f"Total requests: {len(reqs)}")


def print_counts_by_status(reqs: list[Request]) -> None:
    status_counts = {}
    for req in reqs:
        status_counts[req.status] = status_counts.get(req.status, 0) + 1
    print(f"Counts by status: {status_counts}")


def print_counts_by_endpoint(reqs: list[Request]) -> None:
    endpoint_counts = {}
    for req in reqs:
        endpoint_counts[req.endpoint] = endpoint_counts.get(req.endpoint, 0) + 1
    print(f"Counts by endpoint: {endpoint_counts}")


def print_slowest_request(reqs: list[Request]) -> None:
    if not reqs:
        print("No valid requests to analyze for slowest request.")
        return

    slowest = max(reqs, key=lambda r: r.ms)
    print(f"Slowest request: {slowest.endpoint} {slowest.status} {slowest.ms}ms")
    

if __name__ == "__main__":
    reqs = load_requests()
    print_total_requests(reqs)
    print_counts_by_status(reqs)
    print_counts_by_endpoint(reqs)
    print_slowest_request(reqs)