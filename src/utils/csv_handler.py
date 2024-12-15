import pandas as pd
from typing import List, Dict
from src.models.journey import Journey

class CSVHandler:
    @staticmethod
    def read_journeys(file_path: str) -> List[Journey]:
        df = pd.read_csv(file_path)
        return [Journey.from_dict(row) for _, row in df.iterrows()]

    @staticmethod
    def write_results(file_path: str, results: List[Dict]):
        df = pd.DataFrame(results)
        df.to_csv(file_path, index=False)
        print(f"Created: {file_path}")