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
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-13
ERROR:__main__:Error during ingestion for date 2021-02-13: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-14
INFO:api_client:Fetching air-temperature data for 2021-02-14
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-14
INFO:api_client:Fetching relative-humidity data for 2021-02-14
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-14
INFO:api_client:Fetching rainfall data for 2021-02-14
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-14
INFO:api_client:Fetching wind-speed data for 2021-02-14
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-14
ERROR:__main__:Error during ingestion for date 2021-02-14: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-15
INFO:api_client:Fetching air-temperature data for 2021-02-15
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-15
INFO:api_client:Fetching relative-humidity data for 2021-02-15
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-15
INFO:api_client:Fetching rainfall data for 2021-02-15
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-15
INFO:api_client:Fetching wind-speed data for 2021-02-15
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-15
ERROR:__main__:Error during ingestion for date 2021-02-15: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-16
INFO:api_client:Fetching air-temperature data for 2021-02-16
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-16
INFO:api_client:Fetching relative-humidity data for 2021-02-16
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-16
INFO:api_client:Fetching rainfall data for 2021-02-16
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-16
INFO:api_client:Fetching wind-speed data for 2021-02-16
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
WARNING:api_client:Rate limited. Waiting 6 seconds...
ERROR:api_client:Invalid response structure for wind-speed on 2021-02-16
INFO:api_client:Fetched 0 readings for wind-speed on 2021-02-16
ERROR:__main__:Error during ingestion for date 2021-02-16: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-17
INFO:api_client:Fetching air-temperature data for 2021-02-17
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-17
INFO:api_client:Fetching relative-humidity data for 2021-02-17
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-17
INFO:api_client:Fetching rainfall data for 2021-02-17
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-17
INFO:api_client:Fetching wind-speed data for 2021-02-17
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-17
ERROR:__main__:Error during ingestion for date 2021-02-17: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-18
INFO:api_client:Fetching air-temperature data for 2021-02-18
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-18
INFO:api_client:Fetching relative-humidity data for 2021-02-18
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-18
INFO:api_client:Fetching rainfall data for 2021-02-18
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-18
INFO:api_client:Fetching wind-speed data for 2021-02-18
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-18
ERROR:__main__:Error during ingestion for date 2021-02-18: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-19
INFO:api_client:Fetching air-temperature data for 2021-02-19
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-19
INFO:api_client:Fetching relative-humidity data for 2021-02-19
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-19
INFO:api_client:Fetching rainfall data for 2021-02-19
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-19
INFO:api_client:Fetching wind-speed data for 2021-02-19
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-19
ERROR:__main__:Error during ingestion for date 2021-02-19: string index out of range

