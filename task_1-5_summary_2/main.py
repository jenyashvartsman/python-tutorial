"""
Mini App Task — Log Parser (single file)
Goal: parse log lines, validate, aggregate counts.

Requirements
You have a multiline string LOGS with lines like:

2026-01-29 INFO auth login user=alice
2026-01-29 ERROR api timeout user=bob

Write parse_line(line) -> dict that returns:
{"date": "...", "level": "...", "service": "...", "message": "...", "user": "...|None"}
If the line is invalid, raise InvalidLogLineError

Build aggregations (dicts):
counts by level
counts by service
counts by user (ignore missing user)

Print:
each invalid line as SKIP: <line> (<reason>)

a final “report” dict:
{"levels": {...}, "services": {...}, "users": {...}}

Use: split, dict, for, try/except, enumerate at least once.
No external libs. One file.
"""

LOGS = """
2026-01-29 INFO auth login user=alice
2026-01-29 INFO api request user=alice
2026-01-29 WARN api slow user=bob
2026-01-29 ERROR api timeout user=bob
2026-01-29 INFO auth logout user=alice
2026-01-29 ERROR auth invalid_password user=carol
BAD LINE WITHOUT ENOUGH PARTS
2026-01-29 INFO api request
2026-01-29 DEBUG api trace user=alice extra=ignored
""".strip()

class InvalidLogLineError(Exception):
    pass

def parse_line(line) -> dict:
    parts = line.split()
    if len(parts) < 4:
        raise InvalidLogLineError("Not enough parts")
    
    date, level, service = parts[0], parts[1], parts[2]
    
    # Validate date format (simple check)
    if len(date) != 10 or date[4] != '-' or date[7] != '-':
        raise InvalidLogLineError("Invalid date format")

    message_parts = parts[3:]
    user = None
    message = []
    
    for part in message_parts:
        if "=" in part:
            key, value = part.split("=", 1)
            if key == "user":
                user = value
            # ignore other key=value fields (e.g., extra=ignored)
        else:
            message.append(part)
    
    if not message:
        raise InvalidLogLineError("Missing message")
    
    return {
        "date": date,
        "level": level,
        "service": service,
        "message": " ".join(message),
        "user": user
    }

def aggregate_logs(log_entries: list[dict]) -> dict:
    counts_by_level = {}
    counts_by_service = {}
    counts_by_user = {}
    
    for log_entry in log_entries:
        level = log_entry["level"]
        service = log_entry["service"]
        user = log_entry["user"]
        
        counts_by_level[level] = counts_by_level.get(level, 0) + 1
        counts_by_service[service] = counts_by_service.get(service, 0) + 1
        
        if user:
            counts_by_user[user] = counts_by_user.get(user, 0) + 1
        
    
    return {
        "levels": counts_by_level,
        "services": counts_by_service,
        "users": counts_by_user
    }

if __name__ == "__main__":
    lines = LOGS.split("\n")
    logs = []

    # Parse lines
    for i, line in enumerate(lines):
        try:
            log_entry = parse_line(line)
            logs.append(log_entry)
        except InvalidLogLineError as e:
            print(f"SKIP: {line} ({e})")

    # Print logs
    print("Parsed Logs:")
    for log in logs:
        print(log)

    print()

    # Print report
    report = aggregate_logs(logs)
    print("Summary Report:\n", report)
