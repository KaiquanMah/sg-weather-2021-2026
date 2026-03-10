import os
import logging
from datetime import datetime
import pandas as pd
import concurrent.futures
from google.cloud import storage
from google.cloud import bigquery
from config import Config
from api_client import WeatherAPIClient

# Set up logging
log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "workings")
os.makedirs(log_dir, exist_ok=True)
log_filename = os.path.join(log_dir, f"workings-station-ingestion.txt")

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s:%(name)s:%(message)s',
    handlers=[
        logging.FileHandler(log_filename, mode='a'),
        logging.StreamHandler()
    ],
    force=True
)
logger = logging.getLogger(__name__)


class StationIngestor:
    def __init__(self):
        self.project_id = Config.PROJECT_ID
        self.dataset_id = Config.DATASET_ID
        self.bucket_name = Config.BUCKET_NAME
        
        self.storage_client = storage.Client(project=self.project_id)
        self.bq_client = bigquery.Client(project=self.project_id)
        self.api_client = WeatherAPIClient()

        # We will sample these specific dates to guarantee we catch legacy/decommissioned stations
        self.sample_dates = [
            datetime(2021, 1, 1),
            datetime(2022, 1, 1),
            datetime(2023, 1, 1),
            datetime(2024, 1, 1),
            datetime(2025, 1, 1),
            datetime(2026, 1, 1)
        ]

    def _fetch_stations_for_endpoint_and_date(self, endpoint: str, date_obj: datetime):
        """Fetch the stations array for a specific date and endpoint."""
        logger.info(f"Querying {endpoint} for {date_obj.strftime('%Y-%m-%d')}")
        date_str = date_obj.strftime("%Y-%m-%d")
        url = f"{self.api_client.base_url}/{endpoint}"
        params = {"date": date_str}
        
        response = self.api_client._make_request(url, params)
        stations_list = []
        
        if response and "metadata" in response:
            metadata = response.get("metadata", {})
            stations = metadata.get("stations", [])
            for stn in stations:
                loc = stn.get("location", {})
                stations_list.append({
                    "station_id": stn.get("id"),
                    "name": stn.get("name"),
                    "latitude": loc.get("latitude"),
                    "longitude": loc.get("longitude")
                })
        return stations_list

    def extract_unique_stations(self):
        logger.info("Starting historical station metadata extraction...")
        all_stations = []

        # We want to ping all 4 endpoints across our 6 sample dates
        fetch_tasks = []
        for date_obj in self.sample_dates:
            for endpoint in Config.API_ENDPOINTS:
                fetch_tasks.append((endpoint, date_obj))

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_task = {
                executor.submit(self._fetch_stations_for_endpoint_and_date, ep, dt): (ep, dt) 
                for ep, dt in fetch_tasks
            }
            
            for future in concurrent.futures.as_completed(future_to_task):
                ep, dt = future_to_task[future]
                try:
                    stations = future.result()
                    all_stations.extend(stations)
                    logger.debug(f"Fetched {len(stations)} stations from {ep} on {dt.strftime('%Y-%m-%d')}")
                except Exception as e:
                    logger.error(f"Failed fetching metadata for {ep} on {dt.strftime('%Y-%m-%d')}: {e}")

        # Flatten into Pandas and deduplicate
        df = pd.DataFrame(all_stations)
        
        if df.empty:
            logger.warning("No stations were fetched. Exiting.")
            return

        # Drop duplicates across the entire dataset keeping the last observed (most recent metadata)
        # However, station_id is the primary key.
        df_unique = df.drop_duplicates(subset=["station_id"], keep="last").reset_index(drop=True)
        
        logger.info(f"Successfully extracted {len(df_unique)} UNIQUE stations across all historical queries.")
        
        self.upload_to_gcs_and_bq(df_unique)

    def upload_to_gcs_and_bq(self, df: pd.DataFrame):
        # 1. Save to GCS
        local_parquet = "/tmp/stations.parquet"
        df.to_parquet(local_parquet, index=False)
        
        bucket = self.storage_client.bucket(self.bucket_name)
        blob_path = "stations/stations.parquet"
        blob = bucket.blob(blob_path)
        blob.upload_from_filename(local_parquet)
        logger.info(f"Uploaded station metadata to gs://{self.bucket_name}/{blob_path}")
        
        # 2. Load to BigQuery
        dataset_ref = self.bq_client.dataset(self.dataset_id)
        table_ref = dataset_ref.table("stations")
        
        job_config = bigquery.LoadJobConfig(
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
            source_format=bigquery.SourceFormat.PARQUET,
        )
        
        uri = f"gs://{self.bucket_name}/{blob_path}"
        logger.info(f"Loading station metadata into BigQuery table {self.dataset_id}.stations...")
        
        load_job = self.bq_client.load_table_from_uri(
            uri, table_ref, job_config=job_config
        )
        load_job.result()  # Wait for the job to complete
        
        logger.info(f"Successfully loaded {load_job.output_rows} dimension records into {self.dataset_id}.stations")

if __name__ == "__main__":
    try:
        ingestor = StationIngestor()
        ingestor.extract_unique_stations()
    except Exception as e:
        logger.error(f"Station ingestion failed: {e}")
