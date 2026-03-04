-- stg_wind_speed.sql
-- Staging model for wind speed data

{{ config(
    materialized='view'
) }}

WITH source AS (
    SELECT 
        timestamp AS reading_timestamp,
        station_id,
        speed AS wind_speed,
        unit,
        ingest_timestamp
    FROM {{ source('weather_data', 'raw_wind_speed') }}
),

renamed AS (
    SELECT
        reading_timestamp,
        station_id,
        wind_speed,
        unit,
        ingest_timestamp,
        DATE(reading_timestamp) AS date
    FROM source
)

SELECT * FROM renamed