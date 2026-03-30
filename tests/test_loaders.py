import unittest
from unittest.mock import Mock, patch, MagicMock
from loaders import DataLoader
from config import Config
import pandas as pd

class TestDataLoader(unittest.TestCase):
    def setUp(self):
        # Mock the Config class attributes to avoid needing real GCP credentials
        Config.PROJECT_ID = "test-project"
        Config.DATASET_ID = "test_dataset"
        Config.BUCKET_NAME = "test-bucket"
        
        # Create mock clients
        mock_bq_client = Mock()
        mock_storage_client = Mock()
        
        self.loader = DataLoader(bq_client=mock_bq_client, storage_client=mock_storage_client)

    @patch('loaders.storage.Client')
    def test_save_to_gcs(self, mock_storage_client):
        # Arrange
        test_data = [{"timestamp": "2023-01-01T00:00:00", "station_id": "S01", "value": 25.0}]
        mock_bucket = Mock()
        mock_blob = Mock()
        self.loader.storage_client.bucket.return_value = mock_bucket
        mock_bucket.blob.return_value = mock_blob

        # Act
        result = self.loader.save_to_gcs(test_data, "air-temperature/2023-01-01")

        # Assert
        self.assertTrue(result.startswith("gs://"))
        self.assertIn("air-temperature/2023-01-01.parquet", result)
        mock_blob.upload_from_string.assert_called_once()

    def test_load_to_bigquery(self):
        # Arrange
        test_data = [{"timestamp": "2023-01-01T00:00:00", "station_id": "S01", "temperature": 25.0}]
        mock_job = Mock()
        self.loader.client.load_table_from_dataframe.return_value = mock_job

        # Act
        result = self.loader.load_to_bigquery(test_data, "raw_air_temperature")

        # Assert
        self.assertEqual(result, len(test_data))
        self.loader.client.load_table_from_dataframe.assert_called_once()
        mock_job.result.assert_called_once()

    def test_transform_data_air_temperature(self):
        # Arrange
        test_data = [{
            "timestamp": "2023-01-01T00:00:00",
            "station_id": "S01", 
            "value": 25.0,
            "ingest_timestamp": "2023-01-01T01:00:00"
        }]

        # Act
        result = self.loader._transform_data(test_data, "air-temperature")

        # Assert
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["temperature"], 25.0)
        self.assertEqual(result[0]["unit"], "celsius")
        self.assertEqual(result[0]["station_id"], "S01")

    def test_transform_data_relative_humidity(self):
        # Arrange
        test_data = [{
            "timestamp": "2023-01-01T00:00:00",
            "station_id": "S01",
            "value": 75.0,
            "ingest_timestamp": "2023-01-01T01:00:00"
        }]

        # Act
        result = self.loader._transform_data(test_data, "relative-humidity")

        # Assert
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["humidity"], 75.0)
        self.assertEqual(result[0]["unit"], "percentage")

    def test_transform_data_rainfall(self):
        # Arrange
        test_data = [{
            "timestamp": "2023-01-01T00:00:00",
            "station_id": "S01",
            "value": 5.2,
            "ingest_timestamp": "2023-01-01T01:00:00"
        }]

        # Act
        result = self.loader._transform_data(test_data, "rainfall")

        # Assert
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["rainfall"], 5.2)
        self.assertEqual(result[0]["unit"], "mm")

    def test_transform_data_wind_speed(self):
        # Arrange
        test_data = [{
            "timestamp": "2023-01-01T00:00:00",
            "station_id": "S01",
            "value": 15.5,
            "ingest_timestamp": "2023-01-01T01:00:00"
        }]

        # Act
        result = self.loader._transform_data(test_data, "wind-speed")

        # Assert
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["speed"], 15.5)
        self.assertEqual(result[0]["unit"], "knots")

    def test_load_weather_data_calls_correct_tables(self):
        # Arrange
        all_data = {
            "air-temperature": [{"timestamp": "2023-01-01T00:00:00", "station_id": "S01", "value": 25.0}],
            "relative-humidity": [{"timestamp": "2023-01-01T00:00:00", "station_id": "S01", "value": 75.0}]
        }
        
        # Mock the helper methods
        with patch.object(self.loader, 'save_to_gcs') as mock_save_gcs, \
             patch.object(self.loader, 'load_to_bigquery') as mock_load_bq, \
             patch.object(self.loader, '_transform_data') as mock_transform:
            
            mock_transform.return_value = [{"transformed": "data"}]
            
            # Act
            self.loader.load_weather_data(all_data, "2023-01-01")

            # Assert
            # Should be called twice (once for each endpoint)
            self.assertEqual(mock_save_gcs.call_count, 2)
            self.assertEqual(mock_load_bq.call_count, 2)
            self.assertEqual(mock_transform.call_count, 2)

if __name__ == '__main__':
    unittest.main()