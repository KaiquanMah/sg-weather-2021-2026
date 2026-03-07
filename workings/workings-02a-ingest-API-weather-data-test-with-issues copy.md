* ingest weather data from 4 APIs - Initial issues
```bash
@KaiquanMah ➜ /workspaces/sg-weather-2021-2026 (main) $ make run-ingestion
python scripts/ingest.py
INFO:__main__:Starting weather data ingestion from 2020-12-01 to 2020-12-05
INFO:__main__:Starting ingestion for date: 2020-12-01
INFO:api_client:Fetching air-temperature data for 2020-12-01
INFO:api_client:Fetched 25 readings for air-temperature on 2020-12-01
INFO:api_client:Fetching relative-humidity data for 2020-12-01
INFO:api_client:Fetched 25 readings for relative-humidity on 2020-12-01
INFO:api_client:Fetching rainfall data for 2020-12-01
INFO:api_client:Fetched 25 readings for rainfall on 2020-12-01
INFO:api_client:Fetching wind-speed data for 2020-12-01
INFO:api_client:Fetched 25 readings for wind-speed on 2020-12-01
INFO:loaders:Saved 367 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/air-temperature/2020-12-01.parquet
/home/codespace/.local/lib/python3.12/site-packages/google/cloud/bigquery/_pandas_helpers.py:486: FutureWarning: Loading pandas DataFrame into BigQuery will require pandas-gbq package version 0.26.1 or greater in the future. Tried to import pandas-gbq and got: No module named 'pandas_gbq'
  warnings.warn(
ERROR:__main__:Error during ingestion for date 2020-12-01: 503 POST https://bigquery.googleapis.com/upload/bigquery/v2/projects/2026-01-gemini-hackathon/jobs?uploadType=multipart: Service Unavailable
INFO:__main__:Starting ingestion for date: 2020-12-02
INFO:api_client:Fetching air-temperature data for 2020-12-02
INFO:api_client:Fetched 25 readings for air-temperature on 2020-12-02
INFO:api_client:Fetching relative-humidity data for 2020-12-02
INFO:api_client:Fetched 25 readings for relative-humidity on 2020-12-02
INFO:api_client:Fetching rainfall data for 2020-12-02
INFO:api_client:Fetched 25 readings for rainfall on 2020-12-02
INFO:api_client:Fetching wind-speed data for 2020-12-02
INFO:api_client:Fetched 25 readings for wind-speed on 2020-12-02
INFO:loaders:Saved 367 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/air-temperature/2020-12-02.parquet
/home/codespace/.local/lib/python3.12/site-packages/google/cloud/bigquery/_pandas_helpers.py:486: FutureWarning: Loading pandas DataFrame into BigQuery will require pandas-gbq package version 0.26.1 or greater in the future. Tried to import pandas-gbq and got: No module named 'pandas_gbq'
  warnings.warn(
ERROR:__main__:Error during ingestion for date 2020-12-02: 503 POST https://bigquery.googleapis.com/upload/bigquery/v2/projects/2026-01-gemini-hackathon/jobs?uploadType=multipart: Service Unavailable
INFO:__main__:Starting ingestion for date: 2020-12-03
INFO:api_client:Fetching air-temperature data for 2020-12-03
INFO:api_client:Fetched 25 readings for air-temperature on 2020-12-03
INFO:api_client:Fetching relative-humidity data for 2020-12-03
INFO:api_client:Fetched 25 readings for relative-humidity on 2020-12-03
INFO:api_client:Fetching rainfall data for 2020-12-03
INFO:api_client:Fetched 25 readings for rainfall on 2020-12-03
INFO:api_client:Fetching wind-speed data for 2020-12-03
INFO:api_client:Fetched 25 readings for wind-speed on 2020-12-03
INFO:loaders:Saved 371 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/air-temperature/2020-12-03.parquet
/home/codespace/.local/lib/python3.12/site-packages/google/cloud/bigquery/_pandas_helpers.py:486: FutureWarning: Loading pandas DataFrame into BigQuery will require pandas-gbq package version 0.26.1 or greater in the future. Tried to import pandas-gbq and got: No module named 'pandas_gbq'
  warnings.warn(
ERROR:__main__:Error during ingestion for date 2020-12-03: 503 POST https://bigquery.googleapis.com/upload/bigquery/v2/projects/2026-01-gemini-hackathon/jobs?uploadType=multipart: Service Unavailable
INFO:__main__:Starting ingestion for date: 2020-12-04
INFO:api_client:Fetching air-temperature data for 2020-12-04
INFO:api_client:Fetched 25 readings for air-temperature on 2020-12-04
INFO:api_client:Fetching relative-humidity data for 2020-12-04
INFO:api_client:Fetched 25 readings for relative-humidity on 2020-12-04
INFO:api_client:Fetching rainfall data for 2020-12-04
INFO:api_client:Fetched 25 readings for rainfall on 2020-12-04
INFO:api_client:Fetching wind-speed data for 2020-12-04
INFO:api_client:Fetched 25 readings for wind-speed on 2020-12-04
INFO:loaders:Saved 374 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/air-temperature/2020-12-04.parquet
/home/codespace/.local/lib/python3.12/site-packages/google/cloud/bigquery/_pandas_helpers.py:486: FutureWarning: Loading pandas DataFrame into BigQuery will require pandas-gbq package version 0.26.1 or greater in the future. Tried to import pandas-gbq and got: No module named 'pandas_gbq'
  warnings.warn(
ERROR:__main__:Error during ingestion for date 2020-12-04: 503 POST https://bigquery.googleapis.com/upload/bigquery/v2/projects/2026-01-gemini-hackathon/jobs?uploadType=multipart: Service Unavailable
INFO:__main__:Starting ingestion for date: 2020-12-05
INFO:api_client:Fetching air-temperature data for 2020-12-05
INFO:api_client:Fetched 25 readings for air-temperature on 2020-12-05
INFO:api_client:Fetching relative-humidity data for 2020-12-05
INFO:api_client:Fetched 25 readings for relative-humidity on 2020-12-05
INFO:api_client:Fetching rainfall data for 2020-12-05
INFO:api_client:Fetched 25 readings for rainfall on 2020-12-05
INFO:api_client:Fetching wind-speed data for 2020-12-05
INFO:api_client:Fetched 25 readings for wind-speed on 2020-12-05
INFO:loaders:Saved 374 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/air-temperature/2020-12-05.parquet
/home/codespace/.local/lib/python3.12/site-packages/google/cloud/bigquery/_pandas_helpers.py:486: FutureWarning: Loading pandas DataFrame into BigQuery will require pandas-gbq package version 0.26.1 or greater in the future. Tried to import pandas-gbq and got: No module named 'pandas_gbq'
  warnings.warn(
ERROR:__main__:Error during ingestion for date 2020-12-05: 503 POST https://bigquery.googleapis.com/upload/bigquery/v2/projects/2026-01-gemini-hackathon/jobs?uploadType=multipart: Service Unavailable
INFO:__main__:Weather data ingestion completed!
```