INFO:__main__:Starting ingestion for date: 2021-02-20
INFO:api_client:Fetching air-temperature data for 2021-02-20
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-20
INFO:api_client:Fetching relative-humidity data for 2021-02-20
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-20
INFO:api_client:Fetching rainfall data for 2021-02-20
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-20
INFO:api_client:Fetching wind-speed data for 2021-02-20
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-20
ERROR:__main__:Error during ingestion for date 2021-02-20: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-21
INFO:api_client:Fetching air-temperature data for 2021-02-21
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-21
INFO:api_client:Fetching relative-humidity data for 2021-02-21
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-21
INFO:api_client:Fetching rainfall data for 2021-02-21
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-21
INFO:api_client:Fetching wind-speed data for 2021-02-21
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-21
ERROR:__main__:Error during ingestion for date 2021-02-21: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-22
INFO:api_client:Fetching air-temperature data for 2021-02-22
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-22
INFO:api_client:Fetching relative-humidity data for 2021-02-22
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-22
INFO:api_client:Fetching rainfall data for 2021-02-22
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-22
INFO:api_client:Fetching wind-speed data for 2021-02-22
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-22
ERROR:__main__:Error during ingestion for date 2021-02-22: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-23
INFO:api_client:Fetching air-temperature data for 2021-02-23
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-23
INFO:api_client:Fetching relative-humidity data for 2021-02-23
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-23
INFO:api_client:Fetching rainfall data for 2021-02-23
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-23
INFO:api_client:Fetching wind-speed data for 2021-02-23
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-23
ERROR:__main__:Error during ingestion for date 2021-02-23: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-24
INFO:api_client:Fetching air-temperature data for 2021-02-24
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-24
INFO:api_client:Fetching relative-humidity data for 2021-02-24
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-24
INFO:api_client:Fetching rainfall data for 2021-02-24
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-24
INFO:api_client:Fetching wind-speed data for 2021-02-24
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-24
ERROR:__main__:Error during ingestion for date 2021-02-24: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-25
INFO:api_client:Fetching air-temperature data for 2021-02-25
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-25
INFO:api_client:Fetching relative-humidity data for 2021-02-25
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-25
INFO:api_client:Fetching rainfall data for 2021-02-25
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-25
INFO:api_client:Fetching wind-speed data for 2021-02-25
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-25
ERROR:__main__:Error during ingestion for date 2021-02-25: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-26
INFO:api_client:Fetching air-temperature data for 2021-02-26
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-26
INFO:api_client:Fetching relative-humidity data for 2021-02-26
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-26
INFO:api_client:Fetching rainfall data for 2021-02-26
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-26
INFO:api_client:Fetching wind-speed data for 2021-02-26
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-26
ERROR:__main__:Error during ingestion for date 2021-02-26: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-27
INFO:api_client:Fetching air-temperature data for 2021-02-27
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-27
INFO:api_client:Fetching relative-humidity data for 2021-02-27
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-27
INFO:api_client:Fetching rainfall data for 2021-02-27
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-27
INFO:api_client:Fetching wind-speed data for 2021-02-27
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-27
ERROR:__main__:Error during ingestion for date 2021-02-27: string index out of range
INFO:__main__:Starting ingestion for date: 2021-02-28
INFO:api_client:Fetching air-temperature data for 2021-02-28
INFO:api_client:Fetched 25 readings for air-temperature on 2021-02-28
INFO:api_client:Fetching relative-humidity data for 2021-02-28
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-02-28
INFO:api_client:Fetching rainfall data for 2021-02-28
INFO:api_client:Fetched 25 readings for rainfall on 2021-02-28
INFO:api_client:Fetching wind-speed data for 2021-02-28
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-02-28
ERROR:__main__:Error during ingestion for date 2021-02-28: string index out of range
















