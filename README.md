# Transit Fare Calculator System
A modular and extensible fare calculation system for public transit networks.

## Overview
System calculates fares for a transit network with multiple lines, implementing peak/off-peak pricing, daily caps, and weekly caps. It handles various scenarios including cross-line journeys and special weekend rates.

## Features
- 🚇 Multi-line fare calculation (Green and Red lines)
- ⏰ Peak and off-peak pricing
- 💰 Daily and weekly fare capping
- 📊 CSV input/output processing
- ✅ Comprehensive test coverage
- 🔄 Extensible architecture

## Directory Structure
```plaintext
fare-system/
│
├── src/
│   ├── config/
│   │   ├── fare_config.py      # Fare rules and caps
│   │   └── time_config.py      # Peak hours configuration
│   │
│   ├── models/
│   │   ├── line.py            # Transit line definitions
│   │   └── journey.py         # Journey data structure
│   │
│   ├── services/
│   │   ├── fare_calculator.py # Core fare calculation logic
│   │   ├── fare_processor.py  # Journey processing and cap application
│   │   └── time_service.py    # Time-based calculations
│   │
│   └── utils/
│       ├── csv_handler.py     # CSV file operations
│       └── validators.py      # Input validation
│
├── tests/
│   ├── test_data/
│   │   ├── sample_input.csv
│   │   └── expected_output.csv
│   ├── test_fare_calculator.py
│   ├── test_fare_processor.py
│   └── test_time_service.py
│
├── main.py
├── requirements.txt
└── README.md