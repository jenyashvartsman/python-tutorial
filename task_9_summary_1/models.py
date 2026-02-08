
from dataclasses import dataclass


class InvalidRequestError(Exception):
    pass


@dataclass
class Request:
    endpoint: str
    status: int
    ms: int

    def __post_init__(self):
        if not isinstance(self.endpoint, str) or not self.endpoint.strip():
            raise InvalidRequestError("Endpoint cannot be empty")
        
        if not isinstance(self.status, int) or self.status not in {200, 401, 404, 500}:
            raise InvalidRequestError(f"Invalid status code: {self.status}")
        
        if not isinstance(self.ms, int) or self.ms <= 0:
            raise InvalidRequestError("Response time (ms) must be greater than 0")