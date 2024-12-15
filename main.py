from src.services.time_service import TimeService
from src.services.fare_calculator import FareCalculator
from src.services.fare_processor import FareProcessor
from src.utils.csv_handler import CSVHandler

def process_fare_file(input_file: str, output_file: str):
    # Initialize services
    time_service = TimeService()
    fare_calculator = FareCalculator(time_service)
    fare_processor = FareProcessor(fare_calculator)

    # Read input journeys
    journeys = CSVHandler.read_journeys(input_file)

    # Process journeys
    results = []
    for journey in journeys:
        fare = fare_processor.process_journey(journey)
        results.append({
            'FromLine': journey.from_line.value,
            'ToLine': journey.to_line.value,
            'DateTime': journey.datetime.isoformat(),
            'Fare': fare
        })

    # Write results
    CSVHandler.write_results(output_file, results)

if __name__ == "__main__":
    process_fare_file('tests/test_data/sample_input.csv', 'output.csv')