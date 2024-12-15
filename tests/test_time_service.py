# tests/test_time_service.py
import unittest
from datetime import datetime
from src.services.time_service import TimeService

class TestTimeService(unittest.TestCase):
    def setUp(self):
        self.time_service = TimeService()

    def test_weekday_morning_peak(self):
        """Test weekday morning peak hours"""
        # Monday 8:30 AM
        dt = datetime.fromisoformat("2024-03-25T08:30:00")
        self.assertTrue(self.time_service.is_peak_hour(dt))

        # Monday 7:59 AM (before peak)
        dt = datetime.fromisoformat("2024-03-25T07:59:00")
        self.assertFalse(self.time_service.is_peak_hour(dt))

        # Monday 10:01 AM (after peak)
        dt = datetime.fromisoformat("2024-03-25T10:01:00")
        self.assertFalse(self.time_service.is_peak_hour(dt))

    def test_weekday_evening_peak(self):
        """Test weekday evening peak hours"""
        # Monday 17:30 (5:30 PM)
        dt = datetime.fromisoformat("2024-03-25T17:30:00")
        self.assertTrue(self.time_service.is_peak_hour(dt))

        # Monday 16:29 (before peak)
        dt = datetime.fromisoformat("2024-03-25T16:29:00")
        self.assertFalse(self.time_service.is_peak_hour(dt))

        # Monday 19:01 (after peak)
        dt = datetime.fromisoformat("2024-03-25T19:01:00")
        self.assertFalse(self.time_service.is_peak_hour(dt))

    def test_saturday_peak(self):
        """Test Saturday peak hours"""
        # Saturday 11:00 AM (first peak period)
        dt = datetime.fromisoformat("2024-03-30T11:00:00")
        self.assertTrue(self.time_service.is_peak_hour(dt))

        # Saturday 20:00 (8:00 PM) (second peak period)
        dt = datetime.fromisoformat("2024-03-30T20:00:00")
        self.assertTrue(self.time_service.is_peak_hour(dt))

        # Saturday 15:00 (3:00 PM) (between peak periods)
        dt = datetime.fromisoformat("2024-03-30T15:00:00")
        self.assertFalse(self.time_service.is_peak_hour(dt))

    def test_sunday_peak(self):
        """Test Sunday peak hours"""
        # Sunday 20:00 (8:00 PM)
        dt = datetime.fromisoformat("2024-03-31T20:00:00")
        self.assertTrue(self.time_service.is_peak_hour(dt))

        # Sunday 17:59 (before peak)
        dt = datetime.fromisoformat("2024-03-31T17:59:00")
        self.assertFalse(self.time_service.is_peak_hour(dt))

        # Sunday 23:01 (after peak)
        dt = datetime.fromisoformat("2024-03-31T23:01:00")
        self.assertFalse(self.time_service.is_peak_hour(dt))

    def test_edge_cases(self):
        """Test edge cases"""
        # Exactly at start of peak hour
        dt = datetime.fromisoformat("2024-03-25T08:00:00")
        self.assertTrue(self.time_service.is_peak_hour(dt))

        # Exactly at end of peak hour
        dt = datetime.fromisoformat("2024-03-25T19:00:00")
        self.assertTrue(self.time_service.is_peak_hour(dt))

        # Midnight
        dt = datetime.fromisoformat("2024-03-25T00:00:00")
        self.assertFalse(self.time_service.is_peak_hour(dt))

    def test_different_weekdays(self):
        """Test different weekdays"""
        # Test same time (8:30 AM) across different weekdays
        weekday_times = [
            datetime.fromisoformat(f"2024-03-{day}T08:30:00")
            for day in range(25, 30)  # Monday to Friday
        ]

        for dt in weekday_times:
            self.assertTrue(self.time_service.is_peak_hour(dt),
                          f"Failed for {dt.strftime('%A')}")

    def test_holiday_schedule(self):
        """Test holiday schedule (if implemented)"""
        # Note: This is a placeholder for future implementation
        # Could test special holiday schedules if they're different
        pass

if __name__ == '__main__':
    unittest.main()