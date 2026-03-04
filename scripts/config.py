import os
from datetime import datetime

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
    START_DATE = datetime(2021, 1, 1)
    END_DATE = datetime(2026, 2, 28)
    
    # GCP Configuration
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "")
    DATASET_ID = os.getenv("BIGQUERY_DATASET_ID", "weather_data")
    BUCKET_NAME = os.getenv("GCS_BUCKET_NAME", "")
    
    # Rate limiting configuration
    REQUEST_DELAY = 1.5  # seconds between API requests
    MAX_RETRIES = 3
    RETRY_DELAY = 2  # seconds between retries
    
    # Batch size for data loading
    BATCH_SIZE = 1000