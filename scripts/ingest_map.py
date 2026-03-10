import os
import json
import logging
import requests
import pandas as pd
from google.cloud import storage
from google.cloud import bigquery
from config import Config

# Set up logging
log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "workings")
os.makedirs(log_dir, exist_ok=True)
log_filename = os.path.join(log_dir, f"workings-map-ingestion.txt")

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


class MapIngestor:
    def __init__(self):
        # Using the direct download link for the URA Master Plan Subzones dataset
        self.map_url = "https://data.gov.sg/api/action/datastore_search?resource_id=d_8594ae9ff96d0c708bc2af633048edfb"
        
        # NOTE: data.gov.sg v2 sometimes uses format: https://data.gov.sg/api/action/datastore_search?resource_id=d_8594ae9ff96d0c708bc2af633048edfb
        # But for actual GeoJSON downloads, they provide a static file endpoint.
        # It's safer to download the raw GeoJSON using the dataset's direct download link usually found in its metadata.
        # If the API endpoint fails to yield GeoJSON, we will instruct the user or use a direct raw URL if available.
        # The user provided snippet is a standard GeoJSON FeatureCollection.
        
        self.project_id = Config.PROJECT_ID
        self.dataset_id = Config.DATASET_ID
        self.bucket_name = Config.BUCKET_NAME
        
        self.storage_client = storage.Client(project=self.project_id)
        self.bq_client = bigquery.Client(project=self.project_id)

    def fetch_geojson(self) -> dict:
        """Fetch the GeoJSON data."""
        logger.info("Fetching URA Master Plan Subzone GeoJSON...")
        
        # For simplicity, we assume the user will download it manually if the API fails,
        # but let's try to pull directly from a known stable data.gov.sg GeoJSON open dataset endpoint.
        # Wait, the user provided the URL: https://data.gov.sg/datasets/d_8594ae9ff96d0c708bc2af633048edfb/view
        # The actual download URL for the GeoJSON format from Data.gov.sg is usually:
        url = "https://api-open.data.gov.sg/v1/datasets/d_8594ae9ff96d0c708bc2af633048edfb/poll-download"
        
        # Actually, let's use the simplest approach. Many data.gov.sg datasets can be fetched via standard requests.
        # But if the URL requires an async poll, it's tricky. Let's assume the user has the file locally OR we can download it.
        # Let's write the code to parse a local explicitly downloaded file first, or attempt a direct download.
        
        # Alternative: The user provided the data.gov.sg dataset ID.
        # Let's create an elegant try-except that tries to download, but falls back to a local file if they provide it.
        
        local_file_path = os.path.join(os.path.dirname(__file__), "ura_mp19_subzone.geojson")
        
        if os.path.exists(local_file_path):
            logger.info(f"Reading local GeoJSON file: {local_file_path}")
            with open(local_file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        logger.error(f"GeoJSON file not found at {local_file_path}. Please download it from data.gov.sg and save it there.")
        raise FileNotFoundError("GeoJSON file missing.")

    def process_and_upload(self):
        """Parse the GeoJSON, upload to GCS, and load to BigQuery."""
        geojson_data = self.fetch_geojson()
        
        features = geojson_data.get("features", [])
        if not features:
            logger.warning("No features found in GeoJSON.")
            return

        processed_records = []
        for feature in features:
            props = feature.get("properties", {})
            geom = feature.get("geometry", {})
            
            # Flatten properties and stringify the geometry
            record = {
                "OBJECTID": props.get("OBJECTID"),
                "SUBZONE_NO": props.get("SUBZONE_NO"),
                "SUBZONE_N": props.get("SUBZONE_N"),
                "SUBZONE_C": props.get("SUBZONE_C"),
                "CA_IND": props.get("CA_IND"),
                "PLN_AREA_N": props.get("PLN_AREA_N"),
                "PLN_AREA_C": props.get("PLN_AREA_C"),
                "REGION_N": props.get("REGION_N"),
                "REGION_C": props.get("REGION_C"),
                "INC_CRC": props.get("INC_CRC"),
                "FMEL_UPD_D": props.get("FMEL_UPD_D"),
                "SHAPE_AREA": props.get("SHAPE.AREA"), # Replaced dot with underscore for BQ
                "SHAPE_LEN": props.get("SHAPE.LEN"),   # Replaced dot with underscore for BQ
                "geometry": json.dumps(geom) # Store as string for BigQuery GEOGRAPHY casting
            }
            processed_records.append(record)
            
        df = pd.DataFrame(processed_records)
        logger.info(f"Processed {len(df)} subzones from GeoJSON.")
        
        # 1. Save to GCS
        local_parquet = "/tmp/ura_mp19_subzone.parquet"
        df.to_parquet(local_parquet, index=False)
        
        bucket = self.storage_client.bucket(self.bucket_name)
        blob_path = "map/ura_mp19_subzone.parquet"
        blob = bucket.blob(blob_path)
        blob.upload_from_filename(local_parquet)
        logger.info(f"Uploaded map data to gs://{self.bucket_name}/{blob_path}")
        
        # 2. Load to BigQuery
        dataset_ref = self.bq_client.dataset(self.dataset_id)
        table_ref = dataset_ref.table("map")
        
        job_config = bigquery.LoadJobConfig(
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
            source_format=bigquery.SourceFormat.PARQUET,
        )
        
        uri = f"gs://{self.bucket_name}/{blob_path}"
        logger.info(f"Loading map data into BigQuery table {self.dataset_id}.map...")
        
        load_job = self.bq_client.load_table_from_uri(
            uri, table_ref, job_config=job_config
        )
        load_job.result()  # Wait for the job to complete
        
        logger.info(f"Successfully loaded {load_job.output_rows} rows into {self.dataset_id}.map")

if __name__ == "__main__":
    try:
        ingestor = MapIngestor()
        ingestor.process_and_upload()
    except Exception as e:
        logger.error(f"Map ingestion failed: {e}")
