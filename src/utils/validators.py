from datetime import datetime
from src.models.journey import Journey

class JourneyValidator:
    @staticmethod
    def validate_journey(journey: Journey) -> bool:
        if not isinstance(journey.datetime, datetime):
            return False
        if journey.datetime > datetime.now():
            return False
        return True