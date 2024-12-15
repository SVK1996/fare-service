from typing import Dict, Tuple
from src.models.line import Line

class FareConfig:
    PEAK_FARES: Dict[Tuple[Line, Line], float] = {
        (Line.GREEN, Line.GREEN): 2,
        (Line.RED, Line.RED): 3,
        (Line.GREEN, Line.RED): 4,
        (Line.RED, Line.GREEN): 3
    }

    NON_PEAK_FARES: Dict[Tuple[Line, Line], float] = {
        (Line.GREEN, Line.GREEN): 1,
        (Line.RED, Line.RED): 2,
        (Line.GREEN, Line.RED): 3,
        (Line.RED, Line.GREEN): 2
    }

    DAILY_CAPS: Dict[Tuple[Line, Line], float] = {
        (Line.GREEN, Line.GREEN): 8,
        (Line.RED, Line.RED): 12,
        (Line.GREEN, Line.RED): 15,
        (Line.RED, Line.GREEN): 15
    }

    WEEKLY_CAPS: Dict[Tuple[Line, Line], float] = {
        (Line.GREEN, Line.GREEN): 55,
        (Line.RED, Line.RED): 70,
        (Line.GREEN, Line.RED): 90,
        (Line.RED, Line.GREEN): 90
    }