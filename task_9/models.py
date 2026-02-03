from enum import Enum
from dataclasses import dataclass

class Level(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"


class InvalidLogError(Exception):
    pass


@dataclass
class LogEntry:
    level: Level
    service: str
    message: str

    @classmethod
    def from_line(cls, line: str) -> 'LogEntry':
        parts = line.split(maxsplit=2)
        
        if len(parts) != 3:
            raise InvalidLogError(f"Log entry must have exactly three parts: {line}")
        
        level_str, service, message = parts
        level = LogEntry.parse_level(level_str)
        
        if not service.strip():
            raise InvalidLogError("Service cannot be empty")
        
        if not message.strip():
            raise InvalidLogError("Message cannot be empty")
        
        return cls(level, service, message)
    
    @staticmethod
    def parse_level(level_str: str) -> Level:
        match level_str:
            case "DEBUG":
                return Level.DEBUG
            case "INFO":
                return Level.INFO
            case "WARN":
                return Level.WARN
            case "ERROR":
                return Level.ERROR
            case _:
                raise InvalidLogError(f"Invalid log level: {level_str}")

