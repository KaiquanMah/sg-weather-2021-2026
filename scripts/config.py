import os
from datetime import datetime

# Load .env file manually if it exists
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ.setdefault(key.strip(), value.strip('"\''))

# Configuration for the weather data pipeline
class Config:
    # API Configuration
    BASE_URL = "https://api-open.data.gov.sg/v2/real-time/api"
    
    # List of API endpoints to fetch data from
    API_ENDPOINTS = [
        "air-temperature",
        "relative-humidity", 
        "rainfall",
        "wind-speed"
    ]
    
    # API Keys and Headers
    API_KEY = os.getenv("DATA_GOV_SG_API_KEY", "")
    HEADERS = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    } if API_KEY else {"Content-Type": "application/json"}
    
    # Date range for backfill (Jan 2021 to Feb 2026)
    #   for testing
    # START_DATE = datetime(2020, 12, 1)
    # END_DATE = datetime(2020, 12, 5)
    #   for actual ingestion
    # START_DATE = datetime(2021, 1, 1)
    # END_DATE = datetime(2026, 2, 28)
    #     run ingestion on a yearly basis - to deal with exceptions / debug if they come up
    # START_DATE = datetime(2021, 1, 1)
    # END_DATE = datetime(2021, 12, 31)
    # START_DATE = datetime(2022, 1, 1)
    # END_DATE = datetime(2022, 12, 31)
    # START_DATE = datetime(2023, 1, 1)
    # END_DATE = datetime(2023, 12, 31)
    START_DATE = datetime(2024, 1, 1)
    END_DATE = datetime(2024, 12, 31)
    # START_DATE = datetime(2025, 1, 1)
    # END_DATE = datetime(2025, 12, 31)
    # START_DATE = datetime(2026, 1, 1)
    # END_DATE = datetime(2026, 2, 28)

    
    # GCP Configuration
    PROJECT_ID = os.getenv("PROJECT_ID", os.getenv("GOOGLE_CLOUD_PROJECT", ""))
    DATASET_ID = os.getenv("BIGQUERY_DATASET_ID", "weather_data")
    BUCKET_NAME = os.getenv("GCS_BUCKET_NAME", "")
    
    # Rate limiting configuration
    REQUEST_DELAY = 1.5  # seconds between API requests
    MAX_RETRIES = 3
    RETRY_DELAY = 2  # seconds between retries
    
    # Batch size for data loading
    BATCH_SIZE = 1000