INFO:__main__:Starting ingestion for date: 2021-03-01
INFO:api_client:Fetching air-temperature data for 2021-03-01
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-01
INFO:api_client:Fetching relative-humidity data for 2021-03-01
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-01
INFO:api_client:Fetching rainfall data for 2021-03-01
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-01
INFO:api_client:Fetching wind-speed data for 2021-03-01
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-01
ERROR:__main__:Error during ingestion for date 2021-03-01: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-02
INFO:api_client:Fetching air-temperature data for 2021-03-02
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-02
INFO:api_client:Fetching relative-humidity data for 2021-03-02
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-02
INFO:api_client:Fetching rainfall data for 2021-03-02
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-02
INFO:api_client:Fetching wind-speed data for 2021-03-02
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-02
ERROR:__main__:Error during ingestion for date 2021-03-02: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-03
INFO:api_client:Fetching air-temperature data for 2021-03-03
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-03
INFO:api_client:Fetching relative-humidity data for 2021-03-03
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-03
INFO:api_client:Fetching rainfall data for 2021-03-03
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-03
INFO:api_client:Fetching wind-speed data for 2021-03-03
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-03
ERROR:__main__:Error during ingestion for date 2021-03-03: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-04
INFO:api_client:Fetching air-temperature data for 2021-03-04
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-04
INFO:api_client:Fetching relative-humidity data for 2021-03-04
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-04
INFO:api_client:Fetching rainfall data for 2021-03-04
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-04
INFO:api_client:Fetching wind-speed data for 2021-03-04
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-04
ERROR:__main__:Error during ingestion for date 2021-03-04: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-05
INFO:api_client:Fetching air-temperature data for 2021-03-05
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-05
INFO:api_client:Fetching relative-humidity data for 2021-03-05
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-05
INFO:api_client:Fetching rainfall data for 2021-03-05
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-05
INFO:api_client:Fetching wind-speed data for 2021-03-05
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-05
ERROR:__main__:Error during ingestion for date 2021-03-05: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-06
INFO:api_client:Fetching air-temperature data for 2021-03-06
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-06
INFO:api_client:Fetching relative-humidity data for 2021-03-06
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-06
INFO:api_client:Fetching rainfall data for 2021-03-06
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-06
INFO:api_client:Fetching wind-speed data for 2021-03-06
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-06
ERROR:__main__:Error during ingestion for date 2021-03-06: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-07
INFO:api_client:Fetching air-temperature data for 2021-03-07
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-07
INFO:api_client:Fetching relative-humidity data for 2021-03-07
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-07
INFO:api_client:Fetching rainfall data for 2021-03-07
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-07
INFO:api_client:Fetching wind-speed data for 2021-03-07
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-07
ERROR:__main__:Error during ingestion for date 2021-03-07: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-08
INFO:api_client:Fetching air-temperature data for 2021-03-08
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-08
INFO:api_client:Fetching relative-humidity data for 2021-03-08
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-08
INFO:api_client:Fetching rainfall data for 2021-03-08
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-08
INFO:api_client:Fetching wind-speed data for 2021-03-08
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-08
ERROR:__main__:Error during ingestion for date 2021-03-08: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-09
INFO:api_client:Fetching air-temperature data for 2021-03-09
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-09
INFO:api_client:Fetching relative-humidity data for 2021-03-09
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-09
INFO:api_client:Fetching rainfall data for 2021-03-09
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-09
INFO:api_client:Fetching wind-speed data for 2021-03-09
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-09
ERROR:__main__:Error during ingestion for date 2021-03-09: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-10
INFO:api_client:Fetching air-temperature data for 2021-03-10
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-10
INFO:api_client:Fetching relative-humidity data for 2021-03-10
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-10
INFO:api_client:Fetching rainfall data for 2021-03-10
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-10
INFO:api_client:Fetching wind-speed data for 2021-03-10
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-10
ERROR:__main__:Error during ingestion for date 2021-03-10: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-11
INFO:api_client:Fetching air-temperature data for 2021-03-11
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-11
INFO:api_client:Fetching relative-humidity data for 2021-03-11
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-11
INFO:api_client:Fetching rainfall data for 2021-03-11
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-11
INFO:api_client:Fetching wind-speed data for 2021-03-11
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-11
ERROR:__main__:Error during ingestion for date 2021-03-11: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-12
INFO:api_client:Fetching air-temperature data for 2021-03-12
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-12
INFO:api_client:Fetching relative-humidity data for 2021-03-12
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-12
INFO:api_client:Fetching rainfall data for 2021-03-12
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-12
INFO:api_client:Fetching wind-speed data for 2021-03-12
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-12
ERROR:__main__:Error during ingestion for date 2021-03-12: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-13
INFO:api_client:Fetching air-temperature data for 2021-03-13
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-13
INFO:api_client:Fetching relative-humidity data for 2021-03-13
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-13
INFO:api_client:Fetching rainfall data for 2021-03-13
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-13
INFO:api_client:Fetching wind-speed data for 2021-03-13
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-13
ERROR:__main__:Error during ingestion for date 2021-03-13: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-14
INFO:api_client:Fetching air-temperature data for 2021-03-14
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-14
INFO:api_client:Fetching relative-humidity data for 2021-03-14
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-14
INFO:api_client:Fetching rainfall data for 2021-03-14
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-14
INFO:api_client:Fetching wind-speed data for 2021-03-14
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-14
ERROR:__main__:Error during ingestion for date 2021-03-14: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-15
INFO:api_client:Fetching air-temperature data for 2021-03-15
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-15
INFO:api_client:Fetching relative-humidity data for 2021-03-15
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-15
INFO:api_client:Fetching rainfall data for 2021-03-15
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-15
INFO:api_client:Fetching wind-speed data for 2021-03-15
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-15
ERROR:__main__:Error during ingestion for date 2021-03-15: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-16
INFO:api_client:Fetching air-temperature data for 2021-03-16
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-16
INFO:api_client:Fetching relative-humidity data for 2021-03-16
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-16
INFO:api_client:Fetching rainfall data for 2021-03-16
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-16
INFO:api_client:Fetching wind-speed data for 2021-03-16
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-16
ERROR:__main__:Error during ingestion for date 2021-03-16: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-17
INFO:api_client:Fetching air-temperature data for 2021-03-17
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-17
INFO:api_client:Fetching relative-humidity data for 2021-03-17
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-17
INFO:api_client:Fetching rainfall data for 2021-03-17
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-17
INFO:api_client:Fetching wind-speed data for 2021-03-17
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-17
ERROR:__main__:Error during ingestion for date 2021-03-17: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-18
INFO:api_client:Fetching air-temperature data for 2021-03-18
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-18
INFO:api_client:Fetching relative-humidity data for 2021-03-18
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-18
INFO:api_client:Fetching rainfall data for 2021-03-18
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-18
INFO:api_client:Fetching wind-speed data for 2021-03-18
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-18
ERROR:__main__:Error during ingestion for date 2021-03-18: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-19
INFO:api_client:Fetching air-temperature data for 2021-03-19
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-19
INFO:api_client:Fetching relative-humidity data for 2021-03-19
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-19
INFO:api_client:Fetching rainfall data for 2021-03-19
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-19
INFO:api_client:Fetching wind-speed data for 2021-03-19
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-19
ERROR:__main__:Error during ingestion for date 2021-03-19: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-20
INFO:api_client:Fetching air-temperature data for 2021-03-20
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-20
INFO:api_client:Fetching relative-humidity data for 2021-03-20
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-20
INFO:api_client:Fetching rainfall data for 2021-03-20
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-20
INFO:api_client:Fetching wind-speed data for 2021-03-20
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-20
ERROR:__main__:Error during ingestion for date 2021-03-20: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-21
INFO:api_client:Fetching air-temperature data for 2021-03-21
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-21
INFO:api_client:Fetching relative-humidity data for 2021-03-21
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-21
INFO:api_client:Fetching rainfall data for 2021-03-21
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-21
INFO:api_client:Fetching wind-speed data for 2021-03-21
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-21
ERROR:__main__:Error during ingestion for date 2021-03-21: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-22
INFO:api_client:Fetching air-temperature data for 2021-03-22
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-22
INFO:api_client:Fetching relative-humidity data for 2021-03-22
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-22
INFO:api_client:Fetching rainfall data for 2021-03-22
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-22
INFO:api_client:Fetching wind-speed data for 2021-03-22
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-22
ERROR:__main__:Error during ingestion for date 2021-03-22: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-23
INFO:api_client:Fetching air-temperature data for 2021-03-23
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-23
INFO:api_client:Fetching relative-humidity data for 2021-03-23
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-23
INFO:api_client:Fetching rainfall data for 2021-03-23
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-23
INFO:api_client:Fetching wind-speed data for 2021-03-23
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-23
ERROR:__main__:Error during ingestion for date 2021-03-23: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-24
INFO:api_client:Fetching air-temperature data for 2021-03-24
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-24
INFO:api_client:Fetching relative-humidity data for 2021-03-24
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-24
INFO:api_client:Fetching rainfall data for 2021-03-24
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-24
INFO:api_client:Fetching wind-speed data for 2021-03-24
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-24
ERROR:__main__:Error during ingestion for date 2021-03-24: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-25
INFO:api_client:Fetching air-temperature data for 2021-03-25
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-25
INFO:api_client:Fetching relative-humidity data for 2021-03-25
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-25
INFO:api_client:Fetching rainfall data for 2021-03-25
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-25
INFO:api_client:Fetching wind-speed data for 2021-03-25
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-25
ERROR:__main__:Error during ingestion for date 2021-03-25: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-26
INFO:api_client:Fetching air-temperature data for 2021-03-26
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-26
INFO:api_client:Fetching relative-humidity data for 2021-03-26
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-26
INFO:api_client:Fetching rainfall data for 2021-03-26
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-26
INFO:api_client:Fetching wind-speed data for 2021-03-26
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-26
ERROR:__main__:Error during ingestion for date 2021-03-26: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-27
INFO:api_client:Fetching air-temperature data for 2021-03-27
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-27
INFO:api_client:Fetching relative-humidity data for 2021-03-27
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-27
INFO:api_client:Fetching rainfall data for 2021-03-27
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-27
INFO:api_client:Fetching wind-speed data for 2021-03-27
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-27
ERROR:__main__:Error during ingestion for date 2021-03-27: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-28
INFO:api_client:Fetching air-temperature data for 2021-03-28
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-28
INFO:api_client:Fetching relative-humidity data for 2021-03-28
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-28
INFO:api_client:Fetching rainfall data for 2021-03-28
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-28
INFO:api_client:Fetching wind-speed data for 2021-03-28
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-28
ERROR:__main__:Error during ingestion for date 2021-03-28: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-29
INFO:api_client:Fetching air-temperature data for 2021-03-29
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
WARNING:api_client:Rate limited. Waiting 6 seconds...
ERROR:api_client:Invalid response structure for air-temperature on 2021-03-29
INFO:api_client:Fetched 0 readings for air-temperature on 2021-03-29
INFO:api_client:Fetching relative-humidity data for 2021-03-29
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-29
INFO:api_client:Fetching rainfall data for 2021-03-29
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-29
INFO:api_client:Fetching wind-speed data for 2021-03-29
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-29
ERROR:__main__:Error during ingestion for date 2021-03-29: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-30
INFO:api_client:Fetching air-temperature data for 2021-03-30
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-30
INFO:api_client:Fetching relative-humidity data for 2021-03-30
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-30
INFO:api_client:Fetching rainfall data for 2021-03-30
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-30
INFO:api_client:Fetching wind-speed data for 2021-03-30
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-30
ERROR:__main__:Error during ingestion for date 2021-03-30: string index out of range
INFO:__main__:Starting ingestion for date: 2021-03-31
INFO:api_client:Fetching air-temperature data for 2021-03-31
INFO:api_client:Fetched 25 readings for air-temperature on 2021-03-31
INFO:api_client:Fetching relative-humidity data for 2021-03-31
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-03-31
INFO:api_client:Fetching rainfall data for 2021-03-31
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-03-31
INFO:api_client:Fetching wind-speed data for 2021-03-31
INFO:api_client:Fetched 25 readings for wind-speed on 2021-03-31
ERROR:__main__:Error during ingestion for date 2021-03-31: string index out of range









