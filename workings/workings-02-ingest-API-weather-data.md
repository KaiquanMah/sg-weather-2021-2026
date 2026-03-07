* ingest weather data from 4 APIs
```bash
@KaiquanMah ➜ /workspaces/sg-weather-2021-2026 (main) $ make run-ingestion
python scripts/ingest.py
INFO:__main__:Starting weather data ingestion from 2021-01-01 to 2026-02-28
INFO:__main__:Starting ingestion for date: 2021-01-01
INFO:api_client:Fetching air-temperature data for 2021-01-01
INFO:api_client:Fetched 25 readings for air-temperature on 2021-01-01
INFO:api_client:Fetching relative-humidity data for 2021-01-01
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-01-01
INFO:api_client:Fetching rainfall data for 2021-01-01
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-01-01
INFO:api_client:Fetching wind-speed data for 2021-01-01
INFO:api_client:Fetched 25 readings for wind-speed on 2021-01-01
ERROR:__main__:Error during ingestion for date 2021-01-01: string index out of range




INFO:__main__:Starting ingestion for date: 2021-01-02
INFO:api_client:Fetching air-temperature data for 2021-01-02
INFO:api_client:No data found for URL: https://api-open.data.gov.sg/v2/real-time/api/air-temperature
INFO:api_client:Fetched 0 readings for air-temperature on 2021-01-02
INFO:api_client:Fetching relative-humidity data for 2021-01-02
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:No data found for URL: https://api-open.data.gov.sg/v2/real-time/api/relative-humidity
INFO:api_client:Fetched 0 readings for relative-humidity on 2021-01-02
INFO:api_client:Fetching rainfall data for 2021-01-02
INFO:api_client:No data found for URL: https://api-open.data.gov.sg/v2/real-time/api/rainfall
INFO:api_client:Fetched 0 readings for rainfall on 2021-01-02
INFO:api_client:Fetching wind-speed data for 2021-01-02
INFO:api_client:No data found for URL: https://api-open.data.gov.sg/v2/real-time/api/wind-speed
INFO:api_client:Fetched 0 readings for wind-speed on 2021-01-02
INFO:loaders:Total records loaded: 0
INFO:__main__:Completed ingestion for date: 2021-01-02




INFO:__main__:Starting ingestion for date: 2021-01-03
INFO:api_client:Fetching air-temperature data for 2021-01-03
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:No data found for URL: https://api-open.data.gov.sg/v2/real-time/api/air-temperature
INFO:api_client:Fetched 0 readings for air-temperature on 2021-01-03
INFO:api_client:Fetching relative-humidity data for 2021-01-03
INFO:api_client:No data found for URL: https://api-open.data.gov.sg/v2/real-time/api/relative-humidity
INFO:api_client:Fetched 0 readings for relative-humidity on 2021-01-03
INFO:api_client:Fetching rainfall data for 2021-01-03
INFO:api_client:No data found for URL: https://api-open.data.gov.sg/v2/real-time/api/rainfall
INFO:api_client:Fetched 0 readings for rainfall on 2021-01-03
INFO:api_client:Fetching wind-speed data for 2021-01-03
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:No data found for URL: https://api-open.data.gov.sg/v2/real-time/api/wind-speed
INFO:api_client:Fetched 0 readings for wind-speed on 2021-01-03
INFO:loaders:Total records loaded: 0
INFO:__main__:Completed ingestion for date: 2021-01-03
INFO:__main__:Starting ingestion for date: 2021-01-04
INFO:api_client:Fetching air-temperature data for 2021-01-04
INFO:api_client:No data found for URL: https://api-open.data.gov.sg/v2/real-time/api/air-temperature
INFO:api_client:Fetched 0 readings for air-temperature on 2021-01-04
INFO:api_client:Fetching relative-humidity data for 2021-01-04
INFO:api_client:No data found for URL: https://api-open.data.gov.sg/v2/real-time/api/relative-humidity
INFO:api_client:Fetched 0 readings for relative-humidity on 2021-01-04
INFO:api_client:Fetching rainfall data for 2021-01-04
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:No data found for URL: https://api-open.data.gov.sg/v2/real-time/api/rainfall
INFO:api_client:Fetched 0 readings for rainfall on 2021-01-04
INFO:api_client:Fetching wind-speed data for 2021-01-04
INFO:api_client:No data found for URL: https://api-open.data.gov.sg/v2/real-time/api/wind-speed
INFO:api_client:Fetched 0 readings for wind-speed on 2021-01-04
INFO:loaders:Total records loaded: 0
INFO:__main__:Completed ingestion for date: 2021-01-04
INFO:__main__:Starting ingestion for date: 2021-01-05
INFO:api_client:Fetching air-temperature data for 2021-01-05
INFO:api_client:Fetched 25 readings for air-temperature on 2021-01-05
INFO:api_client:Fetching relative-humidity data for 2021-01-05
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-01-05
INFO:api_client:Fetching rainfall data for 2021-01-05
INFO:api_client:Fetched 25 readings for rainfall on 2021-01-05
INFO:api_client:Fetching wind-speed data for 2021-01-05
INFO:api_client:Fetched 25 readings for wind-speed on 2021-01-05
ERROR:__main__:Error during ingestion for date 2021-01-05: string index out of range
INFO:__main__:Starting ingestion for date: 2021-01-06
INFO:api_client:Fetching air-temperature data for 2021-01-06
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-01-06
INFO:api_client:Fetching relative-humidity data for 2021-01-06
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-01-06
INFO:api_client:Fetching rainfall data for 2021-01-06
INFO:api_client:Fetched 25 readings for rainfall on 2021-01-06
INFO:api_client:Fetching wind-speed data for 2021-01-06
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-01-06
ERROR:__main__:Error during ingestion for date 2021-01-06: string index out of range
INFO:__main__:Starting ingestion for date: 2021-01-07
INFO:api_client:Fetching air-temperature data for 2021-01-07
INFO:api_client:Fetched 25 readings for air-temperature on 2021-01-07
INFO:api_client:Fetching relative-humidity data for 2021-01-07
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-01-07
INFO:api_client:Fetching rainfall data for 2021-01-07
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-01-07
INFO:api_client:Fetching wind-speed data for 2021-01-07
INFO:api_client:Fetched 25 readings for wind-speed on 2021-01-07
ERROR:__main__:Error during ingestion for date 2021-01-07: string index out of range
INFO:__main__:Starting ingestion for date: 2021-01-08
INFO:api_client:Fetching air-temperature data for 2021-01-08
INFO:api_client:Fetched 25 readings for air-temperature on 2021-01-08
INFO:api_client:Fetching relative-humidity data for 2021-01-08
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-01-08
INFO:api_client:Fetching rainfall data for 2021-01-08
INFO:api_client:Fetched 25 readings for rainfall on 2021-01-08
INFO:api_client:Fetching wind-speed data for 2021-01-08
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-01-08
ERROR:__main__:Error during ingestion for date 2021-01-08: string index out of range
INFO:__main__:Starting ingestion for date: 2021-01-09
INFO:api_client:Fetching air-temperature data for 2021-01-09
INFO:api_client:Fetched 25 readings for air-temperature on 2021-01-09
INFO:api_client:Fetching relative-humidity data for 2021-01-09
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-01-09
INFO:api_client:Fetching rainfall data for 2021-01-09
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-01-09
INFO:api_client:Fetching wind-speed data for 2021-01-09
INFO:api_client:Fetched 25 readings for wind-speed on 2021-01-09
ERROR:__main__:Error during ingestion for date 2021-01-09: string index out of range
INFO:__main__:Starting ingestion for date: 2021-01-10
INFO:api_client:Fetching air-temperature data for 2021-01-10
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-01-10
INFO:api_client:Fetching relative-humidity data for 2021-01-10
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-01-10
INFO:api_client:Fetching rainfall data for 2021-01-10
WARNING:api_client:Rate limited. Waiting 2 seconds...






...





INFO:api_client:Fetched 25 readings for rainfall on 2021-02-03
INFO:api_client:Fetching wind-speed data for 2021-02-03
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-03
ERROR:__main__:Error during ingestion for date 2021-02-03: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-04
INFO:api_client:Fetching air-temperature data for 2021-02-04
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-04
INFO:api_client:Fetching relative-humidity data for 2021-02-04
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-04
INFO:api_client:Fetching rainfall data for 2021-02-04
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-04
INFO:api_client:Fetching wind-speed data for 2021-02-04
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-04
ERROR:__main__:Error during ingestion for date 2021-02-04: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-05
INFO:api_client:Fetching air-temperature data for 2021-02-05
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-05
INFO:api_client:Fetching relative-humidity data for 2021-02-05
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
WARNING:api_client:Rate limited. Waiting 6 seconds...
ERROR:api_client:Invalid response structure for relative-humidity on 2021-02-05
INFO:api_client:Fetched 0 readings for relative-humidity on 2021-02-05
INFO:api_client:Fetching rainfall data for 2021-02-05
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-05
INFO:api_client:Fetching wind-speed data for 2021-02-05
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-05
ERROR:__main__:Error during ingestion for date 2021-02-05: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-06
INFO:api_client:Fetching air-temperature data for 2021-02-06
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-06
INFO:api_client:Fetching relative-humidity data for 2021-02-06
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-06
INFO:api_client:Fetching rainfall data for 2021-02-06
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-06
INFO:api_client:Fetching wind-speed data for 2021-02-06
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-06
ERROR:__main__:Error during ingestion for date 2021-02-06: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-07
INFO:api_client:Fetching air-temperature data for 2021-02-07
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-07
INFO:api_client:Fetching relative-humidity data for 2021-02-07
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-07
INFO:api_client:Fetching rainfall data for 2021-02-07
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-07
INFO:api_client:Fetching wind-speed data for 2021-02-07
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-07
ERROR:__main__:Error during ingestion for date 2021-02-07: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-08
INFO:api_client:Fetching air-temperature data for 2021-02-08
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-08
INFO:api_client:Fetching relative-humidity data for 2021-02-08
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-08
INFO:api_client:Fetching rainfall data for 2021-02-08
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-08
INFO:api_client:Fetching wind-speed data for 2021-02-08
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-08
ERROR:__main__:Error during ingestion for date 2021-02-08: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-09
INFO:api_client:Fetching air-temperature data for 2021-02-09
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-09
INFO:api_client:Fetching relative-humidity data for 2021-02-09
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-09
INFO:api_client:Fetching rainfall data for 2021-02-09
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-09
INFO:api_client:Fetching wind-speed data for 2021-02-09
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-09
ERROR:__main__:Error during ingestion for date 2021-02-09: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-10
INFO:api_client:Fetching air-temperature data for 2021-02-10
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-10
INFO:api_client:Fetching relative-humidity data for 2021-02-10
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-10
INFO:api_client:Fetching rainfall data for 2021-02-10
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-10
INFO:api_client:Fetching wind-speed data for 2021-02-10
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-10
ERROR:__main__:Error during ingestion for date 2021-02-10: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-11
INFO:api_client:Fetching air-temperature data for 2021-02-11
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-11
INFO:api_client:Fetching relative-humidity data for 2021-02-11
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-11
INFO:api_client:Fetching rainfall data for 2021-02-11
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-11
INFO:api_client:Fetching wind-speed data for 2021-02-11
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-11
ERROR:__main__:Error during ingestion for date 2021-02-11: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-12
INFO:api_client:Fetching air-temperature data for 2021-02-12
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-12
INFO:api_client:Fetching relative-humidity data for 2021-02-12
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-12
INFO:api_client:Fetching rainfall data for 2021-02-12
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-12
INFO:api_client:Fetching wind-speed data for 2021-02-12
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-12
ERROR:__main__:Error during ingestion for date 2021-02-12: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-13
INFO:api_client:Fetching air-temperature data for 2021-02-13
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-13
INFO:api_client:Fetching relative-humidity data for 2021-02-13
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
```