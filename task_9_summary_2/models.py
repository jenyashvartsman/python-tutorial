from dataclasses import dataclass

class InvalidFileEntryError(Exception):
    pass


@dataclass
class FileEntry:
    path: str
    size_kb: int

    @classmethod
    def from_text_line(cls, line: str) -> FileEntry:
        parts = line.split(maxsplit=1)
        
        if len(parts) != 2:
            raise InvalidFileEntryError(f"Invalid line format: '{line}'")
        
        path, size_str = parts

        if not isinstance(path, str) or not path.strip():
            raise InvalidFileEntryError(f"Invalid file path: '{path}'")
        
        if not isinstance(size_str, str) or not size_str.isdigit() or int(size_str) <= 0:
            raise InvalidFileEntryError(f"Invalid file size: '{size_str}'")
        
        return cls(path=path, size_kb=int(size_str))