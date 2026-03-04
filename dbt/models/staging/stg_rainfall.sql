-- stg_rainfall.sql
-- Staging model for rainfall data

{{ config(
    materialized='view'
) }}

WITH source AS (
    SELECT 
        timestamp AS reading_timestamp,
        station_id,
        rainfall,
        unit,
        ingest_timestamp
    FROM {{ source('weather_data', 'raw_rainfall') }}
),

renamed AS (
    SELECT
        reading_timestamp,
        station_id,
        rainfall,
        unit,
        ingest_timestamp,
        DATE(reading_timestamp) AS date
    FROM source
)

SELECT * FROM renamed