variable "project_id" {
  description = "GCP Project ID"
  type        = string
}

variable "region" {
  description = "GCP Region"
  type        = string
  default     = "asia-southeast1"
}

variable "dataset_id" {
  description = "BigQuery Dataset ID"
  type        = string
  default     = "weather_data"
}