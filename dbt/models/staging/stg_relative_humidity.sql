-- stg_relative_humidity.sql
-- Staging model for relative humidity data

{{ config(
    materialized='view'
) }}

WITH source AS (
    SELECT 
        timestamp AS reading_timestamp,
        station_id,
        humidity,
        unit,
        ingest_timestamp
    FROM {{ source('weather_data', 'raw_relative_humidity') }}
),

renamed AS (
    SELECT
        reading_timestamp,
        station_id,
        humidity,
        unit,
        ingest_timestamp,
        DATE(reading_timestamp) AS date
    FROM source
)

SELECT * FROM renamed