* make terraform-init, make terraform-plan
```bash
make terraform-init
make terraform-plan
make terraform-apply


@KaiquanMah ➜ /workspaces/sg-weather-2021-2026 (main) $ make terraform-init
cd terraform && terraform init
Initializing the backend...
Initializing provider plugins...
- Reusing previous version of hashicorp/random from the dependency lock file
- Reusing previous version of hashicorp/google from the dependency lock file
- Using previously-installed hashicorp/random v3.8.1
- Using previously-installed hashicorp/google v5.45.2

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.















@KaiquanMah ➜ /workspaces/sg-weather-2021-2026 (main) $ make terraform-plan
cd terraform && terraform plan \
        -var="project_id=proud-outrider-483901-c3" \
        -var="region=asia-southeast1"
random_string.bucket_suffix: Refreshing state... [id=kfru2uzo]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.weather_dataset will be created
  + resource "google_bigquery_dataset" "weather_dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "weather_data"
      + default_collation          = (known after apply)
      + delete_contents_on_destroy = false
      + description                = "Dataset for storing weather data from data.gov.sg APIs"
      + effective_labels           = {
          + "owner"   = "data-engineering-zoomcamp"
          + "purpose" = "weather-analytics"
        }
      + etag                       = (known after apply)
      + friendly_name              = "Weather Data Analytics"
      + id                         = (known after apply)
      + is_case_insensitive        = (known after apply)
      + labels                     = {
          + "owner"   = "data-engineering-zoomcamp"
          + "purpose" = "weather-analytics"
        }
      + last_modified_time         = (known after apply)
      + location                   = "asia-southeast1"
      + max_time_travel_hours      = (known after apply)
      + project                    = "proud-outrider-483901-c3"
      + self_link                  = (known after apply)
      + storage_billing_model      = (known after apply)
      + terraform_labels           = {
          + "owner"   = "data-engineering-zoomcamp"
          + "purpose" = "weather-analytics"
        }

      + access (known after apply)
    }

  # google_bigquery_table.raw_air_temperature will be created
  + resource "google_bigquery_table" "raw_air_temperature" {
      + allow_resource_tags_on_deletion = false
      + clustering                      = [
          + "station_id",
        ]
      + creation_time                   = (known after apply)
      + dataset_id                      = "weather_data"
      + deletion_protection             = true
      + effective_labels                = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + etag                            = (known after apply)
      + expiration_time                 = (known after apply)
      + id                              = (known after apply)
      + labels                          = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + last_modified_time              = (known after apply)
      + location                        = (known after apply)
      + num_bytes                       = (known after apply)
      + num_long_term_bytes             = (known after apply)
      + num_rows                        = (known after apply)
      + project                         = "proud-outrider-483901-c3"
      + schema                          = jsonencode(
            [
              + {
                  + description = "Reading timestamp in SGT"
                  + mode        = "REQUIRED"
                  + name        = "timestamp"
                  + type        = "TIMESTAMP"
                },
              + {
                  + description = "Weather station ID"
                  + mode        = "REQUIRED"
                  + name        = "station_id"
                  + type        = "STRING"
                },
              + {
                  + description = "Air temperature in Celsius"
                  + mode        = "REQUIRED"
                  + name        = "temperature"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Unit of measurement"
                  + mode        = "NULLABLE"
                  + name        = "unit"
                  + type        = "STRING"
                },
              + {
                  + description = "Timestamp when data was ingested"
                  + mode        = "NULLABLE"
                  + name        = "ingest_timestamp"
                  + type        = "TIMESTAMP"
                },
            ]
        )
      + self_link                       = (known after apply)
      + table_id                        = "raw_air_temperature"
      + terraform_labels                = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + type                            = (known after apply)

      + time_partitioning {
          + expiration_ms = (known after apply)
          + field         = "timestamp"
          + type          = "DAY"
        }
    }

  # google_bigquery_table.raw_rainfall will be created
  + resource "google_bigquery_table" "raw_rainfall" {
      + allow_resource_tags_on_deletion = false
      + clustering                      = [
          + "station_id",
        ]
      + creation_time                   = (known after apply)
      + dataset_id                      = "weather_data"
      + deletion_protection             = true
      + effective_labels                = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + etag                            = (known after apply)
      + expiration_time                 = (known after apply)
      + id                              = (known after apply)
      + labels                          = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + last_modified_time              = (known after apply)
      + location                        = (known after apply)
      + num_bytes                       = (known after apply)
      + num_long_term_bytes             = (known after apply)
      + num_rows                        = (known after apply)
      + project                         = "proud-outrider-483901-c3"
      + schema                          = jsonencode(
            [
              + {
                  + description = "Reading timestamp in SGT"
                  + mode        = "REQUIRED"
                  + name        = "timestamp"
                  + type        = "TIMESTAMP"
                },
              + {
                  + description = "Weather station ID"
                  + mode        = "REQUIRED"
                  + name        = "station_id"
                  + type        = "STRING"
                },
              + {
                  + description = "Rainfall amount in mm"
                  + mode        = "REQUIRED"
                  + name        = "rainfall"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Unit of measurement"
                  + mode        = "NULLABLE"
                  + name        = "unit"
                  + type        = "STRING"
                },
              + {
                  + description = "Timestamp when data was ingested"
                  + mode        = "NULLABLE"
                  + name        = "ingest_timestamp"
                  + type        = "TIMESTAMP"
                },
            ]
        )
      + self_link                       = (known after apply)
      + table_id                        = "raw_rainfall"
      + terraform_labels                = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + type                            = (known after apply)

      + time_partitioning {
          + expiration_ms = (known after apply)
          + field         = "timestamp"
          + type          = "DAY"
        }
    }

  # google_bigquery_table.raw_relative_humidity will be created
  + resource "google_bigquery_table" "raw_relative_humidity" {
      + allow_resource_tags_on_deletion = false
      + clustering                      = [
          + "station_id",
        ]
      + creation_time                   = (known after apply)
      + dataset_id                      = "weather_data"
      + deletion_protection             = true
      + effective_labels                = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + etag                            = (known after apply)
      + expiration_time                 = (known after apply)
      + id                              = (known after apply)
      + labels                          = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + last_modified_time              = (known after apply)
      + location                        = (known after apply)
      + num_bytes                       = (known after apply)
      + num_long_term_bytes             = (known after apply)
      + num_rows                        = (known after apply)
      + project                         = "proud-outrider-483901-c3"
      + schema                          = jsonencode(
            [
              + {
                  + description = "Reading timestamp in SGT"
                  + mode        = "REQUIRED"
                  + name        = "timestamp"
                  + type        = "TIMESTAMP"
                },
              + {
                  + description = "Weather station ID"
                  + mode        = "REQUIRED"
                  + name        = "station_id"
                  + type        = "STRING"
                },
              + {
                  + description = "Relative humidity percentage"
                  + mode        = "REQUIRED"
                  + name        = "humidity"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Unit of measurement"
                  + mode        = "NULLABLE"
                  + name        = "unit"
                  + type        = "STRING"
                },
              + {
                  + description = "Timestamp when data was ingested"
                  + mode        = "NULLABLE"
                  + name        = "ingest_timestamp"
                  + type        = "TIMESTAMP"
                },
            ]
        )
      + self_link                       = (known after apply)
      + table_id                        = "raw_relative_humidity"
      + terraform_labels                = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + type                            = (known after apply)

      + time_partitioning {
          + expiration_ms = (known after apply)
          + field         = "timestamp"
          + type          = "DAY"
        }
    }

  # google_bigquery_table.raw_wind_speed will be created
  + resource "google_bigquery_table" "raw_wind_speed" {
      + allow_resource_tags_on_deletion = false
      + clustering                      = [
          + "station_id",
        ]
      + creation_time                   = (known after apply)
      + dataset_id                      = "weather_data"
      + deletion_protection             = true
      + effective_labels                = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + etag                            = (known after apply)
      + expiration_time                 = (known after apply)
      + id                              = (known after apply)
      + labels                          = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + last_modified_time              = (known after apply)
      + location                        = (known after apply)
      + num_bytes                       = (known after apply)
      + num_long_term_bytes             = (known after apply)
      + num_rows                        = (known after apply)
      + project                         = "proud-outrider-483901-c3"
      + schema                          = jsonencode(
            [
              + {
                  + description = "Reading timestamp in SGT"
                  + mode        = "REQUIRED"
                  + name        = "timestamp"
                  + type        = "TIMESTAMP"
                },
              + {
                  + description = "Weather station ID"
                  + mode        = "REQUIRED"
                  + name        = "station_id"
                  + type        = "STRING"
                },
              + {
                  + description = "Wind speed in knots"
                  + mode        = "REQUIRED"
                  + name        = "speed"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Unit of measurement"
                  + mode        = "NULLABLE"
                  + name        = "unit"
                  + type        = "STRING"
                },
              + {
                  + description = "Timestamp when data was ingested"
                  + mode        = "NULLABLE"
                  + name        = "ingest_timestamp"
                  + type        = "TIMESTAMP"
                },
            ]
        )
      + self_link                       = (known after apply)
      + table_id                        = "raw_wind_speed"
      + terraform_labels                = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + type                            = (known after apply)

      + time_partitioning {
          + expiration_ms = (known after apply)
          + field         = "timestamp"
          + type          = "DAY"
        }
    }

  # google_bigquery_table.unified_weather will be created
  + resource "google_bigquery_table" "unified_weather" {
      + allow_resource_tags_on_deletion = false
      + clustering                      = [
          + "station_id",
          + "reading_type",
        ]
      + creation_time                   = (known after apply)
      + dataset_id                      = "weather_data"
      + deletion_protection             = true
      + effective_labels                = {
          + "source" = "data.gov.sg"
          + "type"   = "analytics"
        }
      + etag                            = (known after apply)
      + expiration_time                 = (known after apply)
      + id                              = (known after apply)
      + labels                          = {
          + "source" = "data.gov.sg"
          + "type"   = "analytics"
        }
      + last_modified_time              = (known after apply)
      + location                        = (known after apply)
      + num_bytes                       = (known after apply)
      + num_long_term_bytes             = (known after apply)
      + num_rows                        = (known after apply)
      + project                         = "proud-outrider-483901-c3"
      + schema                          = jsonencode(
            [
              + {
                  + description = "Reading timestamp in SGT"
                  + mode        = "REQUIRED"
                  + name        = "reading_timestamp"
                  + type        = "TIMESTAMP"
                },
              + {
                  + description = "Weather station ID"
                  + mode        = "REQUIRED"
                  + name        = "station_id"
                  + type        = "STRING"
                },
              + {
                  + description = "Air temperature in Celsius"
                  + mode        = "NULLABLE"
                  + name        = "temperature"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Relative humidity percentage"
                  + mode        = "NULLABLE"
                  + name        = "humidity"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Rainfall amount in mm"
                  + mode        = "NULLABLE"
                  + name        = "rainfall"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Wind speed in knots"
                  + mode        = "NULLABLE"
                  + name        = "wind_speed"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Type of reading (temperature, humidity, etc.)"
                  + mode        = "NULLABLE"
                  + name        = "reading_type"
                  + type        = "STRING"
                },
              + {
                  + description = "Timestamp when data was ingested"
                  + mode        = "NULLABLE"
                  + name        = "ingest_timestamp"
                  + type        = "TIMESTAMP"
                },
            ]
        )
      + self_link                       = (known after apply)
      + table_id                        = "unified_weather"
      + terraform_labels                = {
          + "source" = "data.gov.sg"
          + "type"   = "analytics"
        }
      + type                            = (known after apply)

      + time_partitioning {
          + expiration_ms = (known after apply)
          + field         = "reading_timestamp"
          + type          = "DAY"
        }
    }

  # google_storage_bucket.weather_raw_bucket will be created
  + resource "google_storage_bucket" "weather_raw_bucket" {
      + effective_labels            = {
          + "owner"   = "data-engineering-zoomcamp"
          + "purpose" = "weather-data-ingestion"
        }
      + force_destroy               = true
      + id                          = (known after apply)
      + labels                      = {
          + "owner"   = "data-engineering-zoomcamp"
          + "purpose" = "weather-data-ingestion"
        }
      + location                    = "ASIA-SOUTHEAST1"
      + name                        = "proud-outrider-483901-c3-weather-raw-kfru2uzo"
      + project                     = (known after apply)
      + project_number              = (known after apply)
      + public_access_prevention    = (known after apply)
      + rpo                         = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + terraform_labels            = {
          + "owner"   = "data-engineering-zoomcamp"
          + "purpose" = "weather-data-ingestion"
        }
      + uniform_bucket_level_access = true
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type          = "Delete"
                # (1 unchanged attribute hidden)
            }
          + condition {
              + age                    = 30
              + matches_prefix         = []
              + matches_storage_class  = []
              + matches_suffix         = []
              + send_age_if_zero       = true
              + with_state             = (known after apply)
                # (3 unchanged attributes hidden)
            }
        }

      + soft_delete_policy (known after apply)

      + versioning (known after apply)

      + website (known after apply)
    }

Plan: 7 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + gcs_bucket_name             = "proud-outrider-483901-c3-weather-raw-kfru2uzo"

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.
```














