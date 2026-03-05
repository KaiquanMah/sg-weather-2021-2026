import requests
import time
import logging
from typing import Dict, List, Optional
from scripts.config import Config
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WeatherAPIClient:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = Config.HEADERS
        self.request_delay = Config.REQUEST_DELAY
        self.max_retries = Config.MAX_RETRIES
        self.retry_delay = Config.RETRY_DELAY

    def _make_request(self, url: str, params: Dict = None) -> Optional[Dict]:
        """Make a request to the API with retry logic"""
        for attempt in range(self.max_retries):
            try:
                response = requests.get(url, headers=self.headers, params=params)
                
                if response.status_code == 200:
                    return response.json()
                elif response.status_code == 429:
                    logger.warning(f"Rate limited. Waiting {self.retry_delay * (attempt + 1)} seconds...")
                    time.sleep(self.retry_delay * (attempt + 1))
                    continue
                elif response.status_code == 404:
                    logger.info(f"No data found for URL: {url}")
                    return {"data": {"readings": []}}
                else:
                    logger.error(f"Request failed with status {response.status_code}: {response.text}")
                    if attempt < self.max_retries - 1:
                        time.sleep(self.retry_delay * (attempt + 1))
                        continue
                    else:
                        raise Exception(f"Request failed after {self.max_retries} attempts: {response.status_code}")
            
            except requests.exceptions.RequestException as e:
                logger.error(f"Request exception: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay * (attempt + 1))
                    continue
                else:
                    raise
        
        return None

    def _fetch_paginated_data(self, endpoint: str, date_str: str) -> List[Dict]:
        """Fetch all data for a given endpoint and date, handling pagination"""
        url = f"{self.base_url}/{endpoint}"
        params = {"date": date_str}
        
        all_readings = []
        pagination_token = None
        
        while True:
            if pagination_token:
                params["paginationToken"] = pagination_token
            
            response = self._make_request(url, params)
            
            if not response or "data" not in response:
                logger.error(f"Invalid response structure for {endpoint} on {date_str}")
                break
                
            data = response["data"]
            
            if "readings" in data:
                all_readings.extend(data["readings"])
            
            # Check if there's a next page
            pagination_token = data.get("next", {}).get("paginationToken")
            if not pagination_token:
                break
            
            # Add delay to respect rate limits
            time.sleep(self.request_delay)
        
        logger.info(f"Fetched {len(all_readings)} readings for {endpoint} on {date_str}")
        return all_readings

    def fetch_data_for_date(self, endpoint: str, date: datetime) -> List[Dict]:
        """Fetch data for a specific endpoint and date"""
        date_str = date.strftime("%Y-%m-%d")
        logger.info(f"Fetching {endpoint} data for {date_str}")
        
        readings = self._fetch_paginated_data(endpoint, date_str)
        
        # Add metadata to each reading
        processed_readings = []
        for reading in readings:
            processed_reading = {
                "timestamp": reading.get("timestamp"),
                "station_id": reading.get("stationId"),
                "value": reading.get("value"),
                "date": date_str,
                "endpoint": endpoint,
                "ingest_timestamp": datetime.utcnow().isoformat()
            }
            processed_readings.append(processed_reading)
        
        # Add delay to respect rate limits
        time.sleep(self.request_delay)
        
        return processed_readings

    def fetch_all_data_for_date(self, date: datetime) -> Dict[str, List[Dict]]:
        """Fetch data from all endpoints for a specific date"""
        all_data = {}
        
        for endpoint in Config.API_ENDPOINTS:
            try:
                data = self.fetch_data_for_date(endpoint, date)
                all_data[endpoint] = data
            except Exception as e:
                logger.error(f"Error fetching data for {endpoint} on {date.strftime('%Y-%m-%d')}: {e}")
                all_data[endpoint] = []
        
        return all_data