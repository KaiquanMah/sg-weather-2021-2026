* ingest weather data from 4 APIs, after fixes to
  * GCS bucket folders - from `1 folder for all API's files` to `1 folder per API`
  * BigQuery - dataset, tables (related to .env)
  * .env issues that deviated from Terraform
  * From `sequential, individual API calls` to `parallelising calling all 4 APIs at the same time`
  * requirements.txt - to work with datetime from data read into df, pyarrow, pandas-gbq, pytz (to set the timezone)
```bash
@KaiquanMah ➜ /workspaces/sg-weather-2021-2026 (main) $ make run-ingestion
python scripts/ingest.py
INFO:__main__:Starting weather data ingestion from 2020-12-01 to 2020-12-05
INFO:__main__:Starting ingestion for date: 2020-12-01
INFO:api_client:Fetching air-temperature data for 2020-12-01
INFO:api_client:Fetching relative-humidity data for 2020-12-01
INFO:api_client:Fetching rainfall data for 2020-12-01
INFO:api_client:Fetching wind-speed data for 2020-12-01
INFO:api_client:Fetched 25 readings for wind-speed on 2020-12-01
INFO:api_client:Fetched 25 readings for air-temperature on 2020-12-01
INFO:api_client:Fetched 25 readings for relative-humidity on 2020-12-01
INFO:api_client:Fetched 25 readings for rainfall on 2020-12-01
INFO:loaders:Saved 367 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/air-temperature/2020-12-01.parquet
INFO:loaders:Saved 317 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/wind-speed/2020-12-01.parquet
INFO:loaders:Saved 367 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/relative-humidity/2020-12-01.parquet
INFO:loaders:Saved 1849 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/rainfall/2020-12-01.parquet
INFO:loaders:Loaded 367 records to weather_data.raw_air_temperature
INFO:loaders:Completed loading 367 records for air-temperature
INFO:loaders:Loaded 1849 records to weather_data.raw_rainfall
INFO:loaders:Completed loading 1849 records for rainfall
INFO:loaders:Loaded 367 records to weather_data.raw_relative_humidity
INFO:loaders:Completed loading 367 records for relative-humidity
INFO:loaders:Loaded 317 records to weather_data.raw_wind_speed
INFO:loaders:Completed loading 317 records for wind-speed
INFO:loaders:Total records loaded: 2900
INFO:__main__:Completed ingestion for date: 2020-12-01



INFO:__main__:Starting ingestion for date: 2020-12-02
INFO:api_client:Fetching air-temperature data for 2020-12-02
INFO:api_client:Fetching relative-humidity data for 2020-12-02
INFO:api_client:Fetching rainfall data for 2020-12-02
INFO:api_client:Fetching wind-speed data for 2020-12-02
INFO:api_client:Fetched 25 readings for wind-speed on 2020-12-02
INFO:api_client:Fetched 25 readings for air-temperature on 2020-12-02
INFO:api_client:Fetched 25 readings for rainfall on 2020-12-02
INFO:api_client:Fetched 25 readings for relative-humidity on 2020-12-02
INFO:loaders:Saved 367 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/relative-humidity/2020-12-02.parquet
INFO:loaders:Saved 317 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/wind-speed/2020-12-02.parquet
INFO:loaders:Saved 1832 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/rainfall/2020-12-02.parquet
INFO:loaders:Saved 367 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/air-temperature/2020-12-02.parquet
INFO:loaders:Loaded 367 records to weather_data.raw_air_temperature
INFO:loaders:Completed loading 367 records for air-temperature
INFO:loaders:Loaded 1832 records to weather_data.raw_rainfall
INFO:loaders:Completed loading 1832 records for rainfall
INFO:loaders:Loaded 367 records to weather_data.raw_relative_humidity
INFO:loaders:Completed loading 367 records for relative-humidity
INFO:loaders:Loaded 317 records to weather_data.raw_wind_speed
INFO:loaders:Completed loading 317 records for wind-speed
INFO:loaders:Total records loaded: 2883
INFO:__main__:Completed ingestion for date: 2020-12-02







INFO:__main__:Starting ingestion for date: 2020-12-03
INFO:api_client:Fetching air-temperature data for 2020-12-03
INFO:api_client:Fetching relative-humidity data for 2020-12-03
INFO:api_client:Fetching rainfall data for 2020-12-03
INFO:api_client:Fetching wind-speed data for 2020-12-03
INFO:api_client:Fetched 25 readings for wind-speed on 2020-12-03
INFO:api_client:Fetched 25 readings for relative-humidity on 2020-12-03
INFO:api_client:Fetched 25 readings for rainfall on 2020-12-03
INFO:api_client:Fetched 25 readings for air-temperature on 2020-12-03
INFO:loaders:Saved 371 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/relative-humidity/2020-12-03.parquet
INFO:loaders:Saved 371 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/air-temperature/2020-12-03.parquet
INFO:loaders:Saved 1799 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/rainfall/2020-12-03.parquet
INFO:loaders:Saved 321 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/wind-speed/2020-12-03.parquet
INFO:loaders:Loaded 321 records to weather_data.raw_wind_speed
INFO:loaders:Completed loading 321 records for wind-speed
INFO:loaders:Loaded 371 records to weather_data.raw_relative_humidity
INFO:loaders:Completed loading 371 records for relative-humidity
INFO:loaders:Loaded 371 records to weather_data.raw_air_temperature
INFO:loaders:Completed loading 371 records for air-temperature
INFO:loaders:Loaded 1799 records to weather_data.raw_rainfall
INFO:loaders:Completed loading 1799 records for rainfall
INFO:loaders:Total records loaded: 2862
INFO:__main__:Completed ingestion for date: 2020-12-03







INFO:__main__:Starting ingestion for date: 2020-12-04
INFO:api_client:Fetching air-temperature data for 2020-12-04
INFO:api_client:Fetching relative-humidity data for 2020-12-04
INFO:api_client:Fetching rainfall data for 2020-12-04
INFO:api_client:Fetching wind-speed data for 2020-12-04
INFO:api_client:Fetched 25 readings for rainfall on 2020-12-04
INFO:api_client:Fetched 25 readings for wind-speed on 2020-12-04
INFO:api_client:Fetched 25 readings for relative-humidity on 2020-12-04
INFO:api_client:Fetched 25 readings for air-temperature on 2020-12-04
INFO:loaders:Saved 324 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/wind-speed/2020-12-04.parquet
INFO:loaders:Saved 374 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/relative-humidity/2020-12-04.parquet
INFO:loaders:Saved 374 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/air-temperature/2020-12-04.parquet
INFO:loaders:Saved 1850 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/rainfall/2020-12-04.parquet
INFO:loaders:Loaded 1850 records to weather_data.raw_rainfall
INFO:loaders:Completed loading 1850 records for rainfall
INFO:loaders:Loaded 374 records to weather_data.raw_air_temperature
INFO:loaders:Completed loading 374 records for air-temperature
INFO:loaders:Loaded 324 records to weather_data.raw_wind_speed
INFO:loaders:Completed loading 324 records for wind-speed
INFO:loaders:Loaded 374 records to weather_data.raw_relative_humidity
INFO:loaders:Completed loading 374 records for relative-humidity
INFO:loaders:Total records loaded: 2922
INFO:__main__:Completed ingestion for date: 2020-12-04






INFO:__main__:Starting ingestion for date: 2020-12-05
INFO:api_client:Fetching air-temperature data for 2020-12-05
INFO:api_client:Fetching relative-humidity data for 2020-12-05
INFO:api_client:Fetching rainfall data for 2020-12-05
INFO:api_client:Fetching wind-speed data for 2020-12-05
INFO:api_client:Fetched 25 readings for wind-speed on 2020-12-05
INFO:api_client:Fetched 25 readings for air-temperature on 2020-12-05
INFO:api_client:Fetched 25 readings for rainfall on 2020-12-05
INFO:api_client:Fetched 25 readings for relative-humidity on 2020-12-05
INFO:loaders:Saved 374 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/air-temperature/2020-12-05.parquet
INFO:loaders:Saved 1848 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/rainfall/2020-12-05.parquet
INFO:loaders:Saved 324 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/wind-speed/2020-12-05.parquet
INFO:loaders:Saved 374 records to gs://proud-outrider-483901-c3-weather-raw-kfru2uzo/raw/relative-humidity/2020-12-05.parquet
INFO:loaders:Loaded 374 records to weather_data.raw_air_temperature
INFO:loaders:Completed loading 374 records for air-temperature
INFO:loaders:Loaded 374 records to weather_data.raw_relative_humidity
INFO:loaders:Completed loading 374 records for relative-humidity
INFO:loaders:Loaded 324 records to weather_data.raw_wind_speed
INFO:loaders:Completed loading 324 records for wind-speed
INFO:loaders:Loaded 1848 records to weather_data.raw_rainfall
INFO:loaders:Completed loading 1848 records for rainfall
INFO:loaders:Total records loaded: 2920
INFO:__main__:Completed ingestion for date: 2020-12-05
INFO:__main__:Weather data ingestion completed!
```