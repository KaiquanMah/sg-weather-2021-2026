import logging
from datetime import datetime, timedelta
from api_client import WeatherAPIClient
from loaders import DataLoader
from config import Config

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_ingestion(start_date: datetime, end_date: datetime):
    """Main ingestion function to fetch and load weather data"""
    client = WeatherAPIClient()
    loader = DataLoader()
    
    current_date = start_date
    
    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        logger.info(f"Starting ingestion for date: {date_str}")
        
        try:
            # Fetch data from all APIs for the current date
            all_data = client.fetch_all_data_for_date(current_date)
            
            # Load data to GCS and BigQuery
            loader.load_weather_data(all_data, date_str)
            
            logger.info(f"Completed ingestion for date: {date_str}")
        except Exception as e:
            logger.error(f"Error during ingestion for date {date_str}: {e}")
            # Continue with next date instead of stopping the entire process
        
        # Move to next date
        current_date += timedelta(days=1)

def run_single_date(date_str: str):
    """Ingest data for a single date"""
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    client = WeatherAPIClient()
    loader = DataLoader()
    
    logger.info(f"Starting ingestion for single date: {date_str}")
    
    try:
        # Fetch data from all APIs for the specified date
        all_data = client.fetch_all_data_for_date(date_obj)
        
        # Load data to GCS and BigQuery
        loader.load_weather_data(all_data, date_str)
        
        logger.info(f"Completed ingestion for single date: {date_str}")
    except Exception as e:
        logger.error(f"Error during ingestion for date {date_str}: {e}")
        raise

if __name__ == "__main__":
    # Run ingestion for the configured date range
    logger.info(f"Starting weather data ingestion from {Config.START_DATE.date()} to {Config.END_DATE.date()}")
    run_ingestion(Config.START_DATE, Config.END_DATE)
    logger.info("Weather data ingestion completed!")