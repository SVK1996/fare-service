from typing import Dict
from datetime import datetime
from src.models.journey import Journey
from src.services.fare_calculator import FareCalculator

class FareProcessor:
    def __init__(self, fare_calculator: FareCalculator):
        self.fare_calculator = fare_calculator
        self.daily_totals: Dict[str, float] = {}
        self.weekly_totals: Dict[str, float] = {}

    def process_journey(self, journey: Journey) -> float:
        date = journey.datetime.date()
        week = f"{date.year}-W{date.isocalendar()[1]}"

        # Calculate base fare
        fare = self.fare_calculator.calculate_base_fare(journey)

        # Apply caps
        fare = self._apply_daily_cap(journey, date, fare)
        fare = self._apply_weekly_cap(journey, week, fare)

        return fare

    def _apply_daily_cap(self, journey: Journey, date: datetime.date, fare: float) -> float:
        date_str = date.isoformat()
        new_daily_total = self.daily_totals.get(date_str, 0) + fare
        daily_cap = self.fare_calculator.get_daily_cap(journey)

        if new_daily_total > daily_cap:
            fare -= (new_daily_total - daily_cap)
            self.daily_totals[date_str] = daily_cap
        else:
            self.daily_totals[date_str] = new_daily_total

        return fare

    def _apply_weekly_cap(self, journey: Journey, week: str, fare: float) -> float:
        new_weekly_total = self.weekly_totals.get(week, 0) + fare
        weekly_cap = self.fare_calculator.get_weekly_cap(journey)

        if new_weekly_total > weekly_cap:
            fare -= (new_weekly_total - weekly_cap)
            self.weekly_totals[week] = weekly_cap
        else:
            self.weekly_totals[week] = new_weekly_total

        return fare