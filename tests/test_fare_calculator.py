import unittest
from datetime import datetime
from src.models.journey import Journey
from src.models.line import Line
from src.services.time_service import TimeService
from src.services.fare_calculator import FareCalculator

class TestFareCalculator(unittest.TestCase):
    def setUp(self):
        self.time_service = TimeService()
        self.calculator = FareCalculator(self.time_service)

    def test_peak_hour_fare(self):
        journey = Journey(
            Line.GREEN,
            Line.GREEN,
            datetime.fromisoformat("2024-03-24T08:30:00")
        )
        fare = self.calculator.calculate_base_fare(journey)
        self.assertEqual(fare, 2)

    def test_non_peak_hour_fare(self):
        journey = Journey(
            Line.RED,
            Line.RED,
            datetime.fromisoformat("2024-03-24T11:30:00")
        )
        fare = self.calculator.calculate_base_fare(journey)
        self.assertEqual(fare, 2)

if __name__ == '__main__':
    unittest.main()