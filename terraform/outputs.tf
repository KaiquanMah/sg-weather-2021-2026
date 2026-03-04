output "gcs_bucket_name" {
  description = "Name of the created GCS bucket"
  value       = google_storage_bucket.weather_raw_bucket.name
}

output "bigquery_dataset_id" {
  description = "ID of the created BigQuery dataset"
  value       = google_bigquery_dataset.weather_dataset.dataset_id
}

output "raw_air_temperature_table" {
  description = "Name of the raw air temperature table"
  value       = google_bigquery_table.raw_air_temperature.table_id
}

output "raw_relative_humidity_table" {
  description = "Name of the raw relative humidity table"
  value       = google_bigquery_table.raw_relative_humidity.table_id
}

output "raw_rainfall_table" {
  description = "Name of the raw rainfall table"
  value       = google_bigquery_table.raw_rainfall.table_id
}

output "raw_wind_speed_table" {
  description = "Name of the raw wind speed table"
  value       = google_bigquery_table.raw_wind_speed.table_id
}

output "unified_weather_table" {
  description = "Name of the unified weather table"
  value       = google_bigquery_table.unified_weather.table_id
}