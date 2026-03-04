terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# GCS Bucket for raw weather data
resource "google_storage_bucket" "weather_raw_bucket" {
  name                        = "${var.project_id}-weather-raw-${random_string.bucket_suffix.result}"
  location                    = var.region
  force_destroy               = true
  uniform_bucket_level_access = true

  lifecycle_rule {
    condition {
      age = 30
    }
    action {
      type = "Delete"
    }
  }

  labels = {
    purpose = "weather-data-ingestion"
    owner   = "data-engineering-zoomcamp"
  }
}

# Random suffix for unique bucket name
resource "random_string" "bucket_suffix" {
  length  = 8
  special = false
  upper   = false
}

# BigQuery Dataset
resource "google_bigquery_dataset" "weather_dataset" {
  dataset_id    = var.dataset_id
  friendly_name = "Weather Data Analytics"
  description   = "Dataset for storing weather data from data.gov.sg APIs"
  location      = var.region

  labels = {
    purpose = "weather-analytics"
    owner   = "data-engineering-zoomcamp"
  }
}

# Raw table for air temperature data
resource "google_bigquery_table" "raw_air_temperature" {
  dataset_id = google_bigquery_dataset.weather_dataset.dataset_id
  table_id   = "raw_air_temperature"

  schema = jsonencode([
    {
      name        = "timestamp"
      type        = "TIMESTAMP"
      mode        = "REQUIRED"
      description = "Reading timestamp in SGT"
    },
    {
      name        = "station_id"
      type        = "STRING"
      mode        = "REQUIRED"
      description = "Weather station ID"
    },
    {
      name        = "temperature"
      type        = "FLOAT"
      mode        = "REQUIRED"
      description = "Air temperature in Celsius"
    },
    {
      name        = "unit"
      type        = "STRING"
      mode        = "NULLABLE"
      description = "Unit of measurement"
    },
    {
      name        = "ingest_timestamp"
      type        = "TIMESTAMP"
      mode        = "NULLABLE"
      description = "Timestamp when data was ingested"
    }
  ])

  time_partitioning {
    type = "DAY"
    field = "timestamp"
  }

  clustering = ["station_id"]

  labels = {
    source = "data.gov.sg"
    type   = "raw"
  }
}

# Raw table for relative humidity data
resource "google_bigquery_table" "raw_relative_humidity" {
  dataset_id = google_bigquery_dataset.weather_dataset.dataset_id
  table_id   = "raw_relative_humidity"

  schema = jsonencode([
    {
      name        = "timestamp"
      type        = "TIMESTAMP"
      mode        = "REQUIRED"
      description = "Reading timestamp in SGT"
    },
    {
      name        = "station_id"
      type        = "STRING"
      mode        = "REQUIRED"
      description = "Weather station ID"
    },
    {
      name        = "humidity"
      type        = "FLOAT"
      mode        = "REQUIRED"
      description = "Relative humidity percentage"
    },
    {
      name        = "unit"
      type        = "STRING"
      mode        = "NULLABLE"
      description = "Unit of measurement"
    },
    {
      name        = "ingest_timestamp"
      type        = "TIMESTAMP"
      mode        = "NULLABLE"
      description = "Timestamp when data was ingested"
    }
  ])

  time_partitioning {
    type = "DAY"
    field = "timestamp"
  }

  clustering = ["station_id"]

  labels = {
    source = "data.gov.sg"
    type   = "raw"
  }
}

# Raw table for rainfall data
resource "google_bigquery_table" "raw_rainfall" {
  dataset_id = google_bigquery_dataset.weather_dataset.dataset_id
  table_id   = "raw_rainfall"

  schema = jsonencode([
    {
      name        = "timestamp"
      type        = "TIMESTAMP"
      mode        = "REQUIRED"
      description = "Reading timestamp in SGT"
    },
    {
      name        = "station_id"
      type        = "STRING"
      mode        = "REQUIRED"
      description = "Weather station ID"
    },
    {
      name        = "rainfall"
      type        = "FLOAT"
      mode        = "REQUIRED"
      description = "Rainfall amount in mm"
    },
    {
      name        = "unit"
      type        = "STRING"
      mode        = "NULLABLE"
      description = "Unit of measurement"
    },
    {
      name        = "ingest_timestamp"
      type        = "TIMESTAMP"
      mode        = "NULLABLE"
      description = "Timestamp when data was ingested"
    }
  ])

  time_partitioning {
    type = "DAY"
    field = "timestamp"
  }

  clustering = ["station_id"]

  labels = {
    source = "data.gov.sg"
    type   = "raw"
  }
}

# Raw table for wind speed data
resource "google_bigquery_table" "raw_wind_speed" {
  dataset_id = google_bigquery_dataset.weather_dataset.dataset_id
  table_id   = "raw_wind_speed"

  schema = jsonencode([
    {
      name        = "timestamp"
      type        = "TIMESTAMP"
      mode        = "REQUIRED"
      description = "Reading timestamp in SGT"
    },
    {
      name        = "station_id"
      type        = "STRING"
      mode        = "REQUIRED"
      description = "Weather station ID"
    },
    {
      name        = "speed"
      type        = "FLOAT"
      mode        = "REQUIRED"
      description = "Wind speed in knots"
    },
    {
      name        = "unit"
      type        = "STRING"
      mode        = "NULLABLE"
      description = "Unit of measurement"
    },
    {
      name        = "ingest_timestamp"
      type        = "TIMESTAMP"
      mode        = "NULLABLE"
      description = "Timestamp when data was ingested"
    }
  ])

  time_partitioning {
    type = "DAY"
    field = "timestamp"
  }

  clustering = ["station_id"]

  labels = {
    source = "data.gov.sg"
    type   = "raw"
  }
}

# Unified analytics table for all weather data
resource "google_bigquery_table" "unified_weather" {
  dataset_id = google_bigquery_dataset.weather_dataset.dataset_id
  table_id   = "unified_weather"

  schema = jsonencode([
    {
      name        = "reading_timestamp"
      type        = "TIMESTAMP"
      mode        = "REQUIRED"
      description = "Reading timestamp in SGT"
    },
    {
      name        = "station_id"
      type        = "STRING"
      mode        = "REQUIRED"
      description = "Weather station ID"
    },
    {
      name        = "temperature"
      type        = "FLOAT"
      mode        = "NULLABLE"
      description = "Air temperature in Celsius"
    },
    {
      name        = "humidity"
      type        = "FLOAT"
      mode        = "NULLABLE"
      description = "Relative humidity percentage"
    },
    {
      name        = "rainfall"
      type        = "FLOAT"
      mode        = "NULLABLE"
      description = "Rainfall amount in mm"
    },
    {
      name        = "wind_speed"
      type        = "FLOAT"
      mode        = "NULLABLE"
      description = "Wind speed in knots"
    },
    {
      name        = "reading_type"
      type        = "STRING"
      mode        = "NULLABLE"
      description = "Type of reading (temperature, humidity, etc.)"
    },
    {
      name        = "ingest_timestamp"
      type        = "TIMESTAMP"
      mode        = "NULLABLE"
      description = "Timestamp when data was ingested"
    }
  ])

  time_partitioning {
    type = "DAY"
    field = "reading_timestamp"
  }

  clustering = ["station_id", "reading_type"]

  labels = {
    source = "data.gov.sg"
    type   = "analytics"
  }
}