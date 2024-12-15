from datetime import time

class TimeConfig:
    WEEKDAY_PEAK_HOURS = [
        (time(8, 0), time(10, 0)),
        (time(16, 30), time(19, 0))
    ]

    SATURDAY_PEAK_HOURS = [
        (time(10, 0), time(14, 0)),
        (time(18, 0), time(23, 0))
    ]

    SUNDAY_PEAK_HOURS = [
        (time(18, 0), time(23, 0))
    ]