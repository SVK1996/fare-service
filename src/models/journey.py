from dataclasses import dataclass
from datetime import datetime
from src.models.line import Line

@dataclass
class Journey:
    from_line: Line
    to_line: Line
    datetime: datetime

    @classmethod
    def from_dict(cls, data: dict) -> 'Journey':
        return cls(
            from_line=Line.from_string(data['FromLine']),
            to_line=Line.from_string(data['ToLine']),
            datetime=datetime.fromisoformat(data['DateTime'])
        )