INFO:__main__:Starting ingestion for date: 2021-04-01
INFO:api_client:Fetching air-temperature data for 2021-04-01
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-04-01
INFO:api_client:Fetching relative-humidity data for 2021-04-01
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-04-01
INFO:api_client:Fetching rainfall data for 2021-04-01
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-04-01
INFO:api_client:Fetching wind-speed data for 2021-04-01
INFO:api_client:Fetched 25 readings for wind-speed on 2021-04-01
ERROR:__main__:Error during ingestion for date 2021-04-01: string index out of range
INFO:__main__:Starting ingestion for date: 2021-04-02
INFO:api_client:Fetching air-temperature data for 2021-04-02
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-04-02
INFO:api_client:Fetching relative-humidity data for 2021-04-02
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-04-02
INFO:api_client:Fetching rainfall data for 2021-04-02
INFO:api_client:Fetched 25 readings for rainfall on 2021-04-02
INFO:api_client:Fetching wind-speed data for 2021-04-02
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-04-02
ERROR:__main__:Error during ingestion for date 2021-04-02: string index out of range
INFO:__main__:Starting ingestion for date: 2021-04-03
INFO:api_client:Fetching air-temperature data for 2021-04-03
INFO:api_client:Fetched 25 readings for air-temperature on 2021-04-03
INFO:api_client:Fetching relative-humidity data for 2021-04-03
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-04-03
INFO:api_client:Fetching rainfall data for 2021-04-03
INFO:api_client:Fetched 25 readings for rainfall on 2021-04-03
INFO:api_client:Fetching wind-speed data for 2021-04-03
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-04-03
ERROR:__main__:Error during ingestion for date 2021-04-03: string index out of range
INFO:__main__:Starting ingestion for date: 2021-04-04
INFO:api_client:Fetching air-temperature data for 2021-04-04
INFO:api_client:Fetched 25 readings for air-temperature on 2021-04-04
INFO:api_client:Fetching relative-humidity data for 2021-04-04
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-04-04
INFO:api_client:Fetching rainfall data for 2021-04-04
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-04-04
INFO:api_client:Fetching wind-speed data for 2021-04-04
INFO:api_client:Fetched 25 readings for wind-speed on 2021-04-04
ERROR:__main__:Error during ingestion for date 2021-04-04: string index out of range
INFO:__main__:Starting ingestion for date: 2021-04-05
INFO:api_client:Fetching air-temperature data for 2021-04-05
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-04-05
INFO:api_client:Fetching relative-humidity data for 2021-04-05
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-04-05
INFO:api_client:Fetching rainfall data for 2021-04-05
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-04-05
INFO:api_client:Fetching wind-speed data for 2021-04-05
INFO:api_client:Fetched 25 readings for wind-speed on 2021-04-05
ERROR:__main__:Error during ingestion for date 2021-04-05: string index out of range
INFO:__main__:Starting ingestion for date: 2021-04-06
INFO:api_client:Fetching air-temperature data for 2021-04-06
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-04-06
INFO:api_client:Fetching relative-humidity data for 2021-04-06
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-04-06
INFO:api_client:Fetching rainfall data for 2021-04-06
INFO:api_client:Fetched 25 readings for rainfall on 2021-04-06
INFO:api_client:Fetching wind-speed data for 2021-04-06
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-04-06
ERROR:__main__:Error during ingestion for date 2021-04-06: string index out of range
INFO:__main__:Starting ingestion for date: 2021-04-07
INFO:api_client:Fetching air-temperature data for 2021-04-07
INFO:api_client:Fetched 25 readings for air-temperature on 2021-04-07
INFO:api_client:Fetching relative-humidity data for 2021-04-07
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-04-07
INFO:api_client:Fetching rainfall data for 2021-04-07
INFO:api_client:Fetched 25 readings for rainfall on 2021-04-07
INFO:api_client:Fetching wind-speed data for 2021-04-07
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-04-07
ERROR:__main__:Error during ingestion for date 2021-04-07: string index out of range
INFO:__main__:Starting ingestion for date: 2021-04-08
INFO:api_client:Fetching air-temperature data for 2021-04-08
INFO:api_client:Fetched 25 readings for air-temperature on 2021-04-08
INFO:api_client:Fetching relative-humidity data for 2021-04-08
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-04-08
INFO:api_client:Fetching rainfall data for 2021-04-08
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-04-08
INFO:api_client:Fetching wind-speed data for 2021-04-08
INFO:api_client:Fetched 25 readings for wind-speed on 2021-04-08
ERROR:__main__:Error during ingestion for date 2021-04-08: string index out of range
INFO:__main__:Starting ingestion for date: 2021-04-09
INFO:api_client:Fetching air-temperature data for 2021-04-09
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-04-09
INFO:api_client:Fetching relative-humidity data for 2021-04-09
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-04-09
INFO:api_client:Fetching rainfall data for 2021-04-09
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-04-09
INFO:api_client:Fetching wind-speed data for 2021-04-09
INFO:api_client:Fetched 25 readings for wind-speed on 2021-04-09
ERROR:__main__:Error during ingestion for date 2021-04-09: string index out of range
INFO:__main__:Starting ingestion for date: 2021-04-10
INFO:api_client:Fetching air-temperature data for 2021-04-10
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-04-10
INFO:api_client:Fetching relative-humidity data for 2021-04-10
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-04-10
INFO:api_client:Fetching rainfall data for 2021-04-10
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-04-10
INFO:api_client:Fetching wind-speed data for 2021-04-10
INFO:api_client:Fetched 25 readings for wind-speed on 2021-04-10
ERROR:__main__:Error during ingestion for date 2021-04-10: string index out of range
INFO:__main__:Starting ingestion for date: 2021-04-11
INFO:api_client:Fetching air-temperature data for 2021-04-11
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-04-11
INFO:api_client:Fetching relative-humidity data for 2021-04-11
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-04-11
INFO:api_client:Fetching rainfall data for 2021-04-11
INFO:api_client:Fetched 25 readings for rainfall on 2021-04-11
INFO:api_client:Fetching wind-speed data for 2021-04-11
INFO:api_client:Fetched 25 readings for wind-speed on 2021-04-11
ERROR:__main__:Error during ingestion for date 2021-04-11: string index out of range
INFO:__main__:Starting ingestion for date: 2021-04-12
INFO:api_client:Fetching air-temperature data for 2021-04-12
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-04-12
INFO:api_client:Fetching relative-humidity data for 2021-04-12
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-04-12
INFO:api_client:Fetching rainfall data for 2021-04-12
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-04-12
INFO:api_client:Fetching wind-speed data for 2021-04-12
INFO:api_client:Fetched 25 readings for wind-speed on 2021-04-12
ERROR:__main__:Error during ingestion for date 2021-04-12: string index out of range
INFO:__main__:Starting ingestion for date: 2021-04-13
INFO:api_client:Fetching air-temperature data for 2021-04-13
INFO:api_client:Fetched 25 readings for air-temperature on 2021-04-13
INFO:api_client:Fetching relative-humidity data for 2021-04-13
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-04-13
INFO:api_client:Fetching rainfall data for 2021-04-13
INFO:api_client:Fetched 25 readings for rainfall on 2021-04-13
INFO:api_client:Fetching wind-speed data for 2021-04-13
INFO:api_client:Fetched 25 readings for wind-speed on 2021-04-13
ERROR:__main__:Error during ingestion for date 2021-04-13: string index out of range
INFO:__main__:Starting ingestion for date: 2021-04-14
INFO:api_client:Fetching air-temperature data for 2021-04-14
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for air-temperature on 2021-04-14
INFO:api_client:Fetching relative-humidity data for 2021-04-14
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-04-14
INFO:api_client:Fetching rainfall data for 2021-04-14
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for rainfall on 2021-04-14
INFO:api_client:Fetching wind-speed data for 2021-04-14
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-04-14
ERROR:__main__:Error during ingestion for date 2021-04-14: string index out of range
INFO:__main__:Starting ingestion for date: 2021-04-15
INFO:api_client:Fetching air-temperature data for 2021-04-15
INFO:api_client:Fetched 25 readings for air-temperature on 2021-04-15
INFO:api_client:Fetching relative-humidity data for 2021-04-15
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-04-15
INFO:api_client:Fetching rainfall data for 2021-04-15
INFO:api_client:Fetched 25 readings for rainfall on 2021-04-15
INFO:api_client:Fetching wind-speed data for 2021-04-15
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-04-15
ERROR:__main__:Error during ingestion for date 2021-04-15: string index out of range
INFO:__main__:Starting ingestion for date: 2021-04-16
INFO:api_client:Fetching air-temperature data for 2021-04-16
INFO:api_client:Fetched 25 readings for air-temperature on 2021-04-16
INFO:api_client:Fetching relative-humidity data for 2021-04-16
WARNING:api_client:Rate limited. Waiting 2 seconds...
WARNING:api_client:Rate limited. Waiting 4 seconds...
INFO:api_client:Fetched 25 readings for relative-humidity on 2021-04-16
INFO:api_client:Fetching rainfall data for 2021-04-16
INFO:api_client:Fetched 25 readings for rainfall on 2021-04-16
INFO:api_client:Fetching wind-speed data for 2021-04-16
WARNING:api_client:Rate limited. Waiting 2 seconds...
INFO:api_client:Fetched 25 readings for wind-speed on 2021-04-16
ERROR:__main__:Error during ingestion for date 2021-04-16: string index out of range

```