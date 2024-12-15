from src.models.journey import Journey
from src.config.fare_config import FareConfig
from src.services.time_service import TimeService

class FareCalculator:
    def __init__(self, time_service: TimeService):
        self.time_service = time_service

    def calculate_base_fare(self, journey: Journey) -> float:
        line_pair = (journey.from_line, journey.to_line)

        if self.time_service.is_peak_hour(journey.datetime):
            return FareConfig.PEAK_FARES[line_pair]
        return FareConfig.NON_PEAK_FARES[line_pair]

    def get_daily_cap(self, journey: Journey) -> float:
        return FareConfig.DAILY_CAPS[(journey.from_line, journey.to_line)]

    def get_weekly_cap(self, journey: Journey) -> float:
        return FareConfig.WEEKLY_CAPS[(journey.from_line, journey.to_line)]