* make terraform-apply with issues
```bash
@KaiquanMah ➜ /workspaces/sg-weather-2021-2026 (main) $ make terraform-apply
cd terraform && terraform apply \
        -var="project_id=proud-outrider-483901-c3" \
        -var="region=asia-southeast1" \
        -auto-approve
random_string.bucket_suffix: Refreshing state... [id=kfru2uzo]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.weather_dataset will be created
  + resource "google_bigquery_dataset" "weather_dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "weather_data"
      + default_collation          = (known after apply)
      + delete_contents_on_destroy = false
      + description                = "Dataset for storing weather data from data.gov.sg APIs"
      + effective_labels           = {
          + "owner"   = "data-engineering-zoomcamp"
          + "purpose" = "weather-analytics"
        }
      + etag                       = (known after apply)
      + friendly_name              = "Weather Data Analytics"
      + id                         = (known after apply)
      + is_case_insensitive        = (known after apply)
      + labels                     = {
          + "owner"   = "data-engineering-zoomcamp"
          + "purpose" = "weather-analytics"
        }
      + last_modified_time         = (known after apply)
      + location                   = "asia-southeast1"
      + max_time_travel_hours      = (known after apply)
      + project                    = "proud-outrider-483901-c3"
      + self_link                  = (known after apply)
      + storage_billing_model      = (known after apply)
      + terraform_labels           = {
          + "owner"   = "data-engineering-zoomcamp"
          + "purpose" = "weather-analytics"
        }

      + access (known after apply)
    }

  # google_bigquery_table.raw_air_temperature will be created
  + resource "google_bigquery_table" "raw_air_temperature" {
      + allow_resource_tags_on_deletion = false
      + clustering                      = [
          + "station_id",
        ]
      + creation_time                   = (known after apply)
      + dataset_id                      = "weather_data"
      + deletion_protection             = true
      + effective_labels                = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + etag                            = (known after apply)
      + expiration_time                 = (known after apply)
      + id                              = (known after apply)
      + labels                          = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + last_modified_time              = (known after apply)
      + location                        = (known after apply)
      + num_bytes                       = (known after apply)
      + num_long_term_bytes             = (known after apply)
      + num_rows                        = (known after apply)
      + project                         = "proud-outrider-483901-c3"
      + schema                          = jsonencode(
            [
              + {
                  + description = "Reading timestamp in SGT"
                  + mode        = "REQUIRED"
                  + name        = "timestamp"
                  + type        = "TIMESTAMP"
                },
              + {
                  + description = "Weather station ID"
                  + mode        = "REQUIRED"
                  + name        = "station_id"
                  + type        = "STRING"
                },
              + {
                  + description = "Air temperature in Celsius"
                  + mode        = "REQUIRED"
                  + name        = "temperature"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Unit of measurement"
                  + mode        = "NULLABLE"
                  + name        = "unit"
                  + type        = "STRING"
                },
              + {
                  + description = "Timestamp when data was ingested"
                  + mode        = "NULLABLE"
                  + name        = "ingest_timestamp"
                  + type        = "TIMESTAMP"
                },
            ]
        )
      + self_link                       = (known after apply)
      + table_id                        = "raw_air_temperature"
      + terraform_labels                = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + type                            = (known after apply)

      + time_partitioning {
          + expiration_ms = (known after apply)
          + field         = "timestamp"
          + type          = "DAY"
        }
    }

  # google_bigquery_table.raw_rainfall will be created
  + resource "google_bigquery_table" "raw_rainfall" {
      + allow_resource_tags_on_deletion = false
      + clustering                      = [
          + "station_id",
        ]
      + creation_time                   = (known after apply)
      + dataset_id                      = "weather_data"
      + deletion_protection             = true
      + effective_labels                = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + etag                            = (known after apply)
      + expiration_time                 = (known after apply)
      + id                              = (known after apply)
      + labels                          = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + last_modified_time              = (known after apply)
      + location                        = (known after apply)
      + num_bytes                       = (known after apply)
      + num_long_term_bytes             = (known after apply)
      + num_rows                        = (known after apply)
      + project                         = "proud-outrider-483901-c3"
      + schema                          = jsonencode(
            [
              + {
                  + description = "Reading timestamp in SGT"
                  + mode        = "REQUIRED"
                  + name        = "timestamp"
                  + type        = "TIMESTAMP"
                },
              + {
                  + description = "Weather station ID"
                  + mode        = "REQUIRED"
                  + name        = "station_id"
                  + type        = "STRING"
                },
              + {
                  + description = "Rainfall amount in mm"
                  + mode        = "REQUIRED"
                  + name        = "rainfall"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Unit of measurement"
                  + mode        = "NULLABLE"
                  + name        = "unit"
                  + type        = "STRING"
                },
              + {
                  + description = "Timestamp when data was ingested"
                  + mode        = "NULLABLE"
                  + name        = "ingest_timestamp"
                  + type        = "TIMESTAMP"
                },
            ]
        )
      + self_link                       = (known after apply)
      + table_id                        = "raw_rainfall"
      + terraform_labels                = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + type                            = (known after apply)

      + time_partitioning {
          + expiration_ms = (known after apply)
          + field         = "timestamp"
          + type          = "DAY"
        }
    }

  # google_bigquery_table.raw_relative_humidity will be created
  + resource "google_bigquery_table" "raw_relative_humidity" {
      + allow_resource_tags_on_deletion = false
      + clustering                      = [
          + "station_id",
        ]
      + creation_time                   = (known after apply)
      + dataset_id                      = "weather_data"
      + deletion_protection             = true
      + effective_labels                = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + etag                            = (known after apply)
      + expiration_time                 = (known after apply)
      + id                              = (known after apply)
      + labels                          = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + last_modified_time              = (known after apply)
      + location                        = (known after apply)
      + num_bytes                       = (known after apply)
      + num_long_term_bytes             = (known after apply)
      + num_rows                        = (known after apply)
      + project                         = "proud-outrider-483901-c3"
      + schema                          = jsonencode(
            [
              + {
                  + description = "Reading timestamp in SGT"
                  + mode        = "REQUIRED"
                  + name        = "timestamp"
                  + type        = "TIMESTAMP"
                },
              + {
                  + description = "Weather station ID"
                  + mode        = "REQUIRED"
                  + name        = "station_id"
                  + type        = "STRING"
                },
              + {
                  + description = "Relative humidity percentage"
                  + mode        = "REQUIRED"
                  + name        = "humidity"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Unit of measurement"
                  + mode        = "NULLABLE"
                  + name        = "unit"
                  + type        = "STRING"
                },
              + {
                  + description = "Timestamp when data was ingested"
                  + mode        = "NULLABLE"
                  + name        = "ingest_timestamp"
                  + type        = "TIMESTAMP"
                },
            ]
        )
      + self_link                       = (known after apply)
      + table_id                        = "raw_relative_humidity"
      + terraform_labels                = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + type                            = (known after apply)

      + time_partitioning {
          + expiration_ms = (known after apply)
          + field         = "timestamp"
          + type          = "DAY"
        }
    }

  # google_bigquery_table.raw_wind_speed will be created
  + resource "google_bigquery_table" "raw_wind_speed" {
      + allow_resource_tags_on_deletion = false
      + clustering                      = [
          + "station_id",
        ]
      + creation_time                   = (known after apply)
      + dataset_id                      = "weather_data"
      + deletion_protection             = true
      + effective_labels                = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + etag                            = (known after apply)
      + expiration_time                 = (known after apply)
      + id                              = (known after apply)
      + labels                          = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + last_modified_time              = (known after apply)
      + location                        = (known after apply)
      + num_bytes                       = (known after apply)
      + num_long_term_bytes             = (known after apply)
      + num_rows                        = (known after apply)
      + project                         = "proud-outrider-483901-c3"
      + schema                          = jsonencode(
            [
              + {
                  + description = "Reading timestamp in SGT"
                  + mode        = "REQUIRED"
                  + name        = "timestamp"
                  + type        = "TIMESTAMP"
                },
              + {
                  + description = "Weather station ID"
                  + mode        = "REQUIRED"
                  + name        = "station_id"
                  + type        = "STRING"
                },
              + {
                  + description = "Wind speed in knots"
                  + mode        = "REQUIRED"
                  + name        = "speed"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Unit of measurement"
                  + mode        = "NULLABLE"
                  + name        = "unit"
                  + type        = "STRING"
                },
              + {
                  + description = "Timestamp when data was ingested"
                  + mode        = "NULLABLE"
                  + name        = "ingest_timestamp"
                  + type        = "TIMESTAMP"
                },
            ]
        )
      + self_link                       = (known after apply)
      + table_id                        = "raw_wind_speed"
      + terraform_labels                = {
          + "source" = "data.gov.sg"
          + "type"   = "raw"
        }
      + type                            = (known after apply)

      + time_partitioning {
          + expiration_ms = (known after apply)
          + field         = "timestamp"
          + type          = "DAY"
        }
    }

  # google_bigquery_table.unified_weather will be created
  + resource "google_bigquery_table" "unified_weather" {
      + allow_resource_tags_on_deletion = false
      + clustering                      = [
          + "station_id",
          + "reading_type",
        ]
      + creation_time                   = (known after apply)
      + dataset_id                      = "weather_data"
      + deletion_protection             = true
      + effective_labels                = {
          + "source" = "data.gov.sg"
          + "type"   = "analytics"
        }
      + etag                            = (known after apply)
      + expiration_time                 = (known after apply)
      + id                              = (known after apply)
      + labels                          = {
          + "source" = "data.gov.sg"
          + "type"   = "analytics"
        }
      + last_modified_time              = (known after apply)
      + location                        = (known after apply)
      + num_bytes                       = (known after apply)
      + num_long_term_bytes             = (known after apply)
      + num_rows                        = (known after apply)
      + project                         = "proud-outrider-483901-c3"
      + schema                          = jsonencode(
            [
              + {
                  + description = "Reading timestamp in SGT"
                  + mode        = "REQUIRED"
                  + name        = "reading_timestamp"
                  + type        = "TIMESTAMP"
                },
              + {
                  + description = "Weather station ID"
                  + mode        = "REQUIRED"
                  + name        = "station_id"
                  + type        = "STRING"
                },
              + {
                  + description = "Air temperature in Celsius"
                  + mode        = "NULLABLE"
                  + name        = "temperature"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Relative humidity percentage"
                  + mode        = "NULLABLE"
                  + name        = "humidity"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Rainfall amount in mm"
                  + mode        = "NULLABLE"
                  + name        = "rainfall"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Wind speed in knots"
                  + mode        = "NULLABLE"
                  + name        = "wind_speed"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Type of reading (temperature, humidity, etc.)"
                  + mode        = "NULLABLE"
                  + name        = "reading_type"
                  + type        = "STRING"
                },
              + {
                  + description = "Timestamp when data was ingested"
                  + mode        = "NULLABLE"
                  + name        = "ingest_timestamp"
                  + type        = "TIMESTAMP"
                },
            ]
        )
      + self_link                       = (known after apply)
      + table_id                        = "unified_weather"
      + terraform_labels                = {
          + "source" = "data.gov.sg"
          + "type"   = "analytics"
        }
      + type                            = (known after apply)

      + time_partitioning {
          + expiration_ms = (known after apply)
          + field         = "reading_timestamp"
          + type          = "DAY"
        }
    }

  # google_storage_bucket.weather_raw_bucket will be created
  + resource "google_storage_bucket" "weather_raw_bucket" {
      + effective_labels            = {
          + "owner"   = "data-engineering-zoomcamp"
          + "purpose" = "weather-data-ingestion"
        }
      + force_destroy               = true
      + id                          = (known after apply)
      + labels                      = {
          + "owner"   = "data-engineering-zoomcamp"
          + "purpose" = "weather-data-ingestion"
        }
      + location                    = "ASIA-SOUTHEAST1"
      + name                        = "proud-outrider-483901-c3-weather-raw-kfru2uzo"
      + project                     = (known after apply)
      + project_number              = (known after apply)
      + public_access_prevention    = (known after apply)
      + rpo                         = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + terraform_labels            = {
          + "owner"   = "data-engineering-zoomcamp"
          + "purpose" = "weather-data-ingestion"
        }
      + uniform_bucket_level_access = true
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type          = "Delete"
                # (1 unchanged attribute hidden)
            }
          + condition {
              + age                    = 30
              + matches_prefix         = []
              + matches_storage_class  = []
              + matches_suffix         = []
              + send_age_if_zero       = true
              + with_state             = (known after apply)
                # (3 unchanged attributes hidden)
            }
        }

      + soft_delete_policy (known after apply)

      + versioning (known after apply)

      + website (known after apply)
    }

Plan: 7 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + gcs_bucket_name             = "proud-outrider-483901-c3-weather-raw-kfru2uzo"
google_bigquery_dataset.weather_dataset: Creating...
google_storage_bucket.weather_raw_bucket: Creating...
google_bigquery_dataset.weather_dataset: Creation complete after 1s [id=projects/proud-outrider-483901-c3/datasets/weather_data]
google_bigquery_table.raw_relative_humidity: Creating...
google_bigquery_table.raw_air_temperature: Creating...
google_bigquery_table.raw_rainfall: Creating...
google_bigquery_table.unified_weather: Creating...
google_bigquery_table.raw_wind_speed: Creating...
google_storage_bucket.weather_raw_bucket: Creation complete after 1s [id=proud-outrider-483901-c3-weather-raw-kfru2uzo]
╷
│ Error: googleapi: Error 400: Label value "data.gov.sg" has invalid characters., invalid
│ 
│   with google_bigquery_table.raw_air_temperature,
│   on main.tf line 58, in resource "google_bigquery_table" "raw_air_temperature":
│   58: resource "google_bigquery_table" "raw_air_temperature" {
│ 
╵
╷
│ Error: googleapi: Error 400: Label value "data.gov.sg" has invalid characters., invalid
│ 
│   with google_bigquery_table.raw_relative_humidity,
│   on main.tf line 109, in resource "google_bigquery_table" "raw_relative_humidity":
│  109: resource "google_bigquery_table" "raw_relative_humidity" {
│ 
╵
╷
│ Error: googleapi: Error 400: Label value "data.gov.sg" has invalid characters., invalid
│ 
│   with google_bigquery_table.raw_rainfall,
│   on main.tf line 160, in resource "google_bigquery_table" "raw_rainfall":
│  160: resource "google_bigquery_table" "raw_rainfall" {
│ 
╵
╷
│ Error: googleapi: Error 400: Label value "data.gov.sg" has invalid characters., invalid
│ 
│   with google_bigquery_table.raw_wind_speed,
│   on main.tf line 211, in resource "google_bigquery_table" "raw_wind_speed":
│  211: resource "google_bigquery_table" "raw_wind_speed" {
│ 
╵
╷
│ Error: googleapi: Error 400: Label value "data.gov.sg" has invalid characters., invalid
│ 
│   with google_bigquery_table.unified_weather,
│   on main.tf line 262, in resource "google_bigquery_table" "unified_weather":
│  262: resource "google_bigquery_table" "unified_weather" {
│ 
╵
make: *** [Makefile:63: terraform-apply] Error 1
```


















