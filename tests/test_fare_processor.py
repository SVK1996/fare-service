# tests/test_fare_processor.py
import unittest
from datetime import datetime
from src.models.journey import Journey
from src.models.line import Line
from src.services.time_service import TimeService
from src.services.fare_calculator import FareCalculator
from src.services.fare_processor import FareProcessor

class TestFareProcessor(unittest.TestCase):
    def setUp(self):
        self.time_service = TimeService()
        self.fare_calculator = FareCalculator(self.time_service)
        self.fare_processor = FareProcessor(self.fare_calculator)

    def test_single_journey_peak(self):
        """Test single journey during peak hours"""
        journey = Journey(
            from_line=Line.GREEN,
            to_line=Line.RED,
            datetime=datetime.fromisoformat("2024-03-25T08:30:00")  # Monday peak
        )
        fare = self.fare_processor.process_journey(journey)
        self.assertEqual(fare, 4)  # Peak fare for Green to Red

    def test_single_journey_off_peak(self):
        """Test single journey during off-peak hours"""
        journey = Journey(
            from_line=Line.GREEN,
            to_line=Line.RED,
            datetime=datetime.fromisoformat("2024-03-25T14:30:00")  # Monday off-peak
        )
        fare = self.fare_processor.process_journey(journey)
        self.assertEqual(fare, 3)  # Off-peak fare for Green to Red

    def test_daily_cap(self):
        """Test daily cap implementation"""
        journeys = [
            Journey(Line.GREEN, Line.GREEN, 
                   datetime.fromisoformat("2024-03-25T08:30:00")),
            Journey(Line.GREEN, Line.GREEN, 
                   datetime.fromisoformat("2024-03-25T10:30:00")),
            Journey(Line.GREEN, Line.GREEN, 
                   datetime.fromisoformat("2024-03-25T17:30:00")),
            Journey(Line.GREEN, Line.GREEN, 
                   datetime.fromisoformat("2024-03-25T18:30:00"))
        ]
        
        total_fare = sum(self.fare_processor.process_journey(j) for j in journeys)
        self.assertLessEqual(total_fare, 8)  # Daily cap for Green-Green

    def test_weekly_cap(self):
        """Test weekly cap implementation"""
        # Create journeys for a whole week
        journeys = [
            Journey(Line.RED, Line.RED, 
                   datetime.fromisoformat(f"2024-03-{day}T08:30:00"))
            for day in range(25, 32)  # Monday to Sunday
        ]
        
        total_fare = sum(self.fare_processor.process_journey(j) for j in journeys)
        self.assertLessEqual(total_fare, 70)  # Weekly cap for Red-Red

    def test_mixed_line_journeys(self):
        """Test journeys between different lines"""
        journeys = [
            Journey(Line.GREEN, Line.RED, 
                   datetime.fromisoformat("2024-03-25T08:30:00")),
            Journey(Line.RED, Line.GREEN, 
                   datetime.fromisoformat("2024-03-25T17:30:00"))
        ]
        
        fares = [self.fare_processor.process_journey(j) for j in journeys]
        self.assertEqual(fares[0], 4)  # Peak Green to Red
        self.assertEqual(fares[1], 3)  # Peak Red to Green

    def test_cap_reset(self):
        """Test that caps reset appropriately"""
        # Day 1 journeys
        day1_journeys = [
            Journey(Line.GREEN, Line.GREEN, 
                   datetime.fromisoformat("2024-03-25T08:30:00"))
            for _ in range(5)
        ]
        
        # Day 2 journeys
        day2_journeys = [
            Journey(Line.GREEN, Line.GREEN, 
                   datetime.fromisoformat("2024-03-26T08:30:00"))
            for _ in range(5)
        ]
        
        day1_total = sum(self.fare_processor.process_journey(j) 
                        for j in day1_journeys)
        day2_total = sum(self.fare_processor.process_journey(j) 
                        for j in day2_journeys)
        
        self.assertLessEqual(day1_total, 8)  # Daily cap
        self.assertLessEqual(day2_total, 8)  # Daily cap reset

    def test_fare_combination(self):
        """Test combination of peak/off-peak fares with caps"""
        journeys = [
            # Morning peak
            Journey(Line.RED, Line.RED, 
                   datetime.fromisoformat("2024-03-25T08:30:00")),
            # Off-peak
            Journey(Line.RED, Line.RED, 
                   datetime.fromisoformat("2024-03-25T14:30:00")),
            # Evening peak
            Journey(Line.RED, Line.RED, 
                   datetime.fromisoformat("2024-03-25T17:30:00"))
        ]
        
        fares = [self.fare_processor.process_journey(j) for j in journeys]
        self.assertEqual(fares[0], 3)  # Peak fare
        self.assertEqual(fares[1], 2)  # Off-peak fare
        self.assertEqual(fares[2], 3)  # Peak fare