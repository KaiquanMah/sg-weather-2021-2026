-- stg_air_temperature.sql
-- Staging model for air temperature data

{{ config(
    materialized='view'
) }}

WITH source AS (
    SELECT 
        timestamp AS reading_timestamp,
        station_id,
        temperature,
        unit,
        ingest_timestamp
    FROM {{ source('weather_data', 'raw_air_temperature') }}
),

renamed AS (
    SELECT
        reading_timestamp,
        station_id,
        temperature,
        unit,
        ingest_timestamp,
        DATE(reading_timestamp) AS date
    FROM source
)

SELECT * FROM renamed