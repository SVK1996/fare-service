from datetime import datetime, time
from src.config.time_config import TimeConfig

class TimeService:
    @staticmethod
    def is_peak_hour(dt: datetime) -> bool:
        weekday = dt.weekday()
        current_time = dt.time()

        if weekday < 5:  # Monday to Friday
            return TimeService._is_time_in_ranges(
                current_time, 
                TimeConfig.WEEKDAY_PEAK_HOURS
            )
        elif weekday == 5:  # Saturday
            return TimeService._is_time_in_ranges(
                current_time, 
                TimeConfig.SATURDAY_PEAK_HOURS
            )
        else:  # Sunday
            return TimeService._is_time_in_ranges(
                current_time, 
                TimeConfig.SUNDAY_PEAK_HOURS
            )

    @staticmethod
    def _is_time_in_ranges(current_time: time, ranges: list) -> bool:
        return any(start <= current_time <= end for start, end in ranges)