* fixed `terraform/main.tf`: labels > source contains '-' instead of '.' because GCP labels cannot contain '.' dots
```
@KaiquanMah ➜ /workspaces/sg-weather-2021-2026 (main) $ make terraform-apply
cd terraform && terraform apply \
        -var="project_id=proud-outrider-483901-c3" \
        -var="region=asia-southeast1" \
        -auto-approve
random_string.bucket_suffix: Refreshing state... [id=kfru2uzo]
google_storage_bucket.weather_raw_bucket: Refreshing state... [id=proud-outrider-483901-c3-weather-raw-kfru2uzo]
google_bigquery_dataset.weather_dataset: Refreshing state... [id=projects/proud-outrider-483901-c3/datasets/weather_data]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_table.raw_air_temperature will be created
  + resource "google_bigquery_table" "raw_air_temperature" {
      + allow_resource_tags_on_deletion = false
      + clustering                      = [
          + "station_id",
        ]
      + creation_time                   = (known after apply)
      + dataset_id                      = "weather_data"
      + deletion_protection             = true
      + effective_labels                = {
          + "source" = "data-gov-sg"
          + "type"   = "raw"
        }
      + etag                            = (known after apply)
      + expiration_time                 = (known after apply)
      + id                              = (known after apply)
      + labels                          = {
          + "source" = "data-gov-sg"
          + "type"   = "raw"
        }
      + last_modified_time              = (known after apply)
      + location                        = (known after apply)
      + num_bytes                       = (known after apply)
      + num_long_term_bytes             = (known after apply)
      + num_rows                        = (known after apply)
      + project                         = "proud-outrider-483901-c3"
      + schema                          = jsonencode(
            [
              + {
                  + description = "Reading timestamp in SGT"
                  + mode        = "REQUIRED"
                  + name        = "timestamp"
                  + type        = "TIMESTAMP"
                },
              + {
                  + description = "Weather station ID"
                  + mode        = "REQUIRED"
                  + name        = "station_id"
                  + type        = "STRING"
                },
              + {
                  + description = "Air temperature in Celsius"
                  + mode        = "REQUIRED"
                  + name        = "temperature"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Unit of measurement"
                  + mode        = "NULLABLE"
                  + name        = "unit"
                  + type        = "STRING"
                },
              + {
                  + description = "Timestamp when data was ingested"
                  + mode        = "NULLABLE"
                  + name        = "ingest_timestamp"
                  + type        = "TIMESTAMP"
                },
            ]
        )
      + self_link                       = (known after apply)
      + table_id                        = "raw_air_temperature"
      + terraform_labels                = {
          + "source" = "data-gov-sg"
          + "type"   = "raw"
        }
      + type                            = (known after apply)

      + time_partitioning {
          + expiration_ms = (known after apply)
          + field         = "timestamp"
          + type          = "DAY"
        }
    }

  # google_bigquery_table.raw_rainfall will be created
  + resource "google_bigquery_table" "raw_rainfall" {
      + allow_resource_tags_on_deletion = false
      + clustering                      = [
          + "station_id",
        ]
      + creation_time                   = (known after apply)
      + dataset_id                      = "weather_data"
      + deletion_protection             = true
      + effective_labels                = {
          + "source" = "data-gov-sg"
          + "type"   = "raw"
        }
      + etag                            = (known after apply)
      + expiration_time                 = (known after apply)
      + id                              = (known after apply)
      + labels                          = {
          + "source" = "data-gov-sg"
          + "type"   = "raw"
        }
      + last_modified_time              = (known after apply)
      + location                        = (known after apply)
      + num_bytes                       = (known after apply)
      + num_long_term_bytes             = (known after apply)
      + num_rows                        = (known after apply)
      + project                         = "proud-outrider-483901-c3"
      + schema                          = jsonencode(
            [
              + {
                  + description = "Reading timestamp in SGT"
                  + mode        = "REQUIRED"
                  + name        = "timestamp"
                  + type        = "TIMESTAMP"
                },
              + {
                  + description = "Weather station ID"
                  + mode        = "REQUIRED"
                  + name        = "station_id"
                  + type        = "STRING"
                },
              + {
                  + description = "Rainfall amount in mm"
                  + mode        = "REQUIRED"
                  + name        = "rainfall"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Unit of measurement"
                  + mode        = "NULLABLE"
                  + name        = "unit"
                  + type        = "STRING"
                },
              + {
                  + description = "Timestamp when data was ingested"
                  + mode        = "NULLABLE"
                  + name        = "ingest_timestamp"
                  + type        = "TIMESTAMP"
                },
            ]
        )
      + self_link                       = (known after apply)
      + table_id                        = "raw_rainfall"
      + terraform_labels                = {
          + "source" = "data-gov-sg"
          + "type"   = "raw"
        }
      + type                            = (known after apply)

      + time_partitioning {
          + expiration_ms = (known after apply)
          + field         = "timestamp"
          + type          = "DAY"
        }
    }

  # google_bigquery_table.raw_relative_humidity will be created
  + resource "google_bigquery_table" "raw_relative_humidity" {
      + allow_resource_tags_on_deletion = false
      + clustering                      = [
          + "station_id",
        ]
      + creation_time                   = (known after apply)
      + dataset_id                      = "weather_data"
      + deletion_protection             = true
      + effective_labels                = {
          + "source" = "data-gov-sg"
          + "type"   = "raw"
        }
      + etag                            = (known after apply)
      + expiration_time                 = (known after apply)
      + id                              = (known after apply)
      + labels                          = {
          + "source" = "data-gov-sg"
          + "type"   = "raw"
        }
      + last_modified_time              = (known after apply)
      + location                        = (known after apply)
      + num_bytes                       = (known after apply)
      + num_long_term_bytes             = (known after apply)
      + num_rows                        = (known after apply)
      + project                         = "proud-outrider-483901-c3"
      + schema                          = jsonencode(
            [
              + {
                  + description = "Reading timestamp in SGT"
                  + mode        = "REQUIRED"
                  + name        = "timestamp"
                  + type        = "TIMESTAMP"
                },
              + {
                  + description = "Weather station ID"
                  + mode        = "REQUIRED"
                  + name        = "station_id"
                  + type        = "STRING"
                },
              + {
                  + description = "Relative humidity percentage"
                  + mode        = "REQUIRED"
                  + name        = "humidity"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Unit of measurement"
                  + mode        = "NULLABLE"
                  + name        = "unit"
                  + type        = "STRING"
                },
              + {
                  + description = "Timestamp when data was ingested"
                  + mode        = "NULLABLE"
                  + name        = "ingest_timestamp"
                  + type        = "TIMESTAMP"
                },
            ]
        )
      + self_link                       = (known after apply)
      + table_id                        = "raw_relative_humidity"
      + terraform_labels                = {
          + "source" = "data-gov-sg"
          + "type"   = "raw"
        }
      + type                            = (known after apply)

      + time_partitioning {
          + expiration_ms = (known after apply)
          + field         = "timestamp"
          + type          = "DAY"
        }
    }

  # google_bigquery_table.raw_wind_speed will be created
  + resource "google_bigquery_table" "raw_wind_speed" {
      + allow_resource_tags_on_deletion = false
      + clustering                      = [
          + "station_id",
        ]
      + creation_time                   = (known after apply)
      + dataset_id                      = "weather_data"
      + deletion_protection             = true
      + effective_labels                = {
          + "source" = "data-gov-sg"
          + "type"   = "raw"
        }
      + etag                            = (known after apply)
      + expiration_time                 = (known after apply)
      + id                              = (known after apply)
      + labels                          = {
          + "source" = "data-gov-sg"
          + "type"   = "raw"
        }
      + last_modified_time              = (known after apply)
      + location                        = (known after apply)
      + num_bytes                       = (known after apply)
      + num_long_term_bytes             = (known after apply)
      + num_rows                        = (known after apply)
      + project                         = "proud-outrider-483901-c3"
      + schema                          = jsonencode(
            [
              + {
                  + description = "Reading timestamp in SGT"
                  + mode        = "REQUIRED"
                  + name        = "timestamp"
                  + type        = "TIMESTAMP"
                },
              + {
                  + description = "Weather station ID"
                  + mode        = "REQUIRED"
                  + name        = "station_id"
                  + type        = "STRING"
                },
              + {
                  + description = "Wind speed in knots"
                  + mode        = "REQUIRED"
                  + name        = "speed"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Unit of measurement"
                  + mode        = "NULLABLE"
                  + name        = "unit"
                  + type        = "STRING"
                },
              + {
                  + description = "Timestamp when data was ingested"
                  + mode        = "NULLABLE"
                  + name        = "ingest_timestamp"
                  + type        = "TIMESTAMP"
                },
            ]
        )
      + self_link                       = (known after apply)
      + table_id                        = "raw_wind_speed"
      + terraform_labels                = {
          + "source" = "data-gov-sg"
          + "type"   = "raw"
        }
      + type                            = (known after apply)

      + time_partitioning {
          + expiration_ms = (known after apply)
          + field         = "timestamp"
          + type          = "DAY"
        }
    }

  # google_bigquery_table.unified_weather will be created
  + resource "google_bigquery_table" "unified_weather" {
      + allow_resource_tags_on_deletion = false
      + clustering                      = [
          + "station_id",
          + "reading_type",
        ]
      + creation_time                   = (known after apply)
      + dataset_id                      = "weather_data"
      + deletion_protection             = true
      + effective_labels                = {
          + "source" = "data-gov-sg"
          + "type"   = "analytics"
        }
      + etag                            = (known after apply)
      + expiration_time                 = (known after apply)
      + id                              = (known after apply)
      + labels                          = {
          + "source" = "data-gov-sg"
          + "type"   = "analytics"
        }
      + last_modified_time              = (known after apply)
      + location                        = (known after apply)
      + num_bytes                       = (known after apply)
      + num_long_term_bytes             = (known after apply)
      + num_rows                        = (known after apply)
      + project                         = "proud-outrider-483901-c3"
      + schema                          = jsonencode(
            [
              + {
                  + description = "Reading timestamp in SGT"
                  + mode        = "REQUIRED"
                  + name        = "reading_timestamp"
                  + type        = "TIMESTAMP"
                },
              + {
                  + description = "Weather station ID"
                  + mode        = "REQUIRED"
                  + name        = "station_id"
                  + type        = "STRING"
                },
              + {
                  + description = "Air temperature in Celsius"
                  + mode        = "NULLABLE"
                  + name        = "temperature"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Relative humidity percentage"
                  + mode        = "NULLABLE"
                  + name        = "humidity"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Rainfall amount in mm"
                  + mode        = "NULLABLE"
                  + name        = "rainfall"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Wind speed in knots"
                  + mode        = "NULLABLE"
                  + name        = "wind_speed"
                  + type        = "FLOAT"
                },
              + {
                  + description = "Type of reading (temperature, humidity, etc.)"
                  + mode        = "NULLABLE"
                  + name        = "reading_type"
                  + type        = "STRING"
                },
              + {
                  + description = "Timestamp when data was ingested"
                  + mode        = "NULLABLE"
                  + name        = "ingest_timestamp"
                  + type        = "TIMESTAMP"
                },
            ]
        )
      + self_link                       = (known after apply)
      + table_id                        = "unified_weather"
      + terraform_labels                = {
          + "source" = "data-gov-sg"
          + "type"   = "analytics"
        }
      + type                            = (known after apply)

      + time_partitioning {
          + expiration_ms = (known after apply)
          + field         = "reading_timestamp"
          + type          = "DAY"
        }
    }

Plan: 5 to add, 0 to change, 0 to destroy.
google_bigquery_table.raw_air_temperature: Creating...
google_bigquery_table.raw_wind_speed: Creating...
google_bigquery_table.raw_rainfall: Creating...
google_bigquery_table.unified_weather: Creating...
google_bigquery_table.raw_relative_humidity: Creating...
google_bigquery_table.raw_air_temperature: Creation complete after 1s [id=projects/proud-outrider-483901-c3/datasets/weather_data/tables/raw_air_temperature]
google_bigquery_table.unified_weather: Creation complete after 1s [id=projects/proud-outrider-483901-c3/datasets/weather_data/tables/unified_weather]
google_bigquery_table.raw_wind_speed: Creation complete after 1s [id=projects/proud-outrider-483901-c3/datasets/weather_data/tables/raw_wind_speed]
google_bigquery_table.raw_rainfall: Creation complete after 1s [id=projects/proud-outrider-483901-c3/datasets/weather_data/tables/raw_rainfall]
google_bigquery_table.raw_relative_humidity: Creation complete after 1s [id=projects/proud-outrider-483901-c3/datasets/weather_data/tables/raw_relative_humidity]

Apply complete! Resources: 5 added, 0 changed, 0 destroyed.

Outputs:

bigquery_dataset_id = "weather_data"
gcs_bucket_name = "proud-outrider-483901-c3-weather-raw-kfru2uzo"
raw_air_temperature_table = "raw_air_temperature"
raw_rainfall_table = "raw_rainfall"
raw_relative_humidity_table = "raw_relative_humidity"
raw_wind_speed_table = "raw_wind_speed"
unified_weather_table = "unified_weather"
```