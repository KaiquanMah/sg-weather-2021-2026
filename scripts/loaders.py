import pandas as pd
from google.cloud import bigquery, storage
import logging
from typing import Dict, List
import json
from scripts.config import Config

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataLoader:
    def __init__(self, bq_client=None, storage_client=None):
        self.client = bq_client or bigquery.Client(project=Config.PROJECT_ID)
        self.storage_client = storage_client or storage.Client(project=Config.PROJECT_ID)
        self.dataset_id = Config.DATASET_ID
        self.bucket_name = Config.BUCKET_NAME
        self.batch_size = Config.BATCH_SIZE

    def save_to_gcs(self, data: List[Dict], filename: str) -> str:
        """Save data to Google Cloud Storage as Parquet"""
        if not data:
            logger.warning("No data to save to GCS")
            return ""
        
        df = pd.DataFrame(data)
        
        # Create blob name
        blob_name = f"raw/{filename}.parquet"
        
        # Upload to GCS
        bucket = self.storage_client.bucket(self.bucket_name)
        blob = bucket.blob(blob_name)
        
        # Convert DataFrame to parquet bytes
        parquet_bytes = df.to_parquet(index=False)
        blob.upload_from_string(parquet_bytes, content_type='application/octet-stream')
        
        logger.info(f"Saved {len(data)} records to gs://{self.bucket_name}/{blob_name}")
        return f"gs://{self.bucket_name}/{blob_name}"

    def load_to_bigquery(self, data: List[Dict], table_name: str) -> int:
        """Load data to BigQuery table"""
        if not data:
            logger.warning(f"No data to load to BigQuery table {table_name}")
            return 0
        
        # Create table reference
        table_ref = self.client.dataset(self.dataset_id).table(table_name)
        
        # Convert to DataFrame and then to list of dictionaries for BigQuery
        df = pd.DataFrame(data)
        
        # Add ingestion timestamp if not present
        if 'ingest_timestamp' not in df.columns:
            df['ingest_timestamp'] = pd.Timestamp.utcnow()
        
        # Load to BigQuery
        job_config = bigquery.LoadJobConfig(
            write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
            schema_update_options=[bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION]
        )
        
        job = self.client.load_table_from_dataframe(df, table_ref, job_config=job_config)
        job.result()  # Wait for the job to complete
        
        logger.info(f"Loaded {len(data)} records to {self.dataset_id}.{table_name}")
        return len(data)

    def load_weather_data(self, all_data: Dict[str, List[Dict]], date_str: str):
        """Load weather data to appropriate BigQuery tables"""
        table_mapping = {
            "air-temperature": "raw_air_temperature",
            "relative-humidity": "raw_relative_humidity", 
            "rainfall": "raw_rainfall",
            "wind-speed": "raw_wind_speed"
        }
        
        total_loaded = 0
        
        for endpoint, data in all_data.items():
            if not data:
                continue
                
            # Transform data based on endpoint type
            transformed_data = self._transform_data(data, endpoint)
            
            # Get target table name
            table_name = table_mapping.get(endpoint)
            if not table_name:
                logger.warning(f"Unknown endpoint: {endpoint}, skipping")
                continue
            
            # Save raw data to GCS
            gcs_filename = f"{endpoint}/{date_str}"
            self.save_to_gcs(data, gcs_filename)
            
            # Load transformed data to BigQuery
            records_loaded = self.load_to_bigquery(transformed_data, table_name)
            total_loaded += records_loaded
            
            logger.info(f"Completed loading {records_loaded} records for {endpoint}")
        
        logger.info(f"Total records loaded: {total_loaded}")
        
    def _transform_data(self, data: List[Dict], endpoint: str) -> List[Dict]:
        """Transform raw API data to match BigQuery schema"""
        transformed = []
        
        for record in data:
            transformed_record = {
                "timestamp": record["timestamp"],
                "station_id": record["station_id"],
                "ingest_timestamp": record.get("ingest_timestamp")
            }
            
            # Add endpoint-specific fields
            if endpoint == "air-temperature":
                transformed_record["temperature"] = float(record["value"]) if record["value"] is not None else None
                transformed_record["unit"] = "celsius"
            elif endpoint == "relative-humidity":
                transformed_record["humidity"] = float(record["value"]) if record["value"] is not None else None
                transformed_record["unit"] = "percentage"
            elif endpoint == "rainfall":
                transformed_record["rainfall"] = float(record["value"]) if record["value"] is not None else None
                transformed_record["unit"] = "mm"
            elif endpoint == "wind-speed":
                transformed_record["speed"] = float(record["value"]) if record["value"] is not None else None
                transformed_record["unit"] = "knots"
            
            transformed.append(transformed_record)
        
        return transformed