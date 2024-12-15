from enum import Enum

class Line(Enum):
    GREEN = "Green"
    RED = "Red"

    @classmethod
    def from_string(cls, value: str) -> 'Line':
        try:
            return cls(value)
        except ValueError:
            raise ValueError(f"Invalid line: {value}")