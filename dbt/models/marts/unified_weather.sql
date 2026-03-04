-- unified_weather.sql
-- Merged model combining all weather data types

{{ config(
    materialized='table',
    partition_by={
        "field": "reading_timestamp",
        "data_type": "timestamp",
        "granularity": "day"
    },
    cluster_by=["station_id", "reading_type"]
) }}

WITH temperature_data AS (
    SELECT 
        reading_timestamp,
        station_id,
        temperature,
        NULL AS humidity,
        NULL AS rainfall,
        NULL AS wind_speed,
        'temperature' AS reading_type,
        date,
        ingest_timestamp
    FROM {{ ref('stg_air_temperature') }}
),

humidity_data AS (
    SELECT 
        reading_timestamp,
        station_id,
        NULL AS temperature,
        humidity,
        NULL AS rainfall,
        NULL AS wind_speed,
        'humidity' AS reading_type,
        date,
        ingest_timestamp
    FROM {{ ref('stg_relative_humidity') }}
),

rainfall_data AS (
    SELECT 
        reading_timestamp,
        station_id,
        NULL AS temperature,
        NULL AS humidity,
        rainfall,
        NULL AS wind_speed,
        'rainfall' AS reading_type,
        date,
        ingest_timestamp
    FROM {{ ref('stg_rainfall') }}
),

wind_speed_data AS (
    SELECT 
        reading_timestamp,
        station_id,
        NULL AS temperature,
        NULL AS humidity,
        NULL AS rainfall,
        wind_speed,
        'wind_speed' AS reading_type,
        date,
        ingest_timestamp
    FROM {{ ref('stg_wind_speed') }}
)

SELECT * FROM temperature_data
UNION ALL
SELECT * FROM humidity_data
UNION ALL
SELECT * FROM rainfall_data
UNION ALL
SELECT * FROM wind